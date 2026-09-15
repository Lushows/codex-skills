# 297 · CI/CD web con GitHub Actions (la app, no el worker GPU)

> El worker GPU se despliega por digest a RunPod ([[16-cicd-modelos-workers]]); la **app web** (dashboard,
> API, frontend) tiene otro pipeline: build rápido, preview por PR, deploy por merge. Más altitud aquí.

## Anatomía de un workflow web
```yaml
name: ci
on:
  pull_request: {}
  push: { branches: [main] }
concurrency: { group: ci-${{ github.ref }}, cancel-in-progress: true }
permissions: { contents: read, id-token: write, pull-requests: write }  # id-token=OIDC, PR=comentar preview
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }   # cachea ~/.pnpm-store por hash del lockfile
      - run: pnpm install --frozen-lockfile
      - run: pnpm lint && pnpm typecheck && pnpm test --run
```
`cancel-in-progress` mata runs viejos del mismo PR; `--frozen-lockfile` falla si el lock no matchea (reproducible).

## Matrix: para qué SÍ y para qué NO
Matrix tiene sentido en **librería** que soporta varias versiones Node/navegadores. Para **una app que tú
deployas a un runtime conocido**, matrix solo quema minutos: fija UNA versión (la de prod) y listo. Reserva
matrix multi-versión para el worker GPU (CUDA/torch, ref 16), no para el dashboard.

## Secrets, environments y OIDC
- **Repository/Environment secrets** encriptados; nunca en el repo. `environments` (`production`) con
  **required reviewers** = gate humano antes de prod, y permite secrets distintos por entorno.
- **OIDC** > tokens largos: GitHub emite un token efímero, el cloud asume un rol. Requiere
  `permissions: id-token: write` (si falta, falla **en silencio**). AWS:
  ```yaml
  - uses: aws-actions/configure-aws-credentials@v4
    with: { role-to-assume: arn:aws:iam::123:role/gha-deploy, aws-region: us-east-1 }
  ```
- Distingue **build-time vs runtime**: una env var horneada en el bundle frontend (`NEXT_PUBLIC_*`, `VITE_*`)
  se filtra al browser. Secrets de servidor van solo en runtime de la plataforma.

## Preview deploys por PR
El patrón que más valor da: cada PR levanta un entorno efímero, comentas la URL, se destruye al cerrar.
- **Vercel/Netlify/Cloudflare Pages**: preview automático nativo, cero YAML (ver [[299-deploy-vercel-render-fly-railway]]).
- **Self-host**: deploya a un slot/namespace por PR y comenta con `actions/github-script`; limpia en
  `on: pull_request: types: [closed]`.

## Monorepo: solo construye lo que cambió
| Técnica | Qué hace |
|---|---|
| `dorny/paths-filter` | gatea jobs por rutas tocadas (`apps/web/**` → corre job web) |
| Turborepo `--filter='...[origin/main]'` | tareas solo de paquetes afectados + deps |
| Turborepo `--affected` | igual pero tolera shallow clone (fallback: corre todo) |
| Remote Cache (`turbo`/Nx Cloud) | reusa artefactos entre runs y devs |

`fetch-depth: 0` (o ≥2) en `checkout` para que el diff contra `origin/main` exista; con shallow clone el
filtrado bespoke falla y `--affected` te salva.

## Gotchas
1. Sin `concurrency` acumulas runs zombies en PRs activos → minutos quemados.
2. `id-token: write` ausente → OIDC falla callado, no con error claro.
3. Cache por `${{ github.sha }}` nunca acierta (cada commit es único) → cachea por **hash del lockfile**.
4. Build-time env (`NEXT_PUBLIC_*`) horneado = secreto en el browser.
5. Shallow clone + diff contra `main` = "no merge base" → fija `fetch-depth`.

**Fuentes:** turborepo.dev/docs/guides/ci-vendors/github-actions · github.com/dorny/paths-filter · docs.github.com/actions/deployment/security-hardening-with-openid-connect.
Cruza con [[16-cicd-modelos-workers]], [[156-ghcr-github-actions-workers-gpu]] y [[299-deploy-vercel-render-fly-railway]].
