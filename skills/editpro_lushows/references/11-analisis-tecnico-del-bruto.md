# 11 — Análisis técnico del bruto

## Qué resuelve

Saber, sin abrir un solo clip en un reproductor, qué tienes entre manos: cuánto dura de verdad cada
archivo, si están todos a la misma resolución y a los mismos fotogramas por segundo, si alguno viene
rotado, cuál trae audio y cuál no, y si el audio está reventado. Todo eso decide el montaje, y todo se
puede leer con un comando.

La razón por la que este módulo va antes de cualquier corte es un error real y caro: **se pidió el tramo
128–136 s de un clip que duraba 101 s.** El comando corrió, no dio error visible, y devolvió un archivo
vacío o congelado. Nadie lo notó hasta el render final. Cinco segundos de `ffprobe` lo habrían evitado.

**ffprobe** es el hermano de ffmpeg que no toca el video: solo lo lee y te cuenta qué hay adentro. Es tu
instrumento de medición.

---

## Las siete preguntas que hay que responder de cada clip

1. ¿Cuánto dura **exactamente**? (en segundos con decimales)
2. ¿Qué resolución tiene? (ancho x alto)
3. ¿A cuántos fps va? (fotogramas por segundo)
4. ¿Viene rotado? (el celular graba horizontal y marca "gírame")
5. ¿Con qué códec está comprimido?
6. ¿Tiene audio? ¿Mono o estéreo?
7. ¿A qué nivel está ese audio? ¿Está saturado?

---

## Duración exacta

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 entrada/clip-01.mp4
```

Devuelve algo como `101.366667`. Ese número, no el que recuerdas, es el techo de cualquier corte.

Desglose de las banderas, porque se repiten en todo el módulo:

- `-v error` — cállate salvo que haya error. Sin esto ffprobe escupe media pantalla de banner.
- `-show_entries format=duration` — muéstrame solo el campo duración del contenedor.
- `-of default=nw=1:nk=1` — formato de salida limpio: `nw` = sin encabezados de sección,
  `nk` = sin el nombre de la clave. Solo el valor.

**Ojo con una trampa:** `format=duration` es la duración del contenedor. En algunos archivos (grabaciones
interrumpidas, streams) la duración real del stream de video es distinta. Cuando la precisión importa:

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=duration,nb_frames -of default=nw=1:nk=1 entrada/clip-01.mp4
```

Si los dos números difieren en más de 0,2 s, confía en el del stream de video y anótalo como clip
sospechoso.

---

## Ficha completa de un clip en un solo comando

```bash
ffprobe -v error -print_format json -show_format -show_streams entrada/clip-01.mp4
```

Escupe un JSON largo. Los campos que importan:

| Campo | Qué es | Por qué importa |
|---|---|---|
| `format.duration` | duración en segundos | techo de los cortes |
| `streams[].codec_type` | `video` o `audio` | detecta clips mudos |
| `streams[].width` / `height` | resolución | mezclar 1080 y 720 obliga a escalar |
| `streams[].r_frame_rate` | fps como fracción, ej. `30000/1001` | mezclar 30 y 60 fps produce saltos |
| `streams[].codec_name` | `h264`, `hevc`, `aac` | HEVC es pesado de editar |
| `streams[].sample_rate` | 44100 / 48000 Hz | mezclar rates produce desincronización |
| `streams[].channels` | 1 = mono, 2 = estéreo | mono en un solo canal = voz que suena de un lado |
| `streams[].side_data_list[].rotation` | -90, 90, 180 | el clip que "se ve acostado" |

---

## Tabla técnica de TODO el bruto de un golpe

Este es el comando que de verdad usas. PowerShell, saca la ficha de cada clip y la deja en CSV:

```powershell
$entrada = "C:\Users\user\Desktop\VIDEO-BOTELLA\entrada"
$salida  = "C:\Users\user\Desktop\VIDEO-BOTELLA\analisis\ficha-tecnica.csv"

$filas = Get-ChildItem $entrada -Filter *.mp4 | Sort-Object Name | ForEach-Object {
  $j = & ffprobe -v error -print_format json -show_format -show_streams $_.FullName | ConvertFrom-Json
  $v = $j.streams | Where-Object { $_.codec_type -eq "video" } | Select-Object -First 1
  $a = $j.streams | Where-Object { $_.codec_type -eq "audio" } | Select-Object -First 1

  $fps = 0
  if ($v.r_frame_rate) {
    $p = $v.r_frame_rate -split "/"
    if ([double]$p[1] -ne 0) { $fps = [math]::Round([double]$p[0] / [double]$p[1], 3) }
  }

  $rot = 0
  if ($v.side_data_list) {
    foreach ($sd in $v.side_data_list) { if ($null -ne $sd.rotation) { $rot = $sd.rotation } }
  }

  [PSCustomObject]@{
    clip      = $_.Name
    segundos  = [math]::Round([double]$j.format.duration, 2)
    ancho     = $v.width
    alto      = $v.height
    fps       = $fps
    rotacion  = $rot
    codec_v   = $v.codec_name
    audio     = if ($a) { $a.codec_name } else { "SIN AUDIO" }
    canales   = if ($a) { $a.channels } else { 0 }
    hz        = if ($a) { $a.sample_rate } else { 0 }
  }
}

$filas | Format-Table -AutoSize
$filas | Export-Csv $salida -NoTypeInformation -Encoding utf8
Write-Output "Ficha en $salida"
```

Lo que buscas al leer esa tabla:

- **Una fila con `SIN AUDIO`** → clip mudo. Sirve como b-roll, no como toma hablada. Si esperabas voz
  ahí, algo pasó con el micrófono: revísalo antes de seguir.
- **fps distintos entre clips** → si mezclas 29,97 y 60 sin normalizar, el montaje da microsaltos.
  Se normaliza todo al fps del entregable con `-r` o con el filtro `fps=`.
- **rotación distinta de 0** → ver la sección de rotación más abajo.
- **resoluciones mezcladas** → decide la resolución del entregable y escala el resto. Nunca subas de
  resolución un clip pequeño: se ve blando. Mejor úsalo como inserto corto.
- **`canales = 1`** → mono. No es un problema en sí, pero al montarlo hay que duplicarlo a los dos lados
  o la voz suena solo por un audífono.

---

## Rotación: el clip que se ve acostado

El celular graba el sensor siempre igual y escribe en los metadatos "al reproducir, gírame 90 grados".
Los reproductores hacen caso. Algunos filtros de ffmpeg **no** hacen caso, y ahí es donde aparece el
video acostado.

Leer la rotación sola:

```bash
ffprobe -v error -select_streams v:0 -show_entries stream_side_data=rotation -of default=nw=1:nk=1 entrada/clip-01.mp4
```

Si devuelve `-90` o `90`, ese clip tiene rotación en metadatos. Para trabajar tranquilo, "quema" la
rotación una vez y guarda un clip normalizado en `trabajo/`:

```bash
ffmpeg -i entrada/clip-01.mp4 -vf "transpose=1" -metadata:s:v rotate=0 -c:v libx264 -crf 18 -preset medium -c:a copy trabajo/clip-01-norm.mp4
```

`transpose=1` gira 90 grados en sentido horario. `transpose=2` es antihorario. `transpose=1,transpose=1`
son 180 grados. El `-metadata:s:v rotate=0` borra la marca para que nadie lo gire dos veces.

Cuál usar depende del signo: rotación `90` en metadatos suele necesitar `transpose=2` para verse derecho,
y `-90` suele necesitar `transpose=1`. **No lo adivines: genera un fotograma de prueba y míralo.**

```bash
ffmpeg -y -ss 1 -i trabajo/clip-01-norm.mp4 -frames:v 1 trabajo/prueba-rotacion.jpg
```

---

## Audio: nivel medio, pico y saturación

**Saturación** (o *clipping*) es cuando el sonido llegó al tope del rango digital, 0 dB, y lo que pasaba
de ahí se cortó en plano. Se oye como distorsión rasposa en las palabras fuertes. No se puede arreglar
después: la información ya no está en el archivo. Se detecta y se decide qué hacer.

