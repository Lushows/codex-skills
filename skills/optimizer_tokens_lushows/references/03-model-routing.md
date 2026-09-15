# 03 — Model Routing Inteligente (60-80% ahorro)

**Impacto:** 60-80% reducción enviando cada tarea al modelo MÁS PEQUEÑO que la resuelva bien.
**Esfuerzo:** Medio (requiere clasificar tareas + router logic).
**Cuándo aplicar:** Cualquier sistema que use solo el modelo top tier "por defecto".

## La trampa del "siempre Opus" / "siempre GPT-4"

Error #1 de developers nuevos: usar el modelo más caro para TODO. Patrón típico:

```python
# ❌ Mal: Opus para todo
def classify_sentiment(text):
    return client.messages.create(
        model="claude-opus-4-8",  # $5/$25 — overkill para clasificación binaria
        max_tokens=10,
        messages=[{"role": "user", "content": f"Sentiment de: {text}\nResponde: positivo/negativo/neutral"}]
    )

# ✅ Bien: Haiku para clasificación
def classify_sentiment(text):
    return client.messages.create(
        model="claude-haiku-4-5",  # $1/$5 — 5x más barato, suficiente para este task
        max_tokens=10,
        messages=[{"role": "user", "content": f"Sentiment de: {text}\nResponde: positivo/negativo/neutral"}]
    )
```

**Diferencia:** 80% ahorro inmediato sin perder calidad. Haiku 4.5 clasifica sentiment tan bien como Opus 4.8 (probado en evals).

## Mapeo: tarea → modelo correcto

### Anthropic tier system

```
┌─────────────────────────────────────────────────┐
│  HAIKU 4.5 ($1/$5)                             │
│  Para 60-70% de las tareas                     │
├─────────────────────────────────────────────────┤
│  • Clasificación (sentiment, categoría, intent) │
│  • Extracción de datos simple                  │
│  • Respuestas FAQ con context provisto         │
│  • OCR de texto limpio                         │
│  • Validación / yes-no                         │
│  • Routing inicial de queries                  │
│  • Resúmenes cortos (<200 words)               │
│  • Reformulación, parafraseo                   │
│  • Traducciones simples                        │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│  SONNET 4.6 ($3/$15)                           │
│  Para 25-30% de las tareas                     │
├─────────────────────────────────────────────────┤
│  • OCR complejo (handwritten, layouts raros)   │
│  • Conversación natural con contexto           │
│  • Análisis de documentos medianos             │
│  • Generación de código standard               │
│  • Reportes con razonamiento moderado          │
│  • Tool use / function calling                 │
│  • Multi-turn con memoria                      │
│  • Análisis financiero estándar                │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│  OPUS 4.8 ($5/$25)                             │
│  Para 5-10% de las tareas (las heavy)          │
├─────────────────────────────────────────────────┤
│  • Coding agente autónomo (Cursor-like)        │
│  • Razonamiento multi-paso complejo            │
│  • Análisis estratégico profundo               │
│  • Debugging complejo                          │
│  • Investigación con tool use intensivo        │
│  • Generación de planes detallados             │
│  • Tareas críticas donde no podés fallar       │
└─────────────────────────────────────────────────┘
```

## Implementación: router por tipo de tarea

```python
from enum import Enum

class TaskType(str, Enum):
    CLASSIFY = "classify"
    EXTRACT_SIMPLE = "extract_simple"
    EXTRACT_COMPLEX = "extract_complex"
    SUMMARIZE = "summarize"
    ANALYZE = "analyze"
    GENERATE_CODE = "generate_code"
    AGENT_AUTONOMOUS = "agent_autonomous"

MODEL_BY_TASK = {
    TaskType.CLASSIFY: "claude-haiku-4-5",
    TaskType.EXTRACT_SIMPLE: "claude-haiku-4-5",
    TaskType.SUMMARIZE: "claude-haiku-4-5",
    TaskType.EXTRACT_COMPLEX: "claude-sonnet-4-6",
    TaskType.ANALYZE: "claude-sonnet-4-6",
    TaskType.GENERATE_CODE: "claude-sonnet-4-6",
    TaskType.AGENT_AUTONOMOUS: "claude-opus-4-8",
}

def call_llm(task_type: TaskType, **kwargs):
    model = MODEL_BY_TASK[task_type]
    return client.messages.create(model=model, **kwargs)
```

