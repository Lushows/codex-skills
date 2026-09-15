# 344 · dbt y la capa de transformación (SQL versionado, testeado, con lineage)

> dbt convirtió la "T" de ELT en ingeniería de software: SQL en Git, con tests, docs y lineage.
> El error caro no es escribir el modelo: es no testearlo y descubrir el bug en el dashboard del CEO.

## Qué es un modelo
Un `.sql` con un `SELECT` que dbt materializa. La materialización decide cómo aterriza:
| Tipo | Qué hace | Cuándo |
|---|---|---|
| `view` | re-computa cada query | dev, modelos baratos/poco usados |
| `table` | reconstruye full cada run | datasets chicos, lógica que cambia mucho |
| `incremental` | solo procesa filas nuevas/cambiadas | tablas grandes append-heavy |
| `ephemeral` | CTE inline, no aterriza | helpers reutilizados, no consultados directo |

```sql
-- models/silver/orders.sql
{{ config(materialized='incremental', unique_key='order_id') }}
SELECT order_id, tenant_id, amount_usd, created_at
FROM {{ ref('bronze_orders') }}
{% if is_incremental() %}
  WHERE created_at > (SELECT max(created_at) FROM {{ this }}) - INTERVAL 3 DAY
{% endif %}
```
La ventana `- 3 DAY` reabsorbe **late-arriving data** ([[342-etl-elt-data-pipelines]]) — sin ella el
incremental pierde filas tardías. El `unique_key` hace el MERGE idempotente: re-correr no duplica.

## `ref()` y `source()` — el grafo gratis
`{{ ref('x') }}` crea la dependencia entre modelos; dbt deduce el **DAG** y el orden de ejecución sin
que lo declares. `{{ source('raw','orders') }}` marca la entrada cruda. De ahí salen lineage y docs auto.

## Tests — el contrato que rompe el build
- **Genéricos**: `unique`, `not_null`, `accepted_values`, `relationships` (FK) en `schema.yml`.
- **Singular**: un `.sql` que devuelve filas malas → si devuelve algo, falla.
- **Contracts** (`enforced: true`): declaras columnas+tipos; si el modelo no calza, falla en compile,
  no en runtime. Esto es lo que frena que un cambio upstream envenene Gold.
- **Corre los tests en cada run de prod**, no solo CI: la fuente cambia entre deploys.

## Semantic layer / MetricFlow — métricas definidas una vez
El **dbt Semantic Layer**, sobre **MetricFlow**, define métricas (revenue, MRR, active_users) como
objetos componibles con measures, dimensions y filters. Una métrica definida una vez se consulta
**consistente desde cualquier herramienta** (Metabase, Tableau, app propia) sin que cada una
reimplemente el `GROUP BY`. Mata el clásico "tu revenue no cuadra con el mío". Cruza con
[[346-dashboards-bi]] y [[337-saas-metrics-mrr-churn-ltv]].

## dbt Fusion (2026) — el cambio de DX
El motor **Fusion** (Rust, herencia de SDF) trae **errores en tiempo real en el IDE**, compilación
local rápida y CI **state-aware** (solo re-corre lo afectado). El loop de feedback baja de minutos a
segundos: la práctica del analytics engineer se parece cada vez más a software engineering.
[no verificado: estado GA/licencia exacta de Fusion — confirmar en docs.getdbt.com]

## Lineage y docs
`dbt docs generate` produce un sitio con el DAG navegable: de qué source viene cada columna, qué
modelos rompería un cambio. Es la herramienta de **impact analysis** antes de tocar algo upstream.

## Gotchas
1. **`SELECT *` en un modelo** rompe contracts cuando el upstream agrega/renombra columna — lista columnas.
2. **Incremental sin ventana de reproceso** pierde late-arriving (ver el `- 3 DAY` arriba).
3. **Tests solo en CI** → data sucia en prod cuando la fuente cambia entre deploys.
4. **Full-refresh olvidado**: si cambias la lógica de un incremental, corre `dbt run --full-refresh`
   o el histórico queda con la lógica vieja mezclada.
5. **Macros mágicas sin docs** — el Jinja se vuelve ilegible; mantén la lógica en SQL plano cuando puedas.

Cruza con [[342-etl-elt-data-pipelines]] y [[346-dashboards-bi]].
