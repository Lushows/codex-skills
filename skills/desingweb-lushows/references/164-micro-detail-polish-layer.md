# 164 — Micro-detail polish layer (las 100 cosas pequeñas)

**CRAFT, code-heavy.** Lo que separa "shipped" de "crafted": 100 micro-decisiones coherentes que el usuario nunca elogia y siempre nota cuando faltan. Pareja de 35 (estados de componente), 16 (a11y), 150 (micro-interacciones), 21 (forms). Regla de oro: **ninguno cuesta >5 líneas, pero juntos comunican intención; el usuario dirá "se siente bien hecho", no "qué buen scroll-margin-top".**

## 1. Page chrome polish

**Custom scrollbar (estándar + WebKit fallback):**
```css
* { scrollbar-width:thin; scrollbar-color:var(--bar) var(--track); }  /* Firefox, Chrome 121+ */
::-webkit-scrollbar{ width:10px; } ::-webkit-scrollbar-track{ background:var(--track); }
::-webkit-scrollbar-thumb{ background:var(--bar); border-radius:99px; border:2px solid var(--track); } /* el borde "encoge" el thumb */
```
Scrollbar thin **solo en paneles internos**, nunca robes el del sistema en mobile. **Selección/caret/nativos:** `::selection{ background:var(--bar); color:#04110d }` · `:root{ caret-color:var(--bar) }` (casi nadie lo pinta) · `input{ accent-color:var(--bar) }` (checkbox/radio/range nativos) · `::marker{ color:var(--bar) }`. **Smooth scroll con el caveat:** `@media (prefers-reduced-motion:no-preference){ html{ scroll-behavior:smooth } }` + `:where(h2,h3,[id]){ scroll-margin-top:calc(var(--nav-h) + 1rem) }` (el bug #1 de "anclas tapadas por el navbar sticky" se resuelve SOLO con `scroll-margin-top`, no con JS de offset).

## 2. Focus & a11y polish

Nunca `outline:none` a secas. **`:focus-visible`** (foco solo en teclado, no al click) + doble-anillo con offset:
```css
:where(a,button,input,[tabindex]):focus-visible{ outline:2px solid var(--bar); outline-offset:3px; border-radius:6px; }
.btn:focus-visible{ outline:none; box-shadow:0 0 0 2px #04110d, 0 0 0 4px var(--bar); } /* halo + core, sobre cualquier fondo */
```
**Skip link:** `.skip{ position:fixed; top:-100% } .skip:focus{ top:1rem }`. **`:target` highlight** (pulso al llegar a `#seccion`). Patrón clave: el foco NUNCA debe verse al click con mouse — `:focus-visible` lo resuelve sin limpiar foco con JS (un anti-patrón histórico).

## 3. Number & counter animation

```css
.stat{ font-variant-numeric:tabular-nums; } /* sin jitter al cambiar dígitos */
```
```js
const fmt = new Intl.NumberFormat('es-CO');
const animate = (el, to, dur=1400)=>{ const start=performance.now();
  const tick=(now)=>{ const p=Math.min((now-start)/dur,1), eased=1-Math.pow(1-p,3); // easeOutCubic
    el.textContent=fmt.format(Math.round(to*eased)); if(p<1) requestAnimationFrame(tick); };
  requestAnimationFrame(tick); };
new IntersectionObserver((es,ob)=>es.forEach(e=>{ if(!e.isIntersecting) return;
  animate(e.target, +e.target.dataset.to); ob.unobserve(e.target); /* una vez */ }), {threshold:0.6}).observe(el);
```
**Odometer/rolling-digit** sin librería: columna de dígitos 0-9 que desliza con `transform:translateY(${-digit}em)`. Respeta reduced-motion (número final de golpe).

## 4. Reward & feedback micro

**Confetti** (canvas-confetti ~3kb): `confetti({ particleCount:80, spread:70, origin:{y:0.7} })` — **una vez**, en el momento exacto, jamás en loop, gateado por reduced-motion. **Success checkmark dibujado** (SVG `stroke-dasharray` → `stroke-dashoffset:0`). **Copy-to-clipboard con feedback de estado** (el detalle es el *cambio de label*, no un alert): `await navigator.clipboard.writeText(code); btn.textContent='¡Copiado!'; navigator.vibrate?.(8); setTimeout(()=>btn.textContent='Copiar', 1600)`. **Toast micro-choreography:** entra `translateY+opacity` (220ms), espera ~3s, sale más lento (320ms), `role="status"`/`aria-live="polite"`. **Like/heart burst:** escala 1→1.3→1 con `cubic-bezier(.34,1.56,.64,1)` (overshoot = "pop").

## 5. Native element upgrades (2026)

**Accordion `<details>` animado SIN JS** (Baseline sept 2025): `:root{ interpolate-size:allow-keywords }` + `details::details-content{ height:0; overflow:hidden; transition:height .35s ease, content-visibility .35s allow-discrete } details[open]::details-content{ height:auto }` (reemplaza el hack de `max-height:9999px`; degrada graceful). **Textarea auto-grow** (`textarea{ field-sizing:content; min-height:3lh; max-height:12lh }` — Chromium; fallback JS en Firefox/Safari). **`<dialog>` polish** (animar entrada *y* `::backdrop` con `transition: ... overlay .25s allow-discrete, display .25s allow-discrete`, cierra con Esc gratis). **Range/checkbox** (parte de `accent-color`; `appearance:none` solo si necesitas forma custom del thumb).

## 6. The taste of finish

**Tokens, no magic numbers** (un escalón de espacio `--space-1:4px` en múltiplos de 8/4 = ritmo de 8pt; la coherencia *es* el lujo). **Paridad de estados** (todo interactivo: `hover`, `focus-visible`, `active` —un `scale(.97)` da tactilidad—, `disabled`; un botón sin `:active` se siente "muerto"). **Optical alignment** (centra íconos por *peso visual*, no por bounding-box; iconos a la izquierda de texto suelen pedir `-1px`). **Skeletons > spinners** para contenido conocido (preservan layout, cero shift). **Empty-state con delight** (ilustración + copy + CTA; nunca una tabla vacía muda). **`prefers-reduced-motion`** envuelve TODO movimiento decorativo (la firma de quien sabe lo que hace):
```css
@media (prefers-reduced-motion:reduce){ *,*::before,*::after{ animation-duration:.01ms!important; animation-iteration-count:1!important; transition-duration:.01ms!important; scroll-behavior:auto!important; } }
```

## Polish anti-patterns — blacklist
**`outline: none` sin reemplazo accesible** (pecado capital; usa `:focus-visible`) · **`scroll-behavior: smooth` global** ignorando reduced-motion · **anclas tapadas por header sticky** (falta `scroll-margin-top`) · **`max-height:9999px` para "animar" acordeones** (ya hay `::details-content` + `interpolate-size`) · **números que tiemblan de ancho al contar** (falta `tabular-nums`) · **confetti/toast en loop** o que bloquea la UI · **limpiar foco con JS al click** (`blur()`) en vez de `:focus-visible` · **`transition: all`** (repinta de más; lista props explícitas) · **botones sin `:active` ni `disabled` coherente** · **`appearance:none` en checkbox/range cuando bastaba `accent-color`** · **spinner eterno donde un skeleton preservaría el layout** · **magic numbers de espaciado** (`13px`, `27px` rompiendo el 8pt) · **`::selection` con contraste ilegible** · **toasts sin `aria-live`** (invisibles para lectores).
