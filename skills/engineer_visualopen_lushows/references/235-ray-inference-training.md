# 235 · Ray (Serve / Train / Data) para escalar difusión

> Cuando pasas de "un worker = un modelo" a una flota con varias réplicas, GPUs fraccionadas y un pipeline
> de etapas, Ray es el pegamento. Es el plano de control que [[158-autoscaling-inferencia-gpu]] supone debajo.

## Los tres componentes (qué usa cada caso)
| Componente | Para qué | En difusión |
|---|---|---|
| **Ray Serve** | servir modelos como deployments con réplicas + autoscaling | endpoint de img/video, varias réplicas por nodo |
| **Ray Train** | training distribuido (envuelve FSDP/DeepSpeed/torchrun) | full-finetune multi-GPU/multi-nodo |
| **Ray Data** | dataset streaming, batch inference paralela | preprocesar/generar miles de clips sin OOM |

No necesitas los tres. Para un endpoint serverless simple, RunPod basta. Ray gana cuando hay **muchas
réplicas heterogéneas**, **GPUs compartidas**, o un **pipeline multi-etapa** que quieres escalar por etapa.

## GPU fraccionada: el truco de costo
Un modelo chico (un VAE, un upscaler, un SDXL cuantizado) no llena una GPU. Ray deja pedir **fracciones**:
```python
@serve.deployment(ray_actor_options={"num_gpus": 0.25})  # 4 réplicas por GPU
class Upscaler: ...
```
`num_gpus=0.5` → dos réplicas comparten la GPU. Ray **no aísla la VRAM**: es contabilidad lógica, tú
garantizas que 2×el footprint cabe. Sirve para exprimir GPUs caras con modelos que sobran de VRAM.
Para LLM/vLLM, Ray Serve infiere el `per_worker_gpus` desde el placement group.

## Placement groups: reservar topología para multi-GPU
Un modelo que necesita 4 GPUs **en el mismo nodo** (NVLink para sequence-parallel, ver
[[234-context-sequence-parallel-video]]) se reserva con un placement group `STRICT_PACK`:
```python
pg = placement_group([{"GPU": 1, "CPU": 8}] * 4, strategy="STRICT_PACK")
```
- `STRICT_PACK`: las 4 GPUs en **un** nodo (lo que quieres para NVLink).
- `PACK`: intenta empacar, pero permite spillover.
- `SPREAD`: una por nodo (réplicas independientes, no para SP).
El `STRICT_PACK` mal puesto sobre GPUs `SYS` no te da NVLink mágicamente — verifica la topología real ([[232-nccl-tuning-topology]]).

## Pipeline de difusión por etapas (el patrón que paga)
Un job de video tiene etapas con perfiles distintos: **encode texto** (CPU/poco GPU), **denoise DiT**
(GPU pesada), **decode VAE** (GPU media), **interpolación/upscale** (GPU media), **ffmpeg** (CPU). Servirlas
como **deployments separados** con réplicas independientes deja que el cuello (el denoise) escale solo, sin
duplicar el VAE ni el text encoder. Ray Serve compone el grafo (`DeploymentHandle`); Ray Data hace el batch
streaming entre etapas sin materializar todo en memoria.

## Ray Train para el finetune
`TorchTrainer` con `ScalingConfig(num_workers=N, use_gpu=True)` lanza el grupo distribuido por ti (setea
`RANK`/`WORLD_SIZE`, hace el rendezvous) y dentro corres tu loop FSDP/DeepSpeed ([[233-fsdp-deepspeed-diffusion-training]]).
Ventaja sobre `torchrun` pelado: checkpointing tolerante a fallos, reintento de workers caídos, y la misma
abstracción para 1 nodo o 50.

## Autoscaling y cold start
Ray Serve autoscalea por `target_ongoing_requests` y métrica de cola; escala a 0 si lo configuras. El
**cold start** de réplicas de difusión (cargar 20-44GB a VRAM) es brutal → mantén `min_replicas≥1` warm si
el SLA es estricto, o acepta latencia de arranque. Esto es exactamente el trade-off de [[158-autoscaling-inferencia-gpu]],
ahora con Ray como ejecutor. En k8s, Ray corre sobre **KubeRay**, y el gang-scheduling de los workers lo da
Volcano ([[236-gang-topology-aware-scheduling]]).

## Cuándo NO usar Ray
- Un solo modelo, un endpoint, escala-a-0: RunPod serverless directo es más simple y barato.
- Latencia ultra-baja single-request: la capa de actores de Ray añade overhead.
- Equipo sin ops: Ray es un sistema distribuido más que mantener (head node, dashboard, versiones).

## Gotchas
1. `num_gpus` fraccionado **no** limita VRAM: dos réplicas que sumen más de la GPU → OOM. Tú haces la cuenta.
2. Olvidar `STRICT_PACK` para un job NVLink → Ray dispersa las GPUs entre nodos y matas el BW.
3. Versiones: Ray, CUDA y torch tienen que casar igual que en el worker (ver matriz de la skill).
4. Head node como SPOF: en producción dale HA o asume que su caída tumba el scheduling.
5. Escala-a-0 + modelo de 40GB = primer request lento por minutos; mide y decide warm vs frío.

Cruza con [[158-autoscaling-inferencia-gpu]].
