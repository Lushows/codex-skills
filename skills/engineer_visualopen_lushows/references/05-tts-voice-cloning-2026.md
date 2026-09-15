# 05 — TTS open-source y clonación de voz (2026)

> Para el flujo "voz de WhatsApp": STT (Whisper) → LLM → **TTS** → audio de salida. Esta ref cubre la pieza TTS.
> Verifica licencia ANTES de usar en producción comercial — varias de las "mejores" son non-commercial.

## Catálogo con licencia (lo que importa para producción)

| Modelo | Params | Licencia | Clonación zero-shot | es-CO / multilingüe | Nota |
|---|---|---|---|---|---|
| **Kokoro** (`hexgrad/Kokoro-82M`) | 82M | **Apache-2.0** ✅ | **NO** (voces pre-hechas, "voicepacks" tensoriales) | en/es/fr/it/pt/zh/ja/hi | Corre en **CPU**, ~10× realtime. El más liviano. Sin clonación. |
| **Chatterbox** (Resemble AI) | 0.5B | **MIT** ✅ | **SÍ** (~10s ref) | EN nativo; multilingüe en `Chatterbox-Multilingual` (23 idiomas, incl. **es**) | ~6GB VRAM. Control de **exageración/emoción** (`exaggeration`). Watermark Perth. |
| **F5-TTS** | ~0.3B | **CC-BY-NC-4.0** ⛔ (non-commercial) | **SÍ** (~5-15s ref, excelente) | en/zh base; finetunes comunitarios es | Calidad alta, rápido. **NO usar comercial sin acuerdo.** |
| **XTTS-v2** (Coqui) | ~0.4B | **Coqui Public Model License (non-commercial)** ⛔ | **SÍ** (~6s ref) | **17 idiomas incl. español** | Coqui cerró; el modelo sigue en HF. Streaming ~200ms. Legado pero usable. |
| **MeloTTS** (MyShell) | pequeño | **MIT** ✅ | **NO** (multi-speaker fijo) | EN/ES/FR/ZH/JP/KR | CPU realtime. Sin clonación. |
| **Parler-TTS** (HF) | mini/large | **Apache-2.0** ✅ | NO (control por **descripción de texto** del timbre) | EN principal | Controlas voz/emoción describiéndola en prompt. |
| **Piper** (rhasspy/OHF) | tiny | **MIT** ✅ | NO (voces ONNX por idioma, incl. **es_ES/es_MX/es_AR**) | muchos idiomas | **El de borde/Raspberry Pi**. ONNX, CPU, ultraligero, latencia mínima. |
| **Fish-Speech / OpenAudio S1** | ~0.5B-4B | **Apache-2.0** (Fish-Speech 1.x) ✅ / OpenAudio variar | **SÍ** | multilingüe, top ELO (~1339 en arenas) | OpenAudio S1 es la evolución; mini es Apache. Verifica la licencia de la variante exacta. |
| **CosyVoice2-0.5B** (Alibaba FunAudioLLM) | 0.5B | **Apache-2.0** ✅ | **SÍ** | zh/en/jp/ko/yue + cross-lingual | **Streaming 150ms**, control de emoción/dialecto/instrucción. El mejor real-time open. |
| **Sesame CSM-1B** | 1B | **Apache-2.0** ✅ | conversacional (contexto multi-turno) | EN | Construido sobre Llama. Para **diálogo** de 2 hablantes, no narración suelta. |
| **Higgs Audio V2** (BosonAI) | sobre Llama-3.2-3B | **Apache-2.0** ✅ | **SÍ**, expresivo | multilingüe | Pre-entrenado en 10M+ horas. Top trending HF. Pesado (~3B+). |
| **IndexTTS-2** (Bilibili) | — | Apache-2.0 ✅ | SÍ, control duración/emoción | zh/en | Fuerte en 2026 para sync emoción. |

**Regla de oro de licencia:** **Apache/MIT = comercial OK** (Kokoro, Chatterbox, MeloTTS, Parler, Piper, Fish-Speech 1.x, CosyVoice2, CSM, Higgs). **F5-TTS (CC-BY-NC) y XTTS-v2 (Coqui non-commercial) = NO comercial.**

## Zero-shot voice cloning: cuántos segundos, calidad, es-CO

- **Referencia de audio:** Chatterbox/XTTS ~**6-10s** limpios; F5 rinde con **5-15s**. Más NO siempre es mejor: usa un clip **limpio, sin música ni ruido** (separa con UVR/`audio-separator` si hace falta — ver `01-audio-avatar-pipeline.md`), 16-24kHz, una sola voz.
- **Español Colombia:** ningún modelo open trae acento "es-CO" nativo. Opciones: (1) **clonar** con 10s de una voz colombiana real (Chatterbox/F5/Fish/Higgs lo capturan razonablemente); (2) **CosyVoice2** soporta español cross-lingual; (3) finetune comunitario de F5/XTTS en español. El timbre/acento sale del clip de referencia, no del idioma base.
- **Calidad percibida (2026, arenas/ELO):** Fish-Speech/OpenAudio ≈ Higgs V2 ≈ CosyVoice2 en la cima open; Chatterbox muy bueno y MIT. Para narración pura de pago, **ElevenLabs** sigue arriba.

