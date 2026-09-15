# 122 — Generar imágenes para video: cuál modelo está habilitado, referencias y la prohibición del texto

## Por qué el editor genera imágenes

Porque **la imagen fija es el punto de control**. Un video generado no lo puedes corregir: sale como
sale. Una imagen fija sí: la ves, la juzgas, la retocas, le fuerzas el color, y solo cuando ya está
buena la mandas a animar.

Los tres usos reales:

1. **El fotograma cero.** La imagen que le pasas a Veo como referencia (módulo `121`). Si esa imagen
   está on-brand, el video sale on-brand. Si está mal, el video está mal antes de empezar.
2. **Placas y fondos.** Fondos para texto, cartones de cierre, texturas, planos de apoyo que no
   necesitan moverse.
3. **B-roll estático con movimiento falso.** Una imagen buena con un empuje lento de 4 segundos en
   post es más barata, más fiel y muchas veces mejor que un plano generado de verdad.

---

## ⚠️ Lo primero: NO asumas qué modelo tienes habilitado

Esta es la lección más cara de este módulo, verificada en un proyecto real de Vertex en agosto de
2026:

> **Los modelos de imagen habilitados varían por proyecto de Google Cloud.**
> En un proyecto real, el único que respondía era `gemini-2.5-flash-image`.
> `gemini-3-pro-image`, `imagen-3` e `imagen-4` devolvían **404**.

Que un modelo exista, esté anunciado en el blog de Google y aparezca en la documentación **no
significa que tu proyecto lo tenga**. La habilitación depende de la región, del tipo de cuenta, de
la lista de espera del modelo y de decisiones de Google que no te explican.

Un 404 en Vertex no siempre significa "no existe". Muchas veces significa "no para ti, todavía".

### La sonda: cómo saber cuál tienes, en 2 minutos

Antes de escribir una sola línea del flujo de producción, corre esta prueba. Un prompt tonto, una
imagen, por cada modelo candidato:

```bash
#!/usr/bin/env bash
PROY="tu-proyecto"
REG="us-central1"
TOKEN="$(gcloud auth print-access-token)"

for M in gemini-3-pro-image gemini-2.5-flash-image imagen-4.0-generate-001 imagen-3.0-generate-002; do
  echo "── probando: $M"
  curl -s -o /dev/null -w "  HTTP %{http_code}\n" \
    -X POST \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    "https://${REG}-aiplatform.googleapis.com/v1/projects/${PROY}/locations/${REG}/publishers/google/models/${M}:generateContent" \
    -d '{"contents":[{"role":"user","parts":[{"text":"una manzana roja sobre fondo blanco"}]}]}'
done
```

Cómo se leen los códigos:

| Código | Qué significa | Qué haces |
|---|---|---|
| **200** | Está habilitado. Ese es tu modelo. | Úsalo |
| **404** | No disponible en este proyecto/región | Prueba otra región o pasa al siguiente |
| **403** | Existe pero no tienes permiso / falta habilitar la API | Habilita `aiplatform.googleapis.com`, revisa el rol |
| **400** | Existe y responde, pero el cuerpo está mal | Ese modelo **sí sirve**, arregla el JSON |

Ojo con el detalle del método: los modelos **Gemini-imagen** responden a `generateContent`; los
**Imagen** clásicos responden a `:predict` con otro cuerpo. Si pruebas un Imagen con el cuerpo de
Gemini vas a ver un 400 que parece un fallo y no lo es.

**Escribe el resultado de esta sonda en el README del proyecto.** Dentro de dos meses, cuando algo
falle, la primera pregunta va a ser exactamente esta.

---

## El panorama de modelos de imagen (agosto 2026)

Verificado por búsqueda a la fecha; los precios se mueven, confírmalos en la página oficial.

| Modelo | Precio aprox./imagen | Para qué |
|---|---|---|
| **Imagen 4 Fast** | ~$0.02 | Lo más barato con calidad de producción. Volumen, pruebas, fondos |
| **Imagen 4** (normal/Ultra) | intermedio | Fotografía de producto, texturas |
| **Gemini 2.5 Flash Image** | bajo | Rápido, multimodal, entiende bien referencias. Es el que muchas veces está habilitado por defecto |
| **Gemini 3 Pro Image** | ~$0.134 a 1K/2K, ~$0.24 a 4K | El bueno. Mejor seguimiento de instrucciones y mejor con texto |
| **Grok Imagine** (xAI) | ~$0.02 | Alternativa barata fuera de Google |

Dos datos que sí valen plata:

- **Gemini 3 Pro Image cobra ~560 tokens por cada imagen que le mandas de entrada.** Si le pasas seis
  referencias, eso se nota en la factura.
- **La Batch API de Google corta el precio exactamente a la mitad** si aguantas una ventana de hasta
  24 horas. Para generar 200 fondos de una campaña, es plata regalada no usarla.

---

## Cómo se le pide una imagen que sirva para video

### La regla del fotograma, no del cuadro

Una imagen para redes sociales se compone para que se vea bien quieta. Una imagen que va a ser
**fotograma cero de un video** se compone para que tenga **a dónde moverse**.

