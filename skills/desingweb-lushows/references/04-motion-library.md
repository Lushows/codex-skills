# 04 — Librería de Movimiento (Motion Library)

Catálogo de efectos de movimiento para web de élite. Cada efecto indica **Cuándo** usarlo, **Técnica vanilla**, **Técnica React** (Framer Motion / `motion`), una **Regla/cuidado**, y un **Snippet** con ruta de ejemplo cuando aplica.

> Principio rector: el movimiento comunica jerarquía, continuidad y causa-efecto. Si no aporta significado, sobra. Anima **solo `transform` y `opacity`**, respeta `prefers-reduced-motion` y mantén las duraciones cortas (120–400ms para UI; 600–1200ms para entradas hero).

---

### Page-load stagger

- **Cuándo**: primera impresión de una página/hero — los elementos entran encadenados, no todos a la vez.
- **Técnica vanilla**: anima `opacity`/`translateY` con un `transition-delay` incremental por índice (`--i`).
- **Técnica React**: contenedor con `variants` + `staggerChildren` y `delayChildren`.
- **Regla/cuidado**: stagger total ≤ 600ms; si hay >8 elementos agrupa, no encadenes infinito. Desactivar con reduced-motion.
- **Snippet**: `assets/effects/vanilla/page-load-stagger.html`

```css
.stagger > * { opacity:0; transform:translateY(16px); animation:rise .5s ease forwards; }
.stagger > *:nth-child(1){animation-delay:.05s} .stagger > *:nth-child(2){animation-delay:.12s}
@keyframes rise{ to{ opacity:1; transform:none } }
```
```jsx
const list={ show:{ transition:{ staggerChildren:.08, delayChildren:.1 } } };
const item={ hidden:{ opacity:0, y:16 }, show:{ opacity:1, y:0 } };
<motion.ul variants={list} initial="hidden" animate="show">
  {items.map(i=> <motion.li key={i} variants={item}>{i}</motion.li>)}
</motion.ul>
```

---

### Scroll reveal

- **Cuándo**: secciones que aparecen al entrar al viewport (texto, tarjetas, imágenes).
- **Técnica vanilla**: `IntersectionObserver` que añade una clase `.in` al cruzar el umbral.
- **Técnica React**: `whileInView` con `viewport={{ once:true, amount:0.3 }}`.
- **Regla/cuidado**: revela **una sola vez** (`once`) para que no parpadee al hacer scroll arriba/abajo; umbral ~25–35%.
- **Snippet**: `assets/effects/vanilla/scroll-reveal.html`

```js
const io=new IntersectionObserver((es)=>es.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target);} }),{threshold:.25});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
```
```jsx
<motion.div initial={{opacity:0,y:24}} whileInView={{opacity:1,y:0}}
  viewport={{once:true, amount:0.3}} transition={{duration:.6, ease:[0.22,1,0.36,1]}} />
```

---

### Parallax

- **Cuándo**: profundidad en heros y fondos; capas que se mueven a distinta velocidad que el scroll.
- **Técnica vanilla**: en `scroll`, `transform:translateY(scrollY * factor)` (factor 0.1–0.4) dentro de `requestAnimationFrame`.
- **Técnica React**: `useScroll` + `useTransform` para mapear `scrollYProgress` a `y`.
- **Regla/cuidado**: nunca uses `background-attachment:fixed` (jank en móvil); limita a 2–3 capas; desactiva en reduced-motion.
- **Snippet**: `assets/effects/vanilla/parallax.html`

```jsx
const { scrollYProgress } = useScroll();
const y = useTransform(scrollYProgress, [0,1], ['0%','30%']);
<motion.div style={{ y }} />
```

---

### Magnetic button

- **Cuándo**: CTAs destacados; el botón "atrae" el cursor para invitar al clic.
- **Técnica vanilla**: en `mousemove` calcula el offset del cursor respecto al centro y aplica `translate` proporcional; resetea en `mouseleave`.
- **Técnica React**: estado de offset con motion values + `spring` para el retorno suave.
- **Regla/cuidado**: solo en dispositivos con puntero fino (`@media (hover:hover) and (pointer:fine)`); desplazamiento máx ~12px.
- **Snippet**: `assets/effects/vanilla/magnetic-button.html`

