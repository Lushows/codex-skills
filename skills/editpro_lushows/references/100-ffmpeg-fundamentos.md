# 100 — ffmpeg: fundamentos, anatomía y cómo leer un error

## Qué es ffmpeg y por qué lo usas

ffmpeg lee archivos de audio y video, los transforma y los vuelve a escribir. No tiene ventana, ni
línea de tiempo, ni botón de deshacer. Le dices exactamente qué hacer y lo hace.

Para un editor eso significa tres cosas: **es reproducible** (el mismo comando da el mismo resultado
hoy y en seis meses); **es rápido para lo repetitivo** (cortar 40 clips o ponerle el mismo logo a 12
videos son segundos, no horas); y **es honesto** (cuando falla, falla con un mensaje; las interfaces
bonitas fallan en silencio).

No reemplaza el criterio de montaje. Reemplaza el trabajo mecánico.

---

## La anatomía de un comando

Todo comando de ffmpeg tiene esta forma, siempre, sin excepción:

```
ffmpeg [opciones globales] [opciones de entrada] -i ENTRADA [opciones de salida] SALIDA
```

Ejemplo real, mínimo:

```bash
ffmpeg -y -hide_banner -i entrada.mp4 -c:v libx264 -crf 20 -c:a aac -b:a 192k salida.mp4
```

Traducido a español:

- `-y` — sobrescribe la salida si ya existe, sin preguntar (opción global)
- `-hide_banner` — no imprimas las 20 líneas de versión y librerías (opción global)
- `-i entrada.mp4` — esta es la entrada
- `-c:v libx264` — codifica el video con H.264
- `-crf 20` — calidad del video (más bajo = mejor calidad y archivo más grande)
- `-c:a aac -b:a 192k` — codifica el audio en AAC a 192 kbps
- `salida.mp4` — lo último siempre es la salida

### La regla que rompe a todo el mundo: la posición manda

**En ffmpeg las opciones no son globales por defecto: se aplican al archivo que viene DESPUÉS.**

Esto no es lo mismo:

```bash
# -ss se aplica a la ENTRADA: salta a los 10s antes de decodificar
ffmpeg -ss 10 -i entrada.mp4 -t 5 salida.mp4

# -ss se aplica a la SALIDA: decodifica desde 0 y descarta hasta los 10s
ffmpeg -i entrada.mp4 -ss 10 -t 5 salida.mp4
```

Los dos producen 5 segundos que empiezan en el segundo 10, pero por caminos distintos, con velocidades
y precisión distintas. Ver `101`.

La misma lógica aplica a `-r`, `-f`, `-c`, `-pix_fmt` y casi todo lo demás. **Mnemotecnia:** lee el
comando como una frase de izquierda a derecha. "Con este arranque (`-ss 10`), abre este archivo
(`-i`), y con estas instrucciones (`-c:v ...`) escribe este otro (`salida.mp4`)".

---

## Varias entradas, varias salidas

ffmpeg acepta cuantas entradas quieras, numeradas desde 0 en el orden en que aparecen.

```bash
ffmpeg -i video.mp4 -i musica.mp3 -i logo.png salida.mp4
```
`0` = video.mp4, `1` = musica.mp3, `2` = logo.png.

También acepta varias salidas en el mismo comando, lo que evita decodificar dos veces:

```bash
ffmpeg -i master.mov \
  -c:v libx264 -crf 20 -vf "scale=1080:1920" -c:a aac reel_vertical.mp4 \
  -c:v libx264 -crf 20 -vf "scale=1920:1080" -c:a aac youtube_horizontal.mp4
```

Cada bloque de opciones aplica solo a la salida que le sigue.

---

## Flujos (streams) y el mapeo con -map

Un archivo de video no es "un video". Es un contenedor con **flujos** adentro: uno o varios de video,
uno o varios de audio, a veces subtítulos, a veces capítulos, a veces datos.

La notación es `ENTRADA:TIPO:INDICE`:

| Referencia | Significa |
|---|---|
| `0:v` | todos los flujos de video de la entrada 0 |
| `0:v:0` | el primer flujo de video de la entrada 0 |
| `0:a:1` | el segundo flujo de audio de la entrada 0 |
| `1:a` | todo el audio de la entrada 1 |
| `0:s:0` | el primer flujo de subtítulos de la entrada 0 |
| `0:0` | el flujo número 0 de la entrada 0, sea del tipo que sea |

### Qué hace ffmpeg si no usas -map

Si no mapeas nada, ffmpeg elige **automáticamente**: el mejor flujo de video, el mejor de audio y el
mejor de subtítulos de **todas** las entradas juntas, y descarta el resto. Con dos entradas de video
escoge una sola y bota la otra sin darte un error: solo lo ves en el resultado.

**Regla: en cuanto tengas más de una entrada, mapea explícitamente. Siempre.**

