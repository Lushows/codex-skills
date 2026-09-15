# 358 · Estrategia de caching multi-capa (cada capa con su TTL y su invalidación)

> El cache no es una capa: son 4 (browser → CDN → app → DB) y cada una falla distinto.
> El 90% de los bugs de cache son de **invalidación** y de **stampede**, no de hit-rate.

## Las 4 capas (latencia y a quién protege)
| Capa | Vive en | TTL típico | Invalidación | Protege a |
|---|---|---|---|---|
| Browser | disco del cliente | min–año (assets) | hash en el nombre del archivo | red + todo lo de abajo |
| CDN edge | PoP cercano | s–días | purge por tag/path, soft-purge | tu origin |
| App | Redis/Memcached | s–min | key delete, versioned key | la DB |
| DB/query | buffer pool, matview | varía | refresh, trigger | el disco |

Regla: cuanto más cerca del usuario, más barato el hit y más difícil la invalidación. Empujá el cache
hacia el borde lo que puedas, pero solo lo que puedas **invalidar con confianza**.

## Browser: immutable + content-hash
```
Cache-Control: public, max-age=31536000, immutable   # app.4f9a.js — el hash cambia con el contenido
Cache-Control: no-cache                               # index.html — revalida siempre (ETag)
```
`immutable` evita revalidaciones condicionales (304) que igual cuestan un round-trip. HTML nunca immutable.

## CDN: stale-while-revalidate es el caballo de batalla
```
Cache-Control: public, s-maxage=60, stale-while-revalidate=600
```
Sirve contenido viejo (hasta 600s) **mientras** revalida en background → el usuario nunca espera al origin.
Ver [[304-cdn-caching-strategy]] y [[22-caching-cdn]] para purge por tag (Fastly/Cloudflare) vs path.

## App (Redis): claves, TTL, jitter
- **Clave** = namespace + entidad + versión + variante: `v3:user:42:profile:es`. Versionar el prefijo
  invalida en masa sin escanear (`SCAN` es O(n) y bloquea). Bumpeás `v3`→`v4` y el viejo expira solo.
- **TTL siempre** (incluso "permanente") como red de seguridad contra fugas de memoria.
- **Jitter**: TTL = base ± rand(10%). Sin jitter, mil claves cacheadas en el mismo deploy expiran
  *al mismo segundo* → stampede sincronizado.

## Stampede / thundering herd (el fallo que mata la DB)
Una clave caliente expira → N requests concurrentes pegan a la DB a la vez. Tres defensas, combinables:
1. **Single-flight / request coalescing**: solo 1 request recomputa; el resto espera y comparte el
   resultado. La ventana de riesgo es ~200ms tras expirar — en-proceso suele bastar (95%+ son hits).
2. **Probabilistic early expiration (XFetch)**: cada proceso decide *independientemente* recomputar
   *antes* de expirar, con probabilidad creciente al acercarse al TTL → desincroniza la expiración.
3. **Distributed lock** (`SET key val NX PX 5000`): serializa el rebuild entre procesos/máquinas.
   Caro (round-trip extra), úsalo solo para claves caras y muy calientes.

## Patrones de escritura
- **Cache-aside** (lazy): leé cache→miss→DB→poblá. Default. Riesgo: dato viejo si no invalidás al escribir.
- **Write-through**: escribís cache+DB juntos. Consistente, más latencia de escritura.
- **Write-behind**: escribís cache, async a DB. Rápido pero podés perder datos en crash.
- Invalidación al escribir: **delete, no update** la clave (evita carreras read-modify-write).

## Gotchas
1. Cachear respuestas de error/empty con TTL largo (negative caching mal hecho) propaga el fallo.
2. Cachear por usuario sin la variante en la clave → fuga de datos entre cuentas (incidente de seguridad).
3. `Vary: Cookie` en CDN destruye el hit-rate (cada cookie = entrada distinta). Normalizá antes del edge.
4. Sin métrica de hit-rate por capa volás a ciegas — instrumentá hits/misses/stampedes.

Cruza con [[22-caching-cdn]], [[304-cdn-caching-strategy]], [[288-redis-patterns]] y [[357-web-performance-core-web-vitals]].
