# 99 — Entrega al cliente: cómo se cierra bien un trabajo

> El trabajo no termina cuando el video queda bien. Termina cuando el cliente **puede usarlo sin
> preguntarte nada**. Todo lo que quede entre esas dos cosas —una duda, un archivo que no abre, un
> "¿cuál era el bueno?"— es trabajo tuyo que todavía no cobraste.

---

## Qué se entrega (y qué casi nadie entrega)

Un cliente que recibe un `.mp4` recibió un archivo. Un cliente que recibe un **paquete de entrega** recibió
un servicio. La diferencia es lo que te hace volver a contratar.

### Lo mínimo indispensable

| Entregable | Formato | Por qué |
|---|---|---|
| **Video final por plataforma** | `.mp4` H.264 High, yuv420p, faststart | Lo que va a publicar |
| **Portada / miniatura** | `.jpg` a las dimensiones de cada plataforma | Para que no la escoja el algoritmo |
| **Archivo de subtítulos** | `.srt` | Para YouTube y para traducción |
| **Nota de entrega** | `.txt` o `.pdf` | Qué es cada archivo y qué hacer con él |

### Lo que eleva la entrega

| Entregable | Formato | Por qué |
|---|---|---|
| **Máster de alta calidad** | `.mov` ProRes 422 HQ | Para que cualquiera pueda reeditar sin recomprimir |
| **Versión sin subtítulos quemados** | `.mp4` | Para traducir o resubtitular después |
| **Versiones alternas de relación de aspecto** | 9:16 / 4:5 / 1:1 | Para pauta y para otras ubicaciones |
| **Variantes de gancho** | 3 archivos | Si va a pauta, esto vale plata |
| **Texto sugerido para publicar** | `.txt` | Descripción, hashtags, capítulos |
| **Proyecto editable** | Ver más abajo | El diferenciador real |

---

## Entregar el proyecto editable: lo que casi nadie hace

**Entrega el proyecto, no solo el video.** Suena contraintuitivo —"si le doy el proyecto, no me vuelve a
necesitar"— y es exactamente al revés.

Por qué conviene:

1. **El cliente se siente dueño de lo que pagó.** Bajas su ansiedad de depender de ti.
2. **Te posiciona como profesional, no como freelance defensivo.** Los estudios grandes entregan proyecto.
3. **Casi nadie lo va a abrir.** Los clientes no editan. Pero saber que lo tienen vale mucho.
4. **Cuando vuelvan a ti** —y vuelven— el proyecto está limpio y organizado, y eso también habla de ti.
5. **Te protege.** Si el cliente se va con otro editor, ese editor abre tu proyecto y ve trabajo ordenado.
   Eso es reputación gratis.

Lo que se entrega como "proyecto editable" depende del editor:

| Editor | Cómo se empaqueta |
|---|---|
| **DaVinci Resolve** | `File → Export Project Archive (.dra)` — incluye medios. O `.drp` sin medios |
| **Premiere Pro** | `File → Project Manager → Collect Files and Copy` |
| **Final Cut Pro** | Library consolidada, o `XML` para intercambio |
| **CapCut** | Carpeta del proyecto (`draft_content.json` + medios) |
| **Intercambio universal** | **XML/AAF/EDL** + carpeta de medios |

**La opción a prueba de todo:** exporta un **XML** (o EDL) más la carpeta de medios usados. Cualquier
editor moderno puede importarlo. Si el cliente usa otro software, ese XML es lo único que le va a servir.

**Y si no vas a entregar el proyecto**, dilo desde el principio en la cotización. Lo que no se puede es
dejarlo ambiguo y descubrirlo peleando.

---

## La estructura del paquete de entrega

```
GastroLatam_Calculadora_Reel01_ENTREGA_2026-08-04/
│
├── LEEME.txt                      ← lo primero que se abre
│
├── 1_PUBLICAR/                    ← lo que sube a redes, listo
│   ├── instagram_reel_1080x1920.mp4
│   ├── instagram_feed_1080x1350.mp4
│   ├── tiktok_1080x1920.mp4
│   ├── youtube_shorts_1080x1920.mp4
│   ├── whatsapp_720x1280.mp4
│   └── portadas/
│       ├── portada_reel_1080x1920.jpg
│       └── miniatura_youtube_1280x720.jpg
│
├── 2_TEXTOS/
│   ├── subtitulos.srt
│   ├── descripcion_sugerida.txt
│   └── transcripcion.txt
│
├── 3_MASTER/                      ← para reeditar o rehacer versiones
│   ├── master_prores422hq.mov
│   └── master_sin_subtitulos.mp4
│
└── 4_PROYECTO/                    ← el editable
    ├── proyecto.drp  (o .prproj / .xml)
    ├── medios/
    └── LICENCIAS.txt
```