```bash
# El video de la entrada 0, el audio de la entrada 1. Descarta el audio original.
ffmpeg -i video.mp4 -i musica.mp3 -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -shortest salida.mp4
```

Otros usos:

```bash
# Quitar TODOS los subtítulos (el signo menos resta)
ffmpeg -i entrada.mkv -map 0 -map -0:s -c copy sin_subs.mkv

# Copiar todo tal cual, incluidos los flujos que ffmpeg normalmente descartaría
ffmpeg -i entrada.mkv -map 0 -c copy copia_completa.mkv

# Mapear audio "si existe" (el ? evita que falle si el clip es mudo)
ffmpeg -i clip.mp4 -map 0:v:0 -map 0:a:0? -c copy salida.mp4
```

Ese `?` final vale oro cuando procesas una carpeta entera y algún clip vino sin audio.

---

## Copiar vs recodificar

Esta es la decisión más importante en cualquier comando.

```bash
# COPIAR: mueve los bits tal cual. Segundos. Cero pérdida.
ffmpeg -i entrada.mp4 -c copy salida.mp4

# RECODIFICAR: decodifica y vuelve a comprimir. Minutos. Pierde algo de calidad.
ffmpeg -i entrada.mp4 -c:v libx264 -crf 20 -c:a aac salida.mp4
```

| | Copiar (`-c copy`) | Recodificar |
|---|---|---|
| Velocidad | 50x a 500x tiempo real | 0.5x a 5x tiempo real |
| Calidad | idéntica, sin pérdida | pierde en cada pasada |
| Puedes filtrar | **No** | Sí |
| Corte exacto | No (solo en keyframes) | Sí |

**Regla del editor:** recodifica el mínimo de veces posible. Cada recodificación es una fotocopia de
una fotocopia. Si vas a hacer cinco operaciones, hazlas todas en un solo comando, no en cinco.

Puedes mezclar: copiar video y recodificar audio, o al revés.

```bash
ffmpeg -i entrada.mp4 -c:v copy -af "loudnorm=I=-14:TP=-1" -c:a aac -b:a 192k salida.mp4
```

Si intentas filtrar un flujo que estás copiando, ffmpeg lo dice claro:
`Filtering and streamcopy cannot be used together.`

---

## Las opciones que vas a usar todos los días

### Globales

```bash
-y                  # sobrescribe sin preguntar
-n                  # nunca sobrescribas (falla si existe)
-hide_banner        # oculta el banner de versión
-loglevel error     # solo muestra errores
-stats              # muestra la barra de progreso aunque bajes el loglevel
-nostdin            # no leas del teclado (imprescindible en scripts y bucles)
```

Niveles de `-loglevel`, de menos a más ruidoso: `quiet`, `panic`, `fatal`, `error`, `warning`,
`info` (por defecto), `verbose`, `debug`, `trace`.

Combinación recomendada para trabajar: `-hide_banner -loglevel warning -stats`. Ves los avisos y el
progreso, sin las 30 líneas de metadatos.

### De video

```bash
-c:v libx264        # códec H.264 (compatible con todo)
-c:v libx265        # H.265/HEVC (mitad de peso, menos compatible)
-crf 18             # calidad constante. 18 = casi indistinguible, 23 = normal, 28 = feo
-preset slow        # esfuerzo de compresión: ultrafast..veryslow
-pix_fmt yuv420p    # OBLIGATORIO para que se reproduzca en todas partes (ver 109)
-r 30               # fotogramas por segundo de salida
-b:v 8M             # bitrate fijo (usa esto solo si la plataforma lo exige)
-movflags +faststart # mueve el índice al inicio: arranca sin descargar todo
```

**CRF vs bitrate.** CRF le dice a ffmpeg "dame esta calidad, gasta los bits que necesites". Bitrate le
dice "gasta estos bits, la calidad que salga". Para redes usa CRF casi siempre. La escala es
logarítmica: bajar 6 puntos duplica el tamaño.

**Preset.** Solo cambia cuánto se demora, no la calidad objetivo: `slow` con CRF 20 pesa menos que
`fast` con CRF 20, con la misma calidad visual. Exportes finales `slow`, pruebas `veryfast`.

### De audio

```bash
-c:a aac            # el estándar para mp4
-b:a 192k           # bitrate de audio. 128k mínimo, 192k bueno, 320k innecesario
-ar 48000           # frecuencia de muestreo. 48 kHz es el estándar de video
-ac 2               # canales: 2 = estéreo, 1 = mono
-an                 # elimina el audio por completo
-vn                 # elimina el video por completo
```

### De tiempo

```bash
-ss 00:01:23.500    # punto de inicio
-t 15               # duración (segundos o hh:mm:ss)
-to 00:01:38.500    # punto final (cuidado, ver 101)
-shortest           # termina cuando el flujo más corto se acabe
```

