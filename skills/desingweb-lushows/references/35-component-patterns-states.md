# 35 — Catálogo maestro de componentes & estados (la "biblia")

Referencia para diseñar cada componente bien y cubrir TODOS sus estados. Validado contra **ARIA APG**, **Radix/shadcn**, Material 3, Carbon, NN/g. **Léelo al construir cualquier componente de UI.** Pareja de 13 (app UI), 15 (tokens/estados), 16 (a11y).

## 0. La MATRIZ DE ESTADOS UNIVERSAL (regla de oro)

Todo componente interactivo se ve "amateur" cuando salta estados (el 90% de las UIs de IA solo diseñan `default`). Checklist obligatorio:

| Estado | Cuándo | Nota crítica |
|---|---|---|
| **default** | reposo | el punto de partida, no el único |
| **hover** | puntero encima | solo desktop; nunca info esencial solo en hover (no existe en touch) |
| **focus-visible** | teclado | usa `:focus-visible` NO `:focus`; ring ≥2px, contraste ≥3:1 (WCAG 1.4.11); nunca `outline:none` sin reemplazo |
| **active/pressed** | al presionar | feedback <100ms (scale/translate sutil) |
| **disabled** | no disponible | `aria-disabled` (mejor que `disabled` puro para tooltip/foco); explica POR QUÉ |
| **loading** | async | bloquea doble-submit, spinner inline, **mantén el ancho** |
| **error/invalid** | validación falla | `aria-invalid` + mensaje `aria-describedby`; nunca solo color |
| **empty** | sin datos | empty state diseñado, no blanco |
| **selected/checked** | elegido | `aria-selected`/`aria-checked`/`aria-current` |
| **dragging** | reordenando | cursor grabbing, ghost/placeholder, anuncio a SR |
| **filled** | input con valor | distingue de placeholder (afecta floating labels) |

**Cross-cutting:** touch targets ≥44×44px / 48dp + ≥8px separación · densidad compact/comfortable/spacious en data-heavy · motion en cambio de estado 150-250ms ease-out + `prefers-reduced-motion`. **Radix/shadcn exponen estados como data-attributes** (`data-state="open|checked"`, `data-disabled`, `data-highlighted`) → estílalos en Tailwind con `data-[state=open]:...` (la forma idiomática 2026).

## 1. Navegación
- **Navbar/header:** default, **scrolled** (sticky compacto + shadow/blur), **transparent-on-hero** (invierte a sólido al scroll, cuida contraste en ambos), mobile (hamburguesa→drawer). `<header><nav aria-label="Main">` + skip link. *Mistake:* header transparente con texto ilegible sobre fotos claras.
- **Mega-menu:** es navegación, **NO `role="menu"`** (APG: menu role es para apps). Disclosure pattern, abre con hover **y** focus/click, cierra con Esc, "safe triangle" para el hover diagonal.
- **Breadcrumbs:** `<nav aria-label="Breadcrumb"><ol>`, último `aria-current="page"` sin link. Colapsa el medio en mobile.
- **Tabs (APG):** `role="tablist/tab/tabpanel"`, **flechas** entre tabs, `Tab` salta al panel. *Mistake:* tabs para flujo secuencial (eso es stepper) o >7 secciones.
- **Pagination:** current `aria-current="page"`, disabled (prev en pág.1). Alternativas: Load more > infinite scroll.
- **Sidebar:** expanded/collapsed (rail con iconos), item active, grupos colapsables (shadcn `Sidebar`).
- **Bottom-nav:** 3-5 destinos, activo con label + icono relleno, `safe-area-inset-bottom`. Solo navegación, no acciones.
- **Command palette (⌘K):** empty/typing/results/highlighted/loading/no-results; combobox + `aria-activedescendant` (shadcn `Command`/cmdk).

## 2. Overlays & disclosure
- **Modal/Dialog:** **focus trap** + foco inicial + retorno al trigger + Esc + scroll-lock. `<dialog>`+`showModal()` (top-layer/inert gratis) o Radix. `role="dialog" aria-modal aria-labelledby`. *Mistake:* modales encadenados; modal para algo que cabía inline.
- **Drawer/Sheet:** side (filtros/detalle) o **bottom sheet** (acciones móviles, drag-handle + snap). Reglas de focus = modal (Radix/Vaul).
- **Popover:** contenido rico/interactivo (vs tooltip). Floating UI (flip/shift), click-outside + Esc, `aria-haspopup`.
- **Tooltip:** solo texto breve. Hover **y focus**, persiste al viajar hacia él, Esc lo descarta (WCAG 1.4.13). *Mistake:* meter interactivos (eso es popover); única fuente de info crítica; tooltip en touch.
- **Dropdown menu:** lista de **acciones** (APG menu: flechas, Enter/Space, Esc, typeahead). NO confundir con `<select>`.
- **Accordion/Disclosure:** simple = `<details>/<summary>`; APG = `<button aria-expanded aria-controls>`. *Mistake:* esconder contenido SEO/crítico en desktop sin necesidad.
- **Toast/Snackbar:** efímero no-bloqueante, auto-dismiss 4-6s (pausa en hover), apila máx 3, `role="status"`/`role="alert"` (Sonner). *Mistake:* toast para errores accionables.
- **Cuándo cuál:** bloquea→Modal · lateral sin perder contexto→Drawer · info al pasar→Tooltip · interactivo flotante→Popover · lista de acciones→Menu · confirmación pasiva→Toast.

