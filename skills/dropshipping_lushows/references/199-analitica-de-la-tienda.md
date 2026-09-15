# Analítica de la tienda

> Vigencia: 14-sep-2026. Métricas de campaña (CPM, CTR, frecuencia, ROAS por conjunto): invoca
> `facebook_ads_lushows`. Cálculos y significancia: invoca `Matematicas_lushows`.

La analítica de la tienda responde una pregunta que la plataforma de anuncios no puede responder:
**¿dónde se está cayendo la gente que ya traje?**

## El embudo mínimo

Estos cinco números, cada día, en una hoja. Nada más.

| Paso | Métrica | Qué significa si falla |
|---|---|---|
| 1 | **Sesiones** | Lo que trajiste |
| 2 | **% que ve el producto** | Si es bajo, el problema es el enlace del anuncio |
| 3 | **% que añade al carrito** (de sesiones) | Si es bajo, el problema es la página. `204` |
| 4 | **% que inicia checkout** (de los que añadieron) | Si es bajo, el problema es el precio o el envío |
| 5 | **% que compra** (de los que iniciaron) | Si es bajo, el problema es el checkout o el pago |

## Las tasas de referencia

| Transición | Rango sano (prepago, tráfico pagado frío) |
|---|---|
| Sesión → añade al carrito | 6-12% |
| Añade al carrito → inicia checkout | 45-65% |
| Inicia checkout → compra | 45-65% |
| **Sesión → compra (conversión)** | **2,0% conservador / 3,0% buena página / 4,0% ganador.** `203` |

> Rangos orientativos para 2026. Varían por producto, país y precio. **Mide los tuyos y compáralos
> contigo mismo, no con estos números.**

Multiplica las tres tasas intermedias para ver si cuadran con tu conversión final. Si no cuadran,
tu medición está rota antes que tu tienda. `201`.

## Las métricas de negocio (las que deciden)

| Métrica | Fórmula | Por qué |
|---|---|---|
| **Ticket promedio (AOV)** | Ingreso / pedidos | Sube el techo de CAC. `11` |
| **CAC** | Gasto en anuncios / pedidos | El número que decide si vives |
| **Margen de contribución por pedido** | Ticket − costo producto − envío − comisiones − CAC | La utilidad real |
| **ROAS de equilibrio** | Ticket / margen bruto por pedido | Con el modelo del proyecto: **1,95** |
| **Tasa de devolución** | Devueltos / entregados | `188` |
| **Tasa de entrega** (solo COD) | Entregados / despachados | En COD manda sobre todo lo demás. `191` |

Modelo verificado del proyecto (México, bundle 1.099 MXN): ticket USD 60,05 · costo USD 29,33 ·
techo de CAC USD 30,73 · CAC USD 10,54 · utilidad USD 20,18 · holgura 2,92x · ROAS de equilibrio
1,95. Ese es el tablero: si el CAC se acerca a 30,73, estás en el borde.

## Las herramientas

| Herramienta | Para qué | Prioridad |
|---|---|---|
| **Panel de tu plataforma** | Embudo, pedidos, ticket, productos | **Primera.** Es la verdad del dinero |
| **GA4** | Origen del tráfico, comportamiento, embudos personalizados | Segunda |
| **Mapa de calor / grabación de sesión** | Ver dónde se atasca la gente | Tercera, y muy reveladora |
| Hoja de cálculo diaria | Gasto, pedidos, ingreso, CAC, ROAS | **Innegociable** |
| Panel de la pasarela | Contracargos, rechazos, retenciones | Semanal |

La hoja de cálculo diaria no es opcional. Las plataformas atribuyen distinto entre ellas; el único
número que no discute nadie es: **cuánto salió de tu banco y cuánto entró**.

## La discrepancia de números (y cómo no volverse loco)

Meta dirá 47 compras, tu tienda dirá 39, tu banco dirá 38.

| Fuente | Qué mide | Cuándo usarla |
|---|---|---|
| Plataforma de anuncios | Conversiones atribuidas con su ventana | Para **optimizar campañas** |
| Panel de la tienda | Pedidos reales | Para **operar** |
| Banco / pasarela | Dinero cobrado | Para **contabilidad** |

Regla: **decide gasto con la plataforma, cuenta dinero con el banco.** Nunca mezcles.

## Las grabaciones de sesión: la herramienta subestimada

Media hora viendo 20 grabaciones te enseña más que una semana de dashboards. Qué buscar:

1. ¿Hasta dónde baja la gente antes de irse? Esa sección es el problema.
2. ¿Hacen clic en cosas que no son clicables? Falta de claridad.
3. ¿Suben y bajan repetidamente en una zona? Ahí hay una duda sin resolver. Va a la FAQ. `187`.
4. ¿Abandonan en un campo específico del checkout? Ese campo sobra o está roto. `190`.
5. ¿Se quedan mirando el precio y se van? Problema de oferta, no de página. `204`.

## La cadencia

| Frecuencia | Qué revisas |
|---|---|
| **Diario** | Gasto, pedidos, ingreso, CAC, ROAS. 5 minutos |
| **Semanal** | Embudo completo, tasas por paso, ticket, devoluciones, 20 grabaciones |
| **Quincenal** | Resultado de las pruebas A/B. `202` |
| **Mensual** | Margen real con todos los costos, contracargos, estado de la pasarela |

## El error de leer datos sin volumen

Con 60 sesiones y 1 pedido no tienes un 1,7% de conversión: tienes ruido. Antes de tomar cualquier
decisión sobre la página, exige:

| Decisión | Mínimo razonable |
|---|---|
| "La página no convierte" | 300-500 sesiones en la página de producto |
| "Este cambio mejoró la conversión" | Prueba A/B con significancia. `202` |
| "El producto no sirve" | 1.000+ sesiones y al menos 3 creativos distintos probados |
| "El checkout está roto" | Basta con **1** compra de prueba fallida. `190` |

## Relacionados
`200` píxel y API de conversiones · `201` eventos · `202` pruebas A/B · `203` conversión esperada · `204` diagnóstico
