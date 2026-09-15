# 331 · Accesibilidad a fondo (WCAG 2.2/3, ARIA, teclado, screen-readers, testing)

> La accesibilidad no es un checklist al final: es HTML semántico desde la primera línea. El 90% se
> resuelve sin ARIA, usando el elemento correcto. ARIA es el parche cuando no hay elemento nativo.

## Estado de los estándares (2026)
- **WCAG 2.2** es el estándar vigente: Recommendation desde oct 2023, **ISO internacional desde oct 2025**.
  Es lo que auditan y exigen las leyes hasta ≥2028. [verificado 2026]
- **WCAG 3.0** sigue en Working Draft (mar 2026: 174 requirements, modelo no binario). 4-5 años de ser
  requisito legal — planifica sobre 2.2, no esperes a 3.0. [verificado 2026]
- Nivel objetivo legal habitual: **AA**.

## Lo nuevo de 2.2 que muerde en diseño
| SC | Regla | Implicación |
|---|---|---|
| **2.5.8 Target Size (AA)** | Targets ≥ **24×24 CSS px** o espaciado equivalente (círculo 24px no toca otro) | Botones/íconos pequeños fallan; sube hit-area [verificado 2026] |
| **2.4.11 Focus Appearance (AA)** | Indicador de foco visible, tamaño y contraste mínimos | No mates el `:focus`; outline contrastado [verificado 2026] |
| **2.4.13 Focus Not Obscured (AA)** | El elemento enfocado no queda tapado por sticky headers/cookie bars | Ajusta scroll-margin |
| **3.2.6 Consistent Help** | Ayuda en el mismo lugar entre páginas | — |
| **3.3.8 Accessible Authentication** | No exigir resolver puzzles/recordar para autenticar | Permite paste de password, no captchas cognitivos |

## Las 4 reglas raíz (POUR) en lo concreto
- **Perceivable**: contraste texto ≥ 4.5:1 (3:1 para texto grande ≥24px/18.66px bold y para UI/foco);
  `alt` con sentido (vacío `alt=""` si es decorativo); no transmitir info solo por color.
- **Operable**: todo accesible por teclado; sin trampas de foco; target 24px; tiempo ajustable.
- **Understandable**: labels claros, errores descritos en texto, comportamiento predecible.
- **Robust**: HTML válido, roles/estados expuestos correctamente a la API de accesibilidad.

## HTML semántico primero (el 90%)
- `<button>` para acciones, `<a href>` para navegar. NUNCA `<div onclick>` (no es focuseable ni anunciado).
- Landmarks: `<header><nav><main><aside><footer>`. Un solo `<main>`. Headings jerárquicos sin saltos (h1→h2→h3).
- `<label for>` ligado a cada input; `<fieldset>/<legend>` para grupos de radios.
- Listas reales `<ul>/<ol>`, tablas con `<th scope>`. El lector de pantalla narra la estructura nativa.

## ARIA: úsalo solo cuando no hay nativo
- **Primera regla de ARIA**: si existe un elemento HTML que lo hace, úsalo en vez de ARIA.
- Patrones que SÍ requieren ARIA (no tienen elemento nativo): tabs, combobox/autocomplete, tree, dialog
  modal, menu, disclosure → sigue **WAI-ARIA Authoring Practices** (roles + estados + teclado exactos).
- `aria-label`/`aria-labelledby` para nombrar; `aria-expanded`, `aria-selected`, `aria-current` para estado;
  `aria-live="polite"` para anuncios dinámicos (toasts, resultados de búsqueda).
- ARIA mal puesto es PEOR que nada: `role` falso o estado desincronizado confunde al lector. No pongas
  `role="button"` a un `<button>`.

## Teclado y foco
- Orden de tab = orden visual/DOM lógico. Evita `tabindex` positivo. `tabindex="0"` solo para custom widgets;
  `tabindex="-1"` para foco programático (mover foco al abrir modal, devolverlo al cerrar).
- **Focus trap** en modales (Tab cicla dentro); Esc cierra; foco vuelve al disparador.
- `:focus-visible` para outline solo en navegación por teclado; nunca `outline:none` sin reemplazo.
- Skip-link "Saltar al contenido" como primer elemento focuseable.

## Testing (automático NO basta)
- **Automático** (cubre ~30-40%): axe-core / `@axe-core/playwright`, Lighthouse, eslint-plugin-jsx-a11y en CI.
- **Manual** (lo demás): navega solo con Tab/Shift-Tab/Enter/Esc/flechas; verifica foco visible siempre.
- **Screen readers reales**: NVDA+Firefox (Win), VoiceOver+Safari (Mac/iOS), TalkBack (Android). Probar 1 mín.
- Zoom 200% sin pérdida de contenido; reflow a 320px; `prefers-reduced-motion` respetado.
- Verifica contraste con DevTools/Stark; revisa que el foco no quede tapado (2.4.13).

Cruza con [[70-accesibilidad-a11y-wcag]].
