# Servir tu Propio LLM: vLLM y SGLang (2026)

## ¿Self-host o API?

Self-host gana cuando: (1) volumen alto y sostenido (>10-50M tokens/día) donde el coste por token de una GPU amortizada bate a la API; (2) datos sensibles que no pueden salir; (3) necesitas un modelo fine-tuned o un open específico; (4) latencia controlada/predecible. La API (Claude, GPT) gana en volumen bajo/variable, time-to-market y cuando necesitas el modelo más capaz. Regla práctica 2026: por debajo de ~1 GPU saturada de tráfico, la API casi siempre es más barata que pagar una H100 24/7.

## vLLM a fondo

vLLM es el motor de inferencia estándar (PagedAttention + continuous batching). Servidor compatible con OpenAI:

```bash
pip install vllm  # 2026: v0.20.x+
vllm serve Qwen/Qwen3-32B \
  --tensor-parallel-size 2 \
  --gpu-memory-utilization 0.90 \
  --max-model-len 32768 \
  --quantization fp8 \
  --enable-prefix-caching
```

Lo consumes con el cliente `openai` apuntando a `http://localhost:8000/v1`.

### Parámetros clave

- **`tensor_parallel_size`**: nº de GPUs para partir el modelo (un 70B no cabe en 1×A100 80GB en fp16 → usa 2-4). Debe dividir nº de attention heads.
- **`gpu_memory_utilization`** (0-1): fracción de VRAM para pesos + KV-cache. 0.90 default; bájalo si compartes la GPU, súbelo para más KV-cache (más concurrencia).
- **`max_model_len`**: contexto máximo. Más largo = KV-cache más grande por request = menos requests concurrentes. No lo pongas más alto de lo que necesitas.
- **`quantization`**: `fp8` (Hopper/Ada, ~2× throughput vs fp16, calidad casi intacta), `awq`/`gptq` (4-bit, para meter modelos grandes en poca VRAM, algo más de pérdida), `nvfp4`/`mxfp4` (Blackwell). En 2026 fp8 es el default recomendado en H100/H200.

### Speculative decoding

Un draft model pequeño propone tokens que el modelo grande verifica en paralelo. 1.3-2× speedup si la tasa de aceptación ≥0.7. Métodos en vLLM: n-gram, EAGLE, draft model.

```bash
vllm serve meta-llama/Llama-3.3-70B-Instruct \
  --speculative-config '{"method":"eagle","num_speculative_tokens":5}'
```

### Prefix caching

`--enable-prefix-caching` reutiliza el KV-cache de prefijos compartidos (system prompt, few-shots) entre requests → enorme ahorro en cargas con prompt común. Es el equivalente self-host del prompt caching de API.

### Multi-LoRA serving

Sirve varios adaptadores LoRA sobre una misma base, casi sin VRAM extra:

```bash
vllm serve meta-llama/Llama-3.1-8B \
  --enable-lora --max-loras 8 --max-lora-rank 64
```

Cada request selecciona su LoRA por nombre → multi-tenant fine-tuned barato.

## SGLang

Motor alternativo optimizado para cargas **prefix-heavy** y programas estructurados, con **RadixAttention** (caché de prefijos en árbol radix, más agresivo que vLLM en árboles de prompts compartidos). Ideal para: agentes con muchos branches del mismo prompt, few-shot pesado, evaluación masiva.

```bash
python -m sglang.launch_server --model-path Qwen/Qwen3-32B \
  --tp 2 --mem-fraction-static 0.9
```

## Structured / guided output

Decodificación restringida garantiza JSON válido sin reintentos:
- **xgrammar** (default en vLLM 2026, el más rápido): gramáticas/JSON schema con overhead mínimo.
- **outlines**: JSON schema, regex, gramáticas EBNF.

```bash
# vLLM, en la request:
{"guided_json": {"type":"object","properties":{"sentiment":{"enum":["pos","neg"]}}}}
```

## KV-cache sizing y continuous batching

El KV-cache domina la VRAM tras los pesos. Tamaño ≈ `2 × n_layers × n_kv_heads × head_dim × seq_len × batch × dtype_bytes`. Modelos con **GQA** (Llama 3/4, Qwen3) reducen `n_kv_heads` → cabe más batch. Para más throughput: sube `gpu_memory_utilization`, baja `max_model_len`, usa fp8 KV-cache (`--kv-cache-dtype fp8`). Continuous batching ya está activo por default; tunéalo con `--max-num-seqs` (concurrencia) y `--max-num-batched-tokens`.

## Modelos open 2026

- **Qwen3 / Qwen3.5** (Alibaba, Apache 2.0): MoE + dense, contexto ultralargo, fuerte en código/agentic. Caballo de batalla open por defecto.
- **DeepSeek-V4** (V4-Pro 1.6T/49B activos, V4-Flash 284B/13B): razonamiento largo y coste/token bajísimo.
- **Llama 4** (Meta): Scout (17B activos/109B) y Maverick (17B/400B), MoE multimodal.
- **Mistral 3 / Small 4** (Apache 2.0): densos 3B/8B/14B + Large 3 MoE; Small 4 unifica visión+razonamiento+coding.
- **gpt-oss** (OpenAI, Apache 2.0): 20B y 120B, reasoning effort configurable, entrenado para tool-use. Excelente relación calidad/licencia.

## Coste vs API

Una H100 (~$2-3/h cloud) sirviendo Qwen3-32B fp8 con buen batching produce tokens a una fracción del precio de GPT/Claude SI la mantienes saturada. Mal utilizada (tráfico bajo, GPU ociosa), sale más cara que la API. El break-even depende casi enteramente de la **utilización**, no del modelo.

## Gotchas

1. **`max_model_len` alto te mata la concurrencia**: cada slot reserva KV-cache para el contexto máximo; 128k de contexto = poquísimos requests simultáneos.
2. **AWQ/GPTQ degradan razonamiento**: el 4-bit ahorra VRAM pero penaliza tareas de razonamiento; mide antes de usarlo en producción. Prefiere fp8 si la VRAM da.
3. **tensor_parallel debe dividir los heads**: TP=3 en un modelo con 32 heads falla; usa potencias divisoras (1,2,4,8).
4. **OOM al arrancar ≠ OOM en runtime**: `gpu_memory_utilization` muy alto deja sin margen para picos de KV-cache y crashea con tráfico real; deja 5-10% de holgura.
5. **Speculative decoding puede ENLENTECER**: si la aceptación del draft es <0.5, verificar tokens rechazados cuesta más que generarlos; mídela y desactívalo si no rinde.

## Fuentes
- [vLLM docs](https://docs.vllm.ai/en/latest/)
- [vLLM speculative decoding](https://docs.vllm.ai/en/latest/features/speculative_decoding/)
- [vLLM production deployment 2026 (Spheron)](https://www.spheron.network/blog/vllm-production-deployment-2026/)
- [SGLang docs](https://docs.sglang.ai/)
- [DeepSeek V4 vs Llama 4 vs Qwen3 2026 (Spheron)](https://www.spheron.network/blog/deepseek-vs-llama-4-vs-qwen3/)
- [Best open-source LLMs 2026 (Hugging Face)](https://huggingface.co/blog/daya-shankar/open-source-llms)
