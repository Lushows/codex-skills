# 00 — Fundamentos de optimización de tokens

Carga SIEMPRE este módulo al inicio de cualquier sesión de optimización. Define el vocabulario, las métricas, y la economía base que todo lo demás asume.

## Anatomía del costo LLM

Una llamada LLM cobra por 3 tipos de tokens:

| Tipo | Qué es | Costo relativo |
|---|---|---|
| **Input tokens** | Lo que tú mandas (prompt + contexto + tools) | 1x (base) |
| **Output tokens** | Lo que el modelo genera | 5x el input típicamente |
| **Cached read tokens** | Input servido desde cache de Anthropic | 0.1x (90% descuento) |
| **Cached write tokens** | Input escrito al cache (5-min TTL) | 1.25x (premium) |
| **Cached write 1h** | Input escrito al cache (1-hora TTL) | 2x (premium mayor) |

## Pricing actual (caché 2026-05-26)

### Anthropic Claude

| Modelo | Model ID | Input $/1M | Output $/1M |
|---|---|---|---|
| Claude Opus 4.8 | `claude-opus-4-8` | $5.00 | $25.00 |
| Claude Opus 4.7 | `claude-opus-4-7` | $5.00 | $25.00 |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | $3.00 | $15.00 |
| Claude Haiku 4.5 | `claude-haiku-4-5` | $1.00 | $5.00 |

**Con caching activo:**
- Sonnet 4.6 cache hit: $0.30/MTok (vs $3.00 base = 90% descuento)
- Opus 4.8 cache hit: $0.50/MTok (vs $5.00 base = 90% descuento)
- Haiku 4.5 cache hit: $0.10/MTok (vs $1.00 base = 90% descuento)

**Con Batch API (combinable con cache):**
- 50% descuento adicional
- Stack máximo: cache + batch = ~95% ahorro vs llamada estándar

### OpenAI (referencia 2026, verificar con WebFetch si crítico)

| Modelo | Input $/1M | Output $/1M |
|---|---|---|
| GPT-5 | $5.00 | $20.00 |
| GPT-5-mini | $1.50 | $6.00 |
| GPT-5-nano | $0.10 | $0.40 |

### Google Gemini (referencia 2026)

| Modelo | Input $/1M | Output $/1M |
|---|---|---|
| Gemini 2.5 Pro | $3.50 | $14.00 |
| Gemini 2.5 Flash | $0.30 | $2.50 |

> ⚠️ Pricing cambia. Si el costo es decisión crítica, verificar con WebFetch a las páginas oficiales.

## Métricas clave que TODO sistema LLM debe medir

Sin estas métricas, optimizar es jugar a la ruleta:

| Métrica | Cómo calcularla | Para qué sirve |
|---|---|---|
| **Tokens/request promedio** | `total_tokens / total_requests` | Detectar requests anormalmente caros |
| **Cache hit rate** | `cache_read_tokens / (cache_read + cache_write + input_tokens)` | Validar que caching realmente funciona |
| **Costo por usuario/mes** | `sum(cost) WHERE user_id = X` | Decidir pricing, identificar power users |
| **Costo por feature** | `sum(cost) GROUP BY feature_name` | Detectar features sobre-consumiendo |
| **Latencia p50, p95, p99** | Percentiles de duración de request | UX + SLA |
| **Output token ratio** | `output_tokens / input_tokens` | Detectar generaciones excesivas |

### Cómo leer `response.usage` (Anthropic SDK)

```python
response = client.messages.create(...)

print(response.usage.input_tokens)               # Input no cacheado
print(response.usage.output_tokens)              # Lo que generó
print(response.usage.cache_creation_input_tokens) # Tokens escritos al cache (1.25x)
print(response.usage.cache_read_input_tokens)    # Tokens servidos del cache (0.1x)

# CÁLCULO REAL del costo total:
total_input_tokens = (
    response.usage.input_tokens +
    response.usage.cache_creation_input_tokens +
    response.usage.cache_read_input_tokens
)
```

