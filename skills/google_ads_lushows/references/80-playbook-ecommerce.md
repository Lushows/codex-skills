# 80 — Playbook e-commerce

Lee este módulo cuando vendes **productos físicos en una tienda online** (Shopify, WooCommerce, VTEX, Tienda Nube, Wix) y quieres una estructura de cuenta de Google Ads que escale de tu primer pedido a vender en serio — sin quemar plata en clics que no convierten. Google aquí **captura** demanda: la persona ya sabe qué producto quiere o tiene la categoría en la cabeza, y busca dónde comprarlo. Lo que NO hace Google: descubrirle el producto a alguien que no lo buscaba — eso es Meta (ver `facebook_ads_lushows`) o TikTok (ver `tiktok_ads_lushows`). En e-commerce real serio, usa los dos lados: Meta/TikTok GENERAN demanda, Google la CAPTURA. El que pauta solo Google se queda esperando que la gente busque; el que pauta solo Meta no recoge al que ya decidió.

Antes de pautar un peso: si no sabes tu **AOV** (Average Order Value = ticket promedio, lo que gasta un cliente por pedido) ni tu **margen de contribución** (lo que queda después de producto + envío + pasarela), no puedes fijar un objetivo de ROAS sano. Eso es de `economist_lushows`. Sin esos números, pautas a ciegas y un "ROAS de 3" te puede estar haciendo perder plata.

## Estructura de cuenta recomendada

No metas todo en una PMax y reces. La estructura que rinde y te deja ver qué pasa, para una tienda con catálogo en COP:

| Campaña | Tipo | Puja | Presupuesto típico arranque | Para qué |
|---|---|---|---|---|
| Marca | Search | tROAS alto (o Max. valor) | $8.000–20.000/día | Defender tu nombre, barato, cierra altísimo |
| Genérico/categoría | Search | tCPA → tROAS | $20.000–40.000/día | "zapatos deportivos hombre", intención media-alta |
| Shopping standalone | Shopping con feed | tROAS | $30.000–60.000/día | Control: producto + foto + precio, sin caja negra |
| PMax retail | PMax con feed | tROAS | $40.000–80.000/día | El caballo de batalla cuando ya hay datos (ver 35, 90) |
| Remarketing | Demand Gen o PMax (segmento) | tROAS | $15.000–30.000/día | Recuperar al que vio y no compró |

- **Marca primero, siempre.** Tu propio nombre es la keyword más barata y la que más cierra (alguien que busca "D'BEST ropa" ya te conoce). Si no la cubres, un competidor o un revendedor te roba ese clic (ver 39 marca-vs-genérico). Es defensa, cuesta poco, da ROAS altísimo — pero ojo: no te engañes creyendo que ese ROAS es "ventas nuevas". Mucha de esa venta ocurriría igual; sepárala para no inflar el promedio.
- **Shopping/PMax con feed es el motor.** En retail, el formato que manda es el que muestra **foto + precio + nombre del producto** directo en el buscador y en la pestaña Shopping. Eso vive del **feed** de Merchant Center (ver 34 shopping, 35 PMax-retail). Un anuncio de texto compite con suerte; uno con la foto del producto y el precio gana el clic del comprador.
- **Shopping standalone antes de PMax.** Consejo 2026: arranca con una campaña Shopping clásica (te deja ver términos de búsqueda y controlar) y mete PMax cuando ya tengas señal de qué convierte. PMax es potente pero opaca; no la enciendas como primer movimiento de una cuenta sin historial.
- **Genérico aparte de marca**, para no mezclar métricas. Búsquedas de categoría ("vestidos de fiesta", "tenis para correr") tienen intención pero menos que marca; necesitan su propio presupuesto y objetivo.

## Feed, Merchant Center y benchmarks COP

El feed es el 80% del resultado en e-commerce. Un feed pobre = anuncios pobres por mucho que pujes.

**Feed mínimo viable (Merchant Center, 2026):**
- **Título** con keywords reales primero: "Tenis running hombre negro talla 42 — Marca X" pega muchísimo más que "Producto 00231". Los primeros 35–40 caracteres son los que se ven.
- **GTIN** (código de barras del producto) cuando exista — mejora visibilidad y matching; Google premia los productos con GTIN válido.
- **Imagen limpia**, fondo blanco, sin texto/logos/marcas de agua encima (Google la rechaza por "imagen promocional").
- **Precio y disponibilidad** exactos y sincronizados — desajuste entre feed y landing = suspensión del producto o de la cuenta por "misrepresentation".
- **Categoría de Google** correcta + atributos (color, talla, material) — alimentan PMax y Shopping.
- **Reseñas de producto y de vendedor** conectadas: las estrellas en el anuncio de Shopping suben el CTR notablemente.