```bash
ffmpeg -hide_banner -i entrada/clip-01.mp4 -af volumedetect -f null -
```

En la salida (por stderr) verás algo así:

```
[Parsed_volumedetect_0 @ ...] mean_volume: -23.4 dB
[Parsed_volumedetect_0 @ ...] max_volume: -1.2 dB
[Parsed_volumedetect_0 @ ...] histogram_0db: 0
```

Cómo se lee:

| Medida | Valor sano | Qué significa fuera de rango |
|---|---|---|
| `mean_volume` | -24 a -16 dB | más bajo de -30: grabado muy suave, al subirlo sube el ruido. Más alto de -12: muy caliente. |
| `max_volume` | -6 a -1 dB | `0.0 dB` exacto = tocó el techo. Sospecha saturación. |
| `histogram_0db` | 0 | cuántas muestras quedaron pegadas al tope. Más de unas pocas decenas = saturación real. |

`histogram_0db` es el dato honesto. Un `max_volume: 0.0` con `histogram_0db: 3` es un pico aislado y no
pasa nada. Un `histogram_0db: 4820` es una toma reventada.

### Medir el audio de todo el bruto

```powershell
$entrada = "C:\Users\user\Desktop\VIDEO-BOTELLA\entrada"
$filas = Get-ChildItem $entrada -Filter *.mp4 | Sort-Object Name | ForEach-Object {
  $txt = & ffmpeg -hide_banner -nostats -i $_.FullName -af volumedetect -f null - 2>&1 | Out-String
  $mean = if ($txt -match "mean_volume:\s*(-?[\d\.]+)") { [double]$Matches[1] } else { $null }
  $max  = if ($txt -match "max_volume:\s*(-?[\d\.]+)")  { [double]$Matches[1] } else { $null }
  $h0   = if ($txt -match "histogram_0db:\s*(\d+)")     { [int]$Matches[1] }    else { 0 }

  $diag = "ok"
  if ($null -eq $mean) { $diag = "SIN AUDIO" }
  elseif ($h0 -gt 50)  { $diag = "SATURADO" }
  elseif ($mean -lt -35) { $diag = "MUY BAJO" }
  elseif ($mean -gt -12) { $diag = "MUY CALIENTE" }

  [PSCustomObject]@{ clip=$_.Name; media_db=$mean; pico_db=$max; muestras_0db=$h0; diagnostico=$diag }
}
$filas | Format-Table -AutoSize
$filas | Export-Csv "C:\Users\user\Desktop\VIDEO-BOTELLA\analisis\audio.csv" -NoTypeInformation -Encoding utf8
```

Nota de PowerShell: `2>&1` sobre un ejecutable nativo puede envolver líneas en objetos de error. Aquí se
neutraliza con `| Out-String`, que aplana todo a texto antes de aplicar las expresiones regulares.

---

## Clips mudos y silencios largos

Un clip puede tener pista de audio y estar en silencio (micrófono apagado, cable suelto). `volumedetect`
te lo dice con un `mean_volume` cercano a -91 dB. Para ubicar los silencios dentro de un clip:

```bash
ffmpeg -hide_banner -i entrada/clip-05.mp4 -af "silencedetect=noise=-40dB:d=0.6" -f null -
```

Sale una lista de `silence_start` / `silence_end` / `silence_duration`. Sirve para dos cosas: detectar
material inservible, y encontrar los espacios entre tomas (el actor suele callar dos segundos entre una
toma falsa y la siguiente — ese silencio es la frontera natural del corte).

---

## Detectar cámara tapada, negro o congelado

```bash
ffmpeg -hide_banner -i entrada/clip-09.mp4 -vf "blackdetect=d=0.5:pix_th=0.10" -f null -
ffmpeg -hide_banner -i entrada/clip-09.mp4 -vf "freezedetect=n=-60dB:d=2" -map 0:v -f null -
```

