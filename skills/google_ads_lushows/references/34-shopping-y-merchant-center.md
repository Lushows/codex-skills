# 34 — Shopping y Merchant Center

Lee este módulo cuando vendas productos físicos con catálogo (e-commerce, moda, productos con foto y precio), te aparezcan fichas con imagen en Google, o tu feed esté "rechazado" y no entiendas por qué.

En Shopping pasa algo distinto a Search de texto: **tú no escribes el anuncio, tu catálogo ES el anuncio.** Google arma fichas (foto + título + precio + tienda) directamente desde un archivo de datos llamado **feed** que vive en **Merchant Center** (hoy "Merchant Center Next", la versión nueva y única en 2026). No eliges keywords: Google decide qué ficha mostrar leyendo los datos de cada producto. Por eso en Shopping la pelea no es de copy, es de **calidad del feed**: un feed sano vende; uno sucio ni siquiera se muestra. La mitad de las cuentas de Shopping en Colombia están dejando ventas sobre la mesa por un feed que Google rechaza a medias.

Esto aplica sobre todo a e-commerce (ver 80) y moda (ver 84). Si vendes un servicio o un producto digital único (como la calculadora gastronómica), Search de texto (ver 30-31) suele ser mejor que Shopping — no tienes catálogo que alimentar.

## Merchant Center Next: cómo entra el feed

En 2026 hay tres formas de alimentar el feed, de menos a más control:

| Método | Cómo funciona | Para quién |
|---|---|---|
| **Lectura automática del sitio** | Google rastrea tu web y arma el feed solo | tiendas chicas que arrancan; menos control |
| **Feed por archivo / Google Sheets** | tú subes una hoja con los atributos | control medio, bueno para empezar serio |
| **Feed por API / app de la plataforma** | Shopify, WooCommerce, VTEX sincronizan en vivo | e-commerce real, stock y precio siempre al día |

Si vendes en serio, conecta la app de tu plataforma (Shopify/Woo/VTEX) — sincroniza precio y stock en tiempo real y mata el 90% de los rechazos por desincronización. La integración técnica vive en `engineer_visualopen_lushows` si hay que tocar API.

## El feed: qué lo vuelve sano

El feed es una tabla donde cada fila es un producto y cada columna un atributo. Google lee esos atributos para entender y mostrar. Estos son los que importan:

| Atributo | Por qué importa | Error típico |
|---|---|---|
| **Título (title)** | es lo que el usuario lee; Google también lo usa para hacer match con la búsqueda | títulos genéricos "Producto 123" |
| **GTIN** (código de barras universal) | identifica el producto; sin él Google a veces ni lo muestra | dejarlo vacío teniéndolo |
| **Imagen** | la foto es el 80% del clic en Shopping | foto con marca de agua o texto encima (la rechazan) |
| **Precio** | debe coincidir EXACTO con el de la web | precio del feed ≠ precio de la página → rechazo |
| **Disponibilidad** | en stock / agotado | mostrar agotados → mala experiencia |
| **Marca (brand)** | ayuda al match y a la confianza | vacío |
| **Categoría de producto Google** | ubica el producto en el árbol de Google | mal categorizado → se muestra en búsquedas equivocadas |
| **Descripción** | Google la lee para entender el producto | copiar la misma en todos |
| **product_type** | tu propia categorización (para segmentar campañas) | dejarlo vacío y no poder filtrar |

### El título del feed es tu "keyword" en Shopping

Como no eliges keywords, el título es lo que conecta tu producto con la búsqueda. Optimízalo con estructura, no con relleno:

**Marca + Tipo de producto + Atributo clave (color/talla/material) + Modelo/género.**

| Título malo | Título bueno (gana) |
|---|---|
| "Camiseta bonita oferta" | "Nike Camiseta Deportiva Dri-FIT Hombre Negra Talla M" |
| "Zapatos cómodos" | "Adidas Tenis Running Ultraboost Mujer Blancos Talla 38" |
| "Producto 4521" | "Samsung Audífonos Galaxy Buds2 Pro Inalámbricos Negros" |

