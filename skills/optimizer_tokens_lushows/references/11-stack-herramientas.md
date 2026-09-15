# 11 — Stack de herramientas para optimización LLM 2026

Catálogo curado de SDKs, gateways, frameworks y servicios. Carga este módulo cuando necesités recomendar UNA herramienta específica para un caso del usuario.

## SDKs oficiales (siempre la primera opción)

| SDK | Para | Install | Cuándo usar |
|---|---|---|---|
| **Anthropic SDK** (Python) | Claude API directo | `pip install anthropic` | Default para Anthropic |
| **Anthropic SDK** (TypeScript) | Claude API directo | `npm install @anthropic-ai/sdk` | Default Node.js |
| **OpenAI SDK** (Python) | GPT direct | `pip install openai` | Default OpenAI |
| **OpenAI SDK** (TypeScript) | GPT direct | `npm install openai` | Default Node.js |
| **Google GenAI SDK** | Gemini | `pip install google-genai` | Default Gemini |

**Regla:** usar SDK oficial sobre wrappers/abstracciones por defecto. Solo agregar abstracciones si justifican el overhead.

## AI Gateways (abstracción multi-provider)

Para routing entre proveedores, caching, fallback, observability — capa unificada.

| Gateway | Pro | Con | Cuándo usar |
|---|---|---|---|
| **Vercel AI Gateway** | Si ya usás Vercel, integración nativa, free tier generoso | Solo si tu app es Vercel | Stack Next.js / Vercel |
| **Portkey** | Open source (desde marzo 2026), feature-complete, semantic caching built-in, guardrails | Vendor lock-in para features avanzadas | Producción seria, equipos pequeños sin ops |
| **Helicone** | Cost observability líder, proxy simple, free tier | Menos features de routing avanzado | Foco en cost tracking |
| **LiteLLM** | Open source, 100+ providers, control total | Hay que mantener infra | Equipos con DevOps, multi-provider |
| **Cloudflare AI Gateway** | Edge caching, near-zero setup | Menos features de governance | Apps en edge / Cloudflare Workers |
| **OpenRouter** | Acceso unificado a 100+ modelos por una sola API key | Pricing markup pequeño | Experimentar / app que necesita acceso a muchos modelos |

### Setup ejemplos

**Vercel AI Gateway (recomendado si stack Vercel):**
```typescript
import { generateText } from 'ai';
import { vercel } from '@ai-sdk/vercel';

const { text } = await generateText({
  model: vercel('anthropic/claude-sonnet-4-6'),
  prompt: 'Hello'
});
```

**Portkey:**
```python
from portkey_ai import Portkey

portkey = Portkey(
    api_key="PORTKEY_KEY",
    config={
        "strategy": {"mode": "fallback"},
        "targets": [
            {"provider": "anthropic", "model": "claude-sonnet-4-6"},
            {"provider": "openai", "model": "gpt-5-mini"}  # fallback
        ],
        "cache": {"mode": "semantic", "max_age": 3600}
    }
)

response = portkey.chat.completions.create(messages=[...])
```

**Helicone:**
```python
client = Anthropic(
    api_key=ANTHROPIC_KEY,
    base_url="https://anthropic.helicone.ai",
    default_headers={"Helicone-Auth": f"Bearer {HELICONE_KEY}"}
)
# Todo se trackea automático en dashboard Helicone
```

## Frameworks de aplicaciones AI

| Framework | Especialidad | Cuándo usar |
|---|---|---|
| **Vercel AI SDK** | Streaming UI, React, structured generations | Apps Next.js/React |
| **LangChain** | RAG, chains, agents, integraciones masivas | Prototipos, sistemas complejos |
| **LlamaIndex** | RAG production-grade, document processing | RAG es el core de tu app |
| **Haystack** | NLP pipelines, enterprise | Casos enterprise con NLP avanzado |
| **DSPy** | Optimización automática de prompts | Investigación, research |
| **Mastra** (TypeScript) | Agentes TypeScript, workflows | Stack Node.js, agentes |

