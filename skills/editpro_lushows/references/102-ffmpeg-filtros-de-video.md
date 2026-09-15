# 102 — Filtros de video: escalar, recortar, encuadrar, mover

Un filtro es una transformación que ffmpeg aplica a cada fotograma. Se encadenan con comas y se
aplican en orden, de izquierda a derecha. Cambiar el orden cambia el resultado.

```bash
ffmpeg -i entrada.mp4 -vf "crop=1080:1080,scale=720:720,format=yuv420p" salida.mp4
```

`-vf` es atajo de `-filter:v` y solo sirve con **una** entrada de video. Para cualquier cosa con
varias fuentes (superponer, unir, transiciones) necesitas `-filter_complex`, que se explica en `104`.

**Regla de orden:** recorta antes de escalar (menos píxeles que procesar), y pon `format=yuv420p` al
final, siempre.

---

## scale — cambiar el tamaño

```bash
scale=1080:1920    # deforma si la proporcion no coincide
scale=1080:-2      # ancho 1080, alto calculado, redondeado a par
scale=-2:1080      # alto 1080, ancho calculado
scale=iw/2:ih/2    # la mitad de lo que sea
scale=iw*0.75:-2   # 75% del ancho
```

**Usa siempre `-2`, nunca `-1`.** `-1` puede dar un número impar, que H.264 con yuv420p **rechaza**
con `width not divisible by 2`. `-2` redondea al par más cercano.

### Ajustar a un lienzo sin deformar

Las dos jugadas que resuelven el 90% de los reencuadres:

```bash
# CUBRIR el lienzo (recorta el sobrante). Para pasar horizontal a vertical.
scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920

# CABER dentro del lienzo (deja barras). Para no perder nada de la imagen.
scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black
```
`force_original_aspect_ratio` acepta `increase`, `decrease` o `disable` (el defecto: deformar).

### Calidad del reescalado

```bash
scale=1080:1920:flags=lanczos
```

| Algoritmo | Cuándo |
|---|---|
| `bilinear` | rápido, borroso. Solo para previsualizar |
| `bicubic` | el defecto. Aceptable |
| `lanczos` | **el mejor para reducir**. Úsalo por defecto |
| `neighbor` | píxel duro, sin suavizado. Pixel art o efectos |
| `spline` | suave, bueno para agrandar |

Al agrandar mucho, `lanczos` puede generar halos; compénsalo con nitidez suave:
```bash
-vf "scale=1920:1080:flags=lanczos,unsharp=5:5:0.6:5:5:0.0"
```

---

## crop — recortar

```bash
crop=ANCHO:ALTO:X:Y     # X,Y = esquina superior izquierda. Sin ellos, recorta CENTRADO.
```
```bash
crop=1080:1920                    # centrado
crop=iw/2:ih:iw/2:0               # mitad derecha
crop=ih*9/16:ih                   # convierte a 9:16 lo que sea, centrado
crop=iw:iw*9/16                   # convierte a 16:9 lo que sea, centrado
```
Variables: `iw`/`in_w`, `ih`/`in_h`, `ow`, `oh`, `x`, `y`, `n`, `t`.

### Recortar donde está la cara, no en el centro

Cuando pasas horizontal a vertical y la persona no está centrada, el recorte centrado la corta:
```bash
# La persona esta en el tercio izquierdo de un 1920x1080
-vf "crop=608:1080:250:0,scale=1080:1920:flags=lanczos"
```
608 es `1080*9/16` redondeado a par. El 250 lo sacas mirando un fotograma:
```bash
ffmpeg -y -ss 5 -i entrada.mp4 -frames:v 1 fotograma.png
```

### Detectar barras negras automáticamente

```bash
ffmpeg -i entrada.mp4 -vf cropdetect=24:16:0 -frames:v 300 -f null -
```
Imprime líneas como `crop=1920:800:0:140`. Toma la que **más se repita**, no la primera.

---

## pad — agrandar el lienzo

```bash
pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black
pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0x1B4D3E    # color de marca
```
`(ow-iw)/2` es "la mitad de la diferencia entre el lienzo y la imagen": centrado horizontal.

### La receta bonita: fondo borroso en vez de barras negras

```bash
ffmpeg -hide_banner -y -i horizontal.mp4 -filter_complex \
"[0:v]split=2[fondo][frente]; \
 [fondo]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=30,eq=brightness=-0.12[bg]; \
 [frente]scale=1080:-2[fg]; \
 [bg][fg]overlay=(W-w)/2:(H-h)/2,format=yuv420p[v]" \
-map "[v]" -map 0:a? -c:v libx264 -crf 20 -preset slow -c:a aac -b:a 192k salida.mp4
```
`split=2` duplica el flujo para usarlo dos veces. Ver `104`.

