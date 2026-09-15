# 01 — Prompt Caching (la palanca #1, 90% descuento)

**Impacto:** 60-90% reducción de costo en cualquier sistema con contexto reutilizable.
**Esfuerzo:** Bajo (3-10 líneas de código).
**Cuándo NO aplicar:** Si el prompt cambia 100% en cada request (no hay prefix reusable).

## El invariante UNO que todo lo demás obedece

> **Caching es prefix match. Cualquier cambio de byte EN CUALQUIER PARTE del prefix invalida TODO lo que viene después.**

El orden de render es: `tools` → `system` → `messages`. Un breakpoint en el último bloque del system cachea tools + system juntos.

## Anthropic — Caching (90% descuento en hits)

### Opción A: Auto-caching top-level (más simple, recomendado)

```python
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    cache_control={"type": "ephemeral"},  # ← cachea el último bloque cacheable
    system="You are an expert on this 50KB document...",
    messages=[{"role": "user", "content": "Resumen?"}]
)
```

**Primera request:** paga 1.25x (write premium) por todo el system.
**Requests siguientes (≤5 min):** paga 0.1x por el system cacheado + 1x por el nuevo mensaje.

### Opción B: Cache_control manual en bloques específicos

```python
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    system=[
        {
            "type": "text",
            "text": SYSTEM_PROMPT_LARGO,
            "cache_control": {"type": "ephemeral"}  # 5-min TTL (default)
        }
    ],
    messages=[{"role": "user", "content": "..."}]
)

# Con TTL de 1 hora (premium 2x en write, pero dura más)
system=[{
    "type": "text",
    "text": SYSTEM_PROMPT_LARGO,
    "cache_control": {"type": "ephemeral", "ttl": "1h"}
}]
```

### Verificar que el cache funciona

```python
print(response.usage.cache_creation_input_tokens)  # Tokens escritos (1.25x cost)
print(response.usage.cache_read_input_tokens)      # Tokens servidos del cache (0.1x cost)
print(response.usage.input_tokens)                 # Tokens no cacheados (1x cost)
```

**Si `cache_read_input_tokens` es 0 entre requests idénticos → algo invalidó el cache.** Auditar contra la tabla de silent invalidators abajo.

### Límites importantes

- **Máximo 4 breakpoints** `cache_control` por request
- **Minimum cacheable prefix** depende del modelo:
  - Opus 4.8/4.7/4.6, Haiku 4.5: **4096 tokens** mínimo
  - Sonnet 4.6, Haiku 3.5: **2048 tokens** mínimo
- Si tu prefix es menor al mínimo, **NO se cachea** (silenciosamente, sin error)
- **Lookback window: 20 bloques** — si una conversación agrega >20 bloques entre breakpoints, el cache se "pierde"

### Economics break-even

**Cache 5-min (default):**
- Write: 1.25x base price
- Read: 0.1x base price
- **Break-even: 2 requests** (1.25 + 0.1 = 1.35 < 2x sin cache)

**Cache 1-hora:**
- Write: 2x base price
- Read: 0.1x base price
- **Break-even: 3 requests** (2 + 0.2 = 2.2 < 3x sin cache)

→ **Solo cachea si esperas mínimo 2 hits** (5min) o **3 hits** (1h). Cachear con 1 sola lectura SALE MÁS CARO.

## Patrones de placement (cuándo poner el breakpoint)

### Patrón 1: System prompt grande, varias requests

```python
system=[
    {"type": "text", "text": SYSTEM_LARGE, "cache_control": {"type": "ephemeral"}}
]
```

### Patrón 2: Multi-turn conversation

Poner breakpoint en el último bloque de la última respuesta del modelo. Cada request reusa todo el historial previo.

```python
messages=[
    *history,
    {"role": "user", "content": [
        {"type": "text", "text": user_message},
        # NO marker aquí — varía cada turno
    ]}
]
# El breakpoint va en system o en el último mensaje del assistant del historial
```

### Patrón 3: Shared prefix + question variable (RAG)

```python
messages=[{
    "role": "user",
    "content": [
        {"type": "text", "text": shared_docs, "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": variable_question}  # SIN marker — varía
    ]
}]
```

### Patrón 4: Mid-conversation system messages (beta)

Cuando hay instrucción operacional mid-sesión (cambio de modo, contexto inyectado), NO edites el system top-level — appendea `role: "system"` a `messages`. Preserva el cache.

```python
client.messages.create(
    model="claude-opus-4-8",
    system=[{"type": "text", "text": STABLE, "cache_control": {"type": "ephemeral"}}],
    messages=[
        *history,
        {"role": "user", "content": user_msg},
        {"role": "system", "content": "Terse mode activated."}  # beta header required
    ],
    extra_headers={"anthropic-beta": "mid-conversation-system-2026-04-07"}
)
```

