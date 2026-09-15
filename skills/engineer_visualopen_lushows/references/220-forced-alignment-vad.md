# 220 · Forced alignment (MFA) + VAD (Silero): timestamps y segmentación

> Saber QUÉ se dijo no basta; para subtítulos al frame, recortar clips por frase o sincronizar gestos
> necesitas saber CUÁNDO se dijo cada palabra. Eso son timestamps precisos — y Whisper solos no bastan.

## Dos herramientas, dos trabajos
- **VAD (Voice Activity Detection)**: marca dónde **hay** voz vs silencio. Rápido, ligero. Sirve para
  cortar chunks sin partir palabras, quitar silencios y alimentar al ASR en bloques limpios.
- **Forced alignment**: dado el audio **y su transcripción**, alinea cada palabra/fonema a su instante
  exacto. Resuelve el "cuándo" con resolución de milisegundos.

## Silero VAD — el VAD de cabecera
Modelo diminuto (PyTorch/ONNX), corre en CPU en tiempo real. Aísla regiones de voz para que los límites
de chunk **nunca caigan sobre habla activa** — clave para WhisperX y para segmentar reels largos
([[114-video-segmentado-largo-clip]]).
```python
import torch
model, utils = torch.hub.load('snakers4/silero-vad', 'silero_vad')
(get_speech_timestamps, _, read_audio, _, _) = utils
wav = read_audio('voz.wav', sampling_rate=16000)
ts = get_speech_timestamps(wav, model, sampling_rate=16000)  # [{'start':..,'end':..}, ...]
```

## Alineación: WhisperX vs MFA
| | WhisperX | Montreal Forced Aligner (MFA) |
|---|---|---|
| Base | Whisper + wav2vec2 align + Silero/pyannote VAD | GMM-HMM clásico con diccionario de fonemas |
| Precisión de borde | buena, pero a veces decenas de ms off | **superior**: ~22-28 ms error medio, F₁@20ms ≈ 65%, resolución 10 ms |
| Requisitos | solo audio (transcribe y alinea) | audio **+** transcripción + diccionario por idioma |
| Coste de setup | bajo, una pasada | mayor: léxico/idioma, pero más exacto |

Veredicto 2026: para el 90% (subtítulos, recortes por frase) **WhisperX** ([[134-whisper-faster-whisperx-self-hosting]])
es suficiente y simple. Cuando necesitas precisión sub-20 ms (lip-sync fino, fonética, doblaje) usa
**MFA**: en benchmarks supera a WhisperX y MMS en todos los umbrales de tolerancia.

## Hands-on (MFA)
```bash
conda install -c conda-forge montreal-forced-aligner
mfa model download acoustic spanish_mfa
mfa model download dictionary spanish_mfa
mfa align corpus/ spanish_mfa spanish_mfa salida/   # corpus = wav + .lab/.txt por archivo
# salida: TextGrid con intervalos palabra y fonema
```

## Para qué lo usas en el avatar
- **Subtítulos quemados** al frame exacto (ffmpeg + tiempos → ASS/SRT).
- **Recorte por frase/escena**: cortar un clip largo en segmentos donde no parta palabras
  ([[114-video-segmentado-largo-clip]]).
- **Sincronizar gestos/cambios de plano** a límites de frase.
- **Limpieza**: VAD elimina silencios largos antes de generar (menos frames, menos costo).

## Detalles que muerden
- **Idioma del diccionario**: MFA necesita léxico del idioma correcto; palabras OOV (nombres, marcas)
  hay que añadirlas al diccionario o fallan en alineación.
- **Transcripción debe coincidir**: forced alignment asume que el texto **es** lo dicho. Si Whisper
  alucinó o faltan palabras, la alineación se desfasa — verifica el ASR primero.
- **VAD agresivo recorta consonantes**: Silero con umbral alto come oclusivas iniciales/finales; afina
  `threshold` y `min_silence_duration_ms`.
- **Sample rate**: ambos esperan 16 kHz mono; remuestrea antes.

Cruza con [[134-whisper-faster-whisperx-self-hosting]] y [[114-video-segmentado-largo-clip]].
