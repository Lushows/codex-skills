# 69 — B2B / Enterprise SaaS web

El error fundacional del diseño B2B es tratarlo como B2C con logos más aburridos. La diferencia real es estructural: **no le vendes a una persona, le vendes a un comité.** **Léelo para el sitio de marketing que vende a empresas Y la UX del producto enterprise** (FACTUM facturación/fintech B2B; AGENTE STUDIO). Pareja de 13 (dashboards/app UI), 49 (CRO), 29 (pricing), 43 (fintech), 17 (copy). Regla de oro 2026: **bello Y claro — la era de "es B2B, puede ser feo" murió.**

## 1. El género y la realidad del comprador

En 2026 la decisión B2B promedio involucra ~8.2 stakeholders (en compras tecnológicas hasta 25). Cada uno tiene definición distinta de "valor" y poder de **veto, no de aprobación**. Tu sitio y producto sirven a varias personas a la vez:
- **El usuario** (lo usa a diario): le importa el workflow, la fricción. Compra con la demo y el free trial.
- **El champion** (Ops/RevOps/líder funcional): time-to-value, riesgo de adopción. Es tu vendedor interno — dale munición (case studies, ROI, comparativas).
- **El economic buyer** (CFO/director con P&L): ROI, costo, payback → la calculadora de ROI y métricas duras.
- **El technical/IT buyer:** integraciones, escalabilidad, arquitectura.
- **Security/legal/procurement:** SOC 2, GDPR, DPA, SLA. **Pueden matar el deal** sin que el champion se entere.
El comprador B2B es **racional, averso al riesgo y juega con dinero ajeno** (el costo de equivocarse supera al de no comprar) → "nobody got fired for buying X": vendes *seguridad de decisión*, no features. Dos motions: **PLG (product-led)** (el producto es el funnel; ACV <$10K, auto-adoptable, free tier; 58% del B2B SaaS ya lo corre) vs **sales-led** (ACV >$25K, comité, ciclo 3-12 meses; el sitio nutre, no cierra) vs **híbrido** (lo dominante: el IC se auto-educa y adopta gratis, escala a sales cuando el uso justifica presupuesto — diseña para ambos: "Start free" *y* "Talk to sales"). Segmenta **SMB** (self-serve, pricing público) → **mid-market** (trial + sales assist) → **enterprise** (demo, contact sales, security review).

## 2. El sitio de marketing B2B (el craft best-in-class)

Estándar Stripe/Linear/Vercel: **bello Y claro.** La primera pantalla responde en 5 segundos *qué haces, para quién, por qué importa*.
**Homepage/hero — estructura canónica:** headline + sub-headline + CTA primario + visual del producto + logos. Fórmula de value prop que convierte: *"[Resultado deseado] sin [dolor común]"* o *"The [categoría] platform for [audiencia específica]"*. "Build pipeline 3X faster" gana a "AI-powered platform with 50+ integrations" — específico filtra al no-ICP (eso es una feature). Linear: claridad de categoría + craft visual obsesivo.
**Mostrar el producto es no negociable:** Stripe/Notion/Slack/Vercel ponen UI real *above the fold* (screenshots de alta fidelidad, demos interactivas, product tours). Evita stock photography e ilustraciones genéricas que ocultan que no hay producto que mostrar.
**Social proof contextual** (no en una sola sección): 3-5 logos bajo el hero ("Trusted by"), case studies en páginas de producto, badges de seguridad en pricing. Testimonios con métrica + nombre + rol + empresa ("Redujo onboarding 50% — María, Head of Ops, Acme") aplastan a "¡gran producto!".
**Orden de secciones:** nav+hero → screenshot/demo → how it works → features (headers por *beneficio*, no por feature) → social proof intercalado → trust signals → pricing/footer.
**Pricing page** (de mayor intención): transparencia gana. Tiers públicos para SMB/mid-market y dirige enterprise a sales *con señal* ("Para equipos de +500 usuarios, contáctanos" — nunca un "Contact sales" desnudo sin pista de precio). Toggle mensual/anual, comparativa, FAQ. Para developer-first (relevante a FACTUM): docs impecables, API reference, quickstart — la documentación *es* marketing.

## 3. Conversión y el ciclo largo

**Doble CTA por intención:** "Start free trial" (listo para evaluar) + "Book a demo" (requiere evaluación guiada) — páginas de un solo CTA convierten mejor por *intent matching*; segmenta por audiencia (CTAs personalizados convierten 202% mejor).
**Benchmarks 2026:** el B2B SaaS promedio convierte visitante→lead ~1.5%; el top 10% llega a 8-15%. La diferencia es claridad, intent matching y diseño de formulario.
**Gating inteligente:** NO gatees todo — solo contenido de alto valor (reportes, calculadoras avanzadas) donde el lead justifica la fricción. Formularios cortos. Para el ciclo largo, captura el lead y nutre por email/retargeting (el deal no se cierra en una visita).
**ROI calculator** (arma decisiva para el economic buyer): el contenido interactivo convierte 2× más; quien construye su business case con tu calculadora es 2.1× más probable de comprar. Para FACTUM: "calcula cuántas horas/mes ahorras automatizando facturación".
**Comparison / vs-competitor pages:** capturan búsquedas de alta intención ("X vs Y") y dan al champion munición para el comité — honestas pero favorables.
**Trial vs freemium vs demo:** trial (urgencia) para mid-market; freemium (PLG, expansión) para SMB; demo para enterprise. Product tours interactivos = demo-proxy para self-serve.

