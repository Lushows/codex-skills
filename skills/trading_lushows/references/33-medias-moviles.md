# 33 — Medias móviles

Una **media móvil** es el promedio del precio de las últimas N velas, recalculado en cada vela.
Suaviza el ruido y muestra la dirección de fondo. Es el indicador más simple y, bien usado,
uno de los más útiles — no porque prediga, sino porque **describe** la tendencia sin drama.

## SMA vs EMA

| Tipo | Cómo promedia | Carácter |
|---|---|---|
| **SMA** (simple) | Todas las velas pesan igual | Más lenta, más estable, menos señales falsas |
| **EMA** (exponencial) | Las velas recientes pesan más | Reacciona antes, pero también se equivoca antes |

No hay una "mejor": es un trade-off velocidad vs estabilidad. El bot usa SMA 20 y 50, una
combinación clásica de swing: la 20 lee el pulso de ~3 semanas de horas, la 50 la tendencia de fondo.

## Cruces (golden cross / death cross)

- **Golden cross**: la media rápida cruza POR ENCIMA de la lenta (SMA20 > SMA50) → estructura alcista.
- **Death cross**: la rápida cruza por debajo → estructura bajista.
- Honestidad: el cruce llega **tarde por diseño** (promedia el pasado). Cuando cruza, buena parte
  del movimiento ya ocurrió. Sirve como **filtro de régimen** ("¿de qué lado estamos?"), no como
  gatillo de entrada. Y en mercado lateral, los cruces se multiplican y todos son falsos.

## La media como zona dinámica

En tendencia sana, el precio no se aleja para siempre de su media: sube, se estira, y **regresa
a la media** antes de seguir. Por eso la SMA20 funciona como soporte dinámico en trending-up:
el retroceso hacia ella es el punto de entrada natural (comprar el HL de `32`, no el HH).

## Distancia a la media: el filtro anti-FOMO

La **distancia porcentual** entre precio y SMA20 mide cuán "estirado" está el movimiento:

```
distancia = (precio - SMA20) / SMA20 × 100
```

- Precio pegado a la SMA20 en tendencia alcista → entrada con stop cerca y espacio por delante.
- Precio muy por encima → entrar es comprar el estirón: el retorno a la media juega en contra,
  el stop queda lejos del soporte real y el R:R se degrada.
- Es una banda elástica: cuanto más estirada, más probable el latigazo de vuelta. No dice CUÁNDO,
  pero sí que la asimetría ya no favorece al que entra.

## Cómo aplica al AGENTE TRADING

- El bot ya usa SMA 20/50: precio sobre ambas + SMA20>SMA50 = estructura alcista (`04`).
- La lección de julio (`10`) fue exactamente este filtro: las entradas a **>3% de la SMA20**
  perdieron 3/3. Regla derivada: distancia >3% → la convicción DEBE bajar, sin excepciones.
  Es un número de la propia experiencia del bot, no un umbral copiado de un libro.
- Implementación barata en JS: el cálculo de distancia es una resta y una división sobre datos
  que ya existen; pasársela a Claude como campo explícito evita que la estime "a ojo".
- Lo que NO haría falta: agregar más medias (9, 100, 200…). Más líneas = más relatos, no más edge.
