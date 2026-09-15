# 307 · RAG en producción a fondo (ingest, hybrid+rerank, citaciones, freshness, eval)

> Un RAG de demo recupera y responde. Un RAG de producción **ingiere a escala, cita la fuente,
> sabe cuándo el dato está viejo y se mide en cada deploy**. El cuello sigue siendo retrieval.

[[31-rag-a-fondo]] cubre el pipeline canónico y la teoría. Aquí va lo que rompe cuando hay
tráfico real, documentos que cambian y un SLA que cumplir.

## Ingest a escala (la mitad del trabajo, el 0% del glamour)
- **Idempotencia por content-hash**: hashea cada doc (sha256 del texto normalizado). Si el hash no
  cambió, no re-embebes → ahorras coste y evitas duplicar vectores. Guarda `doc_id`, `version`, `hash`.
- **Incremental, no full-reindex**: upsert por `doc_id`; borra los chunks huérfanos de la versión vieja
  (delete-by-filter `doc_id == X AND version < N`). Re-indexar todo cada noche no escala a millones.
- **Parsing robusto**: `docling`/`unstructured` para layout y tablas; VLM (Qwen3-VL) como OCR para PDFs
  escaneados. Falla suave: si un PDF revienta, encolar a una DLQ, no tirar el batch entero.
- **Metadata como ciudadano de primera**: `source_url`, `title`, `section`, `updated_at`, `acl`/`tenant`.
  Sin esto no hay citaciones, ni filtrado por permisos, ni freshness.

## Contextual retrieval (Anthropic, sube recall ~35-50%)
Antes de embeber, antepón a cada chunk 1-2 frases de contexto generadas por un LLM barato (Haiku):
"Este fragmento pertenece al informe Q3 de ACME sobre churn...". Resuelve la pérdida de referencias
("la empresa", "ese trimestre") igual que late-chunking, pero compatible con cualquier embedder.
Combínalo con **contextual BM25** (el sparse también indexa el contexto). Cachea el prompt del doc
entero (prompt caching) para que generar el contexto de N chunks no cueste N lecturas del documento.

## Hybrid + rerank en serio
| Capa | Trae | Coste |
|---|---|---|
| Dense (HNSW) | semántica, paráfrasis | medio |
| BM25/sparse | SKUs, nombres, códigos exactos | bajo |
| RRF (k=60) | fusiona ambos sin normalizar scores | ~0 |
| Cross-encoder rerank | precision en top-k | alto (latencia) |

Regla: recupera **alto k** (50-100) en hybrid, rerankea a 5-8. El reranker no rescata lo que nunca
entró. `cohere rerank-3.5` o `bge-reranker-v2-m3` self-host. Filtra ACL/tenant **antes** del rerank,
no después (no pagues reranking de chunks que el usuario no puede ver).

## Citaciones que no alucinan
- Devuelve `[source_url#section]` por chunk y obliga al LLM a citar el `chunk_id` que usó.
- **Verifica la cita**: tras generar, comprueba que cada claim mapea a un chunk recuperado (es un mini
  faithfulness check, ver [[310-evals-llm-apps]]). Si una frase no tiene soporte, márcala o recórtala.
- Cita a nivel de span, no de documento entero: el usuario debe poder saltar a la línea exacta.

## Freshness (el dato viejo es peor que no responder)
- `updated_at` en metadata + **decay temporal** en el ranking: penaliza chunks antiguos cuando la query
  es time-sensitive ("precio actual", "última versión"). RRF con un tercer score de recencia.
- **TTL e invalidación**: docs con caducidad (precios, stock) se re-ingieren por webhook del sistema
  origen, no por cron. Si la fuente cae, sirve con un flag `stale: true` en vez de mentir.
- Responde "no tengo dato posterior a {fecha}" cuando el corpus no cubre el periodo pedido.

## Evaluación continua (sin esto, optimizas a ciegas)
- **RAGAS** como panel de 4: faithfulness (umbral ~0.75), answer-relevance, context-precision (~0.7),
  context-recall. **Léelas juntas**: puedes inflar precision devolviendo menos chunks, pero hundes
  recall. Sepáralo en fallo-de-retrieval vs fallo-de-generación.
- **Golden set** versionado (50-200 query→respuesta esperada) en CI: cada cambio de chunker/embedder/k
  corre el set y bloquea el merge si baja una métrica. RAGAS, DeepEval o Promptfoo.
- **Online eval**: traza cada request (Langfuse/LangSmith), muestrea las de score bajo e inspecciona
  qué se recuperó. El feedback de usuario (👍/👎) alimenta el golden set.

## Gotchas de producción
1. **Cambiar de embedder = reindexar todo**: no son compatibles entre modelos. Planéalo como migración.
2. **Multi-tenant sin filtro de ACL en el retrieval = fuga de datos** entre clientes. Filtra en la query.
3. **Rerank caro en el camino caliente**: cachea (query,docset)→orden; o saltea rerank si hybrid ya es nítido.
4. **El golden set se pudre**: revísalo cuando el corpus cambie de dominio, o medirás contra el pasado.

Cruza con [[31-rag-a-fondo]], [[289-vector-dbs-qdrant-pinecone]], [[310-evals-llm-apps]] y [[309-memoria-contexto-agentes]].
