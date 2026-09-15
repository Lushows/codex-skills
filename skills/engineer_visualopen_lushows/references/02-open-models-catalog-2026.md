# 02 — Catálogo de modelos visuales open (junio 2026)

> Specs, VRAM (fp16 → cuantizado), licencia y entry point. **VRAM = inferencia single-GPU** salvo nota.
> "Gated" = pide acceso HF y/o términos non-commercial. Re-verifica VRAM/licencia en la HF card antes de
> comprometer hardware o vender. `[V]`=confirmado primario · `[~]`=secundario · `[?]`=una fuente.

## Avatares parlantes (foto + audio → video, con gestos)

| Modelo | Params/base | VRAM (fp16→quant) | Licencia | Fuerza | Entry point |
|---|---|---|---|---|---|
| **LongCat-Video-Avatar 1.5** (Meituan) | 13.6B | INT8 DiT `--use_int8`; 480/720P, 8-step | **MIT** `[V]` | lip-sync multilingüe Whisper-v3; AT2V/ATI2V + continuación; comercial-OK | `meituan-longcat/LongCat-Video-Avatar-1.5` |
| **HunyuanVideo-Avatar** (Tencent) | MM-DiT | **min 24GB**, rec **96GB**; **10GB** vía Wan2GP+TeaCache `[V]` | Tencent Community (chequear) | multi-char, emoción (AEM) | `hymm_sp/sample_gpu_poor.py` |
| **EchoMimic V3** (AntGroup) | **1.3B** | **24GB** → **12GB** Flash-Pro quant `[V]` | **Apache 2.0** | tiny, multi-task, 8-step, sin face mask | `run_flash.sh` |
| **InfiniteTalk/MultiTalk** (MeiGen) | **14B** DiT (Wan2.1) | ~24-48GB+ | **Apache 2.0** `[V]` | long-form (~10min) rolling 81-frame; multi-persona | `MeiGen-AI/InfiniteTalk` |
| **Wan2.2-S2V-14B** (Alibaba) | **14B** MoE | **≥80GB** bf16 → **fp8 scaled** mucho menos `[V]` | Apache 2.0 `[~]` | canto/diálogo cinematográfico, ComfyUI nativo | `Wan-AI/Wan2.2-S2V-14B` |
| **OmniHuman / 1.5** (ByteDance) | — | — | **Cerrado, sin pesos** `[~]` | SOTA pero **NO self-hosteable** (solo API) | n/a |
| Hallo3 · Sonic | CogVideoX / portrait | ~24-40GB `[?]` | chequear | portrait talking | repo |

## Texto/imagen → video

| Modelo | Params | VRAM | Licencia | Notas |
|---|---|---|---|---|
| **Wan 2.2 I2V A14B** | 14B activos (MoE) | 480p fp8 **40-48GB**; 720p **65-80GB** `[~]` | Apache 2.0 | máxima calidad, lento; **Wan 2.5 = API only, sin pesos** |
| **HunyuanVideo** | 13B | orig 60-80GB; **v1.5 ~14GB** con offload `[~]` | Hunyuan Community | v1.5 lo hizo prosumer |
| **LTX-Video** (Lightricks) | DiT | **16GB** fp8@720p → 24GB full `[~]` | open | **el más rápido** (>realtime 30fps) |
| **CogVideoX** (2B/5B) | 2/5B | **≥16GB** `[~]` | **Apache 2.0** | soporte diffusers de 1ª clase |
| **Mochi-1** (Genmo) | **10B** AsymmDiT | 60-80GB → offload/quant `[~]` | **Apache 2.0** | el más grande totalmente open |
| **Open-Sora** | ~1.1B+ | 24GB `[?]` | Apache 2.0 | receta + pesos abiertos |

## Generación de imagen

