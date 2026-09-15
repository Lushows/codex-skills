# 121 — Generar video con Veo: parámetros, la trampa del rechazo en seco y cuándo vale la pena

## Qué es y por dónde se entra

**Veo 3.1** es el modelo de video de Google. A agosto de 2026 el identificador que usamos en
producción es:

```
veo-3.1-generate-001
```

Hay tres puertas para llegar:

| Puerta | Cuándo | Nota |
|---|---|---|
| **Vertex AI** (Google Cloud) | Producción, facturación por proyecto, control de cuotas | Es la que documenta este módulo |
| **API de Gemini** | Prototipo rápido con una API key | Parámetros parecidos, no idénticos |
| **Flow / Higgsfield** | Explorar sin código | No sirve para automatizar |

Vertex funciona por **operación de larga duración**: mandas la petición, te devuelve el nombre de
una operación, y tú preguntas cada tantos segundos si ya terminó. Un clip tarda del orden de uno a
varios minutos. No es una llamada síncrona; si tu código espera respuesta inmediata, está mal
escrito.

---

## Los dos modos de generación

### 1. Texto → video

Le describes el plano y él lo inventa completo. Máximo control creativo, mínimo control de marca.

### 2. Imagen de referencia → video

Le pasas una imagen (tu diseño, tu producto, tu personaje, un fotograma) y él la anima. **Este es el
modo que de verdad sirve para trabajo de marca**, y es el que tiene la trampa que explico abajo.

Verificado en pruebas reales de agosto de 2026: **los dos modos funcionan**. El de imagen de
referencia funciona *si y solo si* respetas la combinación de parámetros.

---

## ⚠️ LA TRAMPA CRÍTICA: el rechazo en seco

Esto es lo más importante del módulo y lo que te va a ahorrar una tarde entera.

**Cuando le pasas una imagen de referencia, Veo 3.1 rechaza la petición EN SECO si le mandas
`resolution`, `enhancePrompt: false` o `negativePrompt`.**

"En seco" significa literalmente esto:

- **No** hay error HTTP. Te responde 200.
- **No** hay mensaje de error.
- **No** hay razón de bloqueo, ni aviso de política, ni nada.
- La operación **termina bien** y el campo `response` viene **vacío**.

Es el peor tipo de fallo que existe: el que parece éxito. Vas a asumir que tu código tiene un bug de
parseo, vas a revisar el JSON tres veces, vas a cambiar la imagen, y no es nada de eso.

### La combinación que NO funciona

```jsonc
{
  "instances": [{
    "prompt": "el frasco gira lentamente sobre fondo azul marino",
    "image": { "bytesBase64Encoded": "...", "mimeType": "image/png" }
  }],
  "parameters": {
    "durationSeconds": 6,
    "resolution": "1080p",          // ❌ con imagen → rechazo en seco
    "enhancePrompt": false,          // ❌ con imagen → rechazo en seco
    "negativePrompt": "texto, letras" // ❌ con imagen → rechazo en seco
  }
}
```

Resultado: `response` vacío, sin explicación. Cero pistas.

### La combinación que SÍ funciona

```jsonc
{
  "instances": [{
    "prompt": "el frasco gira lentamente sobre fondo azul marino",
    "image": { "bytesBase64Encoded": "...", "mimeType": "image/png" }
  }],
  "parameters": {
    "durationSeconds": 6,
    "aspectRatio": "9:16",
    "sampleCount": 1
  }
}
```

Quita los tres. Ya. Funciona.

### Qué obtienes cuando no pides resolución

Salida verificada: **720 × 1280 a 24 fps**. Es decir, vertical HD a cadencia de cine.

Para redes eso está bien. Para una pieza que va a proyector o TV, 720 de ancho se nota. Si necesitas
más resolución con imagen de referencia, tienes dos caminos honestos:

1. **Escalar en post** (ffmpeg con `lanczos`, o un upscaler). Recuperas píxeles, no detalle.
2. **Generar sin imagen de referencia** con `resolution` alta, y pagar el precio de perder fidelidad
   a tu diseño.

No hay un tercer camino mágico. Si alguien te dice que sí, que te muestre el JSON.

### La regla que te llevas

> **Con imagen de referencia: prompt + duración + relación de aspecto. Nada más.**
> Cada parámetro extra que agregues es un candidato a matarte la petición en silencio.

---

## Los parámetros, uno por uno

### `prompt` — obligatorio

Texto libre. Veo entiende lenguaje de cámara de verdad. Compara:

```
❌ "un frasco de producto bonito"
✅ "plano cerrado de un frasco ámbar sobre superficie de mármol, cámara en dolly lateral
   lento de izquierda a derecha, luz suave desde la ventana a la izquierda,
   profundidad de campo corta, 50 mm"
```

Lo que entiende bien: tipo de plano (cerrado, medio, general), movimiento de cámara (dolly, travelling,
grúa, estático), lente (35 mm, 85 mm), dirección y calidad de luz, hora del día, textura de la
superficie.

