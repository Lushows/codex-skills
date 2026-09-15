# 63 — Slippage y spread a fondo

## Definiciones exactas

- **Spread**: diferencia entre el mejor precio de venta (ask) y el mejor de compra (bid).
  Se paga al cruzar el libro con una orden market. En BTC/USDT de Binance suele ser de
  centavos — bps de un solo dígito bajo (verificar al día).
- **Slippage**: diferencia entre el precio al que DECIDISTE operar y el precio al que
  realmente se LLENÓ la orden. Incluye el spread y añade: profundidad consumida, latencia
  (el precio se movió mientras tu orden viajaba) y volatilidad del momento.

Fórmula de medición real (la única que vale):

```
slippage = (precio_ejecutado − precio_de_decisión) / precio_de_decisión
(positivo = te costó plata; se mide en bps: 1 bp = 0.01%)
```

El "precio de decisión" es el precio que el bot vio cuando decidió entrar — no el de un
minuto después. Sin registrar ese precio, el slippage no se puede medir, solo suponer.

## Market vs limit en la práctica

| | Market | Limit |
|---|---|---|
| Paga spread | Sí, siempre | No (si actúa de maker) |
| Slippage | Sí, variable | Cero en precio |
| Riesgo real | Pagar de más | **No llenarse** y perder el movimiento |
| Comisión Binance | Taker (mayor) | Maker (menor) si descansa en el libro |

La trampa de las limit que nadie cuenta: sufren **selección adversa** — se llenan con gusto
cuando el precio va en tu contra, y te dejan por fuera justo cuando el trade era bueno.
"Ahorrar" el spread puede costar el trade entero.

## El modelo de 5 bps del bot: cuándo aguanta y cuándo se queda corto

El bot modela 0.05% (5 bps) de slippage por lado. Evaluación honesta:

- **Razonable / conservador**: órdenes chicas en BTC/ETH, horas líquidas (solape
  Europa-EE.UU.), mercado tranquilo. Ahí el slippage real puede ser de 1-3 bps.
- **Se queda corto**:
  - Minutos de pánico o noticia (FOMC, hackeo): el spread se abre 5-20x y la latencia pesa.
  - Madrugadas y fines de semana (libro delgado, ver `64`).
  - Stops que ejecutan en cascada: un stop-market en plena vela de pánico puede llenar
    20-50 bps más allá del nivel — y es exactamente cuando los stops ejecutan.

Conclusión: 5 bps es un buen **promedio** para paper, pero la distribución real tiene cola
gorda: muchos llenados casi perfectos y unos pocos horribles justo en los peores momentos.

## Cómo aplica al AGENTE TRADING

- En Fase 8, **medir en vez de suponer**: guardar por cada orden el precio de decisión, el
  precio medio de llenado y el spread del momento. Con 30-50 trades reales se sabrá si los
  5 bps eran justos — auditar el modelo con datos propios, no con fe.
- Presupuestar asimetría: entradas (elegidas en calma) cerca de 5 bps; **stops** (ejecutados
  en tormenta) merecen supuesto peor, 10-15 bps, para no maquillar el backtest.
- Si el slippage real medido rompe la matemática del `07` (win rate mínimo), la respuesta es
  operar menos y mejor — no "apretar" el modelo para que las cuentas den.