## 4. La UX del producto enterprise

Es la herramienta del *daily driver*: power users, datos densos, workflows complejos. Prioriza **densidad de información y velocidad** sobre minimalismo decorativo. El app shell (sidebar, command palette Cmd+K tipo Linear, búsqueda global — ver 13) debe escalar a cientos de features sin colapsar.
**RBAC — la columna vertebral del enterprise.** Constrúyelo bottom-up: **RBAC primero** (todo depende de roles), audit logs segundo (todos lo piden), SSO tercero, SCIM al final solo si lo piden. Tres capas: page-level (acceso a secciones), operation-level (qué puede hacer), data-level (qué registros ve). Roles custom scoped por organización/recurso.
**Org/team structure:** organizaciones → workspaces/teams → miembros. **Onboarding de equipos, no individuos** (invitaciones, provisioning, roles por defecto, creación de workspace, métricas de uso). El **admin panel** concentra esta complejidad — diséñalo con tanto cuidado como el producto principal (es donde el economic buyer vive).
**Settings/admin:** billing, miembros, seguridad (SSO/SCIM), integraciones, audit logs, API keys — organiza por sección clara; la complejidad enterprise se gestiona con jerarquía y búsqueda, no escondiéndola.
**Ecosistema de integraciones:** un marketplace/directorio de integraciones es señal de madurez y eleva NRR. Para FACTUM: bancos, ERPs, **DIAN/entes fiscales LatAm**, contabilidad.
**Requisitos enterprise:** SSO (SAML/OIDC), audit logs tamper-evident con metadata rica (cada auth, cada cambio de estado, cada acción privilegiada), SLA, soporte dedicado, white-labeling.

## 5. Confianza, seguridad y la venta enterprise

Lo que un enterprise *requiere para poder comprar* — sin esto, procurement bloquea el deal aunque ames el producto.
**Trust center / security page:** permite self-service de procurement y acorta el ciclo de venta. Contiene: certificaciones, sub-procesadores, política de datos, DPA, contacto de seguridad.
**Compliance:** **SOC 2 Type II** es el estándar de facto en B2B US (sin él, deals grandes se bloquean); **ISO 27001** no es opcional para vender en Europa; **GDPR** para EU. Muestra badges públicamente; SOC 3 descargable, SOC 2 Type II bajo NDA (los badges AICPA expiran a 12 meses — actualízalos).
**Status page / uptime** público (tipo status.stripe.com) + **SLA** (uptime, breach notification) + **data residency** (dónde viven los datos — crítico en LatAm/EU). Diseña para el revisor de IT/security del comprador: dale documentación auto-servible, no un form que espera respuesta de un SDR.

## 6. PLG, onboarding & 2026

**PLG:** el producto *es* el funnel — free tier → activación (primer "aha" rápido, ligado al onboarding 30) → expansión/upsell in-product. Optimiza **NRR sobre nuevos logos** (las empresas que lo hacen comandan múltiplos de valuación superiores). Upsell embebido: límites de uso, gates de features premium, prompts contextuales.
**Tendencias 2026:** **AI como table stakes** (su ausencia penaliza; las AI-native crecen 3×), **AI agents para B2B**, **vertical SaaS** supera a horizontal (31% vs 28% crecimiento, mejor NRR — la data de dominio entrena mejor IA), y **el bar de diseño subió** (B2B se volvió bello).
**Para FACTUM (facturación/fintech B2B LatAm):** vertical + AI-native (facturación electrónica con cumplimiento fiscal local DIAN/SAT como moat de dominio — la IA que entiende normativa LatAm es el diferenciador) · trust doblemente crítico (es fintech: seguridad, cumplimiento, data residency local front-and-center) · PLG viable (free tier X facturas/mes → paid al escalar → enterprise con SSO/audit/multi-empresa) · ROI calculator ("horas ahorradas + multas evitadas") · sitio en español impecable mostrando el producto real, logos LatAm, comparativa vs Siigo/Alegra.

## B2B anti-patterns — blacklist
**value prop vago/buzzword** ("plataforma all-in-one impulsada por IA" — no dice qué haces ni para quién) · **no mostrar el producto** (solo ilustraciones/stock — señal de que no hay nada que mostrar) · **jerga y features-no-beneficios** (specs sin traducir a outcome del comprador) · **sin social proof** (ni logos, ni métricas, ni case studies) · **pricing oculto sin señal** ("Contact sales" desnudo — frena al mid-market que se auto-evalúa) · **sin trust/security para enterprise** (no SOC 2, no trust center, no status page → bloquea procurement) · **gatear todo** (formularios en cada contenido — mata el self-serve) · **feo "porque es B2B"** (el bar 2026 es bello Y claro) · **un solo CTA para todas las audiencias** (usuario, champion y CFO necesitan caminos distintos) · **onboarding individual en producto de equipos** (ignorar invitaciones, roles, org structure).
