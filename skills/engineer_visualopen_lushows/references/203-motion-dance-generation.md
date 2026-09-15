# 203 · Generar movimiento / baile desde música o texto (motion-gen)

> Generar **el movimiento** (no el vídeo) a partir de música o texto: salida de poses/SMPL.
> Es el paso de arriba del pipeline; luego un renderer (MimicMotion) lo convierte en píxeles.

## Qué es y qué NO es
Motion-gen produce **secuencias de pose** (esqueleto, SMPL, keypoints) — no un MP4 fotorrealista.
Sirve para: coreografía sincronizada al beat, gesto corporal de un avatar, animación de personaje.
El render final es otro modelo ([[202-fullbody-talking-avatar]]). Mantener separadas las dos etapas
te da control: editas la pose antes de pagar el render caro.

## Dos familias

| Familia | Entrada | Modelos | Nota |
|---|---|---|---|
| **Texto → movimiento** | prompt NL | **MoMask**, **TMR**, T2M-GPT | MoMask usa cascada residual con tokens discretos → buena dependencia larga |
| **Música → baile** | audio/beat | **EDGE**, **Bailando**, **LODGE**, **FineDance**, **SoulDance** (ICCV-2025) | EDGE es el caballo de batalla; SoulDance añade modelado jerárquico holístico |

Trabajos 2025/26 a vigilar: **SoulDance** (3D dance alineado a música, ICCV-2025), **OpenDance/OpenDanceNet**
(mejor FID en AIST++/OpenDanceSet), **MotionRAG-Diff** (retrieval-augmented para clips **largos**, apoyado
en el encoder de MoMask). Datasets de referencia: **AIST++** (baile), **HumanML3D** (texto→movimiento).

## Cómo elegir
- **Avatar que gesticula al hablar** → no necesitas baile completo; un motion-gen ligero o el propio
  gesto adaptativo de OmniAvatar basta. Reserva dance-gen para coreografía real.
- **Coreografía sincronizada a una canción** → **EDGE** (sólido y open) o **SoulDance** si quieres
  holístico 3D y lo último.
- **Movimiento desde guion textual** → **MoMask** (rápido, tokens discretos, editable).
- **Clips largos sin que el baile colapse** → **MotionRAG-Diff** (retrieval) o LODGE (jerárquico).

## Lo que muerde
- **Métricas, no ojo**: se evalúan con **FID_k/FID_m**, diversidad, **PFC** y alineación rítmica sobre
  AIST++/OpenDanceSet. No te fíes de un solo clip bonito.
- **Beat-align ≠ realismo**: un modelo puede pegar al beat y aun así moverse como robot. Mira FID además del ritmo.
- **Salida es pose, falta el render**: presupuesta la **segunda** GPU-pasada (motion → vídeo). El cuello
  de botella de costo suele estar en el render, no en el motion-gen (que es barato y corre en GPU modesta).
- **Formato de salida**: SMPL vs keypoints 2D/3D. Tu renderer (MimicMotion, AnimateAnyone) espera un
  formato concreto de pose/ControlNet → convierte antes, no después.
- **Pies que patinan** (foot-skating): artefacto clásico; PFC lo mide. Modelos recientes lo mitigan, los viejos no.

## Tokens discretos vs difusión continua
- **MoMask / T2M-GPT**: codifican el movimiento en **tokens discretos** (VQ + cascada residual). Rápido,
  editable, buena dependencia larga. Ideal texto→movimiento y para que retrieval (MotionRAG-Diff) reutilice
  su encoder. Riesgo: cuantización pierde matiz fino.
- **EDGE / difusión continua**: genera la trayectoria directamente, mejor expresividad del baile, más caro.
- Para clips **largos** el problema es la deriva: LODGE (jerárquico) y MotionRAG-Diff (recupera fragmentos
  reales y los cose) son las dos vías que evitan que el baile colapse a los pocos segundos.

## Sizing y serving
- Motion-gen es **barato**: el esqueleto es ligero, corre en GPU modesta (no necesita 40/80GB). El gasto
  real está en el **render** posterior. No sobre-dimensiones la GPU de esta etapa.
- Pesos pequeños → cabe hornearlos en la imagen Docker; no siempre hace falta Network Volume aquí
  (sí en el render, [[113-network-volume-modelos-grandes]]).
- **Editabilidad**: la gran ventaja de separar etapas es que puedes recortar/retimear la pose (o corregir
  foot-skating) **antes** de pagar el render. Trátalo como un asset intermedio versionable.

## Pipeline típico
```
música/texto → motion-gen (EDGE/MoMask) → secuencia de pose (SMPL/keypoints)
            → [editar/validar pose] → render pose-guided (MimicMotion) → vídeo → super-res ([[206-video-superres-temporal]])
```

Cruza con [[202-fullbody-talking-avatar]] y [[191-pose-estimation-fullbody-deep]].
