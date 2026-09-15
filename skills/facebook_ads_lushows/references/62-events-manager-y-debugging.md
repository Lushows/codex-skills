# 62 — Events Manager y debugging de medición

El Events Manager es la sala de máquinas de tu medición: ahí ves si los eventos (Purchase, AddToCart, Lead, etc.) están llegando desde tu web o servidor a Meta. Si esto está roto, el algoritmo optimiza a ciegas y todos tus números mienten. Léelo ANTES de gastar tu primer peso y cada vez que un número "no cuadre" (ver 61, prerequisito de diagnóstico). Actualizado jun-2026 con los cambios de señal que subieron el piso de calidad.

**Cambio de nombre que confunde a todos (2026):** el "Píxel" ahora se llama **Dataset** en Events Manager (el Pixel ID = Dataset ID; es el paraguas que junta píxel de browser + CAPI + eventos offline). Si un tutorial dice "píxel" y la UI dice "Dataset", es lo mismo (ver `actualizacion-2026-06`).

Acceso: Business Manager → Todos los recursos → **Administrador de eventos** (business.facebook.com/events_manager2).

## Las 3 zonas que importan

1. **Overview (Resumen)**: por cada Dataset ves los eventos recibidos en los últimos 28 días, su volumen, el método de conexión (Browser = píxel, Server = CAPI) y el **EMQ** (Event Match Quality: 0–10, qué tan bien Meta identifica QUIÉN hizo el evento — sube enviando email/teléfono/nombre hasheados por CAPI, ver 06). **El piso práctico subió a EMQ ≥8 en 2026** (antes 6): en la era Andromeda/GEM la calidad de datos pesa tanto que píxel-solo (EMQ 3–5) ya no compite en la subasta. En LatAm el **teléfono hasheado es oro** porque casi todo el tráfico se identifica por celular.
2. **Test Events (Probar eventos)**: prueba en vivo. Copia el código de test (algo como `TEST12345`), abre tu web en otra pestaña agregando `?test_event_code=TEST12345` si usas CAPI (o navega normal: el píxel de browser aparece solo al detectar tu navegador), haz el recorrido completo (ver producto → carrito → compra de prueba) y verifica que CADA evento aparezca con sus parámetros correctos.
3. **Diagnostics (Diagnóstico)**: avisos automáticos de Meta (eventos sin deduplicar, parámetros faltantes, caídas de volumen). Revísalo mensual — muchos avisos son menores, pero "deduplication issue", "missing value parameter" y "EMQ low" son graves y cuestan rendimiento silencioso.

## CAPI: el piso de 2026

CAPI (Conversions API) envía los eventos desde TU servidor a Meta, no desde el navegador del usuario — sobrevive a adblockers, iOS sin tracking y banners de consentimiento. En 2026 dejó de ser "lo avanzado" y pasó a ser el piso. Tres formas de montarla, de menos a más técnica:
- **CAPI de un clic (Meta-hosted)**: botón **"Activate Conversions API"** en Events Manager → Meta levanta el server-side y pone el `event_id` para dedup solo. Se amplió a anunciantes solo-píxel ~may-2026. Es la vía recomendada para una pyme sin equipo técnico.
- **Conversions API Gateway**: sin código, lo aloja un partner.
- **CAPI propia**: tu sistema dispara el evento (ideal para WhatsApp y casos a medida, ver 06 y abajo).

## Debugging: los 3 fallos clásicos

### Fallo 1: el evento no llega
Checklist en orden:
- ¿El píxel base está en TODAS las páginas? Verifica con **Meta Pixel Helper** (extensión de Chrome): ícono azul con número = detectado; rojo/amarillo = error.
- ¿Adblock o banner de consentimiento lo bloquea? Prueba en incógnito sin extensiones; si solo falla con consent, tu CMP no dispara el píxel tras aceptar.
- ¿El evento tiene el nombre EXACTO estándar? Es `Purchase`, no `purchase` ni `Compra`. Eventos custom no optimizan igual.
- ¿Es venta por WhatsApp? El píxel no ve el cierre en chat: el Purchase debe entrar por CAPI desde tu sistema (ver abajo) o medirse en CRM (ver 53).

### Fallo 2: evento duplicado (píxel + CAPI)
Si envías el mismo evento por browser Y por servidor, ambos deben llevar el MISMO `event_id` (y mismo `event_name`); Meta deduplica por esa pareja. Si los `event_id` difieren → cuentas la venta DOBLE → ROAS inflado y CPA falsamente barato → escalas algo que no rinde.
Verificación: en Test Events, haz una compra de prueba; debes ver el Purchase dos veces (Browser y Server) con la etiqueta **"Deduplicated"** en uno. Si aparecen ambos como procesados sin deduplicar, está roto. Usa **Payload Helper** (developers.facebook.com/docs/marketing-api/conversions-api/payload-helper) para validar el JSON del servidor. Nota: con CAPI de un clic Meta pone el `event_id` solo; con CAPI propia eres TÚ quien debe generar el mismo `event_id` en browser y servidor.

