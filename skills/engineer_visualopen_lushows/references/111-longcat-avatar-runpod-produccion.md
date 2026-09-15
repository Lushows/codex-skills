# 111 · LongCat-Video-Avatar 1.5 en RunPod: playbook de producción real

> Caso vivido (AGENTE STUDIO, jun-2026): imagen + audio → video de presentador con lip-sync y
> gestos, multi-marca. Esto es lo que SÍ funcionó y los errores que costaron horas/dólares.

## Arquitectura end-to-end
```
App (STUDIO)  --submit imagen+audio-->  RunPod /run (async, cola)  -->  worker LongCat
   |  guarda estado durable en disco                                        |  genera N segmentos
   |  poller de servidor (cada 60s) ----poll /status/{id}----------------> sube MP4 a R2
   v  descarga + guarda en biblioteca con su COSTO  <----output_video_url---'
```
- **submit asíncrono** (`/run`, no `/runsync`): el render dura 20-40 min, jamás cabe en una request HTTP.
- **estado durable**: escribe `{jobId, engine, provider, costo}` a disco ANTES de responder. Sobrevive
  reinicios del servidor y cierre del navegador.
- **R2/S3 para el resultado**: el worker sube el MP4 y devuelve `output_video_url`; la app lo descarga.
  Nunca devuelvas el binario por la respuesta del job (límite de tamaño + timeouts).

## El input que el worker espera (verificado vs el repo real)
```json
{ "input": { "input_image_url": "https://.../cara.png",
             "input_audio_url": "https://.../voz.wav",
             "prompt": "News anchor... static camera, no zoom" } }
```
El handler arma `{prompt, cond_image, cond_audio:{person1: aud}}` y corre el demo con
`--use_distill --model_type avatar-v1.5 --use_int8 --num_segments=N`.

## Los 5 errores que costaron caro (y el fix)
1. **Worker caliente reusaba inputs del job anterior** (`if os.path.exists(f): return f`). Síntoma:
   "lanzó una imagen retenida, no la actual". Fix: SIEMPRE descargar fresco; limpiar IN/OUT por job
   (`shutil.rmtree`). Ver [[112-execution-timeout-cold-start-economics]].
2. **Audio mp3 renombrado .wav** → librosa fallaba → `num_segments=1` → video de 3s con audio de 13s.
   Fix: normalizar con ffmpeg a **WAV 16kHz mono** antes de medir. Ver [[114-video-segmentado-largo-clip]].
3. **Execution Timeout bajo (1200s)** → el job murió a los **20m 8s** en el segmento 7/16, `Failed`,
   y SÍ se cobró. Fix: timeout ≥ cold-start(~10min) + N·~1.5min. Ver [[112-execution-timeout-cold-start-economics]].
4. **Render largo > paciencia del navegador (15 min)** → el video quedaba huérfano en R2, no en la
   biblioteca. Fix: **poller de servidor**. Ver [[115-async-render-largo-poller-durable]].
5. **Zoom no deseado** por el prompt ("talks to camera, lively"). Fix: prompt estático.
   Ver [[117-control-camara-movimiento-avatar-prompt]].

## Costo real medido
- 1 video de ~1 min (19 segmentos), **cold** (re-baja 44GB): ~**$2** y ~40 min.
- Con [[113-network-volume-modelos-grandes]]: ~**$1.25** y ~25 min.
- Inferencia ya en lo más barato: `--use_distill` (8 pasos), `--use_int8`, 480p. Ahí no hay grasa.
- `RUNPOD_RATE_PER_SEC` real A100/H100 80GB ≈ **0.0008–0.0012** (no el 0.00019 de placeholder).

## Checklist mínimo antes de lanzar
Ver [[118-checklist-pre-lanzamiento-render-gpu]]. Resumen: timeout alto · imagen/tag correctos ·
num_segments esperado · estimar costo · saber si es cold o warm.

## Gotchas RunPod operativos
- **"New release" se deshabilita** si el tag = el actual: RunPod exige tag NUEVO. Para forzar re-pull
  con el mismo tag → borrar los workers (recrean y bajan la imagen) o usar `:latest`.
- **Header "0 running workers" miente** (lag de UI). Los **Logs** y la pestaña **Requests** mandan.
- **Requests** muestra el veredicto real: `Failed`/`COMPLETED` + `Execution time` exacto.
- IMAGE_NOT_FOUND suele ser **timing**: pinaste el SHA antes de que el build de GHCR publicara el tag.
