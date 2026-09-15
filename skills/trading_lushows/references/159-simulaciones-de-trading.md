# 159 — Simulaciones de trading (Monte Carlo)

> Las simulaciones de este módulo se **ejecutan** con `Matematicas_lushows` (código real, miles de
> corridas) — los números de ejemplo son ilustrativos hasta ejecutarlos.

## La idea: vivir 1.000 vidas en vez de una

Tu historial real es UNA sola secuencia de resultados — una tirada de dados entre las infinitas
posibles. **Monte Carlo** consiste en simular en código miles de "vidas" alternativas del mismo
sistema (mismo win rate, mismo R:R, mismos costos, mismo riesgo por trade) y ver la
**distribución** de destinos, no un solo destino.

## Receta (la que se ejecuta con Matematicas_lushows)

```
Para cada una de 1.000-100.000 vidas:
  capital = 1000
  repetir 100 trades:
    con prob. 40% → capital += 2R − costos ; si no → capital −= 1R + costos
    (R = 1.5% del capital, según la regla de sizing del sistema)
  guardar: capital final, drawdown máximo de la vida, racha máx. de pérdidas
Reportar percentiles 5 / 25 / 50 / 75 / 95 de cada métrica.
```

Decisión de diseño a explicitar: riesgo fijo en $ vs. % del capital corriente — cambia los
resultados y debe reflejar lo que el sistema hace de verdad.

## Qué revela que el promedio esconde

| Métrica | Qué aprendes |
|---|---|
| Distribución del capital final | El mismo edge produce vidas ganadoras Y perdedoras a 100 trades; ver cuántas de cada una |
| Drawdown máximo esperable (p95) | El número contra el cual fijar el umbral de pánico ANTES de vivirlo |
| Racha máxima de pérdidas (p95) | Complementa el módulo 153 con el caso exacto del sistema |
| Prob. de estar en negativo tras N trades | Cuánta paciencia exige el sistema aunque sea ganador |

Ejemplo de lectura honesta: un sistema con expectancy positiva puede mostrar 25-35% de vidas en
rojo tras 100 trades. Si eso sorprende, el problema era la expectativa, no el sistema.

## Variante más honesta: remuestrear los trades reales

En vez de asumir "40% / R:R 1:2" teóricos, cuando haya 30+ trades reales se puede **remuestrear
con reemplazo** los PnL reales del bot (bootstrap): reordena la historia vivida miles de veces.
Captura la distribución real de resultados (incluidos parciales y costos reales) sin asumir
ninguna forma teórica.

## Límites del método

- Asume trades independientes e idénticos — la realidad tiene regímenes y correlación (módulos
  150 y 157), así que los drawdowns reales tienden a ser algo peores que los simulados.
- No inventa edge: si los parámetros de entrada son ruido (10 trades), la simulación es ruido
  elegante. Basura entra, basura sale.

## Cómo aplica al AGENTE TRADING

- Uso inmediato: simular el sistema de diseño (WR 40%, R:R 1:2, costos 0.20R, riesgo 1.5%) para
  fijar los umbrales de drawdown y racha "normales" del bot ANTES de que ocurran — ejecutar con
  `Matematicas_lushows` y guardar los percentiles en un módulo con fecha.
- Cuando `/api/trades` acumule 30+ cerrados, pasar al bootstrap sobre PnL reales.
- Cualquier decisión de "subir el riesgo a X%" debe pasar primero por la simulación: ver el
  drawdown p95 que ese X implica y decidir si se puede convivir con él.
