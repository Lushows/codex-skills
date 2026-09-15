# 07 — Motion Cinemático (Scroll & Animación de élite)

Guía accionable para que una web se vea "cara" (nivel Awwwards). Todo el código es copy-paste real,
basado en las APIs vigentes 2025-2026: **GSAP 3.13** (con SplitText ya gratis), **ScrollTrigger**,
**Lenis** y las **CSS scroll-driven animations** (`animation-timeline`).

---

## 1. El stack cinemático — por qué se ve "caro"

Lo que separa una landing genérica de una premium NO es tener más animaciones, es **el control del
tiempo**. El scroll del navegador es brusco (salta por líneas/rueda). El stack cinemático lo convierte
en una línea de tiempo continua y suave que tú diriges como una cámara.

| Pieza | Qué hace | Por qué importa |
|---|---|---|
| **Lenis** | Smooth scroll real (interpola el `scrollTop`). | Da la sensación "mantequilla". Sin esto, todo scrub se ve a tirones. |
| **GSAP** | Motor de animación (interpola cualquier propiedad con easing). | Precisión sub-pixel + timelines orquestadas. |
| **ScrollTrigger** | Plugin de GSAP que ata una animación al scroll: pin, scrub, snap. | Es la "cámara montada sobre rieles". |
| **SplitText** | Parte texto en líneas/palabras/caracteres (gratis desde 3.13). | Reveals tipográficos por línea = sello de estudio caro. |
| **CSS scroll-driven** | `animation-timeline` nativo, sin JS. | Para reveals y barras de progreso baratas y performantes. |

### CDNs exactos (GSAP 3.13 + Lenis)

```html
<!-- GSAP core + plugins (3.13+ : SplitText y ScrollSmoother ya son gratuitos) -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/SplitText.min.js"></script>

<!-- Lenis smooth scroll -->
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.18/dist/lenis.min.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lenis@1.1.18/dist/lenis.css">
```

```js
// Registrar plugins (siempre, una vez)
gsap.registerPlugin(ScrollTrigger, SplitText);
```

> En npm/bundler: `npm i gsap lenis` y `import gsap from "gsap"; import ScrollTrigger from "gsap/ScrollTrigger"; import { SplitText } from "gsap/SplitText"; import Lenis from "lenis";`

---

## 2. Integración Lenis + ScrollTrigger (el corazón de todo)

Regla de oro: **un solo RAF loop**. Lenis NO debe correr su propio `requestAnimationFrame` cuando
GSAP ya tiene un ticker; los dos compitiendo causan jank. Por eso `autoRaf: false` + montar Lenis en
el ticker de GSAP y `lagSmoothing(0)`.

```js
gsap.registerPlugin(ScrollTrigger);

const lenis = new Lenis({
  duration: 1.1,          // segundos que tarda en "alcanzar" el scroll
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), // expo-out
  smoothWheel: true,
  autoRaf: false,         // CLAVE: no dejes que Lenis maneje su propio loop
});

// 1) Cada vez que Lenis hace scroll, avisa a ScrollTrigger
lenis.on('scroll', ScrollTrigger.update);

// 2) Lenis se actualiza desde el ticker de GSAP (un solo loop, sincronizado)
gsap.ticker.add((time) => {
  lenis.raf(time * 1000); // GSAP da segundos, Lenis espera milisegundos
});

// 3) Desactiva el lag smoothing de GSAP para que no pelee con Lenis
gsap.ticker.lagSmoothing(0);
```

Eso es todo. A partir de aquí, cualquier `ScrollTrigger` con `scrub` se verá suave.

---

## 3. Recetas ScrollTrigger

Notas previas:
- `scrub: true` ata la animación 1:1 al scroll. `scrub: 1` añade 1s de "inercia" (recomendado, se ve premium).
- `markers: true` durante desarrollo para ver start/end.
- `toggleActions: "play none none reverse"` para animaciones que disparan (no scrubbean).

### 3.1 Cámara push-in en el hero (scrub: scale + yPercent)

El hero se "acerca" y sube ligeramente al hacer scroll: efecto cámara cinematográfica.

