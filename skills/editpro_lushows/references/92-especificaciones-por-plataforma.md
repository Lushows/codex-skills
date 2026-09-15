# 92 — Especificaciones por plataforma (verificadas a agosto de 2026)


> ⚠️ **Las cifras de zona segura de este módulo no son la referencia.**
> El dueño es `45-zona-segura-por-plataforma`, que además distingue el recorte
> geométrico (se calcula) de la interfaz de la app (se mide, y caduca). Antes de
> montar con un número de aquí, mídelo con `418-medir-la-zona-segura-de-verdad`.
> Cada plataforma **recomprime todo lo que subes**. No hay excepción. Tu trabajo no es entregar el archivo
> más bonito: es entregar el archivo que **sobreviva mejor** a la recompresión de ellos. Son cosas
> distintas y esa distinción es la mitad de este módulo.

---

## La verdad incómoda: tu video se va a recomprimir sí o sí

Cuando subes un video a Instagram, TikTok o YouTube, la plataforma lo vuelve a codificar para servirlo a
millones de conexiones distintas. Ese segundo paso de compresión es donde se pierde la nitidez.

Consecuencias prácticas:

1. **Subir con más calidad de la que ellos van a servir SÍ ayuda.** Un archivo limpio se recomprime mejor
   que uno ya maltratado. Por eso conviene subir a bitrate alto aunque te lo bajen.
2. **Pero subir un archivo de 3 GB no ayuda más que uno de 60 MB bien hecho.** Hay un techo donde deja de
   importar.
3. **El detalle fino y el grano son enemigos.** El ruido consume bits en la recompresión y hace que el
   resto se vea peor. Si tu material tiene ruido, límpialo antes de subir.
4. **Los degradados grandes** (cielos, fondos de color, viñetas) son lo primero que se rompe en bandas.

---

## Instagram Reels

| Parámetro | Valor |
|---|---|
| Resolución | **1080 × 1920** (9:16) |
| Relación de aspecto | 9:16 para Reels · 4:5 (1080 × 1350) para Feed · 1:1 para cuadrado |
| Fotogramas por segundo | 30 fps (acepta hasta 60) |
| Duración | Hasta **3 minutos** grabando en la app · hasta 15 minutos subiendo desde archivo (formatos largos hasta 20 min en despliegue) |
| **Duración que funciona** | **7–90 segundos.** El grueso del alcance vive bajo 90 s |
| Bitrate de video | 5.000–10.000 kbps (mínimo 3.500 para que aguante) |
| Peso máximo | 4 GB |
| Códec | H.264, perfil High |
| Audio | AAC, 128 kbps, 48 kHz, estéreo |

**Zonas seguras (críticas):** la interfaz de Instagram tapa la parte de arriba y de abajo.

- **Arriba:** deja libres los primeros **~250 px** (barra de estado y controles)
- **Abajo:** deja libres los últimos **~420 px** (usuario, descripción, audio, botones)
- **Derecha:** deja libres **~180 px** (columna de likes, comentarios, compartir)

Traducido: **todo texto importante va entre el píxel 250 y el 1500 de alto, y no pasa de x=900.**

**Portada:** Instagram permite escoger un fotograma o subir una imagen (1080 × 1920). Ver módulo 94.

```bash
# Exportación Reels
ffmpeg -i master.mov -vf "scale=1080:1920:force_original_aspect_ratio=increase,\
crop=1080:1920,setsar=1" -c:v libx264 -crf 19 -preset slow -profile:v high -level 4.1 \
  -pix_fmt yuv420p -r 30 -g 60 -keyint_min 60 -sc_threshold 0 \
  -c:a aac -b:a 128k -ar 48000 -movflags +faststart reel_ig.mp4
```

---

## TikTok

| Parámetro | Valor |
|---|---|
| Resolución | **1080 × 1920** (9:16) |
| Fotogramas por segundo | 30 fps (60 fps si el contenido tiene mucho movimiento) |
| Duración máxima | 10 minutos grabando/subiendo desde la app · **60 minutos** subiendo desde web con material externo |
| **Duración que funciona** | **21–34 segundos** para el mejor promedio de finalización |
| Bitrate de video | 4.000–6.000 kbps a 30 fps · 8.000–10.000 kbps a 60 fps |
| Peso máximo | **287 MB en iOS · 72 MB en Android · 10 GB por web · 500 MB en Ads Manager** |
| Códec | H.264 (o H.265), AAC |

