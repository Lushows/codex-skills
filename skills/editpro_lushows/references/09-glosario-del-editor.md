# 09 — Glosario del editor

Resuelve el problema de leer una instrucción técnica y no entender la mitad. Cada término está en
español sencillo, con el equivalente en inglés (porque las herramientas están en inglés) y con por qué
te importa a ti. Está agrupado por tema, no alfabético, porque los términos se entienden mejor en
compañía de sus vecinos.

**Cómo se usa:** cuando en una respuesta uses un término por primera vez, defínelo en una frase corta
tomada de aquí. No mandes al usuario a leer el glosario: dale la definición donde está el término.

---

## Montaje y cortes

| Término | Qué es y por qué te importa |
|---|---|
| **Corte** (*cut*) | el cambio de un plano a otro sin nada en medio. El 90% de los cortes de un video bueno son así |
| **Corte duro** (*hard cut*) | sinónimo de corte, dicho para diferenciarlo de una transición |
| **Transición** | cualquier cosa entre dos planos: fundido, barrido, zoom. Cuesta atención; se usa cuando comunica algo (paso de tiempo, cambio de bloque), no por decorar |
| **Fundido** (*fade*) | la imagen aparece desde negro o desaparece hacia negro |
| **Fundido encadenado** (*dissolve*) | un plano se disuelve dentro del siguiente. Lee como "pasó tiempo" o "esto es un recuerdo". En video corto casi nunca hace falta |
| **J-cut** | el **audio** del plano siguiente empieza **antes** de que se vea ese plano. Suaviza el cambio sin usar transición. Lo más rentable y más ignorado del video vertical |
| **L-cut** | el audio del plano actual **sigue sonando** después de que la imagen ya cambió. Evita que una frase se corte cuando ya muestras otra cosa |
| **Jump cut** | cortar dentro del mismo plano quitando un pedazo; la persona "salta". Antes era error; hoy es el lenguaje estándar de YouTube y de los reels |
| **Match cut** | cortar entre dos imágenes parecidas en forma, color o movimiento, de modo que el cerebro las une. El fósforo → el sol de *Lawrence de Arabia* es el ejemplo canónico |
| **Cutaway** | plano de otra cosa insertado en medio de una acción; permite tapar un salto o quitar tiempo. En entrevista: cortar a las manos mientras se quita una muletilla |
| **Insert** | plano detalle intercalado que muestra algo específico: el producto, un número, una pantalla |
| **B-roll** | todo el material complementario. El talking head es el A-roll; los planos del local, las manos y el producto son b-roll. Sin b-roll no hay dónde cortar y el video se ve plano |
| **Raccord** | que dos planos peguen en posición, gesto, luz, ropa y objetos. Del francés *raccorder*, empalmar. En inglés, *continuity* |
| **Eje de acción / 180°** | la línea invisible que une a dos personas o marca una dirección. La cámara se queda de un solo lado; si se cruza, las posiciones se invierten y el espectador se desorienta |
| **Elipsis** | quitar tiempo sin que se note. Sale de la casa y en el plano siguiente ya está en el carro; nadie extraña los 40 segundos de caminata |
| **Punch-in** | agrandar digitalmente un plano para simular una cámara más cercana. Grabando en 4K y entregando en 1080 tienes margen de sobra: es tu segunda cámara gratis. Mínimo 25% o se lee como error de encuadre |
| **Reencuadre** | mover el recorte dentro del cuadro final, por ejemplo al pasar de 16:9 a 9:16 sin dejar a la persona descentrada |
| **Corte bruto** (*rough cut*) | el montaje con la estructura completa pero sin pulir. Se ve feo a propósito |
| **Corte fino** (*fine cut*) | el montaje con los cortes ajustados al décimo de segundo |
| **Máster** | el archivo final del que salen todas las versiones |

---

## Tiempo y fotogramas

**fps** (*frames per second*, fotogramas por segundo) — cuántas imágenes hay en cada segundo. Los
valores comunes: **24** (cine), **25** (televisión europea/PAL), **29,97 o 30** (redes sociales),
**50/60** (deportes, cámara lenta), **120/240** (solo para ralentizar).

**Fotograma** (*frame*) — cada imagen individual. A 30 fps, un fotograma dura 0,033 s.

**Timecode** — la posición exacta dentro de un video, escrita `HH:MM:SS:FF` (horas:minutos:segundos:
fotogramas). `00:01:23:12` es 1 minuto, 23 segundos y 12 fotogramas.

