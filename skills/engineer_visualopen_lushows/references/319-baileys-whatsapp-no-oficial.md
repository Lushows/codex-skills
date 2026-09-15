# 319 · Baileys: WhatsApp no-oficial (multi-device, QR, riesgo de ban)

> Baileys es WhatsApp Web reverse-engineered en TS: gratis, sin aprobación de templates, sin BSP.
> El precio oculto es el ban del número — no "si", sino "cuándo". Sirve para dev y prototipos, no para producción a escala.

## Qué es y cómo se conecta
Librería socket-based (`@whiskeysockets/baileys`) que se autentica como un **dispositivo vinculado** vía la arquitectura **multi-device** de WhatsApp. No corre un navegador headless — habla el protocolo binario directo (eficiente, pero frágil ante cambios de Meta). Dos vías de login:
- **QR code**: escaneas desde el teléfono → sesión guardada en `auth_state` (archivos de credenciales). Reusa el estado para no re-escanear.
- **Pairing code**: código alfanumérico de 8 dígitos sin cámara — útil en servidores headless.

La sesión es la joya: persístela cifrada. Si la pierdes, re-login (y cada re-login es señal de riesgo para Meta). Usa `useMultiFileAuthState` (o un store en DB/Redis para escalar): guarda `creds` + las **claves de señal** que cifran cada mensaje. Perderlas = sesión muerta.

## Reconexión y eventos
Baileys emite `connection.update` con `lastDisconnect`. El loop correcto: en desconexión, lee el `statusCode` del `DisconnectReason` y decide — reconecta en casi todos los casos, **salvo `loggedOut` (401)** donde la sesión murió y reconectar es inútil (hay que re-vincular). Mensajes entrantes llegan por `messages.upsert`; guarda credenciales en cada `creds.update` o perderás la sesión al reiniciar. Sin este manejo, el bot "se cae solo" tras horas.

## El riesgo de ban (lo que define todo)
Automatizar tu cuenta personal/comercial con herramientas no oficiales **viola los ToS de Meta**. WhatsApp detecta Baileys por:
- **Fingerprint de protocolo** (no eres la app oficial).
- **Velocidad de mensajes** (ráfagas, mismo texto a muchos).
- **Análisis de comportamiento** (patrón no humano).

Reportes 2025: cuentas **duran 2–8 semanas** antes del ban permanente con uso de producción; subir **status/broadcast** dispara bans inmediatos; lógica que funciona en local **banea al moverla a un servidor** (IP de datacenter = bandera roja). [no verificado: ventana 2–8 semanas, es agregado de issues de GitHub, no cifra oficial]

Mitigaciones (reducen, no eliminan): delays humanos entre mensajes, no broadcast, número "calentado" con uso real previo, nunca masivo, **IP residencial** mejor que datacenter. Existen middlewares anti-ban (patrones human-like) pero **no hay garantía** — Meta gana esta carrera. Regla simple: si el número importa para el negocio, no lo pongas en Baileys de producción. Un ban es permanente y te lleva el número, el historial y los grupos.

## Baileys vs Cloud API: cuándo cada uno
| Eje | Baileys | Cloud API (oficial) |
|---|---|---|
| Costo | gratis | per-mensaje (ver [[317-whatsapp-cloud-api-deep]]) |
| Templates/aprobación | ninguno (texto libre siempre) | requiere aprobación, categorías |
| Ban / SLA | alto riesgo, sin SLA | compliant, sin ban por uso |
| Rompe con cambios de Meta | sí, a menudo | no (Meta mantiene la API) |
| Número | el tuyo (en riesgo) | registrado en WABA |
| Uso correcto | **dev, QR local, demo, volumen ínfimo** | **producción, escala, negocio** |

## Versionado y mantenimiento
Baileys es comunidad — breaking changes frecuentes (la 7.x introdujo varios). Pinea versión, lee el changelog antes de subir. Forks abundan (calidad variable); usa `@whiskeysockets/baileys` oficial. Cuando Meta cambia el protocolo, esperas el parche de la comunidad — downtime no negociado.

## Capacidades vs Cloud API
Baileys ve **todo** WhatsApp Web: grupos, status/stories, presencia (typing, online), historial, reacciones, ediciones — cosas que la Cloud API **no** expone. Por eso tienta para casos como leer grupos o automatizar status. Pero justo esas acciones (status automatizado, mensajería masiva en grupos) son las que más rápido disparan el ban. La potencia extra es la trampa: úsala para leer/asistir en dev, nunca para emitir a escala.

## Recomendación operativa (caso Lushows/BIO-SETA)
Patrón correcto: **Baileys en local con QR para desarrollar y probar el bot** (rápido, sin esperar aprobación de Meta), y **Cloud API en Render para producción**. El código ya separa `src/whatsapp.js` (Baileys) de `src/whatsappCloud.js` (Cloud) — esa frontera es la decisión arquitectónica clave: nunca dejes Baileys atendiendo clientes reales del negocio.

## Cierre
La vía compliant con sus templates, Flows y pricing está en [[317-whatsapp-cloud-api-deep]]. Cruza con [[318-chatbot-conversational-ux]].
