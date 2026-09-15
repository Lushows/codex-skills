# 103 — Filtros de audio: volumen, mezcla, limpieza y normalización

El público perdona una imagen mediocre. No perdona un audio malo. Un video con imagen de celular y
audio limpio se ve profesional; uno con cámara de cine y audio saturado se ve amateur en el primer
segundo.

Se aplican con `-af` (atajo de `-filter:a`) cuando hay una sola entrada de audio, o dentro de
`-filter_complex` cuando hay varias.

```bash
ffmpeg -i entrada.mp4 -af "highpass=f=80,loudnorm=I=-14:TP=-1" -c:v copy -c:a aac -b:a 192k salida.mp4
```
Fíjate en `-c:v copy`: **si solo tocas el audio, no recodifiques el video.**

---

## Unidades: dB, LUFS y por qué importan

- **dBFS** mide el pico instantáneo. `0 dBFS` es el máximo absoluto; pasarse produce distorsión
  (clipping). Un pico sano queda entre `-1` y `-3 dBFS`.
- **LUFS** mide el volumen **percibido** en el tiempo. Es lo que usan las plataformas para decidir si
  te suben o te bajan.
- **LRA** mide cuánto varía el volumen dentro del video.

| Plataforma | Objetivo |
|---|---|
| Instagram / TikTok / Reels / YouTube | -14 LUFS |
| Spotify (podcast) | -14 LUFS |
| Broadcast / TV (EBU R128) | -23 LUFS |
| Pico verdadero (todas) | -1.0 dBTP |

A -20 LUFS tu video suena bajito al lado de todos en el feed y la gente pasa el dedo. A -8 LUFS la
plataforma te lo baja y de paso te aplasta la dinámica. **-14 LUFS es el número.**

---

## volume — subir y bajar

```bash
volume=1.5      # multiplica la amplitud
volume=6dB      # sube 6 decibelios
volume=-4dB     # baja 4
volume=0        # silencio total
volume=enable='between(t,10,18)':volume=-12dB    # solo en un tramo
```
`+6 dB` es el doble de amplitud, `-6 dB` la mitad. Subir más de `+12 dB` sobre una grabación normal
casi siempre trae el ruido de fondo con él.

Para saber cuánto subir sin saturar, mide primero (ver `108`):
```bash
ffmpeg -i entrada.mp4 -af volumedetect -f null -
```
```
mean_volume: -27.4 dB
max_volume: -9.8 dB
```
Ese `max_volume: -9.8 dB` dice que puedes subir hasta `+8.8 dB` antes de tocar el 0. Pero para
entregar, **normaliza con loudnorm**, no con volume a ojo.

---

## afade — fundidos de audio

```bash
afade=t=in:st=0:d=1
afade=t=out:st=28:d=2
afade=t=in:st=0:d=1.5:curve=exp
```
Curvas: `tri` (lineal, el defecto), `qsin`, `hsin`, `esin`, `log`, `ipar`, `qua`, `cub`, `squ`, `cbr`,
`par`, `exp`, `iqsin`, `ihsin`, `dese`, `desi`, `losi`, `nofade`.

- Música que entra: `qsin` o `tri`. Música que sale: `exp` o `log`.
- Voz: fundidos de 0.05 a 0.15 segundos, solo para matar los clics de corte.

**El fundido antichasquido.** Cuando cortas voz a mitad de una onda se oye un clic. 30 milisegundos lo
eliminan sin que se note (para un clip de 6 segundos):
```bash
-af "afade=t=in:st=0:d=0.03,afade=t=out:st=5.97:d=0.03"
```
**Trampa:** `st` del fundido de salida se cuenta desde el inicio del audio filtrado, y no hay
expresión "desde el final". Saca la duración con ffprobe y réstala.

---

## atrim — cortar audio dentro del grafo

```bash
atrim=start=5:end=15
atrim=start=5:duration=10       # equivalente
```
**Siempre acompáñalo de `asetpts=PTS-STARTPTS`**, si no el audio recortado conserva su marca de
tiempo original y aparece tarde:
```bash
[0:a]atrim=start=5:end=15,asetpts=PTS-STARTPTS[a1]
```

---

## aresample — frecuencia de muestreo y sincronía

```bash
aresample=48000
aresample=async=1000            # corrige deriva insertando/quitando muestras
aresample=48000:async=1000:first_pts=0
```
48 kHz es el estándar en video; 44.1 kHz el de música. Mezclarlos en un concat produce audio que se
acelera o se corre.

`async=1000` es la cura para el audio que se desincroniza poco a poco a lo largo de un video largo
(típico de OBS y capturas de pantalla). `first_pts=0` fuerza que el audio empiece en cero.

Como opción de salida: `-ar 48000`.

---

## amix — mezclar varias pistas

