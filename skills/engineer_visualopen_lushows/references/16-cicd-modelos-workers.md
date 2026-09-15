# 16 — CI/CD para modelos y workers

Meta: un push construye una imagen CUDA, la smoke-testea, y apunta atómicamente un endpoint RunPod al nuevo
SHA — con rollback de un comando.

## GitHub Actions esencial
**Matrix** para CUDA/torch combos; **`concurrency`** cancela runs superados; **environments** con **required
reviewers** = gate de aprobación a prod; **OIDC** para asumir roles cloud sin secrets largos; **reusable
workflows** (`workflow_call`) para DRY.
```yaml
concurrency: { group: deploy-${{ github.ref }}, cancel-in-progress: true }
permissions: { contents: read, packages: write, id-token: write }   # id-token = OIDC
jobs:
  test:
    strategy: { matrix: { py: ["3.11","3.12"] } }
    steps: [{uses: actions/checkout@v4}, {run: pip install ruff mypy pytest && ruff check . && mypy src && pytest -q}]
```

## Build + push CUDA a GHCR con cache buildx
**Desde abril 2025 solo Cache API v2.** Para imágenes grandes, `type=registry` suele ser más durable que `type=gha`:
```yaml
  build:
    needs: test
    steps:
      - uses: docker/setup-buildx-action@v3
      - uses: docker/login-action@v3
        with: { registry: ghcr.io, username: ${{ github.actor }}, password: ${{ secrets.GITHUB_TOKEN }} }
      - uses: docker/build-push-action@v6
        with: { push: true, tags: ghcr.io/${{ github.repository }}:${{ github.sha }},
                cache-from: type=gha, cache-to: type=gha,mode=max }
```

## Smoke-test gate
Antes de desplegar, corre la imagen recién construida y pégale un input fijo chiquito; falla el job si no
devuelve resultado válido. Atrapa "importa bien, crashea en la 1ª inferencia" (pesos faltantes, ABI torch/CUDA).

## Deploy: pinear el SHA al endpoint RunPod
El endpoint referencia un **template**; actualiza su `imageName` vía REST `POST https://rest.runpod.io/v1/
templates/{templateId}/update` (Bearer) → dispara un nuevo rollout. **Pin el digest/SHA, nunca `:latest`:**
```bash
curl -X POST https://rest.runpod.io/v1/templates/$TPL/update \
  -H "Authorization: Bearer $RUNPOD_API_KEY" -H "Content-Type: application/json" \
  -d '{"imageName":"ghcr.io/me/worker@sha256:'"$DIGEST"'"}'
```

## Blue-green / canary + rollback
Dos endpoints (o dos templates); manda un % chico al nuevo vía el gateway, observa evals/error rate, cut over.
**Rollback = re-POST el SHA previo conocido-bueno** (guárdalo en un tag de Git o env var). **GitOps:** el SHA
deseado vive en un archivo del repo; un workflow reconcilia RunPod → el repo es source of truth, rollback = `git revert`.

## Gate de eval de modelo
Además de lint/type/unit, añade un **job de eval** (ver ref 17) que corre el golden set y **falla el deploy si la
calidad regresa**.

## Gotchas
1. `:latest` hace imposible el rollback y rompe reproducibilidad — despliega por digest.
2. El cache GHA tiene límite ~10GB/repo — las capas CUDA enormes se evictan; usa `type=registry` para base layers.
3. OIDC necesita `permissions: id-token: write` o falla en silencio.
4. `GITHUB_TOKEN` empuja a GHCR solo con `packages: write`.
5. El rollout de RunPod es async — sondea health/workers antes de declarar éxito; workers calientes sirven la imagen vieja un rato.

**Fuentes:** docs.docker.com/build/cache/backends/gha · docs.runpod.io/api-reference/templates · lucaschmid.net/blog/runpod-deploy.
