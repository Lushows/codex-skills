# 95 — Metadatos y accesibilidad: por qué el video mudo gana


> ## 🔴 CORRECCIÓN MEDIDA · `MarginV` sin `PlayResY` no hace lo que dice
>
> Las cifras de `MarginV` de este módulo (380–500) **solo valen si además declaras
> `PlayResX` y `PlayResY`**. Sin eso, libass interpreta el margen y el cuerpo en su
> resolución por defecto y los escala al vídeo por un factor que nadie declaró.
>
> Medido el 11-sep-2026 sobre un lienzo de 1080×1920 con un `.srt` y el filtro
> `subtitles`:
>
> | Orden | Dónde acaba el subtítulo |
> |---|---|
> | `MarginV=380` | **NO APARECE. Fuera de pantalla.** El vídeo sale sin subtítulo y ffmpeg no avisa |
> | `MarginV=60` | a 459 px del borde — y con el cuerpo inflado, ocupando de y=615 a y=1461 |
> | `MarginV=380,PlayResX=1080,PlayResY=1920` | a **390 px del borde**, con el cuerpo correcto. Lo que se pedía |
>
> **La regla:** en `force_style` van SIEMPRE `PlayResX` y `PlayResY` con las medidas
> reales del vídeo. Si no, ni el margen ni el tamaño de letra significan lo que dicen.
> Y el fallo es mudo: el archivo se genera, pesa lo normal y no lleva subtítulo.

> El 85% de la gente ve video en redes **sin sonido**. Si tu video necesita audio para entenderse, acabas
> de perder a 8 de cada 10. La accesibilidad no es un favor que le haces a nadie: es la palanca de alcance
> más barata que existe.

---

## Los dos tipos de subtítulo (y cuál usar)

Esta distinción decide la mitad de tu flujo de trabajo.

### Subtítulos quemados (*burned-in*, *open captions*)

El texto está **pintado dentro de los píxeles del video**. No se puede apagar. Es parte de la imagen.

- ✅ **Se ven siempre**, en cualquier reproductor, en cualquier plataforma
- ✅ Control total de tipografía, tamaño, posición, animación
- ✅ Funcionan en el feed con autorreproducción sin sonido
- ❌ No se pueden traducir ni desactivar
- ❌ Si te equivocaste, hay que reexportar todo
- ❌ **La plataforma no puede leerlos** para indexarte

**Úsalos en:** Reels, TikTok, Shorts, anuncios. Todo lo vertical y corto.

### Subtítulos cerrados (*closed captions*, CC)

Van en un **archivo aparte** (`.srt`, `.vtt`) o en una pista dentro del contenedor. El espectador los
prende y los apaga.

- ✅ **La plataforma los lee** → mejora búsqueda, recomendación y traducción automática
- ✅ Se pueden corregir sin tocar el video
- ✅ Traducibles a otros idiomas
- ✅ Lectores de pantalla y accesibilidad real
- ❌ El usuario tiene que activarlos (y casi nadie lo hace)
- ❌ Tipografía y posición las decide la plataforma

**Úsalos en:** YouTube largo, video corporativo, cualquier cosa donde el descubrimiento por búsqueda
importe.

### La respuesta correcta casi siempre es: LOS DOS

Quema los subtítulos **y además** sube el archivo `.srt`. Ganas la visibilidad del feed mudo **y** la
indexación de la plataforma. Cuesta cinco minutos extra.

---

## Por qué los subtítulos aumentan el alcance de verdad

No es una creencia, hay mecánica detrás:

1. **Retención.** Sin sonido, sin subtítulos, el espectador no entiende y se va a los 2 segundos. Con
   subtítulos entiende y se queda. **La retención es la señal #1 de distribución en todas las plataformas.**
2. **Indexación.** YouTube y Meta leen el texto del subtítulo y lo usan para decidir a quién mostrarte. Un
   video sin transcripción es un video del que la plataforma no sabe nada.
3. **Traducción automática.** Con `.srt` en español, YouTube puede ofrecer subtítulos en inglés y
   portugués automáticamente. Sin archivo, no puede.
4. **Comprensión con ruido de fondo.** Mucha gente ve video en bus, en la calle, en el trabajo. Ahí el
   audio no existe aunque el sonido esté prendido.
