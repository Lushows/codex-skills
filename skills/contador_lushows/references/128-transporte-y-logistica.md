# 128 — Transporte y logística

Una empresa de transporte (carga, pasajeros, mensajería, última milla) tiene su capital rodando literalmente en la calle: los **vehículos** son su activo más grande y caro, y se desgastan kilómetro a kilómetro. Su contabilidad gira en torno a tres cosas: **depreciar bien la flota**, controlar el **combustible y mantenimiento** (que pueden comerse la utilidad), y aplicar el **régimen tributario especial** que Colombia da al transporte. Saber el costo real de mover una tonelada o un pasajero por kilómetro es lo que define si el negocio gana o solo "se mueve".

Término clave: **depreciación** es repartir el costo de un vehículo a lo largo de los años (o kilómetros) que sirve, en vez de cargarlo todo el día que lo compras.

## Cuentas típicas del sector

| Cuenta | Para qué sirve | Tipo |
|---|---|---|
| Flota de transporte (vehículos) | Camiones, buses, motos | Activo fijo |
| Depreciación acumulada de flota | Desgaste acumulado de los vehículos | Menor activo |
| Combustible | Gasto/costo de operar la flota | Costo |
| Mantenimiento y reparaciones | Llantas, repuestos, talleres | Costo |
| Peajes y costos de viaje | Gastos directos del recorrido | Costo |
| Ingreso por fletes / pasajes | La venta del servicio de transporte | Ingreso |

## Depreciación y costo de la flota

El vehículo es el activo crítico. Puede depreciarse por **tiempo** (vida útil en años) o, más fino, por **kilometraje** (unidades de producción). La depreciación es un **costo del servicio**, no un gasto administrativo. El cálculo se ejecuta con `Matematicas_lushows`.

| Concepto | Significado |
|---|---|
| Costo por kilómetro | Costos totales ÷ km recorridos |
| Costo de combustible/km | Mide eficiencia de la flota |
| Depreciación/km | Desgaste por kilómetro recorrido |
| Disponibilidad de flota | % de vehículos operativos |

## Régimen tributario y particularidades

- El **servicio de transporte de carga** y el **público de pasajeros terrestre** suelen tener tratamientos especiales de IVA en Colombia (excluido en varios casos): verifica la condición exacta del servicio que prestas.
- Hay **retención en la fuente** con tarifa propia para servicios de transporte: no inventes el porcentaje, confírmalo (módulo 43).
- Cuando contratas conductores **dueños de su vehículo**, ojo con la frontera contratista vs. empleado y con la base gravable del servicio.
- El **combustible** suele ser el mayor costo variable: contrólalo por vehículo y por ruta.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Un camión costó $200.000.000, vida útil estimada 800.000 km. En el mes recorrió 10.000 km. Depreciación = (200.000.000 ÷ 800.000) × 10.000 = $250/km × 10.000 = **$2.500.000**.

| Cuenta | Débito | Crédito |
|---|---|---|
| Depreciación (costo) | $2.500.000 | |
| Depreciación acumulada — flota | | $2.500.000 |

Débitos = créditos = $2.500.000. Cifras inventadas; toda suma y el costo por km se verifican con `Matematicas_lushows`.

## Errores comunes

- **No depreciar la flota** o hacerlo con vida útil irreal: oculta el desgaste y el costo real del servicio.
- **Tratar la depreciación como gasto administrativo** en vez de costo del servicio.
- **No controlar el combustible por vehículo**: ahí se fugan utilidades sin que te enteres.
- **Cobrar IVA en servicios excluidos** de transporte o aplicar mal la retención.
- **Capitalizar mantenimientos rutinarios** (son gasto) o llevar a gasto una mejora que alarga la vida útil (es mayor valor del activo).

## Conexión con otros módulos

- Los **activos fijos (PP&E)** en el módulo **31**; la **depreciación** en el **32**.
- El **costeo del servicio** se apoya en el **38**.
- El **IVA** (excluido) en el **41** y la **retención** en el **43**.
- **Contratista vs. empleado** (conductores) en el **59**.
- *Tarifas, rutas y rentabilidad del negocio*: `economist_lushows`.
- Todo costo por km y depreciación: `Matematicas_lushows`.

## Siguiente paso típico

Arma la ficha de cada vehículo (costo, vida útil en años o km, depreciación) y controla combustible y mantenimiento por unidad. Calcula tu costo por kilómetro para saber qué rutas y fletes dejan margen real.
