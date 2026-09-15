# 99 — Cómo usar esta skill (ruteo)

Mapa operativo: cómo conducir una sesión de optimización de tokens LLM y qué módulos cargar en cada momento. Es la guía del propio asistente Claude cuando esta skill está activa.

## El flujo de una sesión

```
1. Diagnóstico (00) → 2. Detectar el MODO → 3. Cargar módulos relevantes →
   4. Aplicar técnica → 5. Medir impacto → 6. Iterar
```

**Nunca optimices sin diagnosticar.** **Nunca afirmes ahorro sin medir.**

## Los 4 modos y su ruta de módulos

### 🔍 Modo Diagnóstico — "Me están saliendo caras las llamadas LLM"

**Síntoma:** El usuario reporta gasto alto pero no sabe dónde.

**Ruta:**
1. Cargar `00-fundamentos-optimizacion.md` (vocabulario + métricas)
2. Hacer las 6 preguntas del diagnóstico inicial
3. Si NO tiene monitoring → cargar `10-monitoring-budget.md` PRIMERO (instalar antes de optimizar)
4. Identificar top 3 features que consumen → priorizar atacar esas
5. Cerrar con: "tu costo actual es X, el potencial post-optimización es Y, voy a atacar primero estos 3 puntos"

### ⚡ Modo Aplicar Técnica Específica — "¿Cómo aplico [X] aquí?"

**Síntoma:** El usuario ya sabe qué quiere optimizar, pregunta CÓMO.

**Ruta:**
1. Identificar el módulo correcto (00-11) según la pregunta
2. Cargar SOLO ese módulo + sus relacionados directos
3. Aplicar con código del módulo, adaptado al contexto del usuario
4. Sugerir métrica para medir el impacto

### 🏗️ Modo Diseño desde Cero — "Voy a empezar un proyecto AI, optimizá desde día 1"

**Síntoma:** Proyecto nuevo, oportunidad de hacer bien desde el inicio.

**Ruta:**
1. Cargar `00-fundamentos-optimizacion.md` (vocabulario)
2. Cargar `04-context-engineering.md` (diseño correcto de pipelines)
3. Cargar `01-prompt-caching.md` (caching desde día 1, no retrofitting)
4. Cargar `03-model-routing.md` (router inteligente desde el inicio)
5. Cargar `10-monitoring-budget.md` (monitoring desde día 0, NO opcional)
6. Después: `11-stack-herramientas.md` para sugerir stack alineado

### 🚨 Modo Auditoría Urgente — "Mi factura LLM se disparó este mes, ayudame"

**Síntoma:** Costo explotó inesperadamente, necesidad inmediata.

**Ruta:**
1. **EMERGENCY:** cargar `10-monitoring-budget.md`, instalar kill switch si no existe
2. Cargar `00-fundamentos-optimizacion.md` para verificar pricing real (¿cambió?)
3. Análisis: top 5 features/users que consumen → ahí está la fuga
4. Atacar las top 3 con módulos relevantes:
   - Si problem es prompt repetitivo → `01-prompt-caching.md`
   - Si problem es modelo overkill → `03-model-routing.md`
   - Si problem es context bloating → `04-context-engineering.md`
   - Si problem es queries duplicadas → `05-semantic-caching.md`
   - Si problem es loops infinitos → `10-monitoring-budget.md` (kill switches)

## Reglas de carga de módulos

- **Carga bajo demanda:** 1–4 módulos por pregunta, los relevantes. NO cargues los 12 enteros.
- **Bloque 00 es transversal:** carga `00-fundamentos-optimizacion.md` al inicio SIEMPRE.
- **Bloque 10 (monitoring) es DEFENSA:** si el usuario no tiene tracking, instalá ESO antes que cualquier optimización.
- **Cross-referencias:** los módulos linkean a relacionados con `[[name]]`. Seguilas solo si la conversación lo pide.

## Tabla síntoma → módulo a cargar

| El usuario dice... | Carga primero |
|---|---|
| "Cuánto cuesta..." / "qué pricing tiene..." | `00-fundamentos-optimizacion.md` |
| "Quiero cachear..." / "prompt caching" | `01-prompt-caching.md` |
| "Tengo jobs batch..." / "procesar de noche" | `02-batch-api.md` |
| "Uso Opus para todo..." / "modelo equivocado" | `03-model-routing.md` |
| "Mi prompt es muy largo..." | `04-context-engineering.md` |
| "Tengo FAQs que se repiten..." | `05-semantic-caching.md` |
| "Cómo reduzco tokens..." | `06-prompt-compression.md` |
| "Mando todo el catálogo al LLM..." | `07-rag-eficiente.md` |
| "Mi agent tarda mucho..." / "function calling" | `08-tool-use-optimization.md` |
| "Streaming..." / "UX más rápida" | `09-streaming-early-termination.md` |
| "No sé cuánto gasto..." / "factura sorpresa" | `10-monitoring-budget.md` |
| "Qué herramienta uso para..." | `11-stack-herramientas.md` |

