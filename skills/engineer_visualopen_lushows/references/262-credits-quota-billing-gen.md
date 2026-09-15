# 262 · Créditos, cuotas y billing para generación

> Cada video/imagen quema GPU-segundos reales; si no mides y limitas ANTES de generar, el usuario gratis te funde el margen.
> El patrón: un saldo de créditos, un débito atómico pre-generación, reconciliación post-job.

## Por qué créditos y no "minutos" ni "requests"
Una generación no cuesta lo mismo que otra: 4s de video LongCat ≠ 720p imagen SDXL ≠ 30s TTS. Cobrar por
"request" castiga al barato y subsidia al caro. Un **crédito** es una unidad abstracta que mapeas a costo
GPU: defines `créditos = ceil(costo_estimado * margen)`. El usuario ve "1 video HD = 50 créditos"; tú ves
GPU-segundos. Desacopla precio público del costo cambiante de la nube.

## Estimar el costo ANTES de generar (gating)
No puedes cobrar lo real porque aún no corriste el job. Estima por **parámetros del request**:

| Driver | Ejemplo | Fórmula aprox |
|---|---|---|
| Duración salida | video Ns | `seg * créditos_por_seg_modelo` |
| Resolución | 720p vs 1080p | factor 1.0 / 2.25 (área²) |
| Pasos/steps | 20 vs 50 | lineal en steps |
| Modelo | LongCat vs SDXL | tabla por modelo (VRAM·tiempo) |

Calibra la tabla con jobs reales (mide GPU-segundos del handler) y deja **margen** (2-4×) para picos,
cold starts y reintentos. Cruza con [[112-execution-timeout-cold-start-economics]] y [[30-finops-gpu]].

## El débito atómico (lo que evita el doble-gasto)
Race clásico: dos requests simultáneos ven saldo 50, ambos lanzan job de 50, terminas en -50. Solución:
debitar en una transacción condicional ANTES de encolar.

```sql
-- atómico: solo descuenta si alcanza; falla si no
UPDATE wallets SET balance = balance - :cost
 WHERE tenant_id = :t AND balance >= :cost
RETURNING balance;            -- 0 filas => 402 Payment Required
```

Postgres con `SELECT ... FOR UPDATE` o el `UPDATE ... WHERE balance >= cost` ya serializa. En Redis usa un
script Lua (atómico) sobre `DECRBY` con check. **Nunca** leas-luego-escribas en dos pasos.

## Reservar → confirmar → reembolsar (saga)
La estimación no es el costo real y los jobs fallan. Patrón de 2 fases:
1. **Reserva**: debita el estimado, marca `hold` con `job_id`. El saldo ya bajó (no se puede gastar dos veces).
2. **Confirma** (job OK): convierte el hold en gasto definitivo. Si el real difería, **ajusta** (reembolsa
   la diferencia o cobra extra hasta un tope).
3. **Reembolsa** (job falla/timeout/OOM): libera el hold completo. El usuario NO paga por tu fallo de infra.

Esto exige un **ledger append-only** (no un solo número mutable): cada fila es `+compra`, `-reserva`,
`-gasto`, `+reembolso`, con `idempotency_key`. El saldo es la suma. Auditable, reconciliable, a prueba de
reintentos. Cruza con [[115-async-render-largo-poller-durable]] para el ciclo submit/poll/webhook del job.

## Cuotas además de créditos
Créditos limitan el total; las **cuotas** limitan el ritmo y el abuso:
- **Rate limit** por tenant (req/min) → protege la GPU de ráfagas, independiente del saldo.
- **Concurrencia** (N jobs simultáneos por plan) → el free no monopoliza la cola.
- **Cuota mensual** que se **resetea** (free tier: 100 créditos/mes) vs créditos comprados que **no
  expiran**. Modela dos buckets y gasta primero el que expira.

## Planes y modelos de cobro
- **Prepago/PAYG**: compra packs de créditos vía [[plugin_stripe]] (Checkout) → webhook `payment_intent.succeeded`
  acredita el ledger con `idempotency_key = event.id` (Stripe reintenta webhooks).
- **Suscripción**: el ciclo `invoice.paid` recarga la cuota mensual.
- **Overage**: si excede el plan, debita de créditos comprados o bloquea (config por tenant).
- **Free tier**: cuota baja + watermark obligatorio + concurrencia 1.

## Errores que muerden
- Acreditar en el webhook SIN idempotencia → Stripe reintenta y duplicas saldo. Clave: el `event.id`.
- Cobrar el estimado y no reembolsar en fallo → soporte lleno de reclamos legítimos.
- Mutar un campo `balance` único sin ledger → imposible auditar "¿por qué tengo -30?".
- Estimar de menos sin margen → el modelo caro corre gratis y sangras.

Cruza con [[63-multi-tenancy-billing-saas]] para aislamiento por tenant y [[254-cost-allocation-chargeback-multitenant]] para imputar el costo GPU real a cada cliente.
