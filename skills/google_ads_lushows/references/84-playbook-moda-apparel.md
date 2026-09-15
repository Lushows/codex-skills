# 84 — Playbook moda/apparel

Lee este módulo cuando vendes **ropa, calzado, accesorios o moda** online — como D'BEST (ropa deportiva + suplementos, estética dark/volt, referencia Adidas + ProScience). La moda es e-commerce visual y estacional: el producto entra por los ojos, las tallas y devoluciones deciden la conversión, y las temporadas mandan el calendario. Google **captura** a quien busca tu marca o una categoría ("tenis running", "buzo oversize negro"); Meta e Instagram GENERAN el deseo del producto nuevo que nadie buscaba (`facebook_ads_lushows`), y TikTok lo vuelve tendencia (`tiktok_ads_lushows`). En moda, casi siempre Meta/TikTok llevan el descubrimiento y Google captura la intención y la marca — úsalos juntos. La dirección de marca/estética que hace que tu ropa se vea deseable es `directorcreativo_lushows`.

## Estructura de cuenta para moda

El motor es **Shopping/PMax con feed** (la ropa se vende con foto + precio), apoyado por Search de marca y genérico y un remarketing dinámico fuerte (la moda tiene mucha consideración: ven, dudan, vuelven).

| Campaña | Tipo | Puja | Presupuesto arranque COP | Rol |
|---|---|---|---|---|
| Marca | Search | tROAS alto | $6.000–15.000/día | "D'BEST ropa", defiende y cierra |
| Genérico | Search | tCPA → tROAS | $20.000–40.000/día | "tenis para correr", "ropa deportiva hombre" |
| Shopping standalone | Shopping con feed | tROAS | $30.000–60.000/día | Control + términos de búsqueda visibles |
| PMax retail | PMax con feed | tROAS | $40.000–80.000/día | El caballo: catálogo completo con fotos (ver 35) |
| Remarketing dinámico | Demand Gen / PMax | tROAS | $15.000–30.000/día | Le muestra al que vio EXACTO lo que vio |

- **Shopping/PMax con feed es el 70% del resultado.** Toda la ropa, con foto, precio y talla disponible (ver 34, 35). Arranca con Shopping standalone para ver qué se busca y mete PMax con datos (la opacidad de PMax se aguanta mejor cuando ya sabes qué convierte).
- **Remarketing dinámico es clave en moda** más que en casi cualquier vertical: la decisión de comprar ropa es emocional y se posterga. Muéstrale al que miró ese buzo, ese mismo buzo, días después — suele ser el ROAS más alto del lado de captura.
- **Marca y genérico separados** para no mezclar el ROAS inflado de marca con el genérico real (ver 39). Y excluye marca de PMax para que no te canibalice (ver 12, 90).

**Keywords tipo por capa:** marca ("D'BEST", "[colección]") → producto específico ("buzo oversize negro hombre", "tenis running mujer") → categoría ("ropa deportiva", "conjuntos gym") → fría ("qué ponerme para el gym" — informacional, separar). Benchmark COP: CPC de Shopping en moda $300–1.200; genérico de categoría $700–2.500; marca $150–500. El CTR vive de la foto: una imagen mala mata el clic aunque pujes bien.

## Feed de moda: tallas, GTIN, devoluciones, variantes

El feed de moda es más complejo que el de un producto único porque cada prenda tiene **variantes** (tallas, colores). Google quiere ver cada variante.

**Feed de apparel — campos que importan de verdad:**

| Campo | Por qué pesa en moda |
|---|---|
| **size** (talla) | Google muestra disponibilidad por talla; sin esto pierdes el match |
| **color** | Variantes; el comprador busca "negro", "blanco" |
| **GTIN / MPN** | Mejora visibilidad y matching de producto |
| **item_group_id** | Agrupa variantes del mismo modelo (todas las tallas del mismo buzo) |
| **gender / age_group** | Hombre/mujer/unisex — filtra el match correcto |
| **imagen** | Limpia, producto bien visible; en moda es decisiva |
| **custom_label** | Etiqueta por temporada/outlet/margen para segmentar campañas |
| **política de devolución** | Configurada en Merchant; sube confianza y conversión |

