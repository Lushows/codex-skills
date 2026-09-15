# 110 — Scalping: por qué NO

## Qué es

**Scalping** = abrir y cerrar posiciones en segundos o minutos, buscando ganancias diminutas
(0.05%-0.3% por trade) muchas veces al día. El scalper no opina sobre el mercado: caza
micro-ineficiencias en el libro de órdenes (la lista de compradores y vendedores en cola).

Suena atractivo: "muchas ganancias pequeñas". La realidad es que es la modalidad de trading
**más competitiva y más cara** que existe.

## Por qué es incompatible con un LLM

| Requisito del scalping | Lo que tiene el bot |
|---|---|
| Decisión en **milisegundos** | Una llamada a Claude tarda **segundos** (a veces 10-30s con análisis) |
| Co-locación (servidor pegado al exchange) | Servidor en la nube, latencia de red normal |
| Datos tick-a-tick del libro de órdenes | Velas de 1 hora |
| Miles de decisiones por día | Un ciclo de análisis por hora |

Cuando el bot "vio" la oportunidad, ya pasó. Es como intentar cazar moscas con una carta:
para cuando llega, la mosca lleva rato en otra parte. Los que ganan en scalping son firmas de
**HFT** (high-frequency trading: trading de alta frecuencia con máquinas especializadas) que
invierten millones en infraestructura. Contra ellas, el retail es la presa, no el cazador.

## Por qué tampoco sirve para retail (aunque fuera rápido)

La matemática mata la idea antes que la latencia:

- **Fees**: si el exchange cobra 0.1% por entrar y 0.1% por salir, cada trade arranca **-0.2%**.
  Un scalp que busca +0.15% ya perdió antes de empezar.
- **Spread**: la diferencia entre el precio de compra y de venta. En movimientos diminutos,
  el spread se come otra tajada.
- **Slippage**: la orden se llena a peor precio del que viste. En segundos, cada punto cuenta.
- **Volumen de errores**: 50 trades/día = 50 oportunidades diarias de equivocarse. Un solo
  error de ejecución borra días de scalps ganadores.

```
Edge por trade (diminuto) − fees − spread − slippage = casi siempre negativo para retail
```

El scalping retail rentable existe, pero es rarísimo, agotador y frágil. No es humildad
falsa: es aritmética.

## La regla general

A menor timeframe (marco temporal), mayor peso de los costos y del ruido, y menor peso del
análisis. El swing en 1h vive en el punto donde el análisis todavía importa más que la latencia.

## Cómo aplica al AGENTE TRADING

- El bot opera **swing en velas de 1h**: decisiones que valen por horas o días, donde tardar
  30 segundos en pensar no cambia nada. Es el terreno natural de un LLM.
- Si algún día alguien propone "bajar a 5 minutos para más señales": más señales = más fees,
  más ruido y menos edge. La respuesta correcta es no.
- La ventaja del bot no es velocidad, es **disciplina + análisis de contexto**. Se compite
  donde esa ventaja aplica, no donde no.
