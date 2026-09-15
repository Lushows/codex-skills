# 96 — Integración con el stack

Lee este módulo cuando los leads llegan pero "se enfrían", cuando Google reporta clics pero tú no sabes cuáles cerraron, o cuando quieras que la venta real cerrada por WhatsApp **vuelva** a Google para que el algoritmo optimice hacia plata, no hacia clics. En LatAm el patrón es: Google **captura la intención** → manda el lead al WhatsApp → un humano cierra. El problema es que Google **no se entera** de qué lead cerró, así que optimiza a ciegas. Este módulo conecta las tuberías: CRM, server-side tagging, Customer Match y automatización para que el circuito se cierre. En 2026, con cookies de terceros muriendo y Consent Mode obligatorio, los **datos propios (first-party)** son el activo que decide si Google aprende bien o mal (ver 28, 29).

## El circuito completo (qué conecta con qué)

```
Anuncio Google → clic → landing → lead (form/WhatsApp)
   → CRM (guarda el lead + el GCLID/GBRAID/WBRAID)
   → humano cierra la venta (ventas_lushows)
   → CRM marca "vendido" + valor en COP
   → OCI sube la venta a Google (ver 53)
   → Smart Bidding optimiza hacia clientes que SÍ compran (ver 13)
   → Customer Match excluye compradores y busca parecidos (ver 25)
```

La pieza que casi todos saltan es el **GCLID** (Google Click ID): un código que Google pega a cada clic. Si tu landing/CRM lo captura y guarda con el lead, después puedes decirle a Google "este clic exacto se volvió venta de $X". Sin GCLID guardado, no hay OCI bueno. Nota 2026: para tráfico de iOS/apps y por privacidad, Google usa también **GBRAID/WBRAID** (identificadores agregados) — guárdalos igual; el plugin/tag de captura los toma todos.

## Las piezas del stack

| Pieza | Qué es | Para qué la quieres |
|---|---|---|
| **CRM** | Donde viven tus leads y su estado (HubSpot, Pipedrive, Kommo, hoja de cálculo, tu propio sistema) | Guardar lead + GCLID + estado + valor de venta |
| **GTM server-side** (etiquetado del lado servidor) | Google Tag Manager corriendo en TU servidor, no solo en el navegador | Medición más confiable, resiste bloqueadores/cookies/ITP (ver 28) |
| **Enhanced Conversions** (conversiones mejoradas) | Manda datos hasheados (email/teléfono) para recuperar conversiones perdidas | Tapa el hueco de cookies/iOS/Consent Mode (ver 06) |
| **Consent Mode v2** | Señales de consentimiento que ajustan el tracking según permiso del usuario | Obligatorio en muchos casos; sin él, modelado peor (ver 06, 29) |
| **Customer Match** (segmentación por lista de clientes) | Subes tu lista de clientes/leads a Google como audiencia | Excluir compradores, buscar parecidos, retargetear (ver 25) |
| **OCI** (Offline Conversion Import) | Subes la venta cerrada offline de vuelta a Google | Que el algoritmo optimice hacia ventas reales (ver 53) |
| **n8n / Make / Zapier** (automatización no-code) | Conectan apps entre sí con "recetas" sin programar | Mover datos entre WhatsApp, CRM y Google solo |
| **WhatsApp Cloud API** (Meta) | WhatsApp programable | Recibir el lead, responder, marcar estados |
| **Google Ads API / Conversion API** | Subir conversiones de forma programática | Automatizar el OCI sin cargar CSV a mano |

## Server-side tagging y Customer Match: el blindaje de medición

**Server-side tagging (GTM server, ver 28):** en vez de que todo el tracking ocurra en el navegador del usuario (donde lo bloquean adblockers, ITP de Safari, Consent Mode), parte ocurre en TU servidor. Resultado: mides más conversiones reales y más estable, y controlas qué datos salen. Es trabajo técnico (rutea a `engineer_visualopen_lushows` para montar el contenedor server-side en Cloud Run/VPS bien), pero el pago es medición que no se cae cuando cambian las reglas de privacidad.

**Customer Match desde el CRM (ver 25):** subes tu lista de clientes a Google (con consentimiento, datos hasheados localmente antes de enviarlos). Tres usos directos:
1. **Excluir** a quien ya compró el producto de pago único (ej. la calculadora $10.000 COP) — que no le sigas pagando anuncios.
2. **Audiencias similares / "lookalike"** (parecidos a tus mejores clientes) como señal en PMax/Demand Gen (ver 90, 41).
3. **Retargeting** a leads que no cerraron, con un mensaje distinto.

Es **first-party data** (datos propios, los que tú mismo recolectaste con permiso) — el activo más valioso en 2026 porque no depende de cookies de terceros que ya están muriendo. Combínalo con OCI: la lista dice "estos son mis clientes"; el OCI dice "este clic exacto se volvió venta".

