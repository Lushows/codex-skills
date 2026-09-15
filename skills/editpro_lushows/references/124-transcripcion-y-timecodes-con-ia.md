# 124 — Transcripción y tiempos con IA: cómo pedirlos para que sirvan de verdad

## El problema real

Una transcripción bonita no sirve para editar. Lo que sirve para editar es **saber en qué segundo
exacto pasa cada cosa**.

Sin tiempos exactos no puedes:
- cortar automáticamente los silencios y las muletillas,
- encontrar el mejor take entre cuarenta,
- poner subtítulos que caigan encima de la palabra,
- generar un mapa del bruto para decidir el montaje,
- sincronizar b-roll con lo que se está diciendo.

Y aquí está el problema: **los modelos de lenguaje son malísimos calculando tiempo si los dejas a su
aire.** Te van a devolver "aproximadamente al minuto 2" o, peor, un `00:02:34` que suena muy exacto
y está desfasado ocho segundos.

Este módulo es sobre cómo obligarlos a darte números que puedas meter en un comando de ffmpeg sin
revisarlos uno por uno.

---

## Primero: ¿ASR o modelo multimodal?

Hay dos caminos y sirven para cosas distintas.

### Camino A — ASR clásico (Whisper, Deepgram, AssemblyAI)

Reconocimiento de voz especializado. Le das audio, te da texto **con marcas de tiempo por palabra**,
calculadas por el propio motor de alineación. Los tiempos son de verdad, no estimados.

| Servicio | Precio aprox. (ago-2026) |
|---|---|
| **AssemblyAI** | ~$0.0061/min (~$0.37/hora); diarización +$0.02/hora |
| **Deepgram** | ~$0.0043/min |
| **OpenAI Whisper API** | ~$0.003–$0.006/min en archivo; ~$0.017/min en tiempo real |
| **Google Cloud Speech-to-Text** | ~$0.016/min (el más caro del grupo) |

Nota de precios: el streaming en tiempo real cuesta entre 20% y 80% más que procesar el archivo
completo. Si el video ya está grabado, **nunca uses streaming**.

**Usa este camino cuando** necesites tiempos precisos para cortar. Que es casi siempre.

### Camino B — Modelo multimodal (Gemini, Claude con audio)

Le pasas el audio o el video y le haces preguntas en lenguaje natural: "¿dónde explica el precio?",
"¿cuál es el mejor take de esta frase?", "resume esto en cinco puntos con sus tiempos".

**Usa este camino cuando** necesites **entender** el material, no cortarlo al frame. Es
insuperable para minería del bruto (módulo `12`).

### La combinación que se usa en producción

```
1. ASR → transcripción con tiempos por palabra (la verdad numérica)
2. Le pasas ESA transcripción con tiempos al modelo de lenguaje
3. El modelo decide QUÉ cortar, apoyándose en tiempos que no inventó
```

Así el modelo nunca tiene que estimar tiempo: solo tiene que **copiar** el número que le diste. Y
copiar sí lo hace bien.

---

## El prompt que funciona (y por qué)

Cuando de verdad tienes que pedirle tiempos a un modelo de lenguaje, estas son las cinco reglas.

### Regla 1 — Una sola unidad, y que sea segundos

Nunca pidas `HH:MM:SS`, ni `MM:SS`, ni "minuto 2 con 30". Pide **segundos decimales desde el
inicio**.

```
Devuelve todos los tiempos como SEGUNDOS DECIMALES desde el inicio del archivo.
Ejemplo: 92.4 significa un minuto con 32,4 segundos.
NO uses formato HH:MM:SS. NO uses minutos. NO uses palabras como "aproximadamente".
```

¿Por qué? Porque el formato `HH:MM:SS` obliga al modelo a hacer aritmética de base 60 mientras
razona sobre otra cosa. Ahí es donde se equivoca. Y porque `92.4` entra directo a ffmpeg:

```bash
ffmpeg -ss 92.4 -to 97.8 -i bruto.mp4 corte.mp4
```

Sin conversiones, sin scripts de parseo, sin errores de traducción.

### Regla 2 — Formato de salida rígido, JSON, sin prosa

```
Responde ÚNICAMENTE con un array JSON. Sin texto antes ni después. Sin bloque de código.
Cada elemento: {"inicio": número, "fin": número, "texto": "...", "hablante": "..."}
```

Un modelo que puede escribir prosa alrededor va a escribir prosa alrededor, y tu parser se rompe.

### Regla 3 — Prohíbe explícitamente estimar

```
Si no puedes determinar el tiempo con precisión, pon null. NO estimes. NO redondees a
números bonitos. Un tiempo inventado es peor que un tiempo ausente.
```

