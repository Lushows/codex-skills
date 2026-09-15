# 242 · Orquestar pipelines ML (Dagster / Flyte / Metaflow / Prefect)

> Encadenar "descargar dataset → preprocesar → entrenar LoRA en GPU → evaluar → publicar pesos" a
> mano con scripts sueltos no escala: sin reintentos, sin caché, sin linaje. Un orquestador convierte
> ese flujo en un DAG con pasos GPU aislados, reanudables y auditables.

## Cuándo necesitas un orquestador
No para un solo worker de inferencia (eso lo cubre la cola de jobs de RunPod). Sí cuando tienes
**pipelines multi-paso** que mezclan CPU y GPU, corren en schedule o por evento, y deben **reanudar
desde el paso que falló** sin re-ejecutar lo caro (re-entrenar 6h porque el eval crasheó = inaceptable).

## Los cuatro, en una frase
| Tool | Filosofía | Cuándo elegirlo |
|---|---|---|
| **Prefect** | Python casi puro, DAG dinámico en runtime | Empiezas; quieres mínima fricción, sin K8s ni DSL |
| **Dagster** | Centrado en *assets* (dataset, modelo, eval son objetos) | El pipeline gira en torno a datos/frescura; quieres linaje y un catálogo |
| **Metaflow** | Centrado en el data scientist (Netflix) | Prototipo local → nube (AWS Batch/K8s) con decoradores `@batch`/`@kubernetes` |
| **Flyte** | K8s-nativo, tipado fuerte, crash-proof | Escala enterprise, equipo cómodo con K8s y su control-plane |

## Mapear pasos a GPU
La clave es declarar recursos **por paso**, no por pipeline. Patrones:
- **Flyte**: `@task(requests=Resources(gpu="1"), ...)` → el scheduler de K8s coloca el pod en un nodo con
  GPU. Pasos CPU (descarga, eval ligero) corren en nodos baratos; solo el training pide GPU.
- **Metaflow**: `@kubernetes(gpu=1)` o `@batch(gpu=1)` sobre el step; Metaflow empaqueta el código,
  lo manda a la nube y recupera resultados.
- **Prefect/Dagster**: no agendan GPU nativamente; delegan el paso pesado a un **executor externo**
  (submit a un endpoint RunPod, job de K8s, o Ray). El orquestador hace submit + poll + recoge artifact.

Para auto-hospedaje barato, el patrón que mejor encaja: **orquestador en CPU barata** (un contenedor
pequeño siempre vivo) que **dispara los pasos GPU como jobs serverless** (ver [[16-cicd-modelos-workers]]).
No tengas el orquestador ocupando una GPU esperando.

## Qué te dan que un cron no
- **Reintentos + idempotencia** por paso (retry solo el step caído, no todo).
- **Caché de resultados**: si el input no cambió, salta el paso (Flyte/Dagster lo hacen por hash).
- **Linaje**: qué dataset + qué hiperparámetros produjeron qué pesos → reproducibilidad y debug.
- **Backfill / schedule**: re-correr el pipeline sobre datos nuevos sin tocar código.

## Recomendación para este stack (avatares/video open)
- **Pocos pipelines, equipo chico, sin K8s** → **Prefect** o **Metaflow**. Empieza con Prefect si el
  flujo es plain-Python; Metaflow si quieres prototipo-local→nube fluido.
- **Ya tienes K8s y quieres tipado/escala** → **Flyte** (curva más alta, pero crash-proof real).
- **Dagster** si el problema central es **datos y frescura de assets** más que orquestar GPU.

## Detalles que muerden
- No metas el peso del modelo dentro del DAG como dato serializado: pasa **referencias** (ruta R2/HF +
  hash), no 44GB inline. El orquestador mueve metadatos, no pesos (ver [[245-data-model-versioning-dvc-lakefs]]).
- Flyte/K8s = coste operativo: necesitas el cluster vivo. Para volumen bajo, Prefect+serverless gana.
- Timeouts: el paso GPU puede durar horas; configura el timeout del step acorde, no el default.

Cruza con [[64-data-pipelines-mlops-etl]] y [[16-cicd-modelos-workers]].
