# 107 — Transiciones con xfade y acrossfade

El filtro `xfade` hace transiciones entre dos videos. Es el filtro más útil para montaje y el que más
gente usa mal, porque el parámetro `offset` no significa lo que parece.

Antes de nada, la advertencia de oficio: **una transición es una herramienta narrativa, no un adorno.**
El 90% de los cortes en un buen montaje son cortes secos. Una transición se justifica cuando cambias
de tiempo, de lugar o de idea. Si pones un `circleopen` entre dos planos de la misma escena, el video
se ve peor, no mejor.

---

## Sintaxis

```bash
[a][b]xfade=transition=fade:duration=1:offset=4[salida]
```

- `transition` — el tipo de transición
- `duration` — cuánto dura la transición, en segundos
- `offset` — **en qué segundo de la línea de tiempo del primer clip empieza la transición**
- `expr` — solo para `transition=custom`

Comando mínimo real:

```bash
ffmpeg -hide_banner -y -i a.mp4 -i b.mp4 -filter_complex \
"[0:v][1:v]xfade=transition=fade:duration=1:offset=4,format=yuv420p[v]" \
-map "[v]" -an -c:v libx264 -crf 20 -preset slow salida.mp4
```

---

## Los requisitos que xfade NO perdona

`xfade` es exigente. Si algo de esto falla, o el comando revienta o el resultado es basura.

1. **Misma resolución** en los dos clips.
2. **Mismo formato de píxel.**
3. **Mismo fps.** Y tiene que ser constante, no variable.
4. **Misma SAR.**
5. **Los timestamps deben empezar en 0** en ambos clips.
6. **El primer clip debe durar al menos `offset + duration`.** Si no, sale negro o se corta.

La preparación estándar, que debes poner **siempre** antes de un `xfade`:

```bash
[0:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,format=yuv420p,setpts=PTS-STARTPTS[v0];
[1:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,format=yuv420p,setpts=PTS-STARTPTS[v1];
[v0][v1]xfade=transition=fade:duration=0.5:offset=4.5[vx]
```

`setpts=PTS-STARTPTS` es el que más se olvida. Si un clip vino de un `-ss` sin reiniciar timestamps,
`xfade` calcula el offset sobre el tiempo original y la transición ocurre en un lugar que no existe:
verás negro, o la transición no ocurre en absoluto.

---

## El cálculo del offset: la parte que todos fallan

**`offset` es el segundo, contado desde el inicio del PRIMER clip, en el que arranca la transición.**

Con un clip A de 5 segundos, un clip B de 5 segundos y una transición de 1 segundo:

```
offset = 5 - 1 = 4
```

La transición empieza en el segundo 4 de A y termina en el 5 (que es donde A se acaba). El resultado
dura `5 + 5 - 1 = 9` segundos.

**Fórmula para el primer par:**

```
offset = duracion_de_A - duracion_de_la_transicion
```

**Fórmula general cuando encadenas varias:** el offset se calcula sobre la línea de tiempo del
**resultado acumulado**, que ya se acortó por las transiciones anteriores.

```
offset_k = (d0 + d1 + ... + dk) - k * T
```

donde `dk` es la duración del clip k (empezando en 0), `T` la duración de la transición, y `k` el
número de transición (1 para la primera, 2 para la segunda, etc.).

### Ejemplo trabajado

Cuatro clips de 6, 4, 8 y 5 segundos. Transiciones de 0.5 segundos.

| Transición | Cálculo | offset |
|---|---|---|
| 1 (A a B) | 6 - 0.5 | **5.5** |
| 2 (AB a C) | 6+4 - 2*0.5 | **9.0** |
| 3 (ABC a D) | 6+4+8 - 3*0.5 | **16.5** |

Duración final: `6+4+8+5 - 3*0.5 = 21.5` segundos.

Comprueba la aritmética: la transición 2 empieza en el segundo 9 del video acumulado. Hasta ahí van A
(6 s) y B (4 s), o sea 10 segundos de material, menos los 0.5 que se solaparon en la transición 1 =
9.5 segundos de material. La transición empieza 0.5 antes del final de B: 9.5 - 0.5 = 9.0. Cuadra.

### Script para calcular los offsets

