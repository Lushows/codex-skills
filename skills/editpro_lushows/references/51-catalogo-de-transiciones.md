# 51 — Catálogo de transiciones: las 58 de xfade

> Lee `50-cuando-usar-transicion.md` antes que este archivo. Este es el catálogo de herramientas;
> el otro te dice si debes abrir la caja.

ffmpeg trae un filtro llamado `xfade` que hace transiciones entre dos videos. En la versión instalada
(ffmpeg 8.1.2, agosto 2026) trae **58 transiciones**, numeradas del `-1` al `57`. Se llaman por nombre,
no por número.

**Comprueba siempre la lista de tu compilación** antes de prometerle algo al cliente:

```bash
ffmpeg -h filter=xfade
```

Si una transición no aparece ahí, tu ffmpeg no la tiene y no hay nada que hacer salvo actualizar.

---

## Lo primero: el cálculo de `offset` (aquí se equivoca todo el mundo)

`xfade` necesita tres cosas:

| Parámetro | Qué es |
|---|---|
| `transition` | Cuál de las 58 |
| `duration` | Cuánto dura la transición, en segundos |
| `offset` | **En qué segundo del PRIMER video empieza la transición** |

El error universal es poner `offset` igual a la duración del primer clip. Si haces eso, la transición
empieza justo cuando el primer clip se acabó — o sea, no hay con qué mezclar, y te queda un congelado
o un negro.

### La fórmula

```
offset = duración_del_primer_clip - duración_de_la_transición
```

**Ejemplo real, verificado:** dos clips de 4,000 s cada uno, transición de 0,5 s.

```
offset = 4.0 - 0.5 = 3.5
```

```bash
ffmpeg -i a.mp4 -i b.mp4 \
  -filter_complex "[0:v][1:v]xfade=transition=smoothleft:duration=0.5:offset=3.5[v];[0:a][1:a]acrossfade=d=0.5[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p -c:a aac salida.mp4
```

Duración resultante medida: **7,53 s**. La cuenta esperada era 4 + 4 − 0,5 = 7,5. Cuadra (el sobrante
es el redondeo del último fotograma de audio).

> **La duración final siempre es:** suma de los clips − suma de las transiciones.

### Cómo saber la duración exacta de un clip

Nunca la adivines ni la leas del explorador de archivos:

```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 a.mp4
```

### El encadenado de 3 o más clips (la segunda trampa)

Cuando encadenas, **el segundo `offset` no se calcula sobre el segundo clip: se calcula sobre la
salida acumulada del primer `xfade`**.

Tres clips de 4 s, transiciones de 0,5 s:

- Primer `xfade`: `offset = 4.0 − 0.5 = 3.5`. La salida `[v01]` dura 4 + 4 − 0,5 = **7,5 s**.
- Segundo `xfade`: `offset = 7.5 − 0.5 = 7.0`.

```bash
ffmpeg -i a.mp4 -i b.mp4 -i c.mp4 -filter_complex \
"[0:v][1:v]xfade=transition=fade:duration=0.5:offset=3.5[v01];\
[v01][2:v]xfade=transition=circleopen:duration=0.5:offset=7.0[v]" \
  -map "[v]" -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p salida3.mp4
```

Duración medida: **11,000 s** = 4 + 4 + 4 − 0,5 − 0,5. Correcto.

### La fórmula acumulada, para N clips

```
offset(1) = dur(1) − trans(1)
offset(n) = offset(n-1) + dur(n) − trans(n)
```

En palabras: al offset anterior le sumas la duración del clip que acabas de meter y le restas la
transición nueva. Si vas a encadenar más de tres clips, **haz la tabla en un archivo antes de escribir
el comando**. Calcular esto de cabeza es cómo se pierden dos horas.

### Requisitos que xfade impone (y que no perdona)

Los dos videos que entran a `xfade` deben coincidir en:

- **Resolución** exacta
- **Formato de píxel** (`yuv420p`, etc.)
- Idealmente, misma tasa de fotogramas

Si no coinciden, el error es este, literal:

```
[Parsed_xfade_0] First input link main parameters (size 640x360) do not match the
corresponding second input link xfade parameters (size 1280x720)
```

La solución es normalizar antes de mezclar:

```bash
ffmpeg -i a.mp4 -i b.mp4 -filter_complex \
"[0:v]scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,fps=30,format=yuv420p,setsar=1[v0];\
[1:v]scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,fps=30,format=yuv420p,setsar=1[v1];\
[v0][v1]xfade=transition=fade:duration=0.3:offset=3.7[v]" \
  -map "[v]" -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p salida.mp4
```

El `setsar=1` no es opcional: sin él, un clip de celular con relación de píxel rara puede pasar el
`scale` y aun así ser rechazado.

### El audio no lo hace xfade

`xfade` es solo video. El audio se cruza aparte con `acrossfade`, con la **misma duración**:

```
[0:a][1:a]acrossfade=d=0.5[a]
```

Si te olvidas, el audio se corta seco en medio de la transición visual y suena a error.

---

## El catálogo — las 58

Las agrupo por lo que **significan**, no por su número. Al lado de cada una: para qué sirve de verdad.

### Grupo 1 — Fundidos (lo que se usa el 80% de las veces)

| Nombre | Nº | Para qué sirve |
|---|---|---|
| `fade` | 0 | La disolvencia clásica. Paso de tiempo, relación entre dos planos. La más segura. |
| `fadeblack` | 12 | Fin de capítulo. Punto y aparte. Nunca en la mitad de un vertical corto. |
| `fadewhite` | 13 | Transformación, energía, "antes y después". Base del flash publicitario (ver `53`). |
| `fadegrays` | 36 | Pasa por gris antes de resolver. Se lee melancólico, de recuerdo. Muy poco usada. |
| `fadefast` | 44 | Fundido con curva acelerada: se va rápido y llega lento. Más punch que `fade`. |
| `fadeslow` | 45 | Lo contrario: arranca despacio. Se siente contemplativo. Documental. |
| `dissolve` | 25 | Disuelve por píxeles al azar, no por opacidad. Textura arenosa, se ve orgánico. |

**Recomendación honesta:** si dudas, `fade`. Es la única transición que nunca se ve pretenciosa.

### Grupo 2 — Barridos duros (el plano nuevo entra con borde recto)

| Nombre | Nº | Para qué sirve |
|---|---|---|
| `wipeleft` | 1 | Borde que barre hacia la izquierda. Cambio de lugar, lista de puntos. |
| `wiperight` | 2 | Igual hacia la derecha. Sugiere "avanzar". |
| `wipeup` | 3 | Hacia arriba. En vertical se siente como deslizar el feed. |
| `wipedown` | 4 | Hacia abajo. Menos natural en vertical. |
| `wipetl` | 37 | Diagonal desde la esquina superior izquierda. |
| `wipetr` | 38 | Diagonal desde arriba a la derecha. |
| `wipebl` | 39 | Diagonal desde abajo a la izquierda. |
| `wipebr` | 40 | Diagonal desde abajo a la derecha. |
| `diagtl` | 27 | Diagonal completa desde arriba-izquierda (barre en ángulo). |
| `diagtr` | 28 | Diagonal desde arriba-derecha. |
| `diagbl` | 29 | Diagonal desde abajo-izquierda. |
| `diagbr` | 30 | Diagonal desde abajo-derecha. |

Los barridos son gráficos, no realistas. Encajan en explicativos, en piezas con mucha tipografía y en
publicidad que ya asume su artificio. En un documental se ven fuera de lugar.

### Grupo 3 — Barridos suaves (borde difuso)

| Nombre | Nº | Para qué sirve |
|---|---|---|
| `smoothleft` | 15 | Como `wipeleft` pero con el borde degradado. Mucho más elegante. |
| `smoothright` | 16 | Ídem hacia la derecha. |
| `smoothup` | 17 | Ídem hacia arriba. En vertical es de las mejores. |
| `smoothdown` | 18 | Ídem hacia abajo. |

**Estos cuatro son el secreto mejor guardado de `xfade`.** Dan sensación de movimiento sin el borde
duro que delata el efecto. En vertical, `smoothup` a 0,25 s se siente premium.

### Grupo 4 — Deslizamientos (la imagen entera se mueve)

