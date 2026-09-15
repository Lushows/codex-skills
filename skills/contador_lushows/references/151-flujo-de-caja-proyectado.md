# 151 — Flujo de caja proyectado

El **flujo de caja proyectado** es una tabla que anticipa cuánta plata va a **entrar** y a **salir** del negocio en los próximos días, semanas o meses, para saber con tiempo si vas a tener suficiente efectivo o si te va a faltar. No es el estado de flujos de efectivo contable (ese mira el pasado, módulo **22**): esto mira hacia **adelante** y es la herramienta más útil de la tesorería para no llevarse sorpresas.

La idea es simple: si proyectas que el 15 del mes te van a faltar $3.000.000 para la nómina, lo sabes hoy y puedes actuar (apurar un cobro, aplazar una compra, pedir un anticipo). Aquí enfocamos **cómo construir y controlar** la proyección; toda la **matemática** de proyectar (tasas de crecimiento, escenarios, valor presente) se ejecuta en `Matematicas_lushows`.

## Estructura básica

| Fila | Qué incluye |
|---|---|
| Saldo inicial | El efectivo con el que arrancas el período |
| (+) Entradas | Cobros a clientes, ventas de contado, préstamos recibidos, aportes |
| (−) Salidas | Pagos a proveedores, nómina, arriendo, impuestos, GMF, cuotas de crédito |
| (=) Flujo neto | Entradas menos salidas del período |
| Saldo final | Saldo inicial + flujo neto (es el inicial del siguiente período) |

El saldo final de una semana es el saldo inicial de la siguiente: así la proyección se "encadena".

## Semanal vs. mensual

| Horizonte | Cuándo usarlo |
|---|---|
| **Semanal (13 semanas)** | Negocios con caja apretada; permite reaccionar rápido |
| **Mensual** | Visión de mediano plazo; planear impuestos, inversiones, temporadas |

Lo común es llevar **ambos**: el semanal para sobrevivir, el mensual para planear.

## Realista, no optimista

Proyecta **cobros por la fecha real** en que suele entrar la plata (no por la fecha de la factura) y **pagos completos** incluyendo lo que se olvida: GMF, comisiones, impuestos, prestaciones. Una proyección optimista es peor que ninguna porque da falsa tranquilidad.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Proyección de 3 semanas (cifras inventadas):

| Concepto | Sem 1 | Sem 2 | Sem 3 |
|---|---|---|---|
| Saldo inicial | $4.000.000 | $5.500.000 | $1.500.000 |
| (+) Cobros | $6.000.000 | $2.000.000 | $7.000.000 |
| (−) Pagos | $4.500.000 | $6.000.000 | $3.000.000 |
| (=) Flujo neto | $1.500.000 | −$4.000.000 | $4.000.000 |
| **Saldo final** | $5.500.000 | $1.500.000 | $5.500.000 |

La semana 2 queda muy ajustada ($1.500.000): hoy puedes apurar un cobro o aplazar un pago para no quedar en rojo. Cifras inventadas para ilustrar; las sumas se verifican con `Matematicas_lushows`.

## Errores comunes

- **Proyectar cobros por la fecha de factura** y no por cuándo paga de verdad el cliente.
- **Olvidar salidas "invisibles"**: impuestos, prima, cesantías, GMF, cuotas de crédito.
- **Hacerla una vez y no actualizarla**: una proyección vieja es ficción.
- **Mezclar lo proyectado con lo real** sin marcar cuál es cuál.
- **Calcular crecimientos de cabeza**: cualquier porcentaje o escenario va a `Matematicas_lushows`.

## Conexión con otros módulos

- Toma datos de cartera (**152**) para las entradas y de pagos (**154**) para las salidas.
- Se controla contra lo que realmente pasó vía conciliación (**35**, **153**).
- El flujo de caja *conceptual* y los unit economics viven en `economist_lushows` (50-59); aquí es la operación.
- Toda la matemática de proyección, escenarios y VPN → `Matematicas_lushows` (70-89).

## Siguiente paso típico

Arma un flujo semanal de 13 semanas, actualízalo cada lunes con lo que realmente entró y salió, y úsalo para decidir a tiempo qué cobrar primero (**152**) y qué pagar después (**154**).
