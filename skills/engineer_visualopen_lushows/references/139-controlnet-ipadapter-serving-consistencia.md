# 139 · Servir ControlNet + IP-Adapter para consistencia (personaje/marca)

> Para que un endpoint produzca el **mismo personaje** o respete una **composición**, no basta el prompt:
> ControlNet fija la *estructura* (pose/depth/canny/tile) e IP-Adapter/InstantID fijan la *identidad/estilo*.

## Qué fija cada cosa

| Herramienta | Fija | Entrada | Uso típico |
|---|---|---|---|
| **ControlNet (pose)** | pose/esqueleto | OpenPose/DWPose | personaje en pose dada |
| **ControlNet (depth)** | volumen/3D | mapa de profundidad | composición, encuadre |
| **ControlNet (canny/lineart)** | contornos | bordes | fidelidad estructural fuerte |
| **ControlNet (tile)** | textura local | imagen base | upscale guiado, detalle coherente |
| **IP-Adapter** | estilo/contenido de una imagen ref | imagen | "como esta imagen", look de marca |
| **IP-Adapter FaceID / InstantID** | **identidad facial** | foto de cara | **mismo rostro** entre escenas |

Consistencia de **personaje** = InstantID/IP-Adapter-FaceID (cara) + ControlNet pose (cuerpo). Consistencia de **marca** = IP-Adapter sobre referencias + LoRA de estilo. Cruza con [[49-consistencia-personaje-marca-ia]] y entrenamiento en [[03-model-customization-lora-controlnet]].

## Estado 2026 por base

| Base | ControlNet | IP-Adapter | Identidad facial |
|---|---|---|---|
| **SDXL** | maduro (todos los tipos) | maduro, FaceID estable | **InstantID** (sólido, producción) |
| **Flux.1-dev** | **ControlNet Union** (InstantX: canny/depth/tile/blur/pose/gray/lowquality en un modelo) | IP-Adapter InstantX (Flux) | en evolución; InstantID-Flux **[no verificado: madurez producción]** |

Para identidad facial **fiable y barata hoy**: SDXL + InstantID. Flux para calidad/prompt-adherence cuando la cara exacta importa menos o vía LoRA. Licencias de SDXL/Flux y adapters: revisar en [[02-open-models-catalog-2026]] (Flux.1-dev es **non-commercial** sin licencia).

## ComfyUI vs diffusers (cómo servir)

| | **ComfyUI** ([[06-comfyui-backend-produccion]]) | **diffusers** |
|---|---|---|
| Multi-controlnet | nodos en cadena, trivial visualmente | listas `controlnet=[...]`, `controlnet_conditioning_scale=[...]` |
| IP-Adapter | nodos IPAdapter/InstantID listos | `load_ip_adapter()`, `set_ip_adapter_scale()` |
| Iteración | rápida (grafo) | control fino en código, mejor para API determinista |
| Producción | warm worker + API `/prompt` | pipeline propio, menos sorpresas de versión |
| Recomendación | prototipar y workflows complejos | endpoint estable de un solo flujo |

diffusers, varios ControlNets + IP-Adapter:
```python
from diffusers import StableDiffusionXLControlNetPipeline, ControlNetModel
cn = [ControlNetModel.from_pretrained("...openpose", torch_dtype=torch.float16),
      ControlNetModel.from_pretrained("...depth",    torch_dtype=torch.float16)]
pipe = StableDiffusionXLControlNetPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", controlnet=cn, torch_dtype=torch.float16).to("cuda")
pipe.load_ip_adapter("h94/IP-Adapter", subfolder="sdxl_models",
                     weight_name="ip-adapter-plus_sdxl_vit-h.safetensors")
pipe.set_ip_adapter_scale(0.6)
img = pipe(prompt, image=[pose_map, depth_map],
           controlnet_conditioning_scale=[0.8, 0.5],
           ip_adapter_image=ref_face).images[0]
```

## Peso / escala (lo que muerde)
- **ControlNet `conditioning_scale`**: 0 = ignora, ~0.8 firme, 1.0+ = rígido y feo. Pose suele 0.7-0.9; tile 0.4-0.6.
- **IP-Adapter scale**: 0.4-0.7 para guiar sin clonar; >1.0 "quema" la identidad y mata variación. FaceID/InstantID admite más alto (0.8-1.2) para fijar rostro.
- **Empezar y soltar** (start/end percent): aplica el control solo en los primeros pasos (estructura) y libera el final (detalle) → menos artefactos.
- **Combinar muchos** controles = se pelean. Más de 2-3 ControlNets a la vez = resultados tiesos; baja escalas.
- **InstantID** ya incluye su propio ControlNet de keypoints faciales → cuenta como un control más en VRAM.

## VRAM extra (sizing)
- Cada ControlNet añade un encoder paralelo: **~+1-2.5GB** por modelo cargado (Union evita cargar varios → un solo modelo para todos los tipos = gran ahorro en Flux).
- IP-Adapter: image encoder (CLIP/ViT-H) ~+1-2GB; InstantID añade su ControlNet + ArcFace.
- SDXL base ~7-10GB + 2 ControlNets + IP-Adapter ≈ **14-18GB** → A10/L4 (24GB) holgado, 16GB ajustado (usa fp16, sequential offload si OOM).
- Flux es pesado de base (~16GB+) → Union ayuda; aun así apunta a 24GB+.
- **Carga una vez, mantén caliente**: recargar ControlNet/IP-Adapter por request destruye throughput. Warm-state en [[06-comfyui-backend-produccion]].

## Patrón de endpoint (un solo flujo de consistencia)
1. Inputs: prompt + ref de identidad (foto) + control (pose/depth) + escalas.
2. Modelos **pre-cargados** en el worker (ControlNet Union si Flux; InstantID si SDXL).
3. Validar que la imagen de control coincide en resolución con la generación.
4. Devolver con seed fijo para reproducibilidad de marca.
5. Evaluar identidad con similitud facial (ArcFace) / CLIP de estilo → ver [[17-evals-modelos-generativos]].

Cruza con [[03-model-customization-lora-controlnet]], [[49-consistencia-personaje-marca-ia]] y [[06-comfyui-backend-produccion]].
