# 55 — Pipeline de producción de video IA end-to-end (2026)

Orquestar idea → video terminado es un *pipeline*, y el oficio está en los handoffs entre etapas — ahí muere la consistencia.

## Las etapas
1. **Brief** — audiencia, plataforma, aspect ratio, duración, mensaje, brand kit. Decide el formato ANTES de generar.
2. **Script / VO** — escribe tight (~150 wpm → 30s ≈ 75 palabras). Genera VO temprano (ElevenLabs) para que la imagen corte a la voz.
3. **Storyboard** — shot list con composición (ref 50), para que la generación tenga target.
4. **Generar stills** — t2i (MJ, FLUX) para fijar personajes/look como **anchor frames**. Generar imágenes primero y *luego* animarlas da MUCHO más control que t2v crudo.
5. **Image-to-video** — anima los anchors (Runway Gen-4, Kling, Veo, Hailuo/MiniMax, Sora). First/last-frame para continuidad.
6. **Seleccionar takes** — genera 3-5 variaciones por plano, descarta sin piedad. La mayoría de clips son inservibles; presupuéstalo.
7. **Edit** — ensambla a la VO/música; J/L cuts (ref 51).
8. **Motion graphics** — títulos, captions, marca (ref 53).
9. **Color** — matchea los clips dispares, grano/halación (ref 52).
10. **Sound** — música, SFX, mezcla a LUFS (ref 54).
11. **Export** — por plataforma.

## Stack de tools 2026 (representativo)
Imagen: MJ v7 / FLUX. I2V: Runway Gen-4, Kling 2.x, Veo 3, MiniMax/Hailuo, Sora. VO: ElevenLabs. Música: Suno/Udio/
Epidemic. Edit/color: DaVinci Resolve (free) o Premiere. Motion: After Effects / Remotion. Captions: Opus Clip / CapCut / Whisper. Glue/batch: ffmpeg.

## Presupuesto de re-rolls
~3-6 generaciones por clip usable. Un reel de 30s (~10 planos) = 30-60 generaciones — mete costo de créditos y
tiempo en el estimado. **No persigas el clip perfecto;** consigue uno que *corte bien* y arregla el resto en post.

## Asset management
Naming: `proj_scene02_shotA_v03_i2v.mp4`. Carpetas: `/01_script /02_stills /03_clips /04_audio /05_project /06_exports`. Mantén un bin de selects. Evita el agujero negro "¿cuál versión era la buena?" a 200+ archivos.

## Aspect ratios + safe areas
9:16 (1080×1920) TikTok/Reels/Shorts — texto fuera del ~15% inferior y ~10% derecho (UI). 1:1 (1080×1080) feed. 16:9
(1920×1080) YouTube. Genera/encuadra con composición **center-safe** para reframear un master a varios ratios.

## Export (el master web confiable)
```bash
ffmpeg -i edit.mov -c:v libx264 -preset slow -crf 18 -profile:v high \
  -pix_fmt yuv420p -movflags +faststart -c:a aac -b:a 320k out.mp4
```
`yuv420p` = obligatorio (sin él, QuickTime/Safari/móviles muestran verde/negro). `+faststart` = streamea antes de
descargar. CRF 18-20 alta calidad; o bitrate target (1080p ≈ 8-12 Mbps, 4K ≈ 35-45). **Exporta un master de alto bitrate, luego deja que las plataformas re-compriman.**

## Realidad de costo/tiempo
Un reel pulido de 30s es realistamente *días*, no minutos — ruleta de generación + edit + color + sound. La promesa "escribe un prompt, obtén un anuncio terminado" es marketing.

## Ejemplo (reel de marca / news-anchor 30s)
Brief (9:16, 30s) → script + VO ElevenLabs → storyboard 8 planos → anchor frames MJ (fija cara/wardrobe) → Kling/
Runway I2V condicionado por cada anchor, 4 takes c/u → cull a 8 selects → ensamble en Resolve cortado a la VO con
J-cuts → lower-third + captions quemados → matchea los 8 clips a un grade de referencia + grano → música duckeada bajo VO, whoosh en cada corte, mezcla a -14 LUFS → export H.264 high/yuv420p/faststart → master + variantes 9:16/1:1/16:9.

## Gotchas
1. **Consistencia entre etapas** — el personaje deriva entre planos; fija la identidad en la etapa de *imagen* y aliméntala adelante, no re-rolles caras en la etapa de video.
2. **Mismatches de formato** — fps/resolución mezclados entre clips IA rompen `concat`/`xfade`; normaliza TODO a un spec (ej. 1080×1920, 30fps, yuv420p) antes de editar.
3. **La trampa del 80%** — los clips se ven 80% listos rápido; el último 20% (consistencia, grade, mezcla) es el 80% del trabajo; no shippees al 80%.
4. Sin `yuv420p`/`+faststart` = frames verdes o streaming roto al subir.
5. Sin naming de assets = selects imposibles de hallar a escala.
6. Generar en el aspect ratio equivocado fuerza crops/upscales feos — fija el ratio en la generación.
7. Saltarse el VO-first te hace re-editar imagen para encajar la voz después.

**Fuentes:** runwayml.com/research · blackmagicdesign.com/products/davinciresolve · trac.ffmpeg.org/wiki/Encode/H.264.
