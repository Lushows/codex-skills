# 323 · Analytics & tracking (PostHog vs GA4, eventos, funnels, replay)

> [[62-analytics-product-tracking]] da el porqué; esto es el cómo: elegir herramienta,
> diseñar el schema de eventos, no perder datos a adblockers y no quemarte con privacidad.

## PostHog vs GA4 — para qué cada uno
**GA4** es analítica web/marketing gratis (sesiones, fuentes, conversiones, GAds). **No tiene session
replay, ni feature flags, ni warehouse**, su modelo de eventos es rígido y el muestreo distorsiona en volumen.
**PostHog** integra product analytics + replay + flags + experimentos + error tracking + warehouse en una
sola plataforma con eventos arbitrarios. Regla práctica para BIO-SETA / AGENTE STUDIO:

| Necesitas | Usa |
|---|---|
| Atribución de canales, GAds, reporting marketing | GA4 |
| Product analytics, funnels custom, replay, flags, experimentos | PostHog |
| Lo honesto | ambos en paralelo (GA4 marketing, PostHog producto) |

## Schema de eventos — el activo que se pudre si no lo cuidas
Diseña ANTES de instrumentar (ver [[345-event-tracking-schema]]):
- **Nombres `object_action`** en pasado: `checkout_started`, `order_placed`, `message_sent`. Consistente,
  legible, ordenable. Nunca mezcles `clickButton` con `button_clicked`.
- **Properties planas y tipadas**: `value` (number, no "$89.000"), `currency`, `product_id`, `source`.
- **`identify()`** liga anónimo↔conocido al login; mantén el mismo `distinct_id` cruzando dispositivos.
- **Diccionario de eventos** versionado (Notion/repo). Evento sin dueño ni definición = deuda.
- Evita el over-tracking: 30 eventos bien definidos > 300 de autocapture sin semántica.

## Funnels, retención, replay
- **Funnel**: pasos ordenados con ventana de conversión; mira drop-off por paso y segmenta por fuente/
  dispositivo. El paso que más gotea es tu prioridad de CRO ([[325-funnels-conversion-cro]]).
- **Retención**: cohortes por semana de registro — distingue producto que pega de fuga de baldazo.
- **Session replay**: PostHog graba DOM + consola + red + métricas; **enmascara inputs por defecto**.
  Úsalo para diagnosticar el "por qué" del drop-off del funnel, no para vigilar usuarios.

## No perder datos: reverse proxy
Los adblockers interceptan llamadas a dominios de tracking conocidos → **subreportas**. Solución:
**reverse proxy** que envía eventos desde TU subdominio (`e.tudominio.com`) en vez de a `posthog.com`.
PostHog trae guías para Cloudflare, Vercel, Netlify, Caddy, CloudFront. Recupera 10-30% de eventos perdidos.

## Privacidad (LatAm + GDPR-like)
- **No PII en properties** salvo necesidad y base legal; nada de teléfonos/emails en texto plano de eventos.
- Replay **enmascara** campos sensibles (`ph-no-capture`); revisa que no filtres tarjetas/cédulas.
- Consent mode para GA4 en UE; en LatAm aplica habeas data (Col. Ley 1581) → aviso + opt-out real.
- Server-side tracking para eventos críticos (`order_placed`): inmune a adblock y a JS que no carga.

## Gotchas
1. GA4 muestrea en alto volumen → tus números "no cuadran" con la base real.
2. Autocapture sin schema = miles de eventos `$autocapture` que nadie puede analizar.
3. Sin reverse proxy: pierdes silenciosamente eventos de usuarios con adblock (los que más convierten).
4. `distinct_id` que cambia entre anónimo y login → funnels rotos y usuarios duplicados.
5. PII en properties → incidente de privacidad + borrado retroactivo carísimo.

**Fuentes:** posthog.com/blog (posthog-vs-ga4) · posthog.com/docs (advanced/proxy, session-replay).

Cruza con [[62-analytics-product-tracking]] y [[345-event-tracking-schema]].