```bash
ffmpeg -y -i voz.wav -i musica.mp3 -filter_complex \
"[0:a]volume=1.0[v];[1:a]volume=0.18[m];[v][m]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]" \
-map "[a]" -c:a aac -b:a 192k mezcla.m4a
```
- `duration=first` — la mezcla dura lo que la primera entrada (otros: `longest`, `shortest`)
- `dropout_transition=2` — rampa cuando una pista se acaba
- `weights='1 0.2'` — pesos relativos

**La trampa de `normalize`.** Por defecto `amix` divide el volumen entre el número de entradas: con 2
entradas todo suena a la mitad, con 4 a la cuarta parte. Mezclas un video, sale bajísimo y no
entiendes por qué. **Pon `normalize=0`**, controla el volumen tú pista por pista antes del `amix`, y
cierra con `alimiter`.

**Niveles de partida:** voz a `1.0`, música de fondo entre `0.10` y `0.20`. Si la música tiene que
"sentirse", `0.25`. Más alto y la voz compite.

---

## amerge y pan — canales, no mezcla

`amix` suma las señales. `amerge` las pone en **canales distintos**.
```bash
ffmpeg -y -i micro.wav -i camara.wav -filter_complex "[0:a][1:a]amerge=inputs=2[a]" -map "[a]" -ac 2 -c:a aac salida.m4a
```
El `-ac 2` es necesario: sin él ffmpeg puede escribir un mapa de canales raro.

`pan` es la navaja suiza de los canales:
```bash
ffmpeg -i estereo.wav -af "pan=mono|c0=c0" mono_izq.wav                  # solo el izquierdo
ffmpeg -i estereo.wav -af "pan=mono|c0=0.5*c0+0.5*c1" mono.wav           # promedio a mono
ffmpeg -i mono.wav -af "pan=stereo|c0=c0|c1=c0" estereo.wav              # duplicar a estereo
```

---

## atempo — cambiar velocidad sin cambiar el tono

```bash
atempo=1.25      # 25% mas rapido
atempo=0.9       # 10% mas lento
```
Una sola instancia acepta un rango amplio, pero **la calidad se degrada notablemente por encima de
2.0 o por debajo de 0.5**. La práctica profesional es encadenar:
```bash
atempo=2.0,atempo=2.0        # 4x
atempo=2.0,atempo=1.5        # 3x
atempo=0.5,atempo=0.8        # 0.4x
```

**Emparejarlo con el video.** El factor de `setpts` es el **inverso** del de `atempo`:
```bash
ffmpeg -y -i entrada.mp4 -filter_complex "[0:v]setpts=PTS/1.25[v];[0:a]atempo=1.25[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -crf 20 -c:a aac -b:a 192k rapido.mp4
```
Video `2.0*PTS` (más lento) va con audio `atempo=0.5`. Acelerar la voz un 5 a 8% (`atempo=1.06`) es un
truco de retención real: el video se siente más ágil y casi nadie nota el cambio de tono.

---

## highpass, lowpass y equalizer

```bash
highpass=f=80           # elimina todo por debajo de 80 Hz
highpass=f=120:p=2      # pendiente mas pronunciada (2 polos)
lowpass=f=12000
```
**El pasa-altos en 80 Hz es el primer arreglo de cualquier voz.** Debajo de 80 Hz en una voz humana no
hay información útil: hay retumbe de mesa, aire acondicionado, tráfico y ruido de manejo del
micrófono. Quitarlo aclara la voz sin tocarla.

- Voz masculina: `f=80`. Femenina: `f=100`. Sala con retumbe: `f=120:p=2`.

`lowpass` se usa menos; sirve para siseo digital o para el efecto teléfono:
```bash
-af "highpass=f=300,lowpass=f=3400,acompressor=threshold=0.1:ratio=6"
```

Para bandas concretas:
```bash
equalizer=f=3000:t=q:w=1.5:g=3       # claridad e inteligibilidad
equalizer=f=250:t=q:w=1.2:g=-3       # quita el "carton" de la voz
equalizer=f=8000:t=q:w=2:g=2         # aire
```
`f` frecuencia, `t=q` el ancho se expresa como Q, `w` el valor de Q, `g` ganancia en dB.

---

## Reducción de ruido

```bash
afftdn=nr=12:nf=-28          # reductor por FFT, viene incluido
afftdn=nr=12:nf=-28:tn=1     # con deteccion automatica del ruido
arnndn=m=std.rnnn            # red neuronal (necesita descargar un modelo .rnnn)
```
Empieza con `nr=10` y sube. **Pasarse de `nr=20` produce el efecto de voz submarina**: la voz suena
metálica y peor que con el ruido.

