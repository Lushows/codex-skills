# 126 — Servicios profesionales

Abogados, contadores, consultores, diseñadores, arquitectos, agencias: venden **tiempo y conocimiento**, no productos. Eso cambia la contabilidad. No hay inventario que costear; el "costo" principal es la **gente** (su propio tiempo y el de su equipo o contratistas). Su ingreso son **honorarios**, casi siempre sujetos a **retención en la fuente** (el cliente les descuenta un anticipo de impuesto al pagarles). Llevar bien las cuentas de un servicio profesional es entender que la rentabilidad se mide por **hora facturable** y que las retenciones son plata a favor, no perdida.

Término clave: **honorarios** son la remuneración por un servicio profesional o técnico; al pagarlos, quien los recibe suele sufrir **retención en la fuente** (un porcentaje retenido que se abona a su impuesto de renta).

## Cuentas típicas del sector

| Cuenta | Para qué sirve | Tipo |
|---|---|---|
| Ingreso por honorarios / servicios | Lo facturado por el servicio | Ingreso |
| Anticipo de retención en la fuente | Lo que el cliente retuvo (a favor) | Activo |
| Costos de servicios — personal/contratistas | El tiempo del equipo que prestó el servicio | Costo |
| Cuentas por cobrar — clientes | Servicios facturados sin pagar | Activo |
| Ingresos recibidos por anticipado | Honorarios cobrados antes de prestar | Pasivo |

## Honorarios, retención e IVA

- Al **emitir la factura**, reconoces el ingreso completo; la **retención** que te practican es un **activo** (anticipo de impuesto), no un menor ingreso ni un gasto.
- Si eres **persona natural**, la tarifa de retención sobre honorarios depende de si eres declarante y de los topes; no inventes el porcentaje, verifícalo.
- Los **servicios profesionales suelen estar gravados con IVA**, salvo excepciones. Quien presta servicios desde el **Régimen Simple** puede no cobrar IVA en ciertos casos (módulo 63): confírmalo.
- Tu **costo** es la mano de obra (la tuya, empleados o contratistas). Si subcontratas, eso es un costo del servicio, no un gasto general.

## Rentabilidad por hora (KPI del sector)

| Concepto | Significado |
|---|---|
| Tarifa por hora | Lo que cobras por hora de trabajo |
| Costo por hora | Lo que te cuesta esa hora (salario/honorario del que la trabaja) |
| Horas facturables | Las que efectivamente cobras vs. las trabajadas |
| Margen del servicio | Tarifa − costo por hora |

El cálculo de tarifa y margen por hora se ejecuta con `Matematicas_lushows`; *cuánto cobrar* es decisión de `economist_lushows`.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Una consultora factura honorarios por $5.000.000 + IVA 19%. El cliente le retiene el 11% sobre los honorarios = $550.000.

| Cuenta | Débito | Crédito |
|---|---|---|
| Bancos | $5.400.000 | |
| Anticipo retención en la fuente | $550.000 | |
| Ingreso por honorarios | | $5.000.000 |
| IVA generado por pagar | | $950.000 |

Débitos = créditos = $5.950.000. Cifras inventadas; toda suma y el % de retención se verifican con `Matematicas_lushows`.

## Errores comunes

- **Tratar la retención como gasto o menor ingreso**: es un anticipo a tu favor que descuentas en tu declaración de renta.
- **No facturar el IVA** del servicio cuando aplica.
- **No costear el tiempo propio**: si no te pagas tu hora, no sabes si el servicio es rentable.
- **Confundir contratista con empleado** (módulo 59): genera riesgo laboral y de UGPP.
- **Reconocer ingreso de un servicio cobrado por adelantado** antes de prestarlo.

## Conexión con otros módulos

- La **retención en la fuente** en el módulo **43**.
- El **IVA** de servicios en el **41**.
- **Contratista vs. empleado** en el **59**; nómina del equipo en el bloque **50**.
- Los **anticipos** cobrados en el **37**.
- *Pricing y tarifa por hora*: `economist_lushows`.
- Todo cálculo de margen, retención y horas: `Matematicas_lushows`.

## Siguiente paso típico

Registra el ingreso bruto y lleva las retenciones a una cuenta de anticipos a tu favor. Calcula tu costo por hora y tu margen por servicio para saber qué clientes y proyectos son realmente rentables.
