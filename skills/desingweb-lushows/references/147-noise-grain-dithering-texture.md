# 147 — Noise, grain, dithering & analog texture

**CRAFT, code-heavy.** Léelo para grano de película, ruido SVG anti-banding, dithering, halftone, ASCII. Pareja de 41 (generative art), 02 (color/gradientes), 81 (CSS art), 06 (anti-slop). Regla de oro: **textura como atmósfera de fondo, nunca sobre el contenido legible; empieza en `opacity:0.04`, súbela hasta verla, baja un punto.**

## 1. Por qué la textura es el antídoto 2026 a lo plano y estéril

Tras años de flat/glassmorphism limpio y gradientes vectoriales perfectos, la web "premium" huele a renderizado por máquina (superficies sin poros, transiciones matemáticamente perfectas) → el ojo lo lee como *sintético*. El grain/noise/dither es la **capa orgánica anti-AI-slop** (reintroduce el grano de película, el error de imprenta, el banding analógico que asociamos con cosas hechas por personas). Tres trabajos: **calidez/profundidad** (grano a 0.04 sobre fondo plano lo convierte de "PDF" a "papel"), **esconde banding** (§6), **alma analógica/textura de marca** (editorial, música, moda, portfolios, wellness). **Eleva** en marcas con voz; **estorba** en dashboards densos, fintech clínico, UI con texto pequeño.

## 2. SVG noise — el más barato y escalable (`feTurbulence`)

Un `feTurbulence` (fractal noise) reducido a alfa con `feColorMatrix`, como data-URI en una capa fija fullscreen (~1KB, escala infinito, no requiere imagen):
```css
.grain-overlay{
  position:fixed; inset:0; z-index:9999; pointer-events:none; /* nunca bloquear clicks */
  opacity:.05;                  /* 0.03–0.08 es el rango de buen gusto */
  mix-blend-mode:overlay;       /* overlay o soft-light */
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='matrix' values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.5 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
```
**Parámetros:** `baseFrequency` = tamaño del grano (`0.6–0.9` fino tipo film; `0.2` nubes grandes), `numOctaves` = detalle (3-4 máx), `stitchTiles='stitch'` evita costuras al tilear, la última fila del `feColorMatrix` (`...0.5 0`) = intensidad del alpha. **Blend:** `overlay` contraste medio, `soft-light` más sutil/seguro sobre color (Chrome y Safari difieren — testear). **Static vs animado:** el SVG estático es GPU-compositado casi sin coste; **animar `feTurbulence` seed cada frame fuerza re-render del filtro en CPU = carísimo** → para grano animado NO animes el SVG (§3).

## 3. Film grain & grano animado

El truco performante NO es reanimar `feTurbulence`, sino **desplazar la posición** de una textura con `steps()`:
```css
@keyframes grain-shift{ 10%{transform:translate(-5%,-5%)} 50%{transform:translate(-4%,6%)} 90%{transform:translate(8%,2%)} }
.grain-overlay--animated{
  width:200%; height:200%; top:-50%; left:-50%; /* 2x viewport para que el translate no muestre bordes */
  animation:grain-shift .6s steps(6) infinite;   /* steps() = jitter discreto del celuloide */
}
@media (prefers-reduced-motion:reduce){ .grain-overlay--animated{ animation:none; } }
```
Solo animamos `transform` (GPU, barato). **Perf:** anima grano solo en heroes/above-the-fold, pausa con `IntersectionObserver`, respeta `prefers-reduced-motion` (el grano animado fullscreen a 60fps sobre scroll pesado mata móviles de gama baja).

## 4. Dithering (look retro / 1-bit Obra Dinn)

El **ordered (Bayer) dithering** usa una matriz de umbral muestreada por coordenadas de pantalla — barato y estable, el estándar 2026 en shaders:
```glsl
const mat4 bayer = mat4(0.,8.,2.,10., 12.,4.,14.,6., 3.,11.,1.,9., 15.,7.,13.,5.)/16.;
void main(){
  float lum = dot(texture2D(uTex,vUv).rgb, vec3(0.299,0.587,0.114));
  int x = int(mod(gl_FragCoord.x,4.)), y = int(mod(gl_FragCoord.y,4.));
  float bw = lum < bayer[x][y] ? 0.0 : 1.0;  // 1-bit
  vec3 dark=vec3(.06,.05,.10), light=vec3(.90,.95,.85); // duotone de marca
  gl_FragColor = vec4(mix(dark, light, bw), 1.0);
}
```
El **duotone + dither** (sustituir blanco/negro por dos colores de marca) es la estética editorial fuerte 2026. Muestrea siempre en `gl_FragCoord` (espacio pantalla), no en UV escalado (o el patrón "respira" con el zoom). Sin WebGL: canvas 2D con la misma matriz (ok para imágenes estáticas).

## 5. Halftone & ASCII

**Halftone (puntos de imprenta) en CSS puro** — `radial-gradient` tileado + `filter:contrast()` que colapsa bordes suaves en puntos duros:
```css
.halftone{ background:radial-gradient(circle at center,#000 0%,transparent 60%), var(--img);
  background-size:6px 6px; filter:contrast(40) grayscale(1); }
```
**ASCII art (canvas char mapping):** leer luminancia por celda y mapear a un char de densidad creciente (`const RAMP=" .:-=+*#%@"`). **Clave que casi todos fallan:** los caracteres **no son píxeles cuadrados** → ajusta `line-height` (~0.8-1.0) y la relación cols/rows según el aspect del glifo monospace, o la imagen sale estirada.

## 6. Grano sobre gradientes (matar el banding) — la "expensive gradient"

El banding aparece en gradientes largos sutiles porque 8 bits no tienen pasos intermedios → superpón ruido SVG como dither:
```css
.expensive-gradient{ position:relative; background:linear-gradient(160deg,#1a1430,#2d1b4e 40%,#0e1a2b); }
.expensive-gradient::after{ content:''; position:absolute; inset:0; pointer-events:none;
  opacity:.06; mix-blend-mode:soft-light;
  background-image:url("data:image/svg+xml,...feTurbulence baseFrequency='0.9'..."); }
```
El ruido rompe los bordes de banda píxel a píxel = dither automático. Técnica avanzada: usar el ruido como `feDisplacementMap` sobre el gradiente para que los píxeles se desplacen y la banda *se disuelva*. Para mesh gradients (Stripe-style) el ruido es prácticamente obligatorio.

## Texture/grain anti-patterns — blacklist
**grain a `opacity > 0.12`** (look sucio/barato; si lo notas conscientemente, es demasiado) · **animar `feTurbulence seed` cada frame** (re-render de filtro en CPU, jank brutal — anima `transform`) · **grano fullscreen animado a 60fps sin `IntersectionObserver`/`prefers-reduced-motion`** · **olvidar `pointer-events:none`** en la capa overlay (roba todos los clicks) · **grain sobre texto de body/UI densa** (reduce legibilidad; textura va en fondos) · **PNG de ruido pesado (500KB+)** cuando un SVG de 1KB hace lo mismo escalable y nítido en retina · **olvidar `stitchTiles='stitch'`** (costuras visibles al tilear) · **dither muestreado en UV escalado** en vez de `gl_FragCoord` (el patrón escala con el zoom) · **ASCII con `line-height` por defecto** (imagen estirada; los glifos no son cuadrados) · **mismo blend mode en todo** sin testear Chrome vs Safari · **halftone con `contrast()` bajo** (puntos borrosos en vez de trama nítida).
