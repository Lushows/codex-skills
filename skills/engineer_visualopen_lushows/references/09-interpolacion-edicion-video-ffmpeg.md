# 09 — Frame interpolation y edición de video con ffmpeg (2026)

> Cierra el pipeline canónico de costo (SKILL §6.25): **render chico → interpolar → upscalar**. Generar
> menos frames y subir el fps después es mucho más barato que generarlos en el difusor (lineal en frames).

## Frame interpolation: RIFE vs FILM vs IFRNet

| Modelo | Enfoque | Fortaleza | Debilidad |
|---|---|---|---|
| **RIFE** (hzwer, ECCV2022 + v4.x) | flujo intermedio en tiempo real | **Rápido (real-time)**, el default. `rife-ncnn-vulkan` (nihui) corre en cualquier GPU sin torch. | Artefactos en movimiento muy grande/oclusión. |
| **FILM** (Google) | feature pyramid, large-motion | **Mejor en movimiento GRANDE** y huecos amplios (frames muy separados) | Más lento que RIFE. |
| **IFRNet** | flujo + refinamiento, eficiente | Buen balance calidad/velocidad, ligero | Menos adoptado/herramientas. |

- **Uso típico:** 2× duplica frames (12→24), 4× (12→48). RIFE permite factores arbitrarios y timestamps.
- **`rife-ncnn-vulkan`** (sin dependencias torch, el más fácil de desplegar):
  ```bash
  # extraer frames -> interpolar 2x -> re-encode
  ffmpeg -i in.mp4 -vsync 0 frames/%08d.png
  rife-ncnn-vulkan -i frames/ -o interp/ -m rife-v4.6        # 2x por default
  ffmpeg -framerate 48 -i interp/%08d.png -c:v libx264 -pix_fmt yuv420p -movflags +faststart out.mp4
  ```
- **RIFE internamente trabaja en RGB float** (convierte desde/hacia yuv420p) — no es algo que controles,
  pero explica el costo de memoria por frame.
- En **ComfyUI**: nodos "RIFE VFI" / "FILM VFI" (paquete `ComfyUI-Frame-Interpolation`) integran esto en
  el grafo justo después del nodo de generación de video.

## El pipeline render-chico → interpolar → upscalar (orden correcto)

```
DiT genera 480p @ 12fps (barato)
  → Real-ESRGAN/SUPIR → 1080p @ 12fps          (upscale espacial, ref 08)
  → RIFE 2-4×          → 1080p @ 24-48fps       (interpolación temporal)
```
- **Upscala ANTES de interpolar** si quieres calidad máxima por frame (menos frames que upscalar = más
  barato y el interpolador trabaja sobre frames nítidos). Si la VRAM/tiempo del upscaler es el cuello,
  interpola primero. Ambos órdenes se usan; **upscale→interpolar** es el más común para calidad.
- Genera el **mínimo de frames** que el difusor aguante (lineal en costo) y deja que RIFE haga el resto.

## Edición ffmpeg avanzada

### Concat (unir clips)
```bash
# Mismo codec/params -> demuxer SIN recodificar (instantáneo, lossless):
printf "file 'a.mp4'\nfile 'b.mp4'\n" > list.txt
ffmpeg -f concat -safe 0 -i list.txt -c copy out.mp4
# Distinto codec/resolución -> concat filter (recodifica):
ffmpeg -i a.mp4 -i b.mp4 -filter_complex "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]" -map "[v]" -map "[a]" out.mp4
```

### Trim/cut sin recodificar (`-c copy`, instantáneo)
```bash
ffmpeg -ss 00:00:10 -to 00:00:25 -i in.mp4 -c copy out.mp4   # corta entre 10s y 25s
```
- **`-c copy` corta en keyframes** → el inicio puede saltar al keyframe más cercano (no exacto al frame).
  Para corte exacto al frame, recodifica (quita `-c copy`).

### crop / scale / pad
```bash
-vf "crop=720:1280:0:0"                                  # recortar (w:h:x:y)
-vf "scale=1080:-2"                                      # escalar a ancho 1080, alto auto par (-2)
-vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2"  # encajar + barras
```

### overlay / watermark
```bash
ffmpeg -i in.mp4 -i logo.png -filter_complex "overlay=W-w-20:H-h-20" out.mp4   # esquina inf-der, margen 20
```

### fade in/out
```bash
-vf "fade=t=in:st=0:d=1,fade=t=out:st=9:d=1" -af "afade=t=in:d=1,afade=t=out:st=9:d=1"
```

### speed change
```bash
-vf "setpts=0.5*PTS" -af "atempo=2.0"     # 2× más rápido (atempo válido 0.5-2.0; encadena para más)
```

