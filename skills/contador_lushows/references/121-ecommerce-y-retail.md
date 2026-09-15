# 121 — E-commerce y retail

Vender por internet o en tienda parece simple ("entra plata, sale producto"), pero contablemente esconde trampas: el cliente paga con tarjeta y la **pasarela** se queda una comisión, devuelve productos, hay fletes, y el dinero llega a tu cuenta días después y **descontado**. Si registras como ingreso lo que ves en la pasarela, tus números quedan mal. La contabilidad de un e-commerce o retail debe seguir el rastro completo: venta bruta → comisiones → devoluciones → plata real que llega.

Un término clave: **pasarela de pago** es el intermediario (Wompi, Mercado Pago, PSE, tarjetas) que cobra al cliente por ti y te transfiere después, reteniendo su comisión.

## Cuentas típicas del sector

| Cuenta | Para qué sirve | Tipo |
|---|---|---|
| Inventario de mercancías | Productos para la venta | Activo |
| Ingreso por ventas | La venta bruta, antes de comisiones | Ingreso |
| Comisiones de pasarela / plataforma | Lo que se queda Wompi, MercadoLibre, etc. | Gasto |
| Devoluciones en ventas | Lo que el cliente devolvió | Menor ingreso |
| Cuentas por cobrar — pasarela | Plata vendida que aún no ha llegado | Activo |
| IVA generado por pagar | El IVA cobrado al cliente | Pasivo |

## El registro correcto de una venta online

La regla de oro: el **ingreso es la venta bruta**; la comisión de la pasarela es un **gasto separado**, no un menor ingreso. Así puedes ver cuánto te cuesta cobrar. La plata entra a "por cobrar de la pasarela" y se cruza cuando la transferencia llega al banco.

| Momento | Qué pasa |
|---|---|
| Venta | Reconoces ingreso bruto + IVA + cuenta por cobrar a la pasarela |
| Liquidación | La pasarela transfiere neto y cobra comisión |
| Devolución | Reviertes ingreso y, si aplica, reintegras inventario |

## IVA y particularidades

- La **venta en línea está gravada igual** que la presencial: el IVA depende del producto, no del canal.
- Si vendes a otra ciudad o departamento, ojo con el **ICA** (módulo 44): se causa donde se realiza la actividad.
- Las **devoluciones** reversan el ingreso y el IVA proporcional; deben quedar documentadas con nota crédito.
- Marketplaces (MercadoLibre, Amazon) a veces **retienen** y emiten certificados: esas retenciones son un anticipo de tus impuestos, no un gasto.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Venta online de $119.000 (producto $100.000 + IVA 19% $19.000). La pasarela cobra 3% sobre el total = $3.570 y transfiere $115.430.

| Cuenta | Débito | Crédito |
|---|---|---|
| Por cobrar — pasarela | $119.000 | |
| Ingreso por ventas | | $100.000 |
| IVA generado por pagar | | $19.000 |

Al recibir la transferencia: Bancos $115.430 (D), Comisiones $3.570 (D), Por cobrar pasarela $119.000 (C). Débitos = créditos. Cifras inventadas; toda suma se verifica con `Matematicas_lushows`.

## Errores comunes

- **Registrar como ingreso lo neto que llega al banco**: oculta la comisión y subestima las ventas.
- **No reintegrar inventario** en las devoluciones: el inventario contable no coincide con el físico.
- **Olvidar el ICA** por vender a otras ciudades.
- **No conciliar la pasarela**: cada liquidación debe cruzar con lo que entró al banco (módulo 35).
- **Tratar retenciones de marketplaces como gasto**: son anticipos de impuestos a tu favor.

## Conexión con otros módulos

- El **inventario** y su valuación están en el módulo **30**; el costo de ventas en el **38**.
- La **conciliación bancaria** (pasarela vs. banco) en el **35**.
- El **IVA** en el **41**; **ICA** y territoriales en el **44**.
- **Retención en la fuente** que te practican en el **43**.
- *Qué vender, a qué precio y márgenes objetivo*: `economist_lushows`.
- Toda suma de comisiones y márgenes: `Matematicas_lushows`.

## Siguiente paso típico

Mapea tu flujo: venta bruta → comisión → IVA → plata que llega. Concilia cada liquidación de la pasarela con el banco y revisa que el inventario físico cuadre con el contable tras las devoluciones.