| Modelo | Params | VRAM | Licencia | Notas |
|---|---|---|---|---|
| **FLUX.1 [dev]** | 12B DiT | ~24-33GB fp16 → **~12GB** fp8, **~8-10GB** GGUF Q4 `[~]` | **NON-commercial** | referencia de calidad, 28 pasos |
| **FLUX.1 [schnell]** | 12B | igual → quant | **Apache 2.0** | 4-step, comercial-OK |
| **FLUX.2 [dev]** | **32B** flow-match (+ text enc ~24B Mistral) | **>80GB** full → fp8 **~32GB**, GGUF Q4 **~19GB**; klein-4B **~13GB** `[V]` | **NON-commercial** | mejor calidad+edición, pesado |
| **SD 3.5 Large** | **8B** | UNet ~10GB; **16-18GB** con 3 text encoders (CLIP-L/G+T5-XXL) `[~]` | Stability Community (<$1M) | |
| **SDXL** | 3.5B | ~10-12GB `[~]` | OpenRAIL++ | ecosistema/LoRAs maduro |
| **Qwen-Image** | **20.4B** MMDiT + Qwen2.5-VL 8.3B | alto; quant existe `[~]` | **Apache 2.0** | SOTA render de texto (ZH/EN), fotorrealismo |
| **Sana** (NVLabs) | 0.6B/1.6B | **9GB**/**12GB** `[V]` | **Apache 2.0** | 4K, linear-attn, ~20× < FLUX; Sana-Sprint 1-step |
| **Chroma** | **8.9B** | **~22GB** fp16 → quant `[~]` | **Apache 2.0** | de-distilled FLUX-schnell, totalmente open |

## Lip-sync sobre video existente

| Modelo | VRAM | Licencia | Notas |
|---|---|---|---|
| **MuseTalk 1.5** (Tencent) | **infer ~4GB** (8s clip); train 74-85GB `[V]` | **MIT** | real-time 30fps+ en V100; 256×256 cara; whisper-tiny; inpaint latente |
| **LatentSync 1.5/1.6** (ByteDance) | **8GB(1.5)** / **18GB(1.6)** `[V]` | **Apache 2.0** | 1.6=512×512 (menos blur); Whisper mel→cross-attn |
| **Wav2Lip** (2020) | muy bajo, CPU-feasible `[~]` | **pesos non-commercial** | viejo, menor fidelidad (96×96), pero a prueba de balas + tiny |

## Fit por tarjeta
- **24GB (RTX 4090):** MuseTalk, LatentSync, EchoMimic V3, Sana, SDXL, SD3.5, FLUX fp8/GGUF, FLUX.2 GGUF-Q4/klein, LTX, CogVideoX, Chroma, **LongCat-Avatar INT8**.
- **48GB (L40S/A6000):** Wan 2.2 480p, HunyuanVideo v1.5, InfiniteTalk, FLUX.2 fp8 (justo), HunyuanVideo-Avatar res baja.
- **80GB (A100/H100):** Wan 2.2 720p, Wan2.2-S2V bf16, Mochi-1, HunyuanVideo full, FLUX.2 full, HunyuanVideo-Avatar alta calidad.

## Gotchas
1. **Minas de licencia:** FLUX.1-dev y **FLUX.2-dev son NON-commercial**; solo schnell es Apache. **OmniHuman NO tiene pesos open.** HunyuanVideo/-Avatar = Tencent Community (restricción regional+escala). **Comercial-safe (Apache/MIT):** schnell, Sana, Chroma, CogVideoX, Mochi-1, Qwen-Image, EchoMimic, InfiniteTalk, MuseTalk, LatentSync, **LongCat-Avatar (MIT)**.
2. **Los números VRAM de titular son fp8/GGUF + offload**, no fp16. "FLUX.2 en 8GB" = Q4 + offload a RAM, lento; fp16 = 80GB+.
3. **"Wan 2.5" y hermanos cerrados son API-only** — no planees self-host sobre ellos; usa Wan 2.2 / 2.2-S2V.
4. **Los text encoders son VRAM oculta:** T5-XXL (SD3.5) y Qwen2.5-VL 8.3B (Qwen-Image) dominan el footprint → presupuéstalos aparte u offload.
5. **Los repos de avatar bajan sub-modelos** (Whisper/wav2vec2 + separador + face detector). La VRAM citada del DiT los EXCLUYE → el pico real es mayor, y un peso faltante (ej. whisper-tiny en MuseTalk) es un silent-fail típico al primer run.