---

## fps y -r — cadencia de fotogramas

```bash
-vf "fps=30"        # filtro: duplica o descarta fotogramas dentro del grafo
-r 30               # opcion de salida: fija la cadencia al escribir
```

**`fps=30` (filtro)** trabaja con los timestamps reales y garantiza cadencia constante desde ese punto
del grafo: es el que quieres cuando vas a unir o superponer. **`-r 30`** actúa al final y puede
duplicar fotogramas de forma menos elegante.

Opciones: `fps=30:round=near`, `fps=30000/1001` (29.97 exacto, NTSC).

**Trampa de las grabaciones de pantalla y del celular:** vienen con fps variable. Al filtrarlas sin
fijar `fps`, el audio se desincroniza. **Pon `fps=30` como primer filtro de la cadena** cuando la
fuente sea grabación de pantalla, OBS o un video de WhatsApp.

---

## setsar y setdar — la relación de aspecto del píxel

SAR es cuán cuadrado es cada píxel. En video moderno siempre es `1:1`. En material viejo o de algunos
exportes puede ser `40:33` u otra rareza: el clip se ve estirado junto a los demás y **rompe el
concat con `-c copy`**.

```bash
setsar=1        # fuerza pixeles cuadrados. Ponlo SIEMPRE al normalizar
setdar=16/9     # fija la relacion de aspecto de la imagen (calcula la SAR necesaria)
```
`setsar` **no reescala nada**, solo cambia el metadato. Si la imagen se ve estirada, la arregla; si se
ve bien, no hace daño. Por eso va en toda plantilla de normalización.

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=sample_aspect_ratio,display_aspect_ratio -of default=nw=1 entrada.mp4
```

---

## format — el espacio de color

```bash
format=yuv420p
```
**Ponlo al final de toda cadena que vaya a un archivo de entrega.** Sin él, si algún filtro trabajó en
RGB o yuv444p, libx264 escribe yuv444p y el video no se reproduce en iPhone, ni QuickTime, ni en la
mayoría de reproductores ni en los previsualizadores de redes.

Otros valores: `format=rgba` (para trabajar transparencias entre filtros), `format=gbrp`,
`format=yuv420p10le` (10 bits, para grados intermedios, no para entrega).

Equivalente como opción de salida: `-pix_fmt yuv420p`. Usa las dos si quieres: no se estorban.

---

## Rotar y voltear

```bash
transpose=1   # 90 grados HORARIO
transpose=2   # 90 grados ANTIHORARIO
transpose=0   # 90 antihorario + volteo vertical
transpose=3   # 90 horario + volteo vertical
hflip         # espejo horizontal
vflip         # espejo vertical
```
Para 180 grados, encadena: `-vf "transpose=1,transpose=1"`. `hflip` sirve para arreglar material de
cámara frontal y para variar un b-roll repetido sin que se note.

Ángulos arbitrarios (recodifica e interpola, por eso no lo uses para 90 grados):
```bash
rotate=PI/6                                        # 30 grados
rotate=a=-3*PI/180:fillcolor=none:ow=rotw(iw):oh=roth(ih)
rotate=2*PI*t/10:fillcolor=black                   # una vuelta cada 10 segundos
```
`ow=rotw(iw):oh=roth(ih)` agranda el lienzo para que no se corten las esquinas.

**La rotación que ya trae el archivo:** los videos del celular vienen grabados en horizontal con un
metadato de rotación. ffmpeg **rota automáticamente** al decodificar desde la 2.7, así que
normalmente no haces nada. Pero con `-c copy` el metadato se copia y algunas plataformas lo ignoran.
Para el crudo sin rotar: `-noautorotate` **antes** de `-i`. Ver la rotación declarada:
```bash
ffprobe -v error -select_streams v:0 -show_entries stream_side_data=rotation -of csv=p=0 entrada.mp4
```

---

## fade — entradas y salidas

```bash
fade=t=in:st=0:d=1                 # aparece desde negro en 1 segundo
fade=t=out:st=9:d=1                # se va a negro desde el segundo 9
fade=t=in:st=0:d=0.5:color=white   # desde blanco
fade=t=in:st=0:d=1:alpha=1         # funde la TRANSPARENCIA, no a color
```
`alpha=1` es lo que usas para que un logo o un texto superpuesto aparezca y desaparezca suave.

Encadenados en un clip de 10 segundos:
```bash
-vf "fade=t=in:st=0:d=0.6,fade=t=out:st=9.4:d=0.6"
```

**Trampa:** `st` se cuenta desde el inicio del **clip filtrado**. Si cortaste con `-ss` sin reiniciar
timestamps, el fundido cae donde no es. Pon `setpts=PTS-STARTPTS` primero. También existe por
fotograma: `fade=t=in:s=0:n=18`.

---

## zoompan — el efecto Ken Burns

```bash
ffmpeg -hide_banner -y -loop 1 -i foto.jpg -t 5 \
  -vf "scale=4320:-2:flags=lanczos,zoompan=z='min(zoom+0.0012,1.35)':d=150:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30,format=yuv420p" \
  -c:v libx264 -crf 20 -preset slow salida.mp4