Esto funciona sorprendentemente bien. Sin ello, el modelo prefiere darte algo antes que admitir que
no sabe, porque "ser útil" le pesa más que "ser exacto". Hay que darle permiso explícito para decir
que no sabe.

### Regla 4 — Fíjale un ancla

```
La duración total del archivo es 384.6 segundos. Ningún tiempo puede ser mayor.
El primer sonido empieza en 0.0.
```

Con el total a la vista, el modelo se auto-calibra. Sin él, la deriva se acumula y para el minuto 5
ya va desfasado.

### Regla 5 — El truco de verificación: "¿qué se oye después?"

Esta es la mejor de todas y casi nadie la usa.

```
Para cada segmento, agrega el campo "siguiente": las primeras 4 o 5 palabras que se
oyen INMEDIATAMENTE DESPUÉS del tiempo de fin.
```

¿Para qué sirve? Para **verificar sin volver a escuchar todo**. Tú abres el video en el tiempo `fin`
que te dio, escuchas dos segundos, y comparas con lo que dijo que venía después.

- **Coincide** → el tiempo es bueno. Y si es bueno ahí, probablemente lo sea en toda la zona.
- **No coincide** → sabes de inmediato que hay desfase, y hasta te dice **hacia dónde**: si lo que
  oyes es lo que él puso en "siguiente" pero más tarde, va adelantado; si ya pasó, va atrasado.

Es un control de calidad que cuesta diez segundos por punto de muestreo y detecta el 100% de los
desfases grandes. Muestrea tres o cuatro puntos repartidos (principio, medio, final) y ya sabes si
la transcripción es confiable.

### El prompt completo

```
Transcribe este audio y devuelve los segmentos con tiempos.

FORMATO — obligatorio:
- Responde ÚNICAMENTE con un array JSON válido. Sin texto antes ni después.
- Cada elemento: {"inicio": n, "fin": n, "texto": "...", "siguiente": "...", "hablante": "..."}

TIEMPOS — obligatorio:
- SEGUNDOS DECIMALES desde el inicio del archivo. Ejemplo: 92.4
- NO uses HH:MM:SS. NO uses minutos. NO uses "aproximadamente".
- Duración total del archivo: 384.6 segundos. Ningún tiempo puede superarla.
- Si no puedes determinar un tiempo con precisión, pon null. NO estimes.

CAMPO "siguiente":
- Las primeras 4 o 5 palabras que se oyen inmediatamente DESPUÉS del tiempo "fin".
- Si es el último segmento, pon "FIN".

TEXTO:
- Transcribe literal, incluyendo muletillas ("eh", "o sea", "este") y repeticiones.
- No corrijas la gramática. No resumas.
- Marca los silencios de más de 1.5 segundos como un segmento con texto "[silencio]".
```

Ese último bloque importa: **transcripción literal, con muletillas**. Una transcripción "limpia" es
inútil para editar, porque justamente las muletillas y los silencios son lo que vas a cortar. Si el
modelo te las quita, no puedes encontrarlas.

---

## Prepara el audio antes de mandarlo

Regla que ahorra plata y mejora resultados: **manda audio, no video, y mándalo mono a 16 kHz.**

```bash
ffmpeg -i bruto.mp4 -vn -ac 1 -ar 16000 -c:a pcm_s16le audio.wav
```

Qué hace y por qué:

- `-vn` — descarta el video. Los servicios de ASR no lo miran y tú estás subiendo megas de más.
- `-ac 1` — mono. La voz no tiene información estéreo útil. Mitad de tamaño.
- `-ar 16000` — 16 kHz. **Es la frecuencia de muestreo con la que están entrenados los modelos de
  voz.** Subir 48 kHz no mejora nada; el servicio lo va a bajar de todos modos.
- `pcm_s16le` — WAV sin comprimir. Si vas a comprimir para subir más rápido, usa FLAC (sin pérdida),
  no MP3.

Un video de una hora en 4K pesa varios gigas. Ese mismo audio en mono 16k pesa unos 55 MB. La subida
pasa de veinte minutos a treinta segundos, y la transcripción es igual de buena o mejor.

Si el audio está muy sucio, límpialo antes (módulo `70`): un paso de reducción de ruido antes de
transcribir baja notablemente la tasa de error.

---

## Qué haces con los tiempos una vez los tienes

### Cortar automáticamente

```bash
# de un JSON de segmentos a cortes reales
jq -r '.[] | select(.texto != "[silencio]") | "\(.inicio) \(.fin)"' segmentos.json |
while read INI FIN; do
  ffmpeg -nostdin -ss "$INI" -to "$FIN" -i bruto.mp4 -c copy "clip_${INI}.mp4"
done
```

