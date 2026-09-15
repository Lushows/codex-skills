# 208 · Kokoro y MeloTTS self-hosted (TTS ligero, sin GPU, sin clonación)

> Cuando NO necesitas clonar una voz —solo voz natural barata y rápida— Kokoro y MeloTTS ganan.
> Corren en **CPU** a tiempo real o más, licencia **comercial OK**, y el costo marginal tiende a cero.

## El caso de uso
WhatsApp transaccional (confirmaciones, respuestas del bot, avisos) no necesita "la voz de X": necesita una voz **fija, natural, barata**. Ahí Kokoro/MeloTTS son la elección correcta — sin GPU, sin cola de jobs pesada, sin licencia non-commercial. Si el producto es locución de marca o "la voz de tu fundador", esto NO sirve (no clonan): salta a [[211-chatterbox-serving]].

## Los dos motores
| Motor | Params | Licencia | Idiomas | Clonación | Hardware |
|---|---|---|---|---|---|
| **Kokoro** (`hexgrad/Kokoro-82M`) | 82M | **Apache-2.0** ✅ | en/es/fr/it/pt/zh/ja/hi (voicepacks) | ❌ voces fijas | **CPU**, <2GB VRAM, ~real-time o más |
| **MeloTTS** (MyShell) | pequeño | **MIT** ✅ | EN(US/UK/IN/AU)/ES/FR/ZH/JP/KR | ❌ multi-speaker fijo | **CPU** real-time |

Kokoro hit #1 en TTS Arena (ene-2026) batiendo modelos 10-100× su tamaño. Arquitectura StyleTTS2 + ISTFTNet: **sin encoder ni diffusion** → genera rápido.

## Serving: el patrón ligero
Estos NO necesitan worker GPU serverless caro. Dos opciones:

1. **Proceso CPU permanente** (Render/VPS): FastAPI que carga el modelo una vez y sintetiza por request. Como corre en CPU, no pagas GPU idle. Para BIOWHATS encaja directo junto al Node.
2. **Serverless GPU** solo si el volumen es enorme y quieres latencia mínima; rara vez justifica para estos.

```
POST /tts {text, voice} → wav
  Kokoro: voice = id de voicepack (ej. 'ef_*' español, 'af_*' inglés)
  MeloTTS: voice = speaker_id del idioma
  carga modelo UNA vez (warm), sintetiza, devuelve
```

- **Warm state**: el modelo es chico → cargar a RAM es barato, pero igual cárgalo en `startup`, no por request.
- **Kokoro voicepacks**: las "voces" son **tensores** pre-hechos, no clonación. Hay packs en español; el acento es el del pack, no configurable a es-CO. [no verificado: existencia de pack es-CO específico — revisar `voices/` del repo].

## Latencia
- Kokoro: ~**real-time o más rápido en CPU** (genera el clip completo, no streaming conversacional de baja latencia).
- MeloTTS: optimizado para **inferencia real-time en CPU**.
- Para WhatsApp (archivo completo) sobra. Para voz en vivo de baja latencia, no son la mejor opción → CosyVoice2 [[210-cosyvoice-fish-speech-serving]].

## Por qué encaja en BIOWHATS
- **CPU = sin GPU serverless**: el costo y la complejidad de un worker GPU desaparecen.
- **Apache/MIT**: comercial sin asteriscos.
- Flujo: Whisper STT → Claude → **Kokoro es** → ffmpeg a opus → enviar como nota de voz (ver pipeline en [[05-tts-voice-cloning-2026]]).

## Gotchas
1. **No clonan voz.** Si alguien pide "que suene como la grabación que mandé", estos no pueden — necesitas Chatterbox/F5/CosyVoice2.
2. **Kokoro genera el clip entero**, no es streaming de baja latencia; no lo metas en una llamada en vivo esperando 150ms.
3. **Acento es del pack/speaker fijo**, no ajustable a es-CO. Para colombiano real hay que clonar (otro motor).
4. **Misratio CPU**: en CPUs muy débiles (free tier saturado) puede caer bajo real-time con textos largos; trocea o sube el plan.

Cruza con [[05-tts-voice-cloning-2026]].
