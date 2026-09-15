# 39 — Toolkit de interacción creativa & craft de lujo

Cookbook de las interacciones firma + la capa de refinamiento que separa "$200k de agencia" de "plantilla". **Léelo cuando construyas experiencias inmersivas/creativas o quieras el pulido de lujo.** Pareja de 07, 12, 26, 34. Stack: vanilla JS + **GSAP 3.13+** (todo gratis desde 2025) + Lenis + View Transitions.
**Reglas de oro transversales:** easings de salida (`expo.out`, `power3.out`, `cubic-bezier(.625,.05,0,1)`) · reveals **0.8-1.4s** · stagger **0.01-0.08** · lerp de cursor/scroll **0.1** · factor magnético **~0.2**. Nada hace bounce. Nada es 1:1.
```js
gsap.registerPlugin(ScrollTrigger,SplitText,Observer,Draggable,InertiaPlugin,Flip);
const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
```

## 1. Custom cursors

Clave del cursor de lujo: **lerp lento (0.12-0.18), pequeño (8-14px), nunca 1:1** (1:1 grita "tech demo").
```css
*{cursor:none} @media(hover:none){*{cursor:auto}.cursor{display:none}}
.cursor{position:fixed;width:10px;height:10px;border-radius:50%;background:#fff;pointer-events:none;z-index:9999;transform:translate(-50%,-50%);mix-blend-mode:difference;will-change:transform}
.cursor--label{padding:0 14px;width:auto;height:auto;border-radius:40px;font-size:12px;color:#000;background:#fff;mix-blend-mode:normal}
```
```js
const cur=document.querySelector('.cursor'), mouse={x:innerWidth/2,y:innerHeight/2};
addEventListener('mousemove',e=>{mouse.x=e.clientX;mouse.y=e.clientY},{passive:true});
const xTo=gsap.quickTo(cur,'x',{duration:.4,ease:'power3'}), yTo=gsap.quickTo(cur,'y',{duration:.4,ease:'power3'});
function renderCursor(){ xTo(mouse.x); yTo(mouse.y); }   // llamar desde el RAF global (§6)
document.querySelectorAll('[data-cursor]').forEach(el=>{
  el.addEventListener('mouseenter',()=>{cur.textContent=el.dataset.cursor;cur.classList.add('cursor--label')});
  el.addEventListener('mouseleave',()=>{cur.classList.remove('cursor--label');cur.textContent=''});
});
```
`mix-blend-mode:difference` + cursor blanco invierte cualquier fondo (truco Cuberto/Obys; quítalo en `--label` para legibilidad). **Anti-slop:** sin blur, sin 40px, sin trail de 20 partículas. Discreto.

## 2. Sliders / galerías arrastrables

**Slider físico (Inertia + snap + skew por velocidad):**
```js
Draggable.create(track,{type:'x',edgeResistance:.85,bounds:{minX:maxX,maxX:0},inertia:true,
  snap:{x:v=>Math.round(v/slideW)*slideW}, onDrag:applySkew, onThrowUpdate:applySkew});
function applySkew(){ const v=gsap.getProperty(track,'x')-(this.prevX||0); this.prevX=gsap.getProperty(track,'x');
  gsap.to(slides,{skewX:gsap.utils.clamp(-12,12,-v*.4),duration:.4,ease:'power2.out'}); }
```
**Wheel+touch+teclado unificados (Observer):**
```js
Observer.create({target:window,type:'wheel,touch,pointer',wheelSpeed:-1,tolerance:10,preventDefault:true,
  onUp:()=>goTo(index+1), onDown:()=>goTo(index-1)});
function goTo(i){ index=gsap.utils.clamp(0,slides.length-1,i); gsap.to(track,{x:-index*slideW,duration:1.1,ease:'expo.out'}); }
```
**Galería pinned (scroll vertical → horizontal):**
```js
gsap.to(sections,{xPercent:-100*(sections.length-1),ease:'none',
  scrollTrigger:{trigger:'.h-wrap',pin:true,scrub:1,snap:1/(sections.length-1),end:()=>'+='+wrap.offsetWidth}});
```
Marquee infinito: GSAP `horizontalLoop` helper o `modifiers:{x:gsap.utils.unitize(x=>parseFloat(x)%total)}`.

