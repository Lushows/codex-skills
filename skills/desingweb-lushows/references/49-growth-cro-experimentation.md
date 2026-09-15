# 49 — Growth, CRO & experimentación (que lo diseñado convierta y crezca)

La ciencia de hacer que lo diseñado **convierta y mejore con el tiempo**. Belleza sin conversión es arte; belleza que convierte y se optimiza es diseño. **Léelo cuando quieras que una página/producto rinda y crezca, no solo se vea bien.** Pareja de 17 (copy), 29 (pricing), 30 (activación), 31 (prueba social).

## 1. El mindset & proceso

CRO ≠ "rediseñar por opinión". *Redesign by opinion* parte del HiPPO (Highest Paid Person's Opinion); **CRO parte de evidencia**. La unidad no es la página bonita, es la **hipótesis falsable.**
**Optimization loop:** `MEASURE → ANALYZE → HYPOTHESIZE → PRIORITIZE → TEST → LEARN → ITERATE`. Hipótesis en formato obligatorio: *"Porque observamos [dato], creemos que [cambio] producirá [efecto en métrica] para [segmento]. Lo sabremos si [métrica] cambia X%."* Un test perdido que enseña *por qué* vale más que un ganador sin explicación.
**Data-driven vs data-informed:** lo **cuantitativo dice QUÉ pasa, lo cualitativo dice POR QUÉ**. Nunca optimices solo con uno.

## 2. A/B testing (a fondo)

**Test válido:** **sample size pre-calculado** (depende de baseline CR + MDE + significancia; 80% power, α=0.05 → N fijo; calcúlalo ANTES). **Significancia** (p<0.05 = 95% confianza) = "probablemente no es ruido", NO "es importante" (reporta también intervalo de confianza + tamaño del efecto). **Duración mín 1-2 ciclos completos** (semanas) por estacionalidad.
**Pitfalls que invalidan:** **peeking** (mirar y parar al ver "ganador" infla el false positive de 5% a ~40% → defensa: pre-commitment N+fecha, o sequential testing/always-valid p-values de PostHog/Statsig) · **novelty effect** (segmenta new vs returning) · **multiple comparisons** (20 variantes → un "ganador" por azar; corrige Bonferroni o reduce) · **SRM** (split torcido = test roto).
**Qué testear (high-impact):** propuesta de valor/headline, CTA (copy + jerarquía, no solo color), oferta/precios, formularios/checkout, social proof. Evita low-impact (color de botón aislado) salvo que sobre tráfico.
**Prioritization:** **ICE** (Impact×Confidence×Effort, ideas) · **PIE** (Potential×Importance×Ease, qué página) · **PXL** (criterios binarios, menos sesgo). Patrón: PIE para elegir página, ICE para tests dentro.
**Stack 2026** (Google Optimize murió 2023): dev-first → **PostHog** (analytics+flags+A/B+replay+surveys unificado, open-source), **Statsig**, **GrowthBook**, Eppo; visual/marketing → VWO, AB Tasty, Optimizely. **Server-side > client-side** (sin flicker/FOUC, mejor CWV, testea lógica — la tendencia 2026).
**Cuándo NO A/B:** **bajo tráfico** (si necesitas >4 semanas para N, no lo hagas) → usa best-practice redesign + before/after, painted-door, **moderated testing (5 usuarios = ~80% de problemas)**, heatmaps, surveys.

## 3. Funnel & conversión

**AARRR (Pirate Metrics):** `ACQUISITION → ACTIVATION → RETENTION → REVENUE → REFERRAL` (muchos ponen Retention antes de Revenue). Mapea cada paso, mide drop-off, **ataca la fuga mayor primero** (el cuello de botella manda).
**Levers de landing de alta conversión (la ciencia):** **one primary action per page** (mide el *attention ratio* links:objetivos, ideal 1:1 en campaña) · above-the-fold responde en 5s (qué/para quién/por qué tú/qué hago) · jerarquía visual hacia el CTA · reducir fricción/ansiedad/riesgo (trust, garantías, prueba social cerca del CTA, precio transparente).
**Form/checkout (donde más se pierde):** elimina campos · **guest checkout** obligatorio · inline validation/autofill/single-column · costo total temprano (shipping shock = abandono) · progress indicator + recuperación de carrito.
**Friction audit:** recorre el flujo como usuario nuevo en móvil, cuenta clicks/esperas/dudas/rage-clicks (session recording). **Micro vs macro conversions:** optimiza micro (add-to-cart, scroll 75%) para diagnosticar dónde se rompe el camino a la macro.

## 4. Analytics & medición

**Vanity vs actionable:** page views/likes/sesiones = vanity si no se ligan a acción. Actionable: conversion rate, **activation rate**, **retention** (curva que se aplana = PMF), **CAC/LTV** (sano **LTV:CAC ≥ 3:1**), payback.
**North Star Metric:** la única que captura el valor entregado ("pedidos completados/semana", no "registrados").
**Tracking plan:** documento vivo que define cada **event** (`order_completed`) + properties + cuándo dispara. Naming `object_action`, snake_case. Sin él, los datos son basura.
**Stack:** **GA4** (web/atribución) + product analytics (**PostHog/Amplitude/Mixpanel** → funnels, cohortes, retention) + heatmaps/replay (**Clarity** gratis, Hotjar, PostHog) + cualitativo (surveys exit-intent "¿qué te frenó?", NPS, entrevistas). Atribución: acepta dirección, no precisión decimal.

## 5. Growth loops & retención

**Funnel vs loop:** el funnel es lineal; el **growth loop** reinvierte el output de una cohorte como input que adquiere la siguiente → **crecimiento compuesto defendible** ("loops are the new funnels"). Tipos: **viral/referral** (usa→invita→nuevo usuario) · **content** (uso genera contenido indexable→SEO→tráfico) · **paid** (revenue→ads, solo si LTV>CAC con payback corto).
**Retención = el cimiento** (sin ella todo loop fuga; optimiza retención ANTES de escalar adquisición — no eches agua a un balde agujereado).
**Activation/aha:** setup → **aha** (valor central por 1ª vez) → habit. Encuentra el aha correlacionando acciones tempranas con retención ("7 amigos en 10 días"). **PLG:** el producto es el motor (free trial/freemium/self-serve) sobre activation loops; lifecycle/email orquesta el ciclo.

## 6. Psicología & tendencias 2026

**Cialdini ético:** social proof real cerca del CTA · scarcity/urgency **solo si es verdad** (falsa = pierde confianza + riesgo legal) · anchoring (plan caro primero) · reciprocity/authority/commitment · reducir riesgo/ansiedad (garantías, "cancela cuando quieras", FAQ que mata objeciones).
**AI en CRO (2026):** AI personalization en tiempo real, hypothesis suggestions, **multi-armed bandits** (auto traffic-allocation al ganador), predictive (probabilidad de conversión/churn). Útil pero **la IA optimiza la métrica que le das** — si le das la equivocada, optimiza el desastre eficientemente. Otras: server-side por defecto, herramientas unificadas, CRO consciente de CWV (velocidad ES conversión), privacy-first measurement.

## Growth/CRO anti-patterns — blacklist
dark patterns (checkboxes pre-marcados, confirmshaming, roach motel, urgencia falsa — ilegal + mata LTV) · HiPPO decisions · redesign sin datos (baseline ni hipótesis) · peeking / parar al primer "ganador" · testear con bajo tráfico y declarar sin significancia · vanity metrics (celebrar signups mientras retención/revenue mueren) · test sin hipótesis ("probemos a ver") · optimizar local ignorando el cuello de botella · demasiadas variantes sin corrección · cambiar el test en marcha · ignorar lo cualitativo (solo números, nunca el porqué) · escalar adquisición sobre balde agujereado · copiar al competidor sin saber si a ellos les funciona.
