# 195 — Casos resueltos paso a paso

La teoría se entiende de verdad cuando se ve aplicada de principio a fin. Aquí resolvemos cuatro casos completos que **integran varios módulos** a la vez: registrar un mes, armar estados, liquidar un impuesto y cerrar un negocio pequeño. Todas las cifras son **ILUSTRATIVAS / inventadas** y todo cálculo se ejecuta/verifica en código (a `Matematicas_lushows`) — aquí mostramos la lógica, no la calculadora.

> Estos casos son un mapa de "cómo se conecta todo". Adáptalos a tus cifras reales; NO reemplazan al contador titulado.

## Caso 1 — Registrar un mes completo de una cafetería (cifras ILUSTRATIVAS)

**Operaciones del mes:**
1. Venta de contado $5.000.000 + IVA. 2. Compra de café a crédito $1.500.000 + IVA. 3. Pago de arriendo $1.200.000. 4. Pago de nómina $2.000.000.

**Asientos (partida doble, módulos 11–13):**

| # | Cuenta | Débito | Crédito |
|---|---|---|---|
| 1 | Caja | 5.950.000 | |
| 1 | Ingresos por ventas | | 5.000.000 |
| 1 | IVA generado | | 950.000 |
| 2 | Inventario / Compras | 1.500.000 | |
| 2 | IVA descontable | 285.000 | |
| 2 | Proveedores | | 1.785.000 |
| 3 | Gasto arriendo | 1.200.000 | |
| 3 | Banco | | 1.200.000 |
| 4 | Gasto nómina | 2.000.000 | |
| 4 | Banco | | 2.000.000 |

Cierre del mes: el balance de comprobación (módulo 15) debe **cuadrar** (débitos = créditos). El IVA por pagar = 950.000 − 285.000 = **665.000** (módulo 41).

## Caso 2 — Armar estados financieros del mes

Con los saldos del Caso 1 (más saldos iniciales):

- **Estado de resultados** (módulo 21): Ingresos 5.000.000 − (costo café + arriendo + nómina) = utilidad del mes.
- **Estado de situación financiera** (módulo 20): Caja, inventario, proveedores, IVA por pagar, patrimonio.
- **Verificación**: Activo = Pasivo + Patrimonio (ecuación contable, módulo 02). Si no cuadra, hay un error de registro (módulo 19) — no se sigue hasta cuadrar.

## Caso 3 — Liquidar el IVA del bimestre (cifras ILUSTRATIVAS)

| Concepto | Valor |
|---|---|
| IVA generado (ventas) | 950.000 |
| (−) IVA descontable (compras) | 285.000 |
| **IVA a pagar** | **665.000** |

Se declara y paga en el plazo del calendario tributario (módulo 46 — verifica las fechas del año). Si se paga tarde, hay sanción e intereses (módulos 49, 68). El neto se **ejecuta en código**.

## Caso 4 — Cierre anual de una microempresa

1. Conciliar bancos e inventario (módulos 35, 76). 2. Depreciar activos (módulo 32). 3. Provisionar prestaciones (módulo 52). 4. Balance de comprobación ajustado cuadra (módulo 15). 5. Cerrar cuentas de resultado y trasladar utilidad (módulo 18). 6. Armar estados financieros (Bloque 2). 7. Conciliación fiscal / Formato 2516 (módulo 191). 8. Archivar soportes (módulo 97).

Resultado: estados financieros confiables + base fiscal lista + todo soportado = la promesa CUADRE + CUMPLIMIENTO + AUDITABLE cumplida.

## Errores comunes

- **Seguir adelante sin que cuadre** el balance de comprobación.
- **Olvidar el IVA** al registrar ventas y compras (los asientos quedan incompletos).
- **Mezclar lo del mes con lo del año** sin cerrar primero.
- **Resolver montos de cabeza** en vez de en código.

## Conexión con otros módulos

- **Bloque 1** — registro y partida doble (Casos 1 y 2).
- **Bloque 2** — estados financieros (Caso 2).
- **Bloque 4** — IVA y demás impuestos (Caso 3).
- **Módulo 190** — cierre anual (Caso 4).
- **Matematicas_lushows** EJECUTA todos los netos y totales.

## Siguiente paso típico

Toma TUS cifras reales y replica el caso más parecido a tu situación. Luego pásalo por el **módulo 198** (checklist de calidad). Esto NO reemplaza al contador titulado que firma.
