# 159 · Monitoreo y SLO de un servicio de generación GPU

> "El job tardó mucho" no es un incidente accionable. Sin latencia por etapa, profundidad de cola y
> GPU-util, debugueás a ciegas. Un SLO con error-budget convierte el ruido en decisiones.

## Las cuatro señales que importan (un servicio de render no es un web server)

| Señal | Métrica | Fuente | Por qué |
|---|---|---|---|
| **Latencia** | `job_duration_seconds` por etapa (submit→render→entrega) | tu handler (histograma) | p95 es el SLO real |
| **Cola** | `requests_in_queue`, `queue_wait_seconds` | broker/serving | predice saturación antes que GPU-util |
| **Saturación GPU** | `DCGM_FI_DEV_GPU_UTIL`, `DCGM_FI_DEV_FB_USED/FB_FREE` | dcgm-exporter :9400 | OOM y throttle |
| **Errores** | `jobs_failed_total{reason}` (OOM, timeout, CUDA, download) | handler | error-budget |

Más: `DCGM_FI_DEV_MEM_COPY_UTIL`, `DCGM_FI_DEV_GPU_TEMP`, `DCGM_FI_DEV_POWER_USAGE` (throttle térmico/power).
`cost_per_job` derivado = `(job_duration_seconds × $/h_GPU)/3600` → la métrica de negocio (ver [[30-finops-gpu]]).

## Instrumentar el handler (lo que RunPod/serving NO te da gratis)

Exporta un histograma por etapa — la suma esconde dónde se va el tiempo:

```python
from prometheus_client import Histogram, Counter
STAGE = Histogram("job_stage_seconds", "", ["stage"],
    buckets=[1,5,15,30,60,120,300,600])   # ajusta a tu distribución real
FAIL  = Counter("jobs_failed_total", "", ["reason"])

with STAGE.labels("download").time():  fetch_inputs()
with STAGE.labels("warmup").time():    ensure_model_loaded()   # cold vs warm
with STAGE.labels("render").time():    run_pipeline()          # el grueso
with STAGE.labels("upload").time():    push_to_r2(result)
# en except: FAIL.labels(reason=classify(e)).inc()
```

Separar **warmup** (cold-start, ver [[113-network-volume-modelos-grandes]]) de **render** es clave:
sin eso un p95 alto parece "modelo lento" cuando es cold-start. Cruza con [[15-observabilidad-produccion]].

## DCGM en serverless vs k8s

- **k8s**: `dcgm-exporter` como DaemonSet en nodos GPU, scrape Prometheus a `:9400`. Estándar 2026
  (NVIDIA GPU Operator lo despliega). Dashboard GPU oficial de NVIDIA en Grafana.
- **RunPod serverless**: no hay sidecar DCGM. Usá las métricas del endpoint (cola, requests in
  progress, exec time, cold-start count) + tus métricas push del handler a un Pushgateway/OTel
  collector externo (el worker es efímero → push, no scrape).

## SLO y error-budget

Definí 2-3 SLO, no 20. Para un servicio de generación:

```
SLI latencia:  % de jobs con duration ≤ 90s (excluyendo cold-start)   → SLO 95%
SLI éxito:     % de jobs completados sin error                        → SLO 99%
SLI cola:      % de tiempo con queue_wait p95 ≤ 10s                    → SLO 95%
```

Error-budget = `1 − SLO`. 99% éxito mensual = **~7.2h** de presupuesto de fallo. Si lo agotás,
congelás features y atacás fiabilidad. Mide budget-burn-rate, no solo el valor instantáneo.

## Alertas (sobre síntoma, no sobre causa)

| Alerta | Condición | Severidad |
|---|---|---|
| Cola creciente | `queue_wait p95 > 10s` 5min | warn → revisar max_workers ([[158-autoscaling-inferencia-gpu]]) |
| Burn rate rápido | error-budget se consume a 14× | page |
| OOM VRAM | `FB_FREE < 5%` o `jobs_failed{reason="oom"} > 0` | page |
| Throttle térmico | `GPU_TEMP > 85C` sostenido | warn |
| Cost spike | `cost_per_job` > 2× baseline | warn → ver [[30-finops-gpu]] |

Alertá por **multi-window burn rate** (rápida 1h + lenta 6h) para no despertar por blips.

## Tracing del pipeline (submit→render→entrega)

OpenTelemetry: un trace por job, `trace_id` viaja desde la API de submit → broker → worker → webhook
de entrega. Spans: `enqueue`, `cold_start`, `render`, `upload`, `callback`. Propaga el `trace_id` en
el payload del job (el broker no lo propaga solo). Así ves un job lento end-to-end y dónde se atascó.
Para progreso visible al cliente durante el render, cruza con [[140-streaming-progreso-difusion-cliente]].

## Dashboard mínimo

Fila 1: p50/p95/p99 `job_stage_seconds` por etapa (apilado) · jobs/min · tasa de error.
Fila 2: `requests_in_queue` + workers activos · `DCGM_FI_DEV_GPU_UTIL` · `FB_USED`.
Fila 3: error-budget restante · `cost_per_job` · cold-start count.

Cruza con [[15-observabilidad-produccion]], [[30-finops-gpu]] y [[140-streaming-progreso-difusion-cliente]].
