# 81 — Advanced CSS art & pure-CSS craft

Complementa 41 (arte generativo canvas/JS) y 09/12 (modern CSS): **aquí CSS puro como medio artístico** — lo que puedes hacer SIN JavaScript, las técnicas CSS-only de vanguardia. El CSS-only art no es nostalgia: es **rendimiento + accesibilidad + degradación elegante por construcción** (no bloquea el main thread, corre en el **compositor/GPU**, cae a un estado base usable si una feature falta). **Léelo para decoración procedural, micro-ilustración, fondos vivos, efectos sin librerías.** Pareja de 09/12 (CSS), 41 (generativo), 39 (craft), 40 (performance). Regla de oro: **si CSS ya lo hace nativo, no metas una librería — pero conoce el límite (datos/miles de partículas → canvas).**

## 1. Filosofía: por qué el craft en CSS puro

La doctrina central es **constraint-as-creativity.** Lynn Fisher (`a.singlediv.com`) y el reto **Divtober** imponen una regla brutal —un solo `<div>`— y de esa restricción nace virtuosismo. El hallazgo clave (Miriam Suzanne observando a Fisher): el single-div art **no es pixel-art con `box-shadow`**, sino capas de `background` gradients sofisticadamente posicionados/dimensionados. **Cuándo CSS-only gana a JS/canvas:** decoración procedural (patrones, texturas, fondos animados), micro-ilustración donde "un SVG se siente apenas demasiado pesado", componentes de librería ligeros y temables. **Cuándo NO:** lógica de datos, animación dependiente de input complejo, escenas con miles de partículas (canvas/WebGL gana). La disciplina es saber el límite.

## 2. Gradientes, shapes y backgrounds como arte

El **layering de backgrounds** es el corazón: una sola propiedad `background` acepta múltiples capas (coma), cada una con gradiente, `background-size` y `background-position`:
```css
background:
  radial-gradient(circle at 30% 20%, #fff 0 8%, transparent 9%),  /* highlight */
  conic-gradient(from 45deg, #e63 0 90deg, #d52 0 180deg, ...),    /* facetas */
  linear-gradient(180deg, #2a1 0%, #061 100%);                      /* base */
```
- **`conic-gradient`** → pétalos, abanicos, pies, facetas geométricas. **`radial-gradient`** con stops duros (`#fff 0 8%, transparent 9%`) → círculos sólidos, lunares, ojos, burbujas. **Patrones tileables:** gradientes repetidos con `background-size:40px 40px` (polka dots, rayas, chevron) sin una imagen.
- **Color moderno (2026):** **OKLCH** da interpolación perceptualmente uniforme (sin "gris muerto" del medio): `linear-gradient(in oklch longer hue, ...)` para auroras · **`color-mix()`** (`color-mix(in oklch, var(--brand) 70%, black)`) · **relative color** (`oklch(from var(--brand) calc(l*.8) c h)` deriva toda una paleta de un token).
- **Shapes con `clip-path`:** `polygon()` (flechas, estrellas, siluetas), `path()` (curvas Bézier), `circle()`/`ellipse()`. Con pseudo-elementos (`::before`/`::after`) tienes **tres capas pintables por elemento**.
- **Mesh/aurora/grain sin JS:** aurora = varios `radial-gradient` difusos con `background-blend-mode:screen` animando `background-position`; **grain/noise** = SVG `feTurbulence` como data-URI en `background-image` o capa con `mix-blend-mode:overlay` baja opacidad.

## 3. El toolkit CSS moderno (2026)

- **Scroll-driven animations:** `animation-timeline` vincula keyframes al scroll **en el compositor** (sin scroll listeners JS): `view-timeline-name` + `animation-range: entry 0% cover 50%`.
- **`@property`** — habilitador de gradientes animados (registra un custom prop tipado para que el navegador lo **interpole**): `@property --angle { syntax:"<angle>"; inherits:false; initial-value:0deg; }` + animar `--angle` en un `conic-gradient`.
- **`:has()`** — estado sin JS (`.card:has(:checked)`, `form:has(input:invalid)`, parent/sibling selection).
- **View Transitions** (`@view-transition`) — morphing entre estados/páginas declarativo. **`@scope`** — encapsula sin colisiones. **Anchor positioning** — tooltips/popovers atados a un ancla. **`@starting-style`** — estado inicial de entrada (toasts, modales).
- **Tipografía:** `text-wrap:balance` (titulares), `text-wrap:pretty` (sin huérfanas), `field-sizing:content`. **Glass:** `backdrop-filter:blur() saturate()`; blend modes (`mix-blend-mode`). **Emergente:** `sibling-index()` para stagger declarativo, `attr()` tipado, CSS `if()`.