### Fallo 3: parámetros faltantes
`Purchase` sin `value` y `currency` = Meta sabe que vendiste pero no cuánto → no puede calcular ROAS ni optimizar por valor (ni usar **Minimum ROAS / ROAS Goal** como estrategia de puja, ver `actualizacion-2026-06`). Verifica en Test Events que cada Purchase llegue con `value: 120000, currency: "COP"` (valor real del pedido, en COP). Lo mismo aplica a `content_ids` para catálogo/Advantage+.

## WhatsApp / CTWA: el evento que casi nadie configura (y es el #1)

Si tu venta cierra en WhatsApp, por default Meta optimiza a "conversaciones iniciadas" → te trae saludadores, no compradores. El upgrade decisivo:
1. Tu bot captura el **`ctwa_clid`** (click id que llega cuando alguien inicia el chat desde un ad CTWA).
2. Cuando ese lead **califica o paga**, tu sistema dispara un evento CAPI con `action_source = business_messaging`, `messaging_channel: "whatsapp"` y el `ctwa_clid`.
3. Recién entonces Meta atribuye la venta al ad y puede optimizar por COMPRADORES.
Sin esos campos, Meta jamás ve la venta del chat y tu pauta optimiza al saludo (ver 53; implementación → engineer_visualopen_lushows / tu backend GASTROWHATS-AVISPA'O).

## Herramientas, resumen

| Herramienta | Para qué | Dónde |
|---|---|---|
| Meta Pixel Helper | Ver eventos de browser en vivo | Extensión Chrome |
| Test Events | Probar todo el recorrido + deduplicación | Events Manager → Probar eventos |
| Payload Helper | Validar formato del payload CAPI | Docs de Meta (web) |
| Diagnostics | Avisos automáticos de problemas | Events Manager → Diagnóstico |
| Graph API Explorer | Probar envíos CAPI a mano | developers.facebook.com (técnico) |

## Checklist de auditoría de medición (ANTES de pautar y luego mensual)

1. Pixel Helper en home, producto, carrito y checkout: píxel verde en todas.
2. Test Events: recorrido completo dispara PageView → ViewContent → AddToCart → InitiateCheckout → Purchase.
3. Purchase llega con `value` y `currency: COP` correctos (compara contra un pedido real).
4. Si hay CAPI: cada evento aparece por Browser y Server con "Deduplicated".
5. **EMQ de Purchase ≥8** (si <8: enviar email/teléfono/nombre/ciudad hasheados por CAPI, ver 06).
6. Diagnostics: cero avisos rojos sin resolver.
7. Volumen coherente: # de Purchases en Events Manager ≈ # de pedidos reales del backend (±20–30% por atribución; si difiere 2×, algo está roto, ver 64).
8. Eventos en incógnito y en celular (la mayoría del tráfico LatAm es móvil).
9. Dominio verificado en Business Manager y eventos priorizados (Aggregated Event Measurement) configurados.
10. Si vendes por WhatsApp: `ctwa_clid` capturado y evento `business_messaging` disparando al calificar/pagar (o asumido explícitamente que la verdad vive en el CRM, ver 53, 64).

## Síntoma → causa probable (chuleta rápida)

| Síntoma en Events Manager | Causa probable | Fix |
|---|---|---|
| Purchase con el doble de volumen que pedidos reales | Deduplicación rota (event_id) | Fallo 2 |
| Eventos solo "Browser", nada "Server" | CAPI no configurada o caída | Activar CAPI de un clic / revisar token (ver 06) |
| EMQ de Purchase <8 | CAPI sin email/teléfono hasheados | Enriquecer payload (ver 06) |
| Volumen cayó de golpe un día | Cambio en la web rompió el píxel, o consent nuevo | Pixel Helper + Test Events ese mismo día |
| Eventos llegan pero campañas no optimizan | value/currency faltantes o evento custom | Fallo 3 |
| Conversaciones suben pero "no compra nadie" | Falta evento `business_messaging`/`ctwa_clid` | Configurar CAPI de WhatsApp (arriba) |

## Errores comunes — blacklist
- Pautar semanas sin abrir nunca Events Manager ("el píxel lo instaló alguien alguna vez").
- Purchase sin value/currency: optimización y ROAS ciegos.
- Píxel + CAPI sin `event_id` compartido → ventas dobles y decisiones sobre datos inflados.
- Probar solo en tu PC con sesión iniciada y nunca en móvil/incógnito.
- Confundir "evento llega" con "evento llega con buena calidad": ignora el EMQ y pierdes rendimiento silenciosamente.
- Crear eventos custom ("CompraFinal") en vez de los estándar que el algoritmo entiende.
- Optimizar CTWA a "conversaciones iniciadas" para siempre: trae saludadores; el dinero está en el evento de calificación/compra por CAPI.
- Creer que CAPI ya no hace falta porque "tengo el píxel": en 2026 píxel-solo (EMQ bajo) ya no compite.
