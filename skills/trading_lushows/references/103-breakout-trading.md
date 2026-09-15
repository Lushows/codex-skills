# 103 — Breakout trading (rupturas)

> Un breakout es cuando el precio ROMPE un nivel que venía respetando (el techo de un rango,
> una resistencia). La apuesta: la ruptura libera un movimiento fuerte en esa dirección.
> El problema: la mayoría de las rupturas son falsas.

## La idea

Los mercados pasan mucho tiempo en rangos: el precio rebota entre un piso (soporte) y un techo
(resistencia). Dentro del rango se acumulan órdenes de ambos bandos. Cuando el precio rompe el
techo con fuerza, los vendedores atrapados cubren, los compradores que esperaban confirmación
entran, y eso puede alimentar un movimiento rápido. El breakout trader compra ESA ruptura.

Es pariente del trend following (módulo 101): de hecho, muchas entradas de tendencia SON
breakouts de estructura.

## El problema central: los falsos breakouts

La mayoría de las rupturas fallan: el precio asoma la cabeza sobre la resistencia, activa las
compras de los ansiosos… y se devuelve al rango, dejándolos atrapados. Se les llama "fakeouts"
o "barridas de liquidez": justo sobre los niveles obvios hay stops y órdenes que a los
jugadores grandes les conviene barrer.

Consecuencia matemática: comprar TODA ruptura sin filtro tiene win rate malo Y ganadores que
no compensan. El oficio del breakout está en filtrar, no en entrar.

## Los dos filtros clásicos

| Filtro | Qué es | Qué señala |
|---|---|---|
| **Volumen** | Cuánto se negoció durante la ruptura | Ruptura con volumen notablemente alto = participación real. Ruptura con volumen flojo = probable fakeout |
| **Retest** | Esperar a que el precio rompa, regrese al nivel roto, y lo respete como nuevo soporte | La confirmación más limpia: renuncias al primer tramo del movimiento a cambio de una entrada con stop cercano y lógico (bajo el nivel retesteado) |

El retest además regala la estructura perfecta para nuestro R:R 1:2: stop justo bajo el nivel,
target a dos veces esa distancia. Entrada, stop y target salen del MISMO nivel — no de números
inventados.

Tercera regla de oro: **contexto**. Un breakout a favor de la tendencia de 4h/1d tiene mucha
mejor tasa de éxito que uno contra ella. Ruptura alcista dentro de estructura alcista > ruptura
alcista en pleno mercado bajista.

## Errores típicos del breakout trader

- Comprar la vela de ruptura ya extendida (pagar el peor precio del día) — esto se cruza con
  la lección FOMO del módulo 104.
- Stop demasiado pegado al nivel: la volatilidad normal del retest lo caza antes del movimiento.
- Ver "rangos" en cada consolidación de 3 velas: un rango que vale la pena tiene días o semanas
  de construcción, no horas.

## Cómo aplica al AGENTE TRADING

- Las rupturas de estructura en 1h con contexto 4h/1d son uno de los setups naturales del bot
  (solo LONG: rupturas alcistas). La exigencia de convicción ≥8 debería encarnar estos filtros:
  volumen, contexto de tendencia, y preferencia por retest sobre persecución.
- El stop del setup breakout es de los más "honestos" que existen (bajo el nivel roto): si el
  precio vuelve bajo el nivel, la tesis MURIÓ y salir es correcto, no mala suerte.
- Anti-FOMO explícito: si la ruptura ya corrió sin nosotros, la respuesta es esperar el retest
  o dejarla ir. Perderse un movimiento cuesta $0 (módulo 104).