## Routing por confianza / 2-tier fallback

Para tareas borderline, usar Haiku primero y promover a Sonnet si la confianza es baja:

```python
def smart_classify(text: str):
    # Tier 1: Haiku
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=50,
        messages=[{"role": "user", "content": f"""
Clasifica el siguiente texto en: {CATEGORIES}.
Responde JSON: {{"category": "...", "confidence": 0.0-1.0}}

Texto: {text}
        """}]
    )

    result = json.loads(response.content[0].text)

    # Si Haiku no está seguro → promover a Sonnet
    if result["confidence"] < 0.75:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=50,
            messages=[...]  # mismo prompt
        )
        result = json.loads(response.content[0].text)

    return result
```

**Resultado:** 80-90% de queries resueltas con Haiku ($1), el 10-20% restante con Sonnet ($3). Costo promedio: ~$1.30/M vs $3.00/M si todo fuera Sonnet (57% ahorro).

## Cross-provider routing (Anthropic + OpenAI + Gemini)

Para casos donde diferentes proveedores brillan en diferentes tareas:

```python
ROUTING_CROSS_PROVIDER = {
    "vision_ocr": "claude-haiku-4-5",        # Anthropic mejor en OCR visual
    "long_context": "gemini-2.5-pro",        # 2M context window
    "function_calling": "gpt-5",              # OpenAI muy bueno en tools
    "code_generation": "claude-sonnet-4-6",   # Anthropic líder en code
    "creative_writing": "claude-opus-4-8",    # Anthropic mejor prose
    "speed_critical": "gemini-2.5-flash",     # Más rápido + barato
}
```

## Routing con AI Gateways (Portkey, OpenRouter, LiteLLM)

Para abstraer el routing y poder cambiar proveedores sin tocar código:

### Vercel AI Gateway
```python
# Vercel AI SDK routea automáticamente
import { generateText } from 'ai';
import { vercel } from '@ai-sdk/vercel';

const { text } = await generateText({
  model: vercel('anthropic/claude-haiku-4-5'),  // Fácil cambiar a 'openai/gpt-5'
  prompt: 'Clasifica este texto'
});
```

### Portkey
```python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="PORTKEY_API_KEY",
    config={
        "strategy": {"mode": "fallback"},
        "targets": [
            {"provider": "anthropic", "model": "claude-haiku-4-5"},
            {"provider": "openai", "model": "gpt-5-mini"},  # Fallback si Anthropic cae
        ]
    }
)
response = portkey.chat.completions.create(messages=[...])
```

### OpenRouter
Una API unificada, 100+ modelos, routing automático por precio/calidad.

```python
import openai

client = openai.OpenAI(
    api_key="OPENROUTER_KEY",
    base_url="https://openrouter.ai/api/v1"
)

response = client.chat.completions.create(
    model="anthropic/claude-haiku-4-5",  # O "auto" para que OpenRouter elija
    messages=[...]
)
```

## Patrón: clasificador + ejecutor

Una arquitectura común y eficiente:

```python
def process_query(user_query: str):
    # Paso 1: Clasificar tipo de query con Haiku (barato)
    classification = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=50,
        messages=[{"role": "user", "content": f"""
Clasifica esta query en uno de:
- simple_faq (pregunta básica)
- data_extraction (pedir extraer datos)
- complex_analysis (requiere razonamiento profundo)
- coding (generar código)

Query: {user_query}

Responde solo la categoría, una palabra.
        """}]
    )

    category = classification.content[0].text.strip()

    # Paso 2: Ejecutar con el modelo correcto
    if category == "simple_faq":
        model = "claude-haiku-4-5"
    elif category == "data_extraction":
        model = "claude-haiku-4-5"  # Haiku 4.5 es excelente en extraction
    elif category == "complex_analysis":
        model = "claude-sonnet-4-6"
    elif category == "coding":
        model = "claude-sonnet-4-6"  # Sonnet mejor en code que Haiku
    else:
        model = "claude-sonnet-4-6"

    response = client.messages.create(
        model=model,
        max_tokens=2048,
        messages=[{"role": "user", "content": user_query}]
    )

    return response.content[0].text
```

