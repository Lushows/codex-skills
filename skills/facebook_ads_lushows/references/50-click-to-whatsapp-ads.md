# 50 — Click-to-WhatsApp Ads (CTWA): el formato rey de LatAm

CTWA (Click-to-WhatsApp) es un anuncio cuyo clic no lleva a una web: **abre un chat de WhatsApp contigo**, con un mensaje pre-llenado listo para enviar. Lee este módulo antes de pautar cualquier negocio que cierre ventas por chat — en Colombia y LatAm eso es casi todos. Es el formato con mejor fit cultural del continente y el que más plata mueve en pymes. Jerga: "CTWA" = *Click-To-WhatsApp Ad*; "free entry point" = ventana gratis que Meta abre cuando el chat nace de un ad.

## Por qué CTWA gana en LatAm

1. **Todo el mundo vive en WhatsApp.** Penetración >90% en Colombia/México/Brasil. No le pides al usuario que aprenda nada: ya chatea ahí con su familia.
2. **Cero fricción de landing/checkout.** No hay web que cargue lenta en datos móviles, no hay formulario de tarjeta que asuste. Un clic → un chat.
3. **El cierre es conversacional**, que es como LatAm compra: pregunta, regatea, pide foto, paga contraentrega o Nequi. Un humano o un bot de IA cierra (el oficio de esa conversación: ventas_lushows 82; el handoff: ver 54).
4. **Cada conversación es un activo**: el número queda guardado para remarketing, recompra y referidos — un visitante web rebotado no deja nada.

## Setup paso a paso (flujo unificado feb-2026)

> Contexto 2026: las campañas "manuales" desaparecieron como objeto separado; hoy hay **un solo flujo de creación** con toggles Advantage+ encendidos por default. Opt-OUT por sección, ya no opt-in (ver `actualizacion-2026-06` §1).

1. **Requisito previo**: un número de WhatsApp Business (app gratuita o API/Cloud API, ver 96) **conectado a tu página de Facebook**. Se conecta en Meta Business Suite → Configuración → WhatsApp, o durante la creación del anuncio. Sin esto el formato no aparece.
2. **Objetivo de campaña** (ver 11):
   - **Engagement → ubicación del mensaje: WhatsApp** — el default. Optimiza por "conversaciones iniciadas". Úsalo si NO mandas eventos de chat a Meta todavía.
   - **Sales → ubicación de conversión: WhatsApp** — el nivel pro. Requiere CAPI for business messaging enviando eventos de venta/lead calificado (ver 53). Solo cuando tienes esa señal; sin ella, el sistema no tiene de qué aprender.
3. **Ad set**: presupuesto, geo (si entregas en una ciudad, pauta esa ciudad — ver 57 para local), edad amplia (deja que el creativo filtre), targeting broad o detallado ligero (ver 20). Placements en **Advantage+ (automático)** — incluye ahora WhatsApp Status y Threads (ver `actualizacion-2026-06` §5).
4. **Anuncio**: creativo normal (video/imagen, ver 30-31) + CTA "Enviar mensaje por WhatsApp".
5. **Plantilla de mensaje**: configura el **mensaje pre-llenado** que el usuario enviará ("Hola, vi el anuncio del combo X y quiero más info"). Hazlo específico al ad: te regala contexto para el saludo del bot (ver 54) y sube la tasa de envío. Distinto por campaña = atribución gratis (ver 53).
6. Publica. El usuario ve el ad → clic → se abre tu chat con el mensaje listo → lo envía → conversación iniciada (eso es lo que pagas).

### Plantilla de presupuesto de arranque (Colombia)

| Etapa | Presupuesto diario COP | Qué buscas |
|---|---|---|
| Test inicial (sem 1-2) | $30.000–$60.000 | 3 creativos, hallar el ganador, ver costo/conv real |
| Validación (sem 3-4) | $60.000–$120.000 | Confirmar que el ganador cierra ventas, no solo conversaciones |
| Escala | +20-30% cada 3-4 días sobre el ganador | Subir sin romper aprendizaje (ver 13/15) |

## Optimización: ¿por conversación o por evento de chat?

| Nivel | Optimizas por | Cuándo |
|---|---|---|
| Básico | Conversación iniciada | Arrancando. Riesgo: Meta trae "saludadores" baratos que no compran |
| Pro | Evento de conversión de chat (lead calificado, pedido, compra) vía CAPI | Cuando tu bot/CRM ya reporta eventos a Meta (ver 53). El algoritmo aprende a traer COMPRADORES de chat |

La trampa del nivel básico: si solo optimizas conversaciones, tu costo por conversación baja y tu CPA real puede subir. Mide siempre el embudo completo (ver 53 y 58).

## Costos honestos (Colombia, jun-2026, referenciales)

El costo por conversación iniciada varía **brutalmente** por vertical, creativo y temporada:

| Vertical | Costo por conversación típico (COP) |
|---|---|
| Comida / producto impulso ticket bajo | $800 – $3.000 |
| E-com general (ropa, hogar, suplementos) | $2.000 – $8.000 |
| Servicios / estética / high-ticket | $5.000 – $25.000+ |

Caveat: estos rangos son brújula, no benchmark. Lo único que importa es tu matemática: % de conversaciones que compran × ticket × margen ≥ costo por conversación (ver 58 y economist_lushows). Un costo por conversación de $10.000 es regalado si cierras 30% de un ticket de $200.000.

### Ejemplo de unit economics CTWA (e-com suplementos)

