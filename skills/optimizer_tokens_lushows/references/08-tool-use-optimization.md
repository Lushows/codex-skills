# 08 — Tool Use & Structured Output Optimization

**Impacto:** 20-40% reducción de tokens + 2-3x menos latency en flujos agénticos.
**Esfuerzo:** Medio (refactor de tool definitions).
**Cuándo aplicar:** Cualquier sistema con function calling, agentes, o structured outputs.

## El problema con tool use mal hecho

```python
# ❌ Mal: tools descritos como novela
tools = [
    {
        "name": "search_database",
        "description": """
This is a very important tool that allows you to search the database.
Use it when the user asks anything about products, orders, customers,
inventory, or any other data stored in our systems. The tool is very
powerful and supports complex queries. Please use it wisely. It will
return results in JSON format. Make sure to handle errors. ...
(500 tokens más de descripción)
        """,
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query string. This should be a natural language description of what you want to find. Make sure to be specific..."
                }
            }
        }
    },
    # ... 20 tools más, similares
]
# Total: ~10K tokens SOLO en tool definitions, en CADA request
```

```python
# ✅ Bien: tools concisos
tools = [
    {
        "name": "search_db",
        "description": "Search products, orders, customers, inventory.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Natural language search query"},
                "table": {"type": "string", "enum": ["products", "orders", "customers", "inventory"]}
            },
            "required": ["query", "table"]
        }
    },
    # ...
]
# Total: ~2K tokens (80% menos)
```

## Técnicas de optimización

### 1. Descripciones concisas pero específicas

```python
# ❌ Verbose
"description": "This tool allows you to fetch the current weather forecast for any city in the world. It supports multiple units like celsius and fahrenheit."

# ✅ Conciso
"description": "Get current weather for a city. Returns temp, conditions, humidity."

# ✅ Mejor aún (incluye WHEN to use)
"description": "Get current weather. Use when user asks about weather, temperature, or conditions for a specific location."
```

**Regla 2026 (Opus 4.7+):** descripciones prescriptivas que dicen CUÁNDO llamar el tool dan más lift que descripciones de qué HACE el tool.

### 2. Parallel tool calls (cuando aplica)

Anthropic y OpenAI soportan parallel function calling. Si tu task requiere múltiples llamadas independientes, hacelas en paralelo:

```python
# ❌ Mal: serial (3 round-trips al LLM)
def process_invoice_serial(invoice):
    # Round 1
    extracted = call_llm_to_extract(invoice)

    # Round 2
    category = call_llm_to_categorize(extracted)

    # Round 3
    supplier = call_llm_to_match_supplier(extracted)

    return {...}

# ✅ Bien: parallel tool use (1 round-trip)
def process_invoice_parallel(invoice):
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        tools=[
            {"name": "extract_data", "description": "...", "input_schema": {...}},
            {"name": "categorize", "description": "...", "input_schema": {...}},
            {"name": "match_supplier", "description": "...", "input_schema": {...}}
        ],
        messages=[{"role": "user", "content": [
            {"type": "image", "source": {...}},  # La factura
            {"type": "text", "text": "Procesá esta factura: extraé datos, categorizá, y matcheá proveedor. Hacelo todo en paralelo."}
        ]}]
    )

    # El modelo emite las 3 tool_use en paralelo en UNA response
    # Tu código ejecuta los 3 en paralelo, manda los 3 results juntos
```

**Ahorro:** 3 round-trips → 1 round-trip. Latencia 3x mejor, tokens ~30% menos (no repetís contexto en cada round).

### 3. Structured outputs en vez de tool calling para extracción

Si solo necesitás JSON output (no función real), structured outputs es más eficiente:

```python
# ❌ Antes (tool call para forzar JSON)
tools = [{
    "name": "format_response",
    "description": "Format response as JSON",
    "input_schema": {...}
}]

response = client.messages.create(
    tools=tools,
    tool_choice={"type": "tool", "name": "format_response"},
    messages=[...]
)
json_output = response.content[0].input  # Extraer del tool call

# ✅ Mejor (structured outputs nativo, Opus 4.8 / Sonnet 4.6)
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1000,
    output_config={
        "format": {
            "type": "json_schema",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "amount": {"type": "number"},
                    "category": {"type": "string", "enum": ["food", "transport", "utils"]}
                },
                "required": ["name", "amount", "category"]
            }
        }
    },
    messages=[{"role": "user", "content": "Extraé datos de esta factura..."}]
)

# Output ya viene parseado como JSON
import json
data = json.loads(response.content[0].text)
```

**Beneficios:**
- Menos tokens (no overhead de tool definition)
- Garantía de schema (no parsing errors)
- Más rápido

### 4. Tool result truncation

Si tu tool retorna mucho output, truncá antes de devolverlo al LLM:

```python
def call_search_tool(query):
    raw_results = expensive_search(query)  # Puede ser 10K tokens

    # Truncá a top 5 más relevantes
    top_results = raw_results[:5]

    # Format compacto
    return {
        "results": [{"title": r.title, "snippet": r.snippet[:200]} for r in top_results]
    }
    # Output al LLM: ~500 tokens
```

**Regla:** el LLM raramente necesita >500-1000 tokens de tool output para razonar. Más es ruido.

### 5. Tool definitions cacheadas

Tools van AL INICIO del prefix. Si el set de tools es estable, cachealos:

```python
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1000,
    tools=tools,  # Set estable
    system=[
        {"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}
    ],
    messages=[...]
)
# Tools + system se cachean juntos (90% descuento en hits)
```