Lo que **no** entiende bien: paletas de color exactas (ver módulo `125`), texto en pantalla (ver
módulo `122`), y cualquier cosa que dependa de una identidad de marca descrita con adjetivos (ver
módulo `126`).

### `image` — la referencia

Se manda como base64 (`bytesBase64Encoded` + `mimeType`) o como URI de Cloud Storage. Consejos de
producción:

- **PNG sin transparencia.** El canal alfa confunde; aplánalo contra el fondo que quieres.
- **Misma relación de aspecto que la salida.** Si vas a 9:16, pásale una imagen 9:16. Si le pasas
  cuadrada y pides vertical, él inventa los bordes y ahí es donde deriva.
- **Que la imagen ya sea el plano.** No le pases un moodboard esperando que "se inspire". La imagen
  es el fotograma cero, no una sugerencia.

### `durationSeconds`

Rango típico de 4 a 8 segundos. Cada segundo cuesta plata (abajo).

**La decisión de duración es económica, no creativa.** Genera exactamente lo que vas a usar más un
colchón de medio segundo por cada punta para tener dónde cortar. Generar 8 para usar 2 es tirar 6
segundos de presupuesto.

### `aspectRatio`

`"16:9"` o `"9:16"`. Ponlo siempre, explícitamente. El valor por defecto cambia entre versiones y
no quieres descubrirlo en la entrega.

### `resolution`

`"720p"` / `"1080p"` (y 4K en algunas variantes, más caro).

⚠️ **Solo en texto→video.** Con imagen de referencia, no lo mandes.

### `generateAudio`

Booleano. **Es la palanca de costo más grande que tienes.** Con audio, el mismo clip puede costar
4× más que sin audio.

Regla práctica: **b-roll sin audio, siempre.** El b-roll va debajo de tu voz en off y tu música; el
audio que genere Veo lo vas a silenciar de todos modos. Solo pide audio cuando el plano tiene un
personaje hablando y necesitas la sincronía labial.

### `negativePrompt`

Lo que NO quieres ver. Útil en texto→video para prohibir texto deformado:

```
"text, letters, words, watermark, logo, subtitles, captions"
```

⚠️ **No lo mandes con imagen de referencia.** Rechazo en seco.

### `enhancePrompt`

Por defecto está en `true`: Google reescribe tu prompt para mejorarlo antes de generar. En
texto→video, ponerlo en `false` te da control literal (bueno cuando el prompt ya está muy afinado).

⚠️ **No lo mandes en `false` con imagen de referencia.** Rechazo en seco. Y ojo: mandarlo en `true`
explícitamente también es mandar el parámetro. Con imagen, **omítelo**.

### `seed`

Número entero. Con la misma semilla, el mismo prompt y los mismos parámetros, obtienes un resultado
reproducible o casi.

Para qué sirve de verdad:

- **Iterar de a un cambio.** Fijas semilla, cambias solo el movimiento de cámara, y ves qué hizo ese
  cambio y nada más.
- **Rehacer un plano que se te perdió.** Guarda la semilla junto al clip. Siempre.
- **Familia de planos coherentes.** Misma semilla, prompts hermanos.

No confíes en que sea determinismo perfecto entre versiones del modelo. Es reproducibilidad
práctica, no garantía contractual.

### `sampleCount`

Cuántas variantes genera de una vez. **Multiplica el costo por ese número.** `2` es un buen punto:
te da opción sin duplicar la factura tres veces.

### `personGeneration`

Controla si puede generar personas y de qué tipo. Los valores y las restricciones cambian por región
y por si estás en texto→video o imagen→video. Si tu pieza lleva gente, verifícalo en la
documentación vigente antes de presupuestar, porque hay combinaciones bloqueadas.

### `storageUri`

Si le das un bucket de Cloud Storage, deja el resultado ahí en vez de devolverte base64. Para clips
de varios megas, es la opción sana.

---

## El bucle de trabajo que funciona

```
1. Diseña el fotograma cero (módulo 122) — imagen fija, on-brand, sin texto
2. Genera con Veo: imagen de referencia + prompt + duración + aspecto. NADA MÁS.
3. Mira el resultado con ojo de editor, no de padre orgulloso:
   ¿el color derivó? ¿apareció texto? ¿la física es creíble? ¿sirve el movimiento?
4. Si derivó el color → NO lo vuelvas a pedir. Fuérzalo en post (módulo 125).
5. Si el movimiento no sirve → fija semilla, cambia SOLO la frase de cámara, repite.
6. Guarda junto al clip: prompt, semilla, parámetros y la imagen de referencia.
```

Ese último paso es el que separa a un profesional de alguien jugando. Sin el registro, dentro de tres
semanas no puedes rehacer nada.

---

## Costos: cuándo vale la pena y cuándo no

Precios de Vertex a agosto de 2026, aproximados y **verificables en la página oficial**:

| Variante | Aprox. USD/segundo |
|---|---|
| Lite, 720p, sin audio | ~$0.03 |
| Lite, 720p | ~$0.05 |
| Fast, 720p | ~$0.10 |
| Estándar, 720p/1080p, con audio | ~$0.40 |
| 4K | ~$0.30–$0.60 |

Un clip de 8 segundos con audio en la variante buena: **~$6 USD**. Ese es el número que tienes que
tener en la cabeza.

### La conclusión dura, de prueba real

**Para un puente de menos de 1 segundo, Veo NO vale la pena.**

Lo probamos: para tapar un salto de menos de un segundo entre dos diseños fijos, generar con Veo
significa (a) pagar el mínimo de duración completo aunque uses 0.8 s, (b) **perder fidelidad al
dibujo original** —el modelo reinterpreta tu diseño—, y (c) bajar de resolución respecto al PNG
original.

Para eso tienes alternativas más baratas y más fieles:
- una transición hecha en ffmpeg (`xfade`, desenfoque de movimiento, empuje),
- un morph entre dos imágenes fijas con Pika (Pikaframes),
- o simplemente un corte seco, que muchas veces es mejor decisión de montaje que el puente.

**Para un plano protagonista sí vale la pena.** El plano donde el producto gira, donde alguien
habla, donde el espectador se queda mirando 3 segundos: ahí los $2 o $6 están bien gastados.

Regla: **paga Veo por los planos que la gente mira; no pagues Veo por los planos que la gente pasa.**

---

## Diagnóstico rápido de fallos

| Síntoma | Causa más probable | Qué haces |
|---|---|---|
| `response` vacío, sin error, con imagen | `resolution`, `enhancePrompt:false` o `negativePrompt` presentes | Quítalos los tres |
| `response` vacío, sin error, sin imagen | Filtro de seguridad silencioso, o parámetro no soportado por esa variante | Simplifica el prompt al mínimo y vuelve a agregar de a uno |
| Sale 720×1280 y querías 1080 | No pediste `resolution` (o no podías, por la imagen) | Escala en post, o replantea a texto→video |
| Sale texto deformado en el plano | El modelo escribe cuando el prompt sugiere signos, letreros o pantallas | `negativePrompt` (solo texto→video) y texto real en post |
| Los colores no son los de la marca | Comportamiento normal del modelo, no es tu culpa | Módulo `125`: fuerza en post |
| 429 | Cuota | Módulo `127`: espera con retroceso, no reintentes en bucle |
| Tarda muchísimo | Es normal, es operación larga | Consulta cada 10–15 s, no cada segundo |

---

## Errores comunes

- **Mandar `resolution` con imagen de referencia.** Es el error #1 y no te avisa. `response` vacío.
- **Mandar `enhancePrompt: false` con imagen de referencia.** Mismo resultado silencioso.
- **Mandar `negativePrompt` con imagen de referencia.** Mismo resultado silencioso.
- **Asumir que `response` vacío es un bug de tu código.** Revisas el parseo 40 minutos y el problema
  estaba en el request.
- **Pedir audio para b-roll.** Multiplicas la factura por un audio que vas a silenciar.
- **Generar 8 segundos para usar 2.** Pagaste 8.
- **No guardar la semilla.** Ese plano que te encantó no lo vuelves a sacar.
- **Usar Veo para puentes de menos de un segundo.** Caro, menos fiel al dibujo y de menor
  resolución que la imagen de la que partiste.
- **Pasarle un moodboard como imagen de referencia.** La imagen es el fotograma cero, no una
  inspiración.
- **Reintentar en bucle contra un 429.** Te bloqueas más y quemas cuota.
- **Esperar respuesta síncrona.** Es operación de larga duración; tu código tiene que consultar.
- **Pelear con el modelo por el color.** Nunca lo vas a ganar. Se gana en post.

---

## Checklist

- [ ] Sé si este plano es **texto→video** o **imagen de referencia** antes de escribir el request
- [ ] Si lleva imagen de referencia: **NO** mandé `resolution`, **NO** mandé `enhancePrompt`, **NO**
      mandé `negativePrompt`
- [ ] Puse `aspectRatio` explícito
- [ ] La imagen de referencia tiene **la misma relación de aspecto** que la salida y no tiene alfa
- [ ] `generateAudio` está **apagado** salvo que el plano lleve voz sincronizada
- [ ] `durationSeconds` es lo que voy a usar + medio segundo por punta, no más
- [ ] Fijé y **guardé** la semilla junto al clip
- [ ] Guardé prompt, parámetros e imagen de referencia en la carpeta del proyecto
- [ ] Calculé el costo del plano **antes** de generarlo (segundos × tarifa × sampleCount)
- [ ] Si el plano dura menos de un segundo, evalué si un `xfade` o un corte seco resuelve mejor
- [ ] Mi código trata `response` vacío como **fallo de parámetros**, no como éxito
- [ ] Mi código maneja la operación como asíncrona con consultas espaciadas y retroceso ante 429
