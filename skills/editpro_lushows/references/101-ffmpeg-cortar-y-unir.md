# 101 — Cortar y unir: -ss, -t, -to, concat demuxer y concat filter

Cortar y pegar es el 80% del montaje. En ffmpeg son cuatro herramientas y unas cuantas trampas que
hacen perder tardes enteras. Este módulo las cierra.

---

## Parte 1 — Cortar

### Las tres opciones de tiempo

| Opción | Qué hace | Dónde va |
|---|---|---|
| `-ss` | dónde empieza | antes de `-i` (rápido) o después (lento) |
| `-t` | **cuánto dura** el tramo | después de `-i` (salida) |
| `-to` | en qué momento **termina** | después de `-i` (salida) |

Formatos de tiempo aceptados, todos válidos:

```
15            = 15 segundos
15.5          = 15 segundos y medio
90            = 90 segundos (1 minuto 30)
00:01:30      = 1 minuto 30
00:01:30.250  = 1 minuto 30 y 250 milésimas
01:30         = 1 minuto 30 (mm:ss también se acepta)
```

**Trabaja siempre con tres decimales.** Un corte de montaje se decide en el orden de los 50
milisegundos. `-ss 12` y `-ss 12.080` son cortes distintos.

### -ss antes o después de -i: la diferencia real

```bash
# BÚSQUEDA RÁPIDA (-ss antes de -i)
ffmpeg -ss 60 -i entrada.mp4 -t 10 -c copy tramo.mp4

# BÚSQUEDA EXACTA POR DECODIFICACIÓN (-ss después de -i)
ffmpeg -i entrada.mp4 -ss 60 -t 10 -c:v libx264 -crf 18 -c:a aac tramo.mp4
```

Qué pasa por dentro: **antes de `-i`**, ffmpeg salta directamente en el archivo sin decodificar nada
(instantáneo incluso en un video de dos horas) y se posiciona en el **keyframe** más cercano.
**Después de `-i`**, decodifica desde el segundo 0 y tira fotogramas a la basura hasta llegar al punto
pedido; en un video largo eso son minutos.

**El dato que casi nadie sabe:** desde ffmpeg 2.1, cuando **recodificas**, `-ss` antes de `-i` ya es
exacto al fotograma — salta al keyframe anterior, decodifica en silencio hasta el punto pedido y
empieza a escribir ahí. Velocidad de búsqueda rápida con precisión de búsqueda lenta.

| Situación | Qué usar |
|---|---|
| Recodificando (lo normal en montaje) | `-ss` **antes** de `-i`. Rápido y exacto. |
| Copiando con `-c copy` | `-ss` **antes** de `-i`, y aceptas que el corte caiga en el keyframe |
| Copiando y necesitas precisión | No se puede. Recodifica. |

### Por qué `-c copy` no corta donde le dices

Un video comprimido no guarda fotogramas completos: guarda un fotograma clave (keyframe) cada 2 a 10
segundos y entre medio solo las diferencias. Un fotograma intermedio no se puede reconstruir sin su
keyframe.

Al copiar, ffmpeg no reconstruye nada: solo puede empezar en un keyframe. Si pides el segundo 12.4 y
el keyframe está en el 10.0, o el clip empieza en el 10.0 (2.4 segundos de más), o empieza en el 12.4
con los primeros fotogramas grises o rotos por falta de referencia.

**Cómo saber dónde están tus keyframes:**

```bash
ffprobe -v error -select_streams v:0 -skip_frame nokey \
  -show_entries frame=pts_time -of csv=p=0 entrada.mp4
```

Eso lista el segundo exacto de cada keyframe. Si vas a cortar copiando, corta en esos números.

**Cómo forzar keyframes al exportar el máster**, para que después puedas cortar copiando donde quieras:

```bash
# Un keyframe cada segundo
ffmpeg -i bruto.mp4 -c:v libx264 -crf 18 -g 30 -keyint_min 30 -sc_threshold 0 \
  -c:a aac -b:a 192k master_cortable.mp4
```

Con `-g 30` a 30 fps tienes un keyframe por segundo. El archivo pesa algo más, pero cortar copiando
se vuelve preciso al segundo.

### -t es más seguro que -to

Cuando combinas `-ss` con un final, **usa `-t` (duración), no `-to` (momento final)**. La semántica de
`-to` depende de dónde esté y de cómo interactúe con `-ss`, y ha cambiado entre versiones: en unas se
cuenta desde el inicio del archivo original, en otras desde donde `-ss` te dejó. Sin revisar la
versión exacta, no puedes predecir el resultado. **`-t` siempre es cuánto dura el tramo que sale.**

