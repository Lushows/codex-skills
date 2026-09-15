# 04 — Capa de app/sistemas: gateway, cola, async, caché

> El "control plane" entre la app del usuario y los workers GPU: **API gateway → cola → DB → caché.**
> Concreto, code-level, verificado mid-2026.

## 1. Async Python (worker handler y client/gateway)

**El GIL y el estado 2026.** El GIL serializa bytecode a 1 thread → threads NO dan speedup paralelo para
CPU-bound puro-Python. Free-threaded CPython (PEP 703): **3.13 = experimental** (`python3.13t`, `--disable-gil`,
hit single-thread notable) · **3.14 = soportado pero opcional** (PEP 779). **NO dependas de no-GIL en prod aún.**

| Workload | Usa | Por qué |
|---|---|---|
| Muchos HTTP polls/uploads concurrentes (→RunPod, →R2) | **asyncio** | I/O-bound; 1 thread multiplexa miles de awaits |
| Lib bloqueante sin API async (`boto3`,`requests`,DB sync,PIL) | **threads** vía `asyncio.to_thread`/`run_in_executor` | el GIL se suelta en el syscall bloqueante |
| CPU-bound (pre/post-proceso imagen, hash, ffmpeg in-proc) | **procesos** (`ProcessPoolExecutor`) | evita el GIL, paralelismo real |

```python
sem = asyncio.Semaphore(20)
async with httpx.AsyncClient(timeout=30) as c:
    async def poll(jid):
        async with sem:                      # capa la concurrencia
            return (await c.get(f"{BASE}/status/{jid}", headers=H)).json()
    results = await asyncio.gather(*(poll(j) for j in job_ids))
```
- `asyncio.gather(*aws)` (resultados en orden; `return_exceptions=True` para no abortar al 1er error) ·
  `asyncio.Semaphore(n)` (cap) · `asyncio.to_thread(fn,*a)` (3.9+, lib bloqueante) · `httpx.AsyncClient` (reusar 1).
- **🔴 Bug #1: bloquear el event loop** con un call sync (`time.sleep`, `requests.get`, DB sync, loop CPU). UN call
  bloqueante congela TODAS las corrutinas. Fix: equivalente async o push a thread/process. (`PYTHONASYNCIODEBUG=1`.)

## 2. FastAPI como API gateway

Async (ASGI), validación Pydantic v2, OpenAPI auto, DI. Estándar para este sistema.

```python
@app.post("/jobs", status_code=202, response_model=JobOut)
async def create_job(body: JobIn, response: Response, user=Depends(auth)):
    job = await enqueue(body, user.id)                  # fila a la cola Postgres
    response.headers["Location"] = f"/jobs/{job.id}"
    return JobOut(id=job.id, status="queued")
```
- **🔴 `BackgroundTasks` NO es una cola.** Corre en el MISMO proceso y **muere con él** (deploy/crash/OOM = pierdes
  el job); no sobrevive entre réplicas. Los docs de FastAPI mandan a Celery/cola real para trabajo pesado. Úsalo
  solo para side-effects triviales fire-and-forget. El job GPU va a Postgres/Redis/SQS.
- **Recibir el webhook de RunPod:** endpoint que RunPod POSTea al terminar (reintenta 2 veces más/10s en non-200)
  → tu handler debe ser **idempotente** y devolver 200 rápido. RunPod **NO firma** → protege la URL con secreto y
  busca el job por id en TU DB (no confíes en el body).
- **Streaming a clientes:** SSE con `StreamingResponse` (`media_type="text/event-stream"`) sobre LISTEN/NOTIFY o Redis pub/sub.
- **Auth** `Depends(auth)` · **CORS** `CORSMiddleware` · **rate limit** slowapi (§6).

## 3. Postgres como cola de jobs (deep)

Una tabla Postgres es buena cola hasta escala moderada (cientos-miles jobs/s).

```sql
-- DEQUEUE canónico: FOR UPDATE SKIP LOCKED (cada worker agarra una fila distinta, no se bloquean)
WITH next AS (
  SELECT id FROM jobs
  WHERE status='queued' AND run_at <= now()
  ORDER BY priority DESC, run_at
  FOR UPDATE SKIP LOCKED
  LIMIT 1)
UPDATE jobs j SET status='running', locked_at=now(), attempts=attempts+1
  FROM next WHERE j.id=next.id RETURNING j.*;
```
- **Txn corta** (claim → commit → procesar FUERA de la txn). **Sweeper** reclama colgados: `status='running' AND locked_at < now()-interval '5 min'` → `queued`.
- **Índice parcial** que matchea el dispatch: `CREATE INDEX ... ON jobs(priority DESC, run_at) WHERE status='queued'`.
- **LISTEN/NOTIFY** en vez de busy-poll: `pg_notify('job_ready', id)` al insertar; worker `LISTEN`. Payload ≤8KB,
  no durable (worker offline lo pierde) → combina NOTIFY (latencia) + poll periódico (red de seguridad). asyncpg `add_listener`.
- **Advisory locks** (`pg_advisory_xact_lock(key)`) para "solo 1 worker corre este singleton/cron", NO para el dequeue (SKIP LOCKED es mejor).
- **Idempotencia:** `INSERT ... ON CONFLICT (idempotency_key) DO NOTHING RETURNING id`.
- **Pooling:** `asyncpg.create_pool` / SQLAlchemy QueuePool / **PgBouncer** (en transaction-mode: `statement_cache_size=0`, LISTEN en conexión directa aparte).
- **Graduar a broker** cuando: throughput muy alto (decenas de miles/s), fan-out pub/sub, multi-región, o el churn de la cola daña tu OLTP. Hasta ahí, DB-as-queue gana en simplicidad (enqueue transaccional con tus writes).

