# 138 · Upscaling y restauración a escala (producción y video)

> [[08-upscaling-restauracion]] cubre los modelos y la cara. Esta ref es el lado de **producción**:
> elegir por throughput, upscalar **video** sin flicker, tiling para no reventar VRAM y batch real.

## Decisión rápida (qué usar)

| Caso | Modelo | Por qué |
|---|---|---|
| Batch / pipeline barato (480p→1080p) | **Real-ESRGAN** (`x4plus`, `realesr-general-x4v3`) | ~10s/img, GAN fiel, no alucina, escala lineal |
| Hero shot, fuente muy degradada | **SUPIR** | difusión SDXL como prior, máximo detalle, pero ≥12GB VRAM y **10-50× más lento** (~70s+/img) |
| Cara | **GFPGAN** (rápido) / **CodeFormer** (degradación severa) | ver [[08-upscaling-restauracion]] para `--fidelity_weight` |
| Anime/ilustración | `RealESRGAN_x4plus_anime_6B` | liviano, específico |
| **Video** | **SeedVR2** (preferente) / **FlashVSR** / `realesr-animevideov3` | ver sección video |

Regla de costo: **upscaler GAN para todo el volumen**; SUPIR solo en el 1-5% de shots que lo justifican. SUPIR en batch masivo arruina el FinOps ([[30-finops-gpu]]).

## Upscaling de VIDEO — el problema es el tiempo, no el espacio

Frame-by-frame con un upscaler de imagen (Real-ESRGAN sobre cada frame) **parpadea**: cada frame se mejora distinto → flicker de textura/borde. Dos caminos:

| Estrategia | Modelo | Consistencia temporal | Costo |
|---|---|---|---|
| Frame-by-frame | Real-ESRGAN / SUPIR por frame | mala (flicker) | barato pero hay que post-suavizar |
| **Temporal-aware** | **SeedVR2** (ByteDance, Apache-2.0, 3B abierto) | alta (atención video-nativa, batch de frames) | difusión 1-paso → viable a escala |
| Temporal-aware | **FlashVSR** | alta, optimizado velocidad | alternativa 2026 |

- **SeedVR2**: difusión de **un solo paso** (denoise condicionado) → upscalea 540p→4K manteniendo coherencia entre frames porque procesa ventanas de frames juntos. Licencia **Apache-2.0** → uso comercial libre. Es el default 2026 para video real (no anime).
- Para **anime/ilustración en video**: `realesr-animevideov3` sigue siendo suficiente y mucho más barato.
- Si usas frame-by-frame por restricción de VRAM: aplica **suavizado temporal** posterior o un EMA del frame previo, y reconstruye con ffmpeg ([[09-interpolacion-edicion-video-ffmpeg]]).

Flujo video típico:
```bash
ffmpeg -i in.mp4 -qscale:v 2 frames/%06d.png        # extraer
# SeedVR2 (ComfyUI o script) sobre la secuencia, no frame aislado
ffmpeg -framerate 30 -i up/%06d.png -i in.mp4 -map 0:v -map 1:a \
       -c:v libx264 -crf 17 -pix_fmt yuv420p out.mp4   # remux con audio original
```

## Tiling para VRAM (clave a alta resolución)
- VRAM crece con el **área**; 4K sin tiling OOMea hasta en A100.
- Real-ESRGAN: `--tile 512 --tile_pad 32`. Tiles más chicos = menos VRAM, más tiempo y riesgo de **costuras** en el borde → `tile_pad` solapa para ocultarlas.
- SUPIR: tiled VAE + tiled diffusion (en su repo/ComfyUI); sin esto, 2K ya no entra en 24GB.
- SeedVR2: usa **BlockSwap** para correr en VRAM modesta moviendo bloques a CPU/RAM bajo demanda (más lento, pero corre).
- Regla: baja `tile` hasta que entre, sube `tile_pad` hasta que desaparezca la costura.

## Throughput y batch (producción)
- **Mantén el modelo caliente** (warm worker): cargar Real-ESRGAN/SUPIR por job destruye el throughput. Patrón warm-state en [[06-comfyui-backend-produccion]].
- **fp16** por defecto; `--fp32` solo si hay artefactos. half ≈ −40% VRAM, ~2× throughput.
- **Agrupa por resolución** para no re-padear el batch.
- **Real-ESRGAN** en L4/A10 escala lineal a miles de imágenes/h; **SUPIR** es de a una.
- Cuello de botella frecuente: **decode/encode** y disco, no la GPU. Pipeline con prefetch + escritura async.
- GPU sizing: Real-ESRGAN corre en 8-12GB; SUPIR quiere ≥16-24GB; SeedVR2 video según res (BlockSwap baja el piso).

## Restauración de cara a escala
- Tras cualquier upscale general, la cara queda "plástica" → pasa **GFPGAN** (rápido, batch) por defecto; **CodeFormer** con `-w 0.5-0.7` para degradación fuerte sin cambiar identidad.
- En **video**, restaurar cara frame a frame **re-introduce flicker de identidad** → o bien upscaler temporal (SeedVR2 ya recupera rostro bien), o restaura cara con `--fidelity_weight` alto + suavizado temporal.
- Para avatares parlantes, la restauración va **antes** del recorte de fondo ([[137-matting-bg-removal-escala]]).

## Evaluar que el upscale no degradó
No confíes en el ojo a escala: mide. PSNR/SSIM vs referencia cuando exista, o no-referencia (NIQE/MANIQA). Para video añade consistencia temporal (warp error). Detalle en [[17-evals-modelos-generativos]].

Cruza con [[08-upscaling-restauracion]], [[09-interpolacion-edicion-video-ffmpeg]] y [[02-open-models-catalog-2026]].
