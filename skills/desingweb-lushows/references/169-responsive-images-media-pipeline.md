# 169 — Responsive images & media pipeline

**CRAFT, code-heavy.** El craft completo de imágenes (la imagen es casi siempre el byte más pesado y el LCP más común). Pareja de 27 (video/media), 40 (performance), 19 (responsive/mobile), 14 (AI imagery). Regla de oro: **nunca lazy-load por encima del fold ni el LCP; AVIF→WebP→JPG; siempre `width`/`height`/`aspect-ratio` (mata CLS); una sola imagen con `fetchpriority="high"`.**

## 1. srcset / sizes / picture — los cimientos

**`srcset` width descriptors (`w`) + `sizes`** (el navegador elige por viewport Y DPR; `sizes` describe el ancho **renderizado** en CSS, no el del archivo):
```html
<img src="/foto-800.jpg"
  srcset="/foto-400.jpg 400w, /foto-800.jpg 800w, /foto-1200.jpg 1200w, /foto-1800.jpg 1800w"
  sizes="(max-width:600px) 100vw, (max-width:1100px) 50vw, 33vw"
  width="1200" height="800" alt="..." decoding="async">
```
**Gotchas:** sin `sizes` el navegador asume `100vw` (descarga de más); `sizes` no entiende variables CSS bien (declara breakpoints reales); en 2026 `sizes="auto"` + `loading="lazy"` deja que el navegador calcule el ancho real una vez maquetado. **`<picture>` para art-direction** (recortes distintos por dispositivo, no solo tamaño) Y format fallback: `<source media="(max-width:700px)" srcset="hero-portrait.avif" type="image/avif">`. **Density (`x`)** para imágenes de tamaño **fijo** (logos/avatares): `srcset="logo.png 1x, logo@2x.png 2x"`.

## 2. Formatos modernos y la cascada

**AVIF** (~95% soporte, default para fotos, ~50% vs JPEG) → **WebP** (97%+, fallback) → **JPEG** (red de seguridad). **JPEG XL** aún no en producción vía `<picture>` (soporte parcial 2026). La cascada `<picture><source type>` (primer `type` que entiende, mejor a peor):
```html
<picture>
  <source type="image/avif" srcset="foto-800.avif 800w, foto-1600.avif 1600w" sizes="100vw">
  <source type="image/webp" srcset="foto-800.webp 800w, foto-1600.webp 1600w" sizes="100vw">
  <img src="foto-1600.jpg" srcset="foto-800.jpg 800w, foto-1600.jpg 1600w" sizes="100vw"
       width="1600" height="1066" alt="..." loading="lazy" decoding="async">
</picture>
```
**Encoding (sweet spots):** AVIF quality 50-65 (`sharp --avif quality=58 effort=6`), WebP 75-85, JPEG 80 MozJPEG progresivo. **Encoda en build/CDN, nunca en runtime del cliente** (5-10× más lento que JPEG).

## 3. Estrategia de carga & CWV

**Regla absoluta: nunca lazy-load el LCP/hero** (quitar `loading="lazy"` + añadir `fetchpriority="high"` mejora el LCP **200-800ms**):
```html
<img src="hero-1600.avif" fetchpriority="high" decoding="async" width="1600" height="900" alt="..."> <!-- LCP -->
<img src="thumb.avif" loading="lazy" decoding="async" fetchpriority="low" width="400" height="300" alt="..."> <!-- below-fold -->
```
**`preload` vs `fetchpriority`:** `preload` resuelve *descubrimiento tardío* (URL enterrada en CSS/`<picture>`), `fetchpriority` resuelve *prioridad baja* — para el LCP úsalos juntos. Para `<picture>` responsivo: `<link rel="preload" as="image" imagesrcset="hero-800.avif 800w, hero-1600.avif 1600w" imagesizes="100vw" fetchpriority="high" type="image/avif">`. **Matar CLS:** siempre `width`/`height` (deriva `aspect-ratio`) o `.media{ aspect-ratio:16/9; width:100%; height:auto }`. **Una sola** imagen con `fetchpriority="high"` (varias compiten).

