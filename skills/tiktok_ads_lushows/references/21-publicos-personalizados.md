# 21 — Públicos personalizados

Un **público personalizado** (custom audience) es una lista de gente que YA tuvo contacto con tu marca: vio tus videos, entró a tu web, te escribió, te compró. Lee este módulo cuando quieras hacer retargeting (ver 23), excluir compradores (ver 24) o crear semillas para lookalikes (ver 22). En TikTok, plataforma de descubrimiento puro (ver 20), estos públicos son tu activo más valioso porque son la **única gente que ya te conoce** en un mar de extraños — y porque en el mundo post-cookie (ver 28) los datos que tú generas valen más que cualquier interés comprado.

## Los seis tipos de público personalizado

| Tipo | De dónde sale | Requiere | Para qué sirve |
|---|---|---|---|
| **Web / Pixel** | Visitas a tu sitio (TikTok Pixel/Events API, ver 14, 57) | Pixel instalado + tráfico | Retargeting de visitantes que no compraron; semilla para lookalike |
| **Engagement** | Vieron o interactuaron con tu perfil/videos (orgánicos o pagados) | Cuenta conectada | Tibios baratos; el público más grande y rápido de llenar |
| **Video viewers** | Vieron X% de un video tuyo (anuncio o post) | Campaña/posts corriendo | Calentar antes de pedir compra; subdividir por % visto |
| **Lead** | Dejaron datos en un Instant Form (ver 54) | Lead gen activo | Excluir leads ya capturados; lookalike de leads buenos |
| **Shop / GMV** | Vieron, agregaron al carrito o compraron en TikTok Shop (ver 50) | Shop activo | Retargeting de abandonos; semilla de compradores |
| **Lista de clientes** | Subes CSV con correos/teléfonos hasheados (ver 28) | ≥ tamaño mínimo + Habeas Data (ver 29) | Excluir compradores, retención, lookalike de los mejores |

## Cómo construir cada uno (acciones exactas)

**Web/Pixel** — Tools → Audiences → Create audience → Customer file / Engagement / App activity / Website traffic. Para web: define reglas como "todos los visitantes 30/90/180 días", "vieron página de producto", "agregaron al carrito sin comprar (add-to-cart menos purchase)". Crea VARIAS ventanas; las usarás distinto en retargeting (ver 23). Necesitas el Pixel + Events API funcionando primero, con los eventos `ViewContent`, `AddToCart`, `Purchase` disparando bien (ver 14); sin esos eventos nombrados, las reglas finas nacen vacías.

**Engagement** — Create → Engagement → elige fuente: video views, profile interactions, clicks/comentarios en anuncios. Ventana hasta 365 días. Es el más fácil de llenar porque las vistas **orgánicas cuentan**: si publicas contenido nativo (ver 32) y haces Spark Ads (ver 34), este público crece gratis mientras duermes. Para una cuenta nueva, este suele ser el primer retargeting viable antes de que el pixel acumule tráfico web.

**Video viewers** — al crear la audiencia de engagement, filtra por % visto: 2s, 6s, 25%, 50%, 75%, 100%. Quien vio el 75% de un video de 30s es MUCHO más cálido que quien vio 2 segundos por accidente. Subdivide: una audiencia "VV 75-100% últimos 30 días" es retargeting de calidad; "VV 2s" es casi frío disfrazado, sirve más como semilla amplia que como audiencia de cierre.

**Lead** — si corres Instant Forms (ver 54), TikTok genera la audiencia de "completaron el formulario". Úsala para excluir leads ya capturados de la prospección de leads, y para sembrar un lookalike de leads (mejor aún: de leads que después compraron).

**Shop/GMV** — si tienes TikTok Shop, las audiencias de "visitó producto", "agregó al carrito", "compró" se generan solas. La de **compradores** es tu mejor semilla de lookalike (ver 22) y tu exclusión obligatoria (ver 24). En 2026 TikTok Shop expande cobertura en LatAm; si vendes producto físico, conéctalo aunque la pauta principal vaya por otro lado, solo por estas audiencias.

