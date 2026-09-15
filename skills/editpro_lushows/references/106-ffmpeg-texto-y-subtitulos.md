# 106 — Texto y subtítulos: drawtext, ASS, fuentes y el infierno de las rutas en Windows

Hay dos caminos para poner texto en un video, y sirven para cosas distintas:

| | `drawtext` | `subtitles` / `ass` |
|---|---|---|
| Qué es | un filtro que dibuja una cadena | un renderizador de archivos de subtítulos |
| Bueno para | títulos, marcas, contadores, texto animado | subtitulado completo, karaoke |
| Animación | expresiones matemáticas, lo que quieras | lo que permita el formato ASS |
| Cantidad de texto | poco | mucho |

**Regla:** menos de 5 apariciones de texto, `drawtext`. La transcripción de un video entero, genera un
`.ass` y quémalo con `subtitles`.

---

## PARTE 1 — drawtext

```bash
ffmpeg -hide_banner -y -i entrada.mp4 -vf \
"drawtext=fontfile='C\:/Windows/Fonts/arialbd.ttf':text='Hola':fontsize=90:fontcolor=white:x=(w-text_w)/2:y=h-400" \
-c:v libx264 -crf 20 -c:a copy salida.mp4
```
Fíjate en `C\:/Windows/...`: barras normales y **dos puntos escapados**. En Windows no es opcional.

### Parámetros

```
fontfile      ruta al .ttf o .otf
font          nombre de la fuente (solo con fontconfig)
text          el texto literal
textfile      ruta a un archivo con el texto (evita problemas de escapado)
fontsize      tamaño en px
fontcolor     nombre, 0xRRGGBB, o con transparencia: white@0.8
x, y          posición, aceptan expresiones
box / boxcolor / boxborderw    caja detrás del texto y su relleno
borderw / bordercolor          contorno del texto
shadowx / shadowy / shadowcolor
line_spacing  interlineado
alpha         opacidad, acepta expresiones
enable        cuándo se dibuja
text_align    L, C, R, T, M, B
reload        1 para releer textfile en cada fotograma
```

Variables de posición: `w`, `h` (video), `text_w`/`tw`, `text_h`/`th`, `line_h`/`lh`, `t`, `n`.

```bash
x=(w-text_w)/2        # centrado horizontal
x=w-text_w-60         # pegado a la derecha
y=h-text_h-560        # zona segura inferior en vertical de redes
y=220                 # zona segura superior
```

### Un título que se ve bien de verdad

```bash
ffmpeg -hide_banner -y -i entrada.mp4 -vf \
"drawtext=fontfile='fonts/Anton-Regular.ttf':\
text='ESTO CAMBIA TODO':fontsize=112:fontcolor=white:\
borderw=10:bordercolor=0x0F2A22:\
shadowx=6:shadowy=6:shadowcolor=black@0.55:\
x=(w-text_w)/2:y=h-text_h-620:\
enable='between(t,0.4,3.2)'" \
-c:v libx264 -crf 20 -preset slow -pix_fmt yuv420p -c:a copy salida.mp4
```

Por qué cada cosa: **fuente Black/Heavy** (las finas desaparecen tras la compresión de Instagram);
**`borderw=10` en color de marca**, no negro genérico, para que se lea sobre cualquier fondo;
**sombra dura sin difuminar**, que da peso; **`y` por encima de la interfaz**; y **`enable`**, porque
el texto entra y sale, no está toda la duración.

### Caja y barra

```bash
drawtext=...:box=1:boxcolor=0x0F0F0F@0.75:boxborderw=28
```
`boxborderw` es el relleno: 24 a 32 px se ve bien en 1080 de ancho. Sin relleno queda apretado y
barato. Para una barra de ancho completo es mejor `drawbox` antes:

```bash
-vf "drawbox=x=0:y=h-300:w=iw:h=300:color=0x0F0F0F@0.85:t=fill, \
     drawtext=fontfile='fonts/Anton-Regular.ttf':text='Sigue para más':fontsize=64:fontcolor=white:x=60:y=h-210"
```

