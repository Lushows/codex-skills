# 232 · NCCL tuning y topología (NVLink/PCIe, hangs, env vars)

> Multi-GPU lento o colgado casi siempre es NCCL eligiendo mal ring o un rank muerto en un collective.
> Aquí va más a fondo que [[13-multi-gpu-distribuido]]: cuándo NO tocar nada, qué tocar, y cómo leer un hang.

## Regla cero: no tunees a ciegas
NCCL detecta topología y autoajusta; en una caja sana con NVLink no necesitas env vars. Tocar `NCCL_ALGO`
o desactivar P2P **a mano** casi siempre empeora. Primero **mide** (`NCCL_DEBUG=INFO` + un all-reduce de
prueba), confirma que el ring/tree elegido usa los links rápidos, y solo entonces interviene.

## Mapa de la topología (qué tienes realmente)
| Comando | Te dice |
|---|---|
| `nvidia-smi topo -m` | matriz de links: `NV#`=NVLink, `PIX/PXB`=mismo switch PCIe, `SYS`=cruza CPU/NUMA |
| `nvidia-smi nvlink -s` | NVLink activo y ancho de banda por link |
| `NCCL_DEBUG=INFO` (log al init) | "via NVLink"/"via SHM"/"via NET"; el **ring/tree** que construyó |

`SYS` entre dos GPUs = el tráfico cruza sockets (QPI/UPI) → lento y sensible a NUMA. Pinea procesos al
NUMA node de su GPU (`numactl --cpunodebind`). En cloud serverless rara vez controlas esto, pero saber
que tu par de GPUs es `SYS` y no `NV#` explica un 2-3x de pérdida.

## Algoritmos y los levers reales
- **Ring**: ancho de banda óptimo para mensajes grandes (gradientes). **Tree**: menor latencia para
  mensajes chicos / muchos nodos. NCCL mezcla; `NCCL_ALGO=Tree,Ring,...` solo restringe (prefijo `^` excluye).
- **NVLS** (NVLink SHARP, Hopper+ con NVSwitch gen3): offloadea el all-reduce al switch. Default on (`NCCL_NVLS_ENABLE=1`);
  en GPUs sueltas sin NVSwitch simplemente no aplica. [no verificado: disponibilidad exacta por SKU cloud].
- **PXN** (`NCCL_PXN_RECV_P2P_SRD`, default 2): relay GPU→GPU intra-nodo para agregar tráfico hacia la NIC
  en multi-nodo con InfiniBand. Solo importa con >1 nodo y red RDMA.
- **`NCCL_BUFFSIZE`**, **`NCCL_MIN/MAX_NCHANNELS`**: micro-tuning de buffers/canales. Mídelos, no los adivines.

## Muletas de debug (matan BW — quítalas después)
```bash
NCCL_P2P_DISABLE=1      # ignora NVLink/PCIe P2P → fuerza SHM. Si "arregla" un crash, el bug es P2P/driver
NCCL_IB_DISABLE=1       # ignora InfiniBand → TCP. Diagnóstico multi-nodo, jamás producción
NCCL_SHM_DISABLE=1      # descarta memoria compartida
NCCL_DEBUG=INFO         # SIEMPRE durante el bring-up; quítalo en prod (es ruidoso)
NCCL_DEBUG_SUBSYS=INIT,GRAPH,ENV   # acota el log a init y construcción del grafo
```
Si el job pasa de colgarse a funcionar al poner `NCCL_P2P_DISABLE=1`, **no lo dejes**: tienes un problema
de P2P (driver/IOMMU/ACS del host, o un par `SYS` mal ruteado) que hay que arreglar de raíz.

## Anatomía de un hang (el 80% de los tickets)
1. Un rank hace OOM o lanza excepción y **muere** dentro de un kernel/collective.
2. Los demás ranks quedan bloqueados esperando ese all-reduce/all-gather que nunca llega.
3. A los N minutos el **watchdog** NCCL dispara `SIGABRT` en todo el grupo → spam de tracebacks idénticos.
4. La causa real es el **primer** rank que falló: **scroll up**, no leas el spam de abajo.

Palancas para que falle rápido y claro en vez de colgar 30 min:
```bash
TORCH_NCCL_ASYNC_ERROR_HANDLING=1   # convierte el cuelgue en error propagado
TORCH_NCCL_TRACE_BUFFER_SIZE=2000   # flight-recorder: vuelca el último collective por rank al timeout
TORCH_NCCL_DUMP_ON_TIMEOUT=1
```
Y sube el watchdog vía el `timeout=` del `init_process_group` (subir el techo, no esconder el bug).

## Causas de hang que no son "rank muerto"
- **Control flow desigual**: un rank entra a un `if` y salta un `all_reduce` que los otros sí ejecutan → deadlock.
  Mantén los ranks en lockstep; nada de collectives condicionales por rank.
- **Shapes distintas por rank**: batch o secuencia variable → el collective espera tamaños que no llegan.
- **Init parcial**: un rank no llamó `init_process_group` (crash temprano antes del rendezvous) → todos cuelgan en el barrier.

## Checklist de bring-up
1. `nvidia-smi topo -m` → confirma `NV#` entre las GPUs que vas a usar (no `SYS`).
2. Corre con `NCCL_DEBUG=INFO` una vez; lee la línea del ring/tree y "via NVLink".
3. Mide un `all_reduce` de ~1GB: BW real debe acercarse al pico NVLink, no al de PCIe.
4. Activa los flags de flight-recorder ANTES de lanzar el entrenamiento largo.
5. Quita toda muleta `*_DISABLE` antes de medir performance final.

Cruza con [[13-multi-gpu-distribuido]].