5. **Accesibilidad real.** Personas sordas o con dificultad auditiva. Es correcto hacerlo y punto.

---

## Generar los subtítulos

### Transcribir con Whisper (lo más práctico)

```bash
# Extrae el audio del video montado
ffmpeg -i video_final.mp4 -vn -acodec pcm_s16le -ar 16000 -ac 1 audio.wav

# Transcribe (whisper.cpp o el CLI de openai-whisper)
whisper audio.wav --language Spanish --model medium --output_format srt
```

Un `.srt` se ve así:

```
1
00:00:00,120 --> 00:00:02,480
Tu plato estrella es el que te está quebrando.

2
00:00:02,480 --> 00:00:05,100
Y te voy a mostrar por qué en treinta segundos.
```

**Siempre revísalo a mano.** Whisper es muy bueno y aun así se come nombres propios, marcas y regionalismos.
"GastroLatam" puede salir "gastro latan". Los números y precios los inventa con frecuencia. **Revisa
nombres, cifras y precios uno por uno.**

### Quemar subtítulos con ffmpeg

**Desde un `.srt`, con estilo:**

```bash
ffmpeg -i video.mp4 -vf "subtitles=subs.srt:force_style=\
'FontName=Montserrat SemiBold,FontSize=22,PrimaryColour=&H00FFFFFF,\
OutlineColour=&H00000000,BorderStyle=1,Outline=3,Shadow=1,\
Alignment=2,MarginV=380,PlayResX=1080,PlayResY=1920'" \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a copy video_subs.mp4
```

Qué es cada cosa:

| Parámetro | Qué hace |
|---|---|
| `FontSize` | Tamaño. En 1080×1920, entre 20 y 28 |
| `PrimaryColour` | Color del texto en formato `&HAABBGGRR` (¡al revés del hexadecimal normal!) |
| `OutlineColour` | Color del contorno |
| `BorderStyle=1` | Contorno + sombra. `3` sería caja de fondo sólido |
| `Outline` | Grosor del contorno. **3 es lo mínimo para legibilidad sobre cualquier fondo** |
| `Alignment=2` | Centrado abajo (teclado numérico: 1=abajo-izq, 5=centro, 8=arriba-centro) |
| `MarginV` | Distancia desde el borde. **En vertical usa 380–450 para esquivar la interfaz** |

**Los colores en formato ASS van al revés.** Blanco puro `#FFFFFF` se escribe `&H00FFFFFF`. Amarillo
`#FFD700` se escribe `&H0000D7FF`. Se acostumbra uno.

**Posición correcta en vertical:** los subtítulos van entre el **55% y el 70% de la altura**. Arriba de
eso tapan la cara; abajo chocan con la descripción de la app y con los subtítulos automáticos de la
plataforma.

Para 1080 × 1920, eso es `MarginV` entre 380 y 500.

### Estilo "karaoke" palabra por palabra

Lo que hace CapCut y todo el mundo copia. Es texto ASS con etiquetas de tiempo (`\k`). Es tedioso a mano;
lo práctico es generar el `.ass` con un script a partir de la transcripción con marcas por palabra que
Whisper puede producir (`--word_timestamps True`).

Honestamente: **para el 90% de los casos, un subtítulo limpio y grande de 3–5 palabras por bloque rinde
igual que el karaoke** y cuesta la décima parte del trabajo. El karaoke ayuda en contenido de ritmo muy
rápido; en contenido explicativo distrae.

---

## Poner subtítulos cerrados (sin quemarlos)

**Como pista dentro del MP4** (compatible con reproductores modernos y YouTube):

```bash
ffmpeg -i video.mp4 -i subs.srt -c:v copy -c:a copy \
  -c:s mov_text -metadata:s:s:0 language=spa \
  -movflags +faststart video_cc.mp4
```

`mov_text` es el formato de subtítulo que acepta el contenedor MP4. Para `.mkv` puedes usar `-c:s srt`
directo.

**Verificar que quedó:**
```bash
ffprobe -v error -select_streams s -show_entries stream=index,codec_name:stream_tags=language \
  -of default=noprint_wrappers=1 video_cc.mp4
```

**Convertir `.srt` a `.vtt`** (el formato que pide la web con HTML5):
```bash
ffmpeg -i subs.srt subs.vtt
```