**Las carpetas numeradas** hacen que el cliente entre por el sitio correcto. `1_PUBLICAR` es lo que
necesita hoy; el resto es para después.

**Regla clave:** si el cliente solo abre `1_PUBLICAR` y el `LEEME.txt`, ya tiene todo lo que necesita para
publicar. Todo lo demás es respaldo.

---

## El LEEME.txt: el documento que evita 10 mensajes

Este archivo es el 5% del trabajo que se lleva el 50% de la percepción de profesionalismo.

```
═══════════════════════════════════════════════════════════
  GASTROLATAM — CALCULADORA DE COSTOS — REEL 01
  Entrega final · 4 de agosto de 2026 · versión v05
═══════════════════════════════════════════════════════════

QUÉ ES ESTO
Un reel de 34 segundos para promocionar la Calculadora de Costos
Gastronómicos, con el gancho "tu plato estrella te está quebrando".


QUÉ SUBIR Y DÓNDE
──────────────────────────────────────────────────────────
Instagram Reels ....... 1_PUBLICAR/instagram_reel_1080x1920.mp4
Instagram Feed ........ 1_PUBLICAR/instagram_feed_1080x1350.mp4
TikTok ................ 1_PUBLICAR/tiktok_1080x1920.mp4
YouTube Shorts ........ 1_PUBLICAR/youtube_shorts_1080x1920.mp4
WhatsApp / Estado ..... 1_PUBLICAR/whatsapp_720x1280.mp4

Los subtítulos ya están QUEMADOS en el video: se ven siempre,
sin que el usuario tenga que activarlos.


LA PORTADA — IMPORTANTE
──────────────────────────────────────────────────────────
Al subir a Instagram o TikTok, la app te va a ofrecer escoger
la portada. NO dejes la que sale por defecto.

Sube manualmente:  1_PUBLICAR/portadas/portada_reel_1080x1920.jpg

Si dejas la automática, la app suele escoger un fotograma con
los ojos cerrados y el reel rinde mucho menos.


TEXTO SUGERIDO PARA LA PUBLICACIÓN
──────────────────────────────────────────────────────────
Está en 2_TEXTOS/descripcion_sugerida.txt
Incluye descripción, hashtags y llamada a la acción.


SI ALGUIEN NECESITA REEDITAR
──────────────────────────────────────────────────────────
3_MASTER/master_prores422hq.mov
   Máster en alta calidad. Es el archivo del que salieron todas
   las versiones. Úsalo si hay que hacer cortes nuevos.

3_MASTER/master_sin_subtitulos.mp4
   La misma edición sin los subtítulos quemados, por si hay que
   traducir el video a otro idioma.

4_PROYECTO/
   El proyecto editable completo (DaVinci Resolve 20).
   Cualquier editor puede abrirlo o importar el XML.


ESPECIFICACIONES TÉCNICAS
──────────────────────────────────────────────────────────
Duración:        34,2 segundos
Video:           H.264 High, 1080x1920, 30 fps, yuv420p
Audio:           AAC 128 kbps, 48 kHz, estéreo, −14,2 LUFS
Verificación:    corrida y limpia (transcripción completa,
                 sin cortes en palabra, final completo)


MÚSICA Y LICENCIAS
──────────────────────────────────────────────────────────
Pista: "Nombre de la pista" — Epidemic Sound
Licencia: ID 8842-XXXX, vigente hasta 2027-03-15
Cubre: redes sociales orgánicas y pauta.
NO cubre: televisión abierta ni cine.

Detalle completo en 4_PROYECTO/LICENCIAS.txt


SI ALGO NO ABRE
──────────────────────────────────────────────────────────
Todos los .mp4 están en H.264, el formato más compatible que
existe: abren en cualquier celular, computador o navegador.

El archivo .mov de la carpeta 3_MASTER es ProRes: es un formato
profesional de alta calidad y puede no abrir en un computador
sin software de edición. Es normal y es a propósito.


═══════════════════════════════════════════════════════════
Cualquier duda: [tu contacto]
═══════════════════════════════════════════════════════════
```

