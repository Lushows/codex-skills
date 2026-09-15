# 56 — Catálogo y feed

Lee este módulo cuando vayas a lanzar Video Shopping Ads, GMV Max o Smart+ con catálogo, cuando un cliente de e-commerce tenga 50 productos y "no sabe por qué no venden", o cuando los ads de Shop arranquen mal sin razón aparente. Casi siempre la razón es el catálogo. **El catálogo es parte del anuncio** — no es un detalle técnico de fondo, es lo que el cliente ve, toca y compra. Un catálogo sucio arruina la mejor pauta. Solo aplica donde TikTok Shop existe (ver 50); sin Shop no hay catálogo de compra, el cierre va por WhatsApp (ver 55).

## El catálogo ES parte del anuncio

En VSA, GMV Max y Smart+ con catálogo (ver 51, 52, 12), TikTok no solo muestra tu video — muestra **la ficha del producto que sale del feed**: foto, título, precio, disponibilidad. Si esa ficha está mal, el usuario que paró a ver tu video llega a un producto sin foto, sin stock o con precio raro, y se va. **Pagaste el clic, perdiste la venta.**

Por eso el catálogo no es trabajo de "sistemas". Es trabajo de quien optimiza la pauta, porque cada atributo del feed afecta directamente la conversión:

| Atributo del feed | Qué pasa si está mal |
|---|---|
| **Foto** | Sin imagen o borrosa → nadie toca |
| **Título** | Confuso → no se entiende qué es |
| **Precio** | Desactualizado → reclamo o abandono |
| **Stock / disponibilidad** | Agotado mostrado → pagas clics muertos |
| **Categoría** | Mal asignada → el algoritmo lo muestra a quien no compra |
| **Variantes (talla/color)** | Faltantes → el comprador se frustra y sale |
| **GTIN / SKU** | Faltante → el algoritmo no matchea bien |

## Anatomía de un catálogo sano

Checklist de feed limpio, atributo por atributo:

1. **Imágenes:** cada producto con al menos una foto clara, fondo limpio, producto visible. Para TikTok, suma imágenes que se vean bien en **vertical y móvil** (la mayoría del tráfico es así). Recomendado: cuadrada o vertical, mínimo 600×600 px, sin texto incrustado pesado ni marcas de agua. Una foto mala mata la conversión más que cualquier puja.
2. **Títulos:** descriptivos y humanos ("Camiseta oversize algodón premium negra"), no códigos internos ("SKU-00123-NEG"). El título es lo que lee el comprador. Pon lo importante al inicio (tipo + atributo clave).
3. **Precios:** sincronizados con tu tienda real. Si el precio cambia en tu web y no en el feed, vendes a pérdida o frustras. Usa el mismo valor que cobras de verdad, en COP.
4. **Stock:** disponibilidad **en tiempo real**. Un producto agotado mostrado en ads = plata quemada. Sincroniza inventario.
5. **Atributos completos:** categoría correcta, marca, GTIN/SKU, variantes (talla, color, sabor). El algoritmo usa esto para matchear producto con comprador.
6. **Sin duplicados ni productos muertos:** limpia SKUs descontinuados y duplicados que dividen la señal.

### Estructura mínima de un feed (CSV/XML)

Columnas que no pueden faltar:

| Campo | Ejemplo |
|---|---|
| `id` / `sku` | CAM-OVS-NEG-M |
| `title` | Camiseta oversize algodón negra talla M |
| `description` | Algodón premium 100%, corte oversize... |
| `price` | 59000 COP |
| `availability` | in stock |
| `image_link` | https://tutienda.com/img/cam-ovs-neg.jpg |
| `link` | https://tutienda.com/p/cam-ovs-neg |
| `brand` | TuMarca |
| `google_product_category` / categoría | Apparel > Shirts |

## Sincronización: que el feed nunca mienta

El catálogo se conecta a TikTok de tres formas, de menos a más automática:

| Método | Cuándo | Riesgo |
|---|---|---|
| **Subida manual / CSV** | Catálogo pequeño y estable (<20 SKUs) | Se desactualiza rápido |
| **Feed por URL** (link a tu CSV/XML que TikTok refresca) | Catálogo mediano | Depende de la frecuencia de refresco |
| **Conexión por plataforma** (Shopify, WooCommerce, etc.) o API | Catálogo grande / cambiante | El más sano; sincroniza solo |

Regla: cuanto más cambia tu inventario (moda, stock rotativo, lanzamientos), **más automática** debe ser la sincronización. Un feed que se actualiza una vez al mes en un negocio de moda miente todo el tiempo (ver 84). Si usas feed por URL, configura el refresco al menos diario; si tienes plataforma e-commerce, usa la integración nativa.

Antes de cada lanzamiento de VSA/GMV Max, **revisa el estado del catálogo en Ads Manager**: cuántos productos están "activos/aprobados" vs "rechazados". Si la mitad están rechazados (foto faltante, atributo inválido, categoría prohibida), arréglalos ANTES de pautar — si no, GMV Max amplifica el desastre (ver 52).

### Mini-auditoría de catálogo (10 minutos antes de lanzar)

1. ¿Cuántos productos están **aprobados** vs **rechazados**? Meta: >90% aprobados.
2. ¿Los **top 5 productos** que vas a empujar tienen foto buena, precio correcto y stock?
3. ¿Hay productos **agotados** activos? Pausa o quita.
4. ¿Los títulos son **humanos** o códigos? Corrige los visibles.
5. ¿El precio del feed **coincide** con tu tienda? Cruza 3 al azar.

## Catálogo sano alimenta todo el bloque comercio

- VSA manual etiqueta productos del catálogo (ver 51).
- GMV Max reparte presupuesto entre el catálogo entero (ver 52) — un catálogo sucio lo hunde.
- Smart+ con catálogo usa el feed para retargeting dinámico (ver 12).
- Live Shopping etiqueta productos con stock real para urgencia genuina (ver 53).

## Rutas a skills hermanas

- Tienda e-commerce / web donde vive el feed → `desingweb-lushows`.
- Moda con stock rotativo (talla/color/devoluciones) → 84; e-commerce general → 80.
- Equivalente catálogo en Meta (Commerce Manager) → `facebook_ads_lushows`; Merchant Center en Google → `google_ads_lushows`.

## Errores comunes — blacklist

- **Tratar el catálogo como tema técnico de fondo.** Es parte del anuncio; revísalo tú (ver arriba).
- **Mostrar productos agotados.** Pagas clics que no pueden comprar; sincroniza stock en tiempo real.
- **Títulos con códigos internos en vez de nombres humanos.** El comprador no entiende; describe claro.
- **Precios desactualizados entre tienda y feed.** Vendes a pérdida o frustras; sincroniza precio.
- **Fotos malas, con texto incrustado o faltantes.** Matan la conversión más que cualquier puja; foto clara y vertical-friendly.
- **Sincronizar manual un inventario que cambia rápido.** El feed miente; usa feed por URL o API (ver moda 84).
- **Lanzar GMV Max/VSA sin revisar productos rechazados.** Amplificas errores; haz la mini-auditoría antes (ver 51, 52).
- **Categoría mal asignada.** El algoritmo muestra el producto a quien no compra; asigna la categoría correcta.
