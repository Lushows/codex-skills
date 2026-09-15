# 27 — Video, audio & media en web (sin matar performance)

Playbook 2026. Media bien usado eleva; mal usado destruye CWV y la batería. **Regla maestra: la imagen carga primero, el video después, y nada con sonido se reproduce solo.** **Léelo cuando uses video de fondo/hero, video de producto, o reemplaces GIFs.** Pareja de 19 (perf móvil) y 26.

## 1. Formatos & codecs

| Codec | Contenedor | Soporte 2026 | Cuándo |
|---|---|---|---|
| **H.264 (AVC)** | `.mp4` | Universal | **Fallback obligatorio, siempre** |
| **VP9** | `.webm` | Chrome/FF/Edge/Android (Safari no fiable) | 2º source, ~30-50% más liviano |
| **AV1** | `.mp4`/`.webm` | Chrome/Edge/FF/Android; **Safari solo con HW** (M3/M4, iPhone 15 Pro+) | El más liviano (~30% sobre VP9), NO como único |
| **HEVC** | `.mp4` (hvc1) | Apple sí, Chrome parcial | Fallback Apple sin AV1 (opcional) |

**Cascada** (el navegador usa el 1er `<source>` que entiende → más liviano a más compatible):
```html
<video autoplay muted loop playsinline preload="none" poster="/media/hero-poster.avif" class="hero-video">
  <source src="/media/hero-av1.mp4"  type="video/mp4; codecs=av01.0.05M.08">
  <source src="/media/hero-vp9.webm" type="video/webm; codecs=vp9">
  <source src="/media/hero-h264.mp4" type="video/mp4; codecs=avc1.4d401f">
</video>
```
**Targets de peso** (hero 1080p, 6-10s, sin audio): AV1 ≤0.8-1.5MB · VP9 ≤1.5-2.5MB · H.264 ≤2.5-4MB. Si superas ~3MB en el fallback, baja resolución (720p basta para fondo difuminado), acorta el loop o usa CDN.
**CDN/streaming** cuando: video >~5MB, catálogo, bitrate adaptativo o tráfico global (Mux/Cloudflare Stream/Bunny transcodifican + HLS). Para un hero loop, MP4 estático basta — no metas HLS donde no hace falta.

## 2. Hero / background video

**Autoplay no negociable: `muted` + `playsinline` + `autoplay`** juntos (sin `muted` se bloquea; sin `playsinline` iOS abre pantalla completa).
**El video NUNCA es el LCP** — su `poster` lo es. Por eso: `poster` con imagen optimizada (AVIF/WebP), `preload="none"` (o `metadata`), y si el poster es LCP súbele prioridad: `<link rel="preload" as="image" href="/media/hero-poster.avif" fetchpriority="high">`.
**CLS=0:** declara dimensiones/`aspect-ratio`. `.hero-video{ width:100%; height:100svh; object-fit:cover; aspect-ratio:16/9 }`.
**Lazy-load** (cargar/reproducir al entrar en viewport): IntersectionObserver que asigna `src` desde `data-src` y llama `.load()`+`.play().catch(()=>{})`.
**Móvil:** autoplay puede fallar (Data Saver/batería) → el `poster` debe verse perfecto solo; sirve video más ligero o `@media (max-width:768px){ .hero-video{display:none} }` (solo poster).
**`prefers-reduced-motion` obligatorio:** `@media (prefers-reduced-motion: reduce){ .hero-video{display:none} }` (el poster como background-image queda estático).

## 3. Reemplazar GIFs (crítico)

GIF = 256 colores, sin compresión inter-frame, **pesa 5-10× más** que el mismo clip en video (caso web.dev: 3.7MB GIF → 551KB MP4 → 341KB WebM, ~90% menos). Lighthouse lo penaliza.
```html
<video autoplay loop muted playsinline preload="metadata" poster="/media/demo-poster.webp" width="600" height="400">
  <source src="/media/demo.webm" type="video/webm"><source src="/media/demo.mp4" type="video/mp4">
</video>
```
```bash
ffmpeg -i in.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -crf 25 out.mp4
ffmpeg -i in.gif -c:v libvpx-vp9 -b:v 0 -crf 35 out.webm
```
**Según el caso:** animación vectorial/UI/iconos → **Lottie** (JSON) o **Rive** (.riv, más liviano e interactivo) · animación corta de imagen → Animated AVIF/WebP/APNG · clip de video real → MP4/WebM. **Casi nunca GIF.**

