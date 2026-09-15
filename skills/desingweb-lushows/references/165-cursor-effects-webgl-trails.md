# 165 — Cursor effects & WebGL trails

**CRAFT, code-heavy.** El toque-firma del award site (Cuberto). Pareja de 150 (micro-interacciones), 39 (interacción), 146 (gooey), 143 (WebGL fx). Regla de oro: **el cursor custom es una capa decorativa sobre una UI que funciona perfecta sin él — gate con `@media (hover:hover) and (pointer:fine)`, NUNCA en touch, jamás ocultes el nativo en inputs.**

## 1. Por qué el cursor es la firma del "award site"

Es la señal más barata de "sitio premium": antes de leer, el usuario mueve el ratón y *algo responde distinto* (un anillo que persigue con retardo, un punto que crece sobre links, una etiqueta "View"). Cuberto construyó **toda su identidad de estudio** sobre esto (~80 líneas de JS = craft instantáneo). Pero es también lo que **más fácil arruina la experiencia** (lag excesivo = "roto"; ocultar el nativo en un `<input>` = no ves dónde escribes; en móvil no tiene sentido). Regla rectora: **si lo quitas, nada se rompe.**

## 2. El cursor base: dot + follower con lerp

Dos elementos: un **dot** que sigue casi 1:1 y un **ring** que persigue con lerp (retardo elástico). Oculta el nativo con `cursor:none` **solo bajo el gate:**
```css
@media (hover:hover) and (pointer:fine){
  *{ cursor:none; }
  input, textarea, [contenteditable]{ cursor:auto; }  /* NUNCA ocultar en campos */
}
.cursor-dot,.cursor-ring{ position:fixed; top:0; left:0; pointer-events:none; z-index:9999; border-radius:50%; translate:-50% -50%; will-change:transform; }
.cursor-dot{ width:6px; height:6px; background:#fff; }
.cursor-ring{ width:40px; height:40px; border:1.5px solid #fff; mix-blend-mode:difference; transition:width .25s, height .25s; } /* difference = invierte sobre cualquier fondo */
.cursor-ring.is-hover{ width:70px; height:70px; background:#fff; }
```
`mix-blend-mode:difference` es el truco Cuberto: el cursor se invierte contra el fondo, siempre visible sin lógica de color. **El loop de lerp (un único RAF, solo `transform`):**
```js
let mx=0,my=0,rx=0,ry=0; const lerp=(a,b,t)=>a+(b-a)*t;
addEventListener('pointermove', e=>{ mx=e.clientX; my=e.clientY; });
(function raf(){ dot.style.transform=`translate(${mx}px,${my}px)`;       // dot casi instantáneo
  rx=lerp(rx,mx,0.15); ry=lerp(ry,my,0.15);                              // ring persigue (0.15 = pereza)
  ring.style.transform=`translate(${rx}px,${ry}px)`; requestAnimationFrame(raf); })();
```
**Estados contextuales** vía delegación: `is-hover` sobre `a,button,[data-cursor]` + label `data-cursor="View"` en `::after`.

## 3. Cursor trails (estela)

**(a) Cadena/snake** (N dots donde cada uno persigue al anterior): `pos[i].x=lerp(pos[i].x, leadX, 0.35); leadX=pos[i].x; dots[i].style.transform=\`translate(${pos[i].x}px,${pos[i].y}px) scale(${1-i/N})\`` (se afina hacia la cola). **(b) Canvas trail (línea que se desvanece):** NO limpies el canvas — pinta con alpha bajo cada frame (`ctx.fillStyle='rgba(0,0,0,0.08)'; ctx.fillRect(0,0,w,h)`) + línea de `prev` a actual = fade natural. **(c) Particle trail** (empuja partículas con velocidad/vida en `pointermove`, decae `alpha`, pool de objetos). **(d) Gooey/sticky trail** (varios blobs fusionados por filtro SVG `#goo` con blur fuerte + `feColorMatrix` alpha alto = lava).

## 4. WebGL fluid cursor

