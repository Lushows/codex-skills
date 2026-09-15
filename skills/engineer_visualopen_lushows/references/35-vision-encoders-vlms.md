# Vision Encoders y VLMs: CLIP, SigLIP2, DINOv3 y Open VLMs (2026)

## Vision encoders: qué embebe cada uno

Un *vision encoder* convierte una imagen en vectores. La diferencia clave es **qué objetivo de entrenamiento** usaron, y eso determina para qué sirve cada embedding.

- **CLIP** (OpenAI): entrenado con pérdida **contrastiva** imagen↔texto sobre lotes. El embedding está **alineado con lenguaje** → excelente para búsqueda por texto ("foto de un perro") y zero-shot classification. Débil en relaciones espaciales finas (optimiza alineación global, no parches).
- **SigLIP / SigLIP2** (Google): reemplaza la softmax contrastiva por **sigmoid loss** que trata cada par imagen-texto independientemente → escala mejor y mejora alineación lenguaje-imagen. SigLIP2 añade objetivos multitarea (captioning, masked prediction) que preservan más información visual de bajo nivel. **El encoder de visión por defecto** en la mayoría de VLMs open de 2026.
- **DINOv2 / DINOv3** (Meta): **self-supervised, sin texto**. Sus parches codifican información local y contextual rica → ideal para tareas **espaciales/densas**: segmentación, detección, correspondencia, dedup visual, agrupar por similitud puramente visual (no semántico-lingüística). No sirve para buscar por texto (no está alineado con lenguaje).

**Regla**: ¿buscar/clasificar por texto? → CLIP/SigLIP2. ¿similitud visual pura, clustering, dedup, tareas densas? → DINOv3. Los mejores sistemas 2026 a menudo **combinan ambos** (SigLIP2 para geometría semántica-lingüística + DINOv3 para uniformidad espacial).

## Image embeddings para search / dedup / classification

- **Búsqueda semántica imagen↔texto**: embebe imágenes con CLIP/SigLIP2, indexa en FAISS o pgvector, consulta con el embedding del texto.
- **Dedup / near-duplicate**: DINOv3 (o un perceptual hash para exactos); umbral de coseno alto.
- **Classification**: zero-shot con CLIP (compara contra embeddings de etiquetas-texto) o entrena un linear probe sobre DINOv3.

## VLMs open 2026

Modelos que aceptan imagen+texto y generan texto (captioning, VQA, OCR, grounding, document understanding):

| VLM | Tamaños | Fuerte en | Licencia |
|---|---|---|---|
| **Qwen3-VL** (Alibaba) | hasta 72B+ | líder open: OCR, grounding, video, agentic | Apache 2.0 |
| **InternVL3** (Shanghai AI Lab) | 1B-78B | ~72% MMMU, el MIT-licensed más fuerte | MIT |
| **Llama 4** (multimodal) | Scout/Maverick MoE | contexto largo + visión | Llama license |
| **Pixtral** (Mistral, ahora en Small 4) | 12B | doc/VQA, Apache | Apache 2.0 |
| **Molmo** (Allen AI) | 7B-72B | fully-open (pesos+datos+código), pointing/grounding | Apache 2.0 |
| **SmolVLM** (HF) | 256M-2.2B | edge/throughput, 3-5× más rápido | Apache 2.0 |
| **Gemma 3 (vision)** (Google) | 4B-27B | multilingüe, OCR cross-border | Gemma license |

Calidad competitiva con GPT-5/Claude Opus/Gemini 3 en MMMU, OCRBench, ChartQA, DocVQA, a coste de despliegue mucho menor.

## Casos de uso de ingeniería

### Auto-captionar un dataset de entrenamiento

Usa un VLM para generar captions de miles de imágenes (entrenar un modelo de difusión, enriquecer metadatos). Qwen3-VL o InternVL3 vía vLLM en batch:

```python
# vLLM sirve el VLM con API OpenAI-compatible
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="x")
r = client.chat.completions.create(model="Qwen/Qwen3-VL-7B-Instruct",
  messages=[{"role":"user","content":[
    {"type":"image_url","image_url":{"url":f"data:image/jpeg;base64,{b64}"}},
    {"type":"text","text":"Describe esta imagen en una frase, en inglés."}]}])
```

Para volumen alto: SmolVLM (256M-2.2B) da 3-5× throughput en la misma GPU con calidad suficiente para captions cortos.

### Moderar / etiquetar imágenes generadas

Pasa cada imagen generada por un VLM con un prompt de política ("¿contiene desnudez/violencia/marca?") y **structured output** (JSON con flags). Útil como filtro post-generación en pipelines de imagen. Combina con constrained decoding (`guided_json`) para etiquetas garantizadas.

## Cómo ejecutarlos

- **transformers** (`AutoModelForImageTextToText`): rápido para prototipo / una imagen.
- **vLLM / SGLang**: producción y batch — sirven los VLMs principales con API OpenAI-compatible y continuous batching. Requieren `--max-model-len` amplio (las imágenes consumen muchos tokens visuales) y vigilar VRAM (los tokens de imagen inflan el KV-cache).

## Búsqueda de imágenes basada en embeddings

```python
# 1) Embebe el corpus con SigLIP2; 2) indexa en FAISS; 3) consulta por texto o imagen
import faiss, numpy as np
index = faiss.IndexFlatIP(1152)          # dim de SigLIP2
index.add(np.ascontiguousarray(img_embs))   # normaliza a L2=1 para coseno
D, I = index.search(query_emb, k=10)
```

Para producción persistente, usa **pgvector** o Qdrant en vez de FAISS en memoria. Misma mecánica que RAG de texto, pero con embeddings de imagen.

## Gotchas

1. **No mezcles espacios de embedding**: CLIP, SigLIP2 y DINOv3 viven en espacios distintos e incompatibles; no puedes comparar un vector CLIP contra uno DINO. Reindexar si cambias de encoder.
2. **DINOv3 no busca por texto**: no está alineado a lenguaje; si quieres query textual, necesitas CLIP/SigLIP2.
3. **Las imágenes queman tokens y VRAM**: en un VLM, una imagen de alta resolución puede valer miles de tokens visuales → sube `max_model_len` y vigila OOM en el KV-cache; baja la resolución si no necesitas detalle fino.
4. **Normaliza antes del coseno**: FAISS `IndexFlatIP` mide producto interno; sin normalizar L2, el "coseno" está mal.
5. **OCR ≠ todos los VLMs igual**: para documentos densos/tablas, Qwen3-VL, InternVL3 y Gemma 3 destacan; un VLM general pequeño alucina texto. Mídelo en OCRBench/DocVQA antes de confiar.

## Fuentes
- [SigLIP 2 (Hugging Face blog)](https://huggingface.co/blog/siglip2)
- [SigLIP/SigLIP2 overview (Emergent Mind)](https://www.emergentmind.com/topics/siglip-siglip2)
- [Best open-weight VLMs 2026 (Presenc AI)](https://presenc.ai/research/best-open-weight-vision-language-models-2026)
- [Open-source VLMs guide (BentoML)](https://www.bentoml.com/blog/multimodal-ai-a-guide-to-open-source-vision-language-models)
- [Deploy VLMs on GPU cloud 2026 (Spheron)](https://www.spheron.network/blog/deploy-vision-language-models-gpu-cloud/)
- [DINOv2 (Meta AI)](https://ai.meta.com/blog/dino-v2-computer-vision-self-supervised-learning/)
