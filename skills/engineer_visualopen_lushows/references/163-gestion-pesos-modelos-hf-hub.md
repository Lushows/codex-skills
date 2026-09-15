# 163 · Gestión de pesos de modelos (HF Hub, auth gated, integridad, pre-poblar volumen)

> Bajar 44GB de pesos bien hecho: con auth para modelos gated, resumible, verificado, una sola vez
> a un volumen. Mal hecho: re-descargas a medias, 401 silenciosos y un cold start eterno.

## huggingface_hub en 2026 (cambió la API)
- **CLI**: `huggingface-cli` **removido** → ahora `hf` (`hf download <repo>`). El flag `--resume-download`
  ya **no existe**: el resume es el comportamiento por defecto. Para forzar re-bajada: `--force-download`.
- **`resume_download`** (Python) **eliminado** en `snapshot_download`/`hf_hub_download` (v1.0): siempre
  resume si puede. No lo pases o lanza error/deprecation.
- **`hf_transfer` deprecado** → reemplazado por **`hf_xet`** (backend Xet, chunk-dedup, más robusto que
  el viejo HF_HUB_ENABLE_HF_TRANSFER). Instala `huggingface_hub[hf_xet]`.

## snapshot_download: el patrón correcto
```python
from huggingface_hub import snapshot_download
path = snapshot_download(
    repo_id="meituan-longcat/LongCat-Video-Avatar",  # ejemplo
    revision="main",                 # PINEA un commit SHA en prod, no 'main' (reproducible)
    cache_dir="/runpod-volume/hf/hub",
    token=os.environ["HF_TOKEN"],    # obligatorio si el repo es gated/privado
    max_workers=8,                   # hilos de descarga concurrentes (default 8)
    allow_patterns=["*.safetensors","*.json","*.txt"],  # baja solo lo que el modelo usa
    ignore_patterns=["*.bin","*.pth","*.onnx"],          # evita formatos duplicados → menos GB
)
```
- **`revision` = SHA fijo en producción.** `main` puede cambiar bajo tus pies (otro hash → otro
  resultado, posible incompatibilidad). Reproducibilidad y rollback. Cruza con [[18-model-registry-versionado]].
- **`allow_patterns`/`ignore_patterns`**: muchos repos traen `.bin` Y `.safetensors` (mismo peso, doble
  tamaño). Bájate solo `safetensors`. Recorta decenas de GB del cold start.
- **`local_dir` vs `cache_dir`**: `cache_dir` = caché HF con symlinks (compartible, dedup); `local_dir`
  = copia plana (algunos loaders la exigen). Para volumen persistente, `cache_dir` + envs (abajo).

## Auth: modelos gated / privados
- **Token**: crea un *read* token en HF, pásalo por `token=` o `HF_TOKEN` env (NO lo hornees en la imagen
  Docker pública → secreto de RunPod). Sin token, un repo gated devuelve **404/401** (no 403) → diagnóstico confuso.
- **Gated**: además del token, hay que **aceptar los términos** del modelo en la web de HF con esa cuenta
  una vez. El token solo no basta si no aceptaste el acuerdo.
- **Verifica acceso** antes del job: `from huggingface_hub import auth_check; auth_check(repo_id, token=...)`
  → falla rápido con mensaje claro en vez de a mitad de descarga.

## Resiliencia de descarga (44GB en red de DC)
- **Resume**: por defecto. Si se corta, vuelve a llamar `snapshot_download` → continúa archivos a medias
  (los `.incomplete` en caché se reanudan). No empieza de cero.
- **Reintentos**: envuélvelo en retry con backoff; cortes 5xx/timeout de HF son normales en archivos enormes.
```python
for i in range(5):
    try: path = snapshot_download(...); break
    except (HfHubHTTPError, ConnectionError):
        if i == 4: raise
        time.sleep(2 ** i)   # 1,2,4,8,16s
```
- **`hf_xet`** mejora cortes: dedup por chunk, re-baja solo los chunks faltantes (no el archivo entero).
- **Mirrors/espejos**: `HF_ENDPOINT=https://hf-mirror.com` (u otro espejo) si HF está bloqueado/lento en
  tu región. Mismo API, otro host. Útil para datacenters con egress restringido a HF.

## Verificar integridad
- HF guarda hashes; el caché valida **etag/sha** al bajar. Tras `snapshot_download`, comprueba que los
  archivos esperados existen y pesan lo previsto antes de cargar a VRAM (un `.safetensors` truncado
  revienta el load con error críptico).
- Para pesos críticos: compara el SHA del blob contra el del Hub
  (`HfApi().model_info(repo_id, revision, files_metadata=True)` trae `lfs.sha256` por archivo).
- `safetensors` es preferible a `pickle/.bin`: load más rápido y **sin ejecución de código** (seguridad).

## Pre-poblar el volumen (matar el cold start de descarga)
- **Una vez**: arranca un Pod normal que monte el Network Volume, exporta los envs, corre el
  `snapshot_download` al volumen, apaga el Pod. El endpoint serverless ya encuentra los pesos.
```bash
export HF_HOME=/runpod-volume/hf
export HUGGINGFACE_HUB_CACHE=/runpod-volume/hf/hub
export HF_TOKEN=hf_xxx
hf download meituan-longcat/LongCat-Video-Avatar --revision <sha> \
  --cache-dir /runpod-volume/hf/hub
```
- Apunta el worker al mismo caché con esos envs → los arranques solo **leen** del volumen.
  Cruza con [[113-network-volume-modelos-grandes]] y [[130-cold-start-optimizacion-profundo]].
- **Concurrencia de escritura**: si varios workers fríos pre-pueblan a la vez, carreras en el caché →
  pre-puebla **una sola vez** con el Pod temporal, no dejes que los workers lo bajen en paralelo.

## Hornear en la imagen vs volumen
- **Hornear** (`hf download` en el Dockerfile): cero descarga en runtime, pero imagen de decenas de GB
  (pull lento, build caro, registry caro). Bueno si el modelo es pequeño/estable.
- **Volumen**: imagen ligera (solo deps), pesos en volumen. Mejor para modelos enormes que cambian poco.
- **Híbrido**: deps + código en imagen; pesos en volumen pre-poblado. Lo más flexible (recomendado).

Cruza con [[113-network-volume-modelos-grandes]], [[18-model-registry-versionado]] y
[[130-cold-start-optimizacion-profundo]].
