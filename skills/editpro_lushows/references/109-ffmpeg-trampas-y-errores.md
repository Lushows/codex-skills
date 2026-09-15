# 109 — Trampas y errores: lo que te va a costar una tarde si no lo sabes

Este módulo no enseña a hacer algo: enseña a **no perder tres horas**. Cada trampa está verificada en
producción y todas comparten lo mismo: **fallan sin decirte por qué**, o no fallan y producen un
archivo malo que descubres tarde. Vuelve aquí cada vez que algo "debería funcionar y no funciona".

---

## 1 — El BOM que rompe el concat en PowerShell

**Síntoma:** generas `lista.txt` desde PowerShell y ffmpeg responde
`lista.txt: Invalid data found when processing input`, o ignora la primera línea y une un clip menos.

**Causa:** en **PowerShell 5.1** (el de Windows 10), `-Encoding utf8` escribe UTF-8 **con BOM**: tres
bytes invisibles (`EF BB BF`) al inicio. El demuxer `concat` **no los tolera** delante de la primera
directiva `file`, y no lo dice. Afecta a `Add-Content`, `Set-Content` y `Out-File`.

**Diagnóstico:**
```powershell
Get-Content "lista.txt" -Encoding Byte -TotalCount 3   # 239 187 191 = tienes BOM
```

**Soluciones:**
```powershell
# A: ascii no lleva BOM (descarta caracteres no ASCII)
Get-ChildItem "clip*.mp4" | Sort-Object Name |
  ForEach-Object { "file '$($_.Name)'" } | Set-Content -Encoding ascii -Path "lista.txt"

# B: UTF-8 sin BOM de verdad (acepta tildes)
$lineas = Get-ChildItem "clip*.mp4" | Sort-Object Name | ForEach-Object { "file '$($_.Name)'" }
[IO.File]::WriteAllLines("$PWD\lista.txt", $lineas, (New-Object System.Text.UTF8Encoding($false)))
```

**Sub-trampa de B:** `[IO.File]::WriteAllLines` usa el directorio de .NET, no el de PowerShell. Con
ruta relativa el archivo aparece en `System32`. Por eso `"$PWD\..."`, siempre absoluta.

**No es solo el concat.** El mismo BOM rompe `-filter_complex_script`, el `textfile=` de `drawtext`,
y los `.ass`/`.srt` (libass se come `[Script Info]` y el archivo entero deja de funcionar).
**Regla: todo archivo de texto que le des a ffmpeg va sin BOM.**

---

## 2 — El concat con -c copy exige clips IDÉNTICOS

**Síntoma:** el concat produce un archivo y a partir del segundo clip se ve mal, se congela, se ve
verde o el audio desaparece. O sale `Non-monotonous DTS in output stream`.

**Causa:** `-c copy` no decodifica: pega flujos comprimidos uno tras otro. Todos los segmentos deben
compartir **exactamente** códec de video, resolución, fps, `pix_fmt`, **SAR**, perfil/nivel, códec de
audio, frecuencia de muestreo y canales. Un clip a 29.97 entre clips a 30 basta para romperlo.

**Diagnóstico:**
```powershell
Get-ChildItem "clip*.mp4" | ForEach-Object {
  $v = ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt,sample_aspect_ratio -of csv=p=0 $_.FullName
  $a = ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,sample_rate,channels -of csv=p=0 $_.FullName
  "{0,-22} V[{1}] A[{2}]" -f $_.Name, $v, $a
}
```
Si las columnas no son idénticas, **no puedes copiar**. Normaliza primero con el mismo comando para
todos (`fps`, `scale`, `crop`, `setsar=1`, `format=yuv420p`, mismo códec y perfil de audio), y a los
clips mudos dales silencio, porque uno sin pista de audio corta el audio del resto:
```bash
ffmpeg -y -i mudo.mp4 -f lavfi -i anullsrc=r=48000:cl=stereo \
  -map 0:v:0 -map 1:a:0 -shortest -c:v copy -c:a aac -b:a 192k con_silencio.mp4
```
**Verificación obligatoria:** duración del resultado contra la suma de las partes.

---

## 3 — -ss antes o después de -i

