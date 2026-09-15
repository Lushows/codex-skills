# 273 · Auth a fondo: OAuth2.1/OIDC, passkeys, sessions vs JWT

> Authentication (quién eres) ≠ authorization (qué puedes). La mayoría de brechas de cuentas
> no rompen la cripto: rompen el *flujo* — un refresh sin rotar, un JWT sin revocar, un OAuth
> sin PKCE. En 2025 el destino es passkeys; el camino, sessions bien hechas.

## OAuth 2.1 — escribe esto, no 2.0
OAuth 2.1 consolida RFC 6749 + PKCE (7636) + Security BCP (9700) en un solo spec. Cambios que importan:
- **PKCE obligatorio para *todos* los clientes** del authorization-code flow (no solo públicos).
  El `code_verifier` aleatorio + `code_challenge = S256(verifier)` impide que un atacante que
  intercepte el `code` lo canjee. Anthropic lo hizo base de la autorización de MCP.
- **Implicit flow y Resource-Owner-Password-Credentials eliminados** (inseguros, no los uses).
- **Refresh tokens** de clientes públicos: deben ser **sender-constrained o rotativos**.
- **`redirect_uri` exact-match** (sin comodines) → corta el robo de `code` por redirección abierta.

**OIDC** = capa de identidad sobre OAuth2: añade `id_token` (JWT firmado con claims del usuario).
Valida **siempre**: firma contra el **JWKS** del provider, `iss`, `aud`, `exp`, y `nonce` (anti-replay).

```
Flujo web/SPA/mobile = Authorization Code + PKCE:
1. client → /authorize?response_type=code&code_challenge=S256(...)&state=...&nonce=...
2. user autentica en el IdP → redirect con ?code=&state=
3. client verifica state, POST /token con code + code_verifier
4. IdP devuelve access_token (+ id_token OIDC, + refresh_token)
```

## Passkeys / WebAuthn — matar la contraseña
Un passkey es un par de claves asimétrico ligado al **RP ID** (tu dominio); la privada vive en el
authenticator (Secure Enclave/TPM/llave FIDO2), nunca viaja. Inmune a phishing (ligada al origen),
a credential stuffing y a brechas de DB (el server solo guarda la clave **pública**).

- **Discoverable credentials (resident keys)**: el authenticator almacena la credencial y el
  `user.name` → permite login **sin teclear usuario**. Creación: `residentKey: 'required'`.
- **Conditional UI (autofill)**: `navigator.credentials.get({ mediation: 'conditional' })` + el
  input con `autocomplete="username webauthn"`. El passkey aparece en el dropdown de autofill junto
  a las contraseñas. Solo funciona con discoverable creds. KAYAK/eBay reportan que es el mayor
  driver de adopción (returning users ≈ 100% passkey share).
- **Ceremonia**: registro (`navigator.credentials.create`) guarda la pública + `credentialId` +
  signCount; login (`.get`) verifica la firma del challenge. Omite `allowCredentials` en login
  para usar discoverable. Verifica server-side: origin, RP ID hash, challenge, firma, `signCount` ↑.
- **Adopción real**: self-serve queda en 5-10%; con signup-default + prompt post-login + conditional
  UI sube a 60-90%. Ofrece passkey como añadido, mantén fallback (no fuerces de golpe).

## Sessions vs JWT — elige consciente
| | **Server session (cookie)** | **JWT stateless** |
|---|---|---|
| Estado | en server (Redis/DB), cookie opaca | self-contained, claims firmados |
| Revocar | inmediato (borra la sesión) | difícil — vive hasta `exp` |
| Escala | requiere store compartido | sin store, pero tokens grandes |
| Riesgo | robo de cookie | robo de token + no revocable |
| Default web | **recomendado** para apps con login | bueno para APIs/microservicios |

**Cookie de sesión correcta:** `HttpOnly` (XSS no la lee), `Secure`, `SameSite=Lax/Strict`,
path acotado, expiración. **Rota el session id en login** (anti session-fixation) y aplica timeout
**absoluto + idle**.

**Si usas JWT:** access corto (~15 min) **en memoria** (nunca `localStorage` — XSS = takeover);
refresh largo en cookie `HttpOnly`. **Pinea el `alg`** (rechaza `alg:none` y la confusión
HS256↔RS256). Para revocar: **denylist** server-side o **rota las firmas**. Refresh con
**rotación** + detección de reuse (si llega un refresh ya usado → revoca toda la familia: indica robo).

## Logout y multi-dispositivo
- Sessions: borra del store → muere global. JWT: requiere denylist del `jti` hasta `exp`.
- **OIDC RP-Initiated Logout** (`end_session_endpoint`) cierra también la sesión del IdP.
- Lista de sesiones activas por usuario (device, IP, última act.) + "cerrar las demás".

## Gotchas
1. JWT en `localStorage` → cualquier XSS roba la cuenta. Va en memoria + cookie HttpOnly.
2. No verificar `aud`/`iss` del id_token → token de otra app es aceptado.
3. Refresh sin rotación ni reuse-detection → un refresh robado vive indefinido.
4. PKCE sin verificar el `state` → CSRF en el callback de OAuth.

**Fuentes:** oauth.net/2.1 · datatracker.ietf.org/doc/draft-ietf-oauth-v2-1 · rfc9700 ·
w3.org/TR/webauthn-3 · web.dev/articles/webauthn-discoverable-credentials ·
developer.chrome.com/docs/identity/webauthn-conditional-ui.

Cruza con [[292-auth-providers-clerk-auth0]] y [[27-seguridad-apps-owasp]].
