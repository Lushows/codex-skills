# 46 — Backtesting: metodología honesta

**Backtesting** = probar una estrategia contra datos históricos: "si hubiera operado con estas
reglas los últimos N meses, ¿qué habría pasado?". Es la herramienta más útil y la más fácil de
autoengañarse del trading sistemático. Un backtest mal hecho no es neutro: es peor que nada,
porque da confianza falsa para arriesgar dinero real.

## Las 3 condiciones de un backtest honesto

| Condición | Qué significa | Cómo se viola (sin darse cuenta) |
|---|---|---|
| **Datos limpios** | Velas reales, completas, del mismo timeframe que operas | Huecos en los datos, velas de otro exchange, timeframe distinto al del bot |
| **Costos incluidos** | Restar comisiones, spread y slippage de CADA trade | Simular entradas al precio exacto de cierre, sin fricción |
| **Sin mirar el futuro** | En cada vela, la decisión solo usa información disponible HASTA esa vela | Usar el cierre del día para decidir "en la mañana" (look-ahead bias) |

**Slippage** = la diferencia entre el precio que pediste y el que te dieron. **Look-ahead bias** =
la trampa de dejar que el simulador "vea" datos que en la vida real aún no existían.

## Por qué los costos cambian todo

Una estrategia con expectancy de +0.3% por trade parece rentable. Si cada trade cuesta 0.2%
entre comisión y slippage (ida y vuelta), el edge real es +0.1% — y con muestra chica eso es
indistinguible de cero. Regla: **si la estrategia solo gana sin costos, no gana.**
Cálculo exacto de expectancy con costos → rutear a `Matematicas_lushows`.

## Sesgos clásicos que matan backtests

- **Survivorship bias**: probar solo sobre activos que "sobrevivieron" (BTC/ETH hoy son grandes,
  pero en 2018 nadie sabía cuáles morirían). Menos grave en cripto mayor, letal en altcoins.
- **Look-ahead bias**: el más común. Cualquier indicador que use la vela actual completa antes
  de que cierre está mirando el futuro.
- **Cherry-picking de periodo**: probar solo en 2023-2024 (mercado alcista) y concluir que
  "comprar siempre funciona". Hay que incluir periodos laterales y bajistas.
- **Datos sintéticos o de otra fuente**: si el bot opera con velas de Binance, el backtest debe
  usar velas de Binance, no de otro proveedor con precios distintos.

## Qué haríamos con las velas guardadas del bot

El AGENTE TRADING guarda las velas 1h de BTC/ETH en JSON cada ciclo. Eso es un dataset real,
del mismo exchange y timeframe con que decide. Un backtest honesto sobre esas velas sería:

1. **Recorrer vela por vela** en orden cronológico, sin saltar ni retroceder.
2. En cada vela, calcular RSI/MACD/SMA **solo con las velas anteriores** (el mismo
   `technicalAnalysis.js` que usa el bot en vivo — misma lógica, cero divergencia).
3. Aplicar las reglas de entrada (LONG, convicción, filtros) y simular stop/target con los
   high/low de las velas siguientes: si el low toca el stop antes que el high toque el target,
   es pérdida (y ante duda en la misma vela, asumir lo peor: stop primero).
4. Restar costos por trade (comisión estimada del exchange + slippage conservador).
5. Reportar: número de trades, win rate, expectancy, profit factor, peor racha.

Limitación honesta: no podemos backtestear las capas de IA (régimen con Haiku, convicción con
Sonnet) sin pagar por re-analizar cada vela histórica. Lo que SÍ es backtesteable barato es la
parte JS: filtros técnicos, stops, targets, sizing. Ver `89` para evaluar la parte IA.

## Cómo aplica al AGENTE TRADING

- Con 10 trades de paper (PF 0.89) la muestra es demasiado chica para conclusiones — el backtest
  sobre las velas guardadas es la forma de multiplicar la muestra sin esperar meses.
- Prueba concreta pendiente: backtestear el filtro anti-FOMO (">3% sobre SMA20 baja convicción")
  contra el histórico y ver si habría evitado los 3 trades perdedores de julio.
- Regla de la casa: ningún cambio de reglas entra al bot sin, mínimo, pasarlo contra las velas
  guardadas. Y todo número del backtest se calcula en código → `Matematicas_lushows`.