---

## Metadatos del archivo

Los metadatos son la información que va dentro del archivo: título, autor, descripción, fecha. Sirven para
tres cosas: que el cliente sepa qué es, que tú lo encuentres dentro de un año, y que los sistemas de
gestión lo indexen.

```bash
ffmpeg -i video.mp4 -c copy \
  -metadata title="Calculadora de Costos — Reel 01 — Gancho Plato Estrella" \
  -metadata artist="GastroLatam" \
  -metadata album="Campaña Agosto 2026" \
  -metadata comment="Máster de entrega. CRF 18. Aprobado 2026-08-04." \
  -metadata date="2026-08-04" \
  -metadata language=spa \
  salida.mp4
```

**Leer los metadatos de un archivo:**
```bash
ffprobe -v error -show_entries format_tags -of default=noprint_wrappers=1 video.mp4
```

**Limpiar todos los metadatos** (útil antes de entregar algo a un cliente, porque los archivos suelen
arrastrar el nombre del software, rutas de tu computador y a veces GPS de la cámara):

```bash
ffmpeg -i video.mp4 -map_metadata -1 -c copy limpio.mp4
```

Ojo con esto último: **los archivos de cámara y celular arrastran coordenadas GPS.** Si grabaste en tu casa
y entregas el archivo tal cual, estás entregando tu dirección. `-map_metadata -1` lo borra.

---

## Metadatos de la publicación (los que sí mueven la aguja)

Aparte del archivo, cada plataforma tiene su capa de texto. Estos importan más que los metadatos internos:

### Descripción / pie de foto

- **Las primeras 125 caracteres** son lo único que se ve antes del "ver más". Ahí va lo que importa.
- Incluye **las palabras que la gente buscaría**. TikTok e Instagram tienen buscador y funciona.
- Una llamada a la acción clara al final.

### Texto alternativo (alt text)

Instagram y Facebook permiten poner descripción alternativa a la portada. Casi nadie lo usa. Lo leen los
lectores de pantalla **y** el sistema de clasificación de contenido de Meta.

### Etiquetas y hashtags

- Instagram: **3 a 5** relevantes. La época de 30 hashtags murió.
- TikTok: 3 a 5, uno amplio y dos específicos.
- YouTube: las etiquetas pesan poco hoy; **el título, la descripción y la transcripción pesan mucho**.

### Capítulos de YouTube

Se generan poniendo marcas de tiempo en la descripción. **La primera debe ser `0:00`** o no funcionan:

```
0:00 Por qué tu plato estrella te quiebra
1:24 Cómo calcular el costo real
3:40 El error del 90% de los restaurantes
5:10 Qué hacer esta semana
```

Sirven de verdad: mejoran la retención porque la gente salta a lo que le interesa en vez de irse.

---

## Otras accesibilidades que sí importan

### Contraste del texto

Un texto blanco sobre un fondo claro es texto que no existe. La norma de accesibilidad web pide una
relación de contraste de **4,5:1 para texto normal y 3:1 para texto grande**. Para video, la regla
práctica es más simple: **todo texto lleva contorno oscuro de al menos 3 px, o va sobre una caja
semitransparente.** Así funciona sobre cualquier fondo.

### Nada de destellos rápidos

Más de **3 destellos por segundo** puede disparar convulsiones fotosensibles. No es paranoia, es la norma
(WCAG 2.3.1). Si tu edición tiene un montaje de cortes muy rápidos con cambios fuertes de brillo,
revísalo.

Detectar cambios bruscos de luminancia:
```bash
ffmpeg -i video.mp4 -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -f null - 2>&1 | grep YAVG | head -50
```

### Audio descriptivo y voz clara

Si la información crítica solo existe en la imagen (un precio en pantalla, un gráfico), **dilo también en
voz**. Y al revés: si algo importante solo está en el audio, ponlo en pantalla.

### Velocidad de lectura

Un subtítulo tiene que poder leerse. La referencia de la industria son **17 caracteres por segundo** como
máximo. Traducido: un bloque de 34 caracteres necesita al menos 2 segundos en pantalla.

Si vas a cortar rápido y el subtítulo pasa volando, **acorta el texto**, no lo dejes ilegible.

---

## Flujo completo recomendado

