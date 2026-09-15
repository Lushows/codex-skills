# 151 — Parallax, depth & 3D-on-scroll

**CRAFT, code-heavy.** Léelo para parallax de scroll/mouse, perspectiva 3D, velocity skew, secciones pinneadas. Pareja de 07 (motion/ScrollTrigger), 26 (scrollytelling), 09 (scroll-driven CSS), 40 (performance). Regla de oro: **la profundidad premium es percibida, no anunciada — desplazamientos de 8-40px máximo; si el usuario nota "ah, parallax", es demasiado.**

## 1. Por qué la profundidad se siente premium (cuando está bien)

El cerebro lee **velocidad diferencial = distancia**: cuando el fondo se mueve más lento que el primer plano, infiere un eje Z que no existe → la página deja de ser papel y se vuelve espacio. El cliché (2012, montañas a 0.5x, jank a 30fps) murió por ruidoso y costoso. La artesanía 2026 es lo opuesto: **sutileza extrema** (8-40px máx entre capas, easing lineal atado al scroll, degradado de intensidad: más cercano = más rápido, fondo casi quieto).

## 2. Scroll parallax — GSAP scrub Y CSS scroll-driven nativo

**Receta A — GSAP ScrollTrigger (control total, compat universal):**
```js
gsap.utils.toArray("[data-speed]").forEach((layer)=>{
  const speed = parseFloat(layer.dataset.speed); // 0.85 fondo, 1.15 frente
  gsap.to(layer, { yPercent:(1-speed)*100, ease:"none",
    scrollTrigger:{ trigger:layer.closest("[data-parallax-scene]"), start:"top bottom", end:"bottom top", scrub:1, invalidateOnRefresh:true } });
});
```
**Receta B — CSS scroll-driven nativo** (`scroll()`/`view()`, soporte 2026: Chrome/Edge 115+, Safari 18+; corre en el **compositor thread** → 0 jank):
```css
@keyframes drift{ to{ transform:translateY(-12%); } }
.layer--bg{ animation:drift linear both; animation-timeline:scroll(root block); }
.card{ animation:drift linear both; animation-timeline:view(); animation-range:entry 0% cover 50%; }
@supports (animation-timeline: scroll()){ /* aplica aquí para no degradar en viejos */ }
```
**`prefers-reduced-motion` obligatorio** (`.layer--bg,.card{ animation:none!important; transform:none!important; }`). **Cuándo cuál:** CSS nativo para efectos simples y de alto volumen (gratis en performance); GSAP cuando necesitas pinning, timelines, `containerAnimation` o velocity.

## 3. Mouse parallax — capas que siguen el cursor, lerped

Capas con `data-depth`, mueves cada una una fracción del delta del cursor, y **suavizas con lerp** en un loop de RAF (nunca directo en `mousemove`):
```js
const lerp=(a,b,n)=>a+(b-a)*n;
addEventListener("mousemove",e=>{ mouseX=(e.clientX/innerWidth-.5)*2; mouseY=(e.clientY/innerHeight-.5)*2; });
function raf(){ layers.forEach((el,i)=>{ const depth=parseFloat(el.dataset.depth); // 0.02 fondo, 0.12 frente
  state[i].x=lerp(state[i].x, mouseX*depth*100, 0.08); state[i].y=lerp(state[i].y, mouseY*depth*100, 0.08);
  el.style.transform=`translate3d(${state[i].x}px,${state[i].y}px,0)`; }); requestAnimationFrame(raf); } raf();
```
`translate3d` fuerza GPU. El `0.08` es el alma (snappy = barato, demasiado lento = lag). **Giroscopio en móvil — opinión honesta: evítalo** (`DeviceOrientationEvent` requiere `requestPermission()` en iOS 13+, está roto/inconsistente, drena batería, marea). Desactiva mouse parallax en touch (`if(matchMedia('(hover:hover)').matches)`); en móvil manda el scroll parallax.

## 4. Perspectiva & 3D-on-scroll