| Posición | Velocidad | Precisión |
|---|---|---|
| **antes** de `-i`, recodificando | instantánea | **exacta** (desde ffmpeg 2.1) |
| **antes** de `-i`, con `-c copy` | instantánea | cae en el keyframe más cercano |
| **después** de `-i` | lenta (decodifica todo) | exacta |

**Si recodificas, pon `-ss` antes de `-i`.** Tienes velocidad y precisión. Mucha gente lo pone después
"porque es más exacto" y espera 6 minutos por nada. Con `-c copy` no hay forma de ser exacto: o
aceptas el keyframe, o recodificas.

---

## 4 — -t es más seguro que -to

La semántica de `-to` **cambia según dónde vaya y según la versión de ffmpeg**: en unas cuenta desde
el inicio del archivo original, en otras desde donde `-ss` te dejó. Sin revisar tu versión exacta, no
puedes predecir el resultado. `-t` significa **siempre** "cuánto dura el tramo que sale".

```bash
ffmpeg -ss 10 -i entrada.mp4 -to 20 -c:v libx264 -crf 18 tramo.mp4   # AMBIGUO
ffmpeg -ss 10 -i entrada.mp4 -t 10 -c:v libx264 -crf 18 tramo.mp4    # INEQUIVOCO
```
Si piensas en entrada y salida, haz la resta tú: `duracion = salida - entrada`.

---

## 5 — Pedir un tramo que no existe

**Síntoma:** `Output file is empty, nothing was encoded`. O peor: un mp4 de 0 segundos que existe y
pasa desapercibido dentro de un lote de 40.

**Causa:** pediste `-ss 90 -t 15` sobre un archivo de 85 segundos. ffmpeg no grita.

**Comprueba SIEMPRE con ffprobe antes:**
```powershell
$dur = [double](ffprobe -v error -show_entries format=duration -of csv=p=0 "entrada.mp4")
$inicio = 90.0; $largo = 15.0
if (($inicio + $largo) -gt $dur) { Write-Host "PARA: pides $($inicio+$largo)s y dura $([math]::Round($dur,3))s" }
else { ffmpeg -hide_banner -y -ss $inicio -i "entrada.mp4" -t $largo -c:v libx264 -crf 18 -c:a aac "tramo.mp4" }
```
Y después de cortar por lote, caza las salidas vacías:
```powershell
Get-ChildItem "tramo*.mp4" | ForEach-Object {
  $d = [double](ffprobe -v error -show_entries format=duration -of csv=p=0 $_.FullName)
  if ($d -lt 0.1) { Write-Host "VACIO: $($_.Name)" }
}
```

---

## 6 — Rutas de Windows dentro de los filtros

**Síntoma:** `subtitles`, `lut3d`, `movie` o `amovie` fallan con `Unable to parse option value` o
`No such file or directory`, aunque el archivo existe.

**Causa:** la ruta atraviesa tres parsers. El de argumentos de filtro usa `:` como separador, y en
Windows la ruta empieza con `C:`. Además `\` es carácter de escape.

**La forma que funciona** — barras normales, dos puntos escapados, comillas simples:
```bash
subtitles='C\:/Users/user/Desktop/proyecto/subs.ass'
```
En grafos complejos a veces hace falta doble escape (`C\\:/...`) porque una capa se come una barra.

**La solución sensata: haz `cd` y usa rutas relativas.**
```powershell
Set-Location "C:\Users\user\Desktop\proyecto"
ffmpeg -hide_banner -y -i "entrada.mp4" -vf "subtitles=subs.ass:fontsdir=fonts" -c:v libx264 -crf 20 "salida.mp4"
```
Cero escapado. Organiza los proyectos en carpetas con nombres cortos, sin espacios ni tildes, y la
trampa desaparece para siempre.

---

## 7 — PowerShell no espera al proceso lanzado con &

**Síntoma:** el script corre Chrome o ffmpeg y el siguiente comando falla porque el archivo "no
existe" — aunque un segundo después sí está.

**Causa:** el operador `&` **no siempre espera**, sobre todo con ejecutables que se desprenden. El
script sigue mientras el archivo todavía se escribe.

```powershell
# NO confiable
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --screenshot=out.png "file:///C:/ruta/x.html"

