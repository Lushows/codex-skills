# 124 — Agro y agronegocios

El campo tiene una particularidad que ningún otro sector comparte: sus activos **están vivos y crecen solos**. Una vaca engorda, un cultivo madura, un árbol de aguacate da fruto año tras año. Contablemente, esto se llama **activos biológicos** y tiene su propia norma. Además, el agro trabaja por **ciclos productivos** largos (una cosecha puede tardar meses) y en Colombia goza de **beneficios tributarios** pensados para impulsar el campo. Llevar bien las cuentas de un agronegocio es entender que el valor cambia mientras el animal o la planta simplemente... vive.

Término clave: **activo biológico** es un animal o planta viva que el negocio controla y del que espera obtener producto o crías.

## Cuentas típicas del sector

| Cuenta | Para qué sirve | Tipo |
|---|---|---|
| Activos biológicos (ganado, cultivos) | Animales y plantas en crecimiento | Activo |
| Productos agrícolas cosechados | Fruto/leche/cosecha lista para vender | Inventario |
| Costos de cultivo / levante | Semillas, alimento, fertilizantes, jornales | Costo |
| Ingreso por venta de productos agrícolas | La venta de la cosecha o el animal | Ingreso |
| Cambio en valor razonable de activos biológicos | Ajuste por crecimiento/precio | Ingreso/Gasto |

## Activos biológicos (NIC 41 / NIIF para pymes sección 34)

La norma pide medir los activos biológicos a su **valor razonable menos costos de venta** (cuánto valdrían hoy en el mercado, menos lo que cuesta venderlos), y registrar el **cambio** de ese valor como ingreso o gasto del período. Cuando se cosecha o sacrifica, el producto pasa a **inventario**. Esa valuación, cuando es compleja, se ejecuta con `Matematicas_lushows`.

| Tipo de planta | Tratamiento |
|---|---|
| Planta productora (árbol frutal, cafeto) | Se trata como propiedad/planta (se deprecia) |
| Producto agrícola (el fruto, el grano) | Inventario al cosechar |
| Animal de engorde o cría | Activo biológico a valor razonable |

## Ciclos productivos y beneficios agro

- Los costos se **acumulan durante el ciclo** (siembra → crecimiento → cosecha) y se llevan al costo de ventas cuando se vende.
- Colombia tiene **incentivos al agro** (rentas exentas para ciertas actividades agropecuarias, beneficios para inversiones en el campo). No inventes tarifas ni plazos: verifica el beneficio vigente y sus requisitos.
- Muchas **ventas de productos agrícolas sin transformar** pueden estar **excluidas o exentas de IVA**: confirma la lista vigente de bienes.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Un hato tiene 50 novillos registrados a $1.500.000 c/u = $75.000.000. Al cierre, por engorde y precio, valen $1.700.000 c/u = $85.000.000.

| Cuenta | Débito | Crédito |
|---|---|---|
| Activos biológicos — ganado | $10.000.000 | |
| Cambio en valor razonable (ingreso) | | $10.000.000 |

Débitos = créditos = $10.000.000. Cifras inventadas; la valuación y toda suma se verifican con `Matematicas_lushows`.

## Errores comunes

- **Tratar el ganado o el cultivo como inventario al costo** ignorando el valor razonable.
- **Llevar todos los costos a gasto del mes** en vez de acumularlos en el activo durante el ciclo.
- **Asumir beneficios tributarios sin cumplir requisitos**: pierdes el beneficio y te sancionan.
- **Cobrar IVA en productos exentos/excluidos** o no documentar bien la condición.
- **No separar planta productora (se deprecia) de su fruto (inventario)**.

## Conexión con otros módulos

- El **inventario** del producto cosechado en el módulo **30**; **costeo** en el **38**.
- Las **plantas productoras** se deprecian (módulo **32**).
- El **IVA** (exentos/excluidos) en el **41**.
- El **impuesto de renta** y rentas exentas en el **42**.
- *Viabilidad del cultivo/hato y precios*: `economist_lushows`.
- Toda valuación a valor razonable y suma: `Matematicas_lushows`.

## Siguiente paso típico

Inventaría tus activos biológicos y sepáralos de las plantas productoras. Acumula los costos por ciclo y, al cierre, ajusta el valor razonable. Verifica con tu contador titulado qué beneficios agro vigentes aplican a tu actividad.
