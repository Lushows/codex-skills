# 237 · DreamBooth y full fine-tune de difusión (cuándo dejar el LoRA atrás)

> El LoRA gana el 95% de las veces. Esta ref es para el 5%: cuando necesitas que el sujeto
> sea *idéntico* en cualquier pose, o reescribir el dominio entero del modelo base.

## El árbol de decisión (no te saltes esto)
```
¿basta con parecido razonable + componibilidad? ──sí──► LoRA (ref 152)
        │ no
¿un sujeto/objeto, máxima fidelidad, base intacto? ──sí──► DreamBooth-LoRA
        │ no
¿cambiar el modelo a un dominio nuevo, miles de img? ──sí──► full fine-tune
```
En 2026 casi nadie hace **DreamBooth clásico** (escribe todos los pesos del UNet/DiT): se usa
**DreamBooth-LoRA** (la *técnica* DreamBooth —trigger + prior preservation— sobre *pesos* LoRA).
Te da la fidelidad de DreamBooth con archivo de 50-200MB y VRAM de LoRA. El full fine-tune se reserva
para "quiero que TODO el modelo piense en mi estilo médico/anime/producto", no para una cara.

## DreamBooth: qué lo distingue del LoRA puro
1. **Trigger + clase**: `a photo of sks man` — el token raro `sks` se ata al sujeto, `man` ancla la clase.
2. **Prior-preservation loss (PPL)**: entrenas en paralelo con **imágenes de regularización** de la clase
   genérica (`man`) generadas por el *propio* base. Sin esto, el modelo sufre **language drift**: todo
   "man" empieza a parecerse a tu sujeto y pierde diversidad. Peso `--prior_loss_weight 1.0`.
3. **Reg images**: 100-200, generadas con el mismo base + sampler + ~50 pasos, prompt = solo la clase.
   Regla común: `nº_reg ≈ nº_train × repeats`. Guárdalas y reúsalas entre runs de la misma clase.

PPL cuesta ~2× el forward (sujeto + clase por step) y rara vez ayuda a un LoRA puro de estilo. Úsalo
cuando entrenas un sujeto Y notas que contamina la clase. Para producto/logo sin clase clara, sáltalo.

## Hiperparámetros reales
| Param | DreamBooth-LoRA SDXL | DreamBooth-LoRA FLUX | Full FT SDXL |
|---|---|---|---|
| lr (UNet/DiT) | 1e-4 | 1e-4 a 4e-4 | **1e-6 a 5e-6** (¡bajísimo!) |
| text-encoder lr | 5e-5 o 0 | 0 (T5/CLIP congelados) | 1e-6 o 0 |
| pasos | 800-1500 | 1000-2000 | 10k-100k+ |
| reg images | 100-200 | 100-200 | n/a (dataset grande) |
| rank | 16-32 | 16-32 | — |
| optimizer | AdamW8bit / Prodigy | AdamW8bit | Adafactor / AdamW |
| precision | bf16 | bf16 (+ fp8 base) | bf16 |
| VRAM | 16-24GB | 20-24GB (fp8) | 48-80GB+ |

**Full fine-tune muerde por el lr**: con 1e-4 (lr de LoRA) revientas el base en pocos cientos de pasos
(catastrophic forgetting). Va **10-100× más bajo** + warmup + EMA de pesos para estabilizar. Activa
**gradient checkpointing** siempre (cambia ~30% de tiempo por mucha VRAM) y **8-bit Adam / Adafactor**
para que el estado del optimizer no duplique los GB de los pesos en fp32 (Adam guarda 2 momentos → 2×).

## VRAM: por qué full FT necesita 48-80GB
No son los pesos (SDXL UNet ≈ 2.6B params ≈ 10GB bf16), es **pesos + gradientes + estado Adam + activaciones**.
Regla: full FT en fp32-mixto ≈ `pesos × ~4` solo para optimizer+grads. SDXL cabe en 1×A100-80GB con
checkpointing; FLUX.2 (32B) exige **FSDP/DeepSpeed multi-GPU** (ver [[233-fsdp-deepspeed-diffusion-training]]).
DreamBooth-LoRA cabe en una 4090 (24GB) porque solo entrena las matrices low-rank + reg forward.

## Gotchas
1. **Overfit es más fácil con DreamBooth** que con LoRA puro (escribes más capacidad). Menos pasos,
   guarda checkpoints cada epoch, elige por inspección visual — no por loss.
2. **Reg images de baja calidad envenenan**: si el base genera basura para tu clase, PPL enseña basura.
   Cura las reg igual que el train set.
3. **Full FT sin EMA oscila**: los samples se ven peor a mitad de run que al inicio. EMA suaviza.
4. **Licencia**: full FT sobre FLUX.1-dev/FLUX.2 hereda *non-commercial*. Para comercial, base permisivo
   (SDXL OpenRAIL, FLUX.1-schnell Apache). Mismo aviso que en [[152-lora-training-avatar-personaje-propio]].
5. **No mezcles lr de SDXL y FLUX** — FLUX es flow-matching, otra dinámica (ver [[07-training-finetuning-a-fondo]]).

## Fuentes
- https://huggingface.co/docs/diffusers/en/training/dreambooth
- https://github.com/huggingface/diffusers/blob/main/examples/dreambooth/train_dreambooth_lora_sdxl.py

Cruza con [[152-lora-training-avatar-personaje-propio]], [[233-fsdp-deepspeed-diffusion-training]] y [[07-training-finetuning-a-fondo]].
