# 231 · Checkpoint / Resume de jobs largos (render y training que no empiezan de cero)

> Un render de 10 min o un training de horas que se cae al minuto 9 y reinicia desde 0 es dinero
> quemado. Checkpoint/resume convierte un job frágil y largo en una suma de tramos cortos recuperables.

## Por qué (más allá de spot)
Aunque NO uses spot ([[230-spot-preemptible-gpu-handling]]), los jobs largos se enfrentan a: OOM tardío,
timeout del serverless, crash de driver, deploy que reinicia el worker, fallo de red al subir. Cualquiera
borra horas. El checkpoint hace el progreso **durable** e independiente de la vida del proceso.

## Qué es un checkpoint reanudable (el estado MÍNIMO)
No guardes "todo": guarda lo imprescindible para continuar exactamente donde ibas.
| Tipo de job | Estado a persistir |
|---|---|
| **Training** | pesos del modelo + estado del optimizer + step/epoch + estado del LR scheduler + RNG |
| **Video largo segmentado** | índice del último segmento completado + sus frames/latents ya escritos |
| **Difusión por steps** | latente actual + número de step + seed/RNG del sampler |
| **Batch de N items** | set de IDs ya procesados (para saltarlos al reanudar) |

Olvidar el **estado del optimizer** o el **RNG** = el resume "funciona" pero diverge o no es
reproducible. Es el error clásico.

## Reglas de implementación
- **Escritura atómica**: `torch.save(state, "ck.tmp"); os.replace("ck.tmp", "ck.pt")`. `os.replace` es
  atómico → nunca lees un checkpoint corrupto a medio escribir.
- **Destino persistente**: Network Volume / R2 / S3, **no** el disco efímero del contenedor (ver
  [[113-network-volume-modelos-grandes]]). Lo efímero muere con el worker.
- **Rotación**: conserva los últimos K (ej. 3) y un `latest` → si el más nuevo salió corrupto por un
  crash en el write, reanudas del anterior. No acumules infinito (costo de storage).
- **Intervalo por costo de re-trabajo**: checkpointea cada `T` tal que perder `T` de cómputo sea
  tolerable. Job de 10 min → cada ~1-2 min. Training de horas → cada N steps que cuesten minutos.
- **Idempotencia del resume**: reanudar dos veces del mismo checkpoint debe dar el mismo resultado; no
  dupliques outputs ya subidos (chequea por ID/hash antes de re-escribir).

## Patrón de resume al arrancar
```python
state = load_latest_checkpoint(volume)  # None si es la primera vez
start = state["step"] if state else 0
if state: model.load_state_dict(state["model"]); opt.load_state_dict(state["opt"])
for step in range(start, total):
    ... compute ...
    if step % CKPT_EVERY == 0:
        atomic_save({"step": step+1, "model": model.state_dict(),
                     "opt": opt.state_dict(), "rng": torch.get_rng_state()}, volume)
```

## Tamaño y costo del checkpoint
El estado del optimizer pesa **2× los pesos** (Adam guarda dos momentos por parámetro): un modelo de
4GB → checkpoint de ~12GB. Para inferencia/render el checkpoint es mucho más liviano (solo latente +
metadatos). Si el checkpoint es grande y lento de escribir, considera: guardarlo en `float16`, escribir
asíncrono en un thread aparte para no bloquear el cómputo, o subir solo el `latest` y rotar local.

## Video/render: granularidad de segmento
Para clip largo segmentado, el "checkpoint" natural es el **segmento terminado** ya escrito al volumen.
Al reanudar, salta los segmentos existentes y sigue desde el primero faltante; al final concatena
(ffmpeg). Esto encaja con el poller durable del render asíncrono — el estado del job vive fuera del
worker, así que cualquier worker nuevo lo retoma.

Cruza con [[115-async-render-largo-poller-durable]] y [[230-spot-preemptible-gpu-handling]].
