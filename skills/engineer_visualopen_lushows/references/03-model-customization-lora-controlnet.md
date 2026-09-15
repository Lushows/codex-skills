# 03 — Personalizar y condicionar modelos de diffusion + prompt engineering

> LoRA, entrenar LoRA, ControlNet, IP-Adapter, otras condiciones, y prompting. `diffusers` ~v0.31+.
> Verificado 2026. Modelos: SD1.5/SDXL = mejor ecosistema ControlNet/IP-Adapter; FLUX.1 = calidad open
> madura; FLUX.2 (32B), Qwen-Image (20B Apache, mejor texto), Z-Image Turbo (8-step, 16GB) = nuevos.

## 1. LoRA (Low-Rank Adaptation)

**Qué es.** En vez de actualizar `W ∈ ℝ^(d×k)`, congela W y aprende un delta de bajo rango `ΔW = B·A`
(`A ∈ ℝ^(r×k)`, `B ∈ ℝ^(d×r)`, rank `r ≪ min(d,k)`). En inferencia `W' = W + (α/r)·B·A`. Se aplica a
proyecciones de atención (`to_q/k/v/out`) y a veces FFN. Solo guardas A y B → **MBs vs GBs.** **El scale
efectivo es `α/r`, NO `r`.**

```python
pipe.load_lora_weights("repo/ikea-sdxl", adapter_name="ikea")
pipe.load_lora_weights("path/feng.safetensors", adapter_name="feng")
pipe.set_adapters(["ikea","feng"], adapter_weights=[0.7, 0.8])   # STACK + peso por LoRA
img = pipe(prompt, cross_attention_kwargs={"scale": 1.0}).images[0]
```
- **`set_adapters(names, weights)`** — la forma canónica de **apilar varias LoRAs** con peso independiente.
- **`cross_attention_kwargs={"scale": s}`** — scale global en runtime sin fusionar. (En FLUX: `joint_attention_kwargs`.)
- **`fuse_lora(adapter_names, lora_scale)`** — hornea ΔW en W (inferencia más rápida) → luego `unload_lora_weights()`.
- **`unfuse_lora()` SOLO revierte si fusionaste UNA.** Fusionar varias = viaje sin retorno (recarga el base). **Gotcha #1.**
- **Hot-swap:** mantén adapters cargados y llama `set_adapters(["x"])`/`["y"]` por request, sin recarga.
- **NO pongas el scale en dos lados** (`fuse_lora(lora_scale=)` + `cross_attention_kwargs["scale"]`) → se compounden.
- **LoRA en video también:** Wan 2.1/2.2, LTX, Hunyuan vía los mismos loaders ("motion LoRAs", subject LoRAs).

## 2. Entrenar tu propia LoRA

- **Dataset:** sujeto/personaje **10-30 imágenes** (ángulo/luz/fondo variados, sujeto consistente); estilo 20-100+.
  Captions `.txt` por imagen o trigger token raro (`sks`,`ohwx`). Crop a la resolución bucket (512/768/1024).
- **Tools:** diffusers `train_dreambooth_lora_*.py` (sdxl/flux/flux2) · **kohya_ss/sd-scripts** (SD/SDXL maduro)
  · **ai-toolkit (Ostris)** y **SimpleTuner** (FLUX/Qwen, con UI).
- **Hiperparámetros (puntos de partida):**

  | | rank | alpha | LR | steps |
  |---|---|---|---|---|
  | SDXL sujeto | 16-32 | rank o rank/2 | 1e-4 | 1000-2000 |
  | FLUX.1 sujeto | 16 (32-64 estilo) | rank/2 | 1e-4 | 1500-3000 |
  | FLUX.2 | similar | rank/2 | **8e-4-1.5e-3** | — |
  - **`alpha ≈ rank/2`** (regularización; la convención vieja era alpha=rank). **AdamW8bit** (ahorra 2-3GB).
    Overfit (sujeto "quemado", ignora prompt) → menos steps / menor LR / menor rank.
- **VRAM/tiempo/costo:** SDXL ~10-12GB (bf16 + 8-bit optim). **FLUX.1 ~24GB práctico.** Una LoRA FLUX ≈ 30-90 min
  en A100/4090 → **~$1-5 por LoRA** en GPU rentada.
- **FLUX vs SDXL:** FLUX es DiT rectified-flow (no UNet) → targetea los double/single blocks, congela el text
  encoder grande; mayor calidad base, más cómputo.
- **Cuándo qué:** **Textual Inversion** (solo un embedding nuevo, KBs, débil en estructura) · **DreamBooth**
  (método de binding sujeto, full o LoRA) · **LoRA** (mejor default: chico, componible, barato) · **Full
  fine-tune** (cambio amplio de comportamiento; mucha VRAM, no componible).

## 3. ControlNet (condición estructural)

