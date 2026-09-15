# 51 — Campañas de mensajes: WhatsApp, Messenger e Instagram Direct

Las campañas de mensajes (objetivo Engagement → ubicación: apps de mensajería) pueden abrir chat en **tres destinos**: WhatsApp, Messenger e Instagram Direct. Lee este módulo para elegir destino(s) y entender qué cambia en el comportamiento del usuario y la operación. El caso WhatsApp a fondo está en 50; aquí está el mapa completo. Jerga: "destino" = la app donde se abre el chat; "ventana de servicio" = lapso en que puedes responder gratis.

## Los 3 destinos y cuándo cada uno

| Destino | Quién es | Cuándo usarlo |
|---|---|---|
| **WhatsApp** | El default LatAm. Donde la gente YA negocia, paga y pide domicilios | Casi siempre en Colombia/LatAm. Venta consultiva, contraentrega, pymes |
| **Messenger** | El canal más viejo. Útil en públicos que viven en Facebook (35+, ciertas zonas, páginas con comunidad FB activa) | Si tu página FB ya recibe mensajes orgánicos ahí; mercados donde Messenger pesa (Filipinas, partes de México) |
| **Instagram Direct** | Joven, visual, lifestyle. Responde quien te descubre o ya te sigue en IG | Moda, belleza, food trendy, creators. Si tus DMs orgánicos ya venden, escálalos con pauta |

**Regla de decisión**: mira dónde te escriben HOY tus clientes orgánicos. La pauta amplifica el canal que ya funciona; no inventes un canal nuevo con plata.

## Setup multi-destino paso a paso

1. Objetivo **Engagement** → tipo de conversión: **mensajes**.
2. En el ad set, sección de ubicación de mensaje, marca los destinos: WhatsApp / Messenger / Instagram. Puedes marcar varios — Meta **elige por persona** el destino donde es más probable que inicie conversación (quien vive en IG va a Direct; el tío de Facebook va a Messenger).
3. Conecta cada destino a su activo: número de WhatsApp Business (ver 50), página de FB para Messenger, cuenta de IG profesional para Direct. Si falta el activo, ese destino no sirve.
4. Configura el **mensaje pre-llenado / saludo de bienvenida** por campaña (ver 54). En multi-destino, cada app tiene su propio campo — revísalos todos.
5. Publica solo cuando la operación de respuesta esté lista (última sección).

- Pro: más inventario, costo por conversación suele bajar 10-30%.
- Contra: tu operación debe atender **las 3 bandejas** con la misma velocidad. Si tu bot solo vive en WhatsApp Cloud API, los chats de IG/Messenger quedan huérfanos.
- Receta pyme: **solo WhatsApp** hasta que la operación esté sólida; multi-destino solo si tienes inbox unificado (Meta Business Suite responde los 3) o bot multicanal (ver 96).

## Diferencias de comportamiento por canal

- **WhatsApp**: el usuario lo trata como canal serio de compra. Espera respuesta de negocio: precio, envío, pago. Conversaciones más cortas y transaccionales. Mayor tasa de cierre.
- **Messenger**: más casual, más curiosos, más gente mayor. Tolera respuestas algo más lentas. Bueno para flujos automatizados largos (los chatbots de Messenger son veteranos).
- **IG Direct**: el usuario llega desde un reel/story con vibra de marca. Pregunta corto ("precio?", "hay en talla M?"). Si la respuesta no llega en minutos, desaparece. Responder stories y comments alimenta el mismo embudo.

## Re-engagement: sponsored messages y ventanas

- **Messenger sponsored messages**: ads que reabren conversación con gente que YA te escribió por Messenger — remarketing dentro del chat. No existe equivalente en ads para WhatsApp: ahí el re-engagement fuera de 24h se hace con **plantillas pagas de la API** (marketing templates) o listas de difusión de la app Business, no con pauta Meta.
- En WhatsApp, la ventana de servicio es 24h desde el último mensaje del usuario (72h gratis si vino de un ad CTWA, ver 50). Diseña la operación para resolver DENTRO de la ventana.

### Tabla de ventanas y costos (jun-2026)

