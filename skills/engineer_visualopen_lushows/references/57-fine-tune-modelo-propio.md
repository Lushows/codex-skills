# 57 — Fine-tune de tu propio modelo (avatar / estilo / video / LLM)

**Orden de decisión antes de entrenar: prompt → RAG → fine-tune.** El fine-tuning enseña *forma, identidad y
estilo*; NO inyecta *hechos* confiables (eso es RAG) ni arregla un base model malo.

## Métodos (recap)
**Full fine-tune** (todos los pesos, máxima VRAM, solo presupuestos grandes/domain shift) · **LoRA** (adapters
low-rank, ~0.1-2% de params, el default) · **QLoRA** (base 4-bit + LoRA → un 70B en 24GB vía Unsloth FP8) ·
**DreamBooth** (subject-driven imagen, usualmente + LoRA).

## Avatar/personaje propio (una persona)
**Identity LoRA** para el look. Imagen: Flux.1-dev LoRA vía **AI-Toolkit** o **kohya_ss**, 15-30 fotos variadas
(ángulos/luz/expresiones, captions `a photo of TOK person`), rank 16-32, ~1500-3000 steps, GPU 24GB+. Empareja con
**voice clone** (XTTS-v2/F5-TTS) + modelo de lip-sync/animación (LongCat-Avatar/Hallo/SadTalker). **El avatar = identity LoRA (look) + voice clone (sonido) + driving model (movimiento); son 3 modelos, no uno.**

## Fine-tune de modelo de VIDEO
LoRAs de **Wan 2.2** (14B) o **LTX/Hunyuan** con **diffusion-pipe** o **AI-Toolkit**. **Wan 2.2 tiene 2 expertos
(high-noise + low-noise) → entrenas y shippeas AMBAS LoRAs.** VRAM: 5B ~8GB; 14B necesita 24-32GB (FP8 + grad
checkpointing + block offload) o 48GB+/H100 full-speed. **Motion LoRAs** capturan un movimiento de unos clips. Datasets chicos (10-50 clips) pero VRAM-bound y lentos.

## Distillation (lento → rápido)
Reducción de steps para correr en 1-8. **LCM-LoRA** (drop-in SD/SDXL), **SDXL-Lightning/Turbo**, **Flux schnell**,
o entrena con **DMD2**. Cambia algo de calidad/diversidad por 5-20× velocidad — ideal real-time.

## Fine-tune de LLM
SFT (LoRA/QLoRA) para formato/persona/tool-call; **preference optimization** para alineación. 2026: **GRPO**
(DeepSeek, sin critic — más simple que PPO, más estable que DPO) es el default; **DPO** ok para pares simples.
Tooling: **Unsloth** (más rápido single-GPU, ~20B QLoRA en 8h en 4090), **Axolotl** (YAML, reproducible), **TRL**
(DPO/GRPO), **LLaMA-Factory**. **La calidad de datos domina sobre el método** — 1K ejemplos limpios > 100K ruidosos.

## Costo (GPU rentada)
4090 (~$0.3-0.7/hr) para imagen/LLM LoRA; A100/H100 (~$1.5-3/hr) para video y 70B. Identity LoRA = pocos dólares;
Wan video LoRA = decenas; 70B SFT = bajos cientos. **Eval:** imagen→A/B humano + CLIP/identity-sim; video→FVD+review; LLM→métrica de tarea (un fine-tune que no mueve tu métrica *falló*, sin importar el train loss).

## Gotchas
1. **Chat template/special tokens equivocados arruinan un LLM fine-tune en silencio** — aplica el template EXACTO del modelo (Llama ≠ Mistral ≠ Qwen).
2. **Overfit de identity LoRA** — demasiados steps/rank alto "hornean" fondo/pose; diversifica fotos, baja rank/steps.
3. **Debes shippear AMBAS LoRAs de Wan 2.2** — solo high- o low-noise = movimiento roto.
4. **Modelos destilados pierden diversidad/prompt-adherence** — Turbo/Lightning a 1-4 steps degradan detalle y control de negative; mantén un path full-step para hero shots.
5. **Mismatch flash-attn/CUDA/torch ABI** = fallo #1 de training de video — pinea flash-attn al build exacto.
6. **No fine-tunees para conocimiento** — los hechos se vuelven stale y se alucinan; usa RAG. Fine-tune solo para comportamiento/estilo/identidad.

**Fuentes:** github.com/Wan-Video/Wan2.2 · github.com/tdrussell/diffusion-pipe · github.com/unslothai/unsloth · huggingface.co/docs/trl.
