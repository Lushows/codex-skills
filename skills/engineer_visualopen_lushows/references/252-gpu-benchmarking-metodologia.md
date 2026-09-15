# 252 · Metodología de benchmarking GPU/modelo (medir sin engañarte)

> Un número de throughput sin warmup, sin percentiles y sin fijar la entrada es ruido caro.
> Benchmark = protocolo repetible que separa cold-start, carga, prefill y decode — y reporta colas, no promedios.

## Las trampas que invalidan el número
- **Sin warmup**: la primera N corridas pagan compilación JIT (torch.compile, CUDA graphs, autotune cuDNN), alloc de caché y carga lazy de kernels → 2-10× más lentas. Descarta 3-5 iteraciones antes de medir.
- **Reloj mal medido**: GPU es asíncrona. `time.time()` mide el *encolado*, no la ejecución. Usa `torch.cuda.synchronize()` antes de parar el cronómetro, o `torch.cuda.Event(enable_timing=True)` (precisión µs).
- **Promedio que miente**: la media esconde colas. Reporta **p50/p90/p99**. MLPerf Inference v5.x fija umbrales en p99 (ej. Llama 3.1 405B: TTFT p99 ≤ 6s, TPOT p99 ≤ 175ms) — no en media. [no verificado el número exacto por versión]
- **Entrada variable**: en LLM el largo de in/out domina el tiempo. Fija prompt y `max_new_tokens`, o reporta **tokens/s normalizado**, no req/s.

## Qué medir, por modalidad
| Modalidad | Métrica primaria | Secundarias |
|---|---|---|
| LLM | tokens/s (decode) | TTFT, TPOT, p99 latencia |
| Difusión imagen | img/s (o s/img) | s a primer denoise, VRAM peak |
| Video/avatar | s de cómputo / s de video (RTF) | s/frame, VRAM peak, OOM rate |
| Embeddings | vectores/s | latencia batch, throughput saturado |

## Protocolo repetible
1. **Fija el entorno**: imagen Docker, versión torch/CUDA, GPU exacta (A100-SXM4-80GB ≠ A100-PCIe-40GB), `nvidia-smi --lock-gpu-clocks` para matar el boost variable, potencia (TDP) constante.
2. **Warmup**: 5 iters descartadas (cubren compile + autotune + alloc del pool).
3. **Mide N≥30** con misma entrada → reporta p50/p90/p99 + desviación. Si CV > 5%, algo no está fijo (clocks, thermal throttle, vecino ruidoso en cloud compartido).
4. **Separa fases**: cold-start (pull + carga a VRAM), prefill (prompt), decode (generación). El cold-start NO va en el tokens/s del modelo — va en el modelo de costo ([[30-finops-gpu]]).
5. **Repite en otra corrida del pod**: la varianza host-a-host en marketplace (Vast.ai) es real; un solo host no es la GPU "promedio".

## Sweep de batch y secuencia
Mide tokens/s vs batch size 1,2,4,8,16,32 hasta saturar la GPU o OOM. La curva revela el punto de máximo throughput por $ — clave para el dynamic batching ([[145-batch-dynamic-batching-difusion]]). Reporta también VRAM peak por punto: el throughput máximo que OOMea en producción es inútil.

## Reportar para que sea accionable
- Tabla: GPU · modelo · quant · batch · p50/p99 tokens(img)/s · VRAM peak · $/1k unidades.
- Deriva **$/unidad** = `$/seg_GPU ÷ throughput_saturado` — eso conecta con capacity planning ([[19-load-testing-capacity-planning]]) y con la decisión self-host vs API ([[255-tco-selfhost-vs-api]]).

## Gotchas
1. Thermal throttle en corridas largas baja clocks → segundo benchmark más lento que el primero (al revés del warmup). Lock clocks o ventila.
2. `torch.compile` cachea por shape: una entrada de shape nuevo recompila mid-run y mete un outlier en p99.
3. Medir con `nvidia-smi` el "GPU-Util %" no es throughput — un kernel ineficiente puede marcar 100% util y rendir poco.

**Fuentes:** mlcommons.org/2025/04/llm-inference-v5 · mlcommons.org/2025/09/small-llm-inference-5-1 · phillippe.siclait.com/blog/llm-benchmarking-from-scratch.

Cruza con [[19-load-testing-capacity-planning]], [[30-finops-gpu]] y [[256-throughput-optimization-checklist]].
