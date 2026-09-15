# 125 — Salud y consultorios

El sector salud (consultorios, clínicas, IPS, profesionales independientes) tiene dos rasgos contables que lo hacen único en Colombia: muchos de sus servicios están **exentos o excluidos de IVA**, y buena parte de sus ingresos viene de **facturar a EPS** (las aseguradoras del sistema), que pagan tarde y a veces **glosan** (objetan) las facturas. Esto crea un reto enorme de **cartera** (cuentas por cobrar): facturaste, prestaste el servicio, pero el dinero puede demorar meses o no llegar completo. La contabilidad de salud vive de controlar esa cartera y de aplicar bien el IVA.

Términos clave: **glosa** es una objeción de la EPS a una factura (la rechaza o paga menos); **excluido** de IVA significa que no se cobra IVA y no se descuenta el IVA de las compras; **exento** significa tarifa 0% pero sí da derecho a descontar IVA.

## Cuentas típicas del sector

| Cuenta | Para qué sirve | Tipo |
|---|---|---|
| Cuentas por cobrar — EPS / aseguradoras | Servicios facturados sin pagar | Activo |
| Glosas en proceso | Facturas objetadas por la EPS | Activo (en disputa) |
| Provisión de cartera / deterioro | Estimación de lo que no se cobrará | Gasto |
| Ingreso por servicios de salud | Honorarios y servicios prestados | Ingreso |
| Ingresos recibidos por anticipado (capitación) | Pago fijo por afiliado por adelantado | Pasivo |

## IVA en salud: exento, excluido y gravado

Lo más delicado del sector. En Colombia, **los servicios médicos para la salud humana suelen estar excluidos de IVA**, pero hay servicios (estéticos, ciertos insumos, medicina prepagada) que **sí se gravan**. La regla:

| Situación | IVA |
|---|---|
| Servicio médico de salud humana | Generalmente excluido (sin IVA) |
| Cirugía/tratamiento estético sin fin terapéutico | Generalmente gravado |
| Insumos y medicamentos | Depende del bien (algunos excluidos/exentos) |

No inventes la clasificación de cada servicio: verifícala con la norma vigente. Si estás **excluido**, el IVA de tus compras es **mayor costo** (no lo descuentas).

## Glosas y cartera (lo que más duele)

- Cuando la EPS **glosa**, parte de la factura queda en disputa: no la des por perdida ni por cobrada; sepárala en "glosas en proceso".
- La cartera vieja exige **deterioro** (provisión): estimar cuánto realmente cobrarás (módulo 36). El cálculo se ejecuta con `Matematicas_lushows`.
- La **capitación** (pago fijo mensual por afiliado) es un ingreso por anticipado que se gana con el tiempo.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Una IPS factura $50.000.000 a una EPS. La EPS glosa $8.000.000 y paga $42.000.000.

| Cuenta | Débito | Crédito |
|---|---|---|
| Bancos | $42.000.000 | |
| Glosas en proceso | $8.000.000 | |
| Cuentas por cobrar — EPS | | $50.000.000 |

Débitos = créditos = $50.000.000. La glosa se resuelve después (se cobra o se castiga). Cifras inventadas; toda suma se verifica con `Matematicas_lushows`.

## Errores comunes

- **Cobrar IVA en servicios excluidos** o descontar IVA de compras estando excluido.
- **Dar por cobradas las facturas glosadas**: infla el activo y la utilidad.
- **No deteriorar la cartera vieja de EPS**: los estados financieros muestran plata que no entrará.
- **Confundir exento (0% con derecho a descuento) con excluido (sin IVA, sin descuento)**.
- **No conciliar lo facturado con lo efectivamente pagado** por cada EPS.

## Conexión con otros módulos

- Las **cuentas por cobrar** y su control en el módulo **33**.
- Las **provisiones y deterioro de cartera** en el **36**.
- El **IVA** (exento/excluido/gravado) en el **41**.
- Los **ingresos por anticipado / capitación** en el **37**.
- *Modelo de negocio del consultorio o IPS*: `economist_lushows`.
- Todo cálculo de deterioro y conciliación de cartera: `Matematicas_lushows`.

## Siguiente paso típico

Clasifica cada servicio que prestas como gravado, exento o excluido (con tu contador titulado). Monta un control de cartera por EPS con edades de cartera y un rubro aparte para glosas en proceso.
