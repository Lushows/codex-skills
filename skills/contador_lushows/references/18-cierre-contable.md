# 18 — Cierre contable: terminar un período y empezar otro

Al final del año (o del período que manejes), llega el momento de **cerrar**: calcular cuánto ganó o perdió el negocio, guardarlo en el patrimonio de los dueños, y dejar las cuentas listas para empezar de nuevo. Es como cerrar la caja al final del día, pero a escala del año entero.

> **Cierre contable** = proceso de saldar a cero las cuentas de resultado (ingresos, gastos, costos) y trasladar la utilidad o pérdida al patrimonio, dejando solo las cuentas de balance abiertas.

## Dos tipos de cuentas (clave para entender el cierre)

| Tipo | Clases | ¿Se cierran? | Por qué |
|---|---|---|---|
| **De resultado** (temporales) | 4 Ingresos, 5 Gastos, 6 Costos | **Sí, a cero** | Miden UN período; el próximo año arrancan en cero |
| **De balance** (permanentes) | 1 Activo, 2 Pasivo, 3 Patrimonio | **No** | Su saldo continúa al año siguiente |

Pensalo así: lo que **tienes y debes** (balance) sigue existiendo el 1 de enero. Lo que **ganaste y gastaste** (resultado) es la historia de ese año y se "reinicia".

## Pasos del cierre

1. Termina de **causar y ajustar** todo (módulos 16 y 17).
2. Saca el **balance de comprobación ajustado** (módulo 15): debe cuadrar.
3. **Cierra ingresos, gastos y costos** contra una cuenta de resultado.
4. Traslada la **utilidad o pérdida** al patrimonio.
5. Las cuentas de balance quedan como **saldos de apertura** del nuevo período.

## Ejemplo de cierre (cifras ILUSTRATIVAS / inventadas)

Supongamos que al final del año tienes: Ventas $100.000 (crédito), Arrendamientos $30.000 (débito). Utilidad = 100.000 − 30.000 = **$70.000**.

**Paso 1 — cerrar los ingresos** (las cuentas 4 tienen saldo crédito; para saldarlas se debitan):

| Cuenta | Débito | Crédito |
|---|---|---|
| Ventas (4135) | 100.000 | |
| Ganancias y pérdidas (5905) | | 100.000 |
| **Totales** | **100.000** | **100.000** |

**Paso 2 — cerrar los gastos** (las cuentas 5 tienen saldo débito; se acreditan para saldarlas):

| Cuenta | Débito | Crédito |
|---|---|---|
| Ganancias y pérdidas (5905) | 30.000 | |
| Arrendamientos (5120) | | 30.000 |
| **Totales** | **30.000** | **30.000** |

Ahora "Ganancias y pérdidas" tiene saldo crédito de 70.000 (la utilidad).

**Paso 3 — trasladar la utilidad al patrimonio:**

| Cuenta | Débito | Crédito |
|---|---|---|
| Ganancias y pérdidas (5905) | 70.000 | |
| Utilidad del ejercicio (3605) | | 70.000 |
| **Totales** | **70.000** | **70.000** |

Resultado: las cuentas 4 y 5 quedan en **cero**, y los dueños tienen $70.000 más de patrimonio. Si hubiera dado pérdida, el traslado iría al revés y restaría patrimonio.

## Apertura del nuevo período

El 1 de enero, las cuentas de balance (activos, pasivos, patrimonio) arrancan con el **saldo de cierre** del año anterior. Las de resultado arrancan en **cero**, listas para registrar la nueva película.

## Errores comunes

- **Cerrar sin haber ajustado** (módulos 16-17): la utilidad sale mal.
- **Cerrar cuentas de balance** por error (esas NO se cierran).
- **Calcular la utilidad de cabeza**: ejecútala en código, suma ingresos menos gastos/costos.
- **Olvidar trasladar la pérdida** (también va al patrimonio, restando).

## Conexión con otros módulos

- **Módulos 16-17** — ajustar y causar antes de cerrar.
- **Módulo 15** — el balance ajustado debe cuadrar antes del cierre.
- **Bloque 2** — los estados financieros se arman con estos saldos finales.
- **Matematicas_lushows** EJECUTA la utilidad/pérdida del ejercicio.

## Siguiente paso típico

Con el período cerrado, pasa al **Bloque 2** para armar los estados financieros (balance general, estado de resultados, flujo de efectivo).
