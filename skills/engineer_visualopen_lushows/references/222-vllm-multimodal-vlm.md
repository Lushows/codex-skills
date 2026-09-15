# 222 · vLLM para VLM/multimodal (imágenes en el prompt a throughput)

> Servir un VLM open (Qwen3-VL, InternVL3) no es servir un LLM con una imagen pegada:
> los tokens visuales inflan el KV-cache y el cold start carga DOS pesos (encoder + LLM).

## Qué cambia respecto a un LLM de texto
[[33-servir-tu-propio-llm]] cubre vLLM para texto. En multimodal, cada imagen se trocea en
**tokens visuales** (cientos a miles según resolución) que el encoder produce y se inyectan en la
secuencia. Eso significa: (1) el `max_model_len` se llena con visión, no solo texto; (2) el KV-cache
por request es mucho mayor → menos concurrencia; (3) hay un segundo modelo (el vision encoder, ver
[[35-vision-encoders-vlms]]) que también ocupa VRAM y tiempo de carga.

## Levantarlo

```bash
vllm serve Qwen/Qwen3-VL-8B-Instruct \
  --limit-mm-per-prompt.image 2 \
  --limit-mm-per-prompt.video 0 \
  --max-model-len 32768 \
  --gpu-memory-utilization 0.88 \
  --quantization fp8 \
  --mm-processor-cache-gb 8
```

Lo consumes con el cliente `openai` (API chat compatible), pasando la imagen como `image_url` en
base64 o URL — idéntico al snippet de [[35-vision-encoders-vlms]].

## Parámetros que solo existen (o muerden) en multimodal

| Flag | Qué hace | Por qué importa |
|---|---|---|
| `--limit-mm-per-prompt.image N` | tope de imágenes por prompt | reserva VRAM para perfilado; ponlo al máximo real, no más |
| `--limit-mm-per-prompt.video 0` | desactiva vídeo | vídeo reserva embeddings enormes; si solo procesas imágenes, libera ese KV-cache |
| `--limit-mm-per-prompt.image 0` (+video 0) | modo solo-texto | salta el vision encoder y su perfilado → más KV-cache si el modelo sirve también texto puro |
| `--mm-processor-cache-gb` | caché del preprocesado de imagen | evita re-tokenizar la misma imagen entre requests |
| `--max-model-len` | contexto total | aquí incluye los tokens visuales: una imagen alta-res puede valer 1-4k tokens |

## El número que predice tu OOM
VRAM ≈ pesos(LLM)+pesos(encoder) + KV-cache. El KV-cache por request crece con
**(tokens de texto + tokens visuales) × slots**. Una sola imagen 1280×1280 en Qwen3-VL puede
costar miles de tokens visuales → con `max_model_len` alto y varias imágenes por prompt, la
concurrencia colapsa. Palancas: baja la resolución de entrada, `--kv-cache-dtype fp8`, recorta
`max_model_len` a lo que el caso real necesita, fija `--limit-mm-per-prompt` ajustado.

## Cold start y storage
El VLM carga DOS conjuntos de pesos. En serverless, hornéalos o móntalos en Network Volume
([[113-network-volume-modelos-grandes]]) con `HF_HOME` apuntando al volumen — si no, cada frío
re-baja encoder + LLM. fp8 reduce pesos ~2× (Hopper/Ada), acelerando carga a VRAM además del throughput.

## Gotchas
1. **`max_model_len` razona en tokens TOTALES**: subestimar los visuales te llena el contexto y
   trunca el prompt de texto sin avisar.
2. **No olvides `--limit-mm-per-prompt.video 0`** si solo usas imágenes: por defecto vLLM reserva
   memoria para vídeo y te roba KV-cache.
3. **fp8 del LLM no cuantiza el encoder igual**: revisa que el vision tower no quede en fp16 comiéndose
   la VRAM que creías ahorrar.
4. **Resolución dinámica**: muchos VLMs reescalan según el contenido; un batch con imágenes grandes
   dispara picos de tokens visuales y OOM intermitente. Normaliza/limita resolución de entrada.
5. **El perfilado de arranque puede OOMear** aunque el runtime quepa: usa el límite mm real para que
   vLLM no reserve para el peor caso imaginario.

## Cuándo NO usar vLLM aquí
Para latencia mínima por request (no throughput) o Int4 agresivo en una sola GPU, mira
[[223-sglang-lmdeploy-serving]]. Para latencia extrema con engine compilado, [[224-tensorrt-llm-vlm]].

Cruza con [[33-servir-tu-propio-llm]], [[35-vision-encoders-vlms]] y [[113-network-volume-modelos-grandes]].
