# 146 — Video para WhatsApp y para anuncios que llevan a WhatsApp (CTWA)

> Verificado a **agosto de 2026**. Los límites de WhatsApp varían por versión de la app, por país y entre
> WhatsApp normal / Business / API. Lo que aquí digo son los valores que se sostienen en la mayoría de
> casos; **si tu app hace otra cosa, tu app tiene la razón.**

## Dos cosas distintas que la gente confunde

| | El video del **anuncio** | El video **dentro del chat** |
|---|---|---|
| Dónde vive | Instagram / Facebook / Reels | Adentro de la conversación de WhatsApp |
| Quién lo ve | Gente que no te conoce | Alguien que ya te escribió |
| Su trabajo | Que hagan clic y abran el chat | Que decidan comprar / reservar |
| Cómo se ve | Pantalla completa | Un cuadrito dentro de una burbuja |
| Peso | No importa (Meta lo aloja) | **Importa muchísimo (16 MB)** |
| Duración | 6–20 s | 8–30 s |

Este módulo cubre los dos. Son piezas distintas y **no debes usar la misma en ambos sitios.**

---

# Parte 1 — El video del anuncio CTWA

## Qué hace especial a un creativo de Click-to-WhatsApp

En un anuncio normal, el objetivo es que compren. En CTWA el objetivo es más chiquito y más fácil:
**que abran una conversación.** Eso cambia cómo se edita.

### La regla central

> **No vendas en el video. Vende la conversación.**

El video que dice "escríbenos y te decimos si hay mesa para el sábado" convierte mejor que el que intenta
explicar todo el menú. La gente hace clic para resolver una duda, no para comprar.

### Qué funciona en el creativo

1. **Que se vea que hay alguien del otro lado.** Una persona hablando, no un cartel. "Escríbeme" con una
   cara funciona mejor que "Contáctanos".
2. **Mostrar la conversación.** Un recurso que rinde: superponer una burbuja de chat de WhatsApp sobre el
   video con la pregunta que quieres que te hagan. Deja clarísimo qué va a pasar al hacer clic.
3. **Una pregunta concreta como CTA**: "Escríbeme *hola* y te mando la carta" es mejor que "Más
   información".
4. **Bajar la fricción explícita**: "sin llenar formularios", "te contesto ya".
5. **Verde de WhatsApp o el ícono en pantalla**, en el último tercio. Le dice al ojo a dónde va.
6. **El precio, si lo tienes.** Filtra a quien no va a comprar y te ahorra conversaciones basura.

### La disciplina de la promesa

Lo que promete el anuncio tiene que ser **exactamente** lo primero que dice el bot o la persona que
contesta. Si el anuncio dice "te mando la carta" y el bot arranca con "¡Hola! ¿En qué te puedo ayudar?",
acabas de romper la expectativa y pierdes a la mitad.

Esto no es edición, pero es lo que decide si tu edición sirvió de algo. Escribe el primer mensaje del chat
**al mismo tiempo** que escribes el CTA del video.

### Especificaciones del anuncio CTWA

Son las mismas de cualquier anuncio de Meta (ver `145`):

| Qué | Valor |
|---|---|
| Formato principal | 9:16 — 1080x1920 (Reels lleva el volumen) |
| Formato secundario | 4:5 — 1080x1350 (Feed) |
| Duración | 6–20 s |
| Códec / audio | H.264 MP4 / AAC 48 kHz |
| Zona libre abajo | **400+ px** (botón "Enviar mensaje") |

El botón de CTA de Meta en CTWA dice "Enviar mensaje" y aparece abajo. **No pongas tu propio CTA escrito
justo encima**: quedan dos llamados peleándose. Pon tu CTA en el centro-bajo, dentro de la zona segura.

### Estructura de 15 segundos que funciona

