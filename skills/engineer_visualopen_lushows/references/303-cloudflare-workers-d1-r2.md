# 303 · Cloudflare stack: Workers, Durable Objects, D1, R2, KV, Queues

> Un solo proveedor que cubre compute al edge, estado fuerte, SQL, blobs, cache y colas —
> todo en isolates baratos sin egress en R2. La clave es saber qué primitiva usar para cada cosa.

## Workers (compute)
Isolate V8 al edge, arranque ~0-10ms (sin OS). El reloj importante es **CPU time**, no wall-clock:
esperar `fetch`/KV/DB **no cuenta**. Límites [verificado]:
- CPU: **50ms** request en free, **30s** en paid (configurable).
- Subrequests: 10.000 por invocación en paid, subible hasta 10M vía `limits.subrequests`.
- Duración HTTP: **sin límite duro** mientras el cliente siga conectado → sirve para stream/proxy largo.
- `waitUntil()`: extiende hasta 30s tras responder (tareas post-respuesta, logging, purge).

## Durable Objects (estado fuerte)
Objeto single-instance globalmente direccionable con **almacenamiento transaccional** y SQLite embebido.
Da lo que Workers no: **consistencia y coordinación**. Casos: contador exacto, sala de chat/colaboración,
rate-limit por usuario, **scheduler durable con `alarm()`** (sobrevive reinicios → ver [[306-cron-scheduling]]),
máquina de estados de un job GPU (warm-state, progreso). Un DO = una sección crítica serializada → evita carreras.

## D1 (SQL)
SQLite serverless al edge. Límites [verificado]:
- **10GB por base, tope duro** (no se sube). Si creces, **shardea** por tenant/región en varias DB.
- **Single-threaded**: procesa queries de a una → no es para OLAP ni escritura masiva concurrente.
- Bueno para: config, catálogos, metadata de jobs, datos relacionales de baja escala.

## R2 (blobs)
S3-compatible **sin egress fees** → ideal para media generada (avatares, video, imágenes). Es el destino natural
del worker GPU: subes el resultado a R2, sirves URL firmada por CDN. Ver [[162-storage-cdn-media-generada]].

## KV (cache eventual)
Key-value, lectura ultrarrápida al edge, **consistencia eventual** (~60s de propagación). Para config, flags,
sesiones, cache de respuestas. **No** para contadores ni datos que exigen leer-tu-propia-escritura → eso es DO o D1.

## Queues (async)
Cola gestionada productor→consumer con batching, reintentos y **DLQ**. Desacopla el webhook del trabajo pesado:
Worker recibe → `queue.send()` → consumer procesa (o dispara el job GPU). Detalle de patrones en [[305-message-queues-cloud]].

## Matriz de decisión
| Necesito | Primitiva |
|---|---|
| Lógica al edge, baja latencia | Workers |
| Estado fuerte / coordinación / scheduler durable | Durable Objects |
| SQL relacional <10GB | D1 |
| Blobs / media (sin egress) | R2 |
| Cache rápido, consistencia eventual | KV |
| Trabajo async / fanout / DLQ | Queues |

## Trampas
- KV no es base de datos transaccional: leer tras escribir puede dar el valor viejo (~60s).
- D1 10GB es **tope duro**: planea sharding desde el día 1 si esperas crecer.
- DO es serializado: meter trabajo CPU pesado dentro lo vuelve cuello de botella → delega a cola/worker.
- "Sin límite de duración" en Workers depende del **cliente conectado**; si cuelga, el Worker muere → para
  render largo usa cola + poll, no un Worker abierto eternamente.

Cruza con [[162-storage-cdn-media-generada]] y [[302-serverless-functions-edge-lambda]].
