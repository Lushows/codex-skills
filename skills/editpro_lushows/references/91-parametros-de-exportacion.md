# 91 — Parámetros de exportación: qué significa cada bandera

> Vas a copiar comandos de ffmpeg toda tu vida. Este módulo existe para que sepas **qué estás copiando**,
> porque el día que algo salga raro, la respuesta está en uno de estos siete parámetros.

---

## El comando base, explicado pedazo por pedazo

Este es el comando de exportación que sirve para el 90% de lo que vas a entregar:

```bash
ffmpeg -i entrada.mov \
  -c:v libx264 \
  -crf 18 \
  -preset slow \
  -profile:v high -level 4.1 \
  -pix_fmt yuv420p \
  -g 60 -keyint_min 60 \
  -c:a aac -b:a 192k -ar 48000 \
  -movflags +faststart \
  salida.mp4
```

Ahora, línea por línea, qué hace cada cosa y cuándo cambiarla.

---

## `-crf` — el control de calidad (el más importante)

CRF significa *Constant Rate Factor*: **factor de calidad constante**. Le dices a ffmpeg "manténme esta
calidad" y él decide cuántos bits gastar en cada momento. En las escenas quietas gasta poco, en las
escenas con mucho movimiento gasta mucho. El resultado tiene calidad pareja de principio a fin.

**La escala va de 0 a 51 y es al revés de lo que uno espera: número más bajo = más calidad y más peso.**

| CRF (x264) | Qué es | Cuándo |
|---|---|---|
| 0 | Sin pérdida. Pesa una barbaridad | Nunca en la práctica |
| 14–16 | Indistinguible del original | Máster de entrega premium, comercial de TV |
| **17–18** | **Visualmente sin pérdida** | **El estándar de entrega. Empieza aquí** |
| 19–21 | Excelente, más liviano | Redes sociales, YouTube |
| 22–23 | Bueno (23 es el valor por defecto de x264) | Previsualizaciones, borradores |
| 24–28 | Se empiezan a ver bloques en degradados | WhatsApp, correos, cuando el peso manda |
| 29+ | Feo y visible | Solo si el archivo tiene que caber sí o sí |

**Regla práctica:** cada +6 en CRF **divide el peso aproximadamente a la mitad**. De CRF 18 a CRF 24 el
archivo pesa la mitad. De 18 a 30, la cuarta parte.

Ojo: **la escala CRF NO es la misma entre códecs.** CRF 18 en x264 no es CRF 18 en x265 ni en AV1.

| Códec | CRF equivalente a "calidad de entrega" |
|---|---|
| libx264 | 18 |
| libx265 | 22–24 |
| libsvtav1 | 28–32 |
| libvpx-vp9 | 30–32 (además necesita `-b:v 0`) |

---

## `-preset` — cuánto se esfuerza el codificador

El preset **no cambia la calidad objetivo**, cambia **cuánto tiempo se toma ffmpeg para lograrla**. Un
preset más lento encuentra mejores formas de comprimir, así que con el mismo CRF te da un archivo **más
liviano** con la misma calidad.

De más rápido a más lento:

`ultrafast` · `superfast` · `veryfast` · `faster` · `fast` · **`medium`** (por defecto) · `slow` ·
`slower` · `veryslow` · `placebo`

| Preset | Cuándo usarlo |
|---|---|
| `ultrafast` | Previsualización rápida, pruebas desechables, grabar pantalla en vivo |
| `veryfast` | Borradores para el cliente, revisiones |
| `medium` | Si tienes prisa y el resultado es final |
| **`slow`** | **Tu preset de entrega. La mejor relación tiempo/peso** |
| `veryslow` | Reels de pauta que van a correr semanas: vale la pena el archivo más liviano |
| `placebo` | Nunca. Tarda 3× más que `veryslow` para ganar 1% |

Entre `medium` y `slow` la diferencia de peso es aprox. 10–15%, y el tiempo se duplica. Entre `slow` y
`veryslow` ganas otro 5% y el tiempo se vuelve a duplicar. **Por eso `slow` es el punto dulce.**

---

## `-profile:v` y `-level` — hasta dónde puede llegar el archivo

Estos dos le dicen al reproductor "para abrir esto necesitas soportar hasta acá". Son **contratos de
compatibilidad**.