> **Trampa importante:** cuando le des una instrucción a una herramienta o a un modelo, usa **una sola
> unidad** y que sea segundos decimales: "corta en el segundo 83,4", no "cerca del minuto 1:23". Mezclar
> unidades produce cortes en el sitio equivocado. Ver `15` y `124`.

**Drop frame / non-drop frame** — un lío heredado de la televisión NTSC: 29,97 fps no es 30 exacto, y
para que el timecode cuadre con el reloj se saltan números. Solo importa si trabajas con material de
broadcast. En redes, ignóralo.

**Cámara lenta** (*slow motion*) — reproducir a menos velocidad de la grabada. Solo se ve bien si se
grabó a más fps de los que se entregan: grabar a 60 y entregar a 30 da media velocidad limpia. Ralentizar
material de 30 fps produce saltos o fotogramas inventados.

**Speed ramp** — cambiar la velocidad progresivamente dentro de un mismo plano. Muy usado como
transición en reels.

---

## Imagen: resolución y forma

**Resolución** — cuántos píxeles tiene la imagen, ancho por alto. `1080x1920` es un vertical de
teléfono; `1920x1080` es un horizontal; `3840x2160` es 4K.

**Relación de aspecto** (*aspect ratio*) — la forma del cuadro: **16:9** horizontal, **9:16** vertical,
**1:1** cuadrado, **4:5** el vertical del feed de Instagram.

**SAR** (*Sample Aspect Ratio*) — la forma de cada píxel individual. Normalmente es 1:1 (píxeles
cuadrados).

**DAR** (*Display Aspect Ratio*) — la forma con la que se debe mostrar el video en pantalla.

> **Por qué te importa el par SAR/DAR:** si un archivo tiene píxeles no cuadrados y una herramienta los
> ignora, el video sale **estirado o aplastado**. Es una de las causas más frecuentes de "se ve raro y
> no sé por qué". Se verifica con `ffprobe` mirando `sample_aspect_ratio` y `display_aspect_ratio`.

**Rotación por metadato** — los celulares graban siempre en horizontal y le pegan al archivo una
etiqueta que dice "gíralo 90°". Algunas herramientas la respetan y otras no. Resultado: un video que en
tu teléfono se ve vertical y en el render sale acostado. Se detecta con `ffprobe` buscando `rotate` o
el `displaymatrix`.

**Escalado** (*scaling*) — cambiar el tamaño de la imagen. Reducir es casi gratis en calidad; ampliar
siempre pierde. Por eso se graba grande y se entrega pequeño.

**Zona segura** (*safe area*) — la parte del cuadro donde la interfaz de la aplicación **no** tapa nada.
En Reels y TikTok, la parte de arriba y una franja gruesa de abajo están ocupadas por botones,
descripción y nombre de usuario. El texto que caiga ahí es texto que nadie lee.

---

## Códecs, archivos y compresión

**Códec** — la fórmula con la que se comprime el video. Los que vas a ver: **H.264** (el universal, lo
abre todo), **H.265/HEVC** (mejor compresión, menos compatible), **AV1** (moderno, eficiente, aún
irregular), **ProRes** (calidad alta para trabajar, archivos enormes), **VP9** (YouTube).

**Contenedor** — la caja que envuelve el video, el audio y los subtítulos: `.mp4`, `.mov`, `.mkv`. No es
lo mismo que el códec. Un `.mp4` puede llevar H.264 o H.265 adentro. Cuando alguien dice "mándamelo en
MP4", está hablando de la caja, no del contenido.

**Bitrate** — cuántos datos por segundo usa el video, en **Mbps** (megabits por segundo). Más bitrate =
más calidad y archivo más pesado. Un vertical de 1080 para redes vive bien entre 6 y 12 Mbps.

**CRF** (*Constant Rate Factor*, factor de calidad constante) — la forma inteligente de comprimir con
x264/x265: en vez de fijar el bitrate, fijas la **calidad** y el codificador usa los datos que necesite.
Escala de 0 a 51, donde **menos es mejor**:

| CRF | Para qué |
|---|---|
| 16–18 | máster de trabajo, prácticamente sin pérdida visible |
| 19–21 | entrega de alta calidad |
| 22–23 | el estándar razonable para redes |
| 26+ | se empieza a notar la degradación |

**GOP** (*Group of Pictures*) — cada cuántos fotogramas se guarda una imagen completa (fotograma clave)
en vez de solo las diferencias. Un GOP corto facilita buscar y cortar; uno largo comprime mejor.

**Fotograma clave** (*keyframe* en compresión, también *I-frame*) — un fotograma guardado completo. Ojo
con la ambigüedad: en animación, *keyframe* significa otra cosa (ver más abajo).