```
Costo por conversación: $4.000 COP
Tasa conversación→venta: 18%   → CPA real = $4.000 / 0,18 = $22.222
Ticket promedio: $90.000 | margen 45% = $40.500
Margen − CPA = $40.500 − $22.222 = $18.278 de utilidad por venta  ✓ sano
```

Si el costo por conversación subiera a $9.000 con la misma tasa: CPA real $50.000 > margen $40.500 → **pierdes plata en cada venta** aunque "el ad funcione". Por eso se mide el embudo, no la conversación (ver 53).

## ¿CTWA o landing?

- **CTWA**: ticket bajo-medio, venta consultiva (el cliente pregunta antes de comprar), contraentrega/Nequi, catálogo corto, pyme sin web sólida. El 80% de los casos LatAm.
- **Web/landing** (Sales a píxel, ver 05-06): e-commerce self-service con checkout sólido, alto volumen, AOV claro, producto que no necesita explicación. Diseño/checkout: desingweb-lushows.
- En la duda: **testea ambos** con el mismo creativo 2 semanas y compara CPA real, no costo por clic/conversación.

## La ventana gratis de 72 horas

Cuando alguien te escribe desde un ad CTWA, Meta abre una **free entry point conversation**: 72 horas donde tus respuestas (incluidas plantillas de marketing) no pagan tarifa de WhatsApp. Implicación doble: responder rápido es **gratis Y vende** — el lead caliente se enfría en minutos (ver 54). Un bot 24/7 explota la ventana al 100%; un "le contesto mañana" la quema.

> ⏱️ **Precio WhatsApp 2026 (ver `actualizacion-2026-06` §8):** desde el **1-jul-2025 WhatsApp cobra POR-MENSAJE** (plantilla entregada), no por conversación de 24h. 4 categorías: **Marketing** (cara), **Utility**, **Authentication**, **Service** (gratis en la ventana de atención de 24h). **Colombia es de los más baratos de LatAm:** Marketing ≈ **$0.0125/msg** (~$50 COP), Utility/Auth ≈ **$0.0008/msg** (~$3 COP). Con la ventana gratis de 72h del CTWA, tu economía de chat es excelente — pero NO mandes plantillas de marketing fuera de ventana a toda tu base (cobra por mensaje y baja tu rating de número).

### Cuánto cuesta realmente cada categoría (referencia COP)

| Categoría | Uso | Costo aprox./msg | Dentro de ventana 72h CTWA |
|---|---|---|---|
| Marketing | Promos, recuperar carrito frío | ~$50 COP | **Gratis** |
| Utility | Confirmación de pedido, guía de envío | ~$3 COP | Gratis |
| Authentication | OTP / códigos | ~$3 COP | Gratis |
| Service | Respuestas en ventana de 24h | $0 | Gratis |

## 🔴 Medir COMPRADORES, no saludadores: el `ctwa_clid` + CAPI (lo más importante)

Por default el CTWA optimiza "conversaciones iniciadas" → Meta trae a quien abre chat, no a quien compra. Para que el algoritmo aprenda a traer **compradores**, tu bot/CRM debe:
1. **Capturar el `ctwa_clid`** (click id que llega en el objeto `referral` del webhook cuando el chat se inicia desde el ad).
2. Disparar un **evento CAPI** cuando el lead califica/paga, con el evento/`action_source` = **`business_messaging`** y **`messaging_channel: "whatsapp"`**, pasando ese `ctwa_clid`.

Sin esos campos, Meta **no puede atribuir la venta al anuncio** y sigues optimizando por curiosos. Es el upgrade #1 de un buyer WhatsApp-first en Colombia (detalle de implementación en 53; tu bot de GASTROWHATS/AVISPA'O ya recibe el webhook donde vive el `ctwa_clid`).

## 🔴 Meta Business Agent: el bot de Meta ahora compite contigo (3-jun-2026)

Meta lanzó global su **Business Agent**: un bot de IA propio que corre dentro de WhatsApp Business, IG DMs y Messenger — responde, recomienda del catálogo, agenda citas y califica leads (ver `actualizacion-2026-06` §4). Es el PRIMER agente que Meta cobra (pymes vía WhatsApp Business Premium). Implicación para ti: el bot a la medida (como GASTROWHATS) sigue ganando en control de guion, datos propios y CAPI fino, pero ya no eres el único con IA en el chat — el diferencial pasa a ser **el oficio de la conversación** (ventas_lushows 82) y la medición (ver 53), no "tener un bot".

## Errores comunes — blacklist

- Pautar CTWA sin nadie (ni bot) que responda en minutos: plata directa a la basura. Primero operación, después pauta (ver 51, 96).
- Optimizar por conversaciones para siempre y nunca medir ventas: terminas premiando al ad que trae curiosos (ver 53).
- Mensaje pre-llenado genérico ("Hola") en todas las campañas: pierdes el contexto del ad y no sabes qué campaña trajo a quién.
- Mandar CTWA a un número personal de WhatsApp no conectado a la página: el formato exige WhatsApp Business vinculado.
- Juzgar CTWA por el costo por clic comparado con tráfico web: métricas distintas; compara CPA final.
- Ignorar la ventana de 72h y responder con plantillas pagas al día siguiente: pagaste el ad Y la conversación.
- Mandar marketing templates a toda la base fuera de ventana "porque salen baratos": sumados cuestan, y bajan el quality rating del número (ver 51).
