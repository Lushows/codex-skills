# 19 — Load testing y capacity planning

Para un **job API async** (submit → poll/webhook) sobre workers GPU: ¿cuántos usuarios concurrentes antes de
que latencia/cola revienten, y cuántos workers necesito?

## Locust (Python) — modela el loop submit-then-poll
```python
from locust import HttpUser, task, between
class JobUser(HttpUser):
    wait_time = between(1, 3)
    @task
    def submit_and_poll(self):
        jid = self.client.post("/jobs", json={"prompt":"a cat"}).json()["id"]
        for _ in range(60):
            r = self.client.get(f"/jobs/{jid}", name="/jobs/[id]")   # agrupa la URL
            if r.json()["status"] == "done": break
            self.wait()
```

## k6 (JS) — fuerte en concurrencia + thresholds (SLOs que fallan el run)
```javascript
export const options = {
  scenarios: { ramp: { executor: 'ramping-arrival-rate', startRate: 5, timeUnit: '1s',
    stages: [{target: 50, duration: '2m'}] } },
  thresholds: { http_req_duration: ['p(95)<500','p(99)<5000'], http_req_failed: ['rate<0.01'] } };
```
Usa **arrival-rate executors** para forzar un RPS objetivo independiente de la latencia (un sistema lento no
throttlea artificialmente tu carga — clave para hallar el punto de quiebre).

## Qué medir
Latencia **p50/p95/p99** (p95 = tu SLA, p99 = dolor de cola), **throughput** (jobs/s), **error rate bajo carga**,
y — único de async — **profundidad/espera de cola**. Plotea todo vs carga ofrecida; la rodilla donde p99 y la cola
disparan = tu techo de capacidad.

## Concurrencia → workers (Ley de Little)
**L = λ × W:** jobs promedio en sistema = tasa de llegada × tiempo en sistema. Si λ=20 jobs/s y cada job W=8s
end-to-end, necesitas L=160 jobs en vuelo. Con 1 job por worker GPU = **~160 workers** para cola ≈0 (redondea por
varianza). Convierte un target de latencia + forecast de tráfico directo en un nº de workers.

## Impacto del cold start
En GPU serverless, un worker escalado-a-idle tarda decenas de seg en pull+load. En un spike, los cold starts
inflan W (y L) → necesitas MÁS workers que la mate de steady-state, o un piso caliente (`min workers > 0`) para
paths latencia-sensibles. **Load-testea desde frío** para ver la cola real del 1er request.

## Autoscaling triggers
La mejor señal para trabajo GPU async es **queue delay / queue depth**, no CPU. Escala cuando la edad del
oldest-pending o el largo de cola cruza un umbral; capa con RunPod **max workers** para acotar costo. Ata el
trigger al SLO ("queue wait p95 < 5s").

## Chaos & soak
**Soak:** carga moderada por horas → atrapa fragmentación VRAM/leaks que un test de 5 min no ve. **Chaos:** mata
workers a mitad de job, tira el broker, inyecta latencia → verifica retries/idempotencia/DLQ y degradación elegante.

## Gotchas
1. Herramientas HTTP miden transporte, no calidad — k6/Locust reportan "éxito" en una generación basura/truncada → añade un content check.
2. URLs por-id (`/jobs/abc123`) explotan la cardinalidad de métricas — usa `name=`/URLs agrupadas.
3. Tests closed-model (`constant-vus`) sub-cargan un sistema lento; usa **arrival-rate** para hallar capacidad real.
4. La Ley de Little asume steady state — tráfico bursty necesita headroom de cola sobre L.
5. Ignorar cold starts hace tu plan de capacidad optimista por un orden de magnitud en spikes.

**Fuentes:** oneuptime.com/blog (k6 thresholds SLOs) · blog.premai.io (load testing LLMs 2026) · yrkan.com/blog (Locust guide).
