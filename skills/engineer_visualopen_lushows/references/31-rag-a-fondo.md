# RAG a Fondo: Pipeline, Embeddings, Vector Stores, Hybrid Search y Evaluación (2026)

Retrieval-Augmented Generation (RAG) inyecta contexto recuperado en el prompt para que el LLM responda con datos frescos/propietarios sin reentrenar. La máxima operativa de 2026: **"the bottleneck is retrieval, not generation"** — los LLMs ya razonan bien; lo que falla es traerles el chunk correcto. Optimizar retrieval (no el prompt de generación) es donde está el 80% del ROI.

## El pipeline canónico

```
ingest → chunk → embed → store → retrieve → rerank → generate
```

1. **Ingest**: parsear PDFs/HTML/Office. Herramientas 2026: `unstructured` (>=0.16), `docling` (IBM, excelente para tablas/layout), `LlamaParse`. Para PDFs complejos, usa un VLM (Qwen3-VL) como OCR de layout.
2. **Chunk**: dividir en unidades indexables (ver abajo).
3. **Embed**: vectorizar cada chunk.
4. **Store**: vector DB + índice ANN (HNSW/IVF).
5. **Retrieve**: top-k por similitud (dense) y/o BM25 (sparse).
6. **Rerank**: cross-encoder reordena los candidatos.
7. **Generate**: el LLM responde citando los chunks.

## Estrategias de chunking

