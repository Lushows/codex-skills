# 52 — Prestaciones sociales: prima, cesantías, intereses y vacaciones

Las **prestaciones sociales** son pagos adicionales al salario que la ley obliga al empleador a reconocerle al trabajador. No son un "bono" ni un favor: son un derecho que se va **causando** mes a mes aunque se paguen en fechas concretas del año. Por eso la contabilidad las **provisiona** (las va reconociendo poco a poco) y no espera a pagarlas de golpe.

Este módulo explica qué es cada prestación y cómo se causa. El cálculo de cada valor se ejecuta en `Matematicas_lushows`; los porcentajes de abajo son estructurales del sistema laboral colombiano.

## Términos que debes conocer
- **Prestación social:** pago obligatorio adicional al salario (prima, cesantías, intereses, vacaciones).
- **Causar:** reconocer contablemente el gasto en el periodo en que se genera, aunque se pague después.
- **Base de prestaciones:** el salario más el auxilio de transporte (para prima y cesantías).
- **Salario base de vacaciones:** el salario, **sin** auxilio de transporte.

## Las cuatro prestaciones
| Prestación | Para qué es | Cuánto (estructural) | Cuándo se paga |
|---|---|---|---|
| Prima de servicios | Repartir utilidades del trabajo | ~1 mes de salario al año (8,33% mensual) | Mitad de año y fin de año |
| Cesantías | Ahorro para cuando termine el empleo | ~1 mes de salario al año (8,33% mensual) | Se consignan al fondo en febrero |
| Intereses a las cesantías | Rendimiento sobre las cesantías | 12% anual sobre la cesantía (1% mensual) | Hasta enero del año siguiente |
| Vacaciones | Descanso remunerado | 15 días hábiles por año (4,17% mensual) | Cuando se toman o se liquidan |

> La prima y las cesantías usan como base el salario **+ auxilio de transporte**. Las vacaciones usan el salario **sin** auxilio. Esta diferencia es fuente típica de errores.

## Cómo se causan mes a mes
Cada mes la empresa reconoce un pedacito de cada prestación como gasto y como pasivo (algo que debe). Esa es la **provisión** (módulo 58). Así, cuando llega la fecha de pago, el dinero ya está reconocido y el resultado de cada mes refleja el costo real.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
"Ferretería El Tornillo", empleado con base de prestaciones de $1.700.000 (sueldo $1.500.000 + auxilio $200.000):
- Prima del mes: 8,33% × $1.700.000 ≈ $141.610.
- Cesantías del mes: 8,33% × $1.700.000 ≈ $141.610.
- Intereses del mes: 1% × cesantía acumulada (aprox.).
- Vacaciones del mes: 4,17% × $1.500.000 (sin auxilio) ≈ $62.550.

(Cifras ILUSTRATIVAS; los porcentajes se aplican y verifican en código, y la base puede variar con extras y comisiones.)

## Errores comunes
- Incluir el auxilio de transporte en la base de **vacaciones** (no va ahí; sí en prima y cesantías).
- No provisionar y "llevarse el susto" cuando llega diciembre o febrero.
- Olvidar los **intereses a las cesantías** (es una cuarta obligación, no parte de la cesantía).
- Calcular sobre el sueldo "limpio" cuando hay comisiones/extras que también forman base.

## Conexión con otros módulos
- **50** y **51** — la nómina del periodo y sus devengados.
- **58** — el asiento mes a mes de la provisión de estas prestaciones.
- **55** — al terminar el contrato, estas prestaciones se liquidan en la liquidación final.
- **57** — las prestaciones son una parte grande del costo real del empleado.
- **130-139** — bases, salario integral y casos especiales (laboral 2026 a fondo).
- **Matematicas_lushows** — todos los porcentajes y bases se calculan allí.

## Siguiente paso típico
Ir al módulo **58** para registrar la provisión mensual de estas prestaciones, o al **55** cuando se termina un contrato y hay que liquidarlas.
