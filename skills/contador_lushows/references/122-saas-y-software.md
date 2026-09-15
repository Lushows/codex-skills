# 122 — SaaS y software

Un negocio de software que cobra suscripción (SaaS, *Software as a Service*) tiene una particularidad contable enorme: el cliente **paga por adelantado** un servicio que tú entregarás mes a mes. Si cobras un plan anual hoy, esa plata todavía **no es ingreso tuyo**: es un anticipo que vas "ganando" a medida que prestas el servicio. Registrarlo todo como ingreso del primer día infla las ventas y distorsiona la realidad. Aquí mandan dos ideas: **ingreso diferido** y **reconocimiento por el tiempo del servicio**.

El estándar que gobierna esto es la **NIIF 15** (*ingresos de contratos con clientes*): se reconoce el ingreso cuando se transfiere el servicio al cliente, no cuando se cobra.

## Cuentas típicas del sector

| Cuenta | Para qué sirve | Tipo |
|---|---|---|
| Ingresos recibidos por anticipado (diferidos) | Plata cobrada que aún no es ingreso | Pasivo |
| Ingreso por suscripciones | El ingreso ya ganado del período | Ingreso |
| Activo intangible — desarrollo capitalizado | Software desarrollado que es activo | Activo |
| Amortización del intangible | Desgaste contable del software propio | Gasto |
| Cuentas por cobrar — clientes | Suscripciones facturadas no cobradas | Activo |

## Ingreso recurrente y diferido (lo esencial)

Cuando cobras un plan anual, el total entra como **pasivo (ingreso diferido)** y cada mes trasladas una porción a ingreso real. Así, un plan de 12 meses se reconoce en 12 partes iguales. El prorrateo se ejecuta con `Matematicas_lushows`.

| Concepto | Significado |
|---|---|
| MRR | Ingreso recurrente mensual ya ganado |
| Ingreso diferido | Cobrado pero pendiente de prestar |
| Reconocimiento | Pasar de diferido a ingreso cada mes |

## Capitalización de desarrollo e IVA

- El **desarrollo propio** del software puede capitalizarse como **activo intangible** cuando es viable, identificable y generará beneficios (fase de desarrollo, no de investigación). Lo que no califica, va a gasto.
- Ese intangible se **amortiza** (módulo 32) a lo largo de su vida útil.
- En Colombia los **servicios de software/SaaS suelen estar gravados con IVA** (servicio); confirma la tarifa y reglas vigentes. Si facturas a clientes del exterior puede haber **exportación de servicios** (tratamiento especial de IVA): verifícalo.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Cliente paga un plan anual de $1.200.000 + IVA. Al cobrar, el ingreso aún no se ha ganado:

| Cuenta | Débito | Crédito |
|---|---|---|
| Bancos | $1.428.000 | |
| Ingresos recibidos por anticipado | | $1.200.000 |
| IVA generado por pagar | | $228.000 |

Cada mes reconoces 1.200.000 ÷ 12 = $100.000: Ingreso diferido (D) $100.000, Ingreso por suscripciones (C) $100.000. Débitos = créditos. Cifras inventadas; toda suma se verifica con `Matematicas_lushows`.

## Errores comunes

- **Reconocer todo el plan anual como ingreso del primer mes**: viola NIIF 15 e infla el resultado.
- **Capitalizar gastos de investigación o mantenimiento**: solo el desarrollo que califica es activo.
- **No facturar el IVA del servicio** asumiendo que "el software no tiene IVA".
- **Confundir MRR con caja**: el flujo de caja y el ingreso reconocido no son lo mismo.
- **No amortizar el intangible** capitalizado.

## Conexión con otros módulos

- Los **ingresos diferidos y anticipos** están en el módulo **37**.
- La **amortización** del intangible en el **32**.
- El **IVA** de servicios en el **41**.
- El reconocimiento bajo **NIIF** en el bloque **03/25/62**.
- *Pricing de planes, CAC/LTV y modelo de negocio*: `economist_lushows`.
- Todo prorrateo y proyección: `Matematicas_lushows`.

## Siguiente paso típico

Separa lo cobrado (caja) de lo ganado (ingreso): lleva un cuadro de ingresos diferidos por cliente y reconoce mes a mes. Decide con criterio qué desarrollo capitalizar y empieza a amortizarlo.
