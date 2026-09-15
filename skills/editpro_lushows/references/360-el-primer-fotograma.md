# 360 — El primer fotograma: la portada que nadie eligió

> Tu video tiene una portada aunque tú no la hayas elegido: es el fotograma 0. Se muestra congelado
> durante la fracción de segundo en que el feed decide si reproduce, aparece en la vista previa de
> WhatsApp, y es lo que queda si el video carga lento. Nadie lo diseña. Por eso está casi siempre mal.
> `94` cubre la portada de la grilla (otra cosa, otro trabajo). Este módulo es solo el fotograma 0.

---

## Las tres superficies donde vive una imagen fija de tu video

| Superficie | Qué imagen se muestra | ¿La eliges tú? |
|---|---|---|
| **Feed / Para ti** (reproducción automática) | El **fotograma 0** del archivo | No, sale del montaje |
| **Grilla del perfil** | La **portada** (cover) que definiste en la app | Sí, en el momento de publicar |
| **Enlace compartido** (WhatsApp, DM, navegador) | Depende: a veces la portada, a veces un fotograma cercano al inicio | A medias |

La confusión más cara de todas: creer que la portada bonita que elegiste en Instagram protege el
arranque del video. **No lo hace.** En el feed en desplazamiento, la portada de la grilla no existe. Ahí
manda el fotograma 0 y nada más.

Traducción operativa: **la portada la eliges al publicar, el fotograma 0 lo eliges al montar.** Son dos
decisiones distintas, en dos momentos distintos, y solo una de las dos afecta la retención.

---

## Lo que está verificado (a agosto de 2026)

- **Instagram** reemplazó la "tasa de visualización" por la **tasa de salto** — el porcentaje de vistas
  de gente que se va **durante los primeros 3 segundos** — y agregó un **gráfico de retención por reel**.
  Anunciado el **24 de agosto de 2025** (Social Media Today) y desplegado del todo, incluida la API de
  Insights, en **abril de 2026**. Es decir: hoy tienes un número que mide exactamente el trabajo del
  fotograma 0 y del primer segundo.
- **TikTok** permite desde **mayo de 2026** (reportado; confírmalo en tu app, va por oleadas) poner un
  **título sobre la portada**, que se ve en la grilla del perfil. Si lo usas, el título y el primer
  fotograma tienen que prometer lo mismo o rompes la expectativa en el peor momento posible.
- **No existe un umbral oficial** publicado por Meta ni por TikTok que diga "una tasa de salto sana es
  X%". Los números que circulan en blogs de herramientas son estimaciones de vendedores, sin metodología
  publicada. El único punto de comparación honesto es **tu propio historial** (ver `369`).

---

## Los seis criterios de un buen fotograma 0

Aplícalos en este orden. Si el candidato falla el primero, no sigas.

### 1. La prueba de la uña
Reduce el fotograma a **120 píxeles de alto** y míralo un segundo. Si no puedes decir *qué es* y *dónde
pasa*, no sirve. En el feed real vas a tener menos tiempo y peor luz que en tu escritorio.

```bash
ffmpeg -y -i reel.mp4 -frames:v 1 -vf "scale=-1:120" prueba_uña.png
```

### 2. Una cosa, no una escena
Un plano general del bar no dice nada en 300 ms. Una mano cortando, una chapa saltando, una cara con
gesto: eso sí. **Un sujeto que ocupa entre el 30% y el 60% del cuadro.**

### 3. Movimiento ya empezado (aunque sea una foto fija)
El fotograma 0 debe estar **a mitad de un gesto**: el cuchillo bajando, la espuma subiendo, la boca
abierta a mitad de una palabra. Un fotograma de alguien quieto esperando su turno se lee como "esto no
ha empezado", y lo que no ha empezado se salta.

### 4. Contraste que se lee a un metro
Sujeto claro sobre fondo oscuro o al revés. Si el fotograma es todo del mismo valor (todo penumbra de
bar, todo mesa de madera), no compite. Mídelo:

```bash
# YAVG = brillo medio del fotograma (0-255 en rango completo)
ffmpeg -y -i reel.mp4 -frames:v 1 -vf "signalstats,metadata=print" -f null - 2>&1 | grep -i "YAVG\|YMIN\|YMAX"
```
Si `YMAX - YMIN` es menor a ~90, tienes un fotograma plano: o le das luz o eliges otro.

### 5. Cero texto, o una sola palabra
El fotograma 0 se ve durante milisegundos. Seis palabras en cascada — tu gramática habitual — necesitan
0,9 a 1,8 segundos para entrar completas; en el fotograma 0 se ven como un bloque ilegible. **Regla: la
primera palabra entra en el fotograma 3 o 4, no en el 0.** El fotograma 0 es imagen pura.

