# 96 — Integración con el stack

Lee este módulo cuando tus leads de TikTok lleguen y se enfríen sin que nadie los atienda, cuando vendas por WhatsApp y no sepas si esas ventas "vuelven" a TikTok como señal, o cuando quieras automatizar el flujo lead→atención→venta sin hacerlo a mano. La pauta no termina cuando alguien clickea: termina cuando el sistema **sabe** que esa persona compró y se lo dice a TikTok. Eso es el stack. TikTok **descubre**; el stack se asegura de que el descubrimiento se convierta en venta y de que la venta vuelva como señal para que Smart+ (ver 90) optimice mejor.

## Las piezas y para qué sirve cada una

| Pieza | Qué es | Qué resuelve |
|---|---|---|
| **TikTok Pixel** | Código en tu landing que registra acciones (ver página, lead, compra) | Señal básica de conversión web (ver 06) |
| **Events API** | Envío de eventos **servidor a servidor** a TikTok (no depende del navegador) | Señal que no se pierde por bloqueadores/iOS; más precisa (ver 06) |
| **ttclid** | El click ID de TikTok que viaja en la URL del clic | El "hilo" que conecta el clic con la venta posterior (offline) |
| **Conversiones offline** | Subir ventas que pasaron fuera de la web (ej: cerró por WhatsApp) | Que TikTok sepa que ese lead SÍ compró aunque no fue en la web |
| **CRM** | Donde viven tus contactos/leads y su estado | Que ningún lead se pierda y midas el funnel real |
| **n8n / Make / Zapier** | Automatizadores que conectan apps sin código | Pegar TikTok ↔ WhatsApp ↔ CRM automáticamente |
| **WhatsApp API** | API de WhatsApp para enviar/recibir mensajes automáticos | Atender al lead en segundos, no en horas |

El **Events API** (servidor a servidor) es prioritario en 2026: los bloqueadores de anuncios, el navegador y las restricciones de privacidad rompen el pixel del lado del cliente. El Events API manda el evento desde TU servidor directo a TikTok, así no se pierde. Lo ideal es **pixel + Events API juntos** (deduplicados por `event_id`) para máxima señal. El detalle de instalación está en 06.

### El papel del ttclid (la pieza que la gente olvida)

Cuando alguien hace clic en tu ad, TikTok mete un parámetro `ttclid` en la URL de destino. Si capturas ese `ttclid` (en la landing, o lo pasas al link de WhatsApp) y lo guardas junto al lead en tu CRM, después puedes mandar la conversión offline **atada a ese clic específico**. Sin `ttclid`, la conversión offline es más difusa (TikTok la asocia por aproximación). Con `ttclid`, le dices a TikTok exactamente cuál clic terminó en venta — y ahí la optimización vuela. Captúralo siempre que puedas.

## El problema que resuelve: que el lead no se enfríe y la conversión vuelva

Hay dos fugas que matan la rentabilidad en LatAm:

**Fuga 1 — el lead se enfría.** Alguien ve tu TikTok, hace clic, escribe por WhatsApp… y nadie responde en 30 minutos. Para entonces ya se fue con la competencia. La velocidad de respuesta es ventas perdidas (→ `ventas_lushows` para el cierre).

**Solución:** automatiza la atención. Flujo típico:

```
TikTok ad → clic a WhatsApp (o lead form) 
   → n8n/Make detecta el lead nuevo 
   → captura ttclid + datos del lead
   → mensaje automático de bienvenida en segundos (WhatsApp API) 
   → lead entra al CRM con etiqueta "TikTok" + ttclid 
   → notifica al vendedor para cierre humano
```

**Fuga 2 — la conversión no vuelve a TikTok.** Vendes por WhatsApp, fuera de la web, así que el pixel nunca registró la compra. TikTok no sabe que ese lead convirtió → optimiza a ciegas, te trae más leads que clickean pero no compran (ver 16).

