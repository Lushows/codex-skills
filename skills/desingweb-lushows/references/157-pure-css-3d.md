# 157 — Pure CSS 3D (sin WebGL)

**CRAFT, code-heavy.** Léelo para card flip, cubos, coverflows, tilt, unfold — profundidad real sin WebGL. Pareja de 09 (modern CSS), 151 (parallax/3D-on-scroll), 81 (CSS art), 150 (micro-interacciones). Regla de oro: **CSS 3D es escena de planos (caras, tarjetas, paneles), no renderizado volumétrico; `perspective` en el PADRE, `preserve-3d` en cada nivel; ordena con `translateZ` real, no `z-index`.**

## 1. El modelo mental + setup mínimo

**`perspective`** define *cuánta* profundidad ves — va en el **padre** ("la cámara"; pequeño `400px` = dramático, grande `1500px` = casi isométrico). **`transform-style: preserve-3d`** le dice a un elemento "deja que mis hijos vivan en mi espacio 3D" (sin él, default `flat`, todo se aplana — **debe estar en cada nivel**). **`backface-visibility: hidden`** oculta la cara trasera al rotar >90°. **Coordenadas:** +X derecha, +Y abajo, +Z hacia el viewer (`translateZ(50px)` acerca). **El orden importa:** `translateZ(100px) rotateY(45deg)` ≠ `rotateY(45deg) translateZ(100px)` (el segundo rota el eje antes de empujar — esto explota cubos y anillos).
```css
.scene{ perspective:1000px; perspective-origin:50% 50%; }   /* la cámara */
.object{ transform-style:preserve-3d; transition:transform .6s cubic-bezier(.2,.8,.2,1); } /* el espacio 3D */
```

## 2. Card flip — el patrón canónico

```css
.card-scene{ perspective:1000px; }
.card{ position:relative; transform-style:preserve-3d; transition:transform .7s cubic-bezier(.2,.8,.2,1); }
.card__face{ position:absolute; inset:0; backface-visibility:hidden; -webkit-backface-visibility:hidden; }
.card__back{ transform:rotateY(180deg); }
.card-scene:hover .card{ transform:rotateY(180deg); }     /* hover */
.card-toggle:checked + .card{ transform:rotateY(180deg); } /* click sin JS, accesible */
.card:focus-visible{ outline:3px solid #4f8cff; outline-offset:4px; }
```
El hover-only NO es accesible: añade control por teclado (`<input>`/`<button>` con `aria-pressed`) y `:focus-visible`. `rotateY` = look "tarjeta", `rotateX` = "calendario que cae".

## 3. Cubo 3D — 6 caras

Cada cara se rota hacia su orientación y se empuja media-arista con `translateZ(half)` (cubo 200px → half 100px):
```css
.cube{ transform-style:preserve-3d; animation:spin 12s linear infinite; }
.cube__face{ position:absolute; inset:0; backface-visibility:hidden; }
.cube__face--front { transform:rotateY(0)    translateZ(100px); }
.cube__face--back  { transform:rotateY(180deg) translateZ(100px); }
.cube__face--right { transform:rotateY(90deg)  translateZ(100px); }
.cube__face--left  { transform:rotateY(-90deg) translateZ(100px); }
.cube__face--top   { transform:rotateX(90deg)  translateZ(100px); }
.cube__face--bottom{ transform:rotateX(-90deg) translateZ(100px); }
@keyframes spin{ from{transform:rotateX(-20deg) rotateY(0)} to{transform:rotateX(-20deg) rotateY(360deg)} }
```
Responsive: `translateZ(calc(var(--size)/2))`. Usos: loaders, packshots rotables, switchers de panel.

## 4. Carrusel / coverflow 3D — anillo

Ítems en círculo: cada uno rota `i*(360/n)` y se empuja por el radio `r=(width/2)/tan(180/n)`:
```css
.ring{ transform-style:preserve-3d; transition:transform .8s cubic-bezier(.2,.8,.2,1); }
.ring__item{ position:absolute; inset:0; backface-visibility:hidden;
  transform:rotateY(calc(45deg * var(--i))) translateZ(290px); }  /* n=8 → step 45deg, radio ~290 */
.ring{ transform:translateZ(-290px) rotateY(calc(-45deg * var(--active))); } /* JS setea --active */
```
El `translateZ(-290px)` retrocede la escena para que el ítem frontal quede en el plano. Control drag con `pointermove` (`angle += e.movementX*0.4`). Para coverflow plano: fila flex + laterales con `rotateY(±55deg) scale(.85)`.

## 5. 3D guiado por puntero y scroll

**Tilt con cursor:** `el.style.transform = \`perspective(900px) rotateY(${x*16}deg) rotateX(${-y*16}deg)\`` (de la posición relativa, reset en `pointerleave`). **Cards que rotan al entrar — CSS scroll-driven puro** (Chrome 115+, Safari 18+; `@supports` para degradar):
```css
@supports (animation-timeline: view()){
  .reveal-3d{ animation:rise linear both; animation-timeline:view(); animation-range:entry 0% cover 40%; }
  @keyframes rise{ from{opacity:0; transform:perspective(800px) rotateX(35deg) translateY(60px)} to{opacity:1; transform:perspective(800px) rotateX(0) translateY(0)} }
}
```
`view()` ata el progreso a la visibilidad del elemento; `scroll()` al scroll del contenedor (parallax por capas con distinto `translateZ`). Para secuencias con scrubbing fino y pin, GSAP ScrollTrigger sigue siendo más robusto.

## 6. Craft, performance & a11y

**Solo compositea `transform` y `opacity`** (animar `width`/`top`/`box-shadow`/`filter` saca del compositor, mata 60fps). **`will-change: transform` con disciplina** (decláralo justo antes, quítalo al terminar; permanente en muchos nodos consume VRAM). **Fix flicker/z-fighting:** `backface-visibility:hidden` + `translateZ(0)` para forzar capa GPU; en Safari añade prefijos `-webkit-` y `perspective` explícito en el padre. **Safari quirks reales:** ignora `overflow:hidden` para recortar hijos 3D transformados (recorta con un wrapper 2D externo); `z-index` no ordena fiable entre hermanos 3D (**ordena con `translateZ`**); evita `filter`/`backdrop-filter` dentro de `preserve-3d` (Safari aplana). **`prefers-reduced-motion`** obligatorio. **A11y de flip cards:** control real con teclado, `:focus-visible`, `aria-pressed`/`aria-expanded`; la cara oculta fuera del orden de tabulación (`inert`/`visibility:hidden`). **¿CSS o WebGL?** CSS basta para flips/cubos/coverflows/tilts/unfolds/parallax por capas; salta a WebGL para luces/sombras dinámicas, modelos importados, profundidad por-píxel, o >50 planos animados.

## CSS-3D anti-patterns — blacklist
**olvidar `preserve-3d` en un nivel intermedio** (la escena se aplana sin error) · **`perspective` en el mismo elemento que rota** (en vez del padre — se ve plano/raro) · **confiar en `z-index` para ordenar caras 3D** (usa `translateZ`; `z-index` no fiable en Safari) · **`will-change: transform` permanente y global** (fuga de memoria GPU) · **animar `top/left/width`** en vez de `transform` · **flip solo en `:hover`** sin foco/teclado · **omitir `backface-visibility:hidden`** en flips/cubos (cara trasera espejada + flicker) · **`overflow:hidden` para recortar hijos 3D** (no funciona en Safari) · **`backdrop-filter`/`filter` dentro de `preserve-3d`** (colapsa la escena en Safari) · **no incluir `@media (prefers-reduced-motion)`**.
