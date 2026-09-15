# 14 — El libro mayor: el saldo de cada cuenta

Si el diario es la **película** (todo en orden de tiempo), el libro mayor es el **álbum de fotos por personaje**: agrupa todos los movimientos de **cada cuenta** y te dice cuánto tiene al final. A pasar del diario al mayor se le llama **mayorizar**.

> **Libro mayor** = un resumen, cuenta por cuenta, donde se acumulan sus débitos y créditos para sacar el **saldo**.

## De dónde sale el saldo

Para cada cuenta:

```
Saldo = total débitos − total créditos   (si es de naturaleza débito)
Saldo = total créditos − total débitos    (si es de naturaleza crédito)
```

Así el saldo de una cuenta **siempre sale positivo** cuando todo está bien. Si una cuenta de activo te da saldo negativo, hay algo que revisar.

## Cómo se mayoriza (cifras ILUSTRATIVAS / inventadas)

Tomamos los tres asientos del módulo 13 y los repartimos por cuenta en formato T.

**Cuenta: Bancos (1110) — Activo, naturaleza débito**

| Débito | Crédito |
|---|---|
| | 30.000 (arriendo) |
| **Saldo** | **−30.000** → cuenta bajó 30.000 |

**Cuenta: Caja (1105) — Activo**

| Débito | Crédito |
|---|---|
| 119.000 (venta) | |
| **Saldo: 119.000 (deudor)** | |

**Cuenta: Ventas (4135) — Ingreso, naturaleza crédito**

| Débito | Crédito |
|---|---|
| | 100.000 |
| **Saldo: 100.000 (acreedor)** | |

**Cuenta: Proveedores (2205) — Pasivo**

| Débito | Crédito |
|---|---|
| | 50.000 |
| **Saldo: 50.000 (acreedor)** | |

(Inventarios queda en 50.000 deudor, IVA generado 19.000 acreedor, Arrendamientos 30.000 deudor.)

## Tabla resumen de saldos (ILUSTRATIVA)

| Cuenta | Naturaleza | Saldo |
|---|---|---|
| Caja | Deudor | 119.000 |
| Bancos | Deudor | −30.000 |
| Inventarios | Deudor | 50.000 |
| Proveedores | Acreedor | 50.000 |
| IVA generado | Acreedor | 19.000 |
| Ventas | Acreedor | 100.000 |
| Arrendamientos | Deudor | 30.000 |

> Estos saldos son la **materia prima** del balance de comprobación (módulo 15) y luego de los estados financieros.

## Para qué te sirve el mayor

- Saber **cuánta plata tienes** (saldo de Caja y Bancos).
- Saber **cuánto debes** (saldo de Proveedores).
- Saber **cuánto vendiste** en el período (saldo de Ventas).
- Detectar saldos raros (un activo en negativo, un gasto enorme).

## Errores comunes

- **No mayorizar a tiempo** y descubrir tarde que un saldo está raro.
- **Sumar mal** los movimientos de una cuenta con muchos asientos (usa código, no la cabeza).
- **Confundir saldo deudor con "deuda"**: un saldo deudor en Caja es plata que tienes, no que debes.
- **Olvidar una cuenta** que sí tuvo movimiento en el diario.

## Conexión con otros módulos

- **Módulo 13** — el mayor se alimenta del diario.
- **Módulo 15** — los saldos del mayor arman el balance de comprobación.
- **Módulo 18** — al cierre, las cuentas 4, 5 y 6 se saldan a cero.
- **Matematicas_lushows** EJECUTA las sumas de cada cuenta con `decimal`, no `float`.

## Siguiente paso típico

Ve al **módulo 15**: poner todos los saldos en una sola tabla y verificar que el total de débitos = total de créditos.
