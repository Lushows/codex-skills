# 191 — Conciliación fiscal y Formato 2516

La contabilidad y los impuestos no siempre cuentan la misma historia. Tu contabilidad sigue las **NIIF** (las normas internacionales de información financiera), pero la **DIAN** tiene sus propias reglas para calcular la renta. La **conciliación fiscal** es el puente entre ambas: explica, peso por peso, por qué la utilidad contable y la utilidad fiscal son distintas. En Colombia ese puente se reporta en el **Formato 2516**.

> **Conciliación fiscal** = documento que parte de la utilidad contable (NIIF) y, sumando o restando diferencias, llega a la renta líquida fiscal (la base sobre la que se paga el impuesto de renta). El **Formato 2516** es el reporte oficial de esa conciliación ante la DIAN.

## ¿Por qué difieren lo contable y lo fiscal?

Porque cada marco persigue un objetivo distinto: la contabilidad busca mostrar la **realidad económica** al dueño; el fisco busca calcular un **impuesto** con reglas propias (a veces más estrictas, a veces con beneficios).

| Concepto | Contable (NIIF) | Fiscal (DIAN) |
|---|---|---|
| Depreciación | Vida útil real del activo | Tasas máximas que fija la norma |
| Provisiones / estimaciones | Se reconocen al estimarlas | Muchas solo se aceptan al realizarse |
| Gastos sin soporte válido | Pueden estar en libros | NO son deducibles |
| Ingresos | Por devengo (módulo 17) | Reglas fiscales específicas |

## Tipos de diferencias

- **Diferencias permanentes**: nunca se igualan (ej. un gasto que la contabilidad acepta pero el fisco rechaza para siempre, como una multa).
- **Diferencias temporarias**: se igualan con el tiempo (ej. depreciación que se reconoce más rápido en un marco que en el otro). Estas generan el **impuesto diferido** (módulo 48).

## ¿Quién presenta el Formato 2516?

A grandes rasgos, los **obligados a llevar contabilidad** que superan ciertos topes de ingresos o patrimonio deben presentarlo junto con la declaración de renta. Los topes y la obligación **cambian cada año** — verifica el valor del año en la normativa vigente y en el módulo 199 (changelog). Quien no esté obligado igual debe tener la conciliación como **soporte interno**.

## Cómo se arma (estructura general)

1. Parte de la **utilidad contable** del estado de resultados (Bloque 2).
2. **Suma** los gastos contables que el fisco NO acepta (no deducibles).
3. **Resta** ingresos contables que el fisco no grava o que ya tributaron.
4. Ajusta por **diferencias en depreciación, provisiones e inventarios**.
5. Llega a la **renta líquida fiscal** → base del impuesto (módulo 42).
6. Documenta cada diferencia con su soporte (promesa AUDITABLE).

## Ejemplo de conciliación (cifras ILUSTRATIVAS / inventadas)

| Concepto | Valor |
|---|---|
| Utilidad contable (NIIF) | 100.000 |
| (+) Multa de tránsito (no deducible) | 3.000 |
| (+) Provisión de cartera no aceptada aún | 5.000 |
| (+) Exceso de depreciación contable vs. fiscal | 2.000 |
| (−) Ingreso no gravado | 1.000 |
| **= Renta líquida fiscal** | **109.000** |

Sobre los $109.000 (no sobre los $100.000) se aplica la tarifa de renta del año. La suma y cada ajuste se **ejecutan y verifican en código** (a `Matematicas_lushows`), nunca de cabeza.

## Errores comunes

- **Pensar que utilidad contable = base del impuesto**: casi nunca son iguales.
- **No documentar cada diferencia**: la DIAN puede rechazar el ajuste.
- **Olvidar el impuesto diferido** que generan las diferencias temporarias (módulo 48).
- **Presentar el 2516 con cifras que no atan** con la declaración de renta ni con los estados financieros.
- **Asumir topes de años anteriores**: la obligación cambia; verifica el valor del año.

## Conexión con otros módulos

- **Módulo 190** — el cierre contable produce la utilidad de la que parte la conciliación.
- **Módulo 42** — el impuesto de renta que se calcula sobre la renta líquida fiscal.
- **Módulo 48** — impuesto diferido por diferencias temporarias.
- **Módulo 199** — changelog que avisa si cambian topes o estructura del formato.
- **economist_lushows** DECIDE planeación tributaria; **contador** CONCILIA y REPORTA; **Matematicas_lushows** EJECUTA.

## Siguiente paso típico

Con la renta líquida fiscal lista, pasa al **módulo 42** para liquidar el impuesto de renta y al módulo 47 para presentar la declaración. Esto NO reemplaza al contador titulado que firma.
