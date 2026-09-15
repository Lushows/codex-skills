# 08 — Upscaling y restauración de imagen/cara (2026)

> El pipeline canónico de costo (SKILL §6.25): **genera 480p barato → upscale a 1080p**. Esta ref cubre
> los upscalers, la restauración de cara, y cómo no reventar la VRAM con imágenes grandes.

## Real-ESRGAN (el caballo de batalla)

- **Repo** `xinntao/Real-ESRGAN`. GAN-based, rápido, sin alucinar mucho. Factores **2× / 4×**.
- **Modelos:** `RealESRGAN_x4plus` (realista general), `RealESRGAN_x4plus_anime_6B` (**anime/ilustración**,
  más liviano), `realesr-animevideov3` (video anime), `realesr-general-x4v3` (general + denoise ajustable).
- **CLI:**
  ```bash
  python inference_realesrgan.py -n RealESRGAN_x4plus -i in/ -o out/ --outscale 4 --tile 512 \
         --face_enhance        # invoca GFPGAN para caras
  ```
- **`--tile`** parte la imagen para no OOM (ver tiled abajo). `--fp32` si hay artefactos en fp16.
- **Limitación:** es un upscaler "fiel", NO inventa detalle nuevo. Para realismo extremo o fuentes muy
  degradadas, usa SUPIR.

## GFPGAN vs CodeFormer (restauración de CARA)

Ambos restauran caras (las caras se degradan al upscalar; un upscaler general las deja "plásticas").

| | **GFPGAN** | **CodeFormer** |
|---|---|---|
| Enfoque | GAN prior (StyleGAN2) | **Transformer + codebook** (modela composición global) |
| Control | `--weight` (blend con original) | **`-w / --fidelity_weight` (0..1)** |
| `w=0` | — | **máxima calidad, MENOS fiel** (puede cambiar identidad) |
| `w=1` | — | **máxima fidelidad al original, menos "arreglo"** |
| Fortaleza | rápido, default razonable | mejor en caras MUY degradadas, más robusto |

- **CodeFormer `--fidelity_weight`:** **0.5-0.7 es el sweet spot** (balance calidad/identidad). Baja a 0.3
  para fuentes muy dañadas (deja que invente), sube a 0.8-0.9 cuando la identidad debe preservarse exacta.
- CLI CodeFormer: `python inference_codeformer.py -w 0.7 --bg_upsampler realesrgan --face_upsample -i in/ -o out/`
- **Regla:** CodeFormer para retratos/identidad crítica; GFPGAN como `--face_enhance` rápido dentro de
  Real-ESRGAN.

## SUPIR (diffusion upscaler SOTA)

- **Repo** `Fanghua-Yu/SUPIR`. Upscaler/restaurador **basado en diffusion (SDXL)** guiado por texto →
  **alucina detalle fotorrealista** que ESRGAN no puede inventar. Calidad SOTA para realismo.
- Pesado: **~24GB+ VRAM** (modelos SUPIR-v0Q/v0F + SDXL base). Lento vs Real-ESRGAN.
- **`--fidelity_weight` (similar concepto):** alto = pega al source; bajo = inventa más (mejor para muy
  degradado o artístico, peor si "bloquea el ruido"). Prompt positivo/negativo guía el detalle.
- Disponible como nodes de **ComfyUI** (popular para integrarlo en grafos, ver ref 06).
- **Cuándo:** producto/retrato donde la calidad final manda y puedes pagar GPU. Para upscale masivo barato,
  Real-ESRGAN.

## ESRGAN / SwinIR / HAT (alternativas de arquitectura)

- **ESRGAN** (el original) — superado por Real-ESRGAN para fotos reales.
- **SwinIR** — transformer, fuerte en denoise/deblur, más lento.
- **HAT** (Hybrid Attention Transformer) — SOTA en métricas PSNR/SSIM clásicas; pesado.
- **DAT / SRFormer** — transformers recientes competitivos.
- En la práctica 2026: **Real-ESRGAN para velocidad, SUPIR para calidad diffusion**, los transformers
  (SwinIR/HAT) para casos PSNR-driven o restauración específica. Muchos están como modelos cargables en
  ComfyUI (`models/upscale_models/`, nodo "Upscale Image (using Model)").

