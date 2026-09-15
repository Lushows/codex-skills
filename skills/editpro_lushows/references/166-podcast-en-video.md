# 166 — Podcast en video

**Qué resuelve:** dos o tres personas hablando una hora y media, tres cámaras, y hay que sacar de ahí un
episodio en video que se vea y se oiga profesional, más 8 o 12 cortos verticales. Es el formato con más
horas de material y menos tiempo por hora de edición, así que **todo aquí se resuelve con sistema, no con
inspiración**.

> **La verdad económica del formato:** el episodio largo casi nunca rinde solo. El negocio está en los
> cortos que salen de él. Se monta el largo pensando ya en de dónde van a salir los cortos.

---

## 1. Preparar el material antes de montar

### La ingesta estándar

```
EP042/  video/ CAM_A_ancho.mp4 · CAM_B_host.mp4 · CAM_C_invitado.mp4
        audio/ MIC_host.wav · MIC_invitado.wav   (pistas aisladas)
        docs/  transcripcion.srt
```

**Las pistas de micrófono separadas son innegociables.** Sin ellas no puedes hacer ni ducking, ni cortar
por hablante, ni limpiar solo a quien suena mal. Si te llega una sola pista mezclada, el podcast se puede
montar pero nunca va a sonar profesional.

### Sincronizar todo

Palmada al inicio o `-itsoffset` con el desfase medido:

```bash
# Ver la palmada en cada pista
ffmpeg -i CAM_A_ancho.mp4 -t 15 -filter_complex "showwavespic=s=3840x300" -frames:v 1 ondaA.png
ffmpeg -i MIC_host.wav    -t 15 -filter_complex "showwavespic=s=3840x300" -frames:v 1 ondaMic.png

# Alinear cámara B que arrancó 3,42 s tarde
ffmpeg -i CAM_B_host.mp4 -ss 3.42 -c copy CAM_B_sync.mp4
```

⚠️ **La deriva.** En grabaciones largas (>1 h) las cámaras baratas derivan: al final del episodio hay
desfase aunque al principio estuviera perfecto. Verifica la sincronía **al final del archivo, no solo al
principio**. Si derivó, se corrige con `atempo` finísimo:

```bash
# La pista de audio va 480 ms adelantada al cabo de 90 min → estirar 0,0089%
ffmpeg -i MIC_host.wav -af "atempo=0.999911" MIC_host_corregido.wav
```

---

## 2. Cortar por hablante: la automatización que salva el formato

Con pistas separadas, **quién habla se puede detectar por volumen**. Eso es lo que permite montar 90
minutos en horas y no en días.

### Sacar el mapa de quién habla cuándo

```bash
# Cada bloque de voz del anfitrión (silencios de más de 0,4 s bajo -30 dB)
ffmpeg -i MIC_host.wav -af silencedetect=noise=-30dB:d=0.4 -f null - 2> host_bloques.txt
ffmpeg -i MIC_invitado.wav -af silencedetect=noise=-30dB:d=0.4 -f null - 2> inv_bloques.txt
```

De esos dos archivos sale una tabla:

```
00:00:00 – 00:00:12   HOST
00:00:12 – 00:00:48   INVITADO
00:00:48 – 00:00:51   HOST      ← intervención corta: NO cortar cámara
00:00:51 – 00:02:14   INVITADO
```

### La regla de los 3 segundos

**No cortes de cámara por intervenciones de menos de 3 segundos.** Si el anfitrión dice "claro" o "exacto"
mientras el invitado habla, quedarse en el invitado es lo correcto. Cortar en cada "ajá" produce un
episodio epiléptico.

### Cuándo SÍ cortar al plano general (CAM A)

- Cuando hablan los dos a la vez
- Cuando alguien se ríe fuerte
- Cuando hay gesto físico (señalan algo, se paran, muestran un objeto)
- **Cada 60–90 s como mínimo**, para recordar que hay dos personas en una sala
- Al cambiar de tema

### Duración mínima de plano

Nunca menos de **4 segundos** en un podcast. Este formato no es video corto: el ritmo alto aquí cansa. El
promedio sano está entre 8 y 20 segundos por plano.

