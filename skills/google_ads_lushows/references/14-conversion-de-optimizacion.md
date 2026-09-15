# 14 — Conversión de optimización

Lee este módulo antes de marcar cualquier acción como "conversión", o cuando tu Smart Bidding entrega muchísimo pero las ventas reales no aparecen (síntoma clásico de optimizar para la conversión equivocada). Esta es la decisión más subestimada de toda la cuenta: **el algoritmo compra exactamente lo que le dices que es valioso.** Si le dices que "vista de página de gracias" vale, te traerá gente que ve esa página; si le dices que "compra confirmada" vale, te traerá compradores. Smart Bidding (ver 13) es un perro perfectamente obediente: persigue el hueso que le tiras. Elige bien el hueso, porque toda la inteligencia del algoritmo se vuelve en tu contra si apunta al objetivo equivocado.

## Primaria vs secundaria (primary vs secondary)

Desde 2023 Google separa las conversiones en dos cubos, y esta distinción es la palanca más limpia que tienes:

| Tipo | Qué hace | Úsalo para |
|---|---|---|
| **Primaria** (primary) | **Optimiza el bidding** Y reporta. Es lo que el algoritmo persigue | La acción más cercana a la venta que tu volumen sostiene |
| **Secundaria** (secondary) | **Solo observa/reporta**, NO mueve el bidding | Micro-conversiones que quieres vigilar sin que distorsionen la puja |

**Regla:** solo tus acciones de venta real (compra, lead calificado, cotización enviada) deben ser **primarias**. Todo lo demás (newsletter, scroll, clic en WhatsApp sin cerrar, ver video) va a **secundaria** para que el algoritmo no las persiga. Tener 5 cosas como primarias contamina la señal: el bidding optimiza para el **promedio** de todas y termina cazando las baratas y fáciles (ver 13).

En 2026, con atribución **data-driven por default** (ver 16), la elección de qué es primario importa todavía más: DDA reparte crédito entre tus conversiones primarias, así que si metes basura en primarias, DDA te reparte crédito hacia la basura.

## Macro vs micro: cuál marcar como objetivo

| Conversión | Tipo | Cercanía a la venta | Volumen típico |
|---|---|---|---|
| **Compra / pago confirmado** | Macro | La venta misma | Bajo |
| **Lead calificado / cotización** | Macro | Muy cerca | Bajo-medio |
| **Inicio de checkout** | Micro | Cerca | Medio |
| **Clic en botón WhatsApp / llamada** | Micro | Intermedio | Medio-alto |
| **Agregar al carrito** | Micro | Lejos | Alto |
| **Vista de página, scroll, tiempo** | Micro basura | Lejísimos | Altísimo |

El dilema real: **la conversión más cercana a la venta (macro) suele tener poco volumen**, y Smart Bidding necesita ~15-30 conversiones/mes para calibrar (ver 13). La regla práctica:

> **Optimiza por la conversión más cercana a la venta que tu volumen pueda sostener (~15-30/mes).**

- Si vendes y tienes **≥15-30 compras/mes**: optimiza por **compra**. Es lo ideal.
- Si tienes **<15 compras/mes**: sube un escalón en el embudo a una **micro-conversión con buena correlación con la venta** (ej. "inicio de checkout" o "lead enviado") que sí dé volumen. Marca compra como **secundaria** para vigilar que la correlación se mantenga.
- A medida que el volumen crece, **baja el objetivo** hacia la venta real (ver 73).

### Escalera de objetivos según volumen (plantilla)

| Compras reales/mes | Conversión PRIMARIA recomendada | Compra queda como |
|---|---|---|
| <15 | Inicio de checkout / lead enviado (micro con buena correlación) | Secundaria (vigilar) |
| 15-30 | Compra, pero vigila estabilidad; o checkout si la compra aún tiembla | — |
| >30 | Compra (o valor de compra si ticket variable) | Primaria |

## El caso WhatsApp (LatAm): la trampa más común