Ojo: con `-c copy` el corte se va al fotograma clave más cercano, así que no es exacto al frame. Si
necesitas exactitud, recodifica (quita `-c copy`).

### Subtítulos SRT

Los tiempos en segundos se convierten a formato SRT trivialmente. La clave editorial no es el
formato: es **el troceo**. Ver módulo `41`. Reglas rápidas: máximo 2 líneas, máximo ~42 caracteres
por línea, mínimo 1 segundo en pantalla, y **corta por unidad de sentido, no por límite de
caracteres**.

### Encontrar el mejor take

Le pasas la transcripción con tiempos a un modelo y le pides:

```
Aquí hay 12 intentos de la misma frase. Para cada uno dime inicio, fin y una nota de 1 a 5
según: fluidez (sin muletillas), energía, y si la frase quedó completa.
Devuelve el mejor primero. Formato JSON, tiempos en segundos decimales.
```

Esto convierte cuarenta minutos de escuchar takes en dos minutos de leer una tabla.

---

## Verificación: el ritual de los tres puntos

Nunca aceptes una transcripción con tiempos sin verificar. El ritual cuesta un minuto:

1. Toma **tres segmentos**: uno al 10% del archivo, uno al 50%, uno al 90%.
2. Para cada uno, salta a su tiempo `fin` en el reproductor.
3. Escucha 3 segundos y compáralo con el campo `siguiente`.
4. Si los tres coinciden → confiable, sigue.
5. Si el del 90% falla y los otros dos no → **hay deriva acumulada**. No confíes en la segunda
   mitad; retranscribe con el archivo partido en trozos más cortos.
6. Si fallan todos → el modelo estimó. Cambia a un ASR de verdad.

La deriva acumulada es el fallo más traicionero: la transcripción arranca perfecta y para el final
va desfasada seis segundos. Si solo verificas el principio, no la ves.

---

## Errores comunes

- **Pedir los tiempos en `HH:MM:SS`.** Obligas al modelo a hacer aritmética de base 60 mientras
  razona. Ahí se equivoca. Pide segundos decimales.
- **Mezclar unidades en el mismo pedido.** Segundos en un campo y minutos en otro es garantía de
  desastre.
- **No prohibir la estimación.** El modelo prefiere darte un número inventado antes que admitir que
  no sabe. Dale permiso explícito para poner `null`.
- **No fijar la duración total como ancla.** Sin techo, la deriva se acumula.
- **No pedir el campo "siguiente".** Es el control de calidad más barato que existe y casi nadie lo
  usa.
- **Verificar solo el principio.** La deriva acumulada aparece al final. Verifica tres puntos.
- **Pedir transcripción limpia sin muletillas.** Las muletillas son lo que vas a cortar; si te las
  quitan, no las encuentras.
- **Subir el video completo.** Extrae el audio: mono, 16 kHz. Es la misma calidad de transcripción y
  una fracción del tamaño y del tiempo.
- **Usar streaming para un archivo ya grabado.** Cuesta entre 20% y 80% más por nada.
- **Comprimir el audio a MP3 antes de transcribir.** Si vas a comprimir, FLAC (sin pérdida).
- **Pedirle tiempos a un modelo de lenguaje cuando había un ASR disponible.** El ASR tiene
  alineación real; el modelo de lenguaje estima.
- **Confiar en el corte con `-c copy`.** Se va al fotograma clave más cercano. Si necesitas
  exactitud, recodifica.
- **No guardar el JSON de segmentos.** Es el mapa del bruto. Vale más que el bruto.

---

## Checklist

- [ ] Extraje el audio a **mono, 16 kHz**, sin video, antes de subir nada
- [ ] Si el audio estaba sucio, lo limpié antes de transcribir
- [ ] Usé un **ASR real** para los tiempos, y el modelo de lenguaje solo para decidir qué cortar
- [ ] El prompt pide **segundos decimales**, nunca `HH:MM:SS`
- [ ] El prompt exige **JSON puro**, sin prosa alrededor
- [ ] El prompt **prohíbe estimar** y permite `null`
- [ ] Le di la **duración total** como ancla
- [ ] Pedí el campo **"siguiente"** (las 4–5 palabras que se oyen después)
- [ ] Pedí transcripción **literal**, con muletillas y silencios marcados
- [ ] Hice el **ritual de los tres puntos** (10%, 50%, 90%) antes de confiar
- [ ] Si detecté deriva, partí el archivo en trozos y retranscribí
- [ ] Guardé el JSON de segmentos en la carpeta del proyecto
- [ ] Si el corte tiene que ser exacto al frame, no usé `-c copy`
