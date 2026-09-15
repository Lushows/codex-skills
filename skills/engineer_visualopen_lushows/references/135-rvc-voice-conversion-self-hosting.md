# 135 · RVC / Voice Conversion self-hosting (cambiar el timbre, no clonar TTS)

> Voice Conversion (VC) toma audio que YA existe y le cambia el **timbre** a otra voz, preservando
> entonación/ritmo del original. Distinto de clonar TTS (texto → voz). Para doblaje, locuciones y voz-a-voz.

## VC vs TTS-clone — cuál usar
| Necesidad | Herramienta |
|---|---|
| Generar voz **desde texto** con la voz de alguien | TTS-clone (ver [[05-tts-voice-cloning-2026]]) |
| Reentonar/cambiar timbre de una **locución ya grabada** (preservar emoción/timing del actor) | **VC (RVC / so-vits / Seed-VC)** |
| Cantar con otra voz (singing voice conversion) | so-vits-svc / Seed-VC |
| Voz-a-voz en vivo (avatar, stream) | **Seed-VC realtime** o RVC realtime |

VC gana cuando ya tienes una buena interpretación (actor, tú mismo) y solo quieres el timbre destino: conserva la prosodia humana que el TTS aplana.

## RVC (Retrieval-based Voice Conversion) — el estándar de facto
Arquitectura: extrae contenido con **HuBERT/ContentVec** + estima pitch (**RMVPE**) → decoder tipo VITS reconstruye con el timbre destino. El **retrieval top-1 sobre un índice (FAISS)** de la voz objetivo reduce el *tone leakage* (que se filtre el timbre original).
- **Entrena con poco**: ~10 min de audio limpio del target bastan para un modelo decente; más datos = más fidelidad.
- **Índice** (`.index` FAISS) se genera junto al modelo (`.pth`); en inferencia el `index_rate` controla cuánto se apoya en el retrieval (más índice = más parecido al target, menos al input).
- **Pitch (f0)**: `RMVPE` es el default robusto (evita el "muted sound"). Alternativas: `crepe` (preciso, lento), `pm`/`harvest` (clásicos). Para hombre↔mujer ajusta transposición en semitonos (`f0_up_key`).

### Entrenar un modelo RVC (WebUI, RVC v2)
1. Audio limpio del target (mono, sin música/ruido; usa un separador tipo UVR5 antes).
2. Preprocesado → extracción f0 (RMVPE) → extracción de features HuBERT.
3. Entrenar (`.pth`) + construir índice FAISS (`.index`).
4. Inferencia: input wav → modelo + índice → wav con timbre destino.

## so-vits-svc y Seed-VC — alternativas
- **so-vits-svc**: predecesor de RVC, fuerte en **singing voice conversion**. Más pesado de entrenar; RVC lo superó en facilidad/calidad para habla. Útil aún para canto donde quieres control fino.
- **Seed-VC** (`Plachtaa/seed-vc`): **zero-shot** (sin entrenar): clona con 1-30 s de referencia, mantiene toda la waveform de referencia como contexto → reproduce breathiness, vocal fry, clicks. Soporta VC, singing VC y **tiempo real** (delay de algoritmo ~300 ms + ~100 ms device). Cuando NO quieres entrenar por voz → Seed-VC primero.

## VC vs TTS-clone en latencia/producción
- **RVC inferencia**: rápida, GPU modesta (4-8 GB) sirve; el cuello es f0 (`crepe` lento, `rmvpe` ok). Batch para vídeo largo.
- **Tiempo real**: Seed-VC ~300 ms algoritmo / RVC tiene GUI realtime; suficiente para avatar/stream, no para conversación ultra-baja-latencia.
- **Pipeline doblaje**: STT (ver [[134-whisper-faster-whisperx-self-hosting]]) → traducir/editar → TTS-clone o re-grabar → **VC para uniformar timbre** → mux. O directamente VC sobre la locución original si solo cambias la voz, no el idioma.
- **Calidad**: la entrada manda — separa voz de música/ruido (UVR5) antes de VC o el modelo "aprende" el ruido. Modelo entrenado (RVC) > zero-shot (Seed-VC) en fidelidad si tienes datos del target.

## Sizing
- Entrenar RVC: GPU 8-12 GB cómodo; ~10-30 min de audio. Inferencia: 4-8 GB.
- Cachea HuBERT/ContentVec + RMVPE (cientos de MB) en Network Volume [[113-network-volume-modelos-grandes]].
- Legal/ético: clonar voz de terceros sin consentimiento es problemático. Usa voces propias o licenciadas.

Cruza con [[05-tts-voice-cloning-2026]] (cuándo generar desde texto en vez de convertir) y [[116-voice-clone-produccion-retencion]] (consistencia de voz en producción y retención de identidad sonora).
