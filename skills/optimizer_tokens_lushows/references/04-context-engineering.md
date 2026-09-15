# 04 — Context Engineering (el paradigma 2026)

**Impacto:** 30-50% reducción de tokens manteniendo o mejorando calidad.
**Esfuerzo:** Alto (rediseño de pipelines de prompt assembly).
**Cuándo aplicar:** Cualquier sistema con prompts largos (>2K tokens) o conversaciones multi-turn.

## Por qué "prompt engineering" murió y nació "context engineering"

En 2023 todo era "cómo escribo el mejor prompt". En 2026 la pregunta es:

> **"¿Qué SABE, VE y RECUERDA el modelo en este preciso instante?"**

Context engineering = diseñar la INFRAESTRUCTURA que arma el contexto, no escribir el texto perfecto.

### Comparación

| Prompt Engineering (viejo) | Context Engineering (2026) |
|---|---|
| "Cómo le hablo al modelo" | "Qué información ve y en qué orden" |
| Optimizar palabras y formato | Optimizar pipelines de assembly |
| Trial-and-error textual | Arquitectura de datos para LLMs |
| Prompts hardcoded de 5K tokens | Context dinámico curado per-request |
| Trabajo de prompt designer | Trabajo de ingeniero de plataforma |

## Las 4 reglas de oro del context engineering (research-backed 2026)

### Regla 1: Sweet spot 150-300 words por instrucción clave

Research muestra que comprehension del LLM **degrada significativamente >3,000 tokens**. Los prompts de "20 páginas de instrucciones" son contraproducentes — el modelo ignora o confunde reglas.

```python
# ❌ Mal: instrucciones acumuladas sin curar
system = """
Eres un asistente.
Sé amable.
Sé profesional.
No uses jerga.
Pero tampoco demasiado formal.
Responde en español.
Pero en inglés si te hablan en inglés.
Usa emojis pero no muchos.
Cita fuentes pero solo si las tienes.
...50 reglas más, contradictorias o redundantes...
"""

# ✅ Bien: instrucciones core, breves y específicas
system = """
Eres el asistente de BIO-SETA, tienda de hongos funcionales.

Tono: cálido pero conciso. Habla del producto, no de generalidades.
Idioma: español (español Colombia preferido).
Si no sabés algo: decilo. No inventes precios ni stock.
"""
```

**Regla práctica:** si tu system prompt tiene >300 palabras, audítalo. Probablemente la mitad es ruido.

### Regla 2: "Lost in the middle" — info importante AL INICIO o AL FINAL

LLMs degradan en recall cuando la info crítica está en el MEDIO de un contexto largo (paper "Lost in the Middle", confirmado en 2026 con Claude 4.x).

```
┌─────────────────────────────────────┐
│  ✅ INICIO: Recall alto             │
│  Instrucciones principales aquí     │
├─────────────────────────────────────┤
│  ⚠️  MEDIO: Recall bajo             │
│  Detalles menos críticos            │
│  Background information             │
├─────────────────────────────────────┤
│  ✅ FINAL: Recall alto              │
│  Pregunta/task actual del user      │
│  Constraints críticas               │
└─────────────────────────────────────┘
```

**Patrón ganador:**

```python
# Estructura recomendada
prompt = f"""
{INSTRUCCIONES_CRITICAS}  # Al inicio

{CONTEXTO_BACKGROUND}      # En el medio (menos importante)

{DATOS_RELEVANTES_RAG}     # Más al final (más importante)

User question: {pregunta}
Constraints: {constraints_criticas}  # Al final, alto recall
"""
```

### Regla 3: Trata el contexto como INFRAESTRUCTURA, no como prompt

Tu pipeline de context assembly debe ser:
- **Reproducible:** mismo input → mismo contexto
- **Loggeado:** cada request loggear qué context se armó
- **Versionado:** prompts en git, no string en código
- **Testeable:** evals que validan que el contexto correcto se ensambla
- **Curado:** privacy controls (no leak PII), redacción automática

```python
# ❌ Mal: contexto armado ad-hoc
def chat(message, user):
    response = client.messages.create(
        system=f"Eres bot. User es {user.name}. Su historial: {user.history}",  # caos
        ...
    )

# ✅ Bien: pipeline estructurado
class ContextBuilder:
    def __init__(self, user_id):
        self.user = self._load_user(user_id)
        self.history = self._load_history(user_id)
        self.preferences = self._load_preferences(user_id)

    def build_system(self) -> str:
        return SYSTEM_TEMPLATE.format(
            persona=self.user.persona,
            preferences=self._format_preferences()
        )

    def build_messages(self, current_msg: str) -> list:
        # Decide qué historial incluir (no todo)
        relevant_history = self._select_relevant(self.history, current_msg)
        return [
            *relevant_history,
            {"role": "user", "content": current_msg}
        ]

    def log_context(self):
        # Para debug/observability
        return {"user_id": self.user.id, "history_msgs": len(self.history)}
```

