# 329 · Dashboards y data-viz (jerarquía, librería correcta, tiempo real)

> Un dashboard no es "meter todos los gráficos en una grid". Es responder UNA pregunta por vista,
> en orden de importancia, con el chart que el dato pide — no el que se ve bonito.

## Jerarquía: el dashboard responde una pregunta
- **Pregunta primero**: ¿qué decisión toma quien lo mira? El layout sirve a esa decisión.
- **F-pattern / inverted pyramid**: lo más importante arriba-izquierda. KPIs/scorecards en la fila 1
  (número grande + delta vs periodo previo + sparkline). Detalle y tablas, abajo.
- **5-second test**: el insight clave debe leerse en 5s. Si hay que estudiarlo, falló la jerarquía.
- **Una métrica, un foco**: no compitan 8 gráficos por atención. Agrupa por tema, usa whitespace.
- Filtros globales (rango de fecha, segmento) arriba y **sticky**; afectan todo el dashboard.

## Elegir el chart por el dato (no al revés)
| Pregunta | Chart |
|---|---|
| Tendencia en el tiempo | Línea / área |
| Comparar categorías | Barras (horizontal si labels largos) |
| Composición / parte-todo | Stacked bar, treemap (NO pie con >4 slices) |
| Correlación | Scatter |
| Un número clave | Scorecard / big number + delta |
| Distribución | Histograma, box plot |
| Progreso a meta | Gauge/bullet (con moderación) |
| Densidad temporal | Heatmap |

Evita: pie con muchas tajadas, ejes Y truncados que exageran, dual-axis engañoso, 3D, donut decorativo.

## Librería React (2026) — elegir por necesidad
| Librería | Cuándo | Notas |
|---|---|---|
| **Recharts v3** | Default pragmático, API por componentes simple | ~2.4M descargas/sem; el estándar de facto [verificado 2026] |
| **Tremor** | Dashboard SaaS rápido, estética shadcn out-of-the-box | Componentes pre-estilados Tailwind; ship veloz [verificado 2026] |
| **visx** (Airbnb) | Viz custom, widget embebido, cada KB cuenta | Primitivas low-level sobre D3; máximo control, más código |
| **Nivo** | Data-heavy, SSR, complejidad visual | Bueno para server-render |
| **ECharts/AG Charts** | Volumen masivo de puntos, canvas/WebGL | Cuando SVG no rinde |

Regla: SVG (Recharts/visx) hasta ~1-2k puntos; canvas/WebGL (ECharts, uPlot) para series grandes o realtime.

## Tiempo real sin matar el navegador
- Transporte: **SSE** para push unidireccional (lo común en dashboards), WebSocket si hay bidireccional.
- **No re-render por cada tick**: bufferiza y aplica en batch con `requestAnimationFrame` o throttle.
- Ventana deslizante: mantén N puntos en memoria, descarta viejos; no acumules infinito.
- Canvas/WebGL para alta frecuencia; SVG repinta DOM y se ahoga.
- Optimistic + skeleton mientras carga; nunca layout shift al llegar datos.

## UX y rendimiento
- **Skeleton loaders** con la forma del chart, no spinners genéricos. Empty states con CTA, no "sin datos".
- Tooltips con el dato exacto al hover; leyenda clicable para aislar series.
- Color con propósito: paleta de tokens (ver [[88-design-systems-tokens]]), secuencial para magnitud,
  categórica para grupos; verde/rojo NUNCA como único canal (daltonismo → ver [[331-accessibility-deep]]).
- Responsive: en móvil colapsa a 1 columna, prioriza KPIs, oculta tablas anchas tras tab.
- Accesibilidad: `<table>` alternativa o `aria-label` con resumen; el chart SVG necesita texto equivalente.

Cruza con [[88-design-systems-tokens]] y [[346-dashboards-bi]].
