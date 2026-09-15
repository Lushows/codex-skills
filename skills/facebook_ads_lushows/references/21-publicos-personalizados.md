# 21 — Públicos personalizados (custom audiences)

Un **público personalizado** (custom audience) es una lista de gente que YA interactuó contigo: visitó tu web, te escribió por Instagram, vio tu video o te compró. Se crean en Ads Manager → Audiences → Create audience → Custom audience. Lee este módulo cuando vayas a montar retargeting (ver 23), exclusiones (ver 24) o semillas de lookalike (ver 22) — estos públicos son la materia prima de las tres cosas, y en 2026 valen más por eso que como targeting de inclusión.

## Catálogo: una por una

| Fuente | Qué captura | Ventana | Requiere |
|---|---|---|---|
| **Website (Dataset)** | Visitantes por página, evento del Dataset o tiempo en sitio | 1-180 días | Dataset/píxel instalado (ver 14) |
| **Customer list** | Tu base de clientes/leads (CSV con email/teléfono) | N/A (la subes tú) | Datos propios + consentimiento (ver 28/29) |
| **Engagement FB/IG** | Interactuó con tu página FB o perfil IG: like, comentario, mensaje, guardado, visita al perfil | Hasta 365 días según fuente — **verifica los límites vigentes en TU Ads Manager**, Meta los cambia | Página/perfil conectados |
| **Video viewers** | Vio X% de un video tuyo (3s, 25%, 50%, 75%, 95%) | 1-365 días | Videos publicados o en ads |
| **Shopping** | Interactuó con tu tienda de FB/IG: vio producto, agregó al carrito | Variable | Catálogo/Shop activo |
| **Lead form** | Abrió o envió tu formulario instantáneo (ver 52) | Hasta 90 días | Campañas de leads |
| **Instant Experience / Eventos / App** | Abrió tu experiencia, respondió a evento, usó tu app | Variable | Cada fuente activa |

Nota de nomenclatura 2026: el "Píxel" ahora se llama **Dataset** en Events Manager (el Pixel ID = Dataset ID, paraguas de píxel + CAPI + offline). Los públicos de website salen del Dataset.

Detalles que importan:

- **Website**: puedes segmentar por URL ("visitó /producto-melena"), por evento (ViewContent, AddToCart, Purchase) o por percentil de tiempo ("top 25% por tiempo en sitio" — visitantes más enganchados, buena semilla LAL). Ventana = días hacia atrás desde hoy, rodante.
- **Video viewers** — la joya barata: corres un video con objetivo de alcance/reproducciones (CPM bajo, $8.000-18.000 COP típico en CO), y los que vieron 50%+ ya son público tibio SIN necesitar clic ni Dataset. Ideal para cuentas sin tráfico web: calientas con video, retargeteas a los viewers. 95% visto = casi tan caliente como un visitante web.
- **Engagement**: incluye gente que te escribió por Messenger/DM — en LatAm, donde todo pasa por DM y WhatsApp, este público suele ser el más caliente que tienes. Ojo: el **view-through** se quitó del API el 12-ene-2026, así que no infles el valor de "vio mi contenido pero no clickeó" en el reporte de retargeting (ver 23).
- **Customer list**: formato, hashing y match rate en el módulo 28. Resumen: CSV con email y teléfono con código de país (+57...), Meta lo cruza con sus usuarios. Es first-party data: el activo que iOS y las cookies muriendo NO te quitan (ver 28).

## Recetas listas para copiar

**"Calientes de IG" (negocio que vende por DM):**
Audience → Instagram account → "Everyone who engaged" → 30 días. Úsala para retargeting con oferta directa, o 90-180d como semilla de LAL si tu engagement es de calidad (no de giveaways).

**"Abandonadores de carrito" (e-com):**
Incluir: evento AddToCart, 7 días. Excluir: evento Purchase, 7 días. Resultado: agregó al carrito esta semana y no compró. Mensaje: recordatorio + remover fricción (envío, garantía, contraentrega), ver 23.

**"Vieron el producto y se fueron":**
Incluir ViewContent 14d, excluir AddToCart 14d y Purchase 14d. Mensaje: prueba social y diferenciador, no la misma foto de producto.

**"Audiencia de contenido" (sin web):**
Video viewers 50%+ de tus 3-5 mejores videos, 30-60d + engagers IG 30d, apilados en el mismo ad set. Tu "tibio" de arranque.

**"Leads que no cerraron":**
Lead form submitters 90d (o customer list de leads del CRM) excluyendo compradores. Mensaje de objeciones + urgencia honesta.

