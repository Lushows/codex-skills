# 305 · Colas cloud: SQS, Pub/Sub, Cloud Tasks, Upstash QStash

> La cola desacopla "recibí el request" de "hice el trabajo". Sin ella, un render de 5 min
> tumba tu webhook por timeout. Con ella: respondes rápido, procesas atrás, reintentas y aíslas fallos.

## Las cuatro que importan
| Servicio | Modelo | Entrega | DLQ | Nota clave |
|---|---|---|---|---|
| **AWS SQS** | cola pull | Standard: at-least-once, orden best-effort · FIFO: orden + dedup ("exactly-once") | sí, nativo | visibility timeout, delay, retención hasta 14d |
| **GCP Pub/Sub** | pub/sub push o pull, fanout | at-least-once (exactly-once opcional) | sí | para **fanout** a muchos consumers |
| **GCP Cloud Tasks** | cola de tareas HTTP | at-least-once | **NO nativo** → reintenta indefinido por defecto [verificado] | para **invocar 1 endpoint** con rate-control |
| **Upstash QStash** | cola HTTP serverless | at-least-once, FIFO en Queues | sí | POST con URL destino, ideal serverless/edge, sin infra |

## Patrón base (el que usarás con GPU)
```
Webhook/Worker recibe → valida → encola {job_id, params} → responde 202 rápido
                                          ↓
Consumer toma el mensaje → dispara worker GPU (submit) → al terminar, sube a R2 + webhook/poll
```
La función serverless **no espera** el render ([[302-serverless-functions-edge-lambda]]). La cola da reintentos,
backpressure y aislamiento: si el GPU falla, el mensaje vuelve, no se pierde el job.

## Fanout
Un evento → N consumers independientes (Pub/Sub, SNS→SQS, Cloudflare Queues). Ej.: "video listo" dispara en
paralelo: notificar usuario, generar thumbnail, indexar, facturar. Cada consumer falla y reintenta aislado.

## DLQ (dead-letter queue)
Tras N reintentos fallidos, el mensaje va a una cola muerta en vez de loopear infinito. **Imprescindible**:
sin DLQ un mensaje "veneno" (params corruptos) reintenta para siempre y quema cuota/dinero. Cloud Tasks **no
trae DLQ** → móntalo a mano (contador de intentos + mover a tabla de fallidos) o usa otra cola.

## Exactly-once: el mito
"Exactly-once" real casi no existe en sistemas distribuidos. Lo que tienes es **at-least-once + idempotencia
en el consumer**. SQS FIFO y Pub/Sub exactly-once reducen duplicados, no los eliminan en todos los bordes.
**La defensa correcta**: dedup por `job_id` único — si ya procesaste ese id, ignora. Guarda el id procesado
en KV/D1/Redis antes de hacer el efecto. Esto también te cubre el doble-disparo de cron ([[306-cron-scheduling]]).

## Cómo elegir
1. ¿Disparar **un** endpoint HTTP con rate y reintento? → Cloud Tasks / QStash.
2. ¿**Fanout** a varios consumers? → Pub/Sub o SNS+SQS.
3. ¿Cola de trabajo clásica pull con FIFO/dedup? → SQS.
4. ¿Serverless/edge sin gestionar infra? → **QStash** (HTTP puro, encaja con Workers/Vercel).

## Trampas
- **Visibility timeout < duración del job** en SQS → el mensaje reaparece y otro worker procesa el mismo job
  en paralelo → duplicado. Ajusta el timeout al peor caso del render.
- **Sin idempotencia** → at-least-once te muerde con efectos duplicados (doble cobro, doble video).
- **Cloud Tasks sin DLQ** → reintento infinito agota recursos; pon tope de intentos.
- **Orden**: solo FIFO/Queues garantizan orden; las colas standard NO.

Cruza con [[23-event-driven-colas]] y [[161-colas-jobs-gpu-a-fondo]].
