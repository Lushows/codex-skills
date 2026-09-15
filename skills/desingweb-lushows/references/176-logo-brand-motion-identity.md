# 176 — Logo & brand motion identity

**CRAFT + brand.** Animar un sistema de marca para la web. Pareja de 24 (brand identity/logo responsive), 156 (SVG anim), 149 (loaders), 173 (motion systems). Regla de oro: **motion ES un activo de marca (cómo se mueve = personalidad); el logo debe quedar "alive but dignified"; el reveal es one-shot por sesión, no en cada navegación.**

## 1. Por qué la marca en movimiento

En 2026 un logo estático ya no basta: en pantallas el logo casi siempre llega *en movimiento*, y **cómo se mueve = personalidad** (portador de marca como el color o la tipografía). El **logo reveal** es la primera impresión —ocurre durante el page-load, antes de leer una palabra— por eso se ancla a la coreografía del loader (§3). La disciplina madura: **motion brand guidelines** (estandarizan cómo anima una marca en todos los touchpoints). Referencias: **Google/Material** (motion funcional/responsivo, curvas estandarizadas), **Mailchimp** (*expressive easing*: bounces snappy, el movimiento ES el tono de voz), **Stripe** (restraint quirúrgico, "premium por sustracción"), **Klarna** (3 principios: *Simple, Purposeful, Playful* — el patrón: 3-4 adjetivos que gobiernan toda decisión).

## 2. Técnicas de animación de logo

**(a) Line-draw / self-drawing** (`stroke-dashoffset`, la más universal): normaliza `stroke-dasharray` a `getTotalLength()` (clave: evita el "salto"):
```css
.logo-stroke{ stroke-dasharray:1; stroke-dashoffset:1; animation:draw 1.4s cubic-bezier(.65,0,.35,1) forwards; }
@keyframes draw{ to{ stroke-dashoffset:0; } }
```
```js
document.querySelectorAll('.logo-stroke').forEach(p=>{ const L=p.getTotalLength(); p.style.strokeDasharray=L; p.style.strokeDashoffset=L; });
```
Con GSAP **DrawSVG** es trivial y maneja sub-paths. **(b) Build/assemble** (las piezas vuelan a su sitio, ideal logos geométricos; stagger es la clave): `gsap.from('.mark > *', { scale:0, opacity:0, duration:.7, ease:'back.out(1.6)', stagger:{ each:.06, from:'center' } })`. **(c) Mask reveal** (wipe sobre el logo sólido completo, el más limpio para logotipos densos). **(d) Morph entre estados** (MorphSVG: mark→glyph, o favicon→logo full; premium pero caro — una vez, no en cada navegación). **(e) Loop vs one-shot:** el **reveal es one-shot** (una vez por sesión, cachea en `sessionStorage`); el **ambient loop** es la respiración sutil en idle (§4). Nunca loopees el reveal completo.

## 3. El momento del reveal (page-load + FLIP)

El reveal premium **no es un fade**: es una entrada con firma. La secuencia de élite es el **FLIP del loader al nav** — el mismo logo que aparece centrado en el loader *vuela* a su posición en la navbar (no hay dos logos, es el mismo elemento; continuidad espacial = "caro"):
```js
const first = logo.getBoundingClientRect();
Object.assign(logo.style, { position:'fixed', top:target.top+'px', left:target.left+'px', width:target.width+'px' });
const last = logo.getBoundingClientRect();
logo.style.transform = `translate(${first.left-last.left}px,${first.top-last.top}px) scale(${first.width/last.width})`;
logo.style.transformOrigin = 'top left';
requestAnimationFrame(()=>{ logo.style.transition='transform .9s cubic-bezier(.7,0,.2,1)'; logo.style.transform='none'; });
```
**Timing/easing que matchea la marca (el easing ES la firma):** luxury/editorial → `cubic-bezier(.7,0,.2,1)` 900-1200ms; tech/energético → `power3.out`/`back.out` 500-700ms snappy; playful → `elastic.out(1,.5)`/bounce. Regla: **decelerar al final** (ease-out) se siente natural y resuelto; linear, mecánico.

