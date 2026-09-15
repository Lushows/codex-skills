# 108 — Análisis y medición: ffprobe, astats, silencio, negro y congelado

Como editor no puedes reproducir el video en tu cabeza. Pero **sí puedes medirlo**. Este módulo es el
instrumental: cómo sacarle datos duros a un archivo para decidir y para verificar que el corte quedó
bien. Todo lo de aquí es de solo lectura: ningún comando modifica archivos.

---

## PARTE 1 — ffprobe

```bash
ffprobe -v error -show_format -show_streams entrada.mp4
```
Escupe todo. Útil una vez, insoportable en un script. Lo normal es pedir campos con `-show_entries`.

### Las consultas que usas de verdad

```bash
# Duración en segundos, sin adornos
ffprobe -v error -show_entries format=duration -of csv=p=0 entrada.mp4

# Ficha completa de video
ffprobe -v error -select_streams v:0 \
  -show_entries stream=codec_name,profile,width,height,r_frame_rate,avg_frame_rate,pix_fmt,sample_aspect_ratio,bit_rate,nb_frames \
  -of default=noprint_wrappers=1 entrada.mp4

# Ficha de audio
ffprobe -v error -select_streams a:0 \
  -show_entries stream=codec_name,sample_rate,channels,channel_layout,bit_rate \
  -of default=noprint_wrappers=1 entrada.mp4

# Todo en JSON, para procesar con código
ffprobe -v error -show_format -show_streams -of json entrada.mp4

# Tamaño, bitrate global, número de flujos
ffprobe -v error -show_entries format=size,bit_rate,nb_streams,format_name -of default=nw=1 entrada.mp4

# Rotación declarada por el celular
ffprobe -v error -select_streams v:0 -show_entries stream_side_data=rotation -of default=nw=1 entrada.mp4
```

### Formatos de salida (-of)

| Valor | Resultado |
|---|---|
| `default` | `width=1080` |
| `default=nw=1` | igual, sin las líneas `[STREAM]` |
| `default=nw=1:nk=1` | `1080` (solo el valor) |
| `csv=p=0` | `1080,1920,30/1` |
| `json` | estructura completa |
| `flat` | `streams.stream.0.width=1080` |

`nw` = `noprint_wrappers`, `nk` = `nokey`.

### Contar fotogramas y listar keyframes

`nb_frames` a veces viene vacío o mentiroso:
```bash
ffprobe -v error -select_streams v:0 -count_frames -show_entries stream=nb_read_frames -of csv=p=0 entrada.mp4
```
Lento pero exacto. Útil cuando sospechas que el archivo está truncado.

**Los keyframes**, imprescindibles antes de cortar con `-c copy`:
```bash
ffprobe -v error -select_streams v:0 -skip_frame nokey -show_entries frame=pts_time -of csv=p=0 entrada.mp4
```
Esos son los únicos puntos donde puedes cortar copiando.

Tipo de cada fotograma (I, P, B) de los primeros 200:
```bash
ffprobe -v error -select_streams v:0 -show_entries frame=pts_time,pict_type \
  -of csv=p=0 -read_intervals "%+#200" entrada.mp4
```
Otras formas de `-read_intervals`: `"30%+#100"` (desde el s 30, 100 paquetes), `"60%+10"` (desde el
60, 10 segundos), `"10%20"` (del 10 al 20).

