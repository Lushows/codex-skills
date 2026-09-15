# 165 — Logging y auditoría: poder reconstruir cualquier decisión

## Por qué un bot de trading necesita logs de verdad

Cuando el bot hace algo raro ("¿por qué compró ETH ayer a las 3am?"), la única forma de saberlo
es que haya quedado escrito **en el momento**, con todos los datos. La memoria del proceso se
pierde al reiniciar; los logs son la caja negra del avión.

## JSONL: el formato elegido

**JSONL** (JSON Lines) = un objeto JSON por línea de texto. Ejemplo:

```
{"ts":"2026-07-05T14:00:02Z","level":"info","event":"analysis.done","pair":"BTCUSDT","conviction":8,"action":"BUY"}
{"ts":"2026-07-05T14:00:03Z","level":"info","event":"order.filled","pair":"BTCUSDT","qty":0.0021,"price":61250.5}
```

| Frente a | Ventaja de JSONL |
|---|---|
| Texto libre ("Compré BTC!!") | Cada línea es parseable: se puede filtrar, contar, graficar |
| Un JSON gigante (array) | Se agrega con append (barato y seguro); un JSON grande habría que reescribirlo entero |
| Base de datos de logs | Cero infraestructura; `grep` y unas líneas de JS bastan a esta escala |

Reglas: timestamp ISO siempre, un campo `event` con nombre estable (`ws.reconnect`,
`order.filled`, `claude.retry`), nivel (`info`/`warn`/`error`), y contexto suficiente para
entender la línea **sin leer las de al lado**.

## Qué loguear por cada orden (el mínimo auditable)

1. **La entrada del análisis:** régimen detectado, indicadores clave, lecciones de memoria usadas.
2. **El request a Claude** (o su resumen) y la **respuesta cruda**: convicción, acción, reasoning.
   Sin esto, "¿por qué decidió eso?" no tiene respuesta.
3. **La decisión de sizing:** riesgo, notional, stop, target calculados.
4. **La ejecución:** precio de fill, comisión, slippage aplicado.
5. **El cierre:** motivo (stop / target / manual), PnL.

Costos y errores de la API de Claude también se loguean: son plata y son señales de salud.

## Caso real: el trade con convicción 0

Auditoría tipo con un trade sospechoso: apareció un trade cuyo registro decía convicción 0 —
imposible, el umbral de auto-ejecución es 8. El camino: buscar en el JSONL el `analysis.done`
de ese par y hora → mirar la respuesta cruda de Claude → comparar con lo que guardó el broker.
Ese tipo de rastreo distingue entre ① Claude respondió mal, ② el parser leyó mal el JSON, o
③ el broker guardó mal el dato. Sin la respuesta cruda logueada, las tres hipótesis serían
indistinguibles y el bug quedaría vivo. Moraleja: **loguear lo crudo, no solo lo interpretado.**

## Higiene

- **Rotación:** los JSONL crecen; rotar por día o por tamaño y podar los viejos (el disco de
  Render es finito). Mismo espíritu FIFO del módulo 162.
- **Nunca loguear secretos:** ni API keys ni el password del basic auth. Un log es lo primero
  que se copia/pega al pedir ayuda.
- **Log ≠ métrica:** el log cuenta la historia; las métricas (`/api/metrics`) la resumen.

## Cómo aplica al AGENTE TRADING

El logger JSONL del bot existe exactamente para esto: cada análisis, orden, retry de Claude y
reconexión de WS deja línea con contexto. Antes del go-live, la vara sube: si un trade con
dinero real no se puede reconstruir de punta a punta desde los logs, el logging está incompleto.
La prueba ácida: tomar un trade cualquiera de hace 2 semanas y reconstruir la película completa
solo con `data/` y los logs. Si algo falta, eso es lo próximo a loguear.
