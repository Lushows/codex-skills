# 56 — Sound design, audio & voice interfaces

La capa sonora — la dimensión más descuidada del diseño y la de mayor potencial emocional. Un sonido bien diseñado confirma, tranquiliza y construye marca; uno mal diseñado expulsa. **Léelo para UI sound, branding sónico, VUI o agentes de voz** (el audio de WhatsApp en GASTROWHATS). Pareja de 18 (AI UI), 16 (a11y), 27 (media).

## 1. UI sound design (la capa sónica)

**Cuándo usar sonido (cada sonido debe ganarse su lugar):** feedback/confirmación (soft click cuando el feedback visual es insuficiente o no se mira) · alertas/errores (error suena distinto del éxito *por diseño*) · notificaciones (identificable sin mirar — el "knock" de Slack) · delight (envío/pago/logro, más personalidad porque ocurre poco).
**Craft:** **sutil no molesto** (volumen bajo el nivel de "te saca de la tarea") · **significativo no decorativo** · **duración corta** (clicks 80-300ms, todo <~500ms) · **frecuencia agradable** (evita agudos >4-5kHz sostenidos que se vuelven "grating"; timbres cálidos — marimba/madera — envejecen mejor) · **consistencia/sistema sónico** (paleta tonal coherente: éxito/error/notificación se oyen como hermanos — es un *design token* sonoro) · **mutable y opcional** (control siempre, recuerda la preferencia).
**Cuándo NO:** **silencio por defecto en web** (no inicies sonido sin gesto del usuario — UX + política del navegador) · acciones de alta frecuencia (cada tecla/scroll → fatiga) · cuando el sonido sería la *única* señal (excluye sordos y dispositivos en silencio) · contextos públicos/oficina.

## 2. Sonic branding / identidad de audio

El logo sonoro = equivalente auditivo del logo visual: un **mnemónico** de 1-3s (Netflix "ta-dum", Intel 5 notas). El audio entra por una vía emocional/mnemónica más directa que lo visual — marcas con identidad sónica consistente alcanzan ~96% de reconocimiento de audio (vs ~7% sin estrategia).
**Cómo construirla:** **audio logo** (mnemónico corto repetible) · **brand sound palette** (instrumentación/escala/textura consistentes en app/ads/IVR/asistente/UI sounds) · **voice characteristics** (tono/acento/personalidad de las voces TTS/locución) · **conexión con la marca visual** (un brand cálido/artesanal no usa bleeps sintéticos). Para GASTROWHATS/BIO-SETA (hongos/bienestar/calma): timbres orgánicos, cálidos, naturales; nada clínico ni agresivo.

## 3. Voice UX / VUI

Diseñar para los oídos, no los ojos. Reto central: **sin affordance visual** (el usuario no "ve" las opciones, las mantiene en memoria).
**Principios:** **brevedad** (<30s hablados, idealmente mucho menos; el texto que se lee bien suele ser demasiado largo para oírse) · **persona de voz** consistente (cálida, regional — personas localizadas aumentan confianza) · **confirmación** (*implícita* repitiendo lo entendido "Anoto Melena de León, 2 frascos…"; *explícita* sí/no solo para acciones críticas como pago) · **error recovery/turn-taking** (clarification específica "¿cápsulas o polvo?", graceful degradation a texto/botones, context retention — nunca "no entendí" en bucle) · **discoverability** (revela opciones progresivamente).
**Voz vs pantalla:** voz gana en manos/ojos ocupados, accesibilidad, entrada rápida; pantalla gana en listas, comparaciones, datos densos, precisión. Lo mejor suele ser **multimodal.**

## 4. Conversacional & audio para messaging (WhatsApp/GASTROWHATS)

