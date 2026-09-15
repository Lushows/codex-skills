# 105 — Superponer capas: overlay con posición, transparencia, tiempo y movimiento

`overlay` pone una imagen o video encima de otro. Es el filtro con el que haces logos, marcas de agua,
picture-in-picture, tarjetas gráficas, barras inferiores, stickers, resaltados y prácticamente todo el
motion graphics que se hace fuera de After Effects.

Siempre va dentro de `-filter_complex`, porque necesita dos entradas.

```bash
ffmpeg -hide_banner -y -i fondo.mp4 -i encima.png -filter_complex \
"[0:v][1:v]overlay=40:40[v]" -map "[v]" -map 0:a? -c:v libx264 -crf 20 -c:a copy salida.mp4
```

**El orden manda: la primera entrada es el fondo, la segunda es lo que va encima.**

---

## Posición

Sintaxis: `overlay=X:Y`, donde X e Y son la esquina superior izquierda de la capa.

Variables disponibles:

| Variable | Significa |
|---|---|
| `W` | ancho del fondo (main) |
| `H` | alto del fondo |
| `w` | ancho de la capa (overlay) |
| `h` | alto de la capa |
| `t` | segundo actual |
| `n` | número de fotograma |
| `x`, `y` | los valores calculados (usables dentro de las expresiones) |

También existen los nombres largos: `main_w`, `main_h`, `overlay_w`, `overlay_h`.

### Las nueve posiciones

```bash
overlay=40:40                    # arriba izquierda
overlay=(W-w)/2:40               # arriba centro
overlay=W-w-40:40                # arriba derecha
overlay=40:(H-h)/2               # medio izquierda
overlay=(W-w)/2:(H-h)/2          # centro
overlay=W-w-40:(H-h)/2           # medio derecha
overlay=40:H-h-40                # abajo izquierda
overlay=(W-w)/2:H-h-40           # abajo centro
overlay=W-w-40:H-h-40            # abajo derecha
```

**Para vertical de redes, no uses `H-h-40`.** Los últimos 500 píxeles de un 1080x1920 están tapados
por el caption, el nombre de usuario y los botones. Abajo usa `overlay=W-w-50:H-h-560`; arriba deja al
menos 220 píxeles: `overlay=W-w-50:220`.

Si vas a reutilizar el grafo con lienzos de distinto tamaño, usa fracciones en vez de píxeles:
`overlay=W-w-W*0.05:H-h-H*0.28` (5% de margen derecho, 28% inferior) funciona igual en 1080x1920 que
en 720x1280.

---

## Tamaño de la capa

Casi nunca superpones un archivo a su tamaño original. Escálalo primero:

```bash
-filter_complex "[1:v]scale=200:-1[lg];[0:v][lg]overlay=W-w-50:H-h-560[v]"
```
Para que el logo mida siempre lo mismo **en proporción al video**, calcula respecto al ancho: 194 px
es el 18% de 1080. Con lienzo fijo (lo normal), calcula el número y ya.

---

## Imágenes como entrada

Una imagen fija es una entrada de un solo fotograma: al superponerla aparece un fotograma y
desaparece. Para que dure todo el video hay dos formas.

```bash
# Forma A: repetir la imagen indefinidamente
ffmpeg -y -i video.mp4 -loop 1 -i logo.png -filter_complex \
"[1:v]scale=200:-1[lg];[0:v][lg]overlay=W-w-50:H-h-560[v]" \
-map "[v]" -map 0:a? -shortest -c:v libx264 -crf 20 -c:a copy salida.mp4

# Forma B: dejar que overlay repita el último fotograma de la capa
ffmpeg -y -i video.mp4 -i logo.png -filter_complex \
"[1:v]scale=200:-1[lg];[0:v][lg]overlay=W-w-50:H-h-560:eof_action=repeat[v]" \
-map "[v]" -map 0:a? -c:v libx264 -crf 20 -c:a copy salida.mp4
```

