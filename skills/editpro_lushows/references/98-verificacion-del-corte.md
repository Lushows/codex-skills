# 98 — Verificación del corte: el módulo más importante de esta skill

> **Renderizar no es terminar.** Un archivo exportado es una hipótesis: la hipótesis de que el video quedó
> como creías. Este módulo es cómo se comprueba esa hipótesis con evidencia en vez de con fe.

---

## El problema de fondo, dicho sin rodeos

Cuando montas un video con ayuda de IA, existe un hueco que casi nadie nombra:

**La IA no puede ver el video corriendo. No puede oír el audio.**

Puede leer el guion, calcular los tiempos, escribir el comando de ffmpeg, cortar en el segundo 12,340 y
pegar la música. Y el archivo sale. Y el archivo se ve perfectamente bien en un fotograma congelado. Y en
la hoja de contactos todo está en su sitio.

**Y el video puede estar roto.**

Porque los defectos que arruinan un video no viven en un fotograma. Viven **en el tiempo**:

- Un corte que se comió media palabra
- Una frase que quedó sin terminar
- Una repetición que quedó pegada dos veces
- Un silencio de 3 segundos en medio de una frase
- Música que tapa la voz
- Un video que termina antes de que la persona termine de hablar

Ninguna de esas cosas se ve mirando fotogramas. **Todas se oyen en dos segundos.** El problema es que ni
la IA que montó, ni el editor apurado que revisó a 2× de velocidad, están oyendo de verdad.

El error mental que hay que matar es este:

> "El comando corrió sin errores, entonces el video quedó bien."

Un comando de ffmpeg que corre sin errores solo prueba que **el archivo se escribió**. No prueba que el
contenido tenga sentido. ffmpeg cortará felizmente en la mitad exacta de la palabra "características" y te
devolverá código de salida 0 con una sonrisa.

---

## La solución verificada: el bucle de verificación

El bucle es esto, y es simple:

```
Montas el video
      ↓
Le extraes el audio AL VIDEO YA MONTADO (no a los brutos)
      ↓
Le mandas ese audio a un modelo que lea audio
      ↓
Le pides que sea ESTRICTO y reporte defectos concretos
      ↓
Filtras los falsos positivos
      ↓
Corriges lo que sí es defecto
      ↓
Vuelves a montar y repites hasta que salga limpio
```

**La clave está en el paso 2: el audio se extrae del video ya montado.** No de los brutos, no del guion, no
de la línea de tiempo. Del archivo exportado, el mismo que se va a publicar. Ese archivo es el único que
contiene la verdad de lo que hicieron todos tus cortes juntos.

Y el paso 3 es lo que cierra el hueco: **un modelo que lee audio SÍ oye el video.** Le devuelve al proceso
el sentido que la edición ciega perdió.

### Cómo se extrae el audio

```bash
# Del video final, tal cual quedó
ffmpeg -i corte_final.mp4 -vn -acodec pcm_s16le -ar 16000 -ac 1 verificar.wav
```

- `-vn` descarta el video (solo queremos audio)
- `-ar 16000` — 16 kHz es suficiente para voz y hace el archivo pequeño
- `-ac 1` — mono, mismo motivo

Si el video es largo y el archivo queda pesado, córtalo en tramos de 10 minutos:
```bash
ffmpeg -i corte_final.mp4 -vn -acodec pcm_s16le -ar 16000 -ac 1 \
  -f segment -segment_time 600 verificar_%02d.wav
```

---

## El prompt exacto de verificación

Este es el prompt. Está afinado para producir hallazgos accionables y no divagaciones. Va acompañado del
archivo de audio.

```
Este es el audio de un video YA MONTADO que está a punto de publicarse.
Escúchalo completo y con atención.

Tu trabajo es ser ESTRICTO. No me digas que suena bien. Búscame los defectos.
Es mejor que reportes algo dudoso a que se me escape un error real.

Reporta, con el SEGUNDO EXACTO de cada hallazgo:

1. CORTES BRUSCOS — cualquier lugar donde una palabra quede partida a la mitad,
   donde el audio arranque o se detenga en medio de una sílaba, o donde se
   escuche un chasquido de edición. Dime qué palabra quedó partida y cómo se
   escucha exactamente.

2. FRASES INCOMPLETAS — cualquier oración que empiece y no termine, o que
   termine sin haber empezado. Transcríbeme la frase tal como quedó.

3. REPETICIONES — cualquier palabra, frase o segmento que se escuche dos veces
   seguidas sin que sea intencional.

4. SILENCIOS LARGOS — cualquier pausa de más de 1,5 segundos. Dime dónde empieza,
   cuánto dura, y si cae en medio de una frase o entre frases.

5. EL FINAL — dime exactamente cómo termina el audio: ¿la última frase está
   completa? ¿se corta a media palabra?

6. INTELIGIBILIDAD — transcríbeme el audio completo. Si hay algún tramo donde no
   puedas entender lo que se dice, dímelo con el segundo exacto y dime qué lo
   está tapando (música, ruido, volumen bajo).

Formato de respuesta: una lista de hallazgos, cada uno con [segundo] + qué pasa +
qué se escucha. Al final, un veredicto de una línea: ¿esto se puede publicar o no?
```

