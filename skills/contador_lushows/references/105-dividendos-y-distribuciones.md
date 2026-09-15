# 105 — Dividendos y distribuciones

Cuando una empresa gana plata, esa utilidad puede quedarse adentro (reinvertirse) o **repartirse entre los socios**. Ese reparto se llama **dividendo** (en una SAS también se les dice "distribución de utilidades"). Aquí aparece un punto que confunde a muchos dueños: la **empresa ya pagó renta** sobre esa utilidad, pero cuando esa misma plata pasa al **bolsillo del socio**, puede volver a tener un impuesto. No es "doble cobro injusto": la ley distingue la utilidad **que ya tributó** en la empresa de la que **no tributó**, y las grava distinto.

Este módulo da el **concepto** de cómo tributan los dividendos. La renta de la empresa vive en el módulo **42**; aquí vemos qué pasa **al repartir** y la retención asociada.

## Conceptos clave (despacio)
- **Dividendo / distribución:** la parte de las utilidades que la empresa entrega a cada socio.
- **Utilidad ya gravada:** la parte de la utilidad sobre la que **la empresa ya pagó renta**.
- **Utilidad no gravada en cabeza de la empresa:** la parte que **no pagó** renta en la sociedad y que, por eso, puede tributar más fuerte en el socio.
- **Retención sobre dividendos:** un porcentaje que se descuenta al pagar el dividendo y se entrega a la DIAN.
- **Socio residente vs. no residente:** las reglas y tarifas cambian según dónde resida el socio.

## Cómo tributa (concepto general)
```
Utilidad de la empresa
  → la empresa paga RENTA (tarifa de sociedades)
  → al repartir el dividendo al socio:
       - parte ya gravada en la empresa → tarifa de dividendos (suele tener tramo exento + tarifa)
       - parte NO gravada en la empresa → tributa más fuerte en el socio
```
La tarifa exacta, los tramos y la retención **dependen de la ley vigente** y de si el socio es persona natural, persona jurídica, residente o no residente. *Verifica las tarifas y tramos vigentes en la DIAN.*

## Quién retiene y declara
| Quién | Qué hace |
|---|---|
| **La empresa que paga** | Practica la **retención** sobre el dividendo y la declara |
| **El socio que recibe** | Incluye el dividendo en su declaración; la retención es un anticipo de su impuesto |

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
Una SAS reparte dividendos a un socio persona natural residente.
- Dividendo de utilidad ya gravada: **$50.000.000** (inventado).
- Tramo exento ilustrativo: primeros **$10.000.000** sin impuesto.
- Sobre los **$40.000.000** restantes, tarifa ilustrativa 10%: **$4.000.000** (inventado) de impuesto/retención.

> Tramos y tarifas 100% ilustrativos. El cálculo real va a `Matematicas_lushows` con los valores vigentes y según el tipo de socio.

## Errores comunes
- Creer que "como la empresa ya pagó renta, el dividendo no tributa nada": depende de los tramos y de la parte gravada/no gravada.
- No practicar la **retención** al repartir (la empresa queda responsable).
- Confundir el reparto de **dividendos** con el **salario** del socio que trabaja en la empresa (son cosas distintas y tributan distinto).
- Repartir utilidades sin acta y sin que estén **realmente disponibles** (problema societario y contable).
- Aplicar tarifas de residentes a un socio **no residente** (cambian).

## Conexión con otros módulos
- **42 (Renta)** — la renta que paga la empresa antes de repartir.
- **43 (Retención en la fuente)** — la retención sobre dividendos es un tipo de retención.
- **39 (Patrimonio y aportes)** — el patrimonio y las utilidades retenidas que se reparten.
- **100** — planear el momento del reparto es legal; simular gastos para no repartir, no.
- **economist_lushows** — decidir cuánto reinvertir vs. repartir; **Matematicas_lushows** — el cálculo.

## Siguiente paso típico
Determinar qué parte de la utilidad ya fue gravada en la empresa, aplicar la tarifa y retención vigentes según el tipo de socio, dejar el **acta** de distribución y declarar la retención. Calcular en `Matematicas_lushows` y confirmar con el contador titulado, sobre todo con socios no residentes.
