# 147 — Paper trading como validación

## Qué es y qué papel juega

**Paper trading** = operar con dinero simulado sobre precios reales: el bot decide en serio, las
órdenes y el saldo son de mentira. Es la segunda etapa del ciclo del sistema (módulo 00:
paper → testnet → live chico → escalar) y su función es una sola: **aprender gratis**. Los
errores que en live cuestan plata, en paper cuestan una anotación en el registro.

El error clásico es tratar el paper como una película de trailer: creer que lo que muestra es
exactamente lo que se estrenará. El paper valida unas cosas y NO valida otras — confundirlas es
la fuente número uno de decepciones en el go-live.

## Qué SÍ valida el paper

| Qué | Por qué el paper sirve aquí |
|---|---|
| **La tubería (pipeline)** | Que velas → análisis → decisión → orden → registro funcione sin caerse, todos los días, con datos reales. Bugs, cuelgues, datos faltantes: todo eso sale a la luz gratis |
| **La disciplina del sistema** | Que las reglas se ejecuten SIEMPRE igual: riesgo 1.5%, stops donde el análisis los pide, sin trades impulsivos. Un bot indisciplinado en paper será indisciplinado en live |
| **La lógica de la estrategia** | Si el edge existe como idea: expectancy, PF, distribución de R sobre trades reales en tiempo real (no en backtest, donde es fácil hacer trampa sin querer) |
| **Los costos MODELADOS** | Que cada trade simulado descuente comisión y slippage estimados (módulo 07). Un paper sin costos es autoengaño con interfaz bonita |
| **El registro y la auditoría** | Que cada trade quede documentado con su razón, convicción y resultado — la materia prima del aprendizaje (pilar 4) |

## Qué NO valida el paper

- **Slippage real.** El paper asume que compras/vendes al precio de la vela. En live, tu orden
  compite en un libro de órdenes vivo: el fill llega peor, especialmente en velas rápidas —
  exactamente cuando los stops se ejecutan.
- **Fills parciales.** En live, una orden puede ejecutarse por partes o no completarse al precio
  esperado. El paper llena todo, siempre, al instante. (En pares tan líquidos como BTC/ETH con
  capital chico esto es menor, pero no es cero.)
- **Caídas de infraestructura en el peor momento.** API caída, rate limits, desconexiones
  durante un movimiento violento. El testnet (la siguiente etapa) prueba parte de esto; el
  paper, nada.
- **La psicología con dinero real.** La más importante. Ver −$40 reales no se siente como ver
  −$40 simulados. La tentación de "apagar el bot un ratito", saltarse un stop o subir el riesgo
  tras una racha buena solo aparece cuando duele. El paper no puede ensayar el dolor.

## La regla de lectura

Los números del paper son la **cota superior optimista** del sistema: lo mejor que puede dar en
condiciones amables. La pregunta de validación nunca es "¿el paper da PF 1.3?" sino "¿el paper da
PF suficiente para que, tras la degradación esperada en live (módulo 149), SIGA siendo > 1?".

## Cómo aplica al AGENTE TRADING

- El bot está exactamente en esta etapa: 10 trades de paper (todos ETH, PF 0.89). Lectura
  honesta: la tubería funciona (eso ya es un logro validado); el edge todavía no aparece — y
  con 10 trades tampoco hay muestra para condenarlo (módulo 00: el azar domina muestras chicas).
- Por eso el criterio de go-live exige ≥30 trades: no es burocracia, es el mínimo para que el PF
  signifique algo.
- El PF > 1.3 exigido ya incorpora esta lógica: es el colchón para que, tras la degradación
  paper→live, el sistema real siga siendo rentable. Un paper en 1.05 no pasa aunque sea > 1.