**Recomendación honesta 2026:**
- **Apps web React/Next:** Vercel AI SDK (light, sin overhead)
- **RAG complejo:** LlamaIndex (más feature-rich que LangChain para RAG)
- **Agentes complejos:** Anthropic SDK directo + tool runner (menos abstracción)
- **NO usar LangChain** para nuevos proyectos a menos que hayas validado que necesitás sus integrations específicas (overhead alto, debugging complejo)

## Caching tools

### Prompt caching (provider-native)
| Provider | Cómo activar | Discount |
|---|---|---|
| Anthropic | `cache_control: ephemeral` | 90% off cache reads |
| OpenAI | Automático para prefix >1024 tokens | 50% off cache hits |
| Gemini | `client.caches.create()` manual | ~75% off + storage cost |

### Semantic caching
| Tool | Setup | Pricing |
|---|---|---|
| **Redis VL** | Self-hosted, librería `redisvl` | Solo infra Redis |
| **Portkey semantic cache** | Built into gateway | Por uso del gateway |
| **Helicone cache** | Plug & play via proxy | Free tier |
| **pgvector** | Postgres + extension | Solo infra Postgres |

## Compression tools

| Tool | Para | Repo / Install |
|---|---|---|
| **LLMLingua-2** (Microsoft) | Comprimir prompts hasta 5x | `pip install llmlingua` |
| **LongLLMLingua** | Específico para contextos muy largos | Mismo paquete |
| **Selective Context** (Microsoft) | Otra técnica de compresión | GitHub |

## RAG tools

### Vector databases
| DB | Pro | Con | Pricing |
|---|---|---|---|
| **Chroma** | Local-first, fácil para dev | No scale prod | Free open source |
| **Pinecone** | Production-grade, managed | $$$ | Pago por uso |
| **Weaviate** | Open source + cloud, hybrid search | Setup más complejo | Free OSS / cloud pagos |
| **Qdrant** | Open source, performant | Comunidad menor | Free OSS / cloud pagos |
| **pgvector** | Postgres extension | Menos features avanzadas | Solo infra Postgres |
| **Vespa** | Enterprise scale | Overkill para casi todo | Free OSS |
| **Turbopuffer** | Serverless, barato a escala | Newer (2024+) | $/uso |

### Embeddings
| Model | Pro | Pricing |
|---|---|---|
| **Voyage AI** (voyage-3) | Mejor calidad retrieval 2026 | $0.12/1M tokens |
| **OpenAI text-embedding-3-large** | Standard, alta calidad | $0.13/1M |
| **OpenAI text-embedding-3-small** | Más barato, calidad ok | $0.02/1M |
| **Cohere embed-v3** | Multilingual fuerte | $0.10/1M |
| **HuggingFace BGE** | Open source, self-hosted | Free |

### Rerankers
| Model | Pro | Pricing |
|---|---|---|
| **Cohere Rerank 3** | Líder calidad, multilingual | $1/1K búsquedas |
| **Voyage Rerank-2** | 2026, mejor calidad/precio | $0.05/1K búsquedas |
| **HuggingFace cross-encoders** | Open source | Free |

## Observability y cost tracking

| Tool | Pro | Pricing |
|---|---|---|
| **Helicone** | Cost tracking líder, semantic caching, dashboard | Free hasta 100K req |
| **Langfuse** | Tracing rico, self-hostable, open source | Free OSS / cloud pagos |
| **Portkey** | Gateway + observability + budget alerts | Por uso |
| **PostHog LLM Analytics** | Si ya usás PostHog | Incluído PostHog |
| **Datadog LLM Observability** | Enterprise, integración con APM | $$$ |
| **Arize Phoenix** | Open source, evals + traces | Free OSS |

## Evaluation tools

| Tool | Para | Pricing |
|---|---|---|
| **Anthropic console evals** | Evaluar Claude prompts | Free (con Anthropic) |
| **OpenAI Evals** | Eval framework para GPT | Free OSS |
| **Promptfoo** | A/B test prompts | Free OSS |
| **Braintrust** | Eval workflows production | Pago |
| **LangSmith** (LangChain) | Si usás LangChain | Pago |

## Stack recomendado por escenario

### Escenario A: Startup MVP (cero infra, max velocidad)
```
Vercel AI SDK (frontend) +
Anthropic SDK (backend) +
Helicone (cost tracking, free) +
Anthropic prompt caching (90% descuento)
```

