# 165 — Musical y videoclip

**Qué resuelve:** montar sobre una canción cuando la canción es el producto, no el fondo. Un videoclip,
un lyric video, una presentación en vivo, un clip promocional de un lanzamiento. Aquí el audio es
intocable y **todo el video se somete a él**: cada corte, cada plano, cada texto.

> **La regla de oro:** en cualquier otro formato el audio se ajusta al montaje. Aquí el montaje se ajusta
> al audio, al fotograma. Si un corte no cae donde debe, no se mueve la canción — se rehace el corte.

---

## 1. Antes de montar: mapear la canción

No se toca un clip hasta tener la canción escrita en el papel. Este mapa es el guion del videoclip.

### El mapa mínimo

```
BPM: 92          → 1 beat = 60/92 = 0,652 s
Compás: 4/4      → 1 compás = 4 beats = 2,609 s

0:00,000 – 0:10,435   Intro          (4 compases)
0:10,435 – 0:31,304   Verso 1        (8 compases)
0:31,304 – 0:41,739   Pre-coro       (4 compases)
0:41,739 – 1:02,609   CORO           (8 compases)
1:02,609 – 1:23,478   Verso 2        (8 compases)
...
```

**Todo timecode en milésimas, no en segundos redondos.** A 92 BPM, 50 ms de error ya se nota en un corte.

### Cómo sacar el BPM sin adivinar

```bash
# Aísla el bombo y lista cada golpe con su tiempo
ffmpeg -i cancion.wav -af "lowpass=f=150,silencedetect=n=-26dB:d=0.08" -f null - 2> golpes.txt
```

Cuentas cuántos golpes hay en 30 segundos y multiplicas por 2. Si salen 46 golpes en 30 s → 92 BPM.

Alternativa visual: la forma de onda ampliada te deja medir los picos a ojo con bastante precisión.

```bash
# Onda de los primeros 20 s, muy ancha, para medir a ojo
ffmpeg -i cancion.wav -t 20 -filter_complex "showwavespic=s=7680x400:colors=white" \
  -frames:v 1 onda_detalle.png
```

### La tabla de duraciones que vas a usar todo el video

Con BPM 92 (1 beat = 0,652 s):

| Unidad | Duración | Se usa en |
|---|---|---|
| ½ beat | 0,326 s | Ráfagas en el coro. Máximo 4 seguidos. |
| 1 beat | 0,652 s | Corte rápido |
| 2 beats | 1,304 s | El estándar del verso |
| 1 compás (4 beats) | 2,609 s | Plano de respiro |
| 2 compases | 5,217 s | Plano largo, intro o puente |

**Nunca cortes fuera de esta tabla.** Un plano de 1,8 s en una canción de 92 BPM está mal aunque se vea
bonito: cae entre dos beats y produce una incomodidad que el espectador siente sin poder nombrar.

---

## 2. Cortar al beat de verdad

"Cortar al beat" no significa poner un corte en cada golpe. Significa que **cada corte cae en un golpe**,
pero no todos los golpes llevan corte.

### Los tres niveles de corte

```
Beat fuerte (1 y 3 del compás)  → aquí van los cortes principales
Beat débil  (2 y 4)             → cortes secundarios, más discretos
Contratiempo (entre beats)      → solo a propósito, para desestabilizar
```

Un videoclip que corta en TODOS los beats se vuelve monótono a los 20 segundos. La variación se logra
alternando duraciones:

```
Verso:      2 - 2 - 2 - 4 - 2 - 2 - 4 - 4        (beats por plano)
Pre-coro:   2 - 2 - 1 - 1 - 2 - 1 - 1 - 1        (acelera)
Coro:       1 - 1 - 2 - 1 - 1 - 4 - 1 - 1 - 2    (energía con respiros)
Puente:     8 - 8 - 4 - 4                        (calma)
```

