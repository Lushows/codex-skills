# 06 — Conversions API (CAPI)

La Conversions API (CAPI) envía tus eventos de conversión directamente desde tu servidor (o desde la plataforma de tu tienda) a Meta, en paralelo al píxel/dataset del navegador. Es la mitad servidor de tu medición. Lee este módulo justo después del 05: en 2026 una cuenta sin CAPI compite con un brazo amarrado, y con la atribución solo-clic (ver 16) la señal de servidor pesa más que nunca.

## Por qué es obligatoria post-iOS 14.5

Con ATT (App Tracking Transparency, el aviso de Apple "¿Permitir que la app rastree?"), la mayoría de usuarios de iPhone dijo que no. Resultado: el píxel del navegador pierde una fracción grande de eventos (iOS + bloqueadores + cookies restringidas). Lo que te da CAPI:

1. **Recuperas señal perdida**: el servidor reporta la compra aunque el navegador haya callado. Más conversiones visibles = mejor optimización y reportes menos mentirosos.
2. **Mejor matching**: desde el servidor puedes adjuntar email, teléfono y nombre del cliente (hasheados), que el píxel no siempre tiene. Meta identifica a la persona con más certeza y el algoritmo aprende de mejor calidad.
3. **Resiliencia**: no depende de cookies ni de extensiones del usuario. Con la atribución solo-clic de 2026, perder el clic por un bloqueador es perder la venta del reporte; el servidor lo recupera.

## EMQ: Event Match Quality

El **EMQ score** mide, evento por evento, qué tan bien puede Meta emparejar tus eventos de servidor con personas reales. Escala **1-10**, visible en Events Manager → tu dataset → pestaña del evento.

- **Piso práctico 2026: ≥ 8.** (Antes ≥6 bastaba; en la era Andromeda la calidad de datos pesa tanto que el píxel-solo, EMQ 3–5, ya no compite — ver `actualizacion-2026-06`.) Apunta a mandar **8+ identificadores hasheados** por evento.
- 6-7 = mejorable; **8-10 = competitivo** (típico de Shopify nativo o CAPI con teléfono+email+external_id+fbp/fbc).
- En LatAm tu palanca más fácil es el **teléfono** (`ph`), que casi siempre tienes por WhatsApp y sube mucho el match.

**Cómo subir el EMQ** — manda más identificadores por evento, todos hasheados con SHA-256 (las integraciones nativas hashean por ti):

| Parámetro | Qué es | Impacto |
|---|---|---|
| `em` (email) | Email del cliente, hasheado | Alto |
| `ph` (teléfono) | Teléfono E.164 (`573001234567`), hasheado | Alto — en LatAm casi siempre lo tienes (WhatsApp) |
| `fn`/`ln` (nombre/apellido) | Hasheados | Medio |
| `fbp` / `fbc` | Cookies de Meta: id del navegador y el id del clic en el anuncio | Alto — captúralas en tu web y guárdalas con el pedido |
| `client_ip_address` + `client_user_agent` | IP y navegador | Base mínima |
| `external_id` | Tu ID interno de cliente | Medio |
| `ct`/`st`/`zp`/`country` | Ciudad/depto/código postal/país, hasheados | Bajo-medio (suma señales) |

Regla práctica: con solo IP + user agent rondas EMQ 3-4. Súmale `ph` y `em` y saltas a 6-7. Añade `fbp`/`fbc` + `external_id` y llegas a 8-9. Esa diferencia es la mitad del rendimiento de la cuenta.

## Deduplicación píxel + CAPI

Como mandas cada evento dos veces (navegador + servidor), Meta debe saber que son EL MISMO evento. La regla: **mismo `event_name` y mismo `event_id` en ambos lados**. El píxel manda `fbq('track','Purchase',{...},{eventID:'pedido-12345'})` y el servidor manda `event_id: 'pedido-12345'`. Meta se queda con uno y descarta el duplicado. Sin esto, reportas el doble de ventas y la cuenta "parece" rentable sin serlo. Verifica en Events Manager: el evento debe aparecer como "Procesado" desde ambas fuentes con deduplicación activa.

## Opciones de implementación (de fácil a pro)

