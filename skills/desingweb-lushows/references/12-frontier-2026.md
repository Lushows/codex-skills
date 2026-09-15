# 12 — Frontera 2026 (capa de actualización: motion · WebGL · CSS)

Delta de lo más nuevo, por encima de `07-cinematic-motion`, `08-webgl-3d`, `09-modern-css`. Léelo cuando quieras lo último-último. Marca de soporte: **Baseline Widely** = seguro en todos lados · **Baseline Newly** = todos los motores actuales (ojo Safari/Firefox viejos) · **Chrome-only** = progressive-enhance con `@supports`.

---

## A. GSAP es 100% GRATIS (cambio mayor 2024–2026)

Webflow compró GreenSock; desde **GSAP 3.13** todos los plugins ex-Club son gratis para uso comercial: **ScrollSmoother, SplitText, MorphSVG, DrawSVG, Flip, Inertia, ScrambleText**. Versión actual **3.15.x**. Ya no hay razón para fingir estos efectos.

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15/dist/SplitText.min.js"></script>
```

### SplitText reescrito (la feature estrella) — reveal de titular canónico
50% más liviano, splitting correcto de emoji/acentos, y **masking + accesibilidad incorporados**:
```js
gsap.registerPlugin(SplitText, ScrollTrigger);
const split = SplitText.create(".headline", {
  type: "lines,words",
  mask: "lines",        // NUEVO: envuelve cada línea en overflow:hidden automáticamente
  autoSplit: true,      // NUEVO: re-divide al resize/cargar fuente (mató el bug histórico)
  aria: "auto",         // NUEVO: aria-label + aria-hidden gratis
  onSplit(self){
    return gsap.from(self.lines,{ yPercent:110, opacity:0, duration:.9, stagger:.08, ease:"expo.out" });
  }
});
```
`mask:"lines"` + `yPercent:110` ES el reveal que ves en casi todo hero Awwwards SOTD.

### `gsap.matchMedia()` — reemplazo moderno para responsive + reduced-motion
```js
gsap.matchMedia().add({
  reduce:"(prefers-reduced-motion: reduce)",
  desktop:"(min-width: 768px) and (prefers-reduced-motion: no-preference)"
},(ctx)=>{
  const {reduce,desktop}=ctx.conditions;
  if(reduce) return;            // no registres timelines; auto-revert al salir del contexto
  if(desktop){ /* pins/scrubs solo desktop */ }
});
```

### Lenis 1.3.x — integración canónica (driver = ticker de GSAP)
```js
import Lenis from "lenis";  // css: import "lenis/dist/lenis.css"
const lenis = new Lenis({ lerp:0.1, smoothWheel:true });  // 0.075 para "lujo" más pesado
lenis.on("scroll", ScrollTrigger.update);
gsap.ticker.add(t => lenis.raf(t*1000));   // una sola fuente de verdad
gsap.ticker.lagSmoothing(0);               // crítico: evita saltos
// reduced-motion: lenis.destroy() o lerp:1. Móvil: smoothTouch suele estorbar al rubber-band iOS.
```

## B. WebGL/3D — regla de decisión + stack actual

**Regla (memorizar):** finge con CSS/SVG salvo que necesites *refracción, parallax de profundidad, luz real o distorsión por-pixel*. Producto que solo rota + sombra suave → CSS `preserve-3d` + PNG. Vidrio/líquido/transmission, partículas GPU, transiciones por displacement → WebGL.

- **React Three Fiber** v9 (React 19) + `drei` + `postprocessing`. Hero de producto-vidrio flotante:
```jsx
<Canvas dpr={[1,2]} camera={{position:[0,0,6]}}>
  <Environment preset="studio"/>                {/* reflejos gratis, sin riggear luces */}
  <Float speed={1.5} rotationIntensity={0.6} floatIntensity={1}>
    <mesh><icosahedronGeometry args={[1.4,4]}/>
      <MeshTransmissionMaterial thickness={0.6} roughness={0.1} chromaticAberration={0.4} distortion={0.3}/>
    </mesh>
  </Float>
</Canvas>
```
  **Perf (clave — `MeshTransmissionMaterial` clava la GPU):** `samples={6}` máx, `resolution={256}`, `dpr={[1,2]}`, `frameloop="demand"` si estático, **lazy-mount** del `<Canvas>` tras 1er scroll (IntersectionObserver), instancing para mallas repetidas.
- **OGL** (oframe/ogl) — favorito de estudio para efectos de imagen 2D (displacement/hover): cero-dependencias, diminuto. Úsalo cuando "solo renderizas un quad texturizado y corres un fragment shader".
- **No-code 2026:** **Unicorn Studio** (breakout — 36kb, shader/scroll/hover, mejor perf-por-esfuerzo, default no-code) · **Spline** (3D real/físicas/AR, más pesado → lazy-load) · **Rive** (micro-interacciones por state-machine, gana en Android viejo; NO para hero 3D).

## C. Shaders "in" 2026

Estética dominante: **mesh gradients animados + grano**, distorsión líquida/lente en hover, warps por velocidad de scroll. Atajo que todos adoptan: **Paper Design shaders** (`@paper-design/shaders-react`, open source):
```jsx
import { MeshGradient } from "@paper-design/shaders-react";
<MeshGradient colors={["#cc3333","#cc9933","#99cc33","#33cc33"]}
  distortion={0.8} swirl={0.1} speed={1} grainMixer={0.15} style={{width:"100%",height:"100vh"}}/>
