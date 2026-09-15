# 149 · FLUX self-hosted a fondo (dev vs schnell vs Kontext, cuantización, LoRA, VRAM)

> FLUX.1 es el SOTA open de imagen en 2026: calidad tipo Midjourney, pero pesa 12B params y muerde VRAM.
> Servirlo barato = elegir la variante correcta + cuantizar bien. La licencia de [dev] es la trampa legal.

## Las tres variantes (Black Forest Labs)
| Variante | Params | Licencia | Pasos | CFG/guidance | Uso |
|---|---|---|---|---|---|
| FLUX.1 **schnell** | 12B | **Apache 2.0** (comercial libre) | 4 | 1.0 (sin CFG real) | producción barata, destilada |
| FLUX.1 **dev** | 12B | **Non-Commercial** (BFL) | 20-50 | 3.5 (guidance distilled) | máxima calidad, NO comercial sin licencia |
| FLUX.1 **Kontext [dev]** | 12B | **Non-Commercial** (BFL) | 20-28 | ~2.5-4 | **edición** in-context (imagen+texto→imagen) |

**Licencia [dev]/[Kontext dev]**: la FLUX.1 [dev] Non-Commercial License prohíbe uso comercial de los pesos
y de los outputs en producción comercial. Para vender outputs necesitas licencia comercial de BFL (self-serve
mensual) o usar **schnell** (Apache 2.0, libre). No te saltes esto: es el error legal #1. [verificado HF/BFL]

## VRAM por variante (transformer + T5-XXL + CLIP + VAE)
| Precisión | Tamaño transformer | VRAM práctica | GPU mínima |
|---|---|---|---|
| bf16/fp16 | ~24 GB | ~24-32 GB | A100/H100, justo en 4090/3090 24GB con offload |
| **fp8** (e4m3) | ~12 GB | ~16 GB | 4090/L40/A100 (FP8 tensor cores en Ada+) |
| **nf4** (bnb 4-bit) | ~7-8 GB | ~10-12 GB | 3060 12GB / 4070 |
| **SVDQuant int4** (Nunchaku, no-Blackwell) | ~6-7 GB | ~10 GB | Ampere/Ada |
| **SVDQuant fp4** (Nunchaku, Blackwell) | ~7 GB | ~8 GB | RTX 50 / B200 (FP4 tensor cores) |

T5-XXL (text encoder, ~9.5GB fp16) domina la huella → cuantizarlo a fp8/int8 libera mucho. Con
`enable_model_cpu_offload()` cabe en 16GB a costa de latencia (swaps CPU↔GPU). Cruza con [[128-cuantizacion-difusion-fp8-svdquant-gguf]].

## Cuantización: qué usar
- **fp8 (diffusers/ComfyUI)**: simple, ~equicalidad, ~1.0-1.2x vel sin compile; con `torch.compile` + fp8 → **~3.3x en H100**. Default sensato para A100/L40/4090.
- **SVDQuant 4-bit (Nunchaku)**: MIT-HAN-Lab, absorbe outliers con low-rank → calidad casi-fp16 a **int4/fp4**. El más rápido y ligero. Modelos: `svdq-int4_r32-flux.1-{dev,kontext-dev}` (Ampere/Ada), `svdq-fp4_r32-*` (Blackwell). Requiere kernels Nunchaku (no diffusers puro). [verificado HF nunchaku-tech]
- **nf4 (bitsandbytes)**: más universal pero menos preciso que SVDQuant; bueno para 12GB.
- **GGUF (city96)**: para llama.cpp-style offload; útil en VRAM muy baja, lento.

## LoRA stacking
- FLUX usa LoRA sobre el transformer (rank 16-64 típico). Diffusers: `pipe.load_lora_weights(repo, adapter_name="a")`, varios adapters + `pipe.set_adapters(["a","b"], adapter_weights=[0.8,0.6])`.
- **Fusión para servir**: `pipe.fuse_lora()` hornea el LoRA en pesos → elimina overhead por-paso (clave en producción). Para hot-swap por request, NO fusiones: usa `set_adapters` y `unload_lora_weights` entre jobs.
- LoRA + **fp8 + torch.compile**: posible pero recompila al cambiar de adapter si cambia el grafo → fusiona o agrupa requests por LoRA.
- Kontext acepta LoRA de edición/estilo; combina LoRA de personaje + instrucción de edición.

## Schedulers / sampling
- **dev**: `FlowMatchEulerDiscreteScheduler` (flow matching nativo), 20-28 pasos buen punto, 50 para máximo. `guidance_scale=3.5` (es guidance destilada, no CFG clásico → no dobla el cómputo).
- **schnell**: Euler simple, **4 pasos**, `guidance_scale=1.0` (NO subir CFG, está destilado).
- Sigmas: usar shift/`use_dynamic_shifting` mejora detalle a alta resolución (1536px+).

## Velocidad (1024×1024, referencia)
| GPU | dev 28-50 pasos | schnell 4 pasos |
|---|---|---|
| H100 (fp8+compile) | ~3-6 s | <1 s |
| A100 80GB (fp8) | ~8-12 s | ~1.5 s |
| 4090 (fp8) | ~12-18 s | ~2-3 s |
| 3090 (fp16, 50p) | ~30-60 s | ~2-4 s |
[cifras aprox., varían con resolución/encoders — verificado órdenes de magnitud HF/jarvislabs]

## Kontext para edición (i2i instruccional)
- **Caso**: cambiar fondo, ropa, estilo, texto en cartel, consistencia de personaje — sin ControlNet ni inpaint manual. Recibe imagen + prompt de instrucción ("cambia la camisa a roja").
- Encadenable: salida → entrada para ediciones iterativas (cuidado con degradación tras muchas pasadas).
- Para edición fina con máscara o pose, sigue valiendo ControlNet/inpaint clásico. Cruza con [[60-edicion-imagen-avanzada-ia]].

## Serving en producción
- **ComfyUI** (API mode) o **diffusers + LitServe/FastAPI**. Hornea pesos en volumen de red (FLUX dev fp16 ≈ 24GB + T5) — cruza con [[113-network-volume-modelos-grandes]].
- Warm-state: carga pipe una vez, `fuse_lora`, `torch.compile(transformer)` en el primer request (warmup falso al boot).
- Elegir variante por licencia ANTES que por calidad si vendes outputs → schnell o licencia BFL.

Cruza con [[02-open-models-catalog-2026]] y [[127-torch-compile-tensorrt-difusion]].
