# 35 — MACD a fondo

El **MACD** (Moving Average Convergence Divergence) mide el **momentum de la tendencia**:
si el impulso alcista o bajista está creciendo o apagándose. El bot usa la configuración
estándar (12, 26, 9).

## Las piezas (sin misterio)

| Componente | Qué es | Qué cuenta |
|---|---|---|
| **Línea MACD** | EMA(12) − EMA(26): la distancia entre una media rápida y una lenta | Positiva y subiendo = el impulso alcista se acelera |
| **Línea de señal** | EMA(9) de la línea MACD | Una versión suavizada de la anterior, para detectar giros |
| **Histograma** | MACD − señal | Las barras: crecen = el impulso gana fuerza; se encogen = se apaga |

Clave conceptual: el MACD **es un derivado de medias móviles**. No aporta información nueva
sobre el precio — reprocesa las mismas medias de `33` para hacer visible su aceleración.

## Las señales clásicas

- **Cruce alcista**: la línea MACD cruza por encima de la señal → el impulso giró al alza.
  Más significativo si ocurre por debajo de cero (giro desde zona bajista) que en pleno rally.
- **Cruce de la línea cero**: MACD pasa de negativo a positivo → la media rápida superó a la
  lenta; equivale al cruce de medias, con el mismo retraso.
- **Histograma**: la señal más temprana del set. Barras que dejan de crecer ANTES del cruce =
  aviso anticipado de que el impulso se agota (también el más ruidoso: anticipa más, falla más).
- **Divergencias**: precio hace máximo más alto, MACD hace máximo más bajo → mismo concepto y
  mismas precauciones que la divergencia de RSI (`34`).

## Los retrasos (la parte honesta)

- Todo el MACD está construido sobre promedios de promedios: **confirma tarde por diseño**.
  Cuando cruza, el giro ya lleva varias velas andando.
- En mercado lateral (`ranging`) es su peor escenario: cruces constantes, todos falsos. El MACD
  solo es confiable cuando HAY tendencia — que es justo lo que el régimen (`03`) determina antes.
- MACD y RSI suelen decir lo mismo (ambos derivan del mismo precio): que los dos "confirmen"
  no son dos evidencias independientes, es la misma evidencia contada dos veces (`45`, `47`).

## Cómo aplica al AGENTE TRADING

- Uso actual (`04`): cruce alcista + histograma creciendo = confirmación de trending-up. Correcto:
  el MACD trabaja como **confirmador de régimen**, no como gatillo de entrada.
- Lectura fina para el prompt: histograma alcista pero **encogiéndose** durante un rally =
  el impulso se apaga → mal momento para un LONG nuevo aunque todo se vea verde. Esa es la
  versión MACD de la lección FOMO de `10`.
- No pedirle al MACD timing de entrada en 1h: para eso están los niveles (`31`) y los
  retrocesos de estructura (`32`). El MACD dice "el viento sopla a favor", no "entra ya".
