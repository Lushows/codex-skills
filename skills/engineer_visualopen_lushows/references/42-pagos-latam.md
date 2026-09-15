# 42 — Pagos LatAm (integración)

## Stripe (baseline global, cobertura local LatAm limitada — full solo BR/MX)
Flujo: crea **PaymentIntent** server-side (amount, currency, `automatic_payment_methods`), confirma client-side con
Stripe.js/Elements, o usa **Checkout** (página hosteada → `checkout.session.completed`). **Siempre `Idempotency-Key`**
(UUID/cart-id) en POSTs. **Verifica webhooks** con `stripe.webhooks.constructEvent(rawBody, sig, secret)` — la ruta
**debe usar el body CRUDO**, no JSON parseado, o la firma falla. **Connect** para marketplaces (split, payouts). Dedupe por `event.id`.

## Wompi (gateway de Bancolombia, default Colombia)
Pide **`acceptance_token`** de `/merchants/{public_key}`, luego `POST /transactions` con `amount_in_cents` (COP,
enteros), `currency:"COP"`, `customer_email`, `reference` única, `payment_method`. Rails: **PSE** (`financial_
institution_code`, `user_type`, `user_legal_id_type/_id`), **Nequi** (cel 10 dígitos), **Bancolombia Transfer**,
cards (tokeniza 1 vez → payment source recurrente). Verifica el checksum/firma del webhook.

## MercadoPago (el gateway dominante LatAm)
**Checkout Pro** (hosteado: crea `preference` → redirige a `init_point`) o **Checkout API/Bricks**. Webhooks con
header **`x-signature`**: split en `ts` y `v1`, reconstruye `id:<data.id>;request-id:<x-request-id>;ts:<ts>;`,
HMAC-SHA256 con tu secret, compara a `v1`. Manda **`X-Idempotency-Key`**. Webhooks en cada cambio (Pending/Approved/Rejected).

## Cross-border (dLocal / EBANX)
Cobras en USD/EUR pero recaudas local → **dLocal**/**EBANX** agregan 200+ métodos locales con una API + FX/
settlement. dLocal es PISP certificado en Brasil (Pix in-app sin redirect bancario).

## Pix (Brasil) / COD
**Pix:** rail instantáneo del Banco Central, 24/7, QR/copia-e-cola, settle en segundos; integra vía EBANX/dLocal/MP;
**Pix Automático** para recurrente. También **boleto** (BR) y **OXXO** (MX) para no-bancarizados.
**Contra-entrega (COD)** — enorme en Colombia. Sin API: modélalo como state machine
(`pending→confirmed→shipped→collected`), reconcilia cash vía reportes del courier; mitiga fraude/no-show con depósitos/verificación de dirección.

## Flujo de checkout WhatsApp-commerce
Carrito en chat → genera **payment link** (Stripe Payment Link, MP `init_point`, o link Wompi) → usuario paga en
browser → **webhook** flipea la orden a paid → bot confirma. Mantén `reference` = tu `order_id` para reconciliación trivial.

## Gotchas
1. **Nunca toques data de tarjeta cruda** — usa hosted checkout/tokenización para quedar en **PCI SAQ-A**; manejar PANs explota tu scope PCI.
2. **Idempotencia de webhook obligatoria** — todos reintentan; dedupe por `event.id`/`payment.id` + unique constraint en DB.
3. La verificación de firma **necesita el body crudo**; cualquier middleware JSON que re-serialice rompe el HMAC (Stripe, MP, Wompi).
4. **Amounts son enteros en centavos** (COP/BRL/MXN) — float causa rechazos off-by-one.
5. Los webhooks **no son la única fuente de verdad** — también haz GET del pago por id antes de fulfillment (se pueden spoofear/llegar fuera de orden).

**Fuentes:** docs.stripe.com/webhooks · docs.wompi.co · mercadopago.com.br/developers (webhooks) · dlocal.com · docs.ebanx.com.
