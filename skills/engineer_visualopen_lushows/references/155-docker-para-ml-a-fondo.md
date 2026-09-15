# 155 · Docker para ML a fondo (imágenes GPU que no pesan ni se re-buildean)

> El worker GPU es una imagen Docker. Si eliges mal la base o el orden de capas, pagas en
> minutos de pull frío, en GB de registry y en re-builds de 20 min por cambiar una línea.

## Elegir la base: runtime vs devel vs pytorch oficial
Tres familias, tres usos:

| Base | Trae | Tamaño aprox | Cuándo |
|---|---|---|---|
| `nvidia/cuda:12.8.0-runtime-ubuntu22.04` | CUDA runtime + libs | ~2-3 GB | si instalas torch ya compilado (wheels) |
| `nvidia/cuda:12.8.0-devel-ubuntu22.04` | runtime + headers + `nvcc` | ~6-8 GB | si compilas kernels (flash_attn, custom CUDA) |
| `pytorch/pytorch:2.8.0-cuda12.8-cudnn9-runtime` | torch+cudnn ya dentro | ~7 GB | arranque rápido, no controlas la versión exacta de torch |

Regla: usa **`devel` como stage de build** (compila flash-attn) y **`runtime` como stage final**
(multi-stage) → la imagen de producción no carga `nvcc` ni headers. La base solo necesita libs CUDA;
el driver lo pone el host (RunPod). El tag CUDA debe ser ≤ CUDA del driver del host. Cruza con [[126-attention-backends-fa3-xformers-sage]] para qué backend exige `devel`.

## Multi-stage: compilar en `devel`, correr en `runtime`
```dockerfile
# ---- build stage: tiene nvcc para compilar flash-attn/xformers ----
FROM nvidia/cuda:12.8.0-devel-ubuntu22.04 AS build
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
      python3.11 python3-pip git build-essential ninja-build && \
    rm -rf /var/lib/apt/lists/*
# torch ANTES que flash-attn (flash-attn lo necesita para compilar)
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install torch==2.8.0 --index-url https://download.pytorch.org/whl/cu128
RUN --mount=type=cache,target=/root/.cache/pip \
    MAX_JOBS=4 pip install flash-attn==2.7.4.post1 --no-build-isolation

# ---- runtime stage: sin nvcc, sin headers, imagen final delgada ----
FROM nvidia/cuda:12.8.0-runtime-ubuntu22.04
RUN apt-get update && apt-get install -y --no-install-recommends \
      python3.11 python3-pip ffmpeg && rm -rf /var/lib/apt/lists/*
COPY --from=build /usr/local/lib/python3.11/dist-packages /usr/local/lib/python3.11/dist-packages
COPY handler.py /app/handler.py
WORKDIR /app
CMD ["python3", "-u", "handler.py"]
```
`--no-build-isolation` evita que pip re-instale un torch fantasma para compilar flash-attn (rompería la ABI). Cruza con [[157-uv-entornos-cuda-reproducibles]] para hacer lo mismo con `uv`.

## Orden de capas = caché (la regla de oro)
Docker cachea por capa; una capa invalida **todas las de abajo**. Orden de menos-a-más volátil:
1. `FROM` + `apt-get` (system deps) — casi nunca cambian.
2. **Fijar versiones** e instalar torch/cuda — cambia rara vez.
3. Instalar el resto de deps (`requirements.txt` / lockfile) — cambia a veces.
4. `COPY handler.py` / código — cambia **cada commit**.

Si copias el código ANTES de instalar deps, cada cambio de una línea re-instala TODO. Copia `requirements.txt` solo, instala, y **después** copia el código.

## `--mount=type=cache`: no re-descargar wheels
Cache mount de BuildKit que persiste el caché de pip/uv entre builds **sin** quedar en la imagen:
```dockerfile
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt
```
Necesita BuildKit (`DOCKER_BUILDKIT=1`, default en buildx). El caché no infla la capa final → imagen más chica y builds repetidos mucho más rápidos.

## Fijar versiones torch + CUDA (o ABI rota)
Nunca `pip install torch` a secas: trae el último build, a veces incompatible con tu CUDA o con flash-attn. Pin exacto + índice de la rueda CUDA:
```
pip install torch==2.8.0 torchvision==0.23.0 --index-url https://download.pytorch.org/whl/cu128
```
El sufijo (`cu126`/`cu128`/`cu130`) debe casar con la base CUDA y el driver del host. Mezclar `cu128` torch con un kernel compilado contra `cu126` → `undefined symbol` en runtime.

## Reducir tamaño (cada GB es pull frío)
- `--no-install-recommends` en apt + `rm -rf /var/lib/apt/lists/*` en la MISMA capa `RUN`.
- `.dockerignore`: `**/.git`, `*.pyc`, `__pycache__`, tests, datasets, `*.mp4`.
- Borrar caché pip si no usas cache-mount: `pip install --no-cache-dir`.
- Multi-stage (arriba): deja `nvcc`, headers y objetos `.o` de compilación fuera del final.
- No copies `.git` (a veces cientos de MB) — de ahí el `.dockerignore`.

## Evitar re-build de pesos del modelo
NO hornees 44 GB de checkpoints en la imagen salvo que cambien muy poco: el pull frío se vuelve eterno y cualquier cambio de código invalida la capa de pesos si está mal ordenada. Prefiere **Network Volume** para pesos grandes y la imagen solo para deps+código. Si horneas pesos, ponlos en su **propia capa al final** y nunca encima de algo que cambie. Cruza con [[113-network-volume-modelos-grandes]] y [[130-cold-start-optimizacion-profundo]].

Cruza con [[29-iac-deploy]], [[112-execution-timeout-cold-start-economics]] y [[130-cold-start-optimizacion-profundo]].
