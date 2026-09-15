# 286 · File uploads y manejo de media (presigned, resumable/tus, validación, scan)

> Subir un archivo parece trivial hasta que pesa 4GB, el cliente se cae al 90%, o el "JPG" es un `.exe`.
> Esto cubre el camino entrante; el saliente (servir media generada por CDN) vive en [[162-storage-cdn-media-generada]].

## Tres estrategias, por tamaño
| Patrón | Tamaño | Cómo |
|---|---|---|
| **Multipart directo** (`multipart/form-data`) | < ~10MB | el cliente sube a tu API (multer); simple, pero el archivo cruza tu server |
| **Presigned URL** | MB–GB | tu API firma una URL **PUT/POST** a S3/R2; el cliente sube **directo** al storage, tu server nunca toca los bytes |
| **Resumable (tus)** | GB, redes malas, móvil | upload en chunks reanudable tras corte de red; el cliente retoma donde quedó |

**Presigned es el default moderno**: descarga tu API de ancho de banda y memoria. Flujo: `POST /uploads` →
devuelves `{ url, fields, file_id }` → el cliente sube al bucket → confirma con `POST /uploads/{id}/complete`
o el bucket dispara un evento (S3 Event / R2 notification) que encola el post-proceso (cf. [[285-background-jobs-queues-web.md]] vía [[23-event-driven-colas]]).

## Resumable: tus
**tus** es el protocolo abierto de upload reanudable (HTTP + headers `Upload-Offset`/`Upload-Length`). El cliente
sube por chunks; tras un corte, hace `HEAD` para preguntar el offset y continúa. Verificado jun-2026: el sucesor
IETF **"Resumable Uploads for HTTP"** sigue en **draft** (`draft-ietf-httpbis-resumable-upload-11`, no es RFC aún);
tus 1.0.x es lo estable hoy y tus 2.0 se alineará con ese estándar. Úsalo para subir el video fuente del avatar,
datasets, o cualquier archivo donde reintentar desde 0 sea inaceptable.

## Validación: nunca confíes en el cliente
1. **Content-Type del header miente** — verifica los **magic bytes** reales (libmagic/`file-type`), no la extensión
   ni el MIME declarado. Un `foto.jpg` puede ser un PHP/ELF.
2. **Tamaño**: tope en el presigned (S3 `content-length-range` en la policy) **y** rechaza en confirmación.
3. **Extensión/MIME allowlist**, no blocklist. Renombra al guardar (UUID), no reuses el nombre del cliente
   (path traversal: `../../etc/passwd`).
4. **Dimensiones/duración** para imagen/video → evita "bombas" (un PNG de 100KB que decodifica a 30000×30000 = OOM).
5. **Decompression bomb**: zips/imágenes que explotan en RAM → límites de píxeles (Pillow `MAX_IMAGE_PIXELS`) y de ratio.

## Virus / contenido malicioso
- **ClamAV** (self-host) o un servicio (VirusTotal, S3 con scan) en el evento post-upload, **antes** de marcar el
  archivo "ready" o servirlo. El objeto vive en estado `pending` hasta pasar el scan.
- **Cuarentena por bucket**: sube a `quarantine/`; al aprobar, copia/mueve a `public/`. Nunca sirves desde cuarentena.
- Para SVG/HTML subidos por usuarios: **sanitiza** (DOMPurify) o sírvelos con `Content-Disposition: attachment` +
  `Content-Security-Policy` — un SVG ejecuta JS (XSS almacenado).

## Procesar la media (después del upload)
El procesamiento (thumbnails, transcode, transcripción, render) es **trabajo async**, nunca en el request:
encola un job (cf. [[285-background-jobs-queues-web.md]]) que lee el blob de R2, procesa con ffmpeg/Pillow, y escribe
las derivadas de vuelta al storage. Patrón en este stack: WhatsApp recibe imagen → guardas a R2/`data/media/` →
encolas análisis con Claude Vision → guardas resultado. El payload de la cola lleva solo la **referencia**, no los bytes.

## Servir lo subido (de vuelta al usuario)
- Bucket **privado** + **presigned GET** de corta vida para descargas autenticadas; público + CDN para assets abiertos.
- `Cache-Control` agresivo con URL versionada/hasheada (cf. [[22-caching-cdn]] y [[162-storage-cdn-media-generada]]).
- Nunca proxees descargas grandes por tu API (mata memoria) → redirige al presigned/CDN.

## Gotchas
1. Presigned URL con expiración larga = link compartible para siempre → minutos, no días; y acota tamaño en la policy.
2. CORS del bucket mal configurado → el PUT directo del browser falla con error opaco; configura `AllowedOrigins`/`PUT`.
3. Confiar en `onUploadComplete` del cliente: puede mentir o no llegar → usa el **evento del bucket** como verdad.
4. Validar MIME por extensión → bypass trivial; magic bytes siempre.
5. Multipart directo a tu API en serverless → límite de body (Vercel ~4.5MB) y RAM; presigned lo evita de raíz.
6. Borrar el objeto en cuarentena tras scan fallido, o acumulas basura (y costo) infinita.

Cruza con [[162-storage-cdn-media-generada]] y [[22-caching-cdn]].