**Solución:** manda la conversión de vuelta. Cuando el vendedor marca "vendido" en el CRM, un automatizador (n8n/Make) dispara un evento de **conversión offline / Events API** a TikTok con el dato de esa venta (y el `ttclid` si lo capturaste). Así TikTok aprende a quién parecido buscar. Esto es lo que separa una cuenta que escala de una que se estanca.

### Mapa del círculo cerrado

| Paso | Quién lo hace | Dato que viaja |
|---|---|---|
| 1. Clic en ad | Usuario | ttclid en la URL |
| 2. Llega a WhatsApp/landing | Automatizador captura | ttclid + teléfono/email |
| 3. Bienvenida automática | WhatsApp API | — (velocidad) |
| 4. Entra al CRM | Automatizador | fuente "TikTok" + ttclid |
| 5. Vendedor cierra | Humano (→ `ventas_lushows`) | marca "vendido" + valor |
| 6. Conversión vuelve | Automatizador → Events API | evento "compra" + valor + ttclid |
| 7. TikTok reoptimiza | Smart+ (ver 90) | busca gente parecida al comprador real |

## Cómo armarlo sin ser técnico

No necesitas programar. El patrón con **n8n** (open-source, barato, autohospedable) o **Make/Zapier** (sin código, más caro):

1. **Trigger:** lead nuevo desde TikTok Lead Form o un clic-a-WhatsApp que cae en tu API de WhatsApp.
2. **Acción 1:** capturar el `ttclid` y crear/actualizar el contacto en el CRM con la fuente "TikTok" y la fecha.
3. **Acción 2:** enviar mensaje automático de bienvenida por WhatsApp API (que el lead sienta respuesta inmediata).
4. **Acción 3 (la clave):** cuando el estado del CRM pase a "vendido", disparar el evento de conversión offline / Events API a TikTok con el valor de la venta y el `ttclid`.
5. **Acción 4:** notificar al vendedor humano para el cierre real.

Esto cierra el círculo: TikTok descubre → automatización atiende rápido → humano cierra → la venta vuelve como señal → TikTok optimiza mejor. Para el guion de cierre y manejo de objeciones, ese trabajo es de `ventas_lushows`. Para que la landing donde cae el clic convierta, → `desingweb-lushows`.

Si tu pipeline de automatización usa IA (clasificar leads, responder con LLM, calificar) y el costo de esas llamadas se dispara, optimízalo en `optimizer_tokens_lushows` — no aquí.

## Datos first-party: la base de todo

Todo esto se apoya en tus **datos propios (first-party)**: tu lista de clientes, sus compras, su comportamiento. Cuanto mejor los captures y los devuelvas a TikTok (vía Events API/offline, con `ttclid` cuando se pueda), mejor optimiza el sistema y menos dependes del targeting (ver 28 sobre first-party). En 2026 con la privacidad apretando, el que tiene buenos datos propios y los reinyecta gana; el que solo confía en el pixel del navegador pierde señal. Estos mismos datos alimentan el omnicanal (ver 97) y el matching de Smart+ (ver 90).

## Errores comunes — blacklist

- **Solo pixel del navegador, sin Events API.** Pierdes señal por bloqueadores/privacidad; usa ambos deduplicados (ver 06).
- **No capturar el ttclid.** La conversión offline queda difusa; con ttclid le dices a TikTok cuál clic vendió.
- **Lead que llega y nadie responde en minutos.** Se enfría y se va; automatiza la bienvenida (→ `ventas_lushows` para cerrar).
- **Vender por WhatsApp y nunca devolver la conversión a TikTok.** El sistema optimiza a ciegas; manda conversión offline (ver 16).
- **Optimizar a "ver contenido"/clic en vez de la venta real** porque la venta no vuelve al pixel. Cierra el círculo offline.
- **Armar todo a mano** (copiar leads del panel al CRM uno por uno). Automatiza con n8n/Make o se cae el sistema.
- **No etiquetar la fuente "TikTok" en el CRM.** Sin eso no sabes qué canal vende de verdad (ver 97 sobre atribución).
- **Ignorar tus datos first-party.** Son la base de la optimización en 2026; captúralos y reinyéctalos (ver 28).