Eso significa:

- **Deja aire.** Si el sujeto está pegado al borde, la cámara no tiene para dónde ir.
- **Compón en la relación final.** 9:16 si va a vertical, 16:9 si va a horizontal. No generes
  cuadrado y recortes: el modelo compone para el marco que le des, y recortar destruye la
  composición.
- **Que haya profundidad.** Un fondo plano no se puede animar; un fondo con planos (primer término,
  sujeto, fondo) sí. El paralaje sale gratis.
- **Un solo foco de atención.** El video te da 2 segundos; dos focos es ninguno.

### El prompt que funciona

Estructura, de más importante a menos:

```
[SUJETO concreto] + [ACCIÓN o pose] + [ENCUADRE y lente] + [LUZ] + [SUPERFICIE/ENTORNO] +
[PALETA con nombres de color o códigos] + [PROHIBICIONES]
```

Ejemplo real:

```
Frasco ámbar de 60 ml, de pie, ligeramente descentrado a la izquierda.
Plano cerrado, lente 85 mm, profundidad de campo corta, el fondo desenfocado.
Luz suave lateral desde la izquierda, sombra larga hacia la derecha.
Superficie de piedra oscura mate. Fondo azul marino profundo (#0B1E3A), liso.
Vertical 9:16, aire arriba para poner texto.
Absolutely no text, no letters, no words, no logos, no watermarks, no packaging labels.
```

---

## 🚫 La prohibición del texto: obligatoria, siempre

**Los modelos de imagen escriben texto deformado.** En 2026 mejoró mucho —Gemini 3 Pro Image es
notablemente mejor— pero sigue siendo verdad para el resto, y sigue apareciendo texto donde no lo
pediste: en etiquetas, en letreros de fondo, en pantallas, en empaques.

Y hay algo peor que un texto feo: un texto feo **con la marca mal escrita**. "GASTROLATAM" con dos
T y una A al revés en una pieza de cliente es un problema serio.

La solución no es pedirle que escriba mejor. La solución es esta, en dos partes:

**1. Prohíbeselo explícitamente, en inglés, redundante:**

```
absolutely no text, no letters, no words, no numbers, no logos, no watermarks,
no signage, no labels, no captions, no subtitles, no UI
```

Sí, es redundante a propósito. Los modelos responden mejor a la prohibición repetida en varias
formas que a una sola frase elegante. Y en inglés funciona mejor que en español aunque el resto del
prompt esté en español: los modelos están entrenados con etiquetas en inglés.

**2. Pon el texto después, con tipografía real.**

En post, con la fuente de la marca, con el interletrado correcto, con el color exacto, y sobre todo:
**editable**. Cuando el cliente pida cambiar "20%" por "25%", cambias una capa de texto en cinco
segundos en vez de regenerar la imagen y pagarla otra vez.

Esta regla no tiene excepciones. **El texto de una pieza profesional nunca lo escribe un modelo de
imagen.**

---

## Referencias de estilo: el atajo que sí funciona

Los modelos Gemini de imagen aceptan **imágenes de entrada** junto con el prompt. Eso cambia todo.

En vez de describir tu marca con adjetivos —"retro, cálido, artesanal, con textura de papel"— le
pasas **el archivo real de tu marca** y le dices "este estilo".

La diferencia, verificada en prueba real, **es abismal**: describir "estilo retro cartoon" te da
cualquier cosa que el modelo entienda por retro cartoon; pasarle el diseño real de la marca te da
algo on-brand a la primera. Esto está desarrollado en el módulo `126` y es probablemente la lección
más útil de toda esta serie.

Cuerpo de la petición, en la forma que funciona:

```jsonc
{
  "contents": [{
    "role": "user",
    "parts": [
      { "inlineData": { "mimeType": "image/png", "data": "<base64 de tu diseño>" } },
      { "text": "Genera una nueva escena EN ESTE MISMO ESTILO gráfico, mismos colores exactos, mismo trazo. Sujeto: [...]. Absolutely no text, no letters, no words." }
    ]
  }]
}
```

Cuántas referencias: **de una a tres**. Con una controlas el estilo. Con dos o tres refuerzas lo que
tienen en común. Con seis, el modelo promedia y te devuelve barro. Y recuerda que cada imagen de
entrada se cobra.

---

## Relación de aspecto

Pídela explícitamente y en el mismo marco en que vas a trabajar.

| Formato | Uso |
|---|---|
| **9:16** | Reels, TikTok, Shorts, estados |
| **1:1** | Feed cuadrado, miniaturas |
| **16:9** | YouTube, TV, presentaciones |
| **4:5** | Feed vertical de Instagram (el que más ocupa pantalla) |

Dos advertencias:

- **No generes 16:9 para recortar a 9:16.** Pierdes la mitad de la imagen y toda la composición.
  Genera en el marco final.
- Si necesitas **la misma escena en dos formatos**, genera dos veces con el mismo prompt y la misma
  referencia, no recortes. Cuesta el doble y se ve el triple de bien.

