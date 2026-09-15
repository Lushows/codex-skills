# 07 — RAG Eficiente (60-90% reducción del contexto enviado)

**Impacto:** 60-90% reducción de tokens enviados manteniendo calidad de respuestas.
**Esfuerzo:** Medio-Alto (rediseño del pipeline RAG).
**Cuándo aplicar:** Sistemas que mandan documentos enteros / catálogos completos al LLM.
**Cuándo NO aplicar:** Datos pequeños (<5K tokens total), tareas que requieren contexto completo siempre.

## El problema con RAG mal hecho

RAG (Retrieval-Augmented Generation) en su versión naive es así:

```python
# ❌ Mal: mandar TODO al LLM
def answer_about_product(question):
    all_products = db.get_all_products()  # 200 productos × 500 tokens = 100K tokens
    return client.messages.create(
        model="claude-sonnet-4-6",
        messages=[{
            "role": "user",
            "content": f"Productos: {all_products}\n\nPregunta: {question}"
        }]
    )
# Costo: 100K × $3/1M = $0.30 POR PREGUNTA
```

```python
# ✅ Bien: RAG con vector search
def answer_about_product(question):
    relevant_chunks = vector_search(question, top_k=3)  # 3 chunks × 500 = 1.5K tokens
    return client.messages.create(
        model="claude-sonnet-4-6",
        messages=[{
            "role": "user",
            "content": f"Contexto:\n{relevant_chunks}\n\nPregunta: {question}"
        }]
    )
# Costo: 1.5K × $3/1M = $0.0045 POR PREGUNTA (99% ahorro)
```

## Componentes de un RAG eficiente

```
┌─────────────────────────────────────────────────┐
│  1. Chunking inteligente                        │
│     Dividir docs en chunks semánticamente útiles│
└─────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────┐
│  2. Embedding caching                           │
│     No re-embeddear lo mismo (cache)            │
└─────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────┐
│  3. Hybrid search (BM25 + vector)               │
│     Mejor recall que solo vectors               │
└─────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────┐
│  4. Reranking                                   │
│     Cohere/Voyage rerank top-K → mejor top-N    │
└─────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────┐
│  5. Context construction                        │
│     Solo top N chunks al LLM, sin ruido         │
└─────────────────────────────────────────────────┘
```

## 1. Chunking inteligente

### ❌ Chunking naive (fixed size)

```python
# Cortar cada 1024 tokens, ignorando contexto
chunks = [text[i:i+1024] for i in range(0, len(text), 1024)]
```

Problema: chunks pueden cortar en mitad de oraciones, perder coherencia.

### ✅ Chunking semántico

```python
# pip install langchain-text-splitters
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,           # ~800 tokens por chunk
    chunk_overlap=100,        # Overlap para preservar contexto
    separators=["\n\n", "\n", ". ", ", ", " "]  # Respeta estructura
)

chunks = splitter.split_text(document)
```

### ✅ Aún mejor: chunking por estructura

Si el doc es Markdown / HTML / PDF estructurado:

```python
from langchain_text_splitters import MarkdownHeaderTextSplitter

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
)

# Cada chunk respeta secciones lógicas del doc
chunks = splitter.split_text(markdown_doc)
```

### Tamaño óptimo de chunk

- **Muy chico (<200 tokens):** muchos chunks, mucho overhead, poco contexto
- **Muy grande (>2000 tokens):** chunks ruidosos, menos relevantes
- **Sweet spot:** 400-1000 tokens por chunk

## 2. Embedding caching

Re-embeddear el mismo texto es desperdicio. Cache.

```python
import hashlib
import redis
from typing import List

r = redis.Redis()

def get_embedding_cached(text: str, model="voyage-3") -> List[float]:
    # Hash del texto como key
    key = f"emb:{model}:{hashlib.sha256(text.encode()).hexdigest()}"

    cached = r.get(key)
    if cached:
        return json.loads(cached)

    # Cache miss: embeddear
    embedding = embed(text, model=model)

    # Cache forever (los embeddings no cambian)
    r.set(key, json.dumps(embedding))

    return embedding
```

**Ahorro:** evitar re-embeddear chunks ya procesados.

## 3. Hybrid search (BM25 + Vector)

