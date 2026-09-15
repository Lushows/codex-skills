# 50 — TikTok Shop a fondo

Lee este módulo cuando un cliente te pregunte "¿puedo vender DENTRO de TikTok?", cuando quieras decidir entre cerrar por TikTok Shop o por WhatsApp, o antes de prometerle a alguien en Colombia que va a vender con la pestaña Shop. Este módulo abre el bloque de comercio (51–59). La primera lección es la más importante y la más incómoda: **verifica disponibilidad antes de prometer**. TikTok es **descubrimiento** (ver 00): la gente entra a entretenerse, no a comprar. El Shop convierte ese descubrimiento en venta sin sacar al usuario de la app — cuando existe en tu país. En Colombia, hoy (jun-2026), todavía no se confirma. Así que la mitad de este módulo es para cuando SÍ está, y la otra mitad es para construir el plan B honesto: cerrar por WhatsApp.

## Qué es TikTok Shop (y qué NO es)

TikTok Shop = comercio **dentro de la app**. El usuario descubre, paga y recibe sin salir de TikTok. No es un link a tu web — es un checkout nativo. Tiene cuatro puntos de venta (superficies):

| Superficie | Qué es | Dónde aparece |
|---|---|---|
| **Product Showcase** | Vitrina de productos en tu perfil | Pestaña fija en tu perfil de marca |
| **Pestaña Shop** | Marketplace dentro de la app (como un Mercado Libre interno) | Tab inferior, navegación de compra |
| **Video Shopping** | Producto etiquetado dentro de un video | En el feed, con icono de carrito (ver 51) |
| **Live Shopping** | Producto a la venta durante un live | Mientras transmites en vivo (ver 53) |

TikTok cobra **comisión por venta** (no por clic). El porcentaje varía por país y categoría — típicamente entre **5% y 8% del GMV** (Gross Merchandise Value, en español *valor bruto de mercancía*: el valor total vendido antes de descontar nada). Esa comisión es ADEMÁS de lo que gastes en ads y ADEMÁS de la pasarela de pago. Tres mordiscos a tu margen, no uno. Métela en tus números con `economist_lushows` antes de fijar precio.

Lo que TikTok Shop NO es: no es un reemplazo de tu web si vendes high-ticket o necesitas explicar mucho (ver 58). No está en todo país (ver abajo). Y no te exime de medir bien — aun con Shop, hay que cerrar el loop con pixel y Events API (ver 57).

### Por qué importa el frame "descubrimiento"

En Meta o Google el usuario suele tener algo de intención (te buscó, o está en un feed donde espera ofertas). En TikTok el usuario **no estaba comprando nada**. El Shop funciona cuando el video genera el antojo en el segundo 0–3 y el checkout está a un toque de distancia. Por eso el ticket bajo-medio de impulso (moda, belleza, gadgets, snacks) es el dulce de TikTok Shop, y el high-ticket es su veneno.

## Disponibilidad en LatAm — verifica Colombia ANTES de prometer

Esto es lo que separa a un media buyer honesto de uno que vende humo. La disponibilidad de TikTok Shop por país, a jun-2026:

| País | Estado (jun-2026) |
|---|---|
| EE.UU., Reino Unido | Activo y maduro |
| Sudeste Asiático (Indonesia, Tailandia, Vietnam, etc.) | Activo (el mercado más grande del mundo) |
| **México** | Activo (lanzó en 2025) |
| **Brasil** | Activo |
| **Colombia** | **POR CONFIRMAR — verifícalo en el momento** |
| Resto de LatAm (Chile, Perú, Argentina) | Por confirmar / en expansión |

Para un cliente colombiano: **no asumas que TikTok Shop está disponible**. Verifícalo así, en orden, el mismo día que vas a prometer algo:

1. Entra a TikTok Seller Center (`seller.tiktok.com`) y mira si Colombia aparece como región de registro.
2. Revisa si la cuenta del cliente ve la opción **"Crear tienda" / "Set up shop"** desde su país y con su documento.
3. Pregunta dentro de TikTok Ads Manager si el objetivo **Product Sales con fuente TikTok Shop** está disponible para la cuenta (si no aparece la fuente, no hay Shop).
4. Si dudas, busca el anuncio oficial de TikTok del mes — los lanzamientos por país cambian rápido y un blog viejo te puede engañar.