Pon lo más importante en los primeros 70 caracteres (es lo que se ve en la ficha). En moda, color y talla son oro (ver 84). El título del feed se trabaja como copy de venta, aunque parezca data — la dirección de marca y nombres consistentes vienen de `directorcreativo_lushows`.

## Aprobación y problemas comunes de feed

Antes de mostrarse, cada producto pasa por revisión de Google. Los rechazos más frecuentes en Colombia y cómo se arreglan:

| Problema | Causa | Solución |
|---|---|---|
| "Precio no coincide" | el feed dice un precio y la web otro | sincroniza feed ↔ web; revisa IVA incluido y descuentos aplicados |
| "Falta GTIN" | producto con código de barras sin declararlo | agrega el GTIN; si es hecho a mano sin GTIN, marca `identifier_exists = no` |
| "Imagen con texto promocional" | foto con "OFERTA", logo o marca de agua | usa foto limpia del producto sobre fondo neutro |
| "Política / contenido" | producto restringido o datos incompletos | revisa políticas de Shopping; completa atributos (ver 08) |
| "Sin política de envío/devolución" | falta configurar en Merchant Center | configura envíos y devoluciones a Colombia |
| "Sin datos de contacto/empresa" | Merchant Center exige verificar el negocio | completa NIT, dirección y contacto verificable |
| "Discrepancia de disponibilidad" | feed dice "en stock", web dice "agotado" | sincroniza stock; idealmente vía API |

Regla de oro: **el feed debe coincidir milimétricamente con tu web.** Precio (con IVA), disponibilidad y nombre tienen que ser idénticos. La mayoría de rechazos son por desincronización, no por mala fe. En Colombia, el caso clásico es: el feed trae el precio sin IVA y la web lo muestra con IVA → "precio no coincide" → producto suspendido. Decide una sola fuente de verdad y que ambos lados lean de ahí.

## Shopping estándar (el formato de control)

Una vez el feed está aprobado, puedes correr **Shopping estándar**: campañas donde TÚ controlas presupuesto, pujas y qué productos entran, y ves en qué búsquedas (términos de búsqueda, ver 68) apareces. Es el formato con CONTROL. Su alternativa es PMax con feed, que da más alcance pero te quita visibilidad y puede canibalizar tu marca — esa decisión completa está en el módulo 35.

Estructura recomendada de Shopping estándar: separa productos por margen o por `product_type` en grupos distintos (ej. "alta rotación" vs "premium") para pujar diferente por cada uno. Usa Smart Bidding (tROAS, ver 13, 15) una vez tengas conversiones; antes, empieza manual o con maximizar clics para juntar datos.

Empieza por entender que: **feed sano primero, formato después.** Sin feed sano, ningún formato funciona — ni Shopping estándar ni PMax. Es el cimiento.

## Errores comunes — blacklist

- **Pensar que el anuncio se escribe**: en Shopping el feed ES el anuncio; toda la optimización vive en el catálogo, no en un copy.
- **Títulos de feed genéricos**: "Producto bonito oferta" no hace match con nada; usa Marca + Tipo + Atributo + Modelo, lo clave en los primeros 70 caracteres.
- **Imagen con marca de agua o texto**: Google la rechaza; usa foto limpia sobre fondo neutro (arte → `directorcreativo_lushows`).
- **Precio del feed distinto al de la web (clásico del IVA)**: rechazo casi seguro; sincroniza incluyendo IVA y descuentos, una sola fuente de verdad.
- **Dejar el GTIN vacío teniéndolo**: pierdes impresiones; declara el código de barras o marca que no existe si es hecho a mano.
- **Mostrar productos agotados**: arruina la experiencia y el rendimiento; mantén la disponibilidad al día, idealmente vía API.
- **No verificar el negocio en Merchant Center**: sin NIT/contacto verificable, Merchant Center suspende toda la cuenta, no solo un producto.
- **Correr Shopping con feed sucio "a ver si jala"**: sin feed aprobado y limpio no hay milagro; arregla el catálogo primero (ver 80).
