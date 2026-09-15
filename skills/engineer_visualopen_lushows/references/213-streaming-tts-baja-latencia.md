# 213 · TTS streaming de baja latencia (first-byte para voz-agente y avatar)

> En un agente de voz el usuario no espera el audio completo: espera *empezar a oír*. La métrica no es
> RTF, es **TTFA** (Time To First Audio). Bajo 300ms suena conversacional; arriba de 800ms suena roto.

## La métrica que manda
**TTFA / TTFB** = ms desde que entra el texto hasta que sale el **primer chunk** reproducible. El cliente
arranca playback al recibir ese chunk → el resto se sintetiza mientras ya suena. La latencia total deja de
importar; importa el primer paquete y que el resto llegue **más rápido de lo que se consume** (sin underrun).

## Números reales (2026, [verificado])
| Modelo | TTFB / first-packet | Nota |
|---|---|---|
| **Kokoro** | ~97ms baseline (300-800ms sobre red pública) | El más rápido; voz fija, sin clonado |
| **Orpheus** | ~187ms promedio | Buen balance velocidad/expresividad |
| **CosyVoice2** | ~150ms primer paquete | Streaming bidireccional; decoder NAR por chunks penaliza el first-packet |

Regla: para conversación natural apunta a **TTFB < 300ms**. Lo demás es ingeniería de chunking y red.

## Por qué chunking importa
Un decoder **autoregresivo** puede emitir audio token a token → primer chunk casi inmediato.
Un decoder **NAR flow-matching** (CosyVoice2) opera sobre **bloques**: necesita acumular un chunk antes de
emitir → mejor calidad, peor first-packet. Trade-off central al elegir engine para agente vs para batch.

## Arquitectura de streaming (las dos fronteras)
```
LLM (stream de tokens) ──► TTS (stream de audio) ──► cliente (playback al primer chunk)
        ▲ frontera 1: no esperes la frase completa del LLM         ▲ frontera 2: no esperes el audio completo
```
1. **Texto en streaming**: alimenta el TTS con los primeros tokens/clauses del LLM. No esperes el punto final.
   Segmenta por *clause boundary* (coma, conjunción) no por frase entera.
2. **Audio en streaming**: el TTS emite chunks de 50-250ms; el cliente los encola en un jitter-buffer pequeño.
3. **Jitter-buffer**: 1-2 chunks de colchón. Más → latencia; menos → riesgo de underrun (corte audible).

## Detalles que muerden
- **Frontera de frase = mayor fuente de latencia**: si esperas a que el LLM cierre la oración, sumas 500ms+.
  Sintetiza por cláusula y acepta prosodia ligeramente peor en los empalmes.
- **El TTFB de red ≠ TTFB del modelo**: Kokoro hace 97ms local pero 300-800ms sobre internet. Co-localiza
  TTS y orquestador, o usa WebSocket persistente; HTTP nuevo por frase mata todo el presupuesto.
- **Underrun > latencia**: un corte audible es peor que 50ms extra. Dimensiona el buffer para no vaciarse
  nunca bajo carga, no para el caso ideal.
- **Warm worker obligatorio**: cold start de serverless (cargar pesos a VRAM) destruye el first-packet.
  Mantén el modelo caliente; ver [[112-execution-timeout-cold-start-economics]].
- **realtimetts** (lib Python) ya envuelve varios engines con interfaz de stream — buen punto de partida.

## Sizing
Kokoro (~82M) corre en CPU o GPU mínima → ideal para voz-agente barata. CosyVoice2/Orpheus piden GPU 8-12GB
pero dan clonado/expresión. Para avatar realtime, el TTS debe ir *por delante* del lip-sync, no a la par.

Cruza con [[40-voz-tiempo-real]] y [[147-avatar-realtime-streaming-baja-latencia]].
