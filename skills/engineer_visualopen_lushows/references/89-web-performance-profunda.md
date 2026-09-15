# 89 — Web performance profunda

## El waterfall de carga
HTML → CSS/JS bloqueante → fonts → images. Cada round-trip y recurso bloqueante retrasa el paint y la
interactividad. Optimizar = aplanar el waterfall (menos bloqueantes, descubrir los críticos antes, diferir el resto).

## Core Web Vitals (umbrales 2026)
**LCP** ≤2.5s (carga) · **INP** ≤200ms (responsividad, reemplazó FID 2024) · **CLS** ≤0.1 (estabilidad).

## INP = el problema #1 de 2026 (~43% de sitios fallan)
Mide la peor latencia interacción-a-paint de la sesión. Causa = **long tasks (>50ms)** bloqueando el main thread.
Tácticas: parte long tasks (`scheduler.yield()` para ceder a mitad de interacción), difiere JS no crítico, minimiza DOM, y **el mayor lever: shippea MENOS JavaScript.**
```js
async function handleClick(){ updateUIImmediately(); await scheduler.yield(); doExpensiveWork() }
```
**RSC/streaming SSR** es el fix estructural: RSC shippea **cero JS cliente** para partes no interactivas (Frigade: -62% bundle, ~3× render). **Ojo:** SSR plano ayuda al *initial load* (LCP/FCP) pero NO arregla INP por sí solo (la interactividad sigue siendo cliente).

## LCP / CLS tácticas
**LCP:** `preload` la imagen/font LCP, critical CSS inline en `<head>`, font preload + `font-display: swap`, TTFB
<200ms, `fetchpriority="high"` en el hero, **nunca lazy-load la imagen LCP**. WebP/AVIF (WebP ~30% < JPEG). **CLS:** `width/height` (o `aspect-ratio`) en todo media/iframe/ad; reserva espacio para contenido dinámico; fallbacks size-adjusted.

## Bundle / caching / lab vs campo
Code-split (solo carga el código de la página inicial), lazy-load con `import()`, tree shaking (ESM,
`sideEffects:false`). Caching en capas (CDN edge + headers immutable + service worker). **Lab vs campo (crítico):**
**Lighthouse** = una carga sintética en tu laptop rápida. **CrUX** = agregado 28-días de usuarios REALES — **y CrUX, no Lighthouse, manda en el ranking de Google.** Tras un fix, ~28-30 días para que Search Console refleje el campo.

## Gotchas
1. Lighthouse 100 con CrUX fallando es común — optimiza para campo, no el lab score.
2. Preload de *todo* causa contención de ancho de banda — preload solo el recurso LCP.
3. SSR/RSC no salva INP si hidratas un árbol interactivo enorme — mide el JS cliente.
4. Scripts de terceros (analytics/chat/ads) son los top regresores de INP/CLS — defer/facade/sandbox.
5. CLS aparece solo en redes lentas/fonts/ads tardíos — testea con throttle.
6. `font-display: swap` sin fallback size-matched cambia CLS por reflow visible — usa `size-adjust`.

**Fuentes:** digitalapplied.com (CWV 2026) · bknddevelopment.com (INP 2026) · flutebyte.com (RSC moves INP) · linkgraph.com (CrUX+Lighthouse).
