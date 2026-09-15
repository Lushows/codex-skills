# 90 — Formatos y códecs: qué es cada cosa y cuál usar

> El 90% de los problemas de "no me sube el video", "se ve raro en el celular del cliente" o "pesa 800 MB"
> se resuelven entendiendo **dos palabras**: contenedor y códec. No son lo mismo y casi todo el mundo las
> confunde.

---

## La analogía que necesitas y ya

Piensa en un video como **una caja con dos cosas adentro**:

- **El contenedor** es la caja: `.mp4`, `.mov`, `.mkv`, `.webm`. Es la extensión del archivo. La caja
  guarda el video, el audio, los subtítulos y los datos (fecha, cámara, rotación).
- **El códec** es el idioma en que está escrito lo de adentro: H.264, H.265, AV1, VP9, ProRes. Es la
  fórmula matemática que comprime la imagen para que no pese 400 GB.

**Una caja `.mp4` puede tener adentro H.264, H.265 o AV1.** Por eso dos archivos `.mp4` pueden comportarse
completamente distinto: uno abre en todas partes y el otro no abre en el computador de tu cliente.

Cuando alguien dice "mándamelo en MP4", en realidad casi siempre quiere decir **"mándamelo en MP4 con
H.264 adentro"**, que es lo único que abre en absolutamente todo lo que tenga pantalla.

Para ver qué hay dentro de una caja:

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=codec_name,profile,width,height,r_frame_rate,pix_fmt,bit_rate \
  -of default=noprint_wrappers=1 entrada.mp4
