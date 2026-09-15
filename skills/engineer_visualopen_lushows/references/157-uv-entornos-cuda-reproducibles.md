# 157 · uv para entornos CUDA reproducibles (lockfile que clava torch+cuda en el worker)

> `pip install torch` da un env distinto cada día. `uv` con lockfile da el **mismo** env exacto
> en tu portátil y en el worker GPU, y resuelve en segundos en vez de minutos.

## Por qué uv > pip/conda aquí
- **Velocidad**: resolver+instalar en segundos (resolver en Rust, descargas paralelas, caché global). conda tarda minutos resolviendo; pip no tiene lockfile real.
- **Reproducible de verdad**: `uv.lock` fija versión + **hash** de cada wheel, incluido torch. `requirements.txt` con `==` no fija hashes ni el árbol transitivo completo.
- **Maneja índices de torch nativamente**: declara el índice CUDA en `pyproject.toml`, no en flags sueltos que se olvidan. Cruza con [[155-docker-para-ml-a-fondo]].

## Índices de torch: cu126 / cu128 / cu130
Las wheels CUDA de torch NO están en PyPI; viven en `https://download.pytorch.org/whl/{backend}` (backends 2026: `cpu`, `cu126`, `cu128`, `cu130`, `rocm6.4`, `xpu`). Se declara como índice **explícito** (solo se usa para los paquetes que lo apuntan, no para todo):
```toml
# pyproject.toml
[project]
name = "longcat-worker"
requires-python = "==3.11.*"
dependencies = ["torch==2.8.0", "torchvision==0.23.0", "runpod>=1.7"]

[[tool.uv.index]]
name = "pytorch-cu128"
url = "https://download.pytorch.org/whl/cu128"
explicit = true            # clave: este índice SOLO sirve a los paquetes de abajo

[tool.uv.sources]
torch       = { index = "pytorch-cu128" }
torchvision = { index = "pytorch-cu128" }
```
**Gotcha**: cada paquete torch que quieras en versión GPU debe listarse en `[tool.uv.sources]`. Si omites `torchvision`, uv lo resuelve desde PyPI (build CPU) → mismatch silencioso. `explicit = true` evita que uv busque el resto de tus deps en el índice de pytorch.

## Fijar CUDA y reproducir el env exacto
```bash
uv lock          # resuelve y escribe uv.lock con versiones + hashes
uv sync          # crea .venv idéntica al lock
uv sync --frozen # FALLA si pyproject y lock divergen → garantiza reproducibilidad en CI/worker
```
`uv.lock` se commitea. En el worker se hace **solo `uv sync --frozen`**: instala bit-a-bit lo del lock, sin re-resolver, sin sorpresas de "ayer funcionaba". Para pinear distintas CUDA por entorno (un dev en CPU, worker en cu128) usa marcadores de plataforma o extras, no edites el lock a mano.

## Integración con Docker (multi-stage + cache-mount)
```dockerfile
FROM nvidia/cuda:12.8.0-devel-ubuntu22.04 AS build
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_INSTALL_DIR=/python \
    UV_PROJECT_ENVIRONMENT=/app/.venv

WORKDIR /app
# 1) Solo el lock+pyproject → capa de deps cacheable (no invalida al cambiar código)
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev
# 2) Código después → cambiar handler.py NO re-resuelve deps
COPY . .
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

FROM nvidia/cuda:12.8.0-runtime-ubuntu22.04
COPY --from=build /app/.venv /app/.venv
COPY --from=build /python /python
ENV PATH="/app/.venv/bin:$PATH"
WORKDIR /app
COPY handler.py .
CMD ["python", "-u", "handler.py"]
```
Claves de este patrón (verificadas con la guía oficial de uv en Docker):
- **`--mount=type=cache,target=/root/.cache/uv`**: reusa descargas entre builds sin engordar la capa.
- **`UV_LINK_MODE=copy`**: el caché y la venv viven en filesystems distintos; sin esto, uv tira warnings de hard-link cross-FS.
- **`UV_COMPILE_BYTECODE=1`**: compila `.pyc` en build → cold-start del worker más rápido (menos trabajo al importar). Cruza con [[155-docker-para-ml-a-fondo]] y el cold-start.
- **Two-stage sync** (`--no-install-project` y luego el proyecto): separa la capa de deps (lenta, estable) de la de código (rápida, volátil) → builds repetidos en segundos.
- **Pin de Python**: `requires-python = "==3.11.*"` + uv gestiona el intérprete → mismo Python en dev y worker.

## flash-attn / kernels que compilan con uv
flash-attn necesita torch presente al compilar y rompe el aislamiento de build:
```bash
uv pip install flash-attn==2.7.4.post1 --no-build-isolation
```
O declara `[tool.uv.extra-build-dependencies]` para que torch esté disponible durante el build del paquete. Misma regla que con pip: torch **antes**, compilar **después**, ABI casada con la CUDA del índice. Cruza con [[126-attention-backends-fa3-xformers-sage]].

Cruza con [[155-docker-para-ml-a-fondo]] y [[126-attention-backends-fa3-xformers-sage]].
