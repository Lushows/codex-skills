# 274 · Seguridad de API: rate-limit, API keys, HMAC, WAF, validación

> Una API expone tu lógica de negocio cruda. El OWASP API Top 10 ya no va de inyección clásica:
> va de **abuso de lógica de negocio** y autorización por-objeto rota. El rate-limit y el HMAC
> son tu cinturón; la validación de input, el airbag.

## OWASP API Top 10 — los que de verdad muerden
- **BOLA / IDOR (API1)**: `GET /orders/123` sin checar que 123 es **tuyo**. El #1. Autoriza por
  objeto server-side: `WHERE id=$1 AND owner=$current_user`. Nunca confíes en el ID del cliente.
- **Broken Authentication (API2)**: endpoints sin auth, tokens débiles, sin rate-limit en login.
- **BOPLA (API3)**: mass-assignment (`{role:'admin'}` cuela) + exposición excesiva de propiedades.
  Usa **allow-list de campos** in/out (DTO explícito), no serialices el modelo entero.
- **Unrestricted Resource Consumption (API4)**: sin paginación/límites → un query barre la DB.
- **SSRF (API7)**: la API hace `fetch(url_del_usuario)` y alcanza la metadata interna (169.254.169.254).

## Rate-limiting — token bucket por defecto
El **token bucket** absorbe ráfagas (un balde de N tokens, +r/s de recarga, cada request gasta 1;
balde vacío → `429`). Mejor que fixed-window (que sufre el efecto borde 2x). Sliding-window log es
preciso pero caro en memoria.

```
Capa por: IP (anti-DoS anónimo) + cuenta/API-key (anti-abuso autenticado) + por-ruta
(login y endpoints caros más estrictos que un GET trivial).
Respuesta: 429 + Retry-After: <segundos> + headers RateLimit-Remaining/Reset.
Estado compartido entre instancias → Redis (INCR+EXPIRE o token bucket atómico en Lua).
```

Para flujos de alto valor (pago, OTP): **velocity rules** por user/device/ASN + **idempotency keys**
(el cliente manda `Idempotency-Key`; reintentos no duplican el cargo). Detalle en
[[141-webhooks-hmac-idempotencia-dlq-jobs-gpu]].

## API keys — qué son y qué no
- **No autentican usuarios** — identifican un *proyecto/cliente* y permiten cuota/atribución.
- Genera key aleatoria (≥32 bytes), guarda **solo el hash** (SHA-256) en DB — como contraseñas.
  Muestra el secreto una sola vez. Prefijo legible (`sk_live_…`) para detección y revocación.
- **En header, nunca en URL** (`Authorization` o `X-API-Key`) — las URLs se loguean y cachean.
- Scopes por key + expiración + rotación + revocación inmediata. Gitleaks/secret-scanning en repos.

## HMAC request signing — integridad y anti-replay (B2B/webhooks)
Para integraciones server-to-server donde una bearer-key sola no basta:

```
firma = HMAC-SHA256(secreto_compartido,  metodo + path + timestamp + sha256(body))
headers: X-Signature: <firma>, X-Timestamp: <epoch>
Verificación server:
  1. recalcula la firma, compara en tiempo constante (crypto.timingSafeEqual).
  2. rechaza si |now - timestamp| > 5 min  → ventana anti-replay.
  3. opcional: nonce ya-visto en cache corto → replay-proof estricto.
```

El timestamp dentro de la firma es lo que impide reusar una petición capturada. Sin él, HMAC solo
prueba integridad, no frescura.

## WAF y validación de input
- **WAF** (Cloudflare/AWS WAF/ModSecurity): primera capa contra patrones conocidos (SQLi, XSS,
  scanners), bot-mitigation y rate-limit en el borde. **Complemento, no sustituto** de validación
  en la app — se bypassea con encoding/ofuscación.
- **Validación en el boundary**: schema estricto (zod/pydantic/JSON Schema) — tipos, rangos,
  longitudes, enums. **Allow-list, no block-list.** Rechaza propiedades extra (`additionalProperties:
  false`) para frenar mass-assignment. Normaliza antes de validar (Unicode, trim).
- **SQL parametrizado siempre** — nunca interpolar strings. ORM o prepared statements.
- **SSRF**: valida la URL contra allow-list de hosts, resuelve DNS y bloquea rangos privados/link-local,
  desactiva redirects a internos.

## Diseño defensivo extra
- **Contrato OpenAPI** como fuente de verdad → valida request/response contra el spec (schema
  validation en el gateway). Versiona la API.
- **Logs estructurados** sin secretos/PII (no loguees bodies completos ni tokens).
- **CORS allow-list** explícita (ver [[272-web-security-frontend-csp-xss-csrf]]).

## Gotchas
1. Rate-limit solo por IP → NAT/proxy comparte IP y CGNAT lo evade; combina con cuenta.
2. Comparar firmas con `==` normal → timing attack; usa comparación en tiempo constante.
3. API key en query string → acaba en logs de acceso, Referer y caché de CDN.
4. WAF "verde" da falsa seguridad: la lógica de negocio (BOLA) no la ve un WAF.

**Fuentes:** owasp.org/API-Security/2023 (Top 10) · cheatsheetseries.owasp.org (REST Security,
Authorization) · learn.microsoft.com (mitigate OWASP API in APIM).

Cruza con [[141-webhooks-hmac-idempotencia-dlq-jobs-gpu]] y [[361-rate-limiting-throttling]].
