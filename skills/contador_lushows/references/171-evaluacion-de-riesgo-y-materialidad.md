# 171 — Riesgo y materialidad: dónde mirar y qué tan fino

Toda auditoría vive con una verdad incómoda: **no se puede revisar todo**. Un auditor no cuenta cada peso ni revisa cada factura. Entonces, ¿cómo da una opinión confiable? Con dos brújulas: el **riesgo** (dónde es más probable que haya un error grande) y la **materialidad** (a partir de qué tamaño un error sí importa). Juntas le dicen al auditor dónde poner los ojos y cuánto esfuerzo gastar.

Este módulo desarrolla A FONDO lo que el módulo 71 y el 78 (gestión de riesgos) introdujeron. Aquí entramos al modelo de riesgo de auditoría y al cálculo de la materialidad —que, como todo número, se ejecuta y verifica, nunca se hace de cabeza.

> **Cumplimiento + auditable.** El nivel de riesgo evaluado y la materialidad fijada se documentan y **justifican** en papeles de trabajo: explican por qué se hizo tanto (o tan poco) trabajo en cada área. Todo cálculo de materialidad y de tamaño de muestra se **rutea a `Matematicas_lushows`**. Este texto explica el oficio; **no reemplaza al auditor habilitado**.

## Términos que debes conocer
- **Riesgo de auditoría (RA):** la probabilidad de dar una opinión limpia cuando los estados sí tienen un error material.
- **Riesgo inherente (RI):** la propensión de una cuenta a tener errores por su naturaleza, sin pensar en controles (el efectivo es más riesgoso que un terreno).
- **Riesgo de control (RC):** el riesgo de que los controles de la empresa no detecten/eviten el error.
- **Riesgo de detección (RD):** el riesgo de que el auditor, con sus pruebas, tampoco lo detecte. Es el único que el auditor controla.
- **Materialidad:** el umbral monetario a partir del cual un error cambia la decisión del lector.

## El modelo de riesgo de auditoría
La idea central, conceptual: **RA ≈ RI × RC × RD**. El auditor fija el RA que está dispuesto a aceptar (bajo, p. ej. 5%). El RI y el RC los **evalúa** (vienen de la empresa). Entonces **despeja el RD** que puede permitirse: a mayor RI×RC, menor RD aceptable → **más pruebas**.

| Si el riesgo inherente y de control es… | El auditor necesita un riesgo de detección… | Es decir… |
|---|---|---|
| Alto | Bajo | Más pruebas, muestras más grandes |
| Bajo | Más alto | Menos pruebas, puede confiar más |

*El despeje aritmético del modelo se ejecuta en `Matematicas_lushows`.*

## Tipos de materialidad
- **Materialidad global:** para los estados en su conjunto.
- **Materialidad de desempeño (o de ejecución):** un umbral más bajo para el trabajo, que deja margen para errores no detectados.
- **Materialidad específica:** para áreas sensibles (p. ej. pagos a la gerencia) donde un error pequeño igual importa.

La base suele ser un porcentaje de una cifra ancla (utilidad antes de impuestos, ingresos o activos). **El porcentaje, la base y el cálculo se deciden con criterio y se ejecutan en Matematicas.**

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
"Distribuidora Andina SAS" tiene ingresos de $2.000.000.000 (inventado). El auditor elige como ancla la utilidad antes de impuestos ($120.000.000) y un 5% → materialidad global $6.000.000. La materialidad de desempeño la fija en 75% de eso: $4.500.000. Matematicas ejecuta y verifica: 120.000.000 × 5% = 6.000.000; 6.000.000 × 75% = 4.500.000. Como la cartera tiene riesgo inherente alto (clientes morosos), el RD se baja y se amplía la muestra.

## Errores comunes
- Confundir materialidad con "lo que me parece grande": es un cálculo con base y porcentaje justificados.
- Olvidar la **materialidad de desempeño** y trabajar todo contra la global → poco margen para lo no detectado.
- Tratar todas las cuentas con el mismo riesgo: el efectivo no es igual a un terreno.
- Hacer el despeje del modelo de riesgo de cabeza → debe ir a Matematicas.
- No reevaluar el riesgo cuando aparecen hallazgos durante la auditoría.

## Conexión con otros módulos
- **170 (Planeación)** — la materialidad y el riesgo son insumos de la estrategia.
- **172 (Muestreo)** — el riesgo y la materialidad determinan el tamaño de muestra.
- **78 (Gestión de riesgos)** — la base que aquí se profundiza.
- **178 (Control interno COSO)** — la evaluación del control alimenta el riesgo de control.
- **176 (Informe y dictamen)** — los errores se evalúan contra la materialidad para opinar.
- **`Matematicas_lushows`** — ejecuta materialidad, despeje del modelo y tamaño de muestra.

## Siguiente paso típico
Con el riesgo y la materialidad fijados, definir **cuánto y cómo muestrear** (módulo 172). El tamaño de muestra se calcula en `Matematicas_lushows`.
