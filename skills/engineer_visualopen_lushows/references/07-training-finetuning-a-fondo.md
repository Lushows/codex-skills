# 07 — Training / fine-tuning a fondo (2026)

> Adaptar un modelo a tu sujeto/estilo/marca. 99% de los casos = **LoRA**. Esta ref decide cuál método,
> cómo preparar datos, y los hiperparámetros REALES para SDXL vs FLUX (y video).

## Qué método y cuándo

| Método | Qué entrena | Tamaño salida | Cuándo | VRAM |
|---|---|---|---|---|
| **LoRA** | matrices low-rank inyectadas en attention/conv | **2-200MB** | **El default.** Sujeto, estilo, concepto. Componible/apilable. | 8-24GB |
| **DreamBooth** | el modelo completo (o con prior preservation) | full ckpt (GB) | Sujeto específico con máxima fidelidad cuando LoRA no basta; hoy casi siempre se hace **DreamBooth-LoRA** (lo mejor de ambos). | 16-40GB |
| **Full fine-tune** | TODOS los pesos | full ckpt | Cambiar el modelo base a fondo (dominio entero, miles de imágenes). Caro, riesgo de catastrophic forgetting. | 40-80GB+ |
| **Textual Inversion** | solo un **embedding** nuevo (token), NO los pesos | **KB** | Capturar un concepto ligero sin tocar el modelo; débil para detalle complejo. | 8-12GB |

Regla: **empieza con LoRA**. Sube a DreamBooth-LoRA si la fidelidad del sujeto no alcanza. Full fine-tune
solo con dataset grande y razón clara. Textual Inversion para conceptos sutiles/baratos.

## Preparación del dataset

- **Nº de imágenes:** sujeto/persona **15-30** buenas (FLUX rinde con 15-25); estilo **30-100+**; concepto
  10-20. Más NO es mejor si son de baja calidad o repetitivas → overfitting.
- **Captions:** **FLUX y SD3 quieren captions en lenguaje natural detallado** (frases descriptivas). SDXL
  tolera tags estilo booru. Para sujeto, usa un **token raro único** ("ohwx", "sks") + clase ("ohwx man").
  Auto-caption con **JoyCaption / Florence-2 / WD14 tagger** y luego limpia a mano. **No describas lo que
  quieres que el LoRA aprenda** (si todas dicen "blue shirt", el LoRA no fija la cara, fija la camisa).
- **Buckets (aspect ratio bucketing):** kohya/SimpleTuner agrupan imágenes por relación de aspecto → NO
  recortas a cuadrado, entrenas a resoluciones mixtas. Activa `enable_bucket`. Resolución base 1024 para
  SDXL/FLUX.
- **Regularization images** (solo DreamBooth): imágenes de la **clase** ("man") generadas por el propio
  modelo, para que no olvide el concepto general. ~100-200. LoRA puro normalmente **no** las necesita.

## Tools

| Tool | Fortaleza |
|---|---|
| **kohya_ss / sd-scripts** (bmaltais GUI) | Estándar histórico, control total, GUI. SDXL y FLUX. LoRA+ (lr separado para A/B). |
| **ai-toolkit** (Ostris) | **El más rápido/fácil para FLUX**, config YAML simple, 20-30% más rápido que SimpleTuner. El de facto para FLUX LoRA. |
| **SimpleTuner** (bghira) | **Gold standard de estabilidad/reproducibilidad**, mejor docs, FLUX/SD3/SDXL, full fine-tune. |
| **OneTrainer** | GUI todo-en-uno (LoRA/DreamBooth/embedding/full), buena para SDXL. |
| **diffusers train scripts** (`train_dreambooth_lora_*.py`) | Oficial HF, base de muchos; bueno para integrar en pipeline propio. |

## Hiperparámetros reales

### SDXL LoRA
- **rank (dim) 16-32**, **alpha = rank** (o rank/2). 64+ para estilos complejos.
- **lr 1e-4** (UNet); text encoder lr **5e-5** o congelado. Optimizer **AdamW8bit** (o **Prodigy**, lr=1, auto).
- **steps:** ~`nº_imgs × 100-150` o **1000-2500** total. batch 1-4.
- Scheduler `cosine` o `constant_with_warmup`. Resolución 1024.

### FLUX.1 / FLUX.2 LoRA (parámetros distintos a SDXL)
- **rank 16-32** (32-48 para estilos; 128 solo conceptos complejos). **alpha = rank**, o **alpha < rank**
  (ej. rank 128 / alpha 64) preferido para *transferencia de estilo más suave*.
