# 79 — Insurance & insurtech

El seguro es el **grudge purchase** arquetípico: la gente lo compra porque debe, no porque quiera. La percepción es triple: **aburrido, confuso, desconfiado** (el 51% admite no entender al menos un aspecto de su cobertura). El mandato de diseño = **trust + clarity**, no delight decorativo. **Léelo para seguros, insurtech, quote/claims flows.** Pareja de 43 (fintech/números/confianza), 21 (forms), 18 (quote conversacional), 51 (AI underwriting). Regla de oro: **cada término técnico no explicado es un punto de abandono — y empatía radical en el claim.**

## 1. El género y la psicología del comprador

Dualidad emocional: el miedo (protección de familia/carro/salud — alto stakes) vs el tedio/fricción (formularios eternos, jerga). El diseño modula tono: cálido y empático en el quote, sereno y rápido en el claim. **El problema de la jerga es central:** *deductible, premium, coverage, copay* son palabras que el usuario no traduce a "cuánto pago / cuánto recibo". **Tipos:** auto (transaccional, telematics), hogar, salud (la jerga más densa), vida (emocional, beneficiarios), viaje (impulso, embedded), SMB/pyme (B2B, broker-driven); LatAm añade SOAT, exequial, microseguro. **La disrupción Lemonade ("make insurance lovable"):** convirtió el trámite en conversación de 90s, alineó incentivos (el sobrante va a caridad → reduce la sospecha de "me niegan el claim para ganar"), bots con personalidad. El principio replicable no es el bot: es **velocidad radical + transparencia de incentivos + lenguaje humano**.

## 2. El quote flow (el core de conversión)

Regla maestra: **minimizar la fricción percibida sin sacrificar la data necesaria para tarificar.**
- **Conversational quote (modelo Maya):** una pregunta a la vez, adaptativa, en vez de un wall-of-form (Maya recomienda cobertura, explica y cobra en <90s; el *one-question-per-screen* dispara completion en móvil).
- **Progressive disclosure:** pedir lo mínimo para un quote inicial; los detalles finos solo cuando ya está comprometido.
- **Pre-fill / data enrichment — "don't ask what you can look up":** placa → marca/modelo/año; dirección → metraje/zona de riesgo; documento → demográficos. Cada campo auto-completado es fricción eliminada.
- **Instant quote con real-time premium:** el precio se actualiza en vivo al mover sliders de cobertura/deducible (el usuario *ve* el trade-off precio↔cobertura).
- **"What affects my price" transparency:** explicar qué variables suben/bajan la prima → convierte el precio de caja negra en algo entendible.
- **Plan comparison:** tiers en columnas (Básico/Recomendado/Premium), uno "recomendado" destacado (anchoring), diferencias en filas escaneables, badge "más popular".
Inputs móviles: dropdowns/sliders/steppers (no texto libre evitable), barra de progreso siempre visible.

## 3. Explicar cobertura y resolver la jerga

La cobertura debe entenderse **sin leer la póliza:** **plain language** ("lo que pagas tú antes de que entre el seguro" en vez de "deducible"; glosario contextual inline, no un PDF aparte) · **visual "qué cubre / qué NO cubre"** (dos columnas con checks y X; las **exclusions visibles y arriba**, no en letra chica — contra-intuitivo pero genera confianza) · **escenarios "si pasa X, recibes Y"** (el patrón CMS de *coverage examples* "tener un bebé"/"manejar diabetes" simula un claim real y muestra cuánto paga el seguro vs el usuario) · **deducible/prima con ejemplo numérico** ("Prima: pagas $X/mes. Deducible: si chocas, pagas los primeros $Y, el seguro el resto") · personalización ("tu carro", "tu apartamento", no genéricos).

## 4. Claims (el momento de la verdad)

