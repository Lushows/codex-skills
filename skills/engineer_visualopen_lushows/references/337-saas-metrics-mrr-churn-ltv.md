# 337 · Métricas SaaS: MRR/ARR, churn, LTV/CAC y la North-Star

> Lo que no mides con definición exacta, lo inflas sin querer.
> MRR, churn y LTV/CAC se calculan con fórmulas frágiles: un mes de gracia mal contado o un
> CAC sin ads cargados y el dashboard miente. Aquí las definiciones que aguantan auditoría.

## El esqueleto: MRR → ARR
- **MRR** = suma de la suscripción **normalizada a mensual** de todo cliente activo. Anual ÷ 12. NO metas one-time fees, setup ni overage variable (eso es *non-recurring*).
- **ARR** = MRR × 12. Solo tiene sentido si el revenue es realmente recurrente; en usage-based puro, ARR es ficción → usa **run-rate** sobre últimos 3 meses.
- Descomponé el delta mensual: **MRR neto nuevo = New + Expansion − Contraction − Churned**. Sin esta cascada no sabés si creces por ventas o por dejar de sangrar.

## Churn: la trampa de las definiciones
| Métrica | Fórmula | Qué dice |
|---|---|---|
| **Customer churn** | clientes perdidos / clientes inicio mes | logos que se van |
| **Gross Revenue Retention (GRR)** | (MRR inicio − contraction − churn) / MRR inicio | piso sin expansión; **techo = 100%** |
| **Net Revenue Retention (NRR)** | (MRR inicio − churn − contraction + expansion) / MRR inicio | puede pasar 100% si expandís |

**Benchmarks 2026 [verificado]:** churn mensual B2B promedio ~3.5% (voluntario 2.6% + involuntario 0.8%); top performers <2%. NRR mediana ~88-90%; strong 110-120%; best-in-class >120%. SMB churna 2-4%/mes, enterprise 0.3-0.8%. GRR mediana privada ~88%. El **involuntary churn (tarjetas que fallan) llega al ~48% del churn total** → optimizar pagos es palanca de retención, no de finanzas (cruza con dunning en [[339-billing-quotas-creditos]]).

## LTV, CAC y la ratio que importa
- **LTV** = ARPA × margen bruto% × (1 / churn de revenue mensual). **Siempre con margen**, no revenue bruto: en GPU-SaaS el COGS se come 40-60% (ref [[30-finops-gpu]]).
- **CAC** = (gasto ventas + marketing **full-loaded**) / clientes nuevos. Cargá sueldos SDR, ads, herramientas. CAC sin nómina es vanity.
- **LTV/CAC**: meta ≥ 3. <1 = quemás plata por cliente; >5 = subinvertís en growth.
- **CAC payback** = CAC / (ARPA × margen). Meta < 12 meses SMB, < 18-24 enterprise. Es el de verdad manda en cash de startup bootstrapped.

## Cohorts y North-Star
- **Cohort de retención**: agrupá por mes de alta, seguí % de revenue/usuarios activos a M1, M3, M6, M12. Una curva que se **aplana** = product-market fit; una que baja a 0 = balde con hueco. Promedios globales esconden esto.
- **North-Star Metric**: una métrica que captura valor entregado (ej. "videos generados/semana" en STUDIO, no "logins"). Liga activación → retención → revenue. El churn casi siempre es **no-activación**, no precio.
- Instrumentá todo esto con eventos, no con queries a la DB de billing: cruza con [[323-analytics-tracking-posthog-ga4]].

## Quick-margin y Rule of 40
- **Quick Ratio** = (New MRR + Expansion) / (Churned + Contraction). >4 = crecés sano; <1 = el balde pierde más de lo que entra. Detecta el problema antes que el MRR neto.
- **Rule of 40**: crecimiento% YoY + margen EBITDA% ≥ 40. Permite quemar plata si creces rápido, o crecer lento si sos rentable. Para gen-AI con COGS GPU alto, el lado del margen pesa más.
- **Burn multiple** = cash neto quemado / MRR neto nuevo. <1 excelente, >2 ineficiente. Es el LTV/CAC del fundraising: cuánto cash quemás por cada $1 de ARR nuevo.
- **Magic Number** = MRR nuevo ×4 (anualizado) / gasto S&M del trimestre previo. >0.75 = pisá el acelerador de ventas.

## Cómo instrumentarlo sin mentir
- **Una sola fuente de verdad** del estado de suscripción (Stripe + tu DB reconciliadas), nunca dos dashboards que difieren.
- Snapshot **mensual congelado** del MRR por cliente: si recalculás el pasado con datos de hoy, los números cambian y pierdes auditoría.
- Eventos de producto (activación, uso) en PostHog/GA4 (ref [[323-analytics-tracking-posthog-ga4]]); revenue en billing. No mezcles: el funnel de producto y el de plata se cruzan, no se confunden.
- Define cada métrica en un doc con su fórmula exacta y ejemplo numérico; sin eso, cada quien calcula "churn" distinto.
- **No persigas un dashboard de 40 KPIs**: para bootstrapped lo que decide es payback < 12 meses, NRR y burn multiple. El resto es contexto, no acción.

## Gotchas
1. **MRR con descuentos**: registrá el MRR **neto del descuento**, no el list price, o infla NRR al expirar el cupón.
2. **Churn con anuales**: un cliente anual no puede churnar a mitad de año en tu contador mensual → usa fecha de renovación, no actividad.
3. **LTV sin margen**: triplicás el LTV y justificás un CAC insostenible.
4. **NRR > 100% tapando logo churn**: GRR baja + NRR alta = pocas cuentas grandes te sostienen; riesgo de concentración.
5. **CAC sin lag**: el cliente de este mes lo pagaste con ads de hace 2-3 meses; alinea ventanas o subestimás CAC en growth.

**Fuentes:** churnfree.com/blog/b2b-saas-churn-rate-benchmarks · digitalapplied.com (NRR benchmarks 2026) · culta.ai/blog/saas-churn-rate-guide-benchmarks · eaglerockcfo.com (SaaS benchmarks by stage).

Cruza con [[102-pricing-monetizacion-2026]], [[323-analytics-tracking-posthog-ga4]] y [[339-billing-quotas-creditos]].
