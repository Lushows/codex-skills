# 134 · Whisper / faster-whisper / WhisperX self-hosting (STT + word-timestamps)

> Transcribir audio open-source: del `openai-whisper` lento al stack de producción.
> Para subtítulos y sync de avatar lo que importa NO es solo el texto, son los **timestamps por palabra**.

## El árbol de decisiones
Cuatro implementaciones del mismo modelo Whisper (pesos de OpenAI), distinto motor/extras:

| Impl | Motor | Velocidad vs openai | VRAM (large-v3) | Word TS | Diarización | Cuándo |
|---|---|---|---|---|---|---|
| `openai-whisper` | PyTorch | 1x (baseline) | ~10 GB fp16 | aprox (DTW) | no | referencia/debug |
| `faster-whisper` | CTranslate2 | ~4x, menos RAM | ~10 GB fp16 · 1.5-4 GB int8 | sí (opcional) | no | **default producción** |
| `WhisperX` | faster-whisper + wav2vec2 + VAD | ~4x + batching 12x | ~10 GB + align | **forzado (preciso)** | sí (pyannote) | subtítulos / sync |
| `distil-whisper` | compat. faster-whisper | ~5.8x, 51% menos params | ~2-6 GB | sí | no | inglés rápido/barato |

## faster-whisper (CTranslate2) — el caballo de batalla
- Reimplementación en CTranslate2: misma precisión, ~4x más rápido, menos VRAM. Cuantización **int8** baja large-v3 a ~1.5-4 GB casi sin perder WER → cabe en GPU pequeña/CPU.
- Tamaños: `tiny`(39M) `base`(74M) `small`(244M) `medium`(769M) `large-v3`(1.55B) `large-v3-turbo`(809M, distil de large-v3, casi tan preciso, ~6 GB fp16).
- `compute_type`: `float16` (GPU normal), `int8_float16` (mixto), `int8` (CPU o VRAM mínima).
```python
from faster_whisper import WhisperModel
m = WhisperModel("large-v3", device="cuda", compute_type="float16")
segs, info = m.transcribe("audio.ogg", language="es", word_timestamps=True, vad_filter=True)
for s in segs:
    for w in s.words: print(w.start, w.end, w.word)
```
- `vad_filter=True` (Silero) corta silencios → menos alucinación y menos cómputo. En releases recientes VAD y feature-extraction ~3x más rápidos en CPU.

## WhisperX — para subtítulos y sync de avatar
Pipeline: VAD → transcribe (faster-whisper, **batched**) → **forced alignment** con wav2vec2 → (opcional) diarización pyannote.
- **Batching** sube el throughput hasta ~12x sobre large-v3 secuencial: clave para transcribir vídeos largos barato.
- Los timestamps por palabra de WhisperX son **a nivel de fonema/wav2vec2**, mucho más precisos que el DTW interno de Whisper → labios/subtítulos no se desfasan.
- Diarización (`who spoke when`) requiere token de pyannote (gated en HF) y suma VRAM. Para 1 sola voz, desactívala.
```bash
whisperx audio.wav --model large-v3 --language es --batch_size 16 \
  --align_model WAV2VEC2_ASR_LARGE_LV60K_960H --diarize --highlight_words True
```

## Español
- Whisper es fuertemente multilingüe; `large-v3` y `turbo` rinden bien en ES. **Fija `language="es"`** (no autodetectar) → evita que frases cortas o con anglicismos se transcriban como inglés.
- distil-whisper original es **solo inglés**; existen distil multilingües pero verifica cobertura ES antes [no verificado caso a caso]. Para ES de producción: `large-v3` o `large-v3-turbo` en faster-whisper.
- El alignment de WhisperX necesita un `align_model` wav2vec2 **del idioma**; hay uno español en HF — sin él, los word-timestamps caen a inglés.

## Sizing y despliegue
- `large-v3` fp16 ≈ 2.87 GB de pesos; runtime ~10 GB con activaciones/batch. `int8` → 1.5-4 GB. Una T4/L4/A10 sobra; CPU sirve para `small`/distil en lotes nocturnos.
- Cachea los pesos en Network Volume para no re-bajarlos en cold start (ver abajo). El modelo wav2vec2 de align también pesa cientos de MB → cachéalo.
- Para tiempo real (dictado, voz-a-voz) usa `tiny`/`base`/distil con chunks pequeños; large-v3 no es para latencia sub-segundo en GPU modesta.

Cruza con [[01-audio-avatar-pipeline]] (los word-timestamps alimentan el lip-sync), [[40-voz-tiempo-real]] (STT de baja latencia) y [[114-video-segmentado-largo-clip]] (transcribir/subtitular vídeo largo por segmentos con batching). Cachea pesos según [[113-network-volume-modelos-grandes]].