## Streaming / latencia (voz en tiempo real)

- **CosyVoice2-0.5B: ~150ms first-chunk en streaming** (el mejor open para real-time). Con **TensorRT-LLM ~4× vs transformers HF**.
- **XTTS-v2:** modo streaming ~200ms time-to-first-byte.
- **Piper:** sub-realtime en CPU, ideal cuando la latencia y el costo mandan (borde).
- **Kokoro:** ~10× realtime en CPU, pero genera el clip completo (no diseñado para streaming de baja latencia conversacional).
- Para WhatsApp **no necesitas streaming**: el mensaje de voz se genera entero y se envía como archivo. Streaming solo importa en llamadas/voz en vivo.

## Prosody / emotion control

- **Chatterbox:** `exaggeration` (intensidad emocional) + `cfg_weight` (ritmo/pacing). Único open con control de exageración explícito.
- **Parler-TTS:** describe la voz en texto ("a calm male voice, slightly fast, studio quality").
- **CosyVoice2 / IndexTTS-2:** instrucciones de emoción/dialecto y control de duración.
- **F5/XTTS:** la emoción se hereda del **tono del clip de referencia** (graba la ref con la emoción deseada).

## Cuándo self-host vs API (ElevenLabs / MiniMax)

- **Self-host (Kokoro/Piper/Chatterbox/CosyVoice2):** volumen alto, costo marginal ~0, control de licencia, datos privados. Kokoro/Piper corren en CPU (sin GPU). Chatterbox/CosyVoice2 piden GPU modesta (6-8GB).
- **API premium (ElevenLabs, MiniMax):** mejor calidad/naturalidad de narración, cero deploy, `voice_id` cacheado (MiniMax clona y reusa). Pagas por carácter. **Úsalo como red de seguridad** o cuando la calidad de narración es el producto. MiniMax es fuerte multilingüe; ElevenLabs lidera naturalidad.
- **Regla:** WhatsApp transaccional (confirmaciones, respuestas del bot) → self-host (Kokoro/Piper barato). Contenido de marca/locución premium → API.

## Flujo "voz de WhatsApp" (STT → LLM → TTS)

```
audio_ogg (opus de WhatsApp)
  → ffmpeg -i in.ogg -ar 16000 -ac 1 in.wav     # 16kHz mono (lo que pide Whisper)
  → Whisper (faster-whisper / whisper.cpp) → texto_es
  → LLM (Claude) → respuesta_es
  → TTS (Kokoro es / Chatterbox clonado) → out.wav
  → ffmpeg -i out.wav -c:a libopus -b:a 32k out.ogg   # opus, lo que WhatsApp acepta
  → enviar como audio/voice note
```
- **STT:** `faster-whisper` (CTranslate2, ~4× más rápido que openai-whisper, mismo modelo `large-v3`). Para CPU/borde, `whisper.cpp`. El proyecto BIOWHATS ya usa Whisper en `src/audioTranscriber.js`.
- **Formato WhatsApp:** voz entra/sale como **OGG/Opus**. Convierte siempre con ffmpeg (Whisper quiere 16kHz wav; WhatsApp quiere opus).

## Gotchas

1. **F5-TTS y XTTS-v2 son non-commercial.** Es el error #1: son de los mejores en calidad, pero CC-BY-NC / Coqui-license. Para BIO-SETA comercial usa **Chatterbox (MIT), CosyVoice2/Fish/Kokoro (Apache)**.
2. **Kokoro y MeloTTS NO clonan voz** — son multi-speaker con voces fijas. Si necesitas "la voz de X", necesitas Chatterbox/F5/XTTS/Fish/Higgs/CosyVoice2.
3. **El acento es-CO viene del clip de referencia, no del modelo.** No esperes acento colombiano de un modelo entrenado en es-ES; clona con audio colombiano real.
4. **Audio de referencia sucio = clon sucio.** Música/ruido/segunda voz en la ref se filtran. Separa la voz (UVR/`audio-separator`) y normaliza (pyloudnorm) antes de clonar.
5. **Coqui (XTTS) está descontinuada como empresa** — el modelo sigue en HF pero sin soporte; para nuevo proyecto prefiere Chatterbox o CosyVoice2.
6. **Whisper quiere 16kHz mono.** Pasar el opus de WhatsApp directo da transcripción degradada; convierte SIEMPRE con `-ar 16000 -ac 1`.

## Fuentes
- https://www.tryspeakeasy.io/blog/open-source-text-to-speech-2026
- https://ocdevel.com/blog/20250720-tts
- https://www.digitalocean.com/community/tutorials/best-text-to-speech-models
- https://www.siliconflow.com/articles/en/best-open-source-models-for-voice-cloning
- https://funaudiollm.github.io/cosyvoice2/ · https://github.com/FunAudioLLM/CosyVoice
- https://modal.com/blog/open-source-tts
- https://github.com/resemble-ai/chatterbox · https://huggingface.co/hexgrad/Kokoro-82M
