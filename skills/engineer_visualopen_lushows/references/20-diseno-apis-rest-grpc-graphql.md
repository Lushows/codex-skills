# 20 — Diseño de APIs (REST / gRPC / GraphQL)

Modela recursos REST como **sustantivos** (`/orders/123/items`), no verbos; usa los métodos HTTP para semántica
(`GET` safe+idempotente, `PUT`/`DELETE` idempotentes, `POST` ninguno). El **Richardson Maturity Model** te
gradúa: L0 (un RPC), L1 (recursos), L2 (verbos + status codes — *donde vive el 95% de "REST" bien hecho*), L3
(HATEOAS). L3 rara vez vale para clientes propios.

**Status codes bien:** `200`, `201 Created` + `Location`, `202 Accepted` (async), `204 No Content`, `400`
(malformado), `401` (no autenticado) vs `403` (autenticado pero prohibido), `404`, `409` (conflicto/versión),
`422` (validación semántica), `429` (rate limit + `Retry-After`), `503`. **Nunca `200` con `{"error":...}`.**

**Idempotencia:** para `POST` no-idempotente (pagos/órdenes), acepta `Idempotency-Key` header; guarda
key→response 24h → los retries replayean el primer resultado (patrón Stripe).

**Paginación:** prefiere **cursor** (`?limit=50&cursor=...`) sobre offset. Offset es O(n) profundo y salta/duplica
filas bajo writes concurrentes; los cursores son estables y usan el índice. Devuelve `next_cursor`.

**Versioning:** URI (`/v1/`) = default pragmático (visible, cacheable, ruteo trivial). Versiona el *contrato*, no cada campo.

**Error envelope — RFC 9457** (Problem Details, julio 2023, *obsoleta RFC 7807*). `Content-Type: application/problem+json`:
```json
{ "type":"https://api.ex.com/errors/insufficient-funds", "title":"Insufficient funds",
  "status":403, "detail":"Balance 30 < required 50", "instance":"/accounts/12/tx/7", "balance":30 }
```

**Cuándo cada protocolo:**
- **gRPC** — service-to-service interno, baja latencia, streaming, schema estricto (HTTP/2 + Protobuf). Malo por browser (necesita grpc-web).
- **GraphQL** — clientes variados (mobile+web) con over/under-fetching; un endpoint, el cliente elige campos. Costos: cost-limiting, N+1 (DataLoader), caché difícil.
- **REST** — APIs públicas, CRUD simple, caché HTTP, tooling más amplio. **Default.**

**OpenAPI-first:** escribe el spec, genera stubs + clientes tipados + docs. **Contract testing** con Pact (consumer-driven) o Schemathesis (fuzzea tu OpenAPI) atrapa breaking changes en CI.

## Gotchas
1. `PUT` debe ser idempotente — no auto-incrementes adentro.
2. No filtres ids de DB/stack traces en `detail`.
3. Cursor pagination rompe si la sort key no es única+estable — ordena por `(created_at, id)`.
4. GraphQL sin límites de profundidad/costo = vector DoS.

**Fuentes:** rfc-editor.org/rfc/rfc9457.html · martinfowler.com/articles/richardsonMaturityModel · docs.stripe.com/api/idempotent_requests · schemathesis.readthedocs.io.