**"Llegaron por WhatsApp y se enfriaron" (CTWA, ver 50/53):**
Engagers de Messenger/IG 30d + (si tu bot guarda los números) customer list de leads que escribieron y no compraron. El cierre real es follow-up en el chat (ventas_lushows), el ad solo re-toca.

## Para qué usar cada público

- **Retargeting** (ver 23): website 7-30d, carrito 7-14d, engagers 30d, video viewers 50%+ 30d.
- **Exclusiones** (ver 24): compradores (Purchase 30-180d o customer list), leads ya captados.
- **Semillas de lookalike** (ver 22): compradores con valor > compradores > leads calificados > top 25% tiempo en sitio. Los engagers genéricos son semilla floja.
- **Existing customers en Advantage+ Sales** (ver 12/24): tu customer list de clientes alimenta el **cap de clientes existentes** (ponlo 25-30%) para que la campaña priorice gente NUEVA.

Nota 2026: con Advantage+ y campañas consolidadas, muchos de estos públicos ya NO se usan como targeting de inclusión (el broad los alcanza solo) sino como **exclusiones y semillas**. No montes 8 ad sets, uno por público — eso fragmenta (ver 10).

## Mapa de decisión: ¿inclusión, exclusión o semilla?

Mismo público, distinto uso según para qué sirva. Úsalo como referencia rápida:

| Público | ¿Incluir (retarget)? | ¿Excluir? | ¿Semilla LAL? |
|---|---|---|---|
| Compradores (Purchase/lista) | No (salvo recompra/reactivación) | SÍ, siempre, en venta | La mejor (value-based, ver 22) |
| Carrito sin compra 7d | SÍ (mensaje de objeción) | de prospecting (opcional) | floja |
| ViewContent 14-30d | SÍ (prueba social) | — | media |
| Engagers IG/FB 30d | SÍ (tibio) | — | floja si vienen de sorteos |
| Video viewers 50%+ 30-60d | SÍ (tibio de contenido) | — | media-buena si engancharon |
| Leads sin cerrar 90d | SÍ (objeciones) | de lead-gen nuevo | buena si calificaron |
| Top 25% tiempo en sitio | SÍ | — | buena (proxy de intención) |

La regla mental: **el comprador se EXCLUYE de todo lo de venta y se usa como SEMILLA; el tibio se INCLUYE en retargeting; el frío lo trae el broad solo.**

## Consentimiento: condición de uso (Data Source Declaration)

Antes de subir o usar una customer list, esa data necesita autorización del titular que mencione publicidad/remarketing (Habeas Data Colombia / LGPD Brasil, ver 29). Meta está rodando la **Data Source Declaration**: quien use custom audiences deberá declarar el origen del dato y probar consentimiento; las audiencias sin consentimiento demostrable quedan inelegibles. No es opcional ni futuro lejano — verifica el estado en tu Business Manager y captura el consentimiento desde la venta #1.

## Nombra tus audiencias para no enloquecer

Convención sugerida: `[FUENTE] - [DETALLE] - [VENTANA]`. Ejemplos:
- `WEB - Todos - 30d`
- `WEB - ATC sin Purchase - 7d`
- `IG - Engagers - 30d`
- `VID - 50%+ lanzamiento - 60d`
- `LISTA - Compradores 2026 - actualizada jun`
- `LAL 1-5% - Compradores con valor - CO`

En 6 meses tendrás 20+ audiencias; sin convención no sabrás cuál apunta a qué ad set ni cuál lista está vieja. El sufijo de fecha en las listas manuales te recuerda re-subirlas (ver 28).

## Errores comunes — blacklist

- Crear el público de website ANTES de instalar el Dataset y esperar que se llene retroactivamente: solo captura desde que existe. Dataset primero, siempre.
- Usar ventanas máximas "para que sea más grande": un visitante de hace 170 días ya no se acuerda de ti; es frío disfrazado de tibio. Tamaño ≠ calidad.
- Retargetear a engagers de un sorteo: interactuaron por el premio, no por tu producto. CPA horrible garantizado.
- Olvidar la exclusión de compradores en el público de carrito: le muestras "¡termina tu compra!" a quien ya pagó. Molesto y caro.
- Páginas de FB e IG sin conectar al Business Manager correcto: tus públicos de engagement salen vacíos y no sabes por qué.
- Confiar en ventanas de memoria ("engagement es 365d seguro"): Meta ajusta límites sin avisar; verifica en el panel al crear el público.
- Usar una customer list sin consentimiento de publicidad: con la Data Source Declaration rodando, queda inelegible y te arriesgas a sanción SIC (ver 29).
- Inflar el valor del retargeting con view-through: ya no existe en el API desde ene-2026; juzga por click.