Con la forma A, `-shortest` es obligatorio: sin él, `-loop 1` genera imagen para siempre y el render
no termina nunca. Es una de las formas más comunes de dejar ffmpeg corriendo toda la noche por nada.

La forma B es más limpia porque no depende de `-shortest`.

### eof_action y shortest, los dos parámetros que evitan renders infinitos

```bash
overlay=X:Y:eof_action=repeat    # cuando la capa se acaba, repite su último fotograma (default)
overlay=X:Y:eof_action=endall    # cuando cualquiera de las dos se acaba, termina todo
overlay=X:Y:eof_action=pass      # cuando la capa se acaba, deja pasar el fondo solo
overlay=X:Y:shortest=1           # el resultado dura lo que la entrada más corta
```

**`eof_action=pass` es el que quieres** cuando superpones un video corto (una animación de 3 segundos)
sobre un video largo: la animación se ve y luego desaparece, en vez de congelarse en pantalla.

---

## Transparencia

### Con PNG que ya tiene canal alfa

Funciona directo. `overlay` respeta el alfa del PNG sin que hagas nada. Pero **verifica que el PNG lo
tenga de verdad**:

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=pix_fmt -of csv=p=0 logo.png
```

Si sale `rgb24` o `pal8`, **no tiene alfa**: el fondo se verá blanco o negro. Necesitas `rgba` o
`ya8`. Vuelve a exportar el PNG con transparencia.

### Bajar la opacidad de la capa

```bash
[1:v]format=rgba,colorchannelmixer=aa=0.6[lg]
```

`aa` es "alpha to alpha": multiplica el canal alfa existente. `0.6` deja la capa al 60%. El
`format=rgba` previo es necesario si la fuente no tiene alfa.

```bash
ffmpeg -y -i video.mp4 -i logo.png -filter_complex \
"[1:v]scale=200:-1,format=rgba,colorchannelmixer=aa=0.55[lg]; \
 [0:v][lg]overlay=W-w-50:H-h-560[v]" \
-map "[v]" -map 0:a? -c:v libx264 -crf 20 -c:a copy salida.mp4
```

### Hacer transparente un color (chroma key)

```bash
# Fondo verde
[1:v]chromakey=0x00FF00:0.20:0.05[capa]

# Fondo de color plano cualquiera, tolerancia por RGB
[1:v]colorkey=0x121212:0.18:0.08[capa]
```

Parámetros: `color:similitud:mezcla`. Sube `similitud` si quedan bordes verdes; sube `mezcla` para
suavizar el borde. Para material real de croma, `despill` y un `erosion` ligero ayudan:

```bash
[1:v]chromakey=0x00B140:0.22:0.08,despill=type=green:mix=0.5[capa]
```

### Video con alfa de verdad

Los MOV con ProRes 4444 y los WebM con VP9 `yuva420p` llevan alfa real. Se superponen directo:

```bash
ffmpeg -y -i base.mp4 -c:v libvpx-vp9 -i animacion_alfa.webm -filter_complex \
"[0:v][1:v]overlay=(W-w)/2:(H-h)/2:eof_action=pass[v]" \
-map "[v]" -map 0:a? -c:v libx264 -crf 20 -c:a copy salida.mp4
```

Verifica que el `pix_fmt` sea `yuva420p` (con `a`), no `yuv420p`. Si no lleva la `a`, no hay alfa.

### Una máscara aparte con alphamerge

Cuando tienes el gráfico por un lado y la máscara en blanco y negro por otro:

```bash
ffmpeg -y -i base.mp4 -i grafico.mp4 -i mascara.mp4 -filter_complex \
"[1:v][2:v]alphamerge[capa];[0:v][capa]overlay=0:0[v]" \
-map "[v]" -c:v libx264 -crf 20 salida.mp4
```

`alphamerge` toma el canal de luminancia del segundo flujo y lo usa como alfa del primero. Blanco =
opaco, negro = transparente.

---

## Tiempo: que la capa aparezca solo cuando quieres

`overlay` soporta la opción de línea de tiempo `enable`. Esto es lo que convierte una marca de agua
estática en motion graphics.

```bash
overlay=W-w-50:H-h-560:enable='between(t,2,8)'
```

La capa se ve entre el segundo 2 y el 8. Fuera de ese rango, ffmpeg pasa el fondo tal cual.

### Expresiones útiles para enable

```bash
enable='between(t,2,8)'                        # entre el 2 y el 8
enable='gte(t,5)'                              # del 5 en adelante
enable='lt(t,3)'                               # solo los primeros 3 segundos
enable='between(t,1,4)+between(t,10,14)'       # dos ventanas (el + funciona como OR)
enable='not(between(t,5,7))'                   # todo MENOS entre el 5 y el 7
enable='lte(mod(t,4),2)'                       # 2 segundos sí, 2 no, en bucle
enable='between(n,150,300)'                    # por número de fotograma
```

Con `+` para unir ventanas: cada `between` devuelve 0 o 1, la suma da 1 o más, y cualquier valor
distinto de 0 activa el filtro.

### Múltiples capas en distintos momentos

```bash
ffmpeg -hide_banner -y -i base.mp4 -i tarjeta1.png -i tarjeta2.png -i tarjeta3.png -filter_complex \
"[1:v]scale=900:-1[t1];[2:v]scale=900:-1[t2];[3:v]scale=900:-1[t3]; \
 [0:v][t1]overlay=(W-w)/2:400:enable='between(t,1.0,3.5)'[c1]; \
 [c1][t2]overlay=(W-w)/2:400:enable='between(t,4.0,6.5)'[c2]; \
 [c2][t3]overlay=(W-w)/2:400:enable='between(t,7.0,9.5)',format=yuv420p[v]" \
