# 45 — Kubernetes a fondo (cuándo y cómo)

## Cuándo se justifica
Para un producto IA/WhatsApp en **Render/Railway**, el veredicto honesto: **probablemente NO necesitas K8s aún.** El
PaaS maneja un servicio web stateless + Postgres + Redis con cero ops. K8s gana su complejidad cuando tienes: (a)
**múltiples servicios** con escala independiente, (b) **inferencia GPU** con scheduling/autoscaling custom, (c)
**workloads batch/cola bursty**, (d) un platform team que pueda dueñar upgrades, RBAC, networking y on-call. Bajo ese umbral, K8s = **deuda operacional.**

## Objetos core
**Pod** (unidad mínima, ≥1 container) → **Deployment** (replica set declarativo, rolling updates) → **Service** (IP/
DNS virtual estable, balancea a pods) → **Ingress** (ruteo HTTP + TLS) → **ConfigMap** (config no-secreta) / **Secret**
(base64, monta como env/file). Usa **`resources.requests`** (reserva del scheduler) y **`limits`** (cap duro; CPU
throttlea, **memoria sobre-limit = OOMKill**).

## GPU scheduling
El kubelet no conoce GPUs nativo. El **NVIDIA device plugin** anuncia `nvidia.com/gpu` como recurso schedulable; los
pods piden `resources.limits: { nvidia.com/gpu: 1 }`. Usa **node selectors / taints+tolerations** para mantener pods
no-GPU fuera de nodos GPU caros. Comparte una GPU vía:
- **Time-slicing** — oversubscribe una GPU en N réplicas lógicas (sin aislamiento de memoria; dev/inferencia ligera).
- **MIG** — instancias particionadas por HW con **aislamiento de memoria + fault** (A100/H100+); multi-tenant producción.

## NVIDIA GPU Operator
No instales drivers a mano. El **GPU Operator** automatiza todo el stack: **driver NVIDIA, Container Toolkit, device
plugin, GPU Feature Discovery, MIG Manager, y DCGM + DCGM-Exporter** (métricas: util, memoria, temp, ECC).

## Autoscaling (lo clave para jobs GPU)
**HPA** escala por CPU/memoria — señal EQUIVOCADA para colas de jobs GPU. Usa **KEDA** para escalar por **queue depth**
(Redis/SQS/RabbitMQ) o **métricas DCGM custom** vía Prometheus (util GPU, throughput) — incluyendo **scale-to-zero**
para que los nodos GPU idle (y su costo) desaparezcan. Empareja con **Cluster Autoscaler / Karpenter** para añadir/quitar nodos GPU.

## Storage & packaging
**PersistentVolume/PVC** para pesos y data stateful (`ReadOnlyMany` para cache de modelo compartido; un modelo grande
en cada cold start mata el throughput — hornéalo en imagen o calienta un volumen compartido). **Helm** charts empaquetan/versionan tus manifests (`values.yaml` por entorno).

## Managed vs self-managed
**GKE/EKS/AKS** manejan el control plane, upgrades, y traen GPU node pools + soporte GPU Operator — muy preferible a
self-manejar el control plane. Self-managed (kubeadm) solo con infra team dedicado u on-prem GPUs.

## Gotchas
1. **Memory `limit` = kill duro**; CPU `limit` solo throttlea. Setea memory requests=limits para predecibilidad; under-request causa OOMKills random.
2. **DCGM-Exporter no atribuye métricas por-container con time-slicing on** — las señales de autoscaling se enturbian; prefiere MIG para métricas por-tenant precisas.
3. **Los nodos GPU son caros y lentos de schedulear** — sin scale-to-zero (KEDA) pagas GPUs idle 24/7; con él, los cold starts añaden minutos (provision + pull + load).
4. **HPA por CPU = señal equivocada** para GPU/cola — usa KEDA por queue depth.
5. **Pinea driver/CUDA/toolkit** vía GPU Operator; driver del nodo ≠ CUDA del container = `CUDA error: no kernel image` críptico en runtime.

**Fuentes:** github.com/NVIDIA/k8s-device-plugin · docs.nvidia.com/datacenter/cloud-native/gpu-operator · learn.microsoft.com/azure/aks (KEDA+DCGM) · spectrocloud.com/blog (GPU Operator).
