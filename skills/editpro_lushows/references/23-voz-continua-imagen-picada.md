# 23 — Voz continua, imagen picada

**Qué resuelve:** el conflicto central del video corto. Necesitas que la imagen cambie cada 1,5–2 segundos
(módulo `20`), pero cada vez que cortas se te parte una palabra y el video suena a robot. Esta técnica
resuelve las dos cosas al tiempo: **la imagen cambia tres veces en siete segundos y ningún corte toca
una sílaba.**

Es la técnica más importante de todo el bloque de ritmo. Si solo aprendes una cosa de esta skill, que
sea esta.

---

## 1. El problema, dicho claro

Cuando editas "normal", cortas audio e imagen juntos:

```
Corte en el segundo 4,0
IMAGEN:  [ ——— plano A ——— | ——— plano B ——— ]
AUDIO:   [ ——— audio A ——— | ——— audio B ——— ]
                            ↑
                  aquí la palabra "restauran-|-te" se partió
```

Resultado: cada corte se oye. El video se siente entrecortado, la voz suena artificial, y el espectador
percibe "esto está mal editado" aunque no sepa explicar por qué.

La reacción intuitiva es cortar menos. Y ahí pierdes el pulso y pierdes la retención. Callejón sin
salida.

---

## 2. La solución: dos pistas independientes

La técnica se llama **voz continua, imagen picada** y el principio es simple:

> **Se extrae el audio del bloque COMPLETO y sin cortar. Aparte, se construye la pista de imagen en
> pedazos. Al final se le pega el audio encima.**

```
IMAGEN:  [ plano A ][ inserto ][ punch-in ][ plano A ]   ← 4 pedazos, 4 cambios
AUDIO:   [ ————————— la misma voz, nunca cortada ————————— ]
```

La voz **no sabe** que la imagen cambió. Sigue siendo la grabación original, con su respiración natural,
su entonación intacta y sin un solo empalme.

Esto no es un truco: es cómo se edita el documental y la publicidad desde siempre. Lo que cambia en 2026
es que ahora lo necesitas en un reel de 20 segundos.

---

## 3. El flujo completo, paso a paso

Ejemplo real: una toma de 7 segundos donde alguien dice una frase de venta, y quieres que la imagen
cambie 3 veces.

### Paso 0 — Conocer el material

Nunca cortes lo que no has medido.

```bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 toma.mp4
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate \
  -of default=noprint_wrappers=1 toma.mp4
```

Si el clip dura 6,8 s y le pides un tramo hasta 7,2 s, ffmpeg no falla: te devuelve un archivo corto y
todo el montaje se te descuadra después. Mide primero.

### Paso 1 — Extraer el audio COMPLETO del bloque

Este es el paso que define la técnica. El audio sale entero, del inicio al fin del bloque, sin ningún
corte.

```bash
ffmpeg -hide_banner -y -ss 12.0 -to 19.0 -i toma.mp4 \
  -vn -c:a pcm_s16le -ar 48000 -ac 1 voz_bloque.wav
```

- `-vn` = sin video.
- `pcm_s16le` = WAV sin comprimir. Trabaja siempre en WAV en el proceso; el MP3/AAC se deja para el
  render final. Recodificar audio comprimido varias veces lo degrada.
- `-ar 48000` = 48 kHz, el estándar de video.
- `-ac 1` = mono. La voz va en mono; el estéreo es para la música.

Mide la duración exacta del audio, porque ese número manda sobre todo lo demás:

```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 voz_bloque.wav
# → 7.000000
```

**Ese 7,000 es tu presupuesto.** La suma de todos los pedazos de imagen tiene que dar exactamente eso.

### Paso 2 — Diseñar la pista de imagen en papel

Antes de tocar ffmpeg, escribe la tabla. Esto es el montaje:

| # | Duración | Qué se ve | Fuente |
|---|---|---|---|
| 1 | 0,0 – 2,3 s | Plano normal | `toma.mp4` desde 12,0 |
| 2 | 2,3 – 4,1 s | Inserto del producto | `broll_producto.mp4` desde 3,0 |
| 3 | 4,1 – 7,0 s | Punch-in 15% | `toma.mp4` desde 16,1 |

**Verificación aritmética obligatoria:**

```
2,3 + 1,8 + 2,9 = 7,0  ✅ cuadra con el audio
```