```bash
# AMBIGUO: ¿termina en el segundo 20 del original o 20 después del corte?
ffmpeg -ss 10 -i entrada.mp4 -to 20 -c:v libx264 -crf 18 -c:a aac tramo.mp4

# INEQUÍVOCO: 10 segundos de duración, empezando en el segundo 10
ffmpeg -ss 10 -i entrada.mp4 -t 10 -c:v libx264 -crf 18 -c:a aac tramo.mp4
```

Si piensas en puntos de entrada y salida, haz la resta tú: para un out en `00:02:20.750` desde
`00:02:14.500`, es `-ss 00:02:14.500 -t 6.250`.

Y si de verdad quieres `-to`, úsalo **sin** `-ss` en la entrada, poniendo ambos como opciones de
salida: es el único caso sin ambigüedad.

```bash
ffmpeg -i entrada.mp4 -ss 10 -to 20 -c:v libx264 -crf 18 -c:a aac tramo.mp4
```

### La trampa de pedir más de lo que hay

**Si pides un tramo que excede la duración del archivo, ffmpeg produce una salida vacía o truncada
sin un error claro.** Verás algo como `Output file is empty, nothing was encoded` — o peor, un mp4 de
0 segundos que existe y pasa desapercibido en un lote de 40.

Esto pasa constantemente cuando cortas por lote con tiempos calculados a ojo.

**Siempre comprueba antes:**

```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 entrada.mp4
```

Y en un script, valida:

```powershell
$dur = [double](ffprobe -v error -show_entries format=duration -of csv=p=0 "entrada.mp4")
$inicio = 45.0; $largo = 12.0
if (($inicio + $largo) -gt $dur) {
  Write-Host "PARA: pides hasta $($inicio+$largo)s y el archivo dura $dur s"
} else {
  ffmpeg -hide_banner -y -ss $inicio -i "entrada.mp4" -t $largo `
    -c:v libx264 -crf 18 -preset veryfast -c:a aac "tramo.mp4"
}
```

### Cortar el mismo tramo de video y audio sin desincronizar

Cuando cortas y luego filtras, los timestamps del tramo pueden empezar en un número raro y el audio
se corre. La cura es reiniciar los timestamps a cero:

```bash
ffmpeg -ss 30 -i entrada.mp4 -t 8 \
  -vf "setpts=PTS-STARTPTS" -af "asetpts=PTS-STARTPTS" \
  -c:v libx264 -crf 18 -preset slow -c:a aac -b:a 192k tramo.mp4
```

`setpts=PTS-STARTPTS` significa "réstale a cada fotograma el tiempo del primero", o sea: que el tramo
empiece en 0. `asetpts` hace lo mismo con el audio. **Ponlos siempre que cortes y filtres a la vez.**

### Quitar un pedazo del medio

No hay una opción para "borra del segundo 20 al 25". Se hace cortando dos tramos y uniéndolos, o con
el filtro `trim` en un solo comando:

```bash
ffmpeg -i entrada.mp4 -filter_complex \
"[0:v]trim=0:20,setpts=PTS-STARTPTS[v1]; \
 [0:a]atrim=0:20,asetpts=PTS-STARTPTS[a1]; \
 [0:v]trim=25:40,setpts=PTS-STARTPTS[v2]; \
 [0:a]atrim=25:40,asetpts=PTS-STARTPTS[a2]; \
 [v1][a1][v2][a2]concat=n=2:v=1:a=1[v][a]" \
