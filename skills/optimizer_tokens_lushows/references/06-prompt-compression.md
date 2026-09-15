# 06 — Prompt Compression (30-50% reducción de tokens)

**Impacto:** 30-50% menos tokens manteniendo calidad equivalente.
**Esfuerzo:** Medio (instalar tooling + integrar pre-processing).
**Cuándo aplicar:** Prompts >3K tokens, RAG con chunks largos, conversaciones multi-turn extensas.
**Cuándo NO aplicar:** Prompts cortos (<500 tokens), tareas que requieren precisión palabra por palabra.

## Por qué importa

Si tu prompt promedio es 5K tokens y comprimís 40%, ahorrás 2K tokens por request. Con 10K requests/día = 20M tokens/día menos = $60-100/día menos (depende del modelo). Anualizado: **$22K-37K USD/año.**

## Técnicas en orden de impacto

### 1. LLMLingua / LongLLMLingua (Microsoft Research)

Compresión inteligente que mantiene semántica:

```python
# pip install llmlingua
from llmlingua import PromptCompressor

compressor = PromptCompressor(
    model_name="microsoft/llmlingua-2-xlm-roberta-large-meetingbank",
    use_llmlingua2=True
)

original_prompt = """
Eres un asistente experto en marketing digital con 15 años de experiencia
en campañas de Google Ads, Facebook Ads, e Instagram. Has trabajado con
marcas Fortune 500 y conoces profundamente las mejores prácticas del
industry. Tu tarea es analizar el siguiente brief y proponer una estrategia
de campaña detallada que incluya...
"""  # 200 tokens

compressed = compressor.compress_prompt(
    original_prompt,
    target_token=100,  # Comprimir a 100 tokens
    rate=0.5,  # O comprimir al 50% del original
)

print(compressed["compressed_prompt"])
# Output: "Asistente marketing digital 15 años experiencia Google/FB/IG Ads.
#          Trabajó marcas Fortune 500. Analizá brief, propone estrategia
#          campaña detallada incluyendo..."
# ~100 tokens, mantiene info clave
```

**Resultados típicos:**
- Compresión 2-5x
- Calidad mantiene 95%+ vs original
- Funciona en español, inglés, multiidioma

**Cuándo usar:**
- System prompts largos
- Few-shot examples (comprime cada example individualmente)
- Documentos retrievados en RAG

**Cuándo NO usar:**
- Instrucciones críticas donde palabra exacta importa
- Código (puede romper sintaxis)
- Datos estructurados (JSON, XML)

### 2. Resumen de turnos antiguos (conversaciones)

Para chats multi-turn que crecen indefinidamente:

```python
def compress_conversation(messages, keep_recent=5):
    """Compress all but the last N messages into a summary."""
    if len(messages) <= keep_recent + 2:
        return messages

    old_messages = messages[:-keep_recent]
    recent_messages = messages[-keep_recent:]

    # Resumir con Haiku (barato)
    summary = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=400,
        messages=[{
            "role": "user",
            "content": f"""Resume esta conversación en máximo 300 palabras.
Preserva:
- Decisiones tomadas
- Preferencias del usuario expresadas
- Información personal compartida
- Cualquier compromiso o promesa hecha

Conversación:
{format_messages(old_messages)}
"""
        }]
    ).content[0].text

    return [
        {"role": "user", "content": f"[CONTEXTO COMPRIMIDO de turnos previos: {summary}]"},
        *recent_messages
    ]
```

**Ahorro típico:** conversación de 50 turns (20K tokens) → resumen + últimos 5 turns (~3K tokens) = **85% menos**.

**Trade-off:** detalles específicos de turnos viejos se pierden. Usar solo si OK perder granularidad.

### 3. Sliding window simple

Menos sofisticado pero más rápido:

```python
def sliding_window(messages, window_size=10):
    """Just keep last N messages."""
    if len(messages) <= window_size:
        return messages

    # Opción A: dropear todo lo viejo
    return messages[-window_size:]

    # Opción B: mantener "anchor" inicial (importante context) + recent
    return [messages[0]] + messages[-window_size:]
```

**Pro:** zero LLM call para comprimir, deterministic.
**Con:** pierde info de turnos viejos completamente.

### 4. Compresión por few-shot pruning

