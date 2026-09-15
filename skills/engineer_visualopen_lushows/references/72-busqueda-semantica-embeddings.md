# 72 — Búsqueda semántica & embeddings a fondo

## Modelos de embedding 2026
En MTEB multilingüe lidera **Qwen3-Embedding-8B** (~70.6, open, contexto 32K, #1 también en MTEB-Code); la familia
incluye 0.6B/4B/8B. En inglés lidera **Gemini Embedding 001** (~68.3, API). Para español: Qwen3 y
`multilingual-e5-large` rinden bien; ligeros open: `bge-m3` (denso/sparse/multivector), Jina v5. La mayoría soporta
**Matryoshka (MRL):** truncar el vector (1024→256 dims) cortando la cola y re-normalizando, perdiendo poca calidad.

## Vector DB a escala
**HNSW** (grafo): `M` (vecinos/nodo 16-64; más = mejor recall, más RAM), `ef_construction` (build), `ef_search`
(esfuerzo en query; sube recall a costa de latencia). **IVF** (clustering): `nlist`, `nprobe`. HNSW gana en recall/
latencia; IVF usa menos RAM en build. **Cuantización** (escala billones): scalar (f32→int8, ~4× menos RAM), product
(PQ, compresión fuerte), binary (1 bit/dim, ~32×, con reranking de candidatos sobre full). Sharding + réplicas para QPS.

## Hybrid search
Denso (semántico) + sparse/BM25 (léxico), fusiona con **RRF**: `score = Σ 1/(k + rank_i)`, k≈60. Captura sinónimos Y términos exactos (SKUs, nombres propios).

## pgvector / Qdrant
pgvector (v0.8.0): `vector`, `halfvec` (2 bytes, ~50% menos storage), `bit` (binario):
```sql
CREATE TABLE docs (id int, emb halfvec(1024));
CREATE INDEX ON docs USING hnsw (emb halfvec_cosine_ops) WITH (m=16, ef_construction=64);
SET hnsw.ef_search = 100;
SELECT id FROM docs ORDER BY emb <=> $1 LIMIT 10;
```
Qdrant (Rust): cuantización scalar/binary/product con reranking opcional, filtrado con índices de payload.

## Filtrado + ANN / chunking / eval
**Pre-filter** (exacto pero rompe el grafo HNSW si quedan pocos candidatos) vs **post-filter** (rápido pero puede
devolver <k). **Overfiltering problem:** filtros muy restrictivos dejan al grafo sin vecinos navegables y el recall
colapsa (Qdrant usa filtered-HNSW para mitigar). **Chunking:** 256-512 tokens con solape 10-20%; semántico > tamaño
fijo. **Eval:** recall@k, nDCG, MRR sobre un golden set propio, NO solo MTEB.

## Gotchas
1. **Embedding drift:** cambiar de modelo invalida el índice entero — **reindexa todo**, no mezcles vectores de modelos distintos.
2. **Distancia incorrecta:** coseno con vectores no normalizados, o L2 donde el modelo espera coseno. Verifica la métrica.
3. **Truncar MRL sin re-normalizar** rompe la similitud coseno.
4. **Overfiltering:** filtros + ANN devuelven <k; añade fallback a búsqueda exacta.
5. **Costo oculto:** la API de embeddings parece barata hasta reindexar millones; self-host bge/Qwen3 en GPU amortiza rápido.
6. **Cold index:** HNSW debe estar en RAM; si swapea a disco, las queries se desploman.

**Fuentes:** github.com/QwenLM/Qwen3-Embedding · github.com/pgvector/pgvector · qdrant.tech/documentation/quantization · neon.com/blog (halfvec).
