# 240 · Entrenar / ajustar un IP-Adapter propio (image-prompt para tu dominio)

> El IP-Adapter mete una IMAGEN como prompt (estilo, cara, producto) sin entrenar por sujeto. Los públicos
> son genéricos; uno propio brilla cuando tu dominio es específico (tu catálogo, un tipo de rostro, tu estética).

## Qué es y por qué entrenarlo
IP-Adapter = **image encoder congelado** (CLIP ViT, normalmente `CLIPVisionModelWithProjection`) +
**decoupled cross-attention**: añade una *segunda* vía de cross-attention en el UNet/DiT, exclusiva para los
embeddings de la imagen, en paralelo a la de texto. Solo entrenas dos cosas pequeñas: el **image projection
model** (proyecta el embed de CLIP a tokens) y los **adapter modules** (los nuevos proyectores K/V de la rama
de imagen). El base y el encoder CLIP quedan **congelados** → entrenable ≈ pocos cientos de MB.

Decoupled = la clave: NO suma image+text en la misma atención (eso diluye), las separa y las combina al final.
Por eso conserva la calidad del texto y a la vez obedece la imagen.

## Variantes (elige la correcta)
| Variante | Encoder / tokens | Para qué |
|---|---|---|
| **IP-Adapter** base | CLIP global (1 vector) | estilo/contenido general, ligero |
| **IP-Adapter Plus** | CLIP **grid** (patches, +tokens) | detalle fino, fidelidad alta |
| **IP-Adapter FaceID** | embedding **ArcFace** (no CLIP) + LoRA | identidad de ROSTRO (lo que quieres para avatar) |
| **IP-Adapter SDXL** | encoder grande, UNet SDXL | calidad 1024 |
[verificado: existen `tutorial_train.py`, `tutorial_train_plus.py`, `tutorial_train_sdxl.py` en el repo tencent-ailab]

Para **cara/avatar** casi siempre quieres **FaceID** (usa ArcFace, mucho más fiel a identidad que CLIP) —
profundízalo en [[174-ip-adapter-face-deep]]. Para producto/estilo, Plus.

## El dataset
Formato del repo: un **JSON, lista de dicts** con `image_file` y `text` por muestra. [verificado]
- La imagen es a la vez **target** (lo que genera) y **fuente del image-prompt** (de ella se saca el embed CLIP).
- En training se aplica **image dropout** (~10%, se manda imagen vacía/cero) para que el adapter aprenda a
  funcionar también sin condición y soporte classifier-free guidance.
- Escala: el IP-Adapter original se entrenó en ~10M pares; **para tu dominio** estrecho, 50k-500k imágenes
  curadas dan un adapter sólido. Calidad y consistencia de dominio > volumen bruto.
- FaceID: necesitas **rostros con su embedding ArcFace** precomputado; cura por calidad de detección facial.

## Hiperparámetros reales
| Param | Valor |
|---|---|
| lr | **1e-4** (constante) [verificado] |
| weight_decay | 0.01 [verificado] |
| optimizer | AdamW sobre `image_proj_model` + `adapter_modules` encadenados [verificado] |
| resolution | **512 → multi-escala** (2 etapas) [verificado] |
| batch (per device) | 8 [verificado] |
| precision | bf16/fp16, encoder CLIP congelado |
| num_tokens | 4 (base) · 16 (Plus) |

**Estrategia 2-etapas** (importante): entrenar directo a 1024 es ineficiente → **pre-entrena a 512**, luego
**fine-tunea multi-escala**. [verificado] El image encoder se **congela** para ahorrar memoria; solo fluyen
gradientes por el proj model + adapters.

## Validar y servir
- Valida con imágenes-prompt *fuera* del train set: ¿transfiere estilo/identidad sin copiar literal el target?
- En inferencia el peso es `scale` (0.0-1.0+): 1.0 = imagen domina, 0.5-0.7 deja respirar al texto.
  Combinable con ControlNet (estructura) + IP-Adapter (apariencia) — ver [[139-controlnet-ipadapter-serving-consistencia]].
- FaceID + un LoRA de identidad encima sube fidelidad de rostro aún más (patrón de [[174-ip-adapter-face-deep]]).

## IP-Adapter vs LoRA de sujeto (cuándo cada uno)
- **IP-Adapter**: zero-shot en inferencia (pasas una foto nueva, sin reentrenar). Ideal para *muchos* sujetos
  o cuando el sujeto cambia por request. Menos fidelidad por-sujeto que un LoRA dedicado.
- **LoRA** (ref 152): un sujeto fijo, máxima consistencia, pero reentrenas por sujeto.
- **Combínalos**: IP-Adapter para apariencia general + LoRA fino para el detalle que IP-Adapter no clava.

## Gotchas
1. **Sin image dropout no hay CFG decente** — el adapter no aprende el caso "sin imagen". 10% es el estándar.
2. **CLIP global (base) pierde detalle**; si necesitas fidelidad usa **Plus** (grid de patches) o **FaceID** para cara.
3. **El encoder DEBE quedar congelado**: descongelarlo dispara VRAM y desestabiliza sin ganancia.
4. **Mismatch de encoder en serving**: el IP-Adapter está atado al CLIP exacto con que se entrenó; servir con
   otra versión de image encoder produce basura silenciosa.
5. **No esperes identidad perfecta del IP-Adapter base** para rostro — para eso es FaceID/ArcFace, no CLIP.

## Fuentes
- https://github.com/tencent-ailab/IP-Adapter/blob/main/tutorial_train.py
- https://github.com/tencent-ailab/IP-Adapter/blob/main/tutorial_train_plus.py · https://ip-adapter.github.io/

Cruza con [[174-ip-adapter-face-deep]] y [[139-controlnet-ipadapter-serving-consistencia]].