Si no cuadra, el audio se te va a desincronizar o te va a sobrar imagen negra al final. **Haz esta suma
siempre.** Es el error número uno de esta técnica.

Fíjate en el detalle del pedazo 3: empieza en el segundo **16,1** de la toma original, no en 12,0. ¿Por
qué? Porque el pedazo 1 usó de 12,0 a 14,3 y el pedazo 2 fue b-roll (1,8 s). Para que el movimiento
labial siga cuadrando con la voz, el pedazo 3 tiene que retomar la toma en `12,0 + 4,1 = 16,1`.

> **Esto es crítico:** cuando vuelves al plano de la persona hablando, tienes que retomarlo **en el punto
> donde iba la voz**, no donde lo dejaste. Si no, se le ve la boca diciendo otra cosa. Se llama
> **sincronía labial** y es lo que separa un montaje profesional de uno amateur.

Si el plano de vuelta NO es de la persona hablando (es b-roll, un gráfico, un producto), esta regla no
aplica: puedes poner lo que quieras.

### Paso 3 — Cortar los pedazos de imagen (sin audio)

Todos van **sin audio** (`-an`), a la misma resolución, mismo fps y mismo códec. Si no coinciden, el
`concat` de después falla o produce un archivo con saltos.

```bash
# Pedazo 1 — plano normal
ffmpeg -hide_banner -y -ss 12.0 -t 2.3 -i toma.mp4 \
  -an -vf "scale=1080:1920:flags=lanczos,fps=30,setsar=1" \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p v1.mp4

# Pedazo 2 — inserto de b-roll
ffmpeg -hide_banner -y -ss 3.0 -t 1.8 -i broll_producto.mp4 \
  -an -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1" \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p v2.mp4

# Pedazo 3 — punch-in 15% de la misma toma, retomando en 16.1
ffmpeg -hide_banner -y -ss 16.1 -t 2.9 -i toma.mp4 \
  -an -vf "scale=1242:2208:flags=lanczos,crop=1080:1920,fps=30,setsar=1" \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p v3.mp4
```

Los cuatro parámetros que **tienen que ser idénticos** en todos los pedazos:

| Parámetro | Valor del ejemplo | Por qué |
|---|---|---|
| Resolución | `1080x1920` | concat exige el mismo tamaño |
| fps | `fps=30` | mezclar 30 y 60 produce saltos |
| SAR | `setsar=1` | píxeles cuadrados; sin esto la imagen se deforma |
| pix_fmt | `yuv420p` | compatibilidad universal de reproducción |

Verifica que cada pedazo dure lo que pediste:

```bash
for f in v1.mp4 v2.mp4 v3.mp4; do
  echo -n "$f  "; ffprobe -v error -show_entries format=duration -of csv=p=0 "$f"
done
```

Si alguno sale corto, el clip fuente no tenía ese tramo. Corrige antes de seguir.

### Paso 4 — Unir la pista de imagen

```bash
printf "file 'v1.mp4'\nfile 'v2.mp4'\nfile 'v3.mp4'\n" > lista.txt
ffmpeg -hide_banner -y -f concat -safe 0 -i lista.txt -c copy imagen_sin_audio.mp4
```

> ⚠️ **Trampa de Windows.** Si generas `lista.txt` desde PowerShell con
> `Add-Content -Encoding utf8`, el archivo queda con **BOM** (tres bytes invisibles al inicio) y ffmpeg
> falla con un mensaje que no explica nada. Usa `printf` desde bash, o `-Encoding ascii` en PowerShell.
> Esta trampa cuesta media hora la primera vez.

Comprueba la duración de la imagen:

```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 imagen_sin_audio.mp4
# → debe dar ~7.000. Si da 6.87 o 7.13, corrige antes de pegar el audio.
```

Una diferencia de hasta ~0,03 s es tolerable (un fotograma). Más que eso, se va a notar en la sincronía
labial al final del bloque.

### Paso 5 — Pegar el audio continuo encima

El momento de la verdad:

```bash
ffmpeg -hide_banner -y -i imagen_sin_audio.mp4 -i voz_bloque.wav \
  -map 0:v:0 -map 1:a:0 \
  -c:v copy -c:a aac -b:a 192k \
  -shortest bloque_final.mp4
```

- `-map 0:v:0` = toma el video del primer archivo.
- `-map 1:a:0` = toma el audio del segundo.
- `-c:v copy` = no recodifica el video (ya está bien, y así no pierdes calidad).
- `-shortest` = corta cuando el más corto termine; es tu red de seguridad si la suma quedó con unas
  centésimas de desfase.

