# 161 · Colas de jobs GPU a fondo (un render de 40 min no es un job de 1s)

> Un job GPU largo invierte cada supuesto de las colas web: el lock dura minutos, no segundos;
> el reintento cuesta dinero real; la idempotencia es obligatoria porque re-ejecutar quema VRAM-hora.

## Por qué un job de 40 min necesita otro diseño
| Eje | Job web (1s) | Job GPU (40 min) |
|---|---|---|
| Visibility / lock | ~30s, irrelevante | debe cubrir 40 min + margen → renovación activa |
| Reintento | gratis, reintenta agresivo | **caro** (re-quema GPU-hora) → backoff largo, `attempts` bajo |
| Idempotencia | nice-to-have | obligatoria: doble entrega = doble factura |
| Concurrencia worker | cientos | 1 por GPU (VRAM no se comparte) |
| Heartbeat | innecesario | imprescindible para detectar worker muerto vs lento |
| Backpressure | cola crece y ya | cola crece → arranca GPU (cold start caro) o rechaza |

La regla: el worker GPU procesa **1 job a la vez por GPU** (`concurrency: 1`), y la cola es la que
absorbe ráfagas. No subas `concurrency` para “ir más rápido” → OOM de VRAM. Escala con más workers.

## Stacks y cuándo
- **BullMQ (Redis, Node)** — encaja con el gateway Node de este skill. Prioridad, rate-limit global,
  stalled-checker, backoff. Default para Lushows.
- **Celery (Redis/RabbitMQ, Python)** — si el orquestador es Python junto al handler. ACK tardío.
- **SQS (managed)** — sin infra propia; visibility timeout explícito, DLQ nativa, FIFO+dedup. Bueno si ya estás en AWS.
- **RunPod queue interna** — el endpoint serverless YA es una cola (`/run` → `IN_QUEUE`). Suele bastar;
  añade una cola propia por delante solo si necesitas prioridad/fairness/multi-tenant que RunPod no da.

## BullMQ: config que importa para GPU (v5, 2026)
```js
const worker = new Worker('gpu-render', processor, {
  connection,
  concurrency: 1,                 // 1 job/GPU — VRAM no se comparte
  lockDuration: 60_000,           // 60s; se renueva en lockDuration/2 (30s)
  stalledInterval: 30_000,        // chequeo de stalled
  maxStalledCount: 1,             // tras 1 stall → failed (no re-quemar a ciegas)
});
await queue.add('render', payload, {
  jobId: idempotencyKey,          // dedup: misma key = mismo job (no se re-encola)
  priority: 1,                    // 1 = más alta; O(log n) al insertar
  attempts: 2,                    // pocos: cada intento cuesta GPU-hora
  backoff: { type: 'exponential', delay: 60_000 }, // 1min, 2min…
  removeOnComplete: { age: 86400 }, removeOnFail: false, // conserva fallos para DLQ
});
```
- **El lock NO cubre 40 min por sí solo.** BullMQ renueva el lock mientras el processor vive
  (`lockRenewTime = lockDuration/2`). Si el worker muere, el lock expira → `stalled` → re-wait.
  El job largo NO necesita `lockDuration: 40min`; necesita un processor vivo que renueve. Si el
  handler bloquea el event-loop (sync pesado), el lock no se renueva y el job se marca stalled
  falsamente → mantén el handler `async`/no-bloqueante (el trabajo GPU corre en el worker remoto).
- **Prioridad no es estricta**: BullMQ pondera, no garantiza orden lineal. Para SLA duro usa **colas
  separadas** (`gpu-render-paid`, `gpu-render-free`) y un worker que drene paga primero.

## Fairness multi-tenant (que un cliente no monopolice las GPUs)
- **Rate-limit por tenant**: BullMQ `Queue.rateLimit` es global; para per-tenant usa **grupos**
  (BullMQ Pro `group`) o **una cola por tenant** + scheduler round-robin que elige la siguiente cola no vacía.
- **Weighted fair queueing casero**: cuenta jobs in-flight por tenant en Redis; al elegir el próximo,
  salta tenants que ya tienen ≥N corriendo. Evita que 1 tenant con 500 jobs ahogue al resto.
- **Cuotas**: contador `tenant:{id}:gpu_minutes` con TTL diario; rechaza encolar si excede.

## Visibility timeout / heartbeat (SQS y equivalente)
- SQS: `VisibilityTimeout` debe ser **> duración máxima del job** o el mensaje reaparece y otro worker
  lo re-ejecuta (doble factura). Para 40 min: pon 60 min, o mejor **extiende dinámicamente**
  (`ChangeMessageVisibility` cada pocos min mientras procesas — heartbeat). Máximo SQS = 12 h.
- Heartbeat propio (cualquier stack): el worker escribe `job:{id}:hb = now()` cada 30s; un reaper
  mueve a DLQ los jobs sin heartbeat reciente cuyo worker murió.

## Idempotencia y dedup (no re-quemar GPU)
- **Idempotency key** = hash del input (prompt+seed+modelo+params). `jobId = key` → encolar dos veces
  no crea dos jobs. Cruza con [[141-webhooks-hmac-idempotencia-dlq-jobs-gpu]].
- **Resultado cacheado**: antes de encolar, mira si `result:{key}` ya existe en R2 → devuélvelo sin GPU.
- **Exactly-once es imposible**; busca *effectively-once*: at-least-once delivery + processor idempotente
  (escribe el output bajo la key; si ya existe, no recomputa).

## Reintentos y backoff con cabeza
- **Distingue fallos**: OOM/cuda → `attempts` no ayuda (mismo input, mismo OOM) → falla rápido a DLQ.
  Timeout de red al subir a R2 → reintenta. Cold-start/worker evicted → reintenta con backoff.
- Backoff **largo** (minutos), no segundos: un retry inmediato re-paga el cold start.
- `maxStalledCount: 1`: si el worker muere a mitad, **un** reintento; más es sangría.

## Dead-letter queue (DLQ)
- Jobs que agotan `attempts` → cola `gpu-render:failed` (no borrar: `removeOnFail: false`).
- Guarda payload + último error + nº intentos. Reproceso manual desde dashboard tras arreglar la causa.
- Alerta si DLQ crece (señal de bug sistémico, no fallo aislado).

## Backpressure
- Cola > N pendientes → o **arrancas más workers** (acepta cold start) o **rechazas/encolas con ETA**
  visible al usuario. Nunca aceptes infinito: la GPU es el cuello, la cola solo difiere el dolor.

Cruza con [[23-event-driven-colas]], [[04-systems-layer-gateway-queue]] y
[[141-webhooks-hmac-idempotencia-dlq-jobs-gpu]].
