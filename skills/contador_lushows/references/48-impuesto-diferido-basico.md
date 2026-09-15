# 48 — Impuesto diferido (básico)

Aquí aparece una de las ideas que más confunde a quien empieza: **la utilidad que muestran tus estados financieros NO es la misma cifra sobre la que pagas renta**. La contabilidad sigue las normas **NIIF** (cómo se mide el negocio para informar a socios y bancos); el impuesto sigue las **normas fiscales** de la DIAN. Como miden distinto, aparecen **diferencias**. El **impuesto diferido** es, en pocas palabras, el reconocimiento contable de que esas diferencias **se van a revertir en el futuro** y traerán más o menos impuesto entonces.

Este módulo da el **concepto básico** para entenderlo y detectarlo. El cálculo detallado y los casos finos viven en el módulo **114**. **No inventamos tarifas:** el diferido se mide con la **tarifa de renta vigente**. *Verifícala en la DIAN.*

## Conceptos clave (despacio)
- **Base contable:** el valor de un activo o pasivo según NIIF (lo que dicen tus estados financieros).
- **Base fiscal:** el valor de ese mismo activo o pasivo según las reglas de la DIAN.
- **Diferencia temporaria:** cuando base contable y fiscal difieren, pero esa diferencia **se cerrará con el tiempo** (no es permanente).
- **Diferencia permanente:** una diferencia que **nunca** se revierte (p. ej. un gasto contable que la ley **jamás** acepta como deducible). Las permanentes **no generan** impuesto diferido.
- **Activo por impuesto diferido:** pagarás **menos** impuesto en el futuro (beneficio futuro).
- **Pasivo por impuesto diferido:** pagarás **más** impuesto en el futuro (obligación futura).

## La regla mental
```
¿Base contable ≠ base fiscal?
   → ¿la diferencia se revertirá algún día?  (temporaria)
        SÍ → genera impuesto diferido (activo o pasivo)
        NO (permanente) → NO genera impuesto diferido
```
Y la magnitud: **diferencia temporaria × tarifa de renta vigente = impuesto diferido**.

## Ejemplos típicos de dónde nacen las diferencias
| Situación | Por qué difiere |
|---|---|
| Depreciación | NIIF puede depreciar a un ritmo distinto al fiscal |
| Provisiones / deterioros | Contables ya, pero deducibles fiscalmente solo al concretarse |
| Pérdidas fiscales por compensar | Reducen impuesto futuro → activo diferido |
| Ingresos reconocidos en momentos distintos | NIIF vs. fiscal cambian el "cuándo" |

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
Un equipo:
- Base contable (NIIF, depreciación más lenta): $10.000.000
- Base fiscal (depreciación más rápida): $7.000.000
- Diferencia temporaria: $3.000.000
- Tarifa de renta **ilustrativa 35%**: impuesto diferido = 3.000.000 × 35% = **$1.050.000** (inventado).
- Como la base contable es mayor, esa diferencia traerá **más** impuesto al revertirse → **pasivo por impuesto diferido**.

> Cifras y tarifa de ejemplo. El cálculo real va a **Matematicas_lushows** con `decimal` y con la tarifa vigente.

## Por qué importa (sin asustarse)
- Hace que el **gasto por impuesto** en el estado de resultados refleje correctamente el periodo, no solo lo que se paga ese año.
- Es exigible para ciertos grupos NIIF; en negocios muy pequeños (Grupo 3) puede simplificarse. *Verifica qué grupo NIIF aplica.*
- Para un negocio pequeño, lo importante hoy es **detectar** que existe la diferencia; el armado fino lo hace el contador titulado (y el módulo 114).

## Errores comunes
- Tratar una diferencia **permanente** como si generara diferido (no lo hace).
- Calcular el diferido con una tarifa **antigua** en vez de la vigente.
- Confundir el **impuesto corriente** (el que pagas este año) con el **diferido** (el efecto futuro).
- Ignorarlo del todo cuando el grupo NIIF sí lo exige.

## Conexión con otros módulos
- **42 (Renta)** — la base fiscal sale de la depuración de renta; el diferido la complementa.
- **114** — el cálculo detallado y los casos avanzados de impuesto diferido.
- Módulos de **estados financieros (20-29)** — el diferido aparece en el balance y en el resultado.
- **economist_lushows** — decisiones de planeación que crean diferencias (depreciación, etc.).
- **Matematicas_lushows** — la liquidación del diferido.

## Siguiente paso típico
Identificar las partidas donde base contable y fiscal difieren, separar temporarias de permanentes, y (si el grupo NIIF lo exige) llevar el cálculo al módulo **114** y a **Matematicas_lushows**. Para la mayoría de pymes pequeñas, basta con detectarlo y consultarlo con el contador.