**Por qué cada parte del prompt está ahí:**

- **"Sé ESTRICTO"** — sin esa instrucción, los modelos tienden a ser amables y decir "suena bien en
  general". Necesitas lo contrario.
- **"Es mejor que reportes algo dudoso"** — le das permiso explícito de equivocarse hacia el lado seguro.
  Prefieres 3 falsos positivos que 1 defecto real que se te escapa.
- **"con el SEGUNDO EXACTO"** — sin el tiempo, el hallazgo es inútil: no puedes ir a arreglarlo.
- **"qué palabra quedó partida"** — te dice si el defecto es grave (una palabra clave) o menor.
- **"transcríbeme el audio completo"** — esto es el paso 6 y es el que hace la magia extra que se explica
  más abajo.
- **"veredicto de una línea"** — te obliga a una decisión, no a un ensayo.

---

## Los cuatro defectos reales que este bucle cazó

Esto no es teoría. En un proyecto real, este bucle encontró **cuatro defectos que no se ven mirando el
video en silencio** y que se habrían publicado tal cual:

### Defecto 1 — El corte que se comió la palabra "Fue"

El corte empezaba una frase en el segundo justo donde la persona ya había dicho "Fue". La frase quedaba:

> *"...una decisión difícil"* en vez de *"Fue una decisión difícil"*

En el video se ve perfecto: la persona está hablando, la boca se mueve, no hay salto visual. **Solo se
detecta oyendo.** Y una vez lo oyes, es obvio que la frase arranca mal.

Costo del arreglo: mover el punto de entrada 0,4 segundos hacia atrás. Costo de no arreglarlo: un video
que suena amateur desde el primer segundo.

### Defecto 2 — El corte que partió "características" en "carac..."

Un corte cayó en medio de una palabra larga y la dejó en:

> *"...las principales carac—"* [corte]

Este es el defecto clásico de la edición por tiempos: el algoritmo cortó en un punto que **numéricamente**
tenía sentido (final de un bloque, inicio de otro), pero que **fonéticamente** cayó en medio de una
palabra de cinco sílabas.

Es el ejemplo perfecto de por qué "el comando corrió bien" no significa nada.

### Defecto 3 — El video que terminaba a media palabra

El video terminaba antes de que la última frase se completara. La duración total era la calculada, el
archivo estaba sano, ffprobe reportaba todo correcto. **Y el video terminaba a la mitad de una palabra.**

Este es especialmente peligroso porque:
- Nadie revisa los últimos segundos con atención (ya viste el video, ya sabes qué dice)
- El fundido de salida o la música pueden disfrazarlo parcialmente
- Es el último recuerdo que se lleva el espectador

### Defecto 4 — El gancho que soltaba la revelación 1,3 segundos antes de tiempo

Este es el más interesante de los cuatro, porque **no es un error técnico: es un error de efecto**.

El gancho estaba construido como un bucle abierto: se planteaba una intriga y la revelación llegaba
después. Pero el corte dejó entrar la revelación **1,3 segundos antes de lo que debía**. Resultado: el
misterio nunca llegó a instalarse. El espectador oía la pregunta y la respuesta casi encimadas, y el efecto
—que era todo el punto del gancho— desapareció.

Ningún fotograma muestra esto. Ninguna métrica lo detecta. **Solo se oye.** Y 1,3 segundos, en un gancho,
es la diferencia entre que funcione y que no.

---

## El descubrimiento adicional: probar que la música no tapa la voz

Esta es la parte que casi nadie ha pensado, y es enormemente útil.

**Si le mandas al modelo el audio del video YA MEZCLADO CON MÚSICA, y el modelo te transcribe la voz
limpia y completa, eso PRUEBA que la música no está tapando la voz.**