`blackdetect` marca tramos negros de más de medio segundo. `freezedetect` marca tramos donde la imagen
no cambia en 2 segundos o más — típico de un celular que se quedó apuntando a la pared mientras alguien
hablaba fuera de cuadro.

---

## Cambios de plano dentro de un mismo clip

Cuando el clip es largo y sospechas que adentro hay varias tomas:

```bash
ffmpeg -hide_banner -i entrada/clip-12.mp4 -vf "select='gt(scene,0.35)',showinfo" -f null - 2>&1 | findstr "pts_time"
```

Cada `pts_time` es un segundo donde la imagen cambió lo suficiente para considerarse otro plano. Ajusta
el umbral: 0,2 detecta hasta un movimiento de mano; 0,5 solo cambios fuertes.

---

## El semáforo del bruto

Con la ficha técnica y la tabla de audio, clasifica cada clip antes de seguir:

| Color | Criterio | Qué hacer |
|---|---|---|
| Verde | audio en rango, fps y resolución iguales al resto, sin rotación rara | usable tal cual |
| Amarillo | audio bajo, mono, o fps distinto | usable con normalización previa |
| Rojo | sin audio esperando voz, saturado, congelado, o duración que no cuadra | decisión explícita: reponer, usar como b-roll mudo, o descartar |

Esa clasificación va al `mapa-bloques.csv` (módulo 19) como columna `estado`.

---

## Errores comunes

- **Cortar sin comprobar la duración real.** El error de los 128 s en un clip de 101 s. Un `ffprobe` de
  cinco segundos lo evita. Nunca escribas un `-ss`/`-to` sin haber visto la duración del archivo.
- **Confiar en la duración que muestra el explorador de Windows.** Redondea y a veces miente en archivos
  con audio y video de distinta longitud.
- **Ignorar la rotación.** El clip se ve derecho en el reproductor, se ve acostado en el render. Se quema
  la rotación una vez, en `trabajo/`, y se trabaja con el normalizado.
- **Mezclar fps sin normalizar.** 30 y 60 en la misma línea produce un tirón que la gente no sabe nombrar
  pero sí siente. Se normaliza todo al fps del entregable.
- **Subir de resolución un clip de 720p a 1080p y creer que se arregló.** Escalar hacia arriba no inventa
  detalle: solo suaviza. Úsalo corto o en punch-in.
- **Diagnosticar saturación solo con `max_volume`.** Un pico aislado en 0 dB no es saturación. El dato
  que decide es `histogram_0db`.
- **Creer que "se puede arreglar en post" un audio reventado.** No. La información ya no existe. Se
  disimula, no se arregla. Si es la toma clave, hay que regrabar.
- **Asumir que todos los clips traen audio.** Un `SIN AUDIO` en la tabla es una alerta, no un detalle.
- **Correr `volumedetect` sin `-f null -`.** Sin eso ffmpeg intenta escribir un archivo de salida y falla
  o te llena el disco.

---

## Checklist

- [ ] Existe `analisis/ficha-tecnica.csv` con clip, segundos, ancho, alto, fps, rotación, códec, audio,
      canales y Hz
- [ ] Existe `analisis/audio.csv` con media, pico, muestras en 0 dB y diagnóstico
- [ ] Ningún clip queda sin duración medida por ffprobe
- [ ] Los clips con rotación en metadatos están normalizados en `trabajo/` y verificados con un fotograma
- [ ] Sabes cuál es la resolución y el fps objetivo del entregable, y qué clips hay que normalizar
- [ ] Los clips sin audio están identificados y hay decisión sobre cada uno
- [ ] Los clips saturados (`histogram_0db` alto) están marcados y el cliente avisado si son claves
- [ ] Los clips con audio muy bajo están marcados para tratamiento de ganancia antes del montaje
- [ ] Se corrió `blackdetect` / `freezedetect` en los clips largos o sospechosos
- [ ] Cada clip tiene color de semáforo (verde / amarillo / rojo) anotado
- [ ] Ninguna decisión de corte se ha tomado todavía: esto es medición, no montaje
