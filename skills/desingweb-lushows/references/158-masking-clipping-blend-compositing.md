# 158 — Masking, clipping & blend-mode compositing

**CRAFT, code-heavy.** Léelo para clip-path, mask-image, SVG masks, mix-blend-mode creativo, reveals combinados. Pareja de 09 (modern CSS), 144 (transitions), 147 (grano/blend), 81 (CSS art). Regla de oro: **clip-path = borde duro, mask = borde suave; `mix-blend-mode` necesita `isolation:isolate` en el padre o sangra hasta el body; duplica siempre `mask-*` con `-webkit-`.**

## 1. clip-path deep

Recorta con borde **duro** (antialiased, no difuminado):
```css
.a{ clip-path:inset(10% 20% 30% 5% round 12px); } /* top right bottom left + radius */
.b{ clip-path:circle(40% at 50% 50%); }            /* iris */
.d{ clip-path:polygon(0 0, 100% 0, 100% 85%, 0 100%); } /* diagonal */
.e{ clip-path:path("M0,50 Q50,0 100,50 T200,50 V100 H0 Z"); } /* curva libre (estático) */
```
**Reveal wipe** (el patrón premium): `.reveal{ clip-path:inset(0 100% 0 0); transition:clip-path .9s cubic-bezier(.7,0,.2,1); } .reveal.in{ clip-path:inset(0 0 0 0); }`. **Iris:** `circle(0% at 50% 50%)` → `circle(75% at 50% 50%)`. **Shape morph (mismo vertex-count OBLIGATORIO):** para morphear cuadrado→hexágono declara el cuadrado con 6 puntos (vértices duplicados) para que las listas `polygon()` interpolen 1-a-1; mezclar conteos distintos = salto. **`clip-path: shape()`** (2025+) permite curvas con `%`/`vw` y es animable a diferencia de `path()` (estático) — prefiérelo para animar curvas.

## 2. mask-image (borde suave)

El canal alpha/luminance define opacidad por píxel — **mask difumina, clip-path no:**
```css
/* Scroll-fade (degradado en bordes — lista que se desvanece) */
.fade{ -webkit-mask-image:linear-gradient(to bottom, transparent, #000 8%, #000 92%, transparent);
               mask-image:linear-gradient(to bottom, transparent, #000 8%, #000 92%, transparent); }
/* Fade en 4 lados con mask-composite */
.fade4{ mask-image:linear-gradient(#000,#000), linear-gradient(to right, transparent,#000 5%,#000 95%,transparent);
        mask-composite:intersect; } /* WebKit: -webkit-mask-composite:source-in */
```
**Soft-edge reveal** (wipe difuminado, imposible con clip-path): `mask-image:linear-gradient(120deg,#000 0 var(--p,0%),transparent var(--p))` + animar `--p` con `@property` `<percentage>`. **PNG/SVG alpha:** `mask-image:url(blob.svg); mask-mode:alpha; mask-size:cover;` (`luminance` usa brillo: blanco=visible). Operadores `mask-composite`: `add`/`subtract`/`intersect`/`exclude`.

## 3. SVG `<mask>` & `<clipPath>`

**Cut-out/stencil (texto recortado de un panel):**
```html
<mask id="knockout"><rect width="100%" height="100%" fill="#fff"/>
  <text x="50%" y="55%" text-anchor="middle" font-size="120" font-weight="900" fill="#000">2026</text></mask>
<rect width="100%" height="100%" fill="tomato" mask="url(#knockout)"/>
```
(blanco=opaco, negro=transparente — luminance por defecto). **clipPath responsive** con `clipPathUnits="objectBoundingBox"` (coords 0-1, escala con el elemento): `<clipPath id="blob" clipPathUnits="objectBoundingBox"><path d="..."/></clipPath>` + `.hero-img{ clip-path:url(#blob); }`.

## 4. mix-blend-mode & background-blend-mode (creativo)

`mix-blend-mode` mezcla con lo que tiene **detrás**; `background-blend-mode` mezcla las capas de background del mismo elemento. **Difference cursor/texto** (se invierte sobre cualquier fondo): `color:#fff; mix-blend-mode:difference;` (sobre blanco se ve negro, sobre negro blanco, cero JS de color). **Duotono:** `img{filter:grayscale(1) contrast(1.2)}` + `::before{background:#1d3fff; mix-blend-mode:screen}` + `::after{background:#ff2d75; mix-blend-mode:multiply}`. **Grain overlay:** `mix-blend-mode:overlay; opacity:.08`. **Glow:** `mix-blend-mode:color-dodge` sobre radial-gradient claro. **El gotcha `isolation`:** sin `isolation:isolate` en el padre, el blend "sangra" hasta el `<body>` y mezcla con todo lo de detrás — **causa #1 de blends que se ven mal**.

## 5. Combined reveals (premium)

**Imagen revelada tras máscara on-scroll** (clip-path + IntersectionObserver): `.scene img{clip-path:inset(0 0 100% 0); transition:clip-path 1.1s} .scene.in img{clip-path:inset(0 0 0 0)}`. **Text reveal stagger** (cada línea con su clip-path y delay `var(--d)`). **Curtain** (desde el centro): `inset(0 50% 0 50%)` → `inset(0 0 0 0)`. **Spotlight que sigue al cursor** (radial mask con variables JS): `mask-image:radial-gradient(circle 180px at var(--mx) var(--my), #000 0, transparent 100%)` + `el.style.setProperty('--mx', e.offsetX+'px')`.

## 6. Perf & gotchas

**¿Compositor o no?** `circle()`/`ellipse()`/`inset()`/`polygon()` de igual vertex-count animan en GPU/compositor; `path()` y cambios de vertex-count caen al main thread. **mask animado:** animar `mask-position`/`mask-size` es barato; animar el string del gradient fuerza repaint (truco: registra un `@property <percentage>` y anima esa variable). **Safari/`-webkit-`:** SIEMPRE duplica `mask-*` con prefijo; `-webkit-mask-composite` usa nombres viejos (`source-in`, `xor`); `background-clip:text` necesita `-webkit-background-clip:text`. **GPU cost:** muchos `mix-blend-mode` simultáneos en scroll = jank. **`prefers-reduced-motion`** envuelve los reveals. **A11y:** texto con `background-clip:text`/`mix-blend-mode` **sigue siendo texto real** (seleccionable, leído, indexable) PERO verifica contraste en el peor caso (un `difference` blanco sobre gris medio puede fallar); texto en SVG `<mask>` NO es seleccionable → añade `aria-label`.

## Masking/blend anti-patterns — blacklist
**animar `clip-path: polygon()` entre distinto número de vértices** (no interpola, salta) · **animar `path()` esperando suavidad** (main-thread o sin animar; usa `shape()`/`inset`/`circle`) · **olvidar `-webkit-mask-*`** (desaparece en Safari/iOS) · **`mix-blend-mode` sin `isolation:isolate`** en el padre (sangra hasta el body, color impredecible) · **mask gradient para un borde duro** (o clip-path para un fade suave — herramienta equivocada) · **texto en SVG `<mask>`/`<clipPath>` como único contenido textual** (invisible para SEO/lectores) · **`will-change: clip-path` permanente** en decenas de nodos · **decenas de capas con blend en una lista que scrollea** (repaint masivo) · **texto `difference` asumido legible siempre** (falla contra fondos de luminancia media) · **confundir `mask-mode: luminance` (blanco=visible) con `alpha`** (máscara invertida/vacía).