**Ese límite de 72 MB en Android es un cuchillo.** Si tu editor está en Android, o el cliente sube desde
Android, un reel de 60 s a bitrate alto no cabe. **Sube siempre desde la web de TikTok** (10 GB) cuando la
calidad importe: es el camino que menos recomprime.

**Zonas seguras de TikTok:** la interfaz es todavía más invasiva que la de Instagram.

- **Arriba:** ~130 px
- **Abajo:** ~480 px (descripción larga + nombre + música + barra de navegación)
- **Derecha:** ~190 px (columna de iconos)

**Los subtítulos automáticos de TikTok caen exactamente donde la gente pone su texto.** Si vas a quemar
subtítulos, ponlos **entre el 55% y el 70% de la altura** para no chocar.

---

## YouTube Shorts

| Parámetro | Valor |
|---|---|
| Resolución | **1080 × 1920** (9:16). YouTube acepta hasta 4K vertical |
| Duración | Hasta **3 minutos** — cualquier video vertical de ≤3 min entra automáticamente como Short |
| Fotogramas por segundo | 30 o 60 |
| Bitrate de video | **10.000–15.000 kbps** (YouTube recomprime fuerte; sube alto) |
| Códec | H.264 High, AAC-LC 48 kHz |

**Diferencia importante contra Reels y TikTok:** YouTube premia **la retención absoluta en segundos**, no
solo el porcentaje. Un Short de 25 segundos con 90% de retención rinde distinto a uno de 3 minutos con
40%. Corta lo que sobre.

**Zonas seguras:** arriba ~150 px, abajo ~350 px, derecha ~160 px.

---

## YouTube (video largo, horizontal)

| Parámetro | Valor |
|---|---|
| Resolución | 1920 × 1080 (mínimo serio) · 2560 × 1440 · **3840 × 2160 (4K)** |
| Relación de aspecto | 16:9 |
| Fotogramas por segundo | **La misma del original.** 24, 25, 30, 48, 50 o 60 |
| Contenedor / códec | `.mp4` con H.264 perfil High (HEVC aceptable en 4K) |
| Audio | **AAC-LC 48 kHz — 384 kbps estéreo** · 512 kbps para 5.1 |
| Codificación | VBR de dos pasadas para material no en vivo |

**Bitrates de subida recomendados (2026):**

| Resolución | 24–30 fps | 48–60 fps |
|---|---|---|
| 1080p | **8–15 Mbps** | 12–20 Mbps |
| 1440p | 16 Mbps | 24 Mbps |
| 4K SDR | **35–45 Mbps** | 53–85 Mbps |

**El truco del 1440p:** YouTube usa el códec VP9/AV1 (mejor) para 1440p y 4K, y H.264 (peor) para 1080p.
Si subes un video de 1080p **escalado a 1440p**, YouTube lo sirve con el códec bueno y **se ve más nítido**
que el mismo material subido a 1080p. Es real y sigue funcionando en 2026.

```bash
# El truco 1440p — escalado con filtro de buena calidad
ffmpeg -i master_1080.mov -vf "scale=2560:1440:flags=lanczos" \
  -c:v libx264 -crf 16 -preset slow -profile:v high -level 5.1 \
  -pix_fmt yuv420p -g 60 -keyint_min 60 \
  -c:a aac -b:a 384k -ar 48000 -movflags +faststart youtube_1440.mp4
```

**Miniatura de YouTube:** 1280 × 720 px, JPG o PNG, **máximo 2 MB**. Ver módulo 94.

---

## WhatsApp

WhatsApp es la plataforma más restrictiva de todas, y en LatAm es donde de verdad se vende. Trátala con
respeto.

| Parámetro | Valor |
|---|---|
| Peso máximo por video en chat | **16 MB** |
| Peso máximo enviándolo **como documento** | **2 GB** (pero sin previsualización ni reproducción en línea) |
| Estado (Status) | MP4 o 3GP · **máximo 30 segundos** · **16 MB** · **máximo 720p** |
| Resolución práctica | **720 × 1280** vertical o 1280 × 720 horizontal |
| Códec | H.264 perfil Main o Baseline, AAC |

**16 MB es poquísimo.** Da para aproximadamente:

