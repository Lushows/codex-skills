# 40 — Bandas de Bollinger

Las **bandas de Bollinger** son tres líneas: una media móvil (típicamente SMA20) y dos bandas a
±2 desviaciones estándar del precio. La **desviación estándar** mide cuánto se dispersa el precio
alrededor de su promedio — así que las bandas se ensanchan cuando hay volatilidad y se aprietan
cuando el mercado se calma. Son, en esencia, la SMA20 de `33` con un "traje de volatilidad".

## Qué dicen (y qué no)

- Por construcción estadística, la mayoría del precio queda dentro de las bandas. Tocar una
  banda **no es señal de nada por sí solo** — es un evento normal y frecuente.
- Las bandas describen dos cosas: **dónde está el precio respecto a su rango reciente** (pegado
  a la banda superior = zona alta) y **cuánta volatilidad hay** (ancho de las bandas).

## El squeeze (su lectura más útil)

**Squeeze** = las bandas se aprietan hasta un ancho inusualmente bajo → la volatilidad se
comprimió → suele venir una expansión violenta.

- Es la misma compresión de volatilidad de `37` y `03`, hecha visible.
- Advertencia crucial: el squeeze anticipa QUE habrá movimiento, **no hacia dónde**. Apostar
  dirección por el squeeze es adivinar; lo honesto es esperar la ruptura (idealmente con
  volumen, `36`) y operar el seguimiento.

## Caminar la banda

En tendencia fuerte, el precio se pega a la banda superior y **avanza sobre ella** vela tras
vela ("walking the band"). Es la versión Bollinger de la trampa del RSI >70 (`34`): la zona
alta, en tendencia, es señal de fuerza — no de venta.

## Errores de uso (los clásicos)

| Error | Por qué duele |
|---|---|
| Vender el toque de banda superior "porque está caro" | En tendencia, el precio camina la banda y te deja abajo (o barre tu contra-trade) |
| Comprar el toque de banda inferior en desplome | El cuchillo que cae también camina la banda — la de abajo |
| Operar la dirección del squeeze antes de la ruptura | Es una moneda al aire con comisiones |
| Ajustar el período/desviación hasta que "encaje" con el pasado | Overfitting de manual (`47`) |

La regla que ordena todo: **en rango, los toques de banda tienden a revertir; en tendencia,
tienden a continuar**. Sin clasificar el régimen primero (`03`), las bandas dan señales opuestas
con la misma cara.

## Cómo aplica al AGENTE TRADING

- El bot no las usa, y hay un argumento sólido para NO agregarlas: ya tiene la SMA20 y ya mide
  volatilidad — las bandas son exactamente esas dos piezas combinadas. Añadirlas sería el
  indicador redundante de manual (`45`): otra línea que "confirma" lo que ya sabemos.
- Lo único que aportarían ya se puede tener más barato: la **distancia a la SMA20 normalizada
  por volatilidad** (el filtro anti-FOMO de `33` con unidades de `37`). Eso ES la posición
  dentro de las bandas, sin dibujarlas.
- Si algún día se agregan al dashboard, que sea como visualización para Luis (el squeeze se VE
  muy bien), no como señal nueva para el motor.
