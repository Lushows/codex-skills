# 172 · Face-swap con InsightFace (inswapper / ReActor / Roop)

> El swap de cara más usado del open-source corre con un modelo de 264MB y da resultados decentes.
> Pero su licencia es **solo investigación no-comercial** y el output es legalmente radioactivo: léelo antes de servirlo.

## Cómo funciona (la tubería real)
1. **Detección + embedding**: InsightFace `buffalo_l` detecta la cara *fuente* y extrae un embedding de identidad (ArcFace, 512-d).
2. **Swap**: `inswapper_128.onnx` toma ese embedding + la cara *destino* y genera la cara intercambiada a **128×128** (de ahí el nombre). Ese tamaño es el cuello de botella de calidad.
3. **Pegado + restauración**: se reinserta en el frame y casi siempre pasa por un restaurador (GFPGAN/CodeFormer) para subir nitidez. Sin ese paso, la cara swapeada se ve borrosa/jabonosa.

`Roop` fue el original (abandonado); `ReActor` (`comfyui-reactor-node`) es el sucesor vivo, mismo motor pero con node de ComfyUI, batch, restauración integrada y restricción SFW.

## Calidad: por qué se ve mal y cómo subirla
- **128px**: el modelo open genera a 128 y reescala. Para HD necesitas restauración facial sí
  o sí (`[[148-face-restoration-output-avatar]]`).
- **Pose/ángulo extremo**: si destino mira de perfil, el swap colapsa. Filtra por ángulo de
  cabeza (yaw/pitch) antes de procesar.
- **Iluminación dispar**: color-match del recorte facial antes de pegar evita el efecto
  "máscara pegada". Iguala histograma/tono al frame destino.
- **Oclusiones** (manos, pelo, gafas): usa máscara facial (occlusion mask) para no swapear
  sobre lo que tapa la cara.
- **Video**: corre frame a frame → parpadeo de identidad. Aplica el mismo embedding fuente a
  todos los frames y suaviza con restauración temporal-consistente.

## Pipeline de producción (orden que funciona)
1. Detectar caras en destino (filtrar por tamaño/ángulo; descartar las que no cumplen).
2. Extraer embedding de la cara fuente **una sola vez** (cachéalo si es batch/video).
3. Swap por cara → recorte 128px.
4. Color-match + máscara de oclusión → pegar en el frame.
5. Restauración facial (CodeFormer con fidelity alto para no perder el parecido).
6. Upscale final si hace falta. No upscalees antes de restaurar: amplifica artefactos.

## Tabla: opciones del ecosistema

| Herramienta | Estado | Motor | Notas |
|---|---|---|---|
| Roop | Muerto | inswapper_128 | No usar; sin mantenimiento |
| ReActor | Activo | inswapper_128 + GFPGAN/CodeFormer | Node ComfyUI/A1111, SFW-gated |
| inswapper (haofanwang) | Activo | inswapper_128 | Script one-click + restoration |
| inswapper-512 (comercial) | Cerrado | propietario | Licencia paga vía InsightFace |

## Licencia — esto NO es negociable
Los modelos pre-entrenados de InsightFace (incl. `inswapper_128.onnx` y `buffalo_l`) son **solo para investigación no-comercial**. Para uso comercial hay que contratar licencia escribiendo a contact@insightface.ai o entrenar tu propio modelo. Servir face-swap en un producto pagado con los pesos open = violación de licencia. No lo escondas en un endpoint "privado".

## Ética y consentimiento — riesgo legal real
Face-swap = generación de **likeness** de una persona real. Implicaciones:
- **Consentimiento explícito** de la persona cuya cara se usa, por escrito. Sin eso, no hay caso de uso legítimo.
- **Deepfake**: muchas jurisdicciones (UE AI Act, leyes estatales US, etc.) exigen **etiquetado** del contenido sintético y prohíben usos no consentidos (íntimos, fraude, suplantación).
- **NSFW**: ReActor incluye filtro SFW a propósito. Quitarlo te pone en territorio de abuso (CSAM, porno no consentido) con responsabilidad penal.
- **Moderación obligatoria** en cualquier servicio que lo exponga: ver `[[165-moderacion-safety-output-generado]]`.

## Sizing y serving
- VRAM: trivial (≈2-4GB). El swap no es el costo; la restauración facial y el upscaler sí.
- ONNX Runtime con provider CUDA; cachea `buffalo_l` + `inswapper_128` en el volumen (`[[113-network-volume-modelos-grandes]]`) para matar el cold-start.

Cruza con [[173-pulid-instantid-identity]], [[148-face-restoration-output-avatar]], [[39-legal-ia-generativa]] y [[165-moderacion-safety-output-generado]].