### Varias líneas

Un salto de línea literal dentro de `text` funciona, pero el escapado duele. Dos alternativas:

**A — `textfile`** (sin BOM, ver `109`):
```bash
drawtext=fontfile='fonts/Anton-Regular.ttf':textfile='titulo.txt':fontsize=90:text_align=C:line_spacing=14:x=(w-text_w)/2:y=400
```

**B — varios `drawtext` encadenados**, uno por línea. Más verboso, pero controlas cada línea por
separado, que es lo que quieres para texto cinético:
```bash
-vf "drawtext=...:text='EL ERROR':fontsize=120:y=h/2-140:enable='between(t,1,4)', \
     drawtext=...:text='QUE TODOS COMETEN':fontsize=84:y=h/2+10:enable='between(t,1.25,4)'"
```
Ese `1.25` de la segunda línea (un cuarto de segundo después) es lo que hace que el texto se sienta
vivo en vez de plano.

### Animación

```bash
# Aparecer y desaparecer con fundido, en una sola expresion
drawtext=...:alpha='clip((t-1)/0.4,0,1)*clip((4.4-t)/0.4,0,1)'

# Entrar deslizando desde abajo
drawtext=...:y='h-text_h-400+120*(1-clip((t-1)/0.5,0,1))'

# Con desaceleracion (se ve profesional: llega frenando)
drawtext=...:y='h-text_h-400+120*pow(1-clip((t-1)/0.5,0,1),2)'
```
Memoriza la envolvente: **`clip((t-inicio)/entrada,0,1) * clip((fin-t)/salida,0,1)`**.

### Texto dinámico

```bash
drawtext=text='%{pts\:hms}':fontsize=48:fontcolor=white:x=40:y=40    # cronometro
drawtext=text='Frame %{n}':fontsize=40:x=40:y=100
drawtext=text='%{eif\:t\:d\:2}s':fontsize=40:x=40:y=160              # segundos con 2 decimales
drawtext=text='%{localtime\:%d-%m-%Y}':fontsize=40:x=40:y=220
```
Los `:` dentro de `%{...}` **hay que escaparlos**, porque el parser del filtro los usa de separador.

`%{pts:hms}` es la herramienta de diagnóstico más útil que existe: quema el reloj sobre el video y
puedes decir "el corte está mal en 00:00:14.320" en vez de "por ahí".

```bash
ffmpeg -hide_banner -y -i corte.mp4 -vf \
"drawtext=fontfile='C\:/Windows/Fonts/consola.ttf':text='%{pts\:hms}':fontsize=44:fontcolor=yellow:box=1:boxcolor=black@0.6:boxborderw=10:x=20:y=20" \
-c:v libx264 -crf 26 -preset veryfast -c:a copy revision.mp4
```

### Escapado dentro de text

`\:` para dos puntos, `\,` para coma, `\%` para porcentaje, `\\\\` para barra invertida. El apóstrofo
es el que más duele. **Si el texto lleva apóstrofos, tildes, comillas o signos, usa `textfile`.**
Peleas cinco minutos con el escapado o escribes un archivo en diez segundos.

### Fuentes

**`fontfile` con la ruta** siempre funciona:
```bash
fontfile='fonts/Anton-Regular.ttf'         # relativa: lo mas simple en Windows
fontfile='C\:/Windows/Fonts/arialbd.ttf'   # absoluta, escapada
```

**`font` con el nombre** requiere fontconfig. Comprueba si lo tienes:
```bash
ffmpeg -hide_banner -buildconf | findstr fontconfig
```
Si no aparece `--enable-libfontconfig`, `font=` no funciona. Usa `fontfile`.

**Práctica recomendada:** carpeta `fonts/` dentro del proyecto, `cd` al proyecto, y
`fontfile='fonts/Anton-Regular.ttf'`. Rutas cortas, cero escapado, proyecto portable.

---

