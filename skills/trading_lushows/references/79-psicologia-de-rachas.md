# 79 — Psicología de rachas

Las rachas (varias pérdidas o ganancias seguidas) son el punto donde la matemática y la psicología
chocan de frente: el cerebro ve PATRÓN y SEÑAL donde la estadística ve VARIANZA NORMAL. Quien no
entiende esto abandona sistemas sanos y se casa con sistemas enfermos.

## La matemática contra el pánico

Con un **win rate** (porcentaje de trades ganadores) del 40% — normal en sistemas de swing que
ganan porque sus ganadoras son más grandes que sus perdedoras — la probabilidad de perder varios
trades SEGUIDOS es alta:

| Racha perdedora | Probabilidad en un trade dado (win rate 40%) | En 100 trades, ¿es esperable verla? |
|---|---|---|
| 3 seguidas | 21.6% | Sí, varias veces |
| 5 seguidas | 7.8% | Sí, casi seguro alguna |
| 7 seguidas | 2.8% | Probable al menos una |
| 10 seguidas | 0.6% | Posible; en 500 trades, esperable |

Lectura correcta: **10 pérdidas seguidas PUEDEN pasar con un sistema perfectamente sano.** No es
evidencia de que "se rompió". Al revés también: 6 wins seguidas no prueban que "ya funciona" —
con 40% de win rate también ocurren por azar.

## La falacia del jugador (y su gemela)

- **Falacia del jugador**: "llevo 5 pérdidas, la próxima TIENE que ganar" → falso; cada trade es
  (aprox.) independiente. La moneda no tiene memoria.
- **Falacia de la mano caliente**: "llevo 5 wins, estoy ON FIRE, subo el tamaño" → mismo error al
  revés, y más caro (módulo 73).

Ambas nacen de la misma raíz: el cerebro humano no tolera la aleatoriedad y le inventa narrativa.

## Preparación mental: decidir ANTES de la racha

1. **Calcular las rachas esperables** de tu sistema (con win rate y número de trades) y escribirlas.
   Cuando lleguen, no son crisis: son la tabla cumpliéndose.
2. **Separar racha de régimen**: 5 pérdidas por varianza ≠ 5 pérdidas porque el mercado cambió de
   régimen y el sistema no aplica. La primera se aguanta; la segunda se detecta con datos (¿las
   pérdidas comparten patrón? ¿mismo tipo de entrada, mismo régimen?), no con angustia.
3. **Tamaño que sobreviva la racha**: con 1.5% de riesgo, 10 pérdidas seguidas ≈ −14% de drawdown.
   Doloroso, sobrevivible, recuperable. Con 10% de riesgo, la misma racha te deja a −65%: muerto.
   El sizing se elige para la peor racha esperable, no para la semana promedio.
4. **Juzgar por muestra, nunca por racha**: los veredictos sobre el sistema se emiten con cientos
   de trades o al detectar violaciones de protocolo — jamás por las últimas 5 operaciones.

## Cómo aplica al AGENTE TRADING

- El cooldown de 4h tras 3 pérdidas NO es porque la 4ª tenga peor probabilidad por sí misma (eso
  sería falacia del jugador): es porque 3 seguidas elevan la probabilidad de que el régimen sea
  hostil al sistema, y porque en live protegería al humano del revenge (módulo 72).
- El riesgo de 1.5% fijo está dimensionado para sobrevivir las rachas de la tabla con drawdowns
  tolerables.
- Para Luis: cuando el equity muestre 4-5 rojas seguidas, abrir ESTE módulo antes que el botón de
  stop. La pregunta no es "¿cuánto perdió?" sino "¿las pérdidas violaron alguna regla?" (módulo 77)
  y "¿comparten patrón?" (eso lo responde el meta-análisis, módulo 84 — como hizo con el FOMO 0/3).