**Lista de clientes** — exporta de tu CRM correos y teléfonos (E.164: +57300...), limpia (minúsculas, sin espacios) y súbelos. TikTok los hashea (SHA-256) en el navegador antes de viajar. Sirve para excluir compradores, lookalike de tus mejores clientes y campañas de retención/recompra. Cumplir Habeas Data antes de subir (ver 28, 29) — no es opcional.

## Reglas de oro al usarlos

- **Por temperatura, no por capricho** (ver 25). Engagement y video viewers = tibios. Web add-to-cart = casi calientes. Compradores = para excluir o para semilla, no para venderles lo mismo otra vez (salvo recompra, ver 25).
- **Tamaño mínimo para que TikTok lo active**: ~1.000 personas que hagan match. Públicos diminutos no entregan o entregan caro. Si tu audiencia es de 300, no la uses sola: combínala o úsala solo como exclusión.
- **Refresca**: las ventanas (30/90/180 días) caducan solas; un público de "compradores 2025" hoy ya no es tu semilla. Revisa tamaños cada mes y vuelve a subir listas cada 1-3 meses.
- **No le vendas al frío con público personalizado.** Estos públicos son chicos por definición; para volumen necesitas broad (ver 20). El custom audience es para retargeting y semillas, no para escalar de cero.

### Plantilla: set base de audiencias para una cuenta de e-com

| Nombre | Tipo | Ventana | Uso |
|---|---|---|---|
| `VV_75-100_30d` | Video viewers 75%+ | 30 días | Retargeting tibio |
| `WEB_ATC_no_compra_14d` | Web add-to-cart sin purchase | 14 días | Retargeting caliente |
| `ENG_perfil_180d` | Engagement perfil | 180 días | Semilla lookalike amplia |
| `CLIENTES_compradores_CO` | Lista de clientes | — | Exclusión + semilla premium |

## El flujo correcto

1. **Prospección** (broad, descubrimiento, ver 20) → llena tus públicos de engagement y video viewers automáticamente, sin costo extra.
2. **Esos tibios** alimentan retargeting (ver 23) y semillas de lookalike (ver 22).
3. **Compradores** se excluyen de prospección (ver 24) y se vuelven semilla de los mejores lookalikes.

Sin paso 1 saludable, los pasos 2 y 3 se mueren de hambre. El descubrimiento alimenta todo el sistema. Para cerrar los tibios que llegan por WhatsApp, rutea a `ventas_lushows`; para que la landing convierta el clic, `desingweb-lushows`; si dudas de si el retargeting paga con tu ticket, valida unidad económica con `economist_lushows`. La lógica de públicos en Meta es parecida pero no idéntica — si vienes de allá, ver `facebook_ads_lushows`.

## Errores comunes — blacklist

1. **Crear públicos personalizados sin tener Pixel/Events API.** Sin la señal (ver 14) el público web nace vacío. Instala primero, deja correr tráfico, luego construye.
2. **Una sola ventana de tiempo.** Necesitas 30/90/180 días separadas para mensajear distinto por temperatura (ver 25).
3. **Venderle al frío con un custom audience chico.** Son para retargeting y semillas; el volumen viene de broad.
4. **No subdividir video viewers por % visto.** Quien vio el 90% vale 10x quien vio el 2%; tratarlos igual desperdicia presupuesto.
5. **Olvidar excluir compradores.** Les sigues pagando impresiones para venderles lo que ya tienen (ver 24).
6. **Subir listas sin cumplir Habeas Data/consentimiento.** Riesgo legal real en Colombia y riesgo de perder la cuenta (ver 29).
7. **No refrescar.** Semillas y exclusiones viejas degradan resultados sin que te des cuenta.
8. **Usar una audiencia de 300 personas como audiencia de cierre.** Por debajo de ~1.000 con match no entrega bien; combínala o déjala solo como exclusión.
