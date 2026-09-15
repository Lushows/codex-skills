# 226 · Output estructurado y function-calling sobre imagen (JSON garantizado)

> "Devuélveme JSON" en el prompt falla en producción: el VLM se desvía, mete prosa, rompe el parser.
> La decodificación restringida hace el JSON inviolable a nivel de tokens — no a nivel de súplica.

## El problema y la solución real
Pedir formato por prompt ([[34-prompt-engineering-llm]]) ayuda pero no garantiza: un VLM puede
empezar con "Claro, aquí está:", omitir comillas o alucinar un campo. La **decodificación
restringida** (constrained/guided decoding) calcula en cada paso qué tokens mantienen la salida
válida contra un schema y **enmascara el resto** → es imposible producir JSON inválido. Esto aplica
igual a entrada multimodal: el modelo *mira la imagen* y el decoder *garantiza la forma* de la salida.

## Cómo se pide en vLLM
Sobre el VLM servido ([[222-vllm-multimodal-vlm]]), añades el schema a la request — la imagen va como
siempre en `image_url`:

```python
r = client.chat.completions.create(
  model="Qwen/Qwen3-VL-8B-Instruct",
  messages=[{"role":"user","content":[
    {"type":"image_url","image_url":{"url":f"data:image/jpeg;base64,{b64}"}},
    {"type":"text","text":"Extrae los campos de esta factura."}]}],
  extra_body={"guided_json": {
    "type":"object",
    "properties":{
      "total":{"type":"number"},
      "moneda":{"type":"string","enum":["COP","USD"]},
      "items":{"type":"array","items":{"type":"string"}},
      "es_factura":{"type":"boolean"}},
    "required":["es_factura","total"]}})
```

Variantes: `guided_choice` (enum cerrado, perfecto para moderación sí/no), `guided_regex` (formatos
tipo placa/fecha), `guided_grammar` (EBNF para salidas complejas).

## Backends: xgrammar es el default 2026
- **xgrammar**: JIT-compilado, autómata de pila (PDA), el más rápido para casi cualquier schema;
  default recomendado en vLLM 2026. SGLang decodifica JSON ~3× más rápido que generación libre
  ([[223-sglang-lmdeploy-serving]]).
- **outlines** / **lm-format-enforcer**: alternativas; outlines cubre regex/EBNF amplios.
Overhead casi nulo con xgrammar → no hay excusa para parsear texto libre en producción.

## Function-calling sobre imagen
El mismo mecanismo habilita tool-use visual: defines herramientas (JSON schema de argumentos) y el
VLM, viendo la imagen, **emite la llamada estructurada**. Casos: "detecta el producto y llama a
`buscar_catalogo(sku)`", "si la imagen tiene texto, llama a `ocr_region(bbox)`". xgrammar ya cubre
function-calling como generación guiada por schema y avanza hacia reemplazar los tool-parsers de
Python. El VLM se vuelve un **router multimodal**: imagen entra → acción tipada sale.

## Dónde encaja en el pipeline visual
- **Moderación/QA** ([[225-vlm-captioning-moderation-deep]]): flags y scores como JSON garantizado →
  el gate del pipeline nunca se rompe por parseo.
- **Extracción documental**: factura/cédula/etiqueta → objeto tipado directo a tu DB.
- **Grounding tipado**: bounding boxes como arrays de números válidos, no texto a regexear.

## Gotchas
1. **El schema no garantiza la verdad, solo la forma**: el VLM puede rellenar un `total` válido pero
   inventado. Constrained decoding evita el JSON roto, no la alucinación — valida valores críticos.
2. **Schemas enormes ralentizan**: gramáticas con cientos de propiedades aumentan el overhead de
   compilación; mantén el schema mínimo necesario.
3. **`required` + `enum` te ahorran lógica**: fuerza los campos obligatorios y cierra los valores
   categóricos en el schema en vez de validar después.
4. **El prompt sigue importando**: restringir la salida no sustituye un buen prompt ([[34-prompt-engineering-llm]]);
   un prompt vago llena los campos con basura bien formada.
5. **Imagen ambigua → campos vacíos, no error**: añade un booleano tipo `es_factura`/`legible` al
   schema para que el modelo declare "no aplica" en vez de inventar.

Cruza con [[34-prompt-engineering-llm]] y [[222-vllm-multimodal-vlm]].
