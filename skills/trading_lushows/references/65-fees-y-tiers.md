# 65 — Fees y tiers de Binance

## Cómo cobra Binance (estructura, no cifras eternas)

Binance cobra un porcentaje del valor de cada operación (el **notional**). La estructura:

| Concepto | Qué es |
|---|---|
| **Taker fee** | Comisión al ejecutar contra el libro (órdenes market). La más cara |
| **Maker fee** | Comisión cuando tu limit descansó en el libro y otro la ejecutó. Más barata |
| **Descuento BNB** | Pagar las comisiones con BNB (la moneda de Binance) da un descuento (~25% históricamente) |
| **Tiers VIP** | A más volumen mensual (y más BNB en cartera), menor comisión: VIP 0, 1, 2… |
| **Promos por par** | A veces hay pares con maker fee 0 u otras promociones temporales |

La tarifa base histórica del tier normal (VIP 0) ha sido **0.1% maker / 0.1% taker** — que
es justo lo que el bot modela. Pero cifras exactas, descuentos y promos: **verificar al día**
en binance.com/fees; cambian sin aviso y varían por país y producto.

Realismo de tiers: los VIP exigen volúmenes mensuales de millones de dólares. Un bot con
capital de laboratorio vivirá en VIP 0 durante toda su adolescencia — planear con 0.1%.

## Lo que las comisiones le hacen al sistema (la parte que duele)

De `07`: el peaje redondo del bot es ~0.30% del notional (0.2% comisión + 0.1% slippage).
Lo que eso significa en métricas:

- **Sube el win rate mínimo 3-7 puntos** según el stop (de 33.3% teórico a 36.7-40%).
- **Erosiona el profit factor**: un sistema con PF 1.4 bruto puede quedar en ~1.15-1.25
  neto. Las estrategias "marginalmente rentables" en backtest sin costos suelen ser
  perdedoras netas en vivo — las comisiones son el filtro que mata la mayoría de bots retail.
- **Castiga la sobreoperación**: 100 trades/mes pagan 100 peajes. El mismo edge en 10 trades
  buenos paga 10. La comisión es el impuesto a la impaciencia.

## Palancas reales para bajar el costo (por orden de sensatez)

1. **Operar menos y mejor** — la palanca más grande y gratis. Cada trade evitado ahorra 0.3%.
2. **Descuento BNB** — bajaría la comisión de 0.2% a ~0.15% redondo. Contras: hay que
   mantener saldo en BNB (un activo volátil más en la cuenta). Evaluar en Fase 8 con cifras
   del día.
3. **Entradas maker (post-only)** — ahorra la diferencia maker/taker, al costo del riesgo de
   no llenarse (`63`). Solo si los datos reales muestran que compensa.
4. Tiers VIP — no aplica a este tamaño; ignorar.

## Cómo aplica al AGENTE TRADING

- El modelo de 0.1% por lado ya refleja la tarifa base histórica de spot: el paper no se
  está mintiendo en comisiones (el punto débil es el slippage en pánico, ver `63`).
- Tarea puntual de la Fase 8: el día que se configure la cuenta real, **anotar la tarifa
  exacta vigente** (con/sin BNB) y actualizar la constante del bot y el módulo `07` si
  difiere. Números viejos en el código = PF de mentira.
- Métrica a vigilar en vivo: **comisiones pagadas / ganancia bruta**. Si el exchange se
  queda con más del 25-30% de lo que el sistema genera bruto, el sistema está sobreoperando.