### subtítulos quemados (burn-in)
```bash
# desde .srt:
ffmpeg -i in.mp4 -vf "subtitles=subs.srt:force_style='Fontsize=24,PrimaryColour=&H00FFFFFF&'" -c:a copy out.mp4
# desde .ass (estilos completos):
ffmpeg -i in.mp4 -vf "ass=subs.ass" out.mp4
```
- Quemar = recodifica el video (el texto pasa a ser píxeles). Para subs *seleccionables* usa
  `-c:s mov_text` (soft subs, no se queman).

### extraer / insertar audio
```bash
ffmpeg -i in.mp4 -vn -c:a copy audio.m4a                       # extraer audio
ffmpeg -i video.mp4 -i audio.m4a -map 0:v -map 1:a -c:v copy -c:a aac -shortest out.mp4   # muxear
```

### GIF ↔ mp4
```bash
ffmpeg -i in.gif -movflags +faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" out.mp4
# mp4 -> GIF de calidad (palette de 2 pasos):
ffmpeg -i in.mp4 -vf "fps=15,scale=480:-1:flags=lanczos,palettegen" palette.png
ffmpeg -i in.mp4 -i palette.png -vf "fps=15,scale=480:-1:flags=lanczos[x];[x][1:v]paletteuse" out.gif
```

## Codecs (H.264 / VP9 / AV1) + web

```bash
# H.264 para web (máxima compatibilidad) — los 2 flags más olvidados:
ffmpeg -i in.mp4 -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 20 -preset medium \
       -c:a aac -b:a 128k -movflags +faststart out.mp4
```
- **`-movflags +faststart`** → mueve el `moov` atom al frente → el navegador reproduce **mientras
  descarga** (sin esto espera el archivo completo). **Imprescindible para web.** (SKILL §6.32)
- **`-pix_fmt yuv420p`** → sin esto **Safari/QuickTime muestran NEGRO** (no soportan yuv444/422).
- **`-crf`** = calidad constante (18 ≈ visualmente lossless, 20-23 web normal; menor = mejor/más pesado).
- **`-preset`** = velocidad↔tamaño (slower = más chico, mismo CRF).
- **Codec por caso:** **H.264 (libx264)** = compat universal, **manda esto por default**. **VP9
  (libvpx-vp9)** ~30% más chico, soporte amplio en navegadores. **AV1 (libaom-av1 / svt-av1)** ~30-50%
  más chico que H.264 pero **encode lento** y decode no universal en hardware viejo → opcional para
  clientes modernos. (SKILL §6.32: manda H.264, AV1 opcional.)

## Gotchas

1. **`-movflags +faststart` y `-pix_fmt yuv420p` son los 2 que TODOS olvidan.** Sin faststart el video web
   "no carga hasta el final"; sin yuv420p sale **negro en Safari/iOS**. Los modelos de video suelen sacar
   yuv444 → conviértelo SIEMPRE al exportar para web/WhatsApp.
2. **`-c copy` corta en keyframes, no al frame exacto.** El inicio del recorte puede saltar segundos. Para
   corte exacto, recodifica (sin `-c copy`).
3. **`atempo` solo acepta 0.5-2.0.** Para 4× encadena `atempo=2.0,atempo=2.0`. Y `setpts` (video) y
   `atempo` (audio) deben ajustarse JUNTOS o el audio se desincroniza.
4. **Concat demuxer exige codecs/params idénticos.** Mezclar resoluciones/codecs con `-c copy` da salida
   corrupta → usa el `concat` *filter* (recodifica) para fuentes heterogéneas.
5. **Quemar subs recodifica el video** y el `.srt`/`.ass` debe ser accesible por ruta (cuidado con rutas
   con espacios/comillas en Windows; escapa o usa rutas POSIX). Soft subs (`-c:s mov_text`) no recodifican.
6. **Interpola sobre frames ya restaurados/upscalados**, no al revés — interpolar frames con artefactos
   los propaga e inventa movimiento sobre basura (ver ref 08).
7. **RIFE/FILM alucinan en movimiento muy grande u oclusiones** (manos, objetos que entran/salen) → para
   saltos grandes entre frames usa **FILM**; RIFE brilla en movimiento suave/incremental.

## Fuentes
- https://github.com/hzwer/ECCV2022-RIFE · https://github.com/nihui/rife-ncnn-vulkan
- https://github.com/google-research/frame-interpolation (FILM)
- https://ffmpeg.org/ffmpeg-formats.html · https://trac.ffmpeg.org/wiki/Concatenate
- https://forum.videohelp.com/threads/413908 (RIFE práctico)