- **Devoluciones claras** en Merchant Center y en la landing: en ropa la talla genera miedo ("¿y si no me queda?"). Una política de cambio/devolución visible **sube la conversión** — quita la fricción que más frena la compra de ropa online en Colombia.
- **Variantes bien armadas** (item_group_id) evitan que muestres una talla agotada — frustración + clic perdido + reseña mala.
- **custom_label** te deja armar una campaña de Shopping solo de "outlet" o solo de "alto margen" y pujar distinto en cada una. Palanca que casi nadie usa.

## Estacionalidad: el calendario manda

La moda es estacional y por campañas. Tu presupuesto NO es plano todo el año:

- **Picos de venta:** lanzamientos de colección, temporada, y sobre todo **fechas comerciales colombianas:** Día sin IVA, Black Friday/Cyber, Navidad, Día de la Madre, Amor y Amistad (septiembre). En esos días sube presupuesto y, si usas tROAS, considera **bajarlo un poco** para ganar volumen (más demanda, vale capturar más) — ver 64, 98 lanzamiento.
- **Liquidación de inventario:** campaña de Shopping específica para lo que quieres rotar, con feed etiquetado (custom_label) por "outlet" o "fin de temporada".
- **Antes de cada pico, calienta el remarketing:** llena tus audiencias semanas antes para tener a quién re-impactar el día del pico. Llegar a Black Friday con audiencias vacías es desperdiciar el día más caro del año.
- **Marca defensiva en picos:** en Black Friday todos pujan; tu propia marca se encarece porque competidores pujan sobre ella. Cúbrela bien esos días (ver 39).

## Medición

Activa **Enhanced Conversions** (piso 2026) para no perder señal post-cookie, y conecta reseñas de producto/vendedor en Merchant para las estrellas en Shopping (ver actualizacion-2026-06). Si parte de tu venta cierra por WhatsApp (común en moda colombiana de IG), sube ese cierre con OCI (ver 53). El break-even de ROAS sale de tu margen (1/margen); con la ropa de buen margen suele aguantar tROAS exigente, pero calcúlalo en `economist_lushows`, no a ojo.

**Devoluciones, el número silencioso de la moda.** La ropa se devuelve mucho (talla, color, expectativa). Un ROAS de Google que se ve hermoso puede esconder una tasa de devolución del 25% que se come el margen real. Mide tu ROAS NETO de devoluciones, no el bruto que reporta la plataforma: si devuelven 1 de cada 4, tu ROAS efectivo es 25% menor del que ves. Por eso la política de talla/devolución clara y las fotos honestas no solo suben conversión: bajan devoluciones y suben el ROAS de verdad. Esto se modela en `economist_lushows`.

## Errores comunes — blacklist

1. **Feed sin tallas/variantes.** Muestras prendas agotadas o sin la talla que buscan: clic perdido y frustración. Arma item_group_id y size (ver 34).
2. **Sin política de devolución visible.** En ropa el miedo a la talla frena la compra; devolución clara sube conversión. Configúrala en Merchant y landing.
3. **Presupuesto plano todo el año.** La moda es estacional; sin subir en picos comerciales (Día sin IVA, Black Friday) dejas ventas en la mesa (ver 98).
4. **Descuidar el remarketing dinámico.** Es el ROAS más alto en moda después de marca; el comprador duda y vuelve. Muéstrale lo que vio.
5. **Mezclar marca y genérico (y dejar que PMax coma la marca).** El ROAS de marca infla el promedio y te oculta si el genérico rinde. Sepáralos y excluye marca de PMax (ver 39, 12).
6. **Imágenes pobres en el feed.** En moda la foto ES el anuncio; una imagen mala mata el clic. Producto bien visible, limpia, sin texto (ver 35).
7. **No calentar audiencias antes del pico.** Llegas a Black Friday sin a quién re-impactar. Llena el remarketing semanas antes (ver 98).
8. **No usar custom_label.** Pujas igual a todo el catálogo, regalando margen en lo barato y dejando ventas en lo premium. Etiqueta por margen/temporada.