```bash
# 1. Extraer audio del corte final
ffmpeg -i corte_final.mp4 -vn -acodec pcm_s16le -ar 16000 -ac 1 audio.wav

# 2. Transcribir
whisper audio.wav --language Spanish --model medium --output_format srt

# 3. REVISAR EL .SRT A MANO (nombres, cifras, precios)

# 4. Versión quemada para redes verticales
ffmpeg -i corte_final.mp4 -vf "subtitles=audio.srt:force_style=\
'FontName=Montserrat SemiBold,FontSize=22,PrimaryColour=&H00FFFFFF,\
OutlineColour=&H00000000,BorderStyle=1,Outline=3,Alignment=2,MarginV=420,PlayResX=1080,PlayResY=1920'" \
  -c:v libx264 -crf 19 -preset slow -pix_fmt yuv420p -c:a copy reel_subs.mp4

# 5. Versión con CC para YouTube
ffmpeg -i corte_final.mp4 -i audio.srt -c:v copy -c:a copy \
  -c:s mov_text -metadata:s:s:0 language=spa -movflags +faststart youtube_cc.mp4

# 6. Metadatos y limpieza de GPS
ffmpeg -i youtube_cc.mp4 -map_metadata -1 -c copy \
  -metadata title="..." -metadata artist="GastroLatam" -metadata date="2026-08-04" \
  entrega_final.mp4
```

---

## Errores comunes

1. **No poner subtítulos.** Con el 85% del consumo en mudo, es la decisión más cara que puedes tomar.
2. **Subir el `.srt` de Whisper sin revisar.** Nombres propios destrozados, precios inventados, marcas mal
   escritas. Revisa siempre cifras y nombres.
3. **Poner los subtítulos abajo del todo en vertical.** Chocan con la descripción de la app y con los
   subtítulos automáticos de la plataforma. Súbelos al 55–70% de altura.
4. **Texto sin contorno.** Sobre un fondo claro desaparece y no te enteras porque tu fondo de prueba era
   oscuro.
5. **Bloques de subtítulo demasiado largos.** Máximo 2 líneas, 3–7 palabras por línea, mínimo 1,2 s en
   pantalla.
6. **Solo quemarlos, sin subir el `.srt`.** Pierdes indexación, búsqueda y traducción automática gratis.
7. **Entregar un archivo con los metadatos GPS de la cámara.** Estás repartiendo la dirección donde
   grabaste.
8. **Karaoke palabra por palabra en contenido explicativo.** Distrae del contenido. Úsalo solo en ritmo
   rápido.
9. **Poner 30 hashtags.** No solo no ayuda: en 2026 se lee como spam.
10. **Olvidar el `0:00` en los capítulos de YouTube.** Sin esa primera marca no se generan y no te dice
    por qué.
11. **Meter el precio o el dato clave solo en pantalla, sin decirlo.** Y al revés. Redundancia
    voz + texto es accesibilidad y además sube la retención.
12. **Subtítulos con velocidad de lectura imposible.** Si el bloque dura 0,6 s y tiene 40 caracteres,
    nadie lo leyó.

---

## Checklist

Antes de publicar cualquier video:

- [ ] Tiene **subtítulos quemados** si va a redes verticales
- [ ] Tiene archivo **`.srt` subido aparte** si va a YouTube o web
- [ ] El `.srt` fue **revisado a mano**: nombres propios, marcas, cifras y precios
- [ ] Los subtítulos están entre el **55% y el 70% de la altura** en vertical
- [ ] Todo texto tiene **contorno de ≥3 px** o caja de fondo
- [ ] Ningún bloque de subtítulo pasa de **2 líneas** ni de 17 caracteres por segundo
- [ ] **Prueba del mudo:** silencié el video y sigue entendiéndose completo
- [ ] La información crítica está **en voz Y en pantalla**
- [ ] No hay más de 3 destellos por segundo en ningún tramo
- [ ] Metadatos del archivo puestos (título, autor, fecha) y **GPS eliminado**
- [ ] Descripción con lo importante en los **primeros 125 caracteres**
- [ ] Si es YouTube: capítulos con `0:00` de primero, título y descripción con palabras buscables
- [ ] Texto alternativo puesto en la portada donde la plataforma lo permita
