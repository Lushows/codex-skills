# 265 · Prompt enhancement con LLM (expandir antes de generar)

> El usuario escribe "un perro"; el modelo de imagen necesita "golden retriever, golden hour, 85mm, bokeh, film grain".
> Un LLM barato entre el input y la GPU sube calidad y tapa el gap entre lo que el humano dice y lo que el modelo entiende.

## Por qué meter un LLM antes del modelo visual
Los modelos de difusión/video responden a prompts **densos y descriptivos**; los usuarios escriben vago y
corto. Un LLM (Claude Haiku/Sonnet barato) reescribe el prompt pobre en uno rico: añade estilo, iluminación,
cámara, composición, calidad. Resultado: menos re-rolls (menos GPU quemada), output consistente, y entrada
para usuarios no expertos. Es el equivalente automatizado de la dirección de arte de [[46-direccion-arte-imagenes-ia]].

## Qué hace el enhancer (más allá de "hazlo más largo")
- **Expandir**: detalle visual concreto (sujeto, entorno, luz, lente, paleta, mood).
- **Estructurar** al formato del modelo destino: SDXL quiere tags densos; un modelo de video quiere acción
  temporal ("la cámara hace dolly-in mientras…"); cada modelo tiene su dialecto.
- **Traducir**: input en español → prompt en inglés (mejor cobertura de la mayoría de checkpoints).
- **Negative prompt** auto: añade lo que conviene excluir (`blurry, extra fingers, watermark`).
- **Inyectar estilo de marca**: en STUDIO multi-marca, prepende la guía de cada cliente (paleta, do/don't).
- **Respetar la intención**: NO inventar sujetos que el usuario no pidió. Enriquecer ≠ secuestrar.

## Cómo: prompt de sistema + structured output
LLM con system prompt que fija reglas y few-shots del estilo deseado, devolviendo **JSON estructurado** (no
prosa) para parsear sin ambigüedad:

```json
{ "prompt": "...", "negative_prompt": "...", "aspect_ratio": "16:9",
  "style_tags": ["cinematic","golden-hour"], "rejected": false, "reason": null }
```

Few-shot con pares (input pobre → output rico) ancla la calidad mejor que instrucciones abstractas. Cruza con
[[34-prompt-engineering-llm]] para el diseño del system prompt y el formato de salida.

## Doble función: calidad Y seguridad (el gate barato)
El mismo paso filtra antes de gastar GPU. El LLM detecta y **rechaza/sanea** intentos de generar NSFW, menores,
deepfakes de personas reales, marcas registradas, violencia. Marca `rejected:true` con razón → no se encola el
job, no se quema GPU, y tienes log auditable. Es una **primera capa barata** (texto), NO la única: el output
visual igual pasa por moderación post-generación en [[165-moderacion-safety-output-generado]] (un prompt limpio
puede producir algo que no lo es).

## Determinismo, control y latencia
- **Que sea opcional/visible**: muestra el prompt mejorado y deja **editarlo** o desactivar el enhancer. Usuarios
  pro odian que les cambien el prompt en silencio. Guarda `prompt` y `enhanced_prompt` por separado
  ([[263-asset-gallery-management.md]]) para reproducir.
- **Temperatura baja** (0–0.4): enhancement consistente, no creativo errático. Para variaciones, sube temp a
  propósito y cachea por (input, modelo).
- **Latencia**: añade 0.5-2s antes de la GPU; despreciable frente a un job de minutos, pero **cachea** inputs
  repetidos. Usa el modelo LLM más barato que dé calidad (Haiku); no necesitas el grande aquí.
- **Modelo correcto**: confirma id/precios antes de cablear → consulta [[claude-api]]; no asumas de memoria.

## Errores que muerden
- Reescribir el prompt y NO mostrarlo → el usuario no entiende por qué salió otra cosa; pierdes confianza.
- Temperatura alta → el mismo input da prompts dispares; imposible iterar.
- Confiar el enhancer como ÚNICO control de seguridad → texto limpio, imagen sucia; falta el gate de output.
- No guardar el enhanced_prompt → no puedes reproducir ni debuggear "¿por qué salió esto?".
- Enhancer que ignora el aspect ratio/params explícitos del usuario y los sobreescribe.

Cruza con [[34-prompt-engineering-llm]] y [[46-direccion-arte-imagenes-ia]].
