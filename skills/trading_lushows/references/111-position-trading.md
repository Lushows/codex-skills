# 111 — Position trading (posiciones de semanas/meses)

## Qué es

**Position trading** = mantener una posición durante semanas o meses, montado en una tendencia
grande. Es lo más lento del espectro de trading activo — un escalón antes de simplemente
"comprar y guardar" (holdear).

## El espectro completo

| Modalidad | Duración típica | Decisiones | Peso de los fees |
|---|---|---|---|
| Scalping | segundos-minutos | miles/día | Enorme (mata el edge) |
| Day trading | horas (cierra el día) | varias/día | Alto |
| **Swing** (el bot) | días a ~2 semanas | pocas/semana | Moderado |
| **Position** | semanas a meses | pocas/mes | Bajo |
| Hold | años | casi ninguna | Mínimo |

## Diferencias con el swing del bot

- **Timeframe de análisis**: el position trader mira velas diarias y semanales; el bot mira 1h.
- **Stop más lejos**: para aguantar semanas hay que tolerar retrocesos de 10-20% sin salirse.
  Eso obliga a posiciones más chicas para mantener el mismo riesgo por trade.
- **Menos trades**: 5-15 al año. Ventaja: menos fees, menos errores. Desventaja: la muestra
  estadística crece lentísimo — tardas años en saber si tienes edge (≥30 trades, ver `00`).
- **Paciencia distinta**: el enemigo del swing es entrar mal; el enemigo del position es
  **salirse bien de algo bueno demasiado pronto** (o aguantar algo muerto demasiado tiempo).

## Cuándo tendría sentido

El position trading brilla cuando el mercado entra en un **régimen largo y claro** —
un `trending-up` que dura meses (los mercados alcistas de cripto históricamente lo han hecho;
verificar al día si estamos en uno). Ahí, el swing paga peaje: cada salida y re-entrada
regala fees y pierde tramo de tendencia que el position trader captura entero.

Su debilidad es el espejo: en `ranging` o mercados picados, el position trader devuelve
meses de ganancia esperando "que vuelva la tendencia".

## Cómo aplica al AGENTE TRADING

- El bot es swing 1h y así debe seguir: su muestra de aprendizaje (10 trades) aún es chica,
  y el swing genera datos mucho más rápido que el position.
- **Idea de futuro, no de ahora**: si macroRegime confirma `trending-up` sostenido durante
  semanas con confianza alta, una evolución natural sería dejar correr los ganadores más
  tiempo (trailing stop en 4h/diario) en vez de tomar ganancia rápida — position trading
  "parcial" sin cambiar de sistema.
- Requisito previo: evidencia en paper de que los trades cerrados temprano habrían seguido
  subiendo. Eso lo responde el meta-análisis semanal, no la intuición.
