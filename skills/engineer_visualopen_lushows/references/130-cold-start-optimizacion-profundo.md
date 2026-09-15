# 130 · Cold-start: optimización profunda (más allá del Network Volume)

> El volumen mató la re-descarga (ver [[113]]). Pero del frío aún quedan minutos: import de libs,
> deserializar pesos, copiarlos a VRAM, inicializar CUDA. Aquí se exprimen esos minutos uno a uno.

## El frío descompuesto (después de ya tener pesos en disco)
| Fase | Qué pasa | Palanca |
|---|---|---|
| Import de libs | `import torch`, diffusers, flash_attn cargan .so pesados | lazy import |
| Init CUDA | primer kernel compila/inicializa contexto | pre-warm |
| Leer pesos de disco | 27GB safetensors → RAM | mmap, lazy |
| Deserializar a tensores | construir el `state_dict` | `low_cpu_mem_usage` |
| Copiar a VRAM | host→device PCIe | cargar directo a device |
| Compilar grafo | `torch.compile` recompila en frío | cache de compile / saltar en frío |

## safetensors + mmap (no dupliques los pesos en RAM)
safetensors usa **mmap**: lee tensores **perezosamente** desde disco con memory-mapping del OS, sin
copiarlos a RAM. Es zero-copy y el formato estándar — evita pickle (lento, inseguro). Carga solo lo
que tocas. Gotcha contra-intuitivo: cargar safetensors **directo a GPU puede ser más lento** que
CPU→GPU en algunos casos (issue conocido de diffusers); **mídelo en tu hardware**, no lo asumas.

## `low_cpu_mem_usage=True` — no construyas el modelo dos veces
Por defecto, transformers/diffusers crea el modelo con pesos random y **luego** los sobre-escribe →
pico de RAM ~2x y tiempo extra. Con `low_cpu_mem_usage=True` (default en `from_pretrained` moderno)
crea el módulo en **meta device** (sin memoria) y materializa cada tensor directo desde el archivo.
Menos RAM, menos tiempo. Combínalo con `device_map="cuda"`/`{"":"cuda"}` para saltarse el rebote por CPU.

## Cargar pesos directo a GPU
```python
pipe = Pipeline.from_pretrained(
    path, torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True, device_map="cuda",   # materializa en VRAM, no en RAM
)
```
Evita el patrón `from_pretrained(...).to("cuda")` que primero llena RAM y luego copia. [no verificado: soporte de `device_map="cuda"` por pipeline/versión de diffusers — algunos pipelines aún requieren `.to()`]

## Lazy import de libs pesadas
`flash_attn`, `xformers`, `bitsandbytes`, `cv2`, `transformers` cargan .so grandes en el import.
Si el handler los importa al tope del archivo, los pagas **en cada cold start** aunque no siempre se
usen. Mueve el import **dentro** de la función que los necesita:
```python
def decode(...):
    import cv2          # se paga solo cuando hace falta, no al arrancar
```
Importa eager **solo** lo que el camino caliente siempre toca.

## Pre-warm del worker
Tras cargar, ejecuta **una inferencia dummy** (1 paso, resolución mínima) en el arranque para:
forzar el init de CUDA, compilar kernels JIT, y disparar la primera recompilación de `torch.compile`
**antes** de que llegue el primer job real. El usuario ve un frío más largo una vez, pero el primer
job real ya cae en estado caliente. En serverless, hazlo en la inicialización del handler, no por job.

## torch.compile en frío: el enemigo silencioso
`torch.compile` recompila desde cero en cada proceso nuevo → puede añadir **minutos** al primer
forward. Opciones: (a) **no compilar** en serverless de baja concurrencia; (b) `mode="reduce-overhead"`
y aceptar la primera compilación dentro del pre-warm; (c) persistir el `TORCHINDUCTOR_CACHE_DIR` en el
Network Volume para reusar artefactos entre workers. [no verificado: portabilidad de la cache de Inductor entre máquinas distintas]

## Snapshot/restore de CUDA (frontera)
Algunas plataformas serverless ofrecen **snapshot de memoria** (CRIU/CUDA checkpoint): congelar el
proceso con pesos ya en VRAM y restaurarlo en milisegundos. Si tu proveedor lo soporta, es la bala de
plata del frío (de minutos a segundos). RunPod **FlashBoot** apunta a esto reusando workers calientes.
[no verificado: disponibilidad y semántica exacta de snapshot CUDA por proveedor en 2026]

## Paralelizar la descarga (cuando aún bajas algo)
Si parte de los pesos no está en el volumen, baja con concurrencia: `hf_transfer`
(`HF_HUB_ENABLE_HF_TRANSFER=1`) usa descarga acelerada multi-conexión en Rust → bastante más rápido
que el cliente HTTP estándar. Útil para el primer poblado del volumen y para LoRAs/adapters externos.

## Baked vs volumen (recordatorio)
Hornear pesos en la imagen Docker = **cero descarga** pero pull lento y build caro; el frío de carga a
VRAM persiste igual. El volumen gana para modelos enormes que cambian poco. Lo óptimo: **imagen con
deps + caches de compile**, **volumen con pesos** (ver [[113]]).

## Orden de ataque del frío
1. Volumen (ya hecho) → mata re-descarga.
2. `low_cpu_mem_usage` + carga directa a device → mata el rebote por RAM.
3. Lazy import → recorta segundos del import.
4. Pre-warm dummy → mueve el costo de CUDA/compile fuera del primer job real.
5. Decide `torch.compile` (saltar o cachear).
6. Si el proveedor lo da: snapshot/FlashBoot → frío de segundos.

Cruza con [[113-network-volume-modelos-grandes]] y [[112-execution-timeout-cold-start-economics]].
