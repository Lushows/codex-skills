# 40 — Performance engineering (Lighthouse ~100 & CWV de élite)

Playbook consolidado y profundo (12 tiene lo básico de CWV; esto es el deep one). **Léelo cuando optimices velocidad o un sitio falle CWV.** El objetivo no es pasar el test — es ser rápido en **campo** (CrUX p75, lo que Google rankea).

## 1. Core Web Vitals 2026

Umbrales (p75, ventana 28 días, datos de campo): **LCP ≤2.5s · INP ≤200ms · CLS ≤0.1.** (Objetivo interno LCP 2.0s; **INP es el más fallado, ~43% no pasa.**)
**LCP — la verdad incómoda:** el cuello de botella casi nunca es descargar la imagen. En sitios pobres el desglose mediano es TTFB ~2270ms, resource load delay ~1290ms, render delay ~360ms — pasan **4× más tiempo esperando para empezar a descargar que descargando**. Ataca en orden: (1) **TTFB** con CDN/edge + caché; (2) **resource load delay** — el `<img>` LCP en el HTML inicial (35% no son descubribles), con `fetchpriority="high"` + `preload` si entra por CSS/JS; (3) **render delay** eliminando JS/CSS render-blocking + SSR.
```html
<img src="/hero.avif" fetchpriority="high" width="1200" height="630" decoding="async" alt="...">
<link rel="preload" as="image" href="/hero.avif" fetchpriority="high"><!-- si se descubre tarde -->
```
**INP — el más difícil:** input delay + processing + presentation. Fix #1: **romper long tasks** (>50ms bloquea). Usa **`scheduler.yield()`** (cede y continúa con prioridad, por delante de terceros):
```js
for(const item of items){ doWork(item); if(shouldYield()) await scheduler.yield(); }
```
Otras palancas: pinta el feedback visual ANTES del trabajo pesado; reduce JS; evita **forced synchronous layout** (agrupa lecturas/escrituras DOM); DOM pequeño + `content-visibility`.
**CLS:** imágenes/iframes/ads sin dimensión (`width`/`height` o `aspect-ratio`) · font swap (`size-adjust`/`ascent-override`) · contenido dinámico inyectado (reserva con min-height/skeleton) · animar layout (anima solo `transform`/`opacity`). **bfcache elimina los shifts** en back/forward.
**Campo vs lab:** Lighthouse = lab (1 carga simulada). Lo que rankea = **campo (CrUX p75)**. Instrumenta con **`web-vitals.js`** (atribución) → tu analytics, para ver el subpart culpable.

## 2. JavaScript & bundle — "ship less JS"

El JS es el recurso más caro (descarga + parse + compile + execute + **hydration**).
- **Budgets:** móvil <100-170KB JS comprimido en ruta crítica; falla el CI si se excede (`lighthouse-ci` assertions, `size-limit`).
- **Code splitting + dynamic `import()`** por ruta + componentes pesados bajo demanda (modales, charts, editores). **Tree-shaking real** (imports nombrados, `sideEffects:false`, evita moment/lodash monolíticos).
- **Coverage** (DevTools) para cazar JS/CSS no usado. `defer`/`async` en todo lo no crítico; nada síncrono en `<head>`.
- **Hydration cost** (el impuesto a INP): **islands/partial hydration** (Astro/Fresh: header/footer = 0 JS) o **RSC** (Next App Router: Server Components no producen bundle cliente; solo `"use client"` viaja). Para SPAs muy interactivas evalúa Svelte/SolidJS (menor overhead).
- **Terceros (el cáncer del INP):** **facade pattern** (carga chat/YouTube/mapa solo al click) + **Partytown** (analytics/tags a Web Worker). Audita Tag Manager.

## 3. Pipeline de imágenes & media

- **Formatos:** **AVIF** → WebP → JPEG vía `<picture>` (AVIF q~65 ≈ JPEG 85). **Responsive** `srcset`+`sizes` (refleja el ancho REAL de render). **Targets:** hero <200KB, contenido <100KB, thumbs <50KB.
- **Lazy correcto:** `loading="lazy"`+`decoding="async"` en below-the-fold; **NUNCA en la LCP** (peor error). LCP lleva `fetchpriority="high"`.
- **CDN de imágenes** (Cloudinary/imgix/Vercel) negocia formato por `Accept`. **`content-visibility:auto`** + `contain-intrinsic-size` en secciones largas fuera de viewport (sin CLS si declaras el tamaño).

