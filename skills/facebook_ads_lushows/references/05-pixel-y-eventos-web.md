# 05 — Píxel (Dataset) y eventos web

El píxel de Meta —hoy técnicamente un **"Dataset"** en Events Manager (el Pixel ID = Dataset ID desde 2026)— es un fragmento de código JavaScript en tu web que le cuenta a Meta qué hace cada visitante: qué páginas vio, qué agregó al carrito, qué compró. Esa señal es la comida del algoritmo: sin ella, Meta optimiza a ciegas. Lee este módulo al montar una cuenta nueva o cuando los números de Ads Manager no cuadren con la realidad.

## Qué es y cómo se instala

El dataset se crea en Events Manager (Administrador de eventos → Conectar datos → Web). Un solo dataset por negocio, dentro del BM del negocio (ver 04). Opciones de instalación:

| Método | Para quién | Cómo |
|---|---|---|
| **Integración nativa** (Shopify, WooCommerce, Wix, Tiendanube) | E-commerce en plataforma | App/plugin oficial de Meta: instala dataset + eventos + CAPI en minutos. La opción default si existe |
| **Google Tag Manager (GTM)** | Webs custom con GTM | Etiqueta Custom HTML con el código base + etiquetas por evento disparadas por triggers (clic en botón, página de gracias) |
| **Código directo** | Landings a mano (ej. hechas con desingweb-lushows) | Pegar el snippet base antes de `</head>` en TODAS las páginas + `fbq('track', ...)` por evento |

## Eventos estándar (los que importan)

Meta entiende ~17 eventos estándar; estos son los que usarás:

| Evento | Cuándo se dispara | Parámetros clave |
|---|---|---|
| `PageView` | Cada página cargada (lo trae el código base) | — |
| `ViewContent` | Vista de página de producto | `content_ids`, `value`, `currency` |
| `AddToCart` | Clic en "agregar al carrito" | `content_ids`, `value`, `currency` |
| `InitiateCheckout` | Inicio del checkout | `value`, `currency`, `num_items` |
| `Purchase` | Página de gracias / confirmación de pago | `value`, `currency`, `content_ids` **(value y currency obligatorios)** |
| `Lead` | Formulario enviado / clic a WhatsApp con intención | `value` opcional |
| `CompleteRegistration` | Registro de cuenta completado | — |

Ejemplo copy-paste de una compra de 89.000 COP:

```html
<script>
  fbq('track', 'Purchase', {
    value: 89000,
    currency: 'COP',
    content_ids: ['excel-gastro-v1'],
    content_type: 'product'
  }, {eventID: 'pedido-12345'});
</script>
```

Fíjate en el `eventID`: es lo que permite deduplicar contra CAPI (ver 06). Ponlo desde el día uno.

- **Parámetros**: `value` (valor monetario), `currency` (`COP`), `content_ids` (SKU del producto, debe coincidir con el catálogo si usas DPA, ver 56). Sin `value`, no hay ROAS en reportes ni optimización por valor.
- **Eventos custom**: `fbq('trackCustom', 'ClicWhatsApp', {...})` para acciones que no calzan en los estándar. Útiles para audiencias; para OPTIMIZAR conviértelos en evento estándar o configúralos como conversión personalizada.
- **Jerarquía**: optimiza siempre por el evento más profundo que tenga volumen suficiente (ver 07, 14). Purchase > InitiateCheckout > AddToCart > ViewContent. En negocios WhatsApp-first, el "Purchase" real ocurre en el chat — eso se resuelve con CAPI de mensajería (ver 06 y 53).

## Aggregated Event Measurement (AEM) y los 8 eventos

Tras iOS 14.5, Meta limita a **8 eventos web priorizados por dominio verificado** (Events Manager → Configuración de eventos agregados). Ordénalos del más valioso (Purchase) al menos: el sistema solo optimiza bien por los de arriba para usuarios iOS que rechazaron rastreo. Por eso verificar el dominio (ver 04) no es opcional. Si tienes 12 eventos disparándose pero solo 8 cuentan, prioriza Purchase, InitiateCheckout, AddToCart y tu Lead/ClicWhatsApp.

Detalle que muerde: cuando cambias el orden de los 8 eventos, Meta **congela la configuración ~72 horas** mientras propaga el cambio. Durante esa ventana la entrega a iOS puede tambalear. No reordenes eventos en plena campaña caliente ni un viernes; hazlo en setup o en valle de tráfico. Y si vendes valor (optimizas por ROAS), activa **Value Optimization** en el evento Purchase dentro de AEM: sin eso, el sistema cuenta compras pero no su valor para usuarios iOS.

