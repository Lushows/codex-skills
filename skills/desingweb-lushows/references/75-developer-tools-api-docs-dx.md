# 75 — Developer tools, API docs & DX

El developer es el usuario más hostil al marketing que existe: **escéptico** (asume que mientes hasta que el código corre), **time-poor** (evalúa en minutos), **odia el fluff** ("seamless/powerful/next-gen" lo expulsan). No lee: escanea buscando código. La verdad central: **"the docs ARE the product"** — para una dev tool la documentación es el marketing, el sales pitch y el onboarding a la vez (Stripe ganó su mercado por DX, no por mejores rails). **Léelo para API docs, dev tools, portales de developers** (FACTUM invoicing API, GASTROWHATS, cualquier API que expongas). Pareja de 51 (productos de IA), 18 (AI-native UI), 69 (B2B), 35 (error states). Regla de oro: **Time-To-First-Call (TTFC) es la métrica reina — código en el hero, sandbox sin registro.**

## 1. El género DX y la audiencia developer

**El developer journey:** `discover → evaluate → integrate → scale`, cada etapa con su métrica: discover (¿entiendo qué hace en 5 seg?), evaluate (¿corro algo en mi terminal sin registrarme?), integrate (**TTFC**: best-in-class llega a un request exitoso en **<2 min**, quickstart en ≤10 pasos), scale (¿confiable, versionada, SDKs idiomáticos?). Lo que el dev valora: speed-to-first-call, claridad sin ambigüedad, confiabilidad (uptime, no breaking changes silenciosos), honestidad (docs que NO mienten sobre la API real). **DX es ventaja competitiva defendible:** cuando dos APIs hacen lo mismo, gana la que el dev integra primero sin frustrarse.

## 2. El dev tool marketing site (code-first)

El homepage responde **"¿qué hace y para quién?"** sin scroll, sin párrafo, sin video (Vercel: "Develop. Preview. Ship."). Patrones best-in-class 2026:
- **Code-first hero:** un snippet *funcional* above the fold (Resend muestra el código de enviar un email; Stripe el `curl` de crear un charge). El dev ve el shape de la API antes de leer marketing.
- **"Show, don't tell":** la interfaz/terminal/output ES el hero, no una ilustración decorativa.
- **Dark mode por defecto** (Linear/Vercel/PlanetScale: contraste para screenshots, señal de "construido para trabajo enfocado").
- **Social proof developer-grade:** devs confían en devs → **GitHub stars** visibles, logos de empresas técnicas, testimonios de ingenieros con su handle (NO testimonios de CEOs no técnicos).
- **Quickstart de 30 segundos** (bloque copy-paste: `npx create-x`, `npm i sdk`).
- **CTAs concretos:** primario **"Get API keys"**, secundario **"Read the docs"** — el link a docs **prominente** en el nav (es la página más visitada).
- **Pricing usage-based transparente** (por request/seat, free tier explícito; devs huyen del "Contact sales" prematuro).

## 3. API documentation (el corazón)

**Estructura canónica (Stripe-tier):** (1) **Getting Started/Quickstart** (de cero a primer call exitoso), (2) **Guides/Tutorials** (por caso de uso), (3) **API Reference** (cada endpoint, param, response, status code).
**El three-column layout** (estándar 2026 — Stripe/Redoc/Mintlify): izquierda = navegación + search; centro = prosa/descripción/parámetros; **derecha (sticky)** = el bloque de código (request + response en el lenguaje seleccionado).
**El quickstart** es donde se gana o pierde: **si tiene >10 pasos, el onboarding necesita simplificarse** — lleva a un single working call que construya confianza ANTES de features avanzadas.
**Code samples:** tabs multi-lenguaje (cURL + Python + Node + Go), **copy button** siempre, ejemplos **reales y ejecutables** (no pseudocódigo), line highlighting.
**API reference:** cada endpoint con propósito, params (tipos + required/optional), request schema, response, y **todos los status codes con sus error subcodes**. Auto-generado vs hand-written: el estándar 2026 es **híbrido** — reference auto-generada desde **OpenAPI spec** (single source of truth, no drift) + guides escritas a mano en Markdown (Fern/Speakeasy/Redocly/Mintlify renderizan OpenAPI a docs Stripe-like).
**Interactividad:** **"Try it" console / API playground** embebido (el dev hace un request real con su key y ve el response live). **Search crítico** (idealmente AI semantic). **Versioning** + changelog visibles.

## 4. Code, ejemplos & interactividad