## 3. Transiciones de página/sección (lujo)

**Clip-path wipe + cross-dissolve con escala ("pasar página de revista"):**
```js
gsap.timeline({scrollTrigger:{trigger:'.fig',start:'top 80%'}})
  .to('.fig',{clipPath:'inset(0% 0% 0% 0%)',duration:1.2,ease:'expo.inOut'})
  .from('.fig img',{scale:1.3,duration:1.4,ease:'expo.out'},0);  // misma start, distinto end = parallax interno
```
**View Transitions MPA (cross-document, cero JS — Chrome 126+/Safari 18.2+):**
```css
@view-transition{navigation:auto}
::view-transition-old(root){animation:fade .5s cubic-bezier(.625,.05,0,1) both}
.hero-img{view-transition-name:hero}   /* shared element entre páginas */
```
**SPA:** `document.startViewTransition(swap)` con fallback a curtain GSAP. **Shared-element con Flip** (grid→detalle, "layoutId" en vanilla):
```js
const state=Flip.getState(card); document.body.classList.add('detail-open');
Flip.from(state,{duration:.8,ease:'power3.inOut',absolute:true,scale:true});
```

## 4. Reveals firma & tipografía cinética

**Line-mask + char reveal (SplitText):**
```css
.line-mask{overflow:hidden}
```
```js
const split=new SplitText('.headline',{type:'lines,chars',linesClass:'line-mask'});
gsap.from(split.lines,{yPercent:120,duration:1.1,ease:'expo.out',stagger:.08,scrollTrigger:{trigger:'.headline',start:'top 85%'}});
// char-by-char SOLO para un hero, con mucha moderación
```
**Skew + marquee por velocidad de scroll:** `ScrollTrigger.create({onUpdate:s=>gsap.to('.skew',{skewY:gsap.utils.clamp(-20,20,s.getVelocity()/-300),duration:.5})})`.
**Grid reveal escalonado (batch) + blur-in:** `ScrollTrigger.batch('.grid-item',{onEnter:b=>gsap.to(b,{y:0,opacity:1,filter:'blur(0px)',stagger:.06,overwrite:true})})`.
**Reglas de gusto:** anima líneas de titular, imágenes al entrar, números, un hero char-by-char. **NO animes** párrafos de body char-by-char, todo a la vez, el menú, cada ícono. Si todo se mueve, nada se siente caro.

## 5. Micro-interacciones magnéticas & táctiles

```js
// Botón magnético — factor 0.2 (0.5+ se siente pegajoso/try-hard)
document.querySelectorAll('.magnetic').forEach(btn=>{
  const xTo=gsap.quickTo(btn,'x',{duration:.6,ease:'power3'}), yTo=gsap.quickTo(btn,'y',{duration:.6,ease:'power3'});
  btn.addEventListener('mousemove',e=>{const r=btn.getBoundingClientRect();
    xTo((e.clientX-(r.left+r.width/2))*.2); yTo((e.clientY-(r.top+r.height/2))*.2);});
  btn.addEventListener('mouseleave',()=>{xTo(0);yTo(0)});
});
```
```css
/* Subrayado que entra por un lado y sale por el otro */
.link::after{content:'';position:absolute;left:0;bottom:-2px;width:100%;height:1px;background:currentColor;transform:scaleX(0);transform-origin:right;transition:transform .5s cubic-bezier(.625,.05,0,1)}
.link:hover::after{transform:scaleX(1);transform-origin:left}
/* Hover de imagen: escala dentro de overflow clip (NUNCA escalar el contenedor) */
.media{overflow:clip}.media img{transition:transform .8s cubic-bezier(.625,.05,0,1)}.media:hover img{transform:scale(1.04)}
```
**Tilt 3D con glare** (sutil, máx ±6-12deg): `gsap.to(c,{rotateY:(px-.5)*12,rotateX:(.5-py)*12,duration:.5,transformPerspective:900})` + glare radial en `::after` con `--gx/--gy`.

