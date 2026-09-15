# 196 — Los errores contables más comunes (y cómo corregirlos)

Casi todos los problemas contables vienen de un puñado de errores que se repiten. Conocerlos te permite **prevenirlos** antes de que ocurran y **detectarlos** cuando ya están. Este módulo es un catálogo del "top" de errores, ordenado por dónde se cometen, con la señal que los delata y la forma correcta de corregirlos sin tapar el rastro.

> **Regla de oro de la corrección**: un error nunca se "borra". Se corrige con un **asiento de reversión o ajuste** que deja la huella de qué pasó y por qué (promesa AUDITABLE). Borrar es lo que rompe la confianza de los libros.

## Errores de registro (Bloque 1)

| Error | Señal | Corrección |
|---|---|---|
| Débito ≠ crédito | El balance de comprobación no cuadra (módulo 15) | Encuentra el asiento descuadrado y ajústalo |
| Cuenta equivocada | Saldo raro en una cuenta | Asiento de reclasificación (módulo 19) |
| Doble registro | Una venta/gasto aparece dos veces | Reversar el duplicado |
| Olvidar el IVA | El asiento de venta/compra no incluye IVA | Completar con el IVA generado/descontable |
| Confundir débito y crédito | Saldo con signo invertido | Reversar y volver a registrar |

## Errores de causación y corte (Bloque 1–3)

- **Registrar por caja en vez de por devengo** (módulo 17): se reconoce el ingreso/gasto cuando entra/sale plata, no cuando ocurre. Resultado: utilidad distorsionada.
- **No causar lo del período** (servicios usados y no facturados): faltan gastos en el mes.
- **No depreciar** los activos fijos (módulo 32): la utilidad sale inflada.
- **No provisionar prestaciones** (módulo 52): aparece un "hueco" en diciembre.

## Errores de conciliación y soporte

- **No conciliar bancos** (módulo 35): el saldo en libros no es el real.
- **Registrar sin soporte**: hay un valor pero no hay factura/documento que lo respalde. Rompe AUDITABLE y el fisco lo rechaza.
- **No archivar** lo que sí tiene soporte (módulo 97): existe el papel pero no se encuentra.

## Errores de cálculo

- **Calcular de cabeza** márgenes, IVA, retenciones, depreciación. Toda cifra no trivial se **ejecuta y verifica en código** (a `Matematicas_lushows`).
- **Redondear plata como float**: el dinero con decimales se maneja con precisión (Matematicas_lushows usa decimal, nunca float).

## Ejemplo de corrección bien hecha (cifras ILUSTRATIVAS / inventadas)

Se registró un gasto de arriendo en la cuenta de "servicios públicos" por $1.200.000. Corrección por reclasificación:

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto arriendo (correcta) | 1.200.000 | |
| Gasto servicios públicos (revertir) | | 1.200.000 |

El saldo neto no cambia, pero ahora cada cuenta refleja la realidad y queda la huella del ajuste.

## Errores comunes (meta-errores)

- **Tapar un error borrándolo** en vez de corregirlo con asiento.
- **Dejar errores "para después"**: se acumulan y al cierre son una bola de nieve.
- **No revisar el balance de comprobación** cada mes (es el primer detector).

## Conexión con otros módulos

- **Módulo 19** — errores de registro y su corrección formal.
- **Módulo 15** — el balance de comprobación, primer detector.
- **Módulo 96** — señales de alerta en tus libros.
- **Módulo 198** — checklist de calidad para atrapar errores antes de entregar.
- **Matematicas_lushows** EJECUTA y verifica cualquier número en duda.

## Siguiente paso típico

Convierte este catálogo en parte de tu **checklist mensual** (módulo 93) para que los errores se atrapen temprano. Esto NO reemplaza la revisión del contador titulado.