## Configuración de eventos por tipo de negocio (plantilla)

| Negocio | Evento de optimización | Eventos a instalar (orden AEM) |
|---|---|---|
| E-commerce con web | Purchase | Purchase, InitiateCheckout, AddToCart, ViewContent, PageView |
| Producto digital (caso GastroLatam) | Purchase (o Lead si poco volumen) | Purchase, InitiateCheckout, Lead, ViewContent |
| Servicios / leads | Lead | Lead, CompleteRegistration, ViewContent, PageView |
| WhatsApp-first sin checkout web | Lead / ClicWhatsApp (custom→estándar) | Lead, ViewContent + CAPI de mensajería (ver 53) |

Regla de elección: optimiza por el evento más profundo que junte ~50/semana (ver 07, 14). Si Purchase no llega a volumen, baja a InitiateCheckout o Lead, no te quedes optimizando por un evento que el sistema ve 6 veces por semana.

## Audiencias que nacen del dataset

Más allá de optimizar, cada evento alimenta **custom audiences** automáticas que usarás en remarketing (ver 23): visitantes de la web (PageView), gente que vio un producto (ViewContent), carritos abandonados (AddToCart sin Purchase), compradores (Purchase, para excluir o vender recompra). Sin el código base en TODAS las páginas, estas audiencias nacen vacías. Por eso "el píxel solo en la home" no solo rompe reportes: te deja sin munición de remarketing. Instala el base en todo el sitio y los eventos en sus páginas, y deja que las audiencias se llenen desde el día uno aunque aún no pautes remarketing.

## Conversiones personalizadas (cuando el estándar no alcanza)

Si tu acción clave no calza en los 17 eventos estándar (ej. "clic en botón de Nequi", "llegó a la página de gracias del producto X"), crea una **conversión personalizada** en Events Manager: defínela por URL o por un evento custom + regla. Te deja optimizar y reportar por ella como si fuera estándar. Útil para separar productos o pasos finos del embudo. Límite: hay un máximo de conversiones personalizadas por dataset, no las desperdicies en cosas triviales.

## Verificación (no publiques sin esto)

1. **Meta Pixel Helper** (extensión de Chrome): navega tu web y confirma que cada evento se dispara una sola vez, en la página correcta, con parámetros.
2. **Test Events** (Events Manager → Probar eventos): pones tu URL, navegas, y ves los eventos llegar en vivo con sus parámetros. Haz una compra de prueba completa.
3. Caso típico de bug: `Purchase` que se dispara al INICIAR el pago (no al confirmar) o que se dispara doble (plugin + código manual) → tus reportes mienten al doble.
4. En Events Manager → Resumen, compara el conteo de Purchases de la última semana contra tus ventas reales: una brecha mayor al 20-30% (varía por mix iOS/Android) indica dataset roto o falta de CAPI (ver 06).

## El píxel solo ya no basta (en 2026 mucho menos)

Desde iOS 14.5 (ATT: el aviso de "permitir rastreo" de Apple), bloqueadores y restricciones de cookies, el píxel del navegador pierde una parte importante de los eventos. En 2026 Meta endureció dos cosas que lo agravan: la **atribución es solo-clic** (quitaron view-through 7d/28d del API en ene-2026, ver 16) y el **EMQ piso subió a 8** (ver 06). La solución es enviar los eventos TAMBIÉN desde tu servidor con la **Conversions API — siguiente parada obligatoria: módulo 06**. Dataset + CAPI deduplicados es el estándar mínimo profesional; un anunciante solo-píxel hoy compite con un brazo amarrado.

## Errores comunes — blacklist

- **Pautar sin dataset "mientras tanto"**: cada peso gastado sin señal es aprendizaje que regalas; el dataset va ANTES del primer anuncio.
- **Purchase sin `value`/`currency`**: Ads Manager no puede calcular ROAS y la optimización por valor queda ciega.
- **Eventos duplicados** (plugin + GTM + código manual a la vez): reportas el doble de ventas; elige UNA fuente por evento (y usa `eventID` para deduplicar con CAPI).
- **No priorizar los 8 eventos en AEM**: para usuarios iOS optimizas por el evento equivocado; ordénalos por valor.
- **Dataset solo en la home**: el código base va en todas las páginas; sin él no hay PageView ni audiencias de visitantes.
- **Crear el dataset en el BM equivocado** (el de la agencia): el historial de datos queda secuestrado (ver 04).
- **No probar con Test Events antes de lanzar**: descubres el evento roto tres semanas y 2 millones de COP después.
- **Optimizar por ViewContent teniendo volumen de Purchase**: le pides al sistema mirones, y mirones te trae.