## 4. Adaptive, streaming & embeds

**MP4 simple** basta para hero loops, clips cortos, demos <30s. **HLS/DASH adaptativo** cuando video largo (>1-2min), visto de principio a fin, o ajuste de calidad a la red (HLS estándar: Safari nativo, resto `hls.js`; Mux/Cloudflare/Bunny generan renditions).
**Facade para YouTube/Vimeo (no negociable):** un iframe de YouTube añade ~1.3MB + 22 requests + ~480ms JS y daña LCP/INP aunque uses `loading="lazy"`. Solución: **facade** (imagen + botón play que solo carga el iframe al clic, ~224× más rápido inicialmente). Usa `<lite-youtube videoid="...">` (Paul Irish) o casero:
```html
<div class="yt-facade" data-id="ID" style="background:#000 url('https://i.ytimg.com/vi/ID/maxresdefault.jpg') center/cover; aspect-ratio:16/9; cursor:pointer">
  <button aria-label="Reproducir video" class="yt-play"></button></div>
<script>document.querySelectorAll('.yt-facade').forEach(f=>f.addEventListener('click',()=>{
  const ifr=document.createElement('iframe'); ifr.width='100%'; ifr.height='100%'; ifr.allow='autoplay; encrypted-media'; ifr.allowFullscreen=true;
  ifr.src=`https://www.youtube-nocookie.com/embed/${f.dataset.id}?autoplay=1`; f.replaceChildren(ifr); },{once:true}));</script>
```

## 5. Audio en web

- **No existe autoplay con sonido** (requiere gesto del usuario). Nunca música/voz sin interacción.
- **Reproductor:** `<audio controls preload="metadata">` simple; custom para diseño (duración, scrubber accesible por teclado, velocidad).
- **Web Audio API** solo para procesamiento real (visualizadores/mezcla): `new AudioContext()` + `ctx.resume()` tras gesto (arranca `suspended`).
- **A11y obligatoria:** audio/podcast → **transcripción**; video con voz → **captions**. Requisito WCAG.
- **Música de fondo:** casi siempre mala idea; si la marca lo exige, arranca **muteada** + botón visible + memoria de preferencia.

## 6. A11y & UX de media

- **Captions** con `<track kind="captions" src="demo.es.vtt" srclang="es" label="Español" default>` (WebVTT).
- **Controles:** background video sin controles, pero todo video informativo lleva `controls` reales, enfocables por teclado, con `aria-label`.
- **Pausa para fondo:** WCAG 2.2.2 exige poder pausar/detener movimiento >5s → añade botón de pausa al hero aunque sea mudo.
- **Contraste de controles** sobre video: overlay/gradiente (ratio ≥3:1).
- **CWV:** poster = LCP optimizado; `aspect-ratio` = CLS 0; `preload="none"` + facades = INP sano (el patrón poster+video mejora LCP ~840ms según web.dev).

## Media anti-patterns — blacklist
autoplay con sonido · GIFs animados (convertir a MP4/WebM o Lottie/Rive) · video como LCP (sin poster) · sin `poster` (pantalla negra al cargar) · `preload="auto"` en el hero (roba banda) · iframe YouTube/Vimeo directo (usa facade) · archivos sin optimizar (4K/30MB para fondo difuminado de 720p) · sin `playsinline` (iOS fuerza pantalla completa) · sin dimensiones/`aspect-ratio` (CLS) · ignorar `prefers-reduced-motion` · HLS donde sobra un MP4 · un solo AV1 sin fallback (invisible en ~70% de Safari sin HW) · video sin captions / audio sin transcripción.