### Escenario B: SaaS multi-tenant production
```
Anthropic SDK direct +
Portkey (gateway con fallback OpenAI) +
Langfuse self-hosted (tracing + cost) +
pgvector (si ya tenés Postgres) o Pinecone +
Voyage AI embeddings +
Cohere Rerank
```

### Escenario C: Enterprise con compliance
```
Anthropic SDK +
LiteLLM self-hosted (control total routing) +
Datadog LLM Observability +
Self-hosted Weaviate (data sovereignty) +
Internal embedding model (privacy)
```

### Escenario D: App Next.js / Vercel
```
Vercel AI SDK +
Vercel AI Gateway (routing nativo) +
PostHog LLM Analytics (si ya usás PostHog) +
Vercel KV o Upstash Redis para semantic cache
```

## Costos comparados (referencia 2026)

### Caso: 10K requests/día, prompt 2K tokens, output 500 tokens

| Approach | Costo mensual estimado |
|---|---|
| Naive (Opus, sin cache) | $1,350 |
| Sonnet routing | $675 |
| + Prompt caching | $200 |
| + Batch (50% del tráfico) | $130 |
| + Compression (30%) | $90 |
| + Semantic cache (40% hits) | $55 |

**Stack completo:** 96% ahorro vs naive. Tooling propio ~$50/mes (Helicone, etc).
**ROI:** $1,295 ahorrado vs $50 tooling = 25x.

## Casos del usuario

### BIO-SETA
**Stack recomendado:**
- Anthropic SDK directo (Node.js)
- Helicone (cost tracking, gratis)
- Anthropic prompt caching activo
- Redis (semantic cache para FAQs)
- Sin gateway complicado (overkill para MVP)

### AGENTE STUDIO
**Stack recomendado:**
- Anthropic + OpenAI (multi-provider para imagen/video)
- Portkey o Vercel AI Gateway (routing inteligente)
- Helicone o Langfuse (tracing complejo, multi-step)
- Voyage AI embeddings para semantic search de assets
- Si volumen alto: Cloudflare AI Gateway para edge caching

### AGENTE TRADING
**Stack recomendado:**
- Anthropic SDK (Opus 4.8 para análisis crítico)
- Langfuse (tracing detallado, decisiones de trading deben ser auditables)
- pgvector si ya hay Postgres (no agregar Redis)
- Sin RAG complejo, datos estructurados (no vectorizar)

### SaaS XPRIZE
**Stack recomendado:**
- Anthropic SDK (Gemini para vision si OCR)
- Vercel AI Gateway (si frontend Next.js)
- Langfuse self-hosted (multi-tenant tracing, control de data)
- pgvector multi-tenant (1 collection per tenant_id)
- Voyage AI embeddings
- Cohere Rerank
- Stripe + budget enforcer custom

## Anti-patterns

❌ **Adoptar LangChain "por default"** — overhead alto, debugging difícil. Evaluar si realmente lo necesitás.
❌ **Pinecone para 1K embeddings** — overkill, usá Chroma o pgvector.
❌ **Custom gateway desde cero** — Helicone/Portkey ya lo resolvieron, no reinventes.
❌ **No medir nada** — sin observability volás a ciegas.
❌ **Vendor lock-in en provider** — usá gateway para poder cambiar de Anthropic a OpenAI sin refactor.

## Checklist al elegir stack

- [ ] ¿SDK oficial del provider o framework abstracto? (defaultear a SDK oficial)
- [ ] ¿Necesitás multi-provider routing? → Gateway
- [ ] ¿Necesitás observability seria? → Helicone/Langfuse/Portkey
- [ ] ¿Necesitás RAG? → LlamaIndex + vector DB + embeddings + reranker
- [ ] ¿Vas a crecer >10K req/día? → considerar caching agresivo (Portkey/Helicone)
- [ ] ¿Datos sensibles? → self-hosted (Langfuse, LiteLLM)
- [ ] Define cost dashboard ANTES de elegir stack

Relacionado: [[00-fundamentos-optimizacion]], [[10-monitoring-budget]], [[01-prompt-caching]], [[07-rag-eficiente]]