```
`grainMixer` agrega la capa de grano que hace el gradiente "cálido/impreso" en vez de "estéril digital" — el detalle definitorio 2026. Vanilla: `@paper-design/shaders`.

**Aberración cromática / lente en hover** (núcleo GLSL, para plano texturizado OGL/Three):
```glsl
vec2 dir = vUv - uMouse; float d = length(dir);
float s = uHover * 0.02 * (1.0 - smoothstep(0.0, 0.5, d));   // offsets <0.02 o "grita demo"
float r = texture2D(uTex, vUv + dir*s*1.5).r;
float g = texture2D(uTex, vUv + dir*s*1.0).g;
float b = texture2D(uTex, vUv + dir*s*0.5).b;
gl_FragColor = vec4(r,g,b,1.0);
```
Maneja `uHover` con GSAP; alimenta velocidad de scroll a `s` para scroll-warp. **Riesgo:** mesh-gradient es barato y seguro; transmission/GPGPU/fluidos son hambrientos → solo hero, nunca detrás de texto que se lee.

## D. View Transitions API — transiciones de página NATIVAS (reemplaza Barba.js en la mayoría)

Same-doc **Baseline Newly** (oct 2025). Cross-doc/MPA: **Chrome/Edge 126+, Safari 18.2+** (Firefox same-doc). MPA = nav animada instantánea sin framework — opt-in en AMBAS páginas:
```css
@view-transition { navigation: auto; }
::view-transition-old(root){ animation: fade .35s ease both; }
.hero-img { view-transition-name: hero; }   /* elemento compartido que "morphea" entre páginas */
```
SPA/React: `document.startViewTransition(()=>updateDOM())`. Nuevo 2025: `view-transition-name:match-element`, `view-transition-class`, `:active-view-transition`.

## E. CSS recién llegado (2024–2026) — snippets mínimos + soporte

- **Scroll-driven animations** *(Baseline Newly: Chrome 115+, Safari 26, FF 144+)* — efectos de scroll sin JS, en el compositor. Siempre `@supports (animation-timeline: scroll())` + `prefers-reduced-motion`.
```css
@keyframes reveal{from{opacity:0;translate:0 40px}to{opacity:1;translate:0 0}}
.card{animation:reveal linear both; animation-timeline:view(); animation-range:entry 0% cover 35%}
.progress{transform-origin:left;animation:grow linear;animation-timeline:scroll(root block)}
```
- **`@starting-style` + `transition-behavior:allow-discrete`** *(Baseline Newly)* — anima entrada **y salida**, incl. `display:none`/popover/dialog. La forma moderna de animar "desde nada".
```css
.toast{transition:opacity .3s, transform .3s, overlay .3s allow-discrete, display .3s allow-discrete; opacity:1}
@starting-style{ .toast{opacity:0; transform:translateY(1rem)} }
```
- **Popover API** *(Baseline Newly)* — top-layer declarativo, a11y/focus/dismiss gratis: `<button popovertarget="m">` + `<div id="m" popover>`.
- **Anchor positioning** *(Chrome/Edge 125+, Safari 26+, FF 147+ → enhance)* — tooltips/menús atados a un elemento con fallback de overflow, mata Floating UI:
```css
.btn{anchor-name:--t} .menu{position:absolute;position-anchor:--t;top:anchor(bottom);position-try-fallbacks:flip-block}
```
- **`text-wrap: balance`** (titulares) *(Baseline Newly)* **/ `pretty`** (body, sin huérfanas) — jerarquía limpia gratis.
- **`field-sizing: content`** *(Chrome 123+, Safari 26; FF no)* — inputs/textarea que crecen solos, sin JS.
- **Color OKLCH + relative syntax + `color-mix()`** — paleta entera desde 1 token, sin lodo gris:
```css
--brand: oklch(62% .21 264);
--brand-hover: color-mix(in oklch, var(--brand), white 12%);
--brand-tint:  oklch(from var(--brand) 95% .04 h);
--surface:     oklch(from var(--brand) l c h / 8%);
```
- **Container queries + style queries** *(size Widely, style Newly)*, **`:has()`** *(Widely)*, **subgrid** *(Newly)*, **nesting nativo** *(Widely)*.
- **Bleeding edge Chrome-only (solo decorativo, nunca load-bearing):** `@function`, `if()`, `corner-shape:squircle`, `text-box:trim-both`, `sibling-index()`, `::scroll-button()/::scroll-marker` (carruseles nativos), speculation rules.

## F. Tipografía fluida + fuentes que se sienten premium (gratis)

- **Escala fluida tipo Utopia** (ancla en `rem`, no px, para respetar zoom):
```css
:root{
  --step-0: clamp(1rem, .91rem + .43vi, 1.25rem);
  --step-1: clamp(1.2rem, 1.07rem + .66vi, 1.56rem);
  --step-3: clamp(1.73rem, 1.43rem + 1.48vi, 2.44rem);
  --space-s-l: clamp(1rem, .5rem + 2.5vi, 2rem);
}
```
  Cambia `vi`→`cqi` para que el tipo escale al *contenedor* (sidebars/modales/zoom).
- **Variables one-file:** subset con glyphhanger (corta 60–80%), self-host, `preload` solo la cara crítica, `font-display:swap` (body) u `optional` (no crítico) + `size-adjust`/`ascent-override` en fallback para matar CLS.
- **`font-optical-sizing:auto`** — titulares más apretados, cuerpo más abierto. "Caro" gratis.
- **Free premium:** Geist/Geist Mono, Satoshi, General Sans, Instrument Sans/Serif, **Bricolage Grotesque** (variable con carácter), **Fraunces** (serif variable opsz/SOFT/WONK), Newsreader (serif editorial), Hanken Grotesk, Schibsted Grotesk, Inter (workhorse opsz).
- **Detalles caros:** `text-wrap:pretty`, `text-box:trim-both cap alphabetic` (centrado óptico), `letter-spacing:-.02em` en display, `font-feature-settings:'ss01','cv05'`.

## G. Performance frontera (Core Web Vitals 2026)

Umbrales p75: **LCP < 2.5s · INP < 200ms** (reemplazó a FID — el más fallado, ~43% de sitios fallan) **· CLS < 0.1**.

- **LCP:** `<img fetchpriority="high">` en el héroe, **nunca** `loading="lazy"` ahí; el `src` en HTML SSR (no inyectado por JS/`data-src`); `srcset`+`sizes`; sirve **AVIF**→WebP. La mayoría pierde en *render-delay*, no descarga → inline critical CSS, `preconnect` a orígenes de fuentes/imágenes.
- **INP:** tareas largas >50ms son el enemigo. Parte trabajo con `await scheduler.yield()`. Prefiere CSS Baseline (popover, dialog, `:has()`, anchor, scroll-driven) sobre JS. Code-split, mata JS sin uso (Coverage), batch de lecturas/escrituras DOM.
- **Render budget:** `content-visibility:auto; contain-intrinsic-size:auto 600px` para saltar render fuera de pantalla; `contain:layout paint` en widgets.
- **Speculation Rules** (nav instantánea, casi cero JS):
```html
<script type="speculationrules">{"prerender":[{"where":{"href_matches":"/*"},"eagerness":"moderate"}]}</script>
```
  `moderate` = prerender al hover/pointerdown. Combina con MPA View Transitions. Asegura bfcache (sin `Cache-Control:no-store`, sin `unload`).

## H. Efectos tasteful en CSS puro (sin JS)

- **Mesh gradient animado** (`@property` lo mueve, GPU-barato):
```css
@property --x{syntax:"<percentage>";inherits:false;initial-value:20%}
@keyframes drift{50%{--x:80%}}
.mesh{animation:drift 14s ease-in-out infinite;background:
  radial-gradient(40% 50% at var(--x) 30%, oklch(70% .2 300/.9), transparent),
  radial-gradient(45% 55% at 80% 70%, oklch(72% .19 210/.85), transparent), oklch(20% .03 280)}
```
- **Grano fílmico** (turbulence SVG inline, sin asset) → ver `11-ecommerce-brand-systems` §"frescura"; opacity 4–8%, `mix-blend-mode:multiply`.
- **Glassmorphism 2026 bien hecho** (blur sutil + hairline + saturación + contraste a11y):
```css
.glass{background:color-mix(in oklch, white 12%, transparent);
  backdrop-filter:blur(12px) saturate(160%);
  border:1px solid color-mix(in oklch, white 22%, transparent);
  box-shadow:0 8px 32px oklch(0% 0 0/.25), inset 0 1px 0 oklch(100% 0 0/.18)}
@supports not (backdrop-filter:blur(1px)){ .glass{background:oklch(20% .02 280/.8)} }
```
  `backdrop-filter` es costoso: no apiles muchos ni lo animes en superficies grandes (mata INP en móvil gama baja).

---

**Regla de oro:** lo nuevo no reemplaza la disciplina. Easing + restricción siguen siendo el sello premium (no la cantidad de efectos). Animá solo `transform`/`opacity`, `will-change` justo-a-tiempo, todo bajo `@media (prefers-reduced-motion: no-preference)`, y nada pesado en el critical path.