---

## 3. Qué se corta del largo

Un podcast de 90 minutos crudos sale entre 65 y 80 en versión publicada. Qué se va:

| Se corta | Se queda |
|---|---|
| El arranque técnico ("¿ya está grabando?") | Las primeras frases naturales |
| Silencios de más de 2,5 s | Silencios de 1–2 s después de algo fuerte |
| Divagaciones que no llegan a ninguna parte | Divagaciones graciosas |
| Interrupciones técnicas (alguien entra, suena el teléfono) | La reacción a la interrupción si es buena |
| Repeticiones de la misma idea | La mejor versión de la idea |
| Muletillas densas (racimos de "eh") | Muletillas sueltas |

**No se corta tanto como en una entrevista documental.** El podcast vive de la sensación de conversación
real; sobre-editar lo vuelve artificial y le quita lo que la gente vino a buscar.

### El arranque del episodio

Los primeros 30 segundos deciden si se escucha el episodio. Estructura estándar:

```
0:00 – 0:20   COLD OPEN. El mejor momento del episodio, sacado del minuto 40.
0:20 – 0:30   Careta / intro de la marca (corta, 8 s máximo).
0:30 – 1:00   Presentación del invitado y de qué se va a hablar.
1:00 →        Conversación.
```

El cold open **se elige al final**, cuando ya viste todo el episodio.

---

## 4. Audio: donde se gana o se pierde el podcast

Un podcast se perdona visualmente feo. **No se perdona que suene mal.** Cadena por pista:

```bash
# Cadena completa para una pista de micrófono de podcast
ffmpeg -i MIC_host.wav -af "\
highpass=f=80,\
afftdn=nr=12:nf=-28,\
equalizer=f=200:t=q:w=1.4:g=-2,\
equalizer=f=3000:t=q:w=1.2:g=2.5,\
deesser=i=0.4:m=0.5:f=0.5,\
acompressor=threshold=-18dB:ratio=3.5:attack=6:release=180:makeup=3,\
alimiter=limit=-1.5dB,\
loudnorm=I=-16:TP=-1.5:LRA=9" \
MIC_host_procesado.wav
```

Qué hace cada eslabón: `highpass` quita el retumbe de mesa y el aire acondicionado · `afftdn` reduce
ruido espectral suave (12 dB, no más) · los 200 Hz a -2 quitan el "barro" de hablar pegado al micro · los
3000 Hz a +2,5 dan presencia · `deesser` baja las "s" silbantes · `acompressor` empareja susurro y risa ·
`alimiter` es el techo de seguridad · `loudnorm` fija el nivel de podcast.

### El nivel objetivo

- **Podcast en Spotify / Apple:** -16 LUFS mono, -16 a -14 estéreo
- **YouTube:** -14 LUFS
- Si publicas en los dos: **-15 LUFS** y quedas bien en ambos.

### La diafonía (bleed)

> **Término nuevo — diafonía / bleed:** la voz de uno que se cuela en el micrófono del otro. Produce eco y
> hace que la mezcla suene "hueca".

Se controla con un gate suave por pista, **suave de verdad**:

```bash
ffmpeg -i MIC_host.wav -af "agate=threshold=-32dB:ratio=2:attack=10:release=250" MIC_host_gate.wav
```

Un gate agresivo corta las respiraciones y el inicio de las palabras: suena peor que la diafonía. Si
tienes que elegir, deja la diafonía.

### La mezcla final

```bash
ffmpeg -i MIC_host_procesado.wav -i MIC_invitado_procesado.wav -filter_complex \
 "[0:a][1:a]amix=inputs=2:duration=longest:normalize=0[mix];\
  [mix]loudnorm=I=-15:TP=-1.5:LRA=9[a]" -map "[a]" mezcla_final.wav
```

`normalize=0` es importante: sin eso, `amix` baja cada pista a la mitad y pierdes 6 dB.

---

## 5. Subtítulos en formato largo

80 minutos de subtítulos no se escriben a mano: se transcriben con IA (`124`), se verifican los tiempos y
se corrigen a mano los nombres propios y las cifras.

