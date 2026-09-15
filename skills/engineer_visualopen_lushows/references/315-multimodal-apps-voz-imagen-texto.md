# 315 · Apps multimodales — orquestar voz + imagen + texto + video

> Un producto multimodal NO es un modelo gigante que lo hace todo: es un pipeline que enruta cada
> modalidad al modelo correcto y cose las salidas. El caso STUDIO/agentes vive aquí.

## La arquitectura real: router + especialistas
Pocas veces un solo modelo gana en todo. Patrón ganador = **un LLM orquestador** que decide qué
especialista invoca por modalidad (vía tool-use, ver [[313-tool-use-function-calling-patterns]]):

```
Usuario (voz) → STT (Whisper) ─┐
Usuario (imagen) → VLM ─────────┼→ LLM orquestador → decide acción
Usuario (texto) ───────────────┘        │
                                         ├→ TTS → audio de respuesta
                                         ├→ difusión img/video → media
                                         └→ texto → UI
```

## Modalidades de entrada
| Entrada | Modelo | Notas |
|---|---|---|
| **Voz→texto** | Whisper / STT streaming | streaming si quieres barge-in (interrumpir al bot) |
| **Imagen→texto** | VLM (ver [[222-vllm-multimodal-vlm]]) | describe, OCR, razonamiento visual |
| **Texto** | LLM | el hub que orquesta todo |
| **Video→texto** | VLM por frames + ASR del audio | muestrea frames, no proceses todos |

## Modalidades de salida
| Salida | Modelo | Latencia que importa |
|---|---|---|
| **Texto** | LLM (stream, ver [[312-streaming-ui-tokens-sse]]) | TTFT |
| **Voz** | TTS (streaming chunked) | first-audio-byte |
| **Imagen** | difusión | full-render, no streamea bien |
| **Video** | pipeline segmentado | ver [[55-pipeline-produccion-video-ia]] |

## El cuello: latencia percibida
Una cadena STT→LLM→TTS suma latencias en serie. Trucos:
- **Streaming en cascada**: empieza el TTS con la primera frase del LLM mientras este sigue generando.
  No esperes la respuesta completa para hablar.
- **Barge-in**: si el usuario habla, corta el TTS y reinicia STT. Requiere VAD (voice activity detection).
- **Frames, no video**: para entender un clip, muestrea 1 frame/seg y pasa al VLM; no decodifiques todo.
- **Modelo barato de primera línea**: clasifica intención con un modelo chico antes de invocar el caro.

## Coser las modalidades: un contexto, IDs estables
- Pasa **referencias**, no blobs gigantes, entre etapas: sube la imagen a R2/S3, pasa la URL al VLM.
- Mantén un **session/turn-id** que ate audio-in, transcript, media-out → para debug y memoria.
- **Sincronía A/V** en avatares: el lip-sync exige que el audio TTS y el video se generen del mismo texto
  y se alineen por timestamps (caso lip-sync STUDIO).

## Detalles que muerden
- **Costo se dispara** con media: cachea transcripciones y descripciones de imagen (ver [[316-cost-control-llm-apps]]).
- **Errores parciales**: si el TTS falla, entrega el texto igual — degradación elegante, no pantalla en blanco.
- **Formatos**: normaliza audio a 16kHz mono para STT; usa ffmpeg como capa única de conversión.
- **Privacidad**: voz e imagen son datos sensibles → retención mínima, borra blobs tras procesar.

Cruza con [[222-vllm-multimodal-vlm]] y [[55-pipeline-produccion-video-ia]].
