# 04 — Análisis técnico (lo que usa el bot)

El técnico no predice: **describe** dónde está el precio respecto a su historia reciente y dónde
hay asimetría (stop cerca, target lejos). Se usa para timing y niveles, nunca solo.

## Indicadores del bot (technicalAnalysis.js — lib `technicalindicators`, cálculo en JS puro)

| Indicador | Qué mide | Lectura del bot |
|---|---|---|
| **RSI(14)** | Velocidad del movimiento (0-100) | >70 sobrecomprado (cuidado LONG tardío), <30 sobrevendido |
| **MACD(12,26,9)** | Momentum de tendencia | Cruce alcista + histograma creciendo = confirma trending-up |
| **SMA 20/50** | Tendencia de fondo | Precio sobre ambas y SMA20>SMA50 = estructura alcista |
| Soportes/resistencias | Niveles de memoria del mercado | Dónde poner stop (bajo soporte) y target (bajo resistencia) |

Los indicadores se calculan en JS (exactos, gratis) y se INTERPRETAN en el prompt de convicción
(Sonnet). Nunca al revés: Claude no calcula números, los lee.

## Stops y targets del sistema (engine.js)

```
stop  = 1.5 × volatilidad reciente (mínimo 1%)   ← respira con el mercado
target = 2 × stop                                 ← R:R fijo 1:2
```

Volatilidad = promedio del rango (high-low)/close de las últimas 20 velas. Un stop más ceñido
que la volatilidad es una donación: el ruido normal lo barre.

## Errores técnicos que ya nos costaron (ver `10`)

- **Entrar en precio extendido**: tras un rally de +4.5% intra-semana, las entradas sobre la zona
  alta fallaron 3/3. Regla derivada: si el precio está a >3% de la SMA20, la convicción debe bajar.
- **Clustering de entradas**: 3 entradas en un rango de $3.68 en horas = misma apuesta comprada
  3 veces, no 3 apuestas. La correlación entre posiciones abiertas importa.

## Lo que el bot NO usa todavía (candidatos, backlog `11`)

- Volumen (confirma o desmiente rupturas)
- Timeframe 4h como filtro del 1h (multi-timeframe)
- ATR formal en vez de la volatilidad proxy actual
- Distancia a SMA20 como filtro anti-FOMO (lección de julio)