```
0,0–1,5 s   Gancho: el problema o el antojo. Movimiento. Texto grande.
1,5–5 s     La cosa: la comida, el trago, el lugar. Con precio.
5–10 s      La razón para escribir HOY: promoción, cupos, fecha.
10–15 s     CTA: "Escríbeme y te confirmo mesa" + verde de WhatsApp.
```

---

# Parte 2 — El video que mandas dentro del chat

Aquí está la parte que casi nadie hace bien.

## El límite que manda: 16 MB

WhatsApp comprime todo lo que le mandes como video, y tiene un tope duro alrededor de **16 MB** para
archivos enviados como *media* (video normal en el chat). Si tu archivo pesa más, WhatsApp lo comprime
agresivamente hasta que quepa — y ahí es donde tu video de la parrilla se convierte en una mancha marrón
pixelada.

### La regla de oro

> **Comprime tú antes, con criterio, en vez de dejar que WhatsApp lo haga sin criterio.**

Si le mandas un archivo de 12 MB bien codificado, WhatsApp lo toca poco. Si le mandas uno de 60 MB, lo
destroza.

### Los números que funcionan

| Duración | Resolución | Bitrate de video | Peso aproximado |
|---|---|---|---|
| 10 s | 1080x1920 | 4.000 kbps | ~5 MB |
| 20 s | 1080x1920 | 3.000 kbps | ~7,5 MB |
| 30 s | 1080x1920 | 2.500 kbps | ~9,5 MB |
| 45 s | 720x1280 | 2.000 kbps | ~11 MB |
| 60 s | 720x1280 | 1.500 kbps | ~11 MB |

**720x1280 se ve perfectamente bien en el chat.** Nadie ve un video de WhatsApp a pantalla completa en un
monitor. Bajar a 720p te compra el doble de bitrate por el mismo peso, y el bitrate es lo que evita los
bloques feos.

### El comando

```bash
# Video de chat: 20 s, vertical, seguro por debajo de 16 MB
ffmpeg -i corte.mov \
  -c:v libx264 -profile:v main -level 4.0 -pix_fmt yuv420p \
  -vf "scale=720:1280:flags=lanczos" \
  -b:v 2500k -maxrate 3000k -bufsize 5000k -r 30 \
  -c:a aac -b:a 96k -ar 44100 -ac 2 \
  -movflags +faststart -y whatsapp_chat.mp4
```

Y para forzar un tamaño exacto (por ejemplo, que quepa en 12 MB), calcula el bitrate:

```
bitrate_total (kbps) = (peso_objetivo_MB × 8192) ÷ duración_en_segundos
bitrate_video = bitrate_total − 96   (lo que se lleva el audio)
```

Para 12 MB en 20 segundos: `(12 × 8192) ÷ 20 = 4915 kbps` total → **~4800 kbps de video**.

Comprueba el peso:

```bash
ls -la whatsapp_chat.mp4
# o, exacto en bytes:
ffprobe -v error -show_entries format=size -of csv=p=0 whatsapp_chat.mp4
```

### Qué formato sobrevive

| Elemento | Sobrevive | Se destruye |
|---|---|---|
| **Texto grande y grueso** | Sí | — |
| **Texto fino o pequeño** | — | Se convierte en papilla |
| **Colores planos y saturados** | Sí | — |
| **Degradados suaves** | — | Aparecen bandas |
| **Planos con poco movimiento** | Sí | — |
| **Planos con mucho movimiento y grano** | — | Bloques por todos lados |
| **Escenas oscuras de bar** | — | **Lo peor de todo.** Sube exposición antes de comprimir |
| **Contraste alto** | Sí | — |

**La consecuencia práctica más importante: el texto de un video para WhatsApp tiene que ser más grande de
lo que crees.** El video se ve en una burbuja de ~250 px de ancho antes de que alguien lo toque. Si tu
texto ocupaba el 60 % del ancho en Reels, en WhatsApp tiene que ocupar el 80 %.

### La salida de emergencia: mandarlo como documento

