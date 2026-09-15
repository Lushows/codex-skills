# 21 — Postgres a fondo + pgvector

## Indexing
**B-tree** (default — igualdad, rangos, sorting, `ORDER BY`) · **GIN** (multi-valor: `jsonb`, arrays, full-text
`tsvector`, `pg_trgm` LIKE) · **GiST** (geométrico, rangos, NN) · **BRIN** (tablas append-only enormes ordenadas
por `created_at` — tiny, lossy). **Partial** (`WHERE status='active'`) encoge el índice a filas calientes.
**Covering** (`INCLUDE (col)`) habilita index-only scans (salta el heap).

## EXPLAIN ANALYZE (corre la query y muestra timing real)
Léelo de adentro hacia afuera: `Seq Scan` en tablas grandes, divergencia rows estimado vs real (stats viejas →
`ANALYZE`), `Nested Loop` sobre sets grandes. `EXPLAIN (ANALYZE, BUFFERS) SELECT ...`.

## Transacciones/isolation (MVCC)
Default `READ COMMITTED`. `REPEATABLE READ` para lecturas multi-statement consistentes; `SERIALIZABLE` para
invariantes entre filas (aborta con `40001` → debes reintentar). `SELECT ... FOR UPDATE` lockea filas (evita lost
updates, ej. decrementar inventario). MVCC → readers nunca bloquean writers.

## Connection pooling — modos PgBouncer
`session` (1 conn por sesión — seguro, soporta prepared stmts/`SET`) · `transaction` (conn devuelto tras cada
txn — alta concurrencia, *rompe features de sesión y algunos prepared stmts*) · `statement`. Apps web quieren
`transaction`; desactiva prepared stmts server-side (asyncpg `statement_cache_size=0`).

## Migraciones / JSONB / partitioning / VACUUM
**Alembic** (autogenerate) o sqlx/Atlas/Flyway. Backward-compatible para zero-downtime (expand→migrate→contract).
`CREATE INDEX CONCURRENTLY` (no lockea writes). **JSONB:** GIN (`jsonb_path_ops` para `@>`); no modeles todo como
un blob. **Partitioning:** `PARTITION BY RANGE (created_at)` para time-series; poda viejas con `DETACH`/`DROP`.
**VACUUM:** dead tuples (MVCC) → bloat; autovacuum normalmente lo maneja; baja `autovacuum_vacuum_scale_factor` en
tablas high-churn; observa `pg_stat_user_tables.n_dead_tup`.

## pgvector (≥0.8.0, nov 2024) — para RAG
`vector(1536)`. Ops: `<->` (L2), `<#>` (inner product neg), `<=>` (coseno). **HNSW vs IVFFlat:** HNSW = mejor
recall/velocidad, sin training (build en tabla vacía), más memoria + build más lento → **default recomendado
2026.** IVFFlat = build rápido, menos memoria, necesita data para entrenar `lists`. **El índice debe matchear el
op de la query.** 0.8.0 añadió **iterative index scans** (`hnsw.iterative_scan`) para el "overfiltering". **Hybrid
search:** combina distancia vector + `tsvector`/BM25, fusiona con Reciprocal Rank Fusion (RRF).
```sql
CREATE INDEX ON items USING hnsw (embedding vector_cosine_ops) WITH (m=16, ef_construction=64);
SET hnsw.ef_search = 100;                                    -- knob recall/latencia en query
SELECT id FROM items ORDER BY embedding <=> $1 LIMIT 10;
```

## Gotchas
1. El build de HNSW es RAM-hungry → sube `maintenance_work_mem`.
2. Olvidar `ANALYZE` tras bulk load → planes malos.
3. PgBouncer `transaction`-mode rompe `SET LOCAL`/advisory locks entre statements en silencio.
4. Un índice coseno no acelera una query L2 — son ops distintos.

**Fuentes:** postgresql.org/about/news/pgvector-080-released · github.com/pgvector/pgvector · pgbouncer.org/features · postgresql.org/docs/current/mvcc.
