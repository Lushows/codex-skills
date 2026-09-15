# 158 — Ley de grandes números en trading

> Los cálculos de ejemplo se verifican ejecutándolos con `Matematicas_lushows`.

## La ley, en una frase

Al repetir una apuesta muchas veces, el **promedio observado** se acerca al **promedio verdadero**
(la expectancy). Es la razón por la que un casino gana siempre a fin de mes aunque pierda manos
todo el día: su edge por mano es diminuto, pero juega millones de manos.

El trader es el casino solo si (a) tiene edge real y (b) juega suficientes manos. Sin muestra,
el edge es una hipótesis, no un hecho.

## La convergencia es LENTA

El error de estimación cae con la **raíz cuadrada** del número de trades, no linealmente:

| Trades | Precisión relativa del promedio observado |
|---|---|
| 10 | ±muy amplio — el ruido domina por completo |
| 40 | el doble de preciso que con 10 |
| 160 | el doble de preciso que con 40 |
| 1.000 | 10× más preciso que con 10 |

Para duplicar la confianza hay que **cuadruplicar** la muestra. Ejemplo concreto: con win rate
verdadero de 45%, en 10 trades es perfectamente normal observar entre 2 y 7 ganadores — es decir,
entre "20%, sistema basura" y "70%, sistema genial". El mismo sistema. (Verificar intervalos
exactos con `Matematicas_lushows`.)

## La trampa de juzgar por 10 trades

Con n = 10, cada resultado individual mueve el win rate observado 10 puntos. Errores típicos que
esa miopía produce:

1. **Matar un sistema ganador** porque arrancó con la racha mala que la matemática ya predecía
   (módulo 153).
2. **Confiar en un sistema perdedor** porque arrancó con suerte.
3. **Retocar parámetros tras cada racha** — cada retoque reinicia la muestra a cero, así que
   nunca se acumulan los trades que permitirían aprender algo. Es el error más caro y el más común.

Regla operativa: definir ANTES el tamaño de muestra de evaluación (50-100 trades) y el criterio
de decisión, y no tocar el sistema en el intermedio salvo bug evidente.

## Qué sí se puede evaluar con muestra chica

No todo requiere 100 trades. Con pocos datos ya se audita: ¿el bot respeta su riesgo máximo?
¿Los stops se ejecutan donde debían? ¿Los costos coinciden con lo modelado? ¿El proceso de
decisión (logs de análisis) es coherente? El **proceso** se audita desde el día 1; el
**resultado** solo con muestra.

## Cómo aplica al AGENTE TRADING

- El bot lleva ~10 trades: su win rate 40% y PF 0.89 son **ruido con cara de número**. La
  posición oficial del proyecto es no juzgar el edge antes de 50+ trades.
- 44 días de uptime con drawdown 1.84% sí dicen algo YA: el proceso funciona — riesgo respetado,
  persistencia estable, sin errores operativos. Eso es lo evaluable hoy.
- Mientras se acumula muestra, resistir la tentación de retocar `AUTO_EXECUTE_THRESHOLD` o el
  riesgo tras cada racha: cada retoque reinicia el experimento.
