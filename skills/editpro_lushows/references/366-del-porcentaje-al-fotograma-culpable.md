# 366 — Del porcentaje al fotograma culpable: el laboratorio

> `301` te enseñó a leer la curva: las formas, qué significa cada una, y la fórmula para pasar de
> porcentaje a segundo. Este módulo es lo que viene después: **el peritaje**. Tienes un segundo
> sospechoso; ahora hay que imputarle la culpa a un fotograma concreto, con pruebas, y no al primero que
> te parezca. Es un procedimiento de nueve pasos que se hace en 15 minutos y se puede repetir igual
> siempre.

---

## El principio del peritaje

> **La gente no se va por lo que está pasando en el segundo de la caída. Se va por lo que dejó de pasar
> unos fotogramas antes.**

Esto es lo que casi todo el mundo hace mal. Ves que la curva cae en el 7,5 y miras el fotograma del 7,5.
Pero la decisión de irse toma entre **0,3 y 0,8 segundos** en convertirse en un deslizamiento de dedo, y
además la plataforma cuenta la salida cuando termina de ocurrir.

**La ventana de la culpa está entre 0,8 y 0,2 segundos ANTES del punto de caída.** Ahí es donde hay que
buscar. Todo el procedimiento se basa en eso.

---

## Paso 1 — Fijar la base: duración exacta y fotogramas por segundo

```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 reel.mp4
# 41.933000

ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate,nb_frames -of csv=p=0 reel.mp4
# 30000/1001,1256
```

Anota los tres números. `30000/1001` son 29,97 fps: cada fotograma dura **0,0334 s**. Ese es tu grano
mínimo; no tiene sentido discutir diferencias más finas.

---

## Paso 2 — Convertir el punto de caída a segundos y a número de fotograma

```
segundo   = porcentaje × duración
fotograma = segundo × fps
```

Caída en el 18% de 41,933 s → **7,548 s** → fotograma **226**.

Y la ventana de la culpa:

```
inicio de ventana = segundo - 0,8   →  6,748 s  →  fotograma 202
fin de ventana    = segundo - 0,2   →  7,348 s  →  fotograma 220
```

Son 18 fotogramas. Ahí está el culpable.

---

## Paso 3 — Sacar la ventana entera, fotograma por fotograma

No en tira: **uno por uno**, para poder pasarlos con las flechas.

```bash
mkdir -p peritaje
ffmpeg -y -ss 6.748 -i reel.mp4 -t 0.65 -vsync 0 -q:v 2 "peritaje/f_%03d.jpg"
```

Y también la tira, para ver el conjunto:

```bash
ffmpeg -y -ss 6.5 -i reel.mp4 -t 1.5 -vf \
"fps=30,scale=180:-1,drawtext=text='%{pts\:hms}':x=3:y=3:fontsize=13:fontcolor=yellow:box=1:boxcolor=black@0.6,tile=9x5" \
-frames:v 1 peritaje/ventana.png
```

---

## Paso 4 — Marcar los eventos objetivos de la ventana

Antes de opinar, lista lo que **objetivamente** ocurre ahí. Tres consultas:

```bash
# cortes de plano
ffprobe -v error -f lavfi "movie=reel.mp4,select=gt(scene\,0.35)" -show_entries frame=pkt_pts_time -of csv=p=0

# nivel de audio segundo a segundo
ffmpeg -y -i reel.mp4 -af "astats=metadata=1:reset=30,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=peritaje/audio.txt" -f null -

# silencios
ffmpeg -y -i reel.mp4 -af "silencedetect=noise=-40dB:d=0.25" -f null - 2>&1 | grep silence
```

Ahora tienes, para la ventana 6,748–7,348: qué cortes hay, si el audio bajó, si hubo silencio.

---

## Paso 5 — La tabla de imputación

Recorre la ventana con esta tabla. **Marca todo lo que aplique**, no te quedes con el primero.

