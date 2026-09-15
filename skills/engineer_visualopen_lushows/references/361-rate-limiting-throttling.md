# 361 · Rate limiting y throttling (token-bucket distribuido, 429 honesto, sin penalizar al inocente)

> Sin rate limit, un cliente abusivo (o un bug en retry) tira el servicio para todos. El límite no es
> castigo: es el fusible que mantiene el sistema disponible bajo abuso, scraping y picos accidentales.

## Los algoritmos (qué tradeoff hace cada uno)
| Algoritmo | Permite ráfagas | Memoria | Precisión en bordes | Nota |
|---|---|---|---|---|
| **Fixed window** | sí (peligroso) | mínima (1 contador) | mala: 2× en el borde | simple, evítalo en prod |
| **Sliding window log** | no | alta (timestamp por req) | perfecta | caro en RAM a escala |
| **Sliding window counter** | controlada | baja | buena (aproxima) | **default práctico** |
| **Token bucket** | **sí, controlada** | baja (2 números) | buena | ráfagas + tasa sostenida |
| **Leaky bucket** | no (suaviza salida) | baja | buena | caudal constante, encola |

**Token-bucket** es el caballo de batalla: bucket de capacidad `B` (la ráfaga máxima) que se rellena a
`r` tokens/s (la tasa sostenida). Cada request consume 1 token; sin tokens → 429. Permite ráfagas cortas
legítimas (carga de página = 20 requests juntos) pero acota el promedio. **Fixed window** sufre el "border
burst": 100 req al final de un minuto + 100 al inicio del siguiente = 200 en 2s sin violar el límite nominal.

## Por quién limitas (la clave importa)
- **Por API key / usuario**: el correcto para APIs autenticadas; aísla por cuenta. Ver [[274-api-security-ratelimit-keys]].
- **Por IP**: para tráfico anónimo (login, signup). Cuidado: NAT/CGNAT/oficinas comparten IP → castigás
  inocentes. Detrás de proxy/CDN usá `X-Forwarded-For` **confiando solo en el último hop tuyo** (spoofeable).
- **Global / por endpoint**: protege recursos caros (export, search, login) con su propio presupuesto.
- **Tiered**: free 60/min, pro 1000/min — la clave incluye el plan. Combinás varias capas (IP + key + endpoint).

## Distribuido: el estado vive en Redis, no en el pod
Con N instancias, un contador local da N× el límite real. Centralizá en Redis ([[288-redis-patterns]]).
Implementación atómica con **Lua** (un round-trip, sin carrera read-modify-write):
```lua
-- token bucket: KEYS[1]=clave, ARGV={rate, burst, now, requested}
local b = redis.call('HMGET', KEYS[1], 'tokens', 'ts')
local tokens = tonumber(b[1]) or tonumber(ARGV[2])      -- arranca lleno
local ts     = tonumber(b[2]) or tonumber(ARGV[3])
local delta  = math.max(0, tonumber(ARGV[3]) - ts) * tonumber(ARGV[1])
tokens = math.min(tonumber(ARGV[2]), tokens + delta)    -- rellena
local ok = tokens >= tonumber(ARGV[4])
if ok then tokens = tokens - tonumber(ARGV[4]) end
redis.call('HMSET', KEYS[1], 'tokens', tokens, 'ts', ARGV[3])
redis.call('EXPIRE', KEYS[1], math.ceil(tonumber(ARGV[2])/tonumber(ARGV[1])))
return { ok and 1 or 0, tokens }
```
Un fallo de Redis NO debe tumbar el servicio: decidí **fail-open** (deja pasar; disponibilidad > protección)
o **fail-closed** (rechaza; protección > disponibilidad) según el endpoint. Login crítico → closed; lectura → open.

## El 429 honesto (cliente colaborador, no adversario)
```
HTTP/1.1 429 Too Many Requests
Retry-After: 12                     # segundos (o fecha HTTP) — el cliente sabe cuándo reintentar
RateLimit-Limit: 100
RateLimit-Remaining: 0
RateLimit-Reset: 12                 # draft IETF RateLimit headers
```
Sin `Retry-After`, los clientes reintentan a ciegas y amplifican el problema (retry storm). Pedí siempre
**backoff exponencial + jitter** del lado cliente. Distinguí 429 (rate limit, reintentable) de 403 (prohibido, no reintentes).

## Patrones que importan
- **Cost-based**: no todo request vale 1 token. Un export pesado = 50 tokens; un GET barato = 1. Limita por *coste real*.
- **Concurrency limit** (en vuelo simultáneo) además del de tasa — protege recursos que no escalan con RPS (conexiones DB, [[359-database-scaling-sharding]]).
- **Shadow/monitor mode**: despliega el límite contando-sin-bloquear primero; mide cuántos legítimos caerían antes de activar.

## Gotchas
1. `X-Forwarded-For` crudo es spoofeable → un atacante rota IPs falsas y evade. Confía solo en el hop que controlás.
2. Límite por IP en login compartido (oficina/escuela) bloquea a todos → combina con límite por cuenta.
3. Fail-closed con Redis caído = autoinfligís la caída que querías prevenir. Decidí fail-mode por endpoint, conscientemente.
4. TTL ausente en las claves Redis → fuga de memoria con millones de IPs únicas. `EXPIRE` siempre.

Cruza con [[274-api-security-ratelimit-keys]], [[288-redis-patterns]] y [[360-load-testing-web]].