-map "[v]" -map "[a]" -c:v libx264 -crf 18 -c:a aac salida.mp4
```

Esto quita los 5 segundos entre el 20 y el 25 y pega lo demás. Ver `104` para entender la sintaxis
del grafo.

---

## Parte 2 — Unir

Hay dos formas de unir clips y **no** son intercambiables.

| | concat demuxer | concat filter |
|---|---|---|
| Cómo se invoca | `-f concat -i lista.txt` | `-filter_complex "...concat=..."` |
| Recodifica | no (puede usar `-c copy`) | sí, obligatoriamente |
| Velocidad | segundos | minutos |
| Exige mismos parámetros | **sí, idénticos** | no, los normaliza tú antes |
| Sirve para transiciones | no | sí, es la base |

**Regla:** si los clips salieron del mismo comando de exporte, usa el **demuxer**. Si vienen de
fuentes distintas (celular + cámara + pantalla + stock), usa el **filter**, o normalízalos primero.

---

### Método 1 — concat demuxer (rápido, sin recodificar)

Necesitas un archivo de texto que liste los clips.

`lista.txt`:
```
file 'clip01.mp4'
file 'clip02.mp4'
file 'clip03.mp4'
```

Y el comando:

```bash
ffmpeg -hide_banner -y -f concat -safe 0 -i lista.txt -c copy salida.mp4
```

- `-f concat` — trata el txt como una lista de clips, no como un video
- `-safe 0` — permite rutas absolutas y nombres "raros". Sin esto falla con
  `Unsafe file name`
- `-c copy` — copia sin recodificar

**Reglas del archivo de lista:**

1. Cada línea es `file 'nombre'` con **comillas simples**.
2. Las rutas relativas se resuelven **respecto al archivo de lista**, no respecto a dónde estés parado.
3. Un apóstrofo dentro del nombre se escapa así: `file 'It'\''s.mp4'`. Más fácil: renombra el archivo.
4. Puedes usar `#` para comentarios.
5. Puedes añadir `duration 5` después de un `file` para imágenes fijas.
6. **El archivo NO puede tener BOM.** Esto es crítico y está detallado en `109`.

**Cómo generar la lista bien en PowerShell 5.1** (`Add-Content -Encoding utf8` mete BOM y el demuxer
la rechaza sin explicar por qué):

```powershell
# Mal: mete BOM, ffmpeg falla
# Get-ChildItem *.mp4 | ForEach-Object { "file '$($_.Name)'" } | Add-Content -Encoding utf8 lista.txt

# Bien, opción A: ascii no lleva BOM
Get-ChildItem "clip*.mp4" | Sort-Object Name |
  ForEach-Object { "file '$($_.Name)'" } |
  Set-Content -Encoding ascii -Path "lista.txt"

# Bien, opción B: UTF-8 sin BOM de verdad (acepta tildes en los nombres)
$lineas = Get-ChildItem "clip*.mp4" | Sort-Object Name | ForEach-Object { "file '$($_.Name)'" }
[IO.File]::WriteAllLines("$PWD\lista.txt", $lineas, (New-Object System.Text.UTF8Encoding($false)))
```

Ojo con la opción B: `[IO.File]::WriteAllLines` usa el directorio de trabajo de .NET, que **no es** el
de PowerShell. Por eso va con `$PWD\` delante, siempre en ruta absoluta.

En Bash no hay problema:

```bash
for f in clip*.mp4; do echo "file '$f'"; done > lista.txt
ffmpeg -hide_banner -y -f concat -safe 0 -i lista.txt -c copy salida.mp4
```

**Cómo verificar que la lista está limpia:**

```powershell
# Los tres primeros bytes. Si salen 239 187 191, tienes BOM.
Get-Content "lista.txt" -Encoding Byte -TotalCount 3
```

### Qué exige el demuxer con `-c copy`

Todos los segmentos tienen que compartir, **exactamente**:

- códec de video (todos H.264, o todos HEVC — no mezclados)
- resolución (1080x1920 en todos, no uno de 1080x1922)
- fotogramas por segundo
- `pix_fmt` (yuv420p en todos)
- SAR — relación de aspecto del píxel (`1:1` en todos)
- perfil y nivel del códec (ideal, aunque a veces perdona)
- códec de audio, frecuencia de muestreo, número de canales

Si algo no coincide, hay tres finales posibles, todos malos: ffmpeg falla con `Non-monotonous DTS`;
avisa `Non-matching frame parameters` y produce un archivo que se ve mal a partir del segundo clip; o
no dice nada y el resultado tiene el audio desfasado o congelado desde cierto punto.

**Cómo comprobar de un vistazo si tus clips son compatibles:**

```powershell
Get-ChildItem "clip*.mp4" | ForEach-Object {
  $info = ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt,sample_aspect_ratio -of csv=p=0 $_.FullName
  "{0,-22} {1}" -f $_.Name, $info
}
```
```bash
for f in clip*.mp4; do
  echo -n "$f  "
  ffprobe -v error -select_streams v:0 \
    -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt,sample_aspect_ratio -of csv=p=0 "$f"
