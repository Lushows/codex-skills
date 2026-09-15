# 202 · Avatar de cuerpo completo hablando (no solo la cara)

> El talking-head mueve labios y cejas; deja el cuerpo congelado y se ve a un maniquí.
> El cuerpo completo añade gesto, torso, manos y postura sincronizados al audio → presentador real.

## Por qué es otra clase de problema
Un head-avatar (Wav2Lip, SadTalker) sólo edita el rectángulo de la cara. Cuerpo completo significa
generar **frames enteros** con coherencia de identidad, ropa, manos y fondo mientras el audio dirige
el gesto. Eso multiplica VRAM, duración del clip y riesgo de artefactos (manos rotas, ropa que hierve).

## Las dos rutas en 2026

| Ruta | Modelo | Entrada | Qué resuelve |
|---|---|---|---|
| **Audio → cuerpo directo** | **OmniAvatar-14B** (ZJU+Alibaba, jun-2025) | 1 imagen + audio + prompt | Lip-sync + gesto adaptativo en un solo paso, sobre Wan2.1-T2V-14B |
| **Audio multi-persona** | **MultiTalk** | imagen + N pistas de audio + prompt | Conversación de varios hablantes, cada uno con su lip-sync |
| **Pose → vídeo (2 etapas)** | **MimicMotion** (Tencent) | imagen + secuencia de pose | Cuerpo guiado por pose; el audio entra vía un motion-gen aparte ([[203-motion-dance-generation]]) |
| **Comercial cerrado** | OmniHuman-1 (ByteDance) | imagen + audio | SOTA de realismo, **no open** — sólo referencia/API |

OmniHuman-1 sigue siendo paper+API en 2026, no hay pesos open. [no verificado] que existan checkpoints públicos.

## Recomendación práctica
- **Presentador hablando a cámara** → **OmniAvatar-14B**. Base Wan2.1-T2V-14B (~28GB de pesos), audio
  vía Wav2Vec2 + módulo Audio Pack inyectado por capas temporales en el DiT. Una imagen + un WAV → vídeo.
- **Dos personas dialogando** → **MultiTalk** (una pista de audio por hablante).
- **Coreografía/movimiento amplio donde el habla es secundaria** → genera la pose con un motion-model
  y renderiza con **MimicMotion**, no con un audio-avatar.

## Lo que muerde
- **VRAM**: un base de 14B en fp16 no cabe holgado en 24GB con clips largos. Apunta a **A100 40/80GB o
  H100**; en 24GB toca cuantizar/recortar resolución y frames. Cruza con la matriz de [[01-matriz-gpu-cuda-torch]].
- **Manos y dedos**: el punto débil. Sube resolución, baja CFG, o post-procesa sólo la región de manos.
- **Duración del clip**: estos DiT generan ventanas cortas; clips largos = generación segmentada con
  solape + anclaje de identidad para que no derive la cara entre segmentos.
- **Deriva de identidad** entre segmentos: re-inyecta la imagen de referencia en cada ventana.
- **Audio feature**: Wav2Vec2 quiere audio limpio y a su sample-rate; ruido/clipping arruina el lip-sync.

## Pose → vídeo: MimicMotion en detalle
Cuando el habla es secundaria y lo que manda es el movimiento amplio, MimicMotion (Tencent) renderiza
una imagen guiada por secuencia de pose con **confidence-aware pose guidance** (pondera keypoints por
su confianza → menos artefactos donde la pose es dudosa).
- **VRAM**: U-Net de 16 frames arranca en **8GB**, pero el **VAE decoder pide 16GB** (opción: decoder en CPU).
  Comparativa: MusePose 16GB a 512², 28GB a 768² con 48 frames. Dimensiona por el VAE, no por el U-Net.
- El audio NO entra aquí: la pose la genera un motion-model aparte ([[203-motion-dance-generation]]).

## Sizing y serving
- Pesos OmniAvatar ~28GB base + encoders → **Network Volume** obligatorio para no re-bajar en cada frío
  ([[113-network-volume-modelos-grandes]]); apunta `HF_HOME` al volumen.
- Handler de producción con **warm-state** (modelo cargado una vez en VRAM, no por job) y progreso por
  segmento; cliente con **submit/poll** y timeout holgado porque cada segmento tarda minutos.
- **Costo**: clip de presentador de pocos segundos en A100/H100 son varios minutos de GPU facturada;
  prototipa a baja resolución/fps y sube sólo al validar. Cruza con [[30-finops-gpu]].
- **Fallback**: si el open no clava manos/identidad para entrega final, cae a OmniHuman-1 vía API y
  reserva el self-host para volumen alto. Decide por calidad medida (FVD/CLIP), no por intuición.

## Decisión rápida
Habla a cámara → OmniAvatar-14B · diálogo multi-persona → MultiTalk · movimiento amplio → motion-gen +
MimicMotion · realismo máximo sin importar coste/cierre → OmniHuman API.

Cruza con [[119-avatares-talking-head-self-hosted-2026]] y [[191-pose-estimation-fullbody-deep]].