## PARTE 2 — subtitles y ASS

### Quemar un SRT

```bash
ffmpeg -hide_banner -y -i entrada.mp4 -vf "subtitles=subs.srt" -c:v libx264 -crf 20 -c:a copy salida.mp4

# Con estilo forzado
ffmpeg -hide_banner -y -i entrada.mp4 -vf \
"subtitles=subs.srt:force_style='FontName=Anton,FontSize=42,PrimaryColour=&H00FFFFFF,OutlineColour=&H00224D0F,Outline=4,Shadow=2,Alignment=2,MarginV=180'" \
-c:v libx264 -crf 20 -preset slow -c:a copy salida.mp4
```
El SRT no tiene estilo propio; aquí es donde se lo pones.

### Por qué preferir ASS

SRT solo tiene tiempos y texto. ASS tiene estilos, posiciones, colores, contornos, animaciones y
karaoke. **Para subtítulos de reels, ASS es la única opción seria.** El filtro `ass=subs.ass` respeta
el archivo tal cual; `subtitles=subs.ass` además permite `force_style` y `fontsdir`, por lo que se
usa casi siempre.

### Anatomía de un .ass

```
[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Base,Anton,150,&H00FFFFFF,&H000000FF,&H00224D0F,&H00000000,0,0,0,0,100,100,0,0,1,14,9,2,80,80,520,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.20,0:00:01.10,Base,,0,0,0,,ESTO
Dialogue: 0,0:00:01.10,0:00:02.05,Base,,0,0,0,,CAMBIA TODO
```

Puntos críticos:

- **`PlayResX`/`PlayResY` deben coincidir con la resolución del video.** Si el ASS dice 384x288 (el
  default de herramientas descuidadas) y tu video es 1080x1920, todos los tamaños salen mal. Es el
  error número uno con archivos ASS.
- **`ScaledBorderAndShadow: yes`**, si no el contorno queda finísimo.
- **Los colores van en BGR**, formato `&HAABBGGRR`. Tu naranja `#F97316` se escribe `&H001673F9`.
- **El alfa está invertido:** `00` = opaco, `FF` = transparente.
- **`Alignment`** usa numpad: 2 = abajo-centro, 5 = centro, 8 = arriba-centro.
- **`MarginV`** en vertical de redes con `Alignment: 2` arranca en **520**, no en 20.

**Conversión de color:** para `#RRGGBB` el valor ASS es `&H00` + `BB` + `GG` + `RR`. Da la vuelta a
los tres pares.

| Color | Hex | ASS |
|---|---|---|
| blanco | `#FFFFFF` | `&H00FFFFFF` |
| verde esmeralda | `#0F4D22` | `&H00224D0F` |
| naranja | `#F97316` | `&H001673F9` |
| amarillo | `#FFD400` | `&H0000D4FF` |

### Etiquetas de animación dentro de ASS

```
{\fad(150,150)}                 fundido de entrada y salida en ms
{\pos(540,1200)}                posicion absoluta
{\an5}                          alineacion para esta linea
{\fscx110\fscy110}              escala 110%
{\t(0,150,\fscx100\fscy100)}    animar hasta 100% en 150 ms
{\c&H1673F9&}                   cambiar color a mitad de linea
{\blur3}   {\b1}   {\k50}       desenfoque del borde, negrita, karaoke
```

El efecto "pop" de los subtítulos de reels:
```
Dialogue: 0,0:00:01.20,0:00:01.85,Base,,0,0,0,,{\fscx125\fscy125\t(0,110,\fscx100\fscy100)}PLATA
```
Entra 25% más grande y se asienta en 110 ms. Ese golpecito es lo que se siente sincronizado con la voz.

Resaltar una palabra dentro de la frase:
```
Dialogue: 0,0:00:03.00,0:00:04.20,Base,,0,0,0,,PIERDES {\c&H0000D4FF&}30%{\c&H00FFFFFF&} CADA MES
```

### fontsdir — dónde busca las fuentes

