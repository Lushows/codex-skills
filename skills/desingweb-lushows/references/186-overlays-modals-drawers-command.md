# 186 — Overlays: modals, drawers, popovers, sheets, command palettes

**CRAFT, code-heavy.** La familia de overlays. Pareja de 35 (componentes), 171 (Popover API/anchor), 175 (gestos/bottom sheet), 16 (a11y). Regla de oro: **un overlay roba contexto — pregúntate "¿necesito un overlay?" (contenido principal/largo/linkeable → full-page route gana); usa `<dialog>` nativo + top-layer, olvida el `z-index:9999`; un modal por vez.**

## 1. La familia & cuándo

| Tipo | Cuándo | Bloquea | Dismiss |
|---|---|---|---|
| **Modal dialog** | tarea enfocada que exige decisión | Sí (top-layer + backdrop) | Esc, backdrop, botón |
| **Drawer/side panel** | contexto secundario que persiste (filtros, carrito) | Opcional | Swipe, botón, Esc |
| **Bottom sheet** | mobile, acciones al alcance del pulgar | Opcional | Drag-down, backdrop |
| **Popover/dropdown** | menú contextual ligero anclado | No (light dismiss) | Click-fuera, Esc |
| **Command palette** | navegación + acciones power-user | Sí (foco) | Esc, ejecución |

Si el contenido es la tarea principal, persiste o requiere scroll largo (form de 8 campos, checkout) → **full-page route** (linkeable, con historial, sobrevive refresh). **Un modal por vez** (apilar = flujo mal diseñado → wizard de pasos).

## 2. `<dialog>` nativo (la forma de 2026)

Da gratis: top-layer (sin guerra de z-index), `::backdrop`, focus trap, Esc-to-close, `inert` del fondo:
```html
<dialog id="dlg" closedby="any" aria-labelledby="t">
  <form method="dialog"><h2 id="t">Confirmar</h2><menu>
    <button value="cancel">Cancelar</button><button value="confirm" autofocus>Eliminar</button></menu></form>
</dialog>
```
```js
dlg.showModal();   // modal (top-layer+backdrop+trap); show() = non-modal
dlg.addEventListener('close', ()=>{ if(dlg.returnValue==='confirm') doDelete(); }); // form method=dialog setea returnValue
```
**`closedby`** (`"any"` light dismiss, `"closerequest"` solo Esc, `"none"` programático) elimina el hack de backdrop-click. **Animate-in con `@starting-style` + `allow-discrete`** (Baseline):
```css
dialog{ opacity:0; transform:translateY(8px) scale(.97); transition:opacity .25s, transform .25s, overlay .25s allow-discrete, display .25s allow-discrete; }
dialog[open]{ opacity:1; transform:none; } @starting-style{ dialog[open]{ opacity:0; transform:translateY(8px) scale(.97); } }
dialog[open]::backdrop{ background:rgb(0 0 0/.55); backdrop-filter:blur(4px); }
```
**Popover API** (`popover`/`popovertarget`) para dismiss ligero (menús/popovers), declarativo, light-dismiss + top-layer; combina con **Anchor Positioning** (`anchor()`).

## 3. Bottom sheets & drawers

**Bottom sheet** (drag handle, snap points, drag-to-dismiss, `env(safe-area-inset-bottom)`):
```js
sheet.addEventListener('pointermove', e=>{ if(!startY) return; dy=Math.max(0, e.clientY-startY); sheet.style.transform=`translateY(${dy}px)`; });
sheet.addEventListener('pointerup', ()=>{ if(dy>120) closeSheet(); else sheet.style.transform='translateY(0)'; });
```
**Drawer lateral** (`translateX(-100%)→0`): decide **push** (empuja el contenido) vs **overlay** (flota con backdrop). Drawers de nav persistente → push en desktop, overlay en mobile. Evita anidados/multinivel.

## 4. Command palette (cmdk / ⌘K)

Power-nav (navegación + acciones). `⌘K` abre, fuzzy search, grupos, recientes, 100% teclado:
```jsx
<Command.Dialog open={open} onOpenChange={setOpen}>
  <Command.Input placeholder="Buscar o ejecutar…" autoFocus />
  <Command.List><Command.Empty>Sin resultados.</Command.Empty>
    <Command.Group heading="Acciones"><Command.Item onSelect={createOrder}>Crear pedido <kbd>C</kbd></Command.Item></Command.Group>
  </Command.List></Command.Dialog>
```
cmdk maneja fuzzy + flechas + `aria-selected`. Craft: empty con sugerencia, loading sin saltos, mostrar `kbd`, recientes arriba con input vacío.

## 5. Foco & dismissal (el núcleo de a11y)

Custom debe implementar todo (el `<dialog>` nativo lo resuelve): **focus trap** (foco entra, Tab cicla, **vuelve al trigger** al cerrar — guarda `document.activeElement`), **foco inicial correcto** (`autofocus` al primer campo o título, **NO** al botón destructivo), **dismiss** (Esc en no-destructivos, backdrop-click, "X" siempre visible; en irreversibles NO cierres con click-fuera accidental), **scroll-lock del body** (mide el ancho del scrollbar para evitar shift), **ARIA** (`role="dialog"`/`alertdialog`, `aria-modal="true"`, `aria-labelledby`), **`inert`** en el fondo.

## 6. Craft, motion & stacking

**Coreografía:** modal = `scale(.97)+fade` (aparece desde el centro), drawer/sheet = `slide` desde el borde (modelo espacial); 200-300ms, easing `cubic-bezier(.32,.72,0,1)` para sheets; la salida debe animar también (`allow-discrete`). **Backdrop** dim + `backdrop-filter:blur(4px)` (no abuses del blur en mobile). **Stacking/top-layer** (usa `<dialog>`/Popover, olvida el z-index; nunca apiles 3). **Responsive: modal→sheet** (mismo contenido, modal centrado en desktop, bottom sheet en mobile, solo cambia el CSS). **`prefers-reduced-motion`** (fade corto). **No atrapar** ("X"/Esc siempre disponibles).

## Overlay anti-patterns — blacklist
**`div` custom con `z-index:99999`** en vez de `<dialog>`/top-layer · **apilar modal sobre modal** (usa wizard) · **overlay para contenido largo/linkeable** que debería ser route · **enfocar el botón destructivo** por defecto · **olvidar devolver el foco** al trigger · **no bloquear el scroll del body** · **layout shift** al abrir por no compensar el scrollbar · **modal sin "X" ni Esc** (usuario atrapado) · **tooltip con contenido interactivo** (debe ser popover) · **bottom sheet sin `safe-area-inset`** · **backdrop-click que descarta un form a medio llenar** sin confirmar · **animación de entrada sin salida** (corte brusco) · **ignorar `prefers-reduced-motion`** · **múltiples popovers `manual`** que no se cierran entre sí.