Vector search solo a veces falla en queries con keywords específicas (códigos, nombres propios). BM25 (lexical search) + Vector = mejor recall.

```python
# pip install langchain rank_bm25
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain_community.vectorstores import Chroma

# Vector retriever
vector_retriever = Chroma(...).as_retriever(search_kwargs={"k": 10})

# BM25 retriever (keyword-based)
bm25_retriever = BM25Retriever.from_documents(documents)
bm25_retriever.k = 10

# Ensemble: combine ambos
ensemble = EnsembleRetriever(
    retrievers=[vector_retriever, bm25_retriever],
    weights=[0.6, 0.4]  # 60% vector, 40% BM25
)

results = ensemble.invoke("query about RFC-2616 standards")
```

**Cuándo BM25 ayuda:**
- Queries con acrónimos, códigos, números de versión
- Nombres propios poco comunes
- Términos técnicos específicos

## 4. Reranking (paso clave que muchos saltan)

Después de retrieval (top 20-50 chunks), un reranker reordena por relevancia real:

```python
import cohere

co = cohere.Client(api_key="...")

# Tras vector + BM25 search obtenés 30 candidatos
candidates = ensemble_retriever.invoke(query)  # 30 chunks

# Rerank con Cohere
reranked = co.rerank(
    query=query,
    documents=[c.page_content for c in candidates],
    top_n=5,  # Quedarse con los top 5 reales
    model="rerank-multilingual-v3.0"  # Soporta español
)

# top_n chunks ordenados por relevancia REAL
final_chunks = [candidates[r.index] for r in reranked.results]
```

**Alternativa:** Voyage Rerank-2 (más reciente, 2026, mejor calidad/precio).

**Por qué reranking importa:**
- Vector search a veces trae "false positives" (similar pero no relevante)
- Reranker es un modelo dedicado a RELEVANCIA, no a similitud
- Calidad up 20-30% típicamente

**Costo:** ~$0.001 por 1K búsquedas. Despreciable vs ahorro de mandar mejores chunks al LLM.

## 5. Embeddings cuantizados (4x menos storage)

Embeddings normales son float32 (4 bytes/dim). Cuantizar a int8 (1 byte/dim) = 4x menos storage:

```python
# Voyage AI soporta cuantización
embeddings = voyage_client.embed(
    texts=[...],
    model="voyage-3",
    output_dtype="int8"  # ← 4x menos espacio, casi misma calidad
)
```

**Cuándo usar:** vector DB con millones de embeddings (Pinecone, Weaviate). Para <100K, no vale la pena complicarse.

## 6. Cuándo SÍ usar RAG vs. NO

### ✅ RAG es ideal para:

| Caso | Ejemplo |
|---|---|
| Knowledge base grande | Documentación técnica, FAQs extensas |
| Datos actualizables | Catálogo de productos cambiante |
| Multi-tenant con data por cliente | SaaS donde cada tenant tiene sus docs |
| Compliance + auditoría | Citar fuente exacta requerida |

### ❌ RAG NO sirve para:

| Caso | Por qué |
|---|---|
| Datos pequeños (<5K tokens total) | Mandalos directo, no vale el setup |
| Razonamiento sobre TODO el dataset | RAG retrieva subset, perdés visión global |
| Generación creativa | No hay que retrievar nada |
| Conversación pura | No hay knowledge base |

### Alternativa cuando dataset entero <100K tokens: fine-tuning

Si tu dataset es pequeño pero estable, fine-tunear puede ser más eficiente que RAG. OpenAI permite fine-tune de GPT-4o-mini ($25/1M training tokens). Anthropic no ofrece fine-tuning público (al menos hasta 2026).

## Patrón completo end-to-end

