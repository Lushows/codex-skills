# 184 · Modelos unificados de edición (OmniGen2 y la familia "un modelo, varias tareas")

> Un solo modelo que hace t2i, edición instruida, in-context y entendimiento — sin pipeline de
> N checkpoints. Menos VRAM total y menos pegamento; a cambio de no ser SOTA en ninguna tarea aislada.

## La idea
En vez de orquestar SDXL-inpaint + Kontext + ControlNet + matting como módulos separados, un modelo **multimodal unificado** acepta texto e imágenes mezclados y decide la tarea por la instrucción. Menos modelos que cargar → menos VRAM y menos código de orquestación. El precio: suele perder contra un especialista (FLUX-Fill en fill, Kontext en preservación).

## OmniGen2 (verificado, arXiv 2506.18871 / GitHub VectorSpaceLab)
- **~7B params**, arquitectura **dual-path**: rutas separadas para texto e imagen con parámetros independientes y **tokenizer de imagen desacoplado** — clave del salto en edición vs OmniGen v1.
- Construido sobre **Qwen2.5-VL** como base de comprensión → buen seguimiento de prompts largos y composición.
- Cuatro capacidades: **understanding, generation, editing, in-context** (combinar inputs cross-modal en un solo prompt).
- Fuerte en **edición local precisa por lenguaje natural** (cambiar ropa, ajustar pose/acción) sin mask.
- Open-source; corre en ComfyUI. VRAM modesta por los 7B [no verificado el mínimo exacto; ~16-24GB típico fp16].

## Familia / alternativas unificadas
| Modelo | Rasgo | Acceso |
|---|---|---|
| **OmniGen2** | dual-path, in-context, editing fuerte | open |
| **Qwen-Image-Edit** | rey del **texto in-image** (CN/EN) y objetos | open |
| **Nano Banana / Pro** (Gemini Image) | entendimiento espacial best-in-class, relight | API-only |
| **OmniGen v1** | predecesor, edición más débil | open |

[no verificado: el ecosistema se mueve rápido; valida pesos/licencia antes de producción].

## Cuándo unificado vs especialista
- **Unificado gana** cuando: prototipas, tienes poca VRAM para varios modelos, o la tarea es "in-context" mezclando varias imágenes + texto en un prompt (lo que un pipeline de módulos hace torpe).
- **Especialista gana** cuando: necesitas la máxima calidad en UNA tarea — FLUX-Fill para fill/expand ([[182-inpaint-outpaint-serving]]), Kontext para preservación de identidad ([[183-flux-kontext-editing-deep]]), Qwen-Image-Edit para texto in-image.
- Regla práctica: **un unificado como default + especialistas para los casos que el unificado falla**, no reemplazo total.

## Serving
- Un solo checkpoint warm → handler más simple que multiplexar 3 modelos; menos VRAM pico.
- Para multi-imagen in-context: define en el prompt el **rol de cada input** (igual que Kontext multi-ref).
- Pesos a Network Volume ([[113-network-volume-modelos-grandes]]); warm-state en VRAM.
- Mide calidad por tarea con un eval propio (CLIP-score alineación + coherencia), porque un unificado puede regresionar en una tarea al mejorar otra ([[17-evals-modelos-generativos]]).

## Gotchas
1. **"Hace todo" ≠ "hace todo bien"** — benchmarkea contra el especialista de TU tarea antes de comprometerte.
2. **Tokenizer/preprocesado propio** — cada unificado normaliza imágenes distinto; no reuses el pipeline de SDXL a ciegas.
3. **Licencia y base model** — OmniGen2 hereda términos de Qwen2.5-VL en parte; revisa cadena de licencias para uso comercial ([[39-legal-ia-generativa]]).
4. **In-context se diluye** con demasiadas imágenes de entrada — pocas y bien etiquetadas.

Cruza con [[183-flux-kontext-editing-deep]], [[35-vision-encoders-vlms]] y [[60-edicion-imagen-avanzada-ia]].
