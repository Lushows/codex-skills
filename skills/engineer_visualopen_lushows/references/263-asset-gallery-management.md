# 263 · Gestión de assets generados (galería, metadata, versiones)

> Generar es la parte fácil; en 3 meses tienes 50k videos sin saber cuál, quién, con qué prompt ni cuánto costó.
> La biblioteca de assets es lo que convierte "un generador" en producto (caso STUDIO).

## El asset no es solo el archivo
Cada salida es un **registro** que apunta a un blob en object storage, con metadata que NO puedes reconstruir
después si no la guardas en el momento:

| Campo | Por qué importa |
|---|---|
| `id`, `tenant_id`, `user_id` | propiedad y aislamiento multi-tenant |
| `storage_key`, `mime`, `bytes`, `duration`, `w×h` | servir, paginar, facturar storage |
| `prompt`, `enhanced_prompt`, `negative` | reproducir, buscar, auditar |
| `model`, `seed`, `steps`, `cfg`, `sampler` | **re-roll determinista** y debug |
| `parent_id` | linaje (variación/upscale/edit de otro asset) |
| `cost_creditos`, `gpu_seconds`, `job_id` | reconciliar con [[262-credits-quota-billing-gen]] |
| `status`, `created_at` | filtrar, ordenar, limpiar fallidos |

Regla: **la metadata de generación se escribe en el mismo momento que se sube el blob**, en la misma
transacción lógica. Reconstruir el prompt o el seed después es imposible.

## Storage del blob vs metadata
El binario va a object storage (R2/S3); la metadata a Postgres. El registro guarda el `storage_key`, NO el
archivo. Sirve por **URL firmada** con expiración (no expongas el bucket). Genera **derivados** al subir:
thumbnail (poster del primer frame para video), preview comprimido, full. La galería pagina con thumbnails;
el full solo cuando se abre. Cruza con [[162-storage-cdn-media-generada]] para el delivery/CDN.

## Versiones y linaje (el grafo, no la lista)
El usuario rara vez genera una vez: hace variaciones, upscales, ediciones. Modela un **DAG** con `parent_id`:
- **Variación**: mismo prompt, distinto seed → hermanos con padre común.
- **Upscale / edit / inpaint**: hijo que referencia al padre + la operación aplicada.
- **Re-roll**: con `seed`+params guardados, reproduces o ramificas exactamente.

Esto te da "historial" navegable y permite **deduplicar costo**: un upscale no re-genera desde cero. NO uses
una columna `version` lineal; el trabajo creativo se ramifica, no avanza en línea.

## Búsqueda: tres capas
1. **Filtros estructurados** (SQL/índices): por modelo, fecha, tenant, status, tags, rango de costo. Cubre el 80%.
2. **Full-text sobre el prompt** (Postgres `tsvector` / `pg_trgm`): "los videos donde dije 'neón'".
3. **Búsqueda semántica por embedding** del prompt o del propio frame (CLIP) → "muéstrame los parecidos a
   este", "vibe cyberpunk" sin coincidencia léxica. Cruza con [[72-busqueda-semantica-embeddings]].

Empieza por la 1; añade 3 cuando la biblioteca crezca y el filtro exacto ya no baste.

## Organización para el usuario
- **Colecciones/proyectos**: agrupar assets de una campaña/marca (multi-marca en STUDIO).
- **Tags** (manuales + auto por modelo de visión): clasificación barata para filtrar.
- **Favoritos / soft-delete**: papelera con retención; no borres el blob al instante (permite deshacer).
- **Estados**: `processing | ready | failed | archived` → la galería no muestra basura a medio generar.

## Ciclo de vida y costo de almacenar
El storage crece para siempre si no lo gestionas:
- **Lifecycle por tier**: hot (CDN) → cold/infrequent tras N días sin acceso → expira borradores no guardados.
- **Borrar derivados regenerables** antes que originales si hay que recortar.
- **Cuota de storage por plan** (free: 20 assets, borra los viejos). Imputa el GB-mes vía
  [[254-cost-allocation-chargeback-multitenant]].
- **Limpieza de huérfanos**: jobs fallidos que subieron blob sin registro → barrido periódico que cruza
  bucket vs DB.

## Errores que muerden
- No guardar `seed`+params → "regenera esto igual" se vuelve imposible; el usuario se va.
- Servir desde URL pública del bucket → cualquiera enumera assets de otros tenants.
- Mezclar metadata en el blob (EXIF) como única fuente → un re-encode la borra; la DB es la verdad.
- No paginar con thumbnails → la galería baja 200 videos full y revienta el navegador y tu egress.

Cruza con [[162-storage-cdn-media-generada]] y [[72-busqueda-semantica-embeddings]].