| # | Sospechoso | Cómo se comprueba | Frecuencia |
|---|---|---|---|
| 1 | **Plano que se estira** | El corte anterior está a más de 4 s de la ventana | Muy alta |
| 2 | **Se acabó la información** | En la ventana no entra ningún dato, imagen o giro nuevo | Muy alta |
| 3 | **Silencio o bajón de audio** | `silencedetect` marca ahí, o el RMS cae más de 6 dB | Alta |
| 4 | **Cambio de registro brusco** | El plano antes y el de después son "otro video" | Alta |
| 5 | **Texto que tapa o que obliga a leer** | Hay más de 3 palabras simultáneas en pantalla | Media |
| 6 | **Se reveló la respuesta** | El bucle se cerró antes de tiempo: ya no hay razón para seguir | Media |
| 7 | **Repetición** | Se dice o se muestra algo que ya se dijo o se mostró | Media |
| 8 | **Imagen fea o confusa** | Desenfoque, movimiento de cámara mareado, contraluz | Baja |
| 9 | **Fundido, transición o logo** | Cualquier efecto que anuncia "fin de sección" | Baja pero letal |
| 10 | **Cara nueva sin presentar** | Aparece alguien que el espectador no sabe quién es | Baja |

Si marcaste **cero**, no estás mirando la ventana correcta: amplíala a −1,5 s y vuelve al paso 3.

Si marcaste **más de tres**, el problema no es un fotograma: es que ese tramo del video no debería
existir. Córtalo entero.

---

## Paso 6 — El diagnóstico diferencial: imagen, audio o sentido

Tres pases sobre el mismo tramo, cada uno cortando un canal. Es la parte que separa el peritaje serio
del "a mí me parece".

```bash
ffmpeg -y -ss 5.5 -i reel.mp4 -t 3.5 -c copy peritaje/tramo.mp4          # el tramo
ffmpeg -y -i peritaje/tramo.mp4 -an -c:v copy peritaje/A_mudo.mp4        # A) solo imagen
ffmpeg -y -i peritaje/tramo.mp4 -vn peritaje/B_audio.wav                 # B) solo audio
ffmpeg -y -i peritaje/tramo.mp4 -vf "crop=1080:700:0:200" -an peritaje/C_sin_texto.mp4  # C) sin la franja del texto
```

Y pregúntate, en este orden:

- **Viendo A (mudo):** ¿pasa algo? Si no pasa nada visible, el culpable es visual.
- **Oyendo B (a ciegas):** ¿hay energía, hay información, hay silencio? Si hay hueco, el culpable es
  sonoro.
- **Viendo C:** ¿el video se sostiene sin el texto? Si sin texto no queda nada, el tramo dependía de leer,
  y leer es donde la gente se va.

El culpable es el canal donde **falta** algo, no donde sobra.

---

## Paso 7 — La contraprueba del vecino

Antes de acusar, comprueba que el tramo anterior estaba bien. Muchas veces el fotograma culpable es
inocente: el daño lo hizo el tramo de antes, que dejó al espectador con la mano en el aire.

Saca el tramo de **3 segundos anteriores** a la ventana y aplícale la misma tabla del paso 5. Si ahí
también marcas 2 o 3 sospechosos, el culpable real es ese, y la caída solo es el momento en que la
paciencia se acabó.

**La firma de esto en la curva:** una pendiente que se va inclinando desde antes, en vez de un escalón
limpio. Escalón = culpa local. Pendiente creciente = culpa acumulada.

---

## Paso 8 — Escribir la sentencia

En una línea, en tu diario (`306`). Formato fijo:

```
[fecha] [video] caída 18% = 7,55 s = fotograma 226
ventana 6,75-7,35 · sospechosos: #1 plano de 8,2 s, #2 sin información
diagnóstico: visual · culpa local
arreglo: cortar el plano a 1,4 s + inserto de parrilla
```

Sin esa línea escrita, el peritaje no sirve de nada: la lección se evapora en tres días.

---

## Paso 9 — Reparar y verificar que reparaste

Repara (los cuatro parches están en `365`), exporta, y **comprueba el archivo**, no la intención:

```bash
# ¿el plano largo se fue?
ffprobe -v error -f lavfi "movie=reel_v2.mp4,select=gt(scene\,0.35)" -show_entries frame=pkt_pts_time -of csv=p=0

# ¿la duración cambió lo que esperabas?
ffprobe -v error -show_entries format=duration -of csv=p=0 reel_v2.mp4

# ¿el tramo reparado se ve como quiero?
ffmpeg -y -ss 5.5 -i reel_v2.mp4 -t 3.5 -vf "fps=6,scale=200:-1,tile=7x3" -frames:v 1 verificacion.png
```

