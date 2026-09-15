# 105 — Marketing con IA / el stack de growth con IA (2026)

A inicios de 2026, **75%+ de marketers usan IA generativa regularmente** → la calidad de generación es table stakes.
**El diferenciador es integración de workflow + consistencia de brand-voice, NO la generación cruda.**

## El stack de 6 capas
data/analytics · content generation · SEO/GEO · paid-media automation · CRM/personalización · **orquestación/workflow
automation**. Los equipos que integran las 6 reportan ciclos más rápidos y menor CPA que los de tools desconectados.

## Orquestación — n8n + LLM workflows (el "automation fabric")
n8n es el default 2026 (branching, webhooks, merging, waiting, error handling, conecta cualquier API). Patrón de
gobernanza probado: **AI propone → reglas validan → workflow ejecuta → humanos aprueban lo riesgoso.** No construyas
un "marketer autónomo sci-fi"; construye AI *steps dentro* de workflows observables/gobernados. Setup de referencia: n8n self-hosted + Claude API + MCP servers — reusable across tus 3 negocios.

## Aplicaciones
- **Ad creative a escala:** cada **hero asset → 10-20 piezas downstream** auto-generadas + LLM drafteando copy por plataforma. Resuelve la creative-fatigue (winners mueren en 7-10 días) industrializando variantes.
- **Content+SEO/GEO:** la IA acelera pero **el content AI a escala tiene riesgo real** (alucina, sesga, se devalúa). Mantén **checkpoints editoriales humanos**. Para GEO la autoridad debe ser REAL — BIO-SETA cita estudios reales, no inventados (riesgo regulatorio/confianza en claims de salud).
- **Personalización:** LLMs construyen un mensaje genuinamente distinto (ángulo/tono/énfasis) por micro-segmento — aquí la IA da lift real, *si* se gobierna por brand voice.
- **AI SDR/outbound** (con límites de envío + revisión humana). **AI customer support — tu edge:** Addrian (el bot WhatsApp) *es* AI support, la app AI de mayor ROI más probada. Extiéndela: auto-draft de respuestas para aprobación del operador, resumir conversaciones, detectar intención. **AI analytics:** LLMs queryan/resumen tu `data/store.json` → narrativas "qué cambió y por qué".

## Qué funciona vs hype
**Funciona:** AI dentro de n8n gobernado; AI customer support; creative-variant scaling; personalización por segmento; analytics summaries; content GEO (humano-verificado). **Hype/riesgo:** marketers "set-and-forget" autónomos; content AI sin editar a escala; outreach sin límites; confiar claims AI en salud regulada.

## Gotchas
1. Sesgo — sistemas de ad AI han mostrado delivery discriminatorio (job ads por género); audita targeting.
2. Sin checkpoint humano en claims de salud = exposición regulatoria para BIO-SETA.
3. Brand-voice drift en content masivo-generado — define y enforce un voice spec.
4. Over-automatizar antes de entender el proceso manual — automatiza uno *que funciona*, no uno roto.
5. Cadenas de agentes inobservables que no puedes debuggear — mantén workflows legibles/logged.
6. Tratar la calidad de generación como el moat (está commoditizada) en vez de integración + data + brand voice.

**Fuentes:** growthhakka.co.uk (AI marketing stack 2026) · marketingagent.blog (n8n marketing 2026) · press.farm (50 AI marketing tools 2026).