---

## ffprobe: mirar antes de tocar

`ffprobe` viene con ffmpeg y no modifica nada. Solo lee y reporta. **Úsalo antes de cada comando
importante.** La mitad de los errores de ffmpeg se evitan sabiendo qué hay realmente en el archivo.

```bash
ffprobe -v error -show_format -show_streams entrada.mp4
```
Escupe todo: duración, tamaño, bitrate, cada flujo con su códec, resolución, fps, canales.

### Las consultas que usas de verdad

```bash
# Duración exacta en segundos, sin adornos
ffprobe -v error -show_entries format=duration -of csv=p=0 entrada.mp4

# Resolución
ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 entrada.mp4

# Fotogramas por segundo reales (sale como fracción: 30000/1001 = 29.97)
ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 entrada.mp4

# Ficha técnica de una línea
ffprobe -v error -select_streams v:0 \
  -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt,sample_aspect_ratio \
  -of default=noprint_wrappers=1 entrada.mp4

# El archivo, ¿tiene audio?
ffprobe -v error -select_streams a -show_entries stream=codec_name -of csv=p=0 entrada.mp4
```

Si el último comando no devuelve nada, el clip es mudo. Eso explica el 80% de los "el concat me salió
sin sonido".

### Formatos de salida de ffprobe

`-of` (alias de `-print_format`) cambia cómo se imprime: `default` (legible, `clave=valor`),
`default=noprint_wrappers=1:nokey=1` (solo valores), `csv=p=0` (ideal para scripts), `json` (para
procesar con código), `flat` (`streams.stream.0.width=1080`).

```powershell
$dur = ffprobe -v error -show_entries format=duration -of csv=p=0 "entrada.mp4"
Write-Host "Dura $dur segundos"
```

---

## Cómo leer un error de ffmpeg

ffmpeg escupe mucho texto. **El error casi siempre está en las últimas 3 líneas.** Todo lo de arriba
es información del archivo. Lee de abajo hacia arriba.

### Los errores que más vas a ver, y qué significan de verdad

**`No such file or directory`**
La ruta está mal. En Windows suele ser una barra invertida que el shell se comió, un espacio sin
comillas, o una tilde. Encierra siempre las rutas en comillas dobles.

**`Invalid data found when processing input`**
El archivo está corrupto, incompleto o no es lo que dice ser. Comprueba con ffprobe. Si ffprobe
tampoco lo lee, el archivo está roto de verdad.

**`Unknown encoder 'libx265'`**
Tu compilación de ffmpeg no trae ese codificador. Mira qué tienes:
```bash
ffmpeg -hide_banner -encoders | findstr 264
```
En Linux o Git Bash usa `grep` en vez de `findstr`.

**`Filtergraph 'X' was defined for output stream 0:0 but codec copy was selected`**
Pediste filtrar y copiar a la vez. Elige uno.

**`width not divisible by 2`**
Tu escalado o recorte dejó un ancho o alto impar. H.264 con yuv420p no lo permite. Ver `109`.

**`Output file is empty, nothing was encoded`**
Casi siempre: pediste un tramo que no existe. `-ss 90` en un video de 60 segundos. Comprueba con
ffprobe primero.

**`Stream map '1:a:0' matches no streams`**
La entrada 1 no tiene audio, o no tiene tantos flujos como creías. ffprobe.

**`Conversion failed!`**
Es la última línea, no el error. El error real está una o dos líneas arriba.

**`Past duration 0.9 too large` (repetido cientos de veces)**
Es un aviso, no un error. Suele salir con entradas de fps variable. Si el resultado se ve bien,
ignóralo; si no, mira `109` (timestamps).

### El truco de diagnóstico: la salida nula

Cuando quieras que ffmpeg procese todo pero no escriba archivo (para medir o para ver si falla):

```bash
ffmpeg -i entrada.mp4 -f null -
```

Ese `-` final es la salida a la nada. En Windows también funciona `-f null NUL`, pero el guion es
portable y funciona igual en PowerShell.

---

## Comillas y rutas en Windows

Esto no es un detalle: es la causa número uno de comandos que "no hacen nada".

**Reglas prácticas:**

1. Encierra **siempre** las rutas en comillas dobles: `-i "C:\Videos\mi clip.mp4"`.
2. Encierra **siempre** las cadenas de filtros en comillas dobles.
3. Dentro de un filtro, usa comillas simples para los valores: `drawtext=text='Hola mundo'`.
4. En PowerShell el carácter de escape es la tilde invertida `` ` ``, no la barra invertida.
5. Para continuar en varias líneas: `` ` `` en PowerShell, `\` en Bash. No los mezcles.
6. Dentro de un filtro que recibe una ruta (subtitles, movie, lut3d) hay que escapar los dos puntos de
   la unidad (ver `106` y `109`). Lo más simple es hacer `cd` a la carpeta y usar rutas relativas.

```powershell
# PowerShell
ffmpeg -hide_banner -y -i "C:\Videos\bruto.mp4" `
  -vf "scale=1080:1920,format=yuv420p" `
  -c:v libx264 -crf 20 -preset slow -c:a aac -b:a 192k `
  "C:\Videos\salida.mp4"
```