| Canal | Ventana gratis | Fuera de ventana | Costo fuera (Colombia) |
|---|---|---|---|
| WhatsApp (orgánico) | 24h desde último msg del usuario | Plantilla de la API por categoría | Mkt ~$50 COP/msg, Util ~$3 COP/msg (ver 50) |
| WhatsApp (vino de CTWA) | **72h, cubre marketing** | Igual que arriba | Gratis dentro de 72h |
| Messenger | 24h | Sponsored message (pauta) o tag de mensaje | Costo de pauta |
| IG Direct | 24h | Solo dentro de ventana | — |

## Cómo se miden

El evento estándar es **"conversaciones iniciadas mediante mensajes"**: alguien que clicó tu ad y envió al menos un mensaje. En Ads Manager agrégala como columna junto a costo por conversación. Eso es lo que el objetivo optimiza por defecto.

Lo que ese número NO te dice: cuántos compraron. Conversación ≠ venta. Cerrar el loop (etiquetas, referral del ad, CAPI de mensajería) es el módulo 53 — léelo antes de escalar cualquier campaña de mensajes.

## Receta de arranque típica (pyme Colombia)

1. Campaña Engagement → destino: solo WhatsApp, presupuesto diario chico ($30-60k COP).
2. 2-3 creativos distintos (ver 30-31), mensaje pre-llenado específico por campaña (ver 50).
3. Operación lista ANTES de publicar: quién responde, en qué horario, con qué guion (ventas_lushows 82).
4. Semana 1-2: mide costo por conversación Y % que pide precio/pedido (etiquetas, ver 53).
5. Solo después considera sumar IG Direct (si tu marca es visual y tus DMs ya venden) o Messenger (si tu página FB tiene comunidad activa).

## La operación detrás: la mitad del resultado

Una campaña de mensajes es un compromiso operativo: **alguien (o un bot) DEBE responder en minutos, en horario real del cliente** (noches, domingos). Pauta de mensajes sin operación de respuesta es plata quemada — el lead que espera 4 horas ya le compró a otro.

| Nivel de operación | Qué incluye | Cuándo |
|---|---|---|
| Mínimo viable | WhatsApp Business app + respuestas rápidas + 1 persona con horario claro | Arranque, <30 conv/día |
| Intermedio | Meta Business Suite (bandeja unificada 3 canales) + 2-3 personas por turnos | Multi-destino, fin de semana |
| Serio | WhatsApp Cloud API + bot de IA 24/7 que califica y escala a humano | Volumen, medición CAPI (ver 96) |

- El guion y oficio de la conversación: ventas_lushows 82 — no lo duplica este bloque.
- Antes de subir presupuesto pregúntate: ¿si llegan 50 conversaciones hoy, quién las atiende?

### Quality rating del número (no lo quemes)

WhatsApp pone un **rating de calidad** a tu número (verde/amarillo/rojo) según cuánta gente te bloquea o reporta. Plantillas de marketing masivas a gente que no pidió nada lo bajan; con rating rojo Meta limita tus envíos o tumba el número. Regla: marketing templates solo a quien interactuó contigo, y dentro de la ventana de 72h del CTWA cuando se pueda (gratis, ver 50). Es operación de WhatsApp, no de pauta — pero te cuesta la cuenta si la ignoras.

## Errores comunes — blacklist

- Activar los 3 destinos "para llegar a más gente" sin atender 3 bandejas: conversaciones perdidas que pagaste.
- Pautar mensajes a IG Direct con respuesta promedio de horas: en IG el lead muere en minutos.
- Medir éxito por costo por conversación sin medir ventas: optimizas curiosos (ver 53).
- Intentar "sponsored messages" a contactos de WhatsApp vía Ads Manager: no existe; eso se hace con plantillas de la API.
- Lanzar campaña de mensajes el viernes a las 6pm sin cobertura de fin de semana: el 60% de las conversaciones llegan cuando no estás.
- Usar Messenger por default en Colombia porque "es de Facebook": tu cliente vive en WhatsApp; ve donde él está.
- Quemar el quality rating con difusiones de marketing masivas: número limitado o tumbado, y perdiste el canal entero.
