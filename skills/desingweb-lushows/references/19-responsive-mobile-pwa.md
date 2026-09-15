# 19 — Responsive, mobile-first & PWA

Playbook 2026. Móvil es **~70% del tráfico** (e-commerce LatAm, gama media Android + iPhones). Filosofía: **dirigido por contenido, no por dispositivo**; mobile-first siempre (CSS base = móvil, mejora hacia arriba). **Léelo en TODO proyecto** — el responsive no es opcional.

## 1. Responsive moderno (post-media-query)

Media queries = **layout global** (estructura, nav, tipografía global). **Container queries** = responsividad **a nivel de componente** (una card que vive en sidebar/modal/grid y se adapta a *su* espacio). Regla: media query para la página, container query para el componente reutilizable.
```css
.card-grid > *{ container-type:inline-size; container-name:card }
@container card (min-width:26rem){ .card{ grid-template-columns:40% 1fr; align-items:center } }
.card h3{ font-size:clamp(1rem, 4cqi, 1.5rem) }   /* cqi = 1% del inline-size del contenedor */
```
**Layouts intrínsecos** (grid que se adapta solo, sin breakpoints):
```css
.products{ display:grid; gap:clamp(1rem,3vw,2rem);
  grid-template-columns:repeat(auto-fit, minmax(min(16rem,100%), 1fr)) }  /* min() evita overflow <16rem */
.container{ width:min(100% - 2rem, 75rem); margin-inline:auto }          /* gutter + max-width */
```
**Tipografía fluida** (clamp; genera con utopia.fyi) y **`aspect-ratio`** (mata el padding-hack y el CLS): `.thumb{ aspect-ratio:4/3; object-fit:cover; width:100% }`.
**Breakpoints dirigidos por contenido:** ponlos *donde el contenido se rompe*, no en 375/768. Menos breakpoints, más lógica intrínseca.

## 2. UX móvil / táctil

**El viewport bug (`100vh` miente):** la barra de URL hace desbordar. Trío nuevo (Baseline jun-2025):
- `svh` (small, barra visible) → garantiza que TODO entra. Ideal hero above-the-fold.
- `lvh` (large, barra oculta) → máxima cobertura (cuidado).
- `dvh` (dynamic) → app shells/viewers; recalcula con repaints al scrollear (no en heros estáticos).
```css
.hero{ min-height:100vh; min-height:100svh }   /* el CTA nunca queda tapado por la barra */
```
**Safe areas (notch/home indicator)** con `env()` (requiere `viewport-fit=cover`):
```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```
```css
.sticky-cta{ position:fixed; inset-inline:0; bottom:0; padding-bottom:calc(12px + env(safe-area-inset-bottom)) }
```
**Touch targets:** mín **44px** (Apple) / 48px (Material); separa ≥8px. Incluye el padding en la cuenta.
**Zonas del pulgar:** acciones primarias en el **60-70% inferior** → patrones **bottom-nav** y **bottom-sheet** (en vez de menú superior y modal centrado). Bottom-sheet: `max-height:90dvh; overscroll-behavior:contain; border-radius:16px 16px 0 0`.
**Inputs — anti-zoom iOS:** iOS hace zoom si el input mide <16px. **Regla: `font-size:16px` en todos los inputs.** Teclado correcto:
```html
<input type="email" inputmode="email" autocomplete="email">
<input type="tel"   inputmode="tel"   autocomplete="tel">
<input inputmode="numeric" autocomplete="one-time-code">  <!-- OTP -->
<input inputmode="decimal">  <!-- precios -->  <input type="search" enterkeyhint="search">
```
**`touch-action`:** `.carousel{touch-action:pan-x}` · scroll-snap horizontal `scroll-snap-type:x mandatory`.
**Hover-safe** (táctil no tiene hover; nunca escondas lo crítico tras `:hover`): `@media (hover:hover) and (pointer:fine){ .card:hover .overlay{opacity:1} }`.
**`overscroll-behavior-y:contain`** evita pull-to-refresh accidental y scroll-chaining al body.

## 3. Performance en móvil real (gama media + 3G/4G)

Mentalidad **"ship less"**: el JS es lo que más mata en Android gama media. INP es el villano 2026 (~43% fallan).
**Imágenes (lo que más mueve LCP):**
```html
<img src="hero-800.avif" srcset="hero-480.avif 480w, hero-800.avif 800w, hero-1200.avif 1200w"
  sizes="(max-width:600px) 100vw, 50vw" width="1200" height="800" fetchpriority="high" alt="...">
```
- **AVIF** ahorra 40-60% vs JPEG (fallback WebP/JPEG con `<picture>`). `fetchpriority="high"` solo en el LCP.
- **NUNCA** `loading="lazy"` en la imagen LCP/hero (regresión garantizada); `lazy` solo bajo el fold.
- `width`+`height` o `aspect-ratio` en toda `<img>` → CLS=0.
**Fuentes:** `font-display:swap` + `<link rel=preload as=font crossorigin>` solo la cara crítica + `size-adjust` en fallback para evitar el salto.
**JS:** objetivo <~150-170KB comprimido en ruta crítica; `import()` diferido, `<script defer>`, prefiere CSS/WAAPI sobre libs pesadas; para INP rompe tareas largas (`scheduler.yield()`), no corras analytics/chat en el hilo principal al inicio.
**Testear:** Lighthouse "Slow 4G + 4× CPU" + **dispositivos reales gama media** + datos de campo (CrUX/web-vitals JS).

