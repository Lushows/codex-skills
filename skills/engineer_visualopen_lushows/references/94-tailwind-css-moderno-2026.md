# 94 — Tailwind & CSS moderno (2026)

## Tailwind CSS v4 (Oxide engine, Rust)
~5× builds completos, ~100× incrementales. Shift definitorio: **config CSS-first** — `tailwind.config.js` SE FUE,
reemplazado por la directiva **`@theme`** en CSS; todos los tokens expuestos como **CSS variables** en runtime.
```css
@import "tailwindcss";
@theme {
  --color-brand: oklch(0.62 0.21 145);    /* OKLCH default */
  --font-display: "Satoshi", sans-serif;
}
.hero { background: var(--color-brand); }
```
**La paleta default pasó de sRGB a OKLCH** (perceptualmente uniforme, gamut más amplio, lightness ramps sanos).
**Container queries en el core** (`@container`, `@sm:`/`@lg:` variantes — el plugin viejo es obsoleto). + `@starting-style` para animaciones de entrada + utilidades 3D transform.

## CSS moderno que deberías usar (broadly shipped 2026)
**`:has()`** (parent selector: `.card:has(img)`) · **nesting nativo** · **`@layer`** (cascade layers) · **container
queries** (`@container`) · **`text-wrap: balance`** (headings) / **`pretty`** (body) · **subgrid** · **scroll-driven
animations** (`animation-timeline: scroll()` — parallax sin JS) · **View Transitions API** (`document.startViewTransition`, ahora cross-document MPA) · **anchor positioning** (`anchor()` — tooltips sin JS, el más nuevo, chequea soporte).

## Utility vs CSS Modules vs CSS-in-JS
**Runtime CSS-in-JS está efectivamente muerto** para trabajo nuevo — incompatible con RSC (sin runtime en server),
añade bundle/runtime. **Consenso 2026:** Tailwind utilities para UI de producto, CSS Modules (o CSS plano con `@layer`) para primitivos de design system, y **zero-runtime CSS-in-JS** (build-time, vanilla-extract/Panda) si insistes en co-locar.

## Gotchas
1. La migración v4 es significativa: config a CSS, plugins/`config.js` v3 necesitan reescritura, PostCSS cambió (`@tailwindcss/postcss`/Vite plugin).
2. La paleta OKLCH default hace que tus hex de marca viejos se vean sutilmente distintos al lado — re-tunea.
3. Container queries built-in chocan con el plugin viejo — quita `@tailwindcss/container-queries`.
4. CSS vars-by-default es genial, pero referenciar tokens Tailwind en CSS crudo requiere saber los nombres generados (`--color-*`).
5. Runtime CSS-in-JS + RSC lanza en build/runtime — no metas styled-components a un Server Component de Next 16.
6. Anchor positioning y algunos scroll-driven aún necesitan fallbacks — feature-detect con `@supports`.

**Fuentes:** tailwindcss.com/blog/tailwindcss-v4 · dev.to (Oxide deep dive 2026) · blog.logrocket.com (Tailwind 2026) · stevekinney.com (OKLCH).
