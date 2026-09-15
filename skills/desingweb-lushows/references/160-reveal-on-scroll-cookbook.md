# 160 — Reveal-on-scroll cookbook

**CRAFT, code-heavy.** El movimiento más usado de la web — y el más fácil de arruinar (AOS-slop). Pareja de 07 (ScrollTrigger), 145 (kinetic type), 149 (intros), 151 (parallax). Regla de oro: **once por defecto; dispara con `start: 'top 85%'`; NUNCA animes en reveal-on-scroll lo que ya es visible al cargar (el above-the-fold usa entrada on-load); `transform`/`opacity` only.**

## 1. El principio

**Once vs replay:** por defecto **once** (re-animar cada entrada/salida es nervioso y rompe la lectura; replay solo para decorativos en bucle). **El trigger point:** dispara cuando el elemento *ya está entrando* — el estándar premium es `start: 'top 85%'` (GSAP) o `rootMargin: '0px 0px -15% 0px'` (IO). Disparar a `top 100%` = la animación termina antes de ser visible; muy tarde (`top 50%`) = aparece "tarde". **La regla del above-the-fold:** NUNCA pongas `opacity:0` esperando un scroll que no ha ocurrido en el hero/H1/primer párrafo — usa entrada *on load* o nada. **Duración/easing premium:** 400-700ms (nunca >800ms), `ease-out` (`cubic-bezier(0.16,1,0.3,1)` = expo-out, el más usado en Awwwards), distancias cortas (`translateY(20-40px)`, jamás `100px+`).

## 2. Los engines

**IntersectionObserver (vanilla, el default correcto para simple):**
```js
const io = new IntersectionObserver((entries, obs)=>{ for(const e of entries){ if(!e.isIntersecting) continue;
  e.target.classList.add('is-visible'); obs.unobserve(e.target); /* once */ }},
  { threshold:0.15, rootMargin:'0px 0px -10% 0px' });
document.querySelectorAll('[data-reveal]').forEach(el=>io.observe(el));
```
```css
[data-reveal]{ opacity:0; transform:translateY(28px);
  transition:opacity .6s cubic-bezier(.16,1,.3,1), transform .6s cubic-bezier(.16,1,.3,1); will-change:transform,opacity; }
[data-reveal].is-visible{ opacity:1; transform:none; }
```
**GSAP ScrollTrigger `batch()` (para grids):** `ScrollTrigger.batch('[data-reveal]', { start:'top 85%', once:true, onEnter:b=>gsap.to(b,{opacity:1, y:0, duration:.7, ease:'expo.out', stagger:0.08}) })` — agrupa los que entran en el mismo frame con stagger conjunto (el efecto "deck deal"). **CSS scroll-driven (no-JS):** `animation:reveal linear both; animation-timeline:view(); animation-range:entry 0% entry 40%` (sin soporte se queda en estado final = fallback perfecto).

## 3. El catálogo de reveals (copy-paste)

```css
.r-fade-up{ opacity:0; transform:translateY(28px); }                    /* el workhorse */
.r-mask{ overflow:hidden; } .r-mask > *{ display:block; transform:translateY(110%); transition:transform .8s cubic-bezier(.16,1,.3,1); } .r-mask.is-visible > *{ transform:translateY(0); } /* mask-up, el más premium */
.r-blur{ opacity:0; filter:blur(12px); transform:translateY(14px); }    /* blur-in */
.r-scale{ opacity:0; transform:scale(.92); }                            /* scale-in */
.r-clip{ clip-path:inset(0 0 100% 0); } .r-clip.is-visible{ clip-path:inset(0 0 0 0); } /* clip wipe */
.is-visible{ opacity:1!important; transform:none!important; filter:none!important; }
```
**Duraciones por efecto:** fade/scale/blur .6-.7s; mask-up .8s (la distancia del 110% pide más); clip-wipe .8s con easing más dramático (`cubic-bezier(.77,0,.18,1)`). **Line-by-line text:** split en líneas en `.mask` + stagger por línea (SplitText/Splitting).

## 4. Coreografía de grid / stagger

No reveles 12 cards a la vez (abrumador) ni una por una lenta (aburre): **stagger de 60-100ms** agrupado por fila. **GSAP `batch()`** lo hace solo. **IO + `transition-delay` por índice (vanilla):** el `i` es el índice **dentro del callback** (los que entran en ese frame), no global — así cada fila reinicia en `0ms` en vez de heredar delays gigantes (card 30 con `2400ms` = bug AOS clásico). **Stagger direccional** (desde el centro): calcula distancia de cada card a un origen → `--d` delay; GSAP nativo `stagger:{each:.06, from:'center', grid:'auto'}`.

## 5. Scrub reveals

Scrub = la animación avanza/retrocede con el scroll (parallax, slow reveals, secuencias pineadas). `gsap.to('.bg-img', {yPercent:-20, ease:'none', scrollTrigger:{trigger:'.section', start:'top bottom', end:'bottom top', scrub:true}})` (`scrub:1` añade 1s de lag inercial; `ease:'none'` obligatorio). **Pinned reveal sequence:** timeline con `pin:true, scrub:1` revelando pasos. **Counter on enter** (no scrub, una vez): `gsap.to({v:0}, {v:2024, duration:2, onUpdate(){ el.textContent=Math.round(this.targets()[0].v).toLocaleString() }})`. Regla: **scrub para movimiento continuo decorativo; once/onEnter para contenido** (re-animar texto al scroll-up marea).

## 6. Craft, perf & a11y

**Solo `transform`/`opacity`** (`top`/`height`/`margin` = reflow/jank). **`will-change` con disciplina** (quítalo en `transitionend`). **`prefers-reduced-motion`** innegociable (estado final inmediato, cero movimiento; en JS `if(matchMedia('(prefers-reduced-motion:reduce)').matches){ revealAll(); return; }`). **Sin layout shift** (`opacity:0` conserva el box — bien; `display:none` no; imágenes con `aspect-ratio`). **No retrases SEO** (`opacity:0` no oculta de Google, pero no escondas contenido crítico tras JS que puede fallar). **El FOUC fix con fallback no-JS:** `<script>document.documentElement.classList.add('js')</script>` + `.js [data-reveal]{opacity:0}` (sin JS → todo visible por defecto, no contenido invisible para siempre).

## Reveal anti-patterns — blacklist (AOS-slop)
**animar el above-the-fold en scroll** (hero con `opacity:0` esperando scroll — pecado capital) · **replay infinito** de reveals de contenido · **delays gigantes acumulados** (`data-aos-delay="2400"`; usa índice por frame, no global) · **distancias largas** (`translateY(100px+)`) · **duraciones largas** (>800ms) · **easing lineal o `ease-in`** (robótico; usa `ease-out`/expo-out) · **animar `width/height/top`** (reflow) · **scrub en copy/texto** (re-animar párrafos al scroll-up = náusea) · **ignorar `prefers-reduced-motion`** · **`will-change` global** o en `*` · **FOUC sin fallback** (`opacity:0` en CSS base sin clase `.js` → invisible si el JS falla) · **everything reveals** (si todo se anima, nada destaca; revelar es jerarquía) · **bounce/overshoot en UI seria** (`back.out` en cada card grita "plantilla 2018").