## 4. Brokers dedicados

| Broker | Ecosistema | Cuándo |
|---|---|---|
| **Redis + RQ** | Python simple | escala chica/media, ya corres Redis |
| **Redis/RabbitMQ + Celery** | Python batteries | scheduling (beat), retries, chains/groups |
| **Redis + Dramatiq** | Python | Celery-like con API más sana |
| **BullMQ** | Node | gateway en Node |
| **AWS SQS** | managed | en AWS, cero-ops; standard (at-least-once) vs FIFO |
| **Redis Streams** | agnóstico | log durable + consumer groups (`XADD/XREADGROUP/XACK`) sin el peso de Celery |

**Gotchas Celery:** result backend ≠ broker (pon `result_expires` o no lo uses) · **visibility timeout < duración
de la tarea → re-entrega y corre 2× en paralelo** (súbelo sobre tu tarea más larga) · **`worker_prefetch_multiplier`
default 4** bloquea con tareas largas → **ponlo en 1** · `task_acks_late` default OFF (crash pierde la tarea) → ON
+ tarea **idempotente** (puede correr >1 vez).

## 5. Caché

- **Dedup de resultados en Redis:** hashea inputs normalizados → key; cachea `output_url` (la "inferencia" más barata):
  ```python
  key = "out:"+hashlib.sha256(canonical(params).encode()).hexdigest()
  if (url := await r.get(key)): return url
  ...run...; await r.set(key, url, ex=86400)        # TTL matcheado a la retención de R2
  ```
- **🔴 Cache stampede:** al expirar una key caliente, N requests fallan a la vez y disparan N jobs caros. Fix:
  **`SET key val NX EX ttl`** (set-if-not-exists; el ganador computa, los demás esperan) · expiry probabilístico ·
  single-flight (`asyncio` coalescing por instancia + lock Redis entre instancias).
- **Los media van a object store + CDN, NO a Redis:** R2 (S3-compat, sin egress). Headers: outputs inmutables
  content-addressed → `Cache-Control: public, max-age=31536000, immutable`. **Signed vs public:** público (cacheable,
  barato) para no sensible; **presigned** (time-limited) para privado/por-usuario (más difícil de CDN-cachear, el query string varía).

## 6. Rate limiting & backpressure

- **Token bucket** (permite bursts hasta B, suaviza a r/s) = mejor limiter general · **Leaky bucket** (drena a tasa
  fija) cuando el downstream GPU necesita tasa estable.
- En límite: **`429` + `Retry-After`**. FastAPI: **slowapi** (`@limiter.limit("10/minute")`, backed por Redis para límites compartidos entre réplicas).
- **Backpressure GPU-específico:** **profundidad de cola como señal** — si `IN_QUEUE` supera un umbral, devuelve
  `429/503 Retry-After` en admisión (no aceptes trabajo que no puedes servir). **Circuit breaker** gateway↔RunPod
  (abre/fail-fast en errores, half-open para probar, close al sanar). Capa el fan-out con `asyncio.Semaphore`.

## 7. Diseño de API (job async)
- `POST /jobs` → **202** + `Location: /jobs/{id}` + `{id,status}` · `GET /jobs/{id}` → estado (mapea a IN_QUEUE/
  IN_PROGRESS/COMPLETED/FAILED) · `GET /jobs/{id}/stream` → SSE · `DELETE /jobs/{id}` → cancel.
- **`Idempotency-Key` header** → `ON CONFLICT DO NOTHING` → mismo job en retries.
- **Paginación cursor/keyset** (`?after=<cursor>&limit=50`, orden `(created_at,id)`) > OFFSET (estable bajo inserts).
- **Error envelope** consistente (RFC 9457 problem+json): `{"error":{"code","message","request_id","retry_after"}}`.
- **Versioning** `/v1/…`. **Webhooks que TÚ emites a clientes:** firma HMAC-SHA256 (`X-Signature: sha256=...` sobre
  bytes crudos) + `X-Timestamp` (replay window), retry con backoff, dead-letter.

## Gotchas
1. **`BackgroundTasks` tratado como cola durable** — muere con el proceso. Para trabajo pesado: Celery/cola real.
2. **Bloquear el event loop de asyncio** — un `requests.get`/`time.sleep`/`boto3` sync congela TODO. "FastAPI lento bajo carga sin razón" = casi siempre esto.
3. **Visibility timeout de Celery < duración → ejecución doble** en paralelo. Súbelo, `acks_late=True`, prefetch=1, tarea idempotente.
4. **Poll de la tabla sin `SKIP LOCKED`** (o sin índice parcial) → workers se bloquean entre sí / seq scan que empeora. Fix: SKIP LOCKED + índice parcial + LISTEN/NOTIFY.
5. **Sin idempotencia + sin protección de stampede** → retries del cliente Y del webhook de RunPod (hasta 3) **cobran GPU doble**; expiry de key caliente = thundering herd de jobs idénticos. Ambos = dinero real.

**Fuentes:** docs.python.org/3.13/whatsnew · peps.python.org/pep-0779 · fastapi BackgroundTasks ·
postgresql.org SELECT/SKIP LOCKED · docs.celeryq.dev configuration · github.com/laurentS/slowapi · docs.runpod.io send-requests.
