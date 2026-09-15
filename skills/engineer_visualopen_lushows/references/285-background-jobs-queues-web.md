# 285 · Background jobs en la web (BullMQ, Inngest, Trigger.dev, Temporal)

> Toda API seria empuja trabajo lento fuera del request: emails, render, llamadas a IA, webhooks salientes.
> [[161-colas-jobs-gpu-a-fondo]] es la cola del worker GPU; esto es la capa de orquestación del **lado web**.

## Por qué nunca lo hagas en el handler HTTP
El request HTTP muere a los ~30s (timeout de proxy/serverless). Un job de render de 5 min, un envío de campaña
WhatsApp o un fan-out de 1000 webhooks **debe** salir a una cola y devolver `202 Accepted` + URL de polling
(cf. [[282-rest-openapi-a-fondo]]). El web encola; un worker drena. Esto desacopla picos y permite retry.

## El espectro: librería que operas ↔ plataforma gestionada
| Herramienta | Modelo | Infra | Brilla en |
|---|---|---|---|
| **BullMQ** | librería Redis, tú corres el worker | Redis + proceso persistente | throughput alto, control fino, rate-limit, flows padre-hijo |
| **Inngest** | event-driven, durable, serverless | gestionada (HTTP) | serverless-first (Vercel), sin Redis, retries por step |
| **Trigger.dev v3** | durable checkpoint-resume, gestionada | gestionada, zero-infra | jobs largos de IA, observabilidad built-in |
| **Temporal** | durable execution, event-sourced replay | self-host/Cloud, **worker persistente** | workflows críticos multi-paso, sagas, compensación |

Regla práctica (verificada jun-2026): **serverless/Vercel → Inngest o Trigger.dev** (BullMQ necesita un proceso
persistente, choca con funciones efímeras). **Ya tienes un server/VPS y quieres control → BullMQ.** **Workflow
crítico, transaccional, multi-servicio → Temporal.** Empezar simple e ir migrando si el volumen/orquestación lo exige.

## Durable execution: el cambio de paradigma
BullMQ reintenta el **job entero** desde cero → tus steps deben ser idempotentes o re-haces trabajo (y re-cobras GPU).
Inngest/Trigger/Temporal persisten **por step**: en un retry, los `step.run()` ya completados se **saltan** y se
reanuda desde el punto de fallo. Para un pipeline "transcribir → llamar IA → renderizar → subir a R2", esto evita
re-pagar la transcripción cuando falla el render. Es la misma idea de [[100-durable-execution-background-jobs-2026]].

## Patrones que siempre necesitas
- **Idempotencia**: clave por job (`jobId = hash(payload)`) → la cola dedup encolados; cada step chequea "¿ya hecho?"
  antes de efectos con costo (mandar email, cobrar, invocar GPU). Sin esto, un retry duplica el efecto.
- **Retry con backoff exponencial + jitter** y un **tope** → luego a **DLQ** (cola muerta) + alerta, no loop infinito.
- **Rate limiting / concurrency**: limita N jobs concurrentes hacia un recurso frágil (API de terceros, pool GPU
  finito de [[161-colas-jobs-gpu-a-fondo]]) → evita 429s y OOM de saturar workers.
- **Prioridad y delay**: cola `high`/`low`; jobs diferidos (recordatorio de recompra a las 24h).
- **Cron / scheduled**: BullMQ `repeat`, Inngest cron, Trigger schedules → reportes diarios, limpieza, reminders.
- **Fan-out / batch**: una campaña → N jobs hijos; espera join con flows (BullMQ) o `step.parallel` (Inngest).

## Observabilidad (no negociable)
Inngest y Trigger.dev traen **trace por run con timing y error por step** en su dashboard — debugging sin instrumentar.
BullMQ requiere **Bull Board** (UI extra que despliegas y mantienes) + métricas propias. Temporal trae su Web UI con
historial de eventos completo. Mínimo a exponer: profundidad de cola, tasa de fallo, latencia p95, jobs en DLQ.

## En este stack (AGENTE / Express + Render)
El proyecto BIOWHATS ya hace trabajo async informal (notificar operador, recordatorio de recompra, campañas). Para
escalar campañas masivas y llamadas a Claude/Whisper sin bloquear el webhook: **BullMQ + Redis** si Render corre un
worker persistente; **Inngest** si se quiere zero-infra y disparo por evento HTTP. El render de video del STUDIO encaja
mejor en **Trigger.dev** (jobs largos, observabilidad) delegando el cómputo al endpoint RunPod ([[161-colas-jobs-gpu-a-fondo]]).

## Gotchas
1. BullMQ en serverless sin proceso vivo = jobs nunca drenan; necesita un worker `while(true)` persistente.
2. Retry del job entero sin idempotencia → email/cobro/GPU duplicados. Diséñala desde el step 1.
3. Payload gordo en la cola (binarios) → pon el blob en R2/S3 y encola solo la **referencia** (cf. [[286-file-uploads-media-handling.md]]).
4. Sin DLQ, un job venenoso reintenta para siempre y tapa la cola — tope de intentos + cola muerta + alerta.
5. Cron sin lock distribuido en multi-instancia → corre N veces; usa el scheduler de la plataforma o un lock Redis.

Cruza con [[161-colas-jobs-gpu-a-fondo]] y [[100-durable-execution-background-jobs-2026]].
