# 143 — WebGL image effects, hover distortion & shader transitions

**CRAFT, code-heavy.** Léelo para distorsión de imagen en hover, RGB split, transiciones de slider con shader, scroll-velocity distortion. Pareja de 08/38 (WebGL/shaders), 07 (motion), 39 (interacción). Regla de oro: **si CSS lo resuelve (filter/blend/mask/clip-path) usa CSS; salta a GL solo cuando necesitas muestrear la textura en UVs desplazados (displacement, RGB split direccional, melt). En reposo la imagen debe verse 100% nítida.**

## 1. Las familias de efecto (y qué comunican)

**Displacement/distortion on hover** (dos imágenes se funden empujando los UVs con un noise map — *materialidad, lujo táctil*; reina en portfolios y moda, el caballo de batalla). **RGB split/chromatic aberration** (se separan los canales R/G/B — *energía, glitch, velocidad*; mortal si es constante, brillante si reacciona a velocidad de scroll/cursor). **Ripple/wave** (onda sinusoidal desde el cursor/click — *agua, suavidad*; bueno en click). **Pixelation** (`floor(uv*blocks)/blocks` — *retro, reveal*; excelente como transición de entrada, no estado permanente). **Zoom/scale-on-scroll** (textura se escala dentro de un plano fijo `uv=(uv-0.5)*scale+0.5` — *profundidad, cine*; el más seguro y universal). **Liquid/melt transitions** (displacement alto + noise entre dos slides — *fluidez premium*). **Scroll-velocity distortion** (el plano se curva/estira según `Math.abs(velocity)` — *peso físico, inercia*; la técnica firma 2024-2026 Lenis+GL). **Gallery slide con GL transition** (el cambio de slide es un shader, no un CSS slide).

## 2. La tecnología

| Lib | Peso (gz) | Cuándo |
|---|---|---|
| **OGL** | ~29kb (core 8kb) | **Default 2026.** Un plano-imagen, hover, slider GL. API tipo Three pero minimal. |
| Three.js | ~150kb+ | Solo si ya hay escena 3D real. Overkill para imágenes. |
| curtains.js | ~30kb | Mapea `<img>`/`<video>` del DOM a planos auto. OGL lo desplaza. |
| raw WebGL | 0kb | Solo un fullscreen shader (1 quad). |

**El patrón DOM↔WebGL sync (la clave):** maquetas con HTML+CSS, ocultas el `<img>` (opacity 0) y dibujas un plano GL **encima**, sincronizado por `getBoundingClientRect()`:
```js
function syncPlane(mesh, el){
  const r = el.getBoundingClientRect();
  mesh.scale.set(r.width, r.height, 1);
  mesh.position.x = r.left - innerWidth/2 + r.width/2;
  mesh.position.y = -r.top + innerHeight/2 - r.height/2; // y invertido (DOM crece abajo, GL arriba)
}
```
Llama en `resize` y cada frame restando el **scroll interpolado de Lenis** (no `window.scrollY`, o GL y DOM se desincronizan durante el smooth-scroll).

## 3. Receta: displacement-map hover transition

Dos texturas + textura de displacement (noise/grunge PNG) + `uProgress`. La animación NO se hace en el shader; **GSAP hace tween al uniform**.
```glsl
precision highp float;
uniform sampler2D uTexture1, uTexture2, uDisp;
uniform float uProgress, uIntensity; // intensity ~0.3
varying vec2 vUv;
void main(){
  float d = texture2D(uDisp, vUv).r * uIntensity;
  vec2 uv1 = vec2(vUv.x + uProgress * d, vUv.y);
  vec2 uv2 = vec2(vUv.x - (1.0 - uProgress) * d, vUv.y);
  gl_FragColor = mix(texture2D(uTexture1, uv1), texture2D(uTexture2, uv2), uProgress);
}
```
```js
el.addEventListener('mouseenter', () => gsap.to(program.uniforms.uProgress, {value:1, duration:.9, ease:'power3.out'}));
el.addEventListener('mouseleave', () => gsap.to(program.uniforms.uProgress, {value:0, duration:.9, ease:'power3.out'}));
```
GSAP es la fuente de verdad del progreso; el ease lo es todo (`power3.out`, no `linear`).

