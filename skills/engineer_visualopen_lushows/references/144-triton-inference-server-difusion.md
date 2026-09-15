# 144 · Triton Inference Server para difusión y ensembles

> Triton orquesta el pipeline de difusión (text-enc → DiT/UNet → VAE) como un solo "modelo ensemble" servido en C++, con dynamic batching e instance groups por etapa.
> Vale la pena cuando quieres throughput máximo y control fino; es overkill si solo corres un modelo con un worker propio.

## Cuándo Triton vs worker propio
| Señal | Elige |
|---|---|
| 1 modelo, 1 GPU, baja concurrencia, iteración rápida | Worker propio (FastAPI/handler) o ComfyUI [[143-comfyui-custom-nodes-api-produccion]] |
| Pipeline multi-etapa con backends mixtos (TRT+Python+ONNX) | Triton ensemble |
| Necesitas dynamic batching nativo C++, métricas Prometheus, A/B de versiones | Triton |
| Modelo cambia cada semana, prototipo | Worker propio (Triton tiene fricción de empaquetado) |

Triton brilla cuando el text encoder está en TensorRT, el sampler en backend Python custom y el VAE en ONNX — y los pega sin que tú escribas el pegamento de transferencia de tensores.

## Model repository (layout en disco)
```
model_repo/
  text_encoder/   config.pbtxt  1/model.plan      # TensorRT
  denoiser/       config.pbtxt  1/model.py        # python backend (loop de sampling)
  vae_decoder/    config.pbtxt  1/model.onnx      # ONNX runtime
  sd_pipeline/    config.pbtxt  1/               # ensemble (dir de versión vacío)
```
Triton elige backend por la extensión del artefacto: `.plan`→tensorrt, `.onnx`→onnxruntime, `model.py`→python, `model.pt`→pytorch (libtorch).

## Ensemble: pegar las etapas (config.pbtxt)
El ensemble no tiene pesos; enruta tensores por nombre entre steps:
```
name: "sd_pipeline"
platform: "ensemble"
max_batch_size: 8
input  [ { name: "PROMPT"  data_type: TYPE_STRING dims: [1] } ]
output [ { name: "IMAGE"   data_type: TYPE_FP16   dims: [3,1024,1024] } ]
ensemble_scheduling { step [
  { model_name: "text_encoder" model_version: -1
    input_map  { key: "TEXT"      value: "PROMPT" }
    output_map { key: "EMBED"     value: "cond_embed" } },
  { model_name: "denoiser" model_version: -1
    input_map  { key: "COND"      value: "cond_embed" }
    output_map { key: "LATENT"    value: "denoised_latent" } },
  { model_name: "vae_decoder" model_version: -1
    input_map  { key: "LATENT"    value: "denoised_latent" }
    output_map { key: "IMG"       value: "IMAGE" } }
] }
```
`model_version: -1` = última. Los `value` son tensores intermedios del scheduler; los `key` son los nombres de I/O reales de cada sub-modelo. Un typo en el mapeo = error silencioso de "tensor not found".

## Backends por etapa
- **TensorRT** (`.plan`): text encoder, VAE → máxima velocidad, pero motor fijado a shape/precisión (rebuild si cambias resolución). Cruza con [[127-torch-compile-tensorrt-difusion]].
- **Python backend** (`model.py` con clase `TritonPythonModel.execute(requests)`): el denoiser/sampler — el loop de pasos vive aquí, mantienes el modelo en VRAM en `initialize()`. Es donde metes el scheduler (DPM++, Euler) y CFG.
- **ONNX/libtorch**: piezas que ya tienes exportadas sin esfuerzo TRT.

## Dynamic batching e instance groups
```
max_batch_size: 8
dynamic_batching {
  preferred_batch_size: [ 2, 4 ]
  max_queue_delay_microseconds: 50000   # espera hasta 50ms para llenar batch
}
instance_group [ { count: 2  kind: KIND_GPU  gpus: [0] } ]
```
- `max_batch_size` 0 desactiva batching (modelo full-batch fijo).
- `preferred_batch_size`: tamaños que Triton intenta formar; ponlos a potencias que tu motor TRT soporte.
- `max_queue_delay_microseconds`: la palanca latencia↔throughput (más delay = batches más llenos = más throughput, peor p99).
- `instance_group count: N` = N copias del modelo concurrentes en la GPU (sube utilización si una sola no satura; cuidado VRAM × N). Para difusión, el denoiser suele querer `count:1` (ya es pesado) y el VAE/encoder `count:2`.
- El batching real para difusión se complica por CFG y resolución → ver [[145-batch-dynamic-batching-difusion]].

## Métricas y observabilidad
Triton expone Prometheus en `:8002/metrics`: `nv_inference_request_duration_us`, `nv_inference_queue_duration_us` (tiempo esperando batch — si crece, sube `count` o baja delay), `nv_gpu_utilization`, `nv_inference_count`. Úsalas para tunear delay/instances en vez de adivinar. Cruza con [[19-load-testing-capacity-planning]].

## Gotchas
- STRING como input (prompts) → `TYPE_STRING`, llega como bytes; decodifica en el python backend.
- El ensemble batchea **por step**: si el denoiser no soporta batch variable, fíjalo y deja el batching en encoder/VAE.
- `model.py` que carga el modelo en cada `execute()` = desastre; cárgalo UNA vez en `initialize()`.
- Versionar: carpetas `1/`, `2/`… + `version_policy` para canary/rollback sin downtime.
- Empaquetar deps Python del backend: usa `EXECUTION_ENV_PATH` (conda-pack) o imagen custom; el contenedor base de Triton trae versiones fijas de torch que pueden chocar con tu modelo.

Cruza con [[127-torch-compile-tensorrt-difusion]] y [[145-batch-dynamic-batching-difusion]].
