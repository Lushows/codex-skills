# 162 · Storage + CDN del media generado (el worker sube a R2, la app descarga)

> El video/imagen que produce la GPU NO debe volver por el handler ni por tu API: el worker lo sube
> directo a R2/S3 y devuelve una URL. La app y el cliente descargan desde el object store/CDN.

## Por qué el worker sube y la app descarga (caso LongCat)
Un MP4 de avatar pesa MB-decenas de MB. Si el handler lo devuelve en el body de `/status`:
- infla la respuesta, revienta timeouts del poller, satura el ancho de banda del worker GPU (caro),
- obliga a la app a hacer de proxy de bytes (memoria, latencia).
Patrón correcto: **worker → `PutObject`/multipart a R2** bajo una key determinista; el job devuelve
`{ key }` o una **signed URL**. La app/cliente bajan de R2 (o del CDN delante). El worker GPU se libera
en cuanto sube. Cruza con [[111-longcat-avatar-runpod-produccion]] y [[115-async-render-largo-poller-durable]].

## R2 vs S3 (2026)
| | Cloudflare R2 | AWS S3 |
|---|---|---|
| Egress | **$0** (gratis) | ~$0.09/GB salida |
| API | S3-compatible (mismo SDK) | nativa |
| CDN | Cloudflare integrado (custom domain) | CloudFront aparte |
| Caso media servido a muchos | **gana** (egress mata en S3) | si ya estás 100% AWS |

Para media que se descarga repetido (un video que ven N usuarios), **R2 gana por el egress $0**.
Mismo `@aws-sdk/client-s3` apuntando al endpoint `https://<account>.r2.cloudflarestorage.com`.

## Subida desde el worker
- **PutObject** simple para < ~100 MB. Para archivos grandes o red inestable → **multipart**:
  `CreateMultipartUpload` → `UploadPart` (5 MB–5 GB/parte, mín 5 MB salvo la última) → `CompleteMultipartUpload`.
  Si falla a mitad: reintenta solo las partes pendientes (resiliencia real en redes de DC GPU).
- **Multipart incompleto = basura que paga storage.** R2 aborta incompletos a los **7 días** por
  defecto; configura una **lifecycle rule** “abort incomplete multipart uploads” a 1–2 días.
```js
// worker: subir resultado (S3 SDK contra R2)
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';
const s3 = new S3Client({ region: 'auto',
  endpoint: `https://${ACCOUNT}.r2.cloudflarestorage.com`,
  credentials: { accessKeyId: R2_KEY, secretAccessKey: R2_SECRET } });
await s3.send(new PutObjectCommand({
  Bucket: 'studio-lipsync', Key: `t/${tenant}/${jobId}.mp4`,
  Body: stream, ContentType: 'video/mp4',
  CacheControl: 'public, max-age=31536000, immutable', // key inmutable → cache eterno
}));
```

## Signed URLs (entregar sin exponer credenciales ni el bucket)
- **GET presignado** para que el cliente descargue/reproduzca sin que el bucket sea público:
  `getSignedUrl(s3, new GetObjectCommand({Bucket,Key}), { expiresIn: 3600 })`. Expira → no se filtra para siempre.
- **PUT presignado por parte** si quieres que el cliente suba el input directo a R2 (R2 soporta
  presigned **PUT** por parte de multipart; **POST** form-upload NO está soportado en R2).
- Para servir a muchos: mejor **custom domain + Cloudflare CDN** delante del bucket (cacheable,
  no firmas cada vez) y reserva las signed URLs para contenido privado/efímero.

## Organización de claves por tenant
```
t/{tenantId}/{yyyy}/{mm}/{jobId}.mp4        # media final
t/{tenantId}/inputs/{hash}.png              # inputs (dedup por hash)
t/{tenantId}/thumbs/{jobId}.jpg             # derivados
```
- Prefijo `t/{tenantId}/` → permisos por prefijo, métricas de costo por tenant, borrado por tenant.
- **Key determinista = idempotencia de storage**: si el job se re-ejecuta, sobreescribe la misma key
  (no duplica). Liga con la idempotency key de [[161-colas-jobs-gpu-a-fondo]].
- Inputs por `hash` → dedup natural (mismo input, mismo objeto).

## Lifecycle / expiración (no acumular media muerto)
- Renders de preview/free: lifecycle **delete a 7–30 días** por prefijo (`t/*/previews/`).
- Borra incompletos multipart a 1–2 días (arriba).
- Logs/derivados: clase de almacenamiento barata o expiración corta.
- En S3 hay tiers (IA/Glacier); en R2 hay **Infrequent Access** para datos fríos. Para media servido
  caliente, almacenamiento estándar + CDN.

## CDN delante
- R2: conecta un **custom domain** → Cloudflare cachea en edge. `Cache-Control: immutable` en keys
  inmutables → un hit, luego edge. Cruza con [[22-caching-cdn]].
- Invalidación: con keys inmutables (jobId en la ruta) **no invalidas**, publicas una key nueva.
- Rango/seek de video: el CDN sirve `Range` requests → reproducción con scrubbing sin bajar todo.

## Costo de egress (el número que decide)
- S3: servir un MP4 de 30 MB a 10.000 vistas = 300 GB × ~$0.09 ≈ **$27** solo en salida.
- R2: **$0** de egress; pagas storage (~$0.015/GB-mes) + operaciones. Para media viral, R2 es 1-2 órdenes más barato.
- El worker GPU subiendo a R2 dentro del mismo flujo: la subida es egress del worker (su red), no de R2.

Cruza con [[22-caching-cdn]], [[111-longcat-avatar-runpod-produccion]] y
[[115-async-render-largo-poller-durable]].
