# 150 — Hover & micro-interaction catalog (la capa de deleite)

**CRAFT, code-heavy.** Catálogo copy-paste de hovers de botón/card/link + cursor. Pareja de 35 (estados de componente), 39 (interacción/magnético), 34 (Motion React), 16 (a11y). Regla de oro: **timing 100-300ms, `@media (hover:hover)` para no romper táctil, `focus-visible` parity para teclado, una sola personalidad de movimiento repetida > 30 efectos peleando.**

## 1. Por qué = calidad percibida

Una interfaz "correcta" y una "wow" suelen tener el mismo HTML. La diferencia es la **capa de deleite** (los 200ms entre que el cursor toca y el feedback aparece): **feedback** (confirma que el sistema te escuchó), **affordance** (sugiere "clickeable/arrástrame"), **personalidad** (la marca se siente viva). El usuario rara vez nota una buena micro-interacción, pero sí nota su ausencia (un botón que cambia de estado sin transición se siente roto aunque funcione).

## 2. Button hovers (catálogo)

**Fill-sweep** (relleno que barre desde abajo):
```css
.btn-sweep{position:relative;isolation:isolate;overflow:hidden;border:1px solid currentColor;padding:.9em 1.8em;transition:color .3s}
.btn-sweep::before{content:"";position:absolute;inset:0;background:currentColor;transform:scaleY(0);transform-origin:bottom;transition:transform .35s cubic-bezier(.7,0,.2,1);z-index:-1}
.btn-sweep:hover{color:var(--bg)} .btn-sweep:hover::before{transform:scaleY(1)}
```
**Text-swap** (dos textos apilados, uno sube y entra el otro):
```css
.btn-swap{overflow:hidden;display:inline-grid;padding:.9em 1.8em}
.btn-swap span{grid-area:1/1;transition:transform .4s cubic-bezier(.7,0,.2,1)}
.btn-swap .in{transform:translateY(110%)}
.btn-swap:hover .out{transform:translateY(-110%)} .btn-swap:hover .in{transform:translateY(0)}
```
**Border-draw** (`::before` border-width:1px 0 scaleX(0) + `::after` border-width:0 1px scaleY(0), ambos a scale(1) en hover). **Icon-slide** (`.btn-icon:hover svg{transform:translateX(.35em)}`). **Magnetic pull** (GSAP, factor ~0.3):
```js
btn.addEventListener('mousemove',e=>{ const r=btn.getBoundingClientRect();
  gsap.to(btn,{x:(e.clientX-r.left-r.width/2)*.3, y:(e.clientY-r.top-r.height/2)*.3, duration:.6, ease:'power3.out'}); });
btn.addEventListener('mouseleave',()=>gsap.to(btn,{x:0,y:0,duration:.6,ease:'elastic.out(1,.4)'}));
```
(mueve el texto interno con factor menor ~0.15 para paralaje sutil).

## 3. Card hovers (catálogo)

**3D tilt** (rotateX/Y desde el puntero + perspective en el padre):
```js
function tilt(card,max=8){ card.addEventListener('mousemove',e=>{ const r=card.getBoundingClientRect();
  const px=(e.clientX-r.left)/r.width-.5, py=(e.clientY-r.top)/r.height-.5;
  card.style.transform=`rotateY(${px*max}deg) rotateX(${-py*max}deg)`; });
  card.addEventListener('mouseleave',()=>card.style.transform=''); }
```
(`.tilt-wrap{perspective:900px}` + `.tilt{transform-style:preserve-3d;transition:transform .4s}`). **Spotlight** (radial-gradient que sigue al cursor vía `--mx/--my`). **Image-zoom-with-mask** (`.zoom{overflow:hidden} .zoom:hover img{transform:scale(1.06)}`). **Reveal-on-hover** (detalles que suben con `translateY(100%)`→`0`). **Lift + shadow** (la receta universal, nota el easing con overshoot):
```css
.lift{transition:transform .3s cubic-bezier(.34,1.56,.64,1),box-shadow .3s ease}
.lift:hover{transform:translateY(-6px);box-shadow:0 18px 40px -12px rgba(0,0,0,.35)}
```

