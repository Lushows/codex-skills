# 23 — Iconografía, ilustración & craft SVG

Playbook 2026 para iconos, ilustración y técnica SVG que hacen un sitio premium y cohesivo. **Léelo cuando elijas iconos, animes SVG, hagas un logo responsive o agregues decoración gráfica.** Pareja de 02/03 y 15.

## 1. Sistemas de iconos: cuál y por qué

**Regla de oro: UNA sola familia por proyecto.** Mezclar familias es el tell #1 amateur (cada set tiene su grid, stroke óptico y radio → "no riman").

| Library | Personalidad | Coverage | Peso | Licencia | Cuándo |
|---|---|---|---|---|---|
| **Lucide** | Limpio, neutral, default seguro (fork de Feather, grid 24px, stroke 2px) | ~1.500+ | Stroke ajustable | ISC | Default del 80% (SaaS/marketing), tree-shaking excelente |
| **Phosphor** | Geométrico, cálido, versátil | ~7.700+ | thin/light/regular/bold/fill/**duotone** | MIT | Variar peso/relleno por estado; look más cálido |
| **Heroicons** | Pulido, Tailwind-native | ~292 | Outline 24 + Solid 20 + Mini 16 | MIT | Proyectos Tailwind, set curado pequeño |
| **Tabler** | Técnico, denso, dashboard-y | ~5.600+ | Stroke 2px / grid 24px | MIT | Dashboards/admin con mucha densidad |
| **Radix Icons** | Minimalista, grid 15px | ~300 | Stroke fino uniforme | MIT | Look "Vercel/Linear" ultra sobrio |
| **Material Symbols** | Google, variable font real | ~3.000+ | Ejes `wght/FILL/GRAD/opsz` | Apache 2.0 | Apps Material; único con optical sizing real |

**Decisión rápida:** Lucide (neutral) → Phosphor (cálido/multi-peso) → Tabler (densidad) → Radix (minimalismo).
**Cohesión:** un `stroke-width` para todo el sitio (2px típico, nunca mezcles 1.5 y 2.5); mantén el uso cerca del grid nativo (24px), no escales 24→64 sin engrosar; stroke = base, filled/solid solo para estado activo (tab seleccionado, favorito).
**Implementación (inline SVG + `currentColor`):**
```html
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"
     stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
  <path d="M5 12h14M12 5l7 7-7 7"/>
</svg>
```
`currentColor` → tematización gratis (dark mode, hover). No uses `fill` hardcoded.
**Inline vs sprite vs font:** inline SVG = default (currentColor, animación, a11y por icono); **`<use href>` sprite** cuando repites el mismo icono decenas de veces en HTML estático; **icon-font (FontAwesome legacy) = evitar en 2026** (FOUT, no multicolor, a11y rota).
```html
<svg style="display:none" aria-hidden="true"><symbol id="i-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></symbol></svg>
<svg class="icon" aria-hidden="true"><use href="#i-arrow"/></svg>
```

## 2. Craft SVG: técnica

- **viewBox:** define coordenadas internas; `width/height` el tamaño en pantalla. Para SVG responsive omite `width/height` y deja el contenedor mandar (`svg{width:100%;height:auto}`).
- **A11y (3 casos):** decorativo → `aria-hidden="true" focusable="false"`; botón solo-icono → `<button aria-label="Cerrar">`; imagen informativa → `<svg role="img"><title id="t">…</title>`.
- **Optimización SVGO:** `npx svgo --multipass icon.svg`. Preserva `viewBox` (`removeViewBox:false`); no fusiones paths que vayas a animar.
- **Gradients/masks/clipPath:** `<defs>` con `<linearGradient>`/`<clipPath>`. **Cuidado con IDs duplicados** si inyectas varios SVG (prefija `g-hero`, `g-card`).
- **SVG vs PNG vs font:** SVG para todo lo vectorial (logos, iconos, ilustración plana); PNG/WebP solo para raster fotográfico. Nunca un logo en PNG si existe el SVG.

## 3. Animación SVG

**Line-draw (la técnica fundamental):**
```css
.draw path{ stroke-dasharray:1; stroke-dashoffset:1; animation:draw 1.5s ease forwards }
@keyframes draw{ to{ stroke-dashoffset:0 } }
```
```js
document.querySelectorAll('.draw path').forEach(p=>{ const len=p.getTotalLength(); p.style.strokeDasharray=len; p.style.strokeDashoffset=len; });
```
**Gotcha crítico de `transform-origin`:** en SVG el origen es `(0,0)` del viewBox, NO el centro. Para rotar/escalar desde el centro: `transform-box:fill-box; transform-origin:center` (la línea que casi todos olvidan).
**Rendimiento:** anima solo `transform`/`opacity` (+ `stroke-dashoffset` que es barato). Animar `d`/`fill`/`stroke-width` fuerza repaint → jank.
**SMIL vs CSS vs JS:** CSS para hovers/loops/line-draw (default); SMIL legacy (no para nuevos); **GSAP** para control total (`DrawSVGPlugin` line-draw robusto, **`MorphSVGPlugin`** morphing entre paths con distinto nº de puntos).
**Lottie vs SVG vs Rive:** SVG+CSS/GSAP = micro-interacciones/iconos/line-draw (liviano, editable); **Lottie** = ilustración animada rica (pesado, no interactivo); **Rive** = ganador 2026 para animación **interactiva/estado** (state machines hover→active→loading en un asset; más liviano que Lottie).
**Hamburguesa→close morph:** `transform-box:fill-box` + rotar `.top`/`.bottom` ±45° y `opacity:0` en `.middle` con `[aria-expanded="true"]`.

## 4. Ilustración: sistemas y tendencias 2026

Macro-tendencia: **calidez táctil y rebelión contra la perfección de IA** (grano, textura, imperfección, lo humano). La ilustración custom es diferenciador de marca de primer nivel.
**Estilos vigentes:** grainy/textured/noise (el más fuerte del año) · 3D render híbrido (Blender/Spline + vector plano) · isométrico (dashboards explicativos) · hand-drawn/orgánico · editorial/autoral (anti-stock) · maximalismo psicodélico (solo música/moda/cultura).
**Cohesión (4 ejes):** misma paleta (2-4 colores de marca + neutros), mismo grosor de línea, mismo style frame (¿outline? ¿grano? ¿sombras planas o degradados?), mismo tratamiento de personas/objetos.
**Sourcing:** unDraw (1 color configurable, el más "visto"), Open Peeps, Humaaans, Blush. **Customiza SIEMPRE a la marca** (color de acento, recolorea grano, recorta el style frame) — un unDraw sin tocar = slop reconocible.

## 5. Logo & mark en SVG

**Responsive (favicon→billboard):** vector único + variantes: completo (horizontal), isotipo/mark (cuadrado, para favicon/avatar), mono. `currentColor` en el mark → hereda tema dark/light. `<svg viewBox="0 0 120 32" fill="currentColor" role="img" aria-label="Marca"><use href="/sprite.svg#logo-full"/></svg>`.
**Reveal animado:** line-draw del mark + fade-in del wordmark con stagger; <1.5s y `@media (prefers-reduced-motion: reduce){ .draw path{ animation:none; stroke-dashoffset:0 } }`.
**Set de favicons moderno (mínimo correcto, 3-4 archivos, no 20):**
```html
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/icon.svg" type="image/svg+xml">     <!-- soporta @media dark internamente -->
<link rel="apple-touch-icon" href="/apple-touch-icon.png"> <!-- 180x180, SIN transparencia -->
<link rel="manifest" href="/site.webmanifest">
```
Maskable (`purpose:"maskable"`): arte crítico dentro del 80% central (safe zone ~409×409 sobre 512). Apple-touch-icon **sin transparencia** (Safari rellena con negro).

## 6. SVG decorativo

**Grano/noise (sin PNG):**
```html
<svg style="position:fixed;inset:0;width:100%;height:100%;pointer-events:none;opacity:.06;mix-blend-mode:overlay">
  <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" stitchTiles="stitch"/></filter>
  <rect width="100%" height="100%" filter="url(#grain)"/>
</svg>
```
`baseFrequency` ↑ = grano más fino; `opacity` 0.04-0.08 = buen gusto.
**Blobs/waves/dividers:** genera con blobmaker/getwaves pero **edítalos** (no el default reconocible); wave divider con el color exacto de la sección siguiente + `preserveAspectRatio="none"`.
**Criterio:** lo decorativo va detrás (`z-index` bajo, `pointer-events:none`, `aria-hidden`); uno o dos elementos por vista, no diez.

## Anti-slop blacklist (iconos + ilustración)
mezclar familias de iconos (el error #1) · stroke-width inconsistente o escalar sin engrosar · mezclar outline/filled sin lógica · icon-fonts legacy en proyectos nuevos · `fill="#000"` hardcoded (roto en dark) · Corporate Memphis/"Alegria" (personas blob de patas largas) · unDraw/Humaaans sin recolorear · emojis como iconos de UI en productos serios · animar `fill`/`d`/`width` en loops (jank) u olvidar `transform-box:fill-box` · grano a opacidad 0.3 (grita "filtro") · apple-touch-icon transparente · logo en PNG cuando existe SVG · blob/wave de generador sin editar · ignorar `prefers-reduced-motion` en reveals.
