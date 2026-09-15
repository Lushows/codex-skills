# 356 · Calls/RTC: LiveKit, Daily, Agora, SFU, grabación y voice-agents en vivo

> Cuando pasas de "datos realtime" ([[352-websockets-sse-webrtc-deep]]) a **media** (voz/video
> de muchos), WebRTC P2P no escala: necesitas un SFU y, casi siempre, una plataforma.

## Por qué SFU (no mesh ni MCU)
- **Mesh P2P**: cada peer envía a todos → ancho de banda O(n²). Muere a >~4–6 participantes.
- **MCU**: el server mezcla todo en un stream → barato para el cliente, **carísimo en CPU** (transcoding) y añade latencia.
- **SFU** (Selective Forwarding Unit): el server **reenvía** streams sin transcodificar; cada cliente sube 1 vez, baja N. Estándar 2026. Con **simulcast** (el emisor sube varias resoluciones) el SFU elige la capa por receptor según su red → no penalizas a todos por el más lento.

## Plataformas (no construyas el SFU)
| Plataforma | Modelo | Fuerte en | Nota |
|---|---|---|---|
| **LiveKit** | open-source + Cloud | control, **voice-agents**, self-host posible | Agents framework de primera clase |
| **Daily** | managed | latencia (first-hop ~13ms), 75+ PoPs [no verificado] | DX simple, grabación incluida |
| **Agora** | propietario (SD-RTN) | red global madura, calidad a escala masiva | infra "out of the box", menos control |
| **100ms / Cloudflare Calls** | managed | precio, edge | alternativas según región |

Costo orientativo 2026 [no verificado]: **LiveKit** agent-minute ~$0.01 + WebRTC ~$0.0004–0.0005/min; suele salir más barato que el stack CAI+ASR de Agora (~$0.0265) para cargas de **agente IA puro**. Self-host LiveKit elimina el por-minuto a cambio de operar el SFU + TURN.

## Voice-agents en vivo (el caso STUDIO/agente)
El loop **STT→LLM→TTS** ([[61-voice-agents-telephony]]) montado sobre un SFU en vez de telefonía:
- **LiveKit Agents**: el agente entra a la **room** como un participante más; recibe el track de audio del usuario, corre STT→LLM→TTS y publica su propio track de audio (y opcional video de avatar).
- **Barge-in**: detecta voz del usuario (VAD) y **corta el TTS** al instante; sin esto el agente "habla encima". El SFU te da los tracks separados para hacerlo.
- **Presupuesto de latencia**: STT parcial (streaming) + LLM con first-token rápido + TTS streaming; objetivo <800ms de turn-around para que se sienta natural.
- **Avatar parlante**: el track de video del agente puede ser un avatar generado en tiempo real → integra con [[147-avatar-realtime-streaming-baja-latencia]] (lip-sync de baja latencia publicado como track WebRTC en la room).

## Grabación
- **Server-side (composite)**: el SFU/egress graba la mezcla (LiveKit Egress, Daily recording) → un MP4/HLS, robusto, no depende del cliente. Default para compliance.
- **Per-track**: graba cada participante por separado → reedición posterior, pero más storage.
- **Egress a S3/R2**: configura el destino; para grabaciones largas, HLS segmentado > un MP4 monolítico.
- **Consentimiento + legalidad**: graba solo con aviso; en LatAm aplica protección de datos — registra el consentimiento.

## TURN: el peaje invisible
~10–20% de usuarios tras **NAT simétrico** no conectan P2P/SFU directo y necesitan **relay TURN** (todo su media pasa por tu server → ancho de banda real). Las plataformas managed lo incluyen; self-host = montar **coturn** dimensionado al ancho de banda, no solo a CPU.

## Calidad adaptativa y red
- **Simulcast + SVC**: el emisor sube capas (p.ej. 1080p/540p/180p); el SFU baja a cada receptor la capa que su ancho de banda aguante. SVC (escalable en un solo stream) es más eficiente que simulcast clásico donde lo soporten codecs (VP9/AV1).
- **Congestion control**: el SFU usa estimación de ancho de banda (REMB/GCC, TWCC) para no saturar; expón métricas de `packetLoss`/`jitter`/`rtt` por participante para diagnosticar.
- **Codec**: VP8/H.264 = compatibilidad; **AV1** = mejor compresión a igual calidad (CPU mayor) — útil en bajo ancho de banda.
- **Audio primero**: degrada video antes que audio; en una llamada, audio entrecortado mata la UX más que video pixelado. Prioriza el track de audio en congestión.

## Signaling, tokens y entrada a la room
- **JWT firmado por sala**: generas en tu backend un token con `room`, `identity` y grants (`canPublish`/`canSubscribe`/`canPublishData`); el cliente lo usa para entrar. Nunca expongas el API secret al frontend.
- **Webhooks de room**: `participant_joined/left`, `room_finished`, `egress_ended` → tu backend reacciona (facturación por minuto, disparar grabación, limpiar estado).
- **TTL del token corto** + refresh: un token filtrado da acceso a la sala; minimiza la ventana.

## Gotchas
1. **Mesh "porque es P2P y gratis"** colapsa pasando de 4–6 personas → SFU desde el día 1 si esperas grupos.
2. **Sin simulcast**, un participante con mala red degrada la calidad de todos.
3. **TURN olvidado**: funciona en tu oficina (NAT amable), falla para ~15% de usuarios reales.
4. **Grabación client-side** se pierde si el cliente crashea → server-side egress para lo que importa.
5. **Voice-agent sin barge-in** se siente robótico; el VAD + corte de TTS es el 80% de la sensación de fluidez.
6. **Self-host LiveKit** ahorra por-minuto pero ahora operas SFU + TURN + escalado — pésalo contra Cloud según volumen ([[30-finops-gpu]] mentalidad de costo).

Cruza con [[147-avatar-realtime-streaming-baja-latencia]], [[61-voice-agents-telephony]] y [[352-websockets-sse-webrtc-deep]].
