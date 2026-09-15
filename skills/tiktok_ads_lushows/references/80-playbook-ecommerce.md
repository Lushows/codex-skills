# 80 — Playbook e-commerce

Lee este módulo cuando vendas un producto físico con tienda en línea (Shopify, WooCommerce, Tiendanube, o checkout propio), cuando quieras llevar a alguien desde su primer pedido en TikTok hasta escalar a millones de pesos al mes, o cuando vengas de Meta y no sepas cómo se traduce tu estructura de e-commerce a TikTok. Este es el playbook base del que cuelgan los verticales (84 moda, 83 salud). Si vendes servicio o cierras por chat, ve a 81. Si vendes evento, a 86.

## La estructura concreta de e-commerce

TikTok para e-commerce tiene **dos caminos de compra** y debes saber cuál usas antes de armar nada:

1. **Tráfico a tu web** (Shopify/Woo) → el *checkout* vive en tu sitio. Mides con **TikTok Pixel + Events API** (ver 56, 57).
2. **TikTok Shop** → el *checkout* vive dentro de TikTok, la gente compra sin salir de la app. Donde está disponible, convierte más porque elimina fricción. **Verifica si TikTok Shop está activo en Colombia hoy** — a la fecha su despliegue en LatAm es parcial; si no está, vas por web o cierras por WhatsApp (ver 50, 55).

Estructura por defecto (gasto < $400.000 COP/día), camino web:

| Capa | Cuántas | Qué define |
|---|---|---|
| Campaign | 1 | Objetivo **Sales**, optimizando *Complete payment* (ver 11, 14) |
| Ad group | 1 broad | Público amplio (país + edad), placement automático |
| Ad | 8–15 | UGC + Spark, 3–5 ángulos × 2–3 hooks (ver 30, 38) |

Cuando ya tengas datos (≥50 compras/sem en el ad group) y un ganador claro, abres **Smart+ Web/Catálogo** (ver 12, 90) para que TikTok automatice puja y reparto, y añades un ad group de **retargeting** (ver 18). No empieces con Smart+ sin señal: necesita datos del Pixel para no quemar plata adivinando.

## Creativo, oferta y los números que mandan

Creativo: **UGC** (persona real con el producto) + **Spark Ads** (ver 34, impulsas un post orgánico que ya jaló — gana confianza y conserva los likes/comentarios). Para e-commerce, los formatos que rinden:

- **Unboxing / "me llegó"** — el paquete abriéndose, primer contacto con el producto.
- **Antes/después o demo en uso** — el producto resolviendo algo en 10 segundos.
- **"3 razones por las que..."** — formato lista, retiene bien.
- **Reseña honesta** — "no esperaba que..." (ver 37 para hooks).

La **oferta** decide más que el creativo (ver 41). Para e-commerce en Colombia, lo que mueve aguja:

- **Envío gratis** sobre cierto monto → sube el AOV (*Average Order Value*, ticket promedio).
- **Combo / bundle** → el 2x más barato sube AOV sin descuento percibido como "barato".
- **Descuento de primera compra** solo en retargeting, no en frío (no malacostumbres al lead nuevo).

Los números que decides ANTES de prender:

| Métrica | Qué es | Para qué |
|---|---|---|
| AOV | Ticket promedio | Define tu CPA máximo |
| Margen | % que queda tras costo + envío | Sin esto, ROAS es humo (ver economist) |
| **CPA objetivo** | Costo por compra que aguantas | = margen × AOV, con holgura |
| **ROAS objetivo** | Ingreso / gasto en ads | Mínimo de equilibrio según margen (ver 64) |

Regla de equilibrio: si tu margen es 50%, tu **ROAS de break-even es 2.0** (vendes $2 por cada $1 de pauta solo para empatar). Apunta a 2.5–3.0+ para ganar. Si tu margen es 30%, break-even es ~3.3 — TikTok te va a costar y debes saberlo antes (la viabilidad la valida `economist_lushows`).

## Del primer pedido a escalar

Fase 1 — **validar** (semanas 1–2): 1 campaña Sales, ABO, $80.000–$150.000 COP/día, 8–15 creativos. Meta: que al menos 1–2 creativos bajen del CPA objetivo. Si nada convierte con 15 creativos probados, el problema es oferta o producto, no la pauta (ver 41).

Fase 2 — **estabilizar** (semanas 3–6): apaga los creativos muertos, deja correr 2–3 ganadores, sube presupuesto **20–30% cada 2–3 días** (subidas bruscas resetean aprendizaje, ver 13, 72). Activa retargeting de quien vio video/visitó web/agregó al carrito.

Fase 3 — **escalar** (mes 2+): mueve los ganadores a **Smart+ / CBO** (ver 12, 90), alimenta el catálogo para retargeting dinámico, y **mantén el flujo de creativos nuevos** — en TikTok el creativo se quema en días/semanas (ver 39). Escalar en TikTok no es subir presupuesto a un video: es producir 5–10 creativos nuevos por semana para no morir de fatiga.

Reparto de responsabilidades: la **landing/tienda** que convierte → `desingweb-lushows`. La **viabilidad de unit economics** (¿aguanta el margen pagar TikTok?) → `economist_lushows`. El **cierre por WhatsApp** si no hay checkout en TikTok → `ventas_lushows`.

## Errores comunes — blacklist

- **Empezar en Smart+ sin datos del Pixel.** Automatiza sobre ruido y quema presupuesto; primero junta señal manual (ver 12).
- **Mandar tráfico a una home genérica** en vez de a una página de producto/landing que convierta (ver desingweb).
- **No medir compras de verdad** — sin Pixel + Events API el ROAS que ves es ficción (ver 56, 57).
- **Optimizar a clics/tráfico** creyendo que "ya luego compran". Optimiza a *Complete payment* o atraes mirones (ver 11).
- **Descuento agresivo en frío** que destruye margen y enseña al cliente a esperar promo (ver 41).
- **Un solo creativo ganador y dejar de producir.** Se quema y la cuenta cae en una semana (ver 39).
- **Ignorar el AOV.** Subirlo con combos/envío gratis cambia tu CPA aguantable más que cualquier ajuste de puja.
