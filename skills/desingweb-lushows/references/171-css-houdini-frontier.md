# 171 — CSS Houdini & frontier CSS APIs

**CRAFT, avanzado, code-heavy.** Estado del arte 2026: lo Baseline, lo production-con-fallback, lo experimental. Pareja de 09 (modern CSS), 12 (frontier), 148 (gradients), 35 (componentes). Regla de oro: **muchas cosas que hace 2 años pedían JS hoy son una línea de CSS — construye en la capa Baseline (`@property`/`:has()`/`@scope`/nesting/`@starting-style`), enriquece con `@supports` (anchor positioning), decora con lo experimental (Paint API/`if()`/style queries).**

## 1. @property — la puerta de entrada

Registra custom properties **tipadas** (sin esto una variable es un string opaco que el motor no sabe interpolar) → **animas valores antes inanimables** (ángulos, colores en gradientes, %):
```css
@property --angle{ syntax:"<angle>"; inherits:false; initial-value:0deg; }
.conic-border{ background:conic-gradient(from var(--angle), #00e5a0, #061410, #00e5a0); animation:spin 4s linear infinite; }
@keyframes spin{ to{ --angle:360deg; } }
/* hover suave de gradiente */
@property --p{ syntax:"<percentage>"; inherits:false; initial-value:0%; }
.btn{ background:linear-gradient(90deg, #0a3 var(--p), #021 var(--p)); transition:--p .4s; } .btn:hover{ --p:100%; }
```
**Baseline desde 2024.** Úsala sin miedo — es la base de medio brief.

## 2. Paint API (Houdini worklet)

Dibujas `background`/`border-image` con un canvas 2D ejecutado por el compositor (GPU-friendly). Registrar worklet + `inputProperties` + pintar:
```js
// noise-worklet.js
registerPaint('noise', class{ static get inputProperties(){ return ['--noise-color','--noise-density']; }
  paint(ctx, size, props){ const color = props.get('--noise-color').toString();
    for(let i=0;i<size.width*size.height*0.024;i++){ ctx.globalAlpha=Math.random()*0.5; ctx.fillStyle=color;
      ctx.fillRect(Math.random()*size.width, Math.random()*size.height, 1.5, 1.5); } } });
```
```js
if('paintWorklet' in CSS){ CSS.paintWorklet.addModule('noise-worklet.js'); }   // feature detect
```
```css
.hero{ background-image:paint(noise); background-color:#04110d; }  /* fallback visible */
@supports not (background: paint(id)){ .hero{ background-image:url('noise.png'); } }
```
Sirve para grano/patrones/blobs/bordes paramétricos vía custom props (animable si están registradas con `@property`). **NO Baseline:** Chromium-only en 2026 (Firefox/Safari no lo envían) → enhancement decorativo, jamás funcional, siempre con `@supports not`.

## 3. CSS Anchor Positioning (la gran noticia de 2026)

Tooltips/popovers/menús anclados a un elemento, con auto-flip, **sin JS ni Floating UI/Popper**:
```css
.trigger{ anchor-name:--tip; }
.tooltip{ position:fixed; position-anchor:--tip; position-area:top center; margin-bottom:8px;
  position-try-fallbacks:bottom, top-start, bottom-start;  /* si "top" desborda, prueba estas */
  position-try-order:most-height; }
```
Con `anchor()` controlas lados individuales (`top:anchor(--tip bottom)`). Combínalo con la **Popover API** nativa (`popovertarget`/`popover`) = menús accesibles top-layer con Esc-dismiss, cero JS de posicionamiento. **Estado 2026:** Chrome 125+, Safari 26, Firefox 147+ (~91%, no Baseline universal) → fallback `@supports not (anchor-name: --x){ .tooltip{ position:absolute; bottom:100%; left:50%; transform:translateX(-50%) } }`.

## 4. @scope — estilos con scope sin BEM

Limita reglas a un subárbol y, con selector de límite, hace **donut-scoping** (estilas el contenedor excluyendo su interior anidado):
```css
@scope (.card) to (.card__media){ :scope{ border:1px solid currentColor; } p{ color:#cfe; } } /* no toca .card__media */
/* proximity: ante igual especificidad gana el scope-root más cercano en el DOM (resuelve temas anidados) */
@scope (.theme-dark){ a{ color:#8ef } } @scope (.theme-light){ a{ color:#06c } }
```
**Baseline en 2026.** Para tokens globales sigue siendo mejor `@layer` + variables, no `@scope`.

## 5. :has() — el selector padre

Selecciona según lo que contiene o según hermanos (lógica de estado y quantity queries puras en CSS):
```css
.card:has(img){ grid-template-columns:120px 1fr; }
.form:has(:invalid) button[type=submit]{ opacity:.5; pointer-events:none; }
html:has(#theme-toggle:checked){ color-scheme:dark; --bg:#04110d; }       /* theming sin JS */
.grid:has(> :nth-child(4)){ grid-template-columns:repeat(auto-fill, minmax(140px,1fr)); } /* quantity query */
.deck:has(.card:hover) .card:not(:hover){ opacity:.55; }                  /* spotlight de hover */
```
**Baseline desde 2023-24.** La herramienta que más JS de UI elimina hoy.

## 6. La frontera 2026

**Nesting nativo** (sin Sass; usa `&` por claridad). **Style queries** (`@container style(--tone: danger){ .badge__dot{ background:#ff4d4d } }` — variantes dirigidas por un token; Chrome/Edge 111+, Safari 18, Firefox aterrizando — no Baseline aún). **`if()`** (condicionales inline: `background: if(style(--tone: danger): #ff4d4d; else: #1affc4)` — lo más nuevo y frágil, Chrome 126/132+, siempre con valor de respaldo). **`@starting-style` + `transition-behavior: allow-discrete`** (anima entradas/salidas desde `display:none`/popover/top-layer — **Baseline ago-2024**, Chrome 117+/Safari 17.5+/Firefox 129+, seguro):
```css
.dialog{ opacity:1; transition:opacity .3s, display .3s allow-discrete; }
@starting-style{ .dialog{ opacity:0; } }
.dialog[hidden]{ opacity:0; display:none; }
```

## Frontier-CSS anti-patterns — blacklist
**animar custom props sin `@property`** (sin `syntax` tipado el navegador no interpola → saltos discretos) · **tratar Paint API como capa funcional** (Chromium-only; si el contenido legible/clicable depende de un `paint()` rompes Firefox/Safari; solo decoración + `@supports not`) · **anchor positioning sin fallback** (~91% no es 100%; sin `@supports not` el tooltip aparece en la esquina) · **`:has()` con selectores carísimos** (`:has(.x .y .z *)`) sobre miles de nodos (reflow) · **`@scope` con límites profundamente anidados** como reemplazo de arquitectura (usa `@layer` para tokens globales) · **confiar en `if()` o style queries como Baseline** (no lo son; nunca única fuente de un valor crítico) · **olvidar `allow-discrete`** en transiciones a `display:none` (la salida desaparece de golpe) · **worklets sin feature-detect** (`'paintWorklet' in CSS`) · **`@property` con `inherits:true` por defecto en props decorativas** (heredan por todo el árbol y rompen hijos; default `false`).
