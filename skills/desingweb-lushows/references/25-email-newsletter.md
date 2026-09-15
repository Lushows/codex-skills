# 25 — Email & newsletter (HTML email, el arte oscuro)

Playbook 2026 para email transaccional y marketing que renderiza en todos los clientes y se ve premium. El email es donde el CSS moderno no llegó: Outlook desktop usa el motor de **Microsoft Word**. **Léelo cuando diseñes cualquier correo** (confirmación de pedido, OTP, newsletter). Consulta **caniemail.com** (el "caniuse" del email) antes de usar cualquier propiedad.

## 1. Fundamentos y realidad de clientes

**Por qué tablas todavía:** Outlook (Word) no entiende `float/flex/grid/position` ni `padding` fiable en `<div>`. La única caja predecible cross-client es `<table>`. Approach moderno = **híbrido/fluido ("spongy")**: tablas para Outlook + `max-width`/`display:inline-block` para que el resto fluya, **minimizando media queries** (Gmail a veces las strippea).
**Clientes:** Apple Mail (WebKit, el más capaz, soporta `@media`/web fonts/dark) · Gmail (soporta `<style>` pero lo **strippea en la parte clipeada**, ignora `prefers-color-scheme`, exige `<!DOCTYPE html>`) · **Outlook desktop Windows** (motor Word = el enemigo: VML, conditional comments, anchos en atributos, sin `max-width`/`border-radius`/`background-image` CSS) · Outlook.com (motor web, mejor) · Yahoo/Samsung/Thunderbird (razonables).
**Inline vs `<style>`:** **estilos inline en cada elemento** (Gmail/otros strippean `<style>`). Usa `<style>` solo para lo que no puede ser inline: media queries, `:hover`, `@font-face`, dark mode. ESPs/inliners (Maizzle, premailer, juice) lo automatizan.
**Web fonts:** Apple Mail/iOS/Outlook.com/Samsung sí; Gmail/Outlook desktop NO → siempre fallback a system stack. `<!--[if !mso]><!-->` para servir la `<link>` solo a no-Outlook.
**600px** = ancho estándar (máx 640). En móvil colapsa a 100%.
**Bulletproof button (VML para Outlook):** Outlook ignora `padding`/`border-radius` en `<a>` → VML solo-Outlook + HTML normal para el resto:
```html
<td align="center" bgcolor="#10b981" style="border-radius:8px;">
  <!--[if mso]>
  <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="https://ex.com"
    style="height:48px;v-text-anchor:middle;width:240px;" arcsize="16%" fillcolor="#10b981">
    <w:anchorlock/><center style="color:#fff;font-family:sans-serif;font-size:16px;font-weight:bold;">Confirmar</center>
  </v:roundrect><![endif]-->
  <!--[if !mso]><!-->
  <a href="https://ex.com" style="display:inline-block;padding:14px 32px;font-size:16px;font-weight:700;color:#fff;text-decoration:none;border-radius:8px;background:#10b981;">Confirmar</a>
  <!--<![endif]-->
</td>
```

## 2. Build approaches

| Herramienta | Approach | Úsalo cuando |
|---|---|---|
| **MJML** | Markup propio → HTML table Outlook-safe, responsive automático | Compat Outlook máxima, backend no-JS |
| **Maizzle** | Tailwind para email (inlinea/purga/minifica) | Equipo Tailwind, control de HTML |
| **React Email / JSX email** | Componentes React → HTML email; integración con **Resend** | Stack React/TS, transaccional |
| **Foundation (Inky)** | `<row>/<columns>` → tablas | Legacy |

Recomendación: **React Email** (equipo JS + Resend) · **MJML** (Outlook crítico) · **Maizzle** (Tailwind).
```xml
<mjml><mj-body width="600px"><mj-section background-color="#fff" padding="32px"><mj-column>
  <mj-image src="logo.png" width="120px"/><mj-text font-size="22px" font-weight="700">Pedido confirmado</mj-text>
  <mj-button background-color="#10b981" border-radius="8px" href="...">Ver pedido</mj-button>
</mj-column></mj-section></mj-body></mjml>
```

## 3. Responsive & dark mode

