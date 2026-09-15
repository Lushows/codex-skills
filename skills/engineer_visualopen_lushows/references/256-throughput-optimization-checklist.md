# 256 · Checklist de optimización de throughput (orden de mayor ROI)

> El throughput se gana en capas: batch primero, IO al final. Optimizar en el orden equivocado pierde semanas.
> Mide después de cada palanca ([[252-gpu-benchmarking-metodologia]]) — la mejora teórica miente; la p99 medida no.

## Orden de ataque (mayor ganancia/esfuerzo primero)
1. **Batching / dynamic batching** — la palanca #1. Una GPU procesando batch 1 desperdicia >80% del SM. Agrupa requests en vuelo ([[145-batch-dynamic-batching-difusion]], [[14-batching-kvcache-throughput]] para LLM). Ganancia típica: 3-10×.
2. **Mantener el modelo residente** — carga 1 vez al arranque del proceso, no por request. Mata el cold-start por-request ([[30-finops-gpu]]).
3. **torch.compile / CUDA graphs** — fusiona kernels, elimina overhead de launch. Ganancia 1.3-2×. Cuidado: recompila por shape nuevo → fija shapes o usa `dynamic=True`.
4. **Cuantización** — fp8/int8/AWQ/GGUF reduce VRAM y a veces sube throughput (menos ancho de banda de memoria). Permite batch más grande o GPU más chica ([[12-cuantizacion-hands-on]]). Valida calidad con evals, no asumas.
5. **Right-sizing de GPU** — el modelo que cabe en 24GB (L4/A10) no debe correr en H100. Cuantiza para bajar de clase ([[30-finops-gpu]]).
6. **Offloading inteligente** — solo si OOM. CPU/disk offload mata throughput; úsalo para *caber*, no para *acelerar* ([[125-diffusers-offloading-memoria]]). Prefiere cuantizar antes que offloadear.
7. **IO / pipeline** — pre/post-proceso en CPU paralelo al cómputo GPU, decode de imágenes async, evita stalls de transferencia H2D. Solapa con `cuda.Stream`. Última capa: solo importa cuando el cómputo ya no es el cuello.

## Palancas por modalidad
| Modalidad | Palanca específica |
|---|---|
| LLM | KV-cache, continuous batching (vLLM/SGLang), prefix caching |
| Difusión | fewer steps (distilled/turbo), batch de latentes, VAE tiling |
| Video/avatar | segmentar clip, reusar latentes entre frames, fp8 |
| Embeddings | batch grande, ONNX/TensorRT ([[11-tensorrt-onnx-compilacion-aot]]) |

## Diagnóstico: ¿dónde está el cuello?
- **GPU-Util alto pero throughput bajo** → kernel ineficiente o batch=1 (compute-bound mal usado). Aplica 1,3,4.
- **GPU-Util bajo y throughput bajo** → starving: el cuello es IO/CPU/data loading. Aplica 7.
- **OOM mid-run** → fragmentación o batch too big. Cuantiza (4) o reduce batch antes de offloadear (6).
- **p99 >> p50** → cold-start por request (2), recompilación por shape (3), o vecino ruidoso (cambia de host).
Usa profiler (Nsight, torch profiler, [[10-profiling-optimizacion-kernels]]) — no adivines la capa.

## Regla de oro
Cada palanca: **mide antes, aplica, mide después**. Si la p99 no mejoró, revierte — añadiste complejidad sin ganancia. El throughput "teórico" del paper no es tu throughput; tu benchmark repetible sí.

## Gotchas
1. Optimizar IO antes que batching: micro-optimizas el 5% mientras el 80% se desperdicia en batch 1.
2. torch.compile con shapes variables → recompila constante, peor que sin compilar.
3. Cuantizar sin eval de calidad → throughput sube, output degrada, nadie nota hasta producción.
4. Offload como atajo de velocidad: te deja correr pero a fracción del throughput; es para caber, no para correr rápido.
5. Batch enorme que maximiza tokens/s pero OOMea bajo carga real o mata la latencia interactiva.

**Fuentes:** mlcommons.org/2025/04/llm-inference-v5 · bentoml.com/llm/inference-optimization/llm-performance-benchmarks · docs de vLLM/SGLang.

Cruza con [[125-diffusers-offloading-memoria]], [[145-batch-dynamic-batching-difusion]] y [[252-gpu-benchmarking-metodologia]].
