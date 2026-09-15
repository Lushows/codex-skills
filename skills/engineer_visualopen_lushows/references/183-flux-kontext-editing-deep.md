# 183 · FLUX.1 Kontext a fondo (edición instruida sin máscara, multi-ref, serving)

> Kontext edita por **instrucción de texto sin máscara** preservando todo lo demás — y trata las
> imágenes de referencia como "palabras" en el contexto. Es el caballo de batalla de edits controlados.

## Qué es (verificado, arXiv 2506.15742)
Transformer de **flow matching rectificado, 12B params**, in-context: concatena la imagen de entrada (vía tokens latentes) con el prompt y genera la imagen editada. No necesita mask ni fine-tuning. `[dev]` open-weights (~24GB fp16), `[pro]`/`[max]` API. La preservación de contexto es su rasgo distintivo: "cambia X, conserva el resto" con drift mínimo.

## Variantes y cuándo cada una
| Variante | Acceso | Para qué |
|---|---|---|
| `[dev]` | open, ~24GB VRAM | self-host, LoRA, edits single-ref |
| `[dev] Multi` | open | hasta **4 imágenes de referencia** + instrucción; combina sujetos/estilos/escenas |
| `[pro]` | API (fal/Replicate/Together/Runware/DataCrunch) | producción sin servir VRAM |
| `[max]` | API | máxima calidad/adherencia |

Multi-ref es la pieza nueva: alimentas referencias como contexto → **consistencia de personaje/producto sin entrenar un LoRA**.

## Casos donde gana sobre inpaint con mask
- **"Conserva el producto, cambia la escena"** — sin recortar ni enmascarar; mantiene label/logo/color del producto real (ver workflow producto en [[60-edicion-imagen-avanzada-ia]] y [[80-visualizacion-fotografia-producto-ia]]).
- **Edits sucesivos** (refinamiento iterativo) con drift mínimo entre pasos — su fortaleza medida.
- **Consistencia de personaje**: misma cara en escenas distintas pasando un retrato de referencia.

## Patrón de prompt (lo que de verdad mueve la aguja)
- Verbo de edición + objeto + **cláusula de preservación explícita**: `"change the background to a marble counter, keep the product label, color and shape exactly"`.
- Sin la cláusula `keep ...`, Kontext igual driftea identidad. La preservación es fuerte pero no automática.
- Para multi-ref: nombra el rol de cada imagen en el prompt (`"use the person from image 1, the jacket from image 2"`).

## Serving (ver [[149-flux-serving-a-fondo]] para el detalle FLUX)
- 24GB → A100/L40S/4090(24GB justo). fp8/NF4 baja VRAM con pérdida menor de calidad (ver [[12-cuantizacion-hands-on]]).
- **Pesos pesados** → Network Volume, no re-bajar por cold start ([[113-network-volume-modelos-grandes]]).
- Mantén el transformer warm en VRAM; el cuello es la carga del checkpoint, no el denoise.
- Partners con endpoints listos: fal, Replicate, Together (6x con Simplismart [no verificado el factor exacto]). Si el volumen es bajo, **API > self-host**: 24GB encendidos cuestan más que llamadas esporádicas.

## Gotchas
1. **Drift de identidad sin cláusula keep** — el #1; siempre ancla lo que NO debe cambiar.
2. **Multi-ref > 4 imágenes** no soportado; más referencias = diluir el contexto, no mejorarlo.
3. **No es pixel-perfect en regiones intactas** — VAE roundtrip recolorea levemente todo; si necesitas conservación EXACTA de una zona, combina con composite-back de mask ([[182-inpaint-outpaint-serving]]).
4. **Licencia `[dev]`**: non-commercial salvo licencia BFL; producto pagado requiere licencia comercial. Revisa SIEMPRE ([[39-legal-ia-generativa]]).
5. **Texto in-image** lo edita peor que **Qwen-Image-Edit**; para tipografía/letras usa Qwen (ver [[184-omnigen-unified-edit]] §comparativa).

Cruza con [[149-flux-serving-a-fondo]], [[60-edicion-imagen-avanzada-ia]] y [[184-omnigen-unified-edit]].
