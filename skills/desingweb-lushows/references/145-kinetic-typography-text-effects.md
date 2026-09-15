# 145 — Kinetic typography & text effects

**CRAFT, code-heavy.** Léelo para reveals de texto, variable font animation, scramble, marquee, text-on-path, text mask. Pareja de 03 (tipografía), 07 (motion), 39 (interacción), 12 (frontier). Regla de oro: **la tipografía es el "lujo" más barato — antes de meter un hero Three.js, un titular bold con split-reveal logra el 90% del impacto al 5% del costo. La legibilidad gana siempre sobre el efecto.**

## 1. Por qué type-as-motion gana

Un titular gigante en variable font con reveal escalonado eleva cualquier sitio a premium **sin WebGL, sin assets pesados, sin librerías de 200kb**. El texto ya está en el DOM: accesible, indexable (SEO), escalable, crujiente. Mientras una imagen "rica" pesa megas y se ve borrosa al zoom, un `<h1>` animado pesa cero bytes extra.

## 2. Split-text reveals — GSAP SplitText (FREE en 3.13)

Desde **GSAP 3.13** SplitText es **gratis**, la mitad de tamaño, con **masking nativo** (`mask:"lines"` crea los wrappers `overflow:hidden` solos) y **`autoSplit`** (re-split automático al cargar fonts o cambiar tamaño):
```js
gsap.registerPlugin(SplitText);
document.fonts.ready.then(() => {
  SplitText.create(".hero", {
    type:"lines", mask:"lines", autoSplit:true,
    onSplit(self){
      return gsap.from(self.lines, { yPercent:110, opacity:0, duration:.9, stagger:.12, ease:"expo.out" });
    }
  });
});
```
Char-by-char (con moderación, solo titulares cortos): `SplitText.create(".hero",{type:"chars,words", mask:"chars"})` + `gsap.from(split.chars,{yPercent:100, rotateX:-90, transformOrigin:"50% 100%", stagger:{each:.025}, ease:"back.out(1.7)"})`. **Accesibilidad (no negociable):** SplitText inyecta `aria-label` con el texto original y marca chars con `aria-hidden` — verifícalo; respeta `prefers-reduced-motion` (`if(reduce){ gsap.set(".hero",{opacity:1}) }` sin split).

## 3. Variable font animation — "type that responds"

Animar `font-variation-settings` (wght, wdth, slnt, opsz + ejes custom) es CSS animable nativo. Truco 2026 para interpolación suave: registrar cada eje como `@property` tipado:
```css
@property --wght{ syntax:"<number>"; inherits:false; initial-value:400; }
.vf{ font-variation-settings:"wght" var(--wght); transition:--wght .35s ease; }
.vf:hover{ --wght:900; }  /* el texto "engorda" al hover */
```
**Scroll-driven sin JS:** `@keyframes weightUp{ from{--wght:200} to{--wght:900} } .scroll-type{ animation:weightUp linear both; animation-timeline:scroll(root block); }`. **Mouse-distance** (cada letra reacciona a la cercanía del cursor): split en chars, en `pointermove` mapea la distancia al peso con `gsap.utils.mapRange`.

## 4. Scramble / decode / typewriter

**Scramble** (GSAP `ScrambleTextPlugin`, gratis): `gsap.to(".decode",{duration:2, scrambleText:{text:"BIO-SETA", chars:"01█▓", speed:.4}})`. **Vanilla decode:**
```js
function scramble(el, final, {speed=30, glyphs="ABCDEF0123█▓░"}={}){
  let frame=0;
  const id=setInterval(()=>{
    el.textContent = final.split("").map((c,i)=> i < frame/3 ? c : glyphs[Math.random()*glyphs.length|0]).join("");
    if(frame++ > final.length*3) clearInterval(id);
  }, speed);
}
```

## 5. Kinetic layouts

**Marquee infinito seamless (CSS puro)** — duplicar contenido + trasladar exactamente `-50%`:
```css
.track{ display:inline-flex; width:max-content; animation:scroll 18s linear infinite; }
@keyframes scroll{ to{ transform:translateX(-50%); } }
.marquee:hover .track{ animation-play-state:paused; }
@media (prefers-reduced-motion:reduce){ .track{ animation:none; } }
```
(el segundo span con `aria-hidden="true"`). **Scroll-velocity skew** (texto se estira/inclina según velocidad de scroll):
```js
ScrollTrigger.create({ onUpdate:(self)=>{
  const s = gsap.utils.clamp(-12, 12, self.getVelocity()/-250);
  gsap.to(".vel-text", {skewY:s, scaleY:1+Math.abs(s)/100, duration:.4, ease:"power3", overwrite:true});
}});
```
**Text on a path** (SVG `<textPath>` animable con `<animate attributeName="startOffset" from="0%" to="-50%" dur="8s" repeatCount="indefinite"/>`). **Text mask con video/imagen** (`background-clip:text`): para video real, `<video>` fullscreen + overlay con texto negro sobre blanco y `mix-blend-mode:screen` (más robusto en Safari que clip directo). **3D/extruded text** (CSS, sin WebGL): stack de text-shadows o pseudo-elementos en `translateZ` dentro de `transform-style:preserve-3d`, rotando con scroll.

## 6. El gusto — editorial-premium vs cheesy

Kinetic type se ve **premium** cuando el movimiento es de entrada (reveal once) o reactivo sutil (hover/velocity), con eases de calidad (`expo.out`, `power4`), duraciones 0.6-1.2s, stagger fino, y **una** idea kinética por sección. **Cheesy** cuando todo rebota, gira y parpadea a la vez. **Pairing con fonts premium gratis 2026:** **Bricolage Grotesque** (variable wght/wdth/opsz, editorial-playful, la estrella open-source), **Clash Display** (Fontshare, geométrica de alto contraste, lujo fashion en grande), **Roboto Flex** y **Recursive** (muchos ejes para animar). Para body, sans neutro y deja el kinetismo solo en displays.

## Kinetic-type anti-patterns — blacklist
**char-by-char en párrafos largos** (stagger de chars en 60 palabras = ruido ilegible y jank; chars solo en titulares ≤8 palabras, `lines` para el resto) · **olvidar `prefers-reduced-motion`** (marquees/autoplay sin opt-out = fallo a11y + mareo) · **animar `font-weight`** en lugar de `font-variation-settings` con `@property` (saltos discretos, no interpolación) · **split sin `aria-label`** (screen readers leen "H-o-n-g-o-s") · **marquee con JS por frame** (`left`) cuando CSS `transform` lo hace en GPU gratis · **no esperar `document.fonts.ready`** antes de split (mide líneas con la fallback font) · **`background-clip:text` con video en Safari** sin fallback (texto invisible) · **velocity-skew sin clamp ni `overwrite`** (el texto se dispara a 80° y acumula tweens) · **todo a la vez** (scramble + skew + 3D + marquee en una sección = parque de diversiones) · **animar layout props** (`width`, `top`, `margin`).
