# 343 · Warehouse y lakehouse (BigQuery, Snowflake, DuckDB, ClickHouse — cuál y por qué)

> El warehouse equivocado se paga en facturas sorpresa o en queries que tardan minutos.
> No hay "el mejor": hay el que encaja con tu volumen, tu patrón de query y quién paga la cuenta.

## El eje que decide: modelo de costo
| Motor | Modelo de cobro | Brilla cuando | Muerde cuando |
|---|---|---|---|
| **BigQuery** | serverless, **$5/TB escaneado** on-demand (1 TB/mes gratis) | volumen de query bajo/irregular; cero ops | `SELECT *` sobre tablas grandes → factura TB; cold-start 1-5 s [no verificado precio exacto] |
| **Snowflake** | crédito por **compute** (storage separado), warehouses que pausan | cargas variables, multi-tenant, time-travel | warehouse olvidado encendido = sangría; tuning de tamaño |
| **ClickHouse** | OSS gratis self-host; Cloud usage-based | OLAP de alto volumen y queries repetitivas; **5-50× más barato a escala** | ops propias (self-host), ingest/joins complejos menos ergonómicos |
| **DuckDB** | gratis, **in-process** (sin servidor) | dev local, datasets <~2 TB, dashboards/batch | concurrencia multi-usuario / escritura concurrente; no es un servidor |

(Cifras 2026 de comparativas públicas; los precios cambian — verifica antes de presupuestar.)

## La regla de bolsillo
- **Query volume bajo o esporádico** → **BigQuery**: pagas solo lo que escaneas, cero infra.
- **Query volume alto y repetitivo** → **ClickHouse**: a escala es órdenes de magnitud más barato que
  pagar por TB escaneado una y otra vez.
- **Dev local / equipo chico / datos que caben en una máquina** → **DuckDB**: el "SQLite del analytics",
  arranca en un import, perfecto para prototipar el modelo dbt antes de subir a la nube.
- **Empresa con cargas mixtas y presupuesto** → **Snowflake** por madurez y separación storage/compute.

## Warehouse vs lakehouse
- **Warehouse**: storage + compute integrados, formato propietario optimizado (BigQuery, Snowflake nativo).
- **Lakehouse**: tablas abiertas (**Iceberg**, Delta) sobre object storage (S3/GCS) + motor de query
  encima. Desacopla el dato del motor → puedes leer las mismas tablas Iceberg desde DuckDB, ClickHouse,
  Snowflake o Spark sin re-copiar. Es la dirección de 2026 para evitar lock-in y duplicar storage.
- **DuckDB + Iceberg/Parquet en S3** = lakehouse de pobre, sorprendentemente capaz para equipo chico.

## ClickHouse: el caso OLAP puro
Columnar, vectorizado, brutalmente rápido en scans de una tabla y agregaciones (5-20× vs BigQuery en
queries que caben en memoria). Es lo que **PostHog** usa por dentro ([[323-analytics-tracking-posthog-ga4]]).
Costo: si self-hosteas, 3 nodos modestos cuestan una fracción de ClickHouse Cloud; el precio es la ops.

## Optimización de costo/rendimiento
1. **Particiona + clusteriza** por fecha y por la columna de filtro frecuente → menos bytes escaneados.
2. **Nunca `SELECT *`** en analytics: lista columnas (columnar solo lee las que pides; `*` lee todo).
3. **Cost controls**: en BigQuery pon límite de bytes por query y por usuario/proyecto → mata el runaway.
4. **Materializa lo caliente**: agregados de Gold como tabla, no vista, si se consultan mucho.
5. **Snowflake auto-suspend** agresivo (60 s) para que el warehouse no cobre idle.

## Gotchas
1. **BigQuery `SELECT *` sobre TB** = factura de cientos de dólares por una query distraída.
2. **DuckDB tratado como servidor** — no maneja muchos escritores concurrentes; es embebido por diseño.
3. **Snowflake warehouse zombi** encendido todo el finde drenando créditos.
4. **Lock-in de formato** — si todo vive en formato propietario, migrar duele; Iceberg lo evita.

Cruza con [[342-etl-elt-data-pipelines]] y [[344-dbt-transformations]].
