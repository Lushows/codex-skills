# 68 — Color por plataforma

Tú no entregas tu video. Entregas un archivo que **la plataforma vuelve a comprimir** antes de que
nadie lo vea. Instagram, TikTok, WhatsApp y YouTube toman tu mp4, lo re-codifican con sus propios
parámetros, a veces lo reescalan, y lo sirven en varias versiones según el dispositivo y la
conexión de cada persona.

O sea: **el video que ves tú no es el video que ve tu cliente.** Y lo primero que se pierde en esa
recompresión es, casi siempre, el color.

Este módulo es sobre cómo entregarles un archivo que sobreviva.

> **Aviso de fecha:** las especificaciones concretas (resoluciones, límites de peso, códecs)
> cambian cada pocos meses. Esto está a **4 de agosto de 2026**. Lo que **no** cambia es la física
> de la recompresión, y eso es lo que de verdad hay que entender. Si vas a publicar hoy algo
> crítico, verifica las cifras exactas en la documentación de la plataforma.

---

## 1. Qué le pasa a tu color cuando lo subes

Cinco daños, en orden de frecuencia:

### a) Banding en los degradados

Es el daño número uno. Un cielo, una pared iluminada, un fondo con gradiente, **tu viñeta**: todo
eso pierde niveles y aparecen escalones. En negros y azules oscuros es donde peor se ve. Si tu marca
usa un azul oscuro (como el `#09163A` del módulo `64`), este es tu enemigo directo.

### b) Croma embarrado

La recompresión gasta el bitrate en el brillo y le quita al color. Los bordes de color saturado
—texto rojo, un letrero de neón, una camiseta amarilla— quedan con halo sucio. Los rojos puros son
los peores.

### c) Bloques en las sombras

Las zonas oscuras se llevan menos bitrate. Un plano de bar de noche que en tu computador se ve
elegante, en Instagram se ve como un mosaico. **El look "oscuro y cinematográfico" es el que peor
sobrevive a las redes.**

### d) Desplazamiento de tinte por etiquetas perdidas

Si tu archivo no lleva las etiquetas de color, algunos reproductores interpretan BT.601 en vez de
BT.709 y todo se corre hacia el verde-magenta. Es sutil pero constante, y hace que "en el celular se
vea distinto". Se arregla gratis (ver `60`).

### e) Aplastamiento por la pantalla del que mira

Nada que ver con la plataforma: los celulares con modo vívido suben la saturación entre 10% y 25%.
Un video que ya venía saturado se ve chillón. No lo controlas, pero **sí puedes no depender de
saturación alta**.

---

## 2. Las seis defensas (valen para todas las plataformas)

Antes de ir plataforma por plataforma, esto es lo que hay que hacer siempre:

**1. Etiqueta el color.** Cuatro parámetros, cero costo:

```bash
-colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
-x264-params "colorprim=bt709:transfer=bt709:colormatrix=bt709"
```

**2. `format=yuv420p`.** Sin negociación. Cualquier otro formato de píxel se ve mal o no se ve.

**3. Entrega a la resolución exacta de la plataforma.** Si subes 4K a un feed que sirve 1080p, el
escalado lo hace el servidor con su algoritmo, no con el tuyo. Escala tú, con calidad:

```bash
-vf "scale=1080:1920:flags=lanczos"
```

**4. Sube un archivo con bitrate generoso.** La plataforma va a recomprimir **a partir de tu
archivo**. Un archivo limpio de entrada produce una recompresión limpia de salida. Entrega en
CRF 17–18, no en 23. Que pese 40 MB no importa: el que se sirve al público es el de ellos.

**5. Mete grano fino.** Es el antídoto contra el banding y cuesta poco. `noise=c0s=5:c0f=t+u`
(ver `66`).

**6. No dependas de matices finos en las sombras ni de saturación extrema.** Todo lo que esté por
debajo del 12% de brillo o por encima del 90% de saturación es material que la plataforma va a
destruir. Diseña el look asumiendo que esas zonas no existen.

---

## 3. Plataforma por plataforma

### 📸 Instagram (Reels y feed)

**Qué hace:** re-codifica a H.264 (y a veces sirve versiones alternativas según el dispositivo).
Reels a 1080×1920. Feed vertical a 1080×1350. Reduce bastante el bitrate.

**Dónde duele:** banding en fondos lisos y en degradados de marca; sombras con bloques; texto de
color saturado con bordes sucios.

**Compensación:**
- Sube el brillo de las sombras un pelín respecto a lo que te gustaría. Lo que en tu monitor es
  "elegante y oscuro", en Instagram es "no se ve nada".
- Grano obligatorio si hay degradados.
- Texto: blanco o negro con contorno. Evita texto de color saturado en tipografía delgada.

```bash
ffmpeg -i master.mp4 -vf \
"scale=1080:1920:flags=lanczos,curves=all='0/0.012 0.2/0.215 0.5/0.5 1/1',noise=c0s=5:c0f=t+u,format=yuv420p" \
  -c:v libx264 -crf 17 -preset slow -profile:v high -level 4.1 -g 60 -pix_fmt yuv420p \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -x264-params "colorprim=bt709:transfer=bt709:colormatrix=bt709" \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart IG_reel.mp4
```