0. **CAPI de un clic (Meta-hosted, 2026)** — en Events Manager → pestaña Resumen → botón **"Activate Conversions API"**: Meta levanta el server-side por ti y pone el `event_id` para deduplicar solo. Lo más fácil que existe; se amplió a anunciantes solo-píxel ~may-2026 (ver `actualizacion-2026-06`). Recuerda: "Píxel" hoy se llama **"Dataset"** (el Pixel ID = Dataset ID).
1. **Integración nativa** — Shopify (app oficial de Meta: dataset + CAPI + dedup automáticos), WooCommerce (plugin Meta/FB for WooCommerce), Tiendanube, etc. Si existe para tu plataforma, ÚSALA. 30 minutos, EMQ alto, cero código.
2. **Conversions API Gateway** — instancia preconfigurada (p. ej. en AWS vía Stape o similar) que recibe los eventos del píxel y los reenvía como servidor. Sin tocar tu backend; costo de hosting bajo (~10-50 USD/mes).
3. **GTM server-side** — un contenedor de Google Tag Manager corriendo en servidor: máxima flexibilidad para webs custom con varios destinos (Meta, GA4, TikTok). Requiere setup técnico.
4. **Código directo contra la API** — tu backend hace POST a `graph.facebook.com/v23.0/{dataset_id}/events` con el access token del dataset. Control total; para devs (si vas por aquí y hay app de por medio, engineer_visualopen_lushows tiene el stack).

## CAPI para WhatsApp / mensajería (clave en LatAm)

¿Negocio que cierra por WhatsApp sin web transaccional? Existe CAPI para mensajería: reportas a Meta la venta que ocurrió en el chat para que las campañas CTWA optimicen por compradores reales, no por "personas que escriben". El estándar 2026:

- Captura el **`ctwa_clid`** (el id de clic del anuncio Click-to-WhatsApp) que llega en el primer mensaje del cliente.
- Envía los eventos del chat por CAPI con dataset `business_messaging` y `messaging_channel: whatsapp`, ligándolos al `ctwa_clid`.
- Así Meta sabe qué anuncio generó la conversación Y la venta, y Andromeda optimiza por compradores. Detalle completo en 53.

## Tabla de decisión: qué método de CAPI elegir

| Tu situación | Método recomendado | Esfuerzo | EMQ esperado |
|---|---|---|---|
| Shopify / WooCommerce / Tiendanube | Integración nativa | 30 min | 8-10 |
| Web custom, sin dev disponible | CAPI de un clic (Meta-hosted) o Gateway | 1-2 h | 6-8 |
| Web custom con dev | GTM server-side o código directo | 1-2 días | 8-10 (si mandas ph+em+fbp/fbc) |
| Cierra todo por WhatsApp, sin web | CAPI de mensajería + `ctwa_clid` | dev (ver 53) | depende del match telefónico |

Para Colombia, donde casi siempre tienes el teléfono del cliente, el `ph` hasheado es tu mejor amigo de EMQ; priorízalo en cualquier método que elijas.

## Por qué la atribución solo-clic (2026) sube la apuesta de CAPI

Hasta ene-2026 Meta contaba conversiones view-through (alguien vio el ad, no hizo clic, y compró días después). En ene-2026 quitaron esas ventanas (7d/28d view) del API: ahora solo cuenta el **clic**. Consecuencia: si un usuario hace clic pero su navegador bloquea la cookie del clic (`fbc`), esa venta se cae del reporte... salvo que el servidor la reporte con buen matching. CAPI con EMQ alto es lo que recupera esas ventas que antes el view-through "perdonaba". Con menos ventanas de atribución, la calidad de tu señal de servidor es directamente tu CPA aparente (ver 16).

## Receta: verificación post-implementación (20 minutos)

1. Events Manager → tu dataset → Resumen: cada evento clave debe mostrar DOS fuentes (Navegador + Servidor).
2. Haz una compra/lead de prueba y confírmala en Test Events con su `event_id`.
3. Revisa "Deduplicación": los eventos servidor deben marcar duplicados descartados; si no, los `event_id` no coinciden.
4. Abre el EMQ de Purchase/Lead: si está < 8, agrega `ph` y `em` hasheados, `fbp`/`fbc` y `external_id` al payload del servidor.
5. Agenda recordatorio mensual: tokens y plugins se rompen sin avisar.

## Errores comunes — blacklist

- **"Con el píxel me basta"**: pierdes la señal de iOS y compites contra anunciantes que sí la recuperan; con atribución solo-clic 2026, tu CPA aparente sube sin que entiendas por qué.
- **CAPI sin deduplicación**: ventas dobles en reportes → decisiones sobre datos inflados → escalas lo que no funciona.
- **Conformarte con EMQ 5-6**: el piso 2026 es 8; revisa el score tras cada cambio y suma identificadores.
- **Datos sin hashear en código propio**: la API los rechaza o, peor, expones datos personales (las integraciones nativas hashean solas).
- **Programar tu propia CAPI teniendo Shopify/Woo**: reinventas con bugs lo que la integración nativa hace mejor y gratis.
- **Olvidar `fbp`/`fbc` en el evento de servidor**: son de los identificadores que más suben el matching y casi nadie los guarda con el pedido.
- **CTWA sin `ctwa_clid` + CAPI de mensajería**: optimizas por "gente que escribe", no por compradores; tiras plata (ver 53).
- **Configurar CAPI y no volver a mirar Events Manager**: tokens vencen, plugins se rompen en updates; revisa la fuente de eventos una vez al mes.
