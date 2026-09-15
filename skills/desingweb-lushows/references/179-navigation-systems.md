# 179 — Navigation systems (mega menu, mobile, breadcrumb, command bar)

**CRAFT, code-heavy.** La IA hecha visible (distinto de search/28). Pareja de 28 (search/filtros), 183 (IA), 186 (overlays), 16 (a11y). Regla de oro: **la nav refleja la arquitectura de información; el mito 7±2 no aplica a nav visible (la escaneas, no la memorizas) — el límite real es densidad/escaneo; usa el vocabulario del usuario, no el organigrama.**

## 1. Nav = IA hecha visible

Define los top-level por *jobs-to-be-done*, no por organigrama. Tipos: top bar (marketing, ≤7 secciones), sidebar (apps con jerarquía), bottom nav (mobile, 3-5 destinos), mega menu (catálogo amplio), command bar ⌘K (power-users, *complementa*). Labeling: vocabulario del usuario ("Precios", no "Commercial Tiers"), front-load la palabra distintiva.

## 2. Desktop nav

Dropdown si ≤7 hijos planos; **mega menu** cuando el contenido es amplio y categorizable en columnas. **El "diagonal problem"** (el cursor viaja en diagonal, sale del área activa, el menú colapsa — Baymard: 60% de sites fallan): solución **hover delay 300-500ms** (open Y close), o **triangle hit-area** (Amazon), o **click activation** (elimina el problema, mejor para touch):
```js
let openT, closeT;
function bind(trigger, panel){
  const open = ()=>{ clearTimeout(closeT); openT=setTimeout(()=>panel.dataset.open="true", 120); };
  const close = ()=>{ clearTimeout(openT); closeT=setTimeout(()=>panel.dataset.open="false", 280); };
  [trigger,panel].forEach(el=>{ el.addEventListener("pointerenter",open); el.addEventListener("pointerleave",close); });
}
```
```css
.mega::before{ content:""; position:absolute; top:-12px; inset-inline:0; height:12px; } /* hover bridge */
```
**Sticky/condense + hide-on-down/show-on-up** (2026: CSS scroll-driven o JS con umbral >80px + dirección):
```js
let lastY=0; addEventListener("scroll",()=>{ const y=scrollY;
  document.documentElement.dataset.scroll = y>lastY && y>80 ? "down":"up"; lastY=y; }, {passive:true});
```
```css
[data-scroll="down"] header{ translate:0 -100% } [data-scroll="up"] header{ translate:0 0 } header{ transition:translate .25s }
```
**Active state** con peso/underline + `aria-current="page"` (no solo color).

## 3. Mobile nav (la parte difícil)

**Hamburger** esconde TODO tras un tap (reduce engagement) → solo jerarquías complejas o nav secundaria. **Bottom tab bar (3-5 destinos)** = estándar (~49% navega con el pulgar, thumb-zone; Airbnb: switch a tab bar → 40% más rápido). Para >5: 4 tabs + "More":
```css
.tabbar{ position:fixed; inset-inline:0; bottom:0; display:flex; justify-content:space-around;
  padding-bottom:env(safe-area-inset-bottom); }    /* notch/home-bar iOS */
.tabbar a{ min-height:48px; min-width:48px } .tabbar a[aria-current="page"]{ color:var(--accent) }
```
**Full-screen overlay** (marketing) **vs slide-in drawer** (apps) — ambos requieren focus trap + Esc + tap-outside + restaurar foco.

## 4. Wayfinding ("you are here")

**Breadcrumbs** en jerarquías profundas (e-commerce/docs), NO en sites planos; último item sin link; emite **schema.org BreadcrumbList** (rich results). **Skip link** obligatorio (`.skip-link{ position:absolute; left:-999px } .skip-link:focus{ left:1rem; top:1rem }`). **Back behavior** (no rompas el botón "atrás" en SPA; en mobile "atrás" sale del drawer no de la página).

## 5. Command bar / ⌘K (2026)

La **fast lane** que coexiste con la nav visual (navegación + acciones + search en un input). Estándar: `cmdk` (Linear/Vercel/Raycast). ⌘K abre, Esc cierra, ↑↓ navega, Enter ejecuta:
```jsx
<Command.Dialog open={open} onOpenChange={setOpen}>
  <Command.Input placeholder="Buscar o ir a..." autoFocus />
  <Command.List><Command.Empty>Sin resultados.</Command.Empty>
    <Command.Group heading="Navegar"><Command.Item onSelect={()=>nav("/orders")}>Pedidos</Command.Item></Command.Group>
  </Command.List></Command.Dialog>
```
Muestra el atajo junto a cada item (enseña el camino rápido). Siempre complemento, nunca el único acceso.

## 6. A11y & craft

**Landmark** `<nav aria-label="Primary">` (label único por nav). **Disclosure** (`aria-expanded`/`aria-controls`/`aria-haspopup`; trigger es `<button>` no `<div>`). **Teclado** (Tab; en menubar flechas; Esc cierra y devuelve foco al trigger). **Focus trap** en overlay/drawer mobile (guardar y restaurar `document.activeElement`). **`:focus-visible`**. **`aria-current="page"`**. **`prefers-reduced-motion`**. Mega-menu: cada columna es `<ul>`; no atrapes foco en hover-menus de desktop (solo overlay mobile).

## Navigation anti-patterns — blacklist
**hover menus sin delay** (flickering, ignora el diagonal problem) · **hamburger en desktop** con espacio de sobra · **hamburger para 3-5 destinos en mobile** (pierde 30-50% de discovery vs bottom tabs) · **active state solo por color** (sin `aria-current`) · **`<div onclick>` como trigger** (no accesible) · **sin Esc/sin restaurar foco** al cerrar overlay · **touch targets <44px** o tabs sin `safe-area-inset` · **nav que reaparece en cada micro-scroll** (jittery; umbral >80px) · **anidar >2-3 niveles** en dropdowns · **⌘K como único acceso** · **breadcrumbs en sites planos** · **mega menú sin columnas/agrupación** (pared de links) · **sin skip-link** · **sticky header gigante** que tapa anclas (usa `scroll-margin-top`) · **romper el botón "atrás"** en SPA.
