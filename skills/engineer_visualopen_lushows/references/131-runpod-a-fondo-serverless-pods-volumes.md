# 131 · RunPod a fondo: Serverless, Pods, Volumes y billing real

> RunPod tiene dos mundos: **Pods** (VM con GPU, tú la prendes/apagas) y **Serverless**
> (cola + autoscaling a 0). Para IA visual self-hosted casi siempre quieres Serverless.
> Esto es el mapa completo de estados, timeouts y $/s reales (jun-2026).

## Serverless vs Pods (cuándo cada uno)
| | Pods | Serverless |
|---|---|---|
| Modelo | VM persistente, SSH, Jupyter | endpoint con cola, escala 0→N |
| Pagas | mientras esté ON (aunque idle) | por segundo de worker activo |
| Uso | desarrollo, pre-popular volumen, debug interactivo | producción, inferencia esporádica/burst |
| Cold start | ninguno (siempre ON) | sí, salvo active/idle warm |

Pre-popular el Network Volume y depurar el handler → **Pod**. Servir el modelo → **Serverless**.
Cruza con [[113-network-volume-modelos-grandes]].

## Active vs Flex workers
- **Flex**: nacen bajo demanda, escalan a 0 cuando no hay cola. Pagas solo lo que corre. Cold start.
- **Active**: workers SIEMPRE encendidos (mín. garantizado), **20-32% más baratos por segundo**, sin
  cold start. Compensan si tienes ≥~25% de uptime mensual (~180h/mes). Para video esporádico → Flex.
- **Max workers**: techo de escalado. Más = más concurrencia, pero RunPod reserva capacidad.

## Estados del worker (los verás en la UI)
| Estado | Significado | Qué hacer |
|---|---|---|
| `initializing` | pull de imagen + carga de modelo a VRAM | normal en frío; aquí YA se factura |
| `idle` | vivo, sin job, esperando (idle timeout) | warm; el siguiente job salta el cold |
| `running` | procesando un request | — |
| `throttled` | no hay GPU libre en la región | sube max workers o cambia región/GPU |
| `unhealthy` | el worker crashea al arrancar | revisar Logs: import error, OOM, tag malo |

"0 running workers" en el header **miente** (lag de UI). Manda **Logs** + pestaña **Requests**.
Ver [[111-longcat-avatar-runpod-produccion]].

## Timeouts
- **Execution Timeout**: máximo que un job puede correr antes de `Failed` (y SÍ se cobra hasta el kill).
  Regla: `timeout ≥ cold_start + N·t_segmento + margen`. Ver [[112-execution-timeout-cold-start-economics]].
- **Idle Timeout** (default 5s): cuánto sigue vivo el worker tras terminar un job. Subirlo crea un
  **warm pool** → el 2º+ video de una tanda no paga frío. Pero pagas esos segundos idle.

## Billing real (jun-2026, verificado en docs.runpod.io)
Se cobra **por segundo** en 3 fases: initializing (incluye carga de modelo) + running + idle timeout.
El cold start CUENTA. Tarifas Serverless ($/s flex → active):

| GPU | VRAM | Flex $/s | Active $/s | Flex $/hr |
|---|---|---|---|---|
| A40 / A6000 | 48 GB | 0.00034 | 0.00024 | 1.22 |
| L40S | 48 GB | 0.00053 | 0.00037 | 1.91 |
| A100 | 80 GB | 0.00076 | 0.00060 | 2.74 |
| H100 PRO | 80 GB | 0.00116 | 0.00093 | 4.18 |
| H200 PRO | 141 GB | 0.00155 | 0.00124 | 5.58 |
| B200 | 180 GB | 0.00240 | 0.00190 | 8.64 |

Storage: Network Volume **$0.07/GB-mes** (<1TB) / **$0.05** (>1TB); container disk ~$0.10/GB-mes.
Esto valida el `RUNPOD_RATE_PER_SEC` ≈ 0.0008–0.0012 para A100/H100 80GB de [[111-longcat-avatar-runpod-produccion]].
Cruza con [[30-finops-gpu]].

## Network Volume + regiones
El volumen es **regional**. El endpoint solo corre donde vive el volumen → elige la región por
disponibilidad de tu GPU, no al revés (o verás `throttled` eterno). Detalle en [[113-network-volume-modelos-grandes]].

## /run (async) vs /runsync
- **`/run`**: encola, devuelve `{id}` al instante. Consultas `/status/{id}`. Único viable para renders
  largos (20-40 min). Patrón submit+poll: ver [[111-longcat-avatar-runpod-produccion]].
- **`/runsync`**: bloquea hasta el resultado. Solo para jobs cortos (<~30s); muere por timeout HTTP en video.

## Scaling
- **Request Count scaling**: añade workers según largo de cola (X requests pendientes → +1 worker).
- **Queue Delay scaling**: añade worker si un job espera > N segundos.
- Más max workers = menos espera, pero más cold starts simultáneos (cada uno re-carga modelo si no hay volumen).

## Gotchas que cuestan horas
- **"New release" deshabilitado** si el tag = el actual: RunPod exige tag NUEVO. Forzar re-pull con
  mismo tag → borrar workers (recrean y bajan imagen) o usar `:latest`.
- **Cache de imagen por nodo**: la imagen se cachea en el nodo físico; un worker en nodo nuevo re-baja
  la imagen (otro tramo de cold). Imágenes pequeñas (multi-stage, sin pesos horneados) arrancan antes.
- **IMAGE_NOT_FOUND** suele ser timing: pinaste el SHA antes de que GHCR publicara el tag.
- **Fallos SÍ se facturan** hasta el kill. Sobre-dimensiona el Execution Timeout.

Cruza con [[112-execution-timeout-cold-start-economics]] y [[132-plataformas-gpu-serverless-comparativa]].