done
```
Si las líneas no son idénticas de la segunda columna en adelante, **no** uses `-c copy`.

### Normalizar antes de unir (la solución de verdad)

Cuando los clips no coinciden, la jugada profesional es pasarlos todos por el mismo molde y **luego**
unirlos copiando. Es rápido, predecible y te deja segmentos reutilizables.

```bash
# Un molde para todos: 1080x1920, 30 fps, yuv420p, SAR 1:1, audio 48 kHz estéreo
for f in bruto*.mp4; do
  ffmpeg -hide_banner -y -i "$f" \
    -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1,format=yuv420p" \
    -c:v libx264 -crf 18 -preset slow -profile:v high -level 4.1 \
    -c:a aac -b:a 192k -ar 48000 -ac 2 \
    "norm_${f}"
done
```

Y si algún clip viene mudo, agrégale silencio para que el audio no se corte al unir:

```bash
ffmpeg -hide_banner -y -i mudo.mp4 -f lavfi -i anullsrc=r=48000:cl=stereo \
  -map 0:v:0 -map 1:a:0 -shortest \
  -c:v copy -c:a aac -b:a 192k con_silencio.mp4
```

`anullsrc` es un generador de silencio. Sin esto, un clip mudo en medio de una lista rompe el concat.

---

### Método 2 — concat filter (recodifica, pero perdona)

El filtro `concat` une flujos **dentro** del grafo de filtros. Como todo pasa por decodificación, no
exige que los archivos sean idénticos — pero sí exige que los flujos que entran al filtro tengan la
misma resolución y `pix_fmt`, así que normalmente escalas dentro del mismo comando.

```bash
ffmpeg -hide_banner -y -i a.mp4 -i b.mp4 -i c.mp4 -filter_complex \
"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30[v0]; \
 [1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30[v1]; \
 [2:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30[v2]; \
 [0:a]aresample=48000[a0];[1:a]aresample=48000[a1];[2:a]aresample=48000[a2]; \
 [v0][a0][v1][a1][v2][a2]concat=n=3:v=1:a=1[v][a]" \
-map "[v]" -map "[a]" \
-c:v libx264 -crf 20 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart \
salida.mp4
```

Sintaxis del filtro:

- `concat=n=3` — tres segmentos
- `v=1:a=1` — cada segmento aporta 1 flujo de video y 1 de audio
- El **orden de las etiquetas de entrada importa**: van intercaladas por segmento
  (`[v0][a0][v1][a1][v2][a2]`), no agrupadas por tipo. Este es el error clásico.
- Salen dos etiquetas: `[v]` y `[a]`, que hay que mapear.

**Solo video, sin audio:**

```bash
ffmpeg -y -i a.mp4 -i b.mp4 -filter_complex \
"[0:v][1:v]concat=n=2:v=1:a=0[v]" -map "[v]" -an -c:v libx264 -crf 20 salida.mp4
```

**Con `unsafe=1`** puedes permitir que los segmentos tengan tamaños distintos, pero el resultado será
un video que cambia de resolución a mitad de camino. No lo uses para entregar: úsalo solo para revisar.

---

### Método 3 — el protocolo concat (para MPEG-TS)

Para material en `.ts`, `.mts` o `.m2ts` de cámaras, existe el protocolo `concat:`, que pega los
archivos a nivel de bytes:

```bash
ffmpeg -i "concat:parte1.ts|parte2.ts|parte3.ts" -c copy salida.mp4
```

Funciona solo con formatos que se pueden pegar así (MPEG-TS, algunos MPEG-PS). Con mp4 **no
funciona**, aunque el comando no dé error.

El truco relacionado: convertir mp4 a ts, pegar y volver a mp4, todo sin recodificar.

```bash
ffmpeg -y -i a.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts a.ts
ffmpeg -y -i b.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts b.ts
ffmpeg -y -i "concat:a.ts|b.ts" -c copy -bsf:a aac_adtstoasc salida.mp4
```

Los dos `-bsf` son "filtros de flujo de bits": convierten la forma de empaquetar H.264 y AAC entre
contenedores. Sin ellos el resultado no se reproduce. Este método es más robusto que el demuxer
cuando los clips vienen del mismo hardware pero con cabeceras ligeramente distintas.

---

## Recetas listas

**Cortar 20 segundos desde el minuto 3, recodificando (exacto):**
```bash
ffmpeg -hide_banner -y -ss 00:03:00 -i entrada.mp4 -t 20 \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k tramo.mp4
```

**Cortar sin recodificar, aceptando el keyframe más cercano:**
```bash
ffmpeg -hide_banner -y -ss 00:03:00 -i entrada.mp4 -t 20 -c copy -avoid_negative_ts make_zero tramo.mp4
```

**Partir un video largo en trozos de 60 segundos automáticamente:**
```bash
ffmpeg -hide_banner -y -i largo.mp4 -c copy -f segment -segment_time 60 \
  -reset_timestamps 1 parte_%03d.mp4