```js
btn.addEventListener('mousemove',e=>{ const r=btn.getBoundingClientRect();
  btn.style.transform=`translate(${(e.clientX-r.left-r.width/2)*.3}px,${(e.clientY-r.top-r.height/2)*.3}px)`; });
btn.addEventListener('mouseleave',()=>btn.style.transform='translate(0,0)');
```

---

### Marquee infinito

- **Cuándo**: tiras de logos, testimonios o tags que se desplazan sin fin.
- **Técnica vanilla**: duplica el contenido y anima la pista con `translateX(-50%)` en loop lineal.
- **Técnica React**: misma técnica; pausa en hover con estado, o usa una lib de marquee.
- **Regla/cuidado**: duplicar el set exacto para loop sin salto; `will-change:transform`; pausar en hover y en reduced-motion.
- **Snippet**: `assets/effects/vanilla/marquee.html`

```css
.track{ display:flex; gap:3rem; width:max-content; animation:marquee 20s linear infinite; }
.track:hover{ animation-play-state:paused; }
@keyframes marquee{ to{ transform:translateX(-50%) } }
```

---

### Hover tilt / 3D

- **Cuándo**: tarjetas de producto/proyecto que inclinan en 3D siguiendo el cursor.
- **Técnica vanilla**: `perspective` en el contenedor; en `mousemove` calcula `rotateX`/`rotateY` según la posición relativa.
- **Técnica React**: `useMotionValue` para x/y + `useTransform` a grados, con `spring`.
- **Regla/cuidado**: rotación máx ~8–10°; añade `transform-style:preserve-3d`; solo puntero fino.
- **Snippet**: `assets/effects/vanilla/hover-tilt.html`

```css
.card{ transition:transform .15s ease; transform-style:preserve-3d; }
.scene{ perspective:800px; }
```
```js
card.addEventListener('mousemove',e=>{ const r=card.getBoundingClientRect();
  const rx=((e.clientY-r.top)/r.height-.5)*-10, ry=((e.clientX-r.left)/r.width-.5)*10;
  card.style.transform=`rotateX(${rx}deg) rotateY(${ry}deg)`; });
```

---

### Text scramble / typing

- **Cuándo**: titulares hero con efecto "máquina de escribir" o descifrado de caracteres.
- **Técnica vanilla**: intervalo que revela caracteres reales y muestra glifos aleatorios en los pendientes.
- **Técnica React**: hook con `setInterval`/`requestAnimationFrame` que actualiza el string en estado.
- **Regla/cuidado**: respeta accesibilidad — el texto final debe existir en el DOM (no solo "animado"); ofrece versión estática en reduced-motion.
- **Snippet**: `assets/effects/vanilla/text-scramble.html`

```js
const chars='!<>-_\\/[]{}=+*^?#'; let frame=0;
const id=setInterval(()=>{ el.textContent=[...target].map((c,i)=> i<frame? c : chars[Math.random()*chars.length|0]).join('');
  if(frame++>=target.length) clearInterval(id); }, 40);
```

---

### Cursor personalizado

- **Cuándo**: sitios creativos/portafolios; un punto o anillo sigue al cursor y cambia sobre elementos interactivos.
- **Técnica vanilla**: un elemento `position:fixed` que sigue al cursor vía `transform`; interpola con `lerp` en rAF para suavidad.
- **Técnica React**: motion values `x/y` con `spring`, actualizados en `mousemove`.
- **Regla/cuidado**: oculta el cursor nativo solo si tu cursor custom cumple su rol; mantén el real en inputs y enlaces para accesibilidad; deshabilita en touch.
- **Snippet**: `assets/effects/vanilla/custom-cursor.html`

```js
let cx=0,cy=0,tx=0,ty=0; addEventListener('mousemove',e=>{tx=e.clientX;ty=e.clientY});
(function loop(){ cx+=(tx-cx)*.18; cy+=(ty-cy)*.18; dot.style.transform=`translate(${cx}px,${cy}px)`; requestAnimationFrame(loop); })();
```

---

### Sticky / scroll-pin

- **Cuándo**: una sección queda fija mientras el contenido adyacente avanza (storytelling, comparativas, pasos).
- **Técnica vanilla**: `position:sticky; top:0` en el panel fijo dentro de un contenedor alto; o GSAP ScrollTrigger `pin`.
- **Técnica React**: `useScroll` con `target`/`offset` y `useTransform` para animar según el progreso del pin.
- **Regla/cuidado**: el contenedor padre debe tener altura suficiente para el recorrido; cuidado con `overflow:hidden` en ancestros (rompe `sticky`).
- **Snippet**: `assets/effects/vanilla/scroll-pin.html`

