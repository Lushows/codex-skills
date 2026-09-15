# 225 · VLM para auto-caption, moderación y QA de imagen a escala (batch + costo)

> Procesar millones de imágenes con un VLM es un problema de throughput y $/imagen, no de calidad
> por imagen. La palanca dominante es **qué tan pequeño puedes ir** sin romper la tarea.

## Las tres tareas y su nivel de exigencia
- **Auto-caption** (enriquecer datasets de difusión, metadatos): tolera modelos pequeños; un caption
  corto y correcto basta. Mejor candidato para SmolVLM.
- **Moderación / safety** (¿desnudez/violencia/marca/PII?): salida binaria/etiquetas → structured
  output garantizado ([[226-structured-output-vision]]); aquí un modelo medio reduce falsos positivos.
- **QA de imagen** (¿la generación cumplió el brief? defectos, manos, texto legible): la más exigente;
  necesita un VLM fuerte en grounding/OCR (Qwen3-VL, InternVL3 — ver [[35-vision-encoders-vlms]]).

## La economía: elegir tamaño es elegir costo
SmolVLM-256M usa <1GB de VRAM en inferencia → procesa volúmenes enormes a fracción del costo del 2B.
Throughput de referencia: SmolVLM ~1.5 it/s, SmolVLM2 ~2 it/s con batching [no verificado: cifras de
HF/blog, dependen de GPU y resolución]. Regla: **arranca con el modelo más pequeño que pase tu eval**
y sube solo si la métrica de la tarea cae. Un caption no necesita un 72B; un QA fino de defectos sí.

| Tarea | Modelo de partida | Subir a |
|---|---|---|
| Caption corto masivo | SmolVLM 256M/500M | SmolVLM 2.2B si alucina |
| Moderación etiquetas | SmolVLM 2.2B / Gemma3 4B | Qwen3-VL si hay matices |
| QA grounding/OCR | Qwen3-VL 8B / InternVL3 | 32B+ solo si la eval lo exige |

## El patrón de batch que escala
1. Sirve el VLM con vLLM ([[222-vllm-multimodal-vlm]]) — API OpenAI-compatible + continuous batching.
2. **Normaliza la resolución de entrada** antes de mandar: redimensiona al mínimo donde la tarea
   funcione. Los tokens visuales son lineales-ish en píxeles → bajar resolución baja costo directo.
3. Lanza muchos requests concurrentes; deja que el batching del motor llene la GPU.
4. **Idempotencia**: indexa por hash de imagen; reprocesar millones por un crash a mitad es caro.
   Guarda resultado por hash y salta los ya hechos (cruza con [[113-network-volume-modelos-grandes]]
   para cachear pesos y evitar cold starts que sangran el batch).
5. Para moderación/QA, fuerza JSON con `guided_json` → cero reintentos por parseo
   ([[226-structured-output-vision]]).

## Cálculo de $/imagen (mental)
Costo ≈ (tiempo_GPU_por_imagen × $/h_GPU). El tiempo lo fija: tamaño del modelo × tokens visuales
(resolución) ÷ batching. Por eso las dos palancas reales son **modelo más chico** y **menos píxeles**,
no la GPU más cara. Una imagen a media resolución en SmolVLM puede costar 10× menos que a full-res en
un 32B sin que el caption empeore.

## QA como gate de pipeline de generación
En un pipeline de imagen/avatar, el VLM es el **filtro post-generación**: cada salida pasa por un
prompt de política/brief con structured output (flags + score). Las que fallan se regeneran o se
mandan a revisión. Es el mismo rol que la moderación de output generado de [[165-moderacion-safety-output-generado]],
pero midiendo *fidelidad al brief* además de *seguridad*.

## Gotchas
1. **OCR no es igual en todos los VLMs**: para texto/tablas densas, un VLM general pequeño alucina;
   usa Qwen3-VL/InternVL3/Gemma3 y mídelo en OCRBench/DocVQA antes de confiar (igual que [[35-vision-encoders-vlms]]).
2. **Caption sesgado contamina el dataset**: si auto-captionas para entrenar difusión, los sesgos del
   VLM se hornean en el modelo final. Audita una muestra a mano (cruza con [[153-dataset-curation-captioning-visual]]).
3. **Resolución demasiado baja rompe QA fino**: bajar píxeles ahorra, pero defectos finos (manos,
   texto) desaparecen. Calibra la resolución por tarea, no global.
4. **Sin idempotencia, un fallo a la imagen 800k te cuesta el doble**: persiste por hash.
5. **Moderación sin structured output = parseo frágil**: texto libre se rompe; exige JSON schema.

Cruza con [[153-dataset-curation-captioning-visual]] y [[165-moderacion-safety-output-generado]].
