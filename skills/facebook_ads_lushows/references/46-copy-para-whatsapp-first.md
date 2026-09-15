# 46 — Copy para WhatsApp-first

Cómo escribir anuncios cuyo destino NO es una landing sino un CHAT de WhatsApp (CTWA = Click-to-WhatsApp, la mecánica completa de campaña está en el 50). En LatAm pyme este es EL formato dominante: el cliente no quiere checkout, quiere preguntar. El copy aquí tiene un trabajo extra: **preparar una conversación, no solo arrancar un clic**. La conversación de venta en sí (descubrimiento, objeciones, cierre) es ventas_lushows 82 — o tu bot GASTROWHATS/AVISPA'O. Este módulo termina donde empieza el primer mensaje del cliente.

> **Snapshot jun-2026 (ver actualizacion-2026-06 §8):** la economía del CTWA mejoró para ti. ① **Ventana gratis de 72h**: cuando respondes dentro de 24h a quien llegó por un ad CTWA, se abre una ventana de 72h donde TODOS los mensajes (incluido marketing) salen gratis. ② **Colombia es de las plazas más baratas de LatAm** en costo por mensaje. ③ Pero el default optimiza "conversaciones iniciadas" (trae saludadores, no compradores): para optimizar por COMPRADORES tu bot debe capturar el `ctwa_clid` y disparar un evento CAPI `business_messaging` cuando el lead califica/paga (atribución: ver 53). ④ Ojo estratégico: el **Meta Business Agent** (lanzado 3-jun-2026) ahora compite con tu bot a la medida — decisión de producto, no de copy.

## Los 4 trabajos del copy CTWA

1. **Dejar claro que el siguiente paso es CONVERSAR.** "Escríbenos", "pregunta sin compromiso", "te cotizamos por WhatsApp" — el lector debe saber que va a un chat, no a una tienda. Sorpresa = abandono. Nunca uses "compra ya" con botón de WhatsApp.
2. **Bajar la barrera.** Escribir a un desconocido da pereza/miedo. Desactívalo: no es compromiso de compra, hay respuesta rápida, contesta un humano real (o un bot honesto y útil). "Pregunta lo que quieras, sin compromiso. Respondemos en minutos."
3. **Pre-calificar suave.** El clic de CTWA es barato y el curioso es gratis para Meta pero CARO para ti: cada "info?" sin plata te cuesta tiempo de chat (o tokens de bot). Si filtrar importa (alto ticket, servicios), pon el precio o un "desde" VISIBLE en el copy: "Planes desde $450.000". Filtras antes del chat, no después. Si tu producto es de impulso barato, NO filtres: deja entrar a todos.
4. **Prometer velocidad y CUMPLIRLA.** El lead de WhatsApp se enfría en minutos, no en horas (ver 96). Si el copy dice "respuesta inmediata", la operación responde inmediato — bot, plantilla o humano de turno. Con la ventana gratis de 72h, responder rápido además te sale gratis.

## El mensaje pre-llenado (ice-breaker): tu arma secreta

Es el texto que aparece YA ESCRITO en el chat cuando el cliente llega del ad. Configúralo SIEMPRE, con dos objetivos:

- **Que el cliente no piense**: solo da "enviar". Ejemplo: "Hola 🙋 Quiero info del combo Melena + Reishi".
- **Que TÚ sepas de dónde viene**: el referral del CTWA trae el ID del anuncio y el `ctwa_clid` (cómo capturarlos y atribuir ventas por ad: ver 53), y además el texto del ice-breaker te dice el producto/oferta sin preguntar.

Un ice-breaker por ad/oferta, NUNCA uno genérico para toda la cuenta: "quiero info" no te dice nada; "quiero el 2x1 de almuerzos" te dice todo. Si pautas 5 ofertas, son 5 ice-breakers distintos — así tu bot/operador sabe de entrada qué responder.

**Estructura del ice-breaker que funciona:** [saludo corto] + [palabra clave o producto exacto] + [emoji]. Ejemplos:
- "Hola! Quiero la Melena de León 🍄"
- "COMBO 🙌 Quiero el 2x1 Día y Noche"
- "Hola, quiero agendar el mantenimiento de mi aire 🙋"

## 8 plantillas completas de copy CTWA (con ice-breaker)

**1 · Comida (impulso, sin filtro)**
> "Almuerzo casero, distinto cada día, en tu oficina antes de la 1pm 🍴 Hoy: bandeja de pollo sudado + jugo natural por $16.900. Pide por WhatsApp ahora y llega caliente. Sin pedido mínimo."
> Ice-breaker: "Hola! Quiero el almuerzo de hoy 🍴"

**2 · Servicio local (con velocidad)**
> "Mantenimiento completo de tu aire acondicionado por $89.000: revisión + lavado + gas verificado, con garantía de 90 días por escrito. Escríbenos por WhatsApp y agenda tu visita esta misma semana — te respondemos en minutos."
> Ice-breaker: "Hola, quiero agendar el mantenimiento de mi aire 🙋"

