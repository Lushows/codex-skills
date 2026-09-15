# 291 · ORMs: Prisma vs Drizzle vs Kysely

> El ORM no es decoración: define tu peso de cold-start, tu factura de N+1 y si puedes correr en edge.
> En 2026 la elección práctica para proyectos TypeScript nuevos se inclina a Drizzle; Kysely si quieres SQL.

## Las tres filosofías
- **Prisma** — ORM con schema propio (`schema.prisma`) y cliente generado. DX inmejorable, types precomputados en `.d.ts` (el IDE responde instantáneo). Históricamente arrastraba un query engine en Rust (binario aparte); Prisma 6+ ofrece cliente sin engine Rust para mejorar serverless.
- **Drizzle** — schema en TypeScript puro, API que **se parece a SQL** (`db.select().from(users).where(eq(...))`). ~7.4kb gzip, **cero dependencias**, corre en cualquier edge runtime.
- **Kysely** — *query builder* type-safe, no ORM. Tú escribes SQL con tipos; sin migraciones mágicas ni lazy loading. El SQL que escribes es el SQL que corre.

## Type-safety: mismo destino, costo de compilación distinto
Prisma **genera** los tipos en build → el typechecker hace pocas instanciaciones. Drizzle **infiere** todo en tiempo de tipos: en un schema de 50+ modelos, Prisma corre ~428 instanciaciones de tipo vs Drizzle ~41,150 — **~96×** [verificado]. Traducción: en monorepos grandes Drizzle puede ralentizar `tsc` y el IDE notablemente. Mitiga con `db.query` API y dividiendo el schema. Kysely infiere desde una interfaz `Database` que tú declaras (o generas con `kysely-codegen`).

## N+1: el impuesto invisible
El patrón clásico: cargas 100 posts, luego un query por autor = 101 queries. 
- **Prisma**: `include`/`select` anidado genera joins o queries batcheadas; evita el loop manual `await` por fila.
- **Drizzle**: `with` (relational queries) emite **una** sentencia optimizada → reportes de hasta **14× menos latencia** que ORMs que caen en N+1 [verificado].
- **Kysely**: tú escribes el `JOIN`/`json_agg` → no hay N+1 porque no hay magia, pero tampoco red de seguridad.
Regla: nunca `for (const x of items) await db.find(x.fk)`. Es N+1 garantizado en cualquier ORM.

## Edge y serverless: peso = dinero
| | Bundle | Cold start | Edge runtime |
|---|---|---|---|
| Prisma | ~1.6MB | 1–3s | mejorando (driver adapters) |
| Drizzle | ~7.4kb gzip, 0 deps | <500ms | sí, nativo |
| Kysely | ligero | bajo | sí (con dialecto compatible) |

En funciones serverless el cold start se paga en latencia y en factura. Drizzle baja de 1–3s (Prisma) a <500ms [verificado]. Usa siempre **driver adapters** sobre HTTP/WebSocket (Neon, PlanetScale) en edge — TCP crudo no existe ahí. Y conexión: en serverless, **pooler en transaction-mode** (PgBouncer/Neon) o agotas las conexiones de Postgres con cada invocación.

## Raw SQL: la válvula de escape obligatoria
Joins pesados, CTEs recursivos, window functions, `LATERAL` → ningún ORM lo expresa bien. 
- Prisma: `$queryRaw` (parametrizado, tipa el retorno manual).
- Drizzle: `sql\`...\`` template, compone con el query builder.
- Kysely: ya es esto; `sql` tag para lo que el builder no cubra.
Si **la mayoría** de tus queries son complejas, salta el ORM: usa Kysely o SQL crudo con una capa fina de tipos. No pelees con la abstracción.

## Migraciones
- Prisma Migrate: declarativo desde `schema.prisma`, autogenera SQL, buen flujo dev. Cuidado: algunas operaciones generan SQL que lockea → revisa el SQL antes de prod (ver [[290-data-modeling-migrations]]).
- Drizzle Kit: `generate` produce SQL versionado que **editas** → controlas locks y `CONCURRENTLY` a mano.
- Kysely: migraciones programáticas en TS, control total, cero magia.

## Recomendación 2026
- **Proyecto nuevo, edge/serverless** → Drizzle.
- **Equipo que prioriza DX, no necesita edge, schema mediano** → Prisma.
- **Queries dominadas por SQL complejo, quieres control total** → Kysely.
Los tres parametrizan queries (anti SQL-injection) si usas su API; el riesgo aparece al concatenar strings en raw.

## Gotchas
1. Prisma engine Rust + serverless = cold start grande; verifica que usas el cliente sin engine / driver adapter.
2. Drizzle infiere tipos pesado → `tsc` lento en schemas enormes; particiona el schema.
3. Pooler transaction-mode rompe prepared statements server-side → desactívalos (`statement_cache_size=0`).
4. Lazy loading de relaciones en loops = N+1; usa eager (`with`/`include`/`JOIN`) explícito.

Cruza con [[290-data-modeling-migrations]] y [[96-bases-datos-modernas-serverless-2026]].