Piénsalo: el modelo tuvo que separar la voz del fondo musical para poder transcribirla. Si lo logró
sin huecos, la voz es inteligible por encima de la música.

**Es la única forma de medir eso sin oírlo tú mismo.** No hay un número de ffmpeg que te diga "la voz se
entiende". Hay medidores de nivel (LUFS, picos), pero un nivel correcto no garantiza inteligibilidad: la
música puede estar 12 dB por debajo y aun así enmascarar la voz si comparten el mismo rango de frecuencias.

Cómo se usa en la práctica:

1. Exportas el video **con la mezcla final** (voz + música + efectos)
2. Extraes ese audio mezclado
3. Se lo mandas al modelo pidiendo transcripción completa
4. **Comparas la transcripción con el guion**

| Resultado | Qué significa |
|---|---|
| Transcripción completa y limpia | ✅ La música no tapa la voz. Publica |
| Huecos en la transcripción | ❌ Ahí la música está enmascarando. Baja la música o sube la voz en ese tramo |
| El modelo dice "no entiendo el tramo del segundo X" | ❌ Te dio el segundo exacto del problema. Ve a arreglarlo |
| Palabras mal transcritas en un tramo concreto | ⚠️ Inteligibilidad marginal. Revisa ese tramo a oído |

Y el dato que hace esto todavía mejor: **el modelo te da el segundo exacto donde la voz se pierde**. No
"la música está muy alta"; te dice "entre 0:23 y 0:26 no entiendo qué dice". Vas a ese tramo y bajas la
música 4 dB solo ahí.

```bash
# Bajar la música solo en un tramo, usando volume con enable
ffmpeg -i corte.mp4 -filter_complex \
  "[0:a]volume=enable='between(t,23,26)':volume=0.45[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k corte_fix.mp4
```

Si tienes las pistas separadas (lo ideal), lo correcto es aplicar *ducking* automático:
```bash
ffmpeg -i voz.wav -i musica.wav -filter_complex \
  "[1:a][0:a]sidechaincompress=threshold=0.03:ratio=8:attack=5:release=300[m];\
[0:a][m]amix=inputs=2:duration=first:weights=1 0.7[out]" \
  -map "[out]" mezcla.wav
```

---

## CRÍTICO: los falsos positivos

Aquí está la parte que separa a quien usa esta herramienta bien de quien la usa mal.

**El verificador va a marcar como "errores de edición" cosas que hiciste a propósito.**

Y tiene que hacerlo. Es su trabajo. Le pediste que fuera estricto y que reportara lo dudoso. Pero eso
significa que **tú tienes que filtrar.**

### La regla de oro

> **El verificador REPORTA. El editor DECIDE.**

Nunca, jamás, apliques automáticamente todo lo que el verificador señala. Si lo haces, vas a destruir
decisiones creativas que eran correctas.

### Los falsos positivos que vas a ver siempre

**1. Los bloopers**

Si tu video tiene una sección de tomas falsas al final, el verificador va a marcar cada una: frases
incompletas, repeticiones, risas cortando palabras, gente diciendo "otra vez". **Va a reportar diez
defectos donde hay una decisión creativa deliberada.**

Reconocerlo es fácil: los hallazgos se agrupan en un tramo continuo al final del video, y la naturaleza de
los "defectos" es exactamente la que hace graciosos a los bloopers.

**2. El gancho cortado a propósito**

Un bucle abierto **es** una frase incompleta. Eso es literalmente lo que lo hace funcionar. El verificador
va a decir "frase incompleta en 0:02". Y tiene razón técnicamente y está completamente equivocado
creativamente.

**3. Las pausas dramáticas**

Un silencio de 2 segundos antes de una revelación es una herramienta, no un defecto. El verificador va a
marcarlo como "silencio largo de 2,1 s". Es intencional.

**4. Las repeticiones retóricas**

*"No es caro. No es caro. Es que no sabes cuánto te cuesta."* El verificador ve una repetición. Tú ves una
figura retórica.

**5. Las interjecciones y muletillas deliberadas**

Si dejaste un "eh" o un "o sea" porque le da naturalidad, el verificador lo marca como imperfección.

**6. Los cortes secos como recurso de ritmo**

Un jump cut agresivo, que es la base del ritmo de un reel, puede leerse como "corte brusco".

### Cómo distinguir: las cuatro preguntas

Ante cada hallazgo, pregúntate en este orden:

1. **¿Yo puse eso ahí a propósito?** Si la respuesta es sí y recuerdas por qué → falso positivo. Sigue.
2. **¿Está en una zona que sé que es intencional?** (bloopers al final, gancho al inicio) → probablemente
   falso positivo. Verifícalo a oído de todas formas.
