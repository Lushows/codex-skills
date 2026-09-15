# 193 · Pipeline de fotografía de producto IA end-to-end (packshot → hero → escena)

> Convertir UNA foto de producto en un catálogo entero (packshot blanco + heros con atmósfera + N escenas lifestyle)
> sin set físico. La clave es **cadena determinista** + **producto pixel-perfect**: el producto nunca se re-genera, solo se recompone y re-ilumina.

## La cadena correcta (2026)
```
cutout (BiRefNet) → escena/fondo (FLUX Kontext / Nano Banana) → relight (IC-Light) → sombra contacto → upscale
```
- **BiRefNet**: matting alta-res (~2K) con bordes limpios incluso en vidrio/transparencias/pelos. Preserva el producto real **pixel-perfect** — es la garantía de identidad.
- **FLUX.1 Kontext / Nano Banana (Pro)**: edición *in-context*; coloca el cutout en cualquier escena manteniendo etiqueta/logo/color SIN fine-tune. Kontext Max para alta-res con texturas/sombras realistas; Nano Banana Pro cuando la etiqueta lleva texto legible (ver [[195-text-typography-in-image]]).
- **IC-Light**: re-ilumina el producto para que **case con la luz de la escena** (dirección, color, dureza). Sin esto el recorte se ve "pegado".
- **Upscale** (Topaz/Magnific/fal) a resolución impresión/Amazon ≥2000px.

## Las tres entregas del catálogo
| Salida | Qué es | Reglas |
|---|---|---|
| **Packshot** | producto limpio, fondo seamless/gradiente, beauty angle (3/4 vende mejor) | quirúrgico, sin props |
| **Hero** | packshot + atmósfera/escena publicitaria, luz dramática | aspiracional, para ads/portada |
| **Lifestyle** | producto en contexto/en uso (mano, mesa, cocina) | deseo, para social/secundarias |

Un catálogo necesita los tres. El packshot manda en e-commerce; el hero/lifestyle en ads.

## Por qué la cadena vence al text-to-image directo
Pedirle a un modelo "frasco de Melena de León en una cocina" **reinventa** el frasco: etiqueta alucinada, forma distinta, pantone derivado. La cadena cutout→compose **congela** el producto real y solo cambia el entorno. Identidad garantizada > prompt-and-pray.

## Costo/throughput (caso real)
Workflow ComfyUI: una foto → quitar fondo → 5 escenas (cocina, escritorio, exterior, lujo, minimal) → relight por escena → export, **<2 min**. Equivalente tradicional: un día de set, **$500-1,500**. El relight es el cuello: sírvelo warm.

## Sombra y reflejo (lo que separa "venta" de "flotando")
- **Contact shadow** OBLIGATORIA: ancla el objeto al plano. Sin ella, flota. Detalle en [[179-shadow-generation]].
- **Reflejo coherente**: el reflejo debe corresponder a una fuente de la escena nueva; reflejo "huérfano" delata el fake.
- **Specular del material**: vidrio/metal necesitan algo que reflejar (gradientes, flags) o se ven muertos — el relight debe respetar eso. Profundidad en [[177-ic-light-relight-serving]].

## Ángulos y variantes que pide un catálogo
| Variante | Uso | Nota de generación |
|---|---|---|
| 3/4 (beauty angle) | hero e-commerce | el que mejor lee la forma; el más vendedor |
| straight-on | etiqueta plana, ficha | etiqueta legible y centrada |
| macro detail | textura, rosca, grano | upscale fuerte; specular controlado |
| 360 spin | multi-ángulo interactivo | mantén identidad entre frames (mismo cutout/seed) |
| mockup packaging | frasco/sachet/caja | composición del arte real sobre la forma 3D |

## Servir el pipeline
- Nodos **warm** persistentes: BiRefNet, IC-Light y el modelo base no se recargan por job.
- **Batch** las N escenas en una pasada; comparte el cutout (se calcula una vez por producto).
- **Determinismo**: mismo seed + mismo cutout = misma toma reproducible para el cliente.
- Guarda el cutout RGBA como artefacto reusable: alimenta packshot, hero, lifestyle y try-on sin recomputar.

## Gotchas
1. **Producto reinventado** — nunca dejes que el modelo regenere el producto; usa siempre el cutout BiRefNet como capa fija.
2. **Etiqueta alucinada** — texto/logo inventado; Nano Banana Pro para texto + revisión char-por-char.
3. **Look plástico** — IC-Light aplana highlights reales; preserva los especulares originales como capa encima.
4. **Reflejo huérfano** — iguala reflejo a la luz de la escena nueva.
5. **Pantone derivado** — el color de marca se desvía tras varios edits; valida contra muestra y corrige por color.
6. **Sin contact shadow** — el clásico "flota"; añádela siempre.

Cruza con [[177-ic-light-relight-serving]] y [[179-shadow-generation]].

**Fuentes:** github.com/ZhengPeng7/BiRefNet · github.com/lllyasviel/IC-Light · rajatgautam.com/blog/scaling-product-photography · flux-ai.io/model/flux-max-kontext · bfl.ai
