# 298 · Docker Compose para apps web (sin GPU)

> [[155-docker-para-ml-a-fondo]] cubre imágenes CUDA pesadas; aquí el stack web cotidiano:
> api + db + cache + reverse-proxy, con healthchecks reales y un dev que matchea prod.

## El stack base
```yaml
services:
  api:
    build: { context: ., target: prod }       # multi-stage; dev usa target distinto
    env_file: .env
    ports: ["3000:3000"]
    depends_on:
      db:    { condition: service_healthy }    # NO arranca hasta que db pase su healthcheck
      redis: { condition: service_started }
    healthcheck:
      test: ["CMD", "node", "-e", "fetch('http://localhost:3000/health').then(r=>process.exit(r.ok?0:1))"]
      interval: 10s
      timeout: 3s
      retries: 5
      start_period: 20s                        # gracia inicial; los fallos no cuentan aún
  db:
    image: postgres:17
    environment: { POSTGRES_PASSWORD: dev, POSTGRES_DB: app }
    volumes: ["pgdata:/var/lib/postgresql/data"]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      retries: 10
  redis:
    image: redis:7-alpine
    volumes: ["redisdata:/data"]
volumes: { pgdata: {}, redisdata: {} }
```

## `depends_on` + condition: el detalle que casi todos fallan
`depends_on` solo (sin `condition`) espera que el contenedor **arranque**, no que el servicio esté **listo**.
Postgres tarda segundos en aceptar conexiones tras `started` → la api crashea con "connection refused".
Fija `condition: service_healthy` y dale al servicio un `healthcheck` real (`pg_isready`, no `sleep`).

## Multi-stage: una imagen, dos perfiles
```dockerfile
FROM node:22-slim AS base
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN corepack enable && pnpm install --frozen-lockfile

FROM base AS dev
CMD ["pnpm","dev"]                # hot-reload; el código entra por bind-mount

FROM base AS prod
COPY . .
RUN pnpm build && pnpm prune --prod
USER node                         # NO corras como root en prod
CMD ["node","dist/server.js"]
```

## Dev vs prod: dos compose, no `if`
```yaml
# compose.override.yml  (Compose lo carga automático en local)
services:
  api:
    build: { target: dev }
    volumes: ["./src:/app/src"]   # bind-mount = hot reload; en prod NO montas código
    command: pnpm dev
```
Prod: `docker compose -f compose.yml up` (sin override). Local: `docker compose up` (mergea override).
Misma definición base, override solo cambia lo de dev — evita drift dev↔prod.

## Reglas que muerden
| Tema | Hazlo así |
|---|---|
| Datos | **named volumes**, no bind-mounts para DB (permisos/perf en Mac/Win) |
| Secrets | `env_file` en dev; en prod, secrets de la plataforma o `docker secret`, nunca en la imagen |
| Logs | a stdout/stderr (12-factor), que el orquestador los recoja |
| Red | servicios se ven por **nombre de servicio** (`db:5432`), no `localhost` |
| Build | `.dockerignore` con `node_modules`, `.git`, `*.env` → build chico y sin secretos |

## Gotchas
1. `depends_on` sin `condition` = race: api conecta antes de que la DB acepte → crash al boot.
2. Healthcheck con `sleep`/exit-0 fijo no detecta caída real → reinicios que no pasan nada.
3. Bind-mount sobre `node_modules` instalado en la imagen lo **tapa** con el del host (arch distinta) → rompe.
4. `latest` en images base = build no reproducible; pinea `postgres:17`, no `postgres`.
5. Olvidar `USER node` → el contenedor corre root (superficie de ataque).

**Fuentes:** docs.docker.com/compose/compose-file (depends_on/healthcheck) · docs.docker.com/build/building/multi-stage · 12factor.net.
Cruza con [[155-docker-para-ml-a-fondo]] y [[299-deploy-vercel-render-fly-railway]].
