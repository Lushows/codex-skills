# 49 — Sanciones e intereses de mora

Este es el módulo que nadie quiere necesitar, pero todos deben conocer. Cuando una obligación tributaria se incumple —se presenta tarde, con errores, o no se presenta— la DIAN impone una **sanción** (una multa) y, si hubo impuesto dejado de pagar a tiempo, cobra **intereses de mora** (el costo del dinero por pagar tarde). Entender la mecánica sirve para **dos cosas**: evitar caer, y cuando ya se cayó, **autoliquidar la sanción** y corregir antes de que la DIAN actúe (lo que casi siempre sale mucho más barato).

Somos **honestos sobre las sanciones**: no las minimizamos. **No inventamos montos ni tasas:** las sanciones se expresan en UVT (con topes mínimos) y los intereses se calculan con una tasa que **cambia constantemente**. *Verifica la sanción mínima en UVT y la tasa de interés moratorio vigente en la DIAN.*

## Conceptos clave
- **Sanción:** multa por incumplir un deber formal o de pago.
- **Sanción mínima:** ninguna sanción puede ser menor a cierto valor en UVT (verifica el del año).
- **Reducción de la sanción:** si **corriges voluntariamente** (antes de que la DIAN te requiera), la sanción suele reducirse fuertemente. Cuanto antes, menor.
- **Intereses de mora:** se cobran sobre el **impuesto** dejado de pagar (no sobre la sanción), día a día, desde el vencimiento hasta el pago.

## Tipos de sanción más comunes (CONCEPTO)
| Situación | Sanción (concepto) |
|---|---|
| **Extemporaneidad** (presentar tarde) | Un % del impuesto por **cada mes o fracción** de retraso (más antes vs. después de emplazamiento). Verifica el % y el tope. |
| **Corrección** (corriges y aumenta el impuesto) | Un % sobre el mayor valor, menor si la haces voluntariamente. |
| **No declarar** | La más grave: la DIAN puede liquidarte de oficio con sanción alta. |
| **Por inexactitud** | Cuando los datos declarados eran falsos/erróneos y bajaron el impuesto. |
| **Sanciones formales** | Por no facturar, no informar, errores en exógena, etc. |

> **Regla clave:** la extemporaneidad y la corrección crecen **con el tiempo y con la intervención de la DIAN**. Corregir **rápido y voluntariamente** siempre cuesta menos.

## Cómo se arma lo que se paga (mecánica)
```
Total a pagar a la DIAN = Impuesto + Sanción + Intereses de mora

Sanción     = según el tipo (% × meses, etc.), nunca menor a la sanción mínima (UVT)
Intereses   = impuesto × tasa moratoria vigente × tiempo (cálculo diario)
```
El cálculo de intereses es **delicado** (tasa diaria que varía): **siempre** va a `Matematicas_lushows` con `decimal`.

## Ejemplo (cifras / tasas ILUSTRATIVAS / inventadas)
Una declaración de retención con impuesto de **$2.000.000** se presenta **2 meses tarde**:
- Sanción de extemporaneidad **ilustrativa 5% por mes** → 10% × 2.000.000 = **$200.000** (inventado, verifica el %).
- Se compara con la **sanción mínima** (UVT del año): se paga la mayor.
- Intereses de mora: $2.000.000 × tasa diaria vigente × días de retraso → **$X** (se calcula con la tasa real).
- **Total = impuesto + sanción + intereses.**

> Porcentajes, tasas y cifras son de ejemplo. La liquidación real se hace con valores vigentes en **Matematicas_lushows**.

## Importante (la promesa de la casa)
- **No reemplazamos al contador titulado** que firma: en sanciones grandes, no declarar o requerimientos de la DIAN, hay que acudir a él.
- Sé honesto con el cliente: una sanción es real y crece; lo barato es **actuar ya**.
- Documenta todo (la base de cálculo de la sanción e intereses) para que sea **auditable**.

## Errores comunes
- Creer que "si nadie me dice, no pasa nada": los intereses corren **solos**, día a día.
- Olvidar la **sanción mínima** (pagar menos de lo que la ley exige como piso).
- Calcular intereses con una **tasa vieja** (cambia muy seguido).
- Esperar a que la DIAN requiera: pierdes la **reducción** por corrección voluntaria.
- Sumar los intereses sobre la **sanción** (van sobre el **impuesto**).

## Conexión con otros módulos
- **46 (Calendario)** — incumplir la fecha de ahí es lo que dispara estas sanciones.
- **47 (Presentación)** — corregir es presentar de nuevo; aquí se calcula su costo.
- **41, 42, 43, 44** — cualquiera de esos impuestos puede generar sanción.
- **Matematicas_lushows** — el cálculo de sanción e intereses (tasa diaria, decimal).
- **economist_lushows** — decidir la estrategia ante una sanción grande es planeación.

## Siguiente paso típico
Si hay un incumplimiento, no esperar: cuantificar impuesto + sanción + intereses con valores vigentes (vía Matematicas), corregir/presentar por **47** lo antes posible para reducir la sanción, y si el caso es grave o hay requerimiento, escalar al contador titulado.
