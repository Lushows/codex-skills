# 188 · Mapas de normales y segmentación (control, 3D, compositing)

> Depth dice "qué tan lejos"; normales dicen "hacia dónde mira la superficie"; segmentación dice
> "qué es cada píxel". Los tres mapas son el lenguaje de control de la generación visual.

## Mapas de normales
Cada píxel codifica un vector 3D (la normal de la superficie) en RGB: R=X, G=Y, B=Z. Capturan
orientación y micro-relieve que la profundidad sola pierde (una pared plana inclinada vs una con relieve).
- **Cómo obtenerlos**: estimadores dedicados (DSINE, Marigold-Normals, Lotus) o derivados de depth (peor:
  derivar normales de un depth ruidoso amplifica el ruido → mejor estimarlas directo).
- **Usos**: ControlNet-normal para fijar relieve/iluminación; relight (con las normales calculas cómo
  rebota una luz nueva); input para mallas 3D junto a depth.
- **Convención que muerde**: hay dos espacios — **world-space** y **tangent/camera-space** — y el eje Y/Z
  puede ir invertido entre herramientas. Un normal-map con Y invertido produce iluminación al revés.
  Verifica la convención del ControlNet destino antes de alimentarlo.

## Mapas de segmentación
Dos sabores distintos, no los confundas:
| Tipo | Qué da | Uso típico | Modelos |
|---|---|---|---|
| **Semántica** | clase por píxel (cielo, persona, coche) | ControlNet-seg (paletas ADE20K), escena por regiones | Mask2Former, OneFormer, SegFormer |
| **Promptable / instancia** | máscara del objeto que señalas | recortar, inpaint dirigido, rotoscopia | **SAM / SAM2** |
| **Open-vocabulary** | máscara por texto ("la taza roja") | seleccionar por descripción sin clases fijas | Grounded-SAM, langSAM |

- **ControlNet-seg** usa paletas de color fijas (cada color = una clase). Si pintas el mapa a mano,
  respeta la paleta exacta del checkpoint o ignora regiones.
- Para **editar un objeto concreto** (quitar/reemplazar) quieres máscara de instancia (SAM), no semántica.

## Pipeline de control multi-mapa
Combinar mapas da más fidelidad que cualquiera solo:
- **depth + normal**: depth fija la silueta/distancia, normal recupera el relieve fino. Estándar para 3D.
- **seg + depth**: seg separa regiones (cielo vs edificio), depth da volumen dentro de cada una.
- **Multi-ControlNet**: encadena 2-3 mapas con pesos distintos. Subir todos a 1.0 satura y "congela" la
  generación (sin libertad creativa); baja pesos (0.4-0.7) para guiar sin clonar.

## Ingeniería
- **VRAM/velocidad**: estimadores de normal/seg son ligeros (similar a depth, 8-12GB). SAM2 es el más
  caro en video por su memoria temporal (ver cierre).
- **Coherencia temporal**: igual que depth, normal y seg por-frame parpadean; propaga con tracking/flujo.
- **Precisión**: normales en EXR/16-bit si van a 3D; seg como índices enteros (no JPEG, que destroza bordes
  de máscara con compresión).
- **Orden del pipeline**: estima todos los mapas del frame original **antes** de generar; no re-estimes
  sobre la salida generada esperando los mismos mapas.

## Receta: relight con normales
1. Estima normal-map del sujeto (DSINE/Marigold-Normals).
2. Define una luz nueva (dirección + color). Lambert: intensidad = max(0, dot(normal, dir_luz)).
3. Multiplica el albedo por ese shading → re-iluminado plausible sin re-renderizar 3D.
4. Combina con depth para sombras proyectadas por distancia. Verifica la convención de eje antes (paso 0).

## Errores que muerden
- Normal-map con eje invertido → relieve y luz al revés (síntoma: parece "hundido" lo que debería sobresalir).
- Usar seg semántica para inpaint de un objeto → editas todos los de esa clase, no el que querías.
- Derivar normales de depth de baja calidad en vez de estimarlas → ruido amplificado.
- Guardar seg como JPEG → la compresión inventa clases falsas en los bordes de máscara.
- Pintar mapa seg con colores libres en vez de la paleta ADE20K del checkpoint → regiones ignoradas.

Cruza con [[187-depth-estimation-depthanything-marigold]].
