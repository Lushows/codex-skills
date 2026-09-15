# 223 · SGLang y LMDeploy: cuándo NO usar vLLM para servir VLM

> vLLM es el default razonable, pero SGLang gana en prefix-heavy/multi-turn y LMDeploy
> aplasta en Int4 y TTFT bajo. Elegir motor es elegir tu cuello de botella.

## El panorama 2026
En H100 con Llama-3.1-8B, SGLang y LMDeploy rondan ~16.2k tok/s frente a ~12.5k de vLLM (≈29% más
throughput) [no verificado: cifras de un benchmark de blog, dependen de carga/versión]. No es que
vLLM sea malo: es que cada motor optimiza algo distinto. Para VLM (ver [[222-vllm-multimodal-vlm]])
los tres soportan los modelos principales con API OpenAI-compatible; la decisión es de patrón de carga.

## SGLang — RadixAttention
Caché de prefijos en **árbol radix**: más agresivo que el prefix-caching de vLLM cuando muchos
requests comparten prefijo (system prompt + few-shots + la misma imagen de contexto en varias
preguntas). Ventajas medidas:
- **Multi-turn**: en chats largos no recalcula la historia cada mensaje → +10-20% extra por cache hits.
- **Structured output**: decodifica varios tokens de golpe precomputando continuaciones válidas;
  JSON ~3× más rápido que generación libre (clave para [[226-structured-output-vision]]).
- **Scheduler zero-overhead** (v0.4+): overhead de scheduling CPU <2% del tiempo total.

```bash
python -m sglang.launch_server --model-path Qwen/Qwen3-VL-8B-Instruct \
  --tp 2 --mem-fraction-static 0.85 --chat-template qwen3-vl
```

Ideal para: agentes con muchos branches del mismo prompt visual, evaluación masiva con plantilla
fija, soporte conversacional con imágenes recurrentes.

## LMDeploy — TurboMind
Backend en **C++/CUDA puro**, sin overhead del intérprete Python. Fuerte donde vLLM flojea:
- **Int4 (AWQ)**: corre un 70B en una sola A100 80GB con ~2.4× speedup vs FP16 — la mejor ruta para
  meter un VLM grande en poca VRAM con buena velocidad.
- **TTFT más bajo** en casi todos los niveles de concurrencia → tiempo-real (<100ms al primer token).

```bash
lmdeploy serve api_server Qwen/Qwen3-VL-8B-Instruct \
  --backend turbomind --tp 2 --quant-policy 4 --cache-max-entry-count 0.85
```

Ideal para: VLM grande embutido en GPU modesta vía Int4, o UX interactiva donde el primer token
manda. Ojo: AWQ/Int4 degrada razonamiento (mismo aviso que [[33-servir-tu-propio-llm]]) — mídelo.

## Tabla de decisión

| Carga | Motor | Razón |
|---|---|---|
| Prefijo/imagen compartida, multi-turn, eval masiva | **SGLang** | RadixAttention reusa KV-cache |
| Int4 agresivo, VLM grande en 1 GPU | **LMDeploy** | TurboMind C++ + AWQ 2.4× |
| TTFT mínimo, tiempo-real interactivo | **LMDeploy** | menor latencia al primer token |
| Mayor ecosistema, features mm más frescas, default | **vLLM** | soporte de modelos nuevos primero |
| Latencia absoluta con engine compilado | TensorRT-LLM | ver [[224-tensorrt-llm-vlm]] |

## Gotchas
1. **El soporte de VLM nuevos llega antes a vLLM**: SGLang/LMDeploy pueden ir semanas detrás en un
   modelo recién salido. Verifica que tu VLM exacto esté soportado antes de comprometerte.
2. **Chat template del VLM**: cada motor espera su plantilla; una mal puesta rompe el formato
   de imagen y el modelo "no ve" nada. Usa la del repo del modelo.
3. **`mem-fraction-static` / `cache-max-entry-count`** son el equivalente a `gpu_memory_utilization`:
   muy alto → OOM con picos de tokens visuales (igual que [[222-vllm-multimodal-vlm]]).
4. **Benchmarks de blog mienten para tu caso**: las cifras de throughput se midieron en texto;
   con imágenes el cuello cambia. Mide con TU distribución de imágenes.

Cruza con [[222-vllm-multimodal-vlm]] y [[33-servir-tu-propio-llm]].
