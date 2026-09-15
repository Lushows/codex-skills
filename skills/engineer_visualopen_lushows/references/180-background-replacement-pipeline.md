# 180 · Pipeline de reemplazo de fondo end-to-end (matting → relight → compositing)

> Cambiar el fondo de un producto NO es "recortar y pegar" — es un pipeline de 5 pasos donde cada uno arregla un tell distinto.
> Saltarte uno (típicamente relight o sombra) produce el clásico recorte que grita "editado".

## La cadena completa (orden estricto)
```
foto original
  → 1. MATTING        (alpha limpio del sujeto)
  → 2. NORMALIZE FG   (aplanar su luz vieja)
  → 3. NUEVO FONDO    (generar/elegir escena)
  → 4. RELIGHT        (matchear luz del sujeto al fondo)
  → 5. SHADOW         (sombra de contacto + proyectada)
  → 6. HARMONIZE      (color/exposición final + grano)
  → 7. UPSCALE/FINISH
```
Cada flecha existe porque el anterior deja un tell sin resolver. El error de novato es ir de matting directo a "pegar en fondo" y saltarse 4-6.

## Paso a paso (qué herramienta y qué arregla)
| # | Paso | Herramienta | Arregla |
|---|---|---|---|
| 1 | Matting | BiRefNet / SAM2 ([[137-matting-bg-removal-escala]]) | recorte con alpha; pelo/borde |
| 2 | Normalize FG | aplanado de luz / delight | que la luz vieja no pelee con la nueva |
| 3 | Fondo nuevo | FLUX t2i / escena real / inpaint | el entorno target |
| 4 | Relight | IC-Light ([[177-ic-light-relight-serving]]) | dirección/temperatura de luz del sujeto |
| 5 | Sombra | shadow-gen difusión ([[179-shadow-generation]]) | anclaje al plano |
| 6 | Harmonize | harmonizer + grano ([[178-harmonization-compositing]]) | color cast, exposición, ruido |
| 7 | Finish | upscale (SUPIR/Real-ESRGAN) | resolución entrega |

## Generar el fondo: t2i puro vs Kontext
- **t2i puro** (FLUX) para el fondo, luego pegar el sujeto REAL encima — preserva identidad del producto. **Recomendado** para catálogo (el producto debe ser fiel).
- **FLUX.1 Kontext** ("place this product on X, keep product exact") hace fondo+colocación en una pasada con preservación de contexto — menos pasos pero más caro, riesgo de leve drift del producto. Bueno para hero.
- **Nunca** t2i que "imagine" el producto: inventa label/forma falsos.

## Serving y orquestación
- Es **multi-modelo**: matting (ligero, escala) + relight (FLUX 24GB) + shadow-gen (difusión) + upscale (pesado). No los metas todos en un worker monolítico si el catálogo es grande.
- **Arquitectura recomendada**: cola de jobs por etapa; matting/harmonize en GPU barata/CPU; relight+upscale en GPU grande caliente. Pesos en network volume ([[113-network-volume-modelos-grandes]]) para evitar re-descarga.
- **Idempotencia**: cachea el output de cada etapa por hash del input — re-correr solo desde el paso que cambió (ej. nuevo fondo no re-hace el matting).
- **Batch por lote/colección**: misma luz/seed para coherencia entre SKUs.

## QA automático (no confíes a ojo a escala)
- **Borde**: detecta fringing/halo (gradiente alto en el alpha) → re-matting.
- **Coherencia de luz**: histograma de luminancia fg vs bg en la zona de contacto.
- **Sombra presente**: verifica que exista oscurecimiento bajo la base (si no → flotando).
- **Drift de producto** (si usaste Kontext): pixel-diff del label/logo contra original.

## Gotchas
1. **Saltarse relight** = sujeto con su luz original sobre fondo de otra luz → el tell más grosero.
2. **Saltarse sombra** = flotando (ver [[179-shadow-generation]]).
3. **Matting malo arrastra todo** — un alpha sucio no se arregla en pasos posteriores; basura entra, basura sale.
4. **Orden invertido** (harmonize antes de relight) recolorea sobre una luz que vas a cambiar → trabajo perdido.
5. **Grano**: fondo generado es liso, foto del producto tiene grano → mismatch; unifica grano al final.
6. **Resolución**: relight a 1024 y entregar a 4K sin upscale = blando; upscalea al final, no antes (upscalear el cutout amplifica el fringe).

Cruza con [[137-matting-bg-removal-escala]] y [[177-ic-light-relight-serving]].