### Detectar fps variable

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate,avg_frame_rate -of csv=p=0 entrada.mp4
```
Si **no coinciden**, la fuente tiene fps variable: grabación de pantalla, OBS, WhatsApp. Fija
`fps=30` en el filtro o el audio se desincroniza (ver `109`).

### Comparar un lote de un vistazo

```powershell
Get-ChildItem "*.mp4" | ForEach-Object {
  $v = ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt,sample_aspect_ratio -of csv=p=0 $_.FullName
  $a = ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,sample_rate,channels -of csv=p=0 $_.FullName
  $d = ffprobe -v error -show_entries format=duration -of csv=p=0 $_.FullName
  "{0,-24} {1,8:N2}s  V[{2}]  A[{3}]" -f $_.Name, [double]$d, $v, $a
}
```
Si alguna línea no coincide con las demás, **ese archivo no se puede unir con `-c copy`** (ver `101`).

---

## PARTE 2 — Medición de audio

### volumedetect — picos y media, rápido

```bash
ffmpeg -hide_banner -i entrada.mp4 -af volumedetect -f null -
```
```
mean_volume: -27.4 dB
max_volume: -9.8 dB
histogram_0db: 0
```
- **`max_volume`** — el pico más alto. `-9.8` significa 9.8 dB de margen antes de saturar.
- **`mean_volume`** — promedio RMS. Voz hablada normal: entre -20 y -26 dB.
- **`histogram_0db`** — muestras que tocaron el techo. **Mayor que 0 = hay clipping.**

Es lo primero que corres sobre cualquier audio que te llega.

### astats — la radiografía completa

```bash
ffmpeg -hide_banner -i entrada.mp4 -af astats -f null -
```
Los campos que importan:

- **`Noise floor dB`** — nivel del ruido de fondo. Por encima de -50 dB hay ruido audible: limpia.
- **`Dynamic range`** — por debajo de 8 dB ya está aplastado; no comprimas más.
- **`Peak count`** — debe ser 0 o muy bajo.
- **`Flat factor`** — alto significa señal recortada (clipping duro).
- **`DC offset`** — debe ser casi 0; si no, un `highpass=f=20` lo arregla.

Por tramos, para ver dónde se cae el nivel:
```bash
ffmpeg -hide_banner -i entrada.mp4 -af "astats=metadata=1:reset=48000,ametadata=print:key=lavfi.astats.Overall.RMS_level" -f null -
```

### ebur128 — loudness, el número que importa

```bash
ffmpeg -hide_banner -i entrada.mp4 -af "ebur128=peak=true" -f null -
```
```
Integrated loudness:  I: -18.4 LUFS
Loudness range:     LRA:   7.2 LU
True peak:         Peak:  -2.1 dBFS
```
**`I` es el número.** Compáralo con -14 LUFS (redes) o -23 LUFS (broadcast). Si da -18.4, tu video
suena 4.4 dB más bajo que el resto del feed. `True peak` debe estar en -1.0 dBTP o menos.

Versión visual, para ver dónde se cae:
```bash
ffmpeg -y -i entrada.mp4 -filter_complex "[0:a]ebur128=video=1:meter=18[v][a]" \
  -map "[v]" -map "[a]" -c:v libx264 -crf 26 -preset veryfast medicion.mp4
```

### loudnorm en modo medición

```bash
ffmpeg -hide_banner -i entrada.mp4 -af "loudnorm=I=-14:TP=-1.0:LRA=11:print_format=json" -f null -
```
Devuelve `input_i`, `input_tp`, `input_lra`, `input_thresh` y `target_offset`: los números de la
segunda pasada (ver `103`).

### silencedetect — encontrar los silencios

```bash
ffmpeg -hide_banner -i entrada.mp4 -af "silencedetect=noise=-35dB:duration=0.5" -f null -
```
```
silence_start: 4.312
silence_end: 5.847 | silence_duration: 1.535
```
**Esto es oro para el montaje.** Cada silencio de más de medio segundo en una toma hablada es un
candidato a corte: dónde se trabó, dónde arranca la frase útil, cómo segmentar una toma larga.

`noise=-35dB` funciona con grabación limpia; con ruido de fondo sube a `-28dB`. `duration` por debajo
de 0.3 captura respiraciones.

Guardar los resultados:
```powershell
ffmpeg -hide_banner -i "entrada.mp4" -af "silencedetect=noise=-32dB:duration=0.4" -f null - 2>&1 |
  Select-String "silence_" | Set-Content -Encoding ascii "silencios.txt"