El claim es **el peor momento del usuario** (algo malo pasó) y donde el seguro cumple o traiciona su promesa — 80% empatía, 20% formulario.
- **Digital FNOL (First Notice of Loss):** captura el aviso de siniestro guiado/conversacional (Lemonade: 96% de FNOL los toma el bot, 55% de claims resuelto 100% automático).
- **Photo/document upload nativo:** subir foto del daño desde el móvil (el móvil ES la cámara del peritaje).
- **Status tracking transparente:** timeline (recibido → en revisión → aprobado → pagado; la incertidumbre es lo que más estresa).
- **Fast payout:** Lemonade evalúa, verifica y paga en ~2 segundos, muchos en <3 min — **el instant payout es el mayor diferenciador emocional del sector**.
- **Empatía en copy/design:** tono calmado, sin culpabilizar, sin jerga, sin pedir 10 documentos de golpe ("Lamentamos lo que pasó. Vamos a resolverlo juntos").
- **Fraud-prevention vs fricción:** la detección antifraude corre **en background**, invisible para el usuario honesto (no castigar al 95% legítimo con fricción diseñada para el 5%).

## 5. Policy management & trust

**Policy dashboard:** un lugar para cobertura activa, documentos descargables, pagos/recibos, beneficiarios; predictivo (avisar renovaciones, gaps de cobertura). **Trust signals con peso real:** ratings AM Best/S&P (A+/A++), estadísticas reales de **claims pagados** ("pagamos el 98%, en promedio en X días"), regulación/licencia visible, años en mercado. **Anti-fine-print ethics:** poner exclusiones y condiciones de frente (la transparencia *es* el trust signal en 2026). **Renewals sin dark patterns:** precio nuevo vs anterior explícito, **cancelación tan fácil como la compra** (cada vez más exigido por regulación). **La relación:** no desaparecer entre la venta y el claim (check-ins, ajustes por cambios de vida, educación útil).

## 6. LatAm, móvil & 2026

**Realidad LatAm:** penetración ~3% del PIB, desconfianza estructural (historia de aseguradoras que no pagan), economía informal/cash, el **broker local** como figura de confianza insustituible. **WhatsApp es el canal, no un canal** (cotizar, comprar, avisar siniestros, hablar con agente — todo dentro de WhatsApp; encaja perfecto con un agente tipo bot + handoff a humano/broker) · **microseguro y on-demand** (pólizas pequeñas, por evento, pago flexible para informales) · **mobile-first absoluto** (peso ligero, pocos pasos) · confianza local (logo Superfinanciera, testimonios reales, el broker como cara humana, prueba de pagos).
**Tendencias 2026:** **AI underwriting** generalizado (telematics/IoT) pero con riesgo de **bias/discriminación** — el EU AI Act clasifica underwriting/claims como *high-risk* (exige explicabilidad, supervisión humana, bias testing) y 23+ estados US adoptaron el model bulletin del NAIC → diseña **explainability visible** ("por qué este precio") · embedded insurance (cobertura en el checkout de otra plataforma) · usage-based/telematics (46-70% de nuevas pólizas auto directas ya son UBI) · AI claims instantáneos.

## Insurance anti-patterns — blacklist
**jerga sin traducir** (deducible/prima/coaseguro sin explicación inline) · **quote form infinito** (30 campos de golpe, sin progress bar, sin pre-fill) · **exclusiones ocultas / letra chica** (enterrar lo que NO cubre = traición de confianza) · **claim doloroso** (pedir papeles físicos, sin status tracking, silencio total) · **pago lento sin visibilidad** (no decir cuándo ni cuánto) · **cero transparencia de precio** (caja negra, sin "qué afecta tu precio") · **no-mobile / pesado** · **ignorar WhatsApp en LatAm** · **señales de desconfianza** (sin ratings, sin claims-paid stats, sin regulador visible) · **dark patterns en cancelación/renovación** (fácil entrar, imposible salir; auto-renovación sorpresa) · **empatía cero en claims** (tono burocrático/culpabilizador en el peor momento) · **AI opaca** (pricing/rechazo sin explicación → riesgo de bias y de incumplimiento 2026).
