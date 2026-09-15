# 118 — Estrategias estacionales (y su fragilidad)

## Qué es la estacionalidad

**Estacionalidad** = patrones de precio ligados al calendario: ciertos meses, días de la
semana u horas que históricamente se comportan distinto. En acciones existen famosos
("sell in May", rally de fin de año); en cripto circulan sus versiones:

| Patrón que se repite en redes | La historia detrás |
|---|---|
| "Uptober" (octubre alcista) | Octubre ha sido bueno para BTC varios años — y malo otros |
| Septiembre débil | Promedio histórico negativo — con enorme dispersión |
| Fin de mes/trimestre | Rebalanceo de fondos: flujos mecánicos de compra/venta |
| Fines de semana ilíquidos | Menos volumen → movimientos más bruscos con menos plata |
| Ciclo de 4 años del halving | La narrativa estacional madre de cripto (ver `113`) |

## La honestidad estadística: por qué son patrones DÉBILES

1. **Muestra ridícula.** Cripto líquido tiene ~una década de historia: cada "octubre" son
   ~10 observaciones. Con 10 datos, un promedio no distingue patrón de casualidad. Lanza una
   moneda 10 veces: 7 caras no prueban que la moneda esté cargada.
2. **Minería de datos.** Con 12 meses × 7 días × 24 horas hay cientos de combinaciones;
   por puro azar, varias se verán "rentables" hacia atrás. Encontrar patrones en el pasado
   es fácil; que sigan existiendo hacia adelante es lo difícil.
3. **Los patrones publicados se degradan.** Si "octubre siempre sube" fuera confiable y
   conocido, la gente compraría en septiembre — adelantando y borrando el patrón. Los edges
   públicos se los come su propia fama.
4. **Un régimen aplasta cualquier estación.** El mejor "mes alcista" del calendario es
   irrelevante en un mercado bajista de verdad. El régimen (ver `03`) pesa 10 veces más.

Lo único estacional con mecánica real (no solo estadística) son los **flujos de rebalanceo**
de fin de mes/trimestre y la **iliquidez de fines de semana y festivos** — porque tienen
causa conocida, no solo correlación histórica.

## El uso correcto: contexto, no señal

La estacionalidad jamás debe ser razón para entrar a un trade. Su uso legítimo es de
segundo orden: saber que un fin de semana ilíquido puede exagerar movimientos, o que un
cierre de trimestre puede traer flujos raros, ayuda a interpretar velas extrañas sin
inventarles historias.

## Cómo aplica al AGENTE TRADING

- **Cero peso estacional en la convicción.** "Es octubre" no suma puntos; "es septiembre"
  no resta. El bot decide por régimen + técnico + memoria, que sí tienen muestra propia.
- Sensato como contexto de riesgo: en fines de semana y festivos de EE.UU., la liquidez cae
  — los movimientos mienten más y los stops sufren mechas. Vale como nota de precaución en
  el análisis, no como filtro duro (todavía: sin datos propios que lo justifiquen).
- Si el meta-análisis semanal algún día muestra un patrón horario real en los trades del
  bot (con muestra suficiente, ≥30), eso sería estacionalidad **propia y medida** — la única
  que valdría la pena codificar.