## 4. Animación y motion en CSS puro

**Choreography:** `@keyframes` + `animation-delay` escalonado; en 2026 **stagger declarativo** vía `calc(sibling-index() * 60ms)`. **Custom props animadas** (con `@property`) son la palanca (anima `--x`/`--hue`/`--angle`, deriva transforms/colores de una variable). **3D scenes:** `transform-style:preserve-3d` + `perspective` + `rotateX/Y/Z` + `translateZ` (cubos, carruseles, flip cards, dioramas — profundidad real). **Easing artistry:** `cubic-bezier()` custom y **`linear()`** (easing de múltiples puntos — bounces/springs sin JS); `steps(n)` para frame-a-frame (sprites, máquina de escribir). **Loaders CSS-only:** `conic-gradient` enmascarado rotando, dots con `animation-delay` desfasado. **Hover/focus craft:** transiciones sobre `transform`/`opacity`/`filter`, magnetic con custom props, reveals con `clip-path`.

## 5. Houdini, filtros SVG y la frontera

- **CSS Paint API (Houdini):** worklets JS que pintan directo en `background`/`border`/`mask`, **off-main-thread** (patrones procedurales sin DOM extra ni imágenes). Soporte: Chromium nativo; Firefox/Safari vía `css-paint-polyfill` (GoogleChromeLabs). La **Properties & Values API** (`@property`) sí es ampliamente soportada — es lo que más se usa en prod. La Layout API sigue experimental, no la uses en prod.
- **SVG filters en CSS:** `filter: url(#turbulence)` con `feTurbulence` (grain, papel, nubes, distorsión) y `feDisplacementMap` (ondas, vidrio, heat-haze).
- **Gooey effect:** combo `filter:blur()` + `feColorMatrix` (sube el contraste del alpha) → blobs metaball que se fusionan. **Masks:** `mask-image` con gradientes o SVG (fades, recortes de texto, reveals); `mask-composite`.
**Honestidad de soporte:** scroll-driven animations, anchor positioning y `@scope` están en Chromium estable y llegando a Firefox/Safari en 2025-26. Trátalos siempre como **enhancement** tras `@supports`, nunca como base.

## 6. Craft, performance & 2026

El **renacimiento CSS** de 2026 movió a nativo lo que durante una década exigía JS (scroll animation, estado, positioning, transiciones de página). **Performance:** anima **solo props del compositor — `transform`, `opacity`, `filter`, `clip-path`** (GPU, fluidas aunque el main thread esté ocupado); evita animar `width/height/top/left/margin` (disparan layout/paint); `will-change` **con moderación** (cada hint crea una capa de compositor que consume memoria — ponlo justo antes de animar, quítalo después).
**A11y (no negociable):**
```css
@media (prefers-reduced-motion: reduce){
  *,::before,::after{ animation-duration:.01ms!important; animation-iteration-count:1!important; transition-duration:.01ms!important; }
}
```
Toda decoración con `aria-hidden="true"`, nunca transmitir información solo por color/movimiento.

## CSS-art anti-patterns — blacklist
**animar `width/height/top/left/margin`** en loops (layout thrashing, jank) · **`will-change` global o permanente** (explosión de capas, memoria agotada, scroll lento) · **cero `prefers-reduced-motion`** (mareo, infracción WCAG 2.3.3, daño vestibular real) · **decoración sin `aria-hidden`** (lectores anuncian basura) · **gimmick sobre craft** (el tech-demo de 200 `@keyframes` que nadie nota — arte que sirve al diseño > alarde) · **reinventar en CSS lo que debe ser SVG/canvas** (ilustración de detalle fino = SVG; miles de partículas = canvas) · **ignorar soporte de navegador** (anchor positioning / Paint API como base sin `@supports` ni fallback) · **`box-shadow` pixel-art masivo** (cientos de sombras = paint costoso) · **`backdrop-filter` apilado** sobre superficies grandes (coste de blur por frame).