- **Fixed-size**: N tokens con `overlap` (10-20%). Simple, rompe semántica. Baseline.
- **Recursive** (`RecursiveCharacterTextSplitter` de LangChain): corta por jerarquía de separadores (`\n\n` → `\n` → `. ` → ` `). Default sensato. 512-1024 tokens, overlap 50-100.
- **Semantic** (`SemanticChunker`): corta donde la distancia coseno entre frases adyacentes supera un umbral. Mejor coherencia, más caro de indexar.
- **By-structure**: respeta headers Markdown, secciones, filas de tabla. Ideal para docs técnicos (`MarkdownHeaderTextSplitter`).
- **Late chunking** (Jina, 2024-2026): embebes el documento ENTERO con un modelo long-context y *después* haces pooling por chunk. Cada chunk hereda contexto global → resuelve la pérdida de referencias ("la empresa" sin nombre). Requiere embedder long-context (jina-v3, 8192 tokens).

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = splitter.split_text(doc)
```

## Modelos de embedding 2026 (dims / coste por 1M tokens)

| Modelo | Dims | Coste/1M | Notas |
|---|---|---|---|
| OpenAI `text-embedding-3-small` | 1536 (Matryoshka↓256) | $0.02 | barato, default cómodo |
| OpenAI `text-embedding-3-large` | 3072 (↓256) | $0.13 | Matryoshka: truncar dims sin reentrenar |
| Cohere `embed-v4` | hasta 1536 | ~$0.01 | multilingüe 100+ idiomas, líder MTEB multilingüe |
| Voyage `voyage-3-large` | 1024-2048 | $0.18 | premium; +4 MTEB en código; contexto 32k |
| `BGE-M3` (open) | 1024 | self-host | dense+sparse+ColBERT en un modelo |
| `jina-embeddings-v3` | 1024 | $0.02 | 8192 ctx, soporta late chunking |
| Nomic `nomic-embed-text-v1.5` | 768 (Matryoshka) | self-host | open, Apache 2.0 |
| `gte-Qwen2-7B-instruct` | 3584 | self-host | top MTEB pero pesado |

**Matryoshka**: text-embedding-3 y Nomic permiten truncar el vector (3072→256) con pérdida mínima → menos almacenamiento/latencia ANN.

## Vector stores

- **pgvector** (Postgres + extensión): si ya tienes Postgres, empieza aquí. Soporta HNSW desde 0.5; en 2026 con `pgvectorscale` (StreamingDiskANN) escala a >100M vectores. Hybrid con `tsvector` nativo.
- **Qdrant**: Rust, rápido, payload filtering excelente, hybrid nativo. Recomendado para nuevos proyectos puros de retrieval.
- **Weaviate / Milvus**: más features (multi-tenancy, GraphQL/Milvus a escala masiva), más ops.
- **Chroma / LanceDB**: embebidos, ideales para prototipo o single-node. LanceDB usa formato columnar Lance (sobre disco, no todo en RAM).

## Hybrid search + RRF

Dense capta semántica; **BM25** (sparse) capta términos exactos (nombres, SKUs, códigos). Combínalos con **Reciprocal Rank Fusion**: `score(d) = Σ 1/(k + rank_i(d))`, k=60 típico. No requiere normalizar scores entre sistemas.

## Rerankers (precision > recall en top-k)

El retrieval trae 50-100 candidatos; el reranker (cross-encoder) reordena y te quedas con top 5-8. Solo ayuda si **recall ya es alto**: ningún reranker rescata un chunk que nunca entró a la lista.
- **Cohere `rerank-3.5`**: default más fuerte, multilingüe, baja latencia. Flojea en queries de identificadores (nombres de función).
- **`bge-reranker-v2-m3`** (open): baseline sólido self-host.
- **ColBERT / late interaction**: embedding por token + MaxSim. Alta calidad pero infra compleja; nicho en 2026.

## Query transformation

- **HyDE**: el LLM genera una respuesta hipotética y embebes *eso* (más cercano a los docs que la pregunta).
- **Multi-query**: generas N reformulaciones, unes resultados.
- **Decomposition**: divides preguntas multi-hop en sub-preguntas.

## Context stuffing vs precisión

Meter 50 chunks en una ventana de 1M tokens degrada por **"lost in the middle"** y dispara coste/latencia. Mejor 5 chunks precisos que 50 ruidosos.

## Evaluación — RAGAS

`ragas` mide sin ground-truth manual: **faithfulness** (la respuesta se apoya en el contexto, anti-alucinación), **answer relevance**, **context precision** (¿el chunk relevante está arriba?) y **context recall** (¿se recuperó todo lo necesario?). Separa fallos de retrieval vs generación.

## Agentic / Graph RAG 2026

- **Agentic RAG**: un agente decide *si* buscar, *qué* índice usar y *re-busca* tras evaluar resultados (LangGraph).
- **GraphRAG** (Microsoft): construye un knowledge graph + resúmenes de comunidad; gana en preguntas globales ("temas principales del corpus") donde el RAG de similitud falla.

## Gotchas

1. **Embedder y reranker deben coincidir en idioma/dominio**: un embedder inglés sobre corpus español destruye recall — usa Cohere embed-v4 o BGE-M3 multilingüe.
2. **El overlap no es gratis**: 20% de overlap = 20% más vectores y coste; demasiado infla el índice sin mejorar recall.
3. **Reranker con bajo recall es inútil**: arregla retrieval (hybrid + más k) ANTES de añadir reranker.
4. **No reuses embeddings entre versiones de modelo**: text-embedding-3 NO es compatible con ada-002; cambiar de modelo = reindexar todo.
5. **Mide con RAGAS antes y después de cada cambio**: "mejorar el prompt" sin medir context-precision es optimizar a ciegas.

## Fuentes
- [Embedding model specs 2026 (PE Collective)](https://pecollective.com/tools/text-embedding-models-compared/)
- [Text embedding models comparison (TokenMix)](https://tokenmix.ai/blog/text-embedding-models-comparison)
- [Reranking & cross-encoders for RAG 2026 (Local AI Master)](https://localaimaster.com/blog/reranking-cross-encoders-guide)
- [Evaluating Cohere Rerank in RAG 2026 (Future AGI)](https://futureagi.com/blog/evaluating-cohere-rerank-rag-2026/)
- [RAGAS docs](https://docs.ragas.io/)
- [Jina late chunking](https://jina.ai/news/late-chunking-in-long-context-embedding-models/)
