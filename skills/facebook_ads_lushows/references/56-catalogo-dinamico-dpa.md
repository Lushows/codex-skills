# 56 — Advantage+ catalog ads (ex DPA): el catálogo que se anuncia solo

Advantage+ catalog ads — antes llamados DPA, Dynamic Product Ads — son anuncios que **se arman solos desde tu catálogo**: Meta elige por persona qué producto mostrarle (el que vio en tu web, o el que el algoritmo predice que le gusta). Tú no diseñas un ad por producto; diseñas la plantilla y el sistema hace el resto. Lee este módulo si tienes tienda online con 10+ productos. Si vendes por WhatsApp sin web, tu versión es el catálogo de WhatsApp (ver 55). Jerga: "feed" = lista estructurada de productos; "`content_ids`" = los IDs que conectan el evento del píxel con el producto del feed.

## Requisitos (sin esto no funciona)

1. **Catálogo en Commerce Manager** con feed sano (siguiente sección).
2. **Píxel/CAPI con eventos de catálogo**: `ViewContent`, `AddToCart`, `Purchase` que envíen **`content_ids` que matcheen exactamente los IDs del feed** (ver 05-06). Este match es EL punto de falla #1: si el píxel reporta `id: "camiseta-azul"` y el feed dice `id: "SKU-0042"`, el retargeting dinámico no sabe qué producto viste.
3. Verifica el match en Commerce Manager → diagnóstico del catálogo: te dice qué % de eventos matchean el feed. Apunta a >90%.

> 2026: en Events Manager el "píxel" se llama **Dataset** y conviene tener CAPI activo (botón "Activate Conversions API"), porque con el EMQ exigente de la era Andromeda/GEM el píxel-solo rinde menos (ver `actualizacion-2026-06` §7). El `content_ids` debe viajar igual por píxel Y por CAPI.

## Feed sano = 80% del éxito

El feed es la lista estructurada de productos (título, foto, precio, link, disponibilidad). Checklist:

| Campo | Estándar |
|---|---|
| `id` | Estable y único; el MISMO que manda tu píxel en `content_ids` |
| Título | Descriptivo y buscable: "Tenis running hombre Pegasus 41 negro" — NO "REF-8842" |
| Foto | Cuadrada (1:1), fondo limpio, producto protagonista, sin texto/watermarks encima |
| Precio | Actualizado SIEMPRE (precio viejo en el ad = devoluciones y desconfianza) |
| Disponibilidad | Stock sincronizado: anunciar agotados quema plata y clientes |
| GTIN/marca/categoría | Completos: mejoran distribución y matching de Meta |
| `sale_price` | Úsalo para ofertas: habilita el badge de descuento automático |

Frecuencia de sincronización: feed programado mínimo diario; tiempo real si hay integración nativa.

## Los 2 usos

1. **Retargeting dinámico** (el clásico): "muéstrale a cada persona el producto que vio o dejó en el carrito". Audiencia: ViewContent/ATC últimos 7-14 días, excluyendo compradores (ver 23 para no quemar). Es de lo más rentable que existe en Meta — intención ya demostrada + producto exacto.
2. **Prospecting dinámico** (Advantage+ catalog para frío): audiencia broad y el **algoritmo elige el producto** del catálogo para cada persona según su comportamiento en todo Meta. Funciona sorprendentemente bien con catálogos grandes (50+ productos) y feed impecable. Es el motor de los e-com chinos y de cualquier Advantage+ Sales con catálogo conectado (ver 12).

### Ventanas de retargeting por tipo de producto

| Producto | Ventana ViewContent/ATC | Por qué |
|---|---|---|
| Impulso / moda rápida / comida | 3-7 días | A los 10 días ya no recuerda ni le importa |
| Considerado (electrónica, hogar) | 14-30 días | Ciclo de decisión más largo |
| High-ticket (muebles, tech caro) | 30-60 días | Compara semanas; pero nunca 90 para impulso |

## Plantillas creativas sobre el feed

El ad dinámico no tiene que ser la foto pelada del producto. En el ad set/anuncio puedes superponer **marcos y elementos dinámicos** sobre cada foto del feed:

- Marco de marca (franja con tu logo/colores — coherencia visual, ver directorcreativo_lushows para el kit).
- **Badge de precio o % de descuento** tomado del feed automáticamente — sube CTR en LatAm donde el precio decide.
- Info de envío ("Envío gratis", "Contraentrega").
- Formatos: carrusel dinámico (varios productos, el orden lo decide Meta) y collection (portada de video/imagen + grilla de productos debajo — abre experiencia instantánea en móvil).

