# 126 · Attention backends (FA2 · FA3 · xformers · SDPA · Sage)

> El backend de atención es la palanca de velocidad #1 en un DiT/UNet, y la fuente #1 de errores de ABI.
> El kernel "más rápido" que no compila contra tu torch/CUDA es 0 TFLOPs. Elige por compatibilidad, luego velocidad.

## El menú

| Backend | Requiere | Velocidad | VRAM | Notas |
|---|---|---|---|---|
| PyTorch **SDPA** (`native`) | nada (built-in torch) | buena | O(N) | default seguro; subkernels: flash/efficient/cudnn/math |
| **FlashAttention-2** (`flash`) | `flash-attn`, Ampere+ (SM80+) | muy buena | O(N) | el caballo de batalla en A100/L40S/4090 |
| **FlashAttention-3** (`_flash_3`) | FA3 build, **óptimo en Hopper SM90** | máxima (fp16/fp8) | O(N) | FP8 en H100 → ~1.2 PFLOPs; en no-Hopper no aporta su asincronía |
| **FlashAttention-4** (`flash_4_hub`) | kernels hub, Hopper/Blackwell | máxima | O(N) | reciente; vía `kernels`, sin compilar local |
| **xFormers** (`xformers`) | `xformers` (match torch/CUDA) | buena | O(N) | el fallback robusto y portable cuando FA falla |
| **SageAttention** (`sage`) | `sageattention`, INT8/FP8 | 2-5x vs FA | O(N) | atención **cuantizada** (INT8 QK [+ FP8 PV]); cuidar calidad |

## Cómo forzarlo en diffusers (dispatcher, ≥ 0.33)

```python
# Persistente, sobre el módulo (NO el pipe):
pipe.transformer.set_attention_backend("flash")     # "_flash_3" / "xformers" / "sage" / "native" ...
pipe.transformer.reset_attention_backend()          # vuelve al default (SDPA)

# Temporal, scope:
from diffusers.models.attention_dispatch import attention_backend
with attention_backend("_flash_3_hub"):
    img = pipe(prompt).images[0]
```

- Variantes `*_hub` (`_flash_3_hub`, `flash_4_hub`, `sage_hub`) cargan kernels precompilados de la librería
  [`kernels`](https://github.com/huggingface/kernels) desde el Hub → **sin compilar `flash-attn` localmente** (esquiva el infierno de ABI).
- `_native_cudnn` / `_native_flash` / `_native_efficient` / `_native_math`: fuerzan un subkernel de SDPA.
- `DIFFUSERS_ATTN_CHECKS=yes`: valida device/dtype/shape antes de cada attn (debug; añade overhead — off en prod).
- En código fuera de diffusers (repos crudos): suele haber flags tipo `--attention xformers` o env del repo;
  algunos modelos auto-detectan `flash_attn` por import y caen a SDPA si falla el import.

## ABI: por qué FlashAttn explota (el bug recurrente)

`flash-attn` y `xformers` traen **kernels CUDA compilados** → la rueda debe coincidir EXACTO con:
versión de **torch**, **CUDA toolkit** (cu121/cu124/cu128…), **ABI de C++** (cxx11abi TRUE/FALSE) y **Python**.
Síntomas: `undefined symbol: _ZN...`, `ImportError ... flash_attn_2_cuda.so`, o el módulo importa pero
`CUDA error: no kernel image is available for execution` (rueda compilada para otra SM).

- Instala la rueda que **matchea tu torch** (no `pip install flash-attn` a ciegas): usa la matriz GPU↔CUDA↔torch.
- Si no hay rueda → `MAX_JOBS=4 pip install flash-attn --no-build-isolation` (compila local, lento, exige nvcc).
- **Atajo recomendado**: backend `*_hub` vía `kernels` → kernel correcto para tu HW sin build local.

## FA3 en NO-Hopper: el caso LongCat (debug real)

FA3 (`_flash_3`) está diseñado para la asincronía de **Hopper (SM90)**: TMA + wgmma + FP8. En **Ampere/Ada**
(A100, L40S, 4090, A6000) FA3 **no aporta** su ventaja y a menudo **falla al cargar el kernel o da peor
rendimiento/NaN**. En el worker de **LongCat-Avatar** corriendo en GPU no-Hopper, la cascada fue:

1. FA3 fallaba/era inestable → **se desactivó FA3**.
2. FA2 (`flash`) dio choques de ABI / kernel no disponible para la SM → **se desactivó FA2**.
3. **Se forzó `xformers`** como backend → estable, buena velocidad, portable. Producción sobre xformers.

Lección: en HW no-Hopper, **xformers es el fallback de oro**. FA3 solo si confirmas SM90. No persigas el kernel
"teóricamente más rápido" si revienta el cold-start del worker. Cruza con [[111-longcat-avatar-runpod-produccion]].

## Sage Attention (cuantizada): cuándo sí

`sageattention` cuantiza Q/K a INT8 (y PV a FP8 en variantes `_sage_qk_int8_pv_fp8_cuda_sm90`) → **2-5x vs FA**
con pérdida de calidad mínima reportada. Disponible ya en **Hopper** (iguala a FA3-FP8 con mejor precisión).
Úsalo en inferencia de video/imagen donde la atención domina el tiempo y toleras una cuantización ligera.
**Valida calidad** (FID/FVD/CLIP) antes de meterlo en prod — es lossy por diseño.

## Impacto en VRAM/velocidad

Todos los backends "flash-like" (FA2/3/4, xformers, SDPA-flash, Sage) son **O(N) en memoria** (sin materializar
la matriz N×N) → habilitan secuencias/resoluciones largas. La diferencia entre ellos es **velocidad**, no VRAM.
El único que sube/baja VRAM notablemente es Sage (cuantización reduce algo el footprint de activaciones).

> La mayoría de estos backends compilan con `torch.compile` **sin graph breaks** → combínalos para el máximo
> speedup. Cruza con [[127-torch-compile-tensorrt-difusion]] y [[10-profiling-optimizacion-kernels]].
