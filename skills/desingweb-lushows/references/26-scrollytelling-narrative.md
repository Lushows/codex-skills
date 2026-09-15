# 26 — Scrollytelling & narrativa inmersiva

Construir experiencias de scroll cinematográficas tipo Apple (AirPods/iPhone), NYT/Pudding, Active Theory. **Léelo cuando quieras una página narrativa, un hero "video por scroll", o storytelling de producto.** Extiende 07 (motion). Regla: **una sola pieza "pesada" por página**; el resto, reveals ligeros.

## 1. Patrones canónicos

| Patrón | Qué es | Cuándo |
|---|---|---|
| **Sticky graphic + scrolling text** (el clásico) | Visual fijo (`position:sticky`) a un lado; el texto scrollea y dispara estados | Periodismo de datos, explicar con un visual persistente (NYT/Pudding) |
| **Step-triggered states** | El scroll cruza "steps"; cada uno activa un estado discreto | Transiciones por pasos (mejor a11y) |
| **Scroll-scrubbed animation/video** | El progreso de scroll mapea 1:1 a un timeline | El "video on scroll" de Apple, producto hero |
| **Pinned sequence** | Sección pineada mientras su contenido interno avanza | Tours de producto, features encadenadas |
| **Horizontal-in-vertical** | Scroll vertical → movimiento horizontal de un track pineado | Galerías, líneas de tiempo |
| **Image sequence scrubbing** | N frames a `<canvas>` según progreso | Efecto AirPods/iPhone |
| **Reveal choreography** | Entradas escalonadas al entrar en viewport | Todo. El default barato y efectivo |

## 2. Image-sequence scrubbing estilo Apple

Apple usaba secuencias JPEG a canvas; desde ~2024 migró a **video scrubbing comprimido** (~70-80% menos peso). El cuello de botella no es la descarga sino el **decode** → pre-decodifica.
```js
const canvas=document.querySelector("#hero-canvas"), ctx=canvas.getContext("2d");
const frameCount=148, urls=i=>`/frames/${String(i+1).padStart(4,"0")}.webp`;
canvas.width=1158; canvas.height=770;
const images=[], seq={frame:0};
for(let i=0;i<frameCount;i++){ const img=new Image(); img.src=urls(i); img.decode?.().catch(()=>{}); images[i]=img; }
function render(){ const img=images[seq.frame]; if(!img||!img.complete)return;
  ctx.clearRect(0,0,canvas.width,canvas.height); ctx.drawImage(img,0,0,canvas.width,canvas.height); }
gsap.to(seq,{ frame:frameCount-1, snap:"frame", ease:"none",
  scrollTrigger:{ trigger:"#hero", start:"top top", end:"+=4000", scrub:0.5, pin:true }, onUpdate:render });
images[0].onload=render;
```
**Guía:** 60-150 frames (>200 = peso prohibitivo) · resolución por DPR/breakpoint (desktop ~1440-1600, mobile 750-828 o **still estático**) · WebP/AVIF (~30-80KB/frame → 100 frames ≈ 3-8MB) · individuales > sprite sheets (cache + lazy por rango).
**Alternativa video:** `gsap.to(video,{currentTime:()=>video.duration, scrollTrigger:{scrub:true,pin:true}})`. Pitfalls: iOS requiere `muted`+`playsinline`; **seeking entrecortado** salvo GOP corto (muchos I-frames, `-g 1` en ffmpeg); `video.duration` es `NaN` hasta `loadedmetadata`. **Canvas = control perfecto + más peso; video = ligero + seeking frágil.** Para heros premium, canvas gana en suavidad.

## 3. Herramientas 2026

- **GSAP ScrollTrigger** (100% gratis desde 2025) — estándar para scrub/pin complejo (`pin`, `scrub` número=inercia, `snap`).
- **Lenis** — smooth-scroll de facto. Sincroniza con ScrollTrigger (un solo rAF): `lenis.on("scroll",ScrollTrigger.update); gsap.ticker.add(t=>lenis.raf(t*1000)); gsap.ticker.lagSmoothing(0)`.
- **Scrollama** (The Pudding) — **estándar de periodismo** para text-step triggers (IntersectionObserver, ligero, accesible):
```js
scrollama().setup({step:".step", offset:0.5, progress:true})
  .onStepEnter(({element,index})=>{ element.classList.add("is-active"); updateGraphic(index); })
  .onStepExit(({element})=>element.classList.remove("is-active"));
```
- **IntersectionObserver a pelo** — reveals y steps simples sin dependencias (`rootMargin:"-45% 0px -45% 0px"` = trigger en mitad de viewport).
- **CSS scroll-driven** (`animation-timeline: scroll()/view()`) — **nativo, off-main-thread, 60fps real**. Chromium 115+/Safari 18+ (~85% caniuse). Para reveals/parallax/progress sin JS. El futuro de los efectos ligeros; GSAP para lo complejo.
- **Theatre.js** — editor visual de timelines para coreografía 3D/cámara compleja (con R3F).