## 4. PWA en 2026 — estado honesto

- **Android (Chrome):** casi nativo. Install rico (`beforeinstallprompt` personalizable), **Web Push funciona en navegador** sin instalar, badging, share target. Vale mucho la pena.
- **iOS/Safari — límites reales:** Web Push existe desde iOS 16.4 **solo si la PWA está instalada en pantalla de inicio** (no en pestaña Safari). No hay `beforeinstallprompt` (install manual: Compartir → "Añadir a inicio") → audiencia alcanzable por push ~10-15× menor. Todos los navegadores iOS usan WebKit (mismas limitaciones).
**Manifest mínimo:**
```json
{ "name":"BIO-SETA Tienda", "short_name":"BIO-SETA", "start_url":"/?source=pwa", "display":"standalone",
  "background_color":"#0b1f17", "theme_color":"#0b1f17",
  "icons":[ {"src":"/icons/192.png","sizes":"192x192","type":"image/png"},
    {"src":"/icons/512.png","sizes":"512x512","type":"image/png"},
    {"src":"/icons/maskable.png","sizes":"512x512","type":"image/png","purpose":"maskable"} ] }
```
`<link rel="apple-touch-icon" href="/icons/180.png">` (iOS lo necesita) + `<meta name="theme-color">`.
**SW offline básico** (navigate → fallback `/offline.html`):
```js
self.addEventListener("install", e=>e.waitUntil(caches.open("v1").then(c=>c.addAll(["/","/offline.html"]))));
self.addEventListener("fetch", e=>{ if(e.request.mode==="navigate") e.respondWith(fetch(e.request).catch(()=>caches.match("/offline.html"))) });
```
**Cuándo recomendar (negocio pequeño LatAm):** **buen sitio móvil responsive** = mejor costo/beneficio, empieza ahí · **PWA** si quieres re-engagement por push en *Android* + offline ligero (barato sobre un sitio existente; en iOS gestiona expectativas) · **nativa** solo si necesitas hardware profundo o push fiable iOS a escala (rara vez se justifica para una tienda).

## 5. Imágenes responsive & art direction

`srcset/sizes` = misma imagen distinto tamaño. `<picture>` = **art direction** (recorte distinto por viewport + fallback de formato):
```html
<picture>
  <source media="(max-width:600px)" type="image/avif" srcset="hero-mobile-480.avif 480w, hero-mobile-800.avif 800w" sizes="100vw">
  <source media="(min-width:601px)" type="image/avif" srcset="hero-1200.avif 1200w, hero-2000.avif 2000w" sizes="100vw">
  <img src="hero-1200.jpg" width="2000" height="1000" alt="..." fetchpriority="high">
</picture>
```
Density (`1x/2x`) para tamaño fijo (logos/avatares).

## 6. Patrones cross-device

- **Nav responsive:** hamburguesa bien hecha (botón ≥48px, `aria-expanded`/`aria-controls`, teclado, Esc/click-fuera). Mejor en e-commerce móvil: **bottom-nav** (Inicio/Buscar/Carrito/Cuenta) al alcance del pulgar.
- **Tablas → cards en móvil** (patrón `data-label`): `td::before{content:attr(data-label);font-weight:600}` con `<td data-label="Precio">`. Alt: scroll horizontal + 1ª columna `position:sticky;left:0`.
- **Data viz:** SVG fluido `viewBox`; en móvil reduce series, barras horizontales, tap no hover.

## Blacklist móvil/responsive
`height:100vh` en full-screen (usa `svh`/`dvh`) · `loading="lazy"` en el LCP · inputs `<16px` (zoom iOS) · targets `<44px` o pegados · info crítica solo en `:hover` · `<img>` sin width/height/aspect-ratio · breakpoints "de dispositivo" · `user-scalable=no`/`maximum-scale=1` (prohibido, viola a11y) · carrusel autoplay sin snap/swipe · JS pesado bloqueante en ruta crítica · CTA pegado al borde sin `env(safe-area-inset-bottom)` · container query sin `container-type` en el ancestro (falla silencioso) · modal centrado en móvil en vez de bottom-sheet · apostar push PWA en iOS como canal principal · tipografía fija px sin clamp.
