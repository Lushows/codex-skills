# 55 — Catálogo de WhatsApp y commerce dentro del chat

WhatsApp no es solo chat: tiene **catálogo de productos y carrito nativo** — el cliente ve fotos y precios, arma su pedido y lo envía sin salir de la app ni pasar por una web. Lee este módulo si vendes productos por WhatsApp y todavía mandas fotos sueltas y listas de precios en texto. Es el stack de e-commerce de la pyme LatAm sin página web. Jerga: "carrito nativo" = el cliente agrega productos del catálogo y manda el pedido como mensaje estructurado; "orders in chat" = ese pedido como evento medible.

## El catálogo de WhatsApp Business

- Qué es: una vitrina en tu perfil de WhatsApp con productos — foto, nombre, precio, descripción, link opcional. El cliente la abre desde tu perfil o cuando le compartes un producto en el chat.
- Dónde se crea: en la **app WhatsApp Business** (Herramientas → Catálogo) o, si usas la API/Cloud API, vía **Commerce Manager** de Meta (catálogo conectado al número).
- Estándar por producto:
  - **Foto** cuadrada (1:1) limpia, producto protagonista, sin marca de agua ajena.
  - **Nombre** descriptivo ("Melena de León cápsulas x120", no "REF-031").
  - **Precio SIEMPRE visible** — en LatAm "precio al inbox" quema confianza... pero en el catálogo el precio ya está; esa es la gracia.
  - **Descripción** de 2-4 líneas con presentación y beneficio.
- Comparte productos del catálogo dentro del chat como tarjetas: reemplaza el "te mando fotos" artesanal.

## Carrito nativo y flujo de pedido en chat

El cliente puede agregar productos del catálogo a un **carrito** y enviártelo como pedido estructurado (con la API son mensajes de tipo `order` — señal medible, ver 53). El flujo completo:

```
1. Cliente arma pedido (carrito o lo pide en texto)
2. Confirmas items + total + costo de envío
3. Datos de envío: nombre, dirección, ciudad, teléfono
4. Pago — las 3 vías LatAm:
   • Link de pago (Wompi/Bold/MercadoPago): para pagar YA con tarjeta/PSE
   • Nequi/Daviplata: QR o número, cliente manda comprobante
   • Contraentrega: paga al recibir (la favorita de Colombia)
5. Confirmación con resumen + tiempo de entrega + guía cuando despaches
```

Define este flujo por escrito y dáselo al bot/equipo (la conversación de venta: ventas_lushows 82; el handoff desde el ad: ver 54).

### Las 3 vías de pago LatAm comparadas

| Vía | Pro | Contra | Cuándo |
|---|---|---|---|
| Link de pago (Wompi/Bold) | Cobras antes de despachar, $0 riesgo de devolución | Comisión ~2,5-3,5% + IVA; algunos desconfían de tarjeta | Ticket medio-alto, cliente urbano |
| Nequi/Daviplata | Sin comisión, instantáneo, masivo en Colombia | Tienes que verificar el comprobante (cuidado con falsos) | Default ticket bajo-medio |
| Contraentrega | Máxima confianza, cero fricción | Devoluciones se comen el margen; pagas flete del rechazo | Validando ciudad + teléfono SIEMPRE |

> ⚠️ Contraentrega: valida ciudad cubierta + teléfono real antes de despachar. Una tasa de devolución del 15-20% puede borrar tu margen entero — mídela y cóbrala en el precio si tu zona la tiene alta (modela el impacto con economist_lushows).

## Conectar el catálogo a la pauta

- **Ads de catálogo con destino WhatsApp**: campañas que muestran productos del catálogo y al clic abren el chat **con ese producto cargado** en el contexto. El cliente llega diciendo "me interesa ESTE" — calificación gratis.
- Setup: catálogo en Commerce Manager + número de WhatsApp Business conectado a la página → en el ad set, formato catálogo/Advantage+ catalog con destino WhatsApp (la versión dinámica completa con píxel: ver 56).
- También sirve orgánico: responder consultas compartiendo la tarjeta del producto en vez de teclear precios.
- 2026: los **orders in chat / carrito** son señal de compra que Meta ve dentro de su ecosistema — combínalos con CAPI de mensajería (ver 53) para optimizar por compradores, no por saludadores.

## Sincronizar el catálogo: Commerce Manager

**Un solo catálogo** en Commerce Manager alimenta FB Shop, Instagram Shopping, WhatsApp y los ads de catálogo (ver 56). Fuentes de datos, de menor a mayor escala:

| Fuente | Cuándo |
|---|---|
| Manual (subes producto por producto) | ≤30 productos, precios estables |
| Hoja de cálculo / feed programado | 30-500 productos, actualizas la hoja y se sincroniza |
| Feed de tienda (Shopify/Woo nativo) | Ya tienes web: la integración monta y actualiza todo sola |

Regla: el precio del catálogo y el precio que dice el chat NUNCA difieren — mata la confianza y viola políticas de comercio de Meta (riesgo de restricción de la tienda, ver 08).

## El stack pyme completo sin web

`Ads CTWA (ver 50) + catálogo de WhatsApp + bot/humano que cierra + Nequi/contraentrega` — es un negocio **válido y rentable**. No necesitas web para empezar a vender en serio.

### Costo de montar el stack (referencia Colombia, jun-2026)

| Pieza | Costo |
|---|---|
| WhatsApp Business app + catálogo | Gratis |
| Cloud API + bot a la medida | Desarrollo (1 vez) + hosting ~$30-100k COP/mes (ver 96) |
| Mensajes WhatsApp (Util/Auth) | ~$3 COP c/u; gratis dentro de ventana de 24h/72h (ver 50) |
| Pasarela de pago (Wompi/Bold) | ~2,5-3,5% + IVA por transacción cobrada |
| Pauta CTWA | Tu presupuesto (ver 50) |

Cuándo SÍ ya necesitas web/checkout (desingweb-lushows):

- Volumen que el chat no aguanta (cada venta cuesta 10-20 min de conversación).
- AOV/ticket alto donde el pago con tarjeta formal sube conversión y baja contraentrega fallida.
- Quieres **Advantage+ catalog ads dinámicos serios** con retargeting por píxel (ViewContent/ATC) — eso exige web con eventos (ver 56).
- SEO, email marketing, marca: activos que el chat no construye.

Las fotos son el 80% del catálogo: dirección de fotografía de producto → skill directorcreativo_lushows.

## Higiene del catálogo: el mantenimiento que casi nadie hace

Un catálogo no es "móntalo y olvídalo". Lo que lo mantiene vendiendo:

- **Revisión de precios semanal**: cualquier cambio de precio entra primero al catálogo, después al chat. Un precio viejo en una tarjeta compartida es una promesa que no puedes cumplir.
- **Orden por rotación**: pon arriba los 3-5 productos que más se venden; el cliente promedio no baja más de media pantalla. Los héroes adelante.
- **Agotados ocultos, no visibles**: marca disponibilidad o esconde el producto sin stock. Mostrar lo agotado genera la consulta que no puedes cerrar.
- **Descripciones que responden la pregunta repetida**: si tres clientes preguntan "¿cuántas porciones trae?", esa respuesta va en la descripción. Cada FAQ resuelta en el catálogo es una conversación más corta y más cierres.
- **Combos como producto propio**: el combo (Melena + Reishi) sube el ticket promedio. Créalo como ítem de catálogo con su foto y su precio de paquete, no como suma improvisada en el chat.

## Del catálogo a la recompra

El número que pidió por catálogo queda guardado: es tu activo de recompra. Tras la entrega, una plantilla de Utility a los X días ("¿cómo te fue con [producto]? Ya casi se te acaba 👇") reactiva al cliente con costo de centavos (ver 50/51 para tarifas y ventana). La recompra es la venta más barata que existe — no tiene costo de pauta. El catálogo bien armado no solo cierra la primera venta: arma la base que financia las siguientes.

## Errores comunes — blacklist

- Catálogo sin precios "para que pregunten": en 2026 el que no ve precio se va donde sí lo ve.
- Fotos oscuras/de WhatsApp reenviado con marca de agua ajena: la vitrina ES la tienda; invierte ahí primero.
- Precios desactualizados entre catálogo, chat y ads: devoluciones, peleas y strikes de Meta.
- Mandar 15 fotos sueltas cuando existe la tarjeta de producto: pareces improvisado y nada queda medible.
- Contraentrega sin validar (dirección incompleta, teléfono apagado): la tasa de devolución se come el margen — mídela (economist_lushows).
- Aceptar comprobante Nequi sin verificarlo: los falsos circulan; confirma el ingreso antes de despachar.
- Aplazar la web cuando ya tienes 30+ pedidos/día por chat: el chat no escala infinito; llegó la hora (desingweb-lushows).
