# 338 · Patrones de multi-tenancy: RLS vs schema vs DB-per-tenant

> La decisión de aislamiento es de una sola vía: migrar de shared-DB a schema-per-tenant con
> tráfico vivo es cirugía a corazón abierto. Elige bien al día 0 según cuántos tenants y qué
> compliance esperás, no según lo que se siente más "seguro".

## Las tres arquitecturas
| Patrón | Aislamiento | Escala práctica | Costo/op | Migraciones |
|---|---|---|---|---|
| **Shared DB + `tenant_id` (RLS)** | lógico (políticas) | miles-decenas de miles | mínimo | **1** esquema |
| **Schema-per-tenant** | namespace Postgres | ~100, no más | medio | **N** (fan-out) |
| **DB-per-tenant** | físico total | pocos, grandes | máximo | N DBs |

**Default para SaaS LatAm pequeño/mediano: shared-DB + RLS.** Schema-per-tenant solo si tenés tenants heterogéneos que exigen aislamiento lógico fuerte pero compartís infra. DB-per-tenant solo por compliance/enterprise (datos en región propia, backup independiente).

## Por qué schema-per-tenant no escala
Suena más seguro, pero a **10.000 tenants × 50 tablas = 500.000 archivos** en el directorio de la DB → `autovacuum` y `pg_dump` se vuelven una pesadilla, el catálogo (`pg_class`) se hincha y el planner se ralentiza. Y **PgBouncer poolea por base de datos**: con DB-per-tenant tus pools se multiplican y revientan `max_connections` casi de inmediato. Por eso RLS gana para multitud de tenants chicos.

## RLS bien hecho (el patrón que aguanta)
```sql
ALTER TABLE jobs ENABLE ROW LEVEL SECURITY;
ALTER TABLE jobs FORCE ROW LEVEL SECURITY;          -- aplica también al owner de la tabla
CREATE POLICY tenant_isolation ON jobs
  USING (tenant_id = current_setting('app.tenant_id', true)::uuid);

SET LOCAL app.tenant_id = 't_42';                    -- por TRANSACCIÓN (LOCAL), por el pooler
```
- La app conecta con un **rol sin `BYPASSRLS`** (nunca superuser/owner sin `FORCE`).
- Con **PgBouncer en transaction-pooling**, `SET LOCAL` por transacción es obligatorio: una conexión se reusa entre tenants, y un `SET` de sesión filtra al tenant equivocado. Mismo problema con `search_path` en schema-per-tenant.
- **Indexá `tenant_id`** en todas las tablas (o índices compuestos `(tenant_id, ...)`). Sin eso RLS escanea toda la tabla; con índice, el rendimiento iguala a schema-per-tenant.

## Rendimiento y "ruido entre vecinos"
- RLS rinde mejor con **workloads uniformes**; schema-per-tenant tiene ventaja marginal con tenants muy dispares (índices más chicos, scan acotado).
- **Noisy neighbor**: un tenant que satura CPU/IO afecta a todos en shared-DB. Mitigá con rate-limit per-tenant (token bucket en Redis), `statement_timeout`, y connection caps por tenant. Para una cuenta enterprise pesada, **promovéla a su propia DB** (modelo híbrido: pool shared + DBs dedicadas para los 3 grandes).
- **Connection pooling**: PgBouncer/Supavisor es no-negociable a escala; RLS lo hace trivial (un rol, `tenant_id` por transacción).

## Modelo híbrido (lo que usan los que escalan)
La realidad de producción rara vez es pura: **shared-DB + RLS para la cola larga de tenants chicos**, y **DB/schema dedicado para los 3-5 enterprise** que pagan por aislamiento o lo exigen por compliance. La app abstrae el routing: un mapa `tenant_id → connection string` decide a qué DB conectar; los tenants shared van al pool RLS, los dedicados a su DB. Así no rediseñás cuando llega el primer cliente grande.

## Costo y operación comparados
| Eje | Shared+RLS | Schema-per-tenant | DB-per-tenant |
|---|---|---|---|
| Backup granular | difícil (todo junto) | medio | trivial (por DB) |
| Restaurar 1 tenant | complejo (filtrar) | medio | trivial |
| Onboarding tenant | instantáneo (INSERT) | crear schema + migrar | provisionar DB |
| Costo infra/tenant | centavos | bajo | alto (DB mínima) |
| Blast radius de bug | **todos** | un schema | un tenant |

El **blast radius** es el argumento real para aislar: un bug de RLS o un query sin filtro expone a todos los tenants a la vez. Por eso los tests de aislamiento (intentar leer otro `tenant_id` y verificar que devuelve vacío) son obligatorios en CI.

## Migrar de shared a aislado (cuando crece un tenant)
1. Snapshot de las filas del tenant (`WHERE tenant_id = X`).
2. Provisioná la DB/schema destino con el esquema actual.
3. Copia los datos, valida conteos.
4. Cambia el routing del tenant a la nueva conexión (feature flag).
5. Verifica, luego borra las filas viejas del pool shared. Hacelo con doble-escritura temporal si no podés tener downtime.

## Gotchas
1. **App como superuser** → RLS NO aplica. Rol dedicado + `FORCE ROW LEVEL SECURITY`.
2. **`SET` de sesión con pooler** → fuga cruzada de datos. Usa siempre `SET LOCAL`.
3. **Olvidar RLS en una tabla nueva** → fuga silenciosa. Test automatizado que verifica que toda tabla con `tenant_id` tiene política.
4. **Migraciones en schema-per-tenant** → un tenant olvidado queda desincronizado; automatizá el fan-out o no lo elijas.
5. **JOINs cruzando tablas sin política** → la tabla sin RLS es el hueco; aplica política a todas, incluidas las de lookup.
6. **`current_setting` sin el `true`** → lanza error si la var no existe; el segundo arg evita el crash y trata ausencia como sin acceso.

**Fuentes:** propelius.tech (RLS vs schema), planetscale.com/blog/approaches-to-tenancy-in-postgres, dzone.com (PgBouncer multi-tenant a escala), postgresql.org/docs/current/ddl-rowsecurity.

Cruza con [[63-multi-tenancy-billing-saas]], [[293-rbac-permissions-multitenant]] y [[339-billing-quotas-creditos]].