```powershell
# Calcula offsets de xfade para todos los mp4 de la carpeta
$T = 0.5
$archivos = Get-ChildItem "clip*.mp4" | Sort-Object Name
$acumulado = 0.0
$k = 0
foreach ($f in $archivos) {
  $d = [double](ffprobe -v error -show_entries format=duration -of csv=p=0 $f.FullName)
  $acumulado += $d
  if ($k -gt 0) {
    $offset = $acumulado - $d - ($k - 1) * $T
    # ese offset corresponde a la transicion que une lo anterior con ESTE clip
  }
  "{0,-16} dur={1,7:N3}  acumulado={2,8:N3}" -f $f.Name, $d, $acumulado
  $k++
}
"Duracion final estimada: {0:N3}" -f ($acumulado - ($archivos.Count - 1) * $T)
```

```bash
# Bash: lista duraciones y offsets
T=0.5; acc=0; k=0
for f in clip*.mp4; do
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  acc=$(echo "$acc + $d" | bc -l)
  if [ $k -gt 0 ]; then
    off=$(echo "$acc - $d - ($k - 1) * $T" | bc -l)
    printf "transicion %d -> offset %.3f\n" "$k" "$off"
  fi
  k=$((k+1))
done
printf "duracion final %.3f\n" "$(echo "$acc - ($k - 1) * $T" | bc -l)"
```

**Nunca calcules offsets a ojo con más de dos clips.** Un error de medio segundo en la transición 2 se
arrastra a todas las siguientes y el video termina con negro al final.

---

## Encadenar varias transiciones

Cada `xfade` produce una salida que alimenta al siguiente.

```bash
ffmpeg -hide_banner -y -i c1.mp4 -i c2.mp4 -i c3.mp4 -i c4.mp4 -filter_complex "\
[0:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,format=yuv420p,setpts=PTS-STARTPTS[v0]; \
[1:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,format=yuv420p,setpts=PTS-STARTPTS[v1]; \
[2:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,format=yuv420p,setpts=PTS-STARTPTS[v2]; \
[3:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,format=yuv420p,setpts=PTS-STARTPTS[v3]; \
[v0][v1]xfade=transition=fade:duration=0.5:offset=5.5[x1]; \
[x1][v2]xfade=transition=wipeleft:duration=0.5:offset=9.0[x2]; \
[x2][v3]xfade=transition=fade:duration=0.5:offset=16.5,format=yuv420p[v]; \
[0:a][1:a]acrossfade=d=0.5:c1=tri:c2=tri[a1]; \
[a1][2:a]acrossfade=d=0.5:c1=tri:c2=tri[a2]; \
[a2][3:a]acrossfade=d=0.5:c1=tri:c2=tri[a]" \
-map "[v]" -map "[a]" \
-c:v libx264 -crf 20 -preset slow -c:a aac -b:a 192k -ar 48000 -movflags +faststart montaje.mp4
```

Ese comando es un montaje de 4 clips con transiciones de video y audio, en una sola pasada. Guárdalo
como plantilla.

**Cuando son más de 5 o 6 clips, escribe el grafo en un archivo** con `-filter_complex_script` (ver
`104`) y genéralo con un script que calcule los offsets. A mano no es sostenible.

---

## Las transiciones disponibles

Lista completa que acepta `transition=`:

```
fade  fadeblack  fadewhite  fadegrays  distance  dissolve  pixelize  radial
wipeleft  wiperight  wipeup  wipedown
wipetl  wipetr  wipebl  wipebr
slideleft  slideright  slideup  slidedown
smoothleft  smoothright  smoothup  smoothdown
circlecrop  rectcrop  circleclose  circleopen
horzclose  horzopen  vertclose  vertopen
diagbl  diagbr  diagtl  diagtr
hlslice  hrslice  vuslice  vdslice
hblur  squeezev  squeezeh  zoomin
hlwind  hrwind  vuwind  vdwind
coverleft  coverright  coverup  coverdown
revealleft  revealright  revealup  revealdown
custom
```

Ver la lista de tu compilación:

```bash
ffmpeg -hide_banner -h filter=xfade
```

### Cuáles usar de verdad

