# 61 — Voice agents y telephony (LatAm)

Un agente de voz telefónico = loop de baja latencia **STT → LLM → TTS** sobre audio real-time, con detección de
turnos y *barge-in* (el usuario interrumpe y el TTS se corta). El reto no es el LLM — es el presupuesto de latencia y la calidad degradada del canal telefónico.

## Plataformas 2026 (BYOK = bring-your-own-key)
- **Vapi** — orquestación $0.05/min, real BYOK ~$0.23-0.33/min; endpointing default alto (~1450ms). Para validar rápido <10k min/mes.
- **Retell AI** — infra $0.055/min; all-in $0.07-0.31/min; endpointing ~700ms; Twilio nativo.
- **Bland** — pila telefónica vertical todo-en-uno, menos control de modelos.
- **Pipecat** (OSS, Daily) — framework Python, el más rápido (~300ms endpointing); Pipecat Cloud ~$0.01/min.
- **LiveKit Agents** — orquestación sobre WebRTC, escala alta (~$0.01/min). Migra a LiveKit/Pipecat al superar ~10k min/mes.
- **Twilio + ConversationRelay** — Twilio maneja STT/TTS/sesión y te conecta por WebSocket; tú mandas texto.

## Twilio Voice / SIP
TwiML controla la llamada. Verbo clave: `<Connect><Stream>` (Media Streams, chunks cada 20ms por WS) o
`<Connect><ConversationRelay>`. SIP trunking conecta tu PBX/carrier para números locales LatAm.
```xml
<Response><Connect>
  <ConversationRelay url="wss://tu-app.com/relay" ttsProvider="ElevenLabs" language="es-CO"/>
</Connect></Response>
```

## Audio telefónico
El canal PSTN es **μ-law (PCMU), 8kHz, mono, base64**. Pierdes todo arriba de ~4kHz → el STT sufre con nombres
propios, números y acentos regionales. Configura STT para 8kHz telefónico (modelos "phone" de Deepgram/AssemblyAI), no estudio.

## Presupuesto de latencia (sub-800ms fin-de-habla → inicio-de-audio del bot)
<1.5s es producción aceptable, >3s "roto". Reparto: endpointing 200-500ms, STT final ~100ms, LLM TTFT 200-400ms
(streaming de tokens), TTS TTFB ~100-300ms. **Streaming en cada etapa es obligatorio.** **Turn detection:** VAD
(Silero) + modelos semánticos (LiveKit turn-detector, smart endpointing Pipecat). **Function calling:** ejecuta el
tool **en paralelo a un filler** ("déjame revisar...") porque 1.5s en silencio = llamada caída.

## WhatsApp voice notes vs llamada real-time
Una nota de voz NO es full-duplex: es asíncrona. La transcribes (Whisper/`audioTranscriber.js`), respondes texto o
TTS, sin presupuesto de latencia ni barge-in. **Mucho más simple/barato — el 90% del caso para BIO-SETA/GastroWhats.** La llamada real-time solo si necesitas atención telefónica en vivo.

## Gotchas
1. **μ-law mata el STT de números/direcciones** — pide confirmación deletreada de datos críticos (cédula, dirección).
2. **Latencia compuesta engaña** — mide end-to-end con audio real, no por componente.
3. **Barge-in mal hecho** — corta el buffer de TTS *y* el de Twilio al detectar habla, o el bot habla encima.
4. **Costo BYOK ≠ headline** — presupuesta $0.20-0.35/min real (STT+LLM+TTS).
5. **Acentos LatAm** — `language="es-CO"`/`es-MX` explícito; el `es` genérico degrada.
6. **WebSocket reconnect** — si cae a media llamada, Twilio no reintenta; maneja `stop`/`mark` events + timeout de gracia.

**Fuentes:** retellai.com/blog/vapi-ai-review · softcery.com/lab (voice agent platforms 2026) · twilio.com/docs/voice (ConversationRelay).
