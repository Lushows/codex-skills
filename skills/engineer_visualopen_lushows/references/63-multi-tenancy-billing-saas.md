# 63 — Multi-tenancy y billing de SaaS

## Modelos de aislamiento de tenant (de menos a más aislado)
- **Shared DB + `tenant_id` (RLS)** — una tabla, columna `tenant_id`, Row-Level Security filtra. Barato, escala a
  miles, un esquema que migrar. **El default para SaaS LatAm pequeño/mediano.** Riesgo: un bug = fuga cruzada.
- **Schema-per-tenant** — un schema Postgres por tenant. Mejor aislamiento lógico, migraciones N veces, pooling complejo. Decenas-cientos.
- **DB-per-tenant** — aislamiento máximo (compliance, enterprise), costo/operación máximos. Pocos tenants grandes.

## Postgres Row-Level Security
```sql
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON orders USING (tenant_id = current_setting('app.tenant_id')::uuid);
SET app.tenant_id = 't_42';          -- por TRANSACCIÓN (por el pooling), no por conexión
```
**Crítico:** la app conecta con un rol **sin `BYPASSRLS`** y setea `app.tenant_id` en cada transacción. Supabase usa este patrón con `auth.uid()`.

## Usage-based / metered billing con Stripe (2026)
Desde la API `2025-03-31.basil` la API legacy de *usage records* desapareció: **todo precio metered requiere un
Meter.** Defines un Meter (cómo agregar eventos), envías **meter events**, Stripe los convierte en cargos. Stripe
hizo usage-based el default para AI startups (mandas tokens/llamadas/tareas de agente).
```js
await stripe.billing.meters.create({ display_name:'AI generations', event_name:'ai_generation',
  default_aggregation:{ formula:'sum' }, value_settings:{ event_payload_key:'units' } })
await stripe.billing.meterEvents.create({ event_name:'ai_generation',
  payload:{ stripe_customer_id:'cus_x', units:'3' }, identifier:'gen_abc123' })   // idempotencia!
```

## Modelo de créditos (común en AI)
El cliente compra saldo, deduces N créditos por generación. Implementa el **ledger en TU DB (tabla append-only de
transacciones, NO un contador mutable)** y reconcilia contra Stripe. Permite **soft cap** (avisar al 80%) vs **hard cap** (bloquear a 0).

## Enforcing limits & entitlements
Quota por tenant (requests/mes, asientos, storage). **Hard cap** = 402/bloqueo; **soft cap** = permites overage y
facturas. Rate limit per-tenant con token bucket en Redis. Liga cada generación a su costo GPU real (FinOps, ref
30) para atribuir margen. **Entitlements** mapea plan→features (`if entitlement` en vez de hardcodear `if plan=='pro'`).
**Dunning:** pagos fallidos → Smart Retries + emails → tras N fallos, downgrade. **Trial→paid:** trackea activación (el churn es por no-activación, no por precio).

## Gotchas
1. **RLS bypass del rol admin** — si la app conecta como superuser/owner, RLS NO aplica; usa rol dedicado.
2. **`SET tenant_id` por conexión con pooler** — con PgBouncer transaction-pooling debes setearlo por transacción o filtras el tenant equivocado.
3. **Meter events sin `identifier`** — sin idempotencia, un retry duplica el cobro.
4. **Contador de créditos mutable** — usa ledger append-only; un `UPDATE balance` pierde consistencia bajo concurrencia.
5. **Usage events tienen latencia de agregación** — no leas el meter para enforcement en tiempo real; lleva tu propio contador y reconcilia.
6. **Migraciones en schema-per-tenant** — olvidar un tenant deja esquemas desincronizados; automatiza el fan-out.

**Fuentes:** docs.stripe.com/api/billing/meter · stripe.com/billing/usage-based-billing · postgresql.org/docs/current/ddl-rowsecurity.
