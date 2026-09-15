# 187 — Simons y Renaissance: el techo del cuant (y por qué no intentamos imitarlo)

## Quién fue

Jim Simons (1938–2024) fue un matemático de primer nivel mundial (geometría diferencial,
la teoría Chern-Simons lleva su nombre; antes fue descifrador de códigos) que fundó
**Renaissance Technologies** (1982). Su fondo interno, **Medallion**, es considerado el mejor
historial de inversión jamás registrado: retornos anuales enormes sostenidos durante más de
tres décadas (se citan cifras del orden de ~66% brutos / ~39% netos anuales promedio, según el
libro *The Man Who Solved the Market* de Gregory Zuckerman, 2019 — la referencia estándar).
Medallion está cerrado a inversores externos desde hace décadas: la capacidad de la estrategia
es limitada y se la quedan los empleados.

## Qué hace Renaissance (a grandes rasgos, porque es secreto)

Trading **cuantitativo puro**: modelos estadísticos que detectan patrones diminutos y fugaces en
enormes cantidades de datos, ejecutados por máquinas en miles de posiciones simultáneas, con
horizontes cortos. Ninguna posición individual importa; lo que importa es tener una ventaja
estadística pequeña repetida millones de veces. Nada de opiniones macro, narrativas ni
convicción: señal, ejecución, siguiente.

## Por qué NO podemos imitarlo (honestidad total)

| Lo que Renaissance tiene | Lo que este proyecto tiene |
|---|---|
| Decenas de PhDs en matemáticas, física, estadística contratados por décadas | Luis + Claude |
| Décadas de datos limpios de todos los mercados, infraestructura propia | Velas públicas de Binance |
| Ejecución de latencia mínima, costos de transacción negociados | Un bot en Render con comisión retail 0.1% |
| Miles de señales simultáneas que diversifican el error | 2 pares correlacionados, swing 1h |
| Secreto industrial férreo (las señales mueren al conocerse) | — |

La trampa a evitar: creer que "con IA ya podemos hacer lo de Renaissance". No. Un LLM razonando
sobre velas de 1h no es un modelo estadístico sobre microestructura de mercado; son deportes
distintos. Los patrones que Medallion explota probablemente ni existen en la escala temporal y
de costos en la que opera el bot. Pretender ese juego con estas herramientas es la vía rápida a
sobreajustar ruido y perder con confianza matemática.

## Qué SÍ copiar de Simons

1. **Sistema sobre opinión.** En Renaissance, si el modelo dice X, se hace X — no hay "es que
   yo siento que...". El historial demostró que la disciplina sistemática le gana al juicio
   caliente. Eso es 100% copiable y el bot ya lo hace.
2. **Rigor de medición.** Todo se registra, todo se evalúa contra datos, ninguna creencia
   sobrevive sin evidencia. Copiable: el bot loguea cada decisión y se auto-evalúa semanalmente.
3. **Los costos importan tanto como las señales.** Renaissance obsesiona sobre comisiones y
   slippage porque devoran ventajas pequeñas. Copiable: el simulador del bot cobra comisión
   0.1% y slippage desde el día uno — nada de PnL de fantasía.
4. **Humildad estadística:** aceptar estar "apenas" por encima del azar y ganar por repetición
   y gestión, no por genialidad puntual.

## Cómo aplica al AGENTE TRADING

Simons marca el **techo** del enfoque cuantitativo y, con ello, delimita el nicho realista del
bot: no competimos en velocidad ni en estadística fina — competimos en **disciplina barata**:
reglas fijas, selección paciente (convicción ≥8), riesgo capado, medición honesta con costos
incluidos. Es el rigor de Renaissance aplicado a la escala de un retail: sistema sobre opinión,
datos sobre sensaciones, y cero pretensión de ser Medallion.
