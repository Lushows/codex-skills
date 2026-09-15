# 47 — Overfitting y curve fitting: la trampa mortal

**Overfitting** (o *curve fitting*) = ajustar la estrategia al pasado hasta que "funciona".
Es tomar los datos históricos y torcer las reglas — un parámetro por aquí, una excepción por
allá — hasta que el backtest se ve hermoso. El problema: no encontraste un edge, **memorizaste
el ruido**. El pasado exacto no se repite; el patrón que solo existió una vez tampoco.

## Por qué es tan seductor

Cada ajuste MEJORA el backtest de verdad — eso es lo perverso. "RSI 14 no funciona, pero RSI 11
sí". "Perdíamos los martes, entonces no operamos martes". Cada regla nueva sube la curva
histórica y baja la probabilidad de que funcione mañana. El backtest overfitteado no miente
sobre el pasado; miente sobre el futuro.

## Señales de que estás overfitteando

| Señal | Qué delata |
|---|---|
| Parámetros "raros" (RSI 11, SMA 23, stop 1.37%) | Se eligieron porque ESE número ganó en ESE histórico |
| Muchas reglas para pocos trades | 8 condiciones filtrando 40 trades = una regla por cada 5 datos |
| Resultados frágiles | Cambias un parámetro de 14 a 15 y la estrategia pasa de ganar a perder |
| Excepciones con nombre propio | "No operar en marzo" porque marzo de un año fue malo |
| Solo funciona en un periodo | Brilla en 2024, muere en 2022 — memorizó un régimen, no un edge |
| El backtest es "demasiado bueno" | Win rate 80%+, curva sin caídas: el mercado real no da eso |

## La regla de oro: pocas variables, mucha muestra

Cada parámetro que la estrategia puede "elegir" es un grado de libertad — una oportunidad de
memorizar ruido. Heurística honesta: **mínimo 30 trades por cada parámetro ajustable**, y mejor
si son 50+. Con 10 trades no se ajusta nada: no hay muestra ni para un solo parámetro.

Los sistemas robustos comparten esto:
- Pocas reglas, cada una con una **razón económica** ("el precio extendido revierte porque los
  compradores tardíos se agotan"), no solo estadística ("el número 3 dio mejor que el 2").
- Parámetros redondos y poco sensibles: si funciona con SMA 20 pero no con SMA 19, no funciona.
- Ganan (aunque menos) en periodos y activos que NO se usaron para diseñarlas.

## Cómo protegerse

1. **Diseñar la regla ANTES de mirar el resultado** — hipótesis primero, datos después.
2. **Tocar pocos parámetros y pocas veces.** Cada iteración de "probar otro valor" gasta
   credibilidad estadística, aunque no se vea.
3. **Reservar datos que la regla nunca vio** para validarla (walk-forward → ver `48`).
4. **Desconfiar de las mejoras milagrosas**: si un cambio chico duplica el resultado, lo más
   probable es que memorizó algo, no que descubrió algo.

## Cómo aplica al AGENTE TRADING

- La regla anti-FOMO (">3% sobre SMA20") nació de una **lección con razón económica** (3/3
  entradas extendidas fallaron: compradores tardíos) — eso es aprendizaje, no curve fitting.
  Pero ojo: 3 trades es anécdota, no estadística. Se valida contra el histórico (ver `46`) y
  contra el paper futuro, no se declara ley.
- Tentación a vigilar: con solo 10 trades, cada pérdida "sugiere" una regla nueva. Si el bot
  acumula una regla por cada mala racha, en 6 meses será una colección de cicatrices
  overfitteadas. Las reglas entran por hipótesis + validación, no por dolor.
- Los parámetros actuales (RSI 14, SMA 20/50, riesgo 1.5%, R:R 1:2) son estándar y redondos —
  eso es una fortaleza. No optimizarlos contra 10 trades bajo ninguna circunstancia.