**Benchmarks COP de referencia (Colombia, varían por nicho — son brújula, no ley):** CPC de Shopping suele correr **$300–1.500**; CPC de Search genérico de categoría **$800–3.000**; el de marca, **$150–600**. CTR sano en Shopping ronda 1–2%; en Search de categoría 3–6%; en marca 10%+. Si tu CPC genérico se va a $4.000+ y no cierras, el problema es feed/landing/oferta, no la puja.

**ROAS objetivo (tROAS):** ROAS = ingresos / inversión. **Tu punto de equilibrio de ROAS = 1 / margen.** Con 50% de margen, break-even ROAS = 2.0; con 60%, = 1.67. Pon el objetivo ARRIBA de eso o estás trabajando para Google. Regla práctica para arrancar:

1. **Primeras 2–4 semanas:** Maximizar valor de conversión SIN tROAS (deja que aprenda). Necesitas datos antes de poner techo.
2. **Cuando tengas ~30–50 conversiones/mes** por campaña: activa tROAS un poco por debajo del ROAS real que viste (si rindió 3.0, pon 2.5) y sube de a poco.
3. **No pongas tROAS altísimo de entrada** — estrangulas el volumen y la campaña no sale de aprendizaje (ver 13, 15 pujas, 64 ROAS).

## Excluir tu marca de PMax y escalar

Error clásico que infla el ROAS y te miente: dejar que **PMax canibalice tus búsquedas de marca**. PMax tiende a comerse el tráfico fácil de marca y reportar un ROAS hermoso que en realidad era venta que ya tenías.

- **Excluye términos de marca en PMax** (pídele a Google la exclusión de marca, o maneja marca en su Search dedicada). Así PMax trae demanda NUEVA y tu Search de marca defiende lo tuyo (ver 12, 90 PMax-AIMax). Con AI Max en Search y la opacidad de PMax, las **exclusiones de marca y los negativos a nivel cuenta son más importantes que nunca** (ver actualizacion-2026-06).
- **Para escalar:** sube presupuesto de a 20–30% cada 3–4 días, no de golpe (un salto brusco reinicia el aprendizaje y te dispara el CPA una semana). Escala primero lo que YA da tROAS sano; no escales lo que apenas sobrevive.
- **Mide con Enhanced Conversions activado** (datos first-party hasheados): en 2026 es el piso de medición, recupera la señal que la cookie perdió y hace que Smart Bidding optimice mejor (ver actualizacion, 05/16).
- **Remarketing dinámico:** muéstrale al que vio un producto ese mismo producto. Recupera carritos abandonados — suele ser el ROAS más alto después de marca.

La landing manda tanto como el anuncio: página de producto lenta, sin reseñas, con checkout confuso o sin medios de pago locales (PSE, Nequi, contraentrega), mata la conversión que tanto pagaste (ver 33 landing, deriva a `desingweb-lushows`). La estética/marca que hace deseable el producto es `directorcreativo_lushows`. Y si tu cierre real ocurre por WhatsApp/llamada, mídelo con OCI (ver 53) y trabaja el cierre en `ventas_lushows`.

## Errores comunes — blacklist

1. **No cubrir tu marca en Search.** Es la keyword más barata y rentable; si no la tomas, un revendedor o competidor te la roba (ver 39).
2. **Dejar que PMax se coma la marca.** Infla el ROAS con ventas que ya tenías. Excluye marca de PMax (ver 12, 90).
3. **Feed descuidado.** Títulos genéricos, sin GTIN, imágenes con texto: anuncios invisibles o rechazados. El feed es el 80% del resultado (ver 34).
4. **Encender PMax como primer movimiento.** En cuenta sin historial es caja negra que no aprendes a leer. Arranca con Shopping/Search, mete PMax con datos (ver 35).
5. **Poner tROAS agresivo sin datos.** Con menos de ~30 conversiones/mes estrangulas el volumen y nunca sale de aprendizaje. Arranca con Maximizar valor (ver 13).
6. **No saber tu break-even ROAS.** Sin margen y AOV no sabes si un ROAS de 2 gana o pierde. Eso es `economist_lushows`.
7. **Escalar de golpe.** Doblar presupuesto reinicia el aprendizaje y dispara el CPA. Sube 20–30% cada 3–4 días (ver 15).
8. **Pautar a una página de producto mala.** Lenta, sin reseñas, sin PSE/Nequi, checkout confuso: pagaste el clic y lo botaste. Arregla la landing primero (ver 33, `desingweb-lushows`).
