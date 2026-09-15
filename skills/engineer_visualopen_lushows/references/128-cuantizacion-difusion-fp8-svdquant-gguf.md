# 128 · Cuantización de difusión: fp8, SVDQuant/Nunchaku, GGUF

> Un DiT de 13B en bf16 ocupa ~27GB solo de pesos. Cuantizar baja eso a 4-7GB
> sin tocar el resto del pipeline — la palanca #1 para meter video en una GPU chica.

## Qué se cuantiza (y qué NO)
El **DiT/transformer** es el grueso de los pesos y tolera bien cuantización → ataca eso primero.
El **VAE** y el **text/audio encoder** son chicos pero sensibles: cuantizarlos suele meter artefactos
(banding, color shift, lip-sync degradado). Regla: **DiT agresivo, VAE/encoder en fp16 o con cuidado.**
SVDQuant ya soporta text-encoder en 4-bit; el VAE casi siempre se deja en fp16.

## fp8 (e4m3 / e5m2) en el DiT
fp8 tiene dos layouts: **e4m3** (4 exp, 3 mantisa — más precisión, rango menor; default para pesos y
activaciones) y **e5m2** (5 exp, 2 mantisa — más rango, menos precisión; útil para gradientes).
- Casi-lossless en DiT, **~2x menos VRAM** que bf16, calidad visual ≈ idéntica.
- Acelera de verdad solo en **Ada (4090) / Hopper (H100) / Blackwell** con tensor cores fp8. En Ampere
  (A100/A6000) fp8 **no** tiene kernels nativos → solo ahorra memoria, no da speed.
- En diffusers: `torchao` con `quantize_(model, float8_weight_only())` o `float8_dynamic_activation_float8_weight()`. [no verificado: nombre exacto de la receta por versión de torchao]

## SVDQuant / Nunchaku (4-bit, bajo error) — la joya para FLUX y video
SVDQuant (ICLR 2025 spotlight, MIT Han Lab) hace **W4A4** absorbiendo los outliers en una rama
**low-rank** vía SVD, en vez de dejarlos romper la cuantización. **Nunchaku** es el motor de inferencia
que fusiona los kernels de la rama low-rank con los de 4-bit (sin acceso redundante a memoria).
- FLUX.1-dev 12B: **3.6x menos memoria** vs bf16; Nunchaku da **3.0x speedup** vs baseline NF4 W4A16.
- Con CPU-offload por capa + text-encoder 4-bit → FLUX corre en **~4 GiB**, manteniendo 2-3x speedup.
- Soporta SDXL, PixArt-Σ, FLUX.1; ecosistema creciente para modelos de video. La diferencia clave vs
  NF4 es **calidad**: NF4 a 4-bit degrada notablemente, SVDQuant no.

## GGUF para modelos de video (city96)
`ComfyUI-GGUF` (city96) trae el formato GGUF de llama.cpp a DiTs nativos de ComfyUI. Sirve para
**WAN, HunyuanVideo, FLUX**. Niveles: `Q8_0` (casi fp16), `Q6_K`, `Q5_K_M`, **`Q4_K_M`** (el sweet
spot calidad/VRAM), hasta `Q3_K`/`IQ4_XS` (agresivo, ya se nota).
- **Gotcha video**: WAN/Hunyuan usan **tensores 5D**. El conversor avisa, guarda un modelo no-funcional,
  y hay que correr `fix_5d_tensor.py` a mano para re-añadir la key faltante. Sin ese paso, no carga.
- GGUF carga la capa y la **deshace a fp16 al vuelo** para computar → ahorra VRAM de *pesos*, no de
  activaciones. Combínalo con tiling de VAE para el pico de decode.

## bitsandbytes / NF4 — por qué es LLM-first
bnb (NF4/INT8) nació para LLMs: NF4 asume una distribución de pesos tipo-normal y su dequant está
optimizada para matmuls de transformer de lenguaje. En difusión funciona pero **degrada más** que
SVDQuant al mismo bit-width, y sus kernels no explotan la estructura del DiT. Úsalo como fallback
rápido (`load_in_4bit`), no como destino de calidad.

## LongCat: el caso real
LongCat-Video-Avatar 1.5 (13.6B) trae **`--use_int8`** = carga el DiT INT8 → menos VRAM. Solo válido
con `--model_type avatar-v1.5`. Combinado con step-distillation (8 pasos) corre 480P/720P en GPU
media. Aun con INT8, Meituan recomienda GPU fuerte: INT8 ahorra memoria pero el cómputo sigue pesado.

## Tabla: técnica → bit / VRAM relativa / calidad / dónde acelera
| Técnica | Bits (W/A) | VRAM pesos vs bf16 | Calidad | Speedup real |
|---|---|---|---|---|
| bf16 (base) | 16/16 | 1.0x | ref | — |
| fp8 e4m3 (torchao) | 8/8 | ~0.5x | ≈ ref | Ada/Hopper/Blackwell |
| INT8 (bnb / `--use_int8`) | 8/16 | ~0.5x | muy buena | Ampere+ |
| GGUF Q8_0 | ~8 | ~0.5x | ≈ ref | sin speed (dequant al vuelo) |
| GGUF Q4_K_M | ~4.5 | ~0.28x | buena | sin speed |
| NF4 (bnb 4-bit) | 4/16 | ~0.28x | aceptable, degrada | poco |
| SVDQuant W4A4 (Nunchaku) | 4/4 | ~0.28x | casi-bf16 | 3x vs NF4 |

## Orden de decisión
1. ¿GPU Ada/Hopper? → **fp8** primero (gratis en calidad, acelera).
2. ¿VRAM apretada y modelo soportado? → **SVDQuant/Nunchaku** (mejor 4-bit).
3. ¿ComfyUI / video WAN-Hunyuan? → **GGUF Q4_K_M** + tiling VAE (cuidado tensores 5D).
4. ¿Solo necesitas que entre, sin obsesión de calidad? → **INT8/NF4 bnb**.
5. Nunca cuantices el VAE para producción salvo que midas el delta de calidad.

Cruza con [[12-cuantizacion-hands-on]], [[111-longcat-avatar-runpod-produccion]] y [[125-diffusers-offloading-memoria]].