## Que el lead no se enfríe: automatización

El lead caliente se enfría en minutos. Automatización mínima que vale oro (con n8n/Make/tu sistema):

1. **Lead entra por WhatsApp/form → respuesta automática inmediata** (segundos, no horas). El bot saluda, el humano sigue (rutea a `ventas_lushows` para el guion; el proyecto GASTROWHATS ya hace esto con Claude).
2. **Lead se guarda en CRM con GCLID + fuente + campaña** automáticamente.
3. **Notificación al vendedor** para que cierre rápido (GASTROWHATS notifica al operador, ver su CLAUDE.md).
4. **Cuando el vendedor marca "vendido"** → automatización dispara OCI a Google con el GCLID y el valor en COP (ver 53).
5. **Periódicamente (diario/semanal), sincroniza la lista de compradores a Customer Match** para excluirlos/buscar parecidos.

El loop cerrado es la diferencia entre un Google Ads que "trae curiosos" y uno que **aprende quién compra de verdad** y va por más como ellos. Sin OCI/CRM, Smart Bidding optimiza hacia el clic más barato, que suele ser el peor cliente.

## Mini-receta n8n (lead WhatsApp → CRM → OCI)

| Paso | Nodo | Qué hace |
|---|---|---|
| 1 | Webhook (WhatsApp Cloud API) | Recibe el mensaje entrante + número |
| 2 | Set / Function | Toma el GCLID de la URL/sesión guardada y lo une al lead |
| 3 | CRM (HTTP/nodo nativo) | Crea/actualiza el lead con GCLID, fuente, estado="nuevo" |
| 4 | (Humano cierra) | El vendedor marca "vendido" + valor en el CRM |
| 5 | Trigger por estado="vendido" | Dispara nodo Google Ads API → sube OCI con GCLID + valor + timestamp |
| 6 | Cron diario | Exporta compradores → actualiza audiencia Customer Match |

Para montar esto sin que se rompa (auth, hashing, reintentos, timeouts), rutea a `engineer_visualopen_lushows`.

## Capa por capa: qué resuelve cada pieza y por qué importa en 2026

| Capa | Pieza | Problema 2026 que resuelve |
|---|---|---|
| Captura | GCLID/GBRAID en landing+CRM | Sin esto no sabes qué clic cerró; OCI imposible |
| Medición navegador | Google tag + GA4 + Consent Mode v2 | Cookies de terceros muriendo; consentimiento obligatorio |
| Medición servidor | GTM server-side | Adblockers/ITP/iOS te ocultan conversiones reales (ver 28) |
| Recuperación | Enhanced Conversions | Reconstruye conversiones perdidas con datos hasheados (ver 06) |
| Verdad de venta | OCI desde CRM | Optimizar hacia VENTA, no hacia clic barato (ver 53, 64) |
| Audiencia propia | Customer Match | First-party reemplaza al targeting de cookies que muere (ver 25) |
| Velocidad | Automatización n8n/Make | El lead caliente se enfría en minutos |

La lectura estratégica: en 2026 quien mide con **datos propios + server-side + OCI** tiene una ventaja real sobre quien mide solo con el pixel del navegador, porque ese pixel ve cada vez menos. No es lujo técnico; es la diferencia entre un Smart Bidding que aprende y uno que adivina (ver 13). El que monta esta tubería bien le cobra más al cliente y retiene mejor (ver 95).

## Errores comunes — blacklist

- **No capturar el GCLID (ni GBRAID/WBRAID) en la landing/CRM.** Sin él no puedes hacer OCI bien y Google nunca sabe qué clic cerró (ver 53).
- **Medir "clic a WhatsApp" como conversión final.** El algoritmo te llena de curiosos; la conversión real es la VENTA cerrada, súbela con OCI (ver 64, 53).
- **No subir las ventas offline de vuelta a Google.** El loop queda abierto; Smart Bidding optimiza a ciegas hacia clics baratos (ver 13).
- **Dejar el lead sin respuesta inmediata.** Se enfría en minutos; automatiza la primera respuesta (rutea a `ventas_lushows`).
- **No excluir a los que ya compraron** vía Customer Match. Pagas anuncios a clientes que ya tienes, sobre todo en pago único (ver 25).
- **Montar todo client-side y nada server-side.** Pierdes conversiones por bloqueadores/cookies/ITP; server-side tagging las recupera (ver 28, rutea a `engineer_visualopen_lushows`).
- **Subir listas a Customer Match sin consentimiento ni hashing.** Problema legal/política; usa solo datos propios con permiso (ver 06, 08, 29).
- **Ignorar Consent Mode v2.** Sin señal de consentimiento, el modelado de conversiones empeora y en algunos casos te frenan (ver 06).
