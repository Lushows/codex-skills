# 37 — Aplicar un manual de marca a la web (recibir e implementar fiel)

Lo opuesto a 24 (crear identidad): aquí **recibes una guía de marca existente** (PDF de brand guidelines de un cliente) y la traduces a una web premium con fidelidad + gusto. **Léelo SIEMPRE que trabajes con un manual/guía de marca dado.** Pareja de 24, 15 (tokens), 02/03.

## 1. Anatomía del manual y cómo leerlo

Los brand books serios tienen ~9 bloques. Lee cada sección preguntando "¿qué regla web sale de aquí?":

| Sección | Qué extraer para web | Trampa habitual |
|---|---|---|
| **Sistema de logo** (variantes, clear space, tamaño mín, usos prohibidos) | SVG responsive (horizontal/isotipo/mono); clear space → `padding` mín; tamaño mín → breakpoint donde cae al isotipo | clear space ignorado en headers apretados |
| **Color** (Pantone/CMYK/RGB/HEX, primarios/tints) | HEX como verdad de origen; jerarquía primario→acento; ratios de uso (60/30/10) | color de marca como texto sin verificar contraste |
| **Tipografía** (display/texto, pesos, jerarquía, tracking, leading) | escala tipográfica, pesos, licencia **web** | el manual da puntos de imprenta, no escala fluida |
| **Fotografía/arte** (encuadre, color grading, "sí/no") | LUT/filtro, reglas de overlay, ratios | stock genérico que rompe el grading |
| **Iconografía/grafismos/patterns** | stroke width, grid de icono, dispositivos gráficos | mezclar set de marca con iconos de librería |
| **Tono de voz** | adjetivos de personalidad, do/don't de copy | tono en headlines pero no en microcopy/errores |
| **Grid/layout/motion** | columnas, márgenes, principios, timings | casi siempre ausente para web → extrapolar |

**Prioridad de extracción:** color → tipografía → logo → grafismos → fotografía → tono → motion (color+tipo = 80% de la percepción "esto es la marca").
**Gaps (lo normal):** el manual fue hecho para imprenta/identidad, no web. Cuando falte algo (hover, dark mode, responsive, componentes), no inventes desde cero — deriva del *espíritu* del manual (§3).

## 2. Traducir assets de marca a web tokens

Arquitectura 3 niveles (W3C `$value`/`$type`): **primitivos** (valores crudos de marca) → **semánticos** (rol/uso) → **componente**. Exporta de Figma → Style Dictionary → Tailwind/CSS sin glue code.
**Color — de print a web accesible:** el HEX/RGB del manual es la fuente de verdad (Pantone es para tinta). (1) primario → OKLCH para escalas perceptualmente uniformes; (2) genera tints/shades variando solo `L`, manteniendo `H`; (3) **verifica WCAG ANTES de asignar roles** — muchos colores de marca brillantes fallan 4.5:1 sobre blanco. La solución NO es cambiar el color: resérvalo para superficies/acentos grandes (≥24px/3:1) y deriva una variante `-on-text` más oscura del mismo hue.
```css
:root{
  --brand-primary:#19335C;                  /* HEX del brand book */
  --brand-700:oklch(.38 .09 256); --brand-500:oklch(.52 .11 256); --brand-300:oklch(.72 .07 256);
  --color-text-on-brand:#fff;               /* validado ≥4.5:1 */
  --color-accent:var(--brand-500); --focus-ring:oklch(.65 .18 256);  /* más saturado para visibilidad */
}
```
**Tipografía — fuente de marca a web:** (1) verifica licencia **web** (webfont ≠ desktop); (2) si la tiene → `@font-face` WOFF2; (3) si NO → equivalente de la foundry o variable font en métricas similares, sistema sólido con la fallback + fuente de marca como progressive enhancement; (4) **reduce CLS** ajustando la fallback a las métricas:
```css
@font-face{font-family:"BrandSans-fallback";src:local("Arial");size-adjust:102%;ascent-override:92%;descent-override:24%;line-gap-override:0%}
body{font-family:"BrandSans","BrandSans-fallback",system-ui,sans-serif}
```
La escala en puntos → escala modular (ratio ~1.25) + `clamp()` fluido respetando la jerarquía H1→body del manual.
**Espaciado/grid:** columnas/márgenes del manual → escala base 4/8px y `--space-*`. **Logo → SVG** responsive (currentColor donde aplique), clear space como `padding`, tamaño mín como breakpoint del cambio a isotipo.