# SI espera
Start-Process -Wait -NoNewWindow -FilePath "C:\Program Files\Google\Chrome\Application\chrome.exe" `
  -ArgumentList '--headless=new','--disable-gpu','--user-data-dir=C:\temp\chrome-1','--window-size=1080,1920','--screenshot=C:\ruta\out.png','file:///C:/ruta/x.html'
if (-not (Test-Path "C:\ruta\out.png")) { throw "Chrome no genero la captura" }
```
Aunque hayas esperado, **verifica que el archivo existe antes de usarlo**.

---

## 8 — Reutilizar --user-data-dir en Chrome headless

**Síntoma:** generas tarjetas gráficas en un bucle. La primera sale bien; de la segunda en adelante el
PNG no se genera, o sale vacío, o el comando retorna al instante sin hacer nada.

**Causa:** Chrome detecta que ya hay una instancia con ese perfil y **le pasa la petición a la
instancia existente y se cierra**. Esa instancia ignora los argumentos de captura. Resultado: nada.

**Solución: un perfil distinto por llamada, borrado después.**
```powershell
$chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$i = 0
foreach ($html in Get-ChildItem "tarjetas\*.html") {
  $i++
  $perfil = Join-Path $env:TEMP "chrome-render-$i-$(Get-Random)"
  $salida = (Resolve-Path "render").Path + "\tarjeta_$i.png"
  $url = "file:///" + ($html.FullName -replace '\\','/')
  Start-Process -Wait -NoNewWindow -FilePath $chrome -ArgumentList `
    '--headless=new','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=2',
    "--user-data-dir=$perfil",'--window-size=1080,1920',"--screenshot=$salida",$url
  Remove-Item -Recurse -Force $perfil -ErrorAction SilentlyContinue
  if (-not (Test-Path $salida)) { Write-Host "FALLO en $($html.Name)" }
}
```
Claves: perfil único, `-Wait`, ruta **absoluta** en `--screenshot`, verificación después.

---

## 9 — Sin yuv420p el video no se reproduce en ningún lado

**Síntoma:** se ve perfecto en VLC en tu PC. Por WhatsApp sale negro, Instagram lo rechaza, QuickTime
no muestra imagen.

**Causa:** libx264 conserva el formato de píxel de la entrada. Si algún filtro trabajó en RGB
(overlay con PNG, drawtext, blend) o la fuente era yuv444p, la salida queda ahí. **H.264 en esos
formatos solo lo decodifican reproductores de escritorio por software.** Los decodificadores por
hardware de teléfonos, navegadores y plataformas solo aceptan `yuv420p`.

```bash
-pix_fmt yuv420p          # como opcion de salida
-vf "...,format=yuv420p"  # al final de la cadena de filtros
```
Ponlo en los dos sitios: no se estorban. Y añade el perfil compatible:
`-c:v libx264 -profile:v high -level 4.1 -pix_fmt yuv420p`.

**Verificación:**
```bash
ffprobe -v error -select_streams v:0 -show_entries stream=pix_fmt -of csv=p=0 salida.mp4
```

---

## 10 — Dimensiones impares

```
[libx264 @ ...] width not divisible by 2 (1079x1920)
```
`yuv420p` submuestrea el color a la mitad en cada eje: un ancho o alto impar no se puede dividir.

```bash
scale=1080:-2                                   # -2 redondea al par mas cercano
scale='trunc(iw/2)*2':'trunc(ih/2)*2'           # fuerza par lo que sea
crop='iw-mod(iw,2)':'ih-mod(ih,2)'              # recorta un pixel si hace falta
pad='ceil(iw/2)*2':'ceil(ih/2)*2'               # añade un pixel si hace falta
```
**Nunca uses `-1` en `scale`. Usa `-2`.** No hay ningún caso en que `-1` sea mejor.

---

## 11 — Sin faststart el video no arranca hasta descargarse entero

El mp4 guarda su índice (átomo `moov`) al **final** por defecto. El reproductor lo necesita para saber
qué hay adentro, así que espera a la descarga completa.

```bash
-movflags +faststart
```
Mueve el índice al principio en una pasada rápida al terminar. **Ponlo en TODA salida mp4 destinada a
la web o a redes.** No tiene contraindicaciones.

---

## 12 — Timestamps rotos

**Síntomas:** audio desincronizado que empeora con el tiempo, `Non-monotonous DTS in output stream`,
`Past duration too large` repetido cientos de veces, video que salta o se congela a tramos.

**Causas:** fuente con fps variable (grabación de pantalla, OBS, WhatsApp, algunos celulares); cortar
con `-ss` sin reiniciar timestamps antes de filtrar; concat de clips que no arrancan en cero; archivo
grabado con corte de corriente.

**Curas, de menos a más agresiva:**
```bash
-vf "fps=30,..."                                  # 1. cadencia constante (prueba esta primero)
-vf "setpts=PTS-STARTPTS" -af "asetpts=PTS-STARTPTS"  # 2. reiniciar al cortar y filtrar
-fps_mode cfr -r 30                               # 3. forzar CFR (en ffmpeg 5 y anteriores: -vsync cfr)
-avoid_negative_ts make_zero                      # 4. evitar timestamps negativos al copiar
-fflags +genpts                                   # 5. regenerar timestamps
-af "aresample=async=1000:first_pts=0"            # 6. corregir deriva progresiva del audio
ffmpeg -y -fflags +genpts -i roto.mp4 -c copy -avoid_negative_ts make_zero reparado.mp4   # 7.
```
**Diagnóstico de fps variable** — si los dos valores no coinciden, lo es:
```bash
ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate,avg_frame_rate -of csv=p=0 entrada.mp4
```

---

## 13 — -shortest y los renders infinitos

`-loop 1` sobre una imagen genera fotogramas **para siempre**. Si nada le pone límite, ffmpeg codifica
hasta llenar el disco. Límites: `-shortest`, `-t 30`, `-loop 1 -t 5 -i img.png`, o
`overlay=...:eof_action=pass` para que overlay no dependa de la imagen.

**Sub-trampa:** `-shortest` decide sobre el flujo más corto **de los que se escriben**. Si el corto es
la música, tu video se corta con ella.
```bash
# La musica manda: dura 30 s
ffmpeg -y -i video_60s.mp4 -i musica_30s.mp3 -map 0:v -map 1:a -shortest salida.mp4

