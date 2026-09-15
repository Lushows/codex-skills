# 55 — Liquidación de contrato: el ajuste de cuentas al terminar

Cuando un contrato de trabajo termina —por renuncia, despido o vencimiento del plazo— hay que hacer la **liquidación final**: pagarle al trabajador todo lo que se le debe hasta ese día. No es un pago opcional ni "de buena voluntad": es una obligación, y hacerla mal genera demandas, sanciones por mora y dolores de cabeza.

Este módulo explica qué conceptos entran en la liquidación y cómo se arma. Cada valor se calcula en `Matematicas_lushows`; aquí está la estructura y el orden.

## Términos que debes conocer
- **Liquidación final:** el pago de todo lo pendiente al terminar el contrato.
- **Días proporcionales:** la fracción de prestaciones causada desde el último corte hasta la fecha de salida.
- **Indemnización:** pago adicional cuando el despido es **sin justa causa** (no aplica en renuncia ni en justa causa).
- **Sanción por mora:** un día de salario por cada día de retraso en pagar la liquidación (verifica condiciones vigentes).

## Conceptos que se pagan en la liquidación
| Concepto | ¿Siempre? | Base |
|---|---|---|
| Salario pendiente de los días trabajados | Sí | Salario diario |
| Cesantías proporcionales | Sí | Salario + auxilio |
| Intereses a las cesantías proporcionales | Sí | 12% anual sobre la cesantía |
| Prima de servicios proporcional | Sí | Salario + auxilio |
| Vacaciones causadas y no disfrutadas | Sí | Salario sin auxilio |
| Indemnización | Solo si es despido sin justa causa | Según tipo y duración del contrato |

## Cómo se arma (paso a paso)
1. Definir la **fecha exacta** de terminación y el motivo (renuncia / justa causa / sin justa causa).
2. Calcular los **días** desde el último pago de cada prestación hasta la fecha de salida.
3. Liquidar cada concepto proporcionalmente (en `Matematicas_lushows`).
4. Si hay despido sin justa causa, calcular la **indemnización** según el contrato.
5. Restar deducciones legales pendientes (préstamos, etc.).
6. Reportar el **retiro (RET)** en la PILA (módulo 54).
7. Pagar dentro del plazo para evitar **sanción por mora**.

## Asiento contable de la liquidación (estructura que cuadra)
| Cuenta | Débito | Crédito |
|---|---|---|
| Prestaciones por pagar (prima, cesantías, intereses, vacaciones) | 1.200.000 | |
| Gasto laboral / indemnización (si aplica) | 800.000 | |
| Retención / deducciones por pagar | | 50.000 |
| Bancos (pago al trabajador) | | 1.950.000 |
| **Sumas** | **2.000.000** | **2.000.000** |

(Cifras ILUSTRATIVAS; idealmente la mayor parte ya estaba provisionada —módulo 58— y aquí solo se cancela el pasivo.)

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
"Restaurante El Fogón", un cocinero renuncia el 15 de un mes tras 7 meses:
- Salario de 15 días.
- Cesantías, intereses, prima y vacaciones **proporcionales** a 7 meses.
- **Sin indemnización** (fue renuncia voluntaria).
- Se reporta RET en PILA y se paga sin demora.

## Errores comunes
- Pagar **indemnización en una renuncia** (no corresponde) o **no pagarla** en un despido sin justa causa (sí corresponde).
- Liquidar mal la **proporcionalidad** de los días (a `Matematicas_lushows`).
- Olvidar las **vacaciones no disfrutadas**.
- No reportar el retiro en PILA o pagar tarde y disparar la **sanción por mora**.

## Conexión con otros módulos
- **52** — las prestaciones que ahora se liquidan proporcionalmente.
- **58** — si se provisionó bien, la liquidación solo cancela el pasivo.
- **54 (PILA)** — el reporte de retiro (RET).
- **130-139** — tipos de contrato, justas causas e indemnizaciones (laboral 2026 a fondo, y aquí **no** reemplaza al abogado laboral).
- **Matematicas_lushows** — toda la liquidación proporcional y la indemnización.

## Siguiente paso típico
Entregar el desprendible de liquidación, pagar a tiempo, reportar el retiro en PILA y archivar el soporte firmado (paz y salvo).
