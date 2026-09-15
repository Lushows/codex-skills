# 158 — Capital de trabajo

El **capital de trabajo** es la plata que el negocio necesita para funcionar en el día a día: comprar mercancía, pagar la nómina y cubrir gastos **mientras** los clientes le pagan. En números, es lo que tienes en activos de corto plazo (efectivo, cartera, inventario) menos lo que debes en el corto plazo (proveedores, impuestos por pagar). Si es positivo y suficiente, el negocio respira; si es negativo o muy ajustado, vives apagando incendios de caja aunque vendas bien. Es uno de los puntos donde **el efectivo mata o salva al negocio**.

Aquí enfocamos cómo **medirlo, controlarlo y optimizarlo** desde la operación de tesorería. La estrategia de cuánto capital necesitas y cómo financiarlo es de `economist_lushows`; los cálculos se ejecutan en `Matematicas_lushows`.

## Qué lo compone

| Activo corriente (a favor) | Pasivo corriente (en contra) |
|---|---|
| Efectivo y bancos | Proveedores por pagar |
| Cuentas por cobrar (cartera) | Impuestos por pagar |
| Inventario | Nómina y prestaciones por pagar |
| Pagos anticipados | Cuotas de crédito del año |

**Capital de trabajo = activo corriente − pasivo corriente.** No se calcula de cabeza: cualquier resta va a `Matematicas_lushows`.

## El ciclo de conversión de efectivo

El **ciclo de conversión de efectivo (CCE)** mide **cuántos días pasa tu plata "atrapada"** desde que pagas el inventario hasta que cobras la venta. Entre más corto, mejor: tu dinero da más vueltas.

| Componente | Qué mide |
|---|---|
| Días de inventario | Cuánto tarda en venderse lo que compraste |
| (+) Días de cartera | Cuánto tardan los clientes en pagarte |
| (−) Días de proveedores | Cuánto tardas tú en pagarle a los proveedores |
| (=) Ciclo de conversión | Días que tu efectivo queda inmovilizado |

Si pagas a proveedores a 60 días pero cobras y vendes en 40, ¡tu ciclo es negativo y los proveedores te financian! Ese es el ideal de muchos negocios.

## Cómo optimizarlo

| Palanca | Efecto |
|---|---|
| Cobrar más rápido (módulo **152**) | Reduce días de cartera |
| Rotar mejor el inventario | Reduce días de inventario |
| Negociar más plazo con proveedores (**154**) | Aumenta días de proveedores |
| Reducir efectivo ocioso | Libera plata para operar |

El equilibrio: optimizar **sin** ahogar al proveedor ni quedarte sin stock.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Activo corriente $30.000.000, pasivo corriente $18.000.000 (cifras inventadas):

Capital de trabajo = $30.000.000 − $18.000.000 = **$12.000.000**.

Si el inventario rota en 30 días, la cartera cobra en 40 y pagas a proveedores en 35: ciclo = 30 + 40 − 35 = **35 días** de efectivo atrapado. Bajar la cartera a 25 días recortaría el ciclo a 20. Cifras inventadas; toda resta y conteo de días se verifica con `Matematicas_lushows`.

## Errores comunes

- **Crecer en ventas sin capital de trabajo**: vender más a crédito te seca la caja ("morir de éxito").
- **Acumular inventario** que no rota: plata dormida en bodega.
- **Cobrar lento y pagar rápido**: el peor combo para el ciclo de efectivo.
- **Confundir utilidad con capital de trabajo**: puedes ser rentable y no tener liquidez.
- **Calcular el ciclo de cabeza**: días y restas siempre a `Matematicas_lushows`.

## Conexión con otros módulos

- Se nutre de cartera (**152**, **33**), inventario (**30**) y proveedores (**154**, **34**).
- Su salud se ve en el flujo de caja proyectado (**151**) y en los ratios de liquidez (**27**).
- Se lee desde el estado de situación financiera (**20**).
- La estrategia de cuánto capital necesitas y unit economics → `economist_lushows` (50-59); los cálculos → `Matematicas_lushows`.

## Siguiente paso típico

Calcula tu capital de trabajo y tu ciclo de conversión de efectivo con `Matematicas_lushows`, identifica la palanca más floja (cartera, inventario o proveedores) y trabájala con los módulos **152** y **154**.
