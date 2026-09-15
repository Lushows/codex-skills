# 121 · Pose, landmarks y audio-encoders para avatar

> Las señales de condicionamiento (pose, landmarks faciales, features de audio) deciden el sync y la naturalidad; elegir mal el encoder arruina el lip-sync por mucho que el generador sea bueno.

## Las tres señales de control
Un avatar talking-head se condiciona con (1) **audio features** → mueven la boca; (2) **pose/keypoints** → mueven cuerpo y cabeza; (3) **face landmarks** → alinean y guían la región facial. Cada generador ([[119-avatares-talking-head-self-hosted-2026]]) consume alguna combinación.

## Audio encoder: wav2vec2 vs Whisper
| Encoder | Entreno | Multilingüe | Para lip-sync |
|---|---|---|---|
| **Wav2Vec2** | self-supervised, sobre todo inglés | débil fuera de inglés | features fonéticas decentes en EN; falla en español/acentos |
| **Whisper (large-v3) encoder** | 680k h supervisado, 99 idiomas | fuerte | bocas más suaves, robusto a español LatAm y acentos |

- La elección **no es cosmética**: el embedding del audio ES la señal que mapea a forma de boca. Audio mal codificado → desincronía o boca "genérica".
- Tendencia 2026: los modelos buenos migraron a **Whisper encoder** (LongCat-Avatar 1.5 lo usa) justamente por el multilingüe. Si tu contenido es en **español**, prioriza generadores con Whisper; wav2vec2-only suele desincronizar.
- Solo necesitas el **encoder** de Whisper (features por frame), no el decoder de transcripción. Se alinea a la tasa de frames del video (ver abajo).
- Phoneme-aware encoders (PASE y derivados) mejoran el sync atando features a fonemas [no verificado: adopción en repos de producción aún limitada].

## Pose: DWPose vs OpenPose vs MediaPipe
| Detector | Qué da | Velocidad | Uso típico |
|---|---|---|---|
| **DWPose** | whole-body: cuerpo+manos+cara, robusto | rápido (RTMPose) | estándar actual para condicionar pose en diffusion (ControlNet/Pose Guider) |
| **OpenPose** | body+hands+face, clásico | más lento | legado; muchos ControlNet entrenados con su formato |
| **MediaPipe** | landmarks ligeros, CPU-friendly | muy rápido | preview/tracking en tiempo real, móvil |

- En pipelines DiT (EchoMimicV2, half/full body) la **secuencia de pose de DWPose** entra a un **Pose Guider** que la lleva a espacio latente y guía el render. Manos y cara de DWPose dan los gestos finos.
- DWPose > OpenPose en manos (menos jitter), por eso domina en avatares con gesticulación.

## Face landmarks y detección
- **InsightFace** (buffalo_l / antelopev2): detección + alineación + embedding de identidad. Lo usan LivePortrait, IP-Adapter, y casi todo el stack. Si falla la detección, **no hay animación** (gotcha de [[120-liveportrait-expression-transfer]]).
- **face-alignment** (1adrianb, FAN): 68/3D landmarks, útil para crop y normalización de pose de cabeza.
- Landmarks editables (EchoMimic) permiten **dirigir** la boca/cara manualmente en vez de solo inferir del audio → control híbrido.

## Alineación frames ↔ audio (donde se rompe el sync)
- El audio sale a un sample-rate (16kHz para Whisper/wav2vec2); el video corre a fps (24/25/30). Hay que **remuestrear las features de audio a tasa de frames**: por cada frame de video tomas la ventana de features de audio correspondiente.
- Errores típicos: **off-by-one / drift** acumulado → la boca se adelanta o atrasa al final del clip. Verifica que `len(audio_features) ≈ n_frames` tras el resampleo.
- En **video segmentado** (clips largos por ventanas, LongCat/MultiTalk), realinea audio↔frames **por segmento**; un desfase por ventana se nota en los cortes.
- ffmpeg para fijar fps y extraer audio limpio antes de codificar features evita la mitad de los bugs de sync.

## Por qué importa el encoder (resumen)
Generador bueno + encoder malo = lip-sync malo. El generador solo "renderiza" la señal que recibe: si el audio encoder no captura fonemas (idioma equivocado) o el audio está mal alineado a frames, no hay arquitectura que lo salve. Invierte en (a) Whisper para multilingüe, (b) alineación frame-exacta, (c) DWPose para gestos limpios.

Cruza con [[01-audio-avatar-pipeline]], [[35-vision-encoders-vlms]], [[119-avatares-talking-head-self-hosted-2026]].