# El video manda: la musica se rellena con silencio. Dura 60 s.
ffmpeg -y -i video_60s.mp4 -i musica_30s.mp3 -filter_complex "[1:a]apad[a]" \
  -map 0:v -map "[a]" -shortest -c:v copy -c:a aac salida.mp4
```
`apad` + `-shortest` es lo que quieres el 90% de las veces. Y `-shortest` a veces corta uno o dos
fotogramas de más: si la precisión importa, añade `-t` con la duración exacta.

---

## 14 — Filtrar y copiar a la vez

```
Filtergraph 'volume=2' was defined for audio output stream 0:1 but codec copy was selected.
```
Elige uno. Y aprovecha para copiar el flujo que **no** estás tocando:
```bash
ffmpeg -y -i entrada.mp4 -af "loudnorm=I=-14:TP=-1" -c:v copy -c:a aac -b:a 192k salida.mp4
ffmpeg -y -i entrada.mp4 -vf "scale=1080:-2" -c:v libx264 -crf 20 -c:a copy salida.mp4
```

---

## 15 — Sobrescribir el archivo de entrada

```bash
ffmpeg -y -i a.mp4 -c copy a.mp4    # ESTO DESTRUYE a.mp4
```
ffmpeg abre la salida para escritura **antes** de terminar de leer la entrada. Escribe a temporal y
renombra:
```powershell
ffmpeg -hide_banner -y -i "a.mp4" -c:v copy -af "loudnorm=I=-14:TP=-1" -c:a aac "a_tmp.mp4"
if (Test-Path "a_tmp.mp4") { Move-Item -Force "a_tmp.mp4" "a.mp4" }
```

---

## 16 — La rotación del celular

Los celulares graban **en horizontal** con un metadato que dice "gírame 90 grados". ffmpeg autorrota
al decodificar desde la 2.7, así que al recodificar suele salir bien. Pero con `-c copy` el metadato
se copia y algunas plataformas lo ignoran; y si aplicas un `crop` con números pensados para la
orientación visible, no corresponden.

```bash
ffprobe -v error -select_streams v:0 -show_entries stream_side_data=rotation -of default=nw=1 entrada.mp4
ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 entrada.mp4
```
Si `width` es mayor que `height` pero se ve vertical, hay rotación por metadato. Cura limpia:
```bash
ffmpeg -hide_banner -y -i celular.mp4 -vf "scale=1080:-2,setsar=1,format=yuv420p" \
  -metadata:s:v:0 rotate=0 -c:v libx264 -crf 20 -c:a aac -b:a 192k normalizado.mp4