- **lr 8e-4 a 1.5e-3** (más ALTO que FLUX.1, que usaba ~1e-4 a 5e-4 — verifica por tool). Optimizer
  AdamW8bit / Prodigy.
- **steps 800-2000** (FLUX converge más rápido que SDXL; buenos resultados a 1000-2000). batch 1-8.
- **FP8 quantization** del transformer para entrenar en consumer (24GB). **Requiere 24GB+**; ai-toolkit
  con offload baja a ~12-16GB con penalización de velocidad.
- Resolución 1024; bucketing on.

### Señales de overfitting
- El sujeto aparece **idéntico e inflexible**, ignora el prompt (no cambia pose/fondo/ropa).
- Artefactos "fritos"/sobre-saturados, fondos quemados.
- El **token de clase** contamina otras generaciones (todo "man" se parece a tu sujeto).
- **Fix:** menos steps, lr más bajo, menos rank, más variedad en el dataset, captions más ricas.
  Guarda checkpoints cada N steps y **elige el mejor por inspección**, no el último.

## VRAM / tiempo / costo (orden de magnitud)

| Tarea | VRAM | Tiempo (A100/4090) | Costo aprox |
|---|---|---|---|
| SDXL LoRA (20 img, 1500 steps) | 12-16GB | 20-40 min | <$1 serverless |
| FLUX LoRA (20 img, 1500 steps, fp8) | 16-24GB | 30-60 min | ~$1-3 |
| FLUX full fine-tune | 48-80GB | horas-días | $$$ |

Entrenar es **bursty** → RunPod serverless/spot con checkpointing (SKILL §6.32) encaja perfecto.

## Fine-tunear modelos de VIDEO / avatar

- **Motion LoRA:** LoRA sobre el bloque temporal/atención de un DiT de video → captura un **movimiento/
  estilo de cámara** (no contenido). Datasets de clips cortos etiquetados por el movimiento.
- **Wan / LTX-Video / Hunyuan:** **diffusion-pipe** (tdrussell) y **musubi-tuner** (kohya) son los tools
  2026 para LoRA de Wan2.x, LTX, Hunyuan-Video. ai-toolkit añadió soporte de algunos modelos de video.
- **Avatares (LongCat/EchoMimic):** rara vez se fine-tunean enteros; se adapta vía LoRA de identidad o se
  condiciona en inferencia (IP-Adapter/InstantID, ver `03-model-customization-lora-controlnet.md`).
- **VRAM video LoRA:** mucho más alta (activaciones = frames×H×W, SKILL §6.5). Suele requerir 24-48GB+ y
  **block-swap/offload** para caber. Datasets de pocos clips, lr bajo, pocos steps (sobreajustan rápido).

## Gotchas

1. **FLUX usa lr ~10× más alto que SDXL** (8e-4–1.5e-3 vs 1e-4). Copiar config de SDXL a FLUX da un LoRA
   que "no aprende". Y FLUX.2 difiere de FLUX.1 — verifica por tool.
2. **alpha = rank NO siempre es óptimo en FLUX:** alpha < rank suaviza estilos. Sabe qué buscas.
3. **Captions que describen el rasgo a aprender lo impiden.** Si quieres fijar una cara, NO la describas;
   describe lo variable (ropa, fondo, pose).
4. **El último checkpoint suele estar sobreajustado.** Guarda cada N steps y elige por inspección visual
   (grid de prompts variados), no por loss ni por "el último".
5. **Licencia del base se hereda.** FLUX.1-dev / FLUX.2 son **non-commercial** → un LoRA entrenado sobre
   ellos arrastra esa restricción para uso comercial. Para comercial entrena sobre SDXL (CreativeML-OpenRAIL)
   o FLUX.1-schnell (Apache) o un base permisivo. (SKILL §catálogo: ojo licencias.)
6. **Video LoRA OOM por activaciones, no por pesos.** Usa block-swap/offload del tuner; no asumas que
   porque el LoRA es chico cabe — el forward del DiT de video es lo que revienta la VRAM (SKILL §6.23).

## Fuentes
- https://apatero.com/blog/flux-2-lora-training-complete-guide-2025
- https://apatero.com/blog/how-to-train-flux-2-lora-complete-fine-tuning-guide-2025
- https://sanj.dev/post/lora-training-2025-ultimate-guide/
- https://learn.thinkdiffusion.com/flux-lora-training-with-kohya/
- https://github.com/bghira/SimpleTuner/discussions/635
- https://github.com/ostris/ai-toolkit · https://github.com/tdrussell/diffusion-pipe
