# 22 — Stops: técnicas

**Stop loss** = el precio al que se cierra la posición aceptando la pérdida, definido ANTES
de entrar. No es opcional: sin stop no hay riesgo definido, y sin riesgo definido no hay
sizing (módulo 20), ni unidades de R, ni sistema — solo esperanza.

## Tipos de stop

| Tipo | Cómo funciona | Fortaleza | Debilidad |
|---|---|---|---|
| Fijo % | Siempre a X% de la entrada (ej. 2%) | Simple, predecible | Ignora el estado del mercado |
| ATR/volatilidad | A un múltiplo de lo que el precio se mueve normalmente | Respira con el mercado | Necesita calibrar el múltiplo |
| Estructura (swing low) | Bajo el último mínimo relevante del gráfico | Se invalida donde la idea muere | Subjetivo; a veces queda lejísimos |
| Tiempo | Cierra si en N horas/velas no pasó nada | Libera capital de trades muertos | No protege de caídas, complementa |

**ATR (Average True Range)** = el rango promedio que el precio recorre por vela; la medida
estándar de volatilidad. Un stop a "1.5× ATR" dice: "salgo si el precio se mueve en contra
más de 1.5 veces lo normal" — es decir, si el movimiento dejó de ser ruido.

Los tipos se combinan: volatilidad para la distancia + tiempo como respaldo es una pareja
sana. El stop de estructura brilla en manual; en un bot es más frágil (detectar "el swing
low relevante" en código es más difícil de lo que parece).

## Dónde NO poner el stop

1. **En niveles obvios**: números redondos ($100.000 en BTC), mínimos evidentes del gráfico,
   la línea que todo el mundo ve. Ahí se acumulan los stops de miles de traders y el precio
   suele barrerlos antes de girar. Colocarse un poco MÁS ALLÁ del nivel obvio.
2. **Demasiado ceñido**: un stop dentro del ruido normal (menos de ~1× la volatilidad) se
   activa por azar, no por estar equivocado. Y como muestra el módulo 07, los stops ceñidos
   pagan más costos relativos: doblemente caros.
3. **Demasiado lejos "para que no me saquen"**: la posición sale diminuta (sizing) y una
   pérdida se come semanas. Si el stop lógico queda lejísimos, el trade no era operable.
4. **Movido a mano hacia abajo**: correr el stop para "darle aire" convierte una pérdida de
   1R en una de 3R. El stop solo se mueve a favor, nunca en contra.

## El stop es un límite, no una garantía

El stop define la pérdida PLANEADA. En movimientos violentos el precio puede saltarse el
nivel y la salida ejecuta peor (slippage). Por eso la última defensa es el tamaño de la
posición, no el stop (módulo 27).

## Cómo aplica al AGENTE TRADING

El bot usa **stop por volatilidad: 1.5× la volatilidad medida, con mínimo de 1%** — nunca
dentro del ruido, y la distancia alimenta el sizing (riesgo constante de 1.5% = $15 con
$1.000). El mínimo de 1% evita stops ridículamente ceñidos en mercados dormidos. Mejora
candidata post-validación: añadir stop de tiempo (cerrar trades que no avanzan en N velas
de 1h) — con máx 2 posiciones, un trade zombi bloquea la mitad de la capacidad. Para el
go-live: los stops deben vivir EN el exchange (orden OCO), no solo en el watcher local
(módulo 02). Calibraciones del múltiplo → `Matematicas_lushows` con datos reales.
