# 147 · Avatar en tiempo real: streaming y baja latencia

> Un avatar conversacional en vivo no falla por la calidad del modelo, falla por la LATENCIA acumulada.
> El objetivo es que el avatar empiece a hablar < 1-1.5 s después de que el usuario calla. Todo se
> diseña hacia atrás desde ese número.

## El pipeline conversacional y su presupuesto de latencia
```
🎤 audio usuario → STT → LLM → TTS → lip-sync → 📺 video
```
Cada eslabón suma. Presupuesto típico para "primera palabra/primer frame del avatar":

| Etapa | Latencia objetivo | Palanca para bajarla |
|---|---|---|
| VAD / fin-de-turno | 100-300 ms | endpointing agresivo, semantic turn-detection |
| STT (streaming) | ~100-200 ms tras fin | ASR en streaming, no batch al final |
| LLM (TTFT) | 200-500 ms | streaming token-a-token, modelo pequeño/rápido |
| TTS (TTFB audio) | 100-300 ms | TTS streaming por chunks, no esperar la frase entera |
| Lip-sync (primer chunk) | 100-400 ms | modelo realtime (MuseTalk), chunk de audio corto |
| Transporte (WebRTC) | 50-150 ms | WebRTC, no HLS/HTTP polling |

Suma realista: **0.8-1.8 s**. Pasar de ~2 s rompe la sensación de conversación.

## La regla de oro: TODO en streaming, nada en batch
El error mortal es esperar a que cada etapa termine antes de empezar la siguiente. El LLM emite tokens
→ se agrupan en **frases parciales** → TTS sintetiza esa frase → su audio se trocea en **chunks** →
el lip-sync genera frames de esos chunks → WebRTC los empuja. El avatar ya habla la primera frase
mientras el LLM aún escribe la tercera. Cruza con [[40-voz-tiempo-real]] para el lado STT/TTS/barge-in.

## Chunking de audio para el lip-sync
- El lip-sync realtime consume audio en **ventanas cortas** (p. ej. 0.2-1 s de mel) y emite los frames
  de video correspondientes. Chunk pequeño → menor latencia pero más overhead y riesgo de costuras en
  los bordes de ventana. Chunk grande → más fluido pero más lag inicial. Ajusta empíricamente.
- **MuseTalk 1.5** es la opción realtime de referencia: 30fps+ en V100, inpainting latente, **MIT**
  (comercial). Detalle del modelo en [[146-lipsync-a-fondo-wav2lip-musetalk-latentsync]].
- **SadTalker** NO es realtime nativo: genera el clip completo desde una foto (segundos-minutos por
  clip). "SadTalker streaming" = pre-generar respuestas o trocear el render, no streaming verdadero.
  Para vivo de verdad, SadTalker no califica; úsalo para respuestas pregrabadas/asíncronas.
- Modelos de difusión (LatentSync, Diff2Lip) **no** son para vivo: demasiado lentos. Solo offline.

## Warm-state: el modelo SIEMPRE caliente
Realtime y serverless-escala-a-0 son **incompatibles** para la sesión activa. No puedes pagar un cold
start de minutos a mitad de conversación.
- Mantén un worker **warm** (mín. 1 réplica encendida) por sesión o pool de sesiones.
- Carga modelo, detector de cara y el **avatar base** (la cara cropeada/encodeada) en VRAM **antes**
  de que empiece a hablar. El crop de la cara se hace una vez, no por frame.
- Cruza con [[112-execution-timeout-cold-start-economics]] y [[113-network-volume-modelos-grandes]]:
  el volumen mata la re-descarga, pero el warm mata el lag de carga a VRAM.

## WebRTC para el video (no HTTP)
- El video del avatar se entrega por **WebRTC** (baja latencia, sub-segundo, peer-to-peer/SFU). HLS/DASH
  añaden 2-10 s de buffer → inservibles para conversación. HTTP polling/chunked = jitter inaceptable.
- Patrón: el worker GPU produce frames → encoder (H.264/VP8) → SFU (LiveKit, mediasoup, Janus) → cliente.
- Sincroniza audio y video con timestamps comunes: el lip-sync ya alinea boca↔audio, pero el transporte
  debe mantener A/V sync o el avatar se "desfasa". WebRTC lo maneja con RTP timestamps.

## Trade-offs honestos
- **Calidad vs latencia**: difusión (LatentSync) se ve mejor pero es offline; MuseTalk se ve "bien" y
  es vivo. Para conversacional, fluidez > nitidez perfecta. El usuario perdona algo de boca, no perdona
  2 s de silencio.
- **Costo**: un worker warm es GPU encendida 24/7 por sesión → caro. Mitiga con pool compartido,
  auto-apagado por inactividad (con margen) y batch de varias caras por GPU si el modelo lo permite.
- **Barge-in**: si el usuario interrumpe, hay que **cortar** TTS + lip-sync + stream a media frase.
  Diseña cancelación en cada etapa, no solo en el LLM. Cruza con [[40-voz-tiempo-real]].
- **Telefonía/agentes de voz**: si el canal es teléfono (sin video), el avatar sobra; el mismo pipeline
  STT→LLM→TTS aplica sin la rama de lip-sync. Cruza con [[61-voice-agents-telephony]].

## Stack mínimo viable (realtime, comercial)
STT streaming + LLM rápido (TTFT bajo) + TTS por chunks + **MuseTalk 1.5 warm** + **LiveKit/WebRTC**.
Presupuesto < 1.5 s, todo en streaming, worker siempre caliente, cancelación en cascada para barge-in.

Cruza con [[40-voz-tiempo-real]], [[61-voice-agents-telephony]] y [[146-lipsync-a-fondo-wav2lip-musetalk-latentsync]].
