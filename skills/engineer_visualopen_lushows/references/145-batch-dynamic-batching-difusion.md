# 145 · Batching y dynamic batching en difusión

> Batchear difusión sube throughput barato (amortizas el lanzamiento de kernels sobre N samples), pero choca con VRAM, CFG y resoluciones mixtas.
> Difusión batchea DISTINTO a un LLM: el batch es por paso de denoising, no por token, y todos los samples del batch comparten el "contrato del tensor".

## Por qué batchear difusión funciona
La GPU está infrautilizada con batch=1 en resoluciones bajas: cada paso del sampler lanza los mismos kernels para un solo latente. Agrupar K prompts en `[K, C, H, W]` corre el UNet/DiT una vez por paso para los K → el overhead fijo (lanzar kernels, leer pesos de HBM) se amortiza. Ganancia típica: throughput sube casi lineal hasta saturar los CUDA cores o la VRAM, **sin** subir mucho la latencia por imagen.

## La diferencia clave vs LLM
| | LLM (continuous batching) | Difusión |
|---|---|---|
| Unidad de iteración | token (autorregresivo, longitud variable) | paso de denoising (fijo: N steps) |
| Por qué entran/salen | secuencias terminan en momentos distintos → hueco se rellena | todos hacen los mismos N pasos → batch homogéneo |
| Estado por request | KV-cache que crece | latente de tamaño fijo (no crece) |
| Restricción de co-batch | mismo modelo | **mismo shape + mismos params CFG-sensibles** |

En LLM el continuous batching gana porque las secuencias tienen longitudes dispares y se reemplazan token a token (ver [[14-batching-kvcache-throughput]]). En difusión clásica todos los samples corren los mismos pasos, así que el **static/dynamic batching** (juntar al admitir, correr juntos) ya captura casi toda la ganancia. El *continuous batching para difusión* (paso a paso, ej. vLLM-omni) existe y aporta cuando los requests tienen **distinto nº de steps** o llegan desfasados: un request que termina sus N pasos sale del batch y otro entra en el siguiente paso, sin esperar a que termine todo el batch.

### Static vs dynamic vs continuous (qué usar)
- **Static batching**: juntas N requests en cola y corres el batch completo de principio a fin. Simple, óptimo para offline homogéneo. Malo si los requests llegan desfasados (los primeros esperan).
- **Dynamic batching**: el servidor forma el batch al admitir (ventana de tiempo/tamaño), luego lo corre fijo. Lo que dan Triton/TorchServe. Buen default para difusión clásica con N steps iguales.
- **Continuous (step-level)**: requests entran/salen entre pasos. Solo aporta con steps heterogéneos o llegadas desfasadas; scheduler complejo. No lo construyas si tu carga es homogénea — no compensa.

## El gotcha de CFG (clasifier-free guidance)
CFG corre DOS forward por paso: condicional + incondicional. La implementación estándar **ya batchea** esos dos en un tensor `[2K, ...]` (cond arriba, uncond abajo). Implicaciones:
- Tu batch efectivo en VRAM es **2× el nº de prompts** cuando CFG está activo. Un "batch de 4" son 8 forwards.
- Requests con CFG distinto (uno con guidance, otro sin, o "CFG zero-init" en ciertos pasos) **no co-batchean** limpio: cambian la forma del tensor de guía. Regla de admisión: solo junta requests que compartan el contrato del tensor de denoise (shape + campos de sampling sensibles a CFG). Distinto nº total de steps SÍ puede compartir batch; distinto shape/CFG no.

## Resolución mixta = el muro
Difusión opera sobre latentes `[C, H/8, W/8]`. Dos prompts a 1024×1024 y 1024×768 tienen **shapes distintos** → no se apilan en un tensor sin padding. Opciones:
- **Bucketing por resolución**: cola separada por (H,W); cada bucket batchea homogéneo. Es lo que hace la mayoría en producción.
- **Padding a la mayor** del batch: desperdicia cómputo en el padding y puede alterar el resultado (atención sobre zonas vacías) — evítalo salvo diferencias mínimas.
- Regla práctica: **una resolución por batch**. Mezclar resoluciones es la causa #1 de "mi dynamic batcher no junta nada".

## Límites de VRAM por batch
La VRAM del batch ≈ `pesos (fijo) + K·activaciones(paso) · (2 si CFG)`. Las activaciones del UNet/DiT escalan con K y con H·W (atención es cuadrática en tokens espaciales). Por eso:
- Resolución alta (1024+, o video) → batch chico (2-4) o batch=1; el OOM aparece a mitad de un paso, no al cargar (ver [[OOM mid-run]] en la skill).
- Sin xformers/flash-attn el batch máximo cae fuerte; con attention eficiente sube 2-3×.
- Mide el batch máximo empíricamente por resolución y déjalo como tope duro; un batch que OOM mata el worker entero, no solo ese request.

### Números de referencia [aprox, depende de GPU/modelo]
- SDXL 1024² en A100 40GB con flash-attn: batch máx ≈ 8-12 sin CFG, ≈ 4-6 con CFG (cuenta el 2×).
- SD1.5 512² en A100: batch 16-32 cómodo. La atención cuadrática en tokens espaciales es lo que limita al subir resolución.
- Video (latentes temporales `[T,C,H,W]`): casi siempre batch=1; el eje temporal ya consume el presupuesto. Segmenta el clip en vez de batchear.

## Trade-off latencia vs throughput (la palanca)
- **max_queue_delay** (Triton [[144-triton-inference-server-difusion]]) o ventana de admisión en tu scheduler: esperar X ms para llenar el batch. Más espera → batches más llenos → más throughput, peor p50/p99 del request individual.
- Para UX interactiva (un usuario esperando): delay bajo o batch=1, prioriza latencia.
- Para generación masiva offline (campaña, dataset): delay alto, batch grande, maximiza imágenes/seg.
- Continuous (step-level) batching da lo mejor de ambos cuando hay mezcla de cargas, a costa de un scheduler más complejo.

## Padding de resoluciones (cuándo sí)
Padding es aceptable solo para diferencias pequeñas (ej. 1024×1024 vs 1024×960): rellenas el latente menor al mayor y recortas la salida. Riesgos: la atención global ve la zona padded (artefactos en bordes) y desperdicias FLOPs. Para diferencias grandes (1024 vs 512) el padding cuesta más que servir por separado → bucketing siempre gana. Variante segura: agrupa por **área** (H·W) y dentro del bucket fuerza una resolución canónica, redimensionando entrada/salida fuera del modelo.

## Scheduling práctico
Una cola por bucket + un planificador que, en cada hueco de GPU, saca el batch más lleno (o el más viejo si vence el `queue_delay`). Prioriza requests interactivos con un carril de baja latencia (batch chico, sin espera) y manda los de campaña al carril de throughput (batch grande, delay alto). Idempotencia por `request_id` para que un retry no genere dos imágenes.

## Checklist de implementación
1. Bucket por (H, W, dtype). 2. Dentro del bucket, junta hasta `max_batch` o hasta `queue_delay`. 3. Cuenta CFG como 2× en el presupuesto VRAM. 4. Tope de batch medido empíricamente por resolución. 5. Mide `queue_duration` vs `compute_duration` para tunear el delay. 6. Carga-testea con mezcla realista de resoluciones, no solo una.

Cruza con [[14-batching-kvcache-throughput]] y [[19-load-testing-capacity-planning]].
