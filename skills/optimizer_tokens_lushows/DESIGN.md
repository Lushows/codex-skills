# DESIGN.md — Filosofía de optimizer_tokens_lushows

## Por qué esta skill existe

Los costos de LLM dominan el presupuesto de cualquier producto AI en producción. Un equipo sin optimización gasta **3 a 10 veces más** que un equipo optimizado en EL MISMO output. La diferencia se acumula:

| Escenario | Sin optimizar | Optimizado | Ahorro/año |
|---|---|---|---|
| Bot WhatsApp 10K usuarios | $1,200/mes | $200/mes | $12,000 |
| SaaS multi-tenant 500 clientes | $4,500/mes | $675/mes | $45,900 |
| Agente trading análisis diario | $800/mes | $120/mes | $8,160 |

Esto NO es "premature optimization". Esto es **economía básica del producto AI**.

## Principios de diseño de la skill

### 1. Pareto manda
Los 10 bloques NO son iguales en impacto. Hay 3 que dan el 60–70% del ahorro:
- **#1 Prompt Caching** (90% descuento)
- **#3 Model Routing** (60–80% ahorro)
- **#4 Context Engineering** (30–50% reducción)

Si solo aplicas estos 3, ya ganaste el partido. Los otros 7 son para llegar de 70% a 95%.

### 2. Mide antes, optimiza después
Toda optimización sin métricas es FE, no ingeniería. La skill insiste en:
- Token counting per request
- Cache hit rate por feature
- Costo por usuario / por endpoint
- Antes/después de cada cambio

Sin esto, "optimizar" es jugar a la ruleta.

### 3. Calidad es no-negociable
Una "optimización" que degrada output NO es optimización. Es destrucción de producto disfrazada de ahorro.

Toda técnica documentada incluye:
- Cuándo aplica (problema que resuelve)
- Cuándo NO aplica (degrada calidad)
- Cómo medir que no degradó (eval, A/B, observación)

### 4. Código real, no teoría
Cada bloque tiene snippet **listo para copiar** en el SDK del usuario:
- Anthropic SDK (TypeScript + Python)
- OpenAI SDK (TypeScript + Python)
- Vercel AI SDK
- Gemini SDK

No hay "podrías usar X" sin código. Hay "esto va aquí, así".

### 5. Reactivo a cambios del mercado
2026 trajo:
- Anthropic prompt caching automático
- Batch API combinable con cache (stack 95%)
- Context engineering > prompt engineering
- Semantic caching como producto enterprise
- AI Gateways como capa estándar

La skill se mantiene viva: cada cambio de pricing, cada feature nueva de los proveedores, cada herramienta nueva — se documenta.

## Tono al hablar con el usuario

- **Directo:** "Esto está mal, así se arregla, aquí el código."
- **Cuantitativo:** "Estás pagando $4,500/mes, con caching baja a $675. 85% ahorro."
- **Sin jerga innecesaria:** Si Lushows no entiende "KV cache", lo explico antes de usarlo.
- **Sin sugarcoating:** Si la arquitectura está mal pensada y caching no ayuda, lo digo. Mejor refactor honesto que parche caro.
- **Atribuye fugas:** "El 70% del costo viene del endpoint /process-invoice. Empezamos ahí."

## Lo que NO hace esta skill

- ❌ No es una skill de **prompt engineering creativo** (mejorar calidad de respuestas). Otras skills cubren eso.
- ❌ No es una skill de **fine-tuning** (entrenar modelos custom). Eso es otra disciplina.
- ❌ No es **arquitectura de producto AI** completa. Es la capa de eficiencia económica de esa arquitectura.
- ❌ No reemplaza la **decisión de qué modelo usar** desde el negocio. Asume que ya elegiste Anthropic/OpenAI/Gemini.

## Lo que SÍ hace

- ✅ Auditoría de costos LLM actuales
- ✅ Refactor de código existente para aplicar caching/batching/routing
- ✅ Diseño de pipeline de contexto eficiente
- ✅ Setup de monitoring + budget guardrails
- ✅ Comparación honesta entre proveedores en términos económicos
- ✅ Cálculo de impacto esperado antes de implementar

## Métricas de éxito de la skill

Cuando esta skill funciona bien, el usuario:
1. Sabe exactamente cuánto gasta su sistema LLM, por feature
2. Aplicó al menos los 3 bloques Pareto (caching + routing + context)
3. Mide hit rate, no asume
4. Tiene budget alerts + kill switches funcionando
5. Ahorra 60%+ vs su línea base
