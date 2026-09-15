# 119 · Avatares talking-head self-hosted (mapa 2026)

> Qué modelo open eliges para "foto + audio → video que habla", según VRAM, licencia y si necesitas gestos de cuerpo o solo boca.

## Dos familias (no las mezcles)
- **Audio-driven full-body / portrait con gestos** (diffusion/DiT): mueven cara, torso, manos y cámara. Caros en VRAM, lentos, pero los únicos que dan presencia "humana". LongCat-Avatar, OmniHuman-1.5, MultiTalk, EMO2, Sonic, Hallo3, EchoMimicV2.
- **Lip-sync sobre video/foto existente** (inpainting de boca): solo reescriben la región labial. Baratos, rápidos, sin gestos. MuseTalk, Wav2Lip, SadTalker (intermedio: añade pose de cabeza leve).

Si ya tienes un video del presentador y solo quieres doblarlo → familia 2. Si partes de UNA foto y quieres que cobre vida → familia 1.

## Tabla comparativa
| Modelo | VRAM (720p aprox) | Licencia | Lip-sync | Gestos cuerpo | Velocidad | Cuándo usarlo |
|---|---|---|---|---|---|---|
| **LongCat-Video-Avatar 1.5** (Meituan/MeiGen) | 16GB INT8 · 24-48GB fp16 · 80GB 4K | **MIT** ✅ comercial | Alto (Whisper enc.) | Sí (full body, multi-persona) | Lento (DiT, video largo) | Producción open #1; clips largos 1-4min, multi-GPU |
| **OmniHuman-1.5** (ByteDance) | — (sin pesos públicos) | Cerrada / solo API ❌ | Muy alto | Sí (MLLM+DiT, multi-char) | API | Calidad tope, pero **no self-hosteable** [no verificado: sin release de pesos a jun-2026] |
| **MultiTalk** (MeiGen, NeurIPS'25) | ~24-48GB | Apache-2.0 ✅ | Alto | Sí (conversación multi-persona) | Medio-lento | Varias personas hablando en una escena (audio por pista) |
| **EMO2** (Alibaba HumanAIGC) | alta (no liberada del todo) | Restrictiva / parcial ⚠️ | Muy alto | Sí (manos+cara expresiva) | Lento | Gestos de manos expresivos; revisar disponibilidad de pesos |
| **Sonic** (Tencent) | ~16-24GB | No-comercial (research) ⚠️ | Alto (global audio) | Pose de cabeza, poco cuerpo | Medio | Retrato expresivo audio-driven; ojo licencia |
| **Hallo3** (Fudan, CVPR'25) | ~24-40GB (DiT) | Solo investigación ⚠️ | Alto | Dinámico (pose, fondo) | Lento | Retratos muy dinámicos; uso research/PoC |
| **EchoMimicV2** (AntGroup, AAAI'25) | ~12-16GB | Apache-2.0 ✅ | Alto (landmark-cond) | Medio cuerpo (half-body) | Medio | Half-body con manos, VRAM razonable, comercial OK |
| **MuseTalk 1.5** (Tencent) | ~6-8GB | MIT ✅ | Medio-alto (256px boca) | No | **Tiempo real 30fps+** (V100) | Doblar video existente barato y rápido |
| **SadTalker** | ~6-8GB | Apache-2.0 ✅ | Medio | Solo cabeza (leve) | Rápido | PoC barato desde foto; calidad modesta |
| **Wav2Lip** | ~4GB | Solo investigación ⚠️ | Medio (boca borrosa) | No | Muy rápido | Baseline/fallback; ojo licencia no-comercial |

> Verifica licencia en el repo antes de producción: varios (Sonic, Hallo3, Wav2Lip, EMO2) son **research-only** y NO permiten uso comercial sin permiso. MIT/Apache son los seguros: LongCat-Avatar, MultiTalk, EchoMimicV2, MuseTalk, SadTalker.

## Fit por GPU
- **24GB (RTX 4090/A10G/L4)**: MuseTalk, SadTalker, EchoMimicV2, Sonic, LongCat-Avatar **INT8** a resolución baja. Familia lip-sync corre sobrada.
- **48GB (A6000/L40S)**: LongCat-Avatar fp16 720p, MultiTalk, Hallo3 en clips medios. Punto dulce calidad/costo.
- **80GB (A100/H100)**: LongCat-Avatar 4K / clips largos, multi-persona pesado, batch. Necesario para 1080p+ con gestos.

## Gotchas
- **LongCat-Avatar 1.5** trae DiT cuantizado **INT8** que baja la barrera a ~16GB; para ≥720p o video largo igual quieres 48GB+. INT8 + multi-GPU para escalar. Usa Whisper como audio encoder (mejor multilingüe que wav2vec2). Ver [[111-longcat-avatar-runpod-produccion]].
- **OmniHuman-1.5 es API-only** (ByteDance no liberó pesos): si lo necesitas, es premium/fallback, no self-hosted → [[112-execution-timeout-cold-start-economics]] no aplica.
- Los DiT (LongCat, Hallo3, MultiTalk) generan **video segmentado**: el clip largo se hace por ventanas con identity-preservation (LongCat usa "pseudo last frame"); vigila el drift de identidad entre segmentos.
- Modelos grandes (44GB+) → monta Network Volume para matar el cold-start: [[113-network-volume-modelos-grandes]].
- "Lip-sync alto" en familia 2 (MuseTalk/Wav2Lip) es solo la BOCA; si el resto del rostro no se mueve, se ve robótico → combínalo con LivePortrait para microexpresión [[120-liveportrait-expression-transfer]].

Cruza con [[02-open-models-catalog-2026]], [[111-longcat-avatar-runpod-produccion]], [[01-audio-avatar-pipeline]].
