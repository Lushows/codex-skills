# 348 · Patrones de automatización (los que aguantan producción)

> Un workflow que corre en la demo y otro que sobrevive a reintentos, duplicados, fallos parciales y
> un humano que aprueba a las 3am son cosas distintas. Estos patrones son la diferencia.

## Triggers: las tres familias
| Tipo | Dispara por | Latencia | Riesgo principal |
|---|---|---|---|
| **Event/Webhook** | un sistema te empuja (push) | ~ms | duplicados, orden, firma falsa |
| **Polling** | tú preguntas cada X (pull) | el intervalo | gaps, re-leer lo mismo, rate-limit |
| **Schedule/Cron** | el reloj | hasta el slot | jobs solapados, drift, zona horaria |

Prefiere **push** si el origen lo ofrece (menos latencia, menos llamadas). Cae a **polling con
cursor** (guarda el `last_id`/`updated_since`, no reproceses) cuando no hay webhook.

## Idempotencia (el patrón que más fallos previene)
Toda automatización dispara dos veces tarde o temprano (reintento del proveedor, redeploy, doble
click). Hazla **idempotente**: el efecto de ejecutar N veces == 1 vez.
- **Idempotency key**: deriva una clave estable del evento (`order_id`, `message_id`, hash del payload).
  Antes de actuar, comprueba/insertá en una tabla `processed_keys` (UNIQUE). Si ya está → skip.
- **Upsert** en vez de insert; **PUT** (idempotente) en vez de POST cuando puedas.
- Proveedores que ya dan clave: Stripe (`Idempotency-Key` header), Meta (`message_id`). Úsalas.

## State: dónde vive el progreso
No guardes estado crítico dentro del runtime de automatización (n8n, Lambda) — es efímero y opaco.
- **Externalízalo** a Postgres/Redis: status de la entidad (`pending|processing|done|failed`), cursor de polling, contador de intentos.
- **Máquina de estados explícita** para procesos multi-paso (pedido: `creado→pagado→empacado→enviado`).
  Cada transición es una fila/evento → auditable y reanudable.
- **Lease/lock** (Redis `SET key val NX EX 30`) para que dos workers no procesen el mismo ítem.

## Error handling en capas
1. **Retry con backoff exponencial + jitter** solo para errores **transitorios** (5xx, timeout, 429).
   Nunca reintentes un 4xx de validación (fallará igual y quema cuota).
2. **Circuit breaker**: si el destino lleva N fallos seguidos, deja de golpearlo un rato.
3. **DLQ (dead-letter queue)**: lo que agota reintentos va a una cola/tabla aparte para inspección manual, **no se pierde**.
4. **Error Workflow / alerta**: un fallo no manejado debe gritar (Slack/email), no morir callado.
5. **Compensación (saga)**: si el paso 3 de 4 falla, deshaz 1 y 2 (refund, liberar stock). No dejes estado a medias.

## Human-in-the-loop (HITL)
Cuando el costo de un error automático es alto (envío masivo, refund grande, baja de cuenta):
- El workflow **pausa** y crea una tarea de aprobación (botón en Slack/dashboard, link firmado).
- Persiste el estado `awaiting_approval` con un **timeout** (si nadie aprueba en X, escala o cancela — no cuelgues para siempre).
- Registra **quién** aprobó y cuándo (auditoría). El humano es un nodo más, con su propio estado y caducidad.

## Diseño de payloads y observabilidad
- **Correlation ID** por flujo: propágalo en cada paso y log → trazas un evento de punta a punta.
- **Logs estructurados** (JSON) con el ID, el paso y el resultado; no `console.log("ok")`.
- **Métricas**: éxitos/fallos por workflow, latencia p95, tamaño de la DLQ. Sin esto vuelas a ciegas.

## Anti-patrones
- Workflow síncrono largo que timeoutea al emisor → este reintenta → duplicados. Responde rápido, procesa async.
- Retry infinito sin DLQ → loop de la muerte quemando cuota de API.
- Estado solo en variables del runtime → un reinicio lo borra.
- "Funciona en mi demo" sin probar el camino de fallo → producción es puro camino de fallo.

Cruza con [[285-background-jobs-queues-web]], [[306-cron-scheduling]], [[347-n8n-make-zapier-deep]] y [[351-rpa-integraciones]].
