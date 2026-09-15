# 324 · A/B testing & experimentación (significancia, CUPED, holdouts)

> Un experimento mal diseñado da más confianza que ninguno y peores decisiones.
> Esto cubre potencia, parar a tiempo, reducir varianza y los pitfalls que invalidan el test.

## Diseño antes de tocar nada
1. **Una hipótesis falsable**: "mover social proof junto al CTA sube `order_placed` ≥X%".
2. **Métrica primaria única** + **guardrails** (latencia, refunds, churn) que no deben empeorar.
3. **Tamaño de muestra / potencia (power 80%, α 5%)** calculado ANTES: define MDE (efecto mínimo
   detectable). Sin esto no sabes cuánto correr y caes en peeking.
4. **Unidad de aleatorización** consistente (usuario, no sesión) y estable cross-device vía `distinct_id`.

## Significancia — el campo minado
- **No mires y pares cuando "ya da significativo"** (peeking): infla el falso positivo del 5% al 20-30%.
- **Sequential testing / always-valid p-values**: diseñado para mirar continuo y parar temprano SIN
  romper el α. Statsig, GrowthBook, Eppo lo traen nativo. Úsalo si necesitas decidir rápido.
- **Frecuentista vs bayesiano**: p-value responde "¿es ruido?"; bayesiano da "P(B>A)" y pérdida esperada,
  más intuitivo para negocio. Elige uno y sé consistente; no cambies de marco a mitad de test.
- **Corrige multiplicidad**: muchas variantes/métricas → Bonferroni o similar, o inflas falsos positivos.

## CUPED — table-stake en 2026
**Controlled-experiment Using Pre-Experiment Data**: regresa el outcome sobre covariables pre-experimento
(ej. tasa de conversión histórica del usuario) para **reducir varianza 30-60%**. Efecto práctico: un test
que necesitaba 4-6 semanas alcanza significancia en 2-3. Si tu herramienta lo soporta, actívalo siempre que
haya historia del usuario. Reduce tamaño de muestra requerido 30-50%.

## Feature flags como motor de experimentos
El mismo flag que hace gradual rollout ([[366-feature-flags-gradual-rollout]]) reparte variantes:
- **Decouple deploy de release**: código en prod a 0%, abres tráfico por flag → rollback instantáneo sin redeploy.
- **Targeting** por segmento (país, plan, cohorte) directamente en el flag.
- **Mismo `distinct_id`** que tu analytics ([[323-analytics-tracking-posthog-ga4]]) → assignment y exposición
  ligados al evento de conversión. Registra **exposición** (`$feature_flag_called`), no solo asignación.

## Holdouts y medición de largo plazo
- **Global holdout**: % de usuarios que NO ve NINGÚN experimento, para medir el impacto agregado real de
  todo el programa (los uplifts individuales no suman; hay interacción y novelty).
- **Novelty / primacy effect**: el lift de la primera semana suele decaer; corre largo o usa holdout para el efecto sostenido.
- **Guardrails**: si la primaria sube pero un guardrail (refunds, INP) empeora, no lanzas.

## Pitfalls que invalidan todo
1. **Peeking** sin método secuencial = decisiones sobre ruido.
2. **SRM (Sample Ratio Mismatch)**: el split real no es 50/50 → bug de asignación, **descarta el test**.
3. Cambiar la métrica primaria a posteriori para "encontrar" un ganador (HARKing).
4. Terminar al primer cruce de la línea sin alcanzar la muestra planeada.
5. No medir guardrails: ganas conversión, pierdes margen o velocidad.
6. Interferencia entre experimentos solapados sin holdout que lo aísle.

**Fuentes:** statsig.com/perspectives (ab-testing vs flags) · businessanalytics.substack.com (AB framework) ·
geteppo.com (flags→AB) · vwo.com (advanced ab-testing).

Cruza con [[366-feature-flags-gradual-rollout]] y [[323-analytics-tracking-posthog-ga4]].
