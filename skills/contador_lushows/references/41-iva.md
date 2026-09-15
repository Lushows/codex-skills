# 41 — IVA: el impuesto al valor agregado

El **IVA (Impuesto al Valor Agregado)** es un impuesto **al consumo**: lo paga el cliente final, pero el negocio actúa como **recaudador** para la DIAN. Tú cobras IVA cuando vendes (IVA generado) y pagas IVA cuando compras (IVA descontable); a la DIAN le entregas la **diferencia**. Por eso se llama "al valor agregado": cada eslabón solo aporta el impuesto sobre el valor que añadió.

Este módulo explica la mecánica. **No inventamos tarifas:** Colombia tiene una tarifa general y tarifas diferenciales, además de bienes excluidos y exentos. *Verifica las tarifas y la lista de bienes/servicios vigentes en la DIAN cada año.*

## Conceptos clave (define la primera vez)
- **IVA generado:** el que cobras a tus clientes en las ventas gravadas.
- **IVA descontable:** el que pagaste en tus compras de bienes/servicios gravados que se relacionan con tu actividad gravada. Es como un "crédito" a tu favor.
- **Responsable de IVA:** quien debe cobrarlo, declararlo y pagarlo (antes "régimen común"). El "no responsable" (antes "régimen simplificado") no lo cobra. *Los topes para ser responsable se miden en UVT y cambian: verifica los del año.*
- **Bienes/servicios gravados:** llevan IVA. **Exentos:** tarifa 0% (dan derecho a descontable). **Excluidos:** no causan IVA (no dan derecho a descontable).
- **Causación:** el momento en que nace el IVA (con la factura, la entrega o el pago, según el caso).

## La fórmula del IVA a pagar
```
IVA a pagar a la DIAN = IVA generado (ventas)  −  IVA descontable (compras)
```
Si el descontable es mayor que el generado, queda **saldo a favor** (lo puedes arrastrar o solicitar en devolución, según el caso).

## Periodicidad de la declaración
La declaración de IVA puede ser **bimestral** o **cuatrimestral** según los ingresos del año anterior (y otros criterios). *La periodicidad y los topes en UVT se verifican en la DIAN.*
| Periodicidad | A grandes rasgos (CONCEPTO) |
|---|---|
| Bimestral | Negocios de mayores ingresos / ciertos responsables |
| Cuatrimestral | Negocios de menores ingresos |

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
Una tienda en el bimestre, con una tarifa **ilustrativa del 19%** (verifica la vigente):
- Ventas gravadas: $20.000.000 → IVA generado = $3.800.000 (ilustrativo)
- Compras gravadas: $11.000.000 → IVA descontable = $2.090.000 (ilustrativo)
- **IVA a pagar = 3.800.000 − 2.090.000 = $1.710.000** (ilustrativo)

> Estos números son inventados y la tarifa es de ejemplo. El cálculo real va a **Matematicas_lushows** con `decimal`.

**Asiento al vender** (ver módulos 10-19 para partida doble):
- Débito: Caja/Clientes $23.800.000
- Crédito: Ingresos por ventas $20.000.000
- Crédito: IVA por pagar $3.800.000

## Nota: restaurantes e impuesto al consumo
Muchos restaurantes y bares **no cobran IVA sino impuesto al consumo (INC)**, que **no es descontable** para el cliente y tiene su propia tarifa y declaración. No los confundas. *Verifica el régimen de la actividad concreta.*

## Errores comunes
- Tomarse como descontable el IVA de compras que **no se relacionan** con la actividad gravada.
- Olvidar declarar en periodo en **ceros** cuando no hubo operaciones (si está obligado).
- Confundir **exento (0%, da derecho a descontable)** con **excluido (no causa, no da derecho)**.
- Aplicar la tarifa "de memoria": **siempre se verifica la vigente**.
- Cobrar IVA siendo **no responsable**, o no cobrarlo siendo responsable.

## Conexión con otros módulos
- **40** — dónde encaja el IVA en el mapa tributario.
- **43 (Retención)** — existe **retención de IVA (reteIVA)** que se cruza con esta declaración.
- **45 (Facturación electrónica)** — la factura es el soporte del IVA generado y descontable.
- **46 / 47** — calendario y presentación de la declaración.
- **Matematicas_lushows** — el cálculo del IVA a pagar.

## Siguiente paso típico
Confirmar si el negocio es responsable de IVA o de consumo, definir la periodicidad y armar el cuadro de IVA generado vs. descontable del periodo. Luego ir a **47** para presentar.