**Pixel format / pix_fmt** — cómo se guardan los colores. El valor seguro para compatibilidad universal
es **`yuv420p`**. Si exportas en `yuv444p` o `yuv422p`, algunos reproductores y algunas redes no lo
abren o lo muestran mal.

**Perfil y nivel** (*profile / level*) — variantes de H.264 con más o menos funciones. `high` con nivel
`4.0` o `4.2` es lo compatible para redes.

**Faststart** — mover la información de índice al principio del archivo para que empiece a reproducirse
antes de terminar de descargarse. Se activa con `-movflags +faststart` y debería estar siempre en
cualquier archivo que vaya a la web.

**Transcodificar** — convertir de un códec a otro. Cada transcodificación pierde calidad; por eso se
trabaja desde el bruto y no desde un render anterior.

**Proxy** — una copia liviana y de baja resolución del material, para poder editar sin que el
computador sufra. Al final se vuelve a los originales.

---

## Audio

**dB** (decibelio) — la unidad con que se mide el nivel de sonido. Es una escala **relativa y
logarítmica**: en video, 0 dB es el techo absoluto y todo lo demás son números negativos. Una voz sana
vive entre -18 y -6 dB.

**dBFS** (*decibels relative to Full Scale*) — la escala de dB en digital, donde 0 es el máximo posible
y pasarse produce distorsión.

**Pico** (*peak*) — el punto más alto que alcanza la señal.

**Pico real** (*true peak*, dBTP) — el pico calculado teniendo en cuenta lo que pasa entre muestras al
reconvertir a analógico. Puede ser más alto que el pico digital. Las plataformas piden dejarlo en
**-1,0 o -1,5 dBTP** para que no sature en el teléfono del espectador.

**Clipping / saturación** — cuando la señal pasa de 0 dB y se recorta. Suena a distorsión sucia y **no
tiene arreglo**: la información ya no está. Se previene, no se corrige.

**LUFS** (*Loudness Units relative to Full Scale*) — la medida de qué tan fuerte se **percibe** un audio
en promedio, no en su pico. Es lo que usan las plataformas para normalizar el volumen de todos los
videos. Referencias a agosto de 2026:

| Destino | Objetivo |
|---|---|
| Instagram / TikTok / redes en general | -14 LUFS integrados |
| YouTube | -14 LUFS |
| Spotify (referencia de podcast) | -14 LUFS |
| Televisión (norma EBU R128) | -23 LUFS |

Si entregas a -20 LUFS, tu video suena más bajo que el de al lado y pierdes. Si entregas a -8, la
plataforma lo baja y de paso lo aplasta.

**LRA** (*Loudness Range*) — cuánta diferencia hay entre las partes suaves y las fuertes. Un LRA muy
alto en video corto significa que el espectador va a tener que subir y bajar el volumen.

**Compresión de audio** — reducir la diferencia entre lo suave y lo fuerte para que todo se oiga
parejo. Nada que ver con la compresión de archivo.

**Ecualización** (*EQ*) — subir o bajar bandas de frecuencia. Quitar graves para eliminar retumbe,
subir 3–5 kHz para dar presencia, controlar 6–8 kHz para las eses.

**Sibilancia** — el exceso de "s" y "ch" que hace daño al oído. Se controla con un *de-esser*.

**Ducking** — que la música baje automáticamente cuando alguien habla y vuelva a subir cuando calla.
Es lo que separa un video amateur de uno profesional en un solo paso. En ffmpeg se hace con
`sidechaincompress`.

**Gate / puerta de ruido** — corta el sonido cuando está por debajo de un umbral, para silenciar el
ambiente entre frases. Mal calibrado produce cortes bruscos que suenan peor que el ruido.

**Lecho de ambiente** (*room tone*) — una capa continua de sonido ambiente que se pone debajo de todo
para que los cortes no se noten. Si cada clip tiene un fondo distinto, esto los une.

**Sample rate** — cuántas muestras por segundo tiene el audio. **48 kHz** es el estándar de video;
44,1 kHz es el de música. Mezclarlos sin convertir produce desincronización lenta.

**Whoosh / riser / impacto** — los tres efectos de diseño sonoro más usados: el barrido de transición,
la subida de tensión y el golpe. Se gastan rápido por habituación (ver `06`).

---

## Color

**Luma** — la información de brillo de la imagen, sin color.

**Croma** — la información de color, sin brillo. También, en otro sentido, el **fondo verde o azul** que
se usa para recortar (*chroma key*): se elimina ese color para dejar transparente lo que hay detrás.