**La aceleración antes del coro es la técnica más eficaz del formato.** Los planos se acortan progresivamente
en los últimos 4 compases del pre-coro, y el primer plano del coro vuelve a ser largo. Ese contraste es
lo que hace que el coro "pegue".

### El corte del downbeat

> **Término nuevo — downbeat:** el primer golpe de cada compás. Es el más fuerte.

El corte que entra al coro va **exactamente en el downbeat**, no un fotograma antes ni después. A 30 fps
un fotograma son 33 ms; a 92 BPM eso es un 5% del beat. Se nota.

```
Coro empieza en 41,739 s
A 30 fps  →  41,739 × 30 = 1252,17  →  fotograma 1252
Timecode exacto de corte: 1252/30 = 41,733 s
```

Redondea siempre **al fotograma más cercano**, y verifica que la canción no se desplace.

---

## 3. Sincronía de labios

Si el artista canta en cámara, la sincronía es innegociable. Un desfase de 2 fotogramas ya se ve.

### El método del playback

En rodaje el artista canta encima de la canción sonando por un parlante. En montaje tienes que alinear
cada toma con la canción máster.

**El truco de campo:** que en cada toma, antes de empezar, se dé una **palmada fuerte al mismo tiempo que
un punto reconocible de la canción**. Esa palmada es tu punto de alineación.

```bash
# Ver la onda de la toma para ubicar la palmada con precisión
ffmpeg -i toma_04.mp4 -filter_complex "showwavespic=s=3840x300" -frames:v 1 onda_toma04.png
```

Y una vez sabes el desfase (la toma arrancó 2,417 s después del punto de la canción):

```bash
# Alinear la toma con la canción máster
ffmpeg -ss 2.417 -i toma_04.mp4 -i cancion.wav -map 0:v -map 1:a \
  -c:v libx264 -crf 18 -c:a aac toma_04_sync.mp4
```

### Verificación de labios, cuadro a cuadro

No confíes en el oído. Verifica con imágenes:

```bash
# Extraer 12 fotogramas alrededor de una consonante fuerte (una "P" o una "B")
ffmpeg -ss 33.20 -i clip_sync.mp4 -frames:v 12 -vf "fps=30" labios_%02d.png
```

En una "P" o "B" los labios se cierran completamente. Ese cierre tiene que coincidir con el sonido en la
onda. Si el cierre está 2 fotogramas antes o después, corriges.

### Cuando no hay sincronía posible

Si la toma quedó mal grabada, tres salidas:

1. **Usarla solo cuando NO se le ve la boca** (planos de espalda, de manos, desenfocados)
2. **Estirar/comprimir levemente** — hasta 2% no se nota:
   ```bash
   ffmpeg -i toma.mp4 -vf "setpts=PTS/1.018" -an toma_ajustada.mp4
   ```
3. **Taparla con b-roll** en los momentos críticos

---

## 4. Estructura por secciones de la canción

Cada sección de la canción pide un tratamiento visual distinto. Esa es la estructura del videoclip.

| Sección | Tratamiento visual | Ritmo |
|---|---|---|
| **Intro** | Establecer lugar y ambiente. Sin artista o de espaldas. Planos largos. | 4–8 beats |
| **Verso 1** | Artista cantando, plano medio. Narrativa si la hay. | 2–4 beats |
| **Pre-coro** | Acelera. Planos más cerrados. Movimiento. | 1–2 beats, decreciendo |
| **Coro** | Máxima energía. Plano abierto o el más icónico. Color más saturado. | 1–2 beats |
| **Verso 2** | Igual que el 1 pero con **material nuevo**, nunca repetido | 2–4 beats |
| **Puente** | Ruptura. Cambia todo: locación, color, velocidad | 4–8 beats |
| **Coro final** | Todo junto. Aquí van los planos guardados. | 1 beat |
| **Cola** | Un solo plano largo. Quietud. | 8+ beats |

### La ley del material guardado

