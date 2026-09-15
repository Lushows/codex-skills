# 241 · Data loading a escala para training (WebDataset, parquet, streaming, bucketing)

> En training serio el cuello de botella casi nunca es la GPU: es alimentarla. Millones de imágenes en
> millones de archivitos matan cualquier filesystem. La solución es **shards** y **streaming**.

## El problema: el "small files" problem
1M imágenes sueltas = 1M `open()`/`stat()`. En disco de red (el Network Volume de [[113-network-volume-modelos-grandes]],
S3, NFS) el random-access por archivo es letal: latencia de metadatos × millones. La GPU se queda esperando
I/O al 30% de uso. La cura: **empaquetar** muchas muestras en pocos archivos grandes leídos en **streaming
secuencial** (lo que el almacenamiento de objetos hace rápido).

## WebDataset: shards .tar + lectura secuencial
Empaquetas las muestras como entradas consecutivas en **tar POSIX estándar**. Cada muestra = varios archivos
con el **mismo basename, distinta extensión**:
```
000123.jpg   000123.txt   000123.json
000124.jpg   000124.txt   000124.json
```
WebDataset los agrupa por basename → un dict `{"jpg":..., "txt":..., "json":...}`. Shards de **100MB-1GB**,
nombrados `shard-{000000..001000}.tar` (brace expansion). [verificado] Sirves los tar desde cualquier URL
(S3/R2/HTTP) y el loader hace **streaming**: lee secuencial, decodifica on-the-fly, sin tocar el disco local.
- **Shuffle a dos niveles**: barajas el ORDEN de shards + un **buffer de shuffle** dentro del shard (no puedes
  random-access dentro de un tar, así que mezclas con buffer en RAM, ej. 1000-10000 muestras).
- **Sharding entre workers/GPUs**: cada `DataLoader` worker / rank toma un subconjunto disjunto de shards →
  escala lineal sin coordinación. Ojo: nº de shards debe ser ≫ nº workers×ranks para repartir bien.

## Alternativas 2026 (el ecosistema se movió)
| Formato | Acceso | Fuerte en |
|---|---|---|
| **WebDataset** (.tar) | secuencial puro | madurez, simplicidad, cloud-native |
| **LitData** (Lightning) | índice + streaming | muy iterado; varios reportan migración WDS→LitData [verificado] |
| **MosaicML Streaming (MDS)** | shard + índice, resume determinista | reanudar mid-epoch exacto, multi-nodo |
| **HF Parquet** | columnar, random-access | datasets del Hub, filtrado por columna |
| **webshart** (bghira, Rust) | tar + **índice JSON sidecar** → random-access | random access sin bajar el tar entero [verificado] |
[verificado: LitData/HF-Parquet/MosaicML como formatos soportados; webshart = reader rápido con índice]

Regla: **WebDataset** sigue siendo el default seguro. Si necesitas **reanudar mid-epoch determinista** en
multi-nodo (jobs spot que se cortan, ver [[113-network-volume-modelos-grandes]]), **MosaicML Streaming**. Si
quieres **random-access** sobre tar sin bajarlo, **webshart**.

## Aspect-ratio bucketing (imprescindible para difusión)
Entrenar a 1024² recortando = pierdes encuadre y enseñas crops malos. Bucketing: agrupas por **relación de
aspecto** en *buckets* de resolución (ej. 1024×1024, 896×1152, 1152×896, 768×1344...) preservando área ~constante.
[verificado] Cada **batch** sale de un solo bucket (mismo tamaño → tensores apilables), pero distintos batches
tienen tamaños distintos.
- **Precalcula** la resolución de cada muestra y su bucket → guárdalo en el `.json` del shard (no recalcules
  por epoch).
- kohya, SimpleTuner, ai-toolkit, OneTrainer traen bucketing nativo (`enable_bucket`). Si montas loader propio,
  un **bucket sampler** que agrupe índices por aspecto antes de batchear.
- NovelAI V3 documentó mejoras de bucketing+resolución sobre SDXL — referencia técnica útil. [verificado]

## Pipeline de preparación (de fotos crudas a shards)
```
imágenes + captions → curar/dedup/caption (ref 153) → calcular aspect+bucket
   → empaquetar en .tar (tarp / wds.ShardWriter, ~10k muestras/shard)
   → subir a R2/S3 → entrenar leyendo por URL en streaming
```
Precomputa lo caro **una vez al empaquetar**: resolución, bucket, y opcionalmente **latentes VAE + embeddings de
texto** (latent caching) → el training salta el VAE/encoder y vuela. Esto se ata al ETL de [[64-data-pipelines-mlops-etl]].

## Sizing y rendimiento
- **Shard 100MB-1GB**: muy chico = overhead de apertura; muy grande = shuffle pobre y reanudación tosca.
- **Buffer de shuffle ≥ varios miles** o el barajado intra-shard es insuficiente (lotes correlacionados).
- **`num_workers`**: sube hasta saturar I/O o CPU de decode/resize. JPEG decode + resize suele ser el cuello CPU
  → considera decode en GPU (nvjpeg/DALI) si el dataloader no alcanza la GPU.
- **Latent caching** elimina VAE+text-encoder del loop: el dataloader entrega tensores listos → mayor throughput.

## Gotchas
1. **No random-access dentro de un .tar** → bucketing global + shuffle perfecto chocan con WDS. Solución:
   pre-ordena por bucket al empaquetar, o usa formato indexado (webshart/MDS) si necesitas acceso aleatorio real.
2. **Shards ≤ workers×ranks** → workers ociosos y datos repetidos. Genera muchos shards pequeños, no pocos enormes.
3. **Reanudar epoch con WDS no es determinista** out-of-the-box → para spot/checkpointing usa MosaicML Streaming.
4. **Decode CPU-bound**: la GPU espera al dataloader, no al revés. Perfila `GPU util`; si baja, el problema es I/O.
5. **Latentes cacheados atan VAE+resolución**: si cambias VAE o resolución, **recachea** o entrenas con basura.

## Fuentes
- https://huggingface.co/docs/hub/en/datasets-webdataset · https://github.com/bghira/webshart
- https://arxiv.org/pdf/2409.15997 (NovelAI V3, bucketing)

Cruza con [[153-dataset-curation-captioning-visual]] y [[64-data-pipelines-mlops-etl]].