```

**Extraer solo el audio de un tramo:**
```bash
ffmpeg -hide_banner -y -ss 45 -i entrada.mp4 -t 30 -vn -c:a pcm_s16le -ar 48000 tramo.wav
```

**Unir todos los mp4 de una carpeta, mismo perfil, sin recodificar (PowerShell):**
```powershell
$lineas = Get-ChildItem "*.mp4" | Sort-Object Name | ForEach-Object { "file '$($_.Name)'" }
[IO.File]::WriteAllLines("$PWD\lista.txt", $lineas, (New-Object System.Text.UTF8Encoding($false)))
ffmpeg -hide_banner -y -f concat -safe 0 -i "lista.txt" -c copy "unido.mp4"
ffprobe -v error -show_entries format=duration -of csv=p=0 "unido.mp4"
```

Esa última línea no es adorno: **compara la duración del resultado con la suma de las partes.** Si no
cuadra, el concat se comió algo.

---

## Errores comunes

- **Usar `-to` junto con `-ss` sin saber qué versión de ffmpeg corres.** Usa `-t` y haz la resta tú.
- **Pedir un tramo que excede la duración.** Sale un archivo vacío sin error claro. ffprobe primero.
- **Cortar con `-c copy` y esperar precisión al fotograma.** No existe. O recodificas, o cortas en
  keyframe.
- **Generar `lista.txt` con `Add-Content -Encoding utf8` en PowerShell 5.1.** Escribe BOM y el
  demuxer la rechaza sin decir por qué. Usa `-Encoding ascii` o `UTF8Encoding($false)`.
- **Olvidar `-safe 0`** cuando la lista tiene rutas absolutas o nombres con espacios.
- **Rutas relativas en la lista mal entendidas.** Se resuelven respecto al txt, no a tu ubicación.
- **Unir con `-c copy` clips de fuentes distintas.** Falla o produce basura. Normaliza primero.
- **Un clip mudo dentro de la lista.** El audio del resultado se corta a partir de ahí. Añádele
  silencio con `anullsrc`.
- **Intercalar mal las etiquetas del filtro concat.** Va `[v0][a0][v1][a1]`, no `[v0][v1][a0][a1]`.
- **Olvidar `setpts=PTS-STARTPTS` / `asetpts=PTS-STARTPTS`** al cortar y filtrar: audio corrido.
- **Usar el protocolo `concat:` con mp4.** No funciona; hay que pasar por MPEG-TS con los `-bsf`.
- **No verificar la duración del resultado.** Es la única prueba de que el concat funcionó de verdad.
- **Nombres con apóstrofo o tilde** dentro de la lista. Renómbralos antes y ahórrate el escapado.

---

## Checklist

- [ ] Corrí `ffprobe` y sé la duración exacta de cada clip.
- [ ] `inicio + duracion` nunca excede la duración real del archivo.
- [ ] Uso `-t` (duración), no `-to`, cuando hay `-ss` de por medio.
- [ ] Si recodifico, `-ss` va **antes** de `-i` (rápido y exacto).
- [ ] Si copio con `-c copy`, acepté que el corte cae en keyframe, o listé los keyframes con ffprobe.
- [ ] Al cortar con filtros, incluí `setpts=PTS-STARTPTS` y `asetpts=PTS-STARTPTS`.
- [ ] Comparé códec, resolución, fps, `pix_fmt` y SAR de todos los clips antes de unirlos.
- [ ] Si no coinciden: normalicé todos con el mismo comando antes de unir.
- [ ] Ningún clip de la lista es mudo (o le añadí silencio con `anullsrc`).
- [ ] `lista.txt` **no tiene BOM** (verificado leyendo los primeros 3 bytes).
- [ ] El comando lleva `-safe 0`.
- [ ] Las etiquetas del filtro concat van intercaladas video-audio por segmento.
- [ ] Verifiqué la duración del archivo unido contra la suma de las partes.
- [ ] Abrí el resultado y revisé el punto exacto de cada unión, no solo el principio.
