# 17 — Devengo vs. caja: cuándo "cuenta" un peso

Esta es una de las ideas más importantes —y más malentendidas— de la contabilidad. La pregunta es simple: **¿cuándo registro un ingreso o un gasto, cuando ocurre el hecho o cuando entra/sale la plata?** Hay dos formas de responder y dan resultados muy distintos.

> **Base de caja** = registras cuando el **dinero** se mueve (entra o sale).
> **Base de devengo (o causación)** = registras cuando **ocurre el hecho** que lo genera, sin importar cuándo se paga.

## La diferencia en una frase

- **Caja:** "lo cuento cuando me pagan / cuando pago".
- **Devengo:** "lo cuento cuando lo gané / cuando lo causé, aunque me paguen después".

La contabilidad formal en Colombia, bajo **NIIF**, se lleva por **devengo**. La base de caja se usa para mirar **liquidez** (flujo de efectivo) y para algunos regímenes muy simples.

## Por qué importa (el mismo negocio se ve distinto)

Un negocio puede tener **utilidad** por devengo y estar **sin plata** en caja (vendió a crédito), o tener mucha plata y estar perdiendo (cobró anticipos que aún debe entregar). Confundir las dos bases lleva a decisiones malas.

## El mismo hecho en ambas bases (cifras ILUSTRATIVAS / inventadas)

**Hecho:** el 28 de marzo entregas un servicio por $1.000.000. El cliente te paga el 15 de abril.

### Base de devengo (lo correcto en NIIF)

Marzo — reconoces el ingreso al entregar:

| Cuenta | Débito | Crédito |
|---|---|---|
| Clientes / CxC (1305) | 1.000.000 | |
| Ingresos por servicios (4140) | | 1.000.000 |
| **Totales** | **1.000.000** | **1.000.000** |

Abril — cuando te pagan, NO hay ingreso nuevo, solo cambia un activo por otro:

| Cuenta | Débito | Crédito |
|---|---|---|
| Bancos (1110) | 1.000.000 | |
| Clientes / CxC (1305) | | 1.000.000 |
| **Totales** | **1.000.000** | **1.000.000** |

> El **ingreso** se reconoció en **marzo** (cuando se ganó), no en abril (cuando se cobró).

### Base de caja

No pasa nada en marzo. Todo el ingreso se registra en **abril**, al recibir el dinero. El esfuerzo de marzo queda "invisible" hasta que pagan.

## Tabla comparativa

| Aspecto | Base de caja | Base de devengo |
|---|---|---|
| Cuándo registra | Al mover el dinero | Al ocurrir el hecho |
| Refleja | Liquidez | Resultado real del período |
| Ventas a crédito | Se ven tarde | Se ven al vender |
| Exigida por NIIF | No (salvo flujo de efectivo) | Sí |
| Riesgo | Subestima esfuerzo del período | Puede mostrar utilidad sin caja |

## Cuándo usar cada una

- **Devengo:** estados financieros, declaraciones, ver la rentabilidad real.
- **Caja:** flujo de efectivo, saber si te alcanza la plata este mes, negocios muy pequeños o de control interno.

Lo ideal: llevas devengo y **además** miras el flujo de caja. Son lentes complementarios, no rivales.

## Errores comunes

- **Pensar que vender = tener plata.** Vendiste a crédito: hay ingreso, no hay caja.
- **Registrar un anticipo como ingreso.** Si cobraste antes de entregar, es un **pasivo** hasta que cumplas.
- **Mezclar las dos bases** en el mismo informe sin avisar.
- **Decidir gastos grandes mirando solo la utilidad** sin revisar la caja.

## Conexión con otros módulos

- **Módulo 16** — los asientos de ajuste existen precisamente para aplicar el devengo.
- **Módulo 12** — cada uno de estos hechos es un asiento.
- **economist_lushows** DECIDE con estos números (rentabilidad vs. liquidez); el contador los REGISTRA bien.

## Siguiente paso típico

Ve al **módulo 18**: cómo cerrar el período una vez todo está causado y ajustado.
