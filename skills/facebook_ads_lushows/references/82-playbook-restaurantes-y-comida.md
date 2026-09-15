# 82 — Playbook: Restaurantes y comida

Restaurantes, dark kitchens (cocinas solo para domicilio), repostería, comida fit, antojos. El vertical más emocional de todos: **el antojo es visual e inmediato** — nadie "considera" una hamburguesa por dos semanas. El ad correcto a la hora correcta en el radio correcto genera el pedido en minutos. Eso define todo: creativo apetitoso, horario de hambre, geo de entrega real, y pedido directo por WhatsApp para no regalar margen a las apps. Es el vertical de GASTROWHATS: el bot que cierra el pedido por chat ES la pieza que vuelve rentable la pauta.

## Creativos: el antojo entra por los ojos

- **El plato en su mejor momento**: vapor saliendo, el queso estirándose, el corte de la torta, la salsa cayendo. Video vertical de 6-15s (ver 34), primer plano, luz natural, SIN intro — el queso estira en el segundo 1 (ver 37).
- **El chef/la cocina en acción**: las manos armando el plato, la parrilla, el horno. Vende frescura y oficio.
- **Reseña de cliente comiendo**: UGC real (ver 32) — la primera mordida y la cara de placer venden más que cualquier claim.
- **Estática de oferta**: foto apetitosa + "Combo del día $25.900" en grande (ver 35).

Producción: tu celular + luz de ventana + el plato recién hecho. La comida es del 10% de verticales donde lo casero gana a lo producido. El **Advantage+ Creative Suite** (image-to-video con hasta 20 fotos del menú → video multi-escena, ver `actualizacion-2026-06`) te da variantes rápido, pero el plato fotogénico es trabajo de cámara, no de IA.

## Horarios de pauta = horarios de hambre

Pautar a las 4am es regalar plata. Programa franjas con **lifetime budget** (presupuesto total con calendario, único modo que permite programar horas — ver 57): **10:30-13:30 y 17:30-20:30**, cuando el cerebro decide qué almorzar/cenar. Ajusta a tu producto: brunch/repostería en mañana de fin de semana, alitas y pizza jueves-domingo noche. El ad de mediodía debe estar entregando desde las 10:30 — el antojo se siembra ANTES del pico.

## CTWA: el pedido directo que salva el margen (lo más importante)

Las apps de domicilio cobran 20-30% de comisión. Un pedido que entra por WhatsApp directo (ver 50/55) te deja ese margen — **y ese margen es el que paga la pauta**. Flujo: ad del plato → CTWA con mensaje pre-llenado ("Hola, quiero el combo del día") → bot (GASTROWHATS) o persona toma el pedido → pago Nequi o contraentrega → domicilio propio. Monta el **catálogo de WhatsApp con el menú** (fotos + precios): el cliente pide sin que le mandes el PDF borroso de siempre.

Economía 2026 a tu favor (ver `actualizacion-2026-06`): WhatsApp cobra **por mensaje** desde jul-2025, pero al responder dentro de 24h a quien llegó por un ad CTWA se abre una **ventana gratis de 72h que cubre marketing incluido**; y Colombia es de los países más baratos. Tu bot prácticamente no paga mensajería en la conversación de venta.