**Perfiles de H.264:**

| Perfil | Qué permite | Para qué |
|---|---|---|
| `baseline` | Lo mínimo. Sin fotogramas B, sin CABAC | Aparatos muy viejos, WhatsApp conservador |
| `main` | Intermedio | Televisores viejos |
| **`high`** | **Todo lo moderno. Comprime mejor** | **Todo. Es tu opción por defecto en 2026** |

Usar `baseline` en 2026 te cuesta **10–15% más de peso** con la misma calidad. Solo úsalo si el destino es
un aparato prehistórico.

**Nivel (`-level`):** define resolución y bitrate máximos.

| Nivel | Aguanta hasta |
|---|---|
| 3.1 | 720p a 30 fps |
| 4.0 | 1080p a 30 fps |
| **4.1** | **1080p a 30 fps con bitrate alto — el estándar seguro** |
| 4.2 | 1080p a 60 fps |
| 5.1 | 4K a 30 fps |
| 5.2 | 4K a 60 fps |

Si exportas 1080p60 con `-level 4.1`, ffmpeg te va a advertir y algunos reproductores viejos van a
rechazar el archivo. Sube a 4.2.

---

## `-pix_fmt yuv420p` — el parámetro que evita el video verde

**Este es el que más problemas silenciosos causa. Ponlo siempre.**

El formato de píxel define cómo se guarda el color. `yuv420p` significa: color en 8 bits, con **submuestreo
de croma 4:2:0** — o sea, guarda el detalle de brillo completo pero el color a la mitad de resolución.
Suena a pérdida, y lo es, pero el ojo humano casi no lo nota y **es lo único que todos los reproductores
del planeta entienden**.

Qué pasa si NO lo pones:

- Si tu fuente es ProRes (que es `yuv422p10le`), ffmpeg puede exportar en 4:2:2 de 10 bits.
- Ese archivo se ve perfecto en tu computador.
- Y en Safari, en QuickTime viejo, en algunos Android y en varios reproductores web **sale verde, negro,
  o simplemente no abre**.

Es un fallo que no ves porque en tu máquina funciona. Por eso: **`-pix_fmt yuv420p` en toda exportación de
entrega, siempre, sin pensarlo.**

Otros formatos que vas a encontrar:

| Formato | Qué es | Cuándo |
|---|---|---|
| **`yuv420p`** | 8 bits, 4:2:0 | **Toda entrega. Siempre** |
| `yuv420p10le` | 10 bits, 4:2:0 | HDR, HEVC/AV1 de alta calidad |
| `yuv422p10le` | 10 bits, 4:2:2 | Másters ProRes |
| `yuva444p10le` | Con canal alfa | Logos animados con transparencia |

**Trampa de resolución impar:** yuv420p exige que ancho y alto sean **pares**. Si recortaste a 1079 px de
ancho, ffmpeg falla con "width not divisible by 2". Se arregla así:

```bash
-vf "scale=trunc(iw/2)*2:trunc(ih/2)*2"
```

---

## `-movflags +faststart` — para que el video arranque de una

Un `.mp4` tiene un índice llamado **moov atom** que dice dónde está cada fotograma. Por defecto ffmpeg lo
escribe **al final del archivo**, porque hasta que no termina no sabe el resultado.

Consecuencia: si ese video está en una página web, el navegador tiene que **descargar el archivo entero**
antes de mostrar el primer fotograma. Un video de 200 MB = espera eterna.

`+faststart` hace una segunda pasada al final y **mueve el índice al principio**. El video empieza a
reproducirse mientras se descarga.

- Cuesta unos segundos extra de exportación.
- **Ponlo siempre en cualquier `.mp4` que vaya a la web, a un cliente, o a una plataforma.**
- No aplica a `.mov` de ProRes ni a `.mkv`.

---

## `-g` y `-keyint_min` — cada cuánto hay un fotograma completo

Un video comprimido no guarda todos los fotogramas completos. Guarda algunos completos (**fotogramas
clave** o *keyframes*) y el resto son "diferencias" respecto al anterior. Al conjunto entre dos fotogramas
clave se le llama **GOP** (*Group of Pictures*).

`-g 60` significa: un fotograma clave cada 60 fotogramas. A 30 fps, eso es **uno cada 2 segundos**.

