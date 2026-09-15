# 09 · Reportes hermosos y organizados

> Los reportes de AVIS deben verse **premium, claros y on-brand (COBALTO)** — que el comerciante
> entienda su plata en 3 segundos. Profundidad en `desingweb_lushows/skill/references/`:
> `13-dashboards-saas-dataviz.md` (el nervio), `43-fintech-financial-trading.md` (dinero/COP),
> `64-data-storytelling-dataviz-narrative.md` (contar con datos), `45-editorial-content-reading.md`,
> `10-art-direction-pro.md`; y `directorcreativo_lushows/references/` 30-34 (color) + 40-49 (tipografía).
> Identidad: ver `[[project_avispao_brand_identity]]` (COBALTO #2742F5).

## Las reglas (en orden de importancia)
1. **Un número protagonista arriba.** Lo que el comerciante NECESITA ver (gasto del mes, total, IVA)
   en grande (clamp ~28-40px), **mono + `tabular-nums`**, color COBALTO. Debajo, el contexto (delta
   vs mes anterior con **flecha + signo + color**, nunca solo color).
2. **Orden accionable, no cronológico:** ① KPI protagonista + delta · ② breakdown por categoría
   (¿en qué se fue?) · ③ tendencia (últimos 3-6 meses) · ④ detalle/lista (denso, abajo) · ⑤ acciones.
3. **Máx 3-4 secciones.** Si hay más, son varios reportes.
4. **Respira:** whitespace generoso entre secciones, cards con **hairline 1px** (no sombras pesadas;
   elevación por luz), fondo crema (#F9FAFB), no blanco puro vibrando con el cobalto.
5. **Un insight gritado:** si una categoría sube/baja >10%, un chip "⬆ Aseo +12%" con 1 línea de
   por qué. El comerciante no analiza; necesita la anomalía señalada.

## Cómo presentar los gastos para entenderlos de un vistazo
- **KPI card:** etiqueta gris en mono mayúscula 11px → número COBALTO grande tabular → delta abajo.
- **Breakdown:** barra horizontal apilada (máx 5-6 categorías), monto exacto alineado a la derecha,
  etiqueta sobre la barra. **Nunca pie con >4 segmentos.**
- **Tendencia:** línea suave de últimos meses + línea sutil de meta/presupuesto. Una serie destacada
  en COBALTO, el resto gris atenuado.
- **Lista de top gastos:** tabla densa OK pero abajo; `tabular-nums`, alineación derecha, hairlines,
  +/− con color **y** signo.
- **Plata en COP:** `Intl.NumberFormat('es-CO')` → `$2.450.000`. Sin centavos en montos grandes.

## Tipografía y color (anti-genérico)
- **Display/texto:** Schibsted Grotesk (700 títulos, 400/500 cuerpo). **Números:** Geist Mono 500
  con `tabular-nums` SIEMPRE (que no "bailen").
- **Color:** COBALTO #2742F5 protagonista; verde #10B981 / rojo #EF4444 semánticos; grises cálidos.
  Fondo cards: cobalto al ~8% (`rgba(39,66,245,.08)`), sutil. **Nada de gradientes arcoíris ni
  sombras pesadas** (eso grita "plantilla genérica/AI-slop").
- **Accesibilidad:** +/− nunca solo por color → siempre flecha + signo.

## Estructura del "Reporte mensual de gastos" (orden exacto)
1. **Encabezado:** "Gastos de junio" + **$total** + delta vs mes anterior.
2. **¿En qué se fue?** breakdown por categoría (barras).
3. **Tendencia:** últimos 6 meses + meta.
4. **Top gastos del mes:** lista con proveedor, monto, fecha, categoría.
5. **El consejo de AVIS:** 1-2 líneas amables (ver `08-consejero-de-gastos`) — el insight que importa.
6. **Acciones:** Exportar CSV (para el contador), ver detalle.

> El reporte por WhatsApp es la versión corta (texto: total, IVA, top categorías + link); el reporte
> hermoso vive en el **panel** (`/panel/facturas`) y en **PDF** (chrome `--headless=new --print-to-pdf`,
> mismo lenguaje COBALTO que la guía de Gmail). Reusa los componentes del panel ya existentes.