### Quemados vs. archivo aparte

| Dónde | Qué hacer |
|---|---|
| YouTube largo | Subtítulos como archivo `.srt` subido. Nunca quemados. |
| Cortos verticales | **Quemados siempre.** |
| Web propia | `.vtt` en el reproductor |
| LinkedIn / X | Quemados (su reproductor de subtítulos es malo) |

### Reglas de subtitulado largo

- **Máximo 2 líneas, 42 caracteres por línea**
- Duración mínima 1 s, máxima 6 s por bloque
- **Identificar hablante** cuando cambia y no se ve en cámara: `— MARÍA:`
- No partir una frase entre dos bloques si se puede evitar

```bash
# Si toca quemarlos: estilo legible en 16:9
ffmpeg -i episodio.mp4 -vf "subtitles=episodio.srt:force_style='FontName=Inter,\
FontSize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H90000000,BorderStyle=3,\
Outline=1,Shadow=0,MarginV=48'" -c:a copy episodio_sub.mp4
```

Detalle en `43-formato-ass-y-libass.md` y `95-metadatos-y-accesibilidad.md`.

---

## 6. Cortos verticales desde el episodio largo

Aquí está el valor real. De un episodio salen **8–15 cortos**.

### Cómo se encuentran

En la transcripción buscas: **afirmaciones fuertes** ("la mayoría de restaurantes quiebran por esto"),
**números** ("el 70% cierra en dos años"), **historias con principio y final** que quepan en 60 s,
**desacuerdos** (el momento donde uno dice "no estoy de acuerdo"), **confesiones** ("yo perdí 40 millones
aprendiendo esto") y **momentos graciosos**.

**Lo que NO funciona como corto:** las partes donde se explica algo con contexto largo. Sin el episodio,
no se entienden.

### Anatomía del corto

```
0,0 – 1,5 s   La frase más fuerte. Ya cortada, sin arranque.
1,5 – 45 s    El desarrollo. Cambio de cámara cada 4–7 s.
45 – 55 s     El cierre de la idea.
(sin CTA de "escucha el episodio completo" al final — va en la descripción)
```

**El corto tiene que funcionar solo.** Si necesita saber quiénes son o de qué venían hablando, no es corto.

### El reencuadre vertical

Tres opciones, de peor a mejor:

**a) Crop centrado fijo** — la peor. Corta cabezas cuando alguien se mueve.

**b) Crop por hablante** — cambias la `x` del crop según quién habla:

```bash
# El invitado está a la derecha del cuadro 1920x1080 → crop hacia x=1100
ffmpeg -i corto_base.mp4 -vf "crop=608:1080:1100:0,scale=1080:1920" -c:a copy corto_inv.mp4
```

**c) Apilado (el estándar del formato)** — los dos primeros planos, uno encima del otro:

```bash
ffmpeg -i CAM_B_host.mp4 -i CAM_C_invitado.mp4 -filter_complex "\
[0:v]crop=1080:960:420:60,scale=1080:960[arriba];\
[1:v]crop=1080:960:420:60,scale=1080:960[abajo];\
[arriba][abajo]vstack=inputs=2[v]" \
-map "[v]" -map 0:a -c:v libx264 -crf 20 -c:a aac corto_apilado.mp4
```

Con apilado ves a los dos siempre, no hay que decidir a quién cortar, y se lee inmediatamente como
podcast. Es lo que más funciona.

**d) Apilado + zona de texto:** dos planos de 1080x800 arriba y abajo, y 320 px al centro o abajo para el
subtítulo grande.

Los subtítulos del corto son distintos de los del largo: **3–4 palabras por golpe, grandes, centrados**,
con la palabra clave resaltada. → `41-subtitulos-vs-palabras-clave.md`, `46-ritmo-del-texto.md`.

---

## 7. Capítulos y navegación del largo

Obligatorios en YouTube. Se sacan de la transcripción por cambios de tema:

```
00:00 Intro
00:38 Quién es Andrea y cómo empezó
08:12 Por qué cerró su primer restaurante
19:44 El error del costeo (esto le pasa a todos)
34:10 Cómo se calcula un plato de verdad
51:02 Preguntas rápidas
```

