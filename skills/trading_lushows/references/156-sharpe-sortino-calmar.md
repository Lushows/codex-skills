# 156 — Sharpe, Sortino y Calmar

> Los cálculos de ejemplo se verifican ejecutándolos con `Matematicas_lushows`.

## Para qué sirven los tres

Miden lo mismo desde ángulos distintos: **¿cuánto retorno obtienes por unidad de riesgo?**
Un +20% anual con sustos de −40% no es lo mismo que un +20% tranquilo. Estos ratios ponen
ese "susto" en el denominador.

## Los tres, comparados

| Ratio | Fórmula (idea) | Qué castiga | Debilidad |
|---|---|---|---|
| **Sharpe** | (retorno − tasa libre de riesgo) / volatilidad total | TODA la variabilidad, subidas incluidas | Castiga las ganancias grandes como si fueran riesgo |
| **Sortino** | (retorno − tasa libre de riesgo) / volatilidad solo de las bajadas | Solo la variabilidad negativa | Necesita suficientes días malos para estimarse |
| **Calmar** | retorno anualizado / drawdown máximo | La peor caída vivida | Depende de UN evento (el peor); muy ruidoso con poco historial |

Interpretación gruesa del Sharpe anualizado: < 0 pierdes ajustado a riesgo; 0-1 mediocre;
1-2 bueno; > 2 sospechosamente bueno (revisar la medición antes de celebrarlo).

## Por qué Sortino es más justo para estrategias asimétricas

Una estrategia con R:R 1:2 **busca** que sus días buenos sean el doble de grandes que los malos.
El Sharpe castiga esos días buenos grandes (suben la volatilidad total); el Sortino no, porque
solo mira la volatilidad de las pérdidas. Para sistemas que cortan pérdidas y dejan correr
ganancias, el Sortino describe mejor la experiencia real. Regla: reportar ambos; si el Sortino
es claramente mayor que el Sharpe, la asimetría está funcionando como se diseñó.

## El Sharpe −0.27 actual del bot, leído honestamente

Tres verdades a la vez, sin elegir la cómoda:

1. **Es negativo**: hasta hoy, el bot ha rendido por debajo de no hacer nada, ajustado a riesgo.
   No se maquilla.
2. **Es estadísticamente vacío**: con ~10 trades y 44 días, el error de estimación de un Sharpe
   es enorme (se necesitan meses o años de datos para que el número se estabilice). Un −0.27
   con esta muestra es compatible tanto con un sistema perdedor como con uno ganador en mala
   racha.
3. **No es alarmante en magnitud**: −0.27 con drawdown 1.84% describe un sistema que pierde
   POQUITO mientras aprende — exactamente el comportamiento deseado en fase de laboratorio.

Conclusión: el número correcto que vigilar ahora no es el Sharpe sino el **tamaño de muestra**.

## Cómo aplica al AGENTE TRADING

- `/api/metrics` expone `sharpeRatio` y `maxDrawdown`; el Calmar se deriva de ambos y el Sortino
  se puede calcular desde `/api/equity` (ejecutar con `Matematicas_lushows`).
- Al reportar performance del bot: citar Sharpe Y Sortino Y el n de trades, siempre juntos.
  Un ratio sin su tamaño de muestra es marketing, no medición.
- Decisiones de sistema (cambiar umbral, riesgo, pares) no se toman por el Sharpe con n = 10;
  se toman con 50+ trades o con un cambio de diseño razonado.
