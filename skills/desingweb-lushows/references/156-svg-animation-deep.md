# 156 — SVG animation deep

**CRAFT, code-heavy.** Léelo para line-draw, path morphing, filtros SVG animados, MotionPath. Pareja de 23 (iconografía/SVG), 145 (kinetic type), 146 (gooey), 152 (anim libs). Regla de oro: **CSS para lo trivial, GSAP para coreografía (DrawSVG/MorphSVG/MotionPath ahora gratis); SMIL evítalo (deprecation incierta, sin timeline). Siempre `transform-box: fill-box` al rotar/escalar sub-paths.**

## 1. Por qué SVG y cómo elegir motor

SVG es la **capa premium de iconos/logos/ilustración** (resolution-independent, KB, DOM real scriptable, `currentColor`). **Decisión:** CSS (`@keyframes`/transitions) para loop simple/hover/draw básico; **GSAP** para secuencias, scrub, morph, motion-path, easing real; **SMIL** (`<animate>`) evítalo salvo microanimaciones aisladas (no se pausa/secuencia bien, deprecation amagada por Chrome). **Novedad 2026:** tras Webflow, **GSAP es 100% gratis incl. DrawSVG/MorphSVG/MotionPath**.

## 2. Line-draw — el efecto "dibujado a mano" (`stroke-dashoffset`)

Una línea es un patrón de guiones; si el guión mide todo el path y lo desplazas fuera de vista, el trazo "se dibuja". **El truco `pathLength`** elimina calcular `getTotalLength()`:
```html
<path class="draw" pathLength="1" d="M10,80 C40,10 90,10 120,80" stroke="currentColor" stroke-width="3"/>
```
```css
.draw{ stroke-dasharray:1; stroke-dashoffset:1; animation:draw 1.6s ease forwards; }
@keyframes draw{ to{ stroke-dashoffset:0; } }
@media (prefers-reduced-motion:reduce){ .draw{ animation:none; stroke-dashoffset:0; } }
```
**GSAP DrawSVG** (gratis, control total): `gsap.from(".logo path",{drawSVG:"0%", duration:1.2, stagger:0.12, ease:"power2.inOut"})`; desde el centro `gsap.fromTo("#sig",{drawSVG:"50% 50%"},{drawSVG:"0% 100%"})`; con ScrollTrigger para líneas que conectan nodos. **El gotcha `transform-box`:** si además rotas/escalas el path, el `transform-origin` por defecto usa el viewport SVG → el elemento "salta"; arréglalo SIEMPRE con `transform-box: fill-box; transform-origin: center` (bug silencioso #1).

## 3. Path morphing (forma A → forma B)

Interpolar `d` a mano falla salvo mismo número/tipo de comandos → plugins que rellenan/reordenan. **GSAP MorphSVG (gratis):**
```js
gsap.to("#bars", {morphSVG:"#cross", duration:.4, ease:"power2.inOut"}); // hamburguesa ↔ X
gsap.to("#play", {morphSVG:{shape:"#pause", shapeIndex:3}}); // shapeIndex resuelve el "twisting"
```
También convierte `<circle>/<rect>` a path auto (`MorphSVGPlugin.convertToPath`). **Alternativa sin GSAP: flubber** (`interpolate(pathA,pathB)` genera el `d` interpolado, animable con cualquier tweener). Casos: menu↔close, play↔pause, check de "añadido al carrito" — iconos que cambian de estado con identidad continua (no un cross-fade barato).

## 4. Filtros SVG animados (gooey, distort, wobble)

Animar parámetros de `<filter>` da efectos imposibles con CSS:
```js
gsap.to("#wobble feDisplacementMap", {attr:{scale:40}, yoyo:true, repeat:-1, duration:2});
gsap.fromTo("#wobble feTurbulence", {attr:{baseFrequency:0.008}}, {attr:{baseFrequency:0.02}, duration:3, yoyo:true, repeat:-1, ease:"sine.inOut"});
gsap.fromTo("#hue feColorMatrix", {attr:{values:0}}, {attr:{values:360}, duration:6, repeat:-1, ease:"none"}); // hue-shift
```
**⚠️ Coste CPU/GPU:** `feTurbulence`/`feDisplacementMap` se recalculan **por píxel, por frame** — los efectos más caros del navegador. Limítalos a zonas pequeñas, baja `numOctaves`, evita animarlos en scroll continuo; si la superficie es grande, canvas/WebGL.

## 5. MotionPath y elementos a lo largo de un path

```js
gsap.to("#rocket", { duration:4, repeat:-1, ease:"none",
  motionPath:{ path:"#flightPath", align:"#flightPath", alignOrigin:[0.5,0.5], autoRotate:true }});
```
`autoRotate:true` = orient-to-path (la nave apunta a donde va; offset angular `autoRotate:90`). **Texto sobre path** (nativo): `<textPath href="#curve" startOffset="0%">` + animar `startOffset` con `gsap.to("textPath",{attr:{startOffset:"100%"}, repeat:-1, ease:"none"})`.

## 6. Craft & performance

**Optimiza con SVGO/SVGOMG** (elimina metadata, precisión decimal excesiva `floatPrecision:2`) **pero conserva los `id`** que tus animaciones referencian y el `viewBox`. **Inline vs sprite vs `<img>`:** solo el SVG **inline** (o `<symbol>` sprite con `<use>`) es animable/estilable; `<img src=".svg">` y `background-image` quedan **opacos** (no tocas paths ni `currentColor`). **`currentColor`** (pinta `stroke="currentColor"` → hereda el `color` del contexto, un asset infinitos temas). **A11y:** decorativo `aria-hidden="true" focusable="false"`; significativo `role="img"` + `<title>`. **`transform-box: fill-box`** para cualquier rotación/escala de sub-elemento. **`prefers-reduced-motion`** (estado final estático; en GSAP `gsap.matchMedia()`).

## SVG-animation anti-patterns — blacklist
**animar `<img src=".svg">`/`background-image` y esperar tocar paths** (opaco, no hay DOM) · **olvidar `transform-box: fill-box`** al rotar/escalar (el "salto" por origin contra el viewport) · **calcular `getTotalLength()` a mano** cuando `pathLength="1"` lo normaliza gratis · **interpolar `d` entre paths con distinto número de comandos** sin MorphSVG/flubber · **ignorar `shapeIndex`** (morphs que se retuercen) · **`feTurbulence`/`feDisplacementMap` a pantalla completa en loop infinito** (termal-killer móvil) · **apostar el sitio a SMIL** para coreografías serias · **animar `width/height/x/y` de geometría** en vez de `transform` · **SVGO agresivo que borra los `id`** referenciados (animación rota tras "optimizar") · **sin `prefers-reduced-motion`** ni estado final estático · **decorativos sin `aria-hidden`** o significativos sin `<title>`/`role="img"`.