**Costo del clasificador:** ~$0.0001/query (Haiku, 50 tokens). Despreciable.
**Ahorro:** 60-80% promedio si la mayoría de queries son simples.

## Evals: cómo decidir si Haiku basta vs necesitas Sonnet

NO confíes en intuición. Mide.

```python
# 1. Tomá 100 queries reales de producción
test_queries = sample_production_queries(n=100)

# 2. Generá respuestas con Haiku y Sonnet
haiku_responses = [call_haiku(q) for q in test_queries]
sonnet_responses = [call_sonnet(q) for q in test_queries]

# 3. Usá un juez (Opus 4.8 o human review) para comparar
def judge_pair(query, haiku_resp, sonnet_resp):
    judgment = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=100,
        messages=[{"role": "user", "content": f"""
Query: {query}

Respuesta A: {haiku_resp}
Respuesta B: {sonnet_resp}

¿Cuál responde mejor la query? Responde: A, B, o EQUAL.
        """}]
    )
    return judgment.content[0].text.strip()

# 4. Si Haiku es EQUAL o A en >80% de casos → migrá a Haiku
results = [judge_pair(q, h, s) for q, h, s in zip(test_queries, haiku_responses, sonnet_responses)]
equal_or_haiku_wins = sum(1 for r in results if r in ["A", "EQUAL"]) / len(results)

if equal_or_haiku_wins > 0.80:
    print(f"✅ Migrar a Haiku: equivalente o mejor en {equal_or_haiku_wins:.0%} de casos")
else:
    print(f"⚠️ Quedarse en Sonnet: Haiku solo equivalente en {equal_or_haiku_wins:.0%}")
```

## Casos del usuario

### BIO-SETA / AGENTE GASTROWHATS
- Respuestas a FAQs frecuentes → **Haiku 4.5** (90% queries)
- Conversación de venta consultiva compleja → **Sonnet 4.6** (10%)
- **Ahorro estimado:** 70% del costo del bot

### AGENTE STUDIO
- Análisis del brief del cliente → **Sonnet 4.6**
- Generación de copy variants → **Sonnet 4.6**
- Resúmenes / categorización assets → **Haiku 4.5**
- **Ahorro estimado:** 50%

### AGENTE TRADING
- Alertas de eventos del mercado → **Haiku 4.5** (clasificación de noticias)
- Análisis técnico profundo → **Opus 4.8** (decisiones críticas)
- Resúmenes diarios → **Sonnet 4.6**
- **Ahorro estimado:** 65%

### SaaS XPRIZE (gastrobares)
- OCR factura (texto claro) → **Haiku 4.5**
- OCR factura con texto manuscrito → **Sonnet 4.6**
- Categorización proveedor → **Haiku 4.5**
- Análisis estratégico mensual del negocio → **Opus 4.8**
- Chat asistido cliente → **Sonnet 4.6**
- **Ahorro estimado:** 75%

## Anti-patterns

❌ **"Vamos a usar Opus para garantizar calidad"** — overkill. Haiku 4.5 es excelente para 60% de tasks.
❌ **"Sonnet para todo"** — pierdes 60-80% de ahorro de Haiku en tasks simples.
❌ **"El user no nota la diferencia"** — sí la nota en tasks complejas. Medí, no asumas.
❌ **No tener fallback cross-provider** — si Anthropic cae, tu app cae. Usa Gateway con fallback.
❌ **Routing hardcoded sin medir** — perfila qué tipos de query llegan y ajusta.

## Checklist al implementar routing

- [ ] Auditar tipos de tasks actuales (clasificarlos en simple/medio/complejo)
- [ ] Asignar tier de modelo a cada task type
- [ ] Implementar router central (no llames `model="..."` ad hoc en código)
- [ ] Si task es ambigua → 2-tier fallback (Haiku → Sonnet si baja confianza)
- [ ] Considerar Gateway (Vercel AI / Portkey / OpenRouter) para fallback cross-provider
- [ ] Eval offline: confirmar Haiku basta en tasks asignadas a Haiku
- [ ] Medir % de queries por tier en producción
- [ ] Revisar mensual: ¿podemos bajar más tasks a tier inferior?

Relacionado: [[00-fundamentos-optimizacion]], [[01-prompt-caching]], [[10-monitoring-budget]], [[11-stack-herramientas]]
