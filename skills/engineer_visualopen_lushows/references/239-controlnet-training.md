# 239 · Entrenar un ControlNet propio (una condición de control nueva)

> Si tu condición de guía no existe (un layout de tu industria, un mapa de profundidad raro, un boceto
> de tu producto), no la finges con prompts: entrenas un ControlNet. Es más barato de lo que crees.

## Qué entrenas (y qué NO)
ControlNet **clona el encoder** del UNet/DiT base (copia entrenable), congela el base entero, y conecta la
copia al base mediante **zero-convolutions** (conv inicializadas a 0 → al arrancar el ControlNet no
perturba nada, aprende a inyectar control gradualmente). Resultado: el base intacto + una rama de ~700MB
(SDXL) que lee tu **imagen de condición** y guía la generación. NO reescribes el base → no hay forgetting.
Para FLUX existe `train_controlnet_flux.py`; misma idea sobre el DiT.

## El dataset: 3 columnas, esa es toda la magia
| Columna | Qué es |
|---|---|
| `image` | la imagen objetivo (lo que el modelo debe producir) |
| `conditioning_image` | tu condición alineada **píxel a píxel** con la objetivo (canny, depth, pose, segmap, tu mapa custom) |
| `text` | caption de la imagen objetivo |
[verificado: las 3 columnas son el contrato del `train_controlnet.py` de diffusers]

**El alineamiento es todo**: la `conditioning_image` debe corresponder *exactamente* a `image` (misma escena,
mismo encuadre). Se genera del par real: tienes la foto → le pasas el extractor (MiDaS para depth, OpenPose
para pose, tu algoritmo para la condición custom) → ese output ES la condición. Para una condición *nueva*
necesitas un proceso que la derive de imágenes reales, o un render sintético donde control y target nacen juntos.

## Cuántos datos
- **Condición "fácil"** (canny, depth — relación casi determinista): converge con **decenas de miles** de pares,
  a veces menos. El paper original muestra que ~50k ya da señal y el efecto "sudden convergence" (de golpe
  el modelo "entiende" la condición, normalmente entre 5k-10k pasos).
- **Condición "semántica"** (segmap → escena): **cientos de miles** para generalizar.
- Para un dominio estrecho (solo TU producto, un tipo de layout) puedes salir con **5k-20k** pares limpios.

## Hiperparámetros reales (diffusers)
| Param | SD1.5/2.x | SDXL | FLUX |
|---|---|---|---|
| lr | 1e-5 | 1e-5 | 1e-5 a 5e-6 |
| batch (per device) | 4 | 1-4 | 1-2 |
| grad-accum | 4-8 | 4-8 | 8+ |
| resolution | 512 | 1024 | 1024 |
| pasos | 50k-300k | 50k-200k | 30k-100k |
| optimizer | AdamW8bit | AdamW8bit | AdamW8bit |
| VRAM | 8-16GB | 24GB (grad-ckpt) | 40GB+ |
[verificado: batch per-device default 4, ≥8GB VRAM para SD base]

Activa **gradient checkpointing** y **8-bit Adam** para SDXL en 24GB. lr **constante** + warmup corto;
ControlNet tolera lr fijo bien. Guarda checkpoints frecuentes y valida con un set fijo de condiciones para
pillar el "sudden convergence" (no entrenes 200k a ciegas si ya convergió a 15k).

## Validación durante el training
Pasa N `conditioning_image` de validación + sus prompts cada M pasos y genera. Mira que: (a) la salida
**respete la condición** (la pose/depth se ve reflejada), y (b) no haya colapsado a ignorar el prompt.
En inferencia el peso se llama `controlnet_conditioning_scale` (0.0-1.0+): 1.0 = control fuerte, baja a
0.5-0.8 si pisa demasiado la creatividad. Eso se afina al SERVIR, no se hornea en el peso (ver
[[139-controlnet-ipadapter-serving-consistencia]]).

## Atajos antes de entrenar desde cero
1. **¿Existe ya un ControlNet de tu tipo?** (canny/depth/pose/scribble/segmap/tile están publicados para
   SD/SDXL/FLUX). Entrena solo si tu condición es genuinamente nueva.
2. **Fine-tune de un ControlNet existente** > scratch: parte de uno cercano y reentrénalo en tu dominio —
   muchísimos menos pasos.
3. **ControlNet-LoRA / Control-LoRA**: versión low-rank de la rama de control, archivo más chico y train más
   barato; menos capacidad que el ControlNet completo pero suele bastar para un dominio estrecho.

## Gotchas
1. **Condición desalineada = ControlNet inútil.** El error nº1: `conditioning_image` no casa píxel-a-píxel
   con `image`. Verifica superponiéndolas a ojo en una muestra grande.
2. **Caption sí importa**: el ControlNet aporta *estructura*, el prompt aporta *contenido/estilo*. Captions
   pobres → el modelo no sabe qué rellenar dentro de la estructura.
3. **Resolución de la condición = la del target.** Mezclar resoluciones rompe el alineamiento.
4. **Sudden convergence**: no juzgues por el loss (apenas se mueve); juzga por el grid de validación.

## Fuentes
- https://huggingface.co/blog/train-your-controlnet
- https://github.com/huggingface/diffusers/blob/main/examples/controlnet/train_controlnet_sdxl.py
- https://github.com/huggingface/diffusers/blob/main/examples/controlnet/train_controlnet_flux.py

Cruza con [[139-controlnet-ipadapter-serving-consistencia]] y [[03-model-customization-lora-controlnet]].