**3 · E-com (bajar barrera de pago)**
> "Melena de León: 120 cápsulas para 2 meses de foco. $89.900, envío a toda Colombia y pagas CUANDO TE LLEGA (contra entrega). ¿Dudas de si es para ti? Pregunta sin compromiso — humano real al otro lado 🍄"
> Ice-breaker: "Hola! Quiero info de la Melena de León 🍄"

**4 · B2B (pre-calificación visible)**
> "Llevamos la contabilidad de tu negocio al día: cierre mensual + informe semanal claro por WhatsApp. Planes desde $150.000/mes según tamaño. Si tu negocio factura y tú sigues a ciegas con los números, escríbenos: primera revisión gratis."
> Ice-breaker: "Hola, quiero la revisión gratis para mi negocio 📊"

**5 · Alto ticket (micro-compromiso)**
> "Cocinas integrales a medida, diseño 3D incluido antes de pagar un peso. Proyectos desde $8.500.000. Escríbenos por WhatsApp con las medidas (o una foto del espacio) y te damos un estimado hoy mismo — sin visitas ni compromiso todavía."
> Ice-breaker: "Hola! Quiero un estimado para mi cocina. Estas son las medidas:"

**6 · Oferta con plazo (palabra clave)**
> "Solo esta semana: combo Día y Noche (Melena + Reishi) en 2x1 — $149.900 con envío gratis. Termina el domingo y este lote es de 60 unidades. Escríbenos 'COMBO' y te lo reservamos de una 👇"
> Ice-breaker: "COMBO 🙌 Quiero reservar el 2x1"

**7 · Cita / agenda (servicio profesional)**
> "Valoración odontológica con radiografía incluida por $45.000 (normal $90.000). Quedan 6 cupos esta semana. Escríbenos y eliges tu hora por WhatsApp en 1 minuto 🦷"
> Ice-breaker: "Hola, quiero agendar mi valoración 🦷"

**8 · Recompra / reactivación (a quien ya compró)**
> "¿Ya se te está acabando el frasco? 👀 Repite tu Melena de León con envío gratis esta semana. Solo respóndenos 'QUIERO' y te lo despachamos mañana."
> Ice-breaker: "QUIERO repetir mi pedido 🙌"

## La continuidad ad → chat (el momento que se rompe casi siempre)

El que abre el chat (bot o humano) debe saludar SABIENDO qué vio el cliente: "¡Hola! Vi que vienes por el combo 2x1 🙌 Te cuento..." — no "Hola, ¿en qué puedo ayudarte?". Esa continuidad se construye con el ice-breaker + el referral del ad (ver 53). Si el ad ofrece el 2x1 y el bot saluda con un menú robótico de 8 opciones, rompiste el message match igual que con una home genérica (ver 48). Configura tu bot/operador para leer la palabra clave del ice-breaker y arrancar EN ESE punto de la conversación.

## Decidir: ¿mostrar precio o no en CTWA?

| Producto | ¿Precio en el copy? | Por qué |
|---|---|---|
| Impulso barato (comida, e-com bajo) | SÍ | El precio es la razón de comprar; mostrarlo filtra curiosos y acelera |
| Servicio con precio variable | "Desde $X" | Filtra a quien no tiene presupuesto antes de llenarte el chat |
| Alto ticket | "Desde $X" o rango | Sin esto, el chat se llena de "¿precio?" que se esfuman al oírlo |
| Producto que necesita conversación de valor | A veces oculto | Solo si tu operador/bot sabe construir valor antes del precio (ventas 82) |

Regla: esconder el precio "para conversar" en producto de impulso es un error — regalas la única razón de abrir el chat. Mostrarlo en alto ticket es pre-calificación, no debilidad.

## Errores comunes — blacklist

- ❌ Copy que vende checkout ("compra ya") con botón de WhatsApp: el cliente llega confundido al chat.
- ❌ Ice-breaker vacío o genérico ("Hola"): pierdes el contexto y el cliente debe redactar — fricción que mata.
- ❌ Esconder el precio en alto ticket "para conversar": chat lleno de "¿precio?" que se esfuman al oírlo.
- ❌ Mostrar precio en impulso barato cuando NO filtra nada: regalas la única razón de abrir el chat. Decide según producto.
- ❌ Prometer "respuesta inmediata" con WhatsApp atendido dos veces al día.
- ❌ Responder con un menú robótico de 8 opciones al que llegó por UNA oferta concreta.
- ❌ No registrar de qué ad vino cada chat: sin el `ctwa_clid` no sabes qué anuncio vende ni puedes optimizar por compradores (ver 53).
- ❌ Dejar la campaña CTWA activa 24/7 sin nadie (ni bot) que responda de noche: programa horarios de pauta según tu capacidad real de respuesta (ver 96).
- ❌ Medir la campaña por "conversaciones iniciadas" y no por ventas cerradas en chat: el curioso infla la métrica (atribución real: ver 53).
- ❌ Ignorar la ventana gratis de 72h: responder lento no solo enfría el lead, te hace pagar mensajes que pudieron ser gratis.
