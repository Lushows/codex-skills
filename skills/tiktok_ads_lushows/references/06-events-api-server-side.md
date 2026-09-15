# 06 — Events API (server-side)

Lee este módulo cuando tus conversiones del Pixel se vean más bajas de lo que vendes realmente, o cuando quieras que tu cuenta optimice como las de los profesionales. Desde los cambios de privacidad de iOS (2021 en adelante), el Pixel solo en el navegador pierde una parte enorme de los datos: bloqueadores, cookies rechazadas, Safari/iOS borrando seguimiento. La **Events API** manda los eventos desde tu servidor, directo a TikTok, esquivando esas pérdidas. Es el equivalente al CAPI de Meta. Va de la mano con el Pixel (ver 05), no lo reemplaza — los dos juntos, deduplicados, son el estándar 2026.

## El problema que resuelve

| Antes (solo Pixel en navegador) | Con Events API (server-side) |
|---|---|
| iOS/Safari bloquean cookies → eventos perdidos | El servidor reporta directo, sin depender del navegador |
| Bloqueadores de anuncios matan el Pixel | El servidor no se bloquea |
| Conversiones subreportadas → algoritmo aprende mal | Datos más completos → mejor optimización (ver 13) |
| ROAS se ve peor de lo real | ROAS más fiel a la realidad (ver 64) |

En la práctica LatAm: una cuenta que solo usa Pixel puede estar perdiendo **20-40%** de sus conversiones reales. La Events API recupera buena parte de eso, y eso se traduce en CPAs reportados más bajos, mejor entrega y un algoritmo que aprende con la imagen completa en vez de con la mitad.

## Cómo funciona (sin tecnicismos)

El navegador del cliente dispara el Pixel (lado del usuario). En paralelo, **tu servidor** (o tu plataforma, o un intermediario) envía el mismo evento por la Events API (lado del servidor). TikTok recibe ambos, los une por **event_id**, y se queda con un solo conteo (ver 05 sobre deduplicación). El truco está en que cada vía cubre lo que la otra pierde: el navegador a veces se bloquea, el servidor nunca; pero el servidor solo sabe lo que tu sistema le cuente, así que necesitas pasarle buenos datos.

| Vía de instalación | Para quién |
|---|---|
| **Integración nativa de plataforma** (Shopify, etc.) | La más fácil; actívala y listo |
| **Events API Gateway** | TikTok te da una solución casi sin código, alojada |
| **Implementación directa por código** | Web custom; tu dev manda los eventos al endpoint de TikTok |
| **Partner de servidor** (GTM Server-Side, Stape, Segment) | Si ya usas un contenedor server-side |

Para Lushows (no técnico): empieza por la **integración nativa** de tu plataforma. Si tu landing es custom, pídele a tu dev que implemente la Events API con `engineer_visualopen_lushows` como referencia, o usa un **Gateway** (lo más rápido sin código). No lo dejes para "la fase 2 del proyecto": es parte del setup base (ver 00).

## Event Matching Quality (EMQ): la nota de tu medición

TikTok califica qué tan bien identifica a la persona detrás de cada evento, según los **parámetros de coincidencia** que le mandes (email, teléfono, etc., siempre hasheados/encriptados antes de enviar). A más y mejores parámetros, mejor optimización:

| Parámetro de coincidencia | Impacto en EMQ |
|---|---|
| Email (hasheado SHA-256) | Alto |
| Teléfono (hasheado) | Alto — clave en LatAm donde el cierre es WhatsApp |
| IP + User Agent | Medio |
| External ID (tu ID de cliente) | Alto |
| `ttclid` (click ID de TikTok) | Muy alto — conecta el evento con el clic exacto |

Busca un EMQ alto (idealmente "Good"/"Great" en el Events Manager). Un EMQ pobre desperdicia la Events API: tienes el canal server-side abierto pero le mandas datos flacos, así que TikTok no logra emparejar la conversión con la persona ni con el anuncio. La forma de subirlo: manda **teléfono + email hasheados + `ttclid` + External ID** en cada evento. En Colombia, el teléfono hasheado es oro porque es el dato que sí tienes cuando el cierre es por WhatsApp.

## El `ttclid`: cerrar el lazo Search/FYP → WhatsApp

El `ttclid` es la pieza que evita que tus ventas se reporten como "tráfico directo" o "desconocido". Flujo correcto en Colombia: el usuario hace clic en el ad → llega a tu landing con `?ttclid=...` en la URL → ese `ttclid` se guarda → al escribir por WhatsApp o convertir, lo reportas de vuelta por Events API junto con el teléfono hasheado. Así TikTok sabe que ESE clic generó ESA venta, aunque hayan pasado por un chat fuera de la web. Es el mismo concepto del `ctwa_clid` de Meta y el OCI de Google: sin él, el descubrimiento de TikTok queda invisible para la atribución (ver 03 sobre efecto demanda).

## SKAN y la atribución en iOS

En iOS, Apple limita el seguimiento individual con **SKAdNetwork (SKAN)** — un sistema agregado y con retraso. TikTok lo usa para reportar conversiones de usuarios iOS que no dieron permiso de seguimiento. Por eso:

- Define la **prioridad de eventos** (ver 05): qué conversión es la más importante para que SKAN la reporte primero.
- Espera **retrasos y conteos agregados** en iOS; no cuadra al peso con tu backend.
- La atribución default de TikTok es **7 días post-clic / 1 día post-vista** (ver 16); ajústala según tu ciclo de compra — ticket impulsivo aguanta ventanas cortas, ticket alto necesita las completas.

## Errores comunes — blacklist

- **Pensar que Events API reemplaza al Pixel.** Se usan JUNTOS y se deduplican. Fix: instala ambos con el mismo event_id (ver 05).
- **No enviar el mismo event_id.** Conversiones dobles, ROAS inflado. Fix: un event_id idéntico desde Pixel y servidor (ver 05).
- **Ignorar el EMQ.** Tienes Events API pero mal alimentada. Fix: manda email/teléfono hasheados + `ttclid` + External ID; busca EMQ alto.
- **Mandar datos sin hashear.** Riesgo de privacidad y de rechazo. Fix: hashea email/teléfono (SHA-256) antes de enviar.
- **No pasar el `ttclid` al WhatsApp.** El descubrimiento queda invisible y subvaloras TikTok. Fix: propaga el `ttclid` landing → chat → Events API (ver 03).
- **Esperar conteo exacto en iOS.** SKAN es agregado y con retraso. Fix: acepta el modelado de iOS; mira tendencias, no centavos (ver 64).
- **No definir prioridad de eventos.** SKAN reporta lo equivocado. Fix: prioriza CompletePayment/Lead (ver 05).
- **Dejarlo para "después".** Sin Events API tu cuenta optimiza con datos a medias. Fix: es parte del setup base, no un extra (ver 00).
