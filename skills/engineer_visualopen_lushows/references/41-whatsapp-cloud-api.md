# 41 — WhatsApp Cloud API a fondo

Hosteada por Meta, vía **Graph API**. 2026: versión actual **v24.0** (oct-2025); **desde sep-2025 Meta rechaza
versiones < v22.0** → pinea reciente y súbela antes del deprecation (~2 años). Base:
`https://graph.facebook.com/v24.0/{PHONE_NUMBER_ID}/{resource}`.

## Identidad & tokens
Un **WABA** contiene phone numbers, cada uno con `PHONE_NUMBER_ID` (para `/messages`, `/media`) y `WABA_ID` (para
`/message_templates`). Tokens temporales del dashboard expiran en 24h — inútiles en prod. Crea un **System User** en
Business Manager → **token permanente** con scopes `whatsapp_business_messaging` + `whatsapp_business_management`.

## Webhook
Callback URL; Meta manda `GET` con `hub.mode`/`hub.verify_token`/`hub.challenge` — echo `hub.challenge` SOLO si el
verify token matchea. Suscribe la WABA al campo `messages`. Los `POST` entrantes traen
`entry[].changes[].value.messages[]` y `.statuses[]` (sent/delivered/read/failed). **Devuelve 200 rápido** y procesa async, o Meta reintenta y throttlea.

## Enviar
`POST /{PHONE_NUMBER_ID}/messages` con `messaging_product:"whatsapp"`:
```json
{ "messaging_product":"whatsapp","to":"57300...","type":"text","text":{"body":"Hola"} }
```
- **Media:** `type:"image|audio|video|document"` con `{"id":"<media_id>"}` (subido) o `{"link":"https://..."}` (HTTPS público alcanzable).
- **Interactive buttons** (max **3**); **lists** (hasta 10 secciones × 10 rows). **Location**: lat/long/name/address.

## Template messages (HSM) — lo único fuera de las 24h
Categorías **MARKETING, UTILITY, AUTH**. `POST /{WABA_ID}/message_templates` → Meta aprueba/rechaza (minutos-horas).
Variables posicionales `{{1}}`,`{{2}}` en `components[].parameters` al enviar.

## Ventana de 24h (CSW)
Cualquier mensaje entrante del usuario abre 24h para mandar **free-form** de cualquier tipo. Al cerrarse, solo **templates aprobados.**

## Media handling
Subir: `POST /{PHONE_NUMBER_ID}/media` (multipart) → `media_id`. Bajar: `GET /{media_id}` → URL corta (~5 min) que
requiere el bearer. Límites: imagen/audio ~5-16MB, video/docs hasta 100MB. **Voice notes = OGG/Opus mono** para que rendericen como burbuja de voz.

## Flows / Pricing 2026
**Flows** = forms server-driven (date pickers, dropdowns), data al **data endpoint** con payloads **AES-cifrados**.
**Desde jul-2025: billing per-MENSAJE** (no per-conversación). Pagas por template entregado por categoría;
**utility dentro de una CSW abierta = gratis**; marketing siempre se cobra; service free-form dentro de la ventana = gratis.

## Gotchas
1. Pinea Graph ≥v22.0; calls sin versión rompen en el próximo cutoff de Meta.
2. Las URLs de descarga de media expiran (~5 min) y necesitan auth — bájalas YA, persiste a tu storage.
3. Templates marketing con baja engagement bajan tu **quality rating** (verde→amarillo→rojo) → baja tu tier (1K→10K→100K→ilimitado).
4. Baileys (no-oficial, WhatsApp Web reversed) es gratis y sin aprobación de templates, pero riesgo de **ban de número**, rompe en cambios de protocolo, sin SLA — ok dev/QR, NO prod a escala; Cloud API = el path compliant.
5. Media por `link` debe ser alcanzable por los servers de Meta (no localhost/VPN); prefiere `media_id`.

**Fuentes:** developers.facebook.com/docs/whatsapp/cloud-api · developers.facebook.com/docs/graph-api/changelog/versions · ycloud.com/blog (pricing update).