-map "[v]" -map 0:a? -c:v libx264 -crf 20 -preset slow -c:a aac -b:a 192k salida.mp4
```

Ese es el patrón de encadenamiento: cada `overlay` toma el resultado del anterior. Puedes apilar todas
las capas que quieras así.

### Aparecer y desaparecer con fundido

`enable` es un interruptor: la capa aparece de golpe. Para que entre suave, hay que animar el alfa.
Dos formas.

**Forma A — `fade` con `alpha=1` sobre la capa** (la limpia, cuando la capa es un video o una imagen
en bucle con duración conocida):

```bash
ffmpeg -y -i base.mp4 -loop 1 -t 6 -i logo.png -filter_complex \
"[1:v]scale=200:-1,format=rgba,fade=t=in:st=0:d=0.4:alpha=1,fade=t=out:st=5.6:d=0.4:alpha=1,setpts=PTS+2/TB[lg]; \
 [0:v][lg]overlay=W-w-50:H-h-560:eof_action=pass[v]" \
-map "[v]" -map 0:a? -shortest -c:v libx264 -crf 20 -c:a copy salida.mp4
```

`setpts=PTS+2/TB` retrasa la capa 2 segundos: aparece en el segundo 2, dura 6, con medio segundo de
entrada y medio de salida. `/TB` convierte segundos a la base de tiempo interna. Este es el mecanismo
para retrasar cualquier capa.

**Forma B — expresión de alfa dependiente del tiempo:**

```bash
[1:v]format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='alpha(X,Y)*clip((T-2)/0.4,0,1)'[lg]
```

Es más flexible pero muchísimo más lento (`geq` calcula píxel por píxel). Úsalo solo si la forma A no
te alcanza.

---

## Movimiento

X e Y aceptan expresiones con `t`. Ahí está todo el movimiento.

### Desplazamiento lineal

```bash
# Entra desde la derecha entre el segundo 2 y el 3, y se queda
overlay=x='if(lt(t,2), W, if(lt(t,3), W-(W-(W-w-50))*(t-2), W-w-50))':y=H-h-560
```

Se lee feo. Es más legible con la fórmula de interpolación:

```bash
# lerp: valor_inicial + (valor_final - valor_inicial) * avance
overlay=x='W-(W-(W-w-50))*clip((t-2)/1,0,1)':y='H-h-560'
```

`clip(valor, min, max)` recorta el avance entre 0 y 1: antes del segundo 2 vale 0, después del 3 vale
1, y entre medio interpola. **`clip` con `(t-inicio)/duracion` es el patrón de animación que resuelve
casi todo.**

### Ejemplos de movimientos frecuentes

```bash
# Barra inferior que sube desde abajo en 0.5 s a partir del segundo 3
overlay=x=0:y='H-h*clip((t-3)/0.5,0,1)'

