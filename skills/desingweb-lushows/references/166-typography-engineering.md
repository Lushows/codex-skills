# 166 — Web typography engineering

**CRAFT, code-heavy.** El lado técnico/performance (distinto de pairing/03): carga de fuentes, CLS, ejes variables, subsetting, OpenType. Pareja de 03 (tipografía/pairings), 145 (kinetic type), 40 (performance), 19 (responsive). Regla de oro: **lo que separa "puesto por defecto" de *maquetado* no es elegir buenas fuentes, sino cómo se cargan, entregan, ajustan y afinan — bytes, CLS, ejes, OpenType.**

## 1. Font loading & performance

El conflicto: **FOIT** (texto invisible mientras carga) vs **FOUT** (se ve la fallback y "salta"). `font-display` lo controla:
```css
@font-face{ font-family:"Inter"; src:url("/fonts/inter-var.woff2") format("woff2-variations");
  font-weight:100 900;          /* rango: una sola fuente variable */
  font-display:swap; }          /* fallback ya, swap al cargar (FOUT) */
```
`swap` (cero invisible, pero swap visible → **siempre con metric overrides**, §2) · `optional` (si no está en ~100ms usa fallback y NO swap esa visita — cero CLS, ideal body) · `fallback` (bloqueo ~100ms + swap 3s, buen medio para headings). **Preload solo la(s) crítica(s)** above-the-fold (preloadear de más compite con el LCP): `<link rel="preload" href="/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>`. **Self-host > Google Fonts en 2026** (tras Schrems II servir desde gstatic se considera transferencia de IP a terceros — multas en UE; + elimina un DNS/TLS y permite subsetear; sirve same-origin con `Cache-Control: immutable`). Esperar fuentes sin bloquear: `document.fonts.ready.then(()=>document.documentElement.classList.add("fonts-loaded"))`.

## 2. size-adjust / ascent-override — matar el CLS del swap

El salto ocurre porque la fallback ocupa distinto alto/ancho. Define una `@font-face` "fantasma" sobre una fuente local que **calca las métricas**:
```css
@font-face{ font-family:"Inter-fallback"; src:local("Arial");
  size-adjust:107.4%; ascent-override:90%; descent-override:22.4%; line-gap-override:0%; }
:root{ font-family:"Inter","Inter-fallback",sans-serif; }
```
Los valores los calcula **Fontaine** (Nuxt/Vite) o `capsize`. Con esto `font-display:swap` reflowea **cero píxeles**: CLS = 0.

## 3. Variable fonts

Una variable reemplaza 9 estáticas (Inter variable ≈90KB vs ~360KB en 4 pesos). Ejes: `wght/wdth/slnt/opsz/ital` + custom. Prefiere las propiedades altas: `h1{ font-weight:720; font-optical-sizing:auto; }`. **Animar ejes con `@property`** (sin él `font-variation-settings` no transiciona): `@property --wght{ syntax:"<number>"; inherits:false; initial-value:400 } .link{ font-variation-settings:"wght" var(--wght); transition:--wght .3s } .link:hover{ --wght:750 }`. **Optical sizing** (`font-optical-sizing:auto` liga `opsz` al `font-size` — de los detalles que más "leen como maquetado").

## 4. Subsetting & delivery — el byte budget

Una fuente trae miles de glyphs que no usas → **subsetea** a lo que aparece:
```bash
glyphhanger https://midominio.com --subset=*.ttf --formats=woff2 --LATIN --whitelist="’“”—…"
pyftsubset inter-var.ttf --unicodes="U+0000-00FF,U+2018-2022" --flavor=woff2 --layout-features="*"
```
WOFF2 es el único formato necesario en 2026. **`unicode-range`** para carga partida (el navegador solo baja el Cirílico si la página tiene esos code points). **Byte budget:** variable de body subseteada ≤35KB, heading ≤25KB, total fuentes <100KB.

## 5. Fluid type & spacing — clamp() + Utopia

`clamp(min, fluido, max)` con `vw` + `rem` (no solo `vw`, que rompe el zoom de a11y):
```css
:root{ --step-0:clamp(1rem, 0.83rem + 0.87vw, 1.25rem); --step-2:clamp(1.56rem, 1.1rem + 2.3vw, 2.81rem); }
```
**Utopia** (utopia.fyi) genera escalas fluidas de tipo *y* espacio que comparten curva. En contenedores usa **`cqi`** (1% del inline-size del contenedor) en vez de `vw`. Reglas: `font-size` en **rem**, `line-height` **unitless** (`1.5`), measure 60-75ch (`max-width:66ch`). Remate: `h1,h2{ text-wrap:balance }` · `p{ text-wrap:pretty }` (evita viudas/huérfanas; Safari 26+/Chrome 117+).

## 6. OpenType features & fina tipografía

Usa `font-variant-*` (semántico) y reserva `font-feature-settings` para sets sin propiedad:
```css
body{ font-variant-ligatures:common-ligatures contextual; font-kerning:normal; }
table{ font-variant-numeric:tabular-nums; }        /* números alineados en columnas */
p{ font-variant-numeric:oldstyle-nums proportional-nums; }
.brand{ font-feature-settings:"ss01" 1, "cv05" 1; } /* stylistic/character variants */
.prose{ hanging-punctuation:first last; hyphens:auto; } /* requiere lang="es" en <html> */
```
`hanging-punctuation` y `text-spacing-trim` aún Safari/Chrome-only — mejora progresiva. `&shy;` para cortes manuales. **Variables free premium 2026:** Inter, Geist, Fraunces (`opsz`/`SOFT`/`WONK`), Bricolage Grotesque, Clash, Satoshi, General Sans, Recursive (5 ejes), Instrument, Newsreader.

## Typography-engineering anti-patterns — blacklist
**`<link>` a Google Fonts en producción UE** (privacidad + render-blocking + DNS extra) · **`font-display:swap` SIN metric overrides** (CLS visible en cada carga) · **preloadear 6 archivos de fuente** (compiten con el LCP; solo la crítica) · **servir 9 WOFF2 estáticos** cuando una variable pesa menos · **fuente sin subsetear** (cargar todo Cirílico/Griego para un sitio en español) · **`font-size` en `px`** (rompe zoom; `line-height:1.5em` no escala) · **`font-size:4vw` puro** sin `clamp()`/`rem` (falla WCAG 1.4.4) · **animar `font-variation-settings` sin `@property`** (salta) · **medidas >80ch** o `line-height:1` en body · **servir TTF/WOFF en 2026**; ignorar `font-optical-sizing:auto` teniendo `opsz` · **olvidar `crossorigin`** en el preload (descarga duplicada) · **`text-align:justify` sin `hyphens:auto`** (ríos de blanco).
