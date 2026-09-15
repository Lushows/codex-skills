# 15 — Estrategias de puja

Lee este módulo cuando vas a elegir cómo pujar, cuando no sabes si poner tCPA o tROAS, o cuando alguien te dijo "ponle pujas manuales que controlas mejor". La estrategia de puja es **cómo** el algoritmo decide cuánto pagar en cada subasta (ver 01). En 2026 Smart Bidding es la norma; el bidding manual quedó para casos muy marginales. Lo que importa no es el nombre de la estrategia, sino **calibrar el target sobre tus números reales** y dejar que el algoritmo calibre sobre datos reales, no sobre tu deseo (ver 13).

## Las estrategias y cuándo cada una

| Estrategia | Qué le dices al algoritmo | Cuándo usarla |
|---|---|---|
| **Maximize conversions** | "Tráeme la mayor cantidad de conversiones gastando el presupuesto" | Campaña nueva con poca señal (<15 conv/mes); fase de arranque (ver 13) |
| **tCPA** (target CPA, hoy una opción de Maximize conversions) | "Tráeme conversiones a ~X de costo cada una" | Ya tienes ~15-30 conv/mes estables; quieres controlar el costo por venta/lead |
| **Maximize conversion value** | "Tráeme el mayor VALOR de ventas con el presupuesto" | E-commerce con tickets variables, sin target de rentabilidad fijo aún |
| **tROAS** (target ROAS, opción de Maximize value) | "Tráeme ventas a ~X de retorno por peso gastado" | E-commerce maduro con datos de valor; ROAS real conocido (ver 35) |
| **Maximize clicks** | "Tráeme el mayor número de clics" | Solo para arrancar tráfico/keywords nuevas; nunca como meta de venta |
| **Manual / Enhanced CPC** | Tú pones la puja base | Casi nunca en 2026. Nichos sin volumen donde Smart Bidding no calibra |

Nota 2026: tCPA y tROAS ya no son estrategias "separadas" en la interfaz — son **un target opcional dentro de Maximize conversions / Maximize conversion value**. El concepto es idéntico; solo cambió dónde lo configuras (en la misma estrategia, activas el campo "objetivo de CPA/ROAS").

**Decisión rápida:**
- ¿Producto de **precio único** (la calculadora a $10.000 COP)? → conteo: **Maximize conversions** → luego añade objetivo **tCPA**.
- ¿Tickets **variables** (e-commerce)? → valor: **Maximize conv. value** → luego añade objetivo **tROAS** (ver 14).
- ¿**Poca señal** (<15 conv/mes)? → empieza sin target y agrega objetivo cuando llegues a ~15-30 conv/mes.

## Maximize → target: la progresión correcta

No arranques con un target. La secuencia sana:

1. Lanza con **Maximize conversions** (o value), **sin** objetivo de CPA/ROAS. Deja correr ~2-4 semanas para juntar señal (ver 13).
2. Mira tu **CPA real** (o ROAS real) que produjo esa fase. Ese número es tu punto de partida, no una opinión.
3. Activa el **objetivo tCPA** poniéndolo **igual o muy cerca de ese CPA real**.
4. Ajusta en **escalones de ≤10-15%** cada ~2 semanas hacia tu objetivo de negocio (ver 74).

Activar el objetivo de CPA/ROAS por primera vez puede tocar el aprendizaje (ver 13), así que hazlo una vez, con intención, no a los tres días.

## Calibrar el target sobre datos REALES, no deseados

Este es el error que más mata cuentas. El target tCPA/tROAS **no es tu deseo, es tu realidad ajustada gradualmente.**

| Tu CPA real actual | tCPA que DEBES poner | tCPA que la gente pone (mal) |
|---|---|---|
| 25.000 COP | ~24.000-25.000 (luego bajas en escalones) | 12.000 "porque quiero pagar la mitad" |
| 60.000 COP (lead B2B) | ~58.000-60.000 | 30.000 "porque suena mejor" |

