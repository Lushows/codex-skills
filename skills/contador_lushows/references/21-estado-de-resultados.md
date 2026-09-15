# 21 — Estado de Resultados (el P&L: ¿ganaste o perdiste?)

El **Estado de Resultados** (en inglés *P&L*, "Profit & Loss") cuenta lo que pasó durante un **período** (un mes, un trimestre, un año): cuánto vendiste, cuánto te costó y cuánto te quedó. A diferencia del balance (que es una foto de un día — módulo 20), este estado es una **película del período**.

Su pregunta central: *¿el negocio ganó o perdió, y por qué?* La línea final, la **utilidad (o pérdida) del período**, viaja luego al patrimonio del balance.

## La estructura en cascada

Se lee de arriba (ingresos) hacia abajo (utilidad), restando en cada escalón:

```
   Ingresos por ventas (operacionales)
 − Costo de ventas
 ─────────────────────────────────────
 = UTILIDAD BRUTA
 − Gastos de administración
 − Gastos de ventas
 ─────────────────────────────────────
 = UTILIDAD OPERACIONAL
 + Otros ingresos  − Otros gastos (financieros, etc.)
 ─────────────────────────────────────
 = UTILIDAD ANTES DE IMPUESTOS
 − Impuesto de renta
 ─────────────────────────────────────
 = UTILIDAD NETA DEL PERÍODO
```

> **Términos clave:**
> - *Costo de ventas:* lo que cuesta producir o comprar lo que vendiste (insumos, materia prima, mano de obra directa).
> - *Gasto:* lo que cuesta operar el negocio aunque no vendas (arriendo, sueldos administrativos, servicios).
> - *Utilidad bruta:* ventas menos costo. *Utilidad operacional:* lo anterior menos gastos. *Utilidad neta:* lo que queda después de impuestos.

## Por función vs. por naturaleza

NIIF permite presentar los gastos de dos formas. Debes elegir una y mantenerla.

| Criterio | Cómo agrupa | Ejemplo de líneas | Ideal para |
|---|---|---|---|
| **Por función** | Según para qué se usó el gasto | Costo de ventas, gastos de admón., gastos de ventas | Comercio, restaurantes, servicios |
| **Por naturaleza** | Según qué tipo de gasto es | Compras de insumos, sueldos, depreciación, arriendos | Industria, manufactura |

La presentación **por función** es la más común en pymes colombianas porque muestra la utilidad bruta, clave para fijar precios.

## Ejemplo rotulado — cifras ILUSTRATIVAS / inventadas

**Restaurante "La Sazón" — Estado de Resultados del 1-ene al 31-dic-2025 (COP, por función)**

| Concepto | Valor | % sobre ventas |
|---|---:|---:|
| Ingresos por ventas | 120.000.000 | 100,0% |
| (−) Costo de ventas (insumos) | (48.000.000) | (40,0%) |
| **Utilidad bruta** | **72.000.000** | **60,0%** |
| (−) Gastos de administración | (30.000.000) | (25,0%) |
| (−) Gastos de ventas | (18.000.000) | (15,0%) |
| **Utilidad operacional** | **24.000.000** | **20,0%** |
| (−) Gastos financieros (intereses) | (3.000.000) | (2,5%) |
| **Utilidad antes de impuestos** | **21.000.000** | **17,5%** |
| (−) Impuesto de renta (ilustrativo) | (6.300.000) | (5,3%) |
| **Utilidad neta del período** | **14.700.000** | **12,3%** |

Los porcentajes son **análisis vertical** (módulo 26). Toda división y porcentaje se ejecuta y verifica en código vía Matematicas_lushows; las tasas de impuesto reales no se inventan: se confirman con la norma vigente.

## Cómo leerlo en 30 segundos
1. **Margen bruto** (utilidad bruta / ventas): ¿tus precios cubren bien el costo? Aquí, 60%.
2. **Margen operacional**: ¿la operación es rentable antes de financiación e impuestos? Aquí, 20%.
3. **Margen neto**: lo que de verdad queda. Aquí, 12,3%.
4. Si la utilidad bruta es buena pero la neta es flaca, el problema está en los gastos, no en el precio.

## Errores comunes
- **Confundir costo con gasto:** el insumo que se vende es costo; el arriendo de la oficina es gasto. Mezclarlos distorsiona el margen bruto.
- **Meter en el P&L compras de activos:** comprar una nevera no es gasto del período; es un activo que se deprecia (va al balance).
- **Registrar el IVA como ingreso:** el IVA cobrado no es tuyo, es de la DIAN; es un pasivo, no ingreso.
- **Olvidar provisionar el impuesto de renta:** la utilidad antes de impuestos no es la que te queda.
- **Reconocer ventas no cobradas mal:** bajo NIIF la venta se reconoce cuando se entrega, no cuando se cobra (base de causación).

## Conexión con otros módulos
- **Módulo 20 (Situación financiera):** la utilidad neta de aquí aumenta el patrimonio allá.
- **Módulo 22 (Flujos de efectivo, método indirecto):** parte de esta utilidad para explicar la caja.
- **Módulo 23 (Cambios en patrimonio):** recibe la utilidad del período.
- **Módulo 26 y 27:** análisis vertical y márgenes de rentabilidad nacen de este estado.
- **Matematicas_lushows:** ejecuta restas en cascada, márgenes y porcentajes con `decimal`.

## Siguiente paso típico
Tienes utilidad pero ¿hay plata en el banco? Eso lo responde el **módulo 22 (Estado de flujos de efectivo)**: ganar no es lo mismo que tener caja.
