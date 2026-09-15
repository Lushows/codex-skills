# 158 · Autoscaling de inferencia GPU (escalar sin quemar idle ni morir en ráfaga)

> La GPU cuesta ~$2-4/h corriendo en vacío. Escalar tarde mata la latencia p95; escalar
> de más sangra dinero. El truco es elegir la señal correcta (cola, no CPU) y aceptar el cold-start.

## Las dos filosofías

| | Scale-to-zero | Warm pool (min workers ≥ 1) |
|---|---|---|
| Costo idle | $0 | min_workers × $/h × 24 |
| Cold-start primer request | 25-40 min (modelo grande, ver [[113-network-volume-modelos-grandes]]) | ~0 |
| Uso ideal | tráfico esporádico, jobs largos async | demo en vivo, SLA latencia estricto |
| Riesgo | usuario espera el frío | pagas la GPU dormida |

Regla práctica: si el job ya dura minutos (video/difusión), el cold-start se diluye → **scale-to-zero**.
Si respondes en <5s y hay SLA, paga **1 worker warm** y deja que el resto escale a 0.

## RunPod serverless: las palancas reales (2026)

Dos estrategias en *Endpoint → Scaling* — son excluyentes:

- **Queue Delay** (default): añade worker cuando un request lleva en cola más que el umbral
  (default **4s**). Tolera latencia → mayor utilización, menos workers. Conservador.
- **Request Count**: agresivo. Workers deseados = `ceil((requestsInQueue + requestsInProgress) / scalerValue)`.
  `scalerValue=1` → 1 worker por request pendiente (máxima respuesta, máximo costo).

```
Active (min) workers   = 0   → scale-to-zero puro (paga cold-start)
                       = 1   → warm pool (1 GPU siempre lista)
Max workers            = techo de concurrencia. Si la cola crece sin parar → max muy bajo.
Idle timeout           = seg que el worker vive sin jobs antes de apagarse (sube si hay ráfagas
                         seguidas: evita apagar-y-reencender = thrashing de cold-starts)
Flashboot              = cachea el estado del worker → cold-start mucho menor en re-arranques
```

Sizing: `max_workers` = peak concurrente esperado. Para jobs de 1 video, `scalerValue=1` +
queue-delay bajo da p95 sano. Para batch tolerante, queue-delay 6-10s ahorra GPUs.
[no verificado] el SDK runpod-python >1.7.10 tuvo un bug enviando todo a un solo worker (issue #432) —
fija versión y valida que la ráfaga reparta.

## KEDA en Kubernetes (self-hosted, control total)

KEDA es el estándar 2026 para **scale-to-zero** en k8s (el HPA nativo no baja a 0). Ver [[45-kubernetes-a-fondo]].

- **Señal por cola** (preferida): scaler `prometheus` sobre `requests_in_queue` de tu serving
  (vLLM/Triton/ComfyUI). Escala por trabajo pendiente, no por GPU-util (que va a 100% y satura tarde).
- **Señal por GPU**: scaler prometheus sobre `DCGM_FI_DEV_GPU_UTIL` del dcgm-exporter
  (KEDA 2.19+; thresholds típicos 75% target / 50% activation).
- **HTTP add-on** (`http-add-on`, beta): escala por RPS HTTP, útil para inferencia síncrona.
- **External scaler gRPC**: DaemonSet que lee NVML local y sirve métricas a KEDA — patrón CNCF 2026
  para autoscalar vLLM/Triton incluyendo a 0.

```yaml
# ScaledObject: escala por profundidad de cola, 0→N
spec:
  minReplicaCount: 0          # scale-to-zero
  maxReplicaCount: 8
  cooldownPeriod: 300         # espera antes de bajar a 0 (evita thrashing)
  triggers:
  - type: prometheus
    metadata:
      query: sum(requests_in_queue)   # NO uses gpu_util como señal primaria
      threshold: "4"                  # ~requests por réplica
```

KEDA solo activa el pod; el **nodo GPU** lo provee Cluster Autoscaler/Karpenter (cold-start real =
arranque de pod + pull de imagen + carga a VRAM; con nodo nuevo súmale el aprovisionamiento del nodo).

## Cold-start vs idle: la decisión de plata

- **Pre-warming programado**: 1 worker warm en horario pico, scale-to-zero de madrugada (cron/schedule).
- **Pin de imagen + pesos en volumen** mata el grueso del frío (ver [[113-network-volume-modelos-grandes]]).
- **Ráfagas**: sube `idle_timeout` para no apagar entre requests cercanos. Mide el intervalo real entre jobs.
- Nunca escales inferencia GPU por **CPU%** ni **memoria del contenedor**: no correlacionan con saturación
  de la GPU. Señal = profundidad de cola o tiempo en cola.

## Capacity planning

p95 objetivo → mide throughput por worker (jobs/min) bajo carga → `workers = ceil(peak_RPS × dur_job / 60)`.
Valida con prueba de carga real antes de fijar `max`. Cruza con [[19-load-testing-capacity-planning]].

Cruza con [[131-runpod-a-fondo-serverless-pods-volumes]], [[45-kubernetes-a-fondo]], [[19-load-testing-capacity-planning]] y [[30-finops-gpu]].
