# 47 — Tipografía cinética avanzada

> Este módulo asume que ya dominas el golpe estándar (`42`) y el formato ASS (`43`). Aquí está lo que
> viene después: el texto que hace algo más que aparecer.

## La advertencia primero

La tipografía cinética avanzada es **cara de hacer y fácil de arruinar**. Antes de meterte:

1. Un video con el golpe estándar bien hecho ya está en el percentil 90. Lo avanzado es el último 10%.
2. Cada técnica de aquí debe usarse **una o dos veces por pieza**, no en todo el video. Un video donde
   todo el texto hace algo raro se ve como una demo de plantillas, no como una pieza.
3. Si la técnica no le sirve a la idea, es decoración. Y la decoración en video es ruido.

**La pregunta de control:** ¿esto ayuda a que se entienda o a que se quede? Si la respuesta honesta es
"se ve chévere", no va.

---

## 1. Texto que sigue el movimiento (tracking)

El texto se ancla a un objeto del plano y se mueve con él. Es lo que hace que un rótulo se sienta parte
del mundo y no pegado encima.

### Cuándo vale la pena

- Señalar un objeto en un plano que se mueve (un producto, una parte de una máquina, un ingrediente).
- Un nombre que sigue a una persona caminando.
- Un precio pegado a un plato que gira.

### Cómo se hace con ASS

`\move(x1,y1,x2,y2,t1,t2)` interpola en línea recta entre dos puntos. Para movimiento con
aceleración o curvas, se encadenan varias líneas `Dialogue` cortas, cada una con su `\move`.

Movimiento simple, siguiendo un objeto que va de izquierda a derecha durante 2 segundos:

```
Dialogue: 0,0:00:05.00,0:00:07.00,Rotulo,,0,0,0,,{\an5\move(320,880,760,910,0,2000)}FONDO DE COCCION
```

Movimiento en tres tramos (para seguir una curva):

```
Dialogue: 0,0:00:05.00,0:00:05.70,Rotulo,,0,0,0,,{\an5\move(320,880,480,840,0,700)}FONDO DE COCCION
Dialogue: 0,0:00:05.70,0:00:06.40,Rotulo,,0,0,0,,{\an5\move(480,840,640,870,0,700)}FONDO DE COCCION
Dialogue: 0,0:00:06.40,0:00:07.00,Rotulo,,0,0,0,,{\an5\move(640,870,760,910,0,600)}FONDO DE COCCION
```

Cada línea empieza donde terminó la anterior. Si no coinciden exactamente, se ve un salto.

### Cómo sacar las coordenadas

Extrae fotogramas del tramo y mide la posición del objeto en cada uno:

```bash
ffmpeg -ss 5.0 -to 7.0 -i entrada.mp4 -vf "fps=10" -y track_%03d.png
```

Abre `track_001.png`, `track_007.png`, `track_014.png` y anota las coordenadas del objeto en cada uno.
Con 3 o 4 puntos de referencia y `\move` entre ellos, la ilusión funciona. **No necesitas trackear cada
fotograma**: el ojo perdona la interpolación lineal en tramos de 0,5-0,7 s.

**Honestidad:** ASS no hace tracking automático. Para movimiento complejo (rotación, escala, cámara que
gira) el camino correcto es un editor con motion tracking real, o generar el texto como una secuencia PNG
con alfa y superponerla (ver `105`). ASS cubre el 80% de los casos con una fracción del trabajo.

---

## 2. Máscaras: texto que se revela

Un texto que se **descubre** en vez de aparecer. Da sensación de material físico.

ASS tiene `\clip` y `\iclip`, que recortan lo que se dibuja a una región.

### Revelado horizontal (barrido)

`\clip(x1,y1,x2,y2)` define un rectángulo: solo se dibuja lo que cae dentro. Para el barrido, animas ese
rectángulo desde ancho cero hasta el ancho completo:

```
Dialogue: 0,0:00:03.00,0:00:05.00,Golpe,,0,0,0,,{\clip(60,1180,60,1420)\t(0,320,\clip(60,1180,1020,1420))}COSTO REAL
```

El rectángulo arranca con ancho cero (x1 = x2 = 60) y crece hasta x2 = 1020 en 320 ms. El texto se
descubre de izquierda a derecha.

