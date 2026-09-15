# 27 — Seguridad de apps (OWASP)

**OWASP Top 10 — edición 2025** (589 CWEs). Cambios vs 2021: **A01 Broken Access Control** sigue #1 (ahora absorbe
**SSRF**); **A02 Security Misconfiguration** subió de #5; dos nuevos: **A03 Software Supply Chain Failures** y
**A10 Mishandling of Exceptional Conditions** (manejo de errores, failing open). Crypto Failures e Injection siguen core.

**AuthN vs AuthZ:** authentication = *quién eres*; authorization = *qué puedes hacer*. Broken access control (falta
de authZ por-objeto — IDOR) = riesgo #1. Checa ownership server-side: `WHERE id=$1 AND owner=$current_user`.

**Password hashing:** **argon2id** — params OWASP `m=19456 (19 MiB), t=2, p=1` (o `m=47104, t=1, p=1`). Si no:
**scrypt**, o **bcrypt** (work factor ≥10, *enforce 72-byte max* — bcrypt trunca en silencio), o PBKDF2-HMAC-SHA256
(600k iters) para FIPS. **Nunca SHA-256/MD5 solo.**

**JWT:** **access token** corto (~15 min) + **refresh** más largo. Access en memoria; refresh en cookie
**HttpOnly, Secure, SameSite** (no `localStorage` — leíble por XSS). JWTs stateless → difícil revocar; mantén
denylist server-side o rota keys. **Bugs clásicos:** `alg=none` (recházalo), aceptar `HS256` esperando RS256
(algorithm confusion — pinea el algoritmo), no verificar `exp`/`aud`/`iss`, secret HMAC débil.

**OAuth2/OIDC:** usa **Authorization Code + PKCE** para web/mobile/SPA (PKCE previene interceptación; implicit
deprecado). OIDC añade `id_token`. Valida la firma contra el JWKS del provider, checa `aud`/`iss`/`nonce`.

**Sessions:** rota session id en login (anti-fixation); cookies HttpOnly+Secure+SameSite; timeouts absoluto + idle.

**Secrets:** nunca en código/repo/logs. Manager (Vault, AWS Secrets Manager, env de Render/Railway, Doppler/
Infisical); rota; inyecta por env en runtime. Escanea con gitleaks.

**Rate limiting** (por-IP + por-cuenta) anti brute force/DoS; `429` + `Retry-After`. **CORS:** allow-list orígenes
específicos, nunca `*` con credentials. **Headers:** `Content-Security-Policy` (mata casi todo XSS), HSTS,
`X-Content-Type-Options: nosniff`, `Referrer-Policy`.

**Input validation:** valida/normaliza en el boundary (pydantic). **SQL injection:** *siempre* queries
parametrizadas — nunca string-format SQL. **Supply chain:** **pip-audit** (o `uv pip audit`) en CI contra la
advisory DB; pinea + lockea deps (`uv.lock`/requirements con hashes); Dependabot. `pip-audit -r requirements.txt`.

## Gotchas
1. JWTs en `localStorage` → XSS = account takeover total.
2. No pinear el `alg` del JWT → forja por algorithm-confusion.
3. `CORS *` + credentials filtra data autenticada cross-origin.
4. Loguear bodies completos filtra passwords/tokens/PII.

**Fuentes:** owasp.org/Top10/2025 · cheatsheetseries.owasp.org (Password Storage) · datatracker.ietf.org/doc/html/rfc9700 (OAuth Security BCP/PKCE) · pypi.org/project/pip-audit.
