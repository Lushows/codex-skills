# 289 · Vector DBs: pgvector vs Qdrant/Pinecone/Weaviate/Milvus

> [[21-postgres-a-fondo-pgvector]] te metió HNSW dentro de Postgres. Aquí decides cuándo eso ya no
> alcanza: el punto de quiebre es el **filtrado** y la escala, no la búsqueda vectorial pura.

## El eje real de decisión: filtrado, no recall puro
Todos hacen HNSW. La diferencia operativa es cómo combinan `WHERE` con el vecino más cercano:
- **pgvector**: el filtro es SQL normal. Sin `iterative_scan` (0.8.0), un `WHERE` selectivo provoca **overfiltering** — HNSW devuelve K candidatos, el filtro los descarta y te quedas con menos de K. Solución: `SET hnsw.iterative_scan = strict_order` o subir `ef_search`.
- **Qdrant**: **pre-filtra** vía payload indexado dentro del grafo HNSW → solo añade 1–3ms sin importar la selectividad. El mejor filtrado del mercado.
- **Pinecone serverless**: **post-filtra**, comportamiento opaco, no controlas cuántos candidatos se recuperan antes del filtro → recall impredecible con filtros agresivos.

## Números (benchmark 100M vectores, HNSW m=16, ef_construction=128) [verificado]
| Motor | p99 filtrado (15–25% selectividad) | Costo/mes @100M | Operación |
|---|---|---|---|
| Qdrant 1.10 self-hosted | **18.4ms** | ~$280 (c5.4xlarge) | tú operas |
| Pinecone serverless | 22.1ms | ~$650 (incl. queries) | gestionado, p99 consistente |
| pgvector 0.7 / PG16 | creíble **<50M** | costo de tu PG | cero infra nueva |

Lectura: a 100M Qdrant gana en filtrado y costo self-hosted; Pinecone gana en simplicidad operativa. pgvector es la opción correcta **si ya estás en Postgres y por debajo de ~50M vectores** — no añadas un sistema nuevo antes.

## HNSW: las palancas que importan
- `m` (vecinos por nodo, 16–64): más recall y memoria, build más lento. 16 es buen default.
- `ef_construction` (64–256): calidad del grafo en build. Sube si el recall en build vacío es pobre.
- `ef_search` (query-time): el knob recall↔latencia que ajustas **sin rebuild**. Empieza en 100.
- Memoria HNSW ≈ `num_vectors × (dim × 4 bytes + m × 8 bytes)`. 10M × 1536d ≈ 60GB RAM → planifica.
- **Cuantización**: scalar (int8, ~4× menos RAM, recall ~99%) o binary (~32×, recall cae, sirve de primer filtro + rerank). Qdrant/Milvus lo traen nativo; reduce el costo del nodo a la mitad.

## Cuándo cada uno
- **pgvector** — RAG mediano, ya usas Postgres, quieres `JOIN` entre vectores y datos relacionales en una query, transacciones. Hybrid search con `tsvector` + RRF en el mismo motor (ver [[21-postgres-a-fondo-pgvector]]).
- **Qdrant** — filtrado pesado por metadata (multi-tenant, permisos, fechas), self-hosted barato, cuantización agresiva. Mejor relación filtrado/costo.
- **Pinecone** — no quieres operar nada, presupuesto holgado, p99 estable importa más que el precio.
- **Weaviate** — módulos de vectorización/reranking integrados, GraphQL, búsqueda híbrida out-of-the-box.
- **Milvus** — escala a billones de vectores, GPU indexing, separación storage/compute. Overkill bajo 100M.

## Multi-tenancy (el detalle que define la arquitectura)
- pgvector: `WHERE tenant_id=?` + índice parcial o RLS. Un índice HNSW compartido → el filtro corre post-HNSW (cuidado overfiltering).
- Qdrant: payload index sobre `tenant_id` con pre-filtro → escala bien con miles de tenants en una colección. O colección por tenant si son pocos y grandes.
- Pinecone: **namespaces** (partición lógica por tenant, gratis) — la forma idiomática de aislar.

## Gotchas
1. El índice debe matchear la métrica de los embeddings (coseno vs L2 vs dot) — un índice coseno no acelera una query L2.
2. Normaliza vectores si usas dot product como proxy de coseno, o el ranking miente.
3. Rebuild de HNSW es caro y RAM-hungry: sube `maintenance_work_mem` en pgvector; en Qdrant indexa offline.
4. No metas el chunk de texto como payload gigante en el vector store — guarda solo IDs + metadata de filtro, el texto vive en Postgres/S3.

Cruza con [[72-busqueda-semantica-embeddings]] y [[307-rag-en-produccion-a-fondo]].