### 6. Que no revele el final
Si abres un bucle (ver `364`), el fotograma 0 no puede mostrar la respuesta. Si el video es "adivina qué
lleva esta hamburguesa", el fotograma 0 no puede ser la hamburguesa abierta.

---

## Los cinco fotogramas 0 que hay que borrar siempre

1. **Negro.** Un fundido de entrada de medio segundo se come un tercio de la ventana de decisión.
2. **El logo.** Bendita Pola no es conocida; el logo al inicio no es marca, es un peaje.
3. **La persona quieta esperando.** El clásico "ya grabando" antes de arrancar a hablar.
4. **El plano general de contexto.** "El bar por fuera" antes de entrar. Va después, si va.
5. **Desenfocado.** El primer fotograma del bruto muchas veces es el enfoque buscando. Corta hacia
   adentro hasta que el enfoque esté hecho.

---

## Procedimiento: elegir el fotograma 0 con una tira de contactos

No lo elijas de memoria. Míralos todos juntos.

```bash
# 1) tira de los primeros 3 segundos, 4 fotogramas por segundo, en cuadrícula
ffmpeg -y -i reel.mp4 -t 3 -vf "fps=4,scale=180:-1,drawtext=text='%{pts\\:hms}':x=4:y=4:fontsize=14:fontcolor=yellow:box=1:boxcolor=black@0.5,tile=6x2" -frames:v 1 tira_inicio.png
```

Ábrela, mírala **al tamaño de una uña**, y elige el que gana. Anota su tiempo (la tira lleva el reloj
quemado encima). Ese tiempo es tu nuevo punto de arranque.

Si el ganador está en otra parte del video y no al principio, tienes dos caminos: mover ese plano al
inicio (mejor) o pegarlo como fotograma congelado delante (peor, pero sirve).

---

## Cómo forzarlo con ffmpeg — tres técnicas

### Técnica A — Recortar hasta el fotograma elegido (la correcta el 80% de las veces)

Elegir el fotograma 0 casi siempre es **elegir dónde empieza el corte**. Recorta con reencodificación
para que sea exacto al fotograma:

```bash
ffmpeg -y -ss 2.400 -i reel.mp4 -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p \
  -c:a aac -b:a 192k -movflags +faststart reel_v2.mp4
```

Sin `-c:v libx264` (o sea, con `-c copy`) el corte salta al fotograma clave anterior y **no vas a tener
el fotograma que elegiste**. Esa es la trampa: crees que cortaste en 2,400 y arrancaste en 1,933.

Verifica siempre:

```bash
ffmpeg -y -i reel_v2.mp4 -frames:v 1 nuevo_frame0.png
```

### Técnica B — Pegar delante un fotograma congelado (2 a 3 fotogramas, ni uno más)

Cuando el fotograma que quieres está en el medio del video y no puedes reordenar.

```bash
# 1) sacar el fotograma elegido
ffmpeg -y -ss 6.200 -i reel.mp4 -frames:v 1 portada.png

# 2) pegarlo delante, 0,067 s (2 fotogramas a 30 fps), corriendo el audio lo mismo
ffmpeg -y -loop 1 -framerate 30 -t 0.067 -i portada.png -i reel.mp4 -filter_complex \
"[0:v]scale=1080:1920,setsar=1,format=yuv420p[p]; \
 [1:v]scale=1080:1920,setsar=1,format=yuv420p[v]; \
 [p][v]concat=n=2:v=1:a=0[outv]; \
 [1:a]adelay=67|67[outa]" \
-map "[outv]" -map "[outa]" -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p \
-c:a aac -b:a 192k -movflags +faststart reel_v2.mp4
```

**Límite duro: 3 fotogramas.** Más que eso ya es un congelado visible al inicio y se lee como error de
carga. Y si el video abre con voz, correr el audio 67 ms es inaudible; correrlo 300 ms ya desincroniza.

### Técnica C — Forzar fotograma clave en 0 y sembrar claves al inicio

No cambia qué se ve, pero mejora **cómo se ve mientras carga**: si el primer fotograma es clave y hay
claves densas en los primeros segundos, la plataforma arranca más limpio y el arranque no se ve
embarrado.

```bash
ffmpeg -y -i reel.mp4 -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p \
  -force_key_frames "0,expr:gte(t,n_forced*1)" -c:a copy -movflags +faststart reel_v2.mp4
```

Comprueba dónde quedaron las claves:

```bash
ffprobe -v error -select_streams v -skip_frame nokey -show_entries frame=pts_time -of csv=p=0 reel_v2.mp4 | head
```

### Lo que NO funciona: la carátula incrustada

Puedes incrustar una imagen de portada en el MP4:

