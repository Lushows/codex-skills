# 290 · Modelado de datos + migraciones zero-downtime

> Una migración que toma `ACCESS EXCLUSIVE` sobre una tabla de 200M filas en horario pico es un
> incidente, no un deploy. La regla: el esquema viejo y el nuevo deben coexistir mientras rotan los pods.

## Normalización: cuánto, y cuándo parar
3NF por defecto: cada hecho en un lugar, sin anomalías de update. **Desnormaliza con intención**, no por pereza:
- Contador derivado caliente (`order_count` en `users`) que recalcular costaría un `COUNT(*)` por request → desnormaliza, mantén con trigger o en la escritura.
- Snapshot histórico (precio al momento de la compra) → **copia el valor** a `order_items.unit_price`; si referencias `products.price` el histórico se corrompe cuando cambia el precio.
- jsonb para atributos esparsos/variables (config por tenant, metadata de eventos) — **no** para relaciones que vas a filtrar/joinar; eso es una tabla.

## Claves, tipos y los errores que cuestan caro
- **PK**: `bigint GENERATED ALWAYS AS IDENTITY` (no `serial`, deprecado) o **UUIDv7** (k-ordenable por tiempo → no fragmenta el B-tree como UUIDv4 random, que destroza la localidad de inserción). UUIDv4 como PK en tabla grande = bloat de índice y cache misses.
- `timestamptz` **siempre**, nunca `timestamp` (sin tz es una bomba de relojería en producción multi-región).
- `numeric` para dinero, jamás `float` (0.1+0.2≠0.3). `text` no `varchar(n)` salvo restricción real.
- FKs con `ON DELETE` explícito; índice sobre la columna FK (Postgres **no** lo crea solo → borrados y joins lentos).

## Multi-tenancy: tres modelos
| Modelo | Aislamiento | Costo op | Cuándo |
|---|---|---|---|
| `tenant_id` en cada tabla + **RLS** | lógico | bajo | SaaS B2C/B2B masivo, miles de tenants |
| schema por tenant | medio | medio | decenas–cientos, compliance moderado |
| DB por tenant | fuerte | alto | enterprise, datos regulados, ruido vecino |

RLS de Postgres: `CREATE POLICY tenant_isol ON orders USING (tenant_id = current_setting('app.tenant')::int)`. Setea `app.tenant` por request. **Trampa con PgBouncer transaction-mode**: `SET` no persiste entre statements → usa `SET LOCAL` dentro de la txn o pasa el tenant en cada query. Índice compuesto siempre con `tenant_id` primero.

## Migraciones zero-downtime: expand → backfill → contract
La regla **N/N-1**: la app nueva debe correr contra el esquema viejo y la app vieja contra el nuevo. Una migración destructiva = secuencia de pasos seguros, no un cambio grande.
1. **Expand** (no destructivo, compatible hacia atrás): `ADD COLUMN` nullable o con default constante, nueva tabla, `CREATE INDEX CONCURRENTLY`. La app vieja lo ignora.
2. **Backfill**: rellena datos históricos en **lotes pequeños** (`UPDATE ... WHERE id BETWEEN` por bloques de 5–10k con pausa), nunca un `UPDATE` masivo que lockea y genera 200M dead tuples de golpe. Despliega app que escribe a viejo **y** nuevo (dual-write).
3. **Cut over**: la app lee del nuevo. Verifica paridad.
4. **Contract** (destructivo): `DROP COLUMN`/`DROP TABLE` **solo tras un ciclo completo de rollout** — si un pod viejo aún referencia la columna, `DROP` causa errores en runtime.

### Operaciones peligrosas en Postgres y su versión segura
| Peligroso | Seguro |
|---|---|
| `ADD COLUMN ... DEFAULT volatil()` (reescribe tabla) | default constante (instantáneo PG11+), o add nullable + backfill |
| `ALTER COLUMN TYPE` (reescritura + lock) | columna nueva + backfill + swap |
| `ADD CONSTRAINT ... CHECK` (escanea con lock) | `ADD ... NOT VALID` → `VALIDATE CONSTRAINT` (lock débil) |
| `CREATE INDEX` (bloquea writes) | `CREATE INDEX CONCURRENTLY` |
| renombrar columna en uso | añadir nueva, dual-write, migrar, borrar vieja |

Pon `lock_timeout = '3s'` en la sesión de migración: si no consigue el lock rápido, falla y reintenta en vez de encolar y congelar la tabla a todo el tráfico.

## Gotchas
1. `NOT NULL` sobre columna nueva poblada: añade nullable, backfill, luego `SET NOT NULL` con `NOT VALID`+`VALIDATE` (PG12+ valida sin escaneo exclusivo largo).
2. Enums: `ADD VALUE` no se borra ni reordena → usa tablas de lookup o `text` + CHECK si evolucionan.
3. Migración + deploy de código en el mismo paso = rollback imposible; separa siempre.

Cruza con [[291-orms-prisma-drizzle]] y [[338-multitenancy-patterns]].
