# 272 · Seguridad frontend: CSP, XSS, CSRF, clickjacking

> El backend puede estar blindado y el frontend ser la puerta abierta: un `<script>` inyectado
> roba la sesión, un iframe oculto te clickjackea, un `fetch` cross-origin filtra datos.
> Defensa en profundidad en el navegador, no una sola capa.

## XSS — las tres familias
- **Reflejado**: el payload viaja en la URL y se refleja sin escapar (`?q=<script>`).
- **Almacenado**: persiste en DB (un comentario) y golpea a todos los que lo ven. El peor.
- **DOM-based**: nunca toca el server; `el.innerHTML = location.hash` y el sink lo ejecuta.

**Mitigación en capas (no una sola):** (1) **output encoding contextual** — escapa según el contexto
(HTML body, atributo, JS, URL, CSS); frameworks como React/Vue escapan por defecto pero
`dangerouslySetInnerHTML`/`v-html` rompen eso. (2) **No usar sinks peligrosos**: `innerHTML`, `eval`,
`document.write`, `el.setAttribute('onclick', …)`. (3) **CSP estricta** como red de seguridad.

## CSP estricta basada en nonce (el patrón 2025)
El allow-list por host (`script-src 'self' cdn.x.com`) es frágil y bypasseable (JSONP, gadgets).
La recomendación OWASP/Google es **nonce + `strict-dynamic`**:

```http
Content-Security-Policy:
  script-src 'nonce-r4Nd0m' 'strict-dynamic';
  object-src 'none';
  base-uri 'none';
  require-trusted-types-for 'script';
```

```html
<script nonce="r4Nd0m" src="/app.js"></script>
```

- El **nonce** es aleatorio por respuesta (≥128 bits, generado server-side, nunca cacheado).
- **`strict-dynamic`**: un script con nonce válido puede cargar más scripts sin nonce → propaga
  confianza, sobrevive a bundlers que inyectan `<script>`. Es CSP L3, soportado en todos los
  navegadores modernos. Hace que los allow-list por host se ignoren (compat: añádelos para legacy).
- **`object-src 'none'`** mata plugins; **`base-uri 'none'`** bloquea robo de nonce vía `<base>`.
- **Trusted Types** (`require-trusted-types-for 'script'`): obliga a pasar todo DOM-sink por una
  política tipada → mata el XSS DOM-based en la raíz. Defínela: `trustedTypes.createPolicy(...)`.

**Rollout sin romper prod:** despliega primero con `Content-Security-Policy-Report-Only` + un
endpoint `report-to`/`report-uri`, observa violaciones reales, luego conmuta a enforcement.
Alternativa a nonce para HTML estático/cacheado: `'sha256-...'` del inline script.

## CSRF — el navegador adjunta la cookie por ti
Si autenticas con **cookies**, cualquier sitio puede disparar un POST a tu API con la cookie del
usuario. Defensas (combinar):
- **`SameSite=Lax`** (default moderno) o **`Strict`** en la cookie de sesión → corta el cross-site
  en la mayoría de casos. `Lax` permite navegación top-level GET; `Strict` ni eso.
- **Token anti-CSRF**: synchronizer token (server lo emite, form lo reenvía) o **double-submit
  cookie** (token en cookie + header, server compara). Para SPAs, el patrón header `X-CSRF-Token`.
- **Verificar `Origin`/`Sec-Fetch-Site`** en mutaciones — barato y efectivo.
- **APIs con `Authorization: Bearer`** (token en memoria, no cookie) **no son vulnerables a CSRF**
  porque el navegador no adjunta el header solo. Pero entonces cuida el XSS (ver [[273-…]]).

## Clickjacking y headers de hardening
Tu página embebida en un iframe transparente engaña al usuario a clickear. Mata con:
- **`Content-Security-Policy: frame-ancestors 'none'`** (o lista de orígenes) — el método moderno;
  reemplaza a `X-Frame-Options: DENY` (déjalo también por navegadores viejos).
- **`Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`** — fuerza HTTPS.
- **`X-Content-Type-Options: nosniff`** — no adivinar MIME (evita que un .txt se ejecute como JS).
- **`Referrer-Policy: strict-origin-when-cross-origin`** — no filtrar paths/tokens en el Referer.

## CORS — no es una defensa, es una relajación
CORS **permite** lecturas cross-origin; no las bloquea por seguridad de tu API. Reglas:
- **Nunca `Access-Control-Allow-Origin: *` con `Allow-Credentials: true`** (el navegador lo rechaza,
  pero gente lo "arregla" reflejando el `Origin` → equivale a `*` con credenciales = fuga total).
- **Allow-list explícita** de orígenes; refleja solo si el `Origin` está en la lista.
- CORS protege al **usuario**, no al server: la autorización real va server-side igual.

## Gotchas
1. React te protege de XSS… hasta `dangerouslySetInnerHTML` con HTML de usuario sin sanitizar (usa DOMPurify).
2. Nonce **cacheado** = nonce reutilizable = CSP inútil. Debe ser único por respuesta.
3. `SameSite=None` requiere `Secure`; sin él la cookie se descarta silenciosamente.
4. CSP sin `base-uri` ni `object-src` deja bypasses aun con nonce.

**Fuentes:** cheatsheetseries.owasp.org (CSP, XSS Prevention) · web.dev/articles/strict-csp ·
csp.withgoogle.com/docs/strict-csp.html · w3.org/TR/CSP3 · developer.mozilla.org (CSP, Trusted Types).

Cruza con [[27-seguridad-apps-owasp]] y [[274-api-security-ratelimit-keys]].