## 4. Fonts & CSS

- **`font-display:swap`** (`optional` para CLS cero garantizado). **`<link rel=preload as=font crossorigin>`** solo la cara crítica. **Subset + WOFF2 + variable font.**
- **Anti-CLS de fuentes:** fallback con `size-adjust`/`ascent-override`/`descent-override`/`line-gap-override` (Fontaine o `next/font` lo calcula; ~30% mejor CLS).
- **Critical CSS** inline en `<head>`, resto async; elimina CSS no usado (Coverage/PurgeCSS); minimiza `@import` (encadena requests); `contain`/`content-visibility` para acotar el render path.

## 5. Red & entrega

- **HTTP/2-3** (QUIC) + **CDN/edge** (solo 33% de HTML se sirve de CDN — gran oportunidad de TTFB). **Brotli** en texto/JS/CSS.
- **Caching por "¿cambia la URL al cambiar el contenido?":** assets con hash → `Cache-Control: public, max-age=31536000, immutable`; HTML/API → `max-age` corto + `stale-while-revalidate`.
- **bfcache:** evita `Cache-Control: no-store` y `unload` listeners (usa `pagehide`). **Resource hints en prioridad:** `preconnect`/`dns-prefetch` (orígenes terceros) > `preload` (crítico descubierto tarde) > `prefetch` (próxima nav).
- **Speculation Rules API** (nav instantánea): `prerender` (página completa en background → 0ms al click) con `eagerness:"moderate"` (hover). **Early Hints (103)** adelanta `preload`/`preconnect` durante el thinking-time del backend.
```html
<script type="speculationrules">{"prerender":[{"where":{"href_matches":"/*"},"eagerness":"moderate"}]}</script>
```

## 6. Estrategia de render & medición

**Decisión:** **SSG/ISR** (estático: blogs/marketing — TTFB/LCP más bajos) · **SSR/streaming + RSC** (dinámico/personalizado: shell rápido, hidratación parcial) · **edge** (personalización con TTFB mínimo) · **CSR puro** (solo apps tras login muy interactivas; paga hydration). Regla: **SSR/SSG > CSR para LCP**, **islands/RSC > SPA para INP**.
**Medición:** lab (Lighthouse/PageSpeed, con sus límites) · campo (CrUX + `web-vitals.js` → RUM, la verdad) · profiling INP (Performance panel, long tasks + forced reflows) · CI (`lighthouse-ci` + bundle budgets que rompen el build).

### Checklist "Lighthouse ~100"
LCP `<img>` en HTML + `fetchpriority=high` + sin lazy + preload · TTFB bajo (CDN/edge + SWR) · AVIF/WebP + srcset/sizes + dimensiones explícitas · JS crítico <~150KB + splitting + terceros con facade/Partytown · `defer`/`async` + coverage limpio · fonts swap + métricas de fallback + preload + WOFF2 subset · critical CSS inline + CSS no usado eliminado + `content-visibility` · long tasks rotas con `scheduler.yield()` + sin forced reflow · Brotli + HTTP/3 + `immutable` · bfcache-eligible + Speculation Rules + preconnect · CLS: nada anima layout + espacio reservado · a11y/SEO/best-practices al 100.

## Performance anti-patterns — blacklist
`loading="lazy"` en la LCP · hidratar toda la página cuando el 90% es estático · chat/analytics/widgets síncronos en `<head>` · imágenes/embeds sin dimensión · animar `top/left/width/margin` · banners/ads encima sin reservar espacio · `Cache-Control:no-store` "por si acaso" (rompe bfcache) · confiar solo en Lighthouse (lab) e ignorar CrUX (campo) · `@import` encadenados + fonts sin métricas de fallback · una imagen gigante para todos los viewports · bundles monolíticos sin splitting/budgets · forced synchronous layout en loops (leer `offsetHeight` tras escribir estilos).
