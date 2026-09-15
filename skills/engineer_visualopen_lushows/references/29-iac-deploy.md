# 29 — IaC & deploy

## Local multi-servicio — Docker Compose
```yaml
services:
  api: { build: ., ports: ["3000:3000"], env_file: .env, depends_on: [db] }
  db:  { image: postgres:16, environment: { POSTGRES_PASSWORD: dev }, volumes: ["pgdata:/var/lib/postgresql/data"] }
volumes: { pgdata: {} }
```
Entorno de dev reproducible que matchea las imágenes de prod.

## Render / Railway (el host del usuario)
Push-to-deploy desde GitHub. Infra como código: **Render Blueprint `render.yaml`** (web + worker + cron + DB en
un archivo versionado) o config de Railway. **Los health checks son cómo logras zero-downtime:** expón
`GET /health` → `200` cuando esté listo; la plataforma bootea la instancia nueva, gatea el tráfico en el health
check, luego cut over (Render corre vieja+nueva en paralelo y switchea; Railway sondea hasta `200`). **Secrets/env**
viven en los settings de la plataforma (o sync desde Doppler/Infisical), nunca en el repo — distingue build-time
vs runtime (secrets build-time se filtran al bundle del cliente).

## Cuándo Kubernetes es overkill
Para equipo chico / un producto, K8s añade un control plane, YAML sprawl, y carga SRE que no necesitas.
Render/Railway/Fly/ECS-Fargate cubren. K8s solo con muchos servicios, multi-team, networking custom, o scheduling específico.

## Terraform básico
IaC declarativa multi-provider. **State** (`terraform.tfstate`) = source of truth → guárdalo **remoto** (S3/GCS +
locking), nunca lo commitees (tiene secrets) ni edites a mano. **Providers** (aws, cloudflare, render) = plugins.
**Modules** = sets reusables con input variables. Flujo: `init → plan → apply`. Workspaces o dirs por entorno.

## GitHub Actions deploy
CI en PR (lint + mypy + pytest + pip-audit), CD en merge a `main`. Tokens de deploy como **repository secrets** encriptados; OIDC para asumir roles cloud sin keys largas.

## Zero-downtime deploys
Cutover rolling/blue-green gateado por health (la plataforma lo hace); migraciones DB **backward-compatible**
(expand→migrate→contract) para que código viejo y nuevo corran juntos durante el swap; drena conexiones en `SIGTERM`.

## Secrets/config (12-factor)
Config en env, no en código; un config object por servicio; misma imagen promovida entre entornos con distintos env vars.

## Stack pragmático equipo chico 2026
GitHub → GitHub Actions CI (test+audit) → push imagen / git-deploy a **Render o Railway** con `render.yaml`/health
checks → secrets en env de la plataforma (o Doppler) → Postgres + Redis managed. Terraform solo al superar el PaaS. **Skip Kubernetes.**

## Gotchas
1. Health check ausente/instant-`200` → tráfico a instancia no-lista = downtime.
2. Commitear `terraform.tfstate` filtra secrets y corrompe en runs concurrentes (usa remote state + locking).
3. Migración DB breaking durante rolling deploy crashea las instancias viejas a mitad del swap.
4. Env vars build-time horneados en un bundle frontend filtran secrets al browser.

**Fuentes:** render.com/articles (zero-downtime) · render.com/docs/blueprint-spec · docs.railway.com/guides/healthchecks · developer.hashicorp.com/terraform (remote state) · 12factor.net.
