# 191 · Pose full-body: DWPose (2D) y SMPL-X (3D) para avatar de cuerpo

> Para animar un avatar de cuerpo entero necesitas saber dónde están cuerpo, manos y cara. Dos niveles:
> keypoints 2D (esqueleto en la imagen) y malla paramétrica 3D (cuerpo+manos+cara en el espacio).

## Los dos niveles
| | 2D whole-body | 3D expresivo (mesh) |
|---|---|---|
| Qué da | keypoints (x,y,conf): body+foot+face+hands | parámetros de pose+forma+expresión → malla 3D |
| Modelos 2026 | **DWPose**, **RTMPose**, ViTPose+ | **SMPL-X** (modelo); estimadores: SMPLer-X/SMPLest-X |
| Uso | ControlNet-pose (OpenPose), guía de generación 2D | retarget a rig 3D, avatar volumétrico, AR |

- **DWPose**: whole-body 2D destilado en dos etapas; cubre cuerpo, pies, **cara y manos** en un pase.
  Tamaños `t/s/m/l` (velocidad↔precisión). Es la fuente estándar del mapa OpenPose para ControlNet. [verificado]
- **ViTPose/ViTPose+**: ViT plano que iguala o supera arquitecturas multiescala; backbone fuerte para 2D.
- **SMPL-X**: modelo paramétrico que une cuerpo + **manos (MANO)** + **cara (FLARE/expresiones)** en una
  malla. Los estimadores **SMPLer-X / SMPLest-X** son foundation models (hasta ViT-Huge, ~4.5M instancias)
  que regresan SMPL-X desde una imagen. [verificado]

## Por qué manos y cara importan tanto
Un avatar parlante de cuerpo entero se cae en dos sitios: **manos** (dedos cruzados o derretidos delatan al
instante) y **cara** (lip-sync + expresión). DWPose/SMPL-X los modelan explícitamente; un pose-estimator de
solo-cuerpo (17 keypoints COCO) no te sirve para gesto fino ni boca.

## Decidir el nivel
- **Generar/controlar video 2D** (ControlNet-pose, animate-anyone-likes) → DWPose 2D. Suficiente y rápido.
- **Avatar 3D real, retarget a un rig, vista libre, AR** → SMPL-X (necesitas profundidad y orientación que
  el 2D no da).
- **Cuerpo + lip-sync + gesto** (caso avatar parlante) → DWPose para el cuerpo/manos en el control 2D, y la
  cabeza/boca del módulo de avatar; SMPL-X si el pipeline es 3D.

## Conceptos que muerden
- **Confidence por keypoint**: keypoints de baja confianza (mano tapada) generan poses imposibles si los
  fuerzas. Filtra por umbral; deja que el generador interpole en vez de anclar a ruido.
- **Coherencia temporal**: pose por-frame tiembla (jitter). Suaviza la trayectoria de keypoints (filtro
  temporal / One-Euro) antes de mandarla al ControlNet, o el avatar vibra.
- **Convención de esqueleto**: OpenPose, COCO y MMPose ordenan/numeran keypoints distinto. El ControlNet-pose
  espera **el formato OpenPose**; alimentar otro orden retuerce el esqueleto. DWPose ya exporta a OpenPose.
- **Ambigüedad de profundidad en 3D**: desde 1 cámara, SMPL-X tiene ambigüedad escala/profundidad; multi-vista
  o priors la reducen. No esperes métrica perfecta de monocular.

## Ingeniería de serving
- **VRAM**: DWPose/RTMPose ligeros (caben en 6-8GB), corren en tiempo real en Ada. SMPLer-X-Huge pesa más
  (≥12-16GB) por el ViT grande.
- **Throughput**: 2D va a decenas de fps; SMPL-X es más lento (regresión de malla). Para video largo, 2D si
  basta el control.
- **Pipeline avatar**: estima pose → suaviza → render del control map → generador. No metas la pose cruda.
- **Almacenamiento**: keypoints como JSON/npy con conf; parámetros SMPL-X como `.npz` (pose, betas, expr).

## Errores que muerden
- Forzar keypoints de baja confianza (mano ocluida) → poses imposibles; filtra por umbral y deja interpolar.
- Mandar pose cruda sin suavizado temporal → avatar que vibra frame a frame.
- Alimentar orden COCO/MMPose al ControlNet-pose que espera OpenPose → esqueleto retorcido (DWPose ya exporta OpenPose).
- Esperar profundidad métrica fiable de SMPL-X monocular → hay ambigüedad escala/profundidad; usa multi-vista o priors.

Cruza con [[121-pose-landmarks-audio-encoders-avatar]] y [[202-fullbody-talking-avatar]].