## Tiled upscaling (imágenes grandes sin OOM)

- Upscalar una imagen grande de una vez = activaciones enormes → OOM. **Solución: tiles con overlap.**
- Real-ESRGAN: **`--tile 512 --tile_pad 10`** (procesa en bloques de 512 con padding, los une).
- ComfyUI: nodos **"Ultimate SD Upscale"** o tiling nativo del nodo de upscale.
- diffusers: para diffusion-upscale, **`enable_vae_tiling()`** (SKILL §6.23) decodifica el VAE en tiles.
- Trade-off: tiles más chicos = menos VRAM pero más **seams** (costuras) → sube el overlap/pad si ves
  líneas en las uniones.

## El pipeline "genera 480p → upscale 1080p"

```
DiT/SD genera 480p (barato, ~2.25× menos cómputo que 720p nativo)   # SKILL §6.5
  → Real-ESRGAN x2/x4 (o SUPIR si calidad premium) → 1080p+
  → (cara) CodeFormer w=0.6  → retoque facial
```
Esto es **mucho más barato** que generar a alta resolución en el difusor (costo ∝ píxeles). El upscaler
corre en una pasada rápida vs decenas de denoise steps a resolución alta.

## Restauración de VIDEO (frame-by-frame + consistencia temporal)

- **Frame-by-frame:** extrae frames (`ffmpeg -i in.mp4 frames/%06d.png`) → upscala cada uno → re-encodea.
  **Problema: flicker temporal** (cada frame se restaura distinto → parpadeo).
- **Modelos con conciencia temporal:** `realesr-animevideov3` (Real-ESRGAN video), **BasicVSR++ /
  RealBasicVSR** (recurrentes, propagan info entre frames → consistencia), y para diffusion **Upscale-A-
  Video / VEnhancer** (2024-2025, restauración de video con coherencia temporal).
- **Cara en video:** CodeFormer/GFPGAN frame-a-frame da identidad inestable → usa modelos de video o un
  `--fidelity_weight` alto (más fiel = menos variación entre frames).
- **Re-encode:** SIEMPRE `-pix_fmt yuv420p -movflags +faststart` (ver ref 09) y conserva el fps original.
- **Orden:** upscala/restaura → LUEGO interpola fps (ref 09), no al revés (interpolar frames degradados
  propaga artefactos).

## Gotchas

1. **El upscaler general "plastifica" las caras.** Por eso SIEMPRE pasa `--face_enhance`/CodeFormer
   DESPUÉS (o junto) del upscale general — un x4 sin restauración facial da caras de cera.
2. **CodeFormer `w` está invertido respecto a la intuición:** `w=0` = mejor calidad/MENOS fiel; `w=1` =
   más fiel/menos arreglo. Sweet spot **0.5-0.7**. SUPIR `fidelity_weight` es el concepto análogo.
3. **Real-ESRGAN no inventa detalle.** Si la fuente es 240p borrosa, ESRGAN da 1080p borrosa-grande. Para
   detalle nuevo necesitas **SUPIR** (diffusion alucina textura).
4. **Tiling causa seams.** Si ves líneas de rejilla en imágenes grandes, sube `--tile_pad`/overlap. Tile
   demasiado grande → OOM; demasiado chico → costuras. 512 con pad 10-32 suele ir bien.
5. **Restauración de video frame-by-frame parpadea.** Para video usa modelos temporales (BasicVSR++,
   VEnhancer) o sube la fidelidad para minimizar variación entre frames.
6. **fp16 puede dar artefactos en algunos upscalers.** Si ves bandas/colores raros, prueba `--fp32`.

## Fuentes
- https://github.com/xinntao/Real-ESRGAN
- https://blog.segmind.com/codeformer-vs-esrgan/
- https://botmonster.com/ai/local-ai-image-upscaling-real-esrgan-topaz-supir/
- https://arxiv.org/html/2504.14600v1  (NTIRE 2025 Real-World Face Restoration)
- https://github.com/Fanghua-Yu/SUPIR · https://github.com/sczhou/CodeFormer · https://github.com/TencentARC/GFPGAN
