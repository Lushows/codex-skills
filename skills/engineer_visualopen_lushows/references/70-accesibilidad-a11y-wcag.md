# 70 — Accesibilidad (a11y / WCAG)

**WCAG 2.2** (W3C, oct 2023) organiza criterios en **4 principios POUR**: **Perceivable** (alt text, contraste,
captions) · **Operable** (teclado, sin trampas, tiempo suficiente) · **Understandable** (legible, predecible, ayuda
en errores) · **Robust** (compatible con tecnologías asistivas). Niveles **A/AA/AAA** — **AA es el objetivo legal.**

## Marco legal (crítico 2025+)
El **European Accessibility Act (EAA)** es exigible desde el **28-jun-2025**: productos/servicios digitales
(e-commerce, banca, ebooks) vendidos a consumidores UE deben cumplir. Conformidad con **WCAG 2.2 AA** da presunción
(vía EN 301 549). Multas hasta ~3M EUR. En EE.UU., ADA Title III genera litigios. Aunque BIO-SETA es LatAm, **si vendes a la UE aplica.**

## Nuevos criterios WCAG 2.2 (9)
Focus Appearance (2.4.11), Dragging Movements (2.5.7, alternativa a arrastrar), **Target Size mínimo 24×24px** (2.5.8), Accessible Authentication (sin CAPTCHA cognitivo puro), Consistent Help (3.2.6).

## HTML semántico primero
`<button>`, `<nav>`, `<main>`, `<header>`, `<h1>`-`<h6>` en orden. Un `<div onclick>` NO es accesible; un `<button>` lo es gratis (foco, Enter/Space, rol).

## ARIA — "no ARIA is better than bad ARIA"
Solo cuando HTML semántico no alcanza. **Roles** (`role="dialog"`, `role="alert"`; no `role="button"` en un `<button>`).
**States/properties:** `aria-expanded`, `aria-checked`, `aria-label`, `aria-describedby`, `aria-current`. **Landmarks**
(`<nav>`,`<main>`,`<aside>`) permiten saltar por regiones. **Live regions:** `aria-live="polite"` (sin interrumpir) / `"assertive"` (interrumpe) para toasts/validaciones async.

## Teclado / foco
Todo lo interactivo con Tab; orden lógico (no `tabindex` positivos). **Skip link** ("Saltar al contenido") primero.
**Focus management:** al abrir modal, mueve foco dentro y atrápalo (focus trap); al cerrar, devuélvelo al disparador. `tabindex="-1"` para foco programático, nunca `tabindex > 0`.

## Screen readers / contraste / formularios
**SR** (VoiceOver/NVDA/JAWS) leen el accessibility tree: "botón, Enviar, contraído". **Contraste:** texto normal
**4.5:1**, grande 3:1, componentes/foco 3:1. **Formularios:** cada input con `<label for>`; errores con
`aria-invalid="true"` + `aria-describedby`; agrupa con `<fieldset><legend>`; no solo color para error.
**`:focus-visible`** (foco solo para teclado): `button:focus-visible { outline: 2px solid #2563eb; outline-offset: 2px; }`. Nunca `outline: none` sin reemplazo.

## Testing
Automatizado (axe DevTools, Lighthouse) detecta ~30-40%; el resto **manual:** navega solo con teclado, prueba con un SR real, verifica zoom 200% y contraste.

## Gotchas
1. Quitar `outline` sin reemplazo deja a usuarios de teclado perdidos.
2. `role="button"` en `<div>` sin manejar `Enter`/`Space` y `tabindex` = botón roto para teclado.
3. Placeholder no es label; desaparece al escribir y suele fallar contraste.
4. `aria-live` agregado *después* de cargar no anuncia; debe existir en el DOM antes del cambio.
5. Modales sin focus trap dejan al usuario tabular detrás del overlay.
6. Lighthouse 100 ≠ accesible: no detecta orden de foco ilógico ni labels sin sentido.

**Fuentes:** w3.org/TR/WCAG22 · levelaccess.com (EAA) · developer.mozilla.org/Web/Accessibility/ARIA.