## 3. Fiel pero elevado: "¿qué haría la marca?"

El manual casi nunca cubre hover/focus/dark/motion/componentes — aquí está el 90% del juicio. Framework para extrapolar sin desviarte:
- **Deriva, no inventes.** Cada estado sale de un token existente. Hover = shift de lightness del primario (no un color nuevo). Active = un paso más. Disabled = misma familia, baja opacidad/chroma.
- **Focus visible siempre** (accesibilidad, no decoración): anillo derivado del acento, más saturado, sobre toda superficie.
- **Dark mode = adaptación, no inversión.** No inviertas HEX; re-mapea tokens semánticos (superficies oscuras de la familia del primario, acento un poco más brillante, logo en variante mono del propio manual).
- **Motion según personalidad:** "calma/premium" → easing suave (~`cubic-bezier(.4,0,.2,1)`), 200-400ms; "enérgica" → más snap. Deriva del tono.
- **Test del espíritu:** ante cada decisión no documentada, "¿esto se ve como algo que el manual *aprobaría*?". Evita **sub-interpretación** (literal/plano, web que parece el PDF) y **sobre-interpretación** (glassmorphism/gradientes que la marca nunca pidió).

## 4. Voz de marca → copy y microcopy web

La voz es constante; el *tono* se adapta al contexto (celebración vs error). Extrae los adjetivos de personalidad y aplícalos medible: **headlines** con carácter de marca · **CTAs** en voz activa/imperativa (según el nivel que permita el manual) · **microcopy** (placeholders/tooltips/labels) cercano y activo · **errores** empáticos/útiles, nunca culpan al usuario. Crea una **matriz contexto×tono** (éxito/espera/error/vacío) para que todo el equipo escriba consistente.

## 5. Imágenes y dirección de arte

Extrae encuadre, sujetos, color grading → construye un **LUT/preset** y aplícalo a TODA imagen (incl. stock — sin grading rompe la marca al instante). Reglas de overlay/duotono → `mix-blend-mode`/filtros tokenizados (no por imagen). Un solo set de iconos con el stroke del manual. Patterns/dispositivos gráficos → componentes reutilizables con su token. Define ratios y `object-fit` para que el encuadre sobreviva al responsive.

## 6. Proceso y entregables

1. **Audit del manual** — anota cada regla como *explícita* o *gap a extrapolar*.
2. **Extrae tokens** — primitivos→semánticos→componente (W3C).
3. **Web style tile / mini-sistema** — 1 página con color (ratios WCAG anotados), tipo en escala, logo responsive, botón en 5 estados, card, foto tratada, 3 piezas de microcopy. **Apruébalo ANTES de diseñar páginas** — aquí se defienden las extrapolaciones.
4. **Diseña** consumiendo solo tokens.
5. **QA contra el manual** (checklist abajo).
6. **Documenta y defiende:** cada decisión no-literal lleva nota "el manual dice X → en web se traduce como Y porque Z".

### Checklist de fidelidad de marca (QA)
Logo: variante correcta por contexto, clear space, tamaño mín, isotipo en mobile, SVG nítido · Color: todo HEX coincide; ningún color inventado; cada par texto/fondo ≥4.5:1 (3:1 grande/UI); acento en proporción del manual · Tipo: familias correctas (o fallback validada), jerarquía fiel, pesos del manual, sin CLS · Espaciado/grid deriva de la escala · Estados (hover/active/focus/disabled) derivados de tokens, focus visible · Dark mode por re-mapeo, no inversión · Imágenes con grading/encuadre del manual (incl. stock) · Voz consistente en headlines/CTA/microcopy/errores · Motion coherente con la personalidad · cada extrapolación documentada.

### Anti-patterns de aplicación de marca
ignorar el manual y "mejorar" a tu gusto · aplicación literal/plana (web que parece el PDF, sin estados/vida) · irse off-brand (gradientes/glass/motion que el manual nunca contempló) · fallo de contraste por color de marca como texto · Pantone/CMYK literal en pantalla en vez del HEX/RGB · fuente de marca sin licencia web servida igual, o fallback con CLS · dark mode por inversión de HEX · stock sin grading mezclado con foto tratada · tono solo en headlines · clear space del logo ignorado.
