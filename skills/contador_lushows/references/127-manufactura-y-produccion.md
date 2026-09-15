# 127 — Manufactura y producción

Una fábrica **transforma** materias primas en productos terminados, y ahí vive la complejidad contable más rica de todos los sectores: el costo de un producto se arma con **tres ingredientes** (materia prima, mano de obra y costos indirectos), y el producto pasa por etapas (materia prima → producto en proceso → producto terminado). Saber cuánto cuesta cada unidad fabricada no es opcional: es la base para fijar precios, decidir qué producir y no quebrar. La contabilidad de costos es el corazón de este sector.

Términos clave: **MOD** (Mano de Obra Directa, los operarios que tocan el producto), **CIF** (Costos Indirectos de Fabricación: energía, depreciación de máquinas, supervisión) y **producto en proceso** (lo que está a medio fabricar al cierre).

## Los tres elementos del costo

| Elemento | Qué es | Ejemplo |
|---|---|---|
| Materia prima directa | Insumos que se ven en el producto | Tela en una camisa |
| Mano de obra directa (MOD) | Operarios que fabrican | El que cose la camisa |
| Costos indirectos (CIF) | Todo lo demás de la planta | Energía, depreciación de máquinas, supervisor |

Costo de producción = Materia prima + MOD + CIF. El reparto de los CIF entre productos (por horas máquina, unidades, etc.) se ejecuta con `Matematicas_lushows`.

## Cuentas e inventarios por etapa

| Cuenta | Para qué sirve | Tipo |
|---|---|---|
| Inventario de materias primas | Insumos sin usar | Activo |
| Inventario de productos en proceso | Lo que está a medio fabricar | Activo |
| Inventario de productos terminados | Listo para vender | Activo |
| Costo de ventas | Lo que costó lo vendido | Costo |
| CIF aplicados / control | Acumula y reparte indirectos | Cuenta de costo |

El flujo: la materia prima entra a proceso, se le suman MOD y CIF, sale como producto terminado y, al venderse, pasa a costo de ventas. Cada flecha es un asiento.

## Órdenes de producción y métodos

- **Costeo por órdenes**: para productos a la medida (mueblería, imprenta) — se acumula el costo por cada orden.
- **Costeo por procesos**: para producción continua y homogénea (cemento, gaseosas) — el costo se promedia por unidad del período.
- El **IVA** de la materia prima comprada es **descontable** (lo recuperas), distinto del IVA de un negocio excluido. La maquinaria se **deprecia** (módulo 32) y esa depreciación es CIF.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Una orden de producción consume: materia prima $4.000.000, MOD $2.500.000, CIF aplicados $1.500.000.

Costo de producción = 4.000.000 + 2.500.000 + 1.500.000 = **$8.000.000**.

| Cuenta | Débito | Crédito |
|---|---|---|
| Inventario productos terminados | $8.000.000 | |
| Inventario productos en proceso | | $8.000.000 |

Débitos = créditos = $8.000.000. Cifras inventadas; el reparto de CIF y toda suma se verifican con `Matematicas_lushows`.

## Errores comunes

- **Olvidar los CIF**: el producto parece más barato de lo que es y vendes con margen falso.
- **No valorar el producto en proceso** al cierre: el costo de ventas queda inflado o subestimado.
- **Meter gastos de administración o ventas al costo del producto**: solo lo de planta es costo.
- **Repartir los CIF "a ojo"** sin una base razonable y verificada.
- **No separar las tres etapas de inventario**: pierdes la trazabilidad del costo.

## Conexión con otros módulos

- El **costeo y costo de ventas** general en el módulo **38**.
- Los **inventarios** y su valuación en el **30**.
- La **depreciación** de maquinaria (CIF) en el **32**.
- El **IVA descontable** de insumos en el **41**.
- *Qué producir, mezcla de productos y precios*: `economist_lushows`.
- Todo reparto de CIF y costeo unitario: `Matematicas_lushows`.

## Siguiente paso típico

Define si costeas por órdenes o por procesos, separa tus inventarios en tres etapas y arma la hoja de costos de un producto con sus tres elementos. Establece una base razonable para repartir los CIF y verifícala con `Matematicas_lushows`.
