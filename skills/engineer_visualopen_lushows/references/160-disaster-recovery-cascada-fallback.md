# 160 · Disaster recovery: cascada self-hosted → API premium

> Tu GPU se va a caer: RunPod sin capacidad en la región, OOM, cold-start eterno, throttle.
> La diferencia entre "servicio degradado" y "caído" es una cascada de fallback con circuit breaker.
> Regla: nunca dejes que un usuario espere el fallo completo de la GPU sin una salida.

## La cascada (capas, de barata a cara)

```
Capa 0  GPU self-hosted (RunPod serverless)          $ — preferida ([[131-runpod-a-fondo-serverless-pods-volumes]])
   │  falla / timeout / circuito abierto
Capa 1  Misma API, GPU en otra región/datacenter     $$  — quita dependencia de región
   │
Capa 2  Calidad degradada (menos steps, menor res)   $   — mismo modelo, más barato/rápido
   │
Capa 3  API premium (Replicate / fal / Higgsfield)   $$$ — cara pero siempre disponible
   │
Capa 4  Encolar async + avisar "te llega en X"       — última red: no perder el job
```

No saltes directo a la API premium: cuesta 5-20× más. Degradar calidad (capa 2) suele salvar el SLA
de éxito sin disparar el costo. Capa 4 (encolar y notificar) evita perder el trabajo del usuario.

## Circuit breaker (no martilles una GPU caída)

Tres estados (estándar 2026): **Closed** (normal) → **Open** (saltó el umbral de fallos, cortás y vas
directo al fallback) → **Half-Open** (tras `reset_timeout`, dejás pasar 1 sonda; éxito → Closed, fallo → Open).

```python
class Breaker:
    def __init__(s, fail_max=5, reset_timeout=30):
        s.fails=0; s.open_until=0; s.fail_max=fail_max; s.reset=reset_timeout
    def allow(s):                     # Half-Open al expirar el timeout
        return time()>=s.open_until
    def ok(s):   s.fails=0; s.open_until=0
    def ko(s):
        s.fails+=1
        if s.fails>=s.fail_max: s.open_until=time()+s.reset   # → Open
```

Un breaker **por capa/proveedor**: si RunPod región-A está Open, seguís intentando región-B antes de
caer a la API premium. Sin breaker, cada request paga el timeout completo de la GPU muerta.

## Timeouts (presupuesto de tiempo, no esperas infinitas)

- **Timeout por capa < timeout total del cliente.** Si el cliente espera 120s y tenés 3 capas, no le
  des 120s a la capa 0. Repartí: capa0 60s → capa1 30s → capa3 20s, con margen.
- **Connect vs read timeout** separados. Cold-start de GPU (minutos) vs API premium (segundos): el
  read-timeout de capa 0 debe contemplar el cold-start o lo vas a abortar sano. Mide el warmup real
  ([[113-network-volume-modelos-grandes]]) y poné el timeout por encima del p99 de warmup.

## Reintentos idempotentes (o duplicás cobros y renders)

Un retry tras timeout puede ejecutar el job **dos veces** (el primero quizá sí corrió). Antibalas:

- **Idempotency-Key** por job (UUID del cliente). El worker deduplica: si ya vio la key con resultado,
  lo devuelve sin re-renderizar. Anthropic y muchas APIs premium soportan idempotency-key nativo — úsalo.
- **Backoff exponencial con jitter**: `wait = base·2^intento + random(0, jitter)` — el jitter evita el
  retry-storm cuando 100 clientes reintentan a la vez sobre una GPU que vuelve.
- Solo reintentes errores **transitorios** (429, 503, timeout, "no capacity"). Un error de validación
  o de prompt no se arregla reintentando — falla rápido. Cruza con [[141-webhooks-hmac-idempotencia-dlq-jobs-gpu]].

```python
for capa in [runpod_a, runpod_b, premium]:
    if not capa.breaker.allow(): continue          # circuito abierto → salta
    for intento in range(3):
        try:
            r = capa.submit(job, idem_key=job.id, timeout=capa.budget)
            capa.breaker.ok(); return r
        except Transient:
            capa.breaker.ko(); sleep(2**intento + random()*0.5)
        except Permanent: raise                     # no reintentar, no degradar
enqueue_async(job); notify(user, "te llega por webhook")   # capa 4
```

## Health checks (detectá antes de que el usuario lo sufra)

- **Liveness**: ¿el worker responde? **Readiness**: ¿el modelo está cargado en VRAM? No enrutes jobs
  a un worker readiness=false (está en cold-start). En k8s, readiness gate sobre "modelo en VRAM".
- **Sonda sintética**: un job trivial cada N min mide el cold-start real y abre el breaker proactivamente
  si la región se degrada, antes de que entre tráfico real.

## Presupuesto de fallback (que la red de seguridad no te quiebre)

La API premium es 5-20× más cara. Pone un **tope diario de gasto en fallback**: al superarlo, capa 3 se
desactiva y caés directo a capa 4 (encolar async) en vez de sangrar dinero. Alertá cuando el % de
tráfico servido por fallback supere ~10% sostenido → la GPU self-hosted tiene un problema estructural,
no un blip. Cruza con [[30-finops-gpu]] y monitoreá la tasa de fallback como SLI ([[159-monitoreo-slo-servicio-gpu]]).

## Para jobs largos: no bloquees, usá async

Render de video/difusión no cabe en un request síncrono con fallback en cascada. El patrón correcto es
submit → poller durable → webhook, y la cascada vive dentro del worker del job, no en el request HTTP
del cliente. Cruza con [[115-async-render-largo-poller-durable]] y [[141-webhooks-hmac-idempotencia-dlq-jobs-gpu]].

Cruza con [[115-async-render-largo-poller-durable]], [[141-webhooks-hmac-idempotencia-dlq-jobs-gpu]] y [[131-runpod-a-fondo-serverless-pods-volumes]].
