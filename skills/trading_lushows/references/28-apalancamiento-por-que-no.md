# 28 — Apalancamiento: por qué no

**Apalancamiento (leverage)** = operar con dinero prestado por el exchange para mover una
posición más grande que tu capital. "10x" significa: con $100 controlas $1.000. Las
ganancias se multiplican por 10 — y las pérdidas también. **Spot** = comprar el activo real
con tu propio dinero, sin préstamo. El bot opera spot. Este módulo explica por qué eso no
es timidez sino diseño.

## La liquidación: el stop que no eliges tú

Con apalancamiento, el exchange presta con una condición: si la pérdida se acerca al valor
de TU dinero (el margen), el exchange cierra la posición a la fuerza para cobrarse. Eso es
la **liquidación** — y suele costar además una comisión extra.

| Apalancamiento | Movimiento en contra que liquida (aprox.) |
|---|---|
| Spot (1x) | No existe liquidación — solo el stop propio |
| 5x | ~20% |
| 10x | ~10% |
| 25x | ~4% |
| 100x | ~1% |

Con 25x, un movimiento del 4% —ruido normal en cripto, menos que muchas velas diarias—
borra el 100% del margen. El apalancamiento alto convierte el ruido cotidiano en muerte
súbita. Y en las caídas violentas, las liquidaciones en cadena de miles de apalancados son
justamente lo que acelera el crash (módulo 27): el apalancado no solo sufre la cola, la
alimenta.

## Por qué para retail suele ser la ruta rápida a cero

Honesto y sin humo: la mayoría de traders retail con apalancamiento pierde su dinero, y
los datos de brokers regulados que publican sus cifras lo confirman consistentemente
(porcentajes exactos: verificar por broker y periodo). Las razones son estructurales, no
de inteligencia:

1. **El margen de error se encoge**: errores que en spot cuestan 1R, apalancados liquidan.
2. **Costos multiplicados**: comisiones y funding (el interés del préstamo, en futuros
   perpetuos) se pagan sobre el notional inflado. El peaje del módulo 07, por 10.
3. **Psicología imposible**: nadie decide bien viendo su cuenta oscilar ±30% en una hora.
4. **La asimetría de la ruina** (módulo 02) con esteroides: −50% exige +100%, y con leverage
   llegar a −50% toma horas, no meses.

Lo perverso: el apalancamiento se VENDE como "hacer más con poco capital" exactamente al
público con poco capital — el que menos margen de error tiene.

## ¿Cuándo (si acaso) reconsiderarlo?

Casi nunca. Las condiciones mínimas serían TODAS a la vez: sistema validado con cientos de
trades en vivo (no 10), leverage bajo (2-3x máximo, jamás 10x+), riesgo por trade calculado
igual que en spot (el leverage NO cambia el % arriesgado, solo el capital inmovilizado),
stops en el exchange, y entendimiento pleno del funding y la liquidación. Aun así, la
pregunta correcta no es "¿puedo usar leverage?" sino "¿mi edge es tan sólido que el capital
es mi único límite?" — y esa respuesta hoy es no.

## Cómo aplica al AGENTE TRADING

El bot opera **spot, sin apalancamiento, solo LONG**: no existe liquidación, el peor caso
por trade es el stop (más slippage), y el peor caso absoluto es el valor de lo comprado —
nunca más. Con PF 0.89 en paper (6-jul-2026), el sistema aún no demuestra edge NI en spot;
apalancar un sistema sin edge solo acelera la pérdida. Regla del proyecto: el leverage no
entra en la conversación hasta tener el go-live cumplido + meses de vivo rentable + capital
que se quede corto de verdad. Si algún día se evalúa, los escenarios de liquidación y
funding se calculan primero en `Matematicas_lushows` — nunca se aprende ese costo en vivo.