| Transición | Cuándo funciona |
|---|---|
| `fade` | cambio de escena, paso de tiempo. El caballo de batalla. 0.3 a 0.8 s |
| `fadeblack` | final de bloque, cambio de capítulo. 0.5 a 1.2 s |
| `fadewhite` | recuerdo, flashback, cambio de energía hacia arriba |
| `dissolve` | fundido con textura, más orgánico que `fade` |
| `wipeleft` / `wiperight` | cambio de tema en contenido explicativo. Rápido: 0.25 a 0.4 s |
| `slideleft` / `slideup` | navegación, listas, pasos numerados. 0.25 a 0.35 s |
| `smoothleft` | como wipe pero con borde difuso. Más suave |
| `zoomin` | energía, ritmo alto. Muy corto: 0.15 a 0.25 s |
| `hblur` | ocultar un salto de eje o un corte feo |
| `pixelize` | estética digital, glitch |

Lo demás (`circleopen`, `radial`, `hlwind`, `diagbl`) existe pero se ve a plantilla de PowerPoint.
Úsalo solo si la marca lo pide.

### Duraciones honestas

- **Contenido rápido (reels, TikTok):** 0.15 a 0.35 segundos. Más largo mata el ritmo.
- **Contenido medio (YouTube, explicativos):** 0.4 a 0.7 segundos.
- **Documental, corporativo, emocional:** 0.8 a 1.5 segundos.
- **Fundido a negro de cierre:** 1 a 2 segundos.

**Regla:** si dudas, más corto. Una transición que se nota es una transición demasiado larga.

### Transición personalizada

```bash
xfade=transition=custom:duration=1:offset=4:expr='A*(1-P)+B*P'
```

Variables disponibles en `expr`: `X`, `Y` (coordenadas), `W`, `H` (tamaño), `P` (progreso de 0 a 1),
`PLANE`, `A` (valor del primer video), `B` (valor del segundo).

Ejemplos:

```bash
# Barrido diagonal duro
expr='if(gt(X/W+Y/H, 2*P), A, B)'

# Fundido con curva (arranca lento, termina rápido)
expr='A*(1-P*P)+B*(P*P)'

# Barrido vertical con borde suave de 100 px
expr='mix(A, B, clip((Y-(H+200)*P+100)/100, 0, 1))'
```

Es lento (calcula por píxel) pero permite cosas que no están en la lista.

---

## acrossfade — la transición de audio

`xfade` **solo toca el video**. Si no haces nada con el audio, el audio del clip A se corta seco
mientras el video se funde. Se nota muchísimo.

```bash
[0:a][1:a]acrossfade=d=0.5:c1=tri:c2=tri[a]
```

- `d` — duración del cruce. **Debe coincidir con la `duration` del `xfade`.**
- `c1` — curva de salida del primer audio
- `c2` — curva de entrada del segundo
- `o` — 1 (por defecto) para que se solapen; 0 para que sea secuencial

Curvas: las mismas de `afade` (`tri`, `qsin`, `hsin`, `esin`, `log`, `exp`, `par`, `cub`, `squ`,
`nofade`...).

**Combinaciones que suenan bien:**

- Voz con voz: `c1=tri:c2=tri` (lineal, no deja hueco)
- Música con música: `c1=qsin:c2=qsin` (potencia constante, sin bajón en el medio)
- Ambiente con ambiente: `c1=log:c2=exp`

**La trampa de `acrossfade`:** no tiene `offset`. Siempre cruza **al final del primer audio con el
inicio del segundo**. Eso significa que **`acrossfade` funciona solo si el audio del clip dura
exactamente lo que el clip**. Si recortaste el video con `xfade` pero el audio es más largo, el cruce
cae donde no debe.

Solución: recorta el audio a la misma longitud antes:

```bash
[0:a]atrim=0:6,asetpts=PTS-STARTPTS[a0];
[1:a]atrim=0:4,asetpts=PTS-STARTPTS[a1];
[a0][a1]acrossfade=d=0.5:c1=tri:c2=tri[a]
```

### Cuando el audio es una pista continua

Si el montaje va con música que corre por encima de todo, **no uses `acrossfade` en absoluto**.
Monta el video con `xfade` y pon la música aparte:

```bash
ffmpeg -hide_banner -y -i c1.mp4 -i c2.mp4 -i c3.mp4 -i musica.mp3 -filter_complex "\
[0:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,setpts=PTS-STARTPTS[v0]; \
[1:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,setpts=PTS-STARTPTS[v1]; \
[2:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,setpts=PTS-STARTPTS[v2]; \
[v0][v1]xfade=transition=fade:duration=0.4:offset=4.6[x1]; \
[x1][v2]xfade=transition=fade:duration=0.4:offset=9.2,format=yuv420p[v]; \
[3:a]volume=0.5,afade=t=in:st=0:d=1,afade=t=out:st=12.4:d=1.4,loudnorm=I=-14:TP=-1.0[a]" \
-map "[v]" -map "[a]" -t 13.8 \
-c:v libx264 -crf 20 -preset slow -c:a aac -b:a 192k -ar 48000 -movflags +faststart montaje.mp4
```

Es más simple, suena mejor y no hay que cuadrar duraciones de audio.

---

## La alternativa: transiciones sin xfade

`xfade` no es la única forma. Para algunos efectos, otras rutas son mejores.

**Fundido a negro entre dos clips ya unidos** (más simple que xfade si ya tienes el concat):

```bash
-vf "fade=t=out:st=5:d=0.5,fade=t=in:st=5.5:d=0.5"
```

**Corte con destello blanco** (el "flash cut" de los reels):

```bash
ffmpeg -y -i unido.mp4 -vf \
"drawbox=x=0:y=0:w=iw:h=ih:color=white@1:t=fill:enable='between(t,5.00,5.06)'" \
-c:v libx264 -crf 20 -c:a copy salida.mp4
```

Dos fotogramas de blanco puro. Cuesta nada y funciona mejor que cualquier `xfade` en contenido rápido.

**Corte con desenfoque de movimiento** (whip pan falso):

```bash
-vf "gblur=sigma='if(between(t,4.9,5.1), 40*(1-abs(t-5)/0.1), 0)':enable='between(t,4.9,5.1)'"
```

**Superposición corta en vez de transición** (ver `105`): a veces lo que quieres no es fundir dos
planos sino que uno pase por encima del otro.

---

## Errores comunes

- **Calcular `offset` como "el segundo donde quiero que se vea el cambio".** `offset` es donde
  **empieza** la transición, no donde termina.
- **Olvidar restar la duración de la transición al acumular offsets.** El error se acumula y el video
  termina en negro.
- **Olvidar `setpts=PTS-STARTPTS`.** La transición ocurre en un tiempo que no existe.
- **Clips con fps distintos.** `xfade` produce saltos o falla.
- **Clips con resolución o SAR distinta.** Falla con error de reinicialización.
- **`offset + duration` mayor que la duración del primer clip.** Sale negro al final de la transición.
- **Olvidar el audio.** El video se funde y el sonido se corta seco. Usa `acrossfade` o una pista
  continua aparte.
- **`d` de `acrossfade` distinto de `duration` de `xfade`.** El audio y el video se desfasan.
- **Usar `acrossfade` con audio más largo que el video.** El cruce cae donde no es. Recorta primero.
- **Transiciones de 1 segundo en contenido rápido.** Mata el ritmo y la retención.
- **Poner transición en cada corte.** Un montaje con 30 transiciones es un montaje sin ritmo.
- **Escoger `circleopen` o `radial` porque estaban en la lista.** Se ve a plantilla.
- **Encadenar 10 transiciones a mano en una línea de comando.** Genera el grafo con un script y
  usa `-filter_complex_script`.

---

## Checklist

- [ ] Cada transición tiene una razón narrativa: cambio de tiempo, lugar o idea.
- [ ] Todos los clips pasan por la misma normalización antes del `xfade`: fps, escala, recorte, SAR,
      formato.
- [ ] Todos los clips llevan `setpts=PTS-STARTPTS`.
- [ ] Saqué la duración exacta de cada clip con `ffprobe`, no a ojo.
- [ ] Calculé los offsets con la fórmula `offset_k = suma(d0..dk) - k*T`, no a ojo.
- [ ] Verifiqué que `offset + duration` cabe dentro del primer clip en cada par.
- [ ] La duración esperada del resultado es `suma - (n-1)*T` y la comprobé con ffprobe al final.
- [ ] El audio está resuelto: `acrossfade` con la misma `d`, o una pista continua aparte.
- [ ] Si uso `acrossfade`, los audios están recortados a la misma longitud que los videos.
- [ ] Las duraciones de transición corresponden al ritmo del contenido (corto en reels).
- [ ] `format=yuv420p` cierra la cadena.
- [ ] Vi el resultado **en el punto exacto de cada transición**, no solo el principio y el final.
- [ ] No hay negro inesperado al final del video.