| Duración | Bitrate total que cabe |
|---|---|
| 15 s | ~8.700 kbps (lujo) |
| 30 s | ~4.300 kbps (cómodo) |
| 60 s | ~2.100 kbps (justo) |
| 90 s | ~1.400 kbps (se ve regular) |
| 3 min | ~700 kbps (feo) |

**WhatsApp recomprime brutalmente igual.** Un video de 40 MB que le mandes se convierte en una papilla.
Por eso lo mejor es **entregarle un archivo que ya cumple el límite**, hecho por ti con buen criterio, en
vez de dejar que él lo destroce.

```bash
# WhatsApp — 60 segundos que caben en 16 MB y se ven decentes
ffmpeg -i master.mov -vf "scale=-2:720" \
  -c:v libx264 -b:v 1800k -maxrate 2000k -bufsize 4000k -preset slow \
  -profile:v main -level 3.1 -pix_fmt yuv420p \
  -c:a aac -b:a 96k -ar 48000 -ac 1 -movflags +faststart wa.mp4

# Verifica que sí cabe
ls -lh wa.mp4
```

Si te pasas de 16 MB, baja el bitrate de video, no la resolución. 720p a 1500 kbps se ve mejor que 480p a
2500 kbps para contenido con cara hablando.

---

## Meta Ads (Facebook / Instagram publicidad)

| Parámetro | Valor |
|---|---|
| **Relaciones de aspecto** | **4:5 (1080 × 1350)** para Feed · **9:16 (1080 × 1920)** para Reels y Stories · 1:1 para carrusel |
| Peso máximo | **4 GB** |
| Duración | 1 s a 241 minutos (técnico) — **útil: 6 a 30 segundos** |
| Códec | H.264 perfil High, AAC 128 kbps |
| Fotogramas por segundo | 30 fps |
| Resolución mínima aceptable | 1080 px en el lado más largo |

**La regla de 2026 en Meta:** más del 70% de las impresiones son móviles y el vertical captura entre 25% y
30% más interacción. **Sube 9:16 y 4:5 como mínimo.** El 16:9 solo si es específicamente para escritorio.

**Ubicaciones Advantage+:** Meta recorta automáticamente tu creativo para cada ubicación. Eso significa que
**si tu texto está cerca del borde, Meta te lo va a cortar** sin avisar. Sube el creativo con el texto bien
adentro y, si puedes, **sube versiones nativas de cada relación de aspecto** en vez de dejar que Meta
recorte.

**Zona segura para anuncios en Reels/Stories:** 14% arriba y 20% abajo libres de texto. Meta pone ahí el
perfil, el CTA y la etiqueta de "Patrocinado".

**Sobre el texto en la imagen:** la vieja regla del 20% de texto ya no rechaza anuncios, pero **el sistema
de entrega sigue penalizando** creativos saturados de texto con menor alcance por el mismo presupuesto.
Menos texto, más grande.

```bash
# Un máster 9:16 → las tres relaciones de Meta de una sola vez
ffmpeg -i master_vertical.mov \
  -vf "scale=1080:1920,setsar=1" -c:v libx264 -crf 19 -preset slow -profile:v high \
     -pix_fmt yuv420p -r 30 -c:a aac -b:a 128k -movflags +faststart ad_9x16.mp4 \
  -vf "crop=ih*4/5:ih,scale=1080:1350,setsar=1" -c:v libx264 -crf 19 -preset slow \
     -profile:v high -pix_fmt yuv420p -r 30 -c:a aac -b:a 128k -movflags +faststart ad_4x5.mp4 \
  -vf "crop=ih*9/16:ih*9/16,scale=1080:1080,setsar=1" -c:v libx264 -crf 19 -preset slow \
     -profile:v high -pix_fmt yuv420p -r 30 -c:a aac -b:a 128k -movflags +faststart ad_1x1.mp4
```

Ojo: los recortes automáticos sirven de punto de partida, pero **revísalos**. Un recorte 4:5 sobre un plano
9:16 puede decapitar a la persona.

---

## Tabla rápida — todo junto

