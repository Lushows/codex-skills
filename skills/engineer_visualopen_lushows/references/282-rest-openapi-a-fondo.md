# 282 · REST + OpenAPI a fondo (contract-first, paginación, errores RFC 9457)

> [[20-diseno-apis-rest-grpc-graphql]] gradúa REST con el Richardson Maturity Model; esto baja al barro:
> cómo modelar recursos que no son CRUD, versionar sin romper, paginar a escala y escribir el spec primero.

## Recursos: cuando el dominio no es CRUD
Modela **sustantivos** (`/orders/123/items`), nunca verbos. ¿Una acción no-CRUD (refund, publish, retry)?
Tres salidas, en orden de preferencia:
1. **Sub-recurso de estado**: `PUT /orders/123/status {"value":"refunded"}` — idempotente, audita transiciones.
2. **Colección de eventos/acciones**: `POST /orders/123/refunds` — el refund *es* un recurso (tiene id, historial).
3. **Verbo controlado** (`POST /orders/123:cancel`, estilo Google AIP) — último recurso para RPC genuino.
Evita `POST /doRefund`. El sub-recurso te da idempotencia, paginación e historial gratis.

## Versionado sin sangre
- **URI `/v1/`** = default pragmático: visible, cacheable, ruteo trivial (coincide con [[20-diseno-apis-rest-grpc-graphql]]).
- Versiona el **contrato**, no cada campo. Añadir un campo opcional o un enum-value nuevo **no** es breaking
  si los clientes ignoran lo desconocido (regla de tolerancia). Quitar/renombrar/cambiar tipo o cardinalidad **sí**.
- Header `Sunset:` (RFC 8594) + `Deprecation:` para avisar EOL de `/v1` antes de apagarlo.
- Alternativa media: versionado por **media-type** (`Accept: application/vnd.ex.v2+json`) — más limpio, peor tooling.

## Paginación a escala
| Estrategia | Cuándo | Costo |
|---|---|---|
| **Cursor** (`?limit=50&cursor=...`) | default; feeds, listas grandes | O(1), estable bajo writes |
| Offset (`?page=3`) | UIs con "ir a página N", datos chicos | O(n) profundo, salta/duplica filas |
| Keyset puro (`?after_id=&after_ts=`) | máximo throughput | requiere índice `(sort, id)` |

El cursor es un keyset **opaco** (base64 de `(created_at,id)` + sentido). Ordena por clave **única+estable**
o duplicas/saltas filas (gotcha clásico). Devuelve `next_cursor` null al final; no expongas el offset interno.

## Errores: RFC 9457 (Problem Details, obsoleta la 7807)
`Content-Type: application/problem+json`. Campos: `type` (URI doc), `title` (estable, legible), `status`,
`detail` (instancia concreta), `instance`, + extensiones de dominio. **Nunca `200` con `{"error":...}`.**
```json
{ "type":"https://api.ex.com/errors/gpu-busy", "title":"All GPU workers busy",
  "status":503, "detail":"queue depth 42, retry later", "instance":"/jobs/abc", "retry_after_s":30 }
```
Mapea: `400` malformado · `401` no-autenticado vs `403` prohibido · `409` conflicto/versión · `422` validación
semántica · `429` (+`Retry-After`) · `503`. No filtres ids de DB ni stack traces en `detail`.

## Contract-first con OpenAPI 3.1
Escribe el `.yaml` **antes** del código → genera stubs de servidor, **clientes tipados** (orval, openapi-generator)
y docs. OpenAPI 3.1 alinea su schema con **JSON Schema 2020-12** (antes era un dialecto propio) → puedes reusar
el mismo schema para validar request *y* persistencia. `examples` en el spec alimentan mocks (Prism) y tests.

## Contract testing en CI (atrapa breaking antes del deploy)
- **Schemathesis**: fuzzea tu OpenAPI contra el server real → encuentra 500s, violaciones de schema, edge cases.
- **Pact** (consumer-driven): el cliente declara qué espera; el provider verifica en su pipeline → rompe el build
  si cambias el contrato bajo un consumidor vivo. Esencial en microservicios.
- Diff de spec (`oasdiff`) marca cambios breaking automáticamente en el PR.

## Gotchas
1. `PUT` idempotente: no auto-incrementes ni generes ids dentro — usa el id del path.
2. `201 Created` debe traer `Location:` al recurso nuevo; `202 Accepted` para async devuelve URL de polling del job.
3. Cursor que codifica solo `id` rompe si el sort no es por id — codifica **todas** las sort keys.
4. `PATCH` ambiguo: declara JSON Merge Patch (RFC 7386) **o** JSON Patch (RFC 6902), no inventes.
5. OpenAPI que miente (drift spec↔código) es peor que no tenerlo → Schemathesis en CI lo mantiene honesto.

Verificado jun-2026: RFC 9457 vigente; tus drafts no aplican aquí. Cruza con [[20-diseno-apis-rest-grpc-graphql]] y [[283-graphql-a-fondo]].