Y la verificación del corte completa, con transcripción incluida, está en `98`. **No publiques un
arreglo sin verificar el archivo exportado.** El error más humillante es reparar en la línea de tiempo y
subir el export viejo.

---

## Los cuatro engaños de la curva (léelos antes de acusar a nadie)

1. **Pocos puntos.** El gráfico de Instagram tiene una resolución gruesa: no te va a decir "7,55 s", te
   va a mostrar una pendiente. Úsalo para saber **en qué tercio** cayó y afina con la tira de contactos.
   TikTok da más detalle.
2. **Las repeticiones inflan.** Si la gente reproduce dos veces, hay tramos que pueden superar el 100% o
   verse antinaturalmente planos. Un repunte al final casi siempre es gente repitiendo el inicio, no
   gente entrando (ver `367`).
3. **Muestras chicas mienten.** Con 200 reproducciones, una curva es ruido con forma. No hagas peritaje
   de un video con pocas vistas: espera, o suma varios videos parecidos (ver `369`).
4. **La distribución no es el video.** Si un video se mostró a público muy distinto al habitual, la curva
   compara peras con manzanas. Anota siempre si el video salió en otro tipo de público.

---

## Caso completo, de punta a punta

**Video:** 41,9 s, la parrilla. **Síntoma:** escalón entre el 15% y el 20%.

1. Base: 41,933 s · 29,97 fps. 18% → **7,548 s** → fotograma 226. Ventana: 6,748–7,348.
2. `scene detect`: último corte en **3,10 s** y el plano seguía hasta 11,3. Plano de **8,2 s**.
3. Tabla: sospechosos #1 (plano estirado) y #2 (sin información nueva). Audio normal, sin silencio.
4. Diferencial: en mudo no pasa nada; en audio hay voz explicando de dónde viene la carne → culpa
   **visual**. Vecino: el tramo 3,5–6,5 era el mismo plano → culpa **acumulada**, no local.
5. Arreglo: plano recortado a 1,4 s, la explicación de la carne movida al segundo 22, inserto de fuego
   de 2 s en el hueco. Verificado en el export: cortes ahora en 3,10 · 4,52 · 6,48 · 8,10.

Tiempo total: 14 minutos. Sin grabar nada nuevo.

---

## Errores comunes

1. Mirar el fotograma exacto de la caída en vez de la ventana de 0,8 a 0,2 segundos antes.
2. Calcular el segundo con la duración redondeada en vez de la de `ffprobe`.
3. Cortar el tramo con `-c copy` para inspeccionarlo y quedarse con otro tramo (salta al fotograma clave).
4. Quedarse con el primer sospechoso de la tabla sin revisar los diez.
5. No hacer el diferencial de canales y decidir "es que está aburrido", que no es un diagnóstico.
6. Acusar a un fotograma cuando la culpa era acumulada del tramo anterior.
7. Hacer peritaje sobre un video con muy pocas reproducciones: estás leyendo ruido.
8. Confundir un repunte final con gente que llegó, cuando son repeticiones.
9. Comparar la curva de un video que salió a público nuevo con la de uno que vio tu público de siempre.
10. Reparar en CapCut y verificar en CapCut. Se verifica en el **archivo exportado**.
11. No escribir la sentencia. Sin registro, en un mes repites el mismo error.
12. Republicar el mismo video "arreglado" el mismo día y comparar los dos: el segundo arranca en
    desventaja porque el público ya lo vio (ver `369`).
13. Buscar un culpable único cuando marcaste cuatro sospechosos: ese tramo hay que borrarlo, no repararlo.

---

## Checklist

- [ ] Tengo duración exacta y fps reales del archivo
- [ ] Convertí el porcentaje a segundo y a número de fotograma
- [ ] Definí la ventana de culpa: de −0,8 s a −0,2 s del punto de caída
- [ ] Saqué los fotogramas de la ventana uno por uno y la tira de conjunto
- [ ] Corrí detección de cortes, niveles de audio y silencios sobre ese tramo
- [ ] Recorrí la tabla de los diez sospechosos completa
- [ ] Hice el diferencial de tres canales: mudo, solo audio, sin texto
- [ ] Revisé el tramo anterior para descartar culpa acumulada
- [ ] Escribí la sentencia en una línea en el diario
- [ ] Reparé y verifiqué sobre el archivo exportado, no sobre la línea de tiempo
- [ ] Comprobé que la muestra era suficiente antes de sacar conclusiones
