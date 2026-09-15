# 05 — Semantic Caching (70%+ ahorro en queries repetitivas)

**Impacto:** 70-73% reducción en sistemas con queries similares recurrentes.
**Esfuerzo:** Medio (requiere vector store + lógica de matching).
**Cuándo aplicar:** FAQs, búsquedas frecuentes, support chatbots, autocompletes de tareas comunes.
**Cuándo NO aplicar:** Decisiones únicas, creatividad, conversaciones contextuales.

## Cómo funciona

```
Usuario: "¿Cuánto cuesta la melena de león en cápsulas?"
           ↓
    Embed la query (Voyage AI, OpenAI embeddings, etc.)
           ↓
    Vector search en cache (Redis VL, Pinecone, pgvector)
           ↓
    ¿Hay respuesta cached con similitud > 0.90?
           ├─ SÍ → Devolver cached (ZERO costo LLM)
           └─ NO → Llamar LLM, guardar nueva entry en cache
```

**Diferencia con prompt caching de Anthropic:**
- **Prompt caching** cachea el PREFIX exacto (byte match). Diferente palabra = miss.
- **Semantic caching** cachea por SIGNIFICADO. "Qué precio tiene X" = "cuánto vale X" = "cost of X".

Son complementarios. Usar ambos cuando aplique.

## Implementación con Redis Vector

### Setup

```python
# pip install redis redisvl
import redis
from redisvl.extensions.llmcache import SemanticCache

r = redis.Redis(host="localhost", port=6379)

cache = SemanticCache(
    name="bio_seta_faq_cache",
    redis_client=r,
    distance_threshold=0.1,  # 0.1 = 90% similar (1 - 0.1)
    ttl=3600,  # 1 hora
    vectorizer=...  # OpenAI, Cohere, HuggingFace embedder
)
```

### Usar el cache

```python
def chat_with_cache(user_query: str) -> str:
    # Buscar en cache primero
    cached = cache.check(prompt=user_query)
    if cached:
        return cached[0]["response"]  # HIT — zero LLM cost

    # MISS — llamar LLM
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=300,
        messages=[{"role": "user", "content": user_query}]
    )
    answer = response.content[0].text

    # Guardar en cache para próximas queries similares
    cache.store(prompt=user_query, response=answer)

    return answer
```

### Tuning del threshold de similitud

```python
# Threshold demasiado bajo (e.g., 0.5) = false positives
#   "¿qué hora es?" puede hacer match con "¿qué día es?"

# Threshold demasiado alto (e.g., 0.99) = casi nunca hits
#   Solo queries idénticas matchean

# Sweet spot típico: 0.85 - 0.95
cache = SemanticCache(distance_threshold=0.08)  # = ~92% similar mínimo
```

## Implementación con Portkey (managed, sin infra)

Portkey ofrece semantic caching como feature del gateway:

```python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="PORTKEY_KEY",
    config={
        "cache": {
            "mode": "semantic",
            "max_age": 3600  # 1 hora
        }
    }
)

# Cualquier completion automáticamente checkea cache semántico
response = portkey.chat.completions.create(
    messages=[{"role": "user", "content": "¿Qué horarios atienden?"}],
    model="claude-haiku-4-5"
)
```

**Pro:** zero infra setup.
**Con:** vendor lock-in + costo de Portkey.

## Implementación con pgvector (Postgres)

Si ya usás Postgres, evitar agregar Redis:

```python
# CREATE EXTENSION vector;
# CREATE TABLE llm_cache (
#     id SERIAL PRIMARY KEY,
#     query_text TEXT,
#     query_embedding VECTOR(1536),
#     response_text TEXT,
#     created_at TIMESTAMP DEFAULT NOW(),
#     hit_count INT DEFAULT 0
# );

def check_cache(query: str, threshold: float = 0.92):
    embedding = embed_query(query)  # OpenAI text-embedding-3-small

    result = db.execute("""
        SELECT response_text, 1 - (query_embedding <=> %s::vector) AS similarity
        FROM llm_cache
        WHERE created_at > NOW() - INTERVAL '1 hour'
        ORDER BY query_embedding <=> %s::vector
        LIMIT 1
    """, (embedding, embedding))

    row = result.fetchone()
    if row and row["similarity"] > threshold:
        # Increment hit counter para analytics
        db.execute("UPDATE llm_cache SET hit_count = hit_count + 1 WHERE id = %s", (row["id"],))
        return row["response_text"]
    return None

def store_cache(query: str, response: str):
    embedding = embed_query(query)
    db.execute("""
        INSERT INTO llm_cache (query_text, query_embedding, response_text)
        VALUES (%s, %s::vector, %s)
    """, (query, embedding, response))
```

## TTL strategies (cuándo expirar entries)

| Tipo de query | TTL recomendado |
|---|---|
| FAQ static (info que no cambia) | 24-48 horas |
| Info que cambia diario (precios) | 1-6 horas |
| Búsquedas time-sensitive | 5-30 minutos |
| Opiniones / análisis personalizados | NO cachear |
| Generaciones creativas | NO cachear |

## Cuándo SÍ y cuándo NO

### ✅ Casos ideales

| Caso | Por qué |
|---|---|
| FAQ bot ("¿cuáles son sus horarios?") | Muchas variaciones de la misma query |
| Soporte de producto | "Cómo configuro X" — varía wording pero respuesta es la misma |
| Search semántico | Queries similares retornan similar info |
| Definiciones técnicas | "Qué es OAuth" = "explicación de OAuth" = "OAuth en simple" |
| Recomendaciones por categoría | "Mejor cordyceps" = "cordyceps recomendado" |

