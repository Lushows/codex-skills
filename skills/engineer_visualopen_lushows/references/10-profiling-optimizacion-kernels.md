# 10 — Profiling y optimización de kernels (PyTorch)

Profiling es un embudo: primero ubica en CUÁL de 4 clases de cuello estás — **(1)** CPU-bound launch
overhead (GPU hambrienta entre kernels chicos), **(2)** GPU compute-bound, **(3)** memory-bandwidth-bound,
**(4)** data-loading-bound (GPU idle esperando el `DataLoader`) — luego baja al kernel ofensor. Herramienta
por capa: `torch.profiler` (vista framework), **Nsight Systems (`nsys`)** (timeline del sistema), **Nsight
Compute (`ncu`)** (detalle SM/memoria de UN kernel).

## torch.profiler con schedule
Nunca perfiles cada step — warm up y captura unos pocos. `schedule(wait, warmup, active, repeat)` salta
`wait`, corre `warmup` con profiler pero descartado (el caching allocator/cuDNN autotune se asientan), luego graba `active`.

```python
from torch.profiler import profile, schedule, ProfilerActivity, tensorboard_trace_handler
with profile(
    activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA],
    schedule=schedule(wait=1, warmup=1, active=3, repeat=1),
    on_trace_ready=tensorboard_trace_handler("./tb_logs"),
    record_shapes=True, with_stack=True, profile_memory=True) as prof:
    for step, batch in enumerate(loader):
        train_step(batch); prof.step()          # OBLIGATORIO: avanza el schedule
print(prof.key_averages().table(sort_by="cuda_time_total", row_limit=20))
prof.export_chrome_trace("trace.json")          # abre en Perfetto (ui.perfetto.dev)
```
`record_shapes` agrupa por shape; `with_stack` adjunta stacks Python (pesado); `profile_memory` añade stats
del allocator. Para traces grandes, **Holistic Trace Analysis (HTA)** computa idle-time breakdown y overlap
de comunicación entre ranks. El plugin de TensorBoard está deprecado → usa **Perfetto** o HTA.

## nsys (timeline) y ncu (un kernel)
`nsys profile --trace=cuda,nvtx,osrt,cudnn,cublas -o run python train.py`. Gaps en la fila del CUDA stream
→ CPU/launch-bound o dataloader-bound; stream lleno → GPU-bound. Anota con `torch.cuda.nvtx.range_push/pop`.
`ncu --set full --launch-skip 30 --launch-count 1 -k regex:my_kernel python ...` → la sección "Speed of
Light" dice al instante si eres compute- o memory-bound. **ncu serializa/replaya → lentísimo; restringe siempre con `-k`/`--launch-count`/`--launch-skip`.**

## Timing manual (los calls GPU son async)
Wall-clock sin sync no significa nada. Usa eventos CUDA:
```python
s, e = torch.cuda.Event(enable_timing=True), torch.cuda.Event(enable_timing=True)
torch.cuda.synchronize(); s.record(); fn(); e.record(); torch.cuda.synchronize()
ms = s.elapsed_time(e)
```

## torch.compile graph breaks
Cada break parte el grafo y reintroduce overhead eager. Encuéntralos: `TORCH_LOGS="graph_breaks,recompiles"
python ...`, o `TORCH_TRACE=/tmp/tt python ...` + `tlparse /tmp/tt/*`.

## Gotchas
1. Olvidar `prof.step()` → el schedule no avanza, no capturas nada.
2. Timing sin `synchronize()` reporta tiempo de LANZAMIENTO en CPU, no GPU — bug clásico "100× muy rápido".
3. `with_stack` + `record_shapes` en cada step → trace de GBs; gátealo a la ventana `active`.
4. `ncu` sin `--launch-count`/`-k` puede tardar horas (replaya cada kernel muchas veces).
5. Timeline GPU llena pero util baja = kernels chicos → fusiona con `torch.compile`/batch mayor, NO "compra una GPU más grande".

**Fuentes:** docs.pytorch.org/docs/stable/profiler.html · huggingface.co/blog/torch-profiler · developer.nvidia.com/nsight-systems · docs.nvidia.com/nsight-compute · torch.compiler_troubleshooting.
