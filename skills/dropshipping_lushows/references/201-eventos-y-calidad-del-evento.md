# Eventos y calidad del evento

> Vigencia: 14-sep-2026. Cómo usar estos eventos para optimizar y construir públicos: invoca
> `facebook_ads_lushows`. Aquí va **qué debe emitir tu tienda y con qué datos**.

## Los eventos que necesita una tienda

| Evento | Cuándo dispara | Para qué sirve | ¿Obligatorio? |
|---|---|---|---|
| `PageView` | Cada página | Base de públicos | Sí |
| `ViewContent` | Página de producto | Remarketing y aprendizaje | Sí |
| `AddToCart` | Añadir al carrito | Público caliente, diagnóstico de embudo | Sí |
| `InitiateCheckout` | Empieza el checkout | Público muy caliente, recuperación | Sí |
| `AddPaymentInfo` | Mete datos de pago | Señal de intención máxima | Recomendado |
| **`Purchase`** | **Después del pago confirmado** | **El evento que optimiza todo** | **Sí** |
| `Lead` | Envía el formulario COD | En COD, es el evento de conversión. `191` | Solo COD |
| `Search` | Usa el buscador | Poco útil en tienda de un producto | No |

Una tienda de un producto necesita **cinco**: PageView, ViewContent, AddToCart, InitiateCheckout y
Purchase. Más eventos no es mejor: es más superficie para errores.

## Los parámetros que no pueden faltar

| Evento | Parámetros mínimos |
|---|---|
| `ViewContent` | `content_ids`, `content_type`, `value`, `currency` |
| `AddToCart` | `content_ids`, `value`, `currency`, `contents` con cantidad |
| `InitiateCheckout` | `value`, `currency`, `num_items` |
| **`Purchase`** | **`value`, `currency`, `content_ids`, `order_id`** |

El `order_id` es el que permite deduplicar y conciliar contra tus pedidos reales. Sin él, no puedes
auditar nada.

## La calidad del evento: qué es y por qué importa

Las plataformas puntúan qué tan bien pueden hacer coincidir tu evento con una persona real. Esa
puntuación depende de cuántos parámetros de identificación mandas. Cuanto mejor la coincidencia,
mejor la optimización, y **más bajo tu CAC con el mismo creativo**.

| Parámetro | Efecto en la coincidencia |
|---|---|
| **Correo electrónico** | El más fuerte |
| **Teléfono** (con código de país) | Muy fuerte, sobre todo en LatAm |
| Nombre y apellido | Medio |
| Ciudad, estado, código postal, país | Medio |
| ID externo (tu ID de cliente) | Alto si es consistente |
| IP y user agent | Automáticos por la API |
| Cookies de clic y de navegador | Altos, pero frágiles |

Todos se envían **cifrados** por la integración oficial; tú nunca mandas datos en claro. Si una
herramienta te pide subir correos sin cifrar, no la uses.

## El diagnóstico por evento

Este es el uso que casi nadie le da y el que más sirve: los eventos te dicen dónde está roto el
negocio.

| Síntoma en los eventos | Diagnóstico | Módulo |
|---|---|---|
| Muchos `PageView`, pocos `ViewContent` | El anuncio manda a la página equivocada | `facebook_ads_lushows` |
| Muchos `ViewContent`, pocos `AddToCart` | La página no convence: promesa, precio o confianza | `204` |
| Muchos `AddToCart`, pocos `InitiateCheckout` | Costo de envío o plazo sorprenden en el carrito | `190` |
| Muchos `InitiateCheckout`, pocos `Purchase` | Checkout roto, método de pago faltante, o precio final inesperado | `190`, `192` |
| `Purchase` con valor 0 | Configuración rota. Tu ROAS es ficción | `200` |
| Más `Purchase` que pedidos reales | Duplicación o disparo al recargar | `200` |
| Menos `Purchase` que pedidos reales | Falta la API de conversiones | `200` |

**La auditoría semanal:** compara el número de `Purchase` de la plataforma contra los pedidos reales
de tu panel. Si la diferencia pasa del 10-15%, deja de optimizar y arregla la medición primero.

## Valor: ingreso o margen

| Qué mandas en `value` | Consecuencia |
|---|---|
| Ingreso bruto (lo estándar) | La plataforma optimiza por facturación |
| Margen de contribución | Optimiza por utilidad. Más avanzado, más correcto |
| 0 o vacío | No optimiza nada |

Si vendes un bundle de 1.099 MXN y un producto suelto de 699 MXN, mandar el valor real hace que la
plataforma aprenda a buscar compradores del bundle. Eso vale mucho: la utilidad pasa de USD 2,63 a
USD 20,18. `195`.

## El caso COD

En contraentrega, el pedido creado **no es una venta**. Si optimizas por `Lead`, la plataforma te
traerá gente que llena formularios y no recibe el paquete.

| Práctica | Veredicto |
|---|---|
| Optimizar por `Lead` del formulario | Funciona para arrancar, pero atrae pedidos basura |
| **Mandar `Purchase` cuando el pedido se entrega y se cobra** | **Lo correcto.** Requiere enviar el evento desde tu sistema, con retraso |
| Mandar el valor bruto sin descontar devoluciones | ROAS inflado |

Es más trabajo, pero es la diferencia entre escalar ventas y escalar devoluciones. `191`.

## Errores frecuentes

| Error | Costo |
|---|---|
| Moneda mal puesta (USD en tienda MXN) | ROAS irreal por ~18x |
| Disparar `Purchase` al cargar la página de gracias (y al recargarla) | Conversiones infladas |
| `content_ids` que no coinciden con el catálogo | El catálogo dinámico no funciona |
| No mandar `order_id` | Imposible auditar o deduplicar |
| Cambiar la estructura de eventos en plena campaña | Resetea el aprendizaje |
| Instalar tres apps que disparan los mismos eventos | Duplicación triple |

## Antes de encender pauta

1. Los cinco eventos disparan, **una sola vez cada uno**.
2. `Purchase` trae valor, moneda y `order_id` correctos.
3. Correo y teléfono se envían por la API.
4. La deduplicación está verificada.
5. La moneda es la de cobro.
6. Una compra real de prueba aparece completa y luego se concilia con el panel.

## Relacionados
`200` píxel y API de conversiones · `199` analítica · `190` checkout · `191` COD · `204` diagnóstico
