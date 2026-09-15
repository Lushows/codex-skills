# 15 — Observabilidad de producción

Tres pilares: **métricas** (time-series numéricas baratas, "¿está sano?"), **logs** (eventos discretos, "¿qué
pasó exactamente?"), **traces** (caminos causales, "¿dónde está la latencia?"). Para un stack GPU
(gateway → cola → worker), quieres los tres correlacionados por un `request_id`/`trace_id` compartido.

## Logging estructurado JSON
Nunca texto libre en prod — emite JSON queryable. `structlog` o `python-json-logger`. Bindea un correlation id 1 vez y propágalo:
```python
import structlog
structlog.configure(processors=[structlog.contextvars.merge_contextvars,
    structlog.processors.add_log_level, structlog.processors.TimeStamper(fmt="iso"),
    structlog.processors.JSONRenderer()])
log = structlog.get_logger()
structlog.contextvars.bind_contextvars(request_id=rid, job_id=job_id)   # middleware FastAPI
log.info("inference.start", model="longcat-1.5", prompt_tokens=812)
```

## Prometheus + Grafana
Instrumenta FastAPI con `prometheus-fastapi-instrumentator` (**8.0.0**, requiere Python ≥3.10):
```python
from prometheus_fastapi_instrumentator import Instrumentator
Instrumentator().instrument(app).expose(app)   # sirve /metrics
```
Las **4 golden signals** (Google SRE): **latency** (split éxito vs error, histogramas p50/p95/p99), **traffic**
(req/s), **errors** (5xx + jobs fallidos), **saturation** (profundidad de cola, VRAM/SM util). **RED** (Rate/
Errors/Duration) para servicios; **USE** (Utilization/Saturation/Errors) para recursos como la GPU.

## Métricas GPU vía DCGM-exporter
`dcgm-exporter` expone Prometheus en `:9400/metrics`. Para tensor-core debes habilitar profiling metrics en CSV
custom (+ `SYS_ADMIN`). Campos clave: `DCGM_FI_DEV_GPU_UTIL` (grueso), `DCGM_FI_PROF_SM_ACTIVE` (occupancy),
`DCGM_FI_PROF_PIPE_TENSOR_ACTIVE` (¿tensor cores ocupados?), `DCGM_FI_DEV_FB_USED/FREE` (VRAM), `...POWER_USAGE`, `...GPU_TEMP`.

## Error tracking — Sentry
`sentry-sdk` 2.x auto-habilita la integración FastAPI. Setea **release** (errores → deploy); breadcrumbs dan el rastro:
```python
sentry_sdk.init(dsn=DSN, release="worker@"+GIT_SHA, traces_sample_rate=0.1)  # enable_tracing deprecado
```

## OpenTelemetry
`opentelemetry-api/-sdk/-exporter-otlp` para emitir spans por **OTLP**, propagando **W3C `traceparent`** de
gateway a worker → un trace abarca ambos. Manda a **Jaeger v2** (sobre OTel Collector, OTLP nativo) o **Grafana Tempo**.

## Alerting
Alertmanager rutea/dedupea/silencia. **Alerta de SÍNTOMAS, no causas** (page por "p99 > 5s" o "error budget
quemándose", no "CPU 90%"). Define **SLOs** + **error budgets**; multi-window burn-rate para evitar ruido.

## Gotchas
1. `expose()` añade un `/metrics` sin auth — firewalléalo.
2. Las métricas tensor-core de DCGM devuelven 0 en silencio sin profiling + `SYS_ADMIN`.
3. Labels de alta cardinalidad (por-usuario, por-prompt) revientan la memoria de Prometheus — nunca label por request id.
4. `traces_sample_rate=1.0` en prod es caro y te rate-limita en Sentry — samplea.
5. Sin propagación explícita de contexto, gateway y worker producen 2 traces desconectados.

**Fuentes:** pypi.org/project/prometheus-fastapi-instrumentator · github.com/NVIDIA/dcgm-exporter · docs.sentry.io/platforms/python/integrations/fastapi · opentelemetry.io/docs/languages/python.
