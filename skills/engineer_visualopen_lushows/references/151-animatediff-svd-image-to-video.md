# 151 · AnimateDiff y Stable Video Diffusion (animar una imagen, low-VRAM)

> Antes de los DiT pesados (Wan/Hunyuan), animar imágenes era AnimateDiff (sobre SDXL/SD1.5) y SVD.
> En 2026 son los reyes del **low-VRAM** (8-16GB) y de la integración con el ecosistema SDXL/LoRA/ControlNet.

## AnimateDiff (motion module sobre un checkpoint de imagen)
Inyecta un **motion module** (capas temporales) en un UNet SD1.5/SDXL existente → el modelo de imagen genera
secuencias coherentes. NO es un modelo de video aparte: reusa tu checkpoint + LoRA + ControlNet de imagen.
- **VRAM**: ~8-10 GB (SD1.5) / ~12-16 GB (SDXL). El piso de VRAM más bajo de todo i2v/t2v.
- **Motion modules**: `mm_sd_v15_v2` (SD1.5), `AnimateDiff-SDXL` (beta). Versionado importa (mismatch de arquitectura rompe).
- **Motion LoRA**: LoRAs de cámara (`zoom-in`, `pan-left`, `tilt`, `rolling`) que dirigen el movimiento. Apilables.
- **Frames/contexto**: ventana típica 16 frames; clips largos vía **context scheduling** (ventanas solapadas, ej. ComfyUI `Context Options`) → encadena sin OOM.
- **Fortaleza**: estilizado/anime/abstracto + control total (ControlNet pose/depth por frame, IP-Adapter). Cruza con [[139-controlnet-ipadapter-serving-consistencia]].
- **Debilidad**: realismo y coherencia física pobres vs DiT modernos; flicker sin AnimateLCM/FreeNoise.
- **AnimateLCM**: LoRA que baja a **2-8 pasos** → casi tiempo real. El combo de producción.

## Stable Video Diffusion (SVD / SVD-XT) — i2v puro
Modelo de difusión de video de Stability: entra **una imagen**, sale movimiento natural. Sin prompt de texto
(condiciona solo en la imagen). Bueno para movimiento realista corto (paneos, parallax, ambient).
| Checkpoint | Frames | Resolución | VRAM (fp16) |
|---|---|---|---|
| `svd` (img2vid) | 14 | 576×1024 | ~10-11 GB |
| `svd-xt` (img2vid-xt) | **25** | 576×1024 | ~11 GB (< 10GB con chunk bajo) |
Con `enable_model_cpu_offload()` cabe en **12GB**. [verificado HF/diffusers]

### Parámetros clave (diffusers `StableVideoDiffusionPipeline`)
| Param | Default | Efecto |
|---|---|---|
| `motion_bucket_id` | 127 | 0-255; ↑ = más movimiento (180+ = mucho, riesgo de artefactos) |
| `fps` / `fps_id` | 6-7 | velocidad de movimiento condicionada (entrenado 1-30) |
| `noise_aug_strength` (cond_aug) | 0.02 | ↑ = más libertad/movimiento, menos fidelidad a la imagen |
| `decode_chunk_size` | 14 | frames decodificados a la vez; **bájalo (4-8) si OOM** en el VAE temporal |
| `num_frames` | 14/25 | según checkpoint |
```python
frames = pipe(image, decode_chunk_size=8, motion_bucket_id=180,
              noise_aug_strength=0.1).frames[0]
export_to_video(frames, "out.mp4", fps=7)
```
- El VAE temporal es el que dispara VRAM en el decode → `decode_chunk_size` es la palanca anti-OOM. Cruza con [[113-network-volume-modelos-grandes]].
- Clips ~2-4s (25 frames a 6-7fps). Para más largo: interpolar (RIFE/FILM) o encadenar (degrada).

## Cuándo AnimateDiff/SVD vs Wan/LTX
| Necesitas | Usa |
|---|---|
| VRAM 8-12GB, animar imagen rápido y barato | **AnimateDiff (+AnimateLCM)** o **SVD-XT** |
| Control fino por frame (pose/depth), estilo SDXL/LoRA | **AnimateDiff** |
| i2v realista corto sin prompt, simple | **SVD-XT** |
| Calidad/coherencia SOTA, prompt de texto, clips largos | **Wan 2.x** ([[122-wan-video-self-hosting-2026]]) |
| Tiempo real / latencia mínima en video | **LTX-Video** ([[124-ltx-video-realtime-rapido]]) |

**Veredicto 2026**: AnimateDiff y SVD ya NO son SOTA en calidad (Wan/Hunyuan/LTX los superan), pero siguen
imbatibles cuando mandan el **VRAM bajo**, el **control SDXL** o el **costo**. Para producto premium → Wan/LTX.

Cruza con [[48-animacion-con-ia]] y [[02-open-models-catalog-2026]].
