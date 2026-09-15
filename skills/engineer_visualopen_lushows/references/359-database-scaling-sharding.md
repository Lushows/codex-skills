# 359 · Escalar la base de datos (réplicas → pooling → partición → sharding, en ese orden)

> Escalá en el orden barato→caro: optimizá queries, luego réplicas, luego pooling, luego partición,
> y solo al final sharding. Shardear antes de tiempo es la decisión más cara de revertir.

## El orden correcto (no saltes pasos)
1. **Índices + EXPLAIN** ([[287-postgres-avanzado-indices-explain]]) — el 80% de "la DB no aguanta" es un seq-scan.
2. **Read-replicas** — descarga las lecturas del primario.
3. **Connection pooling** — el primario se ahoga en conexiones mucho antes que en CPU.
4. **Partición** — una tabla gigante en piezas, mismo servidor.
5. **Sharding** — datos en *varios* servidores. Último recurso, complejidad permanente.

## Read-replicas: descarga lecturas, paga lag
Streaming replication async: el primario escribe, las réplicas siguen el WAL. Las lecturas (reports,
listados, búsquedas) van a réplicas; escrituras al primario. **Replication lag** (ms–s) = una réplica
puede no tener tu escritura recién hecha → **read-your-writes** roto. Mitigá: lee de primario tras
escribir (sticky), o esperá LSN. No pongas lógica de saldo/stock en una réplica.

## Connection pooling: PgBouncer (el cuello real de Postgres)
Cada conexión Postgres = un proceso (~5-10MB). 10k clientes ≠ 10k conexiones al primario. PgBouncer
multiplexa miles de clientes sobre decenas de conexiones backend.
| Modo | Asigna backend | Uso | Coste |
|---|---|---|---|
| **session** | toda la sesión del cliente | apps legacy con estado de sesión | poca multiplexación |
| **transaction** | solo durante la transacción | **default web/serverless** | máxima multiplexación |
| statement | por sentencia | OLAP simple | rompe transacciones multi-stmt |

En **transaction pooling** no podés usar lo que cuelga de la sesión: `SET`, `LISTEN/NOTIFY`, advisory
locks de sesión, temp tables, y `PREPARE` SQL-level. **Prepared statements** SÍ funcionan vía protocolo
si configurás `max_prepared_statements` > 0 (PgBouncer ≥1.21): trackea los named statements y los asegura
en el backend asignado. Subirlo mejora reuso pero cuesta RAM/CPU en el bouncer. Dimensioná
`default_pool_size` ≈ (cores del primario × 2-4), no más — saturar el primario con un pool gigante anula el pooling.

## Partición (declarativa, un servidor)
Postgres `PARTITION BY`:
- **RANGE** por fecha (`created_at`) — el caso rey: logs/eventos/órdenes. Tirás meses viejos con
  `DETACH`+`DROP` (instantáneo, sin `DELETE` masivo que infla el bloat).
- **LIST** por región/tenant. **HASH** para repartir parejo sin clave natural.
Beneficio: **partition pruning** — el planner toca solo las particiones relevantes. Exige que la query
filtre por la clave de partición; si no, escanea todas y perdés el beneficio.

## Sharding (varios servidores — la frontera de complejidad)
Repartís filas entre nodos por **shard key**. Lo que ganás en escritura/almacenamiento lo pagás en:
- **Elegir la shard key bien (irreversible-ish)**: alta cardinalidad, distribución pareja, presente en
  casi toda query. `tenant_id` para SaaS multi-tenant suele ganar; `user_id` reparte parejo.
- **Cross-shard queries**: un JOIN o agregado entre shards = scatter-gather (lento, frágil). Diseñá para
  que el 99% de queries toquen **un** shard.
- **Rebalanceo**: añadir un shard mueve datos. Hash-ring/consistent-hashing minimiza el movimiento.
- **Transacciones distribuidas**: 2PC es lento y frágil — evitá escrituras cross-shard.
Antes de shardear vos mismo, evaluá Citus, Vitess, o un Postgres distribuido — resuelven el routing.

## Gotchas
1. Réplica para read-your-writes sin manejar lag = bug "guardé y no aparece". Sticky al primario tras escribir.
2. `pgbouncer` en transaction mode con un ORM que usa session prepared statements rompe en silencio → modo protocolo o `max_prepared_statements`.
3. Partición sin filtrar por la clave = escaneás todas las particiones (peor que sin partición por el overhead).
4. Shard key con hot-spot (ej. `created_at` → todo el tráfico de hoy a un shard) mata el balanceo.

Cruza con [[287-postgres-avanzado-indices-explain]], [[21-postgres-a-fondo-pgvector]] y [[358-caching-strategy-multilayer]].