Patrón del agente con voz (mapea a `audioTranscriber.js` + `messageHandler.js`):
```
Usuario envía nota de voz → descargar audio (Cloud API) → STT (Whisper) → procesar con Claude (mismo pipeline que texto) → responder
```
**Decisiones clave:**
- **Responder en texto por defecto** a una nota de voz (más rápido de consumir, accesible, búscable, revisable). Voz solo si el usuario lo pide.
- **Transcripción visible como confirmación/red de seguridad:** "Entendí: '¿tienen Cordyceps en polvo?'" — confirmación VUI + seguro ante errores de STT (acentos/ruido/jerga de productos).
- **Voz en ordering:** capta el pedido hablado pero **confirma por texto** los datos críticos (producto/cantidad/dirección/total) antes de cerrar. **Nunca cierres una venta solo con audio no confirmado.**
- **Escalado a humano:** tono/urgencia de la voz puede gatillar handoff al operador (encaja con `operatorNotifier.js`), pasándole la transcripción.
- **Agente multimodal (texto+voz+imagen):** unifica todo a texto interno (transcribe audio, describe imagen con Vision) → pipeline único. Tu stack ya lo hace (`claudeAnalyzer.js` + `audioTranscriber.js`).

## 5. Web Audio & implementación (dashboard)

**Web Audio API vs `<audio>`:** `<audio>` para pistas largas/streaming; **Web Audio API** para sonidos cortos tipo sample con control (UI sounds, visualizadores, generativo).
**Política de autoplay (regla de oro):** desde 2018 el `AudioContext` arranca **`suspended`** — no suena hasta un **gesto del usuario**. Crea/reanuda dentro de un handler de interacción:
```js
const ctx=new AudioContext(); let buffer;
fetch("/sounds/success.webm").then(r=>r.arrayBuffer()).then(a=>ctx.decodeAudioData(a)).then(b=>buffer=b);  // preload+decode una vez
function playSuccess(){ if(ctx.state==="suspended")ctx.resume();
  const src=ctx.createBufferSource(); src.buffer=buffer;          // BufferSource es de un solo uso
  const gain=ctx.createGain(); gain.gain.value=0.4;               // volumen contenido
  src.connect(gain).connect(ctx.destination); src.start(); }
```
**Gotchas:** un `AudioBufferSourceNode` es de un solo uso (crea uno por reproducción) · precarga/decodifica una vez · para muchos sonidos pequeños usa un **audio sprite** (un archivo, segmentos por offset).
**Librerías:** **howler.js** (all-rounder, maneja autoplay/unlock/sprites/fallbacks) · **tone.js** (scheduling/síntesis) · standardized-audio-context (consistencia cross-browser).
**Formatos:** **WebM/Opus** (mejor calidad/tamaño) + **fallback MP3** (Safari fue tardío con Opus).

## 6. Accesibilidad, ética & 2026

**Accesibilidad (no negociable):** **transcripciones y captions siempre** (captions incluyen hablante + efectos de sonido) · **nunca info solo por audio** (duplica con visual/textual) · **sin autoplay con sonido >3s** sin pausa/stop (WCAG 1.4.2, axe lo marca) · controles de volumen/mute etiquetados (`role="switch"`).
**Ética:** silencio respetado, sonido **mutable siempre** · nada jarring/manipulador (sonidos para crear ansiedad/FOMO) · **voice cloning**: el **consentimiento** es el eje; declara cuando una voz es sintética.
**Tendencias 2026:** voice agents conversacionales voz-a-voz (con detección de tono/urgencia) · spatial/3D audio (contexto direccional, útil en a11y de baja visión) · **sonification** (datos como sonido para ciegos) · AI voices más naturales (con deber de marcado/consentimiento).

## Audio/voice anti-patterns — blacklist
autoplay con sonido al cargar (UX + WCAG + bloqueado por el navegador) · sonido no muteable o sin control de volumen · **información solo por audio** (excluye sordos/silencio) · sonidos jarring/chillones o largos (>500ms en micro-interacciones) · sonido en acciones de alta frecuencia (cada tecla/scroll) · sonido decorativo sin significado · sin transcripciones/captions en audio/video · paleta sónica inconsistente (éxito/error/notificación sin parentesco tonal) · VUI con respuestas largas, sin confirmación de acciones críticas, o "no entendí" en bucle · **cerrar pedido/pago solo con audio no confirmado por texto** · voice cloning sin consentimiento ni transparencia · sonido manipulador (ansiedad/FOMO).
**Para GASTROWHATS:** transcribe la nota, **confirma por texto lo entendido**, responde en texto por defecto, guarda la transcripción para el operador, nunca cierres venta sin confirmar producto/cantidad/dirección/total en texto.
