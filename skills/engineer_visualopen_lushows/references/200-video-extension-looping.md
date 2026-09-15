# 200 · Extender y loopear video manteniendo coherencia

> Los modelos de difusión generan ~5s por ventana. Para 30s o 2min necesitas **encadenar**: cada
> segmento debe arrancar donde terminó el anterior, sin saltos de color, identidad ni movimiento.

## El límite que estás esquivando
Wan y similares tienen una ventana fija (~81 frames / ~5s). Generar más en una sola pasada no cabe en
VRAM ni en la atención temporal del modelo. La solución no es "un video gigante" sino **N ventanas
solapadas y cosidas**.

## Las tres técnicas
| Técnica | Cómo | Cuándo |
|---|---|---|
| **Sliding window** (WanGP/Wan2GP) | Genera ventanas secuenciales con **overlap**, mezcla la zona solapada | Largo continuo, una escena que evoluciona |
| **Video-extender (VACE)** | Toma el clip previo como **control latent**, genera continuación | Extender un clip que ya te gusta |
| **FLF encadenado** | Último frame del clip N = primer frame de N+1 | Tomas dirigidas, transiciones aprobadas |

- **Sliding window**: clave = el **solapamiento**. Las ventanas comparten frames; al fusionar la
  región común se evita la costura. Sin overlap → corte visible cada 5s (bug clásico: "loopea a 5s").
- **Video-extender**: usa VACE ([[198-vace-control-video-deep]]) con el clip anterior como condición →
  continuación coherente, prompt nuevo por tramo para evolucionar la escena.

## Patrón de deriva (drift) y cómo frenarlo
Encadenar acumula error: el color se desatura, la identidad muta, el detalle se degrada tramo a tramo.
- **Re-anclar con referencia**: re-inyecta la imagen/identidad original cada N segmentos (ref de VACE).
- **Overlap generoso**: más frames compartidos = transición más suave, menos deriva.
- **Prompt por segmento**: un LLM multimodal (Qwen2.5-VL) lee el último frame y escribe el prompt del
  siguiente → continuidad semántica automática (patrón WAN2.2 5B long-video).
- **Color match**: post-proceso que iguala histograma del segmento N al N-1 mata la desaturación.

## Looping perfecto
- **FLF con first == last**: fuerza que el final empate el inicio → loop sin corte.
- O genera normal y **cruza-disuelve** (crossfade) los extremos con overlap; menos exacto pero rápido.
- Cuida que el **movimiento** también cierre (no solo el frame): si la mano sube al final y empieza
  abajo, el loop salta aunque el frame coincida.

## Detalles que muerden
- **Coste lineal**: 1min ≈ 12 ventanas ≈ 12× el coste/tiempo de una. Presupuesta y usa modelo chico
  (1.3B/5B) para iterar la continuidad antes del 14B.
- **VRAM constante, no acumulativa**: cada ventana es independiente → no escala memoria con duración
  (ventaja del sliding window sobre "todo de una").
- **Audio/lip-sync**: si el largo lleva voz, sincroniza por segmento y cose; no generes 1min de
  lip-sync de un tirón.
- **Seed**: misma seed entre ventanas ayuda a la coherencia de textura, pero puede congelar el
  movimiento. Equilibra.

Cruza con [[114-video-segmentado-largo-clip]].
