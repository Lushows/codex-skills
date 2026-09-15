# 33 — Cuentas por cobrar (cartera)

Las **cuentas por cobrar** son la plata que te deben: vendiste o prestaste un servicio, pero el cliente todavía no te paga. En el día a día se le dice **cartera**. Es un activo real (te van a pagar), pero también un riesgo: parte de esa plata puede que nunca llegue. Llevar bien la cartera evita dos desastres comunes: creer que tienes utilidad que en realidad es solo "papel", y descubrir tarde que un cliente lleva meses sin pagar.

Una venta a crédito **no es lo mismo** que una venta de contado. Aunque la utilidad se reconoce igual (vendiste), el efectivo todavía no entró. Por eso la cartera se vigila aparte.

## Reconocimiento: cuándo nace la cuenta por cobrar

Nace cuando entregas el bien o prestas el servicio y tienes el **derecho a cobrar**, aunque no te hayan pagado. Asiento típico de una venta a crédito:

| Cuenta | Débito | Crédito |
|---|---|---|
| Clientes (cuentas por cobrar) | (valor) | |
| Ingresos por ventas | | (valor) |

Cuando el cliente paga, la cartera se cancela contra el banco:

| Cuenta | Débito | Crédito |
|---|---|---|
| Bancos | (valor) | |
| Clientes (cuentas por cobrar) | | (valor) |

## Edades de cartera (aging)

Es una tabla que clasifica lo que te deben **según hace cuánto venció**. Es la herramienta número uno para no dejar envejecer la plata:

| Rango | Estado | Acción típica |
|---|---|---|
| Por vencer | Sano | Seguimiento normal |
| 1–30 días vencido | Atención | Recordatorio amable |
| 31–60 días | Riesgo | Llamada, plan de pago |
| 61–90 días | Alto riesgo | Gestión formal de cobro |
| +90 días | Posible incobrable | Evaluar deterioro |

## Deterioro (cartera de dudoso recaudo)

Cuando hay **evidencia** de que un cliente probablemente no pagará (lleva meses vencido, quebró, no responde), bajo NIIF para pymes se reconoce un **deterioro**: se reconoce un gasto y se crea una cuenta que resta de la cartera, sin borrar todavía la deuda.

## Ejemplo de deterioro (cifras ILUSTRATIVAS / inventadas)

Un cliente te debe $1.000.000, lleva 120 días sin pagar y no responde. Estimas que probablemente no recuperarás $300.000.

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto por deterioro de cartera | $300.000 | |
| Deterioro acumulado de clientes | | $300.000 |

Débitos = créditos = $300.000. Si más adelante confirmas que es totalmente incobrable, se da de baja contra ese deterioro. Cifras inventadas para ilustrar; el monto a deteriorar se estima con criterio y, si involucra cálculo, con `Matematicas_lushows`.

## Errores comunes

- **No separar cartera por edades**: la plata envejece sin que nadie la cobre.
- **Confundir utilidad con caja**: vendiste a crédito, pero ese dinero aún no está disponible.
- **No reconocer el deterioro** de cartera vieja: los activos quedan inflados.
- **Borrar (castigar) la deuda sin soporte** de que es incobrable: rompe la auditabilidad.
- **No registrar el pago contra la cartera correcta**: descuadra el saldo del cliente.

## Conexión con otros módulos

- El **deterioro** es una estimación, emparentada con las provisiones del módulo **36**.
- La cartera afecta el **flujo de efectivo**: hay utilidad pero no necesariamente caja (módulos de reportes).
- Su espejo —lo que tú debes— son las **cuentas por pagar** del módulo **34**.
- La **conciliación** confirma qué pagos realmente entraron (módulo **35**).
- El monto a deteriorar, si requiere cálculo, lo ejecuta **Matematicas_lushows**.

## Siguiente paso típico

Arma el reporte de **edades de cartera** cada mes, define una política de deterioro por rango y conéctalo con el control de proveedores del módulo **34**.