```
```bash
ffmpeg -hide_banner -i entrada.mp4 -af "silencedetect=noise=-32dB:duration=0.4" -f null - 2>&1 | grep silence_ > silencios.txt
```

---

## PARTE 3 — Imágenes de diagnóstico

### showwavespic — la forma de onda como PNG

```bash
ffmpeg -hide_banner -y -i entrada.mp4 -filter_complex \
"[0:a]showwavespic=s=1920x480:colors=white|white:split_channels=1" -frames:v 1 onda.png
```
**Esta imagen sí la puedes mirar y sacar conclusiones sin oír el audio:** tramos planos = silencio;
onda que toca arriba y abajo del todo = clipping; alturas muy distintas entre tramos = niveles
descuadrados; amplitud constante como un ladrillo = sobrecomprimido.

Variantes: `scale=log` (se ven mejor las partes bajas), `colors=0x00FF88`, `draw=full`.

### showspectrumpic — el espectrograma

```bash
ffmpeg -hide_banner -y -i entrada.mp4 -filter_complex \
"[0:a]showspectrumpic=s=1920x1080:legend=1:mode=separate:color=intensity" -frames:v 1 espectro.png
```
Frecuencia (vertical) contra tiempo (horizontal). Qué buscar:

- **Banda horizontal constante abajo** = zumbido de 50/60 Hz o retumbe. Lo quita un `highpass`.
- **Corte limpio y horizontal arriba** (p. ej. en 15 kHz) = ya pasó por compresión con pérdida. No
  esperes recuperar brillo.
- **Nube difusa cubriendo todo** = ruido de fondo alto.
- **Rayas verticales aisladas** = chasquidos o golpes de micrófono.
- **Zona densa entre 200 y 500 Hz** = voz encartonada, ecualízala.

### signalstats — medir la imagen

```bash
ffmpeg -hide_banner -i entrada.mp4 -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null -
ffmpeg -hide_banner -i entrada.mp4 -vf "signalstats,metadata=print:file=stats.txt" -f null -
```
Claves: `YMIN YLOW YAVG YHIGH YMAX` (luminancia), `UAVG VAVG` (dominante de color),
`SATAVG SATMAX` (saturación), `HUEAVG`, `YDIF UDIF VDIF` (diferencia entre fotogramas).

En escala 0-255 (16 es negro, 235 blanco):

- **`YAVG` bajo 60** = subexpuesta. **Sobre 170** = quemada.
- **`YMIN` muy por encima de 16** = negros lavados, falta contraste.
- **`YMAX` pegado a 235-255 en muchos fotogramas** = altas luces recortadas.
- **`SATAVG` bajo 40** = imagen apagada, la marca no se ve.
- **`YDIF` altísimo de golpe** = corte de escena.

Versiones visuales:
```bash
ffmpeg -y -i entrada.mp4 -vf "split=2[a][b];[b]vectorscope=mode=color3:g=green[vs];[a][vs]overlay=W-w-20:20" \
  -frames:v 300 -c:v libx264 -crf 26 vectorscopio.mp4
ffmpeg -y -ss 5 -i entrada.mp4 -vf "histogram=display_mode=stack:levels_mode=logarithmic" -frames:v 1 histograma.png
```

### blackdetect — detectar negros

```bash
ffmpeg -hide_banner -i entrada.mp4 -vf "blackdetect=d=0.3:pix_th=0.10" -f null -
```
```
black_start:14.2 black_end:15.033 black_duration:0.833
```
**Para qué sirve de verdad:** después de un montaje con `xfade`, lo corres sobre el resultado. Si
aparece un negro que tú no pusiste, tienes un offset mal calculado. Es la verificación más directa de
que las transiciones quedaron bien. También detecta clips que arrancan con negro de más.

Para un solo fotograma negro perdido: `-vf "blackframe=amount=98:threshold=32"`.

### freezedetect — detectar imagen congelada

```bash
ffmpeg -hide_banner -i entrada.mp4 -vf "freezedetect=n=-60dB:d=2" -f null -
```
Detecta: un render que se colgó y repitió el último fotograma, un `overlay` con `eof_action=repeat`
que dejó una capa pegada, un clip que en realidad era una foto, fallos de captura.

**Corre esto sobre todo entregable.** Un congelado de 3 segundos en un video publicado es un error
que se evita con un comando.

### cropdetect — encontrar barras negras

```bash
ffmpeg -hide_banner -i entrada.mp4 -vf "cropdetect=24:16:0" -frames:v 300 -f null -
```
Imprime `crop=1920:800:0:140`. Toma la que **más se repita**, no la primera (los primeros fotogramas
pueden ser negros).

### Cambios de escena y hoja de contactos

```bash
# Segundo de cada cambio de escena (0.3 a 0.4 es buen umbral para material real)
ffmpeg -hide_banner -i entrada.mp4 -vf "select='gt(scene,0.35)',metadata=print" -f null -

# Un fotograma por escena: la mejor forma de "ver" un video largo
ffmpeg -hide_banner -y -i entrada.mp4 -vf "select='gt(scene,0.35)',scale=480:-2" -vsync vfr escena_%03d.png

# Mosaico: un fotograma cada 5 s en cuadrícula 5x4
ffmpeg -hide_banner -y -i entrada.mp4 -vf "fps=1/5,scale=320:-2,tile=5x4" -frames:v 1 contactos.png
```

---

## PARTE 4 — Comparar dos versiones y detectar entrelazado

```bash
ffmpeg -hide_banner -i original.mp4 -i comprimido.mp4 -lavfi psnr -f null -
ffmpeg -hide_banner -i original.mp4 -i comprimido.mp4 -lavfi ssim -f null -