**Los mejores tres planos NO van en el primer coro.** Van en el coro final. Si gastas lo bueno al minuto
uno, el resto del video es un descenso.

### La ley de la variación por sección

El verso 2 **nunca repite planos del verso 1**. Si no tienes material suficiente, cambias el tratamiento:
mismo plano pero con otro color, con velocidad distinta, o reencuadrado. Repetir literalmente se lee como
falta de material.

---

## 5. Recursos propios del videoclip

### Corte a negro rítmico

Negros de 2–4 fotogramas entre planos, en el beat. Da golpe sin efecto.

```bash
# Insertar 3 fotogramas de negro (0,1 s a 30 fps) entre dos clips
ffmpeg -f lavfi -i color=c=black:s=1920x1080:d=0.1:r=30 -c:v libx264 -crf 18 negro.mp4
```

### Congelado en el golpe

El plano se congela en el acento y sigue. 4–8 fotogramas.

```bash
# Congelar el fotograma del segundo 18,4 durante 0,2 s y continuar
ffmpeg -i clip.mp4 -vf "select='lte(t,18.4)',setpts=N/FRAME_RATE/TB" parte1.mp4
ffmpeg -ss 18.4 -i clip.mp4 -frames:v 1 congelado.png
ffmpeg -loop 1 -i congelado.png -t 0.2 -r 30 -c:v libx264 -crf 18 -pix_fmt yuv420p freeze.mp4
```

### Speed ramp en el downbeat

Acelerar y frenar justo en el golpe. El más usado y el más fácil de arruinar. → `55-velocidad-y-rampas.md`.

### Cambio de color por sección

El coro con más saturación y contraste que el verso. Sutil (10–15%), no evidente.

```bash
# Coro: +15% saturación, +8% contraste
ffmpeg -i coro.mp4 -vf "eq=saturation=1.15:contrast=1.08" -c:a copy coro_color.mp4
```

### Flash blanco en el downbeat del coro

2 fotogramas de blanco. Uno solo por video, en el momento más grande. Más de eso es epilepsia de plantilla.

---

## 6. Lyric video: el caso aparte

El texto lleva todo el peso. Reglas propias:

- **La palabra aparece cuando se canta**, sílaba a sílaba si la canción lo permite
- **Nunca adelantada.** Si el texto va antes que la voz, se lee a karaoke barato
- Máximo **una frase en pantalla**, no dos líneas de estrofa
- La tipografía es la identidad del artista → pasa por `directorcreativo_lushows` antes
- El fondo se mueve **lento y constante**; el texto es el que hace el ritmo

En formato ASS, la sincronía karaoke se hace con las etiquetas `\k`:

```
Dialogue: 0,0:00:41.73,0:00:44.34,Default,,0,0,0,,{\k24}Na{\k18}die {\k30}sa{\k22}be
```

Cada `\k` es la duración en centésimas de segundo de esa sílaba. Ver `43-formato-ass-y-libass.md`.

---

## 7. Presentación en vivo (multicámara musical)

Otro sub-formato: la banda tocando, 2–4 cámaras.

- **Corta al instrumento que suena.** Si entra la guitarra, se corta a la guitarra. Es lo único que
  distingue a un buen montaje musical en vivo de una sucesión aleatoria de planos.
- **Los solos van en plano cerrado del que toca**, y se aguantan más de lo cómodo (4–8 compases).
- **El cantante en el coro**, siempre. Es lo que la gente espera ver.
- El audio se sustituye por la mezcla de mesa, nunca el de cámara.

```bash
# Sustituir audio de cámara por mezcla de mesa, con desfase conocido de 0,73 s
ffmpeg -i camara2.mp4 -itsoffset 0.73 -i mezcla_mesa.wav -map 0:v -map 1:a \
  -c:v copy -c:a aac -b:a 320k vivo_sync.mp4
```

---

## 8. Exportar sin dañar la música

El error técnico más frecuente del formato: exportar el videoclip con audio a 128 kbps y arruinar la
canción que era el producto.