Copia entrenable que ingiere una **imagen de condición** (canny/depth/pose/scribble/seg/normal/lineart/**tile**)
e inyecta residuales en el base congelado → fija la estructura espacial mientras el texto controla contenido.

```python
from diffusers import ControlNetModel, StableDiffusionControlNetPipeline
cn = ControlNetModel.from_pretrained("lllyasviel/sd-controlnet-canny", torch_dtype=torch.float16)
pipe = StableDiffusionControlNetPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", controlnet=cn, torch_dtype=torch.float16)
img = pipe(prompt, image=canny_image, controlnet_conditioning_scale=0.8).images[0]
```
- **`controlnet_conditioning_scale`** (default 1.0; baja a ~0.5-0.8 para "respirar"). **Multi-ControlNet:**
  `controlnet=[cn1,cn2]`, `image=[i1,i2]`, `scale=[1.0,0.5]`; `control_guidance_start/end` para aplicar solo
  parte del schedule.
- **SDXL:** `StableDiffusionXLControlNetPipeline` + un **Union/Promax** ControlNet (muchos modos en 1).
- **FLUX (mecanismo distinto):** (1) `FluxControlNetModel`+`FluxControlNetPipeline` (Union cubre canny/tile/
  depth/blur/pose, con `control_mode`). (2) **Flux Tools:** FLUX.1-Canny/Depth-dev son **modelos 12B completos**
  (la condición se concatena a los canales de input) vía `FluxControlPipeline`. Qwen-Image trae una structure-control LoRA.

## 4. IP-Adapter (condición por imagen de referencia)

Condiciona en una **imagen-prompt** (estilo/sujeto/cara) vía cross-attention desacoplada que inyecta
embeddings del image-encoder junto al texto. Liviano, componible con ControlNet y LoRA.

```python
pipe.load_ip_adapter("h94/IP-Adapter", subfolder="models", weight_name="ip-adapter_sd15.bin")
pipe.set_ip_adapter_scale(0.6)            # 0.5-0.7 balancea ref vs texto; 1.0 domina la ref
img = pipe(prompt, ip_adapter_image=ref_img).images[0]
```
- **Variantes:** **Plus** (ViT-H, ref más fina) · **FaceID/Plus(-v2)** usan embeddings **InsightFace** (no CLIP)
  → pasas `ip_adapter_image_embeds=[tensor]`. **InstantID** (SDXL): IP-Adapter de cara + ControlNet de keypoints
  → identidad + pose fuerte de UNA foto, zero-shot.
- **vs reference-only:** reference-only = truco sin pesos extra (community); IP-Adapter = adapter entrenado, más fuerte.

## 5. Otras condiciones
- **img2img** — `strength` (0-1): bajo (0.2-0.4) conserva la fuente, alto (0.7-0.9) reinventa.
- **Inpainting** (`*InpaintPipeline`, `mask_image` blanco=editar) · **Outpainting** = inpaint en canvas extendido.
  FLUX.1-Fill-dev = modelo dedicado.
- **Regional prompting** (prompts distintos por región) · **T2I-Adapter** (alt. más ligera a ControlNet).
- **Video:** **first/last-frame (FLF2V)** (Wan 2.2 interpola entre 2 imágenes) · **I2V** (anima un still) ·
  **video-to-video / motion transfer** (IC-LoRA en LTX 2.3 / Wan) · **Motion LoRA** (inyecta un movimiento de cámara).

## 6. Prompt engineering (imagen + video)
- **Estructura (front-loaded, comas):** sujeto → descriptores → estilo/medio → composición → luz → cámara/lente → calidad/mood.
  Ej: `a weathered fisherman, knitted sweater, oil painting, rule-of-thirds, golden-hour rim light, 85mm, shallow DoF, highly detailed`.
  - **Cámara/lente:** `35/85mm, macro, wide/close-up, low angle, Dutch angle, bokeh, f/1.8`. **Luz:** `golden hour, rim, softbox, volumetric, chiaroscuro, backlit`. **Video:** `slow dolly-in, pan left, tracking, handheld, orbit, time-lapse`.
- **Weighting:** **`(word:1.3)`** sube, `(word:0.7)` baja (sintaxis CLIP/A1111; usa **`compel`** para construir embeddings
  pesados en diffusers y pasar el límite de 77 tokens). **NO aplica a T5/Mistral/Qwen** (FLUX/SD3/FLUX.2/Qwen-Image) → prosa natural.
- **Negative prompts & CFG:** solo existen con **classifier-free guidance** (`guidance_scale>1`, 2 passes):
  - **CFG (SD1.5/SDXL):** `negative_prompt` normal, `guidance_scale` 5-8.
  - **Guidance-distilled (FLUX.1-dev):** scalar de guidance horneado (1 pass) → **negatives NO aplican**; para
    negative real usa **`true_cfg_scale>1` + `negative_prompt`** (re-activa 2-pass, más lento).
  - **Turbo/few-step (schnell, SDXL-Turbo/Lightning, Z-Image Turbo):** CFG 0-1 → **sin negative**; 1-8 pasos.
    NO pegues boilerplate de negatives ahí (se ignora).
- **Aspect ratio:** matchea el bucket nativo (SD1.5→512, SDXL/FLUX→1024, Qwen-2.0→2K) o duplicación/artefactos.
- **Seed:** `generator = torch.Generator(device).manual_seed(n)` → reproducible; fija seed para iterar UNA variable.

## Gotchas
1. **`unfuse_lora()` tras fusionar varias LoRAs no hace nada útil** — recarga el base. Para stacks dinámicos usa `set_adapters()`.
2. **Negatives en FLUX-dev/Turbo se ignoran silenciosamente** (guidance-distilled / CFG-free). FLUX-dev: opta a `true_cfg_scale>1`.
3. **`(word:1.3)` no-opea en encoders T5/LLM** (FLUX/SD3/FLUX.2/Qwen). Es CLIP-específico (y necesita `compel` aun en SDXL).
4. **Confusión alpha/rank:** la fuerza efectiva es `α/r`. Subir rank sin ajustar alpha cambia el scale → "mi LoRA quedó muy fuerte/débil".
5. **Scale de LoRA en dos lados** (`fuse_lora(lora_scale=)` + runtime scale) → se compounden. Igual: `controlnet_conditioning_scale=1.0` rígido → bájalo a ~0.5-0.8.

**Fuentes:** diffusers docs (merge_loras, using_peft_for_inference, controlnet, ip_adapter, weighted_prompts) ·
github.com/damian0815/compel · ai-toolkit (Ostris) · FLUX/Qwen model cards.