3. **¿La palabra partida es una palabra completa dicha a medias, o es una frase que decidí no terminar?**
   - Palabra partida (`carac—`) → **defecto real, siempre**
   - Frase completa que no se cierra (`"y lo que descubrí fue..."`) → puede ser un bucle abierto
     intencional
4. **¿Escuchándolo yo mismo, suena a error o suena a decisión?** Esta pregunta cierra todas las dudas.
   **Cuando dudes, escucha ese tramo específico.** El verificador ya te dio el segundo exacto: escuchar 4
   segundos cuesta 4 segundos.

### Los que NUNCA son falsos positivos

Estos, si aparecen, **son defectos reales sin excepción**:

- Una palabra **partida a mitad de sílaba** (`caract—`, `respon—`)
- El video que **termina a media palabra**
- Un tramo donde el modelo **no puede transcribir** por enmascaramiento de música
- Un chasquido o clic de edición audible
- La misma frase completa **duplicada** fuera de una sección de bloopers

Si el verificador reporta uno de estos, ve y arréglalo. No hay debate.

### La forma correcta de trabajar el reporte

Coge el reporte y clasifica cada hallazgo en tres columnas antes de tocar nada:

| Hallazgo | Segundo | Veredicto |
|---|---|---|
| Palabra "características" partida | 0:18,4 | 🔴 **Arreglar** |
| Frase incompleta "y ahí fue cuando..." | 0:02,1 | 🟢 Intencional (gancho) |
| Silencio 2,3 s | 0:27,0 | 🟡 Escuchar y decidir |
| Repetición "no es caro / no es caro" | 0:33,8 | 🟢 Intencional (retórica) |
| Video termina a media palabra | 0:44,9 | 🔴 **Arreglar** |
| No se entiende el tramo | 0:23–0:26 | 🔴 **Arreglar** (música) |
| Frases incompletas múltiples | 0:48–1:02 | 🟢 Intencional (bloopers) |

Solo después de esa tabla, tocas el corte.

---

## Verificación visual: lo que sí se ve

El bucle de audio caza los defectos temporales. Estos comandos cazan los defectos visuales y técnicos.

### Hoja de contactos del resultado final

Una imagen con muchos fotogramas del video terminado. Te deja ver de un vistazo cortes negros, fotogramas
duplicados, texto mal puesto y saltos de color.

```bash
# 36 fotogramas del resultado final, con marca de tiempo
ffmpeg -i corte_final.mp4 -vf "fps=1,\
drawtext=text='%{pts\\:hms}':fontcolor=yellow:fontsize=26:box=1:boxcolor=black@0.7:x=6:y=6,\
scale=320:-1,tile=6x6" -frames:v 1 -q:v 2 contactos_final.jpg
```

Qué buscar en la hoja de contactos:
- Fotogramas **negros o en blanco** donde no debería haberlos
- Fotogramas **idénticos consecutivos** (un congelado que no querías)
- **Texto que aparece cortado** por el borde
- Cambios de **color/exposición** entre tomas que no habías notado
- El **primer** y el **último** fotograma (esquinas de la imagen)

### ffprobe: los números duros

```bash
ffprobe -v error -show_entries format=duration,size,bit_rate \
  -show_entries stream=index,codec_type,codec_name,profile,width,height,r_frame_rate,pix_fmt,nb_frames \
  -of default=noprint_wrappers=1 corte_final.mp4
```

Contra qué comparar:

| Dato | Qué verificar |
|---|---|
| `duration` | ¿Coincide con lo que esperabas? ¿O quedó 3 s más corto? |
| `width` × `height` | ¿Es la resolución de la plataforma destino? ¿Ambos pares? |
| `r_frame_rate` | ¿30/1? ¿O quedó en 29,97 o 25 sin querer? |
| `pix_fmt` | **¿Dice `yuv420p`?** Si no, video verde en camino |
| `codec_name` | ¿`h264`? ¿Con `profile=High`? |
| `size` | ¿Cabe en el límite de la plataforma? |
| `nb_frames` | duración × fps debería dar aprox. este número |

**Verificar que el archivo no está corrupto:**
```bash
ffmpeg -v error -i corte_final.mp4 -f null - 2>errores.txt && \
  ([ -s errores.txt ] && echo "❌ HAY ERRORES" && cat errores.txt || echo "✅ archivo sano")
```

