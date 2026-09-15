# 123 — Generar música con IA: Lyria, el método correcto y qué se le puede pedir

## Por qué esto importa para un editor

Porque la música es la mitad del video y casi siempre es la mitad peor resuelta.

Tres problemas reales que la música generada resuelve:

1. **Derechos.** La pista de librería con la que montaste puede ser reclamada, silenciada o
   desmonetizada. Una pista generada por ti no.
2. **Duración exacta.** Ninguna pista de librería dura exactamente lo que dura tu video. Terminas
   haciendo un corte tramposo o un fundido de salida que suena a rendición.
3. **Coherencia de marca.** Si la marca tiene un sonido, puedes generar veinte piezas con el mismo
   ADN sonoro. Con librería, cada pieza suena a otra empresa.

Lo que **no** resuelve: la música generada no tiene el gancho de una canción escrita por alguien. Es
excelente como cama, como fondo, como energía. Es mediocre como protagonista.

---

## Lyria: qué es y en qué versión estamos

**Lyria** es la familia de modelos de música de Google DeepMind, disponible en Vertex AI.

A agosto de 2026 el mapa es este:

| Modelo | Qué hace |
|---|---|
| **Lyria 3** | Pistas de hasta ~30 segundos. Para prototipar, social, stingers |
| **Lyria 3 Pro** | Composiciones completas de hasta ~3 minutos, con estructura real (intro, verso, coro, puente) |
| **Lyria 3.5** | Anunciado el 29 de julio de 2026, con mejor voz y letra. Salió primero dentro de Google Flow Music; verifica su disponibilidad en API antes de contar con él |

El identificador que usamos y verificamos en producción:

```
lyria-3-pro-preview
```

La palabra `preview` en el nombre no es decorativa: significa que puede cambiar, que puede tener
cuotas más estrechas y que no tienes garantía de servicio. Para trabajo de cliente, ten un plan B.

---

## ⚠️ El método correcto: `generateContent`, no `predict`

Esta es la trampa técnica del módulo, verificada en pruebas reales:

> **Lyria se llama con `generateContent` y `responseModalities: ['AUDIO']`.**
> **NO con `:predict`.**

Es contraintuitivo, porque el resto de los modelos de medios de Vertex (Imagen, Veo) usan
`:predict` o `:predictLongRunning`. Lyria no. Lyria se comporta como un modelo Gemini: conversación
de entrada, modalidad de salida declarada.

Si intentas `:predict` vas a recibir un error que no dice "usaste el método equivocado", sino algo
sobre el formato del cuerpo. Vas a perder media hora corrigiendo un cuerpo que estaba bien.

### La forma que funciona

```jsonc
POST https://us-central1-aiplatform.googleapis.com/v1/projects/PROY/locations/us-central1/publishers/google/models/lyria-3-pro-preview:generateContent

{
  "contents": [{
    "role": "user",
    "parts": [{ "text": "<tu descripción musical>" }]
  }],
  "generationConfig": {
    "responseModalities": ["AUDIO"]
  }
}
```

En Node, con el SDK de Google GenAI:

```js
const res = await ai.models.generateContent({
  model: 'lyria-3-pro-preview',
  contents: [{ role: 'user', parts: [{ text: descripcionMusical }] }],
  config: { responseModalities: ['AUDIO'] },
});

const part  = res.candidates[0].content.parts.find(p => p.inlineData);
const mime  = part.inlineData.mimeType;   // 'audio/mpeg'
const datos = Buffer.from(part.inlineData.data, 'base64');
```

---

## ⚠️ La trampa del `mimeType`: `audio/mpeg` ES mp3

Segundo hallazgo verificado, y es de los que rompen guiones de automatización:

> **Lyria devuelve `mimeType: 'audio/mpeg'`.**
> **Eso ES un MP3.** No es `audio/mp3`.

`audio/mp3` no es un tipo MIME estándar. El estándar es `audio/mpeg`. Pero como casi todo el mundo
escribe la detección de extensión así:

```js
// ❌ ROTO: nunca entra al caso mp3
const ext = { 'audio/mp3': 'mp3', 'audio/wav': 'wav' }[mime] || 'bin';
```

…terminas con un archivo `salida.bin` que en realidad es un MP3 perfecto, y con una hora perdida
pensando que la generación falló.

La forma correcta:

```js
const EXT = {
  'audio/mpeg': 'mp3',   // ← el que devuelve Lyria
  'audio/mp3':  'mp3',   // por si acaso
  'audio/wav':  'wav',
  'audio/x-wav':'wav',
  'audio/L16':  'wav',
  'audio/ogg':  'ogg',
  'audio/flac': 'flac',
};
const ext = EXT[mime.split(';')[0].trim()] || 'bin';
```