**Corrección de color** — dejar la imagen neutra y técnicamente correcta: exposición bien, blancos
blancos, contraste sano. **Va primero, siempre.**

**Gradación de color** (*color grading*) — darle un look, un carácter. **Va después de corregir.**
Aplicar un look sobre una imagen mal expuesta amplifica el error.

**Balance de blancos** — ajustar para que lo que es blanco se vea blanco. Si está mal, todo tira a azul
o a naranja.

**Temperatura** — qué tan cálida (naranja) o fría (azul) está la imagen. Se mide en Kelvin.

**Saturación** — cuánta intensidad tiene el color. Cero saturación es blanco y negro.

**LUT** (*Look-Up Table*, tabla de consulta) — un archivo (`.cube` normalmente) con una transformación
de color predefinida. Se aplica y toda la imagen cambia de look. Sirve para dar carácter rápido; **no
sirve para imponer una paleta de marca** — para eso se usa duotono.

**Duotono** — mapear toda la imagen a dos colores: uno para las sombras y otro para las luces. Es la
forma real de imponer una paleta de marca a material que viene de fuentes distintas. Ver `64`.

**Scope** — un instrumento de medición de la imagen. Los tres que se usan:

- **Histograma** — cuántos píxeles hay en cada nivel de brillo. Detecta zonas quemadas y aplastadas.
- **Forma de onda** (*waveform*) — el brillo distribuido a lo largo del ancho de la imagen.
- **Vectorscopio** — la distribución de los colores. Tiene una línea marcada de tono de piel; si la
  piel de tu sujeto no cae cerca de esa línea, está verde o naranja.

**Se lee el scope, no el monitor.** El monitor miente según su calibración, su brillo y la luz de la
habitación.

**Rango dinámico** — cuánta diferencia entre lo más oscuro y lo más claro puede capturar la cámara.

**Log** — un modo de grabación plano y sin contraste que guarda más información para poder gradar
después. Material en log **sin gradar** se ve lavado y feo; eso no es un error, es que falta el paso.

**Banding** — escalones visibles en un degradado (típico en cielos y fondos lisos). Aparece cuando se
comprime mucho o se procesa a poca profundidad de bits. Se disimula con un poco de grano.

**Viñeta** — oscurecer los bordes del cuadro para dirigir el ojo al centro. Sutil funciona; evidente
se ve barato.

---

## Gráficos, texto y animación

**Alfa** (*alpha channel*) — el canal de transparencia de una imagen. Un PNG con alfa tiene zonas
transparentes; un JPG **nunca** puede tenerlas. Si pides un logo "sin fondo" y te mandan un JPG, te
mandaron un logo con fondo blanco.

**Keyframe** (en animación) — un punto en el tiempo donde defines un valor (posición, tamaño, opacidad).
La herramienta calcula lo que hay entre dos keyframes. Ojo con la ambigüedad: en compresión de video,
*keyframe* significa otra cosa.

**Interpolación** — cómo se calcula el movimiento entre dos keyframes. **Easing** es la curva de esa
interpolación: **lineal** = velocidad constante, y es lo que hace que un motion se vea barato, porque
en la naturaleza nada se mueve a velocidad constante. *Ease out* (entra rápido y frena) se usa el 80%
de las veces.

**Overshoot / sobre-impulso** — el elemento se pasa un poco de su posición final y regresa. Es lo que
da la sensación de "golpe" en el texto de los reels. **Anticipación** es lo contrario: un movimiento
pequeño en dirección opuesta antes del movimiento principal. Los dos son de los 12 principios de Disney.

**Lower third / rótulo** — el gráfico que aparece abajo para presentar a alguien o dar un dato.
**Kinetic type / tipografía cinética** es texto animado que es el elemento principal del video, no un
subtítulo.

**Subtítulo quemado** (*burned-in*) — el texto va grabado en los píxeles del video; no se puede apagar.
Es lo estándar en redes.

**Subtítulo cerrado** (*closed caption*) — el texto va como pista aparte y el espectador lo activa o
desactiva. Es lo estándar en YouTube y lo correcto para accesibilidad.

**SRT** — el formato de subtítulos más simple: tiempos y texto plano, sin estilos.

**ASS** (*Advanced SubStation Alpha*) — el formato de subtítulos con estilos: fuente, color, contorno,
sombra, posición, animación. Es lo que se usa con `libass` en ffmpeg para subtítulos que se ven bien.

**Zona segura de texto** — ver arriba, en la sección de imagen. Es donde el texto sí se lee.

---

## Producción y organización

