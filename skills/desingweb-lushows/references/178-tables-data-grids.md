# 178 — Tables, data grids & complex data display

**CRAFT, code-heavy.** El componente más denso de cualquier UI. Pareja de 13 (dashboards), 35 (componentes), 180 (estados), 16 (a11y). Regla de oro: **empieza con `<table>` semántico; baja a div-grid solo cuando virtualización o reflow lo fuercen (y entonces ARIA es obligatorio); números a la derecha con `tabular-nums`.**

## 1. Anatomía & cuándo (taxonomía)

| Tipo | Uso | Herramienta |
|---|---|---|
| Read-only list | mostrar registros | `<table>` plano |
| Sortable/filterable | dashboards, admin | TanStack Table (headless) |
| Editable grid | CRM, inventario, edición inline | TanStack + inline edit / MUI DataGrid |
| Analytical/spreadsheet | pivots, 100k+ filas | AG Grid (canvas) |

`<table>` semántico siempre que los datos sean tabulares (screen readers anuncian "fila 3 de 50, columna Precio"; `<th scope>` asocia). Solo cojea con virtualización extrema o reflow móvil → div-grid con `role="grid"`/`row"`/`gridcell"` reaplicando la semántica.

## 2. Interacciones core

**Sort** (single default; multi con `Shift+click` mostrando índice; indicador inequívoco ▲▼). **Filtering** (global search debounce 200-300ms + per-column + faceted con conteos). **Paginación** (saltar a páginas + total) **vs infinite scroll** (feeds, nunca datos accionables) **vs load-more**. **Row selection** (checkbox + select-all con estado **indeterminate** en parcial; `Shift+click` rango). **Column resize/reorder/show-hide** (persiste anchos en localStorage; menú de columnas esencial en tablas anchas).
```js
ref.current.indeterminate = selected.size > 0 && selected.size < rows.length;
```

## 3. Legibilidad & escaneabilidad

**Alignment:** texto izquierda, **números a la derecha** con `font-variant-numeric:tabular-nums` (columnas verticales perfectas). **Zebra vs borders vs whitespace:** whitespace (bordes horizontales tenues) lo más limpio; zebra en tablas muy anchas; gridlines completos solo en grids editables. **No combines zebra + bordes completos** (ruido). **Density modes** (compact 28-32px / comfortable 44-48px, togglable vía `data-density`). **Truncation + tooltip** (`text-overflow:ellipsis` + `title`). **Sticky header + sticky first column:**
```css
.table thead th{ position:sticky; top:0; z-index:2; background:#0c1410; }
.table .col-pin{ position:sticky; left:0; z-index:1; } .table thead .col-pin{ z-index:3; } /* esquina */
```

## 4. Performance a escala

**Virtualización (windowing):** a partir de ~1.000 filas renderiza solo las visibles + overscan. **TanStack Virtual** es el estándar headless 2026 (funciona con div-grid):
```jsx
const rv = useVirtualizer({ count: rows.length, getScrollElement:()=>parentRef.current, estimateSize:()=>40, overscan:8 });
rv.getVirtualItems().map(v => <div style={{ position:'absolute', transform:`translateY(${v.start}px)` }}>{/* rows[v.index] */}</div>)
```
**Server-side** para 50k+ (`?page=2&sort=price:desc&q=`). **Memoization** (`useMemo` columns, `React.memo` cell renderers, `getRowId` estable — un renderer no memoizado re-renderea N filas por keystroke). **Canvas-grid (AG Grid, ~330KB)** solo justificado con 100k+ filas, pivots server-side, range-select Excel.

## 5. Tablas responsive (el problema difícil)

**(a) Horizontal scroll + sticky first column** (menos disruptivo). **(b) Stacked cards / key-value collapse** (cada fila → card con label vía `data-label`):
```css
@media (max-width:640px){ .table thead{ display:none } .table tr{ display:block; border:1px solid; border-radius:10px }
  .table td{ display:flex; justify-content:space-between } .table td::before{ content:attr(data-label); font-weight:600 } }
```
**(c) Priority columns** (`data-priority` 1-6, ocultar progresivamente). **Filosofía: mobile-first** (comprimir hacia abajo es más difícil).

## 6. Edición & a11y

**Inline edit** (click-to-edit, save Enter/blur, cancel Esc revirtiendo, feedback saving/saved/error por celda). **Keyboard nav spreadsheet** (flechas mueven celda activa con roving tabindex —solo una con `tabIndex=0`—, Enter edita, Esc sale). **Bulk actions toolbar** (sticky al seleccionar). **ARIA** (`aria-sort` en headers; grids virtualizados `role="grid"` + `aria-rowcount` total real + `aria-rowindex` por fila). **Estados** (empty con CTA, loading con skeleton rows que imitan la estructura, error con retry — cada uno en `<tbody>`). **Librerías:** TanStack Table (headless ~15KB, default), MUI DataGrid (~120KB, si ya usas MUI), AG Grid (~330KB, enterprise).

## Data-table anti-patterns — blacklist
**números a la izquierda o sin `tabular-nums`** (imposible comparar) · **zebra + gridlines + bordes** (ruido) · **renderizar 10k `<tr>` sin virtualizar** (congela el thread) · **sort sin indicador o ambiguo** · **filtrar/ordenar en cliente sobre datos paginados en servidor** (solo la página visible — bug silencioso) · **truncar sin tooltip** · **infinite scroll en tablas accionables** (sin footer/total) · **header no sticky en tablas largas** · **div-grid sin `role`/ARIA** · **cell renderers sin memo** · **tabla vacía muda** sin empty/loading · **select-all sin `indeterminate`** · **horizontal scroll oculto** sin sticky first column · **AG Grid (330KB) para 200 filas** · **densidad fija** ignorando power-users.
