# 257 · Difusión on-device en Apple Silicon (CoreML / MLX)

> Un M-series con memoria unificada es una GPU de inferencia gratis que ya está en el bolsillo del cliente.
> Bien convertido, FLUX-4bit o SDXL corren localmente sin RunPod, sin egress, sin enviar la foto a un servidor.

## Por qué Apple Silicon gana en edge
La **memoria unificada** es un solo pool que CPU, GPU y Neural Engine direccionan sin copias ni bus PCIe. Un M3/M4 con 16-32GB usa casi todo ese pool como "VRAM" → cargas un modelo de 12B en 4-bit donde una RTX de 8GB ni arranca. No hay `cudaMemcpy`: el tensor que escribe el CPU lo lee la GPU en sitio. Eso cambia la economía: la inferencia que pagarías en la nube la corre el dispositivo del usuario.

## Las dos rutas (no son la misma)
| | **CoreML** (`apple/ml-stable-diffusion`) | **MLX** (`mlx`, `mflux`) |
|---|---|---|
| Ejecuta en | ANE + GPU + CPU (scheduler de Apple) | GPU (Metal), kernels MLX |
| Mejor para | apps empotradas, app del App Store, ANE | scripting, FLUX/LLM, iteración rápida |
| Conversión | `torch → coremltools → .mlpackage` (offline, lenta) | carga directa de pesos HF, cuantiza en segundos |
| Cuantización | palettization 6/4-bit (coremltools) | group-wise uniforme, `group_size=64` por defecto |
| Control fino | bajo (la caja negra decide compute units) | alto (eliges precisión por capa) |

Regla: **producto cerrado para usuario final → CoreML/ANE**; **laboratorio, FLUX, prototipo → MLX**.

## CoreML: el flujo de conversión que muerde
1. `python -m python_coreml_stable_diffusion.torch2coreml --convert-unet --convert-text-encoder ...` genera los `.mlpackage`. Lento (minutos por componente) y consume RAM.
2. `--attention-implementation SPLIT_EINSUM` → optimizado para **ANE** (móvil/iPhone). `ORIGINAL` → mejor en **GPU** de Mac. Elegir mal deja la mitad del rendimiento en la mesa.
3. `--quantize-nbits 6` (o 4) hace **palettization**: comparte una paleta de pesos por capa. 6-bit suele ser el punto dulce calidad/tamaño; 4-bit degrada visiblemente en UNet.
4. El `.mlpackage` se empaqueta en la app Swift y se invoca con el framework `StableDiffusion`.

## MLX: el camino corto
```bash
pip install mflux            # port línea-a-línea de Diffusers a MLX
mflux-generate --model dev --quantize 4 --steps 4 --prompt "..."   # FLUX-dev 12B en 4-bit
```
- Cuantiza al vuelo: descargas el modelo HF, `mlx` lo comprime en segundos a 4/8-bit, sin pipeline de conversión.
- **M5** estrena aceleradores neuronales en la GPU: FLUX-dev-4bit (1024²) ≈ **3.8× más rápido que M4** [no verificado el factor exacto, fuente Apple ML Research].

## Presupuesto de memoria / velocidad (orientativo)
| Modelo | Precisión | RAM unificada mínima | Notas |
|---|---|---|---|
| SD 1.5 | fp16 / 6-bit | 8 GB | viable hasta en M1 base |
| SDXL | 6-bit palettized | 16 GB | varios pasos por imagen en GPU |
| FLUX-dev 12B | 4-bit | 24-32 GB | usable solo con memoria unificada grande |

## Gotchas
- **8GB no es 8GB**: el SO y la app comen pool; un FLUX-4bit en 16GB puede empujar a swap → se cae o se arrastra.
- **ANE no es la GPU**: `SPLIT_EINSUM` rinde en ANE pero limita resoluciones/atención; no asumas que "compute units = all" es lo más rápido, mídelo.
- **Conversión ≠ una vez por modelo**: cada resolución/scheduler/LoRA fundido puede requerir reconvertir. Versiona los `.mlpackage`.
- **Térmica móvil**: en iPhone, generación sostenida tira el clock; diseña para 1-4 pasos (ver [[260-quant-distill-para-edge]]), no 30.
- **mlx-community en HF** ya publica cientos de modelos pre-cuantizados → no reconviertas lo que ya existe.

Cruza con [[73-edge-computing-wasm]], [[258-onnx-tflite-mobile-diffusion]] y [[260-quant-distill-para-edge]].