⚠️ **CRÍTICO:** si cambiás un tool entre requests, INVALIDA TODO el cache (tools van al inicio). Mantené tools estables.

### 6. Tool search para sets grandes (Anthropic beta)

Si tenés >20 tools, mandalos todos cuesta tokens y confunde al modelo. **Tool search** carga schemas on-demand:

```python
# Tool search está en beta, valida si está GA en tu fecha
response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=2000,
    betas=["tool-search-2025-XX-XX"],  # check current beta header
    tools=[
        {
            "type": "tool_search_20250410",
            "name": "tool_search",
            "tool_database_id": "your_db_id"  # 100+ tools registrados
        }
    ],
    messages=[...]
)
# Modelo busca solo los tools relevantes, no carga todos
```

**Use case:** AGENTE STUDIO con 50+ herramientas (Imagen, Veo, Brush, etc.) — tool search reduce 80% de overhead.

## Patrón completo: agente con tools optimizado

```python
class OptimizedAgent:
    def __init__(self):
        # Tool definitions: concisos + estables (para caching)
        self.tools = [
            {
                "name": "search_db",
                "description": "Search products/orders/customers by natural language query",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "table": {"type": "string", "enum": ["products", "orders", "customers"]},
                        "limit": {"type": "integer", "default": 5}
                    },
                    "required": ["query", "table"]
                }
            },
            {
                "name": "send_email",
                "description": "Send transactional email. Use only when explicitly requested by user.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "to": {"type": "string", "format": "email"},
                        "subject": {"type": "string"},
                        "body": {"type": "string"}
                    },
                    "required": ["to", "subject", "body"]
                }
            }
        ]

    def run(self, user_query):
        messages = [{"role": "user", "content": user_query}]

        while True:
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=2000,
                tools=self.tools,  # Estable → cacheado
                system=[{
                    "type": "text",
                    "text": "You are a helpful assistant.",
                    "cache_control": {"type": "ephemeral"}
                }],
                messages=messages
            )

            messages.append({"role": "assistant", "content": response.content})

            if response.stop_reason == "end_turn":
                return response.content

            if response.stop_reason == "tool_use":
                # Ejecutar tools en PARALELO
                tool_uses = [b for b in response.content if b.type == "tool_use"]
                tool_results = self._execute_parallel(tool_uses)

                messages.append({
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": result["tool_use_id"],
                            "content": result["output"][:1000]  # Truncar a 1000 chars
                        }
                        for result in tool_results
                    ]
                })

    def _execute_parallel(self, tool_uses):
        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {
                executor.submit(self._execute_tool, tu): tu.id
                for tu in tool_uses
            }
            return [
                {
                    "tool_use_id": tool_id,
                    "output": future.result()
                }
                for future, tool_id in [(f, futures[f]) for f in concurrent.futures.as_completed(futures)]
            ]
```

## Casos del usuario

### BIO-SETA / AGENTE GASTROWHATS
- Tools posibles: `check_inventory`, `get_price`, `register_order`, `escalate_to_human`
- **Optimizar:**
  - Cachear tool definitions + system (estables)
  - Structured output para parsear intent del cliente
- **Ahorro estimado:** 30% en latency, 25% en tokens

### AGENTE STUDIO
- Muchas herramientas: Imagen 4, Veo 3, Brush, Photo Edit, etc.
- **Optimizar:**
  - Tool search (cuando GA) si llegamos a 30+ tools
  - Mientras tanto: tools subset por intent del brief
  - Parallel: generar imagen + extraer paleta + analizar mood en paralelo
- **Ahorro estimado:** 40% en latency

### AGENTE TRADING
- Tools: `get_price`, `get_news`, `analyze_chart`, `execute_trade` (con confirmación humana)
- **Optimizar:**
  - Parallel: price + news + chart en simultáneo
  - Truncate news output a top 5 headlines
  - Tool result caching para `get_news` (no cambia minuto a minuto)
- **Ahorro estimado:** 50% en latency

### SaaS XPRIZE
- Pipeline: extract → categorize → match_supplier → push_to_siigo (tools encadenados)
- **Optimizar:**
  - Parallel para extract + categorize + match (3 tools en 1 round)
  - Push a Siigo como tool separado (require previous results)
  - Structured outputs para extract schema
- **Ahorro estimado:** 50% latency, 30% tokens

## Anti-patterns

❌ **Tool con 20+ parameters opcionales** — modelo se confunde
❌ **Description "use this tool wisely"** — useless, no guía cuándo
❌ **Tool retorna 10K tokens de output** — truncá
❌ **Cambiar tools entre requests** — invalida cache, lento
❌ **Serial cuando podría ser parallel** — paga latencia innecesaria

## Checklist

- [ ] Tool descriptions <100 caracteres cada una
- [ ] Cada description dice CUÁNDO usar el tool (no solo qué hace)
- [ ] Input schemas usan `enum` donde aplica
- [ ] Tools list ESTABLE (no cambia entre requests) → permite caching
- [ ] Tool outputs truncados (<1000 tokens cada uno)
- [ ] Parallel tool calls cuando independientes
- [ ] Structured outputs en vez de tool call si solo querés JSON
- [ ] Para sets grandes (>20 tools): considerar tool search beta
- [ ] Cache tools + system con `cache_control`
- [ ] Medir: tokens promedio por agentic loop vs baseline

Relacionado: [[01-prompt-caching]], [[03-model-routing]], [[09-streaming-early-termination]]