# Ticker horizontal en bucle (marquesina)
overlay=x='W-mod(t*180,W+w)':y=H-h-620

# Rebote suave vertical
overlay=x=(W-w)/2:y='(H-h)/2+30*sin(2*PI*t/2)'

# Diagonal de esquina a esquina en 4 segundos
overlay=x='(W-w)*clip(t/4,0,1)':y='(H-h)*clip(t/4,0,1)'

# Entra desde arriba con desaceleración (ease-out cuadrático)
overlay=x=(W-w)/2:y='-h+(220+h)*(1-pow(1-clip((t-1)/0.6,0,1),2))'
```

Ese último es el que se ve profesional: la desaceleración `1-pow(1-p,2)` hace que el elemento llegue
frenando en vez de golpear. Compáralo con el lineal y la diferencia es obvia.

### Funciones disponibles en las expresiones

```
abs, min, max, clip(x,min,max), if(cond,a,b), ifnot, between(x,a,b)
lt, lte, gt, gte, eq, not
sin, cos, tan, atan, exp, log, sqrt, pow(x,y), mod(x,y)
floor, ceil, round, trunc, hypot(x,y)
random(seed), gauss(seed)
PI, E
st(0,valor) / ld(0)     guardar y leer una variable temporal
```

`st` y `ld` sirven para no repetir un cálculo largo:

```bash
overlay=x='st(0,clip((t-2)/0.8,0,1)); (W-w)/2*ld(0)':y='(H-h)/2'
```

---

## Picture in picture (video dentro de video)

Con borde blanco (vía `pad`) y los dos audios mezclados:

```bash
ffmpeg -hide_banner -y -i principal.mp4 -i secundario.mp4 -filter_complex \
"[1:v]scale=416:-2,setsar=1,pad=iw+8:ih+8:4:4:color=white[pip]; \
 [0:v][pip]overlay=W-w-40:40:shortest=1,format=yuv420p[v]; \
 [0:a][1:a]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]" \
-map "[v]" -map "[a]" -c:v libx264 -crf 20 -preset slow -c:a aac -b:a 192k pip.mp4
```
Sin el borde ni la mezcla es solo `[1:v]scale=420:-2,setsar=1[pip];[0:v][pip]overlay=W-w-40:40:shortest=1[v]`
con `-map 0:a`.

---

## Lado a lado sin overlay: hstack y vstack

Para comparaciones (antes/después) es más simple que `overlay`:

```bash
# Dos videos lado a lado (deben tener el mismo alto)
ffmpeg -y -i a.mp4 -i b.mp4 -filter_complex \
"[0:v]scale=960:-2,setsar=1[l];[1:v]scale=960:-2,setsar=1[r];[l][r]hstack=inputs=2[v]" \
-map "[v]" -an -c:v libx264 -crf 20 comparacion.mp4

# Uno encima del otro (mismo ancho)
"[l][r]vstack=inputs=2[v]"

