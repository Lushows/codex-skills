# 153 — Varianza y rachas

> Los cálculos de ejemplo se verifican ejecutándolos con `Matematicas_lushows` (los de rachas en
> muchos trades requieren código o simulación — no hay fórmula cerrada simple; ejecutar exacto ahí).

## Qué es la varianza aquí

**Varianza** = cuánto se dispersan los resultados alrededor del promedio. Dos sistemas con la
misma expectancy pueden sentirse completamente distintos: uno gotea resultados parejos, el otro
alterna rachas brutales. Con win rate 40% (pierdes 6 de cada 10), la varianza se manifiesta como
**rachas de pérdidas largas y normales**.

## La pregunta correcta

No es "¿cuál es la probabilidad de 5 pérdidas seguidas?" sino "¿cuál es la probabilidad de que
**en algún momento** de mis próximos 100 trades aparezcan 5 (o 10) pérdidas seguidas?". Son
preguntas muy distintas: la segunda da números mucho más altos.

## Orden de magnitud (win rate 40%, 100 trades, independencia)

| Racha de pérdidas | Prob. en un punto dado (0.6^k) | Prob. de verla en 100 trades (orden de magnitud) |
|---|---|---|
| 5 seguidas | ≈ 7.8% | **Casi segura** (~99%+) |
| 7 seguidas | ≈ 2.8% | **Muy probable** (~85-95%) |
| 10 seguidas | ≈ 0.6% | **Plausible** (~35-45%) |

> Estos porcentajes de la tercera columna son orden de magnitud. Para el número exacto, ejecutar
> con `Matematicas_lushows` (recursión de rachas o simulación Monte Carlo de 100.000 corridas).

Lectura: con este win rate, **5-7 pérdidas seguidas no son señal de que el sistema se rompió** —
son matemática pura. Incluso 10 seguidas pueden pasarle a un sistema sano.

## Traducir rachas a drawdown

Con riesgo 1.5% por trade, una racha de 7 pérdidas ≈ −10% de drawdown solo por la racha (un poco
menos si el riesgo es sobre capital que va bajando). Por eso el criterio "drawdown < 15%" debe
convivir con la expectativa de rachas: un sistema con win rate 40% y riesgo 1.5% **tocará −10%**
en algún momento sin estar roto.

## Preparación para la varianza normal

1. **Calcular antes** la racha esperable (tabla de arriba) y escribirla. Cuando llegue, comparar
   contra lo escrito, no contra el estómago.
2. **Separar señal de ruido**: una racha dentro de lo esperable no justifica cambiar el sistema;
   cambiarlo en medio de la racha destruye la muestra.
3. **Circuit breakers mecánicos** (no emocionales): pausas automáticas tras N pérdidas, para
   cortar el caso en que la racha SÍ sea un cambio de régimen.

## Cómo aplica al AGENTE TRADING

- Con win rate ~40% y riesgo 1.5%, el bot verá casi con certeza rachas de 5+ pérdidas en sus
  primeros 100 trades. El drawdown actual de 1.84% es **tranquilidad engañosa**: aún no ha vivido
  su racha estadísticamente normal.
- El cooldown de 4h tras 3 pérdidas y el bloqueo de overtrading (>5 trades/24h) son los circuit
  breakers mecánicos del bot — están bien puestos.
- Antes de juzgar una racha del bot como "falla", ejecutar el cálculo exacto de probabilidad con
  `Matematicas_lushows` y compararla contra lo esperable.