```
Para el crudo sin rotar (raro): `-noautorotate` **antes** de `-i`.

---

## 17 — 30 no es lo mismo que 29.97

`30000/1001` = 29.97 (NTSC). `30/1` = 30 exactos. Mezclarlos en un concat con `-c copy` rompe la
sincronía progresivamente: al minuto hay dos fotogramas de desfase, a los diez son veinte. Decide un
fps y fuerza todo con `-vf "fps=30,..."`. Elige 30 para redes.

---

## 18 — Mezclar 44.1 kHz con 48 kHz

La música descargada suele venir a 44.1 kHz; el audio de video es 48 kHz. Sin igualar, ffmpeg inserta
un `auto_aresample` o el audio se acelera. Pon `[1:a]aresample=48000[m]` y `-ar 48000` en la salida.

---

## 19 — amix baja el volumen sin avisar

Por defecto `amix` divide entre el número de entradas: con 2, todo suena a la mitad. Usa
`amix=inputs=2:duration=first:normalize=0`, controla el volumen pista por pista antes, y cierra con
`alimiter=limit=0.95`.

---

## 20 — loudnorm remuestrea a 192 kHz

`loudnorm` trabaja internamente a 192 kHz y **deja la salida ahí**. Un AAC a 192 kHz es raro y algunos
reproductores lo rechazan. **Añade siempre `-ar 48000` después de usar `loudnorm`.**

---

## 21 — -loglevel error esconde problemas reales

Los avisos de ffmpeg son informativos de verdad: `Non-monotonous DTS`, `Past duration too large`,
`fontselect: not found`. Usa **`-hide_banner -loglevel warning -stats`**: ves avisos y progreso sin
las 30 líneas de arranque. Cuando algo salga raro, sube a `-v debug` para ver qué filtros insertó
ffmpeg por su cuenta.

---

## 22 — El disco lleno no da error claro

Si el disco se llena a mitad del render, ffmpeg puede terminar "bien" con un archivo truncado.
```powershell
$esperada = 28.5
$real = [double](ffprobe -v error -show_entries format=duration -of csv=p=0 "salida.mp4")
if ([math]::Abs($real - $esperada) -gt 0.5) { Write-Host "SOSPECHOSO: esperaba $esperada, salio $real" }
```

---

## 23 — Copiar AAC desde MPEG-TS

Al copiar AAC de un `.ts` a un `.mp4` el resultado no se reproduce: falta el filtro de flujo de bits.
```bash
ffmpeg -y -i entrada.ts -c copy -bsf:a aac_adtstoasc salida.mp4
ffmpeg -y -i entrada.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts salida.ts
```

---

## 24 — Nombres con espacios, tildes y emoji

Espacios rompen el comando sin comillas. Tildes y ñ rompen la lista del concat escrita en ASCII.
Emoji rompen casi todo. El apóstrofo rompe la lista del concat (hay que escaparlo como `'\''`).

**Regla profesional: renombra el material al ingestarlo.** Nombres cortos, ASCII, sin espacios.
```powershell
$i = 0
Get-ChildItem "*.mp4" | Sort-Object LastWriteTime | ForEach-Object {
  $i++; Copy-Item $_.FullName ("bruto\{0:d3}.mp4" -f $i)
}
```

---

## 25 — CRF, preset y bitrate mal entendidos

`-preset` **no cambia la calidad objetivo**, solo el esfuerzo: `slow` con CRF 20 se ve igual que
`fast` con CRF 20, pero pesa menos. Pruebas: `-preset veryfast -crf 28`. Entrega: `-preset slow -crf
19`. Nunca `placebo`. Y si pones `-b:v`, el CRF se ignora: no los mezcles.

---

## La plantilla que evita casi todas estas trampas

```bash
ffmpeg -hide_banner -loglevel warning -stats -y \
  -i entrada.mp4 \
  -vf "fps=30,scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,setsar=1,format=yuv420p" \
  -c:v libx264 -crf 20 -preset slow -profile:v high -level 4.1 -pix_fmt yuv420p \
  -af "loudnorm=I=-14:TP=-1.0:LRA=11" \
  -c:a aac -b:a 192k -ar 48000 -ac 2 \
  -movflags +faststart \
  salida.mp4
