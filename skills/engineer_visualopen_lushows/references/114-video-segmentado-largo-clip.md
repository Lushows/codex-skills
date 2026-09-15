# 114 · Video segmentado: del clip de 3s al minuto+ (num_segments)

> Los modelos de video generan una cantidad FIJA de frames por pasada. Para video largo se encadenan
> segmentos con solape. Calcular mal `num_segments` = video cortado o de 3s.

## La matemática (LongCat-Video-Avatar 1.5, ejemplo concreto)
- **93 frames por segmento @25fps** → el 1er segmento dura `93/25 = 3.72s`.
- Cada segmento extra suma `(93-13)/25 = 3.2s` (se solapan **13 frames** para continuidad sin "salto").
- Duración del video ≈ `3.72 + (N-1)·3.2`.
- Inverso (cuántos segmentos para `dur` segundos de audio):
  ```python
  n_seg = max(1, math.ceil((dur - 93/25.0) / ((93-13)/25.0)) + 1)
  ```
- Tabla rápida: 13s→4 seg · 30s→9 · 60s→19 · 110s→35.

## El demo acumula el video completo
LongCat guarda el resultado acumulado en `video_continue_{N}.mp4` (no duplica el solape y recorta al
audio). Tu handler debe agarrar **ese** (el más nuevo en OUTDIR), no el primer segmento.

## Errores clásicos y fixes
- **Audio mal medido → num_segments=1 → video de 3.7s** aunque el audio dure 60s. Causa típica: el
  audio llega en un contenedor que tu medidor (librosa) no parsea (p.ej. mp3 con extensión `.wav`).
  **Fix**: normaliza SIEMPRE antes de medir → ver pipeline de audio abajo.
- **Tope (cap) demasiado bajo** → audio largo se corta. LongCat con cap 16 → ~52s; un audio de 60s
  pierde los últimos ~8s. Sube el cap (configurable) según tu timeout. Cap 35 ≈ 1:52.
  ```python
  MAX_SEG = int(os.getenv('LIPSYNC_MAX_SEGMENTS', '35'))
  n_seg = min(n_seg, MAX_SEG)
  ```
- **Cap vs timeout**: más segmentos = más render. Sube el cap SOLO si subes el Execution Timeout
  acorde. Ver [[112-execution-timeout-cold-start-economics]].

## Normalización de audio obligatoria (mismo paso que mejora lip-sync)
```bash
ffmpeg -y -i entrada.cualquiera -ar 16000 -ac 1 salida.wav   # 16kHz mono
```
16kHz mono es lo que esperan Whisper/wav2vec2 y deja a librosa medir bien la duración. Loggea
`dur` y `num_segments` para depurar de un vistazo:
```
[longcat] audio normalizado -> WAV 16kHz mono
[longcat] audio dur=60.0s -> num_segments=19 (~61.3s de video, tope 35)
```

## Otras familias (referencia)
- Modelos T2V/I2V (Wan, Hunyuan, etc.) tienen su propio frame-count por pasada y técnicas de extensión
  (autoregresivo, ventana deslizante, condicionar el último frame). El principio es el mismo: **frames
  fijos por pasada + encadenado con solape**. Verifica el número en el repo, no asumas.

Cruza con [[01-audio-avatar-pipeline]] y [[09-interpolacion-edicion-video-ffmpeg]].