**Los títulos de capítulo son copy, no descripción.** "El error del costeo" rinde más que "Sobre costos".

Y también incrustados en el archivo → ver `162-tutorial-y-explicativo.md`, sección 5.

---

## 8. Exportar el largo

```bash
# Máster de podcast largo para YouTube (1080p, 80 min)
ffmpeg -i montaje.mov -c:v libx264 -crf 19 -preset slow -pix_fmt yuv420p \
  -g 60 -c:a aac -b:a 256k -ar 48000 -movflags +faststart EP042_master.mp4
```

CRF 19 basta (es una sala estática, no hay movimiento que comprima mal), 256 kbps de audio es el mínimo
—el audio es el producto—, `+faststart` para que empiece a reproducir sin descargar todo. Un episodio de
80 min a 1080p pesa 3–5 GB: es normal.

### Versión solo audio para las plataformas de podcast

```bash
ffmpeg -i EP042_master.mp4 -vn -c:a libmp3lame -b:a 192k -ar 44100 \
  -metadata title="EP042 — Por qué quiebran los restaurantes" \
  -metadata artist="GastroLatam" EP042.mp3
```

---

## Errores comunes

1. **Grabar con una sola pista de audio mezclada.** Sin pistas separadas no hay podcast profesional
   posible. Es el error irreversible del formato.
2. **No verificar la deriva al final del archivo.** Sincroniza al principio, revienta al minuto 70.
3. **Cortar cámara en cada "ajá".** Regla de los 3 segundos.
4. **Ritmo de video corto en un episodio largo.** Planos de 2 s durante 80 minutos agotan.
5. **No volver al plano general nunca.** El espectador olvida que hay dos personas en una sala.
6. **Gate agresivo** que corta respiraciones e inicios de palabra. Peor que la diafonía.
7. **`amix` sin `normalize=0`**, que baja 6 dB la mezcla y obliga a subir todo después.
8. **Sobre-editar la conversación.** El podcast vive de sentirse real.
9. **Cold open elegido al principio.** Se elige al final, cuando ya viste todo.
10. **Cortos que necesitan contexto.** Si hay que saber de qué venían hablando, no funcionan.
11. **Cortos con crop centrado fijo** que decapitan a los invitados.
12. **Subtítulos quemados en el episodio largo de YouTube.** Impide traducción automática y el reproductor
    ya los maneja.
13. **Audio exportado a 128 kbps.** En un podcast eso es sabotaje.
14. **Sin capítulos** en un episodio de 80 minutos.
15. **Títulos de capítulo descriptivos** en vez de copy que da ganas de saltar ahí.

---

## Checklist

- [ ] Pistas de micrófono separadas por hablante disponibles
- [ ] Todas las cámaras sincronizadas, verificado al INICIO y al FINAL del archivo
- [ ] Deriva corregida si la hubo
- [ ] Mapa de quién habla cuándo generado con `silencedetect`
- [ ] Regla de los 3 segundos aplicada: no se corta por intervenciones cortas
- [ ] Plano general presente al menos cada 60–90 s
- [ ] Ningún plano dura menos de 4 s
- [ ] Cold open elegido al final, con el mejor momento del episodio
- [ ] Cadena de audio aplicada por pista; gate suave, no agresivo
- [ ] Mezcla con `normalize=0`; nivel final -15 LUFS (o -16/-14 según destino)
- [ ] Transcripción corregida a mano en nombres propios y cifras
- [ ] Subtítulos del largo como archivo `.srt`, no quemados
- [ ] Capítulos escritos como copy, con timecodes desde 00:00
- [ ] Entre 8 y 15 cortos identificados y montados
- [ ] Cada corto funciona sin contexto del episodio
- [ ] Cortos en apilado o crop por hablante, nunca crop centrado fijo
- [ ] Subtítulos de los cortos quemados, 3–4 palabras por golpe
- [ ] Máster con audio a 256 kbps y `+faststart`
- [ ] Versión solo audio exportada con metadatos
- [ ] Pasó `98-verificacion-del-corte.md`