Y verifica siempre lo que te llegó, sin creerle a la extensión:

```bash
ffprobe -v error -show_entries format=format_name,duration,bit_rate -of default=nw=1 pista.mp3
```

Si `ffprobe` dice `mp3` y te da una duración, tienes un MP3 bueno. Punto.

---

## Duraciones reales

Verificado en pruebas de agosto de 2026 con `lyria-3-pro-preview`: las salidas fueron de **1,5 a 2,6
minutos**.

Eso te dice tres cosas:

1. **No controlas la duración con precisión.** Le puedes sugerir "una pieza corta" o "de unos dos
   minutos", pero lo que sale, sale. No hay parámetro de duración exacta.
2. **Casi siempre te sobra.** Un reel dura 30 segundos y te van a llegar dos minutos. Eso es bueno:
   te da de dónde escoger.
3. **Tienes que saber cortar música.** El corte va **en el golpe**, nunca en el silencio previo. Y
   el final va con un fundido de 0,8 a 1,5 segundos, o con un golpe seco si el video también corta
   seco. Ver módulo `20` sobre el pulso.

Comando para quedarte con el mejor tramo:

```bash
# escuchar la pista completa y decidir el tramo (ej: del 0:47 al 1:20)
ffmpeg -ss 47 -t 33 -i pista.mp3 -af "afade=t=in:st=0:d=0.4,afade=t=out:st=32:d=1.2" tramo.wav
```

---

## Cómo se describe un tema (el prompt que funciona)

El error clásico es pedir "música épica para un anuncio". Eso es como pedir "un video bonito".

La descripción musical que funciona tiene **seis dimensiones**. Dáselas todas:

### 1. Género y referencia estilística
No un artista por nombre (ver módulo `128`), sino la escuela sonora.
> "bossa nova moderna", "house minimalista", "cumbia electrónica", "post-rock instrumental"

### 2. Tempo, en números
> "108 BPM", "tempo medio, alrededor de 90 BPM"

Los números funcionan mejor que "rápido" o "lento", y además te sirven a ti para cortar en el
compás.

### 3. Instrumentación concreta
> "guitarra nylon con el ataque presente, bajo eléctrico redondo, batería con escobillas,
> Rhodes de fondo, sin sintetizadores"

Lo que **no** quieres es tan importante como lo que quieres. "Sin voz", "sin batería", "sin
saxofón" son instrucciones válidas y útiles.

### 4. Emoción y función
> "cálido y confiado, no melancólico"
> "tiene que quedar debajo de una voz en off: sin melodía protagonista en el rango medio"

Esa segunda frase es la más útil de todas y casi nadie la escribe. Si la música va debajo de una
voz, **pídele que deje libre el rango medio**. Te ahorra la mitad del trabajo de ecualización.

### 5. Estructura (solo Pro)
Lyria 3 Pro entiende arquitectura musical:
> "intro de 8 compases con solo el bajo, entra la batería en el compás 9, coro con toda la
> instrumentación desde 0:45, bajada al final"

### 6. Mezcla y textura
> "producción limpia y moderna, sin saturación, rango dinámico amplio, estéreo abierto"
> "grabación con carácter de cinta, un poco sucia, mono"

### Ejemplo completo

```
Cumbia electrónica instrumental, 102 BPM, cálida y confiada.
Guitarra eléctrica con delay corto marcando el patrón, bajo redondo, güira,
percusión de tambor alegre, un pad suave de fondo. Sin voz, sin saxofón.
Producción limpia y moderna, estéreo abierto.
Va a ir debajo de una voz en off: deja despejado el rango medio,
sin melodía protagonista entre 300 Hz y 3 kHz.
Intro sencilla de 4 compases, entra la percusión completa después,
mantiene la energía sin subir a un clímax.
```

---

## Qué se le puede pedir de verdad, y qué no

### Sí

- Género, tempo, instrumentación, emoción, estructura, textura de mezcla
- Música instrumental de casi cualquier estilo
- Voz y letra (mejoró con 3.5; verifica disponibilidad en API)
- Generación a partir de una imagen (Lyria 3 en Vertex acepta entrada de imagen)
- Estéreo de alta fidelidad
- Varias variantes del mismo tema para elegir

### No, o no bien

- **Duración exacta.** No hay parámetro. Recortas tú.
- **Sincronía a golpes específicos de tu video.** No puedes decirle "que el golpe caiga en el
  segundo 4,2". Eso se resuelve al revés: montas el video al ritmo de la música.
- **Continuar una pista existente.** No le pases 30 segundos y le pidas los otros 30. No es esa
  herramienta.
- **Sonar como un artista concreto.** Además de que técnicamente no lo va a lograr bien, es un
  problema legal y ético (módulo `128`). Describe la escuela, no la persona.