`perspective` en el **contenedor padre** (no el hijo), rotas/empujas el hijo en Z según scroll. **CSS nativo — la tarjeta que se desaplana al entrar:**
```css
.scene{ perspective:1200px; }
@keyframes unflatten{ from{ transform:rotateX(28deg) translateZ(-180px); opacity:.4; } to{ transform:rotateX(0) translateZ(0); opacity:1; } }
.scene .card{ transform-style:preserve-3d; animation:unflatten linear both; animation-timeline:view(); animation-range:entry 10% cover 45%; }
```
**GSAP — push "into the screen":** `gsap.to(".hero-image",{rotateX:0, z:0, scale:1, ease:"none", scrollTrigger:{...scrub:true}, startAt:{rotateX:20, z:-300, scale:.9, transformPerspective:1000}})`. Sin perspectiva, `rotateX/Y` se ve plano y muerto.

## 5. Efectos basados en velocidad — el skew/stretch firma de Lenis/Locomotive

Al scrollear rápido los elementos se inclinan/estiran un grado, y al frenar **regresan elásticamente**:
```js
ScrollTrigger.create({ onUpdate:(self)=>{
  const skew = gsap.utils.clamp(-12, 12, self.getVelocity()/-300);
  gsap.to(".velo-item", {skewY:skew, duration:.8, ease:"power3", overwrite:true}); }});
gsap.set(".velo-item",{transformOrigin:"center center", force3D:true});
```
**Con Lenis** (smooth scroll de facto): `lenis.on("scroll",({velocity})=>{ gsap.to(".velo-item",{skewY:gsap.utils.clamp(-10,10,velocity*0.4), duration:.3, overwrite:true}); })`. Mantén el clamp bajo (≤12deg); sutil = momentum premium, exagerado = mareo y kitsch.

## 6. Pinned/sticky depth — secciones fijadas con parallax interno

Fijas una sección, scrolleas "a través", dentro las capas se mueven a distintas velocidades. También galerías horizontales con `containerAnimation`:
```js
const track = gsap.to(".h-track",{ x:()=>-(track.scrollWidth-innerWidth), ease:"none",
  scrollTrigger:{ trigger:".h-gallery", pin:true, scrub:1, end:()=>"+="+(document.querySelector(".h-track").scrollWidth-innerWidth), invalidateOnRefresh:true } });
gsap.utils.toArray(".h-track .panel-img").forEach(img=>{ gsap.fromTo(img,{xPercent:-15},{xPercent:15, ease:"none",
  scrollTrigger:{ trigger:img, containerAnimation:track, start:"left right", end:"right left", scrub:true }}); });
```
**Performance — innegociable:** anima **solo `transform`/`opacity`** (nunca `top/left/width/margin`); `will-change:transform` con moderación (ponlo al entrar, **quítalo al salir**); `translate3d`/`force3D:true` para GPU; combina con Lenis para que el scroll nativo no pelee con el scrub; en móvil reduce capas y mata mouse parallax; `ScrollTrigger.refresh()` tras cargar fonts/imágenes.

## Parallax/depth anti-patterns — blacklist
**animar `top`/`left`/`margin`/`background-position` en JS por scroll** (reflow cada frame, jank; solo `transform`/`opacity`) · **parallax exagerado** (>40px, fondos a 0.5x — cliché 2012, marea) · **`mousemove` sin RAF/lerp** (cientos de writes de layout/s, stutter) · **ignorar `prefers-reduced-motion`** (náusea/vértigo real) · **giroscopio sin permiso ni fallback** (roto en iOS, drena batería) · **`will-change:transform` global/permanente** (explota memoria GPU) · **pinning sin `invalidateOnRefresh`** (posiciones rotas al redimensionar/rotar) · **capas pesadas (imágenes full-res sin optimizar) en parallax** (repaint costoso) · **parallax que desplaza texto crítico** (ilegible en movimiento; mueve decoración, no copy) · **mouse parallax activo en touch** (sin cursor no hace nada; gate con `(hover:hover)`) · **mezclar scroll nativo con scrub agresivo sin smooth scroll** ("doble scroll"; usa Lenis) · **profundidad anunciada en vez de percibida**.
