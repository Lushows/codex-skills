# 54 — PILA: la Planilla Integrada de Liquidación de Aportes

La **PILA** (Planilla Integrada de Liquidación de Aportes) es el formato único con el que en Colombia se pagan, en un solo trámite, **todos** los aportes a seguridad social y parafiscales: salud, pensión, riesgos laborales (ARL), SENA, ICBF y caja de compensación. En vez de pagarle a cada entidad por separado, se llena una planilla en un **operador de información** (Aportes en Línea, SOI, SuAporte, etc.) y se paga de una sola vez.

Este módulo explica qué es la PILA y cómo funciona el flujo. La liquidación de cada aporte ya la vimos en el módulo 53; aquí es el "cómo se paga".

## Términos que debes conocer
- **PILA:** la planilla única que integra todos los aportes en un solo pago.
- **Operador de información:** la plataforma autorizada donde se diligencia y paga la PILA.
- **Tipo de planilla:** un código que indica de qué se trata (empleados, independientes, correcciones, liquidación, etc.).
- **Periodo de cotización:** el mes que se está pagando (salud y pensión a veces tienen periodos distintos por convención).

## Quién usa PILA
| Aportante | Cómo |
|---|---|
| Empresa con empleados | Planilla de empleados (tipo "E" o asistida) |
| Independiente / contratista | Planilla de independientes (tipo "I"), cotiza sobre el 40% del ingreso |
| Empleador doméstico | Planilla específica de servicio doméstico |

## Cómo es el flujo (paso a paso)
1. Se reúne la información del mes: empleados, IBC de cada uno, novedades (ingresos, retiros, incapacidades, licencias, vacaciones).
2. Se diligencia la planilla en el operador de información (o se sube un archivo plano si hay muchos empleados).
3. El operador **liquida** automáticamente cada aporte según los porcentajes vigentes.
4. La empresa **revisa** que cuadre con su nómina (aquí entra el contador).
5. Se **paga** electrónicamente. Queda el soporte de pago.

## Periodicidad y plazos
La PILA se paga **mensualmente**. El plazo depende de los **dos últimos dígitos del NIT** (o cédula) del aportante: la ley fija un calendario escalonado cada año. *Verifica las fechas del calendario del año vigente* — pagar tarde genera intereses de mora y, en pensión, problemas de cobertura.

## Novedades que afectan la PILA
- **ING:** ingreso de un empleado nuevo.
- **RET:** retiro de un empleado.
- **INC:** incapacidad (por enfermedad general o laboral).
- **LMA:** licencia de maternidad/paternidad.
- **VAC:** vacaciones.
- **SLN:** suspensión o licencia no remunerada.

Reportar mal una novedad descuadra los aportes y puede dejar a un empleado sin cobertura.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
"Distribuidora La 80" tiene 3 empleados. En el mes uno tomó vacaciones (novedad VAC) y entró uno nuevo (novedad ING el día 10). El contador:
- Carga los 3 empleados con su IBC.
- Reporta VAC e ING con las fechas exactas.
- El operador liquida ~$1.620.000 entre todos los aportes (ILUSTRATIVO).
- Verifica contra la nómina interna y paga antes de la fecha según el NIT.

## Errores comunes
- Pagar **tarde** y no contar los intereses de mora (van a `Matematicas_lushows`).
- No reportar **novedades** (un retiro no reportado sigue generando aporte).
- Liquidar el IBC del contratista sobre el 100% en vez del **40%** (módulo 59).
- No guardar el **soporte de pago** (es la prueba ante la UGPP).

## Conexión con otros módulos
- **53** — los porcentajes y bases de cada aporte que la PILA integra.
- **51** — la nómina interna contra la que se concilia la PILA.
- **55** — al liquidar un contrato, hay una PILA de retiro.
- **59** — el contratista paga su propia PILA de independiente.
- **130-139** — fiscalización UGPP sobre la PILA, a fondo.
- **Matematicas_lushows** — intereses de mora y verificación de la liquidación.

## Siguiente paso típico
Conciliar la PILA del mes con la nómina causada, archivar el soporte y, si hubo retiro, preparar la **liquidación de contrato** (módulo 55).
