# 189 · Optical flow: RAFT y SEA-RAFT (video coherente, interpolación)

> El flujo óptico es el campo de movimiento por píxel entre dos frames: hacia dónde y cuánto se movió
> cada punto. Es el pegamento que vuelve coherente cualquier proceso aplicado frame-a-frame.

## Qué resuelve
Procesar video frame-por-frame (depth, normal, seg, estilo, upscale) **parpadea** porque cada frame se
estima aislado. El flujo te deja **propagar** información del frame previo al siguiente (warping), matando
el flicker. También es la base de:
- **Interpolación** (slow-motion, subir fps): generar frames intermedios siguiendo el movimiento.
- **Estabilización** y compensación de cámara.
- **Warp-guided editing**: editas un frame y arrastras la edición por el flujo.
- **Detección de oclusiones**: zonas donde el flujo no cuadra (forward-backward check) = algo se tapó.

## RAFT → SEA-RAFT (estado 2026)
| | RAFT | SEA-RAFT |
|---|---|---|
| Arquitectura | correlación + GRU iterativo | RAFT + regresión inicial directa + pérdida mixture-of-Laplace |
| Velocidad | base | **≥2.3× más rápido** [verificado] |
| Generalización | buena | mejor cross-dataset (KITTI, Spring) |
| Precisión | SOTA en su época | SOTA en Spring: EPE 3.69, 1px 0.36 (−22.9%/−17.8% vs previo) [verificado] |

**SEA-RAFT** (Princeton, ECCV 2024 Oral) es el default razonable hoy: más simple, rápido y preciso que
RAFT clásico. Repo `princeton-vl/SEA-RAFT`. Alternativas de gama: GMFlow/FlowFormer (transformers, más
caros), y para interpolación pura **RIFE/FILM** que estiman su propio flujo interno.

## Conceptos que muerden
- **Forward vs backward flow**: flujo de A→B no es el inverso exacto de B→A. Para warp correcto necesitas
  el sentido adecuado; mezclarlos desplaza todo medio objeto.
- **Oclusiones**: lo que aparece/desaparece no tiene correspondencia → el flujo ahí es basura. Detéctalo
  con **forward-backward consistency** y enmascara esas zonas (no las warpees, regenéralas).
- **Movimiento grande / blur**: flujos grandes entre frames lejanos fallan. Encadena frame-a-frame, no
  saltes. Para fps bajo, interpola primero.

## Receta: temporal-consistency frame-a-frame
1. Estima flujo entre frame t-1 y t (SEA-RAFT).
2. Warpea el resultado ya procesado de t-1 hacia t usando ese flujo.
3. Calcula máscara de oclusión (FB-check); donde no hay correspondencia, usa el resultado fresco de t.
4. Mezcla (blend) warped + fresco ponderado por la confianza/oclusión.
Esto es el núcleo de pipelines de estilización de video sin flicker (EBSynth-like, Deflicker).

## Ingeniería de serving
- **VRAM**: SEA-RAFT es ligero (cabe en 8GB para resoluciones medias). El costo escala con resolución²;
  baja resolución del flujo y reescala el campo si vas justo.
- **fp16**: acelera sin perder calidad perceptible en flujo.
- **Throughput**: es un par de imágenes por inferencia; para video largo, el cuello es I/O y el número de
  pares, no el modelo. Procesa en lote secuencial, no recargues pesos por par.
- **Precisión de almacenamiento**: guarda flujo en `.flo`/EXR float; cuantizar a 8-bit pierde
  desplazamientos sub-píxel y reintroduce flicker.

## Errores que muerden
- Saltar frames (estimar flujo entre t y t+5) en escenas con movimiento → el modelo falla, encadena de a 1.
- Confundir forward y backward flow al warpear → la edición se desplaza medio objeto.
- Warpear sobre oclusiones sin máscara FB-check → "arrastres" y fantasmas en bordes de objetos que entran/salen.
- Usar flujo para interpolar fps muy bajo directamente → mejor RIFE/FILM, que están hechos para eso.

Cruza con [[09-interpolacion-edicion-video-ffmpeg]] y [[190-tracking-cotracker-sam2]].
