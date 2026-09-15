# 134 — Ballenas y "smart money": por qué copiarlas suele salir mal

> **Ballena**: billetera o entidad con posiciones enormes. **Smart money**: el dinero
> supuestamente informado (fondos, market makers, insiders). La fantasía: "si copio lo que hacen
> los grandes, gano lo que ganan los grandes". La realidad es más incómoda.

## Cómo se les sigue

- **Wallets etiquetadas**: servicios que identifican billeteras de fondos, fundadores, tesorerías
  (Arkham, Nansen, etiquetas comunitarias). Verificar proveedores y precios al día.
- **Rastreo de movimientos**: ver cuándo una billetera famosa compra, vende o mueve a un exchange.
- **Copy trading**: plataformas que replican automáticamente las operaciones de otro trader.

## Por qué copiar ballenas suele salir mal: el contexto invisible

1. **No ves el portafolio completo**. La ballena que "compró" en la billetera A puede estar
   cubierta con un short en futuros desde una cuenta que no ves. Tú copias media posición.
2. **Horizontes distintos**: un fondo puede aguantar −40% durante dos años. Tu capital y tu
   estómago no. La misma entrada con distinta tolerancia es una estrategia distinta.
3. **Llegas tarde por diseño**: cuando el movimiento es visible on-chain, el precio ya reaccionó.
   Ejecutas peor que la ballena siempre.
4. **Las ballenas también pierden** — y mucho. Solo que sus pérdidas no salen en los hilos virales
   (sesgo de supervivencia, módulo 141).
5. **Juegos deliberados**: los grandes saben que los observan. Mover monedas a un exchange a la
   vista de todos puede ser teatro para provocar exactamente la reacción que van a aprovechar.

## Lo que sí sirve del concepto

La idea de fondo — "opera con los flujos grandes, no contra ellos" — es sana. Pero se captura
mejor con **régimen y tendencia** (precio y volumen agregados) que persiguiendo billeteras
individuales. El precio ya resume lo que hicieron todas las ballenas juntas.

## Cómo aplica al AGENTE TRADING

- El bot **no sigue billeteras** y no debería. Su forma de "respetar al dinero grande" es el
  análisis de régimen (macroRegime): no comprar contra una tendencia bajista clara.
- El skill `wisdomLibrary` incluye a traders como Druckenmiller precisamente por esto: la lección
  es *pensar* como los grandes (concentración cuando hay convicción, respeto al régimen), no
  *copiar* sus tickets.
- Si aparece la tentación de integrar "señales de ballenas" de algún servicio: pedir primero el
  track record verificable de la señal. Casi nunca existe.