### Revelado vertical (sube desde abajo)

```
Dialogue: 0,0:00:03.00,0:00:05.00,Golpe,,0,0,0,,{\clip(60,1420,1020,1420)\t(0,280,\clip(60,1180,1020,1420))}COSTO REAL
```

### `\iclip`: el inverso

`\iclip` oculta lo que está **dentro** del rectángulo. Sirve para hacer que un texto desaparezca por
partes, o para que un objeto del video "tape" el texto (efecto de profundidad).

### Máscara con forma (dibujo vectorial)

`\clip(escala, comandos)` acepta un dibujo vectorial en la sintaxis de dibujo de ASS:

```
{\clip(1,m 60 1180 l 1020 1180 1020 1420 60 1420)}
```

`m` = mover a, `l` = línea a, `b` = curva bézier. Con esto puedes recortar el texto a la silueta de una
forma de marca. Es potente y es tedioso. Úsalo cuando la forma de marca de verdad importe, no por deporte.

**Regla:** un revelado por máscara dura **250-400 ms**, no 140. Es un gesto distinto al golpe: aquí sí
quieres que se perciba el movimiento.

---

## 3. Texto que reacciona al audio

El texto que pulsa con el volumen o con el beat. Es el efecto que hace que un video se sienta musical.

ASS no lee audio. Se hace en dos pasos: **medir el audio, luego generar el `.ass` con esa medida**.

### Paso 1: sacar el volumen instantáneo

```bash
ffmpeg -i entrada.mp4 -af "astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=niveles.txt" -f null -
```

Eso escribe en `niveles.txt` el nivel RMS por bloque de análisis, con su timestamp. Para un análisis más
fino por ventana de tiempo fija:

```bash
ffmpeg -i entrada.mp4 -af "aresample=8000,asetnsamples=n=800,astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=niveles.txt" -f null -
```

`asetnsamples=n=800` a 8000 Hz da bloques de 100 ms. Suficiente resolución para pulsar texto.

El archivo se ve así:

```
frame:0    pts:0       pts_time:0
lavfi.astats.Overall.RMS_level=-38.421
frame:1    pts:800     pts_time:0.1
lavfi.astats.Overall.RMS_level=-21.883
```

### Paso 2: mapear nivel a escala

```javascript
// -40 dB (silencio) -> escala 100 ; -6 dB (fuerte) -> escala 118
const escala = (db) => {
  const c = Math.max(-40, Math.min(-6, db));
  return Math.round(100 + ((c + 40) / 34) * 18);
};
```

### Paso 3: generar una línea `Dialogue` por bloque

```
Dialogue: 0,0:00:01.00,0:00:01.10,Pulso,,0,0,0,,{\fscx104\fscy104}RITMO
Dialogue: 0,0:00:01.10,0:00:01.20,Pulso,,0,0,0,,{\fscx117\fscy117}RITMO
Dialogue: 0,0:00:01.20,0:00:01.30,Pulso,,0,0,0,,{\fscx109\fscy109}RITMO
```

Un texto de 2 segundos se convierte en 20 líneas de 100 ms. Genéralas por código, obviamente.

**Suaviza los saltos.** Si vas de 104 a 117 de golpe, se ve nervioso. Añade un `\t` corto dentro de cada
bloque para que interpole:

```
Dialogue: 0,0:00:01.10,0:00:01.20,Pulso,,0,0,0,,{\fscx104\fscy104\t(0,100,\fscx117\fscy117)}RITMO
```

**Rango:** entre 100 y 118. Más de 120 y el texto convulsiona. El efecto tiene que sentirse, no verse.

### Alternativa: pulsar solo en los golpes de la música

Más limpio y mucho menos trabajo. Detecta los onsets y pulsa solo ahí:

```bash
ffmpeg -i musica.mp3 -af "silencedetect=noise=-30dB:d=0.05" -f null - 2>&1 | grep silence_end
```

Cada `silence_end` es aproximadamente un ataque. Con esos tiempos, pones un pop de 140 ms exactamente en
cada uno. Ver `24`.

---

## 4. Kinetic type de autor: texto que compone el cuadro

Aquí el texto deja de ser subtítulo y se vuelve **la imagen**. Es la tradición de Saul Bass, Kyle Cooper
y los títulos de crédito de cine.

