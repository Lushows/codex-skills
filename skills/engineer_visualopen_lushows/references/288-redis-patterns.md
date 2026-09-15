# 288 · Redis: cache, locks, rate-limit, streams, pub/sub

> Redis no es "un caché". Es un servidor de estructuras de datos single-thread: cada comando es atómico,
> y eso lo vuelve la navaja suiza para coordinar workers, colas y contadores sin condiciones de carrera.

## Cache patterns (y sus fallas)
**Cache-aside** (lazy): app lee Redis → miss → lee DB → `SET key val EX 300`. El 99% de los casos.
- **Stampede / thundering herd**: 10k requests fallan a la vez al expirar una key caliente → todos pegan a la DB. Mitiga con: TTL + jitter (`EX 300 + rand(0,30)`), o `SET key val NX` para que solo uno recompute (lock de recálculo), o early-recompute probabilístico (XFetch).
- **Penetration**: queries a keys inexistentes pasan siempre a DB → cachea el negativo (`SET key "" EX 60`) o bloom filter.
- **Avalanche**: muchas keys expiran simultáneas → escalona TTLs.

## Distributed lock — hazlo bien o no lo hagas
Un solo nodo: `SET lock:resource <token-aleatorio> NX PX 30000`. El **token único** es obligatorio: para liberar, un script Lua verifica `GET==token` antes de `DEL`, si no liberas el lock de otro que ya expiró:
```lua
if redis.call('get', KEYS[1]) == ARGV[1] then return redis.call('del', KEYS[1]) else return 0 end
```
**Renovación**: si el job dura más que el PX, otro Lua extiende el TTL solo si el token sigue siendo tuyo (watchdog). **Redlock** (quorum sobre N=5 instancias, mayoría 3) sube la disponibilidad, pero es controvertido: asume relojes sincronizados y sin pausas de GC; **no garantiza exclusión mutua bajo pausas STW**. Para corrección dura usa fencing tokens (un contador monótono que el recurso valida), no Redis solo.

## Rate limiting
- **Fixed window**: `INCR key` + `EXPIRE key 60` al primer hit. Simple, pero permite ráfaga 2× en el borde de ventana.
- **Sliding window log**: `ZADD` timestamp, `ZREMRANGEBYSCORE` lo viejo, `ZCARD` cuenta. Preciso, más memoria.
- **Token bucket**: script Lua atómico que rellena tokens por tiempo transcurrido. Lo más usado en API gateways.

## Sorted sets (ZSET) — el caballo de batalla
Leaderboards (`ZADD`/`ZREVRANGE`), colas con prioridad/delay (`score=timestamp`, `ZRANGEBYSCORE` para due jobs), sliding windows. O(log N) inserción. Una ZSET con score=tiempo es una **scheduled queue** sin dependencias extra.

## Streams (cola durable con consumer groups)
A diferencia de pub/sub (fire-and-forget, pierde si nadie escucha), Streams persisten y soportan grupos:
```
XADD orders * type paid amount 50          # append, ID auto = ms-seq
XREADGROUP GROUP workers c1 COUNT 10 STREAMS orders >   # lee no entregados
XACK orders workers <id>                    # confirma procesado
XAUTOCLAIM orders workers c2 60000 0        # rescata mensajes colgados de un worker muerto (PEL)
```
El **PEL** (Pending Entries List) rastrea entregados-no-confirmados → reintentos y dead-letter. Recorta con `XADD ... MAXLEN ~ 100000` o `XTRIM`. Para la mayoría de casos, Streams reemplaza a un broker dedicado (ver [[285-background-jobs-queues-web]]).

## Hash field TTL (Redis 7.4+) y helpers (Redis 8)
7.4 trajo `HEXPIRE`/`HPEXPIRE`/`HTTL`/`HPERSIST`: expiración **por campo** dentro de un hash. Antes tenías que partir un hash de sesión en N keys para dar TTL distinto; ahora un solo hash `session:{id}` con campos que caducan independientes. Redis 8 añade `HGETEX`/`HSETEX`/`HGETDEL` (lee+refresca TTL atómico, lee+borra). Ideal para carritos y sesiones.

## Persistencia y memoria
- **RDB** (snapshot periódico): rápido restart, pierde lo último; **AOF** (append log, `appendfsync everysec`): durabilidad ~1s; producción usa **ambos**.
- `maxmemory` + policy: `allkeys-lru` (caché puro), `volatile-lru` (solo keys con TTL), `noeviction` (rechaza writes — peligroso si lo usas de cola).
- Comandos O(N) que bloquean el hilo único: `KEYS *` (usa `SCAN`), `FLUSHALL`, `SMEMBERS` de sets enormes. Un comando lento congela **todo** el server.

## Gotchas
1. `EXPIRE` separado del `SET` no es atómico → usa `SET k v EX n` en un comando.
2. Pub/sub no es durable: si el subscriber está caído, el mensaje se pierde. Usa Streams.
3. Redis Cluster: operaciones multi-key requieren que las keys compartan hash slot → `{tag}` en el nombre.

Cruza con [[22-caching-cdn]] y [[285-background-jobs-queues-web]].
