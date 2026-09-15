# 125 · Diffusers offloading y memoria (caber en la VRAM sin morir de lento)

> Cuando el modelo no entra en VRAM, la pregunta no es *si* offloadear sino *cuánto* throughput
> sacrificas. Cada palanca tiene un costo de velocidad concreto: elige el mínimo que te haga caber.

## Las tres estrategias de offload (de menos a más agresivo)

| Estrategia | API | Granularidad | Ahorro VRAM | Penalización velocidad |
|---|---|---|---|---|
| Model CPU offload | `pipe.enable_model_cpu_offload()` | sub-modelo entero (UNet/DiT, VAE, TE) | alto (mantiene 1 componente en GPU) | ~1.2-1.5x más lento |
| Group offloading | `module.enable_group_offload(...)` | grupos de capas (`ModuleList`/`Sequential`) | muy alto | ~1.1-1.3x **con CUDA streams** |
| Sequential CPU offload | `pipe.enable_sequential_cpu_offload()` | submódulo individual (capa por capa) | extremo (mínimo absoluto) | **brutal**, 5-10x+ (sync por capa) |

Regla: empieza por `enable_model_cpu_offload`. Si aún hace OOM, salta a **group offloading con streams**
(mejor relación VRAM/velocidad que sequential). `enable_sequential_cpu_offload` es el último recurso
para HW muy chico — sangra throughput por transferencias HtoD/DtoH síncronas en cada capa.

> **No combines** `enable_model_cpu_offload()` con `.to("cuda")` manual ni con accelerate device_map:
> el hook de offload reordena los `.to()`. Llama el offload **después** de construir el pipe y nunca muevas
> el pipe a cuda a mano. `enable_model_cpu_offload(device="cuda")` si tienes varias GPUs.

## Group offloading: el punto dulce (diffusers ≥ 0.33)

```python
from diffusers import AutoModel
from diffusers.hooks import apply_group_offloading

transformer = AutoModel.from_pretrained(..., torch_dtype=torch.bfloat16)
transformer.enable_group_offload(
    onload_device=torch.device("cuda"),
    offload_device=torch.device("cpu"),
    offload_type="leaf_level",        # o "block_level" con num_blocks_per_group=N
    use_stream=True,                  # prefetch con CUDA stream → oculta latencia de transferencia
    low_cpu_mem_usage=True,           # pin diferido: baja RAM CPU al nivel de sequential
)
```

- `use_stream=True`: carga la **siguiente** capa a GPU mientras la actual computa → casi gratis en velocidad,
  VRAM mínima. Requiere **memoria pinned** → sube RAM de CPU. `low_cpu_mem_usage=True` (PR #11106) hace el
  pinning al onloadear el grupo, dejando la RAM similar a sequential a cambio de algo de velocidad.
- `offload_type="block_level"` + `num_blocks_per_group`: más grupos = menos VRAM, más overhead de transferencia.
- Funciona sobre cualquier `nn.Module` (no solo pipes): ideal para DiT de video (LongCat, Wan, Hunyuan).

## VAE: tiling y slicing (decode de imágenes/frames grandes)

```python
pipe.enable_vae_slicing()   # decodifica el batch de a 1 imagen → ahorra VRAM en batches grandes
pipe.enable_vae_tiling()    # divide el frame en tiles solapados → habilita 4K / video largo
```

- **Slicing**: ataca VRAM proporcional al **batch**. Costo casi nulo.
- **Tiling**: ataca VRAM proporcional a la **resolución**. Puede dejar costuras (seams) sutiles; el VAE moderno
  usa overlap. Imprescindible para upscale/video donde el decode del VAE es el pico de VRAM, no el denoiser.

## Attention slicing (legacy, casi obsoleto)

```python
pipe.enable_attention_slicing()   # "auto" o int: parte la matriz QK por cabezas
```
Reduce el pico de la matriz de atención a cambio de velocidad. **Hoy casi siempre peor** que usar un backend
de atención eficiente (SDPA/FlashAttention/Sage) que ya es O(N) en memoria. Úsalo solo en GPUs sin soporte
de esos kernels. Cruza con [[126-attention-backends-fa3-xformers-sage]].

## memory_format = channels_last

```python
pipe.unet.to(memory_format=torch.channels_last)   # idem transformer/vae
```
No ahorra VRAM; **mejora velocidad** en convoluciones (UNet) al alinear el layout con los kernels de cuDNN.
Para DiT puros (sin convs) el efecto es marginal. Gratis probarlo, mide. Combina con `torch.compile`
(ver [[127-torch-compile-tensorrt-difusion]]).

## dtype y carga: lo que haces SIEMPRE

```python
pipe = DiffusionPipeline.from_pretrained(
    repo, torch_dtype=torch.bfloat16,   # bf16 en Ampere+ ; fp16 en Turing/Volta
    low_cpu_mem_usage=True,             # default True: carga pesos directo al device sin duplicar en RAM
)
```
- **bf16 vs fp16**: bf16 (rango dinámico de fp32, menos precisión) evita los NaN/overflow típicos de fp16 en
  modelos grandes. En Ampere/Ada/Hopper usa **bf16**. fp16 solo si el HW no soporta bf16.
- `low_cpu_mem_usage=True` (default): mete los pesos al device a medida que carga el `safetensors`, sin
  materializar el state_dict completo en RAM. Bajarlo a `False` solo si depuras carga.
- Cargar en media precisión es lo primero: parte la VRAM/RAM a la mitad antes de cualquier offload.

## Orden de palancas (receta)

1. `torch_dtype=bf16` + `low_cpu_mem_usage` (siempre).
2. Backend de atención eficiente ([[126-attention-backends-fa3-xformers-sage]]).
3. `enable_vae_tiling()` + `enable_vae_slicing()` (baratísimo, ataca el pico del VAE).
4. ¿Aún OOM? `enable_model_cpu_offload()`.
5. ¿Aún OOM? `enable_group_offload(use_stream=True, low_cpu_mem_usage=True)`.
6. Último recurso HW chico: `enable_sequential_cpu_offload()`.

Cruza con [[129-vram-mid-run-oom-hands-on]] (OOM en mitad del run y fragmentación),
[[12-cuantizacion-hands-on]] (cuantizar pesos para no offloadear) y [[10-profiling-optimizacion-kernels]]
(medir dónde está realmente el pico de VRAM antes de tocar nada).