```bash
ffmpeg -y -i entrada.mp4 -vf "subtitles=subs.ass:fontsdir=fonts" -c:v libx264 -crf 20 -c:a copy salida.mp4
```
Sin `fontsdir`, libass busca en el sistema. **Si no la encuentra, sustituye en silencio.** Exportas
feliz y descubres que todo salió en Arial cuando ya lo publicaste.

**Verifica siempre con un fotograma:**
```bash
ffmpeg -y -ss 2 -i entrada.mp4 -vf "subtitles=subs.ass:fontsdir=fonts" -frames:v 1 prueba_fuente.png
```
Diez segundos que salvan un render entero. También puedes cazar el aviso:
```bash
ffmpeg -v info -i entrada.mp4 -vf "subtitles=subs.ass:fontsdir=fonts" -frames:v 1 -y p.png 2>&1 | findstr /i font
```
Si aparece `fontselect: ... not found, falling back to ...`, ahí está el problema.

### Subtítulos blandos y extracción

```bash
ffmpeg -y -i video.mp4 -i subs.srt -c:v copy -c:a copy -c:s mov_text -metadata:s:s:0 language=spa salida.mp4
ffmpeg -y -i video.mp4 -i subs.ass -c copy -metadata:s:s:0 language=spa salida.mkv
ffmpeg -y -i pelicula.mkv -map 0:s:0 subs_extraidos.srt
```
**Para redes sociales esto no sirve:** Instagram, TikTok y Shorts no muestran pistas embebidas. Hay
que quemarlos.

---

## PARTE 3 — El infierno de las rutas en Windows

La ruta atraviesa **tres** parsers: el shell, el de `filter_complex` (usa `[` `]` `;` `,`) y el de
argumentos del filtro (usa `:`). Un `C:\Videos\subs.ass` tiene un `:` y barras invertidas de escape.
Sin tratarlo, ffmpeg lo lee como "opción `C`" y falla con `Unable to parse option value` o
`No such file or directory`.

**La forma que funciona** — barras normales, dos puntos escapados, comillas simples:
```powershell
ffmpeg -hide_banner -y -i "entrada.mp4" -vf "subtitles='C\:/Users/user/Desktop/proyecto/subs.ass':fontsdir='C\:/Users/user/Desktop/proyecto/fonts'" -c:v libx264 -crf 20 -c:a copy "salida.mp4"
```
En grafos complejos a veces hace falta doble escape (`C\\:/...`) porque una capa se come una barra.

**La forma sensata: haz `cd` y usa rutas relativas.**
```powershell
Set-Location "C:\Users\user\Desktop\proyecto"
ffmpeg -hide_banner -y -i "entrada.mp4" -vf "subtitles=subs.ass:fontsdir=fonts" `
  -c:v libx264 -crf 20 -preset slow -pix_fmt yuv420p -c:a copy "salida.mp4"
```
Cero escapado. Estructura que evita el 100% de estos problemas:
```
proyecto/
  bruto/   fonts/   subs.ass   grafo.txt   salida.mp4
