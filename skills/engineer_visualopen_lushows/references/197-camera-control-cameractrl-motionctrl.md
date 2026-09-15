# 197 · Control de cámara en video (CameraCtrl, MotionCtrl, Wan-Fun-Camera)

> "Que la cámara haga un dolly-in mientras el sujeto gira" no se logra con prompt: se logra
> inyectando una trayectoria de cámara como condición geométrica. Tres familias lo hacen.

## El problema
El prompt textual ("camera zooms in") es ambiguo y no reproducible: el modelo improvisa el
movimiento, la velocidad y el eje. Para producción (avatar que necesita el mismo encuadre, b-roll
con dolly idéntico en 10 tomas) necesitas condicionar el movimiento de cámara de forma **numérica y
repetible**, separándolo del movimiento del sujeto.

## Las tres familias
| Método | Cómo condiciona | Precisión | Encaja en |
|---|---|---|---|
| **MotionCtrl** | Valores crudos de cámara (RT matrices) + trayectorias de objeto, modelo unificado | Media (sin pista geométrica) | AnimateDiff/SVD |
| **CameraCtrl** | **Plücker embeddings** (rayos por píxel desde pose) → señal geométrica densa, plug-and-play | Alta | AnimateDiff, módulos compatibles |
| **Wan2.2-Fun-Camera** | **Camera Control Codes** + presets (Pan/Zoom/combos) | Alta, fácil | Wan2.2 nativo |

- **MotionCtrl**: primer intento serio de separar cámara y objeto. Limita: alimenta parámetros sin
  geometría → control aproximado. Bueno para movimientos amplios, no para precisión sub-frame.
- **CameraCtrl**: convierte cada pose en **rayos de Plücker** (origen + dirección por píxel) que el
  modelo entiende como geometría real → control preciso y plug-and-play sobre el backbone.
- **Wan-Fun-Camera**: la vía pragmática 2026. Presets (Pan Up/Down/Left/Right, Zoom In/Out y
  combinaciones) sin manejar matrices a mano. Lo que querrás en el 90% de los casos.

## Trayectorias: de dónde salen
- **Presets** (Wan-Fun): eliges "Zoom In + Pan Right", listo. Cero matemáticas.
- **Pose builder** (ComfyUI `Create CameraCtrl Poses (Adv.)`): defines keyframes de pose y
  velocidad → genera la secuencia RT.
- **Extraída de un video real**: corres SLAM/COLMAP sobre un clip de referencia → poses → re-aplicas
  esa misma trayectoria a tu generación (clonar el movimiento de una toma que te gustó).

## Pipeline ComfyUI (mínimo)
1. Generar/cargar trayectoria de cámara (preset o pose builder).
2. Nodo de control (`Apply AnimateDiff+CameraCtrl` o Wan-Fun-Camera) que inyecta la condición.
3. Sampler normal. La cámara sigue la trayectoria; el sujeto sigue prompt/otros controles.

## Detalles que muerden
- **Cámara vs sujeto se pelean**: si el preset de cámara es agresivo y el sujeto también se mueve
  mucho, el modelo sacrifica uno. Para avatar parlante: cámara sutil (slow push-in), no dolly brusco.
- **FPS y nº de frames**: la trayectoria se discretiza por frame. Cambiar el nº de frames re-mapea la
  velocidad del movimiento → re-calibra si cambias la duración.
- **No es 3D real**: es condicionamiento, no render geométrico. Movimientos extremos (órbita 360°
  cerrada) revelan inconsistencias/alucinación de geometría oculta — ahí entra [[198-vace-control-video-deep]].
- **Repetibilidad**: misma trayectoria + misma seed = mismo movimiento. Guarda la trayectoria como
  asset versionado, no la regeneres "a ojo".

## Cuándo usar cuál
- Avatar/b-roll rápido en Wan → **Wan-Fun-Camera** presets.
- Necesitas precisión geométrica o clonar movimiento de un clip → **CameraCtrl** + poses extraídas.
- Pipeline legacy AnimateDiff/SVD → **MotionCtrl** o CameraCtrl según precisión.

Cruza con [[122-wan-video-self-hosting-2026]] y [[117-control-camara-movimiento-avatar-prompt]].