```js
gsap.to(".hero__media", {
  scale: 1.18,
  yPercent: -8,
  ease: "none",
  scrollTrigger: {
    trigger: ".hero",
    start: "top top",
    end: "bottom top",
    scrub: 1,
  },
});
```

### 3.2 Reveal escalonado (stagger) al entrar en viewport

```js
gsap.from(".reveal-item", {
  y: 60,
  opacity: 0,
  duration: 0.9,
  ease: "power3.out",
  stagger: 0.12,
  scrollTrigger: {
    trigger: ".reveal-grid",
    start: "top 80%",      // cuando el top del grid llega al 80% del viewport
    toggleActions: "play none none reverse",
  },
});
```

Para muchísimos elementos repartidos por la página, usa **`ScrollTrigger.batch()`** (un trigger por
elemento, callbacks agrupados — mucho más performante que crear N triggers a mano):

```js
ScrollTrigger.batch(".card", {
  start: "top 85%",
  onEnter: (els) => gsap.to(els, { opacity: 1, y: 0, stagger: 0.1, overwrite: true }),
  onLeaveBack: (els) => gsap.to(els, { opacity: 0, y: 40, stagger: 0.1, overwrite: true }),
});
```

### 3.3 Contadores animados al entrar

```js
document.querySelectorAll("[data-count]").forEach((el) => {
  const end = +el.dataset.count;
  const obj = { val: 0 };
  gsap.to(obj, {
    val: end,
    duration: 2,
    ease: "power1.out",
    scrollTrigger: { trigger: el, start: "top 85%", once: true },
    onUpdate: () => { el.textContent = Math.round(obj.val).toLocaleString(); },
  });
});
```

### 3.4 Pin de sección (se queda fija mientras animas su contenido)

```js
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".feature",
    start: "top top",
    end: "+=1200",     // distancia de scroll durante la cual queda fija
    pin: true,
    scrub: 1,
    anticipatePin: 1,  // evita un "salto" al pinear
  },
});
tl.from(".feature__title", { yPercent: 100, opacity: 0 })
  .from(".feature__img",   { scale: 0.6, opacity: 0 }, "<0.2")
  .to(".feature__bg",      { backgroundColor: "#0a0a0a" }, 0);
```

### 3.5 Galería HORIZONTAL con pin (el clásico de estudio)

La sección se pinea y el track se desplaza en X mientras scrolleas vertical. **El cálculo de la
distancia** es lo importante: el `end` debe igualar el ancho real que sobra del track.

```html
<section class="gallery">
  <div class="gallery__track">
    <article class="panel">1</article>
    <article class="panel">2</article>
    <article class="panel">3</article>
    <article class="panel">4</article>
  </div>
</section>
```

```css
.gallery { overflow: hidden; }
.gallery__track { display: flex; width: max-content; will-change: transform; }
.panel { width: 100vw; height: 100vh; flex: 0 0 100vw; }
```

```js
const track = document.querySelector(".gallery__track");

// distancia = ancho total del track menos un viewport
const getScrollAmount = () => -(track.scrollWidth - window.innerWidth);

const horizontalTween = gsap.to(track, {
  x: getScrollAmount,            // función => se recalcula en refresh
  ease: "none",                 // OBLIGATORIO: si no, scroll y X no coinciden
  scrollTrigger: {
    trigger: ".gallery",
    start: "top top",
    end: () => `+=${-getScrollAmount()}`, // misma distancia que el desplazamiento
    pin: true,
    scrub: 1,
    invalidateOnRefresh: true,  // recalcula al redimensionar
  },
});
```

**Zoom anidado dentro del scroll horizontal** (`containerAnimation`): un elemento dentro de un panel
necesita su propio trigger, pero el "scroller" ahora es el tween horizontal, no la ventana. Para eso
existe `containerAnimation`. Ojo: con `containerAnimation` **no** se puede usar `pin` ni `snap`.

```js
gsap.from(".panel--3 img", {
  scale: 0.5,
  opacity: 0,
  ease: "none",
  scrollTrigger: {
    trigger: ".panel--3",
    containerAnimation: horizontalTween, // ata este trigger al movimiento horizontal
    start: "left center",                // usa left/right (no top/bottom) en horizontal
    end: "center center",
    scrub: true,
  },
});
```

