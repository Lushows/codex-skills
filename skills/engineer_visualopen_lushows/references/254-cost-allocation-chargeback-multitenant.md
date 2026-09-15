# 254 · Cost allocation y chargeback multi-tenant (cost-per-job atribuible)

> Sin atribución por job no sabes qué marca/feature es no-rentable — y subsidias al cliente que te quema.
> La unidad es el **job**: cada uno tagueado, con `billed_sec × $/seg` grabado al cierre. Todo lo demás agrega de ahí.

## La unidad atómica: cost-per-job
Cada job emite al terminar un registro con:
```
job_id, tenant_id (brand_id), job_type (avatar|video|imagen), gpu_type,
billed_sec (incluye cold_start + queue + inference), price_per_sec,
cost = billed_sec * price_per_sec, ts
```
`cost` debe incluir el cold-start: en jobs cortos domina ([[30-finops-gpu]]). Atribuir solo el tiempo de inferencia sub-factura el job real 5-10×.

## Costos directos vs compartidos (cómo repartir)
| Tipo | Ejemplo | Atribución |
|---|---|---|
| **Directo** | GPU-segundos del job | 100% al tenant del job |
| **Storage** | pesos en Network Volume, outputs en R2 | por GB-mes y por tenant si el output es suyo |
| **Egress** | descarga de resultados | por GB servido al tenant |
| **Compartido** | warm-pool idle, gateway, control plane | prorratea por share de jobs o GPU-seg (no a partes iguales) |

El warm-pool idle es el costo compartido más traicionero: facturas 24/7 a nadie en concreto. Prorratéalo por % de GPU-segundos consumidos por cada tenant en el periodo, no por headcount.

## Showback vs chargeback
- **Showback**: reportas a cada marca su gasto GPU (compute+storage+egress) para visibilidad. No factura. Primer paso siempre.
- **Chargeback**: lo facturas de verdad. Requiere precio con margen sobre el costo atribuido y unit economics sólidos ($/render, $/minuto-avatar).
En un SaaS multi-tenant esto se enlaza al billing real ([[63-multi-tenancy-billing-saas]]): el cost-per-job alimenta el medidor de uso que cobra Stripe.

## Pipeline de datos
1. **Emite** el registro por job a una cola/tabla (no lo calcules después; el precio spot cambió).
2. **Agrega** a diario por `(tenant, job_type, gpu_type)` → tabla de hechos.
3. **Reporta**: dashboard por marca con $ compute/storage/egress, $/job promedio y p99, margen.
4. **Alerta** en anomalías: cost-per-job de una marca que se dispara (cold-start storm, retries en loop) → posible LLM10 Unbounded Consumption.

## Unit economics y pricing con margen
Precio al cliente = `costo_atribuido_por_unidad × (1 + margen)`. Trackea el margen real por tenant: un cliente con muchos cold-starts (jobs cortos esporádicos) cuesta más por unidad que uno con batch denso. El pricing plano subsidia al esporádico. Si vas a chargeback, considera un piso por job que cubra el cold-start.

## Kill-switch y budgets por tenant
Cap duro de `$/día` o `jobs/hora` **por marca**. Un loop de agente o batch runaway de un tenant no debe drenar el budget global ni el de otros tenants. La alerta avisa; el kill-switch corta. Mide contra el SLO del servicio ([[159-monitoreo-slo-servicio-gpu]]) para no cortar carga legítima.

## Gotchas
1. Repartir costos compartidos a partes iguales (no por uso) castiga al tenant pequeño y subsidia al grande.
2. Olvidar storage/egress → el reporte miente; en modelos grandes el GB-mes del volumen pesa.
3. Calcular costo post-hoc con precio actual cuando el job corrió en spot a otro precio → atribución errónea.
4. Sin `job_type` en el tag, sabes qué marca gasta pero no qué feature es no-rentable.

**Fuentes:** finops.org/framework/capabilities (showback vs chargeback) · docs.runpod.io/serverless/pricing.

Cruza con [[63-multi-tenancy-billing-saas]], [[159-monitoreo-slo-servicio-gpu]] y [[30-finops-gpu]].