| Término | Qué es y por qué te importa |
|---|---|
| **Bruto** (*raw footage*) | el material original, sin tocar |
| **Ingesta** | copiar, verificar y organizar el material antes de trabajar |
| **Hoja de contactos** | una imagen con muchos fotogramas en cuadrícula; permite ver un video largo de un vistazo |
| **Transcripción con timecodes** | el texto de lo que se dice, con el segundo en que se dice. Convierte el video en algo buscable; es el documento más útil de un proyecto con voz |
| **A-roll** | el material principal, normalmente la persona hablando |
| **Talking head** | el plano de alguien hablando a cámara. El formato base de casi todo el contenido de marca |
| **Cobertura** | cuánto material distinto tienes de la misma acción. Poca cobertura = pocos sitios donde cortar = video plano |
| **Blooper / toma falsa** | el error, la risa, el momento en que se equivocó. No es basura: suele ser el material más humano del proyecto |
| **EDL / XML / AAF** | formatos para pasar un montaje de un programa a otro sin perder la línea de tiempo |
| **Render** | el proceso de generar el archivo final |
| **Loop** | un video montado para que el final empalme con el principio sin costura. Sube el tiempo de reproducción porque la gente lo ve dos veces sin darse cuenta |

---

## Distribución y métricas

| Término | Qué es y por qué te importa |
|---|---|
| **CTWA** (*Click To WhatsApp*) | el anuncio de Meta que abre una conversación de WhatsApp en vez de llevar a una web. El formato dominante para venta en Colombia |
| **Retención** | el porcentaje de gente que sigue viendo en cada segundo. La curva de retención es el diagnóstico más honesto de un video |
| **Tasa de finalización** | porcentaje que llega al final. Es lo que más sube con un bucle abierto bien cerrado |
| **Gancho** (*hook*) | el primer segundo. Lo que decide si te ven |
| **Bucle abierto** (*open loop*) | plantear algo incompleto que obliga a quedarse para cerrarlo |
| **Remate** | el final del video, donde va la acción que quieres que hagan |
| **CTA** (llamado a la acción) | la instrucción concreta: "escríbeme", "comenta CALC", "link en la bio" |
| **Normalización de volumen** | lo que hacen las plataformas para que todos los videos suenen parejo. Es la razón por la que los LUFS importan |
| **Content ID** | el sistema de YouTube que detecta música con derechos. Puede desmonetizar o bloquear un video, incluso con una licencia comprada pero mal documentada |

---

## Errores comunes

- **Confundir códec con contenedor.** "Mándamelo en MP4" no dice nada sobre el códec de adentro.
- **Confundir bitrate con calidad.** Bitrate alto sobre material ya degradado no recupera nada.
- **Confundir compresión de audio con compresión de archivo**, o los dos significados de *keyframe*
  (compresión vs animación).
- **Confundir corrección con gradación**, y hacerlas en el orden equivocado.
- **Creer que un LUT impone la paleta de marca.** Para eso es el duotono.
- **Pedir un logo "sin fondo" y aceptar un JPG.** El JPG no tiene canal alfa. Nunca.
- **Ignorar SAR/DAR** (video estirado) o **la rotación por metadato** del celular (video acostado).
- **Exportar sin `yuv420p`** o sin `-movflags +faststart` en un archivo que va a la web.
- **Ralentizar material grabado a 30 fps** y culpar al programa de los saltos.
- **Mezclar unidades de tiempo** ("cerca del minuto 1:23"). Siempre segundos decimales.
- **Mezclar 44,1 kHz con 48 kHz** sin convertir, y descubrir la desincronización al final.
- **Creer que el clipping se arregla.** Una vez saturado, la información ya no existe.
- **Juzgar el color en el monitor** en vez de en los scopes.

---

## Checklist

Para usar bien este glosario:

- [ ] Cada término técnico que uso con el usuario lo definí en una frase la primera vez.
- [ ] La definición va **junto al término**, no en un enlace al glosario.
- [ ] Cuando digo un número, digo la unidad (dB, LUFS, Mbps, fps, segundos).
- [ ] Cuando doy un tiempo, lo doy en **segundos decimales**, en una sola unidad.
- [ ] Diferencié códec de contenedor al hablar de formatos.
- [ ] Diferencié corrección de gradación al hablar de color.
- [ ] Diferencié los dos sentidos de *keyframe* si aparecen los dos.
- [ ] Al pedir gráficos, especifiqué PNG con canal alfa o SVG, nunca JPG.
- [ ] Verifiqué SAR/DAR y rotación antes de confiar en un archivo de origen.
- [ ] Al exportar para web, incluí `yuv420p` y `+faststart`.