> 2026: el **Advantage+ Creative Suite** puede generar variaciones de fondo y hasta video desde tus fotos de producto (image-to-video "Video Generation 2.0", ver `actualizacion-2026-06` §3). Útil para refrescar creativos del catálogo sin sesión de fotos nueva — pero el ad con visual generado por IA debe llevar etiqueta (políticas 2026).

## Shopify / WooCommerce: el atajo

La integración nativa (canal "Facebook & Instagram" en Shopify; plugin oficial en Woo) monta TODO: crea el catálogo, sincroniza feed y stock en tiempo real, e instala píxel + CAPI con `content_ids` correctos. Si estás en estas plataformas, no armes nada a mano — instala, verifica eventos en Events Manager y dedica el tiempo a títulos y fotos.

## Conexión con WhatsApp (puente con 55)

Si vendes parte por web y parte por chat: el **mismo catálogo de Commerce Manager** alimenta los DPA web (este módulo) Y los ads de catálogo con destino WhatsApp (ver 55). Un solo feed, dos motores de venta. El retargeting dinámico web recupera carritos; el destino WhatsApp atiende al que prefiere preguntar antes de comprar.

## Estructura de campaña recomendada (e-com con catálogo)

Una estructura simple que rinde sin sobre-segmentar:

| Campaña | Audiencia | Optimiza por | Presupuesto |
|---|---|---|---|
| Advantage+ Sales (prospecting) | Broad, catálogo conectado, Meta elige producto | Purchase con valor | El grueso (70-80%) |
| Retargeting dinámico | VC/ATC 7-14 días, excluye compradores 30 días | Purchase | El resto (20-30%) |

- No abras 15 ad sets por categoría: con Entity ID y GEM (2026) los creativos casi-iguales se colapsan y compiten entre sí (ver `actualizacion-2026-06` §2). Menos estructura, más señal concentrada.
- Pon el **cap de clientes existentes en 25-30%** en el prospecting para forzar adquisición de nuevos (novedad mar-2026, ver `actualizacion-2026-06` §1) — antes ASC inflaba ROAS retargeteando a quien ya iba a comprar.

## Diagnóstico mensual del catálogo (rutina)

Cada mes entra a Commerce Manager → diagnóstico y revisa:

1. **% de match de eventos** con el feed (meta: >90%). Si cae, algo rompió tu `content_ids`.
2. **Productos rechazados** por políticas (imágenes con texto excesivo, claims prohibidos, precios inconsistentes).
3. **Errores de feed**: campos faltantes, links rotos, fotos no cargadas.
4. **Cobertura**: % de tu catálogo elegible para anunciar. Productos invisibles = inventario muerto en la pauta.

Diez minutos al mes que evitan que la mitad de tu catálogo deje de servirse sin que te enteres.

## Cuándo NO usar catálogo dinámico

- **Catálogo de 1-3 productos**: ads normales bien creativados rinden más (ver 30-31); lo dinámico paga con surtido.
- **Fotos horribles o feed desordenado**: el sistema multiplicará tu desorden a escala. Arregla el feed PRIMERO.
- Sin píxel con eventos de catálogo: el retargeting dinámico simplemente no tiene datos; empieza por 05-06.
- Venta 100% por WhatsApp sin web: usa ads de catálogo con destino WhatsApp (ver 55), no DPA web.

## Errores comunes — blacklist

- `content_ids` que no matchean el feed: el error silencioso #1; el retargeting "corre" mostrando productos al azar.
- Títulos con códigos internos: el título ES el copy del ad dinámico; un código no vende.
- Anunciar productos agotados por no sincronizar stock: clic pagado → página de "agotado".
- Retargeting dinámico sin excluir compradores recientes: persigues al que ya compró (ver 23).
- Ventana de retargeting de 90 días para productos de compra impulsiva: a los 60 días ya nadie recuerda ese carrito; 7-14 días.
- Probar prospecting dinámico con 8 productos y fotos de celular: el algoritmo no hace magia con materia prima pobre.
- Olvidar el catálogo después del setup: revisa el diagnóstico de Commerce Manager mensual (errores de feed, rechazos por políticas).
- Tener píxel sin CAPI en 2026: el match y el EMQ caen; activa la Conversions API (ver `actualizacion-2026-06` §7).