### Los tres principios

**a) La palabra se dibuja, no se coloca.** El tamaño, la posición y la rotación de cada palabra
responden a su significado, no a una plantilla. "CAÍDA" cae. "ENORME" es enorme. "MÍNIMO" es diminuto.

```
Dialogue: 0,0:00:02.00,0:00:03.20,Libre,,0,0,0,,{\an5\pos(540,700)\fs320}ENORME
Dialogue: 0,0:00:03.20,0:00:04.40,Libre,,0,0,0,,{\an5\pos(540,960)\fs64}minimo
```

**b) La composición cambia, no solo el contenido.** En vez de que todo el texto salga del mismo sitio,
cada golpe ocupa una zona distinta del cuadro. El ojo se mueve. Eso es lo que crea sensación de montaje
sin cortar nada.

```
Dialogue: 0,0:00:01.00,0:00:01.90,Libre,,0,0,0,,{\an1\pos(120,600)}PRIMERO
Dialogue: 0,0:00:01.90,0:00:02.80,Libre,,0,0,0,,{\an9\pos(960,1100)}DESPUES
Dialogue: 0,0:00:02.80,0:00:03.70,Libre,,0,0,0,,{\an5\pos(540,850)\fs260}SIEMPRE
```

Cuidado: cada `\pos` tiene que respetar la zona segura (ver `45`). Al usar coordenadas los márgenes del
estilo dejan de protegerte.

**c) La palabra clave se queda, el resto pasa.** Un patrón que funciona: cinco golpes rápidos que
desaparecen, y el sexto se queda 3 segundos en el centro. La retención está en el contraste de ritmo.

### El acumulado

El texto anterior no desaparece: se queda y el nuevo se suma. Al final se lee la frase completa. Se hace
con varias líneas que se solapan en el tiempo, cada una en su posición:

```
Dialogue: 0,0:00:01.00,0:00:05.00,Libre,,0,0,0,,{\an5\pos(540,760)\fs150}COMPRAS
Dialogue: 0,0:00:01.60,0:00:05.00,Libre,,0,0,0,,{\an5\pos(540,930)\fs150}COCINAS
Dialogue: 0,0:00:02.20,0:00:05.00,Libre,,0,0,0,,{\an5\pos(540,1100)\fs150}VENDES
Dialogue: 0,0:00:02.80,0:00:05.00,Libre,,0,0,0,,{\an5\pos(540,1270)\fs180\1c&H001C4FE8&}PIERDES
```

Cada una entra con su pop. Al segundo 2,8 el cuadro tiene las cuatro y la última, en color de marca y más
grande, cierra el argumento. Es un recurso de altísimo rendimiento en un video de venta.

**Regla:** máximo 4-5 elementos acumulados. A partir de ahí es una lista y una lista no es kinetic type.

---

## 5. Texto en perspectiva (3D falso)

`\frx` y `\fry` rotan el texto en los ejes X e Y, dando perspectiva.

```
Dialogue: 0,0:00:02.00,0:00:04.00,Golpe,,0,0,0,,{\an5\pos(540,900)\fry40\alpha&HFF&\t(0,260,\fry0\alpha&H00&)}ENTRA
```

El texto entra girando en el eje Y y se endereza. Funciona **una vez por video**, para el titular. Es
llamativo y se gasta rápido.

`\fax` y `\fay` inclinan (shear) el texto. `\fax0.3` da una itálica falsa con carácter gráfico:

```
{\fax-0.25}INCLINADO
```

Rango útil: -0,4 a 0,4. Más allá el texto se deforma feo.

---

## 6. Cuándo salirse de ASS

ASS tiene un techo. Si necesitas alguna de estas, ya no es su trabajo:

| Necesitas | Herramienta |
|---|---|
| Texto que se deforma sobre una superficie 3D | Blender / After Effects |
| Partículas, líquido, texto que se desarma en pedazos | After Effects |
| Motion tracking real con rotación y escala | DaVinci / After Effects |
| Texto con textura, degradado o imagen dentro | PNG con alfa superpuesta (ver `105`) |
| Texto que interactúa con la iluminación del plano | Composición por capas real |

### La salida intermedia: PNG con alfa

