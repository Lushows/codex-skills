# 342 · ETL/ELT y data pipelines (ingesta cruda, transformar adentro, no perder filas)

> Mover datos de A a B suena trivial hasta que un run duplica filas, otro pierde los late-arriving,
> y nadie sabe qué versión es la verdad. La disciplina no es el código: es idempotencia + contratos.

## ETL vs ELT — el default 2026 es ELT
- **ELT**: cargas crudo al warehouse y transformas *adentro* con SQL ([[344-dbt-transformations]]),
  usando el cómputo del warehouse. Es el default porque desacopla ingesta de lógica: si cambia una
  regla, re-transformas sin re-ingerir.
- **ETL clásico** (transformar antes de cargar) sobrevive solo cuando hay que **enmascarar PII** o
  cumplir compliance **pre-load** (no puede aterrizar el dato sensible crudo), o el warehouse no
  aguanta el volumen de raw.

## Ingesta: batch, CDC, streaming
| Modo | Cuándo | Herramienta típica |
|---|---|---|
| **Batch** (hora/día) | 95% de analytics; reportes, BI, ML offline | Airbyte, Fivetran, dlt |
| **CDC** (change data capture) | replicar una DB transaccional sin re-scan completo | Debezium, Fivetran log-based |
| **Streaming** (<1 min real) | fraude, dashboards live, alertas | Kafka + Flink/Materialize |

**Regla:** no empieces con streaming "por si acaso" — es 10× más caro de operar. CDC log-based >
CDC por polling de `updated_at` (el polling pierde deletes y filas que cambian dos veces entre polls).

## Conectores / EL tooling
- **Airbyte** — OSS, cientos de conectores, self-host; el default para equipo chico con muchas fuentes.
- **Fivetran** — managed, cero mantenimiento, **caro** y cobra por MAR (monthly active rows) → vigila.
- **dlt** — librería Python, pipelines como código, schema inference; el "requests del EL", ideal en repo.
- **Meltano / Singer** — taps/targets Git-ops; ecosistema desigual pero versionable.

## Idempotencia — la propiedad que separa pipeline de script
Cada run debe ser **re-ejecutable sin duplicar ni corromper**. Mecanismos:
- **MERGE/UPSERT por `unique_key`** en vez de `INSERT` ciego.
- **Particiones por fecha**: el run de un día reemplaza *esa* partición (idempotente por diseño).
- **Watermark con ventana de reproceso**: no filtres `created_at > max()` a secas → pierdes los
  **late-arriving** (eventos que llegan tarde con timestamp viejo). Reprocesa los últimos N días siempre.

## Calidad de datos y contratos
Un **data contract** rompe el build si el upstream cambia el esquema (columna renombrada, tipo
cambiado) antes de que la data sucia llegue a producción. Valida esquema + reglas con **dbt tests +
contracts** o **Great Expectations**. Corre los tests **en cada run post-load**, no solo en CI: si
solo validas en CI, publicas data rota cuando la fuente cambia entre deploys.

## Medallion (capas de confianza)
**Bronze** (raw inmutable, append-only — tu fuente de verdad para reprocesar) → **Silver**
(limpio/dedup/tipado/joins) → **Gold** (agregados de negocio listos para BI). Nunca limpies en bronze:
si mutas el raw pierdes la capacidad de re-derivar todo desde cero.

## Gotchas
1. **Watermark sin ventana** → pierde late-arriving silenciosamente; nadie nota hasta el cierre de mes.
2. **Fivetran MAR runaway** — una tabla con muchos updates dispara el costo; revisa el plan de sync.
3. **CDC por polling** pierde deletes; usa log-based si la DB lo permite (Postgres WAL, MySQL binlog).
4. **Bronze mutable** — destruye la reproducibilidad; raw siempre inmutable.
5. **Esquema sin contrato** — el upstream cambia un tipo y el dashboard de Gold da números falsos sin error.

## Stack mínimo equipo chico
Airbyte/dlt → BigQuery/DuckDB ([[343-data-warehouse-bigquery-duckdb]]) → dbt → orquestado con Dagster
([[242-pipeline-orchestration-dagster-flyte]]), BI en Metabase ([[346-dashboards-bi]]). Si los datos
son chicos, empieza con **DuckDB + dbt local** y promueve a la nube solo cuando duela.

Cruza con [[64-data-pipelines-mlops-etl]] y [[242-pipeline-orchestration-dagster-flyte]].
