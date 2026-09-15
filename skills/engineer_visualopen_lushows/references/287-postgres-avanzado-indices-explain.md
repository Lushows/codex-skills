# 287 · Postgres avanzado: EXPLAIN, índices, particiones, locks

> [[21-postgres-a-fondo-pgvector]] te dio el catálogo de índices. Aquí se opera la planta:
> leer un plan, elegir el índice por cardinalidad, particionar series temporales y no morir por locks.

## Leer EXPLAIN (ANALYZE, BUFFERS) como un plan de obra
`EXPLAIN` estima; `ANALYZE` ejecuta y mide. Léelo de adentro hacia afuera. Señales de incendio:
- **`rows` estimado ≫/≪ real** (ej. estima 50, real 800k) → stats viejas, corre `ANALYZE tabla` o sube `default_statistics_target` (100→500) en columnas sesgadas.
- **`Seq Scan` + `Filter: rows removed by filter` alto** → falta índice o el planner lo descartó por mala selectividad.
- **`Nested Loop` con loops=N grande** sobre sets grandes → debería ser `Hash Join`; revisa `work_mem`.
- **`Buffers: read=` alto vs `hit=`** → cache miss, el dato no está en `shared_buffers`.
```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT o.id FROM orders o
WHERE o.tenant_id = $1 AND o.created_at >= now() - interval '7 days' AND o.status = 'paid';
```

## Elegir el índice por cardinalidad, no por capricho
| Patrón de query | Índice | Por qué |
|---|---|---|
| `WHERE tenant_id=? AND created_at>=?` | B-tree compuesto `(tenant_id, created_at)` | columna selectiva primero, rango al final |
| `WHERE status='paid'` (1 valor caliente de 5) | **Partial** `WHERE status='paid'` | índice 1/5 del tamaño, solo filas vivas |
| `ORDER BY created_at` en tabla append-only de 500M filas | **BRIN** `(created_at)` | KB en vez de GB; lossy pero correlación física alta |
| `payload @> '{"k":"v"}'` (jsonb) | **GIN** `jsonb_path_ops` | 3× menor que `jsonb_ops`, solo `@>` |
| `email LIKE '%x%'` | **GIN** `gin_trgm_ops` (pg_trgm) | B-tree no sirve para wildcard a la izquierda |

Reglas: el **orden de columnas** en compuesto importa (igualdad antes que rango). **Covering** `INCLUDE (col)` evita el heap fetch (index-only scan) si `VACUUM` mantuvo la visibility map. Multicolumna no sustituye a varios índices de una columna si las queries varían.

## Particiones declarativas (series temporales / multi-tenant)
`PARTITION BY RANGE (created_at)` mensual: poda viejas con `DETACH CONCURRENTLY` (PG14+) sin lockear, luego `DROP`. **Partition pruning** elimina particiones en planeo si el `WHERE` incluye la clave → el plan toca 1 partición, no 60.
```sql
CREATE TABLE events (id bigint, tenant_id int, created_at timestamptz, payload jsonb)
  PARTITION BY RANGE (created_at);
CREATE TABLE events_2026_06 PARTITION OF events
  FOR VALUES FROM ('2026-06-01') TO ('2026-07-01');
```
Gotcha: sin la columna de partición en el `WHERE`, Postgres escanea **todas**. Índices se crean por partición (o en la padre, que cascada). Usa `pg_partman` para automatizar creación/retención.

## VACUUM y autovacuum (la deuda silenciosa de MVCC)
Cada `UPDATE`/`DELETE` deja un dead tuple → bloat e índices inflados. Defaults van bien en tablas chicas, pero `autovacuum_vacuum_scale_factor=0.2` significa esperar **20% de filas muertas**: en una tabla de 100M, son 20M tuplas antes de limpiar. Para tablas calientes, override por tabla:
```sql
ALTER TABLE events SET (autovacuum_vacuum_scale_factor = 0.02,   -- ~2M en vez de 20M
                        autovacuum_vacuum_cost_limit = 3000);     -- SSD: el default 200 es de discos giratorios
```
PG17 prioriza mejor tablas ocupadas y hace menos pasadas más eficientes en alta escritura. Observa `pg_stat_user_tables.n_dead_tup` y `last_autovacuum`. **Wraparound**: vigila `age(relfrozenxid)`; un `VACUUM FREEZE` forzado a 2B XIDs congela la base entera.

## Locks que muerden en producción
- `CREATE INDEX` toma `SHARE` (bloquea writes) → **siempre `CREATE INDEX CONCURRENTLY`** (no lockea, pero no corre en transacción y puede dejar índice `INVALID` si falla → `DROP` y reintenta).
- `ALTER TABLE ... ADD COLUMN ... DEFAULT` con default **constante** es instantáneo desde PG11 (no reescribe); un default **volátil** reescribe toda la tabla con `ACCESS EXCLUSIVE`.
- `SELECT ... FOR UPDATE SKIP LOCKED` para colas en SQL (workers compiten sin bloquearse).
- Detecta bloqueos: `pg_locks` JOIN `pg_stat_activity`; pon `lock_timeout` y `statement_timeout` para no colgar conexiones.

## Gotchas
1. Índice no usado: `pg_stat_user_indexes.idx_scan = 0` → bórralo, solo pesa en writes y VACUUM.
2. `OR` mata índices → reescribe a `UNION ALL` o usa `= ANY(ARRAY[...])`.
3. Funciones sobre la columna (`WHERE lower(email)=?`) ignoran el índice → crea índice de expresión `ON t (lower(email))`.

Cruza con [[21-postgres-a-fondo-pgvector]] y [[359-database-scaling-sharding]].