## 3. Forms & inputs
Estados de TODO input: default/hover/focus(-visible)/filled/error/disabled/loading. Label SIEMPRE visible y asociado; placeholder ≠ label.
- **Text/Textarea:** `field-sizing:content` (auto-grow), contador si hay límite, `inputmode`/`type` correctos.
- **Select/Combobox:** `<select>` nativo para listas cortas (mejor móvil); **combobox** (APG) con búsqueda (`aria-activedescendant`, loading async).
- **Multiselect:** combobox + chips removibles + "+3 more".
- **Checkbox/Radio:** checkbox múltiple, radio exclusivo (mín 2); estado **indeterminate** (padre); label clickable; `aria-checked`.
- **Toggle/Switch:** efecto **inmediato** (sin submit), `role="switch" aria-checked`. *Mistake:* switch que necesita "Guardar" → usa checkbox.
- **Slider:** `role="slider" aria-valuemin/max/now`, flechas+Home/End, thumb ≥44px.
- **Date picker:** permite **entrada por texto** + calendario grid (APG). Móvil: `type="date"` nativo gana.
- **File upload:** drag-zone + botón; idle/**drag-over**/uploading(%)/success/error; preview + remove; valida client+server.
- **Search:** lupa + clear (×) + debounce + loading + sugerencias (combobox) + empty.
- **OTP:** cajas segmentadas, auto-advance, paste reparte, `inputmode="numeric"` + `autocomplete="one-time-code"` (shadcn `InputOTP`).
- **Segmented control:** 2-5 exclusivas visibles + indicador animado. **Rating:** estrellas hover-preview, flechas, readonly para mostrar.

## 4. Data display
- **Table/Data-grid:** header sortable (`aria-sort`), sticky header/col, row hover/selected, loading (**skeleton rows**), empty, error. Responsive: cards o scroll horizontal + col fija (TanStack Table). `<table>` semántico para tablas reales.
- **Card:** una sola acción primaria si toda es clickable (no anides interactivos → "nested interactive"). hover (lift), focus-within, selected. Jerarquía: media→título→meta→acciones.
- **List:** hover/selected/focus por ítem; virtualiza largas.
- **Stat/KPI:** número grande + label + delta (▲▼ con color **y** signo/icono) + sparkline; loading=skeleton.
- **Badge/Tag/Chip:** badge=estado/conteo (no interactivo); chip=interactivo (filtro/removible). Color + texto/icono (daltonismo), contraste ≥4.5:1.
- **Avatar:** imagen→iniciales→icono, `alt` con nombre, "+N", status dot con label, maneja imagen rota.
- **Progress:** determinado (`role="progressbar" aria-valuenow`) vs indeterminado; pasos→stepper.
- **Skeleton:** imita el layout final (evita CLS), `aria-busy`.
- **Empty state:** ilustración + título + explicación + **CTA**; diferencia 1ª vez / sin resultados / error.
- **Timeline / Tree (APG):** tree `role="tree/treeitem"`, flechas, `aria-expanded`, `aria-level`.

## 5. Actions & feedback
- **Button (el más maltratado):** variantes **primary** (1 por vista/sección), secondary, ghost, **destructive** (rojo + confirmación), **icon** (requiere `aria-label`). Estados COMPLETOS incl. **loading** (spinner + mantén ancho + deshabilita + "Saving…"). Tamaños con touch ≥44px, `<button type>` correcto. *Mistake:* sin loading (doble submit); icon sin label; >1 primary compitiendo.
- **Button group / FAB:** group con foco individual; FAB 1 por pantalla, safe-area, `aria-label`.
- **Link:** navega (vs button=acción), señal ≠ solo color, external con icono + `rel="noopener"`. *Mistake:* `<div onclick>` (rompe teclado/SR).
- **Spinner vs Skeleton (decisión 2026):** **Skeleton** cuando conoces la estructura que llega (listas/cards/tablas/1ª carga) → menos CLS y ansiedad; **spinner** para acciones puntuales/indeterminadas en botón o región pequeña, esperas <1s; >10s → progress + mensaje; optimistic cuando el éxito es casi seguro.
- **Alert/Banner:** persistente contextual (no efímero), info/success/warning/error con icono+color+texto, `role="alert"` (urgente) vs `role="status"`. *Mistake:* banner que tapa contenido sin cerrar.
- **Inline validation:** **on blur** (no en cada tecla), revalida on-change tras error, mensaje específico junto al campo + `aria-describedby`/`aria-invalid`, resumen arriba en submit con foco al primero.
- **Confirmation:** destructivo → AlertDialog (`role="alertdialog"`) con verbo claro ("Delete 3 items"); reversible → ejecuta + toast con **Undo** (mejor que confirmar todo).

## 6. Component anti-patterns — blacklist
diseñar solo el `default` (delator #1) · `outline:none` sin reemplazo · `:focus` en vez de `:focus-visible` · color como único indicador · botón sin loading (doble-submit) · placeholder como label · tooltip con contenido esencial/interactivo · `<div onclick>` como botón · nested interactive (botón dentro de card-link) · hover-only para menús · modal sin focus trap/retorno/Esc · layout shift al pasar a loading/error · toast para errores accionables · touch targets <44px · `role="menu"` para nav links · switch que requiere "Guardar" · disabled sin explicar por qué · ignorar `prefers-reduced-motion`.

## Cierre
No inventes patrones: tabs/accordion/dialog/combobox/menu/tree están resueltos en **APG** — cópialos. **Radix/Base UI** dan comportamiento+a11y headless; **shadcn** los estiliza con `data-state` (ojo: su `ring` por defecto suele fallar el 3:1 — súbelo). Un componente está **terminado solo cuando todos los estados de su fila están diseñados.**
