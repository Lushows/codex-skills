# 185 · Edición por instrucción clásica (InstructPix2Pix → MagicBrush → datos de calidad)

> El linaje "edita con una frase, sin mask" empieza aquí. Hoy lo superan Kontext/OmniGen2, pero
> entender InstructPix2Pix explica los gotchas (CFG dual, drift) que TODOS los editores instruidos heredan.

## El árbol genealógico (verificado)
- **InstructPix2Pix** (Brooks et al.) — **primer** modelo de edición por instrucción. Fine-tune de Stable Diffusion sobre pares sintéticos generados con **GPT-3 + Prompt2Prompt**. Define el paradigma: imagen + instrucción → imagen editada, sin mask.
- **MagicBrush** (NeurIPS'23, OSU-NLP) — **primer dataset anotado a mano** (>10K triples), cubre single/multi-turn, con y sin mask. Fine-tunear IP2P sobre MagicBrush mejora mucho los edits reales. Pero es ~10K y sesgado a **transformaciones a nivel objeto** (descuida edits globales: estilo, clima).
- **HQ-Edit** (~200K edits) — pipeline escalable con **GPT-4V + DALL·E 3**; supera a IP2P/HIVE/MagicBrush en alineación (~92.8) y coherencia (~91.9). La lección: **el dataset, no la arquitectura**, fue el cuello.
- **UltraEdit** — edición fine-grained a escala, otra ruta de datos masivos.

## Cómo funciona (y por qué importa para servir)
IP2P usa **dos escalas de guidance (dual CFG)** simultáneas:
- `image_cfg` (image guidance ~1.2-1.8): cuánto se parece al original.
- `text_cfg` (guidance del prompt ~5-9): cuánto obedece la instrucción.
Estos dos pesos **son la palanca principal** de IP2P y derivados. `image_cfg` alto = conserva más (menos edita); `text_cfg` alto = obedece más (más drift). Tunearlos por tipo de edit es el 80% de la calidad.

## Dónde encaja hoy (2026)
- **No es SOTA** — Kontext ([[183-flux-kontext-editing-deep]]) y OmniGen2 ([[184-omnigen-unified-edit]]) lo superan en preservación y adherencia.
- **Sigue útil** porque: SD1.5-class → **barato y rápido** (corre en GPU modesta, <8GB), fácil de fine-tunear para un dominio cerrado (catálogo, un estilo de marca), y ComfyUI-friendly.
- Para volumen alto de edits simples y baratos en un dominio acotado, un IP2P fine-tuneado con tus pares puede batir en **$/edit** a llamar Kontext-pro.

## Fine-tune para tu dominio (la jugada de valor)
1. Genera pares (antes/después/instrucción) de TU caso — sintéticos con un editor SOTA (Kontext/Nano-Banana) como "profesor" → destilas a IP2P barato.
2. Fine-tune corto (LoRA o full) sobre esos pares ([[07-training-finetuning-a-fondo]], [[03-model-customization-lora-controlnet]]).
3. Sirves el IP2P fine-tuneado barato; reservas el editor caro solo para los casos que falla.

## Gotchas (heredados por todo editor instruido)
1. **Drift global** — IP2P recolorea/altera regiones que no mencionaste; si necesitas conservación exacta, composite-back con mask ([[182-inpaint-outpaint-serving]]).
2. **Dual CFG mal tuneado** = o no edita (image_cfg alto) o destruye el original (text_cfg alto). Es el #1 de soporte.
3. **Sesgo del dataset** — un modelo entrenado en MagicBrush hace edits de objeto pero falla en globales (estilo/clima). Elige/mezcla dataset según tus edits.
4. **Resolución baja** vs FLUX-class — SD1.5 a 512² limita detalle; upscale posterior ([[08-upscaling-restauracion]]).
5. **Instrucciones ambiguas** — IP2P es literal y frágil; frases imperativas cortas ("make it night") > descripciones largas.

Cruza con [[183-flux-kontext-editing-deep]], [[60-edicion-imagen-avanzada-ia]] y [[07-training-finetuning-a-fondo]].