### 3.6 Scroll-snap entre secciones

```js
ScrollTrigger.create({
  trigger: ".sections-wrapper",
  start: "top top",
  end: "bottom bottom",
  snap: {
    snapTo: 1 / (numSections - 1), // puntos equidistantes (0, 0.25, 0.5, ...)
    duration: { min: 0.2, max: 0.6 },
    ease: "power1.inOut",
    delay: 0.05,
  },
});
```

> Si Lenis está activo, también puedes hacer snap por CSS (`scroll-snap-type: y mandatory`) en el
> contenedor; pero el snap de ScrollTrigger respeta el smooth scroll de Lenis mejor.

---

## 4. Split-text reveal (el sello tipográfico)

### 4.1 Vanilla — máscara por línea sin librería

Cada línea vive dentro de un contenedor con `overflow: clip` y se anima de abajo hacia arriba. Para
partir por líneas necesitas JS (porque las líneas dependen del ancho); un truco robusto es envolver
cada **palabra** y agrupar por su `offsetTop`.

```css
.mask-line { display: block; overflow: clip; }      /* la máscara */
.mask-line > span { display: inline-block; transform: translateY(110%); }
.mask-line.is-in > span { transform: translateY(0); transition: transform .9s cubic-bezier(.2,.8,.2,1); }
```

```js
function splitIntoLines(el) {
  const words = el.textContent.trim().split(/\s+/);
  el.innerHTML = words.map((w) => `<span class="w">${w}&nbsp;</span>`).join("");
  const spans = [...el.querySelectorAll(".w")];
  let lines = [], current = [], top = null;
  spans.forEach((s) => {
    if (top === null) top = s.offsetTop;
    if (s.offsetTop > top) { lines.push(current); current = []; top = s.offsetTop; }
    current.push(s);
  });
  lines.push(current);
  // reconstruir con una máscara por línea
  el.innerHTML = "";
  lines.forEach((line) => {
    const wrap = document.createElement("span");
    wrap.className = "mask-line";
    const inner = document.createElement("span");
    line.forEach((s) => inner.appendChild(s));
    wrap.appendChild(inner);
    el.appendChild(wrap);
  });
  return [...el.querySelectorAll(".mask-line")];
}

document.querySelectorAll("[data-split]").forEach((el) => {
  const lines = splitIntoLines(el);
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e, i) => {
      if (e.isIntersecting) { setTimeout(() => e.target.classList.add("is-in"), i * 90); }
    });
  }, { threshold: 0.4 });
  lines.forEach((l) => io.observe(l));
});
```

### 4.2 Con GSAP SplitText (3.13+, gratis)

Desde 3.13, `SplitText` puede crear automáticamente las máscaras con `mask: "lines"` (envuelve cada
línea en un contenedor con overflow oculto) y `autoSplit` re-parte el texto al redimensionar.

```js
SplitText.create(".headline", {
  type: "lines",
  mask: "lines",        // crea las máscaras de overflow automáticamente
  autoSplit: true,      // re-divide al cambiar el ancho / cargar fuentes
  onSplit(self) {
    // devolver la animación deja que GSAP la limpie en cada re-split
    return gsap.from(self.lines, {
      yPercent: 110,
      duration: 1,
      ease: "power4.out",
      stagger: 0.12,
      scrollTrigger: { trigger: ".headline", start: "top 80%" },
    });
  },
});
```

> Para revelar por carácter usa `type: "chars"` y anima `self.chars`. Espera a `document.fonts.ready`
> antes de partir, o las líneas se calcularán con la fuente fallback y saltarán.

---

## 5. CSS scroll-driven animations (sin JS)

Nativo, súper performante (corre fuera del hilo principal). Dos timelines:
- **`scroll()`** — progreso del *contenedor de scroll* (ideal: barra de progreso global).
- **`view()`** — progreso de la *visibilidad del propio elemento* dentro del viewport (ideal: reveals).

### 5.1 Reveal de elemento con `view()`