Generas los fotogramas del texto con la herramienta que quieras (incluso HTML + Chrome headless), los
exportas como secuencia PNG con transparencia, y los superpones con ffmpeg:

```bash
ffmpeg -i entrada.mp4 -framerate 30 -i texto_%04d.png -filter_complex \
  "[0:v][1:v]overlay=0:0:enable='between(t,2.0,5.5)'[v]" \
  -map "[v]" -map 0:a -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a copy -y salida.mp4
```

O como video con canal alfa (ProRes 4444 o WebM VP9 con alfa):

```bash
ffmpeg -i entrada.mp4 -i texto_alfa.mov -filter_complex \
  "[0:v][1:v]overlay=0:0[v]" -map "[v]" -map 0:a \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a copy -y salida.mp4
```

Ver `105` para el detalle de superposición de capas y `81` para sacar PNG con alfa.

---

## Cuándo NO usar nada de esto

- **En el 90% de los golpes de un subtitulado completo.** El pop estándar y ya. La consistencia es la que
  crea ritmo; la variedad lo destruye.
- **Cuando la imagen ya es fuerte.** Si el plano es un producto bien iluminado moviéndose, el texto se
  quita del medio.
- **Cuando el mensaje es serio.** Un testimonio, un tema delicado, una disculpa de marca. Ahí el texto
  cinético se lee como frivolidad.
- **Cuando no hay tiempo.** Estas técnicas cuestan horas. En contenido diario de volumen, el retorno no
  está ahí. Está en publicar más y mejor guionado.

---

## Errores comunes

- **Usar tres técnicas avanzadas en el mismo video.** Se lee como demo de plantillas, no como pieza.
- **Aplicar efectos al subtitulado completo.** Cada golpe con un efecto distinto = caos. El subtitulado
  es infraestructura; la variedad va en los resaltes.
- **Revelados de 140 ms.** Un `\clip` animado necesita 250-400 ms para percibirse. A 140 ms es un flash.
- **Encadenar `\move` sin que las coordenadas coincidan.** El punto final de una línea debe ser exactamente
  el inicial de la siguiente, o se ve un salto.
- **Pulsar el texto con el audio en un rango exagerado.** Más de 120% de escala y el texto convulsiona.
  100-118 es el rango.
- **Pulso sin interpolar.** Saltos de escala en bloques de 100 ms sin `\t` interno se ven nerviosos.
- **Olvidar la zona segura al usar `\pos`.** Los márgenes del estilo dejan de aplicar y el texto termina
  bajo el caption.
- **Acumular más de 5 elementos.** Deja de ser composición y se vuelve lista.
- **Rotación 3D (`\fry`) más de una vez por video.** Es un recurso de titular, no de subtítulo.
- **Meterse en ASS cuando el trabajo pedía After Effects.** Reconocer el techo de la herramienta ahorra
  días. Si necesitas partículas o deformación real, sal de ASS.
- **Hacerlo porque se ve chévere.** La pregunta es si ayuda a entender o a quedarse. Si no, es ruido.

---

## Checklist

- [ ] Cada técnica avanzada la usé **1-2 veces en toda la pieza**, no en cada golpe.
- [ ] El subtitulado base sigue siendo consistente: pop estándar, sin variaciones.
- [ ] Puedo justificar cada efecto por lo que le hace al mensaje, no por cómo se ve.
- [ ] Los revelados por máscara duran 250-400 ms, no 140.
- [ ] En los `\move` encadenados, las coordenadas coinciden exactamente entre líneas consecutivas.
- [ ] El pulso por audio está entre 100% y 118% de escala, con `\t` interno para suavizar.
- [ ] **Toda línea con `\pos` o `\move` la verifiqué contra la zona segura** (ver `45`).
- [ ] Los elementos acumulados son máximo 4-5.
- [ ] La rotación 3D (`\frx`/`\fry`) aparece máximo una vez.
- [ ] Rendericé fotogramas de cada efecto y **los miré uno por uno**, no reproduje y ya.
- [ ] Si necesitaba algo fuera del alcance de ASS, lo reconocí y salí a PNG con alfa o a otra herramienta.
- [ ] El video sigue funcionando **en silencio** después de todos los efectos (ver `40`).
- [ ] Vi la pieza terminada en el celular y el texto sigue legible durante los efectos.
