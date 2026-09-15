# 56 — RAG agéntico y GraphRAG (avanzado)

Más allá del "embed → top-k → stuff": el RAG de producción 2026 es **agéntico** — el LLM decide *si*, *qué* y
*cuántas veces* recuperar, y se auto-corrige.

## Patrones agénticos
- **Self-RAG** — el modelo emite reflection tokens decidiendo recuperar y gradúa relevancia/soporte.
- **Corrective RAG / CRAG** — un evaluador ligero puntúa chunks Correct/Ambiguous/Incorrect; en fallo dispara query rewrite + fallback a web.
Impleméntalos como **state machine, no chain** — **LangGraph** es el de-facto (nodos `retrieve→grade→generate→reflect`,
edges condicionales que loopean en grade bajo). LlamaIndex (`AgentWorkflow`, `CorrectiveRAGPack`), Haystack 2.x (Pipeline branching).

## GraphRAG (Microsoft, `pip install graphrag` v1.0+)
Cambia recall vectorial por *razonamiento global*. Indexing: LLM extrae entidades+relaciones → grafo →
comunidades Leiden jerárquicas → un LLM escribe un **community report** por cluster. Query modes: **Global Search**
(map-reduce sobre summaries — responde "¿cuáles son los temas?" que el RAG vectorial NO puede), **Local Search**
(vecindario de entidad), **DRIFT** (local+comunidad), **Basic** (vector fallback). **GraphRAG gana en síntesis
corpus-wide/multi-hop/"conectar puntos"; pierde en factoid simple y cuesta mucho más indexar.** **LazyGraphRAG**
difiere summarization a query-time (~0.1% del costo) — úsalo en corpus grande con queries impredecibles.
```bash
graphrag init --root ./ragproj && graphrag index --root ./ragproj
graphrag query --root ./ragproj --method global --query "temas recurrentes de fallo en los reportes?"
```

## Otras técnicas
- **Query routing:** clasificador barato (o el agente) rutea a SQL/vector/grafo/web (LlamaIndex `RouterQueryEngine`).
- **Multi-hop:** decompose-then-retrieve (sub-queries, retrieve por hop, acumula evidencia).
- **Contextual Retrieval (Anthropic):** prepende 50-100 tokens de contexto LLM a cada chunk ANTES de embeddear Y de
  BM25 → -49% fallos de retrieval; **+ reranking → -67%**. Genera los blurbs barato con prompt caching.
- **Late chunking (Jina):** embeddea el doc COMPLETO con un embedder long-context, luego poolea por chunk → contexto global sin LLM extra.
- **Reranker** (Cohere Rerank 3.5 / Jina-v2 / BGE-v2-m3) sobre candidatos amplios (recupera 50-150, rerank a 5-20).
- **Long-context vs RAG:** con 200K-1M tokens, stuffear gana en docs <~200K (accuracy/simplicidad); RAG gana en costo/latencia/freshness/citación. **Híbrido:** RAG hace shortlist, long-context razona sobre ella.

## Eval
RAGAS (faithfulness, answer-relevance, context-precision/recall) + TruLens; para agéntico mide también
*retrieval-decision accuracy*, *tool-call correctness*, task success — las métricas de componente esconden fallos en cascada.

## Gotchas
1. **El indexing de GraphRAG explota en costo** (O(chunks) LLM calls) — usa LazyGraphRAG o modelo de extracción barato.
2. **Loops agénticos corren para siempre** — capa iteraciones (max 3) + nodo terminal "ríndete y responde con lo que tienes".
3. **Los blurbs contextuales van en AMBOS índices** (embedding Y BM25) — en solo uno pierdes la mitad de la ganancia.
4. **Context window del reranker es chico** — chunks de 8K se truncan; rerank sobre pasajes enfocados.
5. **Los routers hardcoded se pudren** al crecer el corpus — loguea decisiones y reevalúa, o deja que el agente rutee con self-correction.
6. **Evalúa retriever y generator por separado** — una respuesta perfecta sobre contexto malo pasa el eval end-to-end naive.

**Fuentes:** github.com/microsoft/graphrag · anthropic.com/news/contextual-retrieval · langchain-ai.github.io/langgraph.
