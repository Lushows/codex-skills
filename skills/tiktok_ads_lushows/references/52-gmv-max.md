# 52 — GMV Max

Lee este módulo cuando tengas TikTok Shop con varios productos y muchos creativos, cuando un cliente te diga "no quiero estar peleando con 20 campañas", o cuando vengas de Meta y conozcas Advantage+ Shopping (ASC) y quieras su equivalente en TikTok. GMV Max es la apuesta de TikTok por la automatización total del Shop, y a jun-2026 es el formato que TikTok más empuja para sellers. Como toda automatización: gana en simplicidad, cobra en control. Solo aplica donde TikTok Shop existe (ver 50). El frame no cambia: TikTok es **descubrimiento** (ver 00); GMV Max es la máquina que convierte ese descubrimiento en GMV a escala.

## Qué es GMV Max

**GMV Max** = una campaña **automatizada** de TikTok Shop que maximiza el **GMV** (Gross Merchandise Value, en español *valor bruto de mercancía*: el total vendido). Es el "Advantage+ Shopping de TikTok": **una sola campaña para todo el Shop**, donde el algoritmo decide qué productos mostrar, a quién, con qué creativo y a qué puja, optimizando por ventas totales.

En vez de armar campañas producto por producto (como en VSA manual, ver 51), le entregas a TikTok:
- Tu **catálogo completo** (sano — ver 56).
- Tu **banco de creativos** (videos orgánicos que ya etiquetaron productos + ads + videos de creadores con Spark Ads, ver 32).
- Tu **objetivo de GMV o de target ROAS**.

Y el sistema arma, prueba y reparte presupuesto solo, buscando el mayor volumen de venta del Shop entero. A jun-2026 GMV Max también puede **jalar automáticamente videos orgánicos** que ya están etiquetando productos para usarlos como creativos — por eso sembrar orgánico antes (ver 50) lo alimenta gratis.

## Qué controlas y qué cedes

| Controlas | Cedes al algoritmo |
|---|---|
| Presupuesto total | Reparto entre productos |
| Objetivo (GMV o **target ROAS**) | A quién se le muestra cada producto |
| Catálogo (qué productos entran) | Qué creativo se usa con quién |
| Banco de creativos disponible | Pujas individuales (ver 15) |
| Productos excluidos | Combinación producto–audiencia–video |

Lo que ganas: **simplicidad y velocidad de aprendizaje**. Una campaña concentra toda la señal de conversión en vez de fragmentarla en 20 campañas que aprenden lento y compiten entre sí. Lo que pierdes: **granularidad**. No puedes decir "este producto solo a Bogotá con este video". Si necesitas ese control quirúrgico, usa VSA manual (ver 51).

### GMV Max vs VSA manual — tabla de decisión

| Situación | Mejor opción |
|---|---|
| 1 producto, quieres control fino | VSA manual (51) |
| Catálogo amplio (10+ SKUs) | GMV Max |
| Quieres concentrar señal de conversión | GMV Max |
| Necesitas geo/creativo por producto | VSA manual (51) |
| Operación simple, poco tiempo | GMV Max |
| Lanzamiento de un solo SKU estrella | VSA manual (51) |

## Setup paso a paso

1. **Verifica catálogo sano** en Ads Manager: cuántos productos están *activos/aprobados* vs *rechazados* (ver 56). Si la mitad están rechazados, GMV Max amplifica el desastre — arregla primero.
2. **Confirma medición**: pixel + Events API midiendo Complete Payment del Shop (ver 57). Sin señal limpia, GMV Max optimiza a ciegas.
3. Crea la campaña **GMV Max** desde Seller Center o Ads Manager (según país/cuenta).
4. **Define el modo de objetivo**: *GMV* (maximiza volumen, deja que el ROAS flote) o *target ROAS* (fija un ROAS objetivo y el sistema respeta ese piso). Empieza con un **target ROAS realista** según tu margen (ver abajo).
5. **Alimenta creativos**: conecta videos orgánicos, ads existentes y videos de creadores (Spark Ads, ver 32). Cuantos más, mejor prueba (ver 39).
6. **Excluye** productos sin stock, sin margen o que no quieres empujar.
7. **Deja correr 7–14 días** sin tocar antes de juzgar. La automatización necesita ventana de aprendizaje.