**Fíjate en tres cosas de ese documento:**

1. Le dice **exactamente qué archivo va a cada plataforma**. Cero ambigüedad.
2. Le **advierte del error que va a cometer** (dejar la portada automática) antes de que lo cometa.
3. Le explica **por qué un archivo puede no abrir** antes de que te escriba preocupado.

Ese tercer punto solo ya evita el mensaje de "oye, el .mov no me abre" que llega el sábado a las 9 de la
noche.

---

## Cómo mandar los archivos

| Peso total | Método | Notas |
|---|---|---|
| < 25 MB | Correo | Solo para un video suelto |
| < 2 GB | **WeTransfer / Drive / Dropbox** | Lo estándar. Enlace con vencimiento |
| 2–50 GB | Drive, Dropbox, o **carpeta compartida permanente** | Mejor una carpeta que un enlace temporal |
| > 50 GB | **Disco físico** | Sí, en 2026 sigue siendo lo más rápido |

**Recomendación práctica:** entrega en una **carpeta compartida permanente** (Drive o Dropbox), no en un
enlace de WeTransfer que vence en 7 días. Razones:

- El cliente vuelve a buscarlo en tres meses y sigue ahí
- No tienes que reenviar nada
- Puedes agregar versiones nuevas en la misma carpeta

**Comprime el paquete si vas a mandar un enlace:**
```bash
zip -r GastroLatam_Reel01_ENTREGA_2026-08-04.zip GastroLatam_Reel01_ENTREGA_2026-08-04/
```
Un solo `.zip` se descarga completo o no se descarga; 40 archivos sueltos se descargan a medias y el
cliente no se entera.

**Verifica que el ZIP no llegó corrupto** (pasa más de lo que crees en enlaces grandes):
```bash
# Genera la huella y mándasela en el mensaje
sha256sum GastroLatam_Reel01_ENTREGA_2026-08-04.zip
```

---

## Mensaje de entrega

El paquete es la mitad. El mensaje con que lo entregas es la otra mitad. Corto, claro y con la acción
adelante:

> Hola Luis, acá está el reel terminado 👇
>
> **[enlace]**
>
> Lo que necesitas para publicar hoy está en la carpeta `1_PUBLICAR`. Hay una versión ya lista para cada
> plataforma: Instagram, TikTok, Shorts y WhatsApp.
>
> **Dos cosas importantes:**
> 1. Al subirlo, escoge la portada manualmente (está en `1_PUBLICAR/portadas/`). Si dejas la automática, la
>    app suele agarrar un fotograma malo.
> 2. En `2_TEXTOS/` te dejé la descripción sugerida con hashtags, por si te sirve.
>
> El `LEEME.txt` explica qué es cada archivo. También va el máster en alta calidad y el proyecto editable,
> por si en el futuro alguien necesita reeditarlo.
>
> El video quedó en 34 segundos. Ya está verificado: audio limpio, sin cortes en palabra, subtítulos dentro
> de zona segura.
>
> Cualquier cosa me dices.

Qué hace bien ese mensaje:
- El enlace arriba, no enterrado
- Le dice **qué hacer ahora** en una línea
- Advierte del error de la portada
- Menciona el máster y el proyecto **sin hacer un problema de ello**
- Cierra con la verificación: le comunica que hubo control de calidad, sin tecnicismos

---

## Qué NO hacer al entregar

- **No mandes 12 archivos sueltos por WhatsApp.** Se comprimen, se pierden y quedan sin nombre.
- **No mandes el video por WhatsApp como archivo de chat.** WhatsApp lo recomprime a papilla. Si tiene que
  ir por WhatsApp, mándalo **como documento** y avisa, o manda el enlace.
- **No entregues solo el enlace sin explicación.** "Acá está" no es una entrega.
- **No entregues sin verificar** (módulo 98). Entregar un video con una palabra partida es peor que
  entregar tarde.
- **No entregues un `.mov` ProRes como si fuera el archivo para publicar.** El cliente va a intentar
  subirlo y va a fallar o va a tardar dos horas.
