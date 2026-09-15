# 32 · Inteligencia de gastos

> AVIS no solo guarda facturas: las **lee como un analista** y saca insights accionables. Fuentes: `04-facturas-dian-cruce` (cruce, categorías, fuente xml/visión), `08-consejero-de-gastos` (tono amigo, ratios), `12-datos-pagos-y-recordatorios` (recurrentes, recibos), `09-reportes-hermosos` (cómo presentar). Profundidad financiera en `economist_lushows` (`58-costos-y-presupuesto.md`, `92-mejorar-margenes.md`, `90-diagnostico-de-negocio.md`, `100-playbook-restaurante-y-food.md`). **Todo número exacto → `Matematicas_lushows`** (dinero con decimal, nunca float; cálculo verificado en código).

## Principio: del dato al insight
Guardar es la mesa, no el plato. Con las facturas que YA tiene (categoría, proveedor/NIT, fecha, total, ítems), AVIS compara contra el histórico del comercio y **señala la anomalía** — el comerciante no analiza, necesita que se la griten (ver `09`, regla 5). Cada insight: **número + por qué + un paso**. Nunca regaña (ver `08`).

## Gastos hormiga (muchas compras chiquitas que suman)
Detecta cuando una categoría/proveedor acumula **muchas transacciones pequeñas** que, juntas, pesan. Suele esconderse porque ninguna asusta sola. Buen objetivo: aseo, papelería, domicilios, antojos.
> "Ojo 👀 este mes hiciste 14 compras de aseo de $8.000–$15.000 = **$167.000**. Sueltas no se ven, pero juntas pesan. Si las consolidas en una compra grande, ahorras como **$30.000**. ¿Lo intentamos?"

## Proveedor que subió de precio
Mismo NIT (cruce por proveedor, ver `04`), mismo insumo, **precio por unidad arriba** vs compras anteriores. Lo compara contra el promedio histórico de ese proveedor.
> "Tu proveedor [Lácteos X] te subió la leche de **$3.200 a $3.800** el litro (+19%) en 2 meses. Quizá valga cotizar. ¿Te ayudo a comparar?"

## Categoría disparada vs el mes pasado
Si una categoría sube **>10%** respecto al mes anterior (umbral de `09`), chip + 1 línea de causa. Esta es la alerta estrella del reporte mensual.
> "⬆ **Insumos +22%** este mes ($1.840.000 vs $1.510.000). ¿Vendiste más o subió el costo? Si fue costo, revisemos el precio de tus platos."

## Comparar proveedores del mismo insumo
Para un insumo que compra a **varios proveedores**, AVIS pone el precio/unidad lado a lado y muestra el más barato (cuidando calidad/condiciones, no solo precio).
> "Compras pollo a 2 sitios: **[A] $9.800/kg** vs **[B] $11.200/kg**. Si todo lo pasas a A, ahorras ~**$112.000/mes**. ¿Pruebas con A una semana?"

## Pagos duplicados (cruce foto ↔ electrónica)
El cruce de `04` ya une la foto con la factura DIAN para **no contar doble** (la xml es canónica; la foto queda `duplicado_de` y no suma). AVIS también marca **el mismo gasto pagado dos veces de verdad** (dos egresos, mismo proveedor+monto+fechas cercanas que NO son el mismo documento). En duda → pregunta, nunca afirma.
> "🔗 Ya tenías esta compra, la uní para no contar doble."
> "Vi **dos pagos de $480.000 a [Proveedor]** el 3 y el 5. ¿Fue una sola compra pagada dos veces? Si sí, reclámale."

## Estacionalidad (meses pesados que vuelven)
Cruza el histórico con el calendario (ver `25-calendario-del-comerciante` y `12`): meses con prima, impuesto, matrícula (31-mar), temporada alta. Avisa **con anticipación** para que prepare la caja.
> "Heads up: marzo suele ser pesado para ti (prima + matrícula CC ≈ **$2.1M** el año pasado). Vamos guardando un poquito desde enero y llegas tranquilo. 🙂"

## Proponer ahorros concretos (no "gasta menos")
Todo insight cierra con una **palanca medible**, una sola (ver `08`, regla del paso único). Suma los ahorros del mes en un titular.
> "Junté 3 ahorros fáciles: consolidar aseo (~$30k), pasar pollo a [A] (~$112k) y soltar 1 suscripción que no usas (~$45k) = **$187.000/mes** sin que te duela. ¿Por cuál arrancamos?"

## Cómo presentar el insight (amable y accionable)
- **Valida o suaviza primero**, nunca culpa: "sin drama", "ojo", "quizá valga". Tono de `08`.
- **Número exacto** (de Matematicas) + **causa en 1 línea** + **una pregunta** ("¿lo miramos?", "¿pruebas?").
- **Oportuno, no intenso:** al cerrar el reporte del mes o cuando algo cruza el umbral. Si ya lo dijiste y no actuó, calla; vuelve solo si empeora (ver `08`).
- **WhatsApp = versión corta** (1–3 líneas + emoji discreto). El detalle bonito vive en el panel/PDF (ver `09`, COBALTO, `tabular-nums`).
- **Celebra los avances:** "este mes bajaste insumos 8%, ¡bien ahí! 🎉".

## Calidad del dato antes del insight
Solo afirma con confianza si la fuente es sólida: `fuente='xml'` (exacta) pesa más que `'vision'` (0.85). Si hay pocos meses de historia o números que no cuadran (validación de `04`), AVIS matiza ("con lo que llevo registrado…") en vez de sentenciar. Para cualquier porcentaje/proyección, **ejecuta en `Matematicas_lushows`**.

> **Roadmap:** vista materializada de gasto por categoría×mes y precio/unidad×proveedor (sobre `documentos.datos` jsonb), job mensual que calcula deltas y dispara los chips de insight, y detector de precio-por-unidad a nivel de ítem (`InvoiceLine`) para el comparador de proveedores.
