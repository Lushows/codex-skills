# 49 — Consistencia de personaje y marca entre generaciones

El reto real de producción no es generar UNA imagen buena, es generar VEINTE con el mismo personaje, producto y
look. Sin disciplina, cada generación es una persona distinta. Las palancas, de menor a mayor control:

## 1. Character sheet / model sheet
Antes de nada: `character turnaround sheet, same character, front/side/back/3-quarter views, neutral lighting,
plus expression sheet (neutral, smiling, angry)`. Esa hoja es tu fuente de verdad y la entrada para entrenar/referenciar.

## 2. Seed locking
Fijar el seed mantiene composición/identidad estable mientras cambias detalles menores. Útil para variaciones finas, frágil ante cambios grandes de prompt.

## 3. Style & character references (sin entrenar)
- **Midjourney:** `--sref` (estilo), `--cref` + `--cw` (personaje, cw 0-100 controla cuánto), y **Omni-Reference (`--oref`, `--ow`)** en v7 (alta fidelidad de personaje/objeto).
- **FLUX:** **Redux** (variación por referencia) e **IP-Adapter**; **FLUX.2** mejora consistencia multi-referencia.
- **Nano Banana Pro (Gemini):** **consistencia multi-imagen NATIVA** — le das varias fotos del personaje/producto y mantiene identidad entre ediciones; de los mejores 2026 sin entrenar.

## 4. Face consistency dedicada
**InstantID**, **IP-Adapter FaceID**, **PuLID** — toman una foto de cara y la preservan a través de generaciones (ComfyUI/auto-hospedado). Rápido, sin entrenamiento.

## 5. Character LoRA (máximo control)
Entrenas un LoRA con 15-30 imágenes una vez y lo reúsas infinitamente con identidad sólida. Estándar para campañas largas y producto recurrente. FLUX/SDXL vía Replicate, fal.ai o local. (Ver ref 07.)

## 6. Consistencia de producto real
Para tu frasco/empaque físico: **FLUX Kontext** y **Nano Banana edit** permiten *editar* manteniendo el producto
idéntico — cambias fondo/luz/escena, pero el producto real persiste. **Mejor que regenerar** (que lo deforma). Sube la foto real y edita el entorno.

## 7. Brand kit consistente
Define un *style token* fijo: paleta hex, film stock, focal length, tipo de luz → verbatim en cada prompt. Logo/
tipografía: **NO** confíes en el modelo para el lockup; compón el logo en post (Figma/Canva) sobre la imagen generada. Texto en imagen: Ideogram/Nano Banana.

## 8. Workflow multi-shot
Character sheet → entrena LoRA o fija `--cref`/Omni-Ref → produce cada plano con el MISMO style token + misma
referencia → corrige outliers con inpaint. Para image→video, anima desde stills ya consistentes (la consistencia se gana en imagen, no en video).

Ej (MJ v7): `lifestyle shot of [character], drinking coffee at a cafe, 50mm, soft window light, muted palette --cref [url] --cw 80 --sref [url] --s 150`

## Gotchas
- **Deriva en secuencia:** re-ancla SIEMPRE a la MISMA imagen de referencia, no a la última generada (los errores se acumulan).
- **Trade-off cara vs estilo:** `--cw` alto preserva cara pero ignora wardrobe/pose; bájalo si necesitas más libertad de escena.
- **Conflicto prompt vs referencia:** si el prompt contradice la referencia (color de pelo distinto), el modelo promedia y rompe ambos. Que concuerden.
- **LoRA overfit:** demasiadas imágenes iguales = el personaje sale siempre en la misma pose → varía poses/luz en el dataset.
- **Producto deformado al regenerar:** no regeneres, EDITA con Kontext/Nano Banana sobre la foto real.
- **Consistencia imagen→video:** el video introduce deriva propia → start frame consistente + clips cortos + motion bajo.

**Fuentes:** docs.midjourney.com (sref/cref/omni-reference) · bfl.ai (FLUX Kontext/Redux) · deepmind.google (Nano Banana Pro) · github.com/cubiq/PuLID, InstantID.
