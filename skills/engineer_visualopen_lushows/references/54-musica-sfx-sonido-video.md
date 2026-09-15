# 54 — Música, SFX y sonido para video

El sonido es el 50% de la experiencia y la forma más barata de hacer que el video IA se sienta caro. Sonido malo/ausente mata un clip excelente.

## Fuentes de música
**Generación IA** — **Suno** y **Udio** generan tracks completos desde prompt (revisa el tier de licencia para
derechos comerciales; los free tiers normalmente NO están clearados para comercial). **Royalty-free** — **Epidemic
Sound**, **Artlist**, **Uppbeat** (free tier con atribución), **Musicbed**, YouTube Audio Library (free).
**Realidad:** "royalty-free" ≠ "gratis" — pagas una licencia; lee el scope (social vs broadcast vs ads pagados).
**Nunca jales tracks comerciales de Spotify/YouTube** = strike de Content ID instantáneo.

## SFX
Bloques: **whooshes** (venden transiciones/movimientos de cámara), **impacts/booms** (aterrizan un corte/logo),
**risers** (tensión hacia un drop), **foley** (pasos, tela, props — realismo que al video IA le falta), **ambience/
room tone** (cama constante que pega los clips en un solo espacio). **Freesound.org** (revisa la licencia CC de
cada archivo), Epidemic/Artlist SFX, Soundsnap. **Diseñar un sonido de transición** = capa un whoosh (movimiento) + soft impact (llegada) + sub-boom (peso), timed para que el impact pegue exacto en el frame del corte.

## La mezcla — jerarquía
De adelante hacia atrás: **diálogo/VO** más fuerte y claro, **música** debajo, **SFX** puntuando, **ambience** lo
más bajo. La jugada clave es **ducking**: baja la música cuando hay VO. Mejor con **sidechain compressor** keyed al
track de VO (la música baja sola al hablar, se recupera en los huecos); versión manual = keyframear el volumen ~-6 a -10 dB bajo el habla.

## Loudness — entrega al LUFS de la plataforma
Integrated LUFS es lo que las plataformas normalizan. Targets (2025-26): **YouTube/Spotify ≈ -14 LUFS**, podcasts
≈ -16, **TikTok/Instagram más caliente ~-10 a -12**. **True Peak ≤ -1.0 dBTP** (≤ -1.5 más seguro pre-transcode). Masteriza a ~-14 para cross-platform; empuja a -10/-11 solo en short-form social donde lo fuerte gana.

## Sync a la imagen
Corta al beat (snap a transients). Coloca **hit points** — un sonido exacto en un acento visual (boom cuando el
logo aterriza). El sound design *vende el movimiento* que la IA no simuló físicamente: un swoosh hace que un pan se
sienta intencional, un thud da peso a un paso. **VO** generado por TTS (ref 40); colócalo seco y al frente, luego duck la música.

## ffmpeg audio
```bash
# mezclar VO sobre música con ducking (sidechain)
ffmpeg -i music.mp3 -i vo.wav -filter_complex "[0:a][1:a]sidechaincompress=threshold=0.05:ratio=8:release=300[m];[m][1:a]amix=inputs=2:duration=longest" out.wav
# normalizar a broadcast (two-pass = preciso)
ffmpeg -i in.wav -af loudnorm=I=-14:TP=-1:LRA=11 out.wav
# muxear audio a video y cortar al stream más corto
ffmpeg -i v.mp4 -i a.wav -c:v copy -c:a aac -b:a 192k -shortest out.mp4
```

## Gotchas
1. Música muy fuerte sobre VO = el error amateur #1 → ducking.
2. Sin ducking = muro de lodo.
3. Música con copyright = demonetización/takedown, aun 5 segundos.
4. Ignorar LUFS → la plataforma te baja el nivel y tu mezcla "fuerte" suena floja.
5. `loudnorm` single-pass es aproximado; two-pass (medir luego aplicar) clava el target.
6. `-shortest` es esencial o el video sigue con silencio/negro.
7. Tracks de Suno/Udio free-tier NO están clearados comercialmente — verifica antes de usar en marca/cliente.
8. Los clips IA NO tienen ambience nativo — el silencio debajo se lee "fake"; siempre pon una cama de room-tone/ambience.

**Fuentes:** clickyapps.com (LUFS targets 2025) · izotope.com/learn (mastering streaming) · freesound.org · ffmpeg.org (loudnorm).