```

Eso te dice el códec real, no la extensión. Si el nombre dice `.mp4` pero `codec_name=hevc`, ya sabes por
qué el cliente no lo pudo abrir.

---

## Los cinco códecs que importan (agosto 2026)

### H.264 (también llamado AVC)

**El idioma universal.** Tiene más de 20 años y sigue siendo el rey de la compatibilidad. Absolutamente
todo lo reproduce: celulares de 2012, televisores viejos, WhatsApp, el PowerPoint del cliente.

- **Úsalo para:** todo lo que entregues, todo lo que subas a redes, todo lo que mandes por WhatsApp.
- **Ventaja:** nunca falla. Codifica rápido. Hardware de aceleración en todo aparato existente.
- **Desventaja:** es el que peor comprime de los cinco. Un archivo H.264 pesa aprox. **el doble** que el
  mismo video en AV1 con calidad parecida.
- **En ffmpeg:** `-c:v libx264`

**Regla de oro: si tienes duda, es H.264.** Perder 40% de tamaño no vale nada si el video no abre.

### H.265 / HEVC

El sucesor de H.264. Comprime **entre 30% y 50% mejor** con la misma calidad percibida. El problema no es
técnico, es legal: las patentes hicieron que Chrome, Firefox y muchos servicios web tardaran años en
soportarlo, y todavía hay huecos.

- **Úsalo para:** archivar material propio, mandar 4K entre profesionales, video de cámaras y drones
  (que casi siempre graban en HEVC).
- **Desventaja real:** el navegador del cliente puede no reproducirlo. Los editores viejos lo rechazan.
  Codifica bastante más lento que H.264.
- **En ffmpeg:** `-c:v libx265`
- **Trampa clásica:** el iPhone graba en HEVC dentro de `.mov` por defecto. Ese archivo se ve perfecto en
  el iPhone y **falla en medio mundo Windows**. Es la causa #1 de "el video del cliente no abre".

### AV1

Códec abierto y sin regalías, empujado por Google, Netflix y Amazon. **Comprime mejor que H.265** (entre
20% y 30% más). En 2026 ya lo reproducen Chrome, Firefox, Edge, Android moderno, iPhone 15 Pro en
adelante, y YouTube lo sirve por defecto en video popular.

- **Úsalo para:** web propia donde controlas el reproductor, y cuando el peso importa muchísimo.
- **Desventaja:** **codifica lento**. Con `libaom-av1` es una tortura; con `libsvtav1` es usable. Y
  todavía hay dispositivos que no lo decodifican por hardware, lo que quema batería.
- **En ffmpeg:** `-c:v libsvtav1` (el rápido) o `-c:v libaom-av1` (el lento de referencia)
- **No lo uses para entregar a un cliente.** Nunca.

### VP9

El AV1 anterior, también de Google. Vive casi exclusivamente en `.webm` y en YouTube. Comprime parecido a
H.265 pero sin líos de patentes.

- **Úsalo para:** web, si por algo no puedes usar AV1.
- **En 2026 está en retiro**: AV1 hace lo mismo mejor. No arranques proyectos nuevos con VP9.
- **En ffmpeg:** `-c:v libvpx-vp9`

### ProRes (y DNxHR)

Estos juegan otro deporte. No son códecs de **entrega**, son códecs de **trabajo** (mezzanine, o
intermedios). Comprimen poquísimo a propósito para que la imagen aguante correcciones de color, capas y
reexportaciones sin degradarse.

- **Úsalos para:** el máster que guardas, el archivo que le pasas a un colorista, material que vas a
  seguir editando.
- **Peso real:** ProRes 422 HQ a 1080p30 pesa aprox. **880 Mbps... no, 176 Mbit/s ≈ 1,3 GB por minuto.**
  Un video de 10 minutos son 13 GB. No es error: así es a propósito.
- **En ffmpeg:** `-c:v prores_ks -profile:v 3` (el 3 es 422 HQ)

Sabores de ProRes que vas a ver:

| Perfil | `-profile:v` | Para qué |
|---|---|---|
| ProRes Proxy | 0 | Editar en computador lento |
| ProRes LT | 1 | Entregas ligeras |
| ProRes 422 | 2 | Trabajo normal |
| **ProRes 422 HQ** | **3** | **El estándar de máster** |
| ProRes 4444 | 4 | Cuando necesitas canal alfa (transparencia) |

---

## Tabla de decisión — cuál uso para qué

| Situación | Contenedor | Códec video | Códec audio |
|---|---|---|---|
| Subir a Reels / TikTok / Shorts | `.mp4` | H.264 High | AAC 128–192 kbps |
| Subir a YouTube largo | `.mp4` | H.264 High (o HEVC si es 4K) | AAC-LC 48 kHz, 384 kbps |
| Anuncio en Meta Ads | `.mp4` | H.264 | AAC 128 kbps |
| Mandar por WhatsApp | `.mp4` | H.264 Baseline o Main, 720p | AAC 128 kbps |
| Entregar al cliente (visualización) | `.mp4` | H.264 High | AAC 192 kbps |
| Entregar al cliente (máster) | `.mov` | ProRes 422 HQ | PCM 48 kHz 24-bit |
| Guardar tu archivo maestro | `.mov` o `.mkv` | ProRes 422 HQ | PCM |
| Web propia, peso crítico | `.mp4` + `.webm` | AV1 + fallback H.264 | Opus / AAC |
| Video con transparencia (logos animados) | `.mov` | ProRes 4444 | — |

---

## Los contenedores, uno por uno

### `.mp4`
La caja universal. Soporta H.264, H.265, AV1, AAC. **Es tu opción por defecto para todo lo que salga de tu
computador.** Tiene una peculiaridad importante: el índice del archivo (llamado `moov atom`) por defecto
se escribe **al final**, lo que hace que un video en web tenga que descargarse entero antes de empezar.
Se arregla con `-movflags +faststart` (ver módulo 91).

### `.mov`
La caja de Apple. Técnicamente es prima hermana de MP4. Es la única que maneja ProRes correctamente y la
única que lleva canal alfa de forma confiable. **Úsala solo para másters y material de trabajo**, nunca
para subir a redes.

### `.mkv` (Matroska)
La caja más flexible: mete lo que quieras adentro, pistas de audio ilimitadas, subtítulos, capítulos. Es
excelente para archivo personal y **pésima** para entregar: muchos reproductores comerciales y casi ninguna
red social la aceptan.

### `.webm`
La caja de la web abierta. Solo VP9/AV1 + Opus/Vorbis. Úsala solo si estás sirviendo video desde tu propio
sitio y quieres el archivo más liviano posible.

### `.avi`, `.wmv`, `.flv`, `.3gp`
Muertos. Si te llega material así, conviértelo a algo moderno antes de editar y sigue con tu vida.

---

## Conversiones que vas a necesitar

**HEVC del iPhone → H.264 universal** (el arreglo más pedido del mundo):

```bash
ffmpeg -i IMG_4021.MOV -c:v libx264 -crf 18 -preset slow \
  -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart salida.mp4
```

**Cualquier cosa → ProRes 422 HQ para trabajar** (cuando el bruto es muy comprimido y el editor sufre):

```bash
ffmpeg -i bruto.mp4 -c:v prores_ks -profile:v 3 -pix_fmt yuv422p10le \
  -c:a pcm_s24le trabajo.mov
```

**Solo cambiar la caja sin recomprimir** (rapidísimo, sin pérdida — solo funciona si el códec de adentro
es compatible con la caja nueva):

```bash
ffmpeg -i entrada.mkv -c copy salida.mp4
```

Ese `-c copy` es magia: no recomprime nada, solo reempaqueta. Tarda segundos en vez de minutos y la
calidad es **idéntica**. Si lo único que necesitas es cambiar de `.mkv` a `.mp4`, nunca recomprimas.

**Máster ProRes → entrega H.264 para el cliente:**

```bash
ffmpeg -i master.mov -c:v libx264 -crf 18 -preset slow -profile:v high -level 4.1 \
  -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart entrega_cliente.mp4
