# 170 — Web Animations API & native scroll-driven

**CRAFT, code-heavy.** La capa de motion sin librería (cero KB, compositor). Pareja de 07/12 (motion/frontier), 151 (parallax), 152 (anim libs), 160 (reveal). Regla de oro: **native (WAAPI + CSS scroll-driven) es el baseline 2026 para reveals/parallax/progress; GSAP solo cuando necesitas timelines orquestadas, scrub con smoothing o plugins. NUNCA `scroll` listener + rAF leyendo `scrollY` (jank en main thread).**

## 1. Por qué native

WAAPI + CSS scroll-driven son baseline (Chromium 115+, Safari 18+/26, Firefox tras flag, ~85%). Las scroll-driven viven **fuera del main thread** (compositor) → un parallax no se rompe aunque tu JS bloquee. Cero deps, cero bundle, cero `rAF` manual leyendo `scrollY` (el anti-patrón clásico que causa jank/layout thrashing). **Native gana** en reveals, progress bars, parallax, stagger simple, fades. **GSAP gana** en timelines orquestadas (offsets relativos `-=0.3`), scrub con inercia/smoothing, morphing SVG, `pin` con snapping complejo, plugins. Punto medio para spring/stagger sin el peso de GSAP: **Motion** (ex-Motion One, ~5KB, wrapper fino sobre WAAPI).

## 2. WAAPI core

```js
const anim = el.animate(
  [{ transform:'translateY(20px)', opacity:0 }, { transform:'translateY(0)', opacity:1 }],
  { duration:600, easing:'cubic-bezier(.2,.8,.2,1)', fill:'both', delay:100 });
anim.pause(); anim.play(); anim.reverse(); anim.cancel();
anim.playbackRate = 2;          // velocidad en caliente (negativo = atrás)
anim.currentTime = 300;          // scrub manual en ms
await anim.finished;             // Promise → encadenar secuencias
```
**`commitStyles()` + `fill`:** sin `fill:'forwards'` el elemento salta a su base al terminar; mejor `fill:'none'` + al `finish` `commitStyles()` (escribe los computados inline) + `cancel()` (no acumulas animaciones "fill" colgadas que bloquean cambios futuros). **Composite modes:** `composite:'add'` apila un "wobble" sobre un "translate" base sin pisarlos (imposible en CSS puro). **`getAnimations()`** para auditar/limpiar (`el.getAnimations().forEach(a=>a.cancel())`). **Keyframes dinámicos desde JS** (la ventaja real sobre CSS): generar valores en runtime.

## 3. CSS scroll-driven (native, sin JS)

Dos timelines: **`scroll()`** (progreso = posición de scroll del contenedor) y **`view()`** (progreso = visibilidad del elemento). **Progress bar:**
```css
@keyframes grow{ from{ transform:scaleX(0) } to{ transform:scaleX(1) } }
.progress{ transform-origin:left; animation:grow linear; animation-timeline:scroll(root block); }
```
**Reveal al entrar:**
```css
@keyframes reveal{ from{ opacity:0; translate:0 40px } to{ opacity:1; translate:0 0 } }
.card{ animation:reveal linear both; animation-timeline:view(); animation-range:entry 0% cover 40%; }
```
`animation-range` usa los range-names: **`cover`** (recorrido completo), **`entry`** (entrando), **`exit`** (saliendo), `contain`, `entry-crossing`, `exit-crossing`. **Parallax (named view-timeline linkeando dos elementos):** `.hero-img{ view-timeline-name:--img } .hero-bg{ animation:drift linear; animation-timeline:--img; animation-range:cover }` — un elemento usa el timeline de otro sin JS. **Sticky-stack:** cada card `position:sticky; top:0` + animación de `scale`/`opacity` con `animation-range:exit`.

## 4. WAAPI + ScrollTimeline (JS, control programático)

Cuando necesitas el timeline scroll-driven con lógica JS:
```js
const tl = new ScrollTimeline({ source:document.documentElement, axis:'block' });
el.animate({ transform:['translateY(0)','translateY(-200px)'] }, { timeline:tl, fill:'both' }); // sin duration: el scroll ES el reloj
const vt = new ViewTimeline({ subject:card, axis:'block' });
card.animate({ opacity:[0,1] }, { timeline:vt, rangeStart:'entry 0%', rangeEnd:'cover 50%' });
```
Polyfill `scroll-timeline` de Bramus para Firefox si necesitas la versión JS.

## 5. Híbrido & ergonomía

**Motion** (`npm i motion`, ~5KB) cuando quieras springs/stagger sin reimplementar: `animate('.item', { y:[20,0], opacity:[0,1] }, { type:'spring', stiffness:300, delay:stagger(0.05) })` (springs y stagger no existen en WAAPI puro). **Reusar `KeyframeEffect`** entre elementos (DRY + menos GC): `const e = effect.clone(); e.target = n; new Animation(e, document.timeline).play()`. Regla: **WAAPI crudo** para una/dos transiciones imperativas; **CSS scroll-driven** para todo lo declarativo ligado a scroll; **wrapper** solo cuando pidas spring/stagger/orquestación.

## 6. Perf, soporte y a11y

**Solo props del compositor** (`transform`/`opacity`/`filter`; nunca `top`/`left`/`width`/`height`/`margin`). **Fallback con `@supports`** (el estado base debe ser el visible):
```css
.card{ opacity:1; }
@supports (animation-timeline: view()){ .card{ animation:reveal linear both; animation-timeline:view(); animation-range:entry cover 30%; } }
```
**`prefers-reduced-motion` obligatorio** (`@media (prefers-reduced-motion:reduce){ *,.card{ animation:none!important } }`; en JS `if(matchMedia('(prefers-reduced-motion:reduce)').matches) return`). **Cleanup:** al desmontar `el.getAnimations().forEach(a=>a.cancel())` (las `fill` colgadas y timelines pinneados a nodos removidos filtran memoria).

## WAAPI/scroll-driven anti-patterns — blacklist
**`scroll` listener + rAF leyendo `scrollY`** para parallax (el error #1: main thread, jank; usa `animation-timeline:scroll()`) · **animar `top`/`left`/`width`/`height`** (layout/paint cada frame) · **`fill:'forwards'` permanente** sin `commitStyles()`+`cancel()` (acumula animaciones colgadas que bloquean cambios de estilo) · **no `@supports` fallback** (en Firefox-sin-flag el contenido queda invisible con `opacity:0`) · **ignorar `prefers-reduced-motion`** · **`view-timeline` en un elemento `display:none`/colapsado** (timeline sin rango, animación muerta silenciosa) · **animar `box-shadow`/`background-color`** en scroll (no compositan; usa pseudo con `opacity`) · **`element.animate` en un `forEach` de cientos de nodos** sin clonar `KeyframeEffect` (presión de GC; mejor CSS `view()`) · **alcanzar GSAP para un fade-on-scroll** (50KB+ para 4 líneas de CSS nativo) · **olvidar `axis`/`source`** en `scroll()` cuando el scroller no es el root.