# Cuadrícula 2x2
"[a][b][c][d]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]"
```

`hstack` y `vstack` **exigen** dimensiones compatibles. Escala antes, siempre.

---

## Modos de fusión con blend

Para efectos de luz, texturas y grano:

```bash
[0:v][1:v]blend=all_mode=screen:all_opacity=0.5
```

Modos: `addition`, `and`, `average`, `burn`, `darken`, `difference`, `divide`, `dodge`, `exclusion`,
`extremity`, `freeze`, `glow`, `grainextract`, `grainmerge`, `hardlight`, `hardmix`, `heat`,
`lighten`, `linearlight`, `multiply`, `negation`, `normal`, `or`, `overlay`, `phoenix`, `pinlight`,
`reflect`, `screen`, `softlight`, `subtract`, `vividlight`, `xor`.

Los que sirven de verdad en video:

- `screen` — para destellos, humo, luz de fuga. Lo negro se vuelve invisible.
- `multiply` — para sombras y viñetas. Lo blanco se vuelve invisible.
- `softlight` — para texturas y grano sutil.
- `overlay` — contraste, para capas de textura.

**Requisito:** ambos flujos deben tener **exactamente** el mismo tamaño y formato. Escala primero.

```bash
ffmpeg -y -i base.mp4 -i destello.mp4 -filter_complex \
"[1:v]scale=1080:1920,setsar=1,format=yuv420p[fx]; \
 [0:v]scale=1080:1920,setsar=1,format=yuv420p[bg]; \
 [bg][fx]blend=all_mode=screen:all_opacity=0.7,format=yuv420p[v]" \
-map "[v]" -map 0:a? -c:v libx264 -crf 20 -c:a copy salida.mp4
```

---

## Errores comunes

- **Invertir el orden de las entradas.** La primera es el fondo. Si el logo tapa todo, lo pusiste
  primero.
- **PNG sin canal alfa.** Sale con fondo blanco o negro. Verifica el `pix_fmt` con ffprobe.
- **`-loop 1` sin `-shortest`.** El render no termina nunca.
- **`eof_action` por defecto con una capa corta.** El último fotograma se congela en pantalla el
  resto del video. Usa `eof_action=pass`.
- **Superponer sin escalar.** ffmpeg inserta conversiones que no controlas, o la capa sale gigante.
- **Poner el logo abajo del todo en vertical.** Queda detrás de la interfaz de Instagram. Deja 560 px.
- **Olvidar `format=yuv420p` al final** después de trabajar con RGBA.
- **`blend`, `hstack` o `vstack` con tamaños distintos.** Falla o produce basura. Iguala antes.
- **Animar con `if` anidados en vez de `clip`.** Ilegible y propenso a errores. Usa
  `clip((t-inicio)/duracion,0,1)`.
- **Movimiento lineal en todo.** Se ve robótico. Añade desaceleración con `1-pow(1-p,2)`.
- **`geq` para animar alfa en un video largo.** Es lentísimo. Usa `fade` con `alpha=1` y `setpts`.
- **Olvidar `setsar=1`** en el picture-in-picture: el recuadro sale estirado.
- **Usar `chromakey` sobre croma mal iluminado** y luego pelear con la tolerancia. El problema está
  en el rodaje, no en el filtro.

---

## Checklist

- [ ] La primera entrada del `overlay` es el fondo y la segunda la capa.
- [ ] Escalé la capa explícitamente antes de superponerla.
- [ ] Verifiqué con ffprobe que el PNG o el video de la capa tiene canal alfa (`rgba` / `yuva420p`).
- [ ] Si la capa es imagen fija, usé `-loop 1` con `-shortest`, o `eof_action=repeat`.
- [ ] Si la capa es un video corto sobre uno largo, puse `eof_action=pass`.
- [ ] Las posiciones respetan las zonas seguras de la plataforma (560 px abajo en vertical).
- [ ] Las apariciones y desapariciones usan `enable` con tiempos que verifiqué contra el corte real.
- [ ] Las entradas y salidas de capa tienen fundido, no aparecen de golpe (salvo que sea intencional).
- [ ] El movimiento usa `clip((t-inicio)/duracion,0,1)` y tiene desaceleración.
- [ ] `format=yuv420p` cierra la cadena de video.
- [ ] Saqué un fotograma en el momento exacto de cada capa para verificar posición y opacidad.
- [ ] Revisé el video en pantalla de celular, no solo en el monitor.
