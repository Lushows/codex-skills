# 53 — Seguridad social y parafiscales: quién paga qué

Cuando contratas a alguien, además del sueldo y las prestaciones, debes aportar a la **seguridad social** (salud, pensión y riesgos laborales) y a los **parafiscales** (SENA, ICBF y caja de compensación). Una parte la asume el empleado (se le deduce) y otra parte la asume la empresa (es su costo). Confundir quién paga qué es uno de los errores más caros de la nómina.

Este módulo es el mapa de aportes. Los porcentajes son estructurales del sistema; los valores en pesos (IBC, topes) se verifican cada año y se calculan en `Matematicas_lushows`.

## Términos que debes conocer
- **Seguridad social:** protección obligatoria en salud, pensión y riesgos laborales (ARL).
- **Parafiscales:** aportes para formación (SENA), niñez (ICBF) y bienestar familiar (caja de compensación).
- **IBC (Ingreso Base de Cotización):** la base sobre la que se aplican los porcentajes. No incluye auxilio de transporte.
- **ARL:** Administradora de Riesgos Laborales. La tarifa depende del **nivel de riesgo** del trabajo (clases I a V).

## Tabla de aportes (porcentajes estructurales)
| Concepto | Empleado | Empleador | Total sobre IBC |
|---|---|---|---|
| Salud | 4% | 8,5% | 12,5% |
| Pensión | 4% | 12% | 16% |
| ARL (riesgos) | 0% | 0,522% – 6,96% según clase de riesgo | variable |
| SENA | 0% | 2% | 2% |
| ICBF | 0% | 3% | 3% |
| Caja de compensación | 0% | 4% | 4% |

> **Exoneración:** ciertas empresas y empleadores están **exonerados** de pagar la parte de salud (8,5%), SENA (2%) e ICBF (3%) para empleados que ganan menos de un tope en SMMLV. Esto **cambia con las reformas**: verifica si tu caso aplica antes de liquidar.

## Asiento contable de los aportes (causación)
La empresa reconoce su parte como gasto y registra todo lo que debe pagar al sistema. Estructura que cuadra (cifras ILUSTRATIVAS):

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto aportes empleador (salud, pensión, ARL, parafiscales) | 540.000 | |
| Aportes por pagar - salud (4% empleado + 8,5% empresa) | | 187.500 |
| Aportes por pagar - pensión (4% empleado + 12% empresa) | | 240.000 |
| Aportes por pagar - ARL | | 7.830 |
| Aportes por pagar - parafiscales (SENA+ICBF+caja) | | 135.000 |
| **Sumas** | **(según IBC)** | **(según IBC)** |

(El débito incluye solo la parte de empresa; la parte del empleado ya se dedujo en el módulo 51. Valores ILUSTRATIVOS sobre IBC de $1.500.000.)

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
"Taller Mecánico Don Pedro", IBC $1.500.000, riesgo clase III (~2,436%):
- Salud: empleado 4% ($60.000) + empresa 8,5% ($127.500).
- Pensión: empleado 4% ($60.000) + empresa 12% ($180.000).
- ARL: empresa $36.540 (riesgo III).
- Parafiscales: SENA $30.000 + ICBF $45.000 + caja $60.000.

## Errores comunes
- Cobrarle al empleado la parte que es de la empresa (o viceversa).
- Asignar mal la **clase de riesgo ARL**: un riesgo alto pagado como bajo es sanción.
- Asumir exoneración sin verificar si realmente aplica al empleador y al salario.
- Liquidar aportes sobre el devengado total en vez del IBC (que excluye el auxilio).

## Conexión con otros módulos
- **51** — la parte del empleado ya se dedujo allí.
- **54 (PILA)** — todos estos aportes se pagan juntos en una sola planilla.
- **57** — estos aportes son el grueso del costo real del empleado.
- **59** — el contratista cotiza distinto (él mismo, sobre el 40% del contrato).
- **130-139** — UGPP, fiscalización de aportes y casos especiales.
- **Matematicas_lushows** — todos los porcentajes, IBC y topes se calculan allí.

## Siguiente paso típico
Ir al módulo **54 (PILA)** para ver cómo se pagan todos estos aportes en una sola planilla mensual.
