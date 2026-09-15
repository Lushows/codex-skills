# 198 · VACE a fondo (ref / pose / depth / mask en un solo modelo)

> VACE (ICCV 2025, ali-vilab) unifica text-to-video, reference-to-video, video-to-video y edición
> enmascarada bajo UN modelo Wan. Es el ControlNet del video: la palanca de control fuerte.

## Qué resuelve
Antes necesitabas un modelo por tarea (uno para pose, otro para inpaint, otro para ref). VACE
("Video All-in-one Creation and Editing") mete todas las condiciones por el mismo frame de control:
referencia, pose, profundidad, máscara, o combinación. Una imagen/secuencia de control + una máscara
que dice **dónde** aplicar → el modelo respeta la geometría y rellena el resto.

## Las cuatro señales (y para qué)
| Señal | Qué fija | Caso de uso |
|---|---|---|
| **Reference (R2V)** | Identidad/apariencia desde imágenes ref | Mantener al mismo personaje entre tomas |
| **Pose** (DWPose/OpenPose) | Esqueleto/movimiento del cuerpo | Animar avatar siguiendo una coreografía grabada |
| **Depth** | Estructura 3D de la escena | Cambiar estilo/textura sin romper geometría |
| **Mask (MV2V)** | Región editable vs intocable | Convertir solo el personaje en robot, fondo intacto |

- **Combinables**: Depth + Pose juntos dan giros 360° suaves (estructura + esqueleto coherentes).
- **Máscara = aislamiento de estilo**: pintas la región a editar; lo de fuera se preserva pixel a
  pixel (inpaint/outpaint temporal → ver [[201-video-inpainting-outpainting]]).

## Cómo se construye el "control video"
El input no es solo el control: es **control frames + máscara** empaquetados. En ComfyUI:
1. Extraer la señal del video fuente (DWPose para pose, Depth Anything para profundidad).
2. `WanVaceToVideo` recibe: prompt, imágenes ref, control frames, máscara, longitud.
3. `TrimVideoLatent` recorta el latente sobrante (VACE a veces extiende de más).
4. Sampler Wan estándar.

## 1.3B vs 14B
- **14B**: 720p, más detalle y estabilidad. Lo de producción.
- **1.3B**: rápido/barato para iterar el control antes de gastar en el 14B.
- VRAM: el 14B pide GPU gorda (≥24GB cómodo, más con resolución/frames altos) → ver
  [[122-wan-video-self-hosting-2026]] para sizing.

## Detalles que muerden
- **Calidad de la señal manda**: pose mal extraída (DWPose pierde una mano) → artefacto en el output.
  Limpia/valida la señal de control ANTES de gastar la generación.
- **Máscara con feather**: bordes duros de máscara → costura visible. Suaviza el borde y deja overlap
  temporal entre frames para coherencia.
- **Ref vs Pose pueden pelear**: si la ref tiene una pose muy distinta a la pose de control, el modelo
  negocia y degrada ambas. Ref y control coherentes entre sí.
- **No abuses de señales**: 4 condiciones a la vez sobre-restringen y matan el movimiento natural.
  Usa la mínima señal que logre el objetivo.
- **Longitud**: VACE hereda el límite de ventana de Wan (~5s). Para más, encadenar con
  [[200-video-extension-looping]].

## VACE vs CameraCtrl
- **CameraCtrl** ([[197-camera-control-cameractrl-motionctrl]]) controla la **cámara**.
- **VACE** controla **sujeto/escena/estructura**. Son ortogonales y se combinan: trayectoria de
  cámara + pose del sujeto en la misma generación.

Cruza con [[122-wan-video-self-hosting-2026]] y [[139-controlnet-ipadapter-serving-consistencia]].