```bash
# Máster de videoclip: audio AAC 320 kbps, 48 kHz, sin normalizar
ffmpeg -i montaje.mp4 -i cancion_master.wav -map 0:v -map 1:a \
  -c:v libx264 -crf 16 -preset slow -pix_fmt yuv420p \
  -c:a aac -b:a 320k -ar 48000 videoclip_master.mp4
```

- **No apliques `loudnorm` a la canción.** Ya viene masterizada. Normalizarla la aplana.
- **No apliques ducking ni compresión.** No hay voz que proteger.
- YouTube va a normalizar a -14 LUFS de todas formas; que lo haga él, no tú.

---

## 9. Verificación específica

1. **Ver el video sin sonido.** ¿El ritmo visual se sostiene solo? Si los cortes se sienten aleatorios sin
   música, están mal colocados.
2. **Escuchar el video sin ver.** ¿La canción está completa e intacta? ¿Ningún corte de audio?
3. **Cuadro a cuadro en cada entrada de coro.** El corte tiene que caer en el downbeat exacto.
4. **Labios en tres puntos distintos** del video (principio, medio, final). El desfase suele aparecer por
   deriva a lo largo del clip.

---

## Errores comunes

1. **Montar sin mapear la canción.** El mapa es el guion; sin él es adivinanza.
2. **Cortar fuera de la retícula de beats.** Un plano de 1,8 s en una canción de 92 BPM se siente mal
   aunque se vea bien.
3. **Cortar en TODOS los beats.** Monótono a los 20 segundos. La variación de duraciones es la música
   visual.
4. **Gastar los mejores planos en el primer coro.** El resto del video es un descenso.
5. **Repetir literalmente el verso 1 en el verso 2.** Se lee como falta de material.
6. **Labios desfasados 2+ fotogramas.** Es lo primero que el público de música nota y lo que más se
   comenta.
7. **No dar la palmada de sincronía en rodaje.** Alinear después es horas de trabajo evitable.
8. **Texto de lyric video adelantado a la voz.** Karaoke barato.
9. **No cortar al instrumento que suena** en presentación en vivo.
10. **Usar el audio de cámara** en vivo en lugar de la mezcla de mesa.
11. **Normalizar o comprimir la canción máster.** La aplanas y el artista lo va a notar.
12. **Audio exportado a 128 kbps.** El producto era la canción.
13. **Flash blanco en cada coro.** Uno por video, o ninguno.
14. **Speed ramps por todos lados.** Uno o dos bien puestos valen más que quince.

---

## Checklist

- [ ] BPM medido (no adivinado) y mapa de secciones escrito con timecodes en milésimas
- [ ] Tabla de duraciones por beat calculada y usada en todos los cortes
- [ ] Ningún plano tiene duración fuera de la retícula de beats
- [ ] Las duraciones varían dentro de cada sección; no hay corte en todos los beats
- [ ] Aceleración progresiva en el pre-coro
- [ ] El corte de entrada al coro cae en el downbeat exacto, verificado al fotograma
- [ ] Los tres mejores planos están reservados para el coro final
- [ ] El verso 2 no repite material del verso 1
- [ ] El puente rompe visualmente (locación, color o velocidad)
- [ ] Sincronía de labios verificada con fotogramas en 3 puntos del video
- [ ] Ningún desfase de labios mayor a 1 fotograma
- [ ] Cambio de color sutil entre verso y coro (10–15%)
- [ ] Máximo un flash blanco en todo el video
- [ ] En lyric video: la palabra nunca aparece antes de cantarse
- [ ] En vivo: se corta al instrumento que suena; audio de mesa, no de cámara
- [ ] Canción sin normalizar, sin comprimir, exportada a 320 kbps / 48 kHz
- [ ] Video visto sin sonido: el ritmo visual se sostiene
- [ ] Pasó `98-verificacion-del-corte.md`