## Silent invalidators (cosas que rompen el cache sin error)

Auditar prompt assembly contra esta tabla:

| Pattern | Por qué rompe el cache |
|---|---|
| `datetime.now()` en system prompt | Cambia cada request |
| `uuid4()` o IDs aleatorios en prefix | Idem |
| `json.dumps(d)` sin `sort_keys=True` | Orden no-determinístico → bytes diferentes |
| Iterar un `set` en Python | Orden no-determinístico |
| f-string interpolando session_id en system | Cache por-usuario (no cross-user) |
| `if flag: system += "..."` | Cada combinación de flags = prefix distinto |
| Tools cambian entre requests | Tools van al inicio → invalida TODO |
| Cambiar modelo mid-conversación | Cache es model-scoped → todo invalida |

**Fix:** mover lo dinámico al final del prompt (después del último breakpoint), o eliminar si no es load-bearing.

## OpenAI — Caching automático

OpenAI activó caching automático en 2024. **No requiere código.** Cualquier prefix >1024 tokens se cachea automático.

- **Cache hit discount:** 50% (no 90% como Anthropic)
- Aparece en `usage.prompt_tokens_details.cached_tokens`

```python
response = client.chat.completions.create(...)
print(response.usage.prompt_tokens_details.cached_tokens)  # Tokens cacheados
```

**No hay control manual.** OpenAI decide qué cachea. Para max control → usar Anthropic.

## Gemini — Context Caching

Gemini tiene context caching pero requiere setup explícito (no automático):

```python
from google import genai
from google.genai.types import CreateCachedContentConfig

client = genai.Client()

# Crear cache (paga upfront)
cache = client.caches.create(
    model="gemini-2.5-pro",
    config=CreateCachedContentConfig(
        system_instruction=SYSTEM_LARGE,
        ttl="3600s"  # 1 hora
    )
)

# Usar cache
response = client.models.generate_content(
    model="gemini-2.5-pro",
    contents="¿Pregunta?",
    config={"cached_content": cache.name}
)
```

**Pricing:** ~25% del normal en hits + storage cost por minuto.

## Pre-warming (eliminar latencia del primer hit)

Para que el primer usuario no pague el cache write premium:

```python
# Al arrancar el server, hacer 1 request "warmup" con max_tokens=0
client.messages.create(
    model="claude-opus-4-8",
    max_tokens=0,  # No genera output (response.content = [])
    system=[{"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}],
    messages=[{"role": "user", "content": "warmup"}]
)
# Cache queda escrito. Próximas requests reales = cache hits.
```

⚠️ `max_tokens=0` falla si tienes `stream=True` o `thinking enabled`. Solo para warmup puro.

## Casos reales del usuario

### BIO-SETA / AGENTE GASTROWHATS
System prompt del bot (~3K tokens con descripción de productos, precios, FAQs).
**Aplicar caching:** sí, alto ROI. Cada cliente WhatsApp dispara N mensajes → cache hits.
**Ahorro estimado:** 70-85% del costo de Claude API.

### AGENTE STUDIO
Generación creativa con prompts largos por marca (5-15K tokens de brand guidelines).
**Aplicar caching:** sí, crítico. Una marca = 10-50 generaciones/día sobre mismo brand prompt.
**Ahorro estimado:** 80%.

### AGENTE TRADING
Análisis diario con system prompt grande de estrategias y reglas.
**Aplicar caching:** sí, perfecto fit. 1 análisis/hora x 24h = 24 cache hits/día.
**Ahorro estimado:** 85%.

### SaaS XPRIZE multi-tenant
System prompt del OCR de facturas con schema JSON (~2K tokens).
**Aplicar caching:** sí. Cada factura procesada hit el cache.
**Ahorro estimado:** 75%.

## Checklist al implementar

- [ ] Identificar el prefix estable (system + tools + historial común)
- [ ] Verificar que el prefix sea ≥ minimum cacheable size del modelo
- [ ] Decidir TTL (5min default; 1h si tráfico bursty con gaps largos)
- [ ] Auditar silent invalidators (Date.now, sets, conditionals)
- [ ] Implementar con `cache_control: ephemeral`
- [ ] Medir `cache_read_input_tokens` en logs primeras 24h
- [ ] Si hit rate < 30% → algo invalida, debuggear bytes del prefix entre requests
- [ ] Documentar ahorro vs baseline

Relacionado: [[00-fundamentos-optimizacion]], [[04-context-engineering]], [[10-monitoring-budget]]
