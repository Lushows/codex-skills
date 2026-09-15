# 320 · Otros canales: Telegram, Discord, Instagram/Messenger

> WhatsApp domina LatAm, pero el mismo bot puede atender Telegram (gratis, sin fricción), Discord (comunidades) o Instagram DM (donde compra el cliente de marca).
> Cada canal tiene su transporte, su ventana de mensajería y sus límites — y solo Telegram es verdaderamente abierto.

## Telegram Bot API — el más permisivo
Gratis, sin aprobación, sin ventana de 24h, sin BSP. Creas el bot con @BotFather → token. Dos transportes:
- **Long polling** (`getUpdates`): tu proceso pide y cuelga hasta 90s, máx 100 updates/respuesta. **Una sola instancia** por token — dos pollers a la vez = `409 Conflict`. Ideal para dev y bots chicos.
- **Webhook**: Telegram hace `POST` a tu HTTPS. Latencia ~3× menor y CPU ~2× menor que polling agresivo; escala detrás de load balancer. Bot API 7.5 (mar-2025) subió el timeout de webhook a 90s y agregó gzip para payloads >1KB. **Producción = webhook.** [verificado]

Sin ventana de 24h: puedes escribir al usuario cuando quieras (mientras no te bloquee). Soporta:
- **inline keyboards** y **callback queries** (botones que no ensucian el chat).
- archivos hasta 20MB por bot API pública, **2GB con bot API local** (self-hosted).
- **pagos nativos** vía proveedores integrados, y **Web Apps** (mini-apps HTML dentro del chat, análogo a Flows pero sin cripto obligatoria).

Para un bot de soporte/ventas sin las trabas de Meta, Telegram es el camino corto: del token al primer mensaje en minutos. La contra: en LatAm la penetración es menor que WhatsApp — bueno como canal secundario o para early adopters, no como puerta principal de ventas.

## Instagram / Messenger (Graph API de Meta)
El canal de las marcas con audiencia en IG. Mismo dueño que WhatsApp → mismas trabas:
- **Ventana de 24h**: solo respondes dentro de 24h del último mensaje del usuario (igual que CSW de WhatsApp). Fuera de eso, casos limitados con message tags.
- **Rate limits duros**: ~200 llamadas/hora **por cuenta IG**; mensajería ~300 msg/s texto, ~10/s audio-video; tope de DMs automatizados (citan ~200/hora/cuenta en 2026). [no verificado: las cifras exactas varían por tier y cambiaron con el EOL de Basic Display]
- Requiere cuenta **Business/Creator** + página de Facebook vinculada + app de Meta revisada. Onboarding pesado.

Úsalo solo si el negocio ya vende por IG DM; si no, no vale la fricción.

## Discord — comunidades, no ventas 1:1
Para soporte de comunidad, no atención comercial LatAm típica. Modelo de **interactions** (slash commands): tienes **3 segundos** para responder o defieres (`deferred response`) y editas luego — clave si tu backend llama a un LLM lento. Límites: **50 req/s global**, buckets por endpoint (mensajes a canal A no consumen el de B), y **10.000 requests inválidas / 10 min** banean tu IP temporal. discord.js encola y respeta rate limits solo. Para bots de **generación** (comando → media async) ver [[264-discord-telegram-gen-bots]].

## Messenger (Facebook) — el primo de IG
Mismo Graph API y misma ventana de 24h que Instagram, pero sobre páginas de Facebook. En LatAm sigue vivo para negocios con base en FB (clasificados, servicios locales). Soporta **persistent menu**, quick replies y el mismo modelo de message tags para salir de la ventana en casos puntuales (confirmación de cita, actualización post-compra). Si ya integraste IG DM, agregar Messenger es casi gratis (misma app, mismo webhook, distinto `object`).

## Comparativa
| Canal | Ventana | Aprobación | Costo | Mejor para |
|---|---|---|---|---|
| WhatsApp Cloud | 24h (CSW) | templates | per-msg | ventas LatAm, el rey |
| Telegram | ninguna | no | gratis | bots ágiles, dev, soporte |
| Instagram DM | 24h | app review | gratis* | marcas con audiencia IG |
| Discord | n/a (3s resp) | no | gratis | comunidades, gen-bots |

\*gratis la API; el costo es el onboarding y los rate limits.

## Patrón multi-canal
Abstrae el canal detrás de una interfaz común (`recibir`, `enviar`, `media`): el core del bot (LLM, memoria, funnel) no debe saber si habla WhatsApp o Telegram. Cada adapter traduce su payload al formato interno — exactamente lo que hace BIO-SETA con `whatsapp.js`/`whatsappCloud.js`. Añadir Telegram = un adapter más, no reescribir el bot.

Diferencias que el adapter debe absorber:
- **IDs de usuario**: WhatsApp usa teléfono E.164, Telegram un `chat_id` numérico, Discord un snowflake, IG un IGSID. Tu `contacto_id` interno debe mapear todos.
- **Tipos de media**: cada plataforma codifica imagen/audio distinto (media_id de Meta vs file_id de Telegram). Normaliza a una URL/blob propio.
- **Capacidades dispares**: WhatsApp limita a 3 botones interactivos, Telegram permite teclados grandes, Discord usa componentes. Diseña al mínimo común o ramifica por canal.
- **Latencia de respuesta**: Discord exige responder/diferir en 3s; WhatsApp/Telegram toleran segundos. Si tu LLM tarda, **difiere primero** y edita el mensaje después.

## Cierre
Unificar estos canales en una sola bandeja con asignación y métricas está en [[321-omnichannel-inbox]]. Cruza con [[264-discord-telegram-gen-bots]].