```

### Codificación del archivo de subtítulos

Debe ser **UTF-8 sin BOM**. Con BOM, libass a veces no lee `[Script Info]` y el archivo entero se
rompe. Si vienen tildes raras: `subtitles=subs.srt:charenc=UTF-8` (o `charenc=CP1252` para archivos
viejos).

Escribir un ASS correcto desde PowerShell 5.1:
```powershell
$ass = @"
[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Base,Anton,150,&H00FFFFFF,&H000000FF,&H00224D0F,&H00000000,0,0,0,0,100,100,0,0,1,14,9,2,80,80,520,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.20,0:00:01.10,Base,,0,0,0,,{\fscx125\fscy125\t(0,110,\fscx100\fscy100)}ESTO
Dialogue: 0,0:00:01.10,0:00:02.05,Base,,0,0,0,,CAMBIA TODO
"@
[IO.File]::WriteAllText("$PWD\subs.ass", $ass, (New-Object System.Text.UTF8Encoding($false)))
```
`UTF8Encoding($false)` es el "sin BOM". `$PWD\` porque `[IO.File]` no usa el directorio de PowerShell.

---

## Receta completa

```powershell
Set-Location "C:\Users\user\Desktop\proyecto"

# 1. Verificar la fuente en un fotograma ANTES de renderizar
ffmpeg -hide_banner -y -ss 2 -i "corte.mp4" -vf "subtitles=subs.ass:fontsdir=fonts" -frames:v 1 "prueba.png"

# 2. Render final
ffmpeg -hide_banner -y -i "corte.mp4" `
  -vf "subtitles=subs.ass:fontsdir=fonts,format=yuv420p" `
  -c:v libx264 -crf 19 -preset slow -profile:v high -level 4.1 `
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart "reel_final.mp4"

# 3. Verificar zona segura sobre un fotograma real
ffmpeg -hide_banner -y -ss 3 -i "reel_final.mp4" -frames:v 1 `
  -vf "drawbox=x=0:y=ih-520:w=iw:h=520:color=red@0.3:t=fill" "verif_zona.png"
```
Ese último paso pinta lo que tapa Instagram. Si tu subtítulo está dentro del rojo, muévelo.

---

## Errores comunes

- **Rutas de Windows sin escapar dentro de `subtitles`.** Falla con un error que ni menciona la ruta.
  Haz `cd` y usa relativas.
- **`PlayResX`/`PlayResY` distintos de la resolución del video.** Todo sale de tamaño equivocado.
- **Colores del ASS en RGB.** ASS usa **BGR**. Tu naranja sale azul.
- **Alfa del ASS al revés.** `00` es opaco, `FF` transparente.
- **Confiar en que libass encontró la fuente.** Sustituye en silencio. Verifica con un fotograma.
- **Olvidar `fontsdir`** con una fuente que no está instalada en el sistema.
- **`MarginV` por defecto.** Deja el subtítulo detrás del caption de Instagram. En vertical: 520.
- **Archivo `.ass` o `.srt` con BOM.** libass puede ignorar la primera línea y romper todo.
- **Apóstrofos y tildes dentro de `text=`.** Usa `textfile`.
- **Olvidar escapar los `:` dentro de `%{pts\:hms}`.**
- **Fuente fina en subtítulos de redes.** Desaparece con la compresión. Usa Black/Heavy.
- **Subtítulos blandos (`mov_text`) para redes.** No se ven. Hay que quemarlos.
- **Renderizar el video completo para probar el estilo.** Un fotograma basta.
- **`drawtext` con 20 apariciones.** A partir de 5, genera un ASS: es más mantenible.

---

## Checklist

- [ ] Hice `cd` a la carpeta del proyecto y uso rutas relativas cortas, sin espacios ni tildes.
- [ ] Las fuentes están en `fonts/` y el comando lleva `fontsdir=fonts`.
- [ ] **Rendericé un fotograma de prueba y confirmé visualmente que la fuente correcta se usó.**
- [ ] El `.ass` tiene `PlayResX`/`PlayResY` iguales a la resolución del video.
- [ ] El `.ass` tiene `ScaledBorderAndShadow: yes`.
- [ ] Los colores del ASS están en **BGR** y los verifiqué contra el hex de marca.
- [ ] El alfa del ASS usa `00` para opaco.
- [ ] `MarginV` es 520 o más en formato vertical.
- [ ] El archivo de subtítulos está en UTF-8 **sin BOM**.
- [ ] La fuente es pesada (Black/Heavy), con contorno grueso en color de marca.
- [ ] El texto no queda sobre ojos ni boca, ni dentro de la zona de la interfaz.
- [ ] Los tiempos golpean con la sílaba, no después: los verifiqué contra el audio.
- [ ] La cadena termina en `format=yuv420p`.
- [ ] Verifiqué la salida con un fotograma con las zonas seguras pintadas encima.
