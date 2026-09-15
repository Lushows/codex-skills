# 189 — Calendars, date/time pickers & scheduling components

**CRAFT, code-heavy.** El component craft (distinto de booking-business/46). Pareja de 46 (booking/reservas), 21 (forms), 33 (i18n), 16 (a11y). Regla de oro: **el date picker es el input que más fracasa — antes de poner un calendario, pregúntate si lo necesitas (para fechas de nacimiento un typed segmentado DD/MM/AAAA gana); usa `<input type=date>` siempre que puedas (a11y + picker móvil gratis); el bug #1 del dominio es la timezone.**

## 1. Por qué son el input más difícil

Para fechas de nacimiento/vencimiento/lejanas, un calendario obliga a 30+ clics de prev/next → **typed input segmentado** gana siempre. Nativo vs custom:
```html
<input type="date" id="d" min="2026-06-05" max="2026-12-31" value="2026-06-20" required>
<!-- value/min/max SIEMPRE en ISO 8601 (YYYY-MM-DD); la UI se muestra en el locale automáticamente -->
```
`<input type="date">` da el spinner nativo iOS/Android (insuperable en móvil) + a11y completa. **Custom solo cuando necesites:** range, disponibilidad, marca obligatoria, multi-mes. En LatAm el nativo ya muestra DD/MM/AAAA — no reimplementes eso.

## 2. La grilla del calendario

Vista de mes = grilla 6×7 (6 filas para cualquier offset). El cálculo crítico es el padding inicial, **y el inicio de semana depende del locale** (lunes en ES/LatAm, domingo en US):
```js
function buildMonthGrid(year, month, weekStartsOn=1){
  const first=new Date(year,month,1), days=new Date(year,month+1,0).getDate();
  let lead=(first.getDay()-weekStartsOn+7)%7; const cells=[];
  for(let i=0;i<lead;i++) cells.push(null);
  for(let d=1;d<=days;d++) cells.push(new Date(year,month,d));
  while(cells.length%7) cells.push(null); return cells;
}
const dayName = new Intl.DateTimeFormat('es-CO',{weekday:'short'}); // NUNCA hardcodees "Lun,Mar"
```
Estados por celda: `today/selected/disabled/in-range/range-start/range-end/outside-month`. **Keyboard:** ←→ día, ↑↓ semana, PageUp/Down mes, Shift+PageUp/Down año, Home/End semana, Enter/Space seleccionar; foco por **roving tabindex** (una celda con `tabindex=0`; al cruzar el borde, navega al mes adyacente).

## 3. Selección de rango

**start → end con hover-preview** (al mover el mouse las celdas entre inicio y cursor se pintan tentativas):
```js
function onPick(day, s){ if(!s.start||s.end) return {start:day, end:null}; // reinicia
  return day < s.start ? {start:day, end:s.start} : {start:s.start, end:day}; }
```
**Vista de dos meses** lado a lado, **presets** (Hoy/Últimos 7 días/Este mes/90 días — cubren el 80%), botón **Clear**, texto del rango ("20 jun – 27 jun") encima.

## 4. Time & datetime

Tres patrones en orden de preferencia: **typed segmentado** (`HH:MM AM/PM`, el más rápido), **dropdown de slots** pre-generados (15/30 min, ideal scheduling), **scroll/wheel iOS** (móvil). Evita el dropdown de 1.440 minutos (usa `minuteStep`). El ciclo **12h/24h depende del locale** (`Intl.DateTimeFormat(...).resolvedOptions().hour12`). Para datetime, separa fecha y hora (no un control monstruoso).

## 5. Disponibilidad & scheduling (estilo Calendly)

Calendario a la izquierda (días con disponibilidad resaltados, resto grayed-disabled) + columna de **slots** a la derecha. El bug **#1 del dominio es la timezone:** **siempre muestra la zona activa** + selector (auto-detecta `Intl.DateTimeFormat().resolvedOptions().timeZone`); **almacena en UTC/Instant, convierte para mostrar**:
```js
const slotUTC = Temporal.Instant.from('2026-06-20T15:00:00Z');
const guestTZ = slotUTC.toZonedDateTimeISO('America/Bogota');  // 10:00 — muestra ambas si coordinas
```
Temporal maneja DST automáticamente (sumar "1 día" a un `ZonedDateTime` respeta el cambio horario — imposible de hacer bien con `Date`).

## 6. Craft, i18n & a11y

**Stack 2026:** **Temporal** alcanzó Stage 4 (mar-2026), Chrome 144/Node 26 sin flag — `Temporal.PlainDate`/`ZonedDateTime`/`Duration` reemplazan Moment/date-fns/Luxon. UI React: **react-aria `DatePicker`/`DateRangePicker`** (13 calendarios, RTL, validación incorporada, segmentos editables) o **react-day-picker**. Vanilla: nativo + `Intl`. **Formato/parse robusto:** nunca `new Date("20/06/2026")` (ambiguo); parsea ISO, formatea con `Intl` (`new Intl.DateTimeFormat('es-CO',{dateStyle:'medium'})` → "20 jun 2026"). **ARIA grid** (`role="grid"`/`row"`/`gridcell"` con `aria-selected`/`aria-disabled`; día con foco `tabindex=0`; `aria-label` completo). **En móvil el nativo casi siempre gana** (degrada a `<input type=date>`).

## Date-picker anti-patterns — blacklist
**forzar calendario para fechas de nacimiento** (usa typed DD/MM/AAAA) · **`new Date(string)` con formato no-ISO** (ambiguo entre motores) · **hardcodear MM/DD/YYYY o inicio de semana en domingo** (rompe LatAm/EU; usa `Intl`+locale) · **no mostrar la timezone** en scheduling (el bug #1) · **almacenar hora local en vez de UTC/Instant** (corrompe conversión cross-tz y DST) · **dropdown de 1.440 minutos** o de 100+ años sin salto rápido · **sin navegación por teclado en la grilla** · **reimplementar el picker móvil** en vez de degradar al nativo · **permitir seleccionar fechas disabled** sin feedback · **no permitir typed-fallback** · **cerrar el popover al elegir start** en un range picker · **animaciones de cambio de mes sin `prefers-reduced-motion`**.
