# 80 — Visualización y fotografía de producto con IA (el producto como héroe)

El objetivo: que el producto sea el **héroe** — nítido, fiel a su identidad (etiqueta, logo, color, material) y con
luz que **venda el material**. El oficio del fotógrafo de producto + el toolchain 2026 (BiRefNet → FLUX Kontext / Nano Banana → IC-Light → upscale) permite catálogos completos sin set físico — *si* respetas las reglas.

## El packshot / hero shot
**Packshot** = producto limpio sobre fondo seamless/gradient, en su **beauty angle** (el ángulo que mejor lee la
forma). Variantes: **three-quarter** (3/4, cara frontal + lateral, el más vendedor para frascos/cajas), **straight-on**
(etiqueta plana, e-commerce), **macro detail** (textura, rosca de tapa, grano del polvo). El *hero* publicitario añade atmósfera; el packshot de e-commerce es quirúrgico.

## Iluminación de estudio para producto
**Light tent / softbox** envuelve y controla reflejos. Fondos en **gradiente** (oscuro→claro) dan dimensión. Clave en
materiales duros = **specular control**. **Vidrio/líquido:** *bright-field* (botella oscura sobre fondo claro, bordes
negros que definen silueta) o *dark-field* (botella clara sobre fondo oscuro, bordes brillantes); reflejos verticales
largos venden "vidrio". **Metal:** necesita algo que reflejar (gradientes, flags) o se ve muerto. **Rim/edge light**
(kicker) separa del fondo. **Cápsulas/polvos (BIO-SETA):** *raking light* lateral para textura del polvo; control de brillo en cápsulas de gel para que no "quemen".

## Lifestyle vs estudio
**Estudio** (aislado, fondo blanco) = claridad, comparación, e-commerce. **Lifestyle** (en contexto/en uso: el frasco
de Melena de León en una cocina con café, manos sosteniendo cápsulas) = deseo, aspiración, ads sociales. Un catálogo necesita ambos.

## Pipeline AI de producto (el flujo correcto 2026)
1. **Cutout** del producto REAL con **BiRefNet** (matting alta-res ~2K, bordes limpios) — preserva el producto pixel-perfect.
2. **Colocar en cualquier escena** con **FLUX.1 Kontext** o **Nano Banana (Pro)**: edición in-context que mantiene **identidad EXACTA** (etiqueta, color, logo) sin fine-tune. **Nano Banana Pro** = más fuerte en texto/etiqueta legible; **Kontext** = relight/blend y atmósfera.
3. **Relight** con **IC-Light** para integrar la luz del producto con la nueva escena (dirección, color, dureza).
4. **Upscale** final (Magnific/Topaz/fal) para resolución impresión/Amazon.

## Consistencia del producto real & specs
La etiqueta, tipografía, color de marca y forma idénticos entre tomas → usa el cutout real como reference image en
cada generación; verifica logo y pantone. **360 spin/multi-ángulo** y **mockups de packaging** (frasco, sachet, caja).
**Sombras/reflejos que venden:** la **contact shadow** (ancla el objeto al plano) es OBLIGATORIA — sin ella el producto
flota. **Specs e-commerce:** Amazon = imagen principal sobre **fondo blanco puro RGB 255,255,255**, producto ≥85% del
cuadro, sin texto/logos/props añadidos. Meta/IG Shops = fondo limpio, producto centrado, sin marcas de agua. Cumple esto en la imagen *hero*; reserva el lifestyle para secundarias y ads.

## Gotchas
1. **Distorsión del producto** — la IA "reinventa" la forma del frasco; bloquea con el cutout real y verifica geometría.
2. **Etiqueta equivocada** — texto/logo alucinado; usa Nano Banana Pro para texto y revisa carácter por carácter.
3. **Reflejos falsos** — reflejos que no corresponden a ninguna fuente; iguala reflejo a la luz de la escena.
4. **Look plástico** — el relight aplana especulares; preserva highlights reales como capa.
5. **Sin sombra de contacto** — el producto flota; añádela siempre.
6. **Color de marca derivado** — el pantone se desvía tras varios edits; valida con muestra y corrige por color.

**Fuentes:** github.com/ZhengPeng7/BiRefNet · fal.ai/models/fal-ai/birefnet · piclumen.com/blog (FLUX-Kontext vs Nano-Banana) · bfl.ai.
