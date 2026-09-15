# 96 — Bases de datos modernas / serverless (2026)

Tres filosofías: **serverless Postgres** (compute/storage separados), **edge SQLite**, **reactive/sync-first**. "Scale-to-zero + branching" es table stakes.

## Serverless Postgres — Neon vs Supabase
**Neon** (el Postgres serverless más puro): suspende compute tras idle (no pagas CPU) + **branching** Git-style
(copy-on-write, ideal preview DBs per-PR). Free ~0.5GB/proyecto. El default 2026 para "solo quiero Postgres". **Adquirido por Databricks (2025).** **Supabase** = Postgres + Auth + Realtime + Storage + Edge Functions (Firebase-style). Free 500MB DB/50K MAU. **Neon** para Postgres crudo+branching; **Supabase** para backend completo.

## Edge SQLite & PlanetScale
**Turso** (sobre **libSQL**, replica al edge, baja latencia) · **Cloudflare D1** (SQLite-on-Workers, si ya estás en
CF). Ambos para read-heavy/low-latency/edge; ninguno ideal write-heavy relacional. **PlanetScale** (Vitess MySQL,
sin free tier desde 2024, añadió Postgres) = cuando reliability/scale no se negocian. **Contrató al equipo core de Drizzle (mar 2026).** **Convex** = backend reactivo (TS, subscriptions automáticas). **DuckDB** = OLAP embebido (analytics local, Parquet, WASM in-browser).

## Local-first / sync DBs (tema 2026)
**Zero** (Rocicorp, mejor DX, Postgres-backed), **PowerSync** (el más battle-tested, mejor offline mobile), **ElectricSQL** ("Durable Sync" via Shapes), **LiveStore** (event-sourced, Expo), **TanStack DB**.

## ORMs — Drizzle vs Prisma
**Prisma 7** (fin 2025) **removió el query engine Rust** → cliente **pure TypeScript** (~600KB vs 14MB, cold start
1-3s → ~90ms, ~3× más rápido). Arregla años de dolor edge/serverless. **Drizzle** = code-first, SQL transparente (~7KB, 10-20ms init), aún más rápido en todo — decisivo para edge. **Prisma** = tooling que esconde SQL; **Drizzle** = SQL tipado/transparente (ahora PlanetScale-backed).
```ts
export const products = pgTable("products", { id: serial("id").primaryKey(), name: text("name").notNull() })
```

## Gotchas
1. PlanetScale y Convex **sin free tier** — no asumas DB gratis para hobby.
2. El scale-to-zero de Neon añade **cold-start** en la 1ª query tras idle — malo para APIs latencia-crítica salvo keep-warm.
3. Edge SQLite (D1/Turso) es **single-writer/read-replicated** — apps write-heavy relacionales topan límites.
4. El rewrite TS de Prisma 7 es **migración breaking** — audita queries antes de upgrade.
5. Los sync engines son **jóvenes** — semánticas de conflicto difieren mucho (CRDT vs server-auth vs event-sourced).
6. El "Auth+Realtime+Storage gratis" de Supabase puede llevar a lock-in — tu Postgres es portable, los servicios alrededor no.

**Fuentes:** devtoolsacademy.com (serverless SQL) · getautonoma.com (Neon vs Supabase) · makerkit.dev (Drizzle vs Prisma 2026) · johnny.sh/blog (sync engine 2026).
