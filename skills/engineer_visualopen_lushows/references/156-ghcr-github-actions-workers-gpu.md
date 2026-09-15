# 156 · GHCR + GitHub Actions para workers GPU (build, push y pin del SHA en RunPod)

> El worker no se buildea en tu portátil: lo buildea GitHub Actions y lo publica en GHCR.
> RunPod tira de ese registry. El truco fino es **pinear el SHA inmutable** y no chocar con el
> gotcha de timing `IMAGE_NOT_FOUND`.

## Por qué GHCR + Actions
- GHCR (`ghcr.io/usuario/worker`) es gratis para repos públicos, integrado con el `GITHUB_TOKEN` (no manejas credenciales aparte).
- Actions buildea en runners con red rápida → compilar flash-attn y pushear 8 GB es más veloz que tu casa.
- Cada push a `main` reconstruye y publica → CI/CD real para el worker. Cruza con [[16-cicd-modelos-workers]].

## Workflow de build + push
```yaml
name: build-worker
on:
  push: { branches: [main] }
jobs:
  build:
    runs-on: ubuntu-latest
    permissions: { contents: read, packages: write }   # packages:write = push a GHCR
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/metadata-action@v5
        id: meta
        with:
          images: ghcr.io/${{ github.repository_owner }}/longcat-worker
          tags: |
            type=sha,format=long
            type=raw,value=latest,enable={{is_default_branch}}
      - uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          provenance: false      # evita el manifest "attestation" que confunde a algunos runtimes
```

## Cache de capas: `type=gha`
`cache-from/to: type=gha` guarda las capas en el caché de Actions → el segundo build reusa torch/flash-attn ya compilados (de 20 min a 2-3 min si solo cambió `handler.py`). `mode=max` cachea **todas** las capas intermedias, no solo el resultado final. Nota 2025+: solo se soporta la **Cache API v2** (la v1 se apagó el 15-abr-2025) → usa `docker/build-push-action@v6` o superior, las versiones viejas fallan con "legacy service shutting down". Cruza con [[155-docker-para-ml-a-fondo]] para el orden de capas que hace que este caché valga.

## Tags: `sha` vs `latest`
- `type=sha,format=long` → tag inmutable `sha-<commit>`: para **producción**, pineable, reproducible.
- `latest` → móvil, apunta al último `main`: cómodo para dev, **veneno en producción** (el worker puede cambiar bajo tus pies sin que te enteres).
- Mejor aún: pinea el **digest** `ghcr.io/.../worker@sha256:...` (inmutable de verdad; un tag se puede re-pushear, un digest no).

## Smoke-test post-build (no publiques basura)
Antes de marcar el build OK, arranca el contenedor e importa lo crítico. No necesitas GPU para detectar imports rotos o ABI mismatch obvio:
```yaml
      - name: smoke test
        run: |
          docker run --rm ghcr.io/${{ github.repository_owner }}/longcat-worker:sha-${{ github.sha }} \
            python3 -c "import torch, runpod; print('torch', torch.__version__)"
```
Para test con GPU real necesitas un runner con GPU (self-hosted o GitHub larger-runner GPU). El smoke-test sin GPU ya atrapa el 80% (módulo no encontrado, versión incompatible).

## Matrix (varias variantes)
Buildea cu126 y cu128 (o varias GPUs/modelos) en paralelo con `strategy.matrix`:
```yaml
    strategy:
      matrix:
        cuda: [cu126, cu128]
    # pásalo como build-arg y al tag:  tags: ...:sha-${{ github.sha }}-${{ matrix.cuda }}
```
Da `cache-to` un **scope distinto por variante** (`scope=${{ matrix.cuda }}`) o cada build pisa el caché del anterior.

## El patrón: pinear el SHA en RunPod + el gotcha `IMAGE_NOT_FOUND`
1. Actions termina y publica `ghcr.io/.../worker:sha-abc123` (o `@sha256:...`).
2. En el endpoint RunPod, pega **ese tag/digest exacto**, no `latest`. Así sabes qué corre y puedes rollback cambiando una línea.
3. **GOTCHA de timing**: si actualizas el endpoint con el SHA **antes** de que el push a GHCR termine de propagarse, RunPod arranca el worker, no encuentra la imagen y muere con **`IMAGE_NOT_FOUND`**. No es que el tag esté mal: es que llegaste antes que el registry. **Espera a que el workflow esté verde** (push completo) antes de tocar el endpoint, o automatiza el update del endpoint como **último step del workflow** (vía API de RunPod) para serializarlo.
4. GHCR privado: añade el credential de registry en RunPod (PAT con `read:packages`) o el pull falla con auth, no con `IMAGE_NOT_FOUND`.

Cruza con [[16-cicd-modelos-workers]], [[111-longcat-avatar-runpod-produccion]] y [[155-docker-para-ml-a-fondo]].
