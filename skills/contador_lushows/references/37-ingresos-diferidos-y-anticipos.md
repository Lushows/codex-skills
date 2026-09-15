# 37 — Ingresos diferidos y anticipos

A veces te pagan **antes** de entregar el producto o prestar el servicio. Un cliente te da un adelanto, o te paga la suscripción anual por adelantado, o reserva con un abono. En ese momento entró plata a tu cuenta, pero **todavía no te la has ganado**: aún no has cumplido. Por eso ese dinero **no es ingreso todavía**: es una **deuda** (le debes el producto/servicio al cliente). Esto se llama **ingreso diferido** o **anticipo de clientes**.

El principio detrás es el **devengo**: el ingreso se reconoce cuando lo *ganas* (cuando entregas), no cuando *cobras*. Confundir cobrar con ganar es uno de los errores que más infla la utilidad de forma falsa.

## Cobrar ≠ ganar (la regla de oro)

| Momento | ¿Es ingreso? | Qué es |
|---|---|---|
| Te pagan por adelantado | **No** | Un pasivo: anticipo / ingreso diferido |
| Entregas el producto o prestas el servicio | **Sí** | Ahí se reconoce el ingreso |

Mientras no entregues, ese dinero vive en una cuenta de **pasivo** (lo debes). A medida que cumples, se va trasladando a **ingreso**.

## El ciclo en dos asientos

**1) Cuando recibes el anticipo (cifras ILUSTRATIVAS / inventadas):** un cliente paga $1.200.000 por un servicio anual que apenas empieza.

| Cuenta | Débito | Crédito |
|---|---|---|
| Bancos | $1.200.000 | |
| Ingresos recibidos por anticipado (pasivo) | | $1.200.000 |

Débitos = créditos = $1.200.000. Todavía **no hay ingreso**, solo una obligación.

**2) A medida que cumples**, reconoces el ingreso ganado. Si el servicio es anual, cada mes ganas $1.200.000 / 12 = $100.000:

| Cuenta | Débito | Crédito |
|---|---|---|
| Ingresos recibidos por anticipado (pasivo) | $100.000 | |
| Ingresos por servicios | | $100.000 |

Débitos = créditos = $100.000. El pasivo baja $100.000 cada mes; al cabo de 12 meses queda en cero y todo se convirtió en ingreso. Cifras inventadas para ilustrar; el prorrateo exacto se verifica con `Matematicas_lushows`.

## Anticipos a proveedores (el caso espejo)

Cuando **tú** pagas por adelantado a un proveedor, es lo contrario: tienes un **activo** ("anticipo a proveedores"), porque te deben entregarte algo. Se cancela cuando recibes el bien o servicio.

## Errores comunes

- **Reconocer como ingreso el anticipo completo** al cobrarlo: infla la utilidad de un período que no la ganó.
- **No prorratear** los servicios de varios meses: se carga todo el ingreso a un solo mes.
- **Olvidar que es una deuda**: si no entregas, tienes que devolver esa plata.
- **Mezclar anticipos de clientes con ingresos normales** en la misma cuenta: imposible saber qué le debes a quién.
- **Calcular el prorrateo de cabeza** con meses fraccionados: produce centavos descuadrados.

## Conexión con otros módulos

- Es una aplicación directa del **devengo**, principio del método base (módulo **00**).
- El anticipo recibido es un **pasivo**, pariente de las cuentas por pagar (módulo **34**).
- El anticipo pagado a proveedor es un **activo** que se cruza con compras de inventario (módulo **30**).
- El ingreso reconocido alimenta el costo de ventas y el resultado (módulo **38**).
- El prorrateo exacto lo ejecuta **Matematicas_lushows**.

## Siguiente paso típico

Cuando cobres por adelantado, regístralo como pasivo, define el calendario de devengo (cuánto ganas cada mes) y programa el asiento mensual de traslado a ingreso hasta cumplir por completo.
