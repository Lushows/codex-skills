# 154 · Destilar/acelerar TU modelo (pasos 25→4→1)

> Un DiT de difusión que pide 25-50 pasos por frame es carísimo en video. La destilación de pasos lo baja a 1-8 pasos con ~misma calidad → 4-10× más rápido y barato.
> LongCat-Avatar trae destilación lista (`--use_distill`); aplícala antes de optimizar kernels. Cruza con [[127-torch-compile-tensorrt-difusion]].

## La idea
El sampler estándar resuelve la ODE de difusión en muchos pasos pequeños. La **destilación** entrena un *student* (a menudo un LoRA o un set de pesos) que reproduce en 1-8 pasos lo que el *teacher* (tu modelo a 25-50 pasos) produce. Dos caminos:
- **Adaptar un acelerador existente** (LoRA de pocos pasos ya entrenado para el base) → casi gratis.
- **Destilar tú** (necesitas el teacher + training) → cuando el acelerador genérico rompe tu LoRA/estilo.

## Métodos (verificado 2026)
| Método | Pasos | Cómo funciona | Cuándo |
|---|---|---|---|
| **LCM** | 4-8 | consistency distillation sobre la ODE | maduro, fácil, LoRA disponible (SDXL/SD1.5) |
| **Turbo (ADD)** | 1-4 | Adversarial Diffusion Distillation: destila + GAN loss vs imágenes reales | SDXL-Turbo; calidad alta a 1-4 |
| **Lightning** | 1-8 | distill progresivo + adversarial | SDXL-Lightning; varios checkpoints por nº de pasos |
| **Hyper-SD** | 1-8 | trajectory segmented distill + DMD + human-feedback | SOTA multi-paso, LoRA por presupuesto de pasos |
| **DMD2** | 1-4 | Distribution Matching Distillation v2: score model online + GAN, sin datos offline | top calidad/paso; estándar para destilar propio |
| **TDM / Flash-DMD** | 1-4 | trajectory/score-identity distill, costo de training ~1% de DMD2 | barato de entrenar si tienes el teacher |

Para **FLUX** existen LoRA Turbo/Hyper/Lightning de pocos pasos; pruébalos antes de destilar desde cero. Para **video** (LongCat/Wan) la destilación de pasos es la palanca grande (cada paso = todos los frames).

## Trade-off calidad/pasos
- 1 paso: máxima velocidad, pierde detalle fino/diversidad (modo-colapso posible).
- 4 pasos: el **sweet spot** habitual — ~calidad del teacher a 6-10× la velocidad.
- 8 pasos: casi indistinguible del teacher en la mayoría de casos.
- Empieza en 4-8 y baja solo si el throughput lo exige. Mide con FID/FVD + CLIP + ojo humano antes/después ([[17-evals-modelos-generativos]]).

## Aplicar un acelerador (lo barato primero)
- **LoRA de pocos pasos**: carga el Hyper-SD/Lightning/LCM-LoRA SOBRE tu base + tu LoRA de personaje; ajusta sampler/CFG. LCM/Turbo piden **CFG≈1** (guidance bajo) y scheduler propio (LCMScheduler / trailing). Si tu LoRA de marca se degrada con el acelerador genérico → toca destilar tú.
```python
pipe.load_lora_weights("Hyper-SDXL-4steps-lora.safetensors")  # acelerador
pipe.load_lora_weights("ohwx.safetensors")                     # tu personaje
# sampler few-step + CFG≈1, num_inference_steps=4
```

## Destilar tú (DMD2, receta práctica)
1. **Teacher** = tu modelo bueno (base + LoRA fusionado, o checkpoint full) a 25-50 pasos.
2. **Student** init desde el teacher; entrena con: (a) pérdida de distribution-matching contra el teacher + (b) un score model online de la distribución del student + (c) GAN loss vs imágenes reales (estabiliza, evita borrosidad).
3. Sin necesidad de generar dataset offline (ventaja DMD2 vs ADD clásico).
4. Coste: días-GPU en SDXL escala; **TDM/Flash-DMD** recortan eso ~100× si presupuesto ajustado.
5. Salida: un student de 1-4 pasos (o un LoRA de aceleración) que sirves igual que el teacher.
Fundamento de training en [[07-training-finetuning-a-fondo]].

## Servir el modelo destilado
- **LongCat / Wan**: pasa el flag de destilación del repo — LongCat-Avatar expone `--use_distill` → corre el sampler de pocos pasos integrado; combínalo con menos pasos en el config. Detalles del worker en [[111-longcat-avatar-runpod-produccion]].
- **diffusers/ComfyUI**: setea `num_inference_steps`=4-8, scheduler few-step (LCM/Euler trailing), `guidance_scale`≈1. Si destilaste un student full, cárgalo como checkpoint nuevo; si es LoRA-acelerador, hot-swap por request.
- **Orden de optimización**: primero destila (recorta pasos = recorta cómputo bruto), LUEGO compila el DiT con torch.compile/TensorRT y cuantiza ([[127-torch-compile-tensorrt-difusion]], [[12-cuantizacion-hands-on]]). Destilar × compilar es multiplicativo: 6× pasos × 1.5× kernel ≈ 9× total.
- Mide $/video antes y después; la destilación es lo que más mueve la aguja de costo en video serverless ([[30-finops-gpu]]).

## Trampas
- Acelerador genérico puede **borrar** tu estilo/identidad → re-evalúa el LoRA tras aplicarlo.
- CFG alto + few-step = artefactos; baja guidance.
- 1 paso puede colapsar diversidad en datasets pequeños; sube a 4 si ves repetición.
- Destilar requiere el teacher accesible en training (VRAM doble: teacher + student + score model).

Cruza con [[127-torch-compile-tensorrt-difusion]] y [[111-longcat-avatar-runpod-produccion]].
