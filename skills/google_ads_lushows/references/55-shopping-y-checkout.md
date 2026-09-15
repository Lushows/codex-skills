# 55 — Shopping y checkout

Lee este módulo cuando vendes **productos con precio y stock** (e-commerce, catálogo) y quieres aparecer en Google con foto, precio y nombre — el formato que más vende para productos físicos. Pero ojo: Shopping **trae al comprador hasta tu checkout; si tu checkout es malo, pagaste el clic para nada.** Aquí vemos cómo armar el feed para vender más por pedido y reducir el abandono. El checkout y la página de producto en sí los construye → desingweb-lushows; los medios de pago LatAm → engineer_visualopen_lushows; la viabilidad del margen → economist_lushows.

## Qué es Shopping y por qué convierte

**Shopping ads** (anuncios de Shopping) son esas tarjetas con **foto + precio + nombre + tienda** que salen arriba del buscador cuando alguien busca un producto. No los escribes tú: Google los arma desde tu **feed de productos** en **Google Merchant Center** (la plataforma gratis donde subes tu catálogo: títulos, precios, fotos, stock, link de cada producto).

Convierten más que el Search de texto para productos por una razón simple: el cliente **ve el precio y la foto antes de hacer clic**. Quien da clic ya aceptó el precio y le gustó el producto — llega más decidido. Eso baja el "clic curioso" y sube la conversión.

En jun-2026 la realidad moderna es que **Shopping vive en gran parte dentro de Performance Max** (ver 12): subes el feed a Merchant Center, conectas PMax y Google reparte tu producto entre Shopping, Search, YouTube, Display y Gmail. También existe la campaña **Shopping estándar** clásica, que da más control y visibilidad de términos — útil para aprender antes de soltar a PMax. Para que cualquiera funcione necesitas: catálogo con precios reales, fotos limpias, y un **checkout que funcione**. Sin lo último, Shopping es plata tirada.

## El feed manda — títulos, fotos y datos

En Shopping no hay keywords ni copy: **el feed ES tu anuncio.** Google decide cuándo mostrarte leyendo los datos del producto. Optimizar el feed = optimizar la campaña.

| Elemento del feed | Qué hacer | Por qué |
|---|---|---|
| **Título** | Lo importante primero: tipo + marca + atributo clave ("Calculadora costos gastronómicos Excel restaurante") | Google empareja por el título; las primeras ~70 caracteres pesan más |
| **Foto** | Limpia, fondo blanco, producto claro, alta resolución, sin texto/marca de agua | Es lo que decide el clic; foto mala = cero clics |
| **Precio** | Exacto y actualizado, en COP | Si el feed dice un precio y la web otro, Google **desaprueba** el producto |
| **Disponibilidad** | Stock real (`in stock` / `out of stock`) | Anunciar agotado quema clics y molesta a Google |
| **GTIN / marca / categoría** | Completar todo lo que aplique | Más datos = mejor emparejamiento y elegibilidad |
| **Tipo de producto / etiquetas custom** | Agrupar por margen o línea | Te deja pujar distinto por grupo en PMax/estándar |

Regla dura: **el feed tiene que coincidir con la web.** Precio, disponibilidad y nombre distintos entre Merchant Center y la página = desaprobación del producto y campaña frenada. Mantenlos sincronizados (lo automatiza tu plataforma de tienda —Shopify, WooCommerce— o tu dev → desingweb-lushows). Merchant Center además exige **políticas visibles** (envíos, devoluciones, contacto) y **envío/impuestos configurados** o no aprueba la cuenta; déjalo listo antes de pelear con anuncios.

## AOV, promociones y abandono

Tres palancas que mueven la plata después del clic:

**AOV** (*Average Order Value* — valor promedio del pedido): cuánto gasta en promedio cada comprador. Subirlo hace rentable un CPC que antes no lo era — si subes el ticket de $40.000 a $60.000, el mismo costo por venta deja más margen. Cómo:
- **Bundles / combos** en la página de producto ("llévate la calculadora + la guía de menú por $15.000").
- **Envío gratis sobre un monto** ("envío gratis desde $X") — empuja a sumar al carrito hasta llegar al umbral.
- **Order bumps** en el checkout (un extra barato de un clic) y **upsell** post-compra.

**Promociones en el feed:** Merchant Center deja mostrar **descuentos y promos directamente en la tarjeta de Shopping** (precio tachado, etiqueta "oferta"). Eso sube el CTR sin cambiar la puja. Si tienes una promo real, declárala en el feed con su vigencia.

**Abandono de carrito:** la mayoría que llega al carrito **no compra**. Las fugas típicas y su arreglo (lo ejecuta desingweb-lushows):
- Costos sorpresa al final (envío caro que aparece tarde) → muéstralos antes.
- Checkout largo o que obliga a crear cuenta → permite **compra como invitado**.
- Pocos medios de pago → en Colombia, **PSE, Nequi, Bancolombia, tarjetas y contraentrega** según el caso (integración → engineer_visualopen_lushows, Wompi/Mercado Pago).
- Sin confianza (sin reseñas, sin políticas claras, sin candado HTTPS visible) → agrega señales de confianza.

El retargeting al carrito abandonado se trabaja con **Performance Max / Demand Gen** (ver 12) o con Meta (facebook_ads_lushows): el que dejó el carrito es el lead más caliente que tienes — recuperarlo cuesta una fracción de un clic nuevo.

## Cuándo Shopping NO es para ti

Honestidad: Shopping es para **productos con precio público y stock**. NO es para:
- Servicios sin precio fijo (usa Search + lead/call → ver 50, 51, 57).
- Un solo producto digital de bajo ticket donde Search de texto basta y sobra. **Este proyecto (una calculadora de $10.000) vive mejor en Search transaccional bien armado** → ver 11, 20; armar todo un feed + Merchant Center para un SKU es sobre-ingeniería.
- Catálogos sin fotos decentes o sin checkout funcional: arregla eso primero o Shopping solo expone el problema más caro.

## Errores comunes — blacklist

1. **Lanzar Shopping con un checkout malo.** El clic más caliente muere en un checkout largo, sin medios de pago locales o con costos sorpresa. Arregla el checkout primero (desingweb-lushows).
2. **Feed desincronizado con la web.** Precio o stock distinto = Google desaprueba el producto y frena la campaña. Mantén Merchant Center y la web iguales (automático vía la tienda).
3. **Títulos genéricos.** "Plantilla Excel" no empareja con nadie. Mete tipo + atributo + para quién en las primeras palabras.
4. **Fotos pobres.** En Shopping la foto decide el clic. Una imagen oscura, con texto o marca de agua mata el CTR y puede desaprobarse.
5. **No trabajar el AOV.** Si cada pedido es chico, ningún CPC es rentable. Combos, envío gratis por monto y order bumps suben el ticket y el margen (economist_lushows).
6. **Ignorar el carrito abandonado.** El que dejó el carrito es tu mejor lead. Retargetéalo (PMax/Demand Gen o Meta) en vez de buscar tráfico nuevo más caro.
7. **Forzar Shopping en un servicio o producto sin precio público.** No es su formato. Usa Search + lead/call (ver 50, 51, 57) o Search transaccional para un único SKU digital (ver 11).