```
Cubre fps variable, deformación, dimensiones impares, SAR, formato de píxel, perfil compatible,
loudness, frecuencia de muestreo y faststart.

---

## Errores comunes

Los patrones de fondo detrás de las 25 trampas, para que reconozcas la categoría cuando aparezca una
nueva:

- **Dar por hecho que "no dio error" significa "salió bien".** ffmpeg produce archivos vacíos,
  truncados, mudos o irreproducibles sin quejarse. Verifica el resultado, no el retorno del comando.
- **Confiar en archivos de texto escritos por PowerShell.** El BOM invisible rompe concat,
  filter_complex_script, textfile, ass y srt.
- **Suponer que dos archivos "iguales" lo son.** Un fps, una SAR o un `pix_fmt` distinto revienta
  cualquier operación que copie flujos. ffprobe primero, siempre.
- **Olvidar que la posición de las opciones cambia su significado.** `-ss`, `-to`, `-r`, `-c`: antes o
  después de `-i` no es lo mismo.
- **Pelear con el escapado de rutas en vez de hacer `cd`.** Estructura el proyecto y usa relativas.
- **Asumir que un proceso lanzado ya terminó.** `Start-Process -Wait` y `Test-Path` después.
- **Entregar sin `-pix_fmt yuv420p` ni `-movflags +faststart`.** Se ve bien solo en tu PC.
- **Dejar bucles sin límite.** `-loop 1` sin `-shortest` ni `-t` codifica hasta llenar el disco.
- **Aceptar los valores por defecto de los filtros de mezcla.** `amix` divide el volumen, `loudnorm`
  remuestrea a 192 kHz, `overlay` congela la última capa.
- **Silenciar los avisos con `-loglevel error`.** Los `warning` de ffmpeg son los que anuncian el
  problema que descubrirás mañana.

---

## Checklist

- [ ] Todos los archivos de texto que le doy a ffmpeg están **sin BOM** (verificado en bytes).
- [ ] Antes de unir, comparé códec, resolución, fps, `pix_fmt` y SAR de todos los clips.
- [ ] Ningún clip de la lista es mudo, o le añadí silencio.
- [ ] Verifiqué con ffprobe que ningún `-ss + -t` excede la duración real.
- [ ] Uso `-t` en vez de `-to` cuando hay `-ss` de por medio.
- [ ] Con recodificación, `-ss` va antes de `-i`.
- [ ] Hice `cd` a la carpeta del proyecto: cero rutas absolutas dentro de filtros.
- [ ] Los nombres de archivo son cortos, ASCII, sin espacios ni tildes.
- [ ] Los procesos externos se lanzan con `Start-Process -Wait -NoNewWindow` y verifico la salida.
- [ ] Cada llamada a Chrome headless usa su propio `--user-data-dir`, y lo borro después.
- [ ] La salida lleva `-pix_fmt yuv420p` y `format=yuv420p` al final de la cadena.
- [ ] La salida lleva `-movflags +faststart` si va a la web.
- [ ] Ningún `scale` usa `-1`.
- [ ] Si la fuente es de fps variable, `fps=30` es el primer filtro de la cadena.
- [ ] Ningún `-loop 1` queda sin `-shortest` o `-t`.
- [ ] La entrada y la salida tienen nombres distintos.
- [ ] La mezcla lleva `normalize=0` y `alimiter`; después de `loudnorm` va `-ar 48000`.
- [ ] Corrí con `-loglevel warning` y leí los avisos, no solo los errores.
- [ ] **Comparé la duración del resultado con la esperada** y corrí `blackdetect` y `freezedetect`.
