# 22 — Caching & CDN

Capas, rápido→lento: **browser cache** (headers HTTP) → **CDN/edge** → **app cache** (Redis/in-process) → **DB**.
Cachea tan cerca del usuario como la frescura lo permita.

## Patrones Redis
- **Cache-aside (lazy):** app checa Redis; miss → lee DB → `SET` con TTL. El más común. Riesgo: stale hasta TTL.
- **Write-through:** escribe DB *y* cache juntos — fresco pero writes más lentos.
- **Write-behind:** escribe cache, async-flush a DB — rápido pero riesgo de pérdida en crash.
```python
v = r.get(key)
if v is None: v = db.fetch(key); r.set(key, v, ex=300)   # TTL 5 min
```

## Eviction (`maxmemory-policy`)
`allkeys-lru` (cache general) · `allkeys-lfu` (acceso sesgado — mantiene keys calientes) · `volatile-ttl` ·
`noeviction` (rechaza writes — si Redis es store primario). **LFU > LRU** cuando un set chico de keys domina.

## Protección de stampede / dogpile
Cuando una key caliente expira, miles de requests pegan a la DB a la vez:
1. **Single-flight / mutex lock:** el 1er miss toma un lock corto (`SET lock NX EX 5`), recomputa, otros esperan/sirven stale.
2. **Early expiration probabilística (XFetch):** recomputa *antes* del TTL con probabilidad creciente → uno refresca mientras otros sirven cache.
3. **Stale-while-revalidate:** sirve stale, refresca en background.

## CDN (Cloudflare / R2)
Maneja con `Cache-Control`. Assets versionados → filenames con content-hash (`app.4f9a.js`) +
`Cache-Control: public, max-age=31536000, immutable` (nunca revalida, cache-bust cambiando el filename). HTML/API
→ `no-cache` o `s-maxage` corto + `stale-while-revalidate`. **Invalidación:** purge por URL, o **tag/surrogate-key
purge** (Cloudflare Cache-Tag) para grupos. **Signed URLs** (R2/S3 presigned, expiry corto) para privado/expirable.

## Tradeoffs de edge caching
Genial para estático + GETs cacheables; inútil para respuestas personalizadas/auth'd (explota la cache key).
`Vary: Cookie` suele destruir el hit rate. Edge KV (Cloudflare Workers KV) es eventualmente consistente (~seg de
propagación global) — no para contadores de consistencia fuerte.

## Gotchas
1. Cachear respuestas autenticadas en un CDN compartido puede filtrar data de un usuario a otro — `Cache-Control: private`.
2. Caché solo-TTL causa thundering herds; añade jitter a los TTLs.
3. `immutable` + filename no-hasheado = usuarios atascados en JS viejo por un año.
4. `KEYS *` en producción bloquea el thread único de Redis — usa `SCAN`.

**Fuentes:** developer.mozilla.org (Cache-Control) · redis.io/docs (eviction) · developers.cloudflare.com/cache (purge by tags) · vldb.org/pvldb/vol8/p886-vattani (XFetch).