| Plataforma | Resolución | fps | Duración útil | Bitrate subida | Peso máx |
|---|---|---|---|---|---|
| IG Reels | 1080×1920 | 30 | 7–90 s | 5–10 Mbps | 4 GB |
| IG Feed | 1080×1350 | 30 | 15–60 s | 5–10 Mbps | 4 GB |
| TikTok | 1080×1920 | 30/60 | 21–34 s | 4–6 Mbps | 72 MB–10 GB* |
| YT Shorts | 1080×1920 | 30/60 | 15–60 s | 10–15 Mbps | — |
| YT largo | 1920×1080+ | original | libre | 8–15 Mbps | 256 GB |
| WhatsApp chat | 720×1280 | 30 | ≤60 s | ~2 Mbps | **16 MB** |
| WhatsApp estado | 720×1280 | 30 | **≤30 s** | ~4 Mbps | **16 MB** |
| Meta Ads | 1080×1920 / 1080×1350 | 30 | 6–30 s | 5–10 Mbps | 4 GB |

\* depende del dispositivo desde el que subas: Android 72 MB, iOS 287 MB, web 10 GB.

---

## Verificar zonas seguras con ffmpeg

Antes de publicar, dibuja las zonas prohibidas encima de tu video y mira si algún texto cae adentro:

```bash
# Rejilla de zona segura para 1080x1920 (Instagram/TikTok)
ffmpeg -i reel.mp4 -vf "drawbox=x=0:y=0:w=1080:h=250:color=red@0.35:t=fill,\
drawbox=x=0:y=1500:w=1080:h=420:color=red@0.35:t=fill,\
drawbox=x=900:y=250:w=180:h=1250:color=orange@0.30:t=fill" \
  -t 10 -c:v libx264 -crf 24 -pix_fmt yuv420p prueba_zonas.mp4
```

Si tu texto aparece bajo el rojo, muévelo. Punto.

---

## Errores comunes

1. **Subir el mismo archivo a las cinco plataformas.** Cada una tiene límites distintos y penaliza cosas
   distintas. Exporta versiones.
2. **Subir a TikTok desde Android.** El límite de 72 MB te obliga a un archivo maltratado. Sube desde web.
3. **Poner el texto en el tercio inferior de un vertical.** Es exactamente donde la app pone la descripción
   y los botones. Nadie lo lee.
4. **Mandar un video de 5 minutos por WhatsApp.** O no llega, o llega irreconocible. Corta o mándalo como
   documento avisando que no tendrá previsualización.
5. **Subir el estado de WhatsApp de 45 segundos.** El límite es 30 s: WhatsApp lo parte en varios estados y
   arruina el ritmo.
6. **Escalar 1080p a 4K creyendo que YouTube lo sirve mejor.** El truco funciona hasta 1440p; escalar a 4K
   real desde 1080p solo agranda el archivo sin ganar nitidez y puede verse blando.
7. **Dejar que Advantage+ recorte tu creativo y no revisarlo.** Meta corta cabezas y textos sin piedad.
8. **Cambiar los fps del original en YouTube largo.** Si grabaste a 24, sube a 24. Convertir 24→30 mete
   fotogramas duplicados y el movimiento se ve entrecortado.
9. **Meter grano o ruido "estético" en un reel.** La recompresión de la plataforma lo convierte en papilla
   y le roba bits al resto de la imagen.
10. **Confiar en la portada automática.** La plataforma escoge un fotograma al azar, casi siempre con la
    persona con los ojos cerrados. Escógela tú (módulo 94).
11. **Usar 16:9 en pauta de Meta en 2026.** Regalas el 60% de la pantalla del móvil.
12. **No verificar el resultado con `ffprobe`.** "Exporté a 1080p" es una suposición hasta que lo mides.

---

## Checklist

Antes de subir cualquier video a cualquier plataforma:

- [ ] Sé a qué plataforma va y exporté **esa** versión, no una genérica
- [ ] Resolución exacta de la plataforma (`ffprobe` confirmado)
- [ ] fps correcto — y si es YouTube largo, **igual al original**
- [ ] Duración dentro del rango que rinde, no solo dentro del límite técnico
- [ ] Peso por debajo del límite del **método de subida** que voy a usar
- [ ] Todo el texto dentro de la **zona segura** (verificado con la rejilla)
- [ ] `-pix_fmt yuv420p` y `-movflags +faststart` presentes
- [ ] Audio AAC 48 kHz, con el bitrate que la plataforma pide
- [ ] La **portada** la escogí yo, no la plataforma
- [ ] Si va a pauta: exporté las relaciones 9:16 **y** 4:5 y revisé ambos recortes a ojo
- [ ] Si va a WhatsApp: el archivo ya pesa menos de 16 MB **antes** de mandarlo
- [ ] Reproduje el archivo final en un celular real antes de publicar
