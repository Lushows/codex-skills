# 22 — Estado de Flujos de Efectivo (la verdad sobre tu caja)

Hay una frase que todo dueño debe tatuarse: **ganar utilidad no es lo mismo que tener plata**. Un negocio puede mostrar utilidad en el estado de resultados (módulo 21) y aun así quedarse sin caja para pagar la nómina. El **Estado de Flujos de Efectivo** explica exactamente esto: de dónde entró el dinero y a dónde se fue durante el período.

Bajo el marco colombiano (NIIF y NIIF para pymes) es uno de los estados obligatorios. Responde: *¿por qué la caja al final del año no es la misma que al inicio?*

## Las tres actividades

Todo movimiento de efectivo cae en una de tres cajas. Saber en cuál cae te dice si el negocio es sano.

| Actividad | Qué incluye | Señal sana |
|---|---|---|
| **Operación** | Cobros a clientes, pagos a proveedores, nómina, impuestos | Debe ser **positiva**: el negocio genera caja por sí mismo |
| **Inversión** | Compra/venta de equipos, vehículos, locales | Negativa al crecer (compras activos); normal |
| **Financiación** | Préstamos recibidos/pagados, aportes de socios, dividendos | Refleja cómo te financias |

> **Regla de oro:** un negocio sano vive de su **flujo de operación**, no de pedir prestado (financiación) ni de vender sus activos (inversión).

## Dos métodos para la parte de operación

| Método | Cómo arma la operación | Ventaja | Quién lo usa |
|---|---|---|---|
| **Directo** | Lista cobros y pagos reales (cobré a clientes, pagué a proveedores) | Claro e intuitivo | Recomendado por NIIF |
| **Indirecto** | Parte de la utilidad neta y le suma/resta partidas que no son caja | Más rápido de armar | El más común en la práctica |

Inversión y financiación se presentan igual en ambos métodos. La diferencia es solo cómo se construye la operación.

### Por qué el indirecto ajusta la utilidad
La utilidad incluye cosas que **no movieron caja** (depreciación) y excluye movimientos que **sí la movieron** (cobrar una venta del año pasado). El método indirecto corrige eso:
- **Suma** gastos sin caja (depreciación, provisiones).
- **Resta** aumentos de cuentas por cobrar (vendiste pero no cobraste).
- **Suma** aumentos de proveedores (compraste pero no pagaste).

## Ejemplo rotulado — cifras ILUSTRATIVAS / inventadas

**Restaurante "La Sazón" — Flujo de Efectivo 2025, método indirecto (COP)**

| Concepto | Valor |
|---|---:|
| **ACTIVIDADES DE OPERACIÓN** | |
| Utilidad neta del período | 14.700.000 |
| (+) Depreciación (no es salida de caja) | 4.000.000 |
| (−) Aumento de cuentas por cobrar | (1.500.000) |
| (+) Aumento de proveedores | 2.000.000 |
| **Efectivo neto de operación** | **19.200.000** |
| **ACTIVIDADES DE INVERSIÓN** | |
| (−) Compra de equipo de cocina | (8.000.000) |
| **Efectivo neto de inversión** | **(8.000.000)** |
| **ACTIVIDADES DE FINANCIACIÓN** | |
| (−) Abono a préstamo bancario | (5.000.000) |
| **Efectivo neto de financiación** | **(5.000.000)** |
| **AUMENTO NETO DE EFECTIVO** | **6.200.000** |
| (+) Efectivo al inicio del año | 5.800.000 |
| **= Efectivo al final del año** | **12.000.000** |

Verificación de amarre: el efectivo final (12.000.000) **debe coincidir** con la caja y bancos del balance (módulo 20). Si no coincide, hay error. Las sumas se ejecutan en código vía Matematicas_lushows.

## Cómo leerlo en 30 segundos
1. ¿La **operación** es positiva? Si sí, el negocio se sostiene solo. (Aquí: +19,2 M, sano.)
2. ¿De dónde salió la plata para crecer? Aquí, la operación pagó la inversión y aún sobró.
3. ¿Vives de préstamos? Si la financiación es la única positiva, hay alerta.

## Errores comunes
- **Creer que utilidad = caja:** el error #1. Por eso existe este estado.
- **Olvidar sumar la depreciación** en el método indirecto (es un gasto que no salió del banco).
- **Mezclar actividades:** pagar un préstamo es financiación, no operación.
- **No amarrar con el balance:** el efectivo final SIEMPRE debe igualar la caja del balance.
- **Meter el IVA como flujo de operación propio:** es dinero de la DIAN en tránsito.

## Conexión con otros módulos
- **Módulo 20:** el efectivo final amarra con caja y bancos del balance.
- **Módulo 21:** el método indirecto parte de la utilidad neta de ese estado.
- **Módulo 23:** los pagos de dividendos y aportes también aparecen en cambios de patrimonio.
- **Módulo 27 (Ratios):** complementa la liquidez con la capacidad real de generar caja.
- **economist_lushows:** decisiones de inversión o de pedir crédito se basan en este flujo, pero las DECIDE economist.

## Siguiente paso típico
Revisa el **módulo 23 (Cambios en el patrimonio)** para ver cómo se movió lo que es de los dueños, incluyendo aportes y dividendos que ya viste aquí en financiación.