## 4. Link & text hovers

**Underline-grow** (la forma correcta — `transform-origin` para crecer desde izquierda y retraerse hacia derecha):
```css
.link::after{content:"";position:absolute;left:0;bottom:-2px;width:100%;height:1px;background:currentColor;transform:scaleX(0);transform-origin:right;transition:transform .35s cubic-bezier(.7,0,.2,1)}
.link:hover::after{transform:scaleX(1);transform-origin:left}
```
**Swap two stacked texts** (marquee link vertical: `span` con `::after{content:attr(data-t)}` y `:hover span{transform:translateY(-50%)}`). **Char-stagger** (`span` con `transition-delay` incremental `i*25ms`, `:hover span{transform:translateY(-.25em)}`). **Color-fill clip** (`background-size:0% 100%`→`100% 100%` con `background-clip:text`).

## 5. Cursor-driven

**Custom cursor** (dot inmediato + ring con seguimiento lerp):
```js
let mx=0,my=0,rx=0,ry=0;
addEventListener('mousemove',e=>{mx=e.clientX;my=e.clientY; dot.style.transform=`translate(${mx}px,${my}px) translate(-50%,-50%)`});
(function loop(){ rx+=(mx-rx)*0.15; ry+=(my-ry)*0.15; // lerp = el secreto del retardo suave
  ring.style.transform=`translate(${rx}px,${ry}px) translate(-50%,-50%)`; requestAnimationFrame(loop); })();
document.querySelectorAll('a,button,[data-cursor]').forEach(el=>{
  el.addEventListener('mouseenter',()=>ring.classList.add('grow'));
  el.addEventListener('mouseleave',()=>ring.classList.remove('grow')); });
```
**Estados extra:** `mix-blend-mode:difference` en el ring (invierte color automáticamente sobre fondos contrastados); inyectar label de texto (`data-cursor="Ver"`) dentro del ring para CTAs; combinar con magnetic. El lerp factor (0.15) define la "pesadez": más bajo = más perezoso/líquido.

## 6. La capa de artesanía (crafted vs gimmick)

**Timing:** hovers 100-300ms (<100ms sin deleite; >400ms estorba al usuario rápido; entrada un poco más rápida que salida está bien, lo inverso se siente pegajoso). **Easing:** nada de `ease` por defecto — `cubic-bezier(.7,0,.2,1)` para sweeps/swaps, `cubic-bezier(.34,1.56,.64,1)` (overshoot sutil) para lifts/pops, `power3.out`/`expo.out` en GSAP para magnéticos (el overshoot da el "snap" premium). **`@media (hover:hover)`** envuelve TODO efecto hover (en táctil `:hover` queda pegado tras el tap). **`prefers-reduced-motion`** siempre. **Consistencia:** una sola curva de easing y una sola duración base como tokens (`--ease`, `--dur`) reutilizados (esto separa "diseñado" de "ensamblado"). **`focus-visible` parity:** cada `:hover` con su gemelo `:focus-visible` para teclado. **GPU:** anima solo `transform`/`opacity`, evita `width/height/top/left/box-shadow` en bucle.

## Micro-interaction anti-patterns — blacklist
**tilt extremo** (>12° marea y rompe legibilidad) · **magnetic en todo** (resérvalo para 1-3 CTAs clave) · **custom cursor sin fallback táctil** ni respeto a reduced-motion · **animar `box-shadow`/`filter:blur` en bucle de cursor** (jank; usa capas con opacidad) · **hovers >400ms** o con `ease-in` puro de salida (pegajoso) · **hover como única señal de affordance** sin estado de foco (excluye teclado/lectores) · **`transition:all`** (anima propiedades inesperadas y mata rendimiento; nombra las propiedades) · **efectos peleando** (tilt + zoom + spotlight + magnetic en la misma card) · **reaparición instantánea al salir** sin transición de leave (el "parpadeo" delata falta de oficio) · **`:hover` que mueve layout** (cambia padding/margin/font-size → reflow y "salto" del contenido vecino; usa `transform`).
