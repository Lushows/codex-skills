# 300 · Observabilidad web: Sentry, OpenTelemetry, logs, RUM

> [[15-observabilidad-produccion]] mira la **GPU** (DCGM, latencia de inferencia); aquí la **app web**:
> errores con stack legible, trazas request→DB, logs estructurados y experiencia real del usuario.

## Las tres señales (y qué resuelve cada una)
| Señal | Pregunta que responde | Herramienta |
|---|---|---|
| **Errores** | ¿qué crasheó, con qué stack y para quién? | Sentry |
| **Trazas** | ¿en qué span se fue el tiempo (DB, API externa, Claude)? | OTel → Sentry/Tempo |
| **Logs** | ¿qué pasó alrededor de ese error, con contexto? | logs estructurados JSON |
| **RUM** | ¿qué experimentó el usuario real (LCP, INP, errores cliente)? | Sentry Browser / web-vitals |

## Sentry: setup mínimo que vale
```ts
// instrument.ts — DEBE importarse PRIMERO, antes de tu app
import * as Sentry from "@sentry/node";
Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV,
  release: process.env.GIT_SHA,        // ata el error al commit → source maps correctos
  tracesSampleRate: 0.2,               // 20% de trazas; errores van al 100%
  profilesSampleRate: 0.1,
});
```
- **Release = GIT_SHA**: sin esto Sentry no sabe qué source map aplicar y el stack queda ofuscado.
- **Sube source maps en el build** (`sentry-cli sourcemaps upload` o el plugin del bundler) atados al
  mismo release; **no los publiques** en el dir estático (filtras tu código).
- **Tunnel** (`tunnelRoute`): proxea los eventos por **tu** dominio para que ad-blockers no maten el
  reporte del browser. Lo paga: un endpoint extra en tu server que reenvía a Sentry.

## OpenTelemetry: el estándar, y el estado real en Sentry (2026)
OTel es el estándar abierto para trazas/logs/métricas; instrumentas una vez y exportas a donde sea (OTLP).
- Sentry **ingiere trazas y logs vía OTLP** (endpoint OTLP propio) — **en beta**, y **no** métricas.
  Algunas features integradas faltan en la ruta OTLP. [verificado: docs.sentry.io/concepts/otlp]
- Estrategia pragmática: usa el **SDK de Sentry** (que internamente ya usa OTel en Node) para el camino
  feliz; reserva el Collector OTLP puro si necesitas multi-backend o ya tienes pipeline OTel.
```
[app + OTel SDK] --OTLP--> [OTel Collector] --> Sentry (trazas/logs)
                                            \-> Prometheus/Tempo (si multi-backend)
```

## Logs estructurados (no `console.log` suelto)
```ts
logger.info({ event: "order_created", phone, orderId, amount, trace_id: span.spanContext().traceId });
```
- **JSON con `trace_id`**: corta un log y saltas a su traza en Sentry/Tempo (correlación).
- A **stdout** (12-factor); el host los recoge. Niveles reales (`info/warn/error`), no todo a `info`.
- **Nunca** loguees secretos/PII en claro (tokens de WhatsApp, API keys, teléfono completo si aplica).

## RUM / Web Vitals
Mide al **usuario real**, no Lighthouse: `LCP`, `INP`, `CLS`. El SDK browser de Sentry los captura solo;
o `web-vitals` → tu endpoint. Sirve para ver regresiones de UX por release, no solo errores.

## Qué alertar (poco y accionable)
- Spike de **error rate** por release (gatea/rollback — ver [[16-cicd-modelos-workers]] canary).
- **p95 latencia** de endpoints críticos (webhook, checkout).
- **Fallo de dependencia externa** (Claude API, WhatsApp Cloud) — distíngue tu bug de su caída.
- Ruteo y on-call: ver [[363-monitoring-alerting-oncall]]. Evita alertas que nadie acciona (fatiga).

## Gotchas
1. `Sentry.init` no importado primero → instrumentación parcial, spans perdidos.
2. Sin `release`/source maps subidos = stacks ofuscados inútiles en prod.
3. `tracesSampleRate: 1.0` en tráfico alto = factura/ruido; muestrea trazas, no errores.
4. OTLP→Sentry es **beta** y sin métricas: no asumas paridad con el SDK nativo.
5. PII/secretos en logs o breadcrumbs → fuga + incumplimiento.

**Fuentes:** docs.sentry.io/concepts/otlp · develop.sentry.dev/sdk/telemetry/traces/otlp · blog.sentry.io/structured-logging-opentelemetry · sentry.io/solutions/opentelemetry.
Cruza con [[15-observabilidad-produccion]] y [[363-monitoring-alerting-oncall]].
