# 60 — Edición de imagen avanzada con IA (inpainting / compositing / relight)

El toolkit 2026 es **cambiar UNA cosa manteniendo el resto idéntico** — generar está resuelto, los edits *controlados* son el oficio.

## Edición por instrucción ("cambia X, conserva el resto")
- **FLUX.1 Kontext** (BFL) — fuerte preservación de contexto; `[dev]` (open, ~24GB), `[pro]`/`[max]` API. La herramienta pro para "conserva el producto, cambia la escena".
- **Nano Banana / Pro** (Google Gemini 2.5/3 Flash Image) — best-in-class en entendimiento espacial, edits locales, relight coherente; API-only.
- **Qwen-Image-Edit** (Alibaba, open) — soberbio editando *texto* in-image (CN/EN) y objetos; fine-tunable para catálogos de producto.
- **SeedEdit** (ByteDance) — edits con preservación de identidad.

## Inpainting / outpainting (mask-based)
**FLUX Fill** (`[dev]`/`[pro]`) = líder de calidad para fill/expand; SDXL inpaint + ControlNet sigue viable barato.
Outpainting = expandir el canvas con el mismo Fill.

## Background removal / matting
**BiRefNet** (la arquitectura líder) y **RMBG-2.0** (BRIA, sobre BiRefNet — **non-commercial sin licencia**);
**rembg** envuelve varios para one-liner; SAM 2/3 + GroundingDINO para segmentación prompteada.

## Relighting
**IC-Light** (v1/v2) re-ilumina un foreground para matchear una luz/fondo target — la clave para que los composites
sean creíbles. Aliméntalo con el cutout + prompt de luz o environment target.

## Upscale + restore
Real-ESRGAN / 4x-UltraSharp general; **SUPIR** y **CCSR** para restauración fotorrealista; GFPGAN/CodeFormer caras (ver ref 08).

## El workflow killer: fotografía de producto
```python
from rembg import remove                                    # backend BiRefNet/RMBG
cutout = remove(open("product.png","rb").read())            # sujeto + alpha
# → pega el cutout en la escena nueva, luego IC-Light para matchear luz
# → pasada FLUX.1 Kontext: "place this product on a marble counter, soft morning
#   window light, keep product label and color exact"
```
Cortas el producto REAL (BiRefNet) → lo colocas vía **FLUX.1 Kontext** ("keep product identity exact, change only
background/lighting") → IC-Light unifica iluminación → upscale. La preservación de identidad de Kontext mantiene
label/logo/color reales — t2i puro inventaría un producto falso.

## Compositing de elementos IA en fotos reales
Matchea **dirección de luz, temperatura de color, perspectiva/líneas de fuga, DoF blur, y grano/ruido**. Genera el
elemento, relight (IC-Light), matchea grano, feather/match edges; una pasada final low-denoise sobre la costura mezcla.

## Gotchas
1. **Los edits por instrucción driftean toda la imagen** — aun los modelos "keep the rest" recolorean regiones intactas; mask + composite back la zona sin cambios, o A/B pixel-diff para verificar.
2. **RMBG-2.0 es non-commercial sin licencia** — en producto pagado necesitas licencia BRIA; BiRefNet base la evita. Revisa SIEMPRE la licencia de los pesos.
3. **El matting falla en pelo/vidrio/humo/piel** — cutouts duros muestran fringing; usa trimap/matting + despill, no un mask de 1-bit.
4. **Relight sin matchear la sombra proyectada se ve falso** — IC-Light re-ilumina el sujeto pero tú añades/relight la sombra de contacto en el nuevo plano.
5. **Mismatch de grano/perspectiva = el tell #1 del composite** — un elemento IA sin ruido sobre foto con grano se lee fake; matchea grano, lens blur y geometría de punto de fuga.
6. **Face swap/retoque: ética & consentimiento** — no swapees identidades reales sin consentimiento; muchas licencias/ToS lo prohíben; guarda el "before" y divulga edits IA donde se requiera.

**Fuentes:** bfl.ai (FLUX.1 Kontext) · huggingface.co/Qwen/Qwen-Image-Edit · huggingface.co/briaai/RMBG-2.0 · github.com/lllyasviel/IC-Light · ai.google.dev.