Si usás examples en prompt, comprimir cada uno:

```python
# ❌ Mal: 5 examples completos
few_shot = """
Ejemplo 1:
Input: "Quiero comprar zapatos"
Categoría: shopping
Razonamiento: El usuario expresa intención de compra explícita...
[200 tokens]

Ejemplo 2:
[200 tokens]
... 5 examples = 1000 tokens
"""

# ✅ Bien: 2-3 examples + format conciso
few_shot = """
Examples:
"quiero comprar zapatos" → shopping
"qué hora es?" → info
"odio este servicio" → complaint

Now classify:
"""
# ~100 tokens, calidad similar
```

**Regla:** 2-3 examples bien elegidos > 10 examples redundantes.

### 5. Tokenization-aware writing

Algunas palabras consumen menos tokens que otras. Útil en prompts críticos:

```python
# Tokens (Anthropic tokenizer aprox):
"utilizes"  → 1 token
"uses"      → 1 token  ✅ mismo costo, más simple

"approximately"  → 2 tokens
"about"          → 1 token  ✅ ahorro

"in order to"  → 3 tokens
"to"           → 1 token  ✅ ahorro

# Para verificar con precisión:
response = client.messages.count_tokens(
    model="claude-opus-4-8",
    messages=[{"role": "user", "content": "tu texto"}]
)
print(response.input_tokens)
```

**Mini-guía:**
- Preferir palabras cortas cuando posible
- Eliminar filler words ("just", "really", "actually")
- Evitar redundancia ("end result" → "result")
- Listas en lugar de párrafos cuando estructural

### 6. Eliminar metadata innecesaria

Cuando tu prompt incluye structured data:

```python
# ❌ Mal: JSON pretty con verbosidad
context = json.dumps(data, indent=2)
# {
#   "user": {
#     "name": "Luis",
#     "email": "luis@example.com",
#     "preferences": {
#       "language": "es"
#     }
#   }
# }
# 50 tokens

# ✅ Bien: format compacto
context = f"User: Luis ({data['user']['email']}), prefs: es"
# 15 tokens
```

```python
# Si DEBES enviar JSON, usar compact mode
context = json.dumps(data, separators=(',', ':'))  # No spaces extra
```

## Compresión en RAG context

Chunks retrievados suelen tener mucho ruido (headers, footers, navigation, repeated boilerplate):

```python
def clean_rag_chunk(chunk: str) -> str:
    """Strip noise from retrieved chunks before sending to LLM."""
    # Eliminar headers/footers comunes
    chunk = re.sub(r'<!-- HEADER -->.*?<!-- /HEADER -->', '', chunk, flags=re.DOTALL)

    # Eliminar líneas vacías excesivas
    chunk = re.sub(r'\n{3,}', '\n\n', chunk)

    # Eliminar markdown decorativo
    chunk = re.sub(r'^={3,}|^-{3,}', '', chunk, flags=re.MULTILINE)

    # Trim whitespace agresivo
    chunk = '\n'.join(line.strip() for line in chunk.split('\n') if line.strip())

    return chunk.strip()
```

**Ahorro típico:** 20-30% menos tokens en chunks RAG.

## Compresión semántica con LLM (meta-compression)

Para casos extremos, usar Haiku para resumir antes de pasar a Opus:

```python
def two_stage_processing(large_document: str, user_question: str):
    """Pre-process with cheap model, then answer with expensive."""

    # Stage 1: Haiku extrae info relevante del documento (cheap)
    relevant_info = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=500,
        messages=[{
            "role": "user",
            "content": f"""
Documento:
{large_document}

Pregunta del usuario:
{user_question}

Extraé SOLO la información del documento que es relevante para responder
esa pregunta. Máximo 300 palabras. NO respondas la pregunta, solo extraé.
            """
        }]
    ).content[0].text

    # Stage 2: Opus responde con info comprimida (costo reducido)
    final_response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1000,
        messages=[{
            "role": "user",
            "content": f"""
Contexto relevante:
{relevant_info}

Pregunta: {user_question}
            """
        }]
    ).content[0].text

    return final_response
```

**Cuándo vale la pena:**
- Documentos >20K tokens
- Pregunta requiere razonamiento (Opus)
- Costo de Haiku stage ($0.001) << costo de pasarle el doc completo a Opus ($0.10+)

