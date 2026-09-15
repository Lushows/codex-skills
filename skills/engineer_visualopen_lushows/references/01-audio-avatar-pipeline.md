# 01 — Pipeline de audio para avatares parlantes / lip-sync

> Cómo preparar el audio que MUEVE la boca: separación de voz, encoders, alineación frames↔audio,
> evaluación de sync, y TTS open para generar la voz. Verificado 2026.

## 1. Separación de voz (por qué y con qué)

**Por qué los modelos de avatar separan la voz primero.** Los encoders de audio (Whisper, wav2vec2)
que manejan la boca se entrenaron con **voz limpia**. Música de fondo, ruido y voces solapadas meten
energía irrelevante al stream de features → la cross-attention la traduce en movimientos de boca
espurios/turbios (los labios "reaccionan" a la batería/bajo). Separar a un stem de voz limpio sube el
SNR de fonemas → lip-sync más preciso. **Es preproceso upstream, NO está dentro del modelo** — ni
LongCat/EchoMimic/MuseTalk traen separador; lo corres tú antes.

**`audio-separator`** (python-audio-separator, nomadkaraoke fork) — MIT. Wrapper CLI/Python sobre modelos
UVR. Backends **`torch` + `onnxruntime`** (`CUDAExecutionProvider`, CUDA 11.8/12.2). `pip install
"audio-separator[gpu]"`. 4 familias:
- **MDX-Net** (`.onnx`, ej. `Kim_Vocal_2.onnx`) — corre bajo onnxruntime; el workhorse vocal/instrumental.
- **VR Arch** (U-Net espectrograma).
- **Demucs** (`htdemucs`) — multi-stem (voz/batería/bajo/otro), backend torch.
- **MDXC / Mel-Band Roformer** — el más nuevo, mayor SDR (`model_bs_roformer_ep_317_sdr_12.9755`).

Pick para avatar: **Kim_Vocal_2 (MDX-Net)** por velocidad en onnxruntime, o un **Roformer** si quieres el
stem más limpio. Auto-descarga a `--model_file_dir` al primer uso.

## 2. Encoders de audio que manejan la boca

| Encoder | Qué extrae | 16kHz | Usado por |
|---|---|---|---|
| **wav2vec2** (`chinese-wav2vec2-base`, `wav2vec2-base-960h`) | repr. self-supervised, fuertes pistas fonéticas (orig. ASR EN) | **Sí, obligatorio** | LongCat-Avatar **v1.0**; EchoMimic V3 |
| **Whisper-large-v3** | features del encoder supervisado MULTILINGÜE (680k h, 99 idiomas), más suave entre idiomas | **Sí** (resamplea interno) | LongCat-Avatar **v1.5** (`--use_distill`); LatentSync; MuseTalk (whisper-tiny) |

**Confirmado:** LongCat-Avatar 1.5 subió el encoder de **wav2vec2 (v1.0) → Whisper-Large-v3 (v1.5)** por
cobertura multilingüe y "lip dynamics significativamente más suaves y naturales". wav2vec2 era pre-train
mayormente EN; Whisper es multilingüe/supervisado → esa es la razón de que v1.5 generalice mejor a no-EN.

## 3. Prep de audio (receta concreta)

- **Resample a 16kHz mono:** `y, sr = librosa.load(path, sr=16000, mono=True)`. **Pasar 44.1/48kHz
  corrompe silenciosamente el timing de fonemas.**
- **Normalización de loudness:** `pyloudnorm` (ITU-R BS.1770-4). Mide y normaliza, ej. ≈ −16 LUFS
  (estéreo) / −19 LUFS (mono); muchos pipelines van a −23 LUFS broadcast. Bloque de gating = 400ms.
- **Math de alineación frames↔audio:** a `fps` y 16kHz: **samples por frame = 16000/fps.** 25fps → 640
  samples/frame; 30fps → ≈533.3 (no entero → bucket/interpolación). Nº de frames `N = ceil(dur*fps)`;
  audio requerido = `N*(16000/fps)` samples. **Trim o zero-pad la cola** para que el nº de samples
  coincida con N frames exacto, o los últimos frames se quedan sin señal (boca congelada) o se truncan.

## 4. Señal → movimiento, y cómo evaluar el sync

El encoder produce una secuencia de features por ventana; el modelo los alinea al frame rate e inyecta
(típicamente **cross-attention** en un DiT/U-Net) → cada frame atiende al embedding de audio de ese frame
± una ventana de contexto. Eso condiciona los latentes de boca/mandíbula/cara por frame.

**Evaluación — métricas SyncNet (Chung & Zisserman):**
- **LSE-C (Confidence):** **mayor = mejor.** Video real y mejores modelos ~**7-8**; Wav2Lip ≈ 7.79 (LRS2).
- **LSE-D (Distance):** distancia embedding labio↔audio; **menor = mejor.** Bueno ~**6-8**; Wav2Lip ≈ 6.39.
- **Regla:** **LSE-C ≳ 6-7 y LSE-D ≲ 7-8** = "production-grade, casi video real". Bajo LSE-C ~3 hay
  segmentos visiblemente desincronizados.

## 5. TTS open para generar la voz (2026)

| TTS | Clonación | Licencia | Una línea |
|---|---|---|---|
| **F5-TTS** | zero-shot | **MIT** | Flow-matching no-autoregresivo → estable en párrafos; EN+ZH. **Mejor default self-host.** |
| **XTTS-v2 (Coqui)** | zero-shot ~6s ref | **non-commercial** (Coqui difunto, comunidad) | 17 idiomas, baseline clásico; deriva en pasajes largos. |
| **Kokoro** | no | **Apache 2.0** | Tiny (~82M), rápido en CPU, más natural que Piper. Bot de voz fija. |
| **MeloTTS** | no | **MIT** | Multilingüe, rápido, comercial-OK; sin clone. |
| **Chatterbox** (Resemble) | sí | **MIT** | Standout 2026, control de emoción. |

## Gotchas
1. **16kHz es no-negociable** — feeding 44.1/48kHz desplaza cada fonema.
2. **Tail padding** — si `audio_samples ≠ frames×(16000/fps)`, los últimos frames congelan o se cortan.
3. **Mismatch de encoder rompe pesos** — un checkpoint v1.5 (Whisper) no funciona con features v1.0 (wav2vec2).
4. **Sobre-separar daña** — settings Roformer agresivos quitan formantes/sibilancia → DEGRADA el lip-sync.
5. **Trampa de licencia XTTS** — non-commercial por default + Coqui difunto → para avatares comerciales usa F5-TTS (MIT)/Kokoro/MeloTTS.

**Fuentes:** github.com/nomadkaraoke/python-audio-separator · huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5 ·
github.com/bytedance/LatentSync · github.com/TMElyralab/MuseTalk · github.com/csteinmetz1/pyloudnorm ·
Wav2Lip/SyncNet arxiv.org/pdf/2008.10010
