# 32 — Privacidad, consent, cookies & diseño ético

Frontera legal y de diseño para consent, privacy-by-design y persuasión honesta (legal y respetuosa). **Léelo cuando implementes cookie banners, permisos, forms con datos personales, o cualquier flujo persuasivo.** Pareja de 16 (a11y), 29 (pricing ético) y 17.

## 1. Cookie consent done right (2026)

**Lo que la ley exige** (GDPR + ePrivacy Directive transpuesta país por país — la ePrivacy *Regulation* fue retirada en feb-2025):
- **Prior consent:** cookies/scripts no esenciales **bloqueados hasta el opt-in**. Cargar analytics/ads antes = ilegal.
- **Affirmative action:** nada de pre-ticked boxes, "seguir navegando = aceptar", ni scroll-as-consent.
- **Equal prominence:** **"Reject All" tan fácil como "Accept All"** (mismo tamaño/color/contraste y mismos clics). Ya se multa.
- **Granularidad por categoría** (necessary/preferences/analytics/marketing), no esencial **default OFF**.
- **Legitimate interest NO sustituye consent** para storage; no puede venir pre-marcado.
- **Withdrawal tan fácil como dar consent** (link persistente) y debe **detener las lecturas**, no solo dejar de escribir.
- **No re-prompt <6 meses** tras un rechazo.
- **Scope ampliado** (EDPB 2/2023): pixels, fingerprinting, "cookie-less" analytics siguen requiriendo consent.
- **Banner WCAG 2.1 AA** + **consent log** (timestamp ISO 8601, ID pseudónimo, estado por propósito, versión, locale; retención 3-6 años).
**Banner compliant:**
```
[Capa 1, scripts bloqueados] Título claro + propósitos reales + link a policy
  [ Reject All ]   [ Manage preferences ]   [ Accept All ]   ← 3 botones, igual peso
[Capa 2 granular] Necessary [ON fijo] · Preferences/Analytics/Marketing [OFF] · [Save selection]
```
**CMP + Google Consent Mode v2** (obligatorio desde mar-2024 para Ads/GA4 en EEA/UK): emite `ad_storage`, `analytics_storage`, `ad_user_data`, `ad_personalization`. **Basic** (bloquea hasta interacción, más privado) vs **Advanced** (carga con consent denegado + pings para modeling). Ads personalizados EEA/UK → CMP certificado por Google + IAB **TCF v2.3 (obligatorio 28-feb-2026)**.
**Coste real (2025):** Google **€325M**, Shein **€150M**, Meta **€200M** (DMA "consent-or-pay"); total CNIL 2025 **€486.8M** (vs €55M en 2024).

## 2. Dark patterns — qué es ya ilegal + alternativa

**Landscape:** EU **DSA Art. 25** prohíbe dark patterns (1ª multa: X €120M, dic-2025). EU **Digital Fairness Act** en camino (Q3/Q4 2026). FTC: la regla Click-to-Cancel fue anulada en 2025, pero la FTC actúa vía casos (**Amazon $2.5B**, sep-2025) — cancelar debe ser tan fácil como suscribirse.

| Dark pattern | ❌ Riesgo | ✅ Alternativa ética |
|---|---|---|
| **Confirmshaming** ("No, no quiero ahorrar") | DSA/DFA | "No, gracias" neutral |
| **Roach motel** (difícil cancelar) | FTC Amazon $2.5B | Cancelar en los mismos clics que suscribir |
| **Sneak into basket** | Consumer law | Add-ons opt-in, no preseleccionados |
| **Forced continuity** (trial cobra sin avisar) | FTC/DSA | Recordatorio antes del cargo |
| **Fake urgency/scarcity** | Engaño ilegal | Stock/contador real |
| **Disguised ads** | DSA | Etiqueta "Ad/Sponsored" |
| **Nagging** (re-preguntar) | Dark pattern consent | Respetar el "no" ≥6 meses |
| **Trick questions** (doble negación) | DSA/GDPR | Lenguaje claro |
| **Preselection** (casillas pre-marcadas) | Inválido GDPR | No esencial default OFF |
| **Hidden costs** | DFA | Precio total upfront |