```css
@keyframes reveal-up {
  from { opacity: 0; transform: translateY(40px); }
  to   { opacity: 1; transform: translateY(0); }
}

.card {
  animation: reveal-up linear both;
  animation-timeline: view();          /* timeline = visibilidad del elemento */
  animation-range: entry 0% cover 35%; /* desde que entra hasta el 35% cubierto */
}
```

### 5.2 Barra de progreso de lectura con `scroll()`

```css
@keyframes grow { from { transform: scaleX(0); } to { transform: scaleX(1); } }

.progress-bar {
  position: fixed; inset: 0 0 auto 0; height: 4px; transform-origin: left;
  background: linear-gradient(90deg, #6ee7ff, #a78bfa);
  animation: grow linear both;
  animation-timeline: scroll(root block); /* progreso del scroll de la raíz */
}
```

### 5.3 Soporte y fallback (progressive enhancement)

Chrome/Edge ok; Safari/Firefox aún parcial (junio 2026). Detecta con `@supports` y deja el estado
final visible si no hay soporte (nunca dejes contenido escondido sin la animación):

```css
.card { opacity: 1; transform: none; } /* estado base visible = fallback seguro */

@supports (animation-timeline: view()) {
  .card { opacity: 0; animation: reveal-up linear both; animation-timeline: view(); }
}
```

---

## 6. Reglas de performance y accesibilidad

**Solo anima `transform` y `opacity`.** Son las únicas propiedades que el compositor maneja en GPU sin
recalcular layout/paint. Evita animar `width`, `height`, `top`, `left`, `margin`, `box-shadow`.

```css
.will-animate { will-change: transform, opacity; } /* SOLO en lo que de verdad se anima */
```

> `will-change` cuesta memoria: ponlo justo antes de animar y quítalo al terminar. Nunca en `*`.

**`ScrollTrigger.refresh()` tras cargar imágenes/fuentes.** Las medidas (`start`/`end`/distancia
horizontal) se calculan una vez; si una imagen carga después y empuja el layout, los triggers quedan
desfasados.

```js
window.addEventListener("load", () => ScrollTrigger.refresh());
document.fonts.ready.then(() => ScrollTrigger.refresh());
// usa también invalidateOnRefresh: true en triggers con valores calculados (galería horizontal)
```

**`prefers-reduced-motion` — desactivar Lenis y GSAP.** Obligatorio para accesibilidad. Quien lo pide
sufre con el scroll-jacking.

```js
const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (reduce) {
  // 1) NO inicialices Lenis (deja el scroll nativo del navegador)
  // 2) Desactiva todos los scrubs/pins de GSAP:
  ScrollTrigger.getAll().forEach((st) => st.kill());
  // 3) Salta cualquier from/to a su estado final inmediatamente:
  gsap.globalTimeline.timeScale(200);
} else {
  initLenis();
  initScrollAnimations();
}
```

Y en CSS, para las scroll-driven nativas:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
}
```

---

## 7. Cuándo NO usar scroll-jacking

El scroll-jacking (Lenis + pins largos + horizontal) es potente pero abusarlo arruina la UX. Evítalo o
modéralo cuando:

- **Sitios con mucho contenido / lectura** (blogs, docs, e-commerce con listados largos): la gente
  quiere scroll rápido y predecible, no inercia que "pelea" con su rueda/trackpad.
- **El usuario pidió `prefers-reduced-motion`** — desactívalo por completo (ver §6).
- **Mobile / trackpads de gama baja**: el smooth scroll puede sentirse pesado o introducir lag.
  Considera `smoothTouch: false` en Lenis (por defecto ya viene desactivado en touch).
- **Cuando el efecto no aporta narrativa.** El pin horizontal solo vale si cuentas algo (un portfolio,
  un timeline de producto). Pinear "porque sí" frustra: el usuario scrollea y "no avanza".
- **Accesibilidad de teclado**: asegúrate de que `Tab`/`Page Down`/anclas sigan funcionando; Lenis las
  respeta, pero pins muy largos pueden esconder foco. Prueba siempre con teclado.

Regla práctica: **una o dos secciones cinemáticas por página** (hero + un momento "wow"). El resto,
reveals sutiles (§3.2 / §5). El lujo está en la contención, no en la saturación.
