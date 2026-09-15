# 236 · Gang scheduling y topology-aware para jobs multi-GPU (Volcano)

> Un job de N GPUs que arranca con N-1 pods cuelga a todos y desperdicia las GPUs reservadas.
> Gang scheduling lo evita; topology-aware además las pone CERCA. Es la capa de batch que [[45-kubernetes-a-fondo]] no cubre.

## Por qué el scheduler default de k8s no sirve para esto
El kube-scheduler coloca pods **uno a uno**. Para un training distribuido de 8 pods/8 GPUs, va asignando
los que caben; si solo hay 6 GPUs libres, arranca 6 pods que se **bloquean** en el `init_process_group`
esperando a los 2 que nunca llegan. Resultado: 6 GPUs caras reservadas, ocupadas, sin trabajar, y posible
**deadlock de recursos** si otro job hace lo mismo. Necesitas scheduling **all-or-nothing**.

## Gang scheduling: todo o nada
**Volcano** (scheduler de batch sobre k8s, donado a CNCF) introduce el `PodGroup` con `minMember`: el job
solo se programa cuando hay recursos para **todos** sus miembros a la vez; si no, **ninguno** arranca y el
job espera en cola. Adiós a los pods zombis esperando peers.
```yaml
apiVersion: scheduling.volcano.sh/v1beta1
kind: PodGroup
spec:
  minMember: 8            # los 8 pods entran juntos o ninguno
  queue: training
  minResources: { nvidia.com/gpu: 8 }
```
Soporta **two-level gang** (Job y SubJob atómicos), colas con fair-share y prioridad, y preemption. Para
Ray sobre k8s, **KubeRay se integra con Volcano** para que el RayCluster entero respete el gang.

## Topology-aware: que las GPUs estén CERCA
Programar 8 GPUs "donde sea" puede dejarlas repartidas en 4 nodos cruzando red lenta → el all-reduce se
vuelve el cuello (recuerda [[232-nccl-tuning-topology]]: un par `SYS` o inter-nodo cuesta 2-3x). Volcano
modela la red con **HyperNode**:
- Un **HyperNode** = grupo de nodos (o sub-dominios) con **mismo BW/latencia** entre ellos.
- Tienen **tiers**: tier bajo = dominio más apretado (mismo switch / NVLink domain); tier alto = más lejos.
- El plugin puntúa: **cuanto más bajo el tier que contiene todo el job, mayor el score** → el scheduler
  prefiere empacar el job dentro del HyperNode más apretado posible.
- **Auto-discovery** del topology vía ConfigMap desde fuentes **UFM** (InfiniBand/NVIDIA), **RoCE** o **label**.

```yaml
# en el PodGroup / Job: exigir que todo el gang quepa en un tier dado
spec:
  networkTopology:
    mode: hard            # hard = obligatorio; soft = preferencia
    highestTierAllowed: 2 # no disperses más allá del tier 2
```
`hard` rechaza colocar el job si no cabe en ese tier (puede quedar pending); `soft` lo prefiere pero cede.

## El combo que de verdad quieres
Para un finetune de DiT de video con sequence-parallel ([[234-context-sequence-parallel-video]]):
1. **Gang** (`minMember=world_size`) → no arranca a medias.
2. **Topology-aware `hard`, tier bajo** → las GPUs del grupo NVLink/sequence-parallel caen en el mismo dominio.
3. **Colas con prioridad** → los jobs de prod expulsan a los experimentales (preemption) sin fragmentar.
Sin (1) desperdicias GPUs en pods colgados; sin (2) tienes las 8 GPUs pero el all-reduce las vuelve inútiles.

## Alternativas / vecinos
- **Kueue** (k8s nativo): gestión de colas y admisión por lotes; combinable con gang, menos topología fina.
- **Run:ai / Slurm**: en clusters dedicados ofrecen gang + topology maduros; Slurm sigue siendo el estándar HPC.
- En **cloud serverless** (RunPod) nada de esto aplica: no controlas el scheduler. Esto es para tu **propio** k8s con GPUs.

## Gotchas
1. `minMember` mal puesto (≠ world_size) → o nunca arranca, o arranca incompleto: cuélalo con el lanzador.
2. Topology `hard` + cluster fragmentado → job **pending** indefinido; usa `soft` o desfragmenta colas.
3. HyperNodes con labels manuales mal mapeados mienten sobre la topología → el scheduler empaca "cerca" lo que está lejos.
4. Olvidar `minResources` → el PodGroup admite sin garantizar GPUs, reapareciendo el problema que querías matar.
5. Gang sin colas/preemption → un job grande pending bloquea a los chicos (head-of-line). Configura prioridades.

Cruza con [[45-kubernetes-a-fondo]] y [[234-context-sequence-parallel-video]].
