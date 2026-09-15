# 154 — Kelly matemático

> Los cálculos de ejemplo se verifican ejecutándolos con `Matematicas_lushows`.

## La pregunta que Kelly responde

Tienes una apuesta con ventaja. ¿Qué **fracción del capital** apostar en cada repetición para que
el capital crezca lo más rápido posible a largo plazo? Apostar poco desperdicia la ventaja;
apostar mucho garantiza la ruina aunque la ventaja sea real (una racha te saca del juego).

## Derivación intuitiva

El capital crece **multiplicándose**: tras un +50% y un −50% no quedas igual, quedas en 75%
(0.75 = 1.5 × 0.5). Kelly maximiza el crecimiento del **logaritmo** del capital — que es lo mismo
que maximizar la tasa de crecimiento compuesto. El resultado, para una apuesta que paga `b` a 1:

```
f* = p − q/b

p = probabilidad de ganar
q = 1 − p (probabilidad de perder)
b = cuánto ganas por unidad arriesgada (con R:R 1:2, b = 2)
```

Se lee: "apuesta tu ventaja, descontada por el pago".

## Kelly con R:R 1:2 y win rate 40%

```
f* = 0.40 − 0.60/2 = 0.40 − 0.30 = 0.10  →  Kelly completo = 10% del capital por trade
```

**Ojo con la trampa**: eso es SIN costos. Con costos, un win rate de 40% con R:R 1:2 tiene
expectancy ≈ 0 (módulo 151), y con edge cero **Kelly es cero** — no hay nada que apostar.
El 10% solo vale si el 40% es real DESPUÉS de costos. Verificar el caso concreto con
`Matematicas_lushows` antes de citar cifras.

## Por qué nadie usa Kelly completo

| Problema | Consecuencia |
|---|---|
| `p` y `b` son estimaciones, no verdades | Sobreestimar el edge → apostar de más → ruina. El error es asimétrico |
| Kelly completo implica drawdowns salvajes | Con f* = 10%, drawdowns de 50%+ son esperables |
| Retornos con colas gordas (módulo 152) | La fórmula asume la apuesta idealizada; la realidad pierde más de 1R a veces |

Por eso la práctica seria usa **fracción de Kelly**: medio Kelly conserva ~75% del crecimiento
con la mitad de la volatilidad; **un cuarto de Kelly** es lo habitual cuando el edge está estimado
con muestra chica. Con f* = 10%: medio Kelly = 5%, cuarto = 2.5% por trade.

## Cómo aplica al AGENTE TRADING

- El techo del bot es **1.5% de riesgo por trade** = 0.15 de Kelly (si el Kelly completo fuera
  10%). Es más conservador que un cuarto de Kelly — correcto, porque el edge del bot aún no está
  demostrado (10 trades, PF 0.89): cuando el edge estimado puede ser cero, dimensionar cerca de
  cero es lo racional.
- `positionSizing.js` implementa Kelly fraccional con cap 1.5% en JS puro (sin IA): el tamaño
  de la posición nunca depende del "entusiasmo" del modelo, solo de números.
- Si tras 50-100 trades el edge se confirma positivo, se puede recalcular Kelly con los números
  reales (ejecutar con `Matematicas_lushows`) y discutir subir la fracción — nunca antes.
