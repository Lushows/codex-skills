# 224 · TensorRT-LLM para VLM (engine compilado, fp8, latencia mínima)

> Cuando vLLM/SGLang ([[222-vllm-multimodal-vlm]], [[223-sglang-lmdeploy-serving]]) ya no bajan la
> latencia, compilas. TensorRT-LLM da el suelo de latencia más bajo — a cambio de un build rígido.

## Qué te compra y qué te cobra
TensorRT-LLM compila el modelo a un **engine TensorRT** específico de GPU + dtype + shapes. Resultado:
kernels fusionados, fp8 nativo (Hopper/H200, Blackwell), in-flight batching, la menor latencia de la
categoría. El coste: el engine es **frágil** — atado a la arquitectura de GPU, a rangos de shape y a
la versión. Cambias de GPU o de versión → recompilas. Filosofía gemela de [[127-torch-compile-tensorrt-difusion]]
para difusión: compilar paga si el modelo y el hardware quedan fijos.

## El VLM se compila en DOS partes
Un VLM = **vision encoder (ViT)** + **LLM**. TensorRT-LLM los trata por separado:
1. **VisualBuilder** → engine TensorRT optimizado para el vision transformer (encoder de imagen).
2. **LLM engine** → el decoder con in-flight batching.
En runtime, el encoder produce embeddings visuales que se inyectan al LLM. Si solo compilas el LLM y
dejas el encoder en PyTorch, el encoder se vuelve tu cuello de botella de latencia.

## Flujo de build (esquema)

```bash
# 1) (opcional pero recomendado) calibrar fp8 con TensorRT Model Optimizer
#    PTQ: pasa un dataset pequeño para computar scales de activación → reduce engine 40-50%
# 2) exportar componentes a ONNX (dtype: fp16 | fp8 | int4) — LLM y visual por separado
# 3) construir engines
trtllm-build --checkpoint_dir ./ckpt_llm   --output_dir ./engine_llm \
  --gemm_plugin fp8 --max_batch_size 16 --max_input_len 32768
#    + build del visual encoder engine vía VisualBuilder
# 4) servir
trtllm-serve ./engine_llm --tokenizer Qwen/Qwen3-VL-8B-Instruct
```

## fp8 PTQ: el camino de producción
fp8 es el default productivo en H200. La calibración (PTQ) corre un dataset pequeño para fijar las
escalas de activación → inferencia fp8 precisa y engine 40-50% más chico. Mejoras 2026 relevantes:
add-norm-FP8 fusionado, prefill multimodal troceado no-contiguo, mejor serving de visión. Para VLM,
calibra **con imágenes representativas**, no solo texto — las activaciones del path visual difieren.

## Cuándo vale (y cuándo NO)

| Situación | ¿TensorRT-LLM? |
|---|---|
| Latencia p99 crítica, GPU y modelo fijos meses | Sí — el suelo de latencia más bajo |
| Volumen altísimo y estable en H100/H200/Blackwell | Sí — fp8 nativo + in-flight batching |
| Iteras modelos/GPUs cada semana | No — recompilar mata la velocidad de iteración |
| VLM recién salido | Probablemente no — soporte llega tarde; usa vLLM primero |
| Solo throughput batch offline | Marginal — vLLM/SGLang ya saturan y son más flexibles |

## Gotchas
1. **El encoder olvidado**: compilar solo el LLM deja el ViT en eager → la latencia que ganaste se
   la come el preprocesado de imagen. Compila ambos.
2. **Engine atado al hardware**: build en A100 no corre en H100; fp8 exige Hopper+. Planifica el
   build por GPU de destino, no de desarrollo.
3. **Rangos de shape rígidos**: `max_input_len`/`max_batch_size` se hornean; pasarte en runtime falla.
   Los tokens visuales cuentan dentro del input — dimensiónalos como en [[222-vllm-multimodal-vlm]].
4. **Calibración fp8 mala = calidad caída**: dataset de calibración no representativo desplaza las
   escalas; valida OCR/VQA tras cuantizar antes de confiar.
5. **Build lento y versionado**: el engine no es portable entre versiones de TRT-LLM; clava versiones
   en tu Dockerfile o recompilarás sin querer.

Cruza con [[127-torch-compile-tensorrt-difusion]] y [[222-vllm-multimodal-vlm]].