```

- `z` — expresión de zoom. `zoom` es el valor del fotograma anterior. `min(...)` pone tope.
- `d` — **duración en FOTOGRAMAS** por cada imagen de entrada. 150 a 30 fps = 5 segundos.
- `x`, `y` — centro del encuadre. `iw/2-(iw/zoom/2)` mantiene el centro.
- `s` — tamaño de salida. `fps` — cadencia.

**Las dos trampas:**

1. **El temblor.** zoompan calcula posiciones en enteros, así que a resolución nativa el movimiento
   salta. La cura es **escalar la entrada 4x antes** (por eso el `scale=4320`) para que cada paso sea
   sub-pixel en la escala final. Sin eso, el efecto se ve barato.
2. **`d` está en fotogramas, no en segundos.** `d=5` es un parpadeo, no 5 segundos.

Variantes:
```bash
# Alejarse
zoompan=z='if(lte(zoom,1.0),1.35,max(1.001,zoom-0.0012))':d=150:s=1080x1920:fps=30
# Acercarse a la esquina superior derecha
zoompan=z='min(zoom+0.0015,1.4)':d=150:x='iw-(iw/zoom)':y='0':s=1080x1920:fps=30
# Desplazamiento horizontal sin zoom (on = fotograma de salida; on/150 va de 0 a 1)
zoompan=z=1.25:d=150:x='(iw-iw/zoom)*(on/150)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30
```

**Para video (no imagen), zoompan es incómodo.** Un empuje real es más limpio con `crop` animado:
```bash
-vf "crop='iw/(1+0.10*t/5)':'ih/(1+0.10*t/5)',scale=1080:1920:flags=lanczos,fps=30"
```
Recorta cada vez más cerrado (10% en 5 segundos) y reescala: empuje suave sin temblor.

---

## overlay — superponer (resumen; detalle en 105)

```bash
ffmpeg -y -i base.mp4 -i logo.png -filter_complex \
"[1:v]scale=200:-1[lg];[0:v][lg]overlay=W-w-40:H-h-40[v]" \
-map "[v]" -map 0:a? -c:v libx264 -crf 20 -c:a copy salida.mp4
```
`W`/`H` = tamaño del fondo, `w`/`h` = tamaño de lo que superpones.
```bash
overlay=(W-w)/2:(H-h)/2      # centrado
overlay=W-w-40:40            # arriba a la derecha
overlay=(W-w)/2:H-h-560      # centrado abajo, sobre la zona segura de redes
```

---

## drawbox — cajas, marcos y diagnóstico

```bash
drawbox=x=0:y=0:w=iw:h=120:color=black@0.6:t=fill
```
`t=fill` la rellena; sin eso dibuja solo el borde con el grosor que pongas (`t=8`). `color` acepta
nombres, `0xRRGGBB` y transparencia con `@`.

**Marcar la zona segura de Instagram sobre un fotograma de prueba:**
```bash
ffmpeg -y -ss 3 -i reel.mp4 -frames:v 1 -vf \
"drawbox=x=0:y=0:w=iw:h=220:color=red@0.35:t=fill, \
 drawbox=x=0:y=ih-520:w=iw:h=520:color=red@0.35:t=fill, \
 drawbox=x=iw-260:y=0:w=260:h=ih:color=red@0.25:t=fill" \
