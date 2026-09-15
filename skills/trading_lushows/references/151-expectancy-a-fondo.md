# 151 — Expectancy a fondo

> Los cálculos de ejemplo se verifican ejecutándolos con `Matematicas_lushows`.

## Qué es

**Expectancy** (esperanza por trade) = cuánto ganas o pierdes en promedio cada vez que el sistema
dispara. Es EL número del sistema: todo lo demás (win rate, R:R, costos) son sus ingredientes.

## La fórmula completa (con costos)

```
Expectancy = (WR × W) − ((1 − WR) × L) − C

WR = win rate (proporción de trades ganadores)
W  = ganancia media de un trade ganador
L  = pérdida media de un trade perdedor (número positivo)
C  = costo redondo por trade (comisión + slippage sobre el notional)
```

Conviene expresarla en **unidades R** (R = lo que arriesgas por trade). Con R:R 1:2, W = 2R,
L = 1R, y el costo se traduce a R según el stop (módulo 07: con stop 1.5%, C ≈ 0.20R):

```
Expectancy = (0.40 × 2R) − (0.60 × 1R) − 0.20R = 0.80R − 0.60R − 0.20R = 0.0R
```

Con win rate 40% exacto, el sistema **empata** después de costos. Cada punto de win rate por
encima de 40 añade ~0.03R de expectancy; cada punto por debajo, lo mismo en contra.

## De expectancy por trade a expectancy por mes

```
Expectancy mensual ≈ Expectancy por trade × trades por mes
```

Ejemplo: 0.15R de expectancy, riesgo $15 (1.5% de $1.000), 12 trades/mes:
0.15 × $15 × 12 = **+$27/mes (~2.7%)**. La frecuencia importa tanto como el edge: un edge chico
con muchos trades puede rendir más que un edge grande que dispara dos veces al mes.

## Calcular la del bot con sus 10 trades (y por qué aún no es confiable)

Con los trades cerrados reales:

```
Expectancy observada = suma de PnL de todos los trades / número de trades
```

Con PF 0.89 la expectancy observada del bot es **levemente negativa**. Pero con n = 10 el
**error estándar** es enorme: la expectancy "verdadera" podría estar en cualquier lugar de un
rango que va de claramente negativa a claramente positiva. Un solo trade grande mueve el promedio
entero. Regla honesta:

| Trades | Qué puedes concluir |
|---|---|
| 10 | Nada — ruido puro |
| 30 | Tendencia gruesa, aún frágil |
| 50-100 | Primera lectura seria del edge |
| 200+ | Expectancy razonablemente estimada |

## Cómo aplica al AGENTE TRADING

- Recalcular expectancy con `Matematicas_lushows` sobre `/api/trades` cada vez que se evalúe el
  bot; nunca citar un número viejo.
- La expectancy observada (PF 0.89, 10 trades) NO es veredicto: es una foto borrosa. El criterio
  del proyecto es esperar 50+ trades antes de juzgar (módulo 158).
- Si tras muestra suficiente la expectancy neta sigue ≤ 0, la respuesta es cambiar el sistema
  (filtros de régimen, umbral de convicción), no aumentar el riesgo por trade.