```css
.pin-wrap{ height:300vh; } .pin{ position:sticky; top:0; height:100vh; }
```

---

### Número counter

- **Cuándo**: métricas/estadísticas que cuentan desde 0 al entrar en viewport.
- **Técnica vanilla**: `IntersectionObserver` dispara una animación con rAF que interpola el valor con easing.
- **Técnica React**: `useMotionValue` + `animate(mv, target)` y `useTransform` para formatear.
- **Regla/cuidado**: usa `tabular-nums` para que no "salte" el ancho; redondea; en reduced-motion muestra el valor final directo.
- **Snippet**: `assets/effects/vanilla/counter.html`

```js
function count(el,to,dur=1200){ const t0=performance.now();
  (function tick(t){ const p=Math.min((t-t0)/dur,1); const e=1-Math.pow(1-p,3);
    el.textContent=Math.round(to*e).toLocaleString(); if(p<1) requestAnimationFrame(tick); })(t0); }
```

---

### Blur-in

- **Cuándo**: entradas premium de imágenes o titulares que pasan de desenfocado a nítido.
- **Técnica vanilla**: anima `filter:blur()` + `opacity` de borroso/transparente a nítido/opaco.
- **Técnica React**: `initial={{ filter:'blur(12px)', opacity:0 }}` → `animate/whileInView`.
- **Regla/cuidado**: `filter:blur` es costoso; úsalo en pocos elementos y durante poco tiempo; añade `will-change:filter` y quítalo al terminar.
- **Snippet**: `assets/effects/vanilla/blur-in.html`

```jsx
<motion.h2 initial={{filter:'blur(12px)',opacity:0}} whileInView={{filter:'blur(0)',opacity:1}}
  viewport={{once:true}} transition={{duration:.7, ease:[0.22,1,0.36,1]}} />
```

---

### Gradiente animado

- **Cuándo**: fondos "aurora", botones glow, hero vivo (ver gradient mesh en 02-color-systems).
- **Técnica vanilla**: anima `background-position` de un `linear-gradient` grande, o `transform`/`opacity` de capas de `radial-gradient`.
- **Técnica React**: igual con CSS; o motion values sobre la posición de blobs.
- **Regla/cuidado**: animar `background-position` puede causar repaint; prefiere mover capas con `transform` (GPU). Loops lentos (12–20s).
- **Snippet**: `assets/effects/vanilla/animated-gradient.html`

```css
.aurora{ background:linear-gradient(120deg,#34D399,#5B8DEF,#22E0FF,#34D399);
  background-size:300% 300%; animation:grad 16s ease infinite; }
@keyframes grad{ 0%{background-position:0% 50%} 50%{background-position:100% 50%} 100%{background-position:0% 50%} }
```

---

### Image reveal mask

- **Cuándo**: imágenes que se "descubren" con una máscara que se desplaza (entrada editorial).
- **Técnica vanilla**: `clip-path:inset()` animado, o un overlay que sale con `transform:scaleX/translateX`.
- **Técnica React**: `whileInView` sobre `clipPath`, o un `motion.div` overlay que se desliza.
- **Regla/cuidado**: anima `transform` del overlay (no `width`); ease tipo `[0.77,0,0.175,1]` para sensación de "cortina".
- **Snippet**: `assets/effects/vanilla/image-reveal.html`

```css
.reveal-img{ clip-path:inset(0 100% 0 0); animation:wipe .9s cubic-bezier(.77,0,.175,1) forwards; }
@keyframes wipe{ to{ clip-path:inset(0 0 0 0) } }
```

---

### Smooth scroll

- **Cuándo**: scroll con inercia/suavizado tipo agencia (Lenis), o navegación por anclas suave.
- **Técnica vanilla**: `scroll-behavior:smooth` para anclas; para inercia global, librería tipo Lenis interpolando `scrollY`.
- **Técnica React**: integra Lenis en un provider y sincroniza con `useScroll` de Framer Motion vía rAF.
- **Regla/cuidado**: el smooth scroll por JS puede romper accesibilidad de teclado/anclas si está mal hecho; respeta reduced-motion (desactívalo).
- **Snippet**: `assets/effects/vanilla/smooth-scroll.html`

