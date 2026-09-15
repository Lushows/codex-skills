# 18 · WhatsApp Cloud API (el canal de AVIS)

> Fuentes: engineer_visualopen_lushows ref 41 (`references/41-whatsapp-cloud-api.md`) + código real `AVISPAO/src/lib/whatsapp.ts` y `AVISPAO/src/app/api/whatsapp/route.ts`. Meta Cloud API vía Graph API; el proyecto usa `v21.0`.

AVIS vive en WhatsApp. Todo lo que escribe sale por la **Cloud API de Meta** (oficial, hosteada por Meta vía Graph API). Esto NO es Baileys/WhatsApp Web — es el camino compliant, sin riesgo de ban, pero con sus reglas. Si no entendemos estas reglas, AVIS calla cuando más importa (un recordatorio fuera de hora, un aviso de vencimiento) o tira errores silenciosos.

## La ventana de 24h (lo más importante)
Cada vez que el cliente **nos escribe**, se abre una **ventana de servicio de 24 horas**. Dentro de esa ventana AVIS puede mandar **texto libre gratis** (y media, botones, lo que sea). Cuando la ventana se cierra (24h sin que el cliente escriba), AVIS **solo puede mandar una PLANTILLA aprobada** — el texto libre rebota con error `#131047` (reengagement).

Por eso hay dos funciones en `whatsapp.ts`:
- `sendWhatsAppText(to, body)` → texto libre. Sirve SOLO dentro de la ventana de 24h. Es lo que usa el webhook al responder un mensaje entrante.
- `sendWhatsAppTemplate(to, name, language, params)` → plantilla aprobada. Atraviesa la ventana cerrada. **Imprescindible** para recordatorios, avisos de vencimiento y cualquier mensaje que AVIS inicie sin que el cliente haya escrito primero.

> Regla de oro para el equipo: si AVIS **responde**, texto. Si AVIS **inicia** la conversación, plantilla.

## Plantillas: categorías y precio
Toda plantilla tiene una **categoría** que define el precio por conversación:
- **UTILITY** — transaccional/post-disparo de algo del cliente (recordatorio de vencimiento, confirmación, estado). Es lo nuestro. **Gratis si va dentro de una ventana de 24h abierta**; barata fuera de ella.
- **MARKETING** — promoción, reactivación, ofertas. Siempre se cobra.
- **AUTH** — códigos OTP. No aplica a AVIS.

Desde jul-2025 Meta cobra **por mensaje** (no por conversación). Para AVIS la mayoría de envíos son UTILITY, así que el costo es bajo, pero los recordatorios fuera de ventana **sí se cobran** — tenerlo en el modelo de costos.

## Crear y aprobar plantillas en Meta
1. En **WhatsApp Manager → Plantillas de mensaje** (o `POST /{WABA_ID}/message_templates`) se crea con nombre, idioma, categoría y cuerpo.
2. Meta la **revisa y aprueba/rechaza** (minutos a horas). Una plantilla rechazada no se puede enviar.
3. El cuerpo usa **variables posicionales** `{{1}}`, `{{2}}`… que se rellenan al enviar.

En `sendWhatsAppTemplate` las variables van en orden en `params: string[]`, mapeadas a `components: [{ type:"body", parameters:[{type:"text", text}] }]`. El orden del array = el orden de los `{{n}}`.

### Plantillas que ya existen en el proyecto
| Plantilla | Para qué |
|---|---|
| `avis_saludo` | Saludo / delegación inicial de la conversación |
| `WHATSAPP_TEMPLATE_RECORDATORIO` (env) | Recordatorio de obligación / vencimiento próximo |
| `WA_FACTURA_TEMPLATE` (env, opcional) | Aviso relacionado a una factura procesada |

> Antes de cambiar un texto de plantilla: cualquier edición vuelve a pasar por aprobación de Meta. No se edita en caliente como un mensaje normal.

## Enviar media
AVIS recibe facturas como **imagen** o **documento**. Para enviar media de vuelta se usa `type:"image|document|audio"` con `{"id":"<media_id>"}` (subido a Meta) o `{"link":"https://..."}` (URL pública alcanzable por los servidores de Meta — nada de localhost). Hoy AVIS responde sobre todo en texto; la media entrante se descarga, no se reenvía.

