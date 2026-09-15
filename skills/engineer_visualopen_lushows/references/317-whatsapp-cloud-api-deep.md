# 317 · WhatsApp Cloud API a fondo (templates, Flows, ventana 24h, pricing per-mensaje)

> [[41-whatsapp-cloud-api]] te dio el mapa; este baja al detalle que decide si tu bot es rentable o sangra:
> categorías de template que aprueban, Flows cifrados, la mecánica exacta de la ventana de 24h y el billing per-mensaje que rige desde jul-2025.

## Templates: categorías y qué aprueba
Toda plantilla cae en **MARKETING, UTILITY o AUTH**, y Meta **reclasifica** si tu UTILITY huele a promo (te la sube a MARKETING → más cara). Reglas que muerden:

| Categoría | Cuándo úsala | Costo (LatAm aprox 2026) | Trampa |
|---|---|---|---|
| UTILITY | post-compra, recordatorio de pedido, OTP de transacción | $0.004–$0.046, **gratis si hay CSW abierta** | si incluye CTA de venta → te la pasan a MARKETING |
| AUTH | códigos de login/2FA | $0.004–$0.046, con tiers por volumen | plantilla rígida, sin texto libre |
| MARKETING | ofertas, recompra fría, reactivación | $0.025–$0.137, **siempre se cobra** | baja engagement → baja quality rating → baja tier |

Aprobación: minutos a horas. Rechazos típicos: URLs acortadas, `{{1}}` al inicio/fin sin texto, contenido que parece phishing, samples de variables vacíos. Variables posicionales `{{1}}` van en `components[].parameters` al enviar — el orden importa. Componentes disponibles: **header** (texto/imagen/video/doc), **body**, **footer**, **buttons** (quick-reply o CTA url/phone). Versiona el nombre del template (`pedido_confirmado_v2`) porque editar uno aprobado lo manda a re-aprobación y puede romper envíos en vuelo.

### Quality rating y tiers de envío
Cada template tiene un **quality rating** (verde→amarillo→rojo) que se degrada con bloqueos/reportes/baja lectura. Rojo → Meta pausa el template. En paralelo tu número tiene un **messaging tier** (1K→10K→100K→ilimitado destinatarios únicos/24h) que sube con buen rating y volumen. Marketing agresivo a listas frías quema ambos: cuida a quién mandas, no solo qué.

## Flows: forms server-driven cifrados
**Flow** = mini-app dentro del chat (date pickers, dropdowns, multi-pantalla) para capturar pedido/dirección sin salir de WhatsApp. Dos modos:
- **Sin endpoint** (estático): pantallas predefinidas, data vuelve en el mensaje final. Simple, suficiente para un formulario de pedido.
- **Con data endpoint** (dinámico): cada interacción hace `POST` a tu backend. El payload viene **AES-128 cifrado** + clave AES cifrada con tu **RSA pública** + IV. Descifras, respondes con `{version:"3.0", screen, data}` re-cifrado en Base64. Acciones: `navigate` (ir a pantalla X), `data_exchange`, `complete` (cerrar Flow). Meta exige **health check** y subir tu llave pública. [no verificado: versión de data-API exacta, citan "3.0"]

Para un bot de tienda LatAm: el Flow estático cubre 90% (capturar nombre+dirección+producto) sin montar cripto. Reserva el endpoint para stock/precio en vivo.

## Ventana de 24h (CSW) — la regla que define el costo
Cada **mensaje entrante del usuario** abre/renueva 24h de **free-form** (texto, media, interactive, todo gratis). Al cerrarse: **solo templates aprobados** te dejan reabrir. Implicación de diseño:
- Responde rápido y mantén al usuario escribiendo → todo gratis dentro de la ventana.
- Si el cliente calla 24h+ y necesitas retomarlo (recompra), pagas un template MARKETING o UTILITY para reabrir. Por eso la recompra fría tiene costo real — presupuéstalo.
- **UTILITY dentro de CSW abierta = $0.** Truco: confirma el pedido con UTILITY mientras la ventana sigue viva, no después.

## Pricing per-mensaje 2025+
**Desde 1-jul-2025 Meta cobra por MENSAJE entregado, no por conversación** (el modelo per-conversación quedó deprecado). Se cobra por **categoría de template + país del destinatario**. Service/free-form dentro de la ventana = gratis. Tiers por volumen bajan el precio de UTILITY/AUTH (definidos por mercado: Brasil e India tienen tablas propias; Brasil suele ser el más caro de LatAm).

Cálculo mental para tu bot: el grueso del tráfico (cliente pregunta → Addrian responde) es **gratis** porque cae en CSW. Solo pagas las plantillas de reactivación/recompra y los OTP. Un bot bien diseñado mantiene >90% del volumen en mensajes gratis.

## Registro del número y onboarding
Antes de enviar nada: el número va en una **WABA** (WhatsApp Business Account) dentro de Business Manager, verificas el negocio, y registras el número con un PIN de **two-step verification**. Un número ya usado en la app de WhatsApp normal debe **migrarse** (lo desconecta de la app). En modo dev solo escribes a destinatarios en lista de prueba (error `#131030` si no está). Publicar la app y completar la verificación de negocio levanta esos límites. Token: **System User permanente**, nunca el temporal de 24h del dashboard.

## Webhooks: lo no obvio
- Devuelve **200 en <5s** o Meta reintenta y te throttlea; procesa async.
- `statuses[]` trae `sent/delivered/read/failed` con `pricing.category` y `billable` → **úsalo para medir gasto real** por conversación, no estimes.
- URLs de descarga de media expiran ~5 min y requieren el bearer → baja a tu storage YA (ver gotcha 2 de [[41-whatsapp-cloud-api]]).

## Cierre
Profundiza el handoff a humano y los flujos conversacionales en [[318-chatbot-conversational-ux]]. Cruza con [[41-whatsapp-cloud-api]] y [[321-omnichannel-inbox]].
