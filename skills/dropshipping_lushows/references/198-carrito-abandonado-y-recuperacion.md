# Carrito abandonado y recuperación

> Vigencia: 14-sep-2026.

Abandonar el checkout es la norma, no la excepción: la mayoría de los que llegan al carrito no
compran. La recuperación es el canal más rentable que tienes, porque le habla a gente que **ya
levantó la mano** y cuyo clic ya pagaste.

## Antes de recuperar: arregla la fuga

Recuperar el 10% de un checkout roto rinde menos que arreglar el checkout. El orden correcto es:

1. Elimina las causas de abandono. `190`.
2. Muestra el plazo de entrega antes del checkout (~18% abandona por entrega lenta, Baymard).
3. **Luego** monta la recuperación.

## Los tres momentos de abandono

| Momento | Qué tienes | Qué puedes hacer |
|---|---|---|
| **Vio el producto y se fue** | Solo el píxel | Remarketing pagado. `200` |
| **Añadió al carrito y se fue** | Píxel + a veces el correo | Remarketing + correo si lo capturaste |
| **Empezó el checkout y se fue** | **Correo y teléfono** | Correo, WhatsApp, SMS. El más rentable |

La diferencia clave: **captura el correo lo antes posible en el checkout**. Ponlo como primer campo.
Si el cliente escribe el correo y se va en el paso del pago, tienes con qué ir por él. `190`.

## La secuencia de correos

Tres correos. Nunca más de cuatro: el cuarto genera bajas y quejas.

| # | Cuándo | Ángulo | Descuento |
|---|---|---|---|
| 1 | **1 hora** | Servicial: "se te quedó esto" | **No** |
| 2 | **24 horas** | Objeción: garantía, envío, MSI | **No** |
| 3 | **48-72 horas** | Último empujón | **Sí**, pequeño (5-10%) y con fecha |

El descuento va en el tercero, no antes. Si descuentas en el primero, entrenas a tus clientes a
abandonar el carrito a propósito.

## Los correos completos (listos para copiar — México)

### Correo 1 — a la hora

> **Asunto:** Se te quedó algo en el carrito
>
> Hola [nombre]:
>
> Vimos que dejaste tu [producto] a medio camino. Te lo guardamos por si se te fue el internet o te
> interrumpieron.
>
> **[Producto] — $1,099 MXN**
> Envío gratis · Llega en 2 a 4 días hábiles · Hasta 12 meses sin intereses
>
> **[ TERMINAR MI PEDIDO ]**
>
> Si tienes cualquier duda, contéstanos este correo o escríbenos por WhatsApp al [número].
> Contestamos el mismo día.
>
> — [Tu nombre], [Tienda]

### Correo 2 — a las 24 horas (ataca la objeción)

> **Asunto:** ¿Te quedó alguna duda?
>
> Hola [nombre]:
>
> Casi siempre que alguien deja el pedido a medias es por una de estas tres cosas. Te las contesto
> de una vez:
>
> **"¿Cuánto tarda?"** Sale de nuestra bodega en México el mismo día si pides antes de las 2 p.m.
> Te llega en 2 a 4 días hábiles y te mandamos la guía.
>
> **"¿Y si no me sirve?"** Tienes 30 días. Nos escribes, te mandamos la guía de devolución sin costo
> y te regresamos el 100% de tu dinero. Sin explicaciones.
>
> **"¿Puedo pagar a meses?"** Sí. Hasta 12 meses sin intereses con tarjeta de crédito. Son $91.58 al
> mes.
>
> **[ VOLVER A MI PEDIDO ]**
>
> — [Tu nombre], [Tienda]

### Correo 3 — a las 48-72 horas (con incentivo)

> **Asunto:** Te guardo $100 hasta mañana
>
> Hola [nombre]:
>
> Tu [producto] sigue apartado, pero no lo puedo dejar así para siempre: este lote es de 200
> unidades y quedan [X].
>
> Te dejo **$100 de descuento** con el código **VUELVE100**. Vence mañana a medianoche.
>
> **$1,099** → **$999**
>
> **[ USAR MI DESCUENTO ]**
>
> Si al final no es para ti, no pasa nada: contéstame este correo y te saco de la lista.
>
> — [Tu nombre], [Tienda]

## WhatsApp: el canal con mejor tasa en LatAm

Si capturaste el teléfono (obligatorio en COD, opcional en prepago), el WhatsApp supera al correo
por amplio margen. Reglas:

1. **Uno solo**, a las 2-4 horas. No una secuencia.
2. Tono de persona, no de empresa.
3. Pregunta, no vendas.

> Hola [nombre], soy [tu nombre] de [tienda]. Vi que empezaste tu pedido de [producto] y no se
> completó. ¿Te falló el pago o te quedó alguna duda? Cualquier cosa te ayudo por aquí.

Cuidado con dos cosas: el consentimiento para escribir (`197`) y el riesgo de bloqueo si mandas
mensajes en masa. Para el guion y la operación, invoca `ventas_lushows`.

## Remarketing pagado

Para quien no dejó datos, el único camino es el píxel. Públicos, ventanas y presupuesto se tratan
desde el lado de la plataforma: invoca `facebook_ads_lushows`. Lo que a ti te toca es que **los
eventos estén bien**: sin `ViewContent`, `AddToCart` e `InitiateCheckout` correctos, no hay público
a quien perseguir. `201`.

## Qué esperar

| Canal | Tasa de recuperación típica |
|---|---|
| Correo (secuencia de 3) | 5-12% de los carritos con correo |
| WhatsApp (1 mensaje) | Más alta que el correo en LatAm |
| Remarketing pagado | Variable; se mide por ROAS, no por tasa |

> Rangos orientativos. **Mide los tuyos**: la tasa depende muchísimo del producto y del país.

## La condición técnica que arruina todo

Si tus correos caen en spam, la recuperación no existe. Configura SPF, DKIM y DMARC en el dominio
antes de montar la secuencia. `179`. Y revisa la entregabilidad real mandándote los correos a tres
proveedores distintos.

## Lo que no debes hacer

| Error | Consecuencia |
|---|---|
| Cinco correos en dos días | Bajas, quejas de spam, dominio quemado |
| Descuento en el primer correo | Entrenas a abandonar el carrito |
| "Tu carrito expira en 15 minutos" falso | `189`. Nunca |
| Escribir sin consentimiento en la UE | Sanción. `194`, `197` |
| Correos sin enlace de baja | Ilegal en casi todas partes |
| Mandar el correo 1 a los 3 días | La ventana útil es de horas |

## Relacionados
`190` checkout · `197` confianza · `199` analítica · `200` píxel y API de conversiones · `201` eventos
