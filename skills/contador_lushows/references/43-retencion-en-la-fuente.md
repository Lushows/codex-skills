# 43 — Retención en la fuente

La **retención en la fuente NO es un impuesto nuevo**: es un mecanismo para **cobrar un impuesto por adelantado**, en el momento mismo en que ocurre el pago. La idea es sencilla: en vez de esperar a fin de año a que el beneficiario pague renta, quien le paga **retiene** un pedacito y se lo entrega a la DIAN a nombre de él. Luego, el beneficiario **descuenta** esa retención en su declaración. Es "recaudar en la fuente del ingreso".

Este módulo explica la mecánica y deja un ejemplo de asiento. **No inventamos tarifas ni bases:** los porcentajes y las cuantías mínimas (en UVT) varían por concepto y por año. *Verifica las tarifas y bases vigentes en la DIAN.*

## Conceptos clave
- **Agente retenedor:** quien está obligado a retener al hacer ciertos pagos (muchas empresas lo son). Asume una **responsabilidad**: si no retiene, responde con su patrimonio.
- **Sujeto de retención (beneficiario):** quien recibe el pago con la retención descontada.
- **Concepto:** el tipo de pago (compras, servicios, honorarios, arrendamientos, etc.). Cada concepto tiene **su tarifa y su base mínima**.
- **Base de retención:** el monto del pago sobre el cual se aplica la tarifa; si el pago no supera la **cuantía mínima** del concepto, no se retiene.
- **Autorretención:** algunos contribuyentes se retienen a sí mismos (régimen especial; *verifica si aplica*).

## Tipos de retención (todas se cruzan en declaraciones)
| Retención | A cuenta de qué impuesto | Quién la cobra |
|---|---|---|
| Retefuente (renta) | Impuesto de renta | DIAN (nacional) |
| ReteIVA | IVA | DIAN (nacional) |
| ReteICA | ICA | El municipio (ver 44) |

## Cómo funciona, paso a paso
1. Llega un pago a un proveedor por un **concepto** (p. ej. servicios).
2. Verificas si el monto supera la **base mínima** del concepto (en UVT, **verifica la vigente**).
3. Si la supera, aplicas la **tarifa** del concepto sobre la base.
4. Le pagas al proveedor el neto (pago − retención) y le entregas un **certificado de retención**.
5. Declaras y pagas a la DIAN lo retenido (declaración mensual de retención).

## Ejemplo de asiento (cifras ILUSTRATIVAS / inventadas)
Pagas un servicio por $5.000.000 con una **tarifa ilustrativa de retefuente del 4%** (verifica la real):
- Retención = $5.000.000 × 4% = **$200.000** (ilustrativo)
- Le pagas al proveedor: $4.800.000

**Asiento (desde el que paga / agente retenedor):**
- Débito: Gasto/Servicio $5.000.000
- Crédito: Bancos $4.800.000
- Crédito: Retención en la fuente por pagar $200.000

Esos $200.000 los **entregas a la DIAN**; el proveedor los **descuenta** en su declaración de renta.

> Tarifa y cifras de ejemplo. El cálculo real va a **Matematicas_lushows** con `decimal`.

## El certificado de retención
El agente retenedor debe **expedir un certificado** al beneficiario (anual para retefuente, según periodicidad para otros). Sin certificado, al beneficiario le cuesta probar la retención. Guardar y emitir estos certificados es parte del **CUMPLIMIENTO**.

## Errores comunes
- Retener un concepto **con la tarifa de otro** (cada concepto tiene la suya).
- Retener por debajo de la **base mínima** (no había que retener) o no retener cuando sí superaba la base.
- No expedir los **certificados** → el proveedor no puede descontar.
- Confundir reteICA (municipal) con retefuente (nacional): van en declaraciones distintas.
- Como agente retenedor, **declarar pero no pagar**: la retención es plata de un tercero; no pagarla es muy sancionable.

## Conexión con otros módulos
- **42 (Renta)** — las retenciones practicadas son anticipo que el beneficiario descuenta.
- **41 (IVA)** — reteIVA se relaciona con la declaración de IVA.
- **44 (ICA)** — reteICA es municipal.
- **47 / 46** — la retención se declara mensualmente; ver calendario y presentación.
- **Matematicas_lushows** — el cálculo de cada retención.

## Siguiente paso típico
Construir la **tabla de conceptos** que el negocio retiene (con tarifa y base vigentes), aplicarla a los pagos del mes, armar la declaración mensual y emitir certificados. Luego ir a **47**.
