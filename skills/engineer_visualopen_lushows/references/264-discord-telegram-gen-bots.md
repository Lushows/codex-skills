# 264 · Bots de generación en Discord/Telegram (cola + entrega async de media)

> Un bot de generación es Midjourney-en-tu-Discord: comando → job de 30-1200s → media de vuelta en el chat.
> El reto no es el modelo, es el desfase entre "el chat espera respuesta YA" y "la GPU tarda minutos".

## Por qué Discord/Telegram para un generador
Cero frontend: el chat ES la UI. Distribución viral (un server con 10k personas), comunidad, y el patrón de
"reacciona para variar/upscale" es nativo. Para STUDIO/bots de marca: canal privado donde el equipo genera
sin abrir el dashboard. Trade-off: límites de la plataforma y entrega async incómoda (abajo).

## El problema de los timeouts de la plataforma
Ni Discord ni Telegram esperan minutos por una respuesta síncrona:

| Plataforma | Ventana síncrona | Solución |
|---|---|---|
| Discord (slash command) | **3s** para responder, luego token de interacción ~15 min | `deferReply()` → editas el mensaje cuando el job acaba |
| Telegram (bot) | sin límite duro, pero el handler del webhook debe responder rápido | responder 200 al webhook YA; mandar el media después con `sendPhoto/sendVideo` |

Nunca generes dentro del handler del comando. **Acusa recibo en <3s**, encola, devuelve después.

## Arquitectura: el bot NO genera
Tres procesos desacoplados:
```
[Bot gateway] --(encola job + chat_id/interaction_token)--> [Cola] --> [Worker GPU]
     ^                                                                      |
     └──────── (entrega media cuando el worker termina) ───────────────────┘
```
- **Bot gateway**: recibe comando, valida, debita créditos ([[262-credits-quota-billing-gen]]), encola, hace
  `deferReply`/placeholder ("⏳ generando…"). Liviano, sin GPU, siempre vivo.
- **Cola** (Redis/SQS): guarda `prompt`, params, y el **routing de entrega**: `channel_id`, `message_id`/
  `interaction_token`, `chat_id`. Sin esto el worker no sabe a dónde devolver.
- **Worker GPU** (serverless RunPod): toma job, genera, sube a storage, **callback** al bot para entregar.

La entrega (callback/webhook→editar mensaje) es el patrón durable de [[115-async-render-largo-poller-durable]].

## Comandos típicos
- `/imagine <prompt> [--ar 16:9] [--seed N]` → parsea flags, valida, encola.
- **Botones/reacciones** bajo el resultado: `🔁 variar` `⬆️ upscale` `🌱 re-roll` → nuevas interacciones que
  encolan jobs con `parent_id` (linaje, [[263-asset-gallery-management.md]]).
- `/saldo` → consulta créditos. `/cola` → posición/ETA.

## Entrega async (lo que más falla)
- **Discord**: guarda el `interaction_token` (vive ~15 min). El worker hace `PATCH webhook/.../messages/@original`
  con el adjunto. Si el job tarda >15 min → el token muere; entonces `channel.send()` con mención al usuario.
- **Telegram**: guarda `chat_id`; el worker llama `sendVideo`/`sendPhoto` por la Bot API. Para video grande,
  sube el archivo (no URL) o usa `file_id` si reusas.
- **Subir el binario, no URL firmada que expira** si la plataforma re-descarga tarde. Genera thumbnail/poster
  para preview inmediata.

## Cola, concurrencia y fairness
- **Una cola, workers que escalan a 0** (serverless): cold start ≈ minutos → avisa ETA realista en el placeholder.
- **Límite de concurrencia por usuario** (1-2 jobs): un usuario no llena la cola del server. Cruza con la
  cuota de [[262-credits-quota-billing-gen]].
- **Rate limit por canal/server** para no fundir la GPU en un raid.
- **Idempotencia**: si el bot reintenta encolar (gateway se cayó), usa `interaction_id` como clave → no
  duplicas el job ni el débito.

## Seguridad y abuso
- **Moderar el prompt y el output** antes de postear en un canal público (NSFW, marcas) → [[165-moderacion-safety-output-generado]].
- **Watermark obligatorio** en tier free / canales públicos → [[266-c2pa-watermark-implementacion.md]].
- No confíes en el `user_id` del payload sin verificar la **firma del webhook** (Discord: Ed25519 header;
  Telegram: secret token en la URL).
- Aísla por `guild_id`/`chat_id` como tenant → un server no ve assets de otro.

## Errores que muerden
- Generar en el handler → Discord marca el comando como fallido a los 3s aunque el job siga.
- No persistir el `interaction_token`/`chat_id` con el job → el media se genera y no sabes a quién mandarlo.
- URL firmada corta para media que la plataforma descarga tarde → "imagen rota" en el chat.
- Sin idempotencia en el encolado → un retry del gateway cobra y genera dos veces.

Cruza con [[115-async-render-largo-poller-durable]] y [[41-whatsapp-cloud-api]] (mismo patrón submit/entrega async sobre otra plataforma de mensajería).