**Verificar que hay audio de verdad** (más común de lo que crees: exportar sin pista de audio):
```bash
ffprobe -v error -select_streams a -show_entries stream=codec_name,channels,sample_rate \
  -of default=noprint_wrappers=1 corte_final.mp4
# Si no imprime nada, TU VIDEO NO TIENE AUDIO
```

**Detectar silencios (una segunda opinión automática, sin IA):**
```bash
ffmpeg -i corte_final.mp4 -af "silencedetect=noise=-40dB:d=1.5" -f null - 2>&1 | grep silence
```
Esto te da los mismos silencios largos que reporta el verificador. Sirve de contraste: si los dos
coinciden, el hallazgo es sólido.

**Verificar el nivel de audio (LUFS):**
```bash
ffmpeg -i corte_final.mp4 -af loudnorm=print_format=summary -f null -
```
Objetivo para redes sociales: **entre −14 y −16 LUFS integrado**, con picos verdaderos bajo −1 dBTP.

### Verificar que el texto queda en zona segura

```bash
# Superpone las zonas prohibidas de un vertical 1080x1920
ffmpeg -i corte_final.mp4 -vf "drawbox=x=0:y=0:w=1080:h=250:color=red@0.35:t=fill,\
drawbox=x=0:y=1500:w=1080:h=420:color=red@0.35:t=fill,\
drawbox=x=900:y=250:w=180:h=1250:color=orange@0.30:t=fill,\
fps=1,scale=320:-1,tile=6x6" -frames:v 1 -q:v 2 zonas_seguras.jpg
```

Miras esa imagen. **Si algún texto aparece debajo del rojo, no se va a leer en la app.** No es opinión: es
donde la interfaz de Instagram y TikTok ponen sus botones.

Y la prueba complementaria, la de la uña, aplicada a todo el video:
```bash
ffmpeg -i corte_final.mp4 -vf "fps=1,scale=120:-1,tile=10x8" -frames:v 1 uña.jpg
```
Si a 120 px de ancho no distingues de qué va cada momento, tu texto es muy pequeño.

---

## El bucle completo, como script

```bash
#!/bin/bash
# verificar.sh — corre toda la verificación de un corte
V="$1"
[ -z "$V" ] && echo "uso: verificar.sh corte_final.mp4" && exit 1

echo "=== 1. INTEGRIDAD DEL ARCHIVO ==="
ffmpeg -v error -i "$V" -f null - 2>err.txt
[ -s err.txt ] && { echo "❌ ERRORES:"; cat err.txt; } || echo "✅ archivo sano"

echo -e "\n=== 2. ESPECIFICACIONES ==="
ffprobe -v error -show_entries format=duration,size,bit_rate \
  -show_entries stream=codec_type,codec_name,profile,width,height,r_frame_rate,pix_fmt \
  -of default=noprint_wrappers=1 "$V"

echo -e "\n=== 3. ¿HAY AUDIO? ==="
A=$(ffprobe -v error -select_streams a -show_entries stream=codec_name -of csv=p=0 "$V")
[ -z "$A" ] && echo "❌ SIN PISTA DE AUDIO" || echo "✅ audio: $A"

echo -e "\n=== 4. NIVEL DE AUDIO (objetivo −14 a −16 LUFS) ==="
ffmpeg -i "$V" -af loudnorm=print_format=summary -f null - 2>&1 | grep -E "Input (Integrated|True Peak)"

echo -e "\n=== 5. SILENCIOS DE MÁS DE 1,5 s ==="
ffmpeg -i "$V" -af "silencedetect=noise=-40dB:d=1.5" -f null - 2>&1 | grep silence_start

echo -e "\n=== 6. HOJA DE CONTACTOS → contactos_final.jpg ==="
ffmpeg -y -i "$V" -vf "fps=1,drawtext=text='%{pts\\:hms}':fontcolor=yellow:fontsize=26:\
box=1:boxcolor=black@0.7:x=6:y=6,scale=320:-1,tile=6x6" -frames:v 1 -q:v 2 contactos_final.jpg -loglevel error

echo "=== 7. ZONAS SEGURAS → zonas_seguras.jpg ==="
ffmpeg -y -i "$V" -vf "drawbox=x=0:y=0:w=iw:h=ih*0.13:color=red@0.35:t=fill,\
drawbox=x=0:y=ih*0.78:w=iw:h=ih*0.22:color=red@0.35:t=fill,\
fps=1,scale=320:-1,tile=6x6" -frames:v 1 -q:v 2 zonas_seguras.jpg -loglevel error

echo -e "\n=== 8. AUDIO PARA VERIFICACIÓN CON IA → verificar.wav ==="
ffmpeg -y -i "$V" -vn -acodec pcm_s16le -ar 16000 -ac 1 verificar.wav -loglevel error
echo "✅ Listo. Ahora manda verificar.wav al modelo con el prompt de verificación."
```