```bash
ffmpeg -y -i reel.mp4 -i portada.png -map 0 -map 1 -c copy -c:v:1 png -disposition:v:1 attached_pic salida.mp4
```

**Instagram y TikTok reencodifican el archivo al subirlo y esa carátula se pierde.** Sirve para tu
archivo local, para mandarlo por correo o para un reproductor de escritorio. No la uses como estrategia
de publicación.

---

## Cómo hacerlo en CapCut, sin tocar la terminal

El nombre exacto de los botones cambia entre versiones, pero el camino es este:

1. **Elegir el arranque:** arrastra el borde izquierdo del primer clip hasta el fotograma que quieres.
   Amplía la línea de tiempo al máximo (pellizcar para abrir) para poder pararte en un fotograma exacto.
2. **Congelar un fotograma:** párate en el fotograma bueno → botón **Congelar** → te genera un clip fijo
   de ~3 s → recórtalo a la mínima expresión y arrástralo al inicio.
3. **Portada de la grilla:** el recuadro **Portada / Cover** al principio de la línea de tiempo. Ahí
   eliges un fotograma del video o subes una imagen, y le pones el texto. Recuerda: eso es la grilla, no
   el feed.
4. **Al exportar:** revisa el primer fotograma del archivo exportado en la galería del celular. La
   miniatura que te muestra la galería es una buena aproximación al fotograma 0.

---

## El caso Bendita Pola

Un reel de la serie *Historias de Cerveza* arrancaba con el fondo azul y el grabado dorado entrando en
animación. En la grilla se veía precioso. En el feed, el fotograma 0 era **azul liso**: un rectángulo de
color sin información. Cero razón para parar.

La corrección costó 40 segundos: se movió el plano de la botella siendo destapada — que estaba en el
segundo 4 — al inicio, y el fondo azul con el grabado quedó como transición al segundo 2, ya con el
espectador dentro. Mismo material, mismo montaje, mismo texto. Solo cambió qué está en el fotograma 0.

**La regla que salió de ahí:** en esa serie, el fondo azul nunca es el fotograma 0. El fondo azul es la
firma, y la firma va cuando ya tienes a alguien mirando.

---

## Errores comunes

1. Creer que la portada elegida en la app protege el arranque en el feed. No lo hace: en el feed manda
   el fotograma 0.
2. Cortar con `-c copy` creyendo que el corte es exacto. Salta al fotograma clave anterior y arrancas en
   otro sitio del que elegiste.
3. Abrir con negro, con fundido o con logo. Es regalar la ventana de decisión completa.
4. Poner texto en el fotograma 0. Nadie alcanza a leer nada en el fotograma 0; solo tapa la imagen.
5. Elegir el fotograma mirándolo a pantalla completa en el computador, donde todo se ve bien.
6. Dejar un congelado de más de 3 fotogramas al inicio: se lee como que el video no cargó.
7. Pegar un fotograma delante y olvidar correr el audio: quedas desincronizado desde el segundo 0.
8. Confiar en la carátula incrustada (`attached_pic`): las plataformas la borran al reencodificar.
9. Que el fotograma 0 revele la respuesta del bucle que abre el video.
10. Que el título de portada de TikTok prometa una cosa y el fotograma 0 muestre otra.
11. Usar el mismo fotograma como portada de grilla y como fotograma 0 sin pensarlo: tienen trabajos
    distintos (la grilla vende el perfil, el fotograma 0 compra medio segundo).
12. No verificar el archivo final: exportaste, subiste, y nunca miraste el fotograma 0 de lo que subiste
    (ver `98`).

---

## Checklist

- [ ] Saqué el fotograma 0 del archivo final y lo miré a 120 px de alto
- [ ] Se entiende qué es y dónde pasa en menos de medio segundo
- [ ] Hay un sujeto claro que ocupa entre el 30% y el 60% del cuadro
- [ ] El gesto ya está en curso: nadie está quieto esperando
- [ ] `YMAX - YMIN` del fotograma 0 está por encima de ~90
- [ ] No hay negro, ni logo, ni fundido, ni desenfoque de búsqueda
- [ ] No hay texto en el fotograma 0; la primera palabra entra en el fotograma 3 o 4
- [ ] El fotograma 0 no revela la respuesta del bucle
- [ ] Si recorté, lo hice con reencodificación y verifiqué el nuevo fotograma 0
- [ ] Si congelé, son 3 fotogramas o menos y el audio quedó corrido lo mismo
- [ ] La portada de la grilla la elegí aparte, con criterio de perfil (ver `94`)
- [ ] Si usé título de portada en TikTok, promete lo mismo que muestra el fotograma 0
- [ ] Anoté en el diario qué fotograma 0 usé, para poder cruzarlo con la tasa de salto después
