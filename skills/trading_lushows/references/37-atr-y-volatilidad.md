# 37 — ATR y volatilidad

La **volatilidad** es cuánto se mueve el precio, sin importar hacia dónde. Es el dato que decide
el tamaño del stop: un stop más ceñido que el ruido normal del mercado no protege — dona.

## ATR formal vs la volatilidad proxy del bot

El **ATR** (Average True Range, rango verdadero promedio) es la medida estándar. Por cada vela
toma el **true range**: el mayor de tres valores —

```
1. high - low                      (el rango de la vela)
2. |high - cierre anterior|        (gap alcista respecto al cierre previo)
3. |low  - cierre anterior|        (gap bajista respecto al cierre previo)
```

— y lo promedia sobre N velas (típicamente 14). Los puntos 2 y 3 capturan huecos entre velas.

El bot usa un **proxy**: promedio de `(high - low) / close` de las últimas 20 velas (`04`).

| | ATR formal | Proxy del bot |
|---|---|---|
| Gaps entre velas | Los incluye | Los ignora |
| Unidad | Precio absoluto ($) | Porcentaje |
| En cripto 24/7 (casi sin gaps) | ≈ iguales | ≈ iguales |

Veredicto honesto: en BTC/ETH 1h, que cotizan sin cierres, **la diferencia práctica es pequeña**.
Migrar a ATR formal (la lib `technicalindicators` lo trae) es higiene, no un edge — está bien
como mejora de backlog (`11`), mal como prioridad.

## Stops por volatilidad (por qué el 1.5×)

- La lógica: el stop debe quedar **fuera del ruido normal**. Si la vela típica recorre 1%, un
  stop a 0.5% lo barre el vaivén de cualquier hora, sin que la tesis esté equivocada.
- Multiplicadores típicos en swing: 1.5×-3× el ATR/volatilidad. El bot usa **1.5× (mínimo 1%)**
  con target a 2× el stop (R:R 1:2) — coherente y automático: el stop respira con el mercado.
- El costo oculto: stop más ancho = menos trades barridos por ruido, PERO cada pérdida es mayor.
  Por eso stop por volatilidad y tamaño de posición van juntos: a más volatilidad, stop más
  ancho Y posición más pequeña, para que el riesgo en plata sea constante.

## Volatilidad como régimen

La volatilidad no es solo un número para el stop — es un estado del mercado:

- **Compresión** (velas cada vez más chicas durante días) → suele preceder una expansión
  violenta, de dirección desconocida. Mal momento para asumir que el rango seguirá.
- **Expansión** tras compresión → el movimiento que arranca suele tener seguimiento.
- Ya figura como señal de cambio de régimen en `03`; el clasificador la recibe como input.

## Cómo aplica al AGENTE TRADING

- El sistema actual (stop = 1.5× volatilidad, mínimo 1%, target 2× stop) es defendible y simple.
  No tocarlo por moda; solo si el paper trading muestra stops barridos sistemáticamente por ruido
  (→ subir multiplicador) o pérdidas siempre completas (→ revisar la señal, no el stop).
- Mejora útil y barata: pasar a Claude la volatilidad ACTUAL vs su promedio histórico
  ("¿estamos comprimidos o expandidos?") como contexto de régimen, no solo como insumo del stop.
