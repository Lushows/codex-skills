# 13 — Multi-GPU / distribuido a fondo

## Lanzar con torchrun
Setea `RANK`, `LOCAL_RANK`, `WORLD_SIZE` y corre el rendezvous. Single node, 8 GPUs:
`torchrun --standalone --nproc_per_node=8 train.py`. Multi-node (backend `c10d`, preferido, sin etcd):
```bash
torchrun --nnodes=4 --nproc_per_node=8 --rdzv_id=job101 --rdzv_backend=c10d --rdzv_endpoint=node0:29500 train.py
```
`--nproc_per_node` acepta `gpu`/`auto`/int. Elástico: `--nnodes=2:4 --max-restarts=5`.

## DDP vs FSDP
- **DDP** replica el modelo completo por GPU, all-reduce de gradientes — simple, rápido si el modelo CABE.
- **FSDP/FSDP2** shardea params/grad/optim entre ranks — úsalo cuando NO cabe. Strategies: `full_shard` (máximo
  ahorro, más comm), `hybrid_shard` (shard intra-nodo, replica inter-nodo — mejor si el BW inter-nodo es el cuello).
  `CPUOffload(offload_params=True)` cambia velocidad por VRAM. FSDP2: `fully_shard(layer)` por capa, luego `fully_shard(model)`.

## DeepSpeed ZeRO
ZeRO-1 shardea optim state · ZeRO-2 añade grad · ZeRO-3 añade params (≈ FSDP full_shard). **ZeRO-Inference**
offloadea pesos a CPU/NVMe → corre modelos >> VRAM en inferencia (throughput, costo de latencia). Config JSON `ds_config`.

## Context / sequence parallel para DiTs de video (EL lever)
La atención sobre secuencias largas de tokens de video no cabe en 1 GPU. **Ulysses** (all-to-all, parte heads) +
**Ring Attention** (parte secuencia, ring-passa K/V) = **USP**, expuesto por **xDiT** para FLUX/HunyuanVideo/Mochi/
CogVideoX. Setea `ulysses_degree × ring_degree` (producto = world size de sequence-parallel); algunos lo llaman
`context_parallel_size`. xDiT también ofrece **PipeFusion** (pipeline explotando redundancia step-a-step).

## NCCL tuning & debug
`NCCL_DEBUG=INFO` (ve topología/ring). Sin NVLink P2P: `NCCL_P2P_DISABLE=1`; sin InfiniBand: `NCCL_IB_DISABLE=1`
(fuerza TCP). Sube el watchdog timeout vía el `timeout` del process-group.

## Debug de cuelgues
El fallo clásico: un rank hace OOM/excepción y muere; los demás bloquean para siempre en un collective → el
NCCL watchdog dispara `SIGABRT` en todo el grupo. **El traceback del rank muerto es la causa real — scroll up.**
Control flow desigual (un rank toma otra rama y salta un `all_reduce`) cuelga igual. `TORCH_NCCL_ASYNC_ERROR_HANDLING=1`.

## Gotchas
1. Un rank que crashea cuelga TODO el job → lee el stack del PRIMER rank que falla, no el spam de SIGABRT.
2. `full_shard` sobre links inter-nodo lentos = comm-bound → usa `hybrid_shard`.
3. `NCCL_P2P_DISABLE`/`IB_DISABLE` son muletas de debug que matan el BW; quítalas al arreglar.
4. Shapes de batch distintas por rank o collectives condicionales → deadlock; mantén ranks en lockstep.
5. El ulysses degree debe dividir el nº de heads; ring degree parte secuencia — setea ambos deliberadamente.

**Fuentes:** docs.pytorch.org/docs/stable/elastic/run.html · github.com/xdit-project/xDiT · simplismart.ai/blog (hybrid parallelism video-DiT) · DeepSpeed-Ulysses.