**Fluido/híbrido (sin depender de media queries):** tabla externa `width:100%`, interna `max-width:600px`+`width:100%`, columnas `display:inline-block`+`max-width` que reflowen solas. Ghost tables `<!--[if mso]><table width="600">...<![endif]-->` dan ancho fijo a Outlook.
**Dark mode (realidad por cliente):** `prefers-color-scheme` soportado en Apple Mail/Outlook 2019+/Samsung/Thunderbird; **NO** Gmail/Yahoo (aplican su propia inversión). Pon siempre:
```html
<meta name="color-scheme" content="light dark"><meta name="supported-color-schemes" content="light dark">
<style>:root{color-scheme:light dark}
@media (prefers-color-scheme: dark){ .email-bg{background:#0b0f0e!important} .card{background:#14201c!important}
  .text-main{color:#e5e7eb!important} .logo-light{display:none!important} .logo-dark{display:inline-block!important} }</style>
```
**Gotchas:** Gmail/Outlook invierten por su cuenta → evita negro/blanco puros (usa `#111827`/`#f4f4f5`); logos con halo claro o swap `.logo-light`/`.logo-dark`; define `bgcolor` en atributo además de CSS.

## 4. Transaccional (recibos, confirmaciones, reset, OTP)

Principios: **un solo CTA claro**, jerarquía obvia, sin marketing, deliverability impecable, siempre plain-text.
Jerarquía: Logo → titular del evento ("Tu pedido #1234 está confirmado") → resumen (qué/cuánto/cuándo) → CTA único → soporte/footer.
**Preheader oculto** (el resumen que se ve en bandeja, segundo texto más leído):
```html
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;">Pedido #1234 confirmado — entrega 2-4 días.</div>
```
**OTP/código:** grande, monoespaciado, **seleccionable como texto (NUNCA imagen)**, con expiración ("válido 10 min") y aviso anti-phishing ("nadie de BIO-SETA te pedirá este código").
Estructura: `<meta name="x-apple-disable-message-reformatting">` + tabla `role="presentation"` con card `max-width:600px;border-radius:12px`.

## 5. Marketing / newsletter

**Inverted pyramid por bloque:** imagen/contexto → titular → beneficio breve → **un CTA centrado**. Repetible.
**Patterns:** hero (imagen+headline+CTA) → bloques zig-zag → grid de productos (2 col desktop → 1 móvil con `inline-block`) → footer con unsubscribe.
**Preheader:** ~85-100 car tras el subject — escríbelo a propósito (no "View in browser"); rellena con `&zwnj;&nbsp;` para no arrastrar cuerpo.
**Subject:** 30-50 car (móvil corta), personalización real, sin clickbait, emoji con moderación, A/B.
**Above the fold:** ~300-400px — logo + propuesta de valor + 1er CTA ahí.
**GIFs:** soportados salvo **Outlook desktop (solo 1er frame)** → diseña el 1er frame funcional.
**A11y:** `role="presentation"` en TODAS las tablas de layout · `alt` descriptivo (se ve con imágenes bloqueadas) · `lang="es"` · contraste AA · texto real, no en imágenes · fuente ≥14-16px.

## 6. Deliverability & técnico

- **SPF/DKIM/DMARC** (3 records DNS) — sin ellos Gmail/Yahoo (exigen auth a bulk desde 2024) te mandan a spam. Unsubscribe one-click requerido en bulk.
- **Spam no-nos de diseño:** email 100% imagen · ratio imagen-texto muy alto (apunta ~60% texto) · "GRATIS!!!"/MAYÚSCULAS/exceso de `!` · links acortados · mismatch texto-link.
- **Gmail clipping a ~102KB de HTML** (las imágenes no cuentan, su markup sí): al clipear strippea `<style>` y esconde el CTA tras "View entire message". **Mantente <100KB** (minifica, evita CSS redundante).
- **Testing:** **Litmus** / **Email on Acid** (90+ clientes reales incl. Outlook desktop). ESPs: Klaviyo (e-commerce/flows), Mailchimp (marketing), Resend/Postmark (transaccional), SendGrid/Mailgun (API a escala).

## Email anti-patterns — blacklist
email solo-imagen (spam + invisible con imágenes off) · background-image como único portador de info crítica (Outlook no la renderiza; pon `bgcolor` + texto fuera) · tap targets <44px · depender de `<style>` sin inline · negro/blanco puros (se rompen en dark) · web fonts sin fallback · `<a>` con padding/radius sin VML (botón roto en Outlook) · HTML >102KB (Gmail clipea) · tablas de layout sin `role="presentation"` · olvidar el preheader · GIF con mensaje en frames posteriores (Outlook muestra solo el 1º) · sin plain-text version.