(La curva `0/0.012 0.2/0.215` es el "seguro anti-Instagram": levanta muy poco el negro y abre las
sombras bajas lo justo para que sobrevivan.)

### 🎵 TikTok

**Qué hace:** la compresión más agresiva de las tres. Y hay una diferencia grande según **cómo
subes**: grabar dentro de la app, subir desde la galería, o subir desde el escritorio. Subir desde
la galería del celular con el archivo ya en 1080×1920 suele conservar más.

**Dónde duele:** movimiento rápido + detalle fino = mosaico. Cortes rápidos (que en TikTok son la
norma) hacen que cada corte sea un fotograma clave caro, y el resto de fotogramas se quedan sin
bitrate.

**Compensación:**
- **Menos detalle fino.** Un fondo texturado con mil elementos se convierte en papilla. Fondos
  limpios sobreviven.
- **GOP corto** (`-g 30` o menos): más fotogramas clave, mejor recuperación en cortes rápidos.
- Contraste un poco más alto de lo normal: la compresión aplana, así que hay que darle margen.
- El grano aquí es más discutible: con cortes muy rápidos y compresión agresiva, el grano se come
  bitrate que hace falta en otra parte. Baja a `alls=4` o quítalo.

```bash
ffmpeg -i master.mp4 -vf \
"scale=1080:1920:flags=lanczos,eq=contrast=1.04,noise=c0s=4:c0f=t+u,format=yuv420p" \
  -c:v libx264 -crf 17 -preset slow -profile:v high -g 30 -keyint_min 15 \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -x264-params "colorprim=bt709:transfer=bt709:colormatrix=bt709" \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart TT_video.mp4
```

### 💬 WhatsApp

**La peor de todas, y la más importante para negocios en Colombia.** Si vendes por WhatsApp (como
GastroLatam), este es tu canal principal.

**Qué hace:** comprime brutalmente para que el archivo pese poco. En estados y en mensajes normales
recodifica sin piedad. Un video de 40 MB puede quedar en 3 MB.

**Dónde duele:** en todo. Banding, bloques, croma destruido, resolución reducida.

**Compensación — tres tácticas, en orden de efectividad:**

**1. Enviar como documento.** WhatsApp **no recomprime los documentos**. El receptor tiene que
descargarlo y no ve vista previa, pero llega exactamente como lo mandaste. Para un video de venta
que el cliente pidió, es la mejor opción.

**2. Pre-comprimir tú al tamaño objetivo.** Si el archivo ya es pequeño, WhatsApp tiene menos que
quitar. Apunta a **menos de 15 MB** y a **720×1280** (WhatsApp reduce resolución de todos modos):

```bash
# Objetivo: ~12 MB para un video de 45 s → ~2.000 kbps de video
ffmpeg -i master.mp4 -vf "scale=720:1280:flags=lanczos,noise=c0s=4:c0f=t+u,format=yuv420p" \
  -c:v libx264 -b:v 1900k -maxrate 2200k -bufsize 4000k -preset slow -profile:v main -g 60 \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -c:a aac -b:a 128k -ar 44100 -movflags +faststart WA_video.mp4

# Comprobar el peso
ls -lh WA_video.mp4
```

**3. Diseñar el video para WhatsApp desde el principio.** Menos planos oscuros, menos degradados,
texto grande y de alto contraste, y el mensaje entendible aunque el video se vea regular. Esto vale
más que cualquier parámetro de ffmpeg.

### ▶️ YouTube

**La más amable de las cuatro.** Bitrates más altos, y si subes en resolución mayor que 1080p te
asigna un códec mejor (VP9/AV1 en vez de H.264), lo cual **mejora el resultado incluso para quien lo
ve en 1080p**.

**Truco real:** sube un master en 1440p o 2160p aunque tu contenido sea 1080p. La ganancia de códec
es mayor que la pérdida por el escalado.

```bash
# Master 1080p escalado a 1440p para ganar códec
ffmpeg -i master.mp4 -vf "scale=2560:1440:flags=lanczos,format=yuv420p" \
  -c:v libx264 -crf 16 -preset slow -g 60 \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -x264-params "colorprim=bt709:transfer=bt709:colormatrix=bt709" \
  -c:a aac -b:a 320k -ar 48000 -movflags +faststart YT_master.mp4
```

### 📣 Anuncios de Meta (Facebook/Instagram Ads)

Igual que Instagram en cuanto a compresión, pero con un factor extra: el anuncio compite por
atención en un feed lleno. **El contraste y la legibilidad importan más que la sutileza del grado.**
Y el video se va a ver en miniatura, con el brillo del celular al 40%, al sol, en un bus.

Prueba real antes de lanzar: mira tu anuncio en el celular, al sol, con el brillo a la mitad. Si no
se entiende, sube contraste y agranda el texto. Todo el trabajo de color no vale nada si el mensaje
no llega. Ver `145-video-para-anuncios-meta.md`.

