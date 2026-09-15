# 96 — Integración con el stack: que el lead fluya sin fricción

La pauta termina donde empieza tu operación — y ahí es donde más plata se quema. El problema central: **un lead que llega y nadie contacta en minutos es pauta quemada** (speed-to-lead, ver 52: la probabilidad de contacto cae brutalmente con cada hora de espera). Lee este módulo cuando montes el "alrededor" de la pauta: a dónde cae el lead, quién lo atiende, cómo vuelve la señal a Meta. El principio: cada pieza existe para reducir el tiempo entre clic y conversación, y para devolverle datos al algoritmo.

## Pieza 1: Lead ads → CRM/hoja automático

Los leads de Instant Forms caen en un CSV dentro de Meta que nadie revisa. Sácalos en tiempo real:

- **Integraciones nativas de Meta**: en la configuración del form puedes conectar CRMs soportados directo. Si tu CRM está en la lista, es la vía más simple.
- **Zapier/Make/n8n** (conectores de automatización; Make y n8n suelen salir más baratos para LatAm): receta concreta de pyme —
  1. Trigger: "New Lead in Meta Lead Ads" (conectas la página y el form).
  2. Acción 1: agregar fila en Google Sheets (nombre, teléfono, campaña, fecha) — tu registro maestro.
  3. Acción 2: notificar al vendedor por WhatsApp/Telegram/email con los datos y un link `wa.me/57XXXXXXXXXX` para contactar en 1 clic.
  4. Meta: lead atendido en < 5 minutos en horario laboral.

## Pieza 2: CTWA → bot/CRM de WhatsApp

Si corres Click-to-WhatsApp (ver 50) con WhatsApp Cloud API, el webhook del mensaje entrante trae el objeto `referral` cuando el chat nació de un ad: incluye `ctwa_clid` (el ID de clic para atribución) y `source_id`/ad_id, headline y hasta el media del anuncio. Reglas:

- **Guarda el referral SIEMPRE** (en el perfil del cliente en tu CRM/bot): es la única forma de saber qué campaña trajo cada venta de chat (ver 53). Si tu bot lo descarta, tu atribución de WhatsApp muere ahí.
- **Etiqueta por campaña**: cada conversación entra con tag de su ad/campaña → puedes leer tasa de cierre por creativo, no solo costo por conversación.
- **El bot saluda con contexto del ad** (ver 54): si el cliente vino del ad de "Calculadora de costos para tu restaurante", el bot abre hablando de eso, no con un menú genérico. La congruencia ad→chat es la versión conversacional de la congruencia ad→landing (ver 48).

## Pieza 2b: Meta Business Agent vs bot a medida (decisión 2026)

En junio-2026 Meta lanzó el **Meta Business Agent**, un agente de IA nativo que atiende clientes en WhatsApp/Instagram (y que Meta cobra). Antes de construir, decide:

| | Meta Business Agent | Bot a medida (Cloud API + IA) |
|---|---|---|
| Montaje | Rápido, dentro de Meta | Requiere desarrollo (engineer_visualopen) |
| Costo | Lo cobra Meta (por uso) | Tu hosting + tokens (ver optimizer_tokens) |
| Control del guion de venta | Limitado al marco de Meta | Total — tu guion, tu cierre (ver ventas_lushows) |
| Atribución / referral | Manejado por Meta | Tú guardas `ctwa_clid` y reportas CAPI a tu medida |
| Recomendado para | Atención general, FAQ, agendamiento simple | Cierre con guion propio, integración profunda CAPI/CRM |

Regla: si el cierre necesita un guion de ventas específico y atribución fina, el bot a medida gana; si solo necesitas responder dudas y filtrar, el Business Agent puede ahorrarte semanas. (Tu propio proyecto de bot WhatsApp con IA es exactamente la arquitectura a medida.)

## Pieza 3: la señal de vuelta — CAPI desde el chat/CRM

El loop completo: la venta se cierra en WhatsApp o en el CRM, y **se reporta a Meta vía Conversions API** (ver 06/53) como evento Purchase (o tu evento de cierre) con el `ctwa_clid`/teléfono hasheado para el match. Resultado: Meta deja de optimizar por "conversaciones iniciadas" (muchas basura) y empieza a buscar gente parecida a la que COMPRA. Es la palanca de optimización más ignorada en operaciones WhatsApp-first — y la diferencia entre pagar por curiosos o por compradores. Bajo GEM (ver 92), señal de cierre limpia generaliza aún mejor el matching. Implementación técnica (webhooks, hashing, eventos): engineer_visualopen_lushows.

