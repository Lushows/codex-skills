# 100 — Durable execution & background jobs modernos (2026)

A fin 2025 la **durable execution cruzó a early majority** — el driver son los **agentes IA**. AWS shipeó Durable
Functions, Cloudflare Workflows fue GA, Vercel lanzó Workflow DevKit. La idea: el *state* de tu código (qué step
completó, qué devolvió) se **persiste automáticamente** → en crash/restart **resume desde el último step completado**, con retries/sleeps/human-in-the-loop automáticos.

## Por qué importa para agentes IA
Los agentes introducen fallos que el retry tradicional no maneja: orquestación multi-step long-running, **comportamiento LLM probabilístico**, tool calls flaky, y **human-in-the-loop** (un agente puede pausar *horas* por aprobación). La durable execution convierte loops frágiles en workflows production-grade.

## Las opciones
- **Inngest** — event-driven, el **time-to-value más rápido** desde código existente. Steps (`step.run`, `step.sleep`, `step.waitForEvent`) memoizados/retried individualmente. Encaja webhooks/fan-out.
  ```ts
  inngest.createFunction({ id:"process-order" }, { event:"order/created" }, async ({ event, step }) => {
    const ai = await step.run("draft-reply", () => callClaude(event.data))
    await step.run("send-whatsapp", () => sendWhatsApp(ai))   // retried independiente
  })
  ```
- **Trigger.dev (v3/v4)** — el más **JS-native** para long-running (sin timeouts, concurrency/queues/scheduling, self-host). Para video/batch AI/agentes largos en TS.
- **Temporal** — el **estándar enterprise** (workflows-as-code en Go/Java/TS/Python/.NET, cluster dedicado, máximas garantías). Pesado de operar.
- **Restate** — durable + virtual objects + RPC en una **binary ligera** (Temporal-like con menos ops). **DBOS** — **mínimo footprint**: usa **Postgres como capa de durabilidad** (sin cluster aparte).

**vs colas tradicionales:** **BullMQ/Celery** brillan en fire-and-forget de alto throughput pero te empujan toda la orquestación. **Regla: jobs simples independientes → BullMQ/Celery; workflows multi-step stateful (especialmente agentes IA) → durable execution.**

## Gotchas
1. Los steps deben ser **deterministas** — código no-determinista (random, `Date.now()`, I/O directo) fuera de un step rompe el replay; envuelve side effects en `step.run`.
2. Los steps deben ser **idempotentes** — un step puede re-correr tras crash; diseña para at-least-once.
3. **El versioning de workflows es difícil** — cambiar el código de un workflow en vuelo puede romper ejecuciones activas.
4. Los **payloads se persisten** — no pases blobs/secrets grandes por args; pasa referencias.
5. DBOS/Restate son **más jóvenes** con ecosistemas más chicos que Temporal — pesa madurez vs simplicidad.
6. No uses durable execution para **jobs simples** — BullMQ es más ligero; over-engineering añade latencia/ops.

**Fuentes:** pkgpulse.com/guides (Inngest vs Trigger.dev vs Restate 2026) · inngest.com/blog (durable execution + AI agents) · tiarebalbi.com (DBOS vs Temporal).