Listo. Tienes 7 segundos con 3 cambios visuales (pulso de 2,3 s) y la voz completamente intacta.

---

## 4. Verificación obligatoria

No entregues sin esto. Son tres comprobaciones y toman dos minutos.

### a) La palabra no se partió

Transcribe el resultado final y compáralo con el original. Si en la transcripción del resultado aparece
una palabra mocha o una sílaba suelta, algo se rompió. Como el audio nunca se cortó, esto **no debería
pasar** — pero se verifica igual, porque el error suele estar en el paso 1 (extrajiste el audio con un
`-ss` que cayó a mitad de palabra).

**El corte del bloque completo sí puede partir una palabra.** El inicio y el final del bloque son los
únicos puntos donde el audio se corta, y ahí sí hay que ser exacto.

### b) La sincronía labial se mantiene

Exporta fotogramas del final del bloque y compáralos con la forma de la boca esperada:

```bash
ffmpeg -hide_banner -ss 6.5 -i bloque_final.mp4 -frames:v 3 -vf fps=10 lipsync_%02d.png
```

Si la persona está con la boca cerrada mientras se oye una vocal abierta, retomaste el plano en el
segundo equivocado (paso 2).

### c) No hay silencio ni negro al final

```bash
ffmpeg -hide_banner -i bloque_final.mp4 -af "silencedetect=noise=-45dB:d=0.4" -f null - 2>&1 | grep silence
```

Si detecta silencio en el último segundo, la imagen quedó más larga que el audio. Vuelve al paso 2 y
arregla la suma.

---

## 5. Variante: cuando el audio es de otro lado

A veces la voz no viene de la toma. Viene de una grabadora aparte, de una locución hecha en otro
momento, o de un TTS. La técnica es la misma, con dos diferencias:

1. **El audio manda la duración**, no la imagen. Mides el WAV y armas la imagen para que sume eso.
2. **Nunca vuelves a un plano de alguien hablando**, porque no va a cuadrar. Toda la imagen es b-roll,
   insertos, gráficos o planos donde no se ve la boca.

```bash
# Duración del audio locutado
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 locucion.wav)
echo "Presupuesto de imagen: $DUR s"
```

Y desde ahí repartes. Con 18,4 s de locución y objetivo de pulso 1,8 s: `18,4 / 1,8 ≈ 10 pedazos`.

---

## 6. Cuándo NO usar esta técnica

Sé honesto: no todo se monta así.

- **Cuando el corte de audio es el punto.** Si estás cortando entre dos personas distintas, el audio SÍ
  tiene que cortar. Eso es un corte de escena, no un picado de imagen.
- **Cuando hay sonido diegético importante.** Si el plano B tiene un sonido propio que aporta (la
  sartén, el aplauso, la puerta), matarlo con la voz del plano A pierde más de lo que gana. Ahí lo
  correcto es mezclar: voz continua **más** el sonido del plano B por debajo.
- **En bloques de más de 15 segundos.** El audio continuo de un bloque muy largo termina sonando
  monótono. Divide el video en bloques de 5–12 s y aplica la técnica **dentro** de cada bloque; entre
  bloques sí hay corte real de audio.

Para mezclar la voz continua con el sonido del inserto:

```bash
ffmpeg -hide_banner -y -i imagen_sin_audio.mp4 -i voz_bloque.wav -i sonido_inserto.wav \
  -filter_complex "[2:a]volume=0.25[amb];[1:a][amb]amix=inputs=2:duration=first:normalize=0[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k salida.mp4
```

`volume=0.25` deja el sonido de fondo a un cuarto del volumen: se percibe, no compite.

---

## 7. El script completo, listo para adaptar