Y si la imagen va a ser fotograma cero de Veo: **misma relación que el video**, sin excepción
(módulo `121`).

---

## Transparencia (PNG con alfa)

La pregunta que siempre aparece: "¿puedo pedirle un producto recortado, con fondo transparente, para
componer encima?"

La respuesta honesta a agosto de 2026: **depende del modelo y no te fíes.** Algunos modelos y
algunas herramientas ofrecen salida con canal alfa; muchos endpoints de Vertex devuelven PNG opaco
aunque pidas "fondo transparente" —te dan un fondo blanco o gris muy convincente que **no** es
transparencia.

Verifícalo tú, no lo asumas:

```bash
# ¿tiene canal alfa de verdad?
ffprobe -v error -select_streams v:0 -show_entries stream=pix_fmt -of csv=p=0 imagen.png
# rgba / rgba64be → sí tiene alfa
# rgb24 / rgb48be → NO tiene alfa, aunque se vea "transparente"
```

El flujo que sí funciona siempre, sin depender de nadie:

1. Pide la imagen sobre un **fondo liso y muy contrastado** con el sujeto (verde puro, magenta puro).
   Nunca sobre blanco si el producto es claro.
2. Recorta en post: con una herramienta de segmentación, o directamente en ffmpeg con `colorkey`
   para fondos planos:

```bash
ffmpeg -i producto.png -vf "colorkey=0x00FF00:0.30:0.10" -c:a copy producto_alfa.png
```

3. Revisa los bordes. El derrame de color del fondo sobre el borde del sujeto (el halo verde) es el
   detalle que delata el trabajo amateur. Se arregla reduciendo la tolerancia y con un `despill`
   manual.

---

## Cuándo NO generes la imagen

Sé honesto con esto, porque ahorra plata y sale mejor:

- **Si el producto es real y lo tienes**, fotografíalo. Una foto de celular con luz de ventana le
  gana a cualquier generación, y es tu producto de verdad, no una versión inventada.
- **Si es el logo**, úsalo. Nunca lo regeneres. Jamás.
- **Si es un fondo liso o un degradado**, hazlo en CSS, en ffmpeg o en cualquier editor. Gratis,
  exacto, en el color correcto.
- **Si necesitas el color exacto de la marca**, haz la base en post y usa la generación solo para la
  textura. El modelo no te va a dar tu azul (módulo `125`).

---

## Errores comunes

- **Asumir que un modelo está habilitado porque existe.** En un proyecto real solo respondía
  `gemini-2.5-flash-image`; `gemini-3-pro-image`, `imagen-3` e `imagen-4` daban 404.
- **Leer un 404 como "el modelo no existe".** Muchas veces es "no en este proyecto/región".
- **Probar un modelo Imagen con el cuerpo de Gemini** (o al revés) y concluir que está roto. Imagen
  usa `:predict`; los Gemini de imagen usan `generateContent`.
- **No prohibir el texto.** Vas a recibir letreros deformados y la marca mal escrita.
- **Prohibir el texto solo en español.** Ponlo en inglés, redundante, aunque el prompt esté en
  español.
- **Dejar que el modelo escriba el titular.** El texto va en post, con tipografía real y editable.
- **Generar 16:9 para recortar a 9:16.** Destruyes la composición y pagas por píxeles que tiras.
- **Pasarle seis imágenes de referencia.** Promedia y sale barro. Y cada entrada se cobra.
- **Creer que "fondo transparente" en el prompt produce alfa.** Verifica con `ffprobe`; casi siempre
  es un fondo opaco muy bien hecho.
- **Componer un fotograma sin aire.** Si el sujeto toca los bordes, no hay movimiento de cámara
  posible después.
- **Generar en tiempo real lo que podía ir por Batch.** La mitad de precio por esperar unas horas.
- **Regenerar la imagen entera para cambiar un número.** Eso pasa por haber dejado el texto adentro.

---

## Checklist

- [ ] Corrí la **sonda de modelos** y sé exactamente cuál está habilitado en este proyecto y región
- [ ] Anoté el resultado de la sonda en el README del proyecto
- [ ] Usé el **método correcto** para la familia del modelo (`generateContent` vs `:predict`)
- [ ] El prompt prohíbe texto **explícitamente y en inglés**, de forma redundante
- [ ] El texto de la pieza va **después**, con tipografía real y capa editable
- [ ] Generé en la **relación de aspecto final**, sin planes de recortar
- [ ] Si es fotograma cero de Veo: misma relación que el video, sin canal alfa
- [ ] La composición **deja aire** para que la cámara tenga a dónde moverse
- [ ] Pasé de 1 a 3 imágenes de referencia de marca, no más
- [ ] Si necesitaba transparencia, la **verifiqué con `ffprobe`** en vez de asumirla
- [ ] Consideré si esto se resolvía con una foto real, el logo original o un degradado gratis
- [ ] Si eran muchas imágenes, evalué la **Batch API** (mitad de precio)
- [ ] Guardé prompt, referencias y modelo usado junto al archivo
