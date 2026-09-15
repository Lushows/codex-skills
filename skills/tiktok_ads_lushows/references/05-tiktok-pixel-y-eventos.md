# 05 — TikTok Pixel y eventos

Lee este módulo antes de gastar el primer peso en campañas de conversión, o cuando tus campañas "no aprenden" y el algoritmo parece ciego. El Pixel es el sensor que le dice a TikTok qué pasó después del clic: ¿agregó al carrito? ¿compró? ¿dejó sus datos? Sin Pixel, le pides a TikTok que optimice a ventas sin poder verlas — imposible. Esta es la base de toda la medición; su complemento server-side está en el módulo siguiente (ver 06). En 2026 lo correcto es **Pixel + Events API juntos** desde el día uno, no el Pixel solo.

## Qué es el Pixel y por qué es innegociable

El **TikTok Pixel** es un fragmento de código JavaScript que vive en tu sitio web. Cada vez que un visitante hace algo importante (ver producto, comprar), el Pixel "dispara" un evento y se lo cuenta a TikTok. Con esos datos, el algoritmo aprende **a qué tipo de persona mostrarle tu anuncio** para conseguir más de esa acción (ver 13 sobre aprendizaje). El Pixel también captura el **`ttclid`** (el click ID de TikTok que viaja en la URL cuando alguien llega desde un anuncio), que es la pieza que luego conecta la conversión con el clic exacto — el equivalente del `ctwa_clid` de Meta o el OCI de Google (ver 06).

Sin Pixel solo puedes optimizar a métricas tontas (vistas, clics) que no pagan. Con Pixel optimizas a la acción que sí importa (ver 14).

## Cómo instalarlo

| Método | Cuándo usarlo | Cómo |
|---|---|---|
| **Integración de partner** | Tienes Shopify, WooCommerce, etc. | Conecta TikTok desde la app de la plataforma; mapea eventos |
| **Pixel manual (código)** | Web propia / landing custom | Copia el código base del Events Manager y pégalo antes de `</head>` |
| **Google Tag Manager** | Ya usas GTM | Crea una etiqueta con el ID del Pixel y dispara por triggers |

Hay dos modos de Pixel: el **estándar** (tú decides cuándo disparar cada evento) y el **Developer/manual mode** (control total por código, necesario para pasar parámetros de coincidencia limpios). Para e-commerce con plataforma, el estándar basta; para una landing custom con cierre por WhatsApp, conviene el manual para inyectar el `event_id` y los datos hasheados.

Después de instalar, **verifica** con la extensión **TikTok Pixel Helper** (Chrome): abre tu web, navega, y confirma que los eventos disparan en verde antes de pautar. No confíes en "lo instalé y debería andar": el 30% de las cuentas nuevas tiene un evento mal mapeado que nadie revisó.

## Los eventos estándar (los que importan)

| Evento estándar | Cuándo dispara | Para qué optimizas |
|---|---|---|
| **CompletePayment** | Se concreta una compra | E-commerce, el evento rey (ver 14) |
| **AddToCart** | Agrega producto al carrito | Optimización media-funnel cuando hay pocas ventas |
| **InitiateCheckout** | Empieza el checkout | Señal intermedia útil |
| **Lead** | Deja sus datos (formulario, WhatsApp) | Generación de leads, servicios (ver 54) |
| **ViewContent** | Ve una página de producto | Tope de funnel, públicos de retargeting |
| **Subscribe / Contact** | Suscripción o contacto | Según tu modelo de negocio |

Regla: optimiza siempre al evento **más cercano a la plata** que tenga suficiente volumen. Si hay ventas, **CompletePayment**. Si arrancas y hay pocas, sube un escalón (AddToCart o InitiateCheckout) hasta tener datos (ver 14). La meta es ~50 eventos del tipo optimizado por semana por ad group para salir de aprendizaje (ver 13).

## El caso colombiano: medir el Lead de WhatsApp

En Colombia el cierre suele ser por WhatsApp, y ahí mucha gente "no mide nada" porque el chat no es una página web. Solución: dispara un evento **Lead** en el momento del clic al botón de WhatsApp (o cuando el usuario llega a la página puente que abre el chat). Mejor aún, pasa el `ttclid` dentro del enlace `wa.me` o a tu CRM/bot, y reporta el Lead de vuelta por Events API cuando la conversación califica (ver 06, 54). Así TikTok optimiza a "personas que de verdad escriben", no a clics vacíos.

## Deduplicación y prioridad de eventos

Cuando uses Pixel **y** Events API a la vez (lo correcto, ver 06), el mismo evento puede llegar dos veces. Para que TikTok no lo cuente doble:

| Concepto | Qué hacer |
|---|---|
| **event_id** | Envía un identificador único e idéntico desde Pixel y Events API por cada evento; TikTok los une y descarta el duplicado |
| **Prioridad de eventos** | Por límites de iOS/SKAN, define qué evento es más importante (normalmente CompletePayment o Lead) para que se reporte primero (ver 06) |
| **Mapeo limpio** | No dispares "CompletePayment" en una página que no es de compra. Eventos sucios = optimización sucia |

La deduplicación bien hecha es lo que separa una cuenta amateur de una profesional: sin `event_id`, inflas tus conversiones y el algoritmo aprende mal, viendo "ventas" donde solo hubo doble conteo (ver 64 sobre ROAS real).

## Errores comunes — blacklist

- **Pautar conversión sin Pixel instalado.** El algoritmo optimiza a ciegas. Fix: instala y verifica con Pixel Helper antes.
- **No verificar que los eventos disparen.** Crees que mides y no mides nada. Fix: revisa en Events Manager + Pixel Helper en verde.
- **Optimizar a CompletePayment sin volumen.** El algoritmo no sale de aprendizaje. Fix: sube un escalón (AddToCart) hasta tener datos (ver 14).
- **Pixel + Events API sin event_id.** Cuentas conversiones dobles, ROAS inflado. Fix: envía el mismo event_id en ambos (ver 06).
- **Disparar eventos en páginas equivocadas.** Datos sucios = mala optimización. Fix: mapea cada evento a su página real.
- **Olvidar el dominio verificado.** Bloquea eventos web. Fix: verifica el dominio en Business Center primero (ver 04).
- **No instrumentar el Lead de WhatsApp.** En Colombia el cierre es por chat y no lo mides. Fix: dispara Lead al click de WhatsApp y pasa el `ttclid` (ver 06, 54).
- **Instalar solo el Pixel "y ya".** Pierdes 20-40% de señal en iOS. Fix: súmale Events API desde el día uno (ver 06).