### Regla 4: Pruning agresivo — quitar TODO lo no esencial

Cada token cuesta. Si no agrega valor al output, fuera.

**Auditá tu prompt y quitá:**
- Cortesías ("Por favor...", "Sería tan amable...") — el modelo no necesita esto
- Repeticiones de la misma instrucción en diferentes palabras
- Examples que no aportan (1 example bueno > 5 mediocres)
- Markdown decorativo (separadores `===`, líneas vacías excesivas)
- Disclaimers obvios ("Eres un AI", "Tienes limitaciones")
- Contexto histórico irrelevante para esta query específica

```python
# ❌ Mal: 800 tokens
system = """
=====================================
       INSTRUCCIONES DEL SISTEMA
=====================================

Hola querido modelo. Por favor, ten en cuenta lo siguiente:

1) Eres un asistente AI. Eso significa que tienes limitaciones.
2) Por favor, sé útil. La utilidad es muy importante.
3) Pero también sé honesto. La honestidad también es importante.
4) Y por supuesto, no hagas daño.
5) Te recordamos también que no inventes información.
6) Tampoco inventes citas.
7) Recuerda no inventar tampoco fuentes.
8) En general, no inventes nada.

... etc etc ...
"""

# ✅ Bien: 80 tokens, misma efectividad
system = """
Asistente de [proyecto X]. Responde con info verificable.
Si no sabés, decílo. No inventes fuentes ni cifras.
"""
```

## Anti-patterns que destruyen contexto

### Anti-pattern 1: System prompt creciendo orgánicamente

Cada vez que alguien encuentra un edge case → "agrega esto al system". Después de 6 meses tu system tiene 8K tokens, 60% son fixes obsoletos.

**Solución:** revisar mensual. Borrar lo que ya no aplica.

### Anti-pattern 2: Incluir TODO el historial siempre

```python
# ❌ Mal: history de 100 mensajes en cada llamada
messages = user.all_history + [new_message]  # 50K tokens innecesarios

# ✅ Bien: ventana relevante
recent = user.history[-10:]  # Últimos 10
relevant = retrieve_semantically_relevant(user.history, new_message, k=5)
messages = recent + relevant + [new_message]
```

### Anti-pattern 3: Tools list infinito

```python
# ❌ Mal: 50 tools, modelo se confunde
tools = ALL_AVAILABLE_TOOLS  # 50 tools en cada request

# ✅ Bien: subset por contexto (o tool search)
if user_intent == "financial":
    tools = FINANCIAL_TOOLS  # 5 tools
elif user_intent == "support":
    tools = SUPPORT_TOOLS  # 4 tools
```

### Anti-pattern 4: Documentos RAG completos sin chunking

```python
# ❌ Mal: documento entero como context
context = "Aquí está el manual de 200 páginas: ..."  # 80K tokens

# ✅ Bien: chunks relevantes via RAG
chunks = vector_search(query, top_k=5)  # 2K tokens relevantes
context = "Contexto relevante:\n" + "\n---\n".join(chunks)
```

## Técnicas de compresión semántica de contexto

### Resumir conversaciones largas

```python
def compress_conversation(messages, threshold=10):
    if len(messages) > threshold:
        # Resumir los primeros N-5 mensajes
        old = messages[:-5]
        recent = messages[-5:]

        summary = client.messages.create(
            model="claude-haiku-4-5",  # Haiku barato para resumir
            max_tokens=300,
            messages=[{"role": "user", "content": f"""
Resume esta conversación en máximo 200 palabras, preservando:
- Decisiones tomadas
- Preferencias del usuario expresadas
- Info personal compartida

Conversación:
{format_messages(old)}
            """}]
        ).content[0].text

        return [
            {"role": "user", "content": f"[Resumen de conversación previa: {summary}]"},
            *recent
        ]
    return messages
```

**Ahorro típico:** conversaciones de 50 turns que ocupaban 20K tokens → 5K tokens (75% menos).

### Sliding window con anchor importante

```python
def sliding_window_with_anchor(messages, window=10):
    if len(messages) <= window:
        return messages

    # Mantener primeros 2 (suelen tener context crítico)
    # + últimos N (conversación actual)
    return messages[:2] + messages[-window:]
```

## Cómo medir si tu context engineering funciona

### Métrica 1: Token efficiency ratio

