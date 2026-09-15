# 64 — Data pipelines / MLOps de datos (ETL/orchestration)

## Orquestadores 2026 (elige por modelo mental)
- **Dagster** — modelo **asset-based** (Software-Defined Assets): defines el *dato* que produces, no la tarea. Cada
  modelo dbt = un asset con lineage/historial/metadata; la mejor integración dbt OSS. Ganador en greenfield dbt-heavy.
- **Airflow 3** — el peso pesado ubicuo, task-based (DAGs imperativos). Eliges por madurez/ecosistema/talento. UI y scheduler modernizados.
- **Prefect** — Python-puro, decoras funciones; mejor DX para pipelines ligeros; assets son feature reciente/limitada.

**Regla:** dbt-heavy greenfield → **Dagster**; ya tienes Airflow/equipo grande → quédate; script Python rápido → **Prefect**.

## dbt (la "T" de ELT)
Transformaciones SQL versionadas en Git. Models (`SELECT` materializados table/view/incremental), tests (`unique`,
`not_null`, custom), docs auto, lineage.
```sql
-- models/silver/orders.sql
{{ config(materialized='incremental', unique_key='order_id') }}
SELECT order_id, tenant_id, amount_usd, created_at FROM {{ ref('bronze_orders') }}
{% if is_incremental() %} WHERE created_at > (SELECT max(created_at) FROM {{ this }}) {% endif %}
```

## ETL vs ELT
Lo moderno es **ELT**: cargas crudo al warehouse y transformas *adentro* con SQL (dbt), aprovechando el cómputo del
warehouse. ETL clásico (transformar antes de cargar) sobrevive solo con restricciones PII/compliance pre-load.

## Warehouses / ingestión
**BigQuery** (serverless, pago por query escaneado), **Snowflake** (storage/compute separados), **ClickHouse** (OLAP
ultrarrápido, lo que usa PostHog por dentro), **DuckDB** (in-process, el "SQLite del analytics", perfecto dev local).
**Ingestión:** **Airbyte** (OSS, cientos de conectores, self-host), **Fivetran** (managed, caro/cero-mantenimiento), **Meltano** (Singer, Git-ops).

## Streaming vs batch / Medallion / data quality
**Batch** (cada hora/día) cubre el 95% de analytics; **streaming** (Kafka/Flink) solo con latencia <1min real
(fraude, dashboards live) — no empieces con streaming "por si acaso". **Medallion:** **Bronze** (raw inmutable) →
**Silver** (limpio/dedup/tipado/joins) → **Gold** (agregados de negocio). **Data quality:** Great Expectations (o
dbt tests + contracts) valida esquema/reglas; un *data contract* rompe el build si cambia el esquema.

## Idempotencia / backfill
Cada run re-ejecutable sin duplicar (merge por `unique_key`, particiones por fecha). Backfillable = reprocesar rango
histórico (Dagster *partitions*, dbt `--full-refresh`). **Stack equipo chico:** Airbyte → BigQuery/DuckDB → dbt → Dagster, BI en Metabase. Empieza con DuckDB+dbt local si los datos son chicos.

## Gotchas
1. **Incremental sin late-arriving data** — filtrar por `max(created_at)` pierde registros tardíos; usa ventana de re-procesamiento.
2. **`SELECT *` en dbt** rompe contratos cuando cambia el upstream — lista columnas.
3. **Streaming prematuro** — operación 10× más cara sin necesidad real.
4. **Bronze mutable** — si limpias en bronze pierdes la fuente de verdad para reprocesar.
5. **Tests dbt solo en CI, no en prod** — corre tests post-load en cada run o publicas data sucia.
6. **BigQuery cost runaway** — `SELECT *` sobre tablas grandes escanea TB; particiona/clusteriza + cost controls.

**Fuentes:** getorchestra.io/blog (Dagster vs Prefect vs Airflow 2026) · dagster.io/vs/dagster-vs-prefect · docs.getdbt.com.
