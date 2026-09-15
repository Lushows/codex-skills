# 120 — Gastronomía y restaurantes

El sector gastronómico (restaurantes, cafeterías, bares, dark kitchens) es de los más difíciles de costear porque vende un producto que se **transforma y se daña**: los ingredientes se compran, se preparan, se sirven y lo que no se usa se pierde. Aquí la utilidad se gana o se pierde en la cocina, plato por plato, no en el papeleo. Por eso un restaurante necesita una contabilidad que entienda **recetas, mermas, propina e impuesto al consumo**. Este es el sector del proyecto **GASTROWHATS** (la Calculadora de Costos Gastronómicos).

Antes de empezar: un **costo** es lo que se mete en el plato (la carne, el gas); un **gasto** sostiene el negocio (arriendo, mesero, publicidad). Confundirlos hace que creas que ganas cuando pierdes.

## Cuentas típicas del sector

| Cuenta | Para qué sirve | Tipo |
|---|---|---|
| Inventario de materia prima (alimentos/bebidas) | Lo que está en bodega y nevera | Activo |
| Costo de ventas — alimentos | Lo que costó lo que se sirvió | Costo |
| Mermas y desperdicios | Lo que se dañó o se perdió | Costo/Gasto |
| Propinas por pagar | Dinero del personal, no de la empresa | Pasivo |
| Impuesto al consumo (INC) por pagar | El 8% que recaudas para la DIAN | Pasivo |

## Cómo costear una receta (ficha técnica)

La **receta estándar** o ficha técnica lista cada ingrediente, su cantidad y su costo. El costo del plato es la suma de los ingredientes **más la merma** (lo que se pierde al pelar, cocinar o porcionar). Esa merma se expresa como un porcentaje y se ejecuta con `Matematicas_lushows`, nunca de cabeza.

| Concepto | Detalle |
|---|---|
| Costo de ingredientes | Suma de cada insumo por su porción |
| Factor de merma | % que se pierde en preparación |
| Costo del plato | Ingredientes ajustados por merma |
| Food cost % | Costo del plato ÷ precio de venta |

El **food cost %** (porcentaje del precio que se va en comida) es el KPI rey: en restaurantes sanos suele moverse en un rango que conviene validar; *cuánto cobrar* por el plato es decisión de `economist_lushows`, no contable.

## INC y propina (lo particular de Colombia)

- El servicio de restaurante generalmente está gravado con **Impuesto Nacional al Consumo (INC)**, no con IVA. El INC se recauda del cliente, se separa y se paga a la DIAN; **no es ingreso tuyo**.
- Quien está en **Régimen Simple** puede tener un tratamiento distinto del INC: verifícalo (módulo 63).
- La **propina** es del personal: entra y sale, no es ingreso ni gasto de la empresa. Se registra como un pasivo hasta repartirla.
- Los **alimentos crudos** (sin preparar) pueden tener un tratamiento de IVA distinto del plato preparado: confírmalo con la norma vigente.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Un restaurante vende un plato en $40.000. Ingredientes $11.000, merma estimada 10% → costo $12.100. Food cost = 12.100 ÷ 40.000 = **30,25%**. Sobre la venta cobra INC del 8% = $3.200, que es de la DIAN.

Asiento de la venta:

| Cuenta | Débito | Crédito |
|---|---|---|
| Caja / Bancos | $43.200 | |
| Ingreso por ventas | | $40.000 |
| INC por pagar | | $3.200 |

Débitos = créditos = $43.200. Cifras inventadas; toda suma se verifica con `Matematicas_lushows`.

## Errores comunes

- **Tratar la propina como ingreso**: infla las ventas y te hace pagar impuestos sobre plata que no es tuya.
- **Olvidar la merma** al costear: el plato parece más barato y vendes perdiendo.
- **Confundir INC con IVA**: declaras mal y te expones a sanciones.
- **No hacer inventario físico**: el inventario perecedero se daña y, si no lo cuentas, el costo de ventas queda irreal.
- **Costear "a ojo"** sin ficha técnica: cada plato debe tener su costo calculado y verificado.

## Conexión con otros módulos

- El **costeo y costo de ventas** general está en el módulo **38**.
- El **inventario** y su valuación (PEPS/promedio) en el módulo **30**; aquí es perecedero, exige toma física frecuente (módulo **76**).
- El **INC** se declara como impuesto territorial/nacional al consumo: revisa **40** y **44**.
- La nómina del personal de cocina/salón está en el bloque **50**.
- *Cuánto cobrar* por el plato y la viabilidad del negocio: `economist_lushows`.
- Todo cálculo de merma, food cost y márgenes: `Matematicas_lushows`.

## Siguiente paso típico

Arma la ficha técnica de tus platos top con su merma, calcula el food cost de cada uno, y separa propina e INC del ingreso real. Si llevas el restaurante con el bot GASTROWHATS, alinea la Calculadora de Costos con estas mismas cuentas.
