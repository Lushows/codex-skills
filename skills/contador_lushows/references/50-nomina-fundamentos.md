# 50 — Nómina: fundamentos

La **nómina** es el proceso por el cual una empresa le paga a sus empleados y, al hacerlo, cumple con todo lo que la ley le exige alrededor de ese pago: seguridad social, prestaciones, parafiscales e impuestos. No es solo "pasar el sueldo": es el conjunto de obligaciones que nacen cuando alguien trabaja para ti bajo un contrato laboral.

Este módulo abre el bloque de nómina. Aquí entiendes las piezas; el cálculo fino de cada concepto se reparte en los módulos 51 a 59, y la liquidación numérica siempre se ejecuta en código (vía `Matematicas_lushows`), nunca de cabeza.

> **Regla de oro del bloque:** el **SMMLV** (salario mínimo mensual legal vigente), el **auxilio de transporte** y los **topes** de cotización **cambian cada año** (el Gobierno los fija en diciembre para el año siguiente). Aquí explicamos el CONCEPTO y los porcentajes estructurales del sistema; cuando necesites un valor exacto, **verifica los valores vigentes del año** (SMMLV, auxilio, UVT, topes) antes de liquidar.

## Términos que debes conocer
- **SMMLV:** salario mínimo mensual legal vigente. Muchos límites se miden en SMMLV. *Verifica el valor del año.*
- **Salario:** la remuneración por el trabajo. Puede ser fijo (sueldo mensual) o variable (comisiones, destajo).
- **Auxilio de transporte:** un auxilio que la ley obliga a pagar a quienes ganan hasta cierto tope (alrededor de 2 SMMLV). No es salario, pero sí se suma a la base de prestaciones. *Verifica el valor y el tope del año.*
- **IBC (Ingreso Base de Cotización):** la base sobre la cual se calculan los aportes a seguridad social.
- **Periodo de nómina:** cada cuánto se paga (mensual, quincenal, semanal).

## Qué compone una nómina (las grandes piezas)
| Pieza | Qué es | Quién la asume | Módulo |
|---|---|---|---|
| Devengado | Lo que el empleado gana (sueldo + extras + auxilio) | — | 51 |
| Deducciones | Lo que se le descarga al empleado (su parte de salud y pensión, retención, etc.) | Empleado | 51 |
| Neto a pagar | Devengado menos deducciones | — | 51 |
| Seguridad social | Salud, pensión, ARL | Empleador y empleado | 53 |
| Parafiscales | SENA, ICBF, caja de compensación | Empleador | 53 |
| Prestaciones sociales | Prima, cesantías, intereses, vacaciones | Empleador | 52 |

## Salario vs. pagos NO salariales
No todo lo que recibe el trabajador es "salario". Esta distinción es crítica porque el salario es la base de prestaciones y aportes.
- **Salario:** sueldo, comisiones, horas extra, recargos. Forma base de prestaciones y seguridad social.
- **No salarial:** auxilio de transporte, algunos auxilios de alimentación o conectividad pactados como no constitutivos de salario, viáticos ocasionales. *Ojo:* hay límites legales para pactar pagos como "no salariales"; un mal pacto se vuelve sanción en una visita de la UGPP (ver módulo 130-139).

## Periodicidad
La empresa decide cómo paga (mensual, quincenal), pero **causa** la obligación cuando el trabajo ocurre. Aunque pagues quincenal, las prestaciones y aportes se calculan sobre el mes y se reportan según su propio calendario.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
"Panadería La Espiga", un empleado con sueldo de $1.500.000 al mes:
- Devengado: $1.500.000 + auxilio de transporte (si aplica por estar bajo el tope).
- Deducciones: su 4% de salud + 4% de pensión.
- Neto a pagar: lo que recibe en el banco.
- Además, la panadería asume aparte: su parte de salud/pensión/ARL, parafiscales y la provisión de prestaciones.

El sueldo "cuesta" mucho más que el sueldo: ese costo real se ve en el módulo 57.

## Errores comunes
- Creer que "la nómina es el sueldo" e ignorar el costo del empleador (módulo 57).
- Pactar pagos "no salariales" sin respetar los límites legales (riesgo UGPP).
- Asumir el SMMLV o el auxilio "de memoria": **cambian cada año**.
- No causar la nómina contablemente y solo registrar el pago en el banco (rompe el cuadre y la provisión).

## Conexión con otros módulos
- **51** — devengados, deducciones y neto a pagar en detalle.
- **52** — prestaciones sociales.
- **53** — seguridad social y parafiscales.
- **57** — el costo real del empleado.
- **58** — cómo provisionar las prestaciones mes a mes.
- **130-139** — el detalle laboral 2026 (jornada 42h, tipos de contrato, UGPP a fondo).
- **Matematicas_lushows** — toda liquidación de nómina.
- **economist_lushows** — decidir a quién contratar y bajo qué figura se decide allá; aquí se registra y se cumple.

## Siguiente paso típico
Ir al módulo **51** para armar la liquidación de un periodo: qué se devenga, qué se deduce y cuánto recibe el empleado.