| Nombre | Nº | Para qué sirve |
|---|---|---|
| `slideleft` | 5 | Las dos imágenes se corren juntas hacia la izquierda. Como pasar diapositiva. |
| `slideright` | 6 | Hacia la derecha. |
| `slideup` | 7 | Hacia arriba. Lenguaje de app / feed. |
| `slidedown` | 8 | Hacia abajo. Se lee como "volver atrás". |
| `coverleft` | 50 | El plano nuevo **entra encima** desde la derecha. El viejo se queda quieto. |
| `coverright` | 51 | Ídem desde la izquierda. |
| `coverup` | 52 | Entra desde abajo tapando. Muy natural en vertical. |
| `coverdown` | 53 | Entra desde arriba tapando. |
| `revealleft` | 54 | El plano viejo **se corre y deja ver** el nuevo, que estaba debajo. |
| `revealright` | 55 | Ídem hacia el otro lado. |
| `revealup` | 56 | El viejo sube y descubre el nuevo. |
| `revealdown` | 57 | El viejo baja y descubre el nuevo. |

`cover*` y `reveal*` son las más modernas del set. Se sienten como interfaz de aplicación, no como
transición de editor de los 2000. Si el proyecto tiene lenguaje digital, empieza por ahí.

### Grupo 5 — Geométricas y de iris

| Nombre | Nº | Para qué sirve |
|---|---|---|
| `circlecrop` | 9 | Un círculo recorta y revela. Efecto de mirilla. |
| `rectcrop` | 10 | Igual con rectángulo. |
| `circleopen` | 19 | El círculo se abre desde el centro. Apertura, revelación. |
| `circleclose` | 20 | El círculo se cierra. "Fin". Guiño a dibujos animados. |
| `radial` | 14 | Barrido en aspa, como manecilla de reloj. Sugiere paso de tiempo. |
| `vertopen` | 21 | Se abre por el centro en vertical, como una cortina. |
| `vertclose` | 22 | Se cierra por el centro en vertical. |
| `horzopen` | 23 | Se abre horizontalmente. |
| `horzclose` | 24 | Se cierra horizontalmente. |
| `distance` | 11 | Mezcla según la distancia de color entre los dos planos. Resultado impredecible. |

Las de iris (`circleopen` / `circleclose`) cargan mucha referencia de época. Úsalas solo si la quieres.

### Grupo 6 — Deformación y textura

| Nombre | Nº | Para qué sirve |
|---|---|---|
| `hblur` | 35 | Desenfoque horizontal en el cruce. Base del "whip" barato. Cuidado (`56`). |
| `pixelize` | 26 | Se pixela y se resuelve. Lenguaje de videojuego / digital / error. |
| `squeezeh` | 41 | El plano se aplasta horizontalmente. Se siente de televisor viejo. |
| `squeezev` | 42 | Aplastado vertical. |
| `zoomin` | 43 | Zoom hacia dentro al cambiar. **La transición más sobreusada de internet.** Ver `56`. |

### Grupo 7 — Rebanadas y viento (texturas puras, sin lectura cultural)

| Nombre | Nº | Para qué sirve |
|---|---|---|
| `hlslice` | 31 | Tiras horizontales que entran desde la izquierda. |
| `hrslice` | 32 | Tiras horizontales desde la derecha. |
| `vuslice` | 33 | Tiras verticales hacia arriba. |
| `vdslice` | 34 | Tiras verticales hacia abajo. |
| `hlwind` | 46 | Efecto "viento" horizontal a la izquierda: la imagen se deshilacha. |
| `hrwind` | 47 | Viento a la derecha. |
| `vuwind` | 48 | Viento hacia arriba. |
| `vdwind` | 49 | Viento hacia abajo. |

Estas ocho no significan nada por sí solas. Son textura gráfica. Si tu proyecto ya tiene un sistema
visual con tramas o líneas, pueden encajar. Si no, se van a sentir gratuitas.

### Grupo 8 — La que vale por las otras 57: `custom`

| Nombre | Nº | Para qué sirve |
|---|---|---|
| `custom` | -1 | Escribes tú la fórmula de la mezcla. Transición única, imposible de copiar. |

Con `transition=custom` le pasas una expresión en `expr`. Variables disponibles:
`X`, `Y` (posición del píxel), `W`, `H` (tamaño), `P` (progreso de 0 a 1), `A` (el píxel del video
que sale), `B` (el del que entra).

Ejemplo verificado — un barrido de derecha a izquierda escrito a mano:

```bash
ffmpeg -i a.mp4 -i b.mp4 -filter_complex \
"[0:v][1:v]xfade=transition=custom:duration=1:offset=3:expr='if(gt(X, W*(1-P)), A, B)'[v]" \
  -map "[v]" -an -c:v libx264 -preset veryfast -pix_fmt yuv420p custom.mp4
```

Ahí está el valor real de `custom`: es la puerta a una transición que sea **tuya**, derivada de la
marca. Ver `52-transiciones-de-marca.md`.

---

## Plantilla lista para copiar (N clips, offsets calculados)

Guarda esto como referencia. Reemplaza duraciones y transiciones:

```bash
# Paso 1 - mide TODOS los clips, uno por uno
for f in plano01.mp4 plano02.mp4 plano03.mp4; do
  echo -n "$f "
  ffprobe -v error -show_entries format=duration -of csv=p=0 "$f"
done

# Paso 2 - calcula la tabla de offsets a mano y anotala
# plano01 = 3.20  trans = 0.25  -> offset1 = 3.20 - 0.25 = 2.95
# acumulado tras xfade 1 = 3.20 + 2.80 - 0.25 = 5.75
# plano02 = 2.80  trans = 0.25  -> offset2 = 5.75 - 0.25 = 5.50

# Paso 3 - arma el comando con esos numeros
ffmpeg -i plano01.mp4 -i plano02.mp4 -i plano03.mp4 -filter_complex \
"[0:v]scale=1080:1920,fps=30,format=yuv420p,setsar=1[v0];\
 [1:v]scale=1080:1920,fps=30,format=yuv420p,setsar=1[v1];\
 [2:v]scale=1080:1920,fps=30,format=yuv420p,setsar=1[v2];\
 [v0][v1]xfade=transition=smoothup:duration=0.25:offset=2.95[x1];\
 [x1][v2]xfade=transition=fade:duration=0.25:offset=5.50[v]" \
  -map "[v]" -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p montaje.mp4

# Paso 4 - verifica que la duracion sea la esperada
ffprobe -v error -show_entries format=duration -of csv=p=0 montaje.mp4
```

Si el resultado no coincide con `suma_de_clips − suma_de_transiciones`, **algo está mal en tus
offsets**. No sigas: revisa la tabla.

---

## Errores comunes

- **`offset` = duración del primer clip.** El error número uno. Te queda un congelado o un negro
  donde debía haber mezcla. La fórmula es `duración − transición`.

- **Encadenar calculando el segundo offset sobre el segundo clip.** El offset del segundo `xfade` se
  mide sobre la salida acumulada, no sobre el clip nuevo. Es el error número dos.

- **Olvidar `acrossfade` en el audio.** El video cruza suave y el audio pega un salto seco. Suena a
  archivo dañado.

- **Meter clips de distinta resolución.** ffmpeg te tira el error de "input link parameters do not
  match" y la gente cree que el filtro está roto. No: normaliza antes con `scale` + `fps` + `format`
  + `setsar=1`.

- **Usar el número en vez del nombre.** `transition=15` funciona pero nadie lo entiende al releer el
  script en tres meses. Escribe `transition=smoothleft`.

- **Suponer que tu ffmpeg tiene las 58.** Compilaciones viejas traen menos. Corre
  `ffmpeg -h filter=xfade` antes de prometer.

- **Usar `zoomin` porque se ve "dinámica".** Es la firma del video genérico. Ver `56`.

- **No verificar la duración final.** Es la comprobación más barata que existe y caza el 100% de los
  errores de offset.

- **Poner `duration` mayor que el clip más corto.** El clip nunca se ve limpio.

---

## Checklist

- [ ] Corrí `ffmpeg -h filter=xfade` y confirmé que la transición que quiero existe en esta máquina.
- [ ] Medí la duración real de cada clip con `ffprobe`, no la supuse.
- [ ] Escribí la tabla de offsets antes de escribir el comando.
- [ ] Cada `offset` sale de `acumulado_anterior − duración_de_la_transición`.
- [ ] Todos los clips están normalizados: misma resolución, mismo fps, `format=yuv420p`, `setsar=1`.
- [ ] El audio cruza con `acrossfade` usando la misma duración que el video.
- [ ] La transición se llama por nombre, no por número.
- [ ] La duración de la transición es menor que el plano más corto que une.
- [ ] Verifiqué que la duración final = suma de clips − suma de transiciones.
- [ ] Cada transición del montaje pasa el test de `50`: comunica algo concreto.
