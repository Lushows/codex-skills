# 17 — Hoja de contactos

## Qué resuelve

Ver 10 minutos de video en **una sola imagen**, en dos segundos, sin reproducir nada. Es la herramienta
más rentable de todo el bloque de lectura del material: cuesta menos de un minuto generarla para un
rodaje entero y te dice qué hay en cada clip, quién sale, cómo está encuadrado, dónde se movió la cámara
y qué momentos hay que no esperabas.

El nombre viene de la fotografía análoga: la **hoja de contactos** (*contact sheet*) era la hoja donde se
imprimía el rollo entero en miniaturas, para elegir qué negativos ampliar sin revelar todo. Lo mismo, con
video.

Un modelo de lenguaje **no puede ver un video corriendo**, pero sí puede ver una imagen. La hoja de
contactos es literalmente el puente que le permite a una IA "ver" un rodaje.

---

## El comando

```bash
ffmpeg -y -i entrada/clip-01.mp4 -vf "fps=1/5,scale=300:-1,tile=5x4" -frames:v 1 analisis/hojas-contacto/clip-01.jpg
```

Eso produce una imagen con 20 fotogramas en rejilla de 5 columnas por 4 filas, uno cada 5 segundos.

Desglose de la cadena de filtros, que se leen de izquierda a derecha:

| Filtro | Qué hace |
|---|---|
| `fps=1/5` | quédate con **un fotograma cada 5 segundos** (el `1/N` es "1 fotograma cada N segundos") |
| `scale=300:-1` | escala cada fotograma a 300 píxeles de ancho; `-1` calcula el alto manteniendo la proporción |
| `tile=5x4` | pega los fotogramas en una rejilla de 5 columnas por 4 filas = 20 casillas |
| `-frames:v 1` | escribe **una sola imagen** de salida, no una secuencia |

---

## Calcular el paso: la fórmula

El `N` de `fps=1/N` no se elige al azar. Se calcula para que los 20 fotogramas cubran el clip completo:

```
N = duracion_del_clip / 20
```

Ejemplos:

| Duración del clip | N (segundos entre fotogramas) | `fps=` |
|---|---|---|
| 40 s | 2 | `fps=1/2` |
| 101 s | 5,05 → usa 5 | `fps=1/5` |
| 600 s (10 min) | 30 | `fps=1/30` |

Si pones un `N` muy grande, la rejilla queda incompleta (casillas negras al final). Si lo pones muy
pequeño, los 20 fotogramas cubren solo el principio del clip y el resto no lo ves — que es el error
silencioso más común de esta técnica.

**Verifica siempre que la última casilla de la rejilla muestre el final del clip.** Si muestra algo del
minuto 2 en un clip de 5 minutos, el paso está mal.

### Script que calcula el paso solo

```powershell
$proyecto = "C:\Users\user\Desktop\VIDEO-BOTELLA"
$dest = Join-Path $proyecto "analisis\hojas-contacto"
New-Item -ItemType Directory -Force -Path $dest | Out-Null

$COLS = 5
$FILAS = 4
$CASILLAS = $COLS * $FILAS

Get-ChildItem (Join-Path $proyecto "entrada") -Filter *.mp4 | Sort-Object Name | ForEach-Object {
  $dur = [double](& ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 $_.FullName)
  $paso = [math]::Max(0.5, [math]::Round($dur / $CASILLAS, 2))
  $out = Join-Path $dest ($_.BaseName + ".jpg")

  & ffmpeg -y -hide_banner -loglevel error -i $_.FullName `
    -vf "fps=1/$paso,scale=300:-1,tile=${COLS}x${FILAS}" `
    -frames:v 1 -q:v 3 $out

  Write-Output ("{0}: {1} s -> 1 foto cada {2} s -> {3}" -f $_.Name, [math]::Round($dur,1), $paso, (Split-Path $out -Leaf))
}
```

El `-q:v 3` controla la calidad del JPG (2 es casi sin pérdida, 31 es basura). Con 3 la hoja pesa poco y
se lee perfecto.

---

## Cómo se lee una hoja de contactos

Las casillas van de izquierda a derecha y de arriba abajo. La casilla número `k` (empezando en 1)
corresponde aproximadamente al segundo:

```
segundo ≈ (k - 1) * paso
```

Con paso 5, la casilla 8 muestra el segundo 35. Eso te da una **ubicación aproximada** para ir a mirar,
no un timecode de corte. Los timecodes de corte salen de la transcripción (módulo 13) y se miden como
dice el módulo 15.

Qué buscar al mirarla, en orden:

1. **Cambios grandes de imagen entre casillas vecinas** → ahí hay un corte, un cambio de plano o un
   movimiento de cámara. Es donde empieza otra toma.
