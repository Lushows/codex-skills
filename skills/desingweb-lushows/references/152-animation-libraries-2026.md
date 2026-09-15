# 152 — Librerías y herramientas de animación (2026)

**CRAFT, decisión de stack.** Léelo para elegir QUÉ herramienta para cada job. Pareja de 07/12 (motion/frontier), 34 (Motion React), 08/38 (WebGL libs), 04 (motion library). Regla de oro: **scroll/timeline → GSAP; React+estado/gestos → Motion; vector interactivo → Rive; AE export → Lottie; 3D → R3F/Three/OGL; smooth scroll → Lenis. No mezcles dos motores para el mismo eje de animación.**

## 1. The decision map

| Trabajo | Herramienta 2026 | Por qué |
|---|---|---|
| **Scroll-driven + timelines complejos** | **GSAP + ScrollTrigger** | El estándar de oro. Pin, scrub, secuencia absoluta. |
| **Animación de componentes React** | **Motion** (`motion/react`) | Gestos, layout, `AnimatePresence`, spring declarativo. |
| **Micro-animaciones diminutas / vanilla** | **Motion One** (`motion`) | ~4KB, WAAPI, compositor-thread. |
| **SVG/JS declarativo, stagger** | **Anime.js v4** | Ligero, ESM, timeline, SVG. |
| **Vector interactivo / personajes / iconos con estado** | **Rive** | State machine en runtime, archivo minúsculo. |
| **Export de After Effects, playback** | **Lottie** (dotLottie) | Pipeline AE → JSON. |
| **Escena 3D en código** | **R3F / Three.js / OGL** | WebGL declarativo (React) o minimal. |
| **3D no-code, embeds** | **Spline** | Diseñas en su editor (pesado, lazy-load). |
| **Smooth scroll** | **Lenis** | Inercia, sincroniza con ScrollTrigger. |
| **Physics (colisiones, gravedad)** | **Matter.js** | Motor 2D rígido. |
| **Split de texto** | **GSAP SplitText** (free) o Splitting.js | Animar tipografía. |
| **Sequencing tipo editor** | **Theatre.js** | Timeline visual con keyframes editables. |

## 2. GSAP en 2026 — ahora 100% FREE (post-Webflow)

**Cambio de licencia (headline):** Webflow adquirió GreenSock y **liberó todo GSAP gratis**, incluido uso comercial y **todos los plugins Club** (ya no existe el tier "Club GSAP"). Plugins clave: **ScrollTrigger** (dispara/scrubea según scroll; `pin`, `scrub`, `snap` — el caballo de batalla), **SplitText** (reescrito, ~50% más liviano; chars/words/lines con mejor manejo de emojis/line-breaks), **Flip** (FLIP technique para reordenar grids/expandir cards), **Draggable + InertiaPlugin** (arrastre con momentum), **MorphSVG** (interpola entre paths SVG arbitrarios), **DrawSVG** (`stroke-dashoffset` para "dibujado a mano"), **MotionPath** (mueve a lo largo de un path). En React: `useGSAP()` (hook con cleanup automático de `gsap.context()`).

## 3. Motion (ex-Framer Motion) + Motion One

A mediados de 2025 **Framer Motion se independizó y se renombró a Motion**: el paquete pasó de `framer-motion` a `motion`, import recomendado **`motion/react`** (2026 va por v12). **`motion/react`** (React: `<motion.div>`, `animate`, `AnimatePresence` enter/exit, `layout` animations, `whileHover/whileInView`, drag, spring declarativo — la opción cuando la animación es estado-derivada dentro del árbol React). **Motion One (`motion` vanilla)** (núcleo ~4KB framework-agnostic sobre **WAAPI**; corre `transform`/`opacity` en el compositor thread — ideal para micro-interacciones donde GSAP sería overkill). **Motion sobre GSAP cuando:** estás en React con animaciones declarativas ligadas a estado/gestos/layout, o bundle mínimo. **GSAP sobre Motion cuando:** timeline larga, scroll cinematográfico, morphing SVG, control imperativo fino.

## 4. Anime.js v4

Reescritura completa, **ESM-first y tree-shakeable** (latest ~v4.4): nueva API modular — **`createTimeline()`** (secuenciación; `stagger()` como time position), **Scope API** (`createScope()` — instancias reaccionan a media queries, comparten defaults, se **revierten en batch**, clave en cleanup React/Vue), WAAPI opcional + helpers SVG. **Cuándo:** algo más ligero y declarativo que GSAP para SVG/stagger/morphing simple, sin entrar en el ecosistema de plugins (no iguala a ScrollTrigger/MorphSVG en lo cinematográfico; el "sweet spot" de animación de UI media).

## 5. Rive vs Lottie vs Spline

| | **Rive** | **Lottie** | **Spline** |
|---|---|---|---|
| Naturaleza | Vector interactivo con **state machine** | Vector pre-renderizado (export AE) | 3D no-code |
| Interactividad | **Alta** (inputs, hover, estados runtime) | Baja (playback, scrubbing) | Media |
| Tamaño | **Muy pequeño** (.riv binario) | Pequeño-medio (JSON) | **Pesado** (WebGL+assets) |
| Perf | Excelente, runtime propio | Buena (dotLottie comprime) | La más costosa (GPU) |
| Pipeline | Editor Rive | After Effects + Bodymovin | Editor Spline |

**Rive es el favorito 2026** para personajes/iconos/botones interactivos (un `.riv` responde a inputs sin recargar). **Lottie** cuando el activo nace en AE y solo necesitas reproducirlo (usa **dotLottie** comprimido). **Spline** para un hero 3D rápido sin escribir Three.js, asumiendo el coste de bundle (lazy-load obligatorio).

## 6. Stack recipes & perf

**Stack canónico de award site:** `Lenis (smooth scroll) + GSAP ScrollTrigger (orquestación) + Three/R3F/OGL (capa WebGL del hero)`. Lenis emite su posición de scroll, la sincronizas con ScrollTrigger (`lenis.on('scroll', ScrollTrigger.update)` + `gsap.ticker`). OGL es la opción minimalista (~10KB) para un solo efecto shader. **Disciplina:** **lazy-load de librerías pesadas** (Three, Spline, Rive) con dynamic `import()` (nunca en el bundle inicial); **SSR caveats** (WebGL/Lenis/muchos plugins GSAP tocan `window`/`document` → inicializa en `useEffect`/`onMount`; en Next `dynamic(()=>..., {ssr:false})`); anima solo `transform`/`opacity`; **`prefers-reduced-motion` SIEMPRE** (`gsap.matchMedia()` con `(prefers-reduced-motion:reduce)`, o `useReducedMotion()` en Motion); limpia siempre (`useGSAP()`/`ctx.revert()`, `lenis.destroy()`, `ScrollTrigger.killAll()`).

## Library-choice anti-patterns — blacklist
**importar todo Three.js para un efecto simple** (usa OGL o un shader plano) · **GSAP + Motion animando el mismo elemento** (conflicto de motores; elige uno por eje) · **Spline en el hero sin lazy-load** (mata el LCP en móvil) · **Lottie para algo interactivo** (usa Rive; Lottie es playback) · **jQuery animate / CSS transitions improvisadas para secuencias largas** (usa un timeline) · **animar `width/height/margin`** en vez de `transform` · **olvidar `prefers-reduced-motion`** · **pagar/buscar "Club GSAP"** (ya no existe; todo GSAP es gratis en 2026) · **smooth scroll casero con RAF** en vez de Lenis (reinventas mal la rueda y rompes ScrollTrigger) · **cargar `framer-motion`** (paquete viejo; migra a `motion`/`motion/react`).
