# 155 — Multimoneda y diferencia en cambio

Cuando tu negocio cobra o paga en una moneda distinta a la tuya (vendes a un cliente en dólares, le pagas a un proveedor en euros, tienes una cuenta en USD), aparece un fenómeno contable: el valor en pesos de esa operación **cambia con la tasa de cambio**. La **diferencia en cambio** es justamente la ganancia o pérdida que surge porque el dólar (o la moneda que sea) valía X cuando hiciste la operación y vale Y cuando la cobras o la registras al cierre. Es plata real que entra o sale de tu patrimonio sin que hayas vendido nada nuevo: por eso hay que registrarla bien.

Aquí vemos la **operación contable** de operar en varias monedas. El concepto NIIF de moneda funcional y conversión más amplio está en el módulo **115**; toda conversión numérica se ejecuta en `Matematicas_lushows`.

## Conceptos básicos

| Término | Qué significa |
|---|---|
| Moneda funcional | La moneda en que el negocio realmente opera (en Colombia, normalmente el peso) |
| Tasa de cambio | Cuántos pesos vale una unidad de la otra moneda en una fecha |
| Partida monetaria | Saldos en otra moneda que se cobrarán/pagarán (cuentas por cobrar, por pagar, efectivo en USD) |
| Diferencia en cambio | Ganancia o pérdida por el cambio de la tasa entre dos fechas |
| TRM (Colombia) | Tasa Representativa del Mercado, la tasa oficial diaria del dólar |

## Cuándo se registra la diferencia en cambio

1. **Al cierre del período**: se revalúan los saldos en otra moneda a la tasa de cierre. Si el dólar subió y tienes una cuenta por cobrar en USD, ganaste.
2. **Al momento del cobro o pago**: comparas la tasa de cuando nació la operación contra la tasa del día en que efectivamente entró o salió la plata.

La diferencia en cambio puede ser **ingreso** (ganancia) o **gasto** (pérdida). No inventes tasas ni la TRM de un día concreto: se consulta en la fuente oficial.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Le vendes a un cliente USD 1.000 cuando el dólar está a $4.000 (cifras y tasas inventadas). Registras la venta por $4.000.000. Cuando te paga, el dólar subió a $4.100, así que recibes $4.100.000:

| Cuenta | Débito | Crédito |
|---|---|---|
| Bancos | $4.100.000 | |
| Cuenta por cobrar (USD) | | $4.000.000 |
| Ingreso por diferencia en cambio | | $100.000 |

Ganaste $100.000 solo porque el dólar subió entre la venta y el cobro. Si hubiera bajado, sería una pérdida (gasto). Cifras y tasas inventadas; toda conversión se hace con `Matematicas_lushows` y la TRM real.

## Errores comunes

- **Registrar la operación en otra moneda y nunca revaluarla** al cierre: el saldo en pesos queda irreal.
- **Inventar la tasa de cambio**: la TRM se consulta en la fuente oficial del día correspondiente.
- **Confundir diferencia en cambio con una venta nueva**: es solo el efecto de la tasa.
- **Convertir de cabeza**: cualquier multiplicación por tasa va a `Matematicas_lushows`.
- **Mezclar la moneda funcional**: en Colombia los libros se llevan en pesos, no en dólares.

## Conexión con otros módulos

- El marco NIIF de moneda funcional y conversión está en el módulo **115**.
- Afecta cuentas por cobrar (**33**), por pagar (**34**) y el efectivo en bancos (**150**).
- Las cuentas en otra moneda se concilian en conciliaciones avanzadas (**153**).
- La diferencia en cambio aparece en el estado de resultados (**21**).
- Toda conversión y cálculo de tasa → `Matematicas_lushows`.

## Siguiente paso típico

Identifica tus saldos en otra moneda, consigue la tasa oficial (TRM) de cada fecha relevante, revalúalos al cierre y registra la diferencia en cambio como ingreso o gasto, verificando cada conversión con `Matematicas_lushows`.