---

## 4. El ciclo de verificación real: sube, descarga, compara

Esta es la única forma honesta de saber qué le hizo la plataforma a tu video. Toma 10 minutos y hay
que hacerlo **una vez por cliente y por formato**, no en cada pieza.

1. Sube el video (puedes ponerlo privado o solo para ti).
2. Descárgalo de vuelta.
3. Compara:

```bash
# Similitud estructural: 1.000 sería idéntico
ffmpeg -i master.mp4 -i descargado.mp4 -lavfi "[0:v][1:v]ssim=stats_file=ssim.log" -f null -

# Diferencia visual amplificada — te muestra DÓNDE se dañó
ffmpeg -i master.mp4 -i descargado.mp4 -filter_complex \
  "[0:v]scale=1080:1920[a];[1:v]scale=1080:1920[b];[a][b]blend=all_mode=difference,eq=contrast=6" \
  -frames:v 150 diferencia.mp4

# Zonas del frame donde más se perdió
ffmpeg -y -ss 8 -i master.mp4 -frames:v 1 m.png
ffmpeg -y -ss 8 -i descargado.mp4 -frames:v 1 d.png
ffmpeg -y -i m.png -i d.png -filter_complex "hstack=inputs=2" comparacion.png
```

En `diferencia.mp4`, las zonas que se iluminan son las que la plataforma destruyó. Si se ilumina el
cielo → banding. Si se iluminan las sombras → bloques. Si se ilumina el texto → bajaste demasiado el
bitrate o el texto es muy fino.

**Guarda ese resultado.** La siguiente vez ya sabes qué compensar sin tener que probar.

---

## 5. La tabla de decisiones rápida

| Situación | Qué hacer |
|---|---|
| Look oscuro y cinematográfico + Instagram/WhatsApp | Levantar sombras un 2–4%. En serio. |
| Degradado de marca de fondo | Grano obligatorio (`c0s=5:c0f=t+u`) |
| Texto de color saturado, tipografía delgada | Cambiar a blanco/negro con contorno |
| Marca con azul o morado oscuro | Verificar banding **antes** de entregar; considerar levantar el punto negro |
| Video para vender por WhatsApp | Enviarlo como **documento**, o pre-comprimir a < 15 MB |
| Cortes muy rápidos en TikTok | GOP corto (`-g 30`), menos detalle fino, menos grano |
| Contenido para YouTube | Subir en 1440p aunque sea 1080p |
| Anuncio de Meta | Contraste y legibilidad por encima de la sutileza |
| Cliente dice "se ve distinto en mi celular" | Pedir captura antes de tocar nada; revisar etiquetas de color |

---

## Errores comunes

- **Entregar sin etiquetas de color.** Gratis de arreglar, y causa la mitad de las quejas.
- **Entregar sin `format=yuv420p`.** Se ve mal o no reproduce.
- **Subir 4K a Instagram.** El servidor escala peor de lo que escalarías tú.
- **Comprimir mucho antes de subir "para que suba rápido".** La plataforma recomprime encima: doble
  pérdida. Sube pesado (CRF 17–18).
- **Confiar en que el look oscuro se ve igual en el feed.** No se ve. Nunca.
- **Mandar video de venta por WhatsApp como video normal.** Llega hecho papilla. Como documento.
- **Usar degradados de marca sin grano.** Anillos garantizados.
- **Texto rojo o azul puro delgado.** El croma submuestreado más la recompresión = bordes sucios.
- **No hacer nunca el ciclo subir/descargar/comparar** y seguir adivinando en cada pieza.
- **Copiar especificaciones de un blog de hace tres años.** Cambian. Verifica.
- **Optimizar el color y descuidar que el mensaje se entienda en miniatura y al sol.** Es el error
  de prioridades más caro.
- **Entregar con HDR activado** (clips de iPhone) a plataformas que lo convierten mal: sale lavado.
  Convierte a SDR tú mismo (ver `60`).

---

## Checklist

- [ ] Sé exactamente en qué plataformas se va a publicar esta pieza.
- [ ] Escalé yo a la resolución exacta de destino, con `flags=lanczos`.
- [ ] El export lleva `format=yuv420p`.
- [ ] El export lleva las cuatro etiquetas de color + `-x264-params`.
- [ ] El export lleva `-movflags +faststart`.
- [ ] El CRF es 17–18 (o el bitrate está alto). No entregué comprimido de más.
- [ ] Si hay degradados o fondos lisos, hay grano fino.
- [ ] Levanté un poco las sombras si el destino es Instagram o WhatsApp.
- [ ] El texto es de alto contraste, no de color saturado en tipografía delgada.
- [ ] Para WhatsApp: el archivo pesa menos de 15 MB, o lo voy a enviar como documento.
- [ ] Para TikTok: GOP corto y menos detalle fino en fondos.
- [ ] Para YouTube: subí en 1440p o más para ganar códec.
- [ ] Hice al menos una vez el ciclo subir → descargar → comparar para este cliente y este formato.
- [ ] Vi la pieza en un celular real, al sol, con brillo al 50%, y se entiende.
