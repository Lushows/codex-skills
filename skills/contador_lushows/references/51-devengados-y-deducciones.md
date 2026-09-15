# 51 — Devengados y deducciones: del sueldo al neto a pagar

Cada periodo de nómina se arma con una resta sencilla de entender pero llena de detalles: **lo que el empleado gana (devengado) menos lo que se le descuenta (deducciones) = lo que recibe en el banco (neto a pagar)**. Este módulo explica qué entra en cada lado y cómo se registra.

Aquí no inventamos tarifas ni valores: explicamos la mecánica. Los porcentajes de salud y pensión del empleado son estructurales del sistema y los vemos abajo; los valores en pesos (SMMLV, auxilio) se verifican cada año, y el cálculo se ejecuta en `Matematicas_lushows`.

## Términos que debes conocer
- **Devengado:** todo lo que el empleado gana en el periodo.
- **Deducción:** todo lo que legalmente se le descuenta de ese devengado.
- **Neto a pagar:** devengado − deducciones. Es lo que efectivamente se le consigna.
- **IBC (Ingreso Base de Cotización):** base para calcular salud y pensión. El auxilio de transporte **no** entra en el IBC.

## Lado izquierdo: devengados
| Concepto | ¿Es salario? | ¿Entra al IBC? |
|---|---|---|
| Sueldo básico | Sí | Sí |
| Horas extra y recargos | Sí | Sí |
| Comisiones | Sí | Sí |
| Auxilio de transporte | No | No |
| Auxilios no salariales pactados | No | No (con límites) |

## Lado derecho: deducciones
| Concepto | Tarifa estructural | A cargo de |
|---|---|---|
| Salud (parte empleado) | 4% del IBC | Empleado |
| Pensión (parte empleado) | 4% del IBC | Empleado |
| Fondo de Solidaridad Pensional | % adicional si el salario supera cierto tope en SMMLV | Empleado |
| Retención en la fuente por salarios | Según procedimiento y UVT del año | Empleado |
| Otras (préstamos, embargos, libranzas) | Según el caso, con límites legales | Empleado |

> Las partes del empleador (su parte de salud, pensión, ARL, parafiscales) **no** son deducciones del empleado: son costo de la empresa y van en el módulo 53 y 57.

## Asiento contable de la nómina (causación)
La empresa **causa** el gasto y reconoce lo que debe pagar. Ejemplo de la estructura (partida doble que cuadra):

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto de sueldos (devengado) | 1.500.000 | |
| Salud por pagar (parte empleado, 4%) | | 60.000 |
| Pensión por pagar (parte empleado, 4%) | | 60.000 |
| Salarios por pagar (neto al empleado) | | 1.380.000 |
| **Sumas** | **1.500.000** | **1.500.000** |

(Cifras ILUSTRATIVAS; el IBC, los topes y la retención se verifican y se calculan en código.)

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
"Café Aurora", empleada con sueldo de $1.500.000, sin horas extra:
- Devengado salarial (IBC): $1.500.000.
- Salud empleado 4%: $60.000. Pensión empleado 4%: $60.000.
- Si está bajo el tope de retención, no se le retiene.
- Neto a pagar = $1.500.000 − $120.000 = **$1.380.000**.
- Si le corresponde auxilio de transporte, se le suma al neto (pero no al IBC).

## Errores comunes
- Meter el **auxilio de transporte en el IBC** (no va; sí va a la base de prestaciones).
- Confundir la parte del empleado (deducción) con la del empleador (costo).
- Calcular salud/pensión sobre el devengado total en vez de sobre el IBC.
- No retener cuando el salario supera el umbral, o retener "a ojo" sin el procedimiento de la DIAN.

## Conexión con otros módulos
- **50** — qué compone la nómina (visión general).
- **53** — los aportes del empleado y del empleador en detalle.
- **52** y **58** — las prestaciones que se causan aparte y su provisión.
- **57** — el costo total del empleado para la empresa.
- **43 (Retención en la fuente)** — la retención por salarios se conecta con el marco tributario.
- **Matematicas_lushows** — IBC, deducciones y retención se calculan allí con `decimal`.

## Siguiente paso típico
Una vez liquidado el neto del periodo, ir al módulo **53** para los aportes a seguridad social y parafiscales, y al **58** para provisionar las prestaciones.
