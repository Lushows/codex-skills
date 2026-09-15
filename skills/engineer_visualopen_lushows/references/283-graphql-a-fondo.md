# 283 · GraphQL a fondo (schema, resolvers, N+1, federation, vs REST)

> [[20-diseno-apis-rest-grpc-graphql]] dice *cuándo* GraphQL (clientes variados, over/under-fetching);
> esto baja al *cómo*: diseñar el schema, matar el N+1, escalar con federation y no abrir un DoS.

## Schema-first: el contrato es el SDL
El **schema** (SDL) es la fuente de verdad — diséñalo por **caso de uso del cliente**, no espejando tablas.
- **Nullability deliberada**: cada `!` es una promesa. Un campo non-null que falla **propaga el null hacia arriba**
  hasta el ancestro nullable más cercano, anulando hermanos válidos. Default: campos nullable; non-null solo lo garantizado.
- **Conexiones (Relay)**: listas paginables como `edges { node, cursor }` + `pageInfo` → cursor, no offset (cf. [[282-rest-openapi-a-fondo]]).
- **Enums e interfaces** sobre strings libres; **input types** separados de output types.
- **Mutations** devuelven un payload (`{ ok, entity, errors }`), no el scalar pelado → extensible sin breaking.

## Resolvers y el N+1 (el pecado capital)
Cada campo es un resolver. Una query `posts { author { name } }` con 50 posts dispara **1 + 50** queries a DB.
**DataLoader** lo arregla: batchea las claves de un mismo tick del event-loop en **un** `WHERE id IN (...)`
y cachea por request. Un loader por entidad-por-request (no global → cache stale + fugas entre usuarios).
Mide con un trace; el N+1 es invisible en código y mortal en prod.

## Costos que REST no tiene
| Problema | Mitigación |
|---|---|
| Query arbitraria → **DoS** por profundidad/anchura | depth limit + **cost analysis** (puntos por campo/conexión) + `graphql-armor` |
| Caché HTTP no aplica (todo es `POST /graphql`) | **persisted queries** (hash→query, `GET` cacheable en CDN) — cf. [[22-caching-cdn]] |
| Errores parciales | `data` + `errors[]` coexisten; un error no aborta toda la respuesta (a menos que propague por non-null) |
| Introspección abierta filtra el schema | desactívala en prod o gátéala por auth |

**APQ (Automatic Persisted Queries)**: el cliente manda el hash; si el server no lo conoce, reenvía la query
completa una vez. Reduce payload y permite `GET` cacheable → recupera la caché de borde que REST tiene gratis.

## Federation: del monolito a subgraphs
Cuando un schema crece entre equipos, **Apollo Federation v2** es el target estándar (verificado jun-2026; el
GraphQL Foundation *Composite Schemas Working Group* —Apollo, ChilliCream, Hasura, Netflix, The Guild— está
estandarizando el spec). Cada equipo publica un **subgraph**; un **router/gateway** compone el **supergraph**.
- `@key(fields:"id")` define la clave de entidad; un subgraph **extiende** un tipo de otro con `@external`/`@requires`.
- El router planifica: resuelve cada campo en su subgraph y une por la `@key` (un fetch por subgraph, no N+1 entre servicios).
- Alternativas al gateway de Apollo: **Cosmo** (WunderGraph), **Hive** (The Guild), **Grafbase** — mismo spec, distinto runtime.

## ¿GraphQL o REST? (decisión honesta)
- **GraphQL**: muchos clientes heterogéneos (mobile+web+partners) con necesidades de datos divergentes; grafo
  de relaciones profundo; quieres un solo round-trip para vistas compuestas.
- **REST** ([[282-rest-openapi-a-fondo]]): CRUD simple, API pública, caché HTTP de borde, tooling máximo. **Default.**
- **Híbrido común y sano**: REST para CRUD/webhooks/uploads; GraphQL como capa de lectura/BFF agregadora encima.

## Gotchas
1. Non-null mal puesto = un error nulea media respuesta — reserva `!` para invariantes reales.
2. DataLoader **por request**, nunca singleton → fuga datos entre usuarios y cachea stale.
3. Sin depth/cost limit, una query anidada tumba el server — es un vector DoS, no teórico.
4. Mutations que devuelven scalars no escalan; devuelve payload object desde el día 1.
5. Federation sin contract checks (`rover subgraph check`) → un subgraph rompe el supergraph en deploy.

Cruza con [[20-diseno-apis-rest-grpc-graphql]] y [[282-rest-openapi-a-fondo]].