```python
def context_efficiency(response):
    """Ratio de output útil vs input enviado."""
    return response.usage.output_tokens / (
        response.usage.input_tokens +
        response.usage.cache_read_input_tokens * 0.1 +  # Cache cuenta menos
        response.usage.cache_creation_input_tokens * 1.25
    )

# Objetivo: ratio > 0.05 (5%)
# Si ratio < 0.02 → estás enviando mucho context que no se traduce a output
```

### Métrica 2: Quality vs context size A/B

```python
# Test: misma query con context corto vs largo
def ab_test_context_size(query):
    short_context = build_minimal_context(query)
    long_context = build_full_context(query)

    short_response = call_llm(short_context + query)
    long_response = call_llm(long_context + query)

    # Juez evalúa cuál responde mejor
    winner = judge_quality(query, short_response, long_response)

    # Si short gana o empata: el context largo era ruido
    return winner
```

## Patrón completo: pipeline de context engineering

```python
class ProductionContextPipeline:
    """Pipeline reproducible y observable de assembly de contexto."""

    def __init__(self, request):
        self.request = request
        self.metadata = {}  # Para logging

    def build(self) -> dict:
        """Arma el request completo para LLM."""

        # 1. System prompt curado (corto, específico)
        system = self._build_system()

        # 2. Tools relevantes (no todos)
        tools = self._select_tools()

        # 3. History comprimido (no todo)
        history = self._select_history()

        # 4. Contexto RAG si aplica (top-k, no docs completos)
        rag_context = self._retrieve_relevant_docs()

        # 5. Mensaje actual (al final, alto recall)
        messages = [
            *history,
            {"role": "user", "content": [
                {"type": "text", "text": rag_context},
                {"type": "text", "text": self.request.user_message}
            ]}
        ]

        # Log para observability
        self._log_metadata(system, tools, messages)

        return {
            "model": self._select_model(),
            "system": system,
            "tools": tools,
            "messages": messages,
            "cache_control": {"type": "ephemeral"}
        }

    def _build_system(self) -> str:
        # Template versionado, NUNCA hardcoded en código
        return SYSTEM_TEMPLATES[self.request.persona]

    def _select_tools(self) -> list:
        return TOOLS_BY_INTENT.get(self.request.intent, [])

    def _select_history(self) -> list:
        # Compresión inteligente
        return compress_conversation(self.request.history, threshold=10)

    def _retrieve_relevant_docs(self) -> str:
        # RAG con top-k pequeño
        chunks = vector_search(self.request.user_message, top_k=3)
        return "\n---\n".join(chunks)

    def _select_model(self) -> str:
        # Router del módulo 03
        return MODEL_BY_INTENT[self.request.intent]

    def _log_metadata(self, system, tools, messages):
        self.metadata = {
            "system_tokens": count_tokens(system),
            "tools_count": len(tools),
            "messages_tokens": sum(count_tokens(m) for m in messages),
            "model": self._select_model()
        }
        logger.info("context_assembled", **self.metadata)
```

## Casos del usuario

### BIO-SETA
- System actual probable: 3K tokens con FAQs, productos, tonos, edge cases acumulados
- **Aplicar context engineering:**
  - Reescribir system a 800 tokens core
  - History compress después de 10 turns
  - RAG sobre catálogo de productos (no incluir todo)
- **Ahorro esperado:** 60-70%

### AGENTE STUDIO
- Brand guidelines pueden ser 5-15K tokens
- **Aplicar:** cache brand guidelines (módulo 01) + RAG sobre assets pasados
- Variables del brief al final del prompt (alto recall)
- **Ahorro esperado:** 40-50% combinado con caching

### AGENTE TRADING
- Reglas de estrategia + historial de trades pueden ser 10K+ tokens
- **Aplicar:** sliding window de últimos N trades + summary de los anteriores
- **Ahorro esperado:** 50%

### SaaS XPRIZE
- System de OCR puede ser 2K tokens con ejemplos few-shot
- **Aplicar:** cache system completo, RAG para categorías de proveedor específicas del tenant
- **Ahorro esperado:** 50% adicional sobre caching

## Checklist context engineering

- [ ] System prompt < 1000 tokens (ideal: 200-500)
- [ ] Info crítica al inicio o al final, NUNCA en el medio
- [ ] History comprimido después de N turns
- [ ] Tools relevantes al intent, no lista completa siempre
- [ ] Templates versionados (en git), no hardcoded
- [ ] Pipeline observable (logs de qué se ensambló)
- [ ] Eval A/B: ¿el contexto extra agrega valor o es ruido?
- [ ] Refactor mensual: ¿qué partes del system ya no aplican?

Relacionado: [[00-fundamentos-optimizacion]], [[01-prompt-caching]], [[06-prompt-compression]], [[07-rag-eficiente]]
