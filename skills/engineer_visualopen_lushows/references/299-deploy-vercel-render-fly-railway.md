# 299 · Deploy de apps: Vercel / Render / Fly / Railway / Cloudflare

> [[132-plataformas-gpu-serverless-comparativa]] elige la nube **GPU**; esto elige el host de la **app web**.
> Regla: la GPU vive en RunPod; el dashboard/API vive en el PaaS más barato que cumpla. No los mezcles.

## Cuándo cada uno (2026)
| Plataforma | Brilla en | Modelo | Free tier (2026) | Gotcha |
|---|---|---|---|---|
| **Vercel** | Next.js, frontends, edge, preview deploys | serverless + Fluid Compute | Hobby gratis (no comercial) | costo escala con uso ($20–200); no para procesos largos |
| **Render** | servicio + worker + cron + Postgres en un `render.yaml` | contenedores siempre-on | **único free real, sin tarjeta** | free tier **duerme** (cold ~30–50s) |
| **Fly.io** | baja latencia multi-región, apps con estado/volúmenes | VMs (Firecracker) | **sin free** (trial 2 VM-h / 7 días) | IPv4 dedicada y snapshots se cobran aparte |
| **Railway** | DX rápido, prototipos, `docker-compose`-like | contenedores usage-based | **sin free** ($5 trial 30 días, luego $5/mes) | el costo por uso sorprende sin límites |
| **Cloudflare** | edge global, estático, Workers/D1/R2/Pages | edge serverless | free generoso | runtime Workers ≠ Node completo (ver [[303-cloudflare-workers-d1-r2]]) |

Costo típico de un SaaS indie (1 web + 1 worker + 1 Postgres, tráfico modesto): **Render/Railway ~$7–15/mes**,
**Fly ~$10–20** (con IPv4+snapshots), **Vercel $20–200** según uso. [no verificado: cifras de blogs comparativos]

## Fluid Compute (Vercel) — sube el techo de timeout
Activo por defecto en proyectos nuevos: timeout **300s por defecto, hasta 800s** en Pro/Enterprise, con
**Active CPU pricing** (pagas CPU usada, no wall-clock). Sigue sin ser para jobs de minutos: si el handler
GPU tarda 5–20 min, Vercel **no** es el cliente — usa submit/poll contra RunPod (ver [[handler-integracion]]).

## El caso STUDIO en Render (lección real)
El dashboard de AGENTE STUDIO vive en Render (web service, free→starter). Lo que mordió:
- **Disco persistente** monta en `/opt/render/project/src/data`; lo que pongas ahí en el repo queda **oculto**
  por el mount → migraciones/seeds NO pueden vivir en `data/` (corren en otro path o pre-mount).
- **Free tier duerme** → primer request tras inactividad ~30–50s; un cron externo (o plan starter) lo
  mantiene caliente.
- **Cold del worker GPU es problema aparte** (RunPod): no lo resuelve Render. Ver [[112-execution-timeout-cold-start-economics]].

## IaC de la plataforma: `render.yaml`
```yaml
services:
  - type: web
    name: dashboard
    runtime: node
    buildCommand: pnpm install --frozen-lockfile && pnpm build
    startCommand: node dist/server.js
    healthCheckPath: /health          # zero-downtime: Render gatea tráfico aquí
    envVars:
      - key: ANTHROPIC_API_KEY
        sync: false                   # se setea en el dashboard, no en el repo
  - type: worker
    name: reminders
    startCommand: node dist/worker.js
```
`healthCheckPath` es **cómo** logras zero-downtime: Render bootea la nueva, espera `200`, hace cut-over,
drena la vieja. Sin él (o con `200` instantáneo antes de estar listo) = downtime.

## Decisión rápida
- Frontend Next.js / mucho preview → **Vercel** o **Cloudflare Pages**.
- App full-stack con worker+cron+DB y quiero free real → **Render** + `render.yaml`.
- Necesito estado, volúmenes, multi-región baja latencia → **Fly**.
- Prototipo veloz, no me importa pagar desde día 1 → **Railway**.
- Edge puro / KV / objetos → **Cloudflare**.

## Gotchas
1. Free tier que duerme: NO sirve para webhooks de WhatsApp/Meta que esperan respuesta rápida (timeouts).
2. Procesos largos (>timeout del runtime) en serverless → mueve a worker/cola, no estires el handler.
3. Disco persistente que tapa archivos del repo (caso Render `data/`).
4. Costo usage-based (Railway/Vercel) sin límites de gasto → fija budget/alerts.
5. Build-time env filtrado al bundle frontend (ver [[297-cicd-pipelines-github-actions]]).

**Fuentes:** vercel.com/pricing (Fluid/Active CPU) · render.com/articles/platforms-with-a-real-free-tier-2026 · saaspricepulse.com/tools/flyio (free cuts) · birjob.com/blog/paas-comparison-2026.
Cruza con [[132-plataformas-gpu-serverless-comparativa]] y [[303-cloudflare-workers-d1-r2]].
