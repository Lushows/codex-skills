# 204 · Restyle y relight de vídeo (cambiar el look, conservar el movimiento)

> Cambiar la estética o la iluminación de un vídeo **sin** tocar el movimiento ni la identidad.
> El enemigo único es el flicker temporal: lo que funciona por-frame parpadea como estroboscopio.

## Dos tareas distintas, mismo enemigo

| Tarea | Qué cambia | Qué conserva |
|---|---|---|
| **Restyle** | textura/estilo/material (anime, óleo, otro mundo) | pose, layout, timing |
| **Relight** | iluminación, dirección de luz, ambiente | geometría, identidad, movimiento |

Aplicar un modelo de **imagen** frame-a-frame (IC-Light por foto, un IPAdapter suelto) da **inconsistencia
temporal brutal**: cada frame decide distinto y el vídeo hierve. La solución es un modelo con atención
temporal entre frames.

## Relight: el estado del arte open
- **RelightVid** (ene-2025, `Aleafy/RelightVid`): difusión **temporal-consistente** que extiende
  **IC-Light** a vídeo. Control por **prompt de texto**, **vídeo de fondo** o **mapa de entorno** (HDRI).
- Dos modos: **full-scene** (foreground + fondo relit juntos al prompt) y **foreground-preserved**
  (inpinta el fondo, sólo relighta el sujeto).
- Entrenado con augmentaciones de iluminación in-the-wild + render bajo luz dinámica extrema → relight
  arbitrario sin descomposición intrínseca, conservando los priors de su backbone de imagen (IC-Light).

## Restyle: rutas
- **Editar manteniendo movimiento** → V2V con un base de vídeo (Wan/LTX) + control estructural
  (ControlNet de profundidad/pose/canny) para clavar layout, y prompt/IPAdapter para el look.
- **Rápido y barato** → **LTX-Video** como backbone de baja latencia ([[124-ltx-video-realtime-rapido]]).
- El truco anti-flicker es el mismo: condicionar por estructura (depth/pose) que es estable entre frames,
  no por píxel.

## Lo que muerde
- **Per-frame = no**: si tu pipeline corre IC-Light suelto por frame, vas a flickerear. Usa RelightVid o
  un V2V temporal. Para imagen estática de IC-Light, ver [[177-ic-light-relight-serving]].
- **Mapa de entorno (HDRI)**: relight realista quiere HDRI o un fondo-vídeo coherente; un prompt de texto
  da control grueso, no fino.
- **Identidad del sujeto**: modo foreground-preserved evita que el relight le cambie la cara/ropa.
- **VRAM y duración**: backbone de vídeo + atención temporal pesa; clips largos en segmentos con solape.
- **Coherencia entre segmentos**: si segmentas, ancla la iluminación (mismo prompt/HDRI) o saltará entre tramos.
- **Calidad**: evalúa con consistencia temporal (warp-error) además del look, no sólo un frame.

## Control: de grueso a fino (relight)
| Condición | Control | Cuándo |
|---|---|---|
| **Prompt de texto** | grueso ("luz cálida de atardecer") | rápido, dirección general |
| **Vídeo de fondo** | medio (el fondo dicta la luz del sujeto) | compositing, sujeto en escena nueva |
| **Mapa de entorno (HDRI)** | fino (dirección/intensidad reales) | realismo, integración a placa real |

Modo **foreground-preserved** = inpinta fondo y relighta sólo al sujeto → protege identidad/ropa cuando el
relight global le cambiaría la cara.

## Sizing y serving
- Backbone de vídeo + atención temporal **pesa**: presupuesta Ampere+/Ada con VRAM holgada; clips largos
  en **segmentos con solape** anclando el mismo prompt/HDRI por segmento o salta la iluminación entre tramos.
- Pesos de RelightVid + backbone IC-Light → **Network Volume** para frío barato ([[113-network-volume-modelos-grandes]]).
- **Prototipa barato**: valida el look a baja resolución/fps, luego sube y super-resuelve. Generar restyle
  a 4K nativo es tirar GPU. Cruza con [[30-finops-gpu]].
- **Evalúa con warp-error** (consistencia temporal) además del look; un frame bonito que flickerea es un fallo.

## Pipeline
```
vídeo origen → [extraer depth/pose] → RelightVid (relight, HDRI/fondo/texto) o V2V+ControlNet (restyle)
            → super-res temporal ([[206-video-superres-temporal]]) si bajaste resolución
```

Cruza con [[177-ic-light-relight-serving]] y [[124-ltx-video-realtime-rapido]].
