# 97 — Backend frameworks modernos (2026)

El story 2026 es **Web-Standards-first, TypeScript-native, multi-runtime, typesafe end-to-end.**

## Hono — el estándar edge-native
De 1K downloads/semana (2022) a **~20M/semana (2026)**. Superpoder: **portabilidad** — el *mismo código* corre en
Cloudflare Workers, Deno, Bun, Node, Lambda sin cambios (sobre Web Standard `Request`/`Response`). Middleware
built-in (`hono/logger/cors/jwt/rate-limiter`) + **Hono RPC** (clientes tipados). El reemplazo de Express para la era edge.
```ts
import { Hono } from "hono"; const app = new Hono()
app.get("/products/:id", (c) => c.json({ id: c.req.param("id") }))
export default app    // corre en Workers, Bun, Deno, Node, Lambda
```

## Elysia, tRPC, Encore, Nitro
- **Elysia** (Bun-first) — **~2.3× más rápido que Hono en Bun**, end-to-end types sin codegen vía **Eden** client. Ya NO es Bun-only (Web-Standard). Para apps Bun-first con throughput máximo.
- **tRPC** — APIs tipadas cliente↔server **sin codegen ni OpenAPI** (tus tipos TS SON el contrato). Para monorepos full-TS (Next+tRPC). Tradeoff: TS-a-TS only (no API pública/políglota).
- **Encore** — **infra-from-code**: declaras DBs/Pub-Sub/cron/servicios en TS y Encore los provisiona. ~9× Express, ~3× Hono (runtime Rust). Para backend *systems*, no solo APIs.
- **Nitro** — server layer universal (powerea Nuxt/Analog/TanStack Start). Para construir un framework o deploy-anywhere.

## Runtimes & Python
**Bun** (all-in-one Zig, preferido para Elysia) · **Deno 2** (compat npm/Node full, secure-by-default) · **Node** (default seguro). Python: **FastAPI** domina; **Litestar** es el challenger moderno (más rápido, más batteries). **Tendencia "typesafe full-stack":** tipos fluyen DB→server→client sin sync manual (Drizzle → tRPC/Eden/Hono RPC → React).

## Gotchas
1. La portabilidad de Hono es real pero middleware que toca APIs runtime-específicas (Node `fs`, crypto nativo) rompe el "runs everywhere" — quédate en Web Standard.
2. El peak de Elysia es **Bun-specific**; en Node pierdes mucho del edge.
3. tRPC **no es API pública** — no la expongas a terceros/no-TS; usa Hono/OpenAPI para eso.
4. El infra-from-code de Encore es potente pero **lock-in opinado** — migrar = reescribir infra.
5. Bun en prod aún tiene gaps de **native-module** — testea tu árbol de deps completo.
6. End-to-end types en monorepo son geniales hasta que el **type-check de build se vuelve lento** a escala.

**Fuentes:** pkgpulse.com/guides (Hono vs Elysia vs Nitro 2026) · encore.dev/articles · zenn.dev (typesafe APIs tRPC/Hono/Elysia).
