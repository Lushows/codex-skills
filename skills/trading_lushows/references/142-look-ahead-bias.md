# 142 — Look-ahead bias: usar el futuro sin darse cuenta

> El error más traicionero del backtesting: la simulación usa información que en ese momento
> **todavía no existía**. No se siente como trampa — se siente como un backtest buenísimo.
> Si un backtest da resultados espectaculares, sospechar de esto primero.

## Las formas en que se cuela

### 1. Decidir con la vela en curso
El clásico absoluto. La regla dice "comprar si el RSI de la vela cierra bajo 30", pero el código
evalúa la vela **que aún no ha cerrado**. En vivo, ese valor cambia hasta el cierre; en el
backtest ya está congelado y "adivinó". Regla: decidir con la vela N cerrada, **ejecutar al
precio de apertura de la vela N+1** (o peor).

### 2. Indicadores repintados (repainting)
Indicadores que **recalculan su pasado**: el zigzag, ciertos fractales, señales "confirmadas"
varias velas después. En el gráfico histórico se ven perfectos porque ya se redibujaron. En vivo,
la señal que ves hoy puede desaparecer mañana. Si un indicador marca pisos y techos con precisión
quirúrgica en el histórico, casi seguro repinta.

### 3. Datos revisados hacia atrás
Datos on-chain re-etiquetados (módulo 132), volúmenes corregidos, precios ajustados. El dato que
descargas HOY sobre 2023 no es el que se veía en 2023.

### 4. Normalizar con estadísticas del dataset completo
Sutil y letal: "compro cuando el precio está bajo su promedio histórico" calculado con TODO el
dataset — incluido el futuro. Cualquier promedio, máximo o percentil debe calcularse solo con
datos hasta la fecha simulada (ventana rodante).

### 5. Stop y target en la misma vela
La vela tocó el stop Y el target: ¿cuál fue primero? Con velas OHLC no se sabe. Asumir siempre
el target es look-ahead optimista. Regla honesta: **asumir que el stop se ejecutó primero**.

## Prueba del ácido

Pregunta para cada línea del backtest: *"¿este número existía y era conocible en ese milisegundo?"*
Si hay duda, la respuesta es no.

## Cómo aplica al AGENTE TRADING

- En vivo el bot ya es limpio: analiza cada 2h con velas cerradas de `candlesStore`. El riesgo
  está en el **backtest futuro**: el simulador debe replicar exactamente eso — señal con la vela
  cerrada, fill en la apertura siguiente, costos incluidos.
- RSI/MACD/SMA de `technicalAnalysis` no repintan (bien). Mantenerlo así: nada de indicadores
  "mágicos" que redibujan.
- En la simulación de stops/targets con velas 1h: aplicar la regla pesimista (stop primero) cuando
  ambos caben en la misma vela.
