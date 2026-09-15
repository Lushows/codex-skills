# 345 · Schema de eventos y tracking plan (taxonomía, naming, contratos)

> El analytics se pudre por la fuente, no por el dashboard. `Button Clicked`, `button_click`,
> `clicked_button` y `btnClick` son cuatro eventos para el mismo gesto → ninguna métrica cuadra.
> El tracking plan es el contrato que evita ese caos antes de que entre la primera fila.

## La taxonomía: object-action
El framework que recomienda PostHog y la industria: **`object_action`** — el Object es la cosa con la
que el usuario interactúa (button, form, page, order), el Action es lo que hizo (clicked, viewed,
submitted, created). Da una lista navegable y predecible en vez de un basurero de nombres ad-hoc.

```
order_completed        checkout_started      signup_form_submitted
video_played           subscription_cancelled
```

## Reglas de naming (elige UNA y obliga)
- **snake_case**, todo minúsculas (evita el infierno de `Button Clicked` vs `button clicked`).
- **Tiempo verbal consistente**: PostHog sugiere presente (`submit`, `create`); GA4 y muchos planes
  usan pasado (`signed_up`). Da igual cuál — lo letal es mezclar. Elige y documenta.
- **Object primero, action después** → agrupa por entidad al ordenar alfabéticamente.
- **Properties para el contexto, no más eventos**: NO crees `signup_google` y `signup_email`; crea
  `signup_completed` con property `method: google|email`. Menos eventos, más segmentable.
- **Sin PII en nombres ni en properties indexadas** (email, teléfono crudo) → riesgo legal y de costo.

## El tracking plan (la fuente de verdad)
Una tabla viva (Sheet, Notion, o YAML en repo) con, por evento:
| Campo | Ejemplo |
|---|---|
| event name | `order_completed` |
| descripción / cuándo dispara | al confirmarse el pago, una vez por orden |
| properties + tipo | `order_id:string`, `amount_usd:number`, `items_count:int` |
| owner | equipo Growth |
| trigger / ubicación en código | server-side, webhook de pago |

Versiónalo en Git si puedes: el diff del tracking plan es el changelog del analytics.

## Contratos y enforcement
El tracking plan sin enforcement se degrada en semanas. Capas de defensa:
1. **Tipado en el código** — wrapper de `capture()` que solo acepta eventos del plan (TS union types,
   o codegen tipo **Avo**). El IDE rechaza el typo antes del commit.
2. **Schema management en el destino** — PostHog permite definir grupos de propiedades tipadas para
   documentar y validar; rechaza/marca eventos que no calzan. [no verificado: nivel de bloqueo duro vs
   solo advertencia en la versión actual — confirmar en docs.posthog.com].
3. **CI check** — un test que falla si el código emite un evento que no está en el plan.

## Server-side vs client-side
- **Client-side** (SDK en browser/app): captura UI/intención, pero lo bloquean ad-blockers y miente
  con datos del cliente.
- **Server-side**: la verdad para eventos de negocio (pago, orden, suscripción) — inmune a ad-blockers,
  no se puede falsear. Regla: **lo que toca dinero o decide negocio, trackéalo server-side.**
- `distinct_id` consistente entre ambos lados para no partir al usuario en dos identidades.

## Gotchas
1. **Evento por variante** (`signup_google`/`signup_email`) → explosión combinatoria; usa properties.
2. **Mezclar tiempos verbales** entre eventos → imposible recordar el nombre, dashboards inconsistentes.
3. **PII en properties** → bomba GDPR/CCPA y costo de storage.
4. **Trackear todo "por si acaso"** → ruido, costo de ingest y nadie sabe qué evento es real.
5. **Plan sin enforcement** — se desincroniza del código en una sprint; sin tipado/CI no es contrato.
6. **Renombrar un evento en vivo** parte la serie histórica en dos; renombra con alias/migración, no en seco.

Cruza con [[323-analytics-tracking-posthog-ga4]] y [[62-analytics-product-tracking]].