```python
class ProductionRAG:
    def __init__(self, tenant_id):
        self.vector_store = ChromaDB(collection=f"docs_{tenant_id}")
        self.bm25 = self._load_bm25(tenant_id)
        self.reranker = cohere.Client(...)

    def query(self, question: str, top_n: int = 3) -> str:
        # 1. Hybrid retrieval (vector + BM25)
        vector_results = self.vector_store.similarity_search(question, k=15)
        bm25_results = self.bm25.get_relevant_documents(question)[:15]

        # 2. Merge sin duplicados
        all_candidates = self._dedupe(vector_results + bm25_results)

        # 3. Rerank
        reranked = self.reranker.rerank(
            query=question,
            documents=[c.page_content for c in all_candidates],
            top_n=top_n
        )
        final_chunks = [all_candidates[r.index] for r in reranked.results]

        # 4. Clean chunks (eliminar boilerplate)
        cleaned = [self._clean_chunk(c.page_content) for c in final_chunks]

        # 5. Construir context para LLM
        context = "\n\n---\n\n".join(cleaned)

        # 6. Llamar LLM con context comprimido
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=SYSTEM_RAG,  # Cacheado con módulo 01
            messages=[{
                "role": "user",
                "content": f"""Contexto:
{context}

Pregunta del usuario:
{question}

Responde basándote SOLO en el contexto. Si no está en el contexto, decí "No tengo info sobre eso"."""
            }],
            cache_control={"type": "ephemeral"}
        )

        return response.content[0].text

    def _clean_chunk(self, chunk: str) -> str:
        # Eliminar headers/footers, líneas vacías, etc.
        chunk = re.sub(r'\n{3,}', '\n\n', chunk)
        return chunk.strip()

    def _dedupe(self, chunks):
        seen = set()
        unique = []
        for c in chunks:
            content_hash = hashlib.md5(c.page_content.encode()).hexdigest()
            if content_hash not in seen:
                seen.add(content_hash)
                unique.append(c)
        return unique
```

## Casos del usuario

### BIO-SETA
- Catálogo de productos + FAQs + info de envíos
- **Aplicar RAG:**
  - Indexar productos con sus descripciones (1 chunk/producto)
  - Indexar FAQs (1 chunk/FAQ)
  - Search hybrid + rerank → top 3-5 chunks al LLM
- **Ahorro:** de mandar todo el catálogo (~50K tokens) a 1.5K relevantes = 97% menos

### AGENTE STUDIO
- Brand guidelines + assets pasados + competidores scrapeados
- **Aplicar RAG:**
  - Indexar brand guidelines por sección
  - Indexar past creatives por categoría
  - Query relevante → solo chunks alineados
- **Ahorro:** 60% en pipelines de generación

### AGENTE TRADING
- Histórico de análisis + reportes de empresas + news
- **Aplicar RAG:**
  - Indexar reportes por ticker + fecha
  - Search por ticker + temporal filter
- **Ahorro:** 70% al evitar mandar histórico completo

### SaaS XPRIZE (multi-tenant)
- Catálogo proveedores del tenant + sus categorías custom + historial facturas
- **Aplicar RAG:**
  - Index por tenant (`docs_{tenant_id}`)
  - Cuando llega factura → retrievar proveedores similares + categorías relevantes
- **Ahorro:** 80% al evitar mandar todo el catálogo del tenant cada vez

## Stack tecnológico

| Componente | Opciones |
|---|---|
| **Vector store** | Chroma (local), Pinecone (managed), Weaviate, Qdrant, pgvector |
| **Embeddings** | Voyage AI (voyage-3, mejor para retrieval), OpenAI text-embedding-3, Cohere embed |
| **Reranker** | Cohere Rerank-3, Voyage Rerank-2 (mejor 2026) |
| **Chunking** | LangChain RecursiveCharacterTextSplitter, Unstructured.io |
| **Framework** | LangChain, LlamaIndex (más feature-rich para RAG) |

## Checklist

- [ ] Chunking semántico (no fixed-size)
- [ ] Chunks de 400-1000 tokens, con overlap
- [ ] Embeddings cacheados (no re-embeddear lo mismo)
- [ ] Hybrid search: vector + BM25
- [ ] Reranker después de retrieval (Cohere o Voyage)
- [ ] Top N final pequeño (3-5 chunks, no 50)
- [ ] Clean chunks antes de enviar (eliminar boilerplate)
- [ ] System prompt RAG cacheado (módulo 01)
- [ ] Multi-tenant: namespace por tenant
- [ ] Evaluar: comparar respuesta con dataset completo vs RAG (sample)
- [ ] Medir ahorro de tokens vs baseline naive

Relacionado: [[01-prompt-caching]], [[05-semantic-caching]], [[06-prompt-compression]], [[11-stack-herramientas]]