## Recibir mensajes (webhook)
El endpoint es `AVISPAO/src/app/api/whatsapp/route.ts`:
- **GET** = verificación de Meta. Compara `hub.verify_token` con `WHATSAPP_VERIFY_TOKEN` y devuelve el `hub.challenge`. Si no matchea → 403.
- **POST** = mensajes entrantes en `entry[0].changes[0].value.messages[0]`. También llegan `statuses[]` (sent/delivered/read/failed) — esos NO son mensajes, se ignoran.

Detalles críticos del handler:
- **Responder 200 rápido**, pero en serverless (Vercel) hay que **hacer `await` del trabajo ANTES de responder** — sin await, la función se cancela y AVIS no contesta (bug ya vivido). Por eso `maxDuration = 30`.
- **Idempotencia**: cada `message.id` se inserta en `mensajes_procesados`; si ya existía, se sale. Meta **reintenta** si no recibe 200, y sin esto AVIS respondería doble.
- Por tipo: `text` → `manejarMensaje()`; `image`/`document` → descargar y leer la factura; otro tipo → "te entiendo mejor por texto".

## Descargar media entrante
`getWhatsAppMediaUrl(mediaId)` pide la URL a Graph y `downloadWhatsAppMedia()` baja los bytes con el bearer. Esa **URL expira en ~5 minutos** y requiere el token — hay que descargar y persistir de inmediato, nunca guardar la URL.

## Número de prueba vs producción
**Hoy AVISPA'O usa el número de PRUEBA** que da Meta. Implicaciones:
- Solo se puede escribir a **destinatarios en la lista de prueba** (se agregan a mano en Meta for Developers). Mandar a otro número → error `#131030`.
- El número de prueba no sirve para clientes reales a escala.
- **Pendiente**: registrar el **número comercial real** en el WABA (verificación del negocio + número propio).

## Tokens: permanente, no temporal
Los tokens del dashboard de Meta **expiran en 24h** (ya nos tumbó la demo). En producción hay que crear un **System User** en Business Manager y generar un **token permanente** con scopes `whatsapp_business_messaging` + `whatsapp_business_management`. Va en `WHATSAPP_ACCESS_TOKEN`. Junto a él: `WHATSAPP_PHONE_NUMBER_ID` (para `/messages` y `/media`) y el `WABA_ID` (para plantillas).

## Errores comunes
| Código | Significa | Qué hacer |
|---|---|---|
| `#131030` | Destinatario no está en la lista de prueba | Agregar el número en Meta for Developers (o pasar a número de producción) |
| `#131047` | Reengagement: ventana de 24h cerrada | Mandar una **plantilla aprobada**, no texto libre |
| `#131026` | Mensaje no entregable (número sin WhatsApp / formato malo) | Validar el número en formato internacional sin `+` |
| `#100` / `#190` | Token inválido o expirado | Regenerar token; usar System User permanente |
| `#132xxx` | Plantilla mal armada (nombre/idioma/params) | Verificar `name`, `language.code` y el orden de `{{n}}` |
| HTTP 4xx genérico | Versión de Graph muy vieja | Pinear `v22.0`+ (Meta rechaza versiones viejas) |

## Reglas que el equipo no puede olvidar
- Número **sin `+`**, formato internacional (ej. `573004183337`).
- Plantillas **MARKETING** con baja interacción bajan el **quality rating** (verde→amarillo→rojo) y el **tier de envío** (1K→10K→100K→ilimitado). AVIS debe priorizar UTILITY y mensajes útiles, nunca spam.
- El webhook debe estar suscrito al campo `messages` en la WABA, o no llega nada.

> **Roadmap:** registrar el número comercial real y verificar el negocio (salir del número de prueba); crear plantillas UTILITY aprobadas para el reporte de cumplimiento y los recordatorios de vencimiento; pasar a token permanente de System User; pinear Graph a `v22.0`+ antes del próximo cutoff de Meta.
