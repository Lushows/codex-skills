# 162 — Physics & spring-based interactions

**CRAFT, code-heavy.** Léelo para springs, drag-throw con inercia, Matter.js, momentum, "follow with lag". Pareja de 34 (Motion React), 39 (interacción/draggable), 152 (anim libs), 04 (motion library). Regla de oro: **springs/momentum son interrumpibles (conservan velocidad) → se sienten vivos; los tweens con duración fija "saltan" al interrumpir. Física para drag/hover/toggles; control de tiempo para loaders/secuencias.**

## 1. Por qué la física se siente "viva"

Una animación **time-based** (duración fija + easing) viola la intuición física: siempre tarda 300ms sin importar distancia/velocidad/interrupción → se siente "mecánica". Una **physics-based** (spring/momentum) define *fuerzas y propiedades del material*; el tiempo de llegada **emerge** del estado. La clave técnica es la **interrumpibilidad:** un tween con duración necesita reiniciarse o saltar al interrumpirlo (el glitch al hover-out antes de terminar el hover-in); un spring conserva la **velocidad** en el momento de la interrupción y la usa como condición inicial → transición continua. **Usa física:** drag/throw, hover/press, toggles, sheets/modales, listas que se reordenan — cualquier cosa interrumpible. **NO:** loaders deterministas, secuencias coreografiadas con timing exacto.

## 2. Spring math (el núcleo)

Oscilador armónico amortiguado: `F = -k·x - c·v` (Hooke + damping), `a=F/m`. **`stiffness` (k)** = rigidez (más alto = más rápido/agresivo). **`damping` (c)** = fricción (más alto = menos oscilación; más bajo = rebote). **`mass` (m)** = inercia. El **damping ratio** `ζ = c/(2·√(k·m))`: `ζ<1` underdamped (rebota = "bouncy"), `ζ=1` critically damped (rápido SIN rebote = "snappy" ideal), `ζ>1` overdamped (lento/arrastrado).
```jsx
import { motion, useSpring } from "motion/react";  // ex-Framer Motion, ahora motion/react
<motion.div animate={{x:100}} transition={{type:"spring", stiffness:400, damping:30, mass:1}} />
// API por sensación: transition={{type:"spring", duration:0.5, bounce:0.25}}  (bounce 0 = sin rebote)
const x = useSpring(0, {stiffness:300, damping:30}); x.set(200); // persigue con física, interrumpible
```
**Configs de referencia:** SNAPPY `{stiffness:500, damping:32}` (botones/toggles), GENTLE `{stiffness:120, damping:20}` (sheets/modales), BOUNCY `{stiffness:600, damping:15}` (celebración), STIFF `{stiffness:700, damping:40}` (UI densa). **Vocabulario:** react-spring usa `tension`=stiffness / `friction`=damping — NO copies números entre librerías sin convertir.

## 3. Drag-throw con inercia — GSAP Draggable + InertiaPlugin

**GSAP 3.13 hizo TODOS los plugins gratis (abril 2025), incluido InertiaPlugin** (antes ThrowPropsPlugin, solo Club). Draggable mide la velocidad del gesto; al soltar, InertiaPlugin desacelera con física y aterriza en `bounds`/`max-min`/`snap`:
```js
Draggable.create(".card", { type:"x", inertia:true, bounds:".track",
  edgeResistance:0.65, dragResistance:0.05,
  snap:{ x:(v)=>Math.round(v/320)*320 },  // notches de 320px (carrusel)
  onThrowComplete(){ /* settle: actualizar índice */ }});
// Knob rotatorio: type:"rotation", inertia:true, snap:(v)=>Math.round(v/30)*30
```
~12 líneas que reemplazan cientos de cálculo manual de velocidad.

## 4. Matter.js — rigid-body physics