## Cuándo NO comprimir

⚠️ **Compresión puede DEGRADAR calidad.** Tests obligatorios antes de producción.

### Casos donde compresión rompe calidad:

| Caso | Por qué |
|---|---|
| Tareas de extracción precisa | Comprimir puede eliminar el dato exacto |
| Generación de código | Sintaxis o constantes pueden perderse |
| Traducción | Matices se pierden |
| Documentos legales | Cláusulas específicas críticas |
| Datos médicos | Cualquier omisión es problema |
| JSON / XML structured data | Romper estructura = error de parsing |

## Cómo medir si tu compresión funciona

```python
def eval_compression(test_queries, original_prompts, compressed_prompts):
    """A/B test compression on real queries."""
    results = []

    for query, orig, comp in zip(test_queries, original_prompts, compressed_prompts):
        orig_response = call_llm(orig + query)
        comp_response = call_llm(comp + query)

        # Juez evalúa
        winner = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=50,
            messages=[{"role": "user", "content": f"""
Query: {query}
Respuesta A: {orig_response}
Respuesta B: {comp_response}

¿Cuál responde mejor? A / B / EQUAL
            """}]
        ).content[0].text.strip()

        results.append({
            "query": query,
            "orig_tokens": count_tokens(orig),
            "comp_tokens": count_tokens(comp),
            "compression_ratio": count_tokens(comp) / count_tokens(orig),
            "winner": winner
        })

    # Si EQUAL o B en >85% de casos, compresión es safe
    safe = sum(1 for r in results if r["winner"] in ["B", "EQUAL"]) / len(results)
    avg_compression = sum(r["compression_ratio"] for r in results) / len(results)

    print(f"Compresión promedio: {(1-avg_compression)*100:.0f}% menos tokens")
    print(f"Quality equivalente o mejor: {safe*100:.0f}% de casos")
    print(f"{'✅ DEPLOY' if safe > 0.85 else '⚠️ NO DEPLOY — degrada calidad'}")
```

## Casos del usuario

### BIO-SETA
- System prompt actual ~3K tokens → comprimir a ~1K con LLMLingua-2
- Conversaciones multi-turn → sliding window de 10 + summary
- **Ahorro estimado:** 35%

### AGENTE STUDIO
- Brand guidelines (5-15K tokens) → comprimir con LLMLingua a 2-5K
- **Cuidado:** verificar que tokens críticos del brand no se pierden (logo specs, colors)
- **Ahorro estimado:** 40-50% en pipelines creativos

### AGENTE TRADING
- Historial de trades del día (5-10K tokens) → resumir con Haiku stage 1
- **Ahorro estimado:** 50% en análisis end-of-day

### SaaS XPRIZE
- Categorías de proveedor (lista larga) → compresión + alphabetical lookup
- Few-shot examples de OCR → de 5 examples a 3 examples curados
- **Ahorro estimado:** 25%

## Stack de herramientas

| Tool | Para qué |
|---|---|
| **LLMLingua-2** (Microsoft) | Compresión general de texto, calidad estado del arte |
| **LongLLMLingua** | Específico para contextos muy largos (>10K tokens) |
| **Selective Context** (Microsoft) | Otra técnica de compresión, similar |
| **Tiktoken / count_tokens API** | Medir tokens antes y después |
| **Anthropic count_tokens endpoint** | Más preciso para Claude vs tiktoken |

## Checklist

- [ ] Auditar prompts actuales: cuáles tienen >2K tokens?
- [ ] Identificar partes "redundantes" del system prompt
- [ ] Aplicar pruning manual primero (filler words, repeticiones)
- [ ] Probar LLMLingua-2 en casos no-críticos primero
- [ ] Eval A/B con juez antes de deploy a producción
- [ ] Implementar conversation compression para chats multi-turn
- [ ] Si usás RAG: limpiar chunks antes de enviar al LLM
- [ ] Medir tokens antes/después con `count_tokens` (no tiktoken)
- [ ] NO comprimir tareas críticas (extraction precisa, code, legal)

Relacionado: [[04-context-engineering]], [[07-rag-eficiente]], [[03-model-routing]]