El **WebGL-Fluid-Simulation de Pavel Dobryakov** (Navier-Stokes en GPU: el puntero inyecta velocity + dye; shaders resuelven advection→divergence→curl→pressure; ping-pong de framebuffers → estela de tinta que se arremolina). **Cómo acotarlo (no usarlo a pantalla completa robando clicks):** canvas detrás con `pointer-events:none`, contenido encima con z-index mayor:
```js
WebGLFluid(canvas, { SIM_RESOLUTION:128, DENSITY_DISSIPATION:2.5, VELOCITY_DISSIPATION:2, TRANSPARENT:true, BLOOM:false });
```
```css
#fluid{ position:fixed; inset:0; z-index:-1; pointer-events:none; }
```
**Distorsión que sigue al cursor sobre imagen/fondo:** shader fullscreen que desplaza UVs por distancia al puntero — `uv += direction * strength * smoothstep(radius, 0., dist(uv, mouse))`. **Ripple from cursor:** array de anillos (centro, tiempo, amplitud) sumados con `sin(dist*freq - t*speed)*amp*decay`. Coste: ~1 contexto WebGL, ~3-5ms/frame desktop; bájalo/desactívalo en móvil/reduced-motion.

## 5. Magnético & sticky

**Magnético** (el elemento se desplaza hacia el cursor dentro de su área):
```js
el.addEventListener('pointermove', e=>{ const r=el.getBoundingClientRect();
  el.style.transform=`translate(${(e.clientX-(r.left+r.width/2))*0.4}px, ${(e.clientY-(r.top+r.height/2))*0.4}px)`; });
el.addEventListener('pointerleave', ()=> el.style.transform='translate(0,0)'); // CSS transition para el snap-back
```
(Cuberto usa GSAP `quickTo`; con CSS basta `transition:transform .3s cubic-bezier(.2,1,.3,1)`). **Sticky cursor (snap a botón):** cuando el puntero entra a un target, el ring abandona el lerp libre y se *adhiere* al centro, copiando su tamaño/`border-radius` (el **morph-into-element**: el cursor se vuelve un highlight del botón; añade offset hacia el puntero `+(mx-tx)*0.1` para que se sienta "magnético" pero anclado).

## 6. Craft, accesibilidad & performance

**Funciona sin el cursor custom** siempre (capa visual, no UI funcional). **Gate obligatorio:** todo dentro de `@media (hover:hover) and (pointer:fine)`; en JS `if(matchMedia('(hover:hover) and (pointer:fine)').matches)` antes de inicializar (**nunca en touch**). **`prefers-reduced-motion`** (desactiva trails/fluido/lerp agresivo; `if(reduce) return` sin init). **Nunca ocultes el nativo en `input`/`textarea`/`[contenteditable]`/`<select>`/iframes** (el caret y el cursor de texto son funcionales; restáuralos con `cursor:auto`). **Performance:** **un solo RAF** para todo (dot, ring, trail); solo `transform` (compositor); `pointer-events:none` en todos los elementos del cursor; pools de partículas; cachea `getBoundingClientRect`. **A11y — el cursor nativo importa:** usuarios con baja visión/motricidad/lupa dependen de su cursor de SO (tamaño, contraste, esquema); si lo ocultas con un sustituto pobre, los excluyes; respeta `forced-colors`. **La línea del gimmick:** no hagas clickear más difícil (lag excesivo, ring que tapa el target, magnético que "huye" del botón al ir a pulsarlo).

## Cursor anti-patterns — blacklist
**cursor custom en touch/móvil** (sin el media gate; cero valor, solo peso) · **ocultar el nativo en inputs/textareas** (no se ve el caret) · **lerp demasiado lento** (factor <0.08; se siente roto/laggy) · **ring gigante que tapa el target** o intercepta clicks (falta `pointer-events:none`) · **ignorar `prefers-reduced-motion`** · **magnético que aleja el botón** del cursor (signo invertido / strength >0.6) · **WebGL fluid a pantalla completa robando interacción** (sin `pointer-events:none`/z-index correcto) · **múltiples RAF/setInterval** y mutar `top/left` (layout thrash) en vez de `transform` · **crear nodos/partículas por frame** sin pool · **trail tan largo/pesado** que distrae de leer · **no restaurar el nativo en iframes/embeds** (mapas, videos) · **bajo contraste / sin `mix-blend-mode`** (cursor que desaparece sobre medio sitio).
