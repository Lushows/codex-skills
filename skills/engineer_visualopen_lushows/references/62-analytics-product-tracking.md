# 62 — Analytics y product tracking (growth)

**PostHog** = el estándar OSS todo-en-uno 2026: product analytics, session replay, feature flags, A/B experiments,
surveys y LLM analytics en una plataforma. Self-host (Docker/k8s) o cloud. Ventaja: experimentos y flags comparten la misma capa de eventos.

## Autocapture vs manual
Autocapture registra clicks/pageviews/forms vía snippet JS — ideal para arrancar/frontend. Para eventos de negocio
(`order_placed`, `credit_consumed`, `message_sent`) usa **eventos manuales** tipados. **Regla: autocapture para descubrir, manual para métricas que reportas.**

## Taxonomía de eventos
Convención `object_action` en `snake_case`, pasado: `order_completed`, `product_viewed`, `subscription_upgraded`.
Define un diccionario y NO lo cambies (renombrar rompe funnels históricos). Propiedades consistentes: `plan`, `tenant_id`, `amount_usd`, `source`.
```js
import posthog from 'posthog-js'
posthog.init('phc_xxx', { api_host: 'https://us.i.posthog.com', autocapture: true })
posthog.capture('order_completed', { order_id:'o_123', tenant_id:'t_42', amount_usd:49.9, product:'melena', channel:'whatsapp' })
posthog.identify('user_99', { plan:'pro', country:'CO' })     // une sesión anónima ↔ usuario
```

## Funnels / retention / cohorts
**Funnel** = secuencia ordenada (visitó → carrito → compró) con drop-off por paso. **Retention** = de los que
hicieron X el día 0, cuántos vuelven el día N. **Cohorts** = grupos por propiedad/comportamiento para segmentar todo.

## A/B testing
PostHog Bayesiano por default ("probabilidad de ganar", actúas a 90%+) o frecuentista. Antes de lanzar: calcula
**sample size** según MDE + baseline; correr hasta significancia sin tamaño pre-calculado es **peeking** = falsos
positivos. Define **guardrail metrics** (latencia, churn) que no deben empeorar. Hasta 9 variantes + control.

## Atribución / North Star
UTM (`utm_source/medium/campaign`) en el primer pageview. **First-touch** (awareness) vs **last-touch** (conversión);
para SaaS guarda ambos. **North Star** = la métrica única de valor entregado (ej. "mensajes resueltos por el bot/
semana"). **AARRR:** Acquisition, Activation, Retention, Revenue, Referral.

## Feature flags
Rollout gradual (5%→25%→100%), kill switch instantáneo, targeting por propiedad (`country == 'CO'`). Desacopla deploy de release. Limpia flags muertos (deuda).

## Privacy
PII fuera de las propiedades cuando se pueda; `opt_out_capturing()` con consentimiento. En Colombia aplica **Habeas
Data (Ley 1581/2012)**: autorización del titular, finalidad declarada, derecho a supresión. Enmascara inputs en replay (`data-ph-no-capture`).

## Gotchas
1. **Renombrar eventos rompe el histórico** — versiona en propiedad, no en el nombre.
2. **Peeking en A/B** — fija sample size antes; mirar a diario infla falsos positivos.
3. **Autocapture explota volumen/costo** — filtra eventos ruidosos (PostHog cobra por evento).
4. **`identify` mal usado** fragmenta el usuario — un `distinct_id` estable por persona.
5. **PII en replays** — enmascara teléfonos/cédulas o violas Habeas Data.
6. **Significancia ≠ tamaño de efecto** — mira el lift absoluto, no solo el p-value.

**Fuentes:** posthog.com/experiments · posthog.com/docs/feature-flags · posthog.com/docs/experiments.