2. **Series de casillas casi idénticas** → cámara quieta, persona hablando. Material de talking head.
3. **Casillas negras o blancas** → arranque, tapón de lente, sobreexposición. Material a descartar.
4. **Casillas borrosas** → movimiento rápido o desenfoque. Puede ser un desastre o una transición
   natural regalada.
5. **Algo que no esperabas** → una persona de más, un objeto, un gesto. Esto es lo que hace que valga la
   pena: la hoja de contactos revela lo que nadie anotó en el rodaje.
6. **Encuadre y aire sobre la cabeza** → decide de una vez si ese clip aguanta un punch-in (módulo 22).

---

## Variantes útiles

### Con el timecode quemado en cada casilla

Muy útil cuando vas a pasarle la hoja a otra persona o a un modelo:

```bash
ffmpeg -y -i entrada/clip-01.mp4 -vf "fps=1/5,drawtext=text='%{pts\:hms}':x=8:y=8:fontsize=22:fontcolor=yellow:box=1:boxcolor=black@0.6,scale=300:-1,tile=5x4" -frames:v 1 analisis/hojas-contacto/clip-01-tc.jpg
```

`drawtext` va **antes** de `scale` para que el texto se escale con la imagen y quede legible. `%{pts\:hms}`
imprime el tiempo en horas:minutos:segundos.

Advertencia coherente con el módulo 15: ese texto sale en `hms`, o sea en formato `minuto:segundo`. Sirve
para ubicarte visualmente, **no** para dictar cortes. Los cortes se dictan en segundos, siempre.

Si prefieres segundos crudos en la casilla:

```bash
ffmpeg -y -i entrada/clip-01.mp4 -vf "fps=1/5,drawtext=text='%{eif\:t\:d}s':x=8:y=8:fontsize=22:fontcolor=yellow:box=1:boxcolor=black@0.6,scale=300:-1,tile=5x4" -frames:v 1 analisis/hojas-contacto/clip-01-seg.jpg
```

### Hoja de todo el rodaje en una imagen

Cuando quieres una vista de pájaro de los 16 clips. Se genera una tira por clip y se apilan:

```powershell
$proyecto = "C:\Users\user\Desktop\VIDEO-BOTELLA"
$tmp = Join-Path $proyecto "trabajo\tiras"
New-Item -ItemType Directory -Force -Path $tmp | Out-Null

Get-ChildItem (Join-Path $proyecto "entrada") -Filter *.mp4 | Sort-Object Name | ForEach-Object {
  $dur = [double](& ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 $_.FullName)
  $paso = [math]::Max(0.5, [math]::Round($dur / 8, 2))
  & ffmpeg -y -hide_banner -loglevel error -i $_.FullName -vf "fps=1/$paso,scale=200:-1,tile=8x1" -frames:v 1 (Join-Path $tmp ($_.BaseName + ".jpg"))
}

$tiras = Get-ChildItem $tmp -Filter *.jpg | Sort-Object Name
$args = @()
foreach ($t in $tiras) { $args += @("-i", $t.FullName) }
$n = $tiras.Count
& ffmpeg -y -hide_banner -loglevel error @args -filter_complex "vstack=inputs=$n" (Join-Path $proyecto "analisis\hojas-contacto\_rodaje-completo.jpg")
Write-Output "Hoja del rodaje completo lista"
```

Cada fila es un clip, 8 fotogramas por clip. Con 16 clips tienes el rodaje entero en una imagen de 16
filas. Es la vista que le pasas a un modelo cuando le preguntas "¿qué material hay aquí?".

### Onda de audio: ver el sonido

La hoja de contactos no dice nada del audio. La onda sí:

```bash
ffmpeg -y -i entrada/clip-01.mp4 -filter_complex "showwavespic=s=1600x300:colors=white" -frames:v 1 analisis/hojas-contacto/clip-01-onda.png
```

Qué se lee en una onda:

- **Bloques de actividad separados por planos** → cada bloque es una toma, cada plano es la pausa entre
  tomas. La onda te dice **cuántas tomas hay** en el clip sin transcribir.
- **La onda pegada al borde superior e inferior** → saturación. Confirma con `volumedetect` (módulo 11).
- **Una onda muy baja, casi una línea** → grabado muy suave.
- **Un pico aislado enorme** → un golpe, una puerta, un tropiezo. Buen candidato a blooper o a ruido a
  eliminar.

### Espectrograma: diagnosticar problemas de sonido

```bash
ffmpeg -y -i entrada/clip-01.mp4 -lavfi "showspectrumpic=s=1600x600:legend=1" -frames:v 1 analisis/hojas-contacto/clip-01-espectro.png
```

Un **espectrograma** muestra qué frecuencias suenan a lo largo del tiempo: el eje horizontal es tiempo, el
vertical es frecuencia (grave abajo, agudo arriba), y el color es intensidad.

Lo que se diagnostica de un vistazo:

