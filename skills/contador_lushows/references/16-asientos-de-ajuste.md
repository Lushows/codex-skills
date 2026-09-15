# 16 — Asientos de ajuste: poner cada peso en su período

Al final de cada período (mes, trimestre, año), antes de cerrar, hay hechos que **ya ocurrieron económicamente** pero que aún no están registrados, o que están registrados de forma incompleta. Los **asientos de ajuste** corrigen eso para que las cuentas reflejen la realidad.

> **Asiento de ajuste** = registro de fin de período que reconoce ingresos/gastos en el período que les corresponde, aunque el efectivo entre o salga en otro momento.

Esta es la aplicación práctica del **devengo** (módulo 17): el peso va al período donde se generó, no donde se pagó.

## Los cuatro tipos clásicos de ajuste

| Tipo | Qué corrige | Ejemplo |
|---|---|---|
| Depreciación | El desgaste de un activo fijo | El horno pierde valor cada mes |
| Devengos (causaciones) | Algo que ya pasó pero no se ha pagado/cobrado | Sueldos del mes que pagas el 5 del siguiente |
| Diferidos | Algo que pagaste/cobraste por anticipado | Arriendo de 6 meses pagado de una vez |
| Provisiones | Una obligación probable de monto estimado | Posible incobrable de un cliente |

> Esto es una **visión panorámica**. El detalle fino (tablas de depreciación, cálculo de provisiones NIIF, prestaciones) vive en el **Bloque 3** de esta skill.

## Ejemplo 1 — Depreciación mensual (cifras ILUSTRATIVAS / inventadas)

Un horno costó $2.400.000 y se deprecia en 10 años (120 meses) en línea recta. Depreciación mensual = 2.400.000 / 120 = **$20.000/mes**.

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto depreciación (5160) | 20.000 | |
| Depreciación acumulada (1592) | | 20.000 |
| **Totales** | **20.000** | **20.000** |

Nota: el activo no se borra; se "acumula" su desgaste en una cuenta que **resta** del activo.

## Ejemplo 2 — Devengo de sueldos (cifras ILUSTRATIVAS / inventadas)

A 31 de marzo debes $800.000 de sueldos que pagarás el 5 de abril. El gasto es de marzo.

| Cuenta | Débito | Crédito |
|---|---|---|
| Gastos de personal (5105) | 800.000 | |
| Salarios por pagar (2505) | | 800.000 |
| **Totales** | **800.000** | **800.000** |

## Ejemplo 3 — Diferido que se consume (cifras ILUSTRATIVAS / inventadas)

Pagaste $600.000 de arriendo por 6 meses por anticipado (quedó como activo "gastos pagados por anticipado"). Cada mes consumes 600.000/6 = $100.000.

| Cuenta | Débito | Crédito |
|---|---|---|
| Arrendamientos (5120) | 100.000 | |
| Gastos pagados por anticipado (1710) | | 100.000 |
| **Totales** | **100.000** | **100.000** |

## Cómo identificar qué ajustes necesitas

1. ¿Tengo **activos fijos**? → deprecia.
2. ¿Hay gastos del período que **aún no pago**? → devenga.
3. ¿Pagué/cobré algo **por adelantado**? → difiere y consume por partes.
4. ¿Hay una **pérdida probable** (cliente que no pagará)? → provisiona.

## Errores comunes

- **Saltarse los ajustes** y mostrar utilidades infladas (faltan gastos del período).
- **Depreciar de cabeza**: calcula la cuota en código, con `decimal`.
- **Registrar un anticipo como gasto inmediato** en vez de diferirlo.
- **Confundir provisión (estimación) con un pago real**.

## Conexión con otros módulos

- **Módulo 15** — los ajustes se hacen sobre el balance de comprobación.
- **Módulo 17** — el principio de devengo es la razón de existir de estos ajustes.
- **Módulo 18** — después de ajustar y recomprobar, se cierra el período.
- **Bloque 3** — el detalle de depreciación, provisiones y prestaciones.
- **Matematicas_lushows** EJECUTA cuotas, prorrateos y estimaciones.

## Siguiente paso típico

Ve al **módulo 17** para entender el principio que justifica todo esto: devengo vs. caja.