### Cómo fijar el target ROAS inicial (números COP)

El target ROAS no se inventa: sale de tu margen. Ejemplo con un producto de $50.000 COP:

| Concepto | Valor |
|---|---|
| Precio venta | $50.000 |
| Costo producto + envío | $25.000 (margen 50%) |
| Comisión Shop (7%) | $3.500 |
| Margen antes de ads | $21.500 |
| ROAS de equilibrio (break-even) | 50.000 / 21.500 ≈ **2,3x** |
| Target ROAS inicial para ganar | **2,5x – 3x** |

Si exiges 5x el día uno, el sistema no encuentra compras a ese precio y no gasta ni aprende. Arranca cerca del break-even + un colchón, y sube el target solo cuando haya datos estables. Valida toda la unit economics con `economist_lushows` (ver 64 ROAS).

## Cuándo conviene GMV Max (y cuándo no)

**Conviene cuando:**
- Tienes **catálogo amplio** (no 1 producto) y quieres que TikTok priorice los que más venden.
- Tienes **volumen de creativos** para alimentarlo (ver 39).
- Quieres **operación simple** y confías en dejar que el sistema reparta.
- Ya tienes **señal de conversión limpia** (pixel/Events API midiendo compra — ver 57). Sin señal limpia, optimiza a ciegas.

**No conviene cuando:**
- Vendes **un solo producto** → VSA manual te da más control sobre el mismo gasto.
- Tu **catálogo está sucio** → GMV Max amplifica el desastre; límpialo primero (ver 56).
- Necesitas **control fino** por producto, geo o creativo (ver 59 para local).
- No hay **TikTok Shop** en el país → no existe GMV Max; cierra por WhatsApp (ver 50, 55).

## Cómo leer si funciona

- **No le creas el ROAS que reporta la plataforma.** TikTok se sobre-atribuye (se cuelga ventas que no causó — ver 16). Cruza contra ventas reales en tu sistema (pedidos en `data/orders.json`, plata en la cuenta).
- Mira el **GMV total y el ROAS real** semana a semana, no día a día.
- Si el ROAS real está por debajo de tu break-even sostenido, **no subas presupuesto** — revisa catálogo, creativos y precio antes.
- Escala presupuesto en **incrementos de 20–30%** cada 2–3 días, no de golpe (ver 15, 64).

## Rutas a skills hermanas

- ROAS real, márgenes, unit economics → `economist_lushows`.
- Creativos / Spark Ads de creadores que alimentan GMV Max → 32, 39.
- Equivalente Advantage+ Shopping en Meta → `facebook_ads_lushows`; Performance Max en Google → `google_ads_lushows`.
- Web/checkout fuera del Shop → `desingweb-lushows`.

## Errores comunes — blacklist

- **Usar GMV Max con un solo producto.** No aprovecha su fuerza (repartir entre catálogo); usa VSA (ver 51).
- **Alimentarlo con catálogo sucio.** Amplifica productos malos; límpialo primero (ver 56).
- **Exigir ROAS alto el día uno.** No deja aprender; arranca cerca del break-even + colchón y dale 7–14 días.
- **Dejarlo sin volumen de creativos.** Se queda sin material para probar; aliméntalo con orgánicos y Spark Ads (ver 39, 32).
- **Creerle el ROAS que reporta la plataforma.** Se sobre-atribuye; valida con tus números reales (ver 16, 64).
- **Lanzarlo sin pixel/Events API midiendo compra.** Optimiza a ciegas (ver 57).
- **Mezclar GMV Max y VSA manual del mismo producto compitiendo entre sí.** Se canibalizan la puja; decide uno u otro por producto.
- **Subir presupuesto de golpe.** Resetea el aprendizaje; escala 20–30% cada 2–3 días.