**Anti-IA:** generar variantes A/B engañosas con IA no es defensa — la ley mira el *efecto*. Si "materially distorts" la decisión autónoma, es dark pattern aunque lo diseñe un modelo.

## 3. Persuasión ética vs manipulación

**La línea = transparencia + autonomía + beneficio mutuo.** La persuasión *aclara*; la manipulación *oscurece*. El mismo "Solo quedan 2" es persuasión si es verdad y dark pattern si es siempre — el diseño se ve idéntico, la ética no.
**Test del "espejo limpio":** *"¿Estaría cómodo si el usuario viera CLARAMENTE lo que este diseño hace?"* Si exige que NO lo note, es manipulación.
**Cialdini ético:** Scarcity solo si es real · Social proof verificable · Authority con credenciales genuinas · Reciprocity con valor real.
**Nudging honesto:** **good defaults** que sirven al usuario (no solo al negocio); hacer el camino correcto el más fácil sin esconder/penalizar la otra opción. La persuasión ética **supera a la manipulación en LTV multi-año**.

## 4. Privacy UX más allá de cookies

- **Privacy by design (GDPR Art. 25):** privacidad desde el inicio; default = la opción más protectora.
- **Data minimization:** pide SOLO lo necesario; en forms cada campo extra debe justificarse; lo opcional, marcado; nada "por si acaso".
- **Privacy dashboard:** un lugar para ver/editar consentimientos, descargar datos (portabilidad) y borrar cuenta.
- **Transparent data use** en el momento de recogerlo.
- **Privacy policy legible** (layered: resumen humano arriba + detalle abajo), no muro de 8.000 palabras.
- **Account deletion fácil** (Art. 17), en pocos clics, sin "contacta a soporte" como obstáculo. Borrar = tan fácil como registrarse.

## 5. Consent & permisos en la práctica

- **Notification permission:** NUNCA al cargar (cero contexto → bloqueo). **Earn it:** pide tras una acción de valor con **double permission/priming** (pre-prompt propio explicando el valor → solo si dice sí, dispara el prompt nativo). (2025: opt-in Android ~81.5%, iOS ~43.9%.)
- **Geolocation/camera/mic:** pide **en contexto**, cuando la feature lo necesita, con micro-copy del porqué.
- **Marketing opt-in:** casilla **no pre-marcada**, separada de los términos. **Double opt-in email**.
- **Cookie-less future:** first-party data, contextual ads, Privacy Sandbox; modela conversiones con Consent Mode.
**Patrón just-in-time:**
```
onUserActionThatNeedsPermission():
  if !granted: showCustomPrimer({why:"Te avisamos cuando tu pedido salga a reparto", cta:"Activar avisos", dismiss:"Ahora no"})
  if tapped("Activar avisos"): requestNativePermission()   // prompt OS SOLO aquí, nunca en page load
```

## 6. Confianza por transparencia (el trust dividend)

- **Privacy as a feature:** el diseño respetuoso **construye confianza y convierte**; supera a la manipulación en LTV multi-año.
- **Security signals:** HTTPS, badges reales, explicación honesta de qué datos se usan.
- **2026 — AI/data transparency:** entrenar modelos con datos personales necesita base legal/consent explícito (GDPR + EU AI Act); da acceso/rectificación/borrado + opt-out de training; declara cuándo el usuario habla con IA.
- **Regla de oro:** ser honesto sobre los datos no es coste de cumplimiento, es **ventaja competitiva**.

## Checklist rápido
```
CONSENT: scripts no esenciales bloqueados · Reject=Accept (clics/tamaño/color) · toggles default OFF · withdrawal que frena lecturas · no re-prompt <6 meses · CMP + Consent Mode v2 + TCF 2.3 · WCAG AA + log
DARK PATTERNS (prohibidos): confirmshaming · roach motel · sneak-into-basket · fake urgency · hidden costs · preselection · disguised ads · nagging · trick questions
PRIVACY: data minimization · permisos just-in-time (notif: earn it, nunca on-load) · marketing opt-in NO pre-marcado + double opt-in · account deletion en pocos clics · policy layered · AI: base legal/consent + opt-out
```
