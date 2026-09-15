# 172 — Data-viz & chart animation craft

**CRAFT, code-heavy.** La animación/interacción de charts (distinto de data-storytelling/64). Pareja de 64 (dataviz narrativa), 13 (dashboards), 156 (SVG anim), 162 (físico). Regla de oro: **anima la transición, no el reposo — la animación debe terminar en el frame que es exactamente el chart estático correcto; anima el dato, no el eje de forma confusa.**

## 1. Por qué animar (y cuándo NO)

La animación revela estructura (de dónde a dónde cambió un valor), dirige atención, crea *object constancy* (el ojo sigue un dato entre estados). Mal usada destruye comprensión (una barra que rebota oculta su valor, una transición de 2s entre filtros convierte un dashboard en parpadeo). **SÍ:** enter inicial (una vez), transición entre estados (filtro, rango temporal, toggle de serie). **NO:** cada re-render de streaming rápido (ruido), tooltips con delay, ni nada con `prefers-reduced-motion`. **Duración:** 600-1000ms enter, 300-500ms updates. **Easing:** `easeOut`/`cubic-bezier(0.22,1,0.36,1)`; nunca `easeInOut` largo (lento) ni `bounce`/`elastic` en datos (distorsiona el valor leído).

## 2. Catálogo de enter animations

**Barras desde la baseline** (el truco es `transform-origin`, no animar `height` que reflowea):
```css
.bar{ transform:scaleY(0); transform-origin:bottom; transition:transform .7s cubic-bezier(.22,1,.36,1); }
.bar.in{ transform:scaleY(1); } .bar{ transition-delay:calc(var(--i)*40ms); } /* stagger por índice */
```
**Line draw** (`stroke-dashoffset`, mide la longitud real): `path.attr('stroke-dasharray', \`${L} ${L}\`).attr('stroke-dashoffset', L).transition().duration(1400).attr('stroke-dashoffset', 0)`. **Area fill rise** (line-draw del borde + `clip-path`/`scaleY` o gradiente con `opacity` 0→1 tras el draw). **Pie/Donut sweep** (`attrTween('d', d=>{ const i=d3.interpolate({startAngle:0,endAngle:0}, d); return t=>arcGen(i(t)) })`). **Scatter stagger-in** (`r:0→r` + opacity, delay `index*8ms` capado a ~600ms total).

## 3. Transiciones entre estados (D3 enter/update/exit)

El núcleo. `data.join` separa los que entran/actualizan/salen, cada uno con su animación:
```js
svg.selectAll('rect').data(data, d => d.key)   // KEY FN = object constancy
  .join(
    enter => enter.append('rect').attr('height',0).call(e=>e.transition().duration(600).attr('height', d=>H-y(d.v))),
    update => update.call(u=>u.transition().duration(600).attr('y', d=>y(d.v)).attr('height', d=>H-y(d.v))),
    exit => exit.call(x=>x.transition().duration(300).attr('height',0).remove()));
```
La **key function** (`d=>d.key`) hace que un mismo dato se siga entre estados (sin ella la animación miente sobre qué se movió). Para **morphs de forma** (paths de distinto número de puntos) usa **flubber** (`interpolate(pathA, pathB)`). Al animar escala/eje: **anima los datos a su nueva posición, deja que el eje los acompañe** — nunca al revés.

## 4. Capa interactiva

**Crosshair + tooltip que sigue al cursor** (el patrón canónico: un `bisector` encuentra el dato más cercano en X sin loops):
```js
const bisect = d3.bisector(d=>d.date).left;
svg.on('pointermove', e=>{ const x0=xScale.invert(d3.pointer(e)[0]); const d=data[bisect(data, x0)];
  focusDot.attr('cx', xScale(d.date)).attr('cy', yScale(d.value));
  tip.style('transform', `translate(${xScale(d.date)}px,${yScale(d.value)}px)`).text(fmt(d.value)); });
```
Para scatter denso/mapas (vecino más cercano en 2D) usa **`d3.Delaunay`/voronoi** `find(mx,my)` (O(1) amortizado). El tooltip se posiciona con `transform:translate()` y **NO** debe tener transición de posición larga (lag perceptible); `transition:opacity .12s` para aparecer, posición instantánea. **Number readout** con `Intl.NumberFormat` + `font-variant-numeric:tabular-nums` (dígitos que no saltan de ancho). **Brushing** (`d3.brushX`) para focus+context.

## 5. Librerías & cuándo

| Lib | Render | Cuándo |
|---|---|---|
| **Recharts** | SVG | Default React. Animaciones de enter incluidas. Rápido; menos control fino. |
| **visx** | SVG | d3+React de bajo nivel. Control total, bundle disciplinado, más dev. |
| **D3** | SVG/Canvas | Control absoluto, enter/update/exit, morphs. Curva alta. |
| **Chart.js/ECharts** | Canvas | Datos densos, updates frecuentes, real-time. ECharts el más fuerte 2026. |
| **Observable Plot** | SVG | Grammar of graphics, EDA rápido. **No para animación** (estáticos). |

**SVG vs Canvas:** SVG hasta ~1-2k elementos (DOM por nodo = hover/aria/CSS gratis); por encima Canvas/WebGL. Si necesitas tooltip/aria por punto y son pocos → SVG; mapa de calor de 50k → Canvas.

## 6. Craft & performance

**GPU** (anima solo `transform`/`opacity`; animar `width/height/x/cx` SVG reflowea — para barras `scaleY`). **Reduced-motion** (muestra el estado final, no saltes el render; `will-change` solo durante la animación). **A11y** (tabla `<table>` oculta `.sr-only` como fallback, `role="img"` + `aria-label` con el resumen, nunca solo color → añade patrón/forma/etiqueta directa, respeta foco de teclado en el crosshair). **Polish caro:** stagger sutil (30-50ms), easing consistente en todo el dashboard, `tabular-nums`, gridlines que aparecen *antes* que los datos, tooltip con micro-fade pero posición instantánea, eje que no rebota.

## Chart-animation anti-patterns — blacklist
**animar el eje confusamente** (dominio Y y barras a la vez → el ojo no sabe qué se movió; snap del eje, anima los datos) · **bounce/elastic en valores** (una barra que sobrepasa su altura miente sobre el dato mid-flight) · **re-animar enter en cada update** de streaming (parpadeo; enter una vez, updates interpolan) · **sin key function** en D3 join (nodos reciclados al azar, historia falsa) · **tooltip con `transition` de posición larga** (laguea; posición instantánea, solo fade) · **duraciones >1.2s** en interacción · **loops de "nearest point" O(n)** en pointermove con miles de puntos (usa bisector/voronoi) · **ignorar `prefers-reduced-motion`** · **animar `height`/`width` SVG a alta N** en vez de `transform` · **color-only encoding** + animación (ilegible para daltónicos y en captura estática) · **stagger sin tope** (500 puntos × 40ms = 20s) · **Canvas para datos que necesitan hover/aria por punto a baja N** (reinventas accesibilidad que SVG da gratis).
