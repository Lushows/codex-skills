# 150 — Gestión de tesorería

La **tesorería** es la función que cuida el efectivo del negocio: el dinero que está en caja (efectivo físico que tienes a la mano) y en los bancos. Su trabajo es asegurar que siempre haya plata disponible para pagar lo que toca pagar, ni más (dinero ocioso que no rinde) ni menos (quedarte sin con qué pagar la nómina). Una empresa puede ser rentable en el papel y aun así quebrar si se le acaba el efectivo: por eso decimos que **el efectivo es lo que mata o salva al negocio**.

Aquí nos enfocamos en la **operación y el control contable** de la tesorería: cómo registrar, controlar y dejar auditable cada movimiento de dinero. Las decisiones de *estrategia* financiera (cuánto capital levantar, dónde invertir el excedente) viven en `economist_lushows`.

## Qué hace la función de tesorería

| Tarea | En qué consiste |
|---|---|
| Control de caja | Saber cuánto efectivo físico hay y que cuadre con lo registrado |
| Control de bancos | Conocer el saldo real de cada cuenta bancaria |
| Programar pagos | Decidir qué se paga y cuándo (ver módulo **154**) |
| Cobrar a tiempo | Que el dinero entre cuando debe (ver módulo **152**) |
| Proyectar la caja | Anticipar si va a faltar o sobrar dinero (ver módulo **151**) |
| Custodiar el efectivo | Que nadie use la plata sin autorización ni soporte |

## Control de caja: arqueo

El **arqueo de caja** es contar el efectivo físico y compararlo con lo que dicen los libros. Si hay caja menor (un fondo fijo para gastos pequeños), se arquea seguido. Diferencias se investigan, no se "tapan".

| Concepto | Qué significa |
|---|---|
| Fondo fijo de caja menor | Monto autorizado para gastos pequeños del día a día |
| Arqueo | Conteo físico vs. saldo en libros |
| Sobrante / faltante | Diferencia que debe explicarse con soporte |
| Reembolso | Reponer la caja menor por los gastos ya hechos |

## El GMF (4x1000) — Colombia

El **Gravamen a los Movimientos Financieros (GMF)**, conocido como **4x1000**, es un impuesto que cobra el banco sobre ciertos retiros y movimientos de las cuentas. "4x1000" significa que, en términos generales, por cada $1.000 que se mueven se cobra una pequeña fracción. Para tesorería esto importa por dos razones: (1) es un **costo real** que reduce tu efectivo cada vez que mueves plata, y (2) existe el beneficio de **marcar una sola cuenta como exenta** hasta cierto tope mensual, lo que ayuda a no pagar de más. No memorices tarifas ni topes aquí: cámbianse y deben confirmarse con el contador titulado y la norma vigente.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Haces un retiro de $10.000.000 para pagar proveedores. El banco te descuenta GMF (supongamos $40.000, valor inventado solo para ilustrar). El registro:

| Cuenta | Débito | Crédito |
|---|---|---|
| Proveedores (lo que pagas) | $10.000.000 | |
| Gasto GMF (4x1000) | $40.000 | |
| Bancos | | $10.040.000 |

Así el gasto del 4x1000 queda visible como costo de mover el dinero. Las cifras son inventadas; cualquier cálculo del GMF se verifica con `Matematicas_lushows`.

## Errores comunes

- **Confundir rentabilidad con efectivo**: vender mucho a crédito y no tener con qué pagar la nómina.
- **No arquear la caja menor**: el efectivo "se evapora" sin que nadie note el faltante.
- **Olvidar el GMF en las proyecciones**: cada movimiento cuesta y eso reduce la caja real.
- **Mover plata sin soporte**: un movimiento sin documento destruye la auditabilidad.
- **Tener una sola persona que maneja y registra el efectivo sin control**: invita al error y al fraude.

## Conexión con otros módulos

- El flujo de caja proyectado se arma en el módulo **151**.
- Los cobros entran por **152** (cartera) y los pagos salen por **154** (programación de pagos).
- El control contra el banco se hace con la conciliación (**35** básica, **153** avanzada).
- La caja es una cuenta del **plan de cuentas / PUC** (módulo **10**).
- Decisiones estratégicas de capital y excedentes → `economist_lushows`. Cualquier cálculo → `Matematicas_lushows`.

## Siguiente paso típico

Define quién custodia el efectivo, separa el manejo del registro, arquea la caja menor cada semana y proyecta tu flujo de caja (módulo **151**) para no quedarte nunca sin con qué pagar.