```css
html{ scroll-behavior:smooth; }
@media (prefers-reduced-motion: reduce){ html{ scroll-behavior:auto; } }
```

---

### Microinteracciones de botón

- **Cuándo**: feedback inmediato en todos los botones/enlaces (hover, press, loading, success).
- **Técnica vanilla**: `:hover`/`:active` con `transform:scale` + transición; ripple opcional con pseudo-elemento.
- **Técnica React**: `whileHover`/`whileTap` con `scale`, y transición de estado para loading/success.
- **Regla/cuidado**: `:active`/`whileTap` debe sentirse instantáneo (≤120ms); nunca deshabilites el feedback de focus; escala sutil (0.97–1.03).
- **Snippet**: `assets/effects/vanilla/button-micro.html`

```css
.btn{ transition:transform .12s ease, box-shadow .2s ease; }
.btn:hover{ transform:translateY(-2px); }
.btn:active{ transform:translateY(0) scale(.98); }
```
```jsx
<motion.button whileHover={{ y:-2 }} whileTap={{ scale:.97 }}
  transition={{ type:'spring', stiffness:400, damping:25 }}>Comprar</motion.button>
```

---

## Easings recomendados (cubic-bezier custom)

| Nombre | cubic-bezier | Sensación / uso |
|--------|--------------|------------------|
| `ease-out-quint` | `cubic-bezier(0.22, 1, 0.36, 1)` | entradas premium; arranca rápido, frena suave |
| `ease-out-expo` | `cubic-bezier(0.16, 1, 0.3, 1)` | reveals dramáticos, hero |
| `ease-in-out-quart` | `cubic-bezier(0.76, 0, 0.24, 1)` | loops, marquee, transiciones simétricas |
| `wipe / curtain` | `cubic-bezier(0.77, 0, 0.175, 1)` | máscaras, image reveal |
| `back-out (overshoot)` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | pops, badges, confirmaciones lúdicas |
| `snappy UI` | `cubic-bezier(0.4, 0, 0.2, 1)` | microinteracciones de UI estándar (Material) |
| `gentle in-out` | `cubic-bezier(0.45, 0, 0.55, 1)` | parallax, gradientes lentos |

```css
:root{
  --ease-out-quint: cubic-bezier(0.22, 1, 0.36, 1);
  --ease-out-expo:  cubic-bezier(0.16, 1, 0.3, 1);
  --ease-curtain:   cubic-bezier(0.77, 0, 0.175, 1);
  --ease-back:      cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-ui:        cubic-bezier(0.4, 0, 0.2, 1);
}
```

> En Framer Motion, los easings se pasan como array: `transition={{ ease: [0.22, 1, 0.36, 1] }}`. Para físicas naturales prefiere `type:'spring'` (`stiffness`, `damping`) sobre beziers en interacciones de arrastre/tap.

---

## Nota de performance y accesibilidad

1. **Anima solo `transform` y `opacity`.** Son las únicas propiedades que el navegador compone en GPU sin layout ni paint. Evita animar `width`, `height`, `top/left`, `margin`, `box-shadow` o `filter` en loops.
2. **`will-change` con criterio.** Actívalo justo antes de animar y quítalo al terminar; dejarlo permanente consume memoria de capa.
3. **60fps o nada.** Si un efecto baja de 60fps en móvil de gama media, simplifícalo (menos capas de blur, menos parallax).
4. **Respeta `prefers-reduced-motion`.** Es obligatorio. Reduce o elimina animaciones no esenciales para quienes sufren mareo/vestibular.

```css
@media (prefers-reduced-motion: reduce){
  *,
  *::before,
  *::after{
    animation-duration:.01ms !important;
    animation-iteration-count:1 !important;
    transition-duration:.01ms !important;
    scroll-behavior:auto !important;
  }
}
```

```jsx
// React: detectar la preferencia y desactivar efectos no esenciales
import { useReducedMotion } from 'framer-motion';
const reduce = useReducedMotion();
<motion.div animate={reduce ? { opacity:1 } : { opacity:1, y:0 }} />
```

> Regla final: el mejor motion es invisible — guía la atención sin que el usuario "note la animación". Si distrae, mídela; si marea, recórtala; si no comunica nada, elimínala.