```bash
# Bash / Git Bash
ffmpeg -hide_banner -y -i "/c/Videos/bruto.mp4" \
  -vf "scale=1080:1920,format=yuv420p" \
  -c:v libx264 -crf 20 -preset slow -c:a aac -b:a 192k \
  "/c/Videos/salida.mp4"
```

---

## Una plantilla de exporte que puedes usar hoy

Para redes verticales (Reels, TikTok, Shorts), desde cualquier fuente:

```bash
ffmpeg -hide_banner -y -i entrada.mp4 \
  -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p" \
  -c:v libx264 -crf 20 -preset slow -profile:v high -level 4.1 \
  -c:a aac -b:a 192k -ar 48000 -ac 2 \
  -movflags +faststart \
  salida_vertical.mp4
```

Qué hace cada pieza:

- `scale=...:force_original_aspect_ratio=increase` — agranda hasta cubrir el lienzo sin deformar
- `crop=1080:1920` — recorta el sobrante centrado
- `fps=30` — fija la cadencia (importante si la fuente es de fps variable)
- `format=yuv420p` — compatibilidad universal
- `-profile:v high -level 4.1` — perfil que aceptan todos los teléfonos
- `-movflags +faststart` — el video arranca sin esperar la descarga completa

Guarda esta plantilla. El 70% de los exportes salen de aquí cambiando dos números.

---

## Errores comunes

- **Poner una opción después de la salida.** Todo lo que va después del nombre del archivo de salida
  se ignora o se interpreta como otra salida. La salida va SIEMPRE de última.
- **Olvidar `-map` con varias entradas.** ffmpeg elige por ti y descarta lo demás sin decirte nada.
- **Recodificar cuando bastaba `-c copy`.** Diez minutos de espera y pérdida de calidad por nada.
- **Copiar cuando hacía falta recodificar.** Pusiste `-c copy` con un `-vf` y ffmpeg te lo rechazó, o
  peor: el corte salió desplazado porque cayó en el keyframe anterior.
- **Leer el error desde arriba.** Las primeras 25 líneas son la ficha del archivo. El error está abajo.
- **Confiar en la extensión.** Un `.mp4` puede traer adentro HEVC que tu editor no abre. ffprobe primero.
- **No usar comillas en rutas con espacios.** `C:\Mis Videos\clip.mp4` sin comillas es dos argumentos.
- **Mezclar `\` de Bash con `` ` `` de PowerShell** al partir un comando en varias líneas.
- **Sobrescribir el archivo de entrada.** `ffmpeg -i a.mp4 -c copy a.mp4` destruye el original. Nunca
  uses el mismo nombre en entrada y salida.
- **Usar `-y` en un script que corre sobre material único** sin tener copia del bruto.
- **Ignorar los `warning`.** Un aviso de timestamps hoy es un audio desincronizado mañana.
- **Asumir el fps.** `r_frame_rate` de `30000/1001` es 29.97, no 30. Si mezclas ambos, el concat falla.

---

## Checklist

- [ ] Corrí `ffprobe` sobre **cada** entrada antes de escribir el comando.
- [ ] Sé la duración exacta, la resolución, el fps y el `pix_fmt` de lo que voy a procesar.
- [ ] Verifiqué si el clip tiene audio (o si es mudo) antes de mapearlo.
- [ ] Las opciones de entrada están antes de `-i` y las de salida después.
- [ ] Si hay más de una entrada, mapeé explícitamente con `-map`.
- [ ] Decidí conscientemente entre `-c copy` y recodificar, y sé por qué.
- [ ] Si recodifico, hago **todas** las operaciones en un solo comando, no en cadena de archivos.
- [ ] Incluí `-pix_fmt yuv420p` en cualquier salida destinada a reproducirse fuera de mi PC.
- [ ] Incluí `-movflags +faststart` en los mp4 que se van a subir.
- [ ] Todas las rutas y todas las cadenas de filtro van entre comillas dobles.
- [ ] El archivo de salida tiene un nombre distinto al de entrada.
- [ ] Usé `-hide_banner -loglevel warning -stats` para poder ver los avisos reales.
- [ ] Si algo falló, leí las **últimas** tres líneas, no las primeras.
- [ ] Comprobé el resultado con `ffprobe` (duración, resolución, presencia de audio), no solo por el
      peso del archivo.