```bash
#!/usr/bin/env bash
set -euo pipefail

FUENTE="toma.mp4"
INI=12.0
FIN=19.0

# 1) Audio continuo del bloque
ffmpeg -hide_banner -y -ss $INI -to $FIN -i "$FUENTE" -vn -c:a pcm_s16le -ar 48000 -ac 1 voz.wav
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 voz.wav)
echo "Presupuesto de imagen: $DUR s"

# 2) Pedazos de imagen (editar esta sección según la tabla de montaje)
ffmpeg -hide_banner -y -ss 12.0 -t 2.3 -i "$FUENTE" -an \
  -vf "scale=1080:1920:flags=lanczos,fps=30,setsar=1" \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p v1.mp4
ffmpeg -hide_banner -y -ss 3.0 -t 1.8 -i broll_producto.mp4 -an \
  -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1" \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p v2.mp4
ffmpeg -hide_banner -y -ss 16.1 -t 2.9 -i "$FUENTE" -an \
  -vf "scale=1242:2208:flags=lanczos,crop=1080:1920,fps=30,setsar=1" \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p v3.mp4

# 3) Unir imagen
printf "file 'v1.mp4'\nfile 'v2.mp4'\nfile 'v3.mp4'\n" > lista.txt
ffmpeg -hide_banner -y -f concat -safe 0 -i lista.txt -c copy imagen.mp4

# 4) Comprobar que la imagen cuadra con el audio
DIMG=$(ffprobe -v error -show_entries format=duration -of csv=p=0 imagen.mp4)
echo "imagen=$DIMG  audio=$DUR"
awk -v a="$DIMG" -v b="$DUR" 'BEGIN{d=a-b; if(d<0)d=-d; if(d>0.05) print "DESCUADRE de " d " s"; else print "OK"}'

# 5) Pegar audio
ffmpeg -hide_banner -y -i imagen.mp4 -i voz.wav -map 0:v:0 -map 1:a:0 \
  -c:v copy -c:a aac -b:a 192k -shortest bloque_final.mp4
```

---

## Errores comunes

1. **No hacer la suma.** Los pedazos de imagen suman 7,4 s y el audio dura 7,0 s: te quedan 0,4 s de
   imagen muda al final. Es el error número uno y se evita con una resta.
2. **Retomar el plano de la persona en el segundo equivocado.** Si el pedazo 3 vuelve a la toma en 14,3
   en vez de 16,1, la boca dice una cosa y se oye otra. Le pasa a todo el mundo la primera vez.
3. **Cortar el bloque de audio a mitad de palabra.** El interior del bloque está protegido, pero el
   inicio y el final no. Ahí sí hay que medir contra la transcripción.
4. **Mezclar fps distintos entre pedazos.** Un pedazo a 60 y otro a 30 producen saltos al unir. Fuerza
   `fps=30` (o el que sea) en todos.
5. **Olvidar `setsar=1`.** Si un clip viene con píxeles no cuadrados, al unir se deforma. Es una línea
   y evita un problema que después cuesta encontrar.
6. **Generar `lista.txt` con BOM en Windows.** ffmpeg falla y el mensaje no ayuda. `printf` desde bash
   o `-Encoding ascii`.
7. **Trabajar en MP3/AAC durante el proceso.** Cada recodificación degrada. WAV hasta el render final.
8. **Aplicar la técnica a bloques de 30 segundos.** El audio continuo tan largo se vuelve monótono.
   Bloques de 5–12 s.
9. **Matar el sonido propio de los insertos siempre.** A veces el chisporroteo de la sartén vale más que
   el silencio. Mézclalo al 20–25%.
10. **Dar por terminado sin verificar la sincronía labial** en el último pedazo. Es donde el descuadre
    se acumula y donde se nota.

---

## Checklist

- [ ] Medí la **duración real** de la fuente antes de cortar (`ffprobe`).
- [ ] Extraje el audio del bloque **completo y de una sola vez**, en WAV a 48 kHz mono.
- [ ] Escribí la **tabla de montaje** en papel antes de tocar ffmpeg.
- [ ] La **suma de los pedazos de imagen == duración del audio** (verificado, no estimado).
- [ ] Cuando vuelvo al plano de la persona hablando, retomo en el **segundo que corresponde a la voz**.
- [ ] Todos los pedazos comparten **resolución, fps, SAR y pix_fmt**.
- [ ] Cada pedazo dura lo que pedí (comprobado con `ffprobe` uno por uno).
- [ ] `lista.txt` está **sin BOM**.
- [ ] La imagen unida y el audio difieren en **menos de 0,05 s**.
- [ ] El corte de **inicio y de fin del bloque** no parte ninguna palabra.
- [ ] Revisé **fotogramas del final** del bloque y la sincronía labial se sostiene.
- [ ] Corrí `silencedetect` y **no hay silencio ni negro** colgando al final.
- [ ] Si algún inserto tenía sonido propio que aporta, lo **mezclé** en vez de matarlo.