zona_segura.png
```
Abres el PNG y ves de inmediato si tu texto quedó debajo del caption o detrás de los botones. Es la
verificación más barata que existe y casi nadie la hace.

Relacionado: `drawgrid=w=iw/3:h=ih/3:t=2:color=white@0.5` dibuja la regla de los tercios.

---

## Otros filtros que vas a necesitar

```bash
# Velocidad (el audio se ajusta aparte con atempo, ver 103)
setpts=0.5*PTS          # el doble de rapido
setpts=2.0*PTS          # la mitad de rapido
setpts=PTS/1.25         # 25% mas rapido

# Desenfoque y nitidez
gblur=sigma=20          # gaussiano, el que se ve bien
boxblur=10:1            # mas rapido, mas feo
unsharp=5:5:0.8:5:5:0.0 # luma_x:luma_y:cantidad:chroma_x:chroma_y:cantidad_chroma

# Ajustes basicos (el color a fondo va en el bloque 6)
eq=contrast=1.08:brightness=0.02:saturation=1.12:gamma=1.0
hue=h=8:s=1.1
vignette=PI/5

# Congelar el ultimo fotograma 2 segundos
tpad=stop_mode=clone:stop_duration=2
# Añadir 1 segundo de negro al inicio
tpad=start_duration=1:start_mode=add:color=black

# Invertir el clip (OJO: carga todo en RAM, solo clips cortos)
reverse

# Estabilizar (dos pasadas, requiere libvidstab)
#   1: -vf vidstabdetect=shakiness=6:accuracy=15 -f null -
#   2: -vf vidstabtransform=smoothing=30:input=transforms.trf,unsharp=5:5:0.8
```

---

## La plantilla de normalización que deberías memorizar

```bash
-vf "fps=30,scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,setsar=1,format=yuv420p"
```

1. `fps=30` — primero, para domar el fps variable antes de que nada más lo toque
2. `scale=...increase` — agranda hasta cubrir el lienzo, sin deformar, con buen algoritmo
3. `crop=1080:1920` — corta el sobrante centrado
4. `setsar=1` — píxeles cuadrados
5. `format=yuv420p` — compatibilidad universal, siempre al final

Cambia `1080:1920` por `1920:1080` o `1080:1080` y ya tienes las tres relaciones para publicar.

---

## Errores comunes

- **`scale=-1` en vez de `-2`.** Produce dimensiones impares y H.264 falla.
- **Escalar antes de recortar.** Gastas cómputo en píxeles que vas a botar.
- **Olvidar `format=yuv420p` al final.** Se ve bien en tu PC y no abre en el celular de nadie.
- **Olvidar `setsar=1`** al normalizar. El clip se ve estirado o rompe el concat.
- **No fijar `fps` con grabación de pantalla o WhatsApp.** Es fps variable y el audio se corre.
- **`d` de zoompan en segundos.** Está en **fotogramas**.
- **zoompan sin escalar la entrada primero.** El movimiento tiembla y se ve barato.
- **Confiar en `crop` centrado.** El sujeto casi nunca está en el centro. Saca un fotograma y mira.
- **`fade` con `st` calculado sobre el video original** después de haber cortado.
- **Usar `-vf` cuando hay dos entradas.** Da `Filtergraph has more than one input`; necesitas
  `-filter_complex`.
- **Poner `-vf` y `-filter_complex` sobre el mismo flujo.** Se excluyen.
- **`reverse` sobre un clip largo.** Se come toda la RAM.
- **`rotate` para giros de 90 grados.** Usa `transpose`: es exacto y no interpola.

---

## Checklist

- [ ] El orden de la cadena es: cadencia, escala, recorte, SAR, formato.
- [ ] Usé `-2` en vez de `-1` en todos los `scale`.
- [ ] Puse `flags=lanczos` en los escalados que importan.
- [ ] Elegí conscientemente entre `increase+crop` (cubrir) y `decrease+pad` (caber).
- [ ] Si el sujeto no está centrado, saqué un fotograma y ajusté la X del `crop`.
- [ ] `setsar=1` está presente si voy a unir este clip con otros.
- [ ] `format=yuv420p` (o `-pix_fmt yuv420p`) está en la salida final.
- [ ] Si la fuente es grabación de pantalla o WhatsApp, fijé `fps` como primer filtro.
- [ ] En `zoompan`, `d` está en fotogramas y escalé la entrada antes para evitar temblor.
- [ ] Los `fade` calculan `st` sobre el clip ya cortado, no sobre el original.
- [ ] Revisé un fotograma con `drawbox` marcando las zonas seguras de la plataforma.
- [ ] Verifiqué la salida con `ffprobe`: resolución, fps, `pix_fmt` y SAR son los que quería.
