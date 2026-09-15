# 153 · Curación + captioning de dataset visual (donde se gana el LoRA)

> El dataset decide el 80% del resultado de un fine-tune/LoRA. 25 fotos curadas baten a 200 sucias.
> Pipeline: recolectar → dedup → filtrar calidad → balancear → captionar → bucketing → empaquetar. Alimenta [[152-lora-training-avatar-personaje-propio]].

## Objetivo por caso
| Caso | Qué maximizar | Trampa típica |
|---|---|---|
| Persona/avatar | variedad de ángulo/luz/expresión, identidad constante | 30 selfies casi iguales → overfit a una pose |
| Producto/marca | escalas, contextos, 360°, fondo limpio + lifestyle | solo packshots → no generaliza a escenas |
| Estilo | sujetos diversos, look constante | sujeto repetido → aprende el sujeto, no el estilo |

## 1. Recolección
- Fuentes: shoot propio (mejor para persona/producto), frames de video (1 cada N con `ffmpeg -vf "select='gt(scene,0.3)'"` para sacar variedad, no frames gemelos), scraping con derechos. Legal/derechos en [[39-legal-ia-generativa]]; scraping/captioning en lote en [[36-datasets-scraping-captioning]].
- De video: extrae más de lo que necesitas y luego filtra; los frames consecutivos son casi-duplicados.

## 2. Dedup (quita near-duplicados, sesgan fuerte)
- Perceptual hash: `imagededup` (PHash) o embeddings CLIP/DINOv2 + cosine, umbral ~0.95 → fusiona clusters, deja 1 representante.
- DINOv3/SigLIP2 como encoder para clustering de duplicados y de variedad (ver [[35-vision-encoders-vlms]]).
```python
from imagededup.methods import PHash
dups = PHash().find_duplicates(image_dir="raw/", max_distance_threshold=6)
```

## 3. Calidad y resolución
- Descarta: blur (varianza de Laplaciano baja), watermark, baja resolución, JPEG masticado, oclusiones de la cara/producto, recortes cortando el sujeto.
- Resolución: ≥1024px lado corto para FLUX/SDXL (entrenan a 1024); video-DiT según el modelo. No upscalees basura a 1024 — mete artefactos al LoRA.
- Detección de cara/sujeto (insightface/YOLO) para auto-rechazar frames sin el sujeto.

## 4. Balance
- Persona: reparte ángulos (frontal, 3/4, perfil), luz (día/estudio/interior), expresiones, planos (close/medio/cuerpo). Evita que 1 outfit/fondo domine.
- Producto: distintos fondos y escalas; incluye contextos de uso reales (lifestyle) además de packshot.
- Cuenta por bucket y rellena los flacos antes de entrenar.

## 5. Auto-captioning (2026)
| Modelo | Fuerte en | Nota |
|---|---|---|
| **JoyCaption** (alpha/beta) | captions naturales, sin censura, diseñado PARA datasets de training | favorito 2026 para LoRA |
| **Florence-2** | rápido, ligero, `<DETAILED_CAPTION>`; combínalo con WD14 tagger | corre en CPU/GPU chica |
| **Qwen2.5-VL** (3B/7B) | captions ricas y controlables por prompt | SOTA abierto, pesa más |
| **CogVLM / InternVL** | descripciones largas detalladas | overkill para persona |
| WD14 (tagger) | tags estilo booru (anime/estilo) | complementa, no sustituye prosa |

Corre en lote sobre el directorio (nodos ComfyUI tipo CaptionThis, o script con transformers). **Siempre revisa a mano**: el VLM alucina colores/objetos y eso envenena el training.

## 6. Trigger words + qué describir
- Inserta un trigger **único y raro** (`ohwx`, `tk_brand`) al inicio de cada caption → ancla el concepto.
- **Persona**: caption corta, describe lo VARIABLE (pose, fondo, luz) y NO los rasgos fijos. Si pones "blue eyes" en todas, el modelo no los liga al trigger → no salen sin describirlos.
- **Estilo/producto**: más descriptivo. Producto: nombra el producto con el trigger y el contexto.
- Formato kohya/ai-toolkit: un `.txt` por imagen, mismo nombre (`img001.jpg` ↔ `img001.txt`).

## 7. Bucketing por aspect-ratio
- No recortes todo a cuadrado: pierdes encuadre. Activa **bucketing** (kohya `enable_bucket`, ai-toolkit por defecto): agrupa por aspect-ratio (1:1, 3:4, 16:9…) y entrena cada bucket a su resolución → conserva composición sin distorsión.
- `min_bucket_reso`/`max_bucket_reso` (ej. 768-1280); `bucket_reso_steps=64`.
- Mezclar muchos ARs raros fragmenta batches → consolida a 3-5 buckets.

## 8. Empaquetar y versionar
- Estructura kohya: `dataset/<repeats>_<trigger>/` con imágenes + `.txt`. `repeats` controla cuánto se "ve" cada imagen.
- Versiona el dataset (DVC / un manifest con hashes) → reproducibilidad del LoRA. Registro en [[18-model-registry-versionado]].
- Guarda el dataset crudo y el curado por separado; el curado es el artefacto que importa.

## Checklist final
- [ ] Sin near-duplicados · [ ] ≥1024px · [ ] variedad balanceada · [ ] captions revisadas a mano · [ ] trigger en todas · [ ] bucketing activado · [ ] pares img/txt cuadran.

Cruza con [[152-lora-training-avatar-personaje-propio]], [[36-datasets-scraping-captioning]], [[35-vision-encoders-vlms]].