**Cuándo cuál:** texto-por-pasos → Scrollama · reveals/parallax simples → CSS nativo · pin+scrub cinematográfico → GSAP · inercia global → Lenis · 3D/cámara → Theatre.js+R3F.

## 4. Narrativa & craft UX

- **Pacing:** ~25-40px de scroll por frame (hero de 100 frames ≈ `end:+=3000-4000`). Cada step de texto ≥ una pantalla de respiro. Rápido = mareo; lento = abandono.
- **Scroll-jacking — el riesgo:** secuestrar el scroll (forzar saltos, "1 scroll = 1 slide", deshabilitar rueda/teclado) rompe la expectativa, frustra trackpad/teclado y daña a11y. **Scrubbing sí (el contenido avanza con tu scroll natural), hijacking no.** La inercia de Lenis ≠ hijacking.
- **Progreso:** barra de capítulo / contador de steps / mini-índice. Las secciones pineadas largas sin progreso se sienten como un cuelgue.
- **Devolver el control:** toda sección pineada termina y suelta; ofrece "skip"/anclas en experiencias largas.
- **Mobile (lo difícil):** viewport cambia con la barra (usa `dvh`, no `vh`); `sticky` frágil; secuencias pesadas matan datos/batería. Estrategias: still estático en mobile, convertir sticky+scrub en steps apilados, bajar resolución por `matchMedia`.
- **A11y (no opcional):** el contenido **debe existir y leerse sin JS** (texto narrativo en HTML real; el scroll solo realza). `prefers-reduced-motion`: usa `gsap.matchMedia().add("(prefers-reduced-motion: no-preference)", ()=>{...})` — sin rama reduce, el DOM queda en estado base legible. Teclado: nunca captures `keydown` para hijacking.

## 5. Performance para narrativa pesada

- **Image sequence:** AVIF/WebP, resolución por DPR, `img.decode()`, **lazy por rango** (no cargues 150 frames de golpe si está bajo el fold).
- **Canvas siempre** para sequences (un elemento, sin layout/paint de 150 `<img>`).
- **`will-change` con disciplina** (solo lo que anima ahora, quítalo al terminar). Anima solo `transform`/`opacity`.
- **60fps:** evita `width/height/top/left`; `onUpdate` barato (un `drawImage`); no añadas listeners de `scroll` crudos (Lenis/GSAP ya hacen rAF-throttle).
- **LCP cuando el hero es canvas:** pinta un `<img>` poster `fetchpriority="high"` hasta que la secuencia esté lista; pre-carga el frame 0 con `<link rel="preload" as="image">`.
- **Mobile fallback:** still estático o secuencia reducida (30 frames); detecta `navigator.connection?.saveData`/`deviceMemory`.

## 6. Frescura 2026 vs anticuado

**Actual:** WebGL/3D integrado con mesura (R3F, shaders sutiles) · **calm cinematic** (movimientos lentos, eases largos, aire negativo, una idea por pantalla, SplitText por palabra/línea) · generative/orgánico sutil reactivo al scroll · CSS scroll-driven nativo para micro-efectos · **performance como estética** (LCP <2.5s, 60fps = se percibe caro).

### Scrollytelling anti-patterns — blacklist
scroll-jacking agresivo (1 scroll=1 slide, deshabilitar rueda/teclado) · parallax en todo (cliché 2014) · secuencias 300+ frames sin fallback (20MB, mobile muere) · smooth-scroll exagerado (Lenis flotante que desincroniza el cursor) · pin sin escape que atrapa · animar `top/left/width` + `will-change:transform` global · cero fallback reduced-motion ni versión sin-JS · texto crítico encerrado en el scrub (ilegible a medio frame, invisible a buscadores) · efecto sin narrativa (scrub "porque se ve cool") · `vh` en mobile para secciones pineadas (usa `dvh`).
**Principio rector:** el scroll es el reloj de tu película, no un juguete. Cada beat avanza una historia, el contenido sobrevive sin JS, y nada le roba al usuario el control de su scroll.