Si pones un tCPA muy por debajo del CPA real, el algoritmo concluye que **no puede ganar subastas a ese precio** y simplemente **deja de entregar**: tu campaña se apaga, el gasto cae a casi cero, y crees que "no funciona". Lo mismo al revés con tROAS: un tROAS demasiado alto (ej. exiges 800% cuando tu real es 300%) ahoga la entrega.

**Cómo bajar el CPA de verdad** (no es forzando el target): mejora Quality Score (ver 36), mejora la landing y la congruencia con el anuncio (ver 33, 48), afina keywords y negativos (ver 20, 22), mejora el ángulo del anuncio (ver 38) y limpia la señal de conversión (ver 14). El target **sigue** al CPA real; no lo empuja. Bajar el número en la interfaz sin mejorar el negocio detrás solo apaga la entrega.

## tROAS: pensar en retorno, no en costo

ROAS = valor de conversiones ÷ gasto. Un tROAS de 400% significa "por cada $1 que gasto quiero $4 de venta". Para que tROAS funcione necesitas **enviar el valor real** de cada venta al sistema (ver 05, 14). El break-even depende de tu margen:

| Margen del producto | ROAS de equilibrio (1 ÷ margen) | tROAS mínimo para ganar |
|---|---|---|
| 50% | 200% | >200% |
| 40% | 250% | >250% |
| 30% | 333% | >333% |
| 20% | 500% | >500% |

Si tu margen es 40%, un ROAS de 250% apenas empata; necesitas más para ganar dinero real. Calcula tu **ROAS de equilibrio con márgenes reales** (incluye costo de producto, envío, pasarela de pago, devoluciones) antes de poner cualquier target — la viabilidad/unit economics rutea a `economist_lushows`. Un tROAS que "se ve bonito" pero está por debajo del equilibrio te hace vender a pérdida con eficiencia.

## Presupuesto y puja interactúan

- Un **presupuesto muy chico** estrangula a Smart Bidding: no le da subastas suficientes para calibrar (ver 18). Regla práctica: **presupuesto diario ≥ 3x tu CPA objetivo**, para captar al menos ~1 conversión/día posible. Con tCPA 25.000 COP → mínimo ~75.000/día.
- **Shared budgets** (presupuestos compartidos) reparten gasto entre campañas similares; útiles para no microgestionar, pero ocultan qué campaña consume (ver 18). No metas marca y genérico en el mismo (ver 18).
- Subir presupuesto de golpe (>20-30%) puede tocar aprendizaje; sube en escalones (ver 74).

## Seasonality adjustments: ajustar sin romper el target

Para picos cortos y conocidos (día sin IVA, Black Friday, Amor y Amistad: ≤7 días) **no muevas el target a mano** — usa **seasonality adjustments** para avisarle al bidding que esperas más conversión y que puje agresivo desde el inicio del evento (ver 19). Mover el tCPA a mano para el pico resetea aprendizaje justo cuando necesitas estabilidad.

## Errores comunes — blacklist

- **Target = deseo**: pones tCPA/tROAS donde quieres llegar, no donde estás; el algoritmo deja de entregar (ver 13).
- **Arrancar con objetivo de CPA/ROAS** una campaña nueva sin señal: no calibra; empieza con Maximize sin target.
- **Cambiar el target cada pocos días** o moverlo de golpe ±40%: reseteas aprendizaje y desestabilizas (ver 13, 74).
- **Pujar manual "para controlar"** en 2026: pierdes contra Smart Bidding, que ve señales que tú no (ver 01).
- **tROAS sin enviar valor real** de las ventas: el algoritmo optimiza con valores ficticios (ver 14).
- **Ignorar el margen** al fijar tROAS: pones un ROAS que "se ve bien" pero pierde plata por margen bajo (rutea a `economist_lushows`).
- **Presupuesto diario menor a ~3x el CPA**: ahogas el aprendizaje y culpas a la estrategia (ver 18).
- **Mover el tCPA a mano para un pico** en vez de usar seasonality adjustment: reseteas aprendizaje en el peor momento (ver 19).
- **Maximize clicks como meta de venta**: traes clics baratos sin intención de compra; sube el CPA real (ver 64).