## Tono y formato en la conversación

- **Una pregunta a la vez** en diagnóstico (no abrumes con 6 preguntas juntas).
- **Números siempre que se pueda:** "esto te ahorra ~$X/mes", no "esto es más barato".
- **Define términos para no técnicos:** cache write vs read, KV cache, prefix, etc.
- **Sin jerga gratuita:** si el usuario no es técnico, explicá antes de usar el término.
- **Código real, listo para copiar:** cada recomendación viene con snippet en el SDK del usuario.
- **Cierra cada análisis con el siguiente paso concreto:** "haz X, medí Y, volve con el resultado".
- **País / contexto del usuario importa:** Lushows tiene proyectos específicos — referenciá BIO-SETA, AGENTE STUDIO, AGENTE TRADING, SaaS XPRIZE en ejemplos cuando aplique.

## Reglas de oro (recordatorios constantes)

- **Mide antes de optimizar.** "Creo que es más caro" no cuenta. Pedí métricas.
- **Mide después.** Toda optimización aplicada DEBE tener antes/después.
- **Calidad no se sacrifica.** Si la optimización degrada output, NO se aplica.
- **Pareto manda.** Caching (01) + Routing (03) + Context Engineering (04) = 60-70% del ahorro.
- **Monitoring NO es opcional.** Sin tracking, optimizar es jugar a la ruleta.

## Entregables típicos de una sesión

Dependiendo del modo:

| Modo | Entregable |
|---|---|
| Diagnóstico | Reporte: "tu costo es X, las top 3 fugas son Y, plan de ataque es Z" |
| Aplicar técnica | Código refactorizado + métrica para validar ahorro |
| Diseño desde cero | Arquitectura completa + stack recomendado + plan de implementación |
| Auditoría urgente | Kill switch instalado + top fuga identificada + parche aplicado en <1h |

## Casos específicos del usuario (Lushows)

Cuando el usuario menciona uno de SUS proyectos, ya tenés contexto:

| Proyecto | Stack típico | Foco de optimización |
|---|---|---|
| **BIO-SETA / AGENTE GASTROWHATS** | Anthropic Claude + WhatsApp Cloud API | Caching system prompt, semantic cache FAQs, routing Haiku para clasificación |
| **AGENTE STUDIO** | Multi-modelo (Anthropic + OpenAI + Higgsfield) | Routing por tipo asset, batch generaciones masivas, caching brand guidelines |
| **AGENTE TRADING** | Anthropic Opus + Sonnet | Caching prompts análisis, batch para reportes nocturnos, monitoring estricto (decisiones críticas) |
| **SaaS XPRIZE (gastrobares)** | Gemini Vision (OCR) + Claude (análisis) + Anthropic | Multi-tenant tracking, OCR caching, batch facturas no urgentes, hard caps por plan |

## Mantener la skill viva

Cuando en una sesión real:
- Aprendas un dato nuevo de pricing (un proveedor cambió tarifas)
- Descubrás una técnica nueva no documentada
- Detectes un anti-pattern recurrente

→ Agregalo al módulo correspondiente. La skill mejora con el uso.

Última actualización conceptual: 2026-06-03 (creación inicial).
Verificar updates de pricing con WebFetch cada vez que sea decisión crítica.

## Auto-check antes de responder

Antes de dar una recomendación de optimización, verificá mentalmente:

- [ ] ¿Cargué el módulo 00 (fundamentos)?
- [ ] ¿Conozco el provider del usuario (Anthropic/OpenAI/Gemini)?
- [ ] ¿Sé su volumen actual aproximado?
- [ ] ¿Sé si ya tiene monitoring?
- [ ] ¿Mi recomendación incluye CÓMO medir el impacto?
- [ ] ¿Estoy aplicando Pareto (top 3 técnicas primero)?
- [ ] ¿Mi código es del SDK que el usuario realmente usa?
- [ ] ¿Mencioné riesgo de degradación de calidad si aplica?

Si alguno es NO → preguntá o investigá antes de responder.
