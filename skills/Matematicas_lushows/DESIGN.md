# DESIGN — Matematicas_lushows

**Fecha:** 2026-06-14
**Autor:** Lushows + Claude

## Propósito
El cerebro cuantitativo del ecosistema Lushows. Promesa central no negociable: **error cero** — ningún
cálculo no trivial se entrega sin haber sido **ejecutado en código real y verificado por una segunda vía**.
La aritmética mental del LLM está prohibida para resultados que el usuario vaya a usar.

## Decisiones de diseño
1. **Alcance híbrido:** bloques 00–49 = fundamentos matemáticos generales (aritmética → cálculo → álgebra
   lineal); bloques 50–99 = aplicación a decisiones reales (probabilidad, estadística, finanzas, unit
   economics, optimización, riesgo).
2. **Exactitud por código obligatoria** (opción más fuerte): Python (`decimal`, `fractions`, `sympy`,
   `numpy`) o Node. Dinero → `decimal`/centavos enteros, nunca float. Álgebra exacta → `sympy`. Azar →
   simulación. Doble verificación siempre.
3. **100 módulos en 10 bloques de 10**, cargados bajo demanda — mismo patrón que las skills hermanas
   (`ventas_lushows`, `economist_lushows`, etc.).
4. **Idioma español**, explicación para no-experto, glosario de apoyo (`09`).
5. **Entregables presentables → PDF** vía chrome headless (patrón del ecosistema).

## Estructura de cada módulo
- H1 con título.
- **Qué resuelve / cuándo usarlo** (1–2 líneas).
- Conceptos explicados para no-experto, cada término definido la primera vez.
- Fórmulas exactas.
- **Verificación en código** — snippet real (Python/Node) que computa de forma exacta.
- **Ejemplo trabajado** con números, verificado por segunda vía.
- **Errores comunes / trampas.**
- **Cruces** `[[modulo]]` a módulos relacionados.
- Mini-checklist de exactitud cuando aplique.

## Frontera con otras skills
economist (estrategia) · ads (ejecución de pauta) · ventas (cierre) le rutean a Matematicas cualquier
número que importe; Matematicas reproduce y verifica todo número que reciba (modo auditar).

## Construcción
SKILL.md + DESIGN.md (manual) + los 100 módulos generados en paralelo (un agente por módulo), cada uno
con el mismo template y la filosofía de error cero, con cruces internos.
