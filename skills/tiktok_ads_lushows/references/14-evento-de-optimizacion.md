# 14 — Evento de optimización

Lee este módulo cuando crees una campaña Sales y TikTok te pregunte "¿qué evento quieres optimizar?", cuando tengas muchos *Add to cart* pero cero compras, o cuando tu campaña no logre juntar 50 conversiones a la semana. El evento de optimización es **la instrucción más concreta** que le das al algoritmo: le dices "tráeme gente que haga ESTO", y TikTok va y busca gente que hace exactamente eso. Elegir el evento decide a quién trae el sistema — es la diferencia entre llenar tu carrito de curiosos o tu banco de compradores.

## El embudo de eventos: de curiosos a compradores

TikTok manda eventos a través del **Pixel / Events API** (ver 57). Estos eventos forman un embudo, de arriba (mucha gente, poco valor) a abajo (poca gente, máximo valor):

| Evento | Qué hizo la persona | Frecuencia | Calidad de intención |
|---|---|---|---|
| **Page view / ViewContent** | Vio la landing/producto | Altísima | Baja (curiosos) |
| **Add to cart (ATC)** | Agregó al carrito | Alta | Media |
| **Initiate checkout** | Empezó el pago | Media | Media-alta |
| **Complete payment / Purchase** | **Pagó** | Baja | **Máxima** |
| **Lead** | Dejó datos / formulario | Variable | Media-alta (servicios, ver 54) |
| **Custom event** | El que tú definas (ej. "agendó cita", "inició chat WhatsApp") | Tú decides | Tú decides |

**Regla de oro:** optimiza siempre por el evento **más cercano a la venta** que tu volumen permita. Para un e-commerce, eso es **Complete payment**. Ese evento le enseña a TikTok cómo se ve un comprador real tuyo, y va a buscar más como ese. Optimizar por algo más arriba "porque hay más datos" es optimizar por la persona equivocada.

## Subir o bajar en el funnel según el volumen

El conflicto: *Complete payment* es el evento ideal, pero es el más raro. Si vendes poco, nunca juntas las ~50 conversiones/semana que pide la fase de aprendizaje (ver 13), y la campaña se queda en *Learning Limited* — caro e inestable.

La solución es **subir el evento en el funnel** (a uno que ocurra más seguido) cuando no hay volumen:

| Tu situación | Optimiza por | Por qué |
|---|---|---|
| Vendes ≥7/día (juntas 50 compras/sem) | **Complete payment** | Ideal: aprende del comprador real |
| Vendes 4–6/día | **Initiate checkout** | Ocurre ~2× más que la compra; suficiente volumen |
| Vendes 2–3/día | **Add to cart** | Ocurre ~3–5× más; puente temporal |
| Producto nuevo, casi sin ventas | **ATC o ViewContent** | Para arrancar y juntar señal; migra apenas puedas |
| Servicio / high-ticket | **Lead** (ver 54) | La venta real es offline; el lead es tu proxy |
| LatAm WhatsApp-first | **Custom "inició chat"** o Lead | El cierre pasa por chat (ver `ventas_lushows`) |

Trade-off honesto: cuanto más arriba subes (ATC, ViewContent), más volumen y más rápido sale de aprendizaje, **pero menor calidad** — traes gente que agrega al carrito y no paga. Es un puente temporal: arrancas con ATC para que el algoritmo aprenda, y **bajas a Complete payment apenas tengas volumen**. No te quedes optimizando ATC para siempre o vivirás de carritos abandonados que nunca cierran.

Cambiar el evento **resetea el aprendizaje** (ver 13), así que no lo cambies a la ligera — hazlo cuando tengas evidencia de volumen, no por ansiedad. Un buen momento para migrar: cuando tu evento intermedio ya pasa de 50/sem cómodamente y tu tasa de compra/evento es estable.

## El evento decide a quién trae el sistema

Esto es lo que mucha gente no entiende: TikTok no "intenta vender". TikTok **busca personas parecidas a las que ya dispararon tu evento elegido**.

- Optimizas por *ViewContent* → busca gente que ve productos (curiosos, baja conversión).
- Optimizas por *Add to cart* → busca gente que llena carritos (algunos compran, muchos no).
- Optimizas por *Complete payment* → busca gente que PAGA (compradores reales).

Por eso optimizar por un evento alto del funnel "porque hay más datos" sabotea las ventas: le enseñas al algoritmo a buscar mirones. **El evento ES tu definición de "cliente bueno".** Si tu definición es floja, tu tráfico es flojo.

## Eventos de valor (VBO/ROAS goal) y cuándo usarlos

Si vendes productos con tickets muy distintos ($10.000 vs $300.000), el evento *Complete payment* solo no basta: querrás que TikTok persiga **valor**, no cantidad. Ahí entra optimizar por valor con ROAS goal / VBO (ver 15), que exige que el Pixel mande el **value** correcto de cada compra (ver 57). Sin ese dato, VBO optimiza a ciegas. Para tickets parejos (un solo producto a $10.000), Complete payment a secas es suficiente y más estable.

## Cuídate de los eventos sucios

Si tu Pixel dispara *Complete payment* en la página de "gracias" pero también en recargas de página, en pagos fallidos, o dos veces por un solo pedido, le estás enseñando basura a TikTok. Antes de confiar en la optimización, verifica en el **Events Manager** que cada evento dispara **una sola vez y en el momento correcto** (ver 57). Un evento sucio es peor que no tener evento: optimizas con confianza sobre una mentira. Checklist rápida: ¿dispara solo al pagar? ¿una vez por pedido? ¿manda el value real? ¿coincide el conteo con tus pedidos reales del día?

## Errores comunes — blacklist

1. **Optimizar por ViewContent o Page view creyendo que es "más datos".** Le enseñas al algoritmo a traer curiosos; nunca pagan.
2. **Quedarse en Add to cart para siempre.** Acumulas carritos abandonados; baja a Complete payment apenas tengas volumen.
3. **Optimizar por Complete payment sin volumen.** No juntas 50/sem → Learning Limited eterno (ver 13); sube el evento temporalmente.
4. **Cambiar el evento cada semana.** Cada cambio resetea el aprendizaje; cambia solo con evidencia de volumen.
5. **Pixel sucio que dispara el evento dos veces o en la página equivocada.** Optimizas sobre mentira; verifica en Events Manager (ver 57).
6. **Mezclar eventos distintos en el mismo ad group** o esperar que TikTok "promedie". Un ad group = un evento de optimización (ver 10).
7. **Para servicios, optimizar por Page view en vez de Lead.** Traes tráfico que mira y no deja datos; usa Lead (ver 54).
8. **Usar VBO/ROAS goal sin mandar el value al Pixel.** Optimiza por un valor que no recibe; trae basura (ver 15, 57).
9. **No verificar que el conteo de eventos cuadre con tus pedidos reales.** Si TikTok dice 40 compras y tú facturaste 22, o el Pixel infla o duplica — revisa antes de escalar (ver 16, 57).
