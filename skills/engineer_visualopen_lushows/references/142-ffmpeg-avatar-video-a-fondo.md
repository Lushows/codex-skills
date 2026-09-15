# 142 · ffmpeg para avatar/video a fondo (comandos listos)

> El modelo da los píxeles; ffmpeg arma el entregable: concatenar segmentos, pegar el audio, recortar,
> normalizar la entrada, hacer el MP4 reproducible en web. Sin esto el render "termina" pero el
> archivo no sirve. Comandos copy-paste, gotchas medidos.

## 1. Concatenar segmentos: demuxer vs filter
**Demuxer (sin re-encode, instantáneo)** — solo si TODOS los segmentos tienen idénticos codec, resolución,
fps, pix_fmt, timebase. El avatar segmentado del mismo worker normalmente cumple → úsalo:
```bash
# lista.txt:  file 'seg_000.mp4'  (una por línea, rutas relativas al .txt o absolutas con -safe 0)
ffmpeg -f concat -safe 0 -i lista.txt -c copy -movflags +faststart salida.mp4
```
**Filter (re-encodea, lento pero tolerante)** — si difieren en algo (fps/resolución mezclados):
```bash
ffmpeg -i a.mp4 -i b.mp4 -i c.mp4 \
  -filter_complex "[0:v][1:v][2:v]concat=n=3:v=1:a=0[v]" -map "[v]" \
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -movflags +faststart salida.mp4
```
Gotchas:
- `-safe 0` es obligatorio si las rutas en `lista.txt` son absolutas o tienen `/` — si no, ffmpeg lo
  rechaza por seguridad.
- Demuxer con `-c copy` **no acepta** `-crf`/`-preset` (no re-encodea): esos flags se ignoran.
- Si el demuxer pega pero el audio sale desincronizado entre cortes, los timebases difieren →
  re-encodea con el filter, o regenera segmentos con el mismo `-r`.

## 2. Mux de audio (pegar la voz al video del avatar)
Video sin audio + WAV/MP3 de TTS → un MP4. Copia el video (rápido), encodea solo el audio:
```bash
ffmpeg -i video_mudo.mp4 -i voz.wav -c:v copy -c:a aac -b:a 192k -shortest \
  -movflags +faststart salida.mp4
```
- `-shortest` corta al stream más corto → evita cola de video congelado o audio sin imagen.
- `-c:v copy` solo vale si el video ya está en H.264/HEVC compatible; si viene en otro codec, cambia a
  `-c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p`.
- `-map 0:v:0 -map 1:a:0` si hay varios streams y quieres ser explícito sobre cuáles van.

## 3. Recortar el video a la duración del audio
El avatar a veces genera frames de más al final. Recorta exacto a la voz (`-t` limita duración; `-ss`
antes del `-i` salta el inicio, keyframe-accurate):
```bash
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 voz.wav)
ffmpeg -i video.mp4 -i voz.wav -map 0:v -map 1:a -t "$DUR" -c:v copy -c:a aac -movflags +faststart salida.mp4
```

## 4. Normalizar audio a 16kHz mono (entrada de avatar/lip-sync)
La mayoría de modelos de lip-sync (Wav2Lip, SadTalker, LongCat-Avatar) esperan **16kHz mono PCM**.
Audio mal sampleado = labios desincronizados o crash:
```bash
ffmpeg -i entrada.mp3 -ac 1 -ar 16000 -c:a pcm_s16le voz_16k.wav
```
`-ac 1` mono, `-ar 16000` resample, `pcm_s16le` WAV sin comprimir. Para loudness consistente añade
`-af loudnorm=I=-16:TP=-1.5:LRA=11` (EBU R128) antes del resample.

## 5. MP4 para web — flags que importan
| Flag | Para qué | Nota |
|---|---|---|
| `-movflags +faststart` | mueve el `moov` atom al inicio → reproduce sin bajar todo | hace 2ª pasada al final |
| `-pix_fmt yuv420p` | compatibilidad con Safari/QuickTime/WhatsApp | sin esto, video "negro" en algunos players |
| `-crf 18-23` | calidad/peso (libx264; menor=mejor, 18≈visualmente sin pérdida) | NVENC usa `-cq` no `-crf` |
| `-preset` | velocidad↔compresión (`ultrafast`..`veryslow`) | `medium`/`slow` para entrega final |
| `-profile:v high -level 4.1` | compat con dispositivos viejos | opcional |

## 6. Aceleración por hardware (NVENC)
Encodear en GPU es mucho más rápido para piezas largas. NVENC NO usa `-crf`, usa `-cq`:
```bash
ffmpeg -hwaccel cuda -i in.mp4 -c:v h264_nvenc -preset p5 -tune hq -rc vbr -cq 23 \
  -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart out.mp4
```
- Presets NVENC son `p1`(rápido)..`p7`(lento/calidad), distintos de los de libx264.
- Calidad por bit suele ser **algo peor** que libx264 a `crf` equivalente; para máxima calidad y poco
  volumen, libx264 en CPU gana. Para throughput en GPU ya alquilada, NVENC. Costo en [[30-finops-gpu]].
- Verifica que el build tenga NVENC: `ffmpeg -encoders | grep nvenc` (necesita drivers NVIDIA + build con `--enable-nvenc`).

## 7. Frames: extraer e insertar
```bash
ffmpeg -i in.mp4 -vf fps=25 frame_%05d.png            # extraer a PNG (p.ej. para upscaling [[08]])
ffmpeg -framerate 25 -i frame_%05d.png -c:v libx264 -crf 18 -pix_fmt yuv420p out.mp4  # re-armar
```
Gotcha: `fps` de extracción y `-framerate` de re-armado deben coincidir o cambia la duración.

## 8. Crop/overlay para quitar zoom o componer
Si el avatar viene con un zoom/encuadre indeseado (ver control de cámara en
[[117-control-camara-movimiento-avatar-prompt]]), recorta y reescala:
```bash
# crop=ancho:alto:x:y  → recortar el centro y devolver a 1080x1920
ffmpeg -i in.mp4 -vf "crop=900:1600:90:160,scale=1080:1920" -c:v libx264 -crf 18 -pix_fmt yuv420p out.mp4
# overlay: poner el avatar (con alpha) sobre un fondo
ffmpeg -i fondo.mp4 -i avatar.mov -filter_complex "[0][1]overlay=(W-w)/2:(H-h)/2:shortest=1" -pix_fmt yuv420p out.mp4
```
`crop` debe ir **antes** de `scale` en la cadena de filtros. Dimensiones del crop ≤ las del fuente.

## Dónde encaja en el pipeline
Paso final tras el render segmentado: difusión → segmentos → **concat → mux audio → recorte →
faststart**. Reserva ese 5% final de la barra de progreso (ver [[140]]) para esta fase.

Cruza con [[09-interpolacion-edicion-video-ffmpeg]], [[114-video-segmentado-largo-clip]] y
[[117-control-camara-movimiento-avatar-prompt]].