En LatAm muchísimo negocio cierra por **WhatsApp** (el cierre conversacional rutea a `ventas_lushows`). El "clic a WhatsApp" es tentador como conversión porque da volumen y es fácil de medir. Pero es **basura como macro**: optimizas para gente que abre el chat y nunca compra; el algoritmo te inunda de curiosos que escriben "hola, info" y desaparecen.

Lo correcto: importar la **venta real desde tu CRM/backend** vía **Offline Conversion Import (OCI)** usando el **gclid** (ver 16, 53, 66, 64). El flujo:

1. La landing captura el `gclid` de la URL y lo guarda junto al lead (en un campo oculto del form o en la cookie).
2. Cuando ese lead cierra por WhatsApp/teléfono (días después, offline), marcas la venta en tu CRM con su gclid.
3. Subes esas ventas a Google (manual, hoja conectada, o API/Zapier) → Google une la venta real al clic original.
4. El bidding aprende qué clic **cierra venta**, no cuál solo abre chat.

Sin gclid + OCI, en negocios que cierran offline/WhatsApp (mayoría en Colombia) **el algoritmo optimiza a ciegas** y vas a pagar por clics-a-WhatsApp que no facturan. Como puente mientras montas OCI: usa "clic a WhatsApp" como **secundaria** y "inicio de conversación calificada" (si tu plataforma lo distingue) como primaria temporal — pero la meta es OCI con venta real.

## Valor vs conteo (value-based bidding)

| Optimizar por… | Cuándo | Estrategia de puja |
|---|---|---|
| **Conteo de conversiones** | Todas las ventas valen ~lo mismo (producto de precio único: la calculadora a $10.000 COP) | Maximize conversions / tCPA (ver 15) |
| **Valor de conversión** | Ticket variable (e-commerce con productos de $20k a $500k COP) | Maximize conv. value / tROAS (ver 15) |

Si tus ventas tienen valores muy distintos, **pásale el valor real a cada conversión** (no un valor fijo) para que el bidding priorice las ventas grandes. Con producto de precio único, el conteo basta. Para valor necesitas enviar el monto en el tag/GA4 (ver 05) o vía OCI con valor (ver 53). Truco avanzado: si conoces el **margen** por producto, envía el *valor de margen* en vez del precio de venta para que el algoritmo optimice ganancia real, no facturación (la viabilidad/unit economics rutea a `economist_lushows`).

## Higiene de conversiones — checklist

- Una sola acción primaria por objetivo de negocio (o un grupo coherente).
- Enhanced Conversions activado (piso 2026, ver 06) → recupera señal perdida por cookies.
- Sin doble conteo (gracias-page y evento de compra cuentan lo mismo → elige uno, ver 04).
- gclid capturado en el sitio para poder cerrar el loop con OCI (ver 16, 66).
- Conteo "uno" para leads (un lead = una conversión) y "cada" para e-commerce (cada compra cuenta).

## Errores comunes — blacklist

- **Marcar "clic en WhatsApp" o "pageview" como conversión primaria**: el algoritmo te trae aperturas de chat y visitas, no compradores (ver 13).
- **Tener 4-5 conversiones primarias** a la vez: el bidding optimiza por el promedio y persigue las baratas/fáciles (ver 13).
- **Optimizar por compra con <10 ventas/mes**: sin volumen no calibra; sube de escalón en el embudo temporalmente.
- **No importar la venta real del CRM** (OCI) en negocios que cierran offline/WhatsApp: el algoritmo nunca sabe qué lead cerró (ver 53, 66).
- **Usar conteo cuando los tickets varían 10x**: tratas igual una venta de $20k y una de $500k; pierdes plata. Usa valor (ver 15).
- **Contar la misma venta dos veces** (gracias-page + evento de compra): infla todo y engaña al bidding (ver 04).
- **No capturar el gclid** en la landing: te quedas sin forma de cerrar el loop con OCI para siempre (ver 16).
- **Nunca bajar el objetivo hacia la venta** aunque ya tengas volumen: te quedas optimizando una micro-conversión floja para siempre (ver 73).