- **Syntax highlighting:** **Shiki** es el estándar 2026 (mismo engine que VS Code). Dark theme que los devs esperan.
- **Copy-paste que "just works":** el ejemplo corre tal cual al pegarlo (sin placeholders sin explicar, sin imports faltantes).
- **cURL primero, luego SDKs:** cURL es el lingua franca universal; los SDKs idiomáticos (`stripe.charges.create()`) reducen el código que el dev escribe. Ofrece ambos en tabs.
- **Runnable sandboxes:** embeds tipo StackBlitz/CodeSandbox o el playground propio con test keys.
- **SDK/snippet generation:** genera el snippet del lenguaje seleccionado desde el OpenAPI spec en el "Try it".

## 5. Onboarding, auth & time-to-value

El flujo crítico: **`signup → API key → first call`** — minimízalo brutalmente. El "aha moment" = **el primer call exitoso.**
- **API key management dashboard:** claro, con rotación, scopes, revocación.
- **Auth docs = el primer paso más difícil:** documéntalo con el mayor cuidado (credenciales, token refresh, scopes — la mayoría del friction de onboarding vive aquí).
- **Test mode / sandbox:** patrón Stripe — **test keys vs live keys con prefijos visualmente distintos** (`sk_test_` vs `sk_live_`) para prevenir cargos accidentales en prod. Sandbox que permite calls reales con outcomes simulados.
- **Error messages dev-friendly y accionables** (ata a 35): cada error responde **¿qué salió mal? ¿por qué? ¿cómo lo arreglo?** — HTTP status estándar + subcode específico (`invalid_api_key`, `card_declined`) + **link directo al doc relevante**. El error es un debugging guide, no un callejón.
- **Webhooks / integraciones difíciles:** documenta verify de firmas, retries, idempotencia, ofrece un tester de webhooks (donde más devs se atascan — merece guía dedicada con payloads de ejemplo).

## 6. Tools, AI & 2026

**Plataformas de docs:** **Mintlify** (líder DX-first, genera llms.txt y MCP automáticamente), **Docusaurus** (open-source, React), **ReadMe**, **Nextra**, **Fern**, **Redocly/Redoc**, **Speakeasy** (SDKs + docs desde OpenAPI), o self-built. **Docs-as-code:** Markdown/MDX versionado en git, review por PR, deploy por CI (la doc vive junto al código → menos drift).
**AI en docs (el shift 2026):** **"Ask AI" en docs** (asistente conversacional que responde sobre tu API usando tus docs) · **`llms.txt`** (markdown plano que lista links + summaries para consumo por LLMs; Mintlify lo desplegó across todos sus sites — Anthropic/Cursor lo soportan; `llms-full.txt` da el contenido completo) · **docs-MCP** (conecta tu `llms-full.txt` a un MCP server → le das al AI assistant del dev una knowledge base curada **sin embeddings, sin vector DB, sin RAG** — solo una URL) · **el trend agent-readable** (Gartner: >30% del aumento de demanda de APIs en 2026 viene de AI/LLM tools — las APIs ahora son llamadas por agentes que necesitan docs estructuradas/machine-readable).
> **Relevancia directa para tus productos:** para **FACTUM** (invoicing API) y **GASTROWHATS**, expón un OpenAPI spec → renderiza con Mintlify/Fern (three-column, dark, "Try it"), genera `llms.txt` + MCP server, usa test keys con prefijo, mide TTFC. Si un agente AI va a consumir tu API de facturación, las agent-readable docs son requisito, no lujo.

## DX / docs anti-patterns — blacklist
**no code en el hero** (marketing fluff donde debería ir un snippet) · **fluff para devs** ("powerful/seamless/revolutionary" sin sustancia técnica) · **sin quickstart** o quickstart de >10 pasos · **sin copy button** en bloques de código · **sin search** (o search que no encuentra nada) · **ejemplos rotos / no ejecutables** (el peor pecado: pegas y no corre) · **sin API reference** real (solo guides narrativas) · **sin test mode / sandbox** (obligar a usar prod para probar) · **auth demasiado difícil** (el friction killer #1) · **walls antes de probar** (login/credit card obligatorio para ver el primer call) · **errores genéricos** (`400 Bad Request` sin subcode, sin causa, sin link al doc) · **docs que mienten / drift del API real** (pérdida de confianza irreversible) · **docs outdated** sin changelog ni versioning · **light-mode-only** sin dark mode · **"Contact sales" prematuro** en vez de usage-based transparente · **testimonios no técnicos** en vez de devs reales con handle/GitHub stars.
