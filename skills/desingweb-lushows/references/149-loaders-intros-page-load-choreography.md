# 149 — Loaders, intros & la secuencia cinemática de page-load

**CRAFT, code-heavy.** Léelo para preloaders, la coreografía de entrada del hero, el handoff loader→contenido. Pareja de 07 (motion), 145 (SplitText), 142 (award anatomy), 39 (interacción). Regla de oro: **un loader solo se justifica si compra tiempo real (WebGL/video/fonts grandes); en una página de 200ms es fricción de vanidad. El loader nunca debe "popear" hacia el hero — debe *convertirse* en él.**

## 1. Por qué la entrada importa

Los primeros 2 segundos fijan el tono. En sitios Awwwards el page-load no es un spinner: es la **primera coreografía**, la firma del estudio (establece ritmo, peso tipográfico, jerarquía antes del scroll). Clave: **perceived vs actual performance** — un loader bien orquestado no acelera la carga (a menudo la *retrasa*), pero transforma una espera en momento de marca. Antídoto profesional: **honestidad + handoff sin costura**.

## 2. Patrones de loader

**Percentage counter (0→100)** (el clásico; brillante sincronizado a carga real), **wipe/curtain reveal** (panel sólido que sube/baja y descubre el hero), **logo-draw** (`stroke-dashoffset` sobre SVG lineal), **mask-reveal** (`clip-path` obturador), **minimal line-progress** (línea de 1px con `scaleX` — el más elegante y barato). **Justificado:** WebGL/Three, video hero, galerías pesadas, variable fonts grandes. **Vanidad/fricción:** blogs, landings estáticas, SPAs hidratadas, cualquier FCP <1s.

**Copy-paste GSAP loader → counter → exit:**
```js
const counter = {val:0}; const $num = document.querySelector(".loader__num");
gsap.timeline({defaults:{ease:"expo.out"}})
  .to(counter, {val:100, duration:2.4, ease:"power2.inOut", onUpdate:()=>{ $num.textContent = Math.round(counter.val).toString().padStart(3,"0"); }})
  .to(".loader__bar", {scaleX:1, duration:2.4, ease:"power2.inOut"}, 0)
  .to(".loader__num", {yPercent:-120, duration:.6}, ">-0.1")
  .to(".loader", {yPercent:-100, duration:1, onComplete:()=>document.querySelector(".loader").remove()}, "<0.1")
  .add(()=>heroReveal(), "<0.3"); // solapa el hero ANTES de que la cortina termine
```
(`CustomEase.create("expoOut","0.16,1,0.3,1")` es el "look caro" universal.)

## 3. La coreografía del hero reveal

El hero entra **escalonado y orquestado**, no todo a la vez. Orden canónico: imagen (clip/scale) → headline (mask-up por línea con SplitText) → subtexto → nav → CTA. El secreto del "caro" es el **stagger negativo con solape** (`-=1.1`) y un easing único, no `power1`:
```js
function heroReveal(){
  const split = SplitText.create(".hero__title", {type:"lines", mask:"lines"});
  return gsap.timeline({defaults:{ease:"expo.out", duration:1.1}})
    .from(".hero__img", {scale:1.3, duration:1.6, clipPath:"inset(100% 0 0 0)"})
    .from(split.lines, {yPercent:110, stagger:.08}, "-=1.1")
    .from(".hero__sub", {yPercent:100, opacity:0}, "-=0.8")
    .from(".nav a", {y:-20, opacity:0, stagger:.05}, "-=0.9")
    .from(".hero__cta", {opacity:0, y:20}, "-=0.6");
}
```
`overflow:hidden` en el wrapper hace el efecto "mask-up" (las líneas suben desde detrás de un borde invisible).

## 4. Carga real de assets (honestidad)

Sincronizar el counter al progreso **real** > una barra temporizada. El híbrido (el número nunca baja, se interpola hacia el target real):
```js
let target = 0; const proxy = {v:0};
async function loadAssets(onProgress){
  await document.fonts.ready;
  const imgs = [...document.querySelectorAll("img[data-preload]")].map(i=>i.dataset.src);
  let done=0;
  await Promise.all(imgs.map(src=>new Promise(res=>{ const img=new Image();
    img.onload=img.onerror=()=>{ onProgress(++done/imgs.length); res(); }; img.src=src; })));
}
loadAssets(p => { target = p*100; });
gsap.ticker.add(()=>{ proxy.v += (target-proxy.v)*0.06;   // lerp hacia el progreso real
  $num.textContent = Math.round(proxy.v).toString().padStart(3,"0");
  if(proxy.v > 99.5){ proxy.v=100; runExit(); } });
```
Para **WebGL**, usa `THREE.LoadingManager` (`onProgress`) o el `progress` de GLTFLoader. Honestidad: si fakeas, fakea con un mínimo de tiempo visible (~1s) para que no parpadee, pero nunca finjas 100% si el video aún no puede reproducir.

## 5. Transición hacia el contenido (handoff)

El error es la cortina que termina y *después* aparece el hero. Lo correcto: **solapar** (el `heroReveal()` empieza mientras la cortina aún sube — `"<0.3"`). Tres técnicas: **curtain-becomes-page** (el panel del loader y el primer bloque del hero comparten color/posición), **clip-path shared** (animar el mismo `inset()` del loader hacia el `clip-path` de la imagen hero), **FLIP** (si el logo del loader es el logo del nav, `Flip.getState` → mover al nav → `Flip.from` para que vuele en vez de desaparecer y reaparecer).

## 6. Performance & accesibilidad

**No bloquear FCP/LCP** (el loader inline con CSS crítico + JS mínimo no debe esperar un bundle grande; render el loader con CSS puro primero, hidrata GSAP después). **`prefers-reduced-motion`** salta la intro. **Returning-visitor skip** con `sessionStorage` (el intro completo solo en la primera visita de la sesión):
```js
const skip = matchMedia("(prefers-reduced-motion: reduce)").matches || sessionStorage.getItem("introSeen");
if(skip){ gsap.set(".loader",{display:"none"}); gsap.set([".hero__img",".hero__title",".hero__sub"],{clearProps:"all"}); }
else { sessionStorage.setItem("introSeen","1"); runIntro(); }
```
**Anti "loader en 200ms"** (si la página ya está lista, no muestres loader). **A11y:** `role="progressbar"` con `aria-valuenow`, o `aria-busy="true"` en `<body>` que pase a `false` al terminar; nunca atrapes el foco en el loader.

## Loader/intro anti-patterns — blacklist
**loader en una página estática rápida** (vanity friction; FCP <1s no tiene nada que cargar) · **barra fake que no llega a 100** o salta de 80→100 de golpe · **counter que retrocede** (jamás; lerp monotónico hacia el target) · **cortina que termina antes de que el hero exista** (pop jarring; siempre solapar el reveal) · **mínimo de 3-5s forzado** (respeta el tiempo del usuario; tope ~2.5s salvo WebGL real) · **sin `prefers-reduced-motion`** · **repetir el intro en cada navegación interna** (SPA; usa `sessionStorage`) · **bloquear LCP con el bundle de GSAP** (el loader debe pintar con CSS crítico) · **`will-change` permanente** (agótalo solo durante la animación) · **SplitText sin `overflow:hidden`/`mask`** (el "mask-up" se ve como texto flotante, no reveal) · **animar `top/left/width`** en vez de `transform/clip-path` · **spinner genérico infinito** sin progreso real (comunica "roto", no "cargando").
