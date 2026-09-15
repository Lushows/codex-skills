# 175 — Drag, sortable & gestural interfaces

**CRAFT, code-heavy.** La capa de manipulación directa (distinto de physics/162: esto **mapea input a posición en tiempo real**). Pareja de 162 (físico/springs), 39 (interacción), 35 (componentes), 16 (a11y). Regla de oro: **una sola base correcta — Pointer Events (nunca mouse/touch por separado); `touch-action` es la CSS crítica; drag NUNCA es la única vía (siempre teclado + fallback).**

## 1. Pointer Events: la fundación

Un modelo unificado mouse + touch + pen (`mousedown/touchstart` están muertos: duplicabas listeners, peleabas con eventos sintéticos de 300ms, sin stylus). Tres reglas de oro:
```js
el.addEventListener('pointerdown', e=>{
  el.setPointerCapture(e.pointerId);   // 1. CAPTURA: todos los move/up llegan a ESTE elemento aunque el dedo salga
  startX=e.clientX; lastX=e.clientX; lastT=e.timeStamp; el.classList.add('is-dragging');
});
el.addEventListener('pointermove', e=>{ if(!el.hasPointerCapture(e.pointerId)) return;
  const dx=e.clientX-startX; const dt=e.timeStamp-lastT||16; vx=(e.clientX-lastX)/dt; // velocidad px/ms para throw/swipe
  lastX=e.clientX; lastT=e.timeStamp; el.style.transform=`translate3d(${dx}px,0,0)`; });
el.addEventListener('pointerup', e=>{ el.releasePointerCapture(e.pointerId); commitOrThrow(dx, vx); });
el.addEventListener('pointercancel', ()=>snapBack()); // el SO secuestró el gesto (llamada, gesture-nav)
```
**`touch-action` es la CSS crítica** (el error #1: sin ella el navegador hace scroll/zoom *al mismo tiempo* que tu gesto):
```css
.draggable{ touch-action:none; }       /* control total: ni scroll ni zoom */
.h-carousel{ touch-action:pan-y; }     /* yo manejo X, el navegador deja scroll vertical */
.swipe-to-close{ touch-action:pan-x; }
```
Declara el eje que **cedes** al navegador. También elimina el delay de 300ms y previene pull-to-refresh accidental. Combina con `user-select:none`.

## 2. Drag-and-drop: HTML5 DnD vs pointer-based

La **HTML5 DnD API** (`draggable="true"`, `dataTransfer`) sirve **solo para file-drop** (arrastrar archivos del escritorio); para UI interna es horrible (ghost no estilizable, no funciona en touch). Úsala únicamente para zonas de upload (`dropzone.addEventListener('drop', e=>{ e.preventDefault(); [...e.dataTransfer.files].forEach(handleFile) })`). Para todo lo demás → **pointer-based custom**, y en React el estándar 2026 es **dnd-kit** (`@dnd-kit/core` + `/sortable`, reemplazó a react-beautiful-dnd deprecado):
```jsx
const sensors = useSensors(
  useSensor(PointerSensor, { activationConstraint:{ distance:8 } }),  // 8px antes de activar → no roba clicks
  useSensor(KeyboardSensor, { coordinateGetter: sortableKeyboardCoordinates }));
<DndContext sensors={sensors} collisionDetection={closestCenter}
  onDragEnd={({active, over})=>{ if(over && active.id!==over.id) setItems(it=>arrayMove(it, it.indexOf(active.id), it.indexOf(over.id))); }}>
  <SortableContext items={items} strategy={verticalListSortingStrategy}>{...}</SortableContext>
  <DragOverlay>{active ? <li className="lift">{active}</li> : null}</DragOverlay>  {/* ghost fuera del flujo, sin clipping */}
</DndContext>
```
Claves: **`DragOverlay`** (renderiza fuera del flujo, evita clipping por `overflow:hidden`), **`activationConstraint.distance`** (distingue tap de drag), **auto-scroll** incluido cerca del borde.

## 3. Sortable lists & kanban con FLIP

Cuando un ítem se mueve, los demás deben **deslizarse al hueco**, no teletransportarse → **FLIP** (First, Last, Invert, Play). dnd-kit lo hace vía `transform`; vanilla con GSAP Flip o a mano:
```js
function flip(container, mutate){
  const items=[...container.children]; const first=new Map(items.map(el=>[el, el.getBoundingClientRect()])); // FIRST
  mutate();                                                                                                   // LAST
  items.forEach(el=>{ const last=el.getBoundingClientRect(); const dx=first.get(el).left-last.left, dy=first.get(el).top-last.top;
    el.animate([{ transform:`translate(${dx}px,${dy}px)` },{ transform:'none' }], { duration:220, easing:'cubic-bezier(.2,0,0,1)' }); });
}
```
**Placeholder/gap** (el origen queda como hueco fantasma + FLIP alrededor). **Insertion indicator** (línea de 2px de dónde caerá, obligatorio en árboles/tablas densas). **Kanban multi-columna** (cada columna droppable; al cruzar detectas `over.data.columnId`; persiste con `position` fraccional `(prev+next)/2`; **optimistic update** + rollback si la API falla; guarda en `onDragEnd`, no en cada move).

## 4. Swipe gestures

Swipe = drag de un eje + **decisión por umbral al soltar** (commit por distancia O por velocidad, lo que ocurra primero — un flick rápido y corto debe disparar):
```js
function commitOrThrow(dx, vx){
  const dismiss = Math.abs(dx) > el.offsetWidth*0.4 || Math.abs(vx) > 0.5;  // 40% del ancho O 0.5 px/ms
  if(dismiss){ el.animate([{ transform:`translateX(${Math.sign(dx)*innerWidth}px)`, opacity:0 }], { duration:200, fill:'forwards' }).onfinish = removeCard; }
  else { el.animate([{ transform:'translateX(0)' }], { duration:300, easing:'cubic-bezier(.2,.8,.2,1)' }); } // snap-back
}
```
Usos: swipe-to-dismiss (cards Tinder/toasts/notificaciones), swipe-between-views, carousel. **Rubber-band** en los extremos (resistencia exponencial: `pos > max ? max + (pos-max)*0.55 : pos`).

## 5. Gesture craft

**Drag handle vs whole-element** (handle —grip dots, `cursor:grab`— cuando el elemento tiene contenido interactivo; whole-element solo cards simples; dnd-kit: `{...listeners}` solo en el handle). **El "lift" al agarrar** (`scale(1.03)` + box-shadow + leve rotación = se despega de la superficie). **Cursores** (`grab` en reposo, `grabbing` en `.is-dragging`). **Inertia/throw** (al soltar con velocidad, decay `v *= 0.95` por frame). **Magnetic drop** (dentro de un radio del target el ghost se "imanta" al centro — drops más perdonadores). **Long-press to drag en touch** (un drag inmediato roba el scroll → `TouchSensor { activationConstraint:{ delay:200, tolerance:5 } }` + `navigator.vibrate(10)` al activar).

## 6. A11y — drag es el patrón #1 que falla accesibilidad

Un drag-only es **inaccesible por definición** (sin mouse no existe): **alternativa de teclado SIEMPRE** (Tab → `Space`/`Enter` para agarrar → flechas para mover → `Space` soltar, `Esc` cancelar; dnd-kit lo da gratis vía `KeyboardSensor` — *esa* es la razón de elegirlo), **anuncios a screen readers** (`aria-live="assertive"` "Movido item 2 a posición 4 de 6"; dnd-kit trae `announcements`), **focus management** (tras soltar el foco se queda en el ítem movido), **`prefers-reduced-motion`** (reorders instantáneos), **touch targets ≥44×44px**, **never drag-only** (fallback botones ↑↓/menú "mover a…"/campo de posición). **La pregunta crítica:** *¿el drag es necesario?* (para 4 ítems un `<select>` de posición es más rápido, accesible y testeable; reserva drag para cuando la **manipulación espacial es el valor** — kanban, builders, canvas).

## Drag/gesture anti-patterns — blacklist
**`mousedown`+`touchstart` por separado** en vez de Pointer Events · **olvidar `touch-action`** (scroll y gesto pelean; el drag "salta") · **no usar `setPointerCapture`** (el drag se cae al salir del elemento) · **HTML5 `draggable` para sortable/kanban** (roto en touch, ghost feo) · **activar con 0px de umbral** (roba clicks y selección de texto) · **drag inmediato en touch sin long-press** (secuestra el scroll) · **reordenar sin FLIP** (ítems que teletransportan) · **commit de swipe solo por distancia** (ignora velocidad; flicks rápidos no disparan) · **límites duros sin rubber-band** (se siente barato) · **drag-only sin teclado/ARIA/fallback** (inaccesible, falla WCAG 2.1) · **animar `top/left`** en vez de `transform` · **persistir el orden en cada `pointermove`** en vez de `onDragEnd` (flood a la API) · **perder el foco al `<body>`** tras soltar con teclado · **ignorar `pointercancel`** (estado colgado cuando el SO interrumpe).