Si necesitas mandar un video en calidad real, **envíalo como documento** (adjuntar → documento). Ahí
WhatsApp no lo comprime y el límite sube muchísimo (del orden de 2 GB).

Cuándo usarlo:
- Le mandas al diseñador o al socio el corte para aprobar.
- Un cliente de eventos quiere ver el video del salón en calidad.

Cuándo **no** usarlo:
- Para vender. Un documento no se reproduce solo, hay que descargarlo, y la mitad de la gente no lo hace.

---

## Estados de WhatsApp

- Duración: **hasta 90 segundos** por estado en versiones recientes (subió de 30 a 60 y luego a 90).
  Varía por versión; si tu app te corta a 60, es tu versión.
- Peso: **16 MB** por clip.
- Formato: **9:16, 1080x1920**.
- Se ve **a pantalla completa**, no en burbuja. Aquí sí puedes usar texto de tamaño normal.
- Zona segura: deja **200 px arriba** (barra de progreso y tu nombre) y **250 px abajo** (campo de
  responder).

El estado es la superficie más subestimada que tienes: te ve **gente que ya te dio el número**, o sea el
público más caliente que existe. Un video de estado con "hoy hay parrilla desde las 6" a las 4 de la tarde
tiene más efecto directo que un reel.

---

## Errores comunes

- **Usar el mismo video para el anuncio y para el chat.** Formatos, pesos y trabajos distintos.
- **Intentar vender todo en el creativo CTWA.** Solo tienes que conseguir el clic.
- **Que el anuncio prometa una cosa y el bot diga otra.** Se pierde la mitad de la gente ahí.
- **Mandar el video sin comprimir y dejar que WhatsApp lo haga.** Sale con bloques.
- **Insistir en 1080p para el chat.** 720p con más bitrate se ve mejor al mismo peso.
- **Texto del mismo tamaño que en Reels.** En la burbuja no se lee.
- **Escenas oscuras sin corregir.** La compresión de WhatsApp destroza las sombras. Levanta la exposición.
- **Mandar el video como documento para vender.** Nadie lo descarga.
- **Poner tu CTA escrito justo encima del botón "Enviar mensaje".** Dos llamados peleando.
- **No usar los estados.** Es tu público más caliente y es gratis.
- **Degradados y transiciones suaves.** Aparecen bandas horribles al comprimir.
- **Olvidar `+faststart`.** El video tarda más en empezar a reproducirse en el chat.

---

## Checklist

### Anuncio CTWA
- [ ] El video vende **la conversación**, no el producto completo.
- [ ] El CTA es **una acción concreta**: "escríbeme *hola* y te mando la carta".
- [ ] Lo que promete el video es **literalmente** el primer mensaje del bot.
- [ ] Formato **9:16 (1080x1920)** + versión **4:5** para feed.
- [ ] **400+ px libres abajo** (botón "Enviar mensaje" de Meta), y mi CTA no pelea con él.
- [ ] Hay **una cara** o señal de que hay alguien del otro lado.
- [ ] Aparece el **precio** o el filtro que evita conversaciones basura.

### Video para el chat
- [ ] **Pesa menos de 16 MB.** Lo verifiqué con `ffprobe`, no a ojo.
- [ ] Está a **720x1280** con bitrate alto, no a 1080p con bitrate bajo.
- [ ] El **texto ocupa el 80 % del ancho**, no el 60 %.
- [ ] Las **escenas oscuras están levantadas** antes de comprimir.
- [ ] **Sin degradados suaves** ni transiciones que generen bandas.
- [ ] Tiene `-movflags +faststart`.
- [ ] Lo **probé mandándomelo a mí mismo** y mirándolo en la burbuja, sin abrirlo.

### Estado
- [ ] Dura **menos de 90 s** (idealmente menos de 20).
- [ ] Pesa **menos de 16 MB**.
- [ ] **1080x1920**, con 200 px libres arriba y 250 abajo.
- [ ] Está publicado **a la hora en que sirve** (la parrilla de las 6, publicada a las 4).
