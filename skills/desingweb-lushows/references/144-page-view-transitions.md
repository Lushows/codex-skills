# 144 — Page transitions & la View Transitions API

**CRAFT, code-heavy.** Léelo para el "app-like seamless feel" entre páginas, shared-element morph, curtain wipes. Pareja de 12 (frontier 2026), 09 (CSS moderno), 39 (interacción), 34 (Motion React). Regla de oro: **`@view-transition { navigation: auto }` de 3 líneas resuelve el 80%; usa GSAP/Barba solo cuando necesitas control total; SIEMPRE progressive enhancement + `prefers-reduced-motion`.**

## 1. Por qué importan

En una MPA cada navegación es un *flash blanco* — ese parpadeo es la firma de lo "template". Lo que separa premium de genérico es la **continuidad** (el contenido persiste, se transforma, fluye → el cerebro lo lee como *una app cohesiva*). El win clave es **perceived performance**: una transición de 300-400ms ocupa el "tiempo muerto" de navegación y enmascara el repaint → la carga se siente *instantánea* aunque el tiempo real sea idéntico.

## 2. The View Transitions API (la forma 2026)

Dos modos, mismo mecanismo (snapshot viejo + nuevo, superpuestos como pseudo-elementos). **Cross-document/MPA** ya shippea en Chrome/Edge 126+, Safari 18.2+, Firefox parcial. **Setup MPA (cero JS)** — en CSS de AMBAS páginas same-origin:
```css
@view-transition { navigation: auto; }
::view-transition-old(root){ animation: 320ms cubic-bezier(.4,0,.2,1) both fade-slide-out; }
::view-transition-new(root){ animation: 320ms cubic-bezier(.4,0,.2,1) both fade-slide-in; }
@keyframes fade-slide-out{ to{ opacity:0; transform:translateY(-12px); } }
@keyframes fade-slide-in { from{ opacity:0; transform:translateY(12px); } }
```
**Setup SPA (JS):**
```js
function navigate(updateDOM){
  if(!document.startViewTransition){ updateDOM(); return; } // fallback
  document.startViewTransition(() => updateDOM());
}
```
**Árbol de pseudo-elementos:** `::view-transition` → `::view-transition-group(name)` → `::view-transition-image-pair(name)` → `::view-transition-old(name)` + `::view-transition-new(name)`. Cada `view-transition-name` único genera su grupo animable. **View transition types (2026):** distingue dirección sin clases manuales — `document.startViewTransition({update, types:['forward']})` + `html:active-view-transition-type(forward) ::view-transition-old(root){...}`. En cross-document léelos en `pageswap`/`pagereveal`.

## 3. Shared-element transitions (el morph)

La técnica estrella: un thumbnail de grilla se **expande** hasta volverse el hero del detalle. El navegador lo hace solo si AMBOS comparten `view-transition-name`:
```css
/* grid */   .card-img[data-id="42"]{ view-transition-name: hero-42; }
/* detail */ .hero-img             { view-transition-name: hero-42; }
```
El navegador interpola posición, tamaño, border-radius y cross-fade del contenido. **Gotchas críticas:** (1) **nombres únicos por snapshot** (dos elementos con el mismo `view-transition-name` *visibles a la vez* = la transición se aborta sin error; asigna el nombre solo al clicado), (2) **layout shift = morph roto** (reserva `aspect-ratio`/`width`/`height` en el hero o salta cuando la imagen carga), (3) un ancestro con `overflow:hidden` puede recortar el snapshot, (4) no animes `width/height` con texto (distorsiona; morph solo en media).

## 4. El approach JS clásico (sigue siendo necesario)

Para control total (curtain wipes, clip-path secuenciado, legacy, interceptar fetch+swap): barba.js o un router propio con GSAP. **Curtain con clip-path + GSAP:**
```js
barba.init({ transitions: [{
  async leave(){ await gsap.fromTo(overlay,
    {clipPath:'inset(100% 0 0 0)'}, {clipPath:'inset(0% 0 0 0)', duration:.6, ease:'power4.inOut'}); }, // cortina sube y cubre
  async enter(data){ gsap.set(data.next.container,{opacity:1});
    await gsap.to(overlay, {clipPath:'inset(0 0 100% 0)', duration:.6, ease:'power4.inOut'}); } // sale por arriba
}]});
```
`leave` corre antes de inyectar el nuevo HTML; `enter` después. Variantes: `inset()` para wipes lineales, `circle()` para reveals radiales desde el cursor.

## 5. FLIP technique

**First-Last-Invert-Play:** mides la posición inicial (First), aplicas el cambio de layout (Last), aplicas un transform inverso (Invert), animas el transform a cero (Play). **GSAP Flip es 100% gratis:**
```js
const state = Flip.getState('.card');     // First
grid.classList.toggle('expanded');         // Last (CSS cambia layout)
Flip.from(state, {duration:.6, ease:'power2.inOut', absolute:true});
```
**FLIP vs View Transitions:** View Transitions para transiciones *de navegación* (page→page, cross-document; menos código, lo hace el navegador). FLIP para reordenamientos *dentro de la misma página* (filtrar/ordenar grid, expandir cards, masonry reflow) donde necesitas control frame-by-frame/stagger, o como fallback.

## 6. Performance, fallback y a11y

**Progressive enhancement** (nunca bloquees navegación esperando la transición): `if(!document.startViewTransition){ updateDOM(); return; }`. En MPA `@view-transition` se ignora silenciosamente sin soporte (degradación automática, sin polyfill). **`prefers-reduced-motion` obligatorio:**
```css
@media (prefers-reduced-motion: reduce){
  ::view-transition-group(*),::view-transition-old(*),::view-transition-new(*){ animation: none !important; }
}
```
**Performance:** los pseudo-elementos se animan en el compositor (transform/opacity, 60fps sin main thread), pero no nombres *demasiados* elementos (cada `view-transition-name` = snapshot = costo de memoria/raster; limita a 1-3 shared + root; no animes `width`/`top`). **Frameworks:** Astro (`<ClientRouter />` + `transition:name`/`transition:animate`), Next App Router (`<ViewTransition>` experimental + flag), SvelteKit (`onNavigate` + `document.startViewTransition`).

## Page-transition anti-patterns — blacklist
**bloquear navegación** detrás de la animación sin fallback · **transiciones largas** (>500ms) en navegación recurrente (250-400ms) · **ignorar `prefers-reduced-motion`** (náusea vestibular real) · **mismo `view-transition-name` en múltiples elementos visibles** (la transición se aborta sin error) · **overlays full-screen opacos** que esconden contenido ya cargado (matan perceived-performance) · **no reservar dimensiones del destino** en shared-element morphs (el hero "salta" al cargar) · **animar `width/height/top/left`** en vez de `transform/opacity/clip-path` · **cortinas en cada clic interno** (tabs, acordeones — reserva transiciones para cambios de página reales) · **cargar GSAP+Barba** cuando `@view-transition{navigation:auto}` de 3 líneas resuelve el 80% · **olvidar same-origin** (cross-document VT solo funciona same-origin).
