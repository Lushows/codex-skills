# 157 — Financiamiento y leasing contable

Cuando el negocio pide plata prestada o adquiere un activo "a cuotas", esa deuda tiene que quedar registrada bien: cuánto debes hoy, cuánto es **capital** (la plata que te prestaron) y cuánto es **interés** (lo que cuesta el préstamo). Registrarlo mal —por ejemplo, meter toda la cuota como gasto— deforma tus estados financieros y tu flujo de caja. Aquí vemos cómo registrar **créditos** y **leasing** de forma auditable. La decisión de *si conviene endeudarse* es de `economist_lushows`; el cálculo de cuotas e intereses se ejecuta en `Matematicas_lushows`.

## Registro de un crédito

Un préstamo entra como **efectivo que recibes** (débito a Bancos) y una **obligación financiera** (crédito, lo que debes). Cada cuota que pagas se parte en dos:

| Parte de la cuota | Qué es | Dónde va |
|---|---|---|
| Abono a capital | Devuelves parte de lo prestado | Reduce la obligación financiera |
| Interés | El costo del préstamo | Es un gasto financiero |

Por eso **la cuota completa NO es gasto**: solo el interés lo es; el abono a capital baja la deuda. La tabla de amortización (que separa cuánto es capital y cuánto interés en cada cuota) se calcula en `Matematicas_lushows`.

## Leasing: financiero vs. operativo

**Leasing** es un contrato en el que usas un activo (un vehículo, una máquina, un local) pagando cuotas a una entidad que es la dueña. Tradicionalmente se distinguía:

| Tipo | Idea de fondo |
|---|---|
| Leasing **financiero** | En el fondo estás *comprando* el activo a cuotas (sueles quedarte con él al final) |
| Leasing **operativo** | Solo lo *alquilas* por un tiempo y lo devuelves |

Bajo **NIIF 16** (la norma de arrendamientos, ver módulo **111**), para el que toma el activo (arrendatario) esta distinción casi desaparece: en la mayoría de los casos se reconoce un **activo por derecho de uso** y un **pasivo por arrendamiento** en el balance, aunque sea un "alquiler". Hay excepciones (contratos cortos o de bajo valor). El detalle NIIF 16 está en el módulo **111**.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Pides un crédito de $10.000.000 (cifras inventadas). Al recibirlo:

| Cuenta | Débito | Crédito |
|---|---|---|
| Bancos | $10.000.000 | |
| Obligaciones financieras | | $10.000.000 |

Pagas la primera cuota de $1.200.000, de la cual $1.000.000 es capital y $200.000 interés:

| Cuenta | Débito | Crédito |
|---|---|---|
| Obligaciones financieras (capital) | $1.000.000 | |
| Gasto por intereses | $200.000 | |
| Bancos | | $1.200.000 |

Cifras inventadas; la separación capital/interés de cada cuota se obtiene de la tabla de amortización calculada en `Matematicas_lushows`.

## Errores comunes

- **Registrar la cuota completa como gasto**: infla gastos y oculta cuánto debes todavía.
- **No separar capital de interés**: imposible saber el saldo real de la deuda.
- **Ignorar NIIF 16** y dejar un leasing "fuera del balance" cuando debe reconocerse.
- **Olvidar el GMF y seguros** asociados al crédito al proyectar la caja (**151**).
- **Calcular cuotas e intereses de cabeza**: siempre a `Matematicas_lushows`.

## Conexión con otros módulos

- El tratamiento NIIF 16 de arrendamientos está en el módulo **111**.
- Las cuotas son salidas en el flujo de caja proyectado (**151**) y se programan en pagos (**154**).
- La obligación financiera aparece en el estado de situación financiera (**20**) y los intereses en resultados (**21**).
- La decisión de endeudarse y la estructura de capital → `economist_lushows`; tablas de amortización e intereses → `Matematicas_lushows`.

## Siguiente paso típico

Registra el crédito como obligación financiera, pide la tabla de amortización para separar capital de interés en cada cuota, revisa si tu leasing cae bajo NIIF 16 (módulo **111**) y conecta las cuotas al flujo de caja (**151**).
