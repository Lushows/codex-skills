# 122 · Wan 2.x self-hosting (T2V/I2V/VACE/FLF2V — la familia open de video más versátil)

> Wan es el caballo de batalla open para video: T2V, I2V, control (VACE), first-last frame (FLF2V),
> speech-to-video. Variantes de 5B (cabe en 24GB) a 27B-MoE. Aquí qué bajar, cuánta VRAM y cómo correrlo.

## La familia Wan 2.2 (lo último, 2026)
| Modelo | Params | Tarea | Resolución | VRAM real |
|---|---|---|---|---|
| **TI2V-5B** | 5B denso | texto+imagen→video | 720P (1280×704) @24fps | **24GB** (RTX 4090) con offload |
| **T2V-A14B** | 27B MoE, 14B activos | texto→video | 480P/720P | 80GB fp16; **~6-24GB** vía GGUF/fp8 |
| **I2V-A14B** | 27B MoE, 14B activos | imagen→video | 480P/720P | igual que T2V |
| **S2V-14B** | 14B | voz→video (audio-driven) | 480P/720P | ~24GB+ con offload |
| **Animate-14B** | 14B | character replace + pose/face track | 480P/720P | ~24GB+ |

El MoE A14B usa **dos expertos** (high-noise y low-noise) que se activan según el paso de ruido — por
eso son 27B en disco pero 14B activos por step. La **5B es la opción sana** para una sola GPU consumer.
**VACE** y **FLF2V** vienen del linaje Wan 2.1 (VACE-1.3B / VACE-14B) y siguen siendo el camino de control.

## Instalación (repo oficial — recomendado para VACE/S2V)
```bash
git clone https://github.com/Wan-Video/Wan2.2.git && cd Wan2.2
pip install -r requirements.txt
huggingface-cli download Wan-AI/Wan2.2-TI2V-5B --local-dir ./Wan2.2-TI2V-5B
```
Diffusers también integra T2V-A14B / I2V-A14B / TI2V-5B (`WanPipeline`) si prefieres el ecosistema HF
para LoRA y cuantización. Para VACE/control fino, el **repo oficial** expone más palancas.

## Inferencia — comandos reales
TI2V-5B (cabe en 4090, T5 a CPU para no reventar VRAM):
```bash
python generate.py --task ti2v-5B --size 1280*704 --ckpt_dir ./Wan2.2-TI2V-5B \
  --offload_model True --convert_model_dtype --t5_cpu --prompt "..."
```
T2V-A14B una GPU (80GB) — sin volumen multi-GPU:
```bash
python generate.py --task t2v-A14B --size 1280*720 --ckpt_dir ./Wan2.2-T2V-A14B \
  --offload_model True --convert_model_dtype --prompt "..."
```
Multi-GPU (8×) con FSDP + Ulysses (sequence parallel) para el 14B a velocidad:
```bash
torchrun --nproc_per_node=8 generate.py --task t2v-A14B --size 1280*720 \
  --ckpt_dir ./Wan2.2-T2V-A14B --dit_fsdp --t5_fsdp --ulysses_size 8 --prompt "..."
```
I2V: añade `--image examples/i2v_input.JPG`. S2V: `--audio talk.wav --image ref.JPG`.

## Argumentos que importan
- `--offload_model True` → mueve bloques DiT a CPU entre steps (mata OOM, ralentiza algo).
- `--convert_model_dtype` → castea pesos al dtype de cómputo (evita doble copia en VRAM).
- `--t5_cpu` → encoder T5-XXL (9.4GB fp16) a CPU; exige **≥24GB RAM de sistema**. Clave en la 5B.
- `--size` es `H*W`. La 5B solo 720P (1280×704 / 704×1280). El A14B flexea 480P↔720P.
- `--frame_num` (def. 81 ≈ 5s @16fps en 2.1; la 5B sale a 24fps). Más frames = más VRAM y tiempo lineal.
- `--prompt_extend` → expande el prompt con un LLM (mejora adherencia, cuesta latencia).

## VACE — control (pose / depth / referencia / inpaint)
VACE es el **modelo unificado de control** de Wan: una sola red acepta `--src_video` (control: pose,
depth, scribble, gris), `--src_mask` (inpaint/outpaint espacio-temporal) y `--src_ref_images`
(referencia de sujeto/estilo). Sirve para R2V (ref→video), V2V (edición) y extensión. VACE-1.3B corre en
**~8-12GB**; VACE-14B pide gama alta. Es la pieza para animación con guía esquelética o transferencia de
identidad — encadénalo con tu pipeline de pose/depth antes de entrar al DiT.

## Schedulers, LoRA y velocidad
- **Schedulers**: UniPC y DPM++ son los típicos; con la **distill/distilled-fp8** y caché de pasos
  (TeaCache / Cache-dit) bajas steps drásticamente. fp8 GEMM via torchao recorta VRAM ~40% con leve pérdida.
- **LoRA**: hay ecosistema fuerte de LoRA para Wan 2.1/2.2 (estilo, movimiento, identidad) entrenables con
  DiffSynth-Studio o diffusers. **Gotcha**: con **Wan-Animate** los autores desaconsejan LoRA entrenadas
  sobre 2.2 (los deltas de peso del finetune chocan con el modo replace → artefactos).
- **Velocidad aprox** (720P, 5s): 4090 con la 5B ≈ minutos por clip; A14B fp16 en H100 es razonable, en
  80GB single-GPU con offload va lento. Para producción del 14B → multi-GPU Ulysses o fp8 [no verificado: cifras exactas dependen de steps/caché].

## Cuándo Wan
Es el **default** cuando quieres control (VACE), I2V de calidad o audio-driven, y aceptas 24GB+. Si solo
necesitas velocidad casi-realtime con GPU modesta, mira LTX. Si necesitas video largo con VRAM mínima,
mira FramePack. Para clips largos a partir de Wan, segmenta y solapa contexto.

Cruza con [[02-open-models-catalog-2026]], [[114-video-segmentado-largo-clip]] y [[12-cuantizacion-hands-on]].
