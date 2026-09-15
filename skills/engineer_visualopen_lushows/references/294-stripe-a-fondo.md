# 294 · Stripe a fondo: subscriptions, metered, webhooks, Connect, tax

> Stripe es el baseline global de cobro. Lo que separa una integración de juguete de una de producción:
> idempotencia, verificación de webhook con body crudo, y entender que el webhook NO es la verdad final.

## Modelo de objetos (el mapa mental)
```
Customer → Subscription → SubscriptionItem → Price → Product
PaymentIntent (pago único)   Invoice (recurrente)   PaymentMethod (token de tarjeta)
```
- **PaymentIntent** = un cobro único. Creas server-side (amount, currency, `automatic_payment_methods`), confirmas client-side con Stripe.js/Elements.
- **Checkout Session** = página hosteada de Stripe → te quedas en **PCI SAQ-A** (nunca tocas la tarjeta). Cierra con `checkout.session.completed`.
- **Subscription** = facturación recurrente; genera `Invoice` por ciclo. **Customer Portal** hosteado para que el usuario gestione plan/tarjeta sin que escribas UI.

## Pricing: fixed, tiered, usage-based
- **Fijo/escalonado**: `Price` con `recurring` + `tiers` (graduated o volume). Cambio de plan a mitad de ciclo → **proration** automática (Stripe prorratea el crédito/cargo; controla con `proration_behavior`).
- **Usage-based / metered** (clave para SaaS de IA): defines `Price` con `recurring.usage_type=metered`, y reportas consumo. El modelo moderno usa **Billing Meters** + `meter_events` (POST de eventos: `{event_name, payload:{value, stripe_customer_id}}`). Stripe agrega y factura al cierre.
- **Markup sobre uso de IA** (2026): Stripe Billing permite aplicar un % de margen sobre el costo crudo de tokens/llamadas a modelos — mandas tokens procesados, llamadas API, tareas de agente; Stripe los convierte en cargo facturable con tu margen. Cruza con [[262-credits-quota-billing-gen]] y [[339-billing-quotas-creditos]].

## Costos (verificado jun-2026, [no verificado])
| Concepto | Tarifa |
|---|---|
| Procesamiento tarjeta | **2.9% + $0.30** por transacción exitosa |
| **Stripe Billing** (capa subscripción) | **+0.7%** del volumen facturado |
| Incluido en el 0.7% | metering hasta 100M eventos/mes, Smart Retries, dunning, quotes, schedules |
| Capacidad metering | hasta 200k eventos/s, 99.999% uptime histórico |

El 0.7% aplica sobre revenue de subscripción, no es cargo plano por factura.

## Webhooks: el punto donde todos fallan
```js
const event = stripe.webhooks.constructEvent(rawBody, sig, endpointSecret);
```
- **El body DEBE ser crudo**, no JSON parseado. Cualquier middleware que re-serialice (express.json antes del handler) **rompe la firma HMAC**. Monta `express.raw({type:'application/json'})` SOLO en esa ruta.
- **Idempotencia**: todo webhook reintenta. Dedupe por `event.id` con unique constraint en DB. Procesar dos veces = doble fulfillment.
- **No es la única verdad**: pueden llegar fuera de orden o spoofearse. Antes de fulfillment crítico, haz `GET` del objeto por id y verifica `status`.
- Eventos clave: `checkout.session.completed`, `invoice.paid`, `invoice.payment_failed` (dispara dunning), `customer.subscription.updated/deleted`.

## Idempotency-Key (en los POST salientes)
Todo POST que crea cargos lleva header `Idempotency-Key` (UUID o tu `cart_id`/`order_id`). Si la red falla y reintentas, Stripe devuelve el mismo resultado en vez de doble cobro. Válido 24h.

## Connect (marketplaces / multi-seller)
Para pagar a terceros: cuentas **conectadas** (Express = onboarding hosteado por Stripe, recomendado). Patrones de flujo de dinero:
- **Destination charges**: cobras tú, transfieres al conectado (`transfer_data.destination`).
- **Direct charges**: el cargo vive en la cuenta del conectado, tú tomas `application_fee_amount`.
- **Separate charges & transfers**: máximo control, divides después.
KYC/payouts los maneja Stripe. Cruza con [[63-multi-tenancy-billing-saas]].

## Tax
**Stripe Tax** calcula y recauda automático por jurisdicción (`automatic_tax:{enabled:true}` en Checkout/Invoice). Registra nexos, aplica tasas correctas, genera reportes. No emite la factura fiscal legal de LatAm (eso es facturación electrónica aparte → cruza con [[296-facturacion-electronica-latam]]).

## Gotchas
1. **Amounts en enteros (centavos)** — `1999` = $19.99. Float = rechazos off-by-one. Zero-decimal currencies (JPY) no multiplican.
2. **Test vs Live keys** — webhook secrets son distintos por modo; un secret cruzado = firma inválida silenciosa.
3. **Reintentos de tarjeta fallida** (dunning) — configura Smart Retries + emails; si no, churn involuntario invisible.
4. **Proration sorpresa** — upgrades a mitad de ciclo cobran inmediato por defecto. Decide `proration_behavior` conscientemente.
5. **Cobertura LatAm limitada** — Stripe full solo BR/MX. Para CO/AR/PE usa rails locales. Cruza con [[295-pagos-latam-wompi-mercadopago]] y [[42-pagos-latam]].

**Fuentes:** docs.stripe.com (billing, webhooks, connect, tax, meters) · stripe.com/pricing (jun-2026).
