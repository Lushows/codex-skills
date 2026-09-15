# 114 — Impuesto diferido a fondo (NIC 12 / Sección 29)

El impuesto diferido es de los temas que más asustan, pero la idea es simple: **la contabilidad y la DIAN no siempre miden lo mismo en el mismo momento**. A veces un gasto que ya registraste contablemente la DIAN no lo deja deducir todavía; o una utilidad contable la DIAN la grava después. Esas diferencias de TIEMPO se "guardan" como un impuesto que pagarás o ahorrarás más adelante: eso es el **impuesto diferido**. Sirve para que el resultado contable refleje el impuesto que realmente corresponde a esas utilidades, no solo lo que pagas hoy.

En **NIIF plenas** es la **NIC 12**; en **NIIF para pymes** es la **Sección 29**. La mecánica es prácticamente la misma.

Términos: **base contable** = valor del activo/pasivo en tus libros NIIF. **Base fiscal** = valor que le reconoce la DIAN. **Diferencia temporaria** = la resta entre ambas, que se revertirá con el tiempo (≠ diferencia permanente, que nunca se revierte y NO genera diferido).

## Tipos de diferencia y qué generan

| Situación | Genera | Por qué |
|---|---|---|
| Base contable del activo > base fiscal | **Pasivo** por impuesto diferido | Pagarás más impuesto futuro |
| Base contable del activo < base fiscal | **Activo** por impuesto diferido | Pagarás menos impuesto futuro |
| Pérdidas fiscales / excesos de renta presuntiva por compensar | **Activo** por impuesto diferido | Reducen impuesto futuro (si es probable usarlas) |
| Gastos no deducibles nunca (multas, etc.) | Nada (permanente) | No se revierte |

El diferido se calcula multiplicando la diferencia temporaria por la **tarifa de impuesto** que aplicará cuando se revierta (la tarifa de renta vigente en Colombia; no inventes el porcentaje, confírmalo con el estatuto del año).

## Ejemplo completo (cifras ILUSTRATIVAS / inventadas)

GastroLatam deprecia una máquina contablemente en 5 años, pero la DIAN solo le permite depreciar en 10 años. Año 1:
- Depreciación contable: $2.000.000 (costo $10.000.000 / 5).
- Depreciación fiscal aceptada: $1.000.000 ($10.000.000 / 10).
- Base contable del activo al cierre: 10.000.000 − 2.000.000 = **$8.000.000**.
- Base fiscal del activo al cierre: 10.000.000 − 1.000.000 = **$9.000.000**.
- Diferencia temporaria: 9.000.000 − 8.000.000 = **$1.000.000** (la contable es MENOR → **activo** por impuesto diferido).

Con una tarifa supuesta del 35% (verificar tarifa real del año con `Matematicas_lushows`):
- Activo por impuesto diferido = 1.000.000 × 35% = **$350.000**.

| Cuenta | Débito | Crédito |
|---|---|---|
| Activo por impuesto diferido (1710) | 350.000 | |
| Ingreso por impuesto diferido (5405-) | | 350.000 |

Esto significa: contablemente "deduje" más rápido que la DIAN, así que en el futuro la DIAN me dejará deducir esa diferencia y pagaré menos impuesto. Por eso es un activo.

## Errores comunes

- **Confundir temporarias con permanentes**: las multas y gastos no deducibles para siempre NO generan diferido.
- **Usar la tarifa equivocada**: se usa la tarifa que aplicará al revertirse, no necesariamente la de hoy.
- **No reconocer el activo por impuesto diferido sin evidencia de uso futuro**: solo si es probable que habrá utilidades para aprovecharlo.
- **Calcular sobre la utilidad en vez de sobre las diferencias de base**: el diferido nace de bases activo/pasivo, no del resultado.
- **Hacer la cuenta de cabeza**: rutea a `Matematicas_lushows`.

## Conexión con otros módulos

- **111 — NIIF 16**, **113 — Deterioro**: ambos generan diferencias temporarias típicas.
- **30-39** (depreciación): la diferencia entre vida útil contable y fiscal es el caso más común.
- **Matematicas_lushows**: multiplicación por tarifa, conciliación contable-fiscal, formato 2516.
- **Liquidación de renta y formato 2516** (módulos de cumplimiento DIAN): el diferido se concilia allí.

## Siguiente paso típico

Arma una tabla con cada activo/pasivo, su base contable y su base fiscal; las diferencias te dan el diferido. Pásala a `Matematicas_lushows` para multiplicar por la tarifa y verificar. Luego concíliala en el formato 2516.
