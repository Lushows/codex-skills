# 127 · torch.compile + TensorRT para difusión (compilar el DiT/UNet una vez por worker)

> El denoiser (DiT/UNet) se ejecuta N veces por job (un paso por sampling step). Compilarlo amortiza
> el overhead de Python/lanzamiento de kernels en cada paso → 1.3-2.4x gratis. La trampa: el **warmup**.

## torch.compile sobre el denoiser

```python
pipe.transformer = torch.compile(           # o pipe.unet
    pipe.transformer,
    mode="max-autotune",      # autotunea kernels Triton/CUDA Graphs → más rápido, compila lento
    fullgraph=True,           # falla si hay graph break; el forward de un DiT es 1 grafo contiguo
    dynamic=False,            # shapes estáticas (default) → más rápido; True = un grafo dinámico
)
```

| `mode` | Qué hace | Cuándo |
|---|---|---|
| `default` | fusión básica, compila rápido | iteración/dev |
| `reduce-overhead` | CUDA Graphs, mata overhead de lanzamiento | batch chico, muchos steps |
| `max-autotune` | busca los mejores kernels (Triton) | **producción** (compila lento, corre rápido) |

- **`fullgraph=True`**: compílalo desde el inicio del bring-up. Un graph break silencioso convierte el speedup
  en ruido. El forward de un DiT/UNet suele ser un solo grafo → si rompe, hay un `.item()`, branch dependiente
  de dato, o un op no soportado escondido.
- **`mode="max-autotune"`** es el estándar de facto para difusión; la autotune añade minutos al primer run.

## Recompilaciones: el asesino silencioso del throughput

`torch.compile` cachea por **firma de shapes**. Si cambia resolución, batch, nº de frames o longitud de prompt,
**recompila** (otra vez minutos). Defensas:

- **`dynamic=True`**: tras la primera recompilación intenta UN grafo que cubra shapes variables. Pierdes algo de
  velocidad pico pero evitas N compilaciones. Úsalo si tus inputs varían (video de duración variable, multi-resolución).
- **Estandariza inputs**: padea a un set fijo de shapes (ej. resoluciones canónicas) → cae siempre en cache.
- `torch._dynamo.config.cache_size_limit`: súbelo si manejas varias shapes fijas y ves "recompiling" en logs.
- Diagnóstico: `TORCH_LOGS="recompiles"` (o `"+dynamo"`) imprime **por qué** recompiló (qué guard falló).

## Regional / regional compilation (cold-start barato)

En vez de compilar el modelo entero, compila **un bloque transformer** y reúsalo en todas las capas:

```python
pipe.transformer.compile_repeated_blocks(fullgraph=True)   # helper en diffusers (DiTs)
```

Mismo speedup runtime que full-graph en la mayoría de DiTs, pero **8-10x menos tiempo de compilación** → cold-start
del worker mucho más corto. Es la opción por defecto cuando el warmup te está matando la economía serverless
(ver [[112-execution-timeout-cold-start-economics]]).

## Warmup: compilar 1 vez por worker (patrón producción)

`torch.compile` es **lazy**: compila en la **primera** forward con cada shape. En serverless eso significa que
el **primer job del worker frío** paga la compilación (minutos) — inaceptable si timeoutea el cliente. Patrón:

1. En el **arranque del worker** (no por job), tras cargar pesos, corre un **forward dummy** con las shapes
   canónicas para disparar la compilación.
2. Idealmente persiste el cache de Inductor: `TORCHINDUCTOR_CACHE_DIR=/runpod-volume/inductor` en el Network
   Volume → arranques siguientes leen kernels compilados en vez de recompilar. Cruza con [[113-network-volume-modelos-grandes]].
3. Marca el worker "ready" **solo después** del warmup.

```python
# en init del worker, una vez:
with torch.no_grad():
    _ = pipe(**dummy_inputs_canonicos)   # fuerza compile; descarta salida
```

## FP8 y cuantización (Hopper/Ada/Blackwell)

- **torchao + diffusers**: cuantiza el DiT a fp8 (`float8_dynamic_activation_float8_weight`) y combínalo con
  `torch.compile` → speedup adicional en HW con tensor cores FP8 (**Ada SM89, Hopper SM90, Blackwell**). En
  Blackwell, **MXFP8/NVFP4** vía torchao. En GPUs sin FP8 (Ampere) usa INT8.
- Orden correcto: **cuantizar primero, `torch.compile` después** (compila los kernels cuantizados).

## TensorRT / Torch-TensorRT (la milla extra)

`torch-tensorrt` compila el grafo a un engine TensorRT (vía `torch.compile` backend `"tensorrt"` o AOT export).
Más rápido que Inductor en muchos DiT, a costa de un pipeline de build más rígido.

| Stack | Speedup típico (vs PyTorch FP16) | Costo |
|---|---|---|
| `torch.compile` max-autotune | 1.3-1.8x | warmup; cero deps extra |
| Torch-TensorRT FP16 | ~1.5x | build de engine; engine atado a shapes/GPU |
| Torch-TensorRT **FP8** (FLUX, RTX 6000 Ada) | ~2.0-2.4x | calibración/quant; engine no-refittable en FP4 |
| TensorRT INT8/FP8 PTQ (SDXL) | 1.7-1.95x vs `torch.compile` FP16 | calibración PTQ |

Gotchas TensorRT: el **engine es específico de GPU y de rango de shapes** (recompilar para otra SM o resolución);
build lento → hornéalo en la imagen o cachéalo en volumen; pesos de alta precisión en FP4 double-quant **no son
refittables** [no verificado — story FP8+refit aún evoluciona en 2026]. Para iteración rápida, `torch.compile`
suele ganar; TensorRT para cargas estables de alto volumen.

## stable-fast / OneFlow

`stable-fast` y `oneflow` fueron aceleradores de difusión populares en 2023-24 (fusión + trace propio). En 2026
el ecosistema convergió en **`torch.compile` + torchao + dispatcher de atención**, que cubren el mismo terreno
con mantenimiento activo. **No los adoptes en proyectos nuevos** salvo que un repo concreto dependa de ellos
[no verificado — verificar estado del repo antes de usar].

## Receta

1. Backend de atención eficiente ([[126-attention-backends-fa3-xformers-sage]]) — base.
2. `torch.compile(mode="max-autotune", fullgraph=True)` o `compile_repeated_blocks` si el cold-start aprieta.
3. Cuantiza a fp8/int8 (torchao) **antes** de compilar si el HW lo soporta.
4. **Warmup en init del worker** + cache de Inductor en volumen.
5. ¿Volumen alto y estable? Evalúa Torch-TensorRT FP8.

Cruza con [[11-tensorrt-onnx-compilacion-aot]] (export AOT/ONNX a fondo) y
[[112-execution-timeout-cold-start-economics]] (el warmup vs el timeout/cold-start).