## 4. Receta: RGB shift por velocidad de scroll

Captura la velocidad (Lenis te la da) → uniform suavizado con lerp que decae a 0 al parar:
```js
let target=0, current=0;
lenis.on('scroll', ({velocity}) => { target = Math.min(Math.abs(velocity)*0.0015, 0.05); });
function loop(){ current += (target-current)*0.1; target *= 0.92;
  program.uniforms.uShift.value = current; requestAnimationFrame(loop); }
```
```glsl
uniform sampler2D uTexture; uniform float uShift; varying vec2 vUv;
void main(){
  vec2 dir = vec2(0.0, 1.0);
  float r = texture2D(uTexture, vUv + dir*uShift*1.0).r;
  float g = texture2D(uTexture, vUv + dir*uShift*0.5).g;
  float b = texture2D(uTexture, vUv - dir*uShift*1.2).b;
  gl_FragColor = vec4(r,g,b,1.0);
}
```
La magia: distintos multiplicadores por canal (R 1.0×, G 0.5×, B 1.2×) → la aberración se ve *óptica*. En reposo `uShift→0` y la imagen es perfecta y nítida.

## 5. Performance & fallback (no negociable)

```js
renderer.dpr = Math.min(window.devicePixelRatio, 2);  // retina x3 mata fillrate
const io = new IntersectionObserver((es)=>es.forEach(e=>{ if(e.isIntersecting){ initGL(e.target); io.unobserve(e.target); }}), {rootMargin:'200px'}); // lazy-init
const gl = canvas.getContext('webgl2') || canvas.getContext('webgl');
if(!gl || matchMedia('(prefers-reduced-motion: reduce)').matches){ showPlainImages(); return; }
```
**El `<img>` real es el fallback** y la fuente del LCP (déjalo en el DOM con `loading="lazy"`, opacity 1; ocúltalo solo **después** de que GL pinte el primer frame — no penalizas LCP ni a11y). Texturas dimensionadas a pantalla (no 4K), WebP/AVIF para la fuente. **Pausa el RAF** fuera de viewport (`IntersectionObserver`) y en `visibilitychange`. Comparte **una sola textura de displacement** entre todos los planos.

## 6. Dirección de arte: élite vs slop

**Elevan en:** portfolios de fotógrafo/director, e-commerce de moda/lujo, galerías, estudios creativos (la imagen *es* el producto, el usuario llega a contemplar). **Son slop en:** SaaS, dashboards, sitios informativos, e-commerce de volumen (la gente escanea, no contempla). **Reglas:** sutileza (`uIntensity` 0.2-0.4, no 1.0), timing (entrada 0.6-1.0s `power3.out`, salida igual o un pelo más lenta), **reposo nítido** (toda distorsión permanente envejece mal), uno por vista (un lenguaje de efecto por página).

## Image-effect anti-patterns — blacklist
**distorsión permanente en reposo** (si nunca se ve nítida, es ruido) · **RGB split constante** (jaqueca y look de tutorial; debe responder a input) · **`linear` easing / duraciones <0.3s** · **no respetar `prefers-reduced-motion`** · **GL para lo que CSS resuelve** (30kb+WebGL para un zoom que `transform:scale` hace gratis) · **ocultar el `<img>` antes del primer frame GL** (flash de hueco + LCP destruido) · **DPR sin cap** (×3 en móvil = jank) · **texturas 4K sin redimensionar** · **animar el progreso dentro del shader con `uTime`** en vez de tween al uniform (pierdes ease/interrupción/enter-leave) · **no pausar el RAF fuera de viewport** · **Three.js completo para una sola imagen** (usa OGL/raw) · **sincronizar el plano con `window.scrollY` usando Lenis** (desfase visible; usa el scroll interpolado) · **sin fallback no-WebGL** (canvas en blanco en GPU bloqueada).
