# 58 — Provisión de nómina: reconocer las prestaciones mes a mes

**Provisionar** significa reconocer hoy un gasto que se pagará después, porque ya se está causando. En nómina esto es clave: la prima se paga en junio y diciembre, las cesantías en febrero, las vacaciones cuando se toman… pero el **derecho del trabajador se gana cada mes**. Si la empresa no provisiona, sus estados financieros mienten (muestran utilidad de más) y la caja revienta cuando llegan los pagos en bloque.

Este módulo enseña el asiento mensual de provisión. Los valores se calculan en `Matematicas_lushows`; aquí está la mecánica contable que **cuadra**.

## Términos que debes conocer
- **Provisión:** pasivo que se reconoce mes a mes por una obligación que se está causando.
- **Pasivo estimado / por pagar:** la cuenta donde se acumula lo que se debe a los trabajadores.
- **Causación:** principio contable de reconocer el gasto cuando se genera, no cuando se paga.

## Qué se provisiona cada mes
| Prestación | % mensual aprox. (estructural) | Base |
|---|---|---|
| Prima de servicios | 8,33% | Salario + auxilio |
| Cesantías | 8,33% | Salario + auxilio |
| Intereses a las cesantías | ~1% | Sobre la cesantía acumulada |
| Vacaciones | 4,17% | Salario sin auxilio |

## El asiento mensual de provisión (cuadra)
Cada mes la empresa registra un **gasto** (lado débito) contra un **pasivo** (lado crédito) por cada prestación. Estructura (cifras ILUSTRATIVAS sobre base $1.700.000):

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto prima de servicios | 141.610 | |
| Gasto cesantías | 141.610 | |
| Gasto intereses a cesantías | 1.416 | |
| Gasto vacaciones (base sin auxilio) | 62.550 | |
| Prima por pagar | | 141.610 |
| Cesantías por pagar | | 141.610 |
| Intereses a cesantías por pagar | | 1.416 |
| Vacaciones por pagar | | 62.550 |
| **Sumas** | **347.186** | **347.186** |

## Y cuando llega el pago…
Cuando efectivamente se paga la prestación, **no** se vuelve a registrar gasto: se **cancela el pasivo** acumulado. Ejemplo al pagar la prima:

| Cuenta | Débito | Crédito |
|---|---|---|
| Prima por pagar (lo provisionado) | 849.660 | |
| Bancos | | 849.660 |
| **Sumas** | **849.660** | **849.660** |

(Si la provisión quedó corta o sobrada, se ajusta el gasto del mes; por eso se revisa periódicamente.)

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
"Librería El Saber" provisiona cada mes $347.186 por su única empleada. Al llegar junio, ya tiene acumulada la prima de 6 meses (~$849.660) y la paga **sin afectar el resultado de junio**, porque el gasto ya se fue reconociendo. Su utilidad mensual fue siempre realista.

## Errores comunes
- **No provisionar** y registrar el gasto completo solo en junio/diciembre/febrero (distorsiona resultados y caja).
- Volver a registrar **gasto** al pagar (doble gasto): el pago solo cancela el pasivo.
- Provisionar vacaciones con auxilio incluido (su base es **sin** auxilio).
- No **ajustar** la provisión cuando cambian sueldos o entran/salen empleados.

## Conexión con otros módulos
- **52** — qué es cada prestación que aquí se provisiona.
- **51** — la nómina del periodo que da las bases.
- **55** — al terminar el contrato, la provisión bien hecha hace la liquidación casi automática.
- **20 (Estado de situación financiera)** — las provisiones aparecen como **pasivo**.
- **57** — la provisión es parte del costo real del empleado.
- **Matematicas_lushows** — los valores mensuales se calculan allí.

## Siguiente paso típico
Montar el asiento de provisión recurrente cada mes y conciliarlo periódicamente con los pagos reales (prima, cesantías) para ajustar diferencias.
