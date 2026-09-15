# 100 — Swing trading a fondo (la estrategia madre del bot)

> Swing trading = capturar "columpios" del precio que duran de días a semanas. Ni el scalping
> de segundos ni el hold de años: el punto medio. Es LO QUE HACE nuestro bot, elegido a
> propósito — este módulo explica por qué.

## Horizontes: dónde vive el swing

| Estilo | Duración típica de un trade | Velas que mira |
|---|---|---|
| Scalping | Segundos a minutos | 1m-5m |
| Day trading | Horas (cierra el mismo día) | 5m-15m |
| **Swing** | **Días a semanas** | **1h-4h-1d** |
| Position / hold | Meses a años | 1d-1sem |

## Las velas 1h-4h-1d (el trío del swing)

Una vela resume el precio en un período (apertura, cierre, máximo, mínimo). El swing usa tres
lupas a la vez:

- **1d (diaria)**: el contexto — ¿la tendencia grande es alcista, bajista o lateral?
- **4h**: la estructura — ¿dónde están los soportes/resistencias que importan esta semana?
- **1h**: el gatillo — el momento concreto de entrar. Es la vela de decisión de nuestro bot.

Decidir en 1h con contexto de 4h/1d filtra el ruido de los marcos chicos sin perder los
movimientos que duran días.

## Ventajas para retail (por qué es NUESTRO juego)

1. **Tiempo**: decisiones cada hora, no cada segundo. Compatible con tener vida y trabajo.
2. **Costos**: pocos trades = pocos fees y poco slippage acumulado. En scalping, los costos
   se comen edges enteros.
3. **Compatible con IA "lenta"**: una llamada a Claude tarda segundos y cuesta centavos. En
   marcos de 1h eso es instantáneo y barato; en scalping sería inviable. El swing es de los
   pocos estilos donde un LLM puede ser el cerebro sin perder la carrera de velocidad.
4. **No compite con los HFT**: los fondos de alta frecuencia dominan los milisegundos. En
   horizontes de días, el campo está más parejo.

## Desventajas (la parte honesta)

- **Overnight risk / riesgo de fin de semana**: la posición queda abierta mientras duermes.
  Cripto opera 24/7 y puede moverse 10% en una madrugada. Mitigación: stops SIEMPRE (en live,
  OCO en el exchange que no dependen de que el bot esté despierto).
- **Menos trades = muestra lenta**: juntar 30 trades toma meses (lo estamos viviendo: 10 trades
  en ~6 semanas). La evaluación estadística es lenta por diseño.
- **Paciencia obligatoria**: días sin señales son NORMALES. La tentación de "hacer algo" es
  el enemigo #1 del swing trader — humano o bot.
- **Sufre en mercados laterales picados**: los rangos estrechos generan señales que se stopean.

## Cómo aplica al AGENTE TRADING

- El bot ES un swing trader: velas 1h, BTC/ETH, solo LONG, riesgo 1.5%, R:R 1:2, y solo actúa
  con convicción ≥8 — pocos trades buenos en vez de muchos mediocres.
- La muestra lenta explica el estado actual del módulo 08 (10 trades en 6.5 semanas): no es
  un bug, es la naturaleza del estilo. La respuesta correcta es extender el plazo, no bajar
  el umbral de convicción para "generar muestra".
- Los stops OCO en el exchange (Fase 8) son la respuesta directa al overnight risk.
