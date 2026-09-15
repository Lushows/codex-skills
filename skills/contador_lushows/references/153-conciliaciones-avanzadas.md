# 153 — Conciliaciones avanzadas

Conciliar es comparar lo que dicen tus libros contra lo que dice un tercero (el banco, una pasarela de pagos) hasta que cuadre. La conciliación bancaria **básica** —una cuenta, pocos movimientos— está en el módulo **35**. Aquí subimos de nivel: **muchas cuentas, pasarelas de pago, partidas que llevan meses sin resolver y volúmenes grandes**. Es lo que separa una contabilidad "más o menos" de una **auditable de verdad**: si todo cuadra contra terceros independientes, tu efectivo es real y demostrable.

## Múltiples cuentas y bancos

Cuando el negocio tiene varias cuentas (operativa, de impuestos, de nómina, en distintos bancos), cada una se concilia **por separado** y luego se consolida. Errores típicos: traspasos entre cuentas propias que se registran como gasto/ingreso, o un movimiento anotado en la cuenta equivocada.

| Situación | Cómo manejarla |
|---|---|
| Traspaso entre cuentas propias | Es movimiento interno, no ingreso ni gasto |
| Movimiento en cuenta equivocada | Reclasificar a la cuenta correcta con soporte |
| Cuenta en otra moneda | Conciliar en la moneda y registrar diferencia en cambio (módulo **155**) |

## Pasarelas de pago

Una **pasarela de pago** (Wompi, Mercado Pago, PayU, Stripe, etc.) recibe la plata del cliente, le **descuenta su comisión** y te deposita el neto **días después**. Esto crea tres diferencias que hay que conciliar:

| Diferencia | Por qué ocurre |
|---|---|
| Comisión de la pasarela | Te depositan menos de lo que vendiste |
| Plata "en tránsito" | La venta de hoy se deposita en 2–3 días |
| Retenciones / impuestos | La pasarela puede retener antes de pagarte |

La regla: registras la **venta completa** como ingreso, la **comisión como gasto**, y una cuenta puente ("por cobrar a la pasarela") por lo que aún no te han depositado.

## Partidas conciliatorias antiguas

Una **partida antigua** es una diferencia que aparece mes tras mes sin resolverse (un cheque que nunca cobraron, un ajuste mal hecho hace seis meses). Son veneno para la auditabilidad. Hay que investigarlas con soporte y **darles de baja o registrarlas correctamente**, nunca arrastrarlas eternamente.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Vendes $1.000.000 por una pasarela que cobra $35.000 de comisión y deposita el neto en 2 días (cifras inventadas):

| Cuenta | Débito | Crédito |
|---|---|---|
| Cuenta por cobrar pasarela | $965.000 | |
| Gasto comisión pasarela | $35.000 | |
| Ingreso por ventas | | $1.000.000 |

Cuando depositan los $965.000, debitas Bancos y acreditas la cuenta por cobrar pasarela. Cifras inventadas; las sumas se verifican con `Matematicas_lushows`.

## Errores comunes

- **Registrar solo el neto depositado**: pierdes la comisión y el ingreso real queda subvalorado.
- **Tratar traspasos entre cuentas propias como ingreso/gasto**: infla resultados falsamente.
- **Arrastrar partidas antiguas año tras año**: nadie audita eso con confianza.
- **No usar cuenta puente para la pasarela**: la plata "en tránsito" desaparece de la vista.
- **Conciliar a ojo cuando hay miles de movimientos**: cruza por monto/fecha y deja evidencia.

## Conexión con otros módulos

- Es la versión avanzada de la conciliación bancaria básica (**35**).
- Las cuentas en otra moneda conectan con multimoneda y diferencia en cambio (**155**).
- Las partidas antiguas que se pierden pueden requerir provisión (**36**) o baja de activo.
- Alimenta la confianza del flujo de caja (**151**) y de los estados financieros (reportes 20-24).
- Cualquier suma, comisión o conversión → `Matematicas_lushows`.

## Siguiente paso típico

Concilia cada cuenta y cada pasarela por separado cada mes, monta una cuenta puente por pasarela, y arma un plan para limpiar las partidas antiguas una por una con soporte.