**Orden correcto de la cadena de limpieza de voz:**
```bash
-af "highpass=f=80,afftdn=nr=12:nf=-28,equalizer=f=3000:t=q:w=1.5:g=2.5,acompressor=threshold=0.089:ratio=4:attack=20:release=250,loudnorm=I=-14:TP=-1.0:LRA=11"
```
1. Quitar la basura de abajo → 2. Reducir ruido → 3. Ecualizar → 4. Comprimir → 5. Normalizar.

Ese orden importa: **comprimir antes de reducir ruido sube el ruido de fondo** y ya no lo quitas.

---

## acompressor y ducking

```bash
acompressor=threshold=0.089:ratio=4:attack=20:release=250:makeup=2
```
- `threshold` en **amplitud lineal**, no en dB: `0.089` es aprox `-21 dB`, `0.125` es `-18 dB`,
  `0.5` es `-6 dB`.
- `ratio` — por cada 4 dB que se pase, deja pasar 1.
- `attack`/`release` en ms. Voz: ataque 5 a 20, liberación 150 a 300.
- `makeup` — ganancia de compensación.

Para voz hablada, `ratio=3` a `4` con `threshold=0.089` es un punto de partida honesto. Ratios de 10 o
más aplastan la interpretación y suenan a radio de los noventa.

**Ducking automático** (la música baja cuando la voz habla):
```bash
ffmpeg -y -i voz.wav -i musica.mp3 -filter_complex \
"[1:a][0:a]sidechaincompress=threshold=0.03:ratio=8:attack=15:release=350:makeup=1[duck]; \
 [0:a][duck]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]" \
-map "[a]" -c:a aac -b:a 192k mezcla.m4a
```
El orden de entradas es `[la_que_se_comprime][la_que_manda]`. Aquí la música baja y la voz manda.

---

## loudnorm — la normalización para entregar

```bash
loudnorm=I=-14:TP=-1.0:LRA=11
```
En una sola pasada funciona pero actúa de forma dinámica y puede "bombear". **Para el máster final,
dos pasadas.** Es el estándar profesional.

**Pasada 1 — medir:**
```bash
ffmpeg -hide_banner -i entrada.mp4 -af "loudnorm=I=-14:TP=-1.0:LRA=11:print_format=json" -f null -
```
```
{ "input_i":"-23.41", "input_tp":"-5.20", "input_lra":"8.30", "input_thresh":"-33.85", "target_offset":"0.21" }
```

**Pasada 2 — aplicar con las medidas:**
```bash
ffmpeg -hide_banner -y -i entrada.mp4 -af \
"loudnorm=I=-14:TP=-1.0:LRA=11:measured_I=-23.41:measured_TP=-5.20:measured_LRA=8.30:measured_thresh=-33.85:offset=0.21:linear=true:print_format=summary" \
-c:v copy -c:a aac -b:a 192k -ar 48000 salida.mp4
```
`linear=true` es la clave: con las medidas conocidas aplica una ganancia **lineal** en vez de andar
comprimiendo, y conserva la dinámica original.

**Trampa:** `loudnorm` remuestrea internamente a 192 kHz. **Pon `-ar 48000` explícitamente** o la
salida queda en un valor raro que algunos reproductores rechazan.

---

## dynaudnorm — nivelar cuando el volumen va y viene

Cuando hay tramos altos y tramos casi inaudibles (entrevista con dos micrófonos, alguien que se aleja
de la cámara), `loudnorm` no basta porque normaliza el conjunto.

```bash
dynaudnorm=f=250:g=15:p=0.9:m=10:s=12
```
- `f` — cuadro de análisis en ms (default 500)
- `g` — ventana gaussiana en cuadros, impar (default 31). Más alto = más suave
- `p` — pico objetivo de 0 a 1 (default 0.95). `0.9` deja margen
- `m` — ganancia máxima. `10` evita que un silencio se convierta en un rugido de ruido

**Úsalo antes de `loudnorm`, no después.** `dynaudnorm` empareja, `loudnorm` pone el nivel final.
```bash
-af "highpass=f=80,dynaudnorm=f=250:g=15:p=0.9:m=8,loudnorm=I=-14:TP=-1.0:LRA=11"
```
**Advertencia:** sube el ruido de fondo en los silencios. Si hay ruido, redúcelo antes o baja `m`.

---

## alimiter, silencio y relleno

```bash
alimiter=limit=0.95:attack=5:release=50:level=false
```
Impide que nada pase de `0.95` (aprox `-0.45 dBFS`). **Ponlo al final de toda mezcla.** Cuesta cero y
salva el máster.

```bash
-f lavfi -i anullsrc=r=48000:cl=stereo    # generar silencio como entrada
apad                                       # alargar con silencio
apad=pad_dur=2                             # exactamente 2 segundos
silenceremove=start_periods=1:start_duration=0.1:start_threshold=-50dB   # quitar silencio inicial
```
`apad` con `-shortest` es la receta para "que la música rellene hasta el final del video sin
alargarlo":
```bash
ffmpeg -y -i video.mp4 -i musica.mp3 -filter_complex \
"[1:a]volume=0.16,apad[m];[0:a][m]amix=inputs=2:duration=first:normalize=0[a]" \
-map 0:v -map "[a]" -shortest -c:v copy -c:a aac -b:a 192k salida.mp4
```