Por qué te importa:

- **GOP corto (1–2 s):** el usuario puede saltar en la línea de tiempo con precisión, y las plataformas
  recomprimen mejor. Pesa un poco más.
- **GOP largo (5–10 s):** archivo más liviano, pero saltar en el video es impreciso y la recompresión de
  la plataforma sufre.

**Recomendación práctica:** `-g` igual a **2 segundos** de fotogramas.

| fps | `-g` recomendado |
|---|---|
| 24 | 48 |
| 25 | 50 |
| 30 | 60 |
| 60 | 120 |

Añadir `-keyint_min` con el mismo valor evita que x264 meta fotogramas clave extra en cada corte de escena,
lo que hace el GOP impredecible.

Para plataformas exigentes (Meta Ads, algunos reproductores adaptativos) se usa además `-sc_threshold 0`
para forzar un GOP **exactamente** regular.

---

## CRF vs bitrate objetivo: cuándo usar cada uno

Hay dos formas de controlar el peso. **CRF fija la calidad y deja variar el peso. El bitrate fija el peso
y deja variar la calidad.**

**Usa CRF (casi siempre):**
```bash
-c:v libx264 -crf 18 -preset slow
```
El resultado tiene calidad pareja. No sabes de antemano cuánto va a pesar.

**Usa bitrate objetivo cuando el archivo tiene que caber en un tamaño exacto** (WhatsApp 16 MB, un límite
de plataforma, streaming). Y si lo haces, **hazlo en dos pasadas**, porque una sola pasada con bitrate fijo
da resultados feos: el codificador no sabe qué viene y reparte mal.

```bash
# Pasada 1 — analiza y escribe estadísticas
ffmpeg -y -i entrada.mov -c:v libx264 -b:v 5000k -preset slow \
  -pass 1 -an -f mp4 /dev/null

# Pasada 2 — codifica de verdad usando lo aprendido
ffmpeg -i entrada.mov -c:v libx264 -b:v 5000k -preset slow \
  -pass 2 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart salida.mp4
```

En Windows, cambia `/dev/null` por `NUL`.

**Fórmula para calcular el bitrate cuando tienes un tamaño objetivo:**

```
bitrate_total_kbps = (tamaño_objetivo_MB × 8192) / duración_segundos
bitrate_video_kbps = bitrate_total_kbps − bitrate_audio_kbps
```

Ejemplo: un video de 45 s que debe pesar máximo 15 MB, con audio a 128 kbps:

```
(15 × 8192) / 45 = 2730 kbps totales
2730 − 128 = 2602 kbps de video → redondea a 2500k por seguridad
```

**Híbrido inteligente — CRF con techo de bitrate** (lo mejor de los dos mundos, y lo que quieren las
plataformas de streaming):

```bash
ffmpeg -i entrada.mov -c:v libx264 -crf 20 -preset slow \
  -maxrate 8000k -bufsize 16000k \
  -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart salida.mp4
```

Esto dice: "dame calidad CRF 20, pero **nunca** pases de 8000 kbps". El `bufsize` normalmente se pone al
**doble** del `maxrate`.

---

## Parámetros de audio

```bash
-c:a aac -b:a 192k -ar 48000 -ac 2
```

| Bandera | Qué hace | Valor recomendado |
|---|---|---|
| `-c:a` | Códec de audio | `aac` para entrega |
| `-b:a` | Bitrate de audio | 128k voz sola · **192k voz + música** · 256k música protagonista |
| `-ar` | Frecuencia de muestreo | **48000** siempre en video |
| `-ac` | Canales | `2` (estéreo). `1` si es voz sola y quieres ahorrar |

Si tu voz quedó en un solo canal (un lado mudo), esto lo arregla duplicando el canal bueno:

```bash
-af "pan=stereo|c0=c0|c1=c0"
```

---

## Comandos listos para copiar

**Entrega estándar 1080p (el que más vas a usar):**
```bash
ffmpeg -i master.mov -c:v libx264 -crf 18 -preset slow -profile:v high -level 4.1 \
  -pix_fmt yuv420p -g 60 -keyint_min 60 -c:a aac -b:a 192k -ar 48000 \
  -movflags +faststart entrega_1080p.mp4
```

