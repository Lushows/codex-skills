# 245 · Versionar datos y modelos (DVC / lakeFS / HF) reproducible

> "Funcionaba con el dataset de la semana pasada" no es debuggeable si no sabes qué era "la semana
> pasada". Versionar datos y pesos como versionas código convierte cada experimento en algo
> reproducible: este commit de código + este hash de dataset + estos pesos = este resultado, siempre.

## El problema
Git no maneja archivos grandes (datasets de imágenes/video, checkpoints de GB). Necesitas versionar el
**dato** y el **peso** con la misma rigurosidad que el código, sin meterlos en Git. Tres enfoques:

| Tool | Modelo | Encaja cuando |
|---|---|---|
| **DVC** | Versiona **punteros** (metafiles tiny) en Git; el dato real va a un remote (S3/R2/GCS) | Artefactos y pipelines atados a un repo; proyectos chico-medianos |
| **lakeFS** | Capa sobre el object store: branches/commits/merge **sobre el storage** | Datasets grandes (imagen/video) en un data lake; escala petabyte sin copiar |
| **HF Hub** | Repos Git-LFS gestionados para modelos/datasets | Pesos públicos/compartibles, integración directa con `transformers`/`diffusers` |

> **Nota 2026 [verificado]:** DVC fue **adquirido por lakeFS** (nov 2025). Siguen siendo herramientas
> distintas con casos de uso distintos; la adquisición no las fusiona.

## DVC vs lakeFS, la diferencia real
- **DVC** es *Git-adyacente*: pequeños `.dvc` con el hash viven en tu repo, el blob real en R2/S3. Pipelines
  CLI + `dvc.lock` para reproducibilidad. **Pega**: el snapshot de metadata es un JSON serializado → escala
  mal con colecciones grandes (debe deserializar todo el blob para saber qué hay en una versión).
- **lakeFS** es *storage-nativo*: convierte tu object store en un filesystem versionado. Creas branch desde
  `production`, transformas, mergeas — sin copiar terabytes. Arquitectura cliente/servidor, escala horizontal.

## El patrón que combina ambos (recomendado)
No es "uno u otro". Para este stack (avatares/video, datasets de imagen+video, LoRAs):
1. **lakeFS** para los **datasets crudos y curados** grandes en el lake (R2/S3): branching y rollback baratos.
2. **DVC** para **artefactos de modelo y pipelines** atados al repo: pinea una versión de dataset
   referenciando un **commit hash de lakeFS**. Código en Git, semántica de datos en el lake.
3. **HF Hub** para **publicar/compartir pesos** finales o bajar modelos base (cruza con [[163-gestion-pesos-modelos-hf-hub]]).

## Reproducibilidad de extremo a extremo
Un experimento reproducible amarra cuatro hashes: **commit de código** (Git) + **versión de dataset**
(lakeFS commit o `.dvc`) + **hiperparámetros** (logueados en el tracker, [[244-experiment-tracking-wandb-mlflow]])
+ **checkpoint** (registrado en el registry, [[18-model-registry-versionado]]). Si falta uno, el resultado
no se reproduce. El tracker debe **guardar estos hashes en cada run**.

## Detalles que muerden
- **No metas pesos enormes en Git ni en el DAG**: versiona referencias (ruta + hash), no los 44GB inline.
- **Remote de DVC = tu R2/S3**: mismo bucket que ya usas para servir pesos; reutiliza infra, un solo lugar.
- **lakeFS necesita un servidor** (control-plane + KV store): coste operativo; justifícalo con tamaño de datos.
  Para datasets chicos, DVC solo basta y es más simple.
- **Costo de copias**: la gracia de lakeFS es branch sin copiar (copy-on-write); DVC sí duplica si no cuidas
  el caché. En video (archivos pesados) esto importa para la factura de storage.
- Para datasets de visión chicos, DVC alcanza; para colecciones grandes de imagen/video, lakeFS escala mejor.

Cruza con [[18-model-registry-versionado]] y [[163-gestion-pesos-modelos-hf-hub]].
