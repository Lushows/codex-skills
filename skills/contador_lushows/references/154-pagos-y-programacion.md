# 154 — Pagos y programación

**Programar los pagos** es decidir, con cabeza fría, **qué se paga, a quién y en qué fecha**, en vez de pagar lo que grite más fuerte. Es la otra cara de la cobranza (módulo **152**): si la cobranza acelera lo que entra, la programación de pagos ordena lo que sale para que el efectivo alcance y no te quedes en rojo. Bien hecho, además cuida la relación con los proveedores (un proveedor que confía en que le pagas a tiempo te da mejores condiciones).

## El ciclo de pago a proveedores

| Paso | Qué ocurre |
|---|---|
| 1. Recepción | Llega la factura del proveedor con su soporte |
| 2. Validación | Se verifica que lo facturado se recibió y al precio pactado |
| 3. Causación | Se registra la cuenta por pagar en libros (módulo **34**) |
| 4. Programación | Se le asigna fecha de pago según el plazo y la caja |
| 5. Pago | Se paga y se registra la salida (Bancos al crédito) |

Pagar **sin validar** primero es la puerta de entrada a pagos dobles, sobreprecios y hasta facturas falsas.

## Cómo priorizar cuando la caja está apretada

| Prioridad | Por qué |
|---|---|
| Nómina y seguridad social | Es obligación legal y humana; primero siempre |
| Impuestos con vencimiento | El no pago genera intereses y sanciones |
| Proveedores críticos | Sin ellos para el negocio |
| Servicios básicos | Luz, agua, internet, arriendo |
| Resto de proveedores | Negociar plazo si hace falta |

## Calendario de pagos

Un **calendario de pagos** es la lista de todo lo que hay que pagar con su fecha, conectada al flujo de caja (módulo **151**). Permite ver "esta semana salen $8.000.000" antes de que llegue el día y reaccionar.

## Descuento por pronto pago

El **descuento por pronto pago** es la rebaja que un proveedor te da por pagarle **antes** del plazo (ej. "2% si pagas en 10 días en vez de 30"). Puede ser muy rentable —un 2% por adelantar 20 días equivale a un rendimiento anual alto—, **pero solo si tienes la caja sin descuidar pagos prioritarios**. Si tomarlo te deja sin con qué pagar la nómina, no vale la pena. El cálculo de si conviene se ejecuta en `Matematicas_lushows`.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Un proveedor te factura $5.000.000 a 30 días y te ofrece 2% de descuento si pagas en 10 días (cifras inventadas). Si pagas pronto, pagas $4.900.000 y registras:

| Cuenta | Débito | Crédito |
|---|---|---|
| Proveedores | $5.000.000 | |
| Bancos | | $4.900.000 |
| Descuento financiero (ingreso) | | $100.000 |

Solo conviene si tu flujo de caja (**151**) aguanta adelantar el pago. Cifras inventadas; la rentabilidad del descuento se calcula con `Matematicas_lushows`.

## Errores comunes

- **Pagar al que más insiste** en vez de seguir prioridades y fechas.
- **Pagar sin validar** que se recibió lo facturado: pagos dobles y sobreprecios.
- **Tomar descuentos por pronto pago** sacrificando la nómina o los impuestos.
- **No tener calendario de pagos**: te enteras de un vencimiento grande el mismo día.
- **Atrasar impuestos** para pagar proveedores: las sanciones cuestan más que el plazo.

## Conexión con otros módulos

- El registro de lo que debes está en cuentas por pagar (**34**).
- Las salidas alimentan el flujo de caja proyectado (**151**); es el espejo de la cobranza (**152**).
- El pago se confirma luego en la conciliación (**35**, **153**).
- La conveniencia del descuento por pronto pago se calcula en `Matematicas_lushows`; la estrategia de proveedores en `economist_lushows`.

## Siguiente paso típico

Arma un calendario de pagos conectado al flujo de caja, valida cada factura antes de causarla, prioriza nómina e impuestos, y evalúa los descuentos por pronto pago con `Matematicas_lushows` antes de tomarlos.
