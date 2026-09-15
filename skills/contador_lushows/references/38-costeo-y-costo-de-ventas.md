# 38 — Costeo y costo de ventas

El **costo de ventas** es cuánto te costó *producir o adquirir* exactamente lo que vendiste. Si vendiste 100 platos, el costo de ventas es lo que esos 100 platos te costaron en ingredientes y preparación; no incluye lo que pagaste por la mercancía que todavía está en la bodega. Es la diferencia entre lo que *gastaste* y lo que *vendiste*: por eso es la pieza que define tu **utilidad bruta** (ventas − costo de ventas). Si no sabes tu costo de ventas, no sabes si estás ganando o perdiendo en cada producto.

Mucha gente confunde "costo" con "gasto". El **costo** se mete dentro del producto (la harina del pan); el **gasto** sostiene el negocio en general (el arriendo de la oficina, la publicidad). Distinguirlos es clave para fijar precios y para que los estados financieros tengan sentido.

## Costo vs. gasto

| Concepto | Qué es | Ejemplo en una cocina |
|---|---|---|
| **Costo** | Se incorpora al producto vendido | Carne, verduras, gas de cocción, cocinero |
| **Gasto** | Sostiene el negocio, no el producto | Arriendo del local, publicidad, contador |

## Costos directos e indirectos

| Tipo | Definición | Ejemplo |
|---|---|---|
| **Directo** | Se puede atribuir claramente a un producto | Ingredientes de un plato específico |
| **Indirecto** | Apoya la producción pero no se ve en un solo producto | Energía de la cocina, depreciación del horno |

Los indirectos se **reparten** entre los productos con un criterio razonable (horas de cocina, unidades producidas). Ese reparto, cuando se complica, se ejecuta con `Matematicas_lushows`.

## La fórmula del costo de ventas

Costo de ventas = Inventario inicial + Compras − Inventario final.

En palabras: lo que tenías + lo que compraste − lo que te quedó = lo que se fue (se vendió o se consumió). El **inventario final** se valora con PEPS o promedio (módulo 30), así que el método de inventario afecta directamente el costo de ventas.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Una cafetería en un mes: inventario inicial $500.000, compras $2.000.000, inventario final $400.000.

Costo de ventas = $500.000 + $2.000.000 − $400.000 = **$2.100.000**.

Si vendió $3.500.000, su **utilidad bruta** = $3.500.000 − $2.100.000 = **$1.400.000**.

Asiento al reconocer el costo de lo vendido en el mes:

| Cuenta | Débito | Crédito |
|---|---|---|
| Costo de ventas | $2.100.000 | |
| Inventario de mercancías | | $2.100.000 |

Débitos = créditos = $2.100.000. Cifras inventadas para ilustrar; toda suma se verifica con `Matematicas_lushows`.

## Errores comunes

- **Meter el arriendo o la publicidad al costo del producto**: son gastos, no costos; distorsiona el margen del producto.
- **No valuar bien el inventario final**: arrastra error directo al costo de ventas.
- **Olvidar los costos indirectos** (energía, depreciación de la cocina): el producto parece más barato de lo que es.
- **Reconocer el costo en un mes distinto al de la venta**: rompe la utilidad de cada período.
- **Calcular el reparto de indirectos de cabeza**: produce números no defendibles.

## Conexión con otros módulos

- El **inventario** y su método de valuación (PEPS/promedio) están en el módulo **30**.
- La **depreciación** de la maquinaria de producción es un costo indirecto (módulo **32**).
- Las **compras a crédito** generan cuentas por pagar (módulo **34**).
- El costo de ventas alimenta el **Estado de Resultados** (módulos de reportes).
- El reparto de indirectos y toda suma los ejecuta **Matematicas_lushows**.
- *Cuánto cobrar* a partir del costo es decisión de **economist_lushows**.

## Siguiente paso típico

Calcula el costo de ventas del período con la fórmula (inicial + compras − final), separa costos de gastos, y pasa la utilidad bruta a los estados financieros. Para fijar precios, lleva el costo unitario a `economist_lushows`.
