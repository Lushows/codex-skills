# 152 · LoRA de personaje/marca propio (FLUX/SDXL) end-to-end

> Un LoRA bien hecho mete TU cara/producto/estilo en un modelo base con 20-40 fotos y ~30 min de GPU.
> El 80% del resultado se decide en el dataset, no en los hiperparámetros. Cruza con [[153-dataset-curation-captioning-visual]].

## Qué es y cuándo
LoRA = matrices de bajo rango (A·B) inyectadas en las capas de atención del DiT/UNet; entrenas ~0.1-1% de los pesos, archivo de 20-300MB que cargas SOBRE el base sin tocarlo. Úsalo para: una **persona** (avatar consistente), una **marca/producto** (envase, logo), un **estilo**. Para video (LongCat/Wan) el LoRA va sobre el DiT igual; para identidad facial sin training, evalúa primero IP-Adapter/PuLID (zero-shot) — el LoRA gana en consistencia pero cuesta. Cruza con [[03-model-customization-lora-controlnet]] y [[49-consistencia-personaje-marca-ia]].

## Pipeline: dataset → training → serving
```
fotos crudas → curar+caption (ref 153) → bucketing → kohya/ai-toolkit → .safetensors
            → validar (grid de checkpoints) → servir (ComfyUI/diffusers, peso 0.7-1.0)
```

## 1. Dataset (lo crítico)
| Sujeto | Nº imágenes | Notas |
|---|---|---|
| Persona/cara | 20-40 | varía ángulo, luz, fondo, expresión; **no** 30 selfies iguales |
| Producto/envase | 15-30 | 360°, escalas, contextos; fondo limpio + lifestyle |
| Estilo | 50-150 | sujetos diversos, look constante |

Resolución ≥1024px lado corto (FLUX/SDXL entrenan a 1024). Sin watermark, sin compresión basura, sin duplicados near-idénticos (sesgan). Detalle completo de curación, dedup y captioning en [[153-dataset-curation-captioning-visual]].

## 2. Captioning + trigger word
- **Trigger único y raro**: `ohwx`, `tk_brand`, `sks_persona` (token poco usado por el base) → el concepto se "cuelga" del trigger.
- Persona: captions **cortas** (`ohwx man, smiling, studio light`). Describe lo VARIABLE (pose, fondo) y NO el rasgo fijo (si describes "brown eyes" en todas, el modelo no lo ata al trigger).
- Estilo: captions más densas + trigger de estilo.
- Auto-caption con JoyCaption/Florence-2/Qwen2.5-VL y limpia a mano (ver 153).

## 3. Hiperparámetros (recetas verificadas 2026)
FLUX es flow-matching → **lr más bajo y más pasos** que SDXL. No reuses settings de SD1.5.

| Param | FLUX.1/FLUX.2 dev | SDXL |
|---|---|---|
| network_dim (rank) | 16-32 (persona) · 32-64 (estilo) | 16-32 |
| network_alpha | = rank, o rank/2 | = rank |
| learning_rate | 1e-4 (baja a 5e-5 si quema) | 1e-4 · 4e-4 con Prodigy |
| optimizer | adamw8bit / Prodigy (lr=1) | adamw8bit / Prodigy |
| pasos totales | 1000-2000 (sweet spot) | 1500-3000 |
| batch / grad-accum | 1 / 1-4 | 1-2 |
| resolution | 1024 (+ bucketing) | 1024 |
| precision | bf16 | bf16/fp16 |
| text-encoder LR | 0 (FLUX: congela T5/CLIP) | opcional, ~5e-5 |

Regla práctica: `pasos ≈ imágenes × repeats × epochs`. 30 img × 10 repeats × 6 epochs ≈ 1800 pasos. Guarda checkpoint cada epoch para barrer overfit. VRAM: FLUX LoRA cabe en 16-24GB (con `--fp8_base` baja a ~10-12GB; 8GB posible con offload pero lento).

## 4. Herramientas
- **ai-toolkit** (ostris) — *default 2026 para FLUX.2*; web UI, config YAML, soporta FLUX.2 dev (32B) y klein (4B), Wan, SDXL. Más simple que kohya.
- **kohya sd-scripts** — el estándar maduro; máximo control, `flux_train_network.py`, LoRA+, bucketing nativo. Para SDXL sigue siendo referencia.
- **diffusers** `train_dreambooth_lora_flux.py` — si ya vives en HF/diffusers; integrable en pipeline propio.
- Para video (LongCat/Wan): usa el trainer del repo del modelo o diffusers-Wan; mismos principios.
Cruza la teoría profunda con [[07-training-finetuning-a-fondo]] y [[57-fine-tune-modelo-propio]].

## 5. Evitar overfit (el fallo nº1)
Síntomas: clones el fondo/pose del dataset, ignora el prompt, "fríe" colores, artefactos. Palancas:
- Menos pasos (para en cuanto se parece — checkpoint 1000 suele ganar a 2500).
- rank más bajo (16 antes que 64 para persona).
- Más variedad en el dataset (la cura real).
- Sirve a **peso <1.0** (0.6-0.8) en inferencia.
- Opcional: regularization images (clase genérica) en DreamBooth para no devorar la clase entera.

## 6. Validar
- En training, genera un **grid de validación** cada N pasos con prompts fijos (cara conocida + situación nueva) → mira a OJO la curva de parecido vs flexibilidad.
- Test set de prompts: in-distribution (pose vista), out-of-distribution (pose nueva, otro estilo), negativos (el concepto NO debe aparecer sin trigger).
- Métricas opcionales: identidad facial con ArcFace cosine vs referencia; CLIP-score prompt↔imagen. Eval formal en [[17-evals-modelos-generativos]].

## 7. Servir el LoRA
- **ComfyUI**: nodo `Load LoRA` → `strength_model` 0.7-1.0; encadena varios LoRA (persona + estilo) cuidando que no se peleen (baja pesos). Ver [[06-comfyui-backend-produccion]].
- **diffusers**: `pipe.load_lora_weights("ohwx.safetensors"); pipe.fuse_lora(lora_scale=0.8)` — fusiona para inferencia rápida, o deja sin fusionar para hot-swap por request.
- En producción serverless: mete el `.safetensors` en el Network Volume o hornéalo en la imagen; carga 1 vez en warm-state, cambia LoRA por job sin recargar el base. Cruza con [[113-network-volume-modelos-grandes]].
- Trigger word **obligatorio** en el prompt de inferencia o el LoRA no activa.

Cruza con [[153-dataset-curation-captioning-visual]], [[03-model-customization-lora-controlnet]], [[07-training-finetuning-a-fondo]], [[57-fine-tune-modelo-propio]].
