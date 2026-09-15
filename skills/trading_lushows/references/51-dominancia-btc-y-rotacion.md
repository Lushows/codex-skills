# 51 — Dominancia BTC y rotación de capital

## Qué es la dominancia (BTC.D)

La **dominancia de Bitcoin** (ticker común: BTC.D) es el porcentaje que representa BTC del
valor total de todo el mercado cripto. Si todo cripto vale $100 y BTC vale $55, la dominancia
es 55%. No mide si BTC sube o baja — mide si BTC sube/baja **más rápido que el resto**.

| BTC.D | Lectura típica |
|---|---|
| Subiendo | El capital se refugia en BTC (o BTC lidera el rally) |
| Bajando con mercado alcista | El capital rota a ETH y altcoins ("alt season") |
| Bajando con mercado bajista | Todo cae, pero las alts caen menos (raro) o hay ruido |

El nivel actual de dominancia: **verificar al día** en TradingView o CoinMarketCap.

## La rotación clásica BTC → ETH → alts

El patrón que los traders describen (y que a veces ocurre y a veces no):

1. **BTC sube primero.** El dinero nuevo entra por la puerta grande: la moneda más líquida y confiable.
2. **Las ganancias rotan a ETH.** Quien ganó en BTC busca "lo siguiente"; ETH es la segunda parada natural.
3. **De ETH a las alts grandes, y de ahí a las pequeñas.** Cada escalón es más riesgoso e ilíquido.
4. **El final del ciclo:** cuando las monedas más basura suben 300% en una semana, suele ser
   la fase de euforia — el capital inteligente ya está saliendo.

Honestidad: esta secuencia es una **tendencia estadística difusa**, no un reloj. Hay ciclos
donde la "alt season" nunca llega y las alts solo sangran contra BTC.

## El par ETH/BTC como termómetro

Más útil que BTC.D para un bot BTC/ETH: el gráfico **ETH/BTC** (cuántos BTC vale un ETH).
- ETH/BTC subiendo → ETH es el caballo fuerte del momento.
- ETH/BTC bajando → BTC es el activo dominante; ETH pierde contra su hermano mayor.

## Cómo aplica al AGENTE TRADING

- El bot opera **solo BTC y ETH** — los dos primeros escalones de la rotación. Esto es
  deliberado: son los pares más líquidos y menos manipulables (ver `68`).
- Idea de mejora concreta (backlog): usar ETH/BTC para **elegir cuál de los dos operar**
  cuando ambos dan señal — favorecer al que lidera. Hoy el bot los evalúa por separado.
- Lo que NO debe hacer: agregar altcoins "porque están rotando". Cada escalón hacia abajo
  en la rotación multiplica slippage, mechas y manipulación — justo lo que el modelo de
  costos del bot (0.3% redondo, ver `07`) no contempla.
