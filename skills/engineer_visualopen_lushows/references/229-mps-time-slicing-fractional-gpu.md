# 229 · MPS · Time-Slicing · Fractional GPU (compartir GPU sin particionar hardware)

> Cuando MIG no aplica (GPU Ada/RTX, o necesitas reparto flexible), compartes la misma GPU por
> software: MPS ejecuta varios procesos **en paralelo** real, time-slicing los **alterna** rápido. Más
> densidad, menos aislamiento.

## Las tres palancas (no son lo mismo)
| Técnica | Cómo comparte | Aislamiento mem | Aislamiento de fallo |
|---|---|---|---|
| **Time-slicing** | un proceso a la vez, rota por quantum | ❌ comparten VRAM | ❌ un crash/OOM tumba a todos |
| **MPS** (Multi-Process Service) | varios procesos a la vez en los mismos SM | ❌ comparten VRAM | ❌ (parcial; mejor que time-slice) |
| **MIG** (ver [[228-mig-multi-instance-gpu]]) | particiones HW | ✅ dedicada | ✅ duro |

### MPS — Multi-Process Service
Demonio (`nvidia-cuda-mps-control -d`) que multiplexa varios procesos CUDA sobre la GPU **simultáneamente**,
solapando sus kernels en vez de serializar. Ideal cuando cada proceso **infrautiliza** la GPU (server de
inferencia con requests esporádicos): sube la utilización agregada. Puedes capar cómputo por proceso con
`CUDA_MPS_ACTIVE_THREAD_PERCENTAGE` (ej. 30% por worker). Volta+ soporta MPS con mejor aislamiento.

### Time-slicing
El scheduler de la GPU da turnos rotatorios a cada proceso (como un SO con CPUs). Solo uno corre por
quantum → **no** hay paralelismo real, solo la ilusión. Reportado hasta ~90% de ahorro corriendo ~10
jobs en una GPU, pero a costa de latencia variable. En Kubernetes se activa con el device-plugin
(`replicas: N` por GPU) — sobre-suscribe sin pedir nada al hardware.

## La trampa común: oversubscription de VRAM
Ni MPS ni time-slicing reparten memoria. Si pones 4 workers de 8GB en una GPU de 24GB y un pico los
lleva a 7GB cada uno → **28GB > 24GB → OOM que mata a todos**. Sin MIG **tú** eres responsable de que la
suma de picos de VRAM quepa. Regla: dimensiona por el **pico**, no por el promedio, y deja colchón.

## Cuándo cada uno
- **MPS**: muchos procesos que de a uno desperdician la GPU; quieres throughput agregado y toleras que
  un crash raro afecte vecinos. El caso más común para inferencia visual chica/mediana.
- **Time-slicing**: dev/test, demos, colas no críticas donde la densidad importa más que la latencia o
  el aislamiento. No para producción con SLA estricto.
- **Fractional GPU en cloud** (Baseten, RunPod, etc.): el proveedor te vende "0.25 H100" implementado
  por debajo con MIG (aislado) o MPS/time-slice (compartido). **Pregunta cuál** — cambia tu garantía de
  latencia y de no-OOM-por-vecino.

## Activar MPS (lo esencial)
```bash
export CUDA_MPS_PIPE_DIRECTORY=/tmp/mps
export CUDA_MPS_LOG_DIRECTORY=/tmp/mps_log
nvidia-cuda-mps-control -d          # arranca el demonio
# por worker, opcional, capar su cuota de SMs:
export CUDA_MPS_ACTIVE_THREAD_PERCENTAGE=30
```
Todos los procesos que vean el mismo `PIPE_DIRECTORY` se multiplexan por el demonio. Sin demonio, varios
procesos sobre una GPU **serializan** (time-slice implícito del driver) en vez de solaparse.

## Síntomas y diagnóstico
- **Latencia que oscila** sin razón aparente bajo time-slicing: es el quantum rotando; no es bug, es la
  técnica. Si el SLA no lo tolera, sube a MIG o GPU dedicada.
- **OOM intermitente "fantasma"**: dos vecinos picaron VRAM a la vez. `nvidia-smi` no siempre lo atrapa
  porque el pico es breve; instrumenta memoria máxima por proceso (`torch.cuda.max_memory_allocated`).
- **Un worker congela a los demás**: kernel largo monopolizando bajo time-slice, o crash que tumba el
  contexto compartido. Es el precio de no tener aislamiento de hardware.

## Combinar
Patrón de densidad máxima: **MIG** para cortar la H100 en slices aislados + **time-slicing/MPS dentro**
de cada slice para meter varios pods. Aislamiento entre slices, sharing flexible dentro. Decide por SLA:
producción con clientes → MIG o dedicada; cargas internas/batch → MPS o time-slice y exprime la tarjeta.

Cruza con [[228-mig-multi-instance-gpu]].