## 4. Placeholders — el reveal premium

**ThumbHash > BlurHash** (mejor color al mismo tamaño, codifica aspect-ratio, **soporta alpha**; BlurHash renderiza transparencia en negro) — ambos <1% del original pero **requieren JS** para decodificar. **Blur-up transition** (el patrón estándar): placeholder borroso de fondo + imagen real encima que aparece en `load`:
```html
<div class="blur-up" style="background-image:url(data:image/png;base64,...)">
  <img src="foto.avif" loading="lazy" decoding="async" width="1600" height="1066" alt="..."
       onload="this.parentElement.classList.add('loaded')"></div>
```
```css
.blur-up{ background-size:cover; overflow:hidden } .blur-up img{ opacity:0; transition:opacity .5s } .blur-up.loaded img{ opacity:1 }
```
**LQIP base64** (sin JS: JPEG ~20×13px inline + `filter:blur()`) · **dominant-color** (el más barato, `background-color` del color promedio) · **skeleton** (grids donde aún no conoces la imagen).

## 5. Art direction & treatment

**`object-fit`/`object-position`** controlan el recorte + focal point: `.card-img{ object-fit:cover; object-position:50% 30% }`. **Dark-mode image swap** sin JS: `<source srcset="diagrama-dark.avif" media="(prefers-color-scheme: dark)">`. **Treatment CSS** (duotone/grayscale): `.thumb{ filter:grayscale(1) contrast(1.05); transition:filter .4s } .thumb:hover{ filter:grayscale(0) }` (duotone real con `feColorMatrix` o `mix-blend-mode` sobre overlay de color).

## 6. CDN & automatización

Los **image CDN** eliminan exports manuales (transforman on-the-fly + cachean en edge): el patrón `?w=&format=auto&q=auto`:
```
Cloudinary: /upload/f_auto,q_auto,w_800,c_fill,g_auto/foto.jpg
Imgix:      /foto.jpg?w=800&auto=format,compress&q=75&fit=crop
Cloudflare: /cdn-cgi/image/width=800,format=auto,quality=82/foto.jpg
```
`f_auto`/`auto=format` sirve AVIF→WebP→JPEG según el `Accept` header. **Generar `srcset` desde un CDN** sin exportar: `[400,800,1200,1800].map(w=>\`${cdn(w)} ${w}w\`).join(', ')`. **Frameworks:** Next `<Image>` (`priority` para LCP, `placeholder="blur"`), Astro `<Image>`/`<Picture formats={['avif','webp']}>` (cuidado: no dobles-optimices CDN + framework). **Perf budget:** hero AVIF ≤150KB, contenido ≤80KB, total imágenes ≤1MB, LCP <2.5s.

## Image anti-patterns — blacklist
**lazy-loadear el LCP/hero** (retrasa el LCP 200-800ms; eager + `fetchpriority="high"`) · **`fetchpriority="high"` en más de una imagen** (todas compiten, anula el efecto) · **servir un solo tamaño** a todos los viewports · **omitir `width`/`height`/`aspect-ratio`** (CLS) · **`sizes` que no coincide con el ancho CSS real** · **PNG para fotografías** (AVIF/WebP; PNG solo gráficos/transparencia) · **inline base64 de imágenes grandes** (infla el documento, bloquea el parse) · **encodear AVIF en runtime/cliente** (hazlo en build/CDN) · **`background-image` CSS para imágenes de contenido importantes** (descubrimiento tardío; usa `<img>` o preload) · **confiar en JPEG XL en `<picture>`** para producción 2026 · **doble optimización** (CDN + framework re-procesando) · **placeholders ThumbHash sin fallback** para JS deshabilitado.
