# 157 — Correlación de retornos

> Los cálculos de ejemplo se verifican ejecutándolos con `Matematicas_lushows`.

## Qué es la correlación

Un número entre −1 y +1 que mide si dos activos se mueven juntos:

| ρ (rho) | Lectura |
|---|---|
| +1 | Se mueven idéntico — tener ambos es tener uno, en grande |
| 0 | Independientes — diversificación real |
| −1 | Espejo — uno cubre al otro |

Se calcula sobre los **retornos** (variaciones porcentuales), no sobre los precios. Dos precios
que suben a la vez durante meses pueden dar correlaciones engañosas si se mide mal.

## BTC-ETH: casi el mismo caballo

La correlación de retornos diarios BTC-ETH históricamente vive en el rango **0.7-0.9**. En la
práctica: cuando BTC cae 5%, ETH rara vez se salva — normalmente cae igual o más (ETH suele tener
mayor beta: amplifica los movimientos de BTC).

Consecuencia directa: una posición en BTC y otra en ETH **no son dos apuestas, son ~1.8 apuestas
de la misma cosa**. El riesgo agregado real está mucho más cerca de "una posición doble" que de
"dos posiciones diversificadas".

## Cuánta diversificación real queda

La varianza de un portafolio de dos activos iguales con correlación ρ se reduce respecto a
concentrarlo todo en uno, pero poco cuando ρ es alta:

| Correlación | Reducción de volatilidad vs. todo en un activo |
|---|---|
| 0.0 | ~29% |
| 0.5 | ~13% |
| 0.8 | ~5% |
| 0.9 | ~3% |

(Verificar el caso concreto con `Matematicas_lushows`.) Con ρ ≈ 0.8, dividir entre BTC y ETH
apenas rasca el riesgo. Diversificar de verdad exigiría activos de otra clase — que un bot de
cripto spot no tiene.

## La correlación sube en crisis (la traición)

La correlación no es constante: **en pánicos, tiende a 1**. Cuando el mercado se desploma, todo
cripto cae junto — la diversificación desaparece exactamente el día que la necesitabas. Regla de
diseño: dimensionar el riesgo agregado asumiendo el escenario de crisis (ρ ≈ 1), no el promedio
de días tranquilos.

## Cómo aplica al AGENTE TRADING

- Las 2 posiciones máximas del bot (BTC + ETH) deben pensarse como **una sola apuesta de ~3% de
  riesgo** en el día malo, no como dos apuestas de 1.5% independientes. El VaR de diseño del
  módulo 155 ya asume esto (ambos stops saltan juntos).
- El bot es solo-LONG en dos activos correlacionados: en mercado bajista, su win rate cae en
  ambos pares a la vez. Los filtros de régimen (macroRegime) son la defensa principal, más que
  la "diversificación".
- Ejercicio pendiente útil: calcular la correlación BTC-ETH real con las velas 1h que el bot ya
  guarda en `data/` (ejecutar con `Matematicas_lushows`), y citarla con fecha — cambia con el tiempo.