## 6. La capa de pulido de lujo

**El RAF único (Lenis + GSAP + cursor + grain a 60fps):**
```js
const lenis=new Lenis({lerp:.1,smoothWheel:true});   // 0.1 = el lerp que se lee premium
lenis.on('scroll',ScrollTrigger.update);
gsap.ticker.add(t=>{lenis.raf(t*1000);renderCursor();renderGrain();});  // UN solo loop
gsap.ticker.lagSmoothing(0);
```
**Nunca** múltiples `requestAnimationFrame` — Lenis/GSAP/cursor/grain/canvas comparten `gsap.ticker`. Eso mantiene 60fps reales.
**Loader elegante** (contador 0→100 + barra + clip-path reveal):
```js
gsap.timeline()
  .to({n:0},{n:100,duration:1.6,ease:'power2.inOut',onUpdate(){count.textContent=Math.round(this.targets()[0].n)}})
  .to('.loader-bar',{scaleX:1,transformOrigin:'left',duration:1.6,ease:'power2.inOut'},0)
  .to('.loader',{clipPath:'inset(0 0 100% 0)',duration:.9,ease:'expo.inOut'})
  .from('.hero .line',{yPercent:120,stagger:.08,duration:1.1,ease:'expo.out'},'-=.4');
```
**Float idle del hero + sombra en anti-fase** (truco de profundidad):
```js
gsap.to('.hero-obj',{y:-18,duration:3,ease:'sine.inOut',repeat:-1,yoyo:true});
gsap.to('.hero-shadow',{scale:.9,opacity:.4,duration:3,ease:'sine.inOut',repeat:-1,yoyo:true});  // objeto sube → sombra encoge/aclara
```
Soft contact shadow (no `box-shadow` duro): `.hero-shadow{filter:blur(24px);background:radial-gradient(ellipse,rgba(0,0,0,.4),transparent 70%)}`.
**Kill-switch reduced-motion (obligatorio):** `if(reduced){gsap.globalTimeline.timeScale(999);ScrollTrigger.getAll().forEach(t=>t.kill())}`.
**Consistencia:** un solo set de easings (`--ease-out:cubic-bezier(.625,.05,0,1)` siempre), una velocidad base de reveal (1.1s), una escala de hover (1.04). **La coherencia ES el lujo.**

## Anti-slop — "tech demo / try-hard" vs "crafted / lujo"
| Slop | Crafted |
|---|---|
| `bounce`/`elastic`/`back` en UI | `expo.out`/`power3.out`/`cubic-bezier(.625,.05,0,1)` |
| Cursor 1:1, 40px, con trail | lerp 0.1-0.18, 10px, difference, discreto |
| Hover `scale(1.2)` | `scale(1.04)` en `overflow:clip` |
| Magnético 0.5+ (pegajoso) | factor **0.2** |
| Body entero char-by-char | solo titulares en líneas |
| Neon glow `0 0 40px cyan` | soft contact shadow (blur+radial) |
| Reveals 0.3s o 3s | **0.8-1.4s** |
| Stagger 0.2 | **0.01-0.08** |
| Parallax 200px (mareante) | 8-40px |
| Múltiples `rAF` + jank | **un solo `gsap.ticker`** |
| 6 fuentes/5 easings/4 duraciones | un easing, una duración, una escala |
| Ignorar `prefers-reduced-motion` | kill-switch siempre |
| Tilt ±25deg | tilt ±6-12deg con glare tenue |

**Mantra:** lento, pequeño, salida-suave, coherente. El lujo no es *más* movimiento — es **menos, mejor calibrado.** El 90% de la página está quieta para que el 10% que se mueve se sienta inevitable.