- **No dejes la palabra "final" en ningún nombre de archivo.** Ver módulo 96.
- **No entregues con los metadatos GPS de la cámara adentro.** Estás repartiendo la dirección donde
  grabaste. `-map_metadata -1`.

---

## Generar el paquete completo con un script

```bash
#!/bin/bash
# entregar.sh — construye el paquete de entrega desde el máster
M="03_master/master_v05.mov"
D="ENTREGA_$(date +%Y-%m-%d)"

mkdir -p "$D"/{1_PUBLICAR/portadas,2_TEXTOS,3_MASTER,4_PROYECTO}

echo "→ Instagram Reels / TikTok / Shorts (9:16)"
ffmpeg -y -i "$M" -vf "scale=1080:1920,setsar=1" \
  -c:v libx264 -crf 19 -preset slow -profile:v high -level 4.1 \
  -pix_fmt yuv420p -r 30 -g 60 -keyint_min 60 \
  -c:a aac -b:a 128k -ar 48000 -movflags +faststart -map_metadata -1 \
  "$D/1_PUBLICAR/instagram_reel_1080x1920.mp4" -loglevel error

cp "$D/1_PUBLICAR/instagram_reel_1080x1920.mp4" "$D/1_PUBLICAR/tiktok_1080x1920.mp4"
cp "$D/1_PUBLICAR/instagram_reel_1080x1920.mp4" "$D/1_PUBLICAR/youtube_shorts_1080x1920.mp4"

echo "→ Instagram Feed (4:5)"
ffmpeg -y -i "$M" -vf "crop=ih*4/5:ih,scale=1080:1350,setsar=1" \
  -c:v libx264 -crf 19 -preset slow -profile:v high -pix_fmt yuv420p -r 30 \
  -c:a aac -b:a 128k -movflags +faststart -map_metadata -1 \
  "$D/1_PUBLICAR/instagram_feed_1080x1350.mp4" -loglevel error

echo "→ WhatsApp (bajo 16 MB)"
ffmpeg -y -i "$M" -vf "scale=-2:1280" \
  -c:v libx264 -b:v 1800k -maxrate 2000k -bufsize 4000k -preset slow \
  -profile:v main -level 3.1 -pix_fmt yuv420p \
  -c:a aac -b:a 96k -ar 48000 -movflags +faststart -map_metadata -1 \
  "$D/1_PUBLICAR/whatsapp_720x1280.mp4" -loglevel error

echo "→ Portadas"
ffmpeg -y -ss 00:00:04.2 -i "$M" -frames:v 1 -vf "scale=1080:1920" -q:v 2 \
  "$D/1_PUBLICAR/portadas/portada_reel_1080x1920.jpg" -loglevel error
ffmpeg -y -ss 00:00:04.2 -i "$M" -frames:v 1 -vf "scale=1280:720" -q:v 2 \
  "$D/1_PUBLICAR/portadas/miniatura_youtube_1280x720.jpg" -loglevel error

echo "→ Máster"
cp "$M" "$D/3_MASTER/master_prores422hq.mov"
cp 02_textos/subtitulos.srt "$D/2_TEXTOS/" 2>/dev/null

echo "→ Verificación final del paquete"
for f in "$D"/1_PUBLICAR/*.mp4; do
  err=$(ffmpeg -v error -i "$f" -f null - 2>&1 | head -2)
  sz=$(du -h "$f" | cut -f1)
  a=$(ffprobe -v error -select_streams a -show_entries stream=codec_name -of csv=p=0 "$f")
  px=$(ffprobe -v error -select_streams v -show_entries stream=pix_fmt -of csv=p=0 "$f")
  if [ -n "$err" ]; then echo "  ❌ $(basename $f): $err"
  elif [ -z "$a" ]; then echo "  ❌ $(basename $f): SIN AUDIO"
  elif [ "$px" != "yuv420p" ]; then echo "  ❌ $(basename $f): pix_fmt=$px"
  else echo "  ✅ $(basename $f) — $sz"; fi
done

echo -e "\n→ Ahora escribe el LEEME.txt en $D/ y empaqueta."
```

Fíjate que el script **verifica cada archivo antes de dar el paquete por hecho**: integridad, presencia de
audio y `pix_fmt`. Los tres fallos que más se cuelan.

---

## Después de entregar

**Pide confirmación de que descargó y abrió.** No "¿te gustó?", sino:

> "¿Pudiste bajar todo bien y abrir los archivos?"

Es una pregunta cerrada que te confirma que la entrega llegó completa. Si algo se corrompió en la descarga,
te enteras hoy y no en tres días cuando el cliente iba a publicar.

**Consigue la aprobación por escrito.** Un "quedó perfecto, gracias" por WhatsApp basta, pero **anótalo con
fecha y hora en tu registro de versiones** (módulo 96). El día que alguien diga "yo nunca aprobé eso",
tienes el dato.

**Y después de que publiquen, pide los números.** Retención a 3 segundos, tasa de finalización, guardados.
No para presumir: **para saber qué funcionó y hacerlo otra vez.** Es la única forma de que tu edición
mejore con datos en vez de con gusto.

---

## Errores comunes

1. **Entregar solo un `.mp4` sin contexto.** El cliente no sabe cuál subir dónde y te escribe cuatro veces.
2. **No entregar la portada.** El cliente deja la automática, el reel rinde la mitad, y el trabajo se ve
   peor de lo que fue.
3. **Entregar el ProRes como si fuera el archivo para publicar.** No abre en su computador o tarda una
   eternidad en subir.
4. **Mandar los videos por WhatsApp como archivo de chat.** Se destruyen y el cliente publica la papilla.
5. **Usar un enlace de WeTransfer que vence en 7 días.** A los dos meses el cliente pide todo de nuevo.
6. **No incluir el `.srt`.** El cliente pierde la indexación de YouTube y la traducción automática.
7. **No documentar la licencia de la música.** El día que llega un reclamo de derechos, no hay respaldo.
8. **Entregar sin correr la verificación del módulo 98.** Entregar rápido y roto es peor que entregar bien
   y un día después.
9. **Entregar con metadatos GPS de la cámara.** Repartes la ubicación donde grabaste.
10. **No entregar el proyecto editable ni aclarar que no se entrega.** Ambigüedad que se convierte en
    conflicto.
11. **Nombres de archivo genéricos** (`video1.mp4`, `final.mp4`). El cliente no distingue cuál es cuál.
12. **No pedir confirmación de descarga.** Los archivos grandes se corrompen y nadie se entera hasta el día
    de publicar.
13. **Entregar el paquete sin verificar `pix_fmt` de cada archivo.** Un solo archivo sin `yuv420p` es un
    video verde en el celular del cliente.
14. **No pedir los números después de publicar.** Es el único aprendizaje real que sale del proyecto.

---

## Checklist

Antes de mandar el enlace de entrega:

- [ ] La **verificación del módulo 98** está corrida y limpia sobre el corte final
- [ ] Hay una **versión por plataforma** de destino, cada una con sus specs correctas
- [ ] Cada archivo verificado: **sin errores, con audio, `pix_fmt=yuv420p`, faststart**
- [ ] El de WhatsApp **pesa menos de 16 MB**
- [ ] **Portada y miniatura** incluidas, a las dimensiones de cada plataforma
- [ ] **`.srt` de subtítulos** incluido
- [ ] **Máster** (ProRes) incluido, en su carpeta y claramente identificado
- [ ] **Versión sin subtítulos quemados** incluida
- [ ] **Proyecto editable** incluido (o explicitado que no va, desde la cotización)
- [ ] **`LEEME.txt`** escrito: qué sube dónde, la advertencia de la portada, specs, licencias, qué hacer si
      algo no abre
- [ ] **Texto sugerido** para la publicación incluido
- [ ] **Licencia de la música** documentada con vigencia y alcance
- [ ] **Metadatos GPS eliminados** de todos los archivos (`-map_metadata -1`)
- [ ] Ningún nombre de archivo dice **"final"**; todos son descriptivos y en minúsculas
- [ ] Carpetas numeradas `1_PUBLICAR` … `4_PROYECTO` para que entre por el sitio correcto
- [ ] Entregado en **carpeta permanente**, no en un enlace que vence
- [ ] Mensaje de entrega escrito: enlace arriba, qué hacer ahora, la advertencia de la portada
- [ ] **Confirmación de descarga** pedida al cliente
- [ ] **Aprobación anotada** con fecha, hora y medio en el registro de versiones
- [ ] Recordatorio puesto para **pedir los números** una semana después de publicar