Para el hero "las cosas caen, se apilan y rebotan" (marcas playful, 404s con personalidad). **El truco de craft: NO uses `Matter.Render`** (canvas crudo feo) — corre el motor headless y mapea `body.position`/`body.angle` a `transform` de elementos HTML reales (conservas texto seleccionable, imágenes nítidas, CSS):
```js
const engine = Engine.create();
const bodies = els.map((el,i)=>{ const r=el.getBoundingClientRect();
  return Bodies.rectangle(W/2+i*10, -100*i, r.width, r.height, {restitution:0.6, friction:0.3, chamfer:{radius:12}}); });
Composite.add(engine.world, [...walls, ...bodies]); // walls = floor + left + right isStatic
Composite.add(engine.world, MouseConstraint.create(engine, {mouse, constraint:{stiffness:0.2}})); // drag
Runner.run(Runner.create(), engine);
// sync cada frame: els[i].style.transform = `translate(${b.position.x-w/2}px,${b.position.y-h/2}px) rotate(${b.angle}rad)`
```
**Cuándo:** delight de marca, NO UI funcional (nunca metas física de colisiones en algo que el usuario *necesita* operar).

## 5. Soft/elastic, momentum scroll y "follow with lag"

**Magnetic button** (sigue al cursor, vuelve con spring): `pointermove` → `gsap.to(btn,{x:mx*0.4, y:my*0.4, duration:.6, ease:"power3.out"})`; `pointerleave` → `gsap.to(btn,{x:0,y:0, ease:"elastic.out(1,0.3)"})` (el snap-back). **Momentum scroll con Lenis:** `new Lenis({lerp:0.1, smoothWheel:true})` + `lenis.on("scroll", ScrollTrigger.update)`. **"Follow with lag" — el lerp como física barata** (80% de la sensación sin motor): `x += (target-x)*0.1` cada frame (un spring overdamped sin oscilación; 0.08-0.15 para cursors/parallax). La "velocidad" instantánea `target-x` alimenta skew/scale: `img.style.transform = \`translateX(${x}px) skewX(${(target-x)*0.05}deg)\``.

## 6. Performance & taste

**Costo del loop** (60-120/s; anima SIEMPRE `transform`/`opacity`, nunca `top/left/width` = reflow/jank). **Cap de cuerpos Matter** (colisiones O(n²); <~40 activos, `engine.enableSleeping=true`, `Composite.remove` los que salen del viewport). **Un solo rAF** (no un loop por componente; un ticker global; cancela con IntersectionObserver). **`prefers-reduced-motion`** (desactiva springs bouncy, autoplay físico, momentum exagerado; `if(reduce) lenis.destroy()`). **A11y del drag:** un control draggable NUNCA es la única vía (teclado `Arrow keys`, no atrapes el foco, `role="slider"` + `aria-valuenow`, fallback prev/next). **Delight vs gimmick:** la física es delight cuando *refuerza* la affordance (un toggle que rebota confirma el cambio); gimmick cuando *retrasa la tarea* (logos cayendo que tapan el CTA, momentum tan lento que pelea con el usuario).

## Physics anti-patterns — blacklist
**spring sin damping suficiente en UI funcional** (un botón que rebota 5 veces marea; bouncy solo para celebración) · **momentum scroll lento que pelea con el usuario** (lerp <0.06; nunca en páginas largas de lectura) · **animar `top/left/width/height` en el loop** (reflow por frame) · **Matter.js para UI que el usuario debe operar** (física impredecible) · **tween con duración fija para hover/press** (se rompe al interrumpir; usa spring) · **no respetar `prefers-reduced-motion`** · **drag sin alternativa de teclado / sin bounds** · **un rAF loop por componente** (centraliza en un ticker) · **demasiados cuerpos Matter sin `sleeping` ni culling** · **`elastic.out` con amplitud alta en transiciones de página** (overshoot gigante barato) · **confundir vocabularios** (react-spring `tension`/`friction` vs Motion `stiffness`/`damping`) · **inercia infinita sin fricción** (throw que no frena; define `bounds`/resistencia).