## 4. Logo responsivo y sistémico

El **sistema de logo** (ref 24) es una escala, no un archivo: **full lockup → mark → favicon**, intercambiados por breakpoint (un lockup horizontal a 320px es ilegible): `.logo-full{ display:block } .logo-mark{ display:none } @media (max-width:640px){ .logo-full{ display:none } .logo-mark{ display:block } }` (la transición entre niveles puede ser un morph suave). **Ambient motion (loop-safe):** vivo pero no molesto — sutil, lento, periódico, **pausable** (`@media (hover:hover){ .mark-petal{ animation:breathe 6s ease-in-out infinite alternate } }`). **Interactive logo (reacciona al cursor):** magnetic/tilt suave (decoración, nunca esencial; `pointermove` → `rotateY`/`translateX`, reset en `pointerleave`).

## 5. Motion brand guidelines (el sistema documentado)

Define el **motion DNA** y documéntalo como sección del brandbook: **signature easing** (1-2 curvas oficiales, token `--ease-brand`), **duration scale** (`--dur-xs 120 / -s 240 / -m 480 / -l 900`), **principios** (3-4 adjetivos estilo Klarna), **"cómo se mueve nuestra marca"** en reveals/page-transitions/micro — una sola gramática:
```css
:root{ --ease-brand: cubic-bezier(.7,0,.2,1); --ease-brand-bounce: cubic-bezier(.34,1.56,.64,1);
  --dur-s:.24s; --dur-m:.48s; --dur-l:.9s; }
.brand-anim{ transition: transform var(--dur-m) var(--ease-brand); }
```
Estos tokens conectan el logo con el **motion design system** (ref 173): el mismo easing del reveal gobierna botones, modales y page-transitions → coherencia total.

## 6. Craft & restraint

**Premium vs gimmick:** premium = una entrada con firma + ambient sutil; gimmick = girar/rebotar el logo en cada página (anima el reveal **una vez por sesión**, `sessionStorage.firstSeen`). **Formato — cuándo cada uno:** **SVG+CSS/GSAP** para line-draw/build/mask (vectorial, ligero, nítido, accesible — default; un SVG animado suele pesar menos que una sola imagen hero); **Lottie** cuando el logo tiene shape-tweens complejos de After Effects; **Rive** cuando necesitas estado/interactividad runtime (state machines). **Accesibilidad:** SVG decorativo `aria-hidden="true"` (el nombre va en texto/`aria-label` del link); **`prefers-reduced-motion` → estado final estático** (sin draw ni loop). **Performance:** anima solo `transform`/`opacity`; el ambient se pausa fuera de viewport (`IntersectionObserver`).

## Logo-motion anti-patterns — blacklist
**fade genérico** como reveal (sin firma, indistinguible) · **re-animar el logo en cada navegación** (ruido) · **el "salto" del dash** (no normalizar `stroke-dasharray` a `getTotalLength()`) · **loopear el reveal completo** en vez de un ambient sutil · **escalar el lockup horizontal a móvil** en lugar de cambiar a mark/favicon · **ambient distractor** (rotaciones amplias/rápidas que roban atención) · **ignorar `prefers-reduced-motion`** · **animar `width`/`top`/`margin`** (layout thrash) en vez de `transform` · **dos logos** (uno en loader, otro en nav) con un corte feo en vez del FLIP continuo · **easing equivocado para la marca** (`elastic` en lujo, o `linear` en todo) · **Lottie/Rive de 500KB** para lo que un SVG de 4KB resuelve · **mark interactivo que el usuario *necesita* tocar** (el motion es bonus) · **sin `aria-hidden`** en el SVG decorativo (lector deletrea paths).
