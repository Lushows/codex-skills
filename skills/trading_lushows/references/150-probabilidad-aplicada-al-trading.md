# 150 — Probabilidad aplicada al trading

> Los cálculos de ejemplo de este módulo se verifican ejecutándolos con `Matematicas_lushows` — no confiar en aritmética mental.

## La idea central

Cada trade es una **apuesta con probabilidades**, no una predicción. Un buen sistema no acierta
siempre; tiene una ventaja (edge) que solo se ve al repetir la apuesta muchas veces. La probabilidad
es el lenguaje para razonar sobre eso sin engañarse.

## ¿Los trades son independientes?

Dos eventos son **independientes** si el resultado de uno no cambia la probabilidad del otro
(como dos lanzamientos de moneda). En trading la respuesta honesta es: **casi, pero no del todo**.

| Fuente de dependencia | Por qué rompe la independencia |
|---|---|
| Régimen de mercado | En tendencia bajista, varios trades LONG seguidos pierden juntos |
| Correlación BTC-ETH | Dos posiciones abiertas a la vez suelen ser casi la misma apuesta (módulo 157) |
| El propio trader/bot | Tras perder, cambiar el comportamiento (revenge trading) encadena resultados |

Para cálculos de rachas y simulaciones se suele **asumir independencia** como aproximación —
útil, pero recordando que la realidad agrupa las pérdidas más de lo que el modelo dice.

## Probabilidad de rachas (la intuición)

Con win rate 40%, la probabilidad de perder un trade es 60%. La probabilidad de perder `k`
seguidos (asumiendo independencia) es `0.6^k`:

| Racha de pérdidas | Probabilidad de que ocurra en un punto dado |
|---|---|
| 3 seguidas | 0.6³ = 21.6% |
| 5 seguidas | 0.6⁵ ≈ 7.8% |
| 8 seguidas | 0.6⁸ ≈ 1.7% |

Ojo: eso es "en un punto dado". En **muchos trades**, que la racha aparezca en algún momento es
mucho más probable (módulo 153 lo calcula bien). Un sistema sano **vivirá** rachas feas.

## Esperanza matemática (el número que decide todo)

La **esperanza** (o valor esperado) es lo que ganas en promedio por trade si repites la apuesta
infinitas veces:

```
E = (win rate × ganancia media) − (loss rate × pérdida media)
```

Ejemplo con R:R 1:2 y riesgo $15: E = 0.40 × $30 − 0.60 × $15 = **+$3 por trade** (antes de
costos; con costos ver módulo 151). Si E > 0 el sistema gana con el tiempo; si E < 0, **ninguna**
gestión de riesgo lo salva — solo retrasa la pérdida.

## Cómo aplica al AGENTE TRADING

- El bot opera con win rate observado ~40% y R:R 1:2 objetivo — con costos, eso es justo el
  **breakeven** (módulo 07). Su esperanza actual ronda cero; los 10 trades no bastan para saberlo.
- Los trades del bot NO son del todo independientes: analiza BTC y ETH (correlacionados) y solo
  va LONG, así que un mercado bajista encadena pérdidas.
- El cooldown de 4h tras 3 pérdidas seguidas es el reconocimiento práctico de esa dependencia.
