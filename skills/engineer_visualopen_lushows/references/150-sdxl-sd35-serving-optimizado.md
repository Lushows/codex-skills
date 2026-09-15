# 150 · SDXL y SD3.5 self-hosted optimizado (cuándo siguen ganando en 2026)

> FLUX es más bonito, pero en 2026 SDXL sigue siendo el rey de **calidad/costo**: ecosistema enorme de
> LoRA/ControlNet, corre en 8-12GB, y con Lightning/LCM hace imágenes en <1s. SD3.5 cubre el hueco intermedio.

## SDXL: por qué no muere
- 3.5B params (UNet) + 2 text encoders (CLIP-L + OpenCLIP-bigG). Cabe en **8-12GB** fp16.
- **Licencia**: OpenRAIL++ (comercial libre). Sin la trampa NC de FLUX dev.
- Ecosistema: miles de LoRA, ControlNets maduros, IP-Adapter, inpaint. Imbatible para pipelines de marca.
- Mejor **throughput/$** cuando no necesitas el realismo extremo de FLUX: en un A100 haces 5-10x más imágenes/hora.

### Componentes SDXL
| Pieza | Rol | Nota |
|---|---|---|
| Base UNet | gen principal | fp16 estándar |
| **Refiner** | últimos ~20% de pasos (denoise final) | opcional; mejora detalle/textura. Patrón `denoising_end`/`denoising_start`. Muchos ya NO lo usan (base sola basta con buen sampler) |
| **VAE** | decode latente→pixel | usar `madebyollin/sdxl-vae-fp16-fix` para evitar NaN en fp16; o `enable_vae_tiling()` a alta resolución |

## Aceleración: turbo / lightning / LCM
| Método | Pasos | CFG | Calidad | Uso |
|---|---|---|---|---|
| SDXL **base** | 25-40 | 5-8 | máxima | calidad final |
| **LCM** (LoRA) | 4-8 | 1-2 | buena | aplicable como LoRA a cualquier checkpoint SDXL |
| **Lightning** (ByteDance) | 2/4/8 | 1 | muy buena (4-8 pasos) | mejor que LCM en fidelidad; viene como UNet o LoRA |
| **SDXL-Turbo** | 1-4 | 1 (sin CFG) | buena a baja res | tiempo-real, 512px nativo |
- Lightning 4-step + `EulerDiscreteScheduler`(trailing) o `DPM++ SDE` es el punto dulce producción.
- Turbo/Lightning quitan CFG → **mitad de cómputo por paso** (no doble forward). Cruza con [[124-ltx-video-realtime-rapido]] para el equivalente en video.

## Optimización de inferencia
- **fp16** siempre (bf16 si NaN). `torch.compile(unet, mode="max-autotune")` → ~1.3-2x tras warmup; cuidado con recompilación al variar resolución/batch (fija shapes o usa `dynamic=True`). Cruza con [[127-torch-compile-tensorrt-difusion]].
- **TensorRT** (SDXL) → mayor speedup aún (2-3x) pero engine por-shape, build lento; vale para servicio de alto volumen con resolución fija.
- `scheduler` rápido: `DPMSolverMultistep` / `EulerAncestral`. Evitar offload si cabe en VRAM (mata latencia).
- Batching: SDXL escala bien en batch en A100/H100 → sube imágenes/seg.
- `channels_last` + `enable_xformers`/SDPA por defecto.

## ControlNet / IP-Adapter
- SDXL tiene los ControlNets más maduros (canny, depth, openpose, tile). IP-Adapter para consistencia de cara/estilo. Es la razón #1 para quedarse en SDXL en pipelines de marca/producto. Cruza con [[139-controlnet-ipadapter-serving-consistencia]].

## SD3.5 (Stability) — el intermedio
| Variante | Params | Pasos | VRAM (sin encoders) | Nota |
|---|---|---|---|---|
| **Large** | 8B | 28-40 | ~18-24 GB | MMDiT, 1MP, buena adherencia a prompt |
| **Large Turbo** | 8B (distill) | **4** | ~18-24 GB | rápido, calidad alta |
| **Medium** | 2.5B | 28-40 | **~9.9 GB** | MMDiT-X, corre en consumer 12GB |
- Encoders: CLIP-L + CLIP-G + **T5-XXL** (pesado; cuantizar a fp8/int8 reduce mucho la huella, como en FLUX).
- **Licencia Stability Community**: libre comercial si <$1M/año de ingresos; por encima, licencia Enterprise. [verificado stability.ai]
- SD3.5 mejora texto-en-imagen y adherencia vs SDXL, pero su ecosistema de LoRA/ControlNet es **menor** que SDXL.

## Árbol de decisión 2026
- Vendes outputs + necesitas ControlNet/LoRA maduros + bajo costo → **SDXL (+Lightning)**.
- Tiempo real / muchas imágenes baratas → **SDXL-Turbo o Lightning 2-4 pasos**.
- Mejor adherencia/texto sin la NC de FLUX y cabes en 24GB → **SD3.5 Large/Turbo**.
- Consumer 12GB con calidad decente → **SD3.5 Medium**.
- Realismo máximo y outputs no-comerciales (o con licencia BFL) → **FLUX dev** ([[149-flux-serving-a-fondo]]).

Cruza con [[02-open-models-catalog-2026]] y [[113-network-volume-modelos-grandes]].