---

## Errores comunes

1. **Creer que "el comando corrió sin error" significa que el video quedó bien.** Solo significa que el
   archivo se escribió.
2. **Verificar sobre los brutos en vez del corte montado.** Los defectos los produce el montaje. Hay que
   verificar el resultado.
3. **Correr la verificación una vez y darla por hecha.** Si corriges algo, **vuelves a verificar**. Cada
   corrección puede introducir un defecto nuevo.
4. **Aplicar automáticamente todo lo que reporta el verificador.** Vas a borrar tus bloopers y cerrar tus
   bucles abiertos. El verificador reporta, tú decides.
5. **Ignorar todo el reporte porque "el primero que revisé era un falso positivo".** El costo de revisar
   siete hallazgos es cinco minutos. El costo de publicar uno real es la credibilidad del video.
6. **No pedir el segundo exacto.** Un hallazgo sin tiempo no se puede arreglar.
7. **No pedir estrictez explícitamente.** Sin esa instrucción el modelo es amable y te dice que suena bien.
8. **Verificar el audio antes de la mezcla final.** Si verificas solo la voz, pierdes la prueba de que la
   música no la tapa, que es media utilidad del bucle.
9. **Revisar el video a 2× de velocidad.** A esa velocidad no oyes una palabra partida. La verificación no
   se sustituye con "yo ya lo vi".
10. **Saltarse el final del video.** El defecto #3 de la lista real —el video que termina a media palabra—
    vive exactamente ahí, en el tramo que nadie revisa porque ya sabe qué dice.
11. **Fiarse solo de `silencedetect`.** Detecta silencios pero no sabe si una palabra quedó partida. Es
    complemento, no reemplazo.
12. **Publicar sin haber visto la hoja de contactos ni las zonas seguras.** Son dos comandos y treinta
    segundos.
13. **No verificar que el archivo tenga audio.** Exportar un video mudo es un error real y frecuente, y es
    devastador.
14. **Verificar solo en tu computador.** Reproduce el archivo final en un celular, con el volumen del
    celular, en la app real si se puede.

---

## Checklist final de 15 puntos antes de publicar

Ninguno es opcional. Si uno falla, no se publica.

- [ ] **1.** El archivo pasa `ffmpeg -v error -f null -` **sin ningún error**
- [ ] **2.** `ffprobe` confirma **resolución, fps y duración** esperados, con ancho y alto pares
- [ ] **3.** `pix_fmt` es **`yuv420p`** y el códec es **H.264 perfil High** (o el que pide la plataforma)
- [ ] **4.** El video **tiene pista de audio** (verificado con `ffprobe -select_streams a`)
- [ ] **5.** El nivel de audio está entre **−14 y −16 LUFS** integrado, picos bajo −1 dBTP
- [ ] **6.** Extraje el audio **del video ya montado y mezclado** y lo pasé por el bucle de verificación
- [ ] **7.** El reporte **no tiene ninguna palabra partida a media sílaba** sin resolver
- [ ] **8.** El reporte confirma que **el video termina con la última frase completa**
- [ ] **9.** El modelo **transcribió el audio completo sin huecos** → prueba de que la música no tapa la voz
- [ ] **10.** Cada hallazgo del reporte fue **clasificado** en arreglar / intencional / escuchar, y los
      dudosos los **escuché yo** en el segundo exacto
- [ ] **11.** Los silencios de más de 1,5 s son **todos intencionales** y lo confirmé oyéndolos
- [ ] **12.** Revisé la **hoja de contactos** del resultado final: sin negros, sin congelados, sin saltos de
      color
- [ ] **13.** Todo el texto está **dentro de la zona segura** (verificado con la superposición de zonas)
- [ ] **14.** El video se entiende **en silencio** (prueba del mudo) y **a 120 px** (prueba de la uña)
- [ ] **15.** Reproduje el archivo final **completo, a velocidad normal, en un celular real**, con el
      audio puesto — de principio a fin, incluido el último segundo

> Los primeros 14 puntos se pueden automatizar. **El punto 15 no.** Es cinco minutos de tu vida contra la
> pieza que va a representar a tu cliente delante de miles de personas. Hazlo.
