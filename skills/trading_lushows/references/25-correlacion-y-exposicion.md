# 25 — Correlación y exposición

**Correlación** = qué tanto se mueven juntos dos activos. Va de +1 (idénticos) a −1
(opuestos); 0 = independientes. **Exposición** = cuánto capital total está en riesgo sumando
todas las posiciones abiertas. Este módulo existe porque los límites "por trade" pueden
cumplirse todos mientras el riesgo TOTAL se sale de control por la puerta de atrás.

## BTC y ETH se mueven juntos

BTC y ETH mantienen históricamente una correlación alta (típicamente por encima de 0.7-0.8
en la mayoría de periodos; el valor exacto varía por ventana — verificar con datos actuales
antes de citar cifras). Cuando BTC cae fuerte, ETH casi siempre cae, y suele caer MÁS.
En pánico, la correlación de todo el mercado cripto tiende a 1: todo cae junto.

## 2 posiciones long ≈ 1 apuesta doble

La diversificación real exige activos que NO se mueven juntos. Con correlación alta:

| Escenario | Riesgo nominal | Riesgo efectivo |
|---|---|---|
| 1 posición BTC (1.5%) | 1.5% | ~1.5% |
| BTC + ETH long, correlación ~0 | 3.0% | menor que 3% (se compensan a veces) |
| BTC + ETH long, correlación alta | 3.0% | **≈ 3% — una sola apuesta doble** |

Con el bot en 2 posiciones (BTC + ETH, ambas long), no hay dos apuestas independientes de
1.5%: hay UNA apuesta de ~3% a "el mercado cripto sube". Si el mercado cae, es muy probable
que ambos stops se activen casi al tiempo — el peor día del sistema no es −1.5%, es −3%
(más slippage si la caída es violenta, módulo 27).

Esto no es un bug del diseño: es el costo asumido de operar solo cripto. Lo importante es
SABERLO y dimensionar los límites con el riesgo efectivo, no el nominal.

## Reglas de exposición agregada

1. **Presupuesto de riesgo total**: la suma del riesgo de todas las posiciones abiertas tiene
   un techo (la spec del proyecto dice ≤6%; con máx 2 posiciones de 1.5% el bot queda en 3%,
   holgado).
2. **Contar correlacionados como uno**: para efectos de "cuántas apuestas tengo", BTC+ETH
   long = 1 apuesta. Añadir un tercer par cripto long NO diversificaría — solo engordaría la
   misma apuesta.
3. **El drawdown se estima con el riesgo efectivo**: si el peor día realista es −3%, cinco
   días malos seguidos son −14%, rozando el límite go-live de 15%. Escenarios exactos →
   `Matematicas_lushows`.

## Diversificación honesta (y sus límites aquí)

Diversificar de verdad exigiría activos de otra familia (acciones, oro, bonos) o dirección
contraria (shorts). El bot es solo-long y solo-cripto por diseño y simplicidad — decisión
razonable para validar, siempre que los límites reconozcan que la diversificación es ~cero.

## Cómo aplica al AGENTE TRADING

El límite de **máx 2 posiciones simultáneas** es en la práctica un límite de exposición:
cap efectivo de ~3% del capital apostado a una sola tesis ("cripto sube"). Con $1.000, el
peor escenario planeado de un día malo es ~−$30 más costos. Para el análisis de desempeño:
si ambas posiciones suelen abrirse y cerrarse juntas (revisar el log de trades), evaluar
tratar BTC+ETH como un solo slot de riesgo, o exigir que la segunda posición solo abra si
la primera ya movió su stop a breakeven. Cualquier cálculo de correlación real sobre el
historial del bot → `Matematicas_lushows`.