**Medición correcta (el upgrade #1):** por default CTWA optimiza "conversaciones iniciadas" → trae saludadores. Para optimizar por COMPRADORES, el bot debe **capturar el `ctwa_clid`** (click id que llega al iniciar el chat) y disparar un **evento CAPI** con `action_source = business_messaging` y `messaging_channel: "whatsapp"` cuando el cliente confirma/paga el pedido (ver 53). Sin eso, Meta no atribuye la venta y entrega leads que no compran. Esto MAPEA directo al loop de GASTROWHATS.

## Geo: el radio de entrega REAL

Pauta únicamente el polígono donde de verdad entregas caliente (ver 26): 3-5 km típico para domicilio propio. El pedido desde 12 km que llega frío te cuesta el ad + el reembolso + la reseña mala. Para restaurante de mesa (no domicilio): radio de desplazamiento por antojo, 3-6 km, más en fin de semana. Dark kitchen multi-zona: un ad set por zona de cobertura.

## La cuenta concreta

| Campaña | Tipo | Objetivo | Creativos | Medición | Notas |
|---|---|---|---|---|---|
| **Pedidos directos** | Engagement→WhatsApp (CTWA) | conversación → `ctwa_clid` + CAPI pedido | 3-5 platos distintos, video apetitoso | costo por **pedido** (no por chat) | lifetime budget con franjas de hambre |
| **Ventas web** (si mides con píxel) | Advantage+ Sales | Purchase del menú online | combos + estáticas de oferta | ROAS real | solo si tienes checkout propio |
| **Apertura / awareness** | Alcance, radio 2-3 km, 5-10 días | recordación de barrio | "ya abrimos" + oferta de apertura | costo por mil | excepción temporal (ver abajo) |

## Ofertas que funcionan: llenar valles, no picos

El error clásico: promocionar el viernes noche (ya está lleno). La pauta inteligente llena huecos:

- **Combo del día** (lunes-jueves almuerzo): precio cerrado, decisión fácil.
- **2x1 el martes muerto**: el descuento agresivo se justifica el día que igual pierdes plata.
- **Postre/adición gratis en el primer pedido**: adquisición barata, el costo real es ingrediente, no precio de carta.
- **Combo familiar fin de semana**: sube el ticket del domicilio.

Diseño de oferta y matemática: ver 41 y economist_lushows (el **food cost** manda — un 2x1 con 35% de food cost funciona; con 55% te quiebra).

## Apertura y awareness local

Excepción a "nunca pautes alcance": para una **apertura**, una campaña de Alcance con radio chico (2-3 km) por 5-10 días sí sirve (ver 59) — que el barrio sepa que existes. Combínala desde el día 1 con CTWA de oferta de apertura para capturar a los antojados.

## Presupuesto y benchmarks honestos (Colombia)

- **$20.000-$80.000 COP/día** mueve la aguja en un radio de barrio.
- Costo por conversación: **$800-$3.000 COP**; conversación→pedido **20-50%** si respondes en minutos.
- CPM local de comida: **$5.000-$15.000 COP** (de los más baratos, el creativo apetitoso baja el CPM).
- Caveat: depende brutalmente del creativo y la hora; tu plato más fotogénico puede costar la mitad que el menú genérico. Mide costo por **PEDIDO**, no por chat.

## Domicilios propios vs apps

Si vives de apps (Rappi etc.), la pauta lleva a tu perfil en la app — pagas pauta Y comisión, solo tiene sentido para rankear o lanzar. La jugada de margen: usar pauta para **migrar clientes de la app a tu WhatsApp** (volante en el pedido, descuento por pedir directo). Web/menú digital y SEO local: desingweb 42; intención "domicilios sushi cerca" → google_ads.

## Compliance específico

Comida es vertical tranquilo en policy, con dos excepciones: claims de salud en comida fit ("baja de peso con nuestros bowls" ❌ — ver 44, aplica lo de 83) y alcohol si vendes licor con la comida (targeting 18+ obligatorio, ver 08). Registro INVIMA si empacas/etiquetas producto para venta masiva.

## Ruteo a skills hermanas

Cierre del pedido y upsell en el chat ("¿le agrego papas?") → ventas_lushows. Menú digital / landing de pedidos → desingweb-lushows. Identidad, fotografía de comida y branding del local → directorcreativo_lushows. Food cost, margen del combo y punto de equilibrio → economist_lushows. Intención local en buscador → google_ads; food porn en formato nativo y trends → tiktok_ads.

## Errores comunes — blacklist

- Foto oscura del plato tomada de noche con flash: el anti-antojo.
- Pautar 24/7 con presupuesto diario: la mitad del gasto cae fuera de horas de hambre.
- Radio gigante que promete domicilios que llegan fríos: pagas por reseñas de 1 estrella.
- Mandar el clic a un PDF de menú o a un link de app con comisión cuando podías cerrar en WhatsApp.
- Optimizar por "conversaciones iniciadas" sin capturar `ctwa_clid` ni disparar CAPI: pagas saludadores (ver 53).
- Promocionar el día/hora que ya está lleno y dejar el martes vacío.
- No responder el chat en 5 minutos: el antojo es perecedero — a los 20 minutos ya pidió pizza.
- Olvidar el catálogo de WhatsApp y dictar el menú a mano en cada chat.
- Un 2x1 sin mirar food cost: vender más para perder más.