| Lo que ves | Qué es |
|---|---|
| Una línea horizontal constante y fina | zumbido eléctrico (50/60 Hz) o aire acondicionado |
| Una franja gruesa en la parte baja, todo el tiempo | ruido de fondo grave, tráfico, motor |
| Un corte limpio horizontal arriba (nada por encima de 8 o 15 kHz) | el audio ya venía comprimido (WhatsApp, mp3 malo) |
| Manchas verticales que llegan hasta arriba | golpes, "p" explosivas, clics |
| Zona media (300 Hz – 4 kHz) bien poblada | la voz está ahí y está sana |

---

## Cómo pasarle la hoja a un modelo

Sube la imagen y pide lectura estructurada, no impresiones:

```
Te paso la hoja de contactos de clip-12. Son 20 fotogramas en rejilla 5x4,
uno cada 5.05 segundos, en orden de izquierda a derecha y de arriba abajo.
La casilla 1 es el segundo 0.

Describeme, casilla por casilla y en una linea cada una:
que se ve, quien aparece, tipo de plano (general / medio / primer plano),
y si hay algo raro (negro, movido, tapado).

Al final dime:
1. En que casillas parece cambiar la toma (imagen muy distinta a la anterior).
2. Que casillas se ven inservibles y por que.
3. Que ves aqui que no esperarias en un video de producto.

No inventes lo que no se ve. Si una casilla no se entiende, dilo.
```

La tercera pregunta es la importante: es la que hace aflorar lo que nadie anotó.

**Advertencia honesta:** una hoja de contactos muestra 20 instantes de miles. Todo lo que pase entre dos
casillas es invisible. Nunca descartes un clip por su hoja de contactos — descártalo por su
transcripción (módulo 13) o por haberlo visto. La hoja mapea, no juzga.

---

## Cuándo usar cuál

| Necesitas saber | Herramienta |
|---|---|
| Qué se ve en el clip, cuántas tomas hay visualmente | hoja de contactos 5x4 |
| Panorama del rodaje entero de un vistazo | tiras apiladas, 8 por clip |
| Dónde ubicar un momento para ir a mirarlo | hoja con timecode quemado |
| Cuántas tomas hay y dónde están las pausas | onda de audio |
| Por qué el audio suena mal | espectrograma |
| Qué se dice y dónde exactamente | transcripción (módulo 13) — la hoja no sirve para esto |

---

## Errores comunes

- **Usar un paso fijo para todos los clips.** Con `fps=1/5` en un clip de 10 minutos ves solo el primer
  minuto y medio. El paso se calcula: `duracion / 20`.
- **No verificar que la última casilla llegue al final del clip.** Es el fallo silencioso: crees que
  mapeaste el clip y mapeaste el principio.
- **Descartar un clip por su hoja de contactos.** 20 instantes de miles. La joya del proyecto real estaba
  en un clip que se veía aburrido.
- **Poner `drawtext` después de `scale`.** El texto queda diminuto o gigante. Va antes de escalar.
- **Escalar a 300 px y luego quejarse de que no se ven las caras.** Para lectura fina sube a
  `scale=480:-1` y baja a rejilla 4x3; pesa más pero se lee.
- **Olvidar `-frames:v 1`.** Sin eso ffmpeg escribe una secuencia de imágenes y te llena la carpeta.
- **Creer que la hoja dice algo del audio.** No dice nada. Para audio, onda y espectrograma.
- **Pedirle a un modelo "resume esta hoja".** Igual que en el módulo 12: pídele descripción casilla por
  casilla y qué le sorprende, no un resumen.
- **Usar el `hms` del `drawtext` para dictar cortes.** Ese formato es `minuto:segundo` y reintroduce la
  ambigüedad del módulo 15. Sirve para ubicarte, no para cortar.

---

## Checklist

- [ ] Cada clip de `entrada/` tiene su hoja de contactos en `analisis/hojas-contacto/`
- [ ] El paso de cada hoja se calculó como `duracion / 20`, no fijo
- [ ] Se verificó en al menos dos hojas que la última casilla corresponde al final del clip
- [ ] Existe la hoja del rodaje completo (tiras apiladas) para la vista de pájaro
- [ ] Los clips largos o sospechosos tienen además hoja con timecode quemado
- [ ] Cada clip con audio tiene su onda (`showwavespic`) generada
- [ ] Los clips con audio problemático tienen su espectrograma (`showspectrumpic`)
- [ ] Se anotó, por clip, en qué casillas parece cambiar la toma
- [ ] Se anotó qué material se ve inservible (negro, movido, tapado)
- [ ] Se anotó al menos un hallazgo inesperado por rodaje, o se confirmó explícitamente que no hay
- [ ] Ningún clip fue descartado con base únicamente en su hoja de contactos
- [ ] Los hallazgos visuales están volcados al mapa de bloques (módulo 19)
