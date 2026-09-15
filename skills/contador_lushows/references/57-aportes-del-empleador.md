# 57 — El costo real del empleado: la carga prestacional

Una de las sorpresas más grandes para quien contrata por primera vez es esta: **un empleado cuesta mucho más que su sueldo**. Sobre el salario, el empleador suma su parte de seguridad social, los parafiscales y las prestaciones sociales. Ese "extra" se llama **carga prestacional**, y entenderlo bien es la diferencia entre un negocio que sobrevive y uno que se descapitaliza pagando nómina.

Este módulo arma el costo total de un empleado pieza por pieza. Los porcentajes son estructurales; el cálculo final se ejecuta en `Matematicas_lushows`.

## Términos que debes conocer
- **Carga prestacional:** todo lo que el empleador paga **además** del sueldo neto del empleado.
- **Factor prestacional:** el multiplicador aproximado que dice cuánto cuesta el empleado sobre su salario (suele rondar 1,5x, pero **depende del caso**: salario, riesgo ARL, exoneraciones).
- **Costo total empleador:** salario + aportes de empresa + provisión de prestaciones.

## Las piezas del costo (porcentajes estructurales sobre el salario)
| Concepto | A cargo del empleador |
|---|---|
| Salud (parte empresa) | 8,5% (si no hay exoneración) |
| Pensión (parte empresa) | 12% |
| ARL | 0,522% – 6,96% según clase de riesgo |
| SENA | 2% (si no hay exoneración) |
| ICBF | 3% (si no hay exoneración) |
| Caja de compensación | 4% |
| Prima de servicios | 8,33% |
| Cesantías | 8,33% |
| Intereses a las cesantías | ~1% (12% anual sobre cesantías) |
| Vacaciones | 4,17% |

> Súmalos y verás por qué el factor ronda **1,4x a 1,5x** del salario. **No es un número fijo**: con exoneración baja, con riesgo ARL alto sube. Calcúlalo para el caso concreto.

## Por qué importa
- **Para fijar precios:** si no metes la carga prestacional en tus costos, vendes por debajo del costo real.
- **Para decidir contratar:** a veces conviene un contratista, a veces un empleado (la decisión estratégica se ve con `economist_lushows`; la diferencia legal en el módulo 59).
- **Para el flujo de caja:** la prima y las cesantías llegan en bloque; hay que provisionarlas (módulo 58).

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
"Heladería Polo Norte", empleado con sueldo de $1.500.000, riesgo bajo, **sin** exoneración:
- Salud empresa 8,5%: $127.500
- Pensión empresa 12%: $180.000
- ARL (~0,522%): $7.830
- Parafiscales (2%+3%+4% = 9%): $135.000
- Prestaciones (8,33%+8,33%+~1%+4,17% ≈ 21,83%): $327.450
- **Costo extra ≈ $777.780**, así que el empleado cuesta ≈ **$2.277.780**, no $1.500.000.

(Cifras ILUSTRATIVAS; el factor exacto se calcula en código según el caso.)

## Errores comunes
- Cotizarle al cliente o fijar precios usando solo el **sueldo**, ignorando la carga.
- Asumir el factor "1,5x" como ley: **cambia** con exoneración, riesgo ARL y auxilio.
- Olvidar que la **prima y cesantías** llegan en fechas concretas y descuadran la caja si no se provisionan.
- Confundir el costo del empleado con el costo del contratista (módulo 59).

## Conexión con otros módulos
- **53** — el detalle de los aportes de empresa.
- **52** y **58** — las prestaciones y su provisión mensual.
- **59** — comparar el costo de un empleado contra un contratista.
- **economist_lushows** — la decisión de contratar y la estructura de costos del negocio se decide allá; aquí se cuantifica y se registra.
- **Matematicas_lushows** — el factor prestacional y el costo total se calculan allí.

## Siguiente paso típico
Calcular el costo total real de cada empleado y llevarlo a la estructura de costos del negocio (precios, punto de equilibrio) y a la **provisión mensual** del módulo 58.
