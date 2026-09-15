# 132 — Horas extra y recargos: cómo se pagan

Cuando un trabajador labora más de su jornada, de noche, o en domingo/festivo, la ley exige pagar **más** que la hora normal. Eso es el **recargo**. Liquidarlo mal —de menos— es de las cosas que más demandas y reparos de la UGPP genera; pagarlo de más sale caro sin necesidad.

Este módulo explica los tipos de recargo y la lógica del cálculo. Los **números exactos** siempre se ejecutan en `Matematicas_lushows`: nunca de cabeza.

## Términos que debes conocer
- **Hora ordinaria:** valor de una hora dentro de la jornada normal (salario mensual ÷ horas del mes, según el tope vigente — ver módulo 131).
- **Hora extra:** la trabajada por encima de la jornada máxima legal.
- **Recargo:** porcentaje **adicional** que se paga sobre la hora ordinaria.
- **Trabajo nocturno:** el realizado en la franja horaria que la ley define como noche (verifica la franja vigente).
- **Dominical/festivo:** trabajo en día de descanso obligatorio.

## Tipos de recargo (porcentajes referenciales — verifica los vigentes)
| Concepto | Recargo aproximado sobre la hora ordinaria |
|---|---|
| Recargo nocturno (sin ser extra) | + porcentaje sobre la hora ordinaria |
| Hora extra diurna | + 25% |
| Hora extra nocturna | + 75% |
| Trabajo dominical/festivo | + 75% (más el descanso compensatorio o pago) |
| Hora extra diurna en dominical/festivo | recargo dominical **acumulado** con el de extra |
| Hora extra nocturna en dominical/festivo | el más alto: acumula nocturno + dominical |

> Los porcentajes pueden ajustarse por reformas. **Verifica los valores y franjas vigentes del año** antes de liquidar.

## La lógica del cálculo (paso a paso)
1. Calcular el **valor de la hora ordinaria** con el tope de jornada vigente (módulo 131).
2. Identificar **qué tipo** de hora es cada una (diurna/nocturna, ordinaria/festiva).
3. Aplicar el **recargo** correspondiente a cada hora.
4. Cuando se cruzan condiciones (extra + nocturna + festiva), los recargos se **acumulan**.
5. Ejecutar todo en `Matematicas_lushows` y dejar el detalle por tipo de hora.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
"Pizzería Don Tomás": un cocinero trabaja 3 horas extra un domingo en la noche.
- Esas horas son **extra + nocturnas + dominicales** a la vez.
- Se acumulan los recargos correspondientes sobre su hora ordinaria.
- El valor por hora resulta bastante mayor que una hora normal. (Porcentajes y total: a `Matematicas_lushows` con los valores vigentes.)

## Errores comunes
- Calcular el valor hora con **48 horas** cuando el tope ya bajó (módulo 131): toda la liquidación queda mal.
- No **acumular** recargos cuando se cruzan extra, nocturno y festivo.
- Confundir **recargo nocturno** (jornada normal de noche) con **hora extra nocturna**.
- Pagar las extras "por fuera" sin reportarlas: la UGPP las suma al IBC y sanciona (módulo 135).

## Conexión con otros módulos
- **131** — la jornada vigente que define qué es extra y el valor hora.
- **51** — devengados y deducciones donde entran las extras.
- **135** — la UGPP revisa que las extras estén en el IBC.
- **139** — extras no pagadas pueden disparar sanción y demanda.
- **Matematicas_lushows** — ejecuta y verifica cada recargo.

## Siguiente paso típico
Liquidar las horas extra del periodo en `Matematicas_lushows`, incluirlas en el devengado del trabajador y en el IBC de la PILA (módulo 54).
