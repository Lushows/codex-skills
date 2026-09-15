# 339 · Billing, cuotas y créditos en SaaS de IA (el caso STUDIO)

> En un SaaS donde cada acción cuesta GPU real, el billing no es "cobrar la suscripción":
> es un sistema de contabilidad en tiempo real que decide si seguís quemando plata por un
> cliente que ya gastó su cuota. El ledger es tu fuente de verdad, NO el meter de Stripe.

## Las tres formas de cobrar consumo
| Modelo | Cómo | Cuándo conviene |
|---|---|---|
| **Suscripción + cuota** | plan fijo, N unidades/mes incluidas | predecible, el default SaaS |
| **Créditos (burndown)** | compra saldo, deduce N por acción | gen-AI con costo variable por job |
| **Flat + overage** | base fija, se factura el excedente al rate card | clientes que a veces se pasan |

Para STUDIO (videos = GPU caro y variable por duración) el modelo **créditos** es el natural: el cliente compra saldo, cada video cuesta créditos según resolución/segundos. Liga cada job a su **costo GPU real** (ref [[30-finops-gpu]]) para no vender créditos por debajo del COGS.

## Metering con Stripe (API basil, 2026)
Desde `2025-03-31.basil` **todo precio metered requiere un Meter**; los *usage records* legacy murieron.
```js
await stripe.billing.meters.create({ display_name:'Video generations',
  event_name:'video_generation', default_aggregation:{ formula:'sum' },
  value_settings:{ event_payload_key:'units' } })

await stripe.billing.meterEvents.create({ event_name:'video_generation',
  payload:{ stripe_customer_id:'cus_x', units:'3' },
  identifier:'job_abc123' })          // identifier = idempotencia, OBLIGATORIO
```
Stripe tiene **credit grants** nativos (display name + servicing period + monto), pero **[verificado] no soporta grants recurrentes, rollover ni wallets compartidas entre miembros**. Si necesitás eso (lo normal en equipos), el wallet vive en TU DB y Stripe solo cobra recargas.

## El ledger: tu fuente de verdad
- **Tabla append-only de transacciones**, NUNCA un contador mutable. Cada grant (+), cada consumo (−) es una fila inmutable; el saldo es la suma. Un `UPDATE balance = balance - n` pierde consistencia bajo concurrencia (dos jobs en paralelo leen el mismo saldo).
- Deduce créditos **antes** de despachar el job (reserva), y reembolsa si el job falla. Sin esto, un usuario lanza 50 videos en paralelo con saldo para 1.
- Los **meter events de Stripe tienen latencia de agregación** → no los leas para enforcement en tiempo real. Tu ledger enforce; Stripe reconcilia para la factura.

## Enforcement: soft cap vs hard cap
- **Soft cap**: avisás al 80%, permitís overage, facturás el excedente. Mejor UX, riesgo de impago.
- **Hard cap**: a 0 créditos devolvés **402 / bloqueo**. Cero riesgo, peor UX. Para gen-AI cara, hard cap por defecto + opción de auto-recarga.
- **Rate limit per-tenant**: token bucket en Redis, independiente del saldo, para frenar abuso/loops.
- **Entitlements**: mapeá `plan → features` en una tabla (`if entitlement('hd_export')`), no `if plan=='pro'` hardcodeado, o cada cambio de plan es un deploy.

## Dunning (recuperar pagos fallidos)
El involuntary churn es hasta ~48% del churn (ref [[337-saas-metrics-mrr-churn-ltv]]). Stripe **Smart Retries** usa ML sobre la red Stripe y **[verificado] recupera ~57% de los pagos que originalmente fallaron**; los emails de dunning llevan link de un clic para actualizar la tarjeta. Tras N reintentos fallidos → downgrade automático del plan, no corte abrupto.

## El ledger en una tabla (esquema mínimo)
```sql
CREATE TABLE credit_ledger (
  id          bigserial PRIMARY KEY,
  tenant_id   uuid NOT NULL,
  delta       integer NOT NULL,         -- +grant / -consumo (entero, nunca float)
  reason      text NOT NULL,            -- 'grant_purchase' | 'job:job_abc' | 'refund:job_abc'
  job_id      text,                     -- para reembolso idempotente
  created_at  timestamptz DEFAULT now()
);
-- saldo = SELECT COALESCE(SUM(delta),0) FROM credit_ledger WHERE tenant_id = $1;
```
- **Reserva atómica**: deduce e inserta en la misma transacción, con un `SELECT ... FOR UPDATE` o un check `SUM(delta) >= costo` dentro de la tx, para que dos jobs concurrentes no gasten el mismo saldo.
- **Reembolso idempotente**: antes de insertar el `+` por job fallido, verificá que no exista ya una fila `refund:job_abc` (el `job_id` único lo garantiza).
- **Nunca floats** para créditos: usa enteros (créditos enteros o "milicréditos") y evita errores de redondeo que acumulan centavos perdidos.

## Self-serve vs ventas asistidas
- **Self-serve (PLG)**: el usuario compra recargas solo, hard cap por defecto, auto-recarga opcional. Menor fricción, menor ARPA.
- **Asistido / enterprise**: contrato anual, créditos prepagados grandes, soft cap con overage facturado, factura por transferencia (no tarjeta). En LatAm muchos enterprise NO pagan con tarjeta → necesitás PSE/transferencia/factura electrónica, no solo Stripe.
- **Free tier**: créditos gratis limitados para activación; vigílalo como vector de abuso (rate limit + verificación de email/teléfono).

## Gotchas
1. **Meter event sin `identifier`** → un retry de red duplica el cobro.
2. **Contador mutable** → race condition, saldos negativos o jobs gratis.
3. **Leer el meter de Stripe para enforcement** → latencia; el cliente gasta de más antes de que Stripe agregue.
4. **No reembolsar créditos en job fallido** → el cliente paga por GPU que no entregó valor; soporte explota.
5. **Vender créditos bajo el COGS GPU** → cada venta pierde plata; ata el precio del crédito al costo real.
6. **Webhooks de Stripe sin verificar firma** → cualquiera te marca facturas como pagadas.

**Fuentes:** docs.stripe.com/billing/subscriptions/usage-based/advanced · docs.stripe.com/billing/revenue-recovery/smart-retries · stripe.com/billing/usage-based-billing · buildmvpfast.com (Stripe metered guide 2026).

Cruza con [[262-credits-quota-billing-gen]], [[294-stripe-a-fondo]], [[63-multi-tenancy-billing-saas]] y [[30-finops-gpu]].