## Pieza 4: nurturing y recompra

- **Post-24h en WhatsApp**: pasada la ventana de 24 horas desde el último mensaje del cliente, solo puedes iniciar con **plantillas aprobadas** por Meta (templates de marketing/utility). Diseña 2-3: seguimiento de cotización ("¿pudiste revisar la info que te envié?"), carrito/pedido pendiente, y oferta de cierre. Respeta la regla: spam de plantillas = bloqueo del número y baja tu quality rating.
- **Email como respaldo** del lead que no contestó WhatsApp: secuencia simple de 2-3 correos.
- **Recordatorio de recompra**: si tu producto se agota/renueva en N días, programa el mensaje al día N-5 con plantilla. Es el activo de LTV más barato que existe: venta sin costo de pauta (ver 64 — sube tu MER global y el CPA que puedes pagar).

## Automatización útil vs sobre-ingeniería

Para una pyme, el stack completo puede ser: **Google Sheets + WhatsApp Business + 1 Zap**. Eso es TODO — y funciona. Sube de nivel solo cuando el volumen lo exija (≥ 20-30 leads/día o varios vendedores): ahí entra CRM real, bot con IA y CAPI de chat. No montes un Frankenstein de 8 herramientas conectadas que nadie en el negocio entiende ni mantiene: cada eslabón es un punto de fallo silencioso, y un Zap caído una semana son leads pagados a la basura. Regla: cada herramienta nueva debe eliminar un cuello de botella MEDIDO, no un antojo. Si automatizas con IA (clasificar leads, redactar respuestas), vigila el costo de tokens con optimizer_tokens_lushows antes de que el ahorro de tiempo se coma la factura.

Construir el bot/integración técnica (Cloud API, webhooks, CAPI, hosting): engineer_visualopen_lushows. El guion y la conversación de venta del bot: ventas_lushows.

## Stack por etapa (referencia rápida)

| Etapa | Volumen | Stack suficiente |
|---|---|---|
| Arranque | < 10 leads/día | WhatsApp Business app + Google Sheets manual o 1 Zap |
| Crecimiento | 10-30 leads/día | Cloud API o WhatsApp Business + Sheets automatizado + plantillas post-24h + notificación al vendedor |
| Escala | 30+ leads/día o varios vendedores | Bot con IA (Business Agent o a medida) + CRM + referral guardado + CAPI de chat + recompra programada |

Sube de fila solo cuando el cuello de botella actual esté MEDIDO (leads sin contactar, tiempo de respuesta, ventas sin atribuir). Cada fila nueva agrega mantenimiento: alguien del negocio debe poder explicar cómo fluye un lead de punta a punta, o el stack es más grande que el equipo.

## El test end-to-end semanal (10 minutos)

1. Dale clic a tu propio ad desde un celular que no sea tuyo (o el form de lead).
2. Cronometra: ¿en cuánto llega la notificación al vendedor? ¿en cuánto responde alguien?
3. Verifica que la fila cayó en la hoja/CRM con campaña correcta y que el referral/ctwa_clid quedó guardado.
4. Si reportas CAPI: confirma en Events Manager que el evento de prueba llegó y matcheó con buen EMQ (ver 62).
5. Lo que falle, se arregla esa semana: cada día de webhook caído son leads pagados que nadie verá.

## Errores comunes — blacklist

- Lanzar lead ads sin automatizar la salida del lead: los leads mueren en el CSV de Meta mientras pagas por más.
- Bot que descarta el `referral` del webhook: regalaste la atribución de cada venta de chat.
- Saludo genérico de menú a quien llegó por un ad específico: matas la congruencia que el ad pagó (ver 54).
- No reportar ventas cerradas vía CAPI y quejarse de que "CTWA trae puros curiosos": el algoritmo optimiza por lo único que ve.
- Elegir Meta Business Agent cuando el cierre necesitaba un guion de ventas propio (o construir un bot a medida cuando bastaba el nativo): decide con la tabla, no por moda.
- Mandar plantillas de marketing a toda la base cada semana: bloqueos, baja el rating del número, y Meta te restringe el envío.
- Montar n8n + CRM + 3 SaaS para 5 leads diarios: la hoja de cálculo era la respuesta.
- Nadie monitorea si el Zap/webhook sigue vivo: revisa el flujo end-to-end una vez por semana (mándate un lead de prueba).
