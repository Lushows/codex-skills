# 168 — Carruseles, scroll-snap & sliders

**CRAFT, code-heavy.** Pareja de 28 (search/nav), 151 (parallax), 162 (físico/drag), 39 (interacción). Regla de oro: **la pregunta de oro ANTES de escribir nada: ¿necesitas un carrusel? (NN/g: el slide 1 acapara ~84% de la interacción, el auto-rotate mata usabilidad). Si sí: galería simple → scroll-snap CSS; dots/flechas → CSS Carousel nativo + fallback; loop/autoplay → Embla; look de award → GSAP Draggable+Inertia.**

## 1. CSS scroll-snap (el baseline nativo)

Galería horizontal con momentum y snap, sin JS (universal desde 2019):
```css
.gallery{ display:flex; gap:1rem; overflow-x:auto; scroll-snap-type:x mandatory; /* mandatory obliga; proximity suave */
  scroll-padding-inline:1.5rem; scrollbar-width:none; }
.gallery > *{ flex:0 0 80%;            /* 80% => "peek" del siguiente */
  scroll-snap-align:center; scroll-snap-stop:always; } /* impide saltarse slides al flick rápido */
```
`scroll-padding-inline` = el truco del **peek**; `scroll-snap-stop:always` evita el "fast-flick skip" en móvil. Cubre el 80% de las galerías reales.

## 2. El CSS Carousel 2026 — dots + flechas en CSS puro (la gran noticia)

Chrome 135+ (mar 2025) y Safari 18.2+ traen carrusel completo sin JS (el navegador genera marcadores/botones focusables, con ARIA y keyboard-nav auto):
```css
.carousel{ display:flex; overflow-x:auto; scroll-snap-type:x mandatory; scroll-marker-group:after; }
.carousel > .slide{ flex:0 0 100%; scroll-snap-align:center; }
/* DOTS automáticos: un ::scroll-marker por hijo */
.carousel > .slide::scroll-marker{ content:""; width:12px; height:12px; border-radius:50%; border:2px solid currentColor; }
.carousel > .slide::scroll-marker:target-current{ background:var(--accent); } /* dot activo, sin IntersectionObserver */
.carousel::scroll-marker-group{ display:flex; gap:8px; justify-content:center; }
/* FLECHAS prev/next, auto-disabled en los bordes */
.carousel::scroll-button(left){ content:"←" / "Anterior"; }   /* el texto tras "/" es accesible */
.carousel::scroll-button(right){ content:"→" / "Siguiente"; }
.carousel::scroll-button(*):disabled{ opacity:.3; }
```
Bonus: **scroll-state container queries** para emfatizar el slide snapped (`@container scroll-state(snapped: x){ .slide-inner{ transform:scale(1) } }`). **Honestidad de soporte:** progressive enhancement — funciona como scroll-snap normal en Firefox, dots/flechas solo donde hay soporte; detecta con `@supports selector(::scroll-marker)`.

## 3. JS cuando hace falta — Embla vs Swiper

**Embla** (favorito 2026, ~3-7KB gz, cero deps, headless): drag momentum velocity-based, `dragFree` scroll continuo, loop real:
```js
const embla = EmblaCarousel(node, { loop:true, dragFree:false, align:'center', containScroll:'trimSnaps' });
embla.on('select', ()=>updateDots(embla.selectedScrollSnap()));
```
API imperativa (`scrollNext`/`scrollTo`/`selectedScrollSnap`) — tú construyes dots/flechas; wrappers React/Vue/Svelte oficiales. **Swiper** (~25-47KB) cuando piden coverflow 3D/thumbs/virtual slides/todo-ya-hecho (importa solo los módulos que uses).

## 4. Drag slider custom — el look de award (GSAP)

GSAP 100% gratis (incl. InertiaPlugin). Arrastre físico con snap a notches + skew por velocidad (la firma visual):
```js
gsap.registerPlugin(Draggable, InertiaPlugin);
Draggable.create(track, { type:"x", inertia:true,
  bounds:{ minX:-(slides.length-1)*slideW, maxX:0 }, snap:{ x:snaps }, // array de notches = snap-to-slide
  onDrag:applySkew, onThrowUpdate:applySkew });
function applySkew(){ const v = InertiaPlugin.getVelocity(track,"x")/80;
  gsap.set(slides, { skewX: gsap.utils.clamp(-20,20, v*0.05) }); }
```
Para transiciones WebGL de slide (distorsión pointer-reactiva, ref 143): renderiza cada slide a textura, pasa `uProgress`+`uVelocity` al fragment, GSAP tween al uniform.

## 5. Scroll-driven & efectos

CSS-first con scroll-state (§2) o parallax con `view-timeline`:
```css
.slide img{ animation:parallax linear both; animation-timeline:view(inline); animation-range:cover; }
@keyframes parallax{ from{ translate:-15% 0 } to{ translate:15% 0 } }
```
Active-slide emphasis con `@container scroll-state(snapped: x)`; barra de progreso con `animation-timeline:scroll(self inline)`; peek con `flex-basis<100%` + `scroll-padding`.

## 6. A11y & UX (el componente más fallado de la web)

**Keyboard** (←/→ entre slides, Tab al contenido; el CSS Carousel nativo ya lo da). **Roles** (`role="region"` + `aria-roledescription="carousel"`; cada slide `aria-roledescription="slide"` + `aria-label="2 de 5"`; dots `<button aria-label="Ir a slide 3">` con `aria-current`). **Live region** (`aria-live="polite"`, **`off` si autoplay** para no spamear lectores). **Focus** (slide oculto no tabbable — `inert`). **Pause-on-hover/focus** obligatorio si hay autoplay + botón Pausa visible (WCAG 2.2.2). **`prefers-reduced-motion`** (desactiva autoplay/transiciones). **Auto-rotate por defecto OFF**; si lo activas ≥5s, pausa al hover/focus, nunca en CTAs.

## Carousel anti-patterns — blacklist
**hero auto-rotativo con CTAs** (el patrón con peor ROI medido NN/g) · **auto-rotate <5s sin pausa** (viola WCAG 2.2.2) · **dots como única navegación** sin keyboard ni swipe · **`scroll-snap-type:x mandatory` en contenido largo/variable** (atrapa; usa `proximity`) · **slides ocultos tabbables** sin `inert`/`aria-hidden` · **reinventar drag físico a mano** con `mousemove` (usa Embla o GSAP Inertia) · **cargar Swiper completo (47KB)** para 3 logos (usa scroll-snap CSS, 0KB) · **ignorar `prefers-reduced-motion`** en parallax/skew · **confiar 100% en `::scroll-marker`** sin fallback Firefox · **`aria-live="polite"` con autoplay** (anuncia cada slide sin parar; `off`) · **sin `scroll-snap-stop:always`** en móvil (un flick salta 4 slides) · **infinite loop con CTAs paginables** ("12 de ∞").