**Si TikTok Shop NO está en Colombia:** el camino LatAm es **TikTok → WhatsApp**. Descubre en TikTok, cierra en WhatsApp (ver 55, y el oficio de cerrar en `ventas_lushows` módulo 82). No le digas al cliente "vas a vender en la app" si la app no lo deja vender en su país. Decirlo y que falle quema tu credibilidad y su plata. Para GastroLatam, por ejemplo, el cierre de la Calculadora de Costos ($10.000 COP) hoy va por WhatsApp con mensaje prellenado, no por Shop.

## Setup de TikTok Shop (cuando SÍ está disponible)

Pasos exactos, en orden. No saltes pasos.

1. **Registro de seller** en TikTok Seller Center con datos del negocio: RUT, Cámara de Comercio, cuenta bancaria a nombre del negocio. Persona natural o jurídica según el país.
2. **Verificación de identidad y del negocio** — suben documentos; puede tardar de **horas a varios días**. No prometas fecha de lanzamiento hasta tener la cuenta verificada.
3. **Conecta el catálogo** (ver 56) — productos con foto, título humano, precio, stock, atributos limpios. Sin catálogo sano no hay ads de Shop.
4. **Configura pagos y envíos** — pasarela local (en MX: tarjeta, OXXO; en BR: Pix, tarjeta) y reglas de despacho (transportadora, costo, cobertura).
5. **Activa Product Showcase** en el perfil y empieza a **etiquetar productos en videos orgánicos** ANTES de pautar. El algoritmo del Shop aprende de la señal orgánica; si llegas en frío con puro ad, aprende lento y caro.
6. **Recién entonces** lanza Video Shopping Ads (ver 51) o GMV Max (ver 52).

Tabla de tiempos realistas para no sobrevender al cliente:

| Etapa | Tiempo típico |
|---|---|
| Registro + verificación | 1–7 días |
| Catálogo cargado y aprobado | 1–3 días (depende de #productos) |
| Orgánico sembrando señal | 1–2 semanas antes de escalar ads |
| Ads de Shop con datos para decidir | 7–14 días desde el lanzamiento |

## El plan B siempre listo: TikTok descubre, WhatsApp cierra

Aunque el Shop exista, ten siempre el camino WhatsApp armado, porque: (a) muchos productos cierran mejor conversando, (b) el high-ticket no va por checkout (ver 58), y (c) si el Shop se cae o no aprueban un producto, no te quedas sin canal. El handoff TikTok → WhatsApp (mensaje prellenado, etiqueta de origen, contacto en <5 min) está en 55. La medición de esas ventas que pasan fuera de la app, subiendo la conversión de vuelta con Events API, está en 57.

## Cómo enrutas según el caso

- E-commerce ticket bajo-medio, Shop disponible → **VSA / GMV Max** (ver 51, 52, 80).
- Moda con stock rotativo → **Live Shopping + catálogo automatizado** (ver 53, 56, 84).
- Servicios / high-ticket → **lead gen calificado**, no Shop (ver 54, 58).
- Negocio local de barrio → **WhatsApp / visita**, no Shop (ver 59).
- Sin Shop en el país → **WhatsApp** siempre (ver 55).
- Construir la web/checkout fuera del Shop → `desingweb-lushows`.
- Validar si los números cierran con la comisión incluida → `economist_lushows`.

## Errores comunes — blacklist

- **Prometer TikTok Shop en Colombia sin verificar.** Si no está, el cierre va por WhatsApp (ver 55). Verifica primero, siempre, el mismo día.
- **Olvidar la comisión por venta en los números.** 5–8% de GMV + pasarela + ads se comen tu margen; cárgalo al precio con `economist_lushows`.
- **Lanzar ads de Shop con catálogo sucio.** Productos sin foto o sin stock arruinan VSA y GMV Max (ver 56).
- **Pautar antes de tener orgánico en el Shop.** El algoritmo de Shop aprende de tu Product Showcase; siembra orgánico 1–2 semanas primero.
- **Usar TikTok Shop para high-ticket que necesita explicación.** Alto ticket = lead calificado, no checkout impulsivo (ver 58).
- **No verificar la cuenta de seller y esperar resultados.** Sin verificación, los ads de Shop ni arrancan.
- **Tratar el Shop como tu única medición.** Aun con Shop, cierra el loop con pixel y Events API y valida contra ventas reales (ver 57).
- **No tener el plan B WhatsApp armado.** Si el Shop falla o no llega a tu país, te quedas sin canal de cierre.
