# 306 · Cron y scheduling: cron jobs, schedulers durables, idempotencia

> Programar "que corra cada X" es fácil; que corra **exactamente una vez** y sobreviva reinicios, no.
> Todo scheduler serio entrega *at-least-once* → tu job DEBE ser idempotente o se ejecuta doble.

## Sintaxis cron (recordatorio)
```
┌ min (0-59)  ┌ hora (0-23)  ┌ día-mes (1-31)  ┌ mes (1-12)  ┌ día-sem (0-6)
*/5 * * * *   → cada 5 min      0 3 * * *  → 3:00 AM diario     0 0 * * 1 → lunes 00:00
```
Define la **zona horaria** explícita: la mayoría corre en UTC y te quema con horarios locales/DST.

## Opciones cloud
| Servicio | Qué es | Entrega | DLQ/durabilidad |
|---|---|---|---|
| **Cloudflare Cron Triggers** | `scheduled()` handler en un Worker | at-least-once | sin estado propio; combina con DO |
| **Durable Object `alarm()`** | scheduler **stateful** dentro de un DO | persistido en SQLite, **sobrevive reinicios** | el propio DO es el estado |
| **GCP Cloud Scheduler** | cron gestionado → HTTP/Pub/Sub | at-least-once | da headers de dedup |
| **Inngest / Trigger.dev** | durable execution (steps con retry/memo) | durable, reanuda donde falló | nativo |
| **Vercel Cron** | cron → invoca una ruta | at-least-once | combinar con cola |

## La verdad incómoda: at-least-once
- **Cloudflare**: "fallos de red o mantenimiento pueden ejecutar la tarea dos veces. Diseña idempotente." [verificado]
- **GCP Cloud Scheduler**: garantiza *at-least-once*; en casos raros corre varias veces por una misma
  programación → tu handler no debe tener efectos dañinos al repetir [verificado].
→ **Nunca** asumas exactly-once. El doble-disparo es normal, no un bug.

## Idempotencia (la defensa obligatoria)
1. **Clave de ejecución estable**: GCP da `X-CloudScheduler-ScheduleTime` (constante entre reintentos) +
   nombre del job → úsalo como id de dedup [verificado]. En CF, usa el timestamp del tick redondeado al slot.
2. **Lock/dedup antes del efecto**: guarda `run:<id>` en KV/D1/DO/Redis con TTL. Si ya existe → sal sin hacer nada.
3. **Efectos idempotentes**: `UPSERT` en vez de `INSERT`; "marcar enviado" antes de enviar, no después.
4. **Lock de exclusión** para "solo un worker a la vez": un Durable Object serializa el acceso → cero carrera.

## Caso STUDIO: tick durable de 60s
Loop que cada 60s revisa jobs pendientes (cola GPU, polls de render, recordatorios — ver [[115-async-render-largo-poller-durable]]):
- **No** uses `setInterval` en un proceso serverless: muere al escalar a 0 y pierdes el tick.
- Usa **DO `alarm()`**: al terminar el tick, reprograma la alarma a +60s. Sobrevive reinicios y deploys,
  estado en SQLite del DO. Un solo DO = un solo tick → sin solapamiento.
- Cada tick debe ser **corto e idempotente**: si tarda más de 60s, la siguiente alarma puede solapar →
  marca `tick_running` y saltea si ya hay uno en curso.

## Patrón cron → cola (no hagas el trabajo en el tick)
El cron debe ser **disparador**, no ejecutor: encola los jobs ([[305-message-queues-cloud]]) y deja que los
consumers (idempotentes) trabajen. Así un tick lento no bloquea el siguiente y los reintentos viven en la cola.

## Trampas
- Job largo en el handler de cron → se solapa con el siguiente tick → ejecuciones concurrentes pisándose.
- Confiar en exactly-once → doble email/cobro/render. Siempre dedup por id.
- Zona horaria implícita → corre a la hora equivocada tras DST.
- `setInterval`/proceso "siempre vivo" en serverless → se apaga al escalar a 0; usa scheduler durable.

Cruza con [[285-background-jobs-queues-web]] y [[115-async-render-largo-poller-durable]].