- **Stems separados** (bajo por un lado, batería por otro). A la fecha, no. Si necesitas stems,
  necesitas otra herramienta o un compositor.
- **Ser el gancho de la pieza.** Sirve como cama, no como canción memorable.

---

## Alternativas honestas

| Herramienta | Cuándo |
|---|---|
| **Lyria 3 / 3 Pro** | Ya estás en Vertex, quieres API, quieres instrumental de fondo |
| **Suno / Udio** | Necesitas canción con voz y letra, formato canción de verdad. Más orientadas a producto de consumidor. **Ojo: hay litigios de derechos de autor abiertos en el sector**; para trabajo de cliente, lee sus términos vigentes antes de comprometerte |
| **Librería de licencia (Epidemic, Artlist, Musicbed)** | Necesitas una pista que suene a hit, con licencia clara y respaldada. Sigue siendo la opción más segura para publicidad grande |
| **Un músico** | La marca vale la pena y quieres algo que nadie más tenga. Un tema a medida en Colombia cuesta menos de lo que la gente cree |

No vendas la generación como sustituto total. Véndela como lo que es: la forma más rápida y barata
de tener una cama sonora tuya, sin reclamos, del largo que necesitas.

---

## El flujo de trabajo completo

```
1. Mira el corte del video SIN música. ¿Qué le falta? ¿energía? ¿calma? ¿tensión?
2. Escribe la descripción musical con las 6 dimensiones. Incluye "va debajo de voz" si aplica.
3. Genera 2 o 3 variantes del mismo prompt. Cuestan poco y la diferencia entre la primera
   y la tercera suele ser grande.
4. Escúchalas EN EL VIDEO, no sueltas. Una pista que suena increíble sola puede pelear
   con tu montaje.
5. Elige el tramo (te van a sobrar 1 a 2 minutos). Corta EN EL GOLPE.
6. Ajusta el nivel: música de fondo bajo voz, entre -18 y -24 LUFS; la voz manda.
7. Aplica ducking (ver módulo 70) si la voz y la música se pisan.
8. Guarda el prompt junto al proyecto. Si el cliente pide "otra igual pero más alegre",
   partes de ahí.
```

---

## Errores comunes

- **Llamar a Lyria con `:predict`.** Es `generateContent` con `responseModalities: ['AUDIO']`. El
  error que te devuelve no te lo dice.
- **Detectar la extensión buscando `audio/mp3`.** Lyria devuelve **`audio/mpeg`**, que ES mp3. Tu
  archivo `.bin` es un MP3 perfecto.
- **No verificar el archivo con `ffprobe`.** Confiar en la extensión es cómo se cuelan archivos
  corruptos a una entrega.
- **Pedir "música épica para un anuncio".** No es una descripción, es un deseo. Dale las seis
  dimensiones.
- **No decirle que va debajo de una voz.** Es la instrucción con mejor relación esfuerzo/resultado
  que existe y casi nadie la escribe.
- **Esperar duración exacta.** Salen entre 1,5 y 2,6 minutos y no lo controlas. Recortas tú.
- **Cortar la música en el silencio.** El corte va en el golpe. Siempre.
- **Generar una sola variante.** La tercera suele ser mucho mejor que la primera y cuesta lo mismo.
- **Juzgar la pista escuchándola sola.** Se juzga dentro del video.
- **Pedir que suene a un artista por nombre.** Mal técnicamente, peor legalmente.
- **Prometerle stems al cliente.** No hay.
- **Usar un modelo `preview` para un cliente sin plan B.** Preview significa que puede cambiar o
  irse.
- **No guardar el prompt.** El cliente siempre pide "otra igual pero...".

---

## Checklist

- [ ] Llamé con **`generateContent` + `responseModalities: ['AUDIO']`**, no con `:predict`
- [ ] Mi detección de extensión contempla **`audio/mpeg` → `.mp3`**
- [ ] Verifiqué el archivo con `ffprobe` (formato y duración reales)
- [ ] La descripción musical cubre **género, tempo en BPM, instrumentación, emoción, estructura y
      mezcla**
- [ ] Si va debajo de voz en off, se lo dije explícitamente y le pedí el rango medio despejado
- [ ] Dije también **qué NO quiero** (sin voz, sin saxofón, sin batería)
- [ ] Generé **2 o 3 variantes** antes de elegir
- [ ] Escuché las variantes **dentro del video**, no sueltas
- [ ] Corté el tramo **en el golpe** y con fundido de salida coherente con el corte de imagen
- [ ] Ajusté nivel y ducking respecto a la voz
- [ ] Guardé el prompt y el modelo usado en la carpeta del proyecto
- [ ] Si es trabajo de cliente, tengo claro el estado de derechos y un plan B al modelo `preview`
