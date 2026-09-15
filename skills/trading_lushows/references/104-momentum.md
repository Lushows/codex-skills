# 104 — Momentum (y la lección FOMO del bot)

> Momentum = lo que viene subiendo con fuerza tiende a seguir subiendo… por un tiempo. Es un
> efecto real y documentado. El arte no está en detectarlo — está en saber cuándo ya es
> demasiado tarde para subirse.

## La idea

En física, un objeto en movimiento tiende a seguir moviéndose. En mercados pasa algo parecido
por razones humanas: la subida atrae atención, la atención atrae compradores, los compradores
suben el precio, y el ciclo se alimenta. En cripto este efecto es especialmente violento:
narrativas, redes sociales y FOMO masivo amplifican los movimientos en ambas direcciones.

**Fuerza relativa**: comparar qué activo se mueve mejor que los demás (¿ETH está más fuerte
que BTC esta semana?) y favorecer al fuerte. **Continuación**: entrar en las pausas de un
movimiento fuerte (banderas, consolidaciones) esperando la siguiente pata — no en plena
vertical.

## Cuándo el momentum se agota (las señales de "ya es tarde")

| Señal | Qué indica |
|---|---|
| Extensión vertical | El precio lleva muchas velas seguidas subiendo sin pausa, lejos de toda media — el combustible (compradores nuevos) se acaba |
| Volumen clímax | Pico de volumen enorme tras larga subida: los últimos entran en masa; ¿quién queda por comprar? |
| Velas de agotamiento | Mechas largas arriba: se intentó seguir y fue rechazado |
| Euforia ambiente | Cuando "todo el mundo" habla de la subida, el que iba a comprar ya compró |

La trampa estructural del momentum: **la señal es más obvia cuanto más viejo es el movimiento.**
Al principio (donde está la ganancia) parece dudoso; al final (donde está el riesgo) parece
seguro. Comprar cuando "ya es obvio" es comprarle a los que entraron temprano y están saliendo.

## La lección FOMO del bot ES un fallo de momentum tardío

El bot ya cometió este error en paper: entrar a un movimiento YA extendido porque "se ve
fuerte" — convicción alta justo cuando la ganancia/riesgo era peor. Nombrémoslo con precisión:
no fue mala suerte, fue **momentum tardío** — confundir "esto subió mucho" (pasado) con "esto
va a seguir subiendo lo suficiente para pagar mi riesgo" (futuro).

El antídoto operativo, en orden:
1. **Medir la extensión antes de entrar**: ¿a qué distancia está el precio de su media/estructura
   en 1h-4h? Si la respuesta es "lejísimos", la convicción debe BAJAR, no subir.
2. **Preferir continuación a persecución**: entrar en la pausa/retroceso, no en la vela verde
   gigante.
3. **Recordar el costo real**: perderse un movimiento cuesta $0. Entrar tarde cuesta 1R.
   La asimetría es total y siempre favorece esperar.

## Cómo aplica al AGENTE TRADING

- El filtro anti-extensión es candidato #1 si el 22-ago toca PIVOT (módulo 08 lo menciona):
  atacaría directamente el fallo FOMO ya observado.
- El prompt del analista (Claude) debe tratar la extensión como argumento EN CONTRA de la
  convicción: "lleva 8 velas subiendo sin pausa" resta puntos, no suma.
- Momentum bien usado para nosotros = fuerza relativa (elegir el más fuerte entre BTC/ETH) +
  entradas de continuación con estructura (módulo 103), nunca compra de verticales.
