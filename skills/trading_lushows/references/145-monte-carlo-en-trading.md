# 145 — Monte Carlo en trading

## Qué es

Una **simulación Monte Carlo** consiste en tomar los trades que el sistema ya produjo y
"rebarajarlos" miles de veces en órdenes distintos, para ver qué habría pasado con ese MISMO edge
si la suerte hubiera repartido los resultados en otra secuencia. Responde la pregunta clave:

> "Con este mismo sistema, ¿qué tan mal puede ir sin que nada esté roto?"

## Por qué el orden importa tanto

El **drawdown** (la caída máxima desde un pico de capital) no depende solo de qué trades ganas y
pierdes, sino de EN QUÉ ORDEN llegan. Los mismos 30 trades (12 ganados, 18 perdidos) dan
resultados finales parecidos, pero drawdowns muy distintos según si las pérdidas vinieron
repartidas o en racha. Tu historia real es UNA sola barajada de las miles posibles — juzgar el
sistema (o calibrar el riesgo) solo con esa barajada es confundir tu suerte con tu destino.

## El procedimiento (ejecutar con `Matematicas_lushows`)

1. Tomar la lista de resultados por trade en unidades R (múltiplos del riesgo por trade) del
   registro real del bot.
2. Remuestrear: barajar el orden (o muestrear con reemplazo, *bootstrap*) 5.000-10.000 veces.
3. Para cada secuencia simulada, calcular la curva de capital y su drawdown máximo.
4. Mirar la DISTRIBUCIÓN de drawdowns: mediana, percentil 95, peor caso.

## Cómo se leen los resultados

| Pregunta | Dónde mirar |
|---|---|
| ¿Qué drawdown es "normal" para este edge? | Mediana de la distribución |
| ¿Qué debo poder aguantar sin apagar el bot? | Percentil 95 |
| ¿Mi límite de DD 15% es realista con este sizing? | ¿Qué % de simulaciones lo supera? |
| ¿Cuándo un drawdown real es señal de sistema roto? | Cuando excede lo que la simulación dice posible |

Uso práctico doble: **antes** de ir a live, calibra el riesgo por trade (si con 1.5% el percentil
95 de DD supera el límite de 15%, el sizing está grande para ese edge); **durante** el live, da
la línea entre "racha mala dentro de lo esperado" y "el edge se murió".

## Los límites (honestidad primero)

- Monte Carlo NO mejora el edge ni lo valida: si la expectancy es negativa, solo muestra las mil
  formas de perder. Es una lupa sobre el riesgo, no una fuente de ganancia.
- Asume que los trades son independientes entre sí. En cripto no es del todo cierto (las
  pérdidas se agrupan en regímenes malos), así que los drawdowns reales tienden a ser algo
  PEORES que los simulados. Leer los percentiles con ese margen.
- Con muestra chica (10 trades), la simulación hereda toda la incertidumbre de la muestra:
  sirve como ejercicio, no como conclusión.

## Cómo aplica al AGENTE TRADING

- Con los 10 trades actuales (PF 0.89) el Monte Carlo es prematuro como veredicto — pero al
  llegar a ~30 trades es parte del examen de go-live: además de PF > 1.3 y DD < 15% observado,
  preguntar qué dice la distribución simulada sobre el DD que VIENE.
- Los datos ya existen (registro de trades en R); la simulación es un script corto que se
  ejecuta y verifica con `Matematicas_lushows` — nunca a ojo.
- Regla operativa a futuro: definir por Monte Carlo el "drawdown de apagado" (percentil 95-99).
  Si el bot en live lo cruza, se detiene y se audita — sin negociar con la esperanza.
