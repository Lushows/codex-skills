# 115 — Moneda extranjera (NIC 21 / Sección 30)

Si compras a un proveedor en dólares, cobras a un cliente en el exterior o tienes una cuenta en otra moneda, el peso colombiano fluctúa todos los días: lo que valía $4.000 por dólar hoy puede valer $4.100 mañana. La norma de **efectos de las variaciones en las tasas de cambio** te dice cómo registrar esas operaciones y qué hacer con las ganancias o pérdidas que aparecen solo por el movimiento de la tasa. En **NIIF plenas** es la **NIC 21**; en **NIIF para pymes**, la **Sección 30**.

La clave es tu **moneda funcional**: la moneda del entorno económico principal donde operas. Para casi toda empresa colombiana es el **peso (COP)**. Las operaciones en otra moneda se registran convirtiéndolas a tu moneda funcional.

Términos: **moneda funcional** = la de tu operación principal (normalmente COP). **Moneda de presentación** = en la que publicas tus estados (puede ser otra). **Diferencia en cambio** = ganancia o pérdida que surge solo por el cambio de la tasa entre dos fechas. **Partida monetaria** = derecho/obligación de recibir o pagar una cantidad fija de moneda (caja, cuentas por cobrar/pagar). **Partida no monetaria** = activos como inventario o maquinaria.

## Qué tasa uso y cuándo

| Momento | Tasa que aplico |
|---|---|
| Al registrar la operación inicial | Tasa de cambio del día de la transacción (TRM de ese día) |
| Al cierre — partidas monetarias (caja, CxC, CxP) | TRM de cierre; la diferencia va a resultados |
| Al cierre — partidas no monetarias a costo (inventario, PP&E) | Se quedan a la tasa histórica (no se reexpresan) |
| Al pagar/cobrar | Tasa del día del pago; diferencia final a resultados |

En Colombia, la tasa de referencia es la **TRM** publicada oficialmente. No inventes valores de TRM; usa la cifra oficial del día correspondiente.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

GastroLatam compra una herramienta de software a un proveedor de EE. UU. por **USD 1.000**, a crédito.
- Día de la compra: TRM supuesta $4.000 → registro $4.000.000.

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto/Activo software (51 o 16) | 4.000.000 | |
| Proveedores del exterior (2205) | | 4.000.000 |

- Al cierre del mes, aún no he pagado y la TRM subió a $4.100. La deuda (partida monetaria) ahora vale USD 1.000 × 4.100 = $4.100.000. Debo $100.000 más → **pérdida por diferencia en cambio**.

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto diferencia en cambio (5305) | 100.000 | |
| Proveedores del exterior (2205) | | 100.000 |

Si al pagar la TRM hubiera bajado, sería una **ganancia** (ingreso por diferencia en cambio, cuenta 4215). Toda multiplicación USD × TRM la verifica `Matematicas_lushows`.

## Errores comunes

- **Reexpresar el inventario o la maquinaria al cierre**: las partidas NO monetarias a costo se quedan a la tasa histórica.
- **Olvidar el ajuste de cierre** de las partidas monetarias en otra moneda: la deuda/cuenta por cobrar debe quedar a TRM de cierre.
- **Usar una TRM inventada o promedio cuando corresponde la del día**: usa la oficial de cada fecha.
- **Netear ganancias y pérdidas sin sustento**: cada diferencia debe quedar soportada con su TRM y fecha.

## Conexión con otros módulos

- **112 — NIIF 9**: una cuenta por cobrar/pagar en dólares es a la vez instrumento financiero y partida monetaria.
- **Matematicas_lushows**: multiplicación por TRM, diferencias entre fechas, conversión de estados.
- **20-29** (presentación): la diferencia en cambio aparece en el estado de resultados como ingreso/gasto financiero.
- **114 — Impuesto diferido**: el tratamiento fiscal de la diferencia en cambio puede diferir del contable.

## Siguiente paso típico

Identifica tus saldos en moneda extranjera (caja, cuentas por cobrar/pagar). Al cierre, pide a `Matematicas_lushows` reexpresarlos a la TRM oficial de cierre y registra la diferencia en cambio. Revisa el efecto fiscal en **114 — Impuesto diferido**.
