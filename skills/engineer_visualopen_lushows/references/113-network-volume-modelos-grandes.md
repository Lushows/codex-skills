# 113 · Network Volume para modelos grandes (matar la re-descarga del cold start)

> El cold-start que re-baja 44GB en cada arranque es el mayor costo oculto del serverless GPU.
> Un Network Volume persiste los pesos → el frío deja de pagar la descarga.

## El problema
Serverless escala a 0. Cada worker frío re-descarga el modelo (LongCat-Avatar ≈ 44GB) a disco
**efímero** del contenedor. Eso son ~8-12 min facturados **por cada arranque frío**, repetidos para
siempre. Multiplica por cada video → sangría de tiempo y dinero.

## La solución: Network Volume (almacenamiento persistente de red)
Un volumen de red se monta en el worker (RunPod: `/runpod-volume`, o `/workspace` según config) y
**sobrevive** entre jobs/workers. Guardas ahí el caché de modelos una vez → los siguientes arranques
solo **leen del volumen** (rápido) en vez de bajar de HuggingFace.

### Pasos (RunPod)
1. **Storage → New Network Volume** en un **datacenter que tenga tu GPU** (A100/H100). El volumen es
   regional: el endpoint debe poder correr en esa región. Tamaño ≥ modelo + margen (ej. 80-100GB).
2. **Edit Endpoint → Network Volume** = el que creaste. (Limita el endpoint a esa región.)
3. **Apunta el caché de modelos al volumen** vía env del worker:
   ```
   HF_HOME=/runpod-volume/hf
   HUGGINGFACE_HUB_CACHE=/runpod-volume/hf/hub
   TORCH_HOME=/runpod-volume/torch
   ```
   (o el path que use tu descargador: muchos repos bajan a `./checkpoints` → móntalo o symlinkéalo al volumen).
4. **Primer arranque**: baja los 44GB UNA vez al volumen (lento). **Siguientes**: instantáneo.

## Resultado medido (LongCat, caso real)
- Sin volumen: cold ≈ 40 min, ~$2/video.
- Con volumen: cold ≈ 25 min (solo carga a VRAM, sin re-descarga), ~$1.25/video. Y timeout más holgado.

## Detalles que muerden
- **Región**: si tu GPU preferida no está en la región del volumen, el endpoint no la usará. Elige la
  región por disponibilidad de la GPU, no al revés.
- **Concurrencia**: varios workers leyendo el mismo volumen está bien (lectura). Si **escribes** el
  caché desde varios a la vez en el primer arranque, puede haber carreras → pre-popular el volumen una
  vez (un Pod temporal que monte el volumen y haga el download) evita el problema.
- **Costo del volumen**: se paga por GB-mes (barato vs re-bajar 44GB cada vez). Compensa con pocos videos.
- **Pre-popular sin esperar al primer job**: crea un **Pod** normal, monta el volumen, ejecuta el script
  de descarga del modelo, apaga el Pod. El endpoint serverless ya encuentra los pesos.

## Alternativas / complementos
- **Hornear pesos en la imagen Docker**: elimina la descarga pero infla la imagen a decenas de GB
  (pull lento, build caro). Volumen suele ganar para modelos enormes que cambian poco.
- **Snapshot/baked layer + volumen** combinados: imagen con deps, volumen con pesos. Lo más flexible.

Cruza con [[112-execution-timeout-cold-start-economics]] y [[30-finops-gpu]].
