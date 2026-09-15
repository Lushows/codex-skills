# 133 — Exchange flows: entradas y salidas de exchanges

> La teoría: si mucha gente **deposita** cripto en exchanges, es para venderla (presión bajista);
> si la **retira**, es para guardarla (presión alcista). Simple, intuitivo... y mucho más ruidoso
> de lo que parece.

## La lógica básica

| Flujo | Lectura clásica |
|---|---|
| **Inflow** (entra al exchange) | Alguien prepara una venta → presión de oferta |
| **Outflow** (sale del exchange) | Alguien guarda a largo plazo → menos oferta disponible |
| **Netflow** | La resta: positivo = domina la entrada, negativo = domina la salida |

**Whale alerts**: cuentas y servicios que anuncian "se movieron 5.000 BTC a Binance". Generan
titulares y pánico instantáneo en Twitter/X.

## Por qué esto es más ruido que señal (honestidad brutal)

1. **No sabes la intención**: un depósito gigante puede ser un exchange moviendo fondos entre sus
   propias billeteras, un custodio rebalanceando, o colateral para derivados — no una venta.
2. **El etiquetado es imperfecto**: identificar qué dirección pertenece a qué exchange es detective
   work con errores; los proveedores corrigen hacia atrás (mismo problema del módulo 132).
3. **El timing no existe**: aunque el depósito SÍ preceda una venta, puede ejecutarse en horas,
   días o nunca. No te dice cuándo.
4. **Estudios independientes** han encontrado que las whale alerts, por sí solas, tienen poco
   poder predictivo sobre el precio inmediato. El movimiento que "explican" muchas veces ya pasó.

## El uso sensato

- Como **confirmación de contexto** en extremos: outflows sostenidos durante semanas en un piso
  de mercado son un dato más en la balanza. Un tuit de whale alert, no.
- Nunca como gatillo: operar por una alerta de ballena es reaccionar a un titular sin contexto.

## Cómo aplica al AGENTE TRADING

- El bot **no consume exchange flows** y no está en el backlog prioritario. Con 10 trades de
  historia, la prioridad es validar el sistema base (backtesting), no añadir señales ruidosas.
- Si Luis ve una whale alert en redes y le dan ganas de intervenir manualmente: eso es exactamente
  el tipo de impulso que el bot existe para filtrar. La regla es no operar por titulares.
- Si algún día se integra, entraría como contexto de baja prioridad para el análisis de Claude,
  con la advertencia explícita de su ruido en el prompt.