**Reel vertical para redes:**
```bash
ffmpeg -i master.mov -vf "scale=1080:1920:force_original_aspect_ratio=decrease,\
pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black,setsar=1" \
  -c:v libx264 -crf 20 -preset slow -profile:v high -level 4.1 \
  -pix_fmt yuv420p -r 30 -g 60 -keyint_min 60 -sc_threshold 0 \
  -c:a aac -b:a 128k -ar 48000 -movflags +faststart reel.mp4
```

**Borrador rápido para revisión (con marca de agua de tiempo):**
```bash
ffmpeg -i master.mov -vf "scale=854:-2,drawtext=text='%{pts\\:hms}':\
fontcolor=white:fontsize=24:box=1:boxcolor=black@0.6:x=10:y=10" \
  -c:v libx264 -crf 26 -preset veryfast -pix_fmt yuv420p \
  -c:a aac -b:a 96k borrador_v1.mp4
```

**Para WhatsApp (que cabe en 16 MB):**
```bash
ffmpeg -i master.mov -vf "scale=-2:720" -c:v libx264 -crf 26 -preset slow \
  -profile:v main -level 3.1 -pix_fmt yuv420p -maxrate 2000k -bufsize 4000k \
  -c:a aac -b:a 96k -ar 48000 -movflags +faststart whatsapp.mp4
```

---

## Errores comunes

1. **Olvidar `-pix_fmt yuv420p`.** El video se ve bien en tu máquina y verde/negro en la del cliente. Es
   el error #1 y no te enteras hasta que alguien se queja.
2. **Olvidar `-movflags +faststart` en video para web.** El video "no carga" cuando en realidad está
   descargando 200 MB antes de mostrar el primer fotograma.
3. **Creer que un CRF sirve para todos los códecs.** CRF 18 en x264 ≈ CRF 23 en x265 ≈ CRF 30 en AV1.
   Copiar el número entre códecs da resultados absurdos.
4. **Usar bitrate fijo en una sola pasada.** Las escenas con movimiento se pixelan y las quietas
   desperdician bits. Si vas por bitrate, dos pasadas.
5. **Poner `-preset placebo` creyendo que "es lo mejor".** Triplica el tiempo para ganar 1%. `slow` es la
   respuesta.
6. **Exportar con `-level 4.1` a 60 fps.** El nivel no aguanta; sube a 4.2 o el archivo será rechazado.
7. **Exportar a resolución impar.** yuv420p exige números pares. Recorta con `trunc(iw/2)*2`.
8. **Dejar el audio en 44,1 kHz.** Fuente de desincronización lenta. `-ar 48000` siempre.
9. **Poner CRF 28 "para que pese poco" en un video con degradados o cielo.** Los degradados son lo primero
   que se rompe en bloques. Si hay degradados, no bajes de CRF 20.
10. **Reexportar sobre un archivo ya exportado.** Cada pasada de H.264 pierde calidad. Siempre exporta
    desde el máster o desde el proyecto, nunca desde la entrega anterior.
11. **No poner `-g`.** Dejas el GOP a criterio del codificador y las plataformas recomprimen peor.
12. **Perder los archivos de estadísticas de dos pasadas** (`ffmpeg2pass-*.log`) entre pasada 1 y 2. La
    pasada 2 falla o queda igual que una sola pasada.

---

## Checklist

Antes de dar por buena una exportación:

- [ ] `-c:v libx264` (o el códec correcto para el destino, ver módulo 90)
- [ ] `-crf` elegido según destino, y sé que la escala depende del códec
- [ ] `-preset slow` si es entrega final, `veryfast` si es borrador
- [ ] `-profile:v high` y `-level` acorde a resolución y fps
- [ ] **`-pix_fmt yuv420p` presente** (el no-negociable)
- [ ] `-movflags +faststart` si el archivo va a la web o al cliente
- [ ] `-g` = 2 segundos de fotogramas, con `-keyint_min` igual
- [ ] Audio en **AAC 48 kHz**, bitrate acorde al contenido
- [ ] Ancho y alto son **números pares**
- [ ] Si usé bitrate objetivo, lo hice **en dos pasadas**
- [ ] Corrí `ffprobe` sobre el resultado y confirmé resolución, fps, códec y duración
- [ ] Abrí el archivo final en un aparato distinto al mío antes de entregarlo