### ❌ Casos NO usar

| Caso | Por qué |
|---|---|
| Conversación contextual ("y qué hay de eso?") | Pierde contexto previo |
| Tareas personalizadas con datos del user | Cada user → diferente respuesta |
| Análisis con datos en tiempo real | Stock, precio, tiempo cambian |
| Creatividad ("escribime un poema") | Cada generación debe ser fresh |
| Decisiones con stakes | Banca, médico, legal — riesgo de respuesta vieja |

## Multi-tenancy: cache por tenant

Para evitar leak de info entre clientes:

```python
def get_cache_for_tenant(tenant_id: str):
    return SemanticCache(
        name=f"cache_tenant_{tenant_id}",  # Namespace per-tenant
        redis_client=r,
        distance_threshold=0.10
    )

# En tu request handler
def handle_query(tenant_id: str, query: str):
    cache = get_cache_for_tenant(tenant_id)
    cached = cache.check(prompt=query)
    if cached:
        return cached[0]["response"]
    # ... llamar LLM, store en cache del tenant
```

## Métricas que importan

```python
class SemanticCacheStats:
    def __init__(self):
        self.hits = 0
        self.misses = 0
        self.false_positive_reports = 0  # Usuario marca respuesta como "no era lo que pregunté"

    @property
    def hit_rate(self) -> float:
        return self.hits / (self.hits + self.misses) if (self.hits + self.misses) > 0 else 0

    @property
    def cost_saved(self) -> float:
        avg_cost_per_call = 0.005  # $0.005 promedio por call al LLM
        return self.hits * avg_cost_per_call
```

**Targets típicos:**
- Hit rate **>30%** → semantic caching está aportando valor
- Hit rate **<10%** → threshold muy alto o queries muy únicas, replantear
- False positives **<2%** → si más, bajar threshold

## Problema común: respuestas obsoletas

```python
# ❌ Problema: alguien actualiza el precio, cache devuelve precio viejo
old_response = "El melena de león cuesta $50.000"
# Usuario pregunta nueva consulta, cache hit, devuelve $50.000
# Pero ahora vale $55.000

# ✅ Solución 1: TTL corto para data sensible
cache = SemanticCache(ttl=300)  # 5 minutos

# ✅ Solución 2: Invalidación manual cuando cambia data
def update_product_price(product_id, new_price):
    db.update(product_id, new_price)
    cache.invalidate_pattern(f"*{product_id}*")  # Borrar entries relacionadas

# ✅ Solución 3: NO cachear queries que dependen de data volátil
def chat(query):
    if any(word in query.lower() for word in ["precio", "costo", "stock", "disponible"]):
        # Bypass cache para estas queries
        return call_llm(query)
    else:
        return cached_chat(query)
```

## Casos del usuario

### BIO-SETA / AGENTE GASTROWHATS
- "¿Qué horarios atienden?" → 100x al día con variaciones
- "¿Tienen [producto X]?" → 50x al día
- "¿Hacen envíos a [ciudad Y]?" → 30x al día
- **Aplicar semantic cache:** SÍ, perfecto fit
- **TTL:** 1 hora para FAQs, 5 min para "stock"
- **Ahorro estimado:** 60-70% del tráfico

### AGENTE STUDIO
- Queries únicas y creativas
- **NO aplicar:** cada brief es único, no hay patrón repetitivo

### AGENTE TRADING
- "Resumen del día de [ticker]" → SÍ cachear (refresh cada hora)
- "Análisis técnico de [ticker]" → SÍ cachear (TTL 30 min)
- "Debería comprar [X]?" → NO cachear (decisión contextual)
- **Ahorro estimado:** 30-40%

### SaaS XPRIZE
- OCR de facturas → cada factura es ÚNICA, NO cachear
- "¿Cuál es mi top proveedor?" → SÍ cachear (cambia poco intra-día)
- "Explicame este cargo de mi factura" → depende, evaluar caso por caso

## Tooling comparado

| Solución | Pro | Con | Costo |
|---|---|---|---|
| **Redis VL** | Self-hosted, full control | Tener que mantener Redis | Infra |
| **Portkey** | Zero infra, fácil | Vendor lock-in, $/req | $0.001/cached req aprox |
| **Helicone** | Observability + cache | Más caro | Pricing por volumen |
| **pgvector** | Si ya usás Postgres | Más lento que Redis | Solo infra Postgres existente |
| **Pinecone** | Production-grade vector DB | Overkill para solo cache | $$$/mes |

## Checklist

- [ ] Identificar 5-10 queries más frecuentes de producción
- [ ] Validar que tienen alta tasa de repetición (>20% del tráfico)
- [ ] Elegir vector store (Redis VL es el más popular)
- [ ] Implementar check → call → store flow
- [ ] Tunear threshold con sample de queries reales
- [ ] Definir TTL por tipo de query
- [ ] Implementar invalidación manual para data volátil
- [ ] Multi-tenant: namespace por tenant
- [ ] Métricas: hit_rate, cost_saved, false_positive_rate
- [ ] Monitorear primeras 2 semanas para tunear threshold

Relacionado: [[01-prompt-caching]], [[07-rag-eficiente]], [[10-monitoring-budget]], [[11-stack-herramientas]]