# Ver la diferencia
ffmpeg -y -i original.mp4 -i comprimido.mp4 -filter_complex \
"[0:v][1:v]blend=all_mode=difference,eq=contrast=6" -c:v libx264 -crf 20 diferencia.mp4
```
PSNR: por encima de 42 dB es indistinguible; 36 a 42 es bueno; bajo 32 se nota. Sirve para decidir
hasta dónde bajar el CRF.

```bash
ffmpeg -hide_banner -i entrada.mp4 -vf idet -frames:v 500 -f null -
```
Si `TFF` o `BFF` superan a `Progressive`, el material está entrelazado: `-vf "yadif=mode=1:parity=-1"`.
Solo aparece en material de cámaras viejas, TV o DVD.

---

## Rutina de verificación de un entregable

Corre esto sobre **todo** archivo antes de publicarlo:

```powershell
$f = "reel_final.mp4"
ffprobe -v error -show_entries format=duration,size,bit_rate -of default=nw=1 $f
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt -of default=nw=1 $f
ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,sample_rate,channels -of default=nw=1 $f
ffmpeg -hide_banner -i $f -af "ebur128=peak=true" -f null -
ffmpeg -hide_banner -i $f -vf "blackdetect=d=0.3:pix_th=0.10" -f null -
ffmpeg -hide_banner -i $f -vf "freezedetect=n=-60dB:d=1.5" -f null -
ffmpeg -hide_banner -i $f -af "silencedetect=noise=-40dB:duration=0.8" -f null -
ffmpeg -hide_banner -y -i $f -filter_complex "[0:a]showwavespic=s=1920x400:colors=white" -frames:v 1 verif_onda.png
ffmpeg -hide_banner -y -i $f -vf "fps=1/2,scale=270:-2,tile=6x5" -frames:v 1 verif_contactos.png
```

Si `blackdetect`, `freezedetect` y `silencedetect` no reportan nada inesperado, el loudness da -14
más o menos 0.5, y las dos imágenes se ven bien, el archivo está listo. Ese es el estándar.

---

## Errores comunes

- **Confiar en `nb_frames`.** A veces viene vacío o mentiroso. Usa `-count_frames` si importa.
- **Leer `r_frame_rate` como número.** Viene como fracción: `30000/1001` es 29.97.
- **Ignorar que `r_frame_rate` y `avg_frame_rate` no coinciden.** Eso es fps variable y trae problemas
  de sincronía.
- **Usar `volumedetect` para decidir el nivel de entrega.** Mide picos, no loudness percibido. Para
  entregar, `ebur128` o `loudnorm`.
- **Un `histogram_0db` mayor que 0 y seguir adelante.** Eso es saturación.
- **Umbral de `silencedetect` mal calibrado.** Con -35dB en grabación ruidosa no detecta nada; con
  -20dB en una limpia marca todo como silencio.
- **Tomar la primera línea de `cropdetect`.** Toma la que más se repite.
- **No correr `blackdetect` después de un montaje con `xfade`.** Es la forma más rápida de cazar un
  offset mal calculado.
- **No correr `freezedetect` sobre el entregable.** Un congelado al final es evitable.
- **Mirar solo el peso del archivo** como prueba de que el render salió bien.
- **Olvidar `-f null -`.** Sin eso ffmpeg no tiene salida y no procesa.
- **Buscar la medición en la salida estándar.** Casi todo sale por stderr; para capturarlo a archivo
  hay que redirigir con `2>&1`.

---

## Checklist

- [ ] Corrí ffprobe sobre cada entrada antes de tocarla.
- [ ] Sé si el material es de fps constante o variable.
- [ ] Comparé la ficha técnica de todos los clips antes de intentar unirlos.
- [ ] Medí el audio original con `volumedetect` y `ebur128` antes de procesarlo.
- [ ] Verifiqué que `histogram_0db` es 0 en la entrada y en la salida.
- [ ] Saqué la forma de onda como PNG y la miré.
- [ ] Si sospechaba ruido, saqué el espectrograma y lo miré.
- [ ] Usé `silencedetect` para encontrar los puntos de corte candidatos.
- [ ] Corrí `blackdetect` sobre el montaje final: no hay negros que yo no haya puesto.
- [ ] Corrí `freezedetect` sobre el montaje final: no hay imagen congelada.
- [ ] El loudness integrado del entregable es -14 LUFS (más o menos 0.5) y el pico verdadero está
      bajo -1.0 dBTP.
- [ ] Generé una hoja de contactos del resultado y la revisé.
- [ ] La duración del entregable es exactamente la que esperaba.
