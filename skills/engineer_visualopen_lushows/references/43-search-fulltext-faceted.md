# 43 — Search (full-text + faceted)

## Cuándo basta Postgres FTS
Si el corpus es < pocos millones de filas, ya vive en Postgres, y no necesitas instant-search typo-tolerant <50ms:
**`tsvector` + GIN** + **`pg_trgm`** (similitud trigram para fuzzy/`ILIKE`) cubre mucho. Patrón: columna `tsvector`
generada, `to_tsquery`/`websearch_to_tsquery`, `ts_rank` para relevancia, `pg_trgm` para typos/autocomplete. Sin
servicio extra, transaccionalmente consistente, sin pipeline de sync. Lo superas cuando necesitas typo tolerance real
multi-campo, faceting rápido con counts, sinónimos, y search-as-you-type.

## Motores dedicados
- **Meilisearch** — mejor DX, single binary, admin UI, typo tolerance + faceting on por default, **LMDB on-disk**
  (memory-mapped → el dataset puede exceder RAM). Para content/CMS/docs y prototipado. Ranking = lista ordenada de **ranking rules** (words, typo, proximity, attribute, sort, exactness).
- **Typesense** — C++, **índice entero en RAM** (necesita RAM ≥ dataset), típico **<50ms**, clustering/HA built-in, weights por campo, y **auto-embedding** (vectores internos). Ideal e-commerce / alto tráfico.
- **Elasticsearch / OpenSearch** — el más potente/flexible (aggregations, queries complejas, analytics, escala enorme) pero **mayor costo de ops** (JVM heap, sharding, cluster). Cuando también necesitas logs/analytics o escala petabyte. OpenSearch = el fork Apache-2.0.

## Indexing & relevancia
Schema de documento plano, marca **searchable** vs **filterable/facetable** vs **sortable** explícito (Meili/Typesense
exigen declarar facet/filter fields). Index en writes (outbox/CDC) o reindex batch. **Denormaliza** — no hacen joins.
Relevancia: ordena **ranking rules**, **sinónimos** (ej. "melena de león" ↔ "hericium"), stop words, weights por campo
(title > description), pin/boost. Tunea typo tolerance por largo de palabra.

## Hybrid / vector search
Los tres hacen **semantic + keyword hybrid**. **Typesense auto-embebe** (sin pipeline externo). **Meilisearch** trae
tus embeddings (OpenAI/HF) y tunea `semanticRatio`. ES/OpenSearch: kNN dense-vector + BM25 con rank fusion. Usa hybrid cuando keyword pierde paráfrasis/intención.

## Autocomplete / instant
**Prefix search** + endpoint debounced search-as-you-type; Meili/Typesense devuelven en single-digit ms (query por
keystroke). El faceted filtering devuelve **facet counts** junto a hits → "Cápsulas (12), Polvo (4)".

## Gotchas
1. **RAM de Typesense:** el índice debe caber en memoria — un catálogo grande con embeddings revienta tu RAM; dimensiona antes.
2. **Los facet fields se declaran** up-front en Meili/Typesense; olvidar = reindexar la colección entera.
3. **Drift de sync:** los motores son eventualmente consistentes con tu DB — un indexer crasheado deja resultados stale; haz reindex idempotente.
4. **pg_trgm no escala** a búsquedas fuzzy grandes como un motor dedicado — ok autocomplete, lento full fuzzy ranking.
5. Hybrid añade **latencia/costo de embedding**; cachea embeddings, corre semantic solo cuando el keyword recall es bajo.

**Fuentes:** meilisearch.com/blog (vs Typesense) · typesense.org/docs (comparison) · postgresql.org/docs (textsearch, pg_trgm).
