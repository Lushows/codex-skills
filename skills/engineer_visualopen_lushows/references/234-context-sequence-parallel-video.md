# 234 · Context / sequence parallel para video que no cabe (USP: Ulysses + Ring)

> Un clip largo genera una secuencia de tokens (frames × parches) que no entra en la atención de 1 GPU.
> Sequence parallelism parte ESA secuencia entre GPUs. Es el lever que [[13-multi-gpu-distribuido]] solo nombró.

## El problema concreto
La atención del DiT de video es O(seq²) en cómputo y guarda activaciones proporcionales a `seq`. Para un
clip de varios segundos a buena resolución, `seq` = miles de tokens × N frames → ni el cómputo ni la
memoria caben en una GPU. No es "el modelo pesa mucho" (eso lo arregla FSDP, [[233-fsdp-deepspeed-diffusion-training]]):
es que **una sola muestra** es demasiado larga. Necesitas partir la secuencia, no replicar el modelo.

## Las dos primitivas (y por qué se combinan)
| | Qué parte | Comunicación | Punto débil |
|---|---|---|---|
| **DeepSpeed-Ulysses** | los **heads** de atención | `all-to-all` (1 ráfaga densa) | no escala más allá del nº de heads |
| **Ring-Attention** | la **secuencia** en bloques | `P2P` en anillo, pasa K/V vecino a vecino | más rondas de comm, latencia por salto |

**USP** (Unified Sequence Parallelism) las une en una **malla 2D de procesos**: una dimensión Ulysses
(head-parallel) × una dimensión Ring (sequence-parallel). Así escalas más allá del límite de heads sin
ahogarte en la comunicación en anillo. Es lo que expone **xDiT** para FLUX/HunyuanVideo/Mochi/CogVideoX/Wan.

## Configurarlo (los dos grados de libertad)
```
world_size_sp = ulysses_degree × ring_degree     # = nº de GPUs en sequence-parallel
```
- `ulysses_degree` **debe dividir el número de heads** del modelo. Si tienes 24 heads y 8 GPUs:
  `ulysses=8, ring=1` funciona; `ulysses=16` no (no divide 24).
- `ring_degree` parte la secuencia; súbelo cuando ya saturaste los heads con Ulysses.
- **Heurística**: maximiza Ulysses primero (all-to-all intra-nodo sobre NVLink es barato), usa Ring para
  cruzar nodos o cuando heads/ulysses ya no da. Algunas libs lo llaman `context_parallel_size` (= el producto).

```python
# patrón xDiT (esquemático)
from xfuser import xFuserArgs
args = xFuserArgs(ulysses_degree=4, ring_degree=2, ...)  # 8 GPUs de SP
# launch: torchrun --nproc_per_node=8 inference.py --ulysses_degree 4 --ring_degree 2
```

## Topología: dónde poner cada degree
Ulysses hace **un all-to-all denso por capa** → quiere el link más gordo: ponlo **intra-nodo sobre NVLink**.
Ring pasa K/V vecino-a-vecino, tolera mejor saltos → úsalo para **cruzar nodos** (InfiniBand). Mapear
ulysses a NVLink y ring a la red inter-nodo es la diferencia entre escalar y quedar comm-bound. Verifica
con `NCCL_DEBUG=INFO` que el all-to-all de Ulysses no esté cayendo a `SYS`/PCIe (ver [[232-nccl-tuning-topology]]).

## Complementos de xDiT (no confundir con SP)
- **PipeFusion**: pipeline parallel que explota la **redundancia step-a-step** del difusor (los inputs entre
  pasos de denoising se parecen) → menos comm que tensor-parallel clásico. Compone con USP.
- **CFG-parallel**: las ramas condicional/incondicional del classifier-free guidance corren en paralelo
  (factor 2 trivial). Casi gratis: actívalo antes que nada.
- **tensor parallel**: parte las matrices; útil para el modelo pero no resuelve el `seq²` por sí solo.

## Inferencia vs entrenamiento
Lo de arriba es **inferencia** (generar el clip). En **entrenamiento** combinas SP (para que la muestra
larga quepa) **con** FSDP/ZeRO (para que el optimizer state quepa) → malla 3D: data × shard × sequence.
Ahí el orden de los grupos de proceso importa: pon el grupo SP dentro del nodo, el data-parallel afuera.

## Gotchas
1. `ulysses_degree` que no divide los heads → crash o resultados corruptos. Cuéntalos primero.
2. Ring con muchos saltos sobre red lenta = latencia que come la ganancia; mide tokens/s reales, no teóricos.
3. all-to-all de Ulysses cayendo a PCIe/`SYS` mata el speedup — fíjalo a NVLink.
4. Sumar SP no baja el peso del modelo; si además no cabe en VRAM por params, necesitas [[233-fsdp-deepspeed-diffusion-training]].
5. La calidad debe ser **idéntica** a single-GPU (SP es matemáticamente exacto): si difiere, hay un bug de partición, no "precisión".

Cruza con [[13-multi-gpu-distribuido]] y [[122-wan-video-self-hosting-2026]].