⚠️ Trampa común: `usage.input_tokens` es SOLO los tokens no-cacheados. El total de input es la suma de los 3. Muchos sistemas reportan mal "tokens usados" por ignorar esto.

## La regla del Pareto en optimización LLM

**3 técnicas dan el 60-70% del ahorro total:**

```
┌─────────────────────────────────────────────┐
│  TIER 1 - Aplicar SIEMPRE (60-70% ahorro)  │
├─────────────────────────────────────────────┤
│  1. Prompt Caching         (módulo 01)     │
│  3. Model Routing          (módulo 03)     │
│  4. Context Engineering    (módulo 04)     │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  TIER 2 - Aplicar según caso (+15-20%)     │
├─────────────────────────────────────────────┤
│  2. Batch API              (módulo 02)     │
│  5. Semantic Caching       (módulo 05)     │
│  7. RAG Eficiente          (módulo 07)     │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  TIER 3 - Pulir (+5-10%)                   │
├─────────────────────────────────────────────┤
│  6. Prompt Compression     (módulo 06)     │
│  8. Tool Use Optimization  (módulo 08)     │
│  9. Streaming + Early Term (módulo 09)     │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  TIER 0 - Defensa (cero ahorro, evita      │
│           desastre financiero)              │
├─────────────────────────────────────────────┤
│ 10. Monitoring + Budget    (módulo 10)     │
└─────────────────────────────────────────────┘
```

## Vocabulario que el usuario debe entender

Define estos términos la primera vez que aparezcan en una sesión:

- **Token:** unidad mínima de texto que procesa el LLM (~0.75 palabras en español). Ejemplo: "hola mundo" = 3 tokens.
- **Context window:** capacidad máxima de input que acepta el modelo. Opus 4.8 = 1M tokens, Sonnet 4.6 = 1M, Haiku 4.5 = 200K.
- **Prompt prefix:** todo lo que va ANTES del último mensaje del usuario (system + tools + historial). Es lo que se cachea.
- **Cache breakpoint:** marca explícita (`cache_control: ephemeral`) que le dice a Anthropic "cachea hasta aquí".
- **Cache hit:** request donde el prefix ya estaba en cache. Cuesta 10% del normal.
- **Cache miss:** primer request o request donde algo invalidó el prefix. Cuesta 125% del normal (premium de escritura).
- **TTL (Time To Live):** tiempo que vive el cache. Anthropic: 5 min (default) o 1 hora.
- **Effort parameter:** nuevo en Anthropic, controla cuánto piensa el modelo. Opciones: low, medium, high, xhigh, max.

## Diagnóstico inicial (preguntar SIEMPRE)

Antes de proponer cualquier optimización:

1. **¿Qué proveedor(es) LLM usas hoy?** (Anthropic / OpenAI / Gemini / mixto)
2. **¿Cuál es el volumen actual?**
   - Requests/día
   - Tokens/día promedio
   - $USD/mes facturados
3. **¿Tipo de tráfico?**
   - Realtime (chat con usuario esperando) → no batch
   - Async (jobs nocturnos, enrichment) → batch ideal
   - Hybrid → routing inteligente
4. **¿Stack actual?**
   - SDK directo del proveedor
   - Vercel AI SDK
   - LangChain / LlamaIndex
   - Algún Gateway (Portkey, Helicone, etc.)
5. **¿Constraints duros?**
   - Latencia máxima (ms p95)
   - Privacy/compliance (no third parties, regiones)
   - Budget mensual hard cap
6. **¿Mides algo hoy?**
   - Tienes dashboard de costos? (Anthropic console, OpenAI usage, custom)
   - Mides cache hit rate?
   - Atribuyes costos por feature/usuario?

Con estas 6 respuestas, ya sabes qué módulos priorizar.

## Regla de oro

> **"Mide antes de optimizar. Optimiza solo lo que duele. Mide después."**

Sin esto, vas a "optimizar" cosas que no eran problema y crear problemas nuevos.

Relacionado: [[10-monitoring-budget]], [[01-prompt-caching]], [[03-model-routing]]
