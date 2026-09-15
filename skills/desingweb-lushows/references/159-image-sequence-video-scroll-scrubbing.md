# 159 — Image-sequence & video-on-scroll scrubbing (el efecto AirPods)

**CRAFT, code-heavy.** Léelo para el "scroll controla un video/animación frame-by-frame" (Apple product pages). Pareja de 26 (scrollytelling), 27 (video/media), 07 (ScrollTrigger), 40 (performance). Regla de oro: **Apple NO usa `<video>` — precarga N frames y los pinta en `<canvas>`; la image-sequence es más suave que el video scrubbing porque cada frame es independiente (sin decodificación inter-frame). Si un `transform` CSS o un Lottie de 200KB cuenta la historia, no metas 150 JPGs.**

## 1. La técnica y cuándo

El scroll deja de mover la página y **controla el tiempo de una animación cuadro por cuadro**: la sección se "pega" (pin) y al hacer scroll avanza el *frame*, no la página. Scrubbing = scroll bidireccional = rewind/forward determinista. **Gana:** hero de producto que rota/se desarma, storytelling con beats sincronizados, reveal cinematográfico de "una sola vez" arriba de la página (el usuario *siente* que controla el objeto). **Overkill:** contenido informativo, listados, cualquier cosa donde se quiera leer rápido (pinear bloquea el avance natural); además es caro en bytes (varios MB) y GPU/CPU.

## 2. Image-sequence sobre canvas (la forma Apple)

Apple precarga N frames (147 en AirPods Pro) y los pinta en `<canvas>` con `drawImage`:
```js
const ctx = canvas.getContext("2d", {alpha:false});
const frameCount = 147, images = [], seq = {frame:0};
function drawCover(img){ const cw=canvas.width, ch=canvas.height;
  const r=Math.max(cw/img.width, ch/img.height), w=img.width*r, h=img.height*r;
  ctx.drawImage(img, (cw-w)/2, (ch-h)/2, w, h); }   // object-fit: cover
function render(){ const img=images[seq.frame]; if(img&&img.complete) drawCover(img); }
for(let i=0;i<frameCount;i++){ const img=new Image(); img.src=`/seq/${String(i+1).padStart(4,"0")}.webp`; images.push(img); }
images[0].onload = render;
gsap.to(seq, { frame:frameCount-1, snap:"frame", ease:"none",
  scrollTrigger:{ trigger:"#hero", start:"top top", end:"+=4000", pin:true, scrub:0.5 }, onUpdate:render });
```
**Tradeoff frame-count vs peso:** 60-90 frames suele bastar para 4000px de scroll (~15 frames/pantalla); por debajo de ~24 se nota a saltos. `snap:"frame"` evita pedir medio frame. El `end` define cuántos píxeles mapean a toda la secuencia.

## 3. Precarga y estrategia de peso

El hero **no debe romper el LCP:** **formato** AVIF primero (~50% más liviano que JPG), WebP fallback. **Resolución por viewport** (@1x móvil, @2x solo DPR>1 + ancho>768; nunca 2560px en un teléfono). **Byte budget** <3-4 MB (147 frames × ~25KB AVIF ≈ 3.6MB; móvil 40-60 frames). **Progressive preload + loader** (frame 0 primero, resto en background con barra). **`decode()` async** (fuera del main thread):
```js
async function preload(urls, onProgress){ let done=0;
  await Promise.all(urls.map(async src=>{ const img=new Image(); img.src=src;
    try{ await img.decode(); }catch{} images.push(img); onProgress(++done/urls.length); })); }
```
**Alternativa sprite-sheet** (un archivo, sub-rect con `drawImage(sheet, sx,sy,fw,fh, 0,0,cw,ch)`): genial para 16-36 frames; para 147 la imagen excede el límite de textura GPU (~8192-16384px).

## 4. Video scrubbing (y por qué la secuencia suele ganar)

Con `<video>` controlas `video.currentTime` desde el scroll. **El problema:** los codecs (H.264/VP9) usan keyframes separados por inter-frames; al hacer seek arbitrario aterrizas en un inter-frame no decodificable solo → **stutter** (el encoder mete 1 keyframe cada ~72 frames). Mitigaciones: **re-encodear con keyframe interval = 1** (seek perfecto pero el archivo se dispara 5-10×), **threshold + smoothing** (no spamear seeks: `if(Math.abs(t-prev)>0.04){ video.currentTime=t }`), **`requestVideoFrameCallback`** (pintar a canvas cuando el frame realmente llegó). **Setup obligatorio:** `muted playsinline preload="auto"` (sin `muted playsinline`, iOS abre fullscreen). **Cuándo video:** animación muy larga (>10s) donde una secuencia sería prohibitiva + puedes re-encodear. En todo lo demás, **image-sequence en canvas es más suave** (lo que usa Apple).

## 5. Sincronizar con contenido

El `pin` mantiene la sección fija durante el scrub. Para overlays de texto que cambian por rango de frames, una timeline única:
```js
const tl = gsap.timeline({ scrollTrigger:{ trigger:"#hero", start:"top top", end:"+=4000", pin:true, scrub:0.5 }});
tl.to(seq, {frame:frameCount-1, snap:"frame", ease:"none", onUpdate:render}, 0)
  .fromTo(".caption-1", {autoAlpha:0}, {autoAlpha:1}, 0.0).to(".caption-1", {autoAlpha:0}, 0.25)
  .fromTo(".caption-2", {autoAlpha:0}, {autoAlpha:1}, 0.30);
```
Cada label (0-1) mapea a un % del scroll → el texto aparece sobre el rango de frames deseado.

## 6. Performance y accesibilidad

**Canvas sizing/DPR:** buffer real a `width*Math.min(devicePixelRatio,2)`, escala por CSS, recalcula en `resize` (debounce) o se ve borroso en retina. **No bloquees el LCP** (la secuencia no debe ser el LCP element; poster estático inmediato + frames después). **Decode off main thread** (`img.decode()`/`createImageBitmap()`; `OffscreenCanvas` en worker para secuencias pesadas). **Móvil:** menos frames, menor resolución, DPR capado a 2, fallback estático si `navigator.connection.saveData`. **`prefers-reduced-motion`:** muestra un poster/frame final, sin scrubbing. **Ética de ancho de banda:** 3-4MB antes de que el usuario sepa si quiere ese contenido es agresivo — carga bajo demanda (IntersectionObserver), respeta `saveData`, ofrece versión estática.

## Image-sequence anti-patterns — blacklist
**cargar los N frames con `<img>` sin `decode()`** (jank en el primer scrub) · **olvidar `snap:"frame"`** (frames fraccionarios, parpadeo) · **no escalar el canvas por DPR** (hero borroso en retina) · **servir resolución desktop a móvil** (10+MB en 4G, rebote) · **JPG en 2026** cuando AVIF/WebP pesan la mitad · **`<video>` con keyframe interval por defecto** esperando seek suave (stutter garantizado) · **sprite-sheet con 147 frames** (textura excede el límite de GPU) · **hacer la secuencia el LCP element** (penaliza CWV) · **ignorar `prefers-reduced-motion`** · **sin loader ni frame 0 inmediato** (canvas en blanco mientras precarga) · **`setInterval`/scroll listener crudo** en vez de `scrub`+rAF (tearing) · **mantener todos los frames como `ImageBitmap` sin liberar en SPA** (memory leak entre rutas).