```

**AV1 para tu web (con SVT-AV1, el rápido):**

```bash
ffmpeg -i master.mov -c:v libsvtav1 -crf 32 -preset 6 \
  -pix_fmt yuv420p -c:a libopus -b:a 128k salida.webm
```

---

## Averigua qué tiene tu ffmpeg

No todos los ffmpeg vienen con todos los códecs. Antes de pelear con un comando que "no funciona":

```bash
# ¿Tengo x265?
ffmpeg -encoders | grep -i 265

# ¿Tengo AV1 rápido?
ffmpeg -encoders | grep -i av1

# ¿Tengo libvmaf para medir calidad?
ffmpeg -filters | grep -i vmaf
```

Si `libsvtav1` no aparece, tu compilación no lo trae. En Windows, la compilación de gyan.dev "full" trae
todo; la "essentials" no.

---

## El audio también tiene códec

Se olvida siempre y causa problemas silenciosos.

| Códec audio | Cuándo |
|---|---|
| **AAC** | Todo lo que entregues o subas. 128 kbps para voz, 192 kbps si hay música importante |
| **PCM** (`pcm_s24le`) | Másters y material de trabajo. Sin compresión, pesa mucho, suena perfecto |
| **Opus** | Solo web con AV1/VP9. Mejor que AAC a bitrates bajos |
| **MP3** | Legado. No lo uses en video nuevo |

Y **siempre 48 kHz** en video. 44,1 kHz es de música/CD; si tu proyecto mezcla 44,1 y 48 vas a tener
desincronización de audio que aparece a los tres minutos y te vuelve loco.

---

## Errores comunes

1. **Creer que `.mp4` es un códec.** Es la caja. Lo que importa es lo de adentro. Verifica con `ffprobe`
   antes de asumir.
2. **Entregarle HEVC a un cliente.** Se ve perfecto en tu Mac y no abre en su Windows. Entrega H.264 High
   siempre, sin excepciones, salvo que el cliente te lo pida por escrito.
3. **Subir el `.MOV` del iPhone directo a YouTube.** Funciona, pero es HEVC en una caja rara: la
   plataforma lo recomprime peor. Convierte a H.264 antes.
4. **Recomprimir cuando solo necesitabas reempaquetar.** Si vas de `.mkv` a `.mp4` con el mismo códec,
   `-c copy`. Recomprimir gratis es regalar calidad.
5. **Usar AV1 para entregar.** Ahorras 30% de peso y ganas 100% de correos preguntando por qué no abre.
6. **Editar directo sobre H.264 de larga duración (long-GOP) en un computador flojo.** El editor tiene que
   reconstruir fotogramas y va a arrastrarse. Convierte a ProRes Proxy y sigue.
7. **Mezclar 44,1 kHz y 48 kHz en la misma línea de tiempo.** Deriva de audio garantizada.
8. **Guardar el máster en H.264.** Cada vez que lo reabras y reexportes pierdes calidad. El máster es
   ProRes (o el proyecto original), no el archivo de entrega.
9. **Exportar sin `-pix_fmt yuv420p`.** Ver módulo 91: es la causa de "se ve verde/negro" en algunos
   reproductores.
10. **Confiar en la extensión que alguien le puso al archivo.** Renombrar `.mkv` a `.mp4` no convierte
    nada; solo esconde el problema.

---

## Checklist

Antes de exportar o entregar cualquier archivo:

- [ ] Sé qué **códec** lleva adentro, no solo la extensión (`ffprobe` corrido)
- [ ] El destino final está definido: ¿redes, cliente, archivo, web?
- [ ] Si es entrega o red social: **H.264 dentro de `.mp4`**, sin excepciones
- [ ] Si es máster: **ProRes 422 HQ dentro de `.mov`** con audio PCM
- [ ] El audio va en **AAC 48 kHz** (entrega) o **PCM 48 kHz** (máster)
- [ ] Ninguna pista de audio del proyecto viene a 44,1 kHz
- [ ] Si el material fuente es HEVC de iPhone, ya lo convertí antes de editar
- [ ] Si solo cambié de contenedor, usé `-c copy` y no recomprimí
- [ ] Verifiqué que mi ffmpeg **sí trae** el códec que voy a usar (`ffmpeg -encoders`)
- [ ] El archivo que entrego lo abrí en **un aparato que no es el mío** antes de mandarlo
