# 14 — Batching, KV-cache y throughput

La estrategia depende del workload. **Static batching** espera a llenar un batch fijo — simple, pero
head-of-line blocking desperdicia GPU cuando las secuencias terminan a destiempo. **Dynamic batching**
(Triton) agrupa requests que llegan en una ventana. **Continuous (in-flight) batching** opera a nivel de
*iteración*: apenas una secuencia emite EOS, su slot se libera y un request en cola entra a mitad de vuelo —
el mayor unlock de throughput en serving de LLM.

## PagedAttention (vLLM)
El KV-cache es el cuello de memoria en decode de LLM. PagedAttention aplica paginación tipo OS: el KV-cache se
parte en bloques fijos (default 16 tokens), alocados on-demand en vez de reservar el contexto máx. Baja la
fragmentación/waste de ~60-80% a <4% → caben muchos más requests concurrentes. vLLM lo combina con continuous
batching como default de producción.

## RadixAttention (SGLang)
Extiende la paginación con un **radix tree** sobre el KV-cache para **reuso de prefijo** automático: requests que
comparten un prefijo (system prompt, few-shot, historia multi-turn) reusan el KV cacheado. En workloads
prefix-heavy (RAG, agentes, multi-turn) es un gran win — hasta ~6.4× en esas trazas, y ~29% más throughput que
vLLM en H100 en serving general.

## 🔴 Estos son SOLO para LLM
PagedAttention y RadixAttention manejan un *KV-cache autoregresivo* — diffusion y video NO tienen KV-cache
token-a-token → ninguno aplica. La inferencia de diffusion es típicamente **batch=1** por request: una sola
imagen/video ya satura la GPU (todo el latente se procesa en cada step de denoise), no hay capacidad idle para
batchear, y la latencia importa más que el packing.

## Subir throughput de diffusion/video (otros levers)
- **Más workers paralelos** (uno por GPU) detrás de una cola para throughput agregado.
- **Sequence/context parallel** (xDiT Ulysses+Ring) para bajar la latencia de UN request entre GPUs.
- **Menos pasos de denoise** (destilación, LCM/Turbo, mejores schedulers).
- Cuantización + `torch.compile`. Caché de cómputo reusable (block/step caches).
- Batching real solo ayuda cuando muchos requests *chicos* comparten una GPU con VRAM de sobra — raro en video high-res.
- **Micro-batching** parte un batch grande en chunks para caber/overlap. **Request coalescing en el gateway**
  fusiona requests idénticos/prefix-sharing in-flight → computa 1 vez y fan-out.

## Latencia vs throughput
Batches más grandes + continuous batching suben tokens/seg PERO suben la cola de latencia. Tunea `max_num_seqs`/
`max_num_batched_tokens` (vLLM) a tu SLA: chat interactivo = batches chicos/menor latencia; bulk offline = batches grandes.

## Gotchas
1. NO esperes que PagedAttention/RadixAttention ayuden a diffusion/video — no hay KV-cache que paginar.
2. Continuous batching sube throughput pero empeora p99 bajo carga — capa el batch en endpoints latencia-SLA.
3. Para diffusion "solo batchéalo" suele fallar: batch>1 OOMea en video high-res y no ayuda si un ítem ya satura.
4. El prefix caching solo paga con prefijos *realmente* compartidos; tráfico de prompts únicos ve poco beneficio + overhead del árbol.
5. El coalescing del gateway debe respetar sampling params/seeds por request — coalescear con sampling distinto corrompe outputs.

**Fuentes:** runpod.io/articles (vLLM PagedAttention) · particula.tech/blog (SGLang vs vLLM 2026) · cs.cmu.edu/~zhihaoj2 (LLM-serving slides).
