# 190 · Tracking: CoTracker3 (puntos) y SAM2 (objetos) en video

> Flujo óptico te da movimiento entre dos frames; el tracking te da **trayectorias largas**: seguir el
> mismo punto u objeto a lo largo de todo el clip, incluso con oclusiones.

## Dos problemas, dos herramientas
| | Point tracking | Object/mask tracking |
|---|---|---|
| Qué sigue | puntos concretos (trayectoria 2D + visibilidad) | la máscara de un objeto frame a frame |
| Modelo 2026 | **CoTracker3** (Meta) | **SAM2 / SAM2.1** (Meta) |
| Salida | (x,y) por frame + flag visible/ocluido | máscara binaria por frame |
| Uso | motion-transfer, anclar efectos, medir movimiento | rotoscopia, object removal, inpaint dirigido |

- **CoTracker3**: rastrea muchos puntos conjuntamente (aprovecha correlación entre puntos → robusto en
  oclusión). Más preciso que el flujo encadenado para trayectorias largas, pero **computacionalmente caro**. [verificado]
- **SAM2**: segmentación promptable con **memoria temporal**: señalas el objeto en un frame (clic/caja/máscara)
  y lo propaga por el video, re-identificándolo tras oclusiones.

## Cómo se combinan (patrón fuerte)
CoTracker3 alimenta puntos a SAM2: los puntos rastreados se convierten en **prompts** que guían/refinan la
máscara de SAM2 frame a frame; las trayectorias dinámicas se reinyectan para afinar segmentación. SAM2
rinde mejor emparejado con un tracker de puntos que solo con su propagación interna. [verificado] Variantes
2025 (p. ej. HiM2SAM) añaden estimación de movimiento jerárquica + optimización de memoria para tracking
de **largo plazo** (clips largos, oclusiones repetidas). [verificado]

## Cuándo cada uno
- **Quitar/reemplazar un objeto** en todo el clip → SAM2 para la máscara, luego video-inpaint.
- **Pegar un efecto/etiqueta que siga un punto** (un logo en una camiseta, brillo en un ojo) → CoTracker3.
- **Motion transfer / pose desde puntos** → CoTracker3.
- **Sustituir todo el flujo encadenado por algo robusto a oclusión larga** → tracking, no flujo.

## Conceptos que muerden
- **Visibilidad ≠ posición**: CoTracker reporta cuándo un punto está ocluido. Si ignoras el flag y usas la
  posición "adivinada" durante la oclusión, el efecto anclado salta. Respeta el flag.
- **Deriva (drift)**: trackers acumulan error en clips largos. Re-anclar/re-promptear cada N frames
  estabiliza. SAM2 deriva menos por su memoria, pero si el objeto cambia mucho de apariencia, re-prompt.
- **Memoria de SAM2**: su banco de memoria crece con el clip → más VRAM cuanto más largo. Clips muy largos
  → trocea con solapamiento o usa variantes con memoria optimizada.

## Ingeniería de serving
- **VRAM**: SAM2 image es ligero; SAM2-video escala con longitud por la memoria temporal (vigila OOM en
  clips largos). CoTracker3 escala con nº de puntos × frames → no rastrees 10k puntos si necesitas 200.
- **Throughput**: ambos son inferencia secuencial sobre frames; mantén pesos calientes y procesa el clip
  de un tirón (recargar pesos por frame mata el rendimiento).
- **Resolución de máscara**: SAM2 da máscaras suaves; binariza con umbral y aplica morfología si vas a
  inpaint (bordes limpios evitan halos).
- **Formato**: máscaras como PNG índice/1-bit por frame (no JPEG); trayectorias como `.npy` (x,y,vis).

## Errores que muerden
- Ignorar el flag de visibilidad de CoTracker durante oclusión → el efecto anclado salta a una posición inventada.
- Procesar un clip de 10 min con SAM2-video de un tirón → OOM por memoria temporal; trocea con solape.
- No re-promptear SAM2 cuando el objeto cambia mucho de apariencia → la máscara se pierde y no vuelve.
- Rastrear miles de puntos cuando necesitas decenas → CoTracker se vuelve carísimo sin ganancia.

Cruza con [[186-object-removal-replace]] y [[201-video-inpainting-outpainting]].