---

## Recetas listas

**Limpiar y normalizar una voz grabada con el celular:**
```bash
ffmpeg -hide_banner -y -i bruto.mp4 \
  -af "highpass=f=90,afftdn=nr=12:nf=-28,equalizer=f=3000:t=q:w=1.5:g=2.5,acompressor=threshold=0.089:ratio=3.5:attack=15:release=250,loudnorm=I=-14:TP=-1.0:LRA=11" \
  -c:v copy -c:a aac -b:a 192k -ar 48000 limpio.mp4
```

**Música de fondo con ducking sobre un video con voz:**
```bash
ffmpeg -hide_banner -y -i video.mp4 -i musica.mp3 -filter_complex \
"[1:a]volume=0.35,afade=t=in:st=0:d=1.5[mus]; \
 [mus][0:a]sidechaincompress=threshold=0.035:ratio=8:attack=15:release=400:makeup=1[duck]; \
 [0:a][duck]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]" \
-map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 con_musica.mp4
```

**Reemplazar el audio completo:**
```bash
ffmpeg -hide_banner -y -i video.mp4 -i nuevo_audio.wav \
  -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k -shortest salida.mp4
```

**Extraer el audio para transcribir** (16 kHz mono es lo que quieren los modelos; mandarles 48 kHz
estéreo es tirar dinero):
```bash
ffmpeg -hide_banner -y -i video.mp4 -vn -ac 1 -ar 16000 -c:a pcm_s16le para_whisper.wav
```

**Arreglar sincronía retrasando el audio 250 ms** (la misma entrada dos veces, una desplazada):
```bash
ffmpeg -y -i entrada.mp4 -itsoffset 0.25 -i entrada.mp4 \
  -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k sincronizado.mp4
```

---

## Errores comunes

- **Normalizar con `volume` a ojo.** No hay forma de acertar el LUFS así. Usa `loudnorm`.
- **Usar `loudnorm` en una sola pasada para el máster.** Bombea. Haz las dos pasadas.
- **Olvidar `normalize=0` en `amix`.** Toda la mezcla sale a la mitad de volumen.
- **Olvidar `-ar 48000` después de `loudnorm`.** El filtro remuestrea a 192 kHz.
- **Comprimir antes de reducir ruido.** El compresor levanta el ruido y ya no lo quitas.
- **Pasarse de `nr` en `afftdn`.** Por encima de 20 la voz suena a submarino.
- **`dynaudnorm` sobre grabación con ruido.** Convierte los silencios en ruido a todo volumen.
- **Cambiar la velocidad del video y olvidar el audio.** `setpts` sin `atempo` desincroniza todo.
- **`atempo` con un factor extremo en una sola instancia.** Encadena en vez de forzar.
- **`atrim` sin `asetpts=PTS-STARTPTS`.** El audio recortado llega tarde.
- **Mezclar 44.1 kHz con 48 kHz.** Unifica con `aresample=48000`.
- **Poner música al 0.5.** La voz desaparece. Empieza en 0.15.
- **No poner `alimiter` al final.** Un pico de la música satura todo el máster.
- **Olvidar `-c:v copy` cuando solo tocas audio.** Diez minutos y una generación de pérdida por nada.

---

## Checklist

- [ ] Medí el audio original con `volumedetect` o `ebur128` antes de tocar nada.
- [ ] La cadena de voz va en orden: pasa-altos, ruido, ecualización, compresión, normalización.
- [ ] `highpass=f=80` (o 100) está presente en toda voz.
- [ ] La reducción de ruido no supera `nr=15` y escuché buscando el efecto submarino.
- [ ] La mezcla lleva `normalize=0` en `amix` y `alimiter` al final.
- [ ] La música de fondo está entre 0.10 y 0.20, o con ducking por `sidechaincompress`.
- [ ] Normalicé con `loudnorm` a -14 LUFS / -1.0 dBTP, **en dos pasadas**, con `linear=true`.
- [ ] Puse `-ar 48000` explícito en la salida.
- [ ] Si cambié la velocidad del video, apliqué el `atempo` inverso al audio.
- [ ] Todos los `atrim` van con `asetpts=PTS-STARTPTS`.
- [ ] Todas las fuentes están a la misma frecuencia de muestreo antes de mezclar.
- [ ] Usé `-c:v copy` porque solo estaba tocando audio.
- [ ] Verifiqué midiendo otra vez: el LUFS integrado da -14 (más o menos 0.5).
- [ ] Escuché el archivo final completo, con audífonos, buscando clics, saturación y bombeo.
