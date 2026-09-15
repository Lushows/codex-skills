# 264 — Tracking y seguimiento

**Qué resuelve:** anclar algo a lo que se mueve. Un precio pegado a un producto que la mano levanta,
una pantalla falsa dentro de un celular que aparece en el plano, un gráfico que acompaña el temblor de
tu mano al grabar caminando.

> El módulo `205` ya cubrió el seguimiento práctico: la herramienta de CapCut, el método de bisección
> con keyframes, las tres trampas (congelar, anclar al cuadro, elegir el tramo quieto) y cuándo no vale
> la pena. **No lo repito.** Este módulo es la capa de abajo: los **tres tipos de seguimiento** que
> existen en VFX, cuál de ellos puedes hacer de verdad con lo que tienes, y las dos técnicas que `205`
> no menciona porque no son de CapCut: el **corner pin** y el **movimiento de cámara**.

---

## 1. Los tres tipos de seguimiento

| Tipo | Qué resuelve | ¿Lo puedes hacer? |
|---|---|---|
| **De punto** | dónde está una cosa en el cuadro | **Sí** — CapCut lo hace (`205`) |
| **De plano (planar / corner pin)** | una superficie plana: pantalla, cartel, pared | **A medias** — con ffmpeg si la cámara casi no se mueve |
| **De cámara (3D / matchmove)** | reconstruir el movimiento de la cámara en el espacio | **No** — necesita software que no tienes |

### El de cámara: por qué no y qué hacer

El matchmove 3D reconstruye la trayectoria de la cámara para poder meter un objeto tridimensional que
se queda quieto en el mundo mientras la cámara gira alrededor. Eso es **After Effects con 3D Camera
Tracker**, **Blender**, **Mocha Pro** o **SynthEyes**. No los tienes, y para reels no los necesitas.

**La alternativa que sí puedes hacer:** el **parallax por capas** de `89`. Recortas el sujeto, pones un
fondo detrás, y mueves las dos capas a velocidades distintas. El cerebro lee eso como profundidad y no
necesitó ni una sola cámara 3D. Cuesta cinco minutos y funciona.

---

## 2. Seguimiento de plano: el corner pin

> **Corner pin:** deformar una imagen para que sus cuatro esquinas coincidan con las cuatro esquinas de
> una superficie plana dentro del video. Es como se meten pantallas falsas en celulares y carteles
> falsos en paredes.

ffmpeg tiene el filtro `perspective`, que es exactamente eso. La sintaxis: le das las cuatro esquinas
de destino, en píxeles, y él deforma la imagen para que encajen.

```bash
# Meter una captura de pantalla dentro de la pantalla de un celular que aparece en el plano
ffmpeg -y -i plano.mp4 -i captura.png -filter_complex "\
[1:v]scale=600:1200,format=rgba,\
perspective=x0=0:y0=0:x1=600:y1=0:x2=0:y2=1200:x3=600:y3=1200:sense=destination[pin];\
[0:v][pin]overlay=x=340:y=520[out]" \
  -map "[out]" -map 0:a? -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p pantalla.mp4
```

Los ocho números `x0..y3` son las cuatro esquinas: arriba-izquierda, arriba-derecha, abajo-izquierda,
abajo-derecha. Los cambias hasta que la imagen encaje en la pantalla del celular del video.

**Cómo sacas esos números sin adivinar:** exportas un fotograma, lo abres en cualquier visor que muestre
coordenadas (Paint sirve: la barra de estado muestra la posición del cursor en píxeles) y anotas las
cuatro esquinas de la superficie.

```bash
ffmpeg -y -ss 2.4 -i plano.mp4 -frames:v 1 fotograma_ref.png
```

> ⚠️ **Verifica esto en tu equipo antes de usarlo en producción.** `perspective` tiene dos modos
> (`sense=source` y `sense=destination`) y hacen lo contrario. Si la imagen se deforma al revés, cambia
> el `sense`. Prueba siempre con `-frames:v 1` antes de renderizar el video.

### La limitación grande, dicha de frente

**Con `perspective` las esquinas son fijas durante todo el clip.** Si la cámara se mueve, la pantalla
falsa se queda quieta mientras el celular se mueve, y se ve espantoso.

Se puede animar con `eval=frame` y expresiones en función de `t`:

```bash
# Las esquinas se desplazan linealmente durante el clip (movimiento simple y constante)
perspective=x0='10+t*8':y0='0':x1='610+t*8':y1='0':x2='10+t*8':y2='1200':x3='610+t*8':y3='1200':\
sense=destination:eval=frame
```

Pero escribir a mano las expresiones de cuatro esquinas para un movimiento real es un trabajo horrible.
**Regla honesta: el corner pin con ffmpeg solo sirve para planos donde la cámara está en trípode o casi
quieta.** Si la cámara se mueve, o grabas el plano otra vez con trípode, o abandonas la idea.

### La alternativa de CapCut

CapCut no tiene corner pin. Lo más cerca: máscara de forma + escala + rotación + keyframes. Para una
pantalla que gira en perspectiva no da. **Para una superficie de frente y quieta, sí da y es más rápido
que ffmpeg.**

**La solución real para tu caso de uso:** si necesitas mostrar una pantalla de celular, **no la metas en
el video**. Pon el celular en el plano con la pantalla ya mostrando lo que quieres, o muestra la captura
en pantalla completa como plano aparte. Es lo que hace el 100% de los reels que funcionan, y cuesta
cero.

---

## 3. Seguir el movimiento de la cámara con vidstab

Esta es la técnica de este módulo que no está en ningún otro. Sirve para un problema muy concreto:
**grabaste a pulso, la cámara tiembla, y el gráfico que pusiste encima está perfectamente quieto.** Ese
contraste —escena que tiembla, gráfico que no— es una de las señales más fuertes de "esto es una capa
pegada".

ffmpeg trae `vidstabdetect`, que **mide el movimiento de la cámara fotograma a fotograma** y lo escribe
en un archivo.

```bash
# Paso 1: medir el movimiento y guardarlo
ffmpeg -y -i plano.mp4 -vf "vidstabdetect=shakiness=6:accuracy=15:result=movimiento.trf" -f null -
```

Ese `movimiento.trf` es un archivo de texto con las mediciones por fotograma. **Es información real
sobre cómo se movió tu cámara.**

Y ahora las dos formas de usarlo:

### 3.1. Estabilizar → componer → aceptar (la práctica)

```bash
# Paso 2: estabilizar el plano
ffmpeg -y -i plano.mp4 -vf "vidstabtransform=input=movimiento.trf:smoothing=25:zoom=2,unsharp=5:5:0.6" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p plano_estable.mp4
```

Compones sobre el plano estabilizado. Como el plano ya no tiembla, el gráfico quieto **encaja
perfectamente**. Resultado: composición limpia, plano estable, y el video se ve más caro por partida
doble.

**Ese `zoom=2` es el precio:** estabilizar recorta bordes, así que pierdes un 2% de cuadro. En vertical
no se nota. Es una ganga.

> **Esta es la respuesta correcta el 95% de las veces.** No intentes hacer que el gráfico tiemble como
> la cámara: haz que la cámara deje de temblar.

### 3.2. Darle el temblor al gráfico (cuando quieres conservar el movimiento)

A veces el temblor es parte del estilo —un plano caminando, energía de celular— y estabilizarlo mata la
sensación. Ahí la opción es **añadirle un temblor parecido al gráfico**. Con ffmpeg no puedes leer el
`.trf` directamente dentro del filtro, así que se falsifica con expresiones:

```bash
# Temblor sintético sobre el gráfico: dos senos de frecuencias distintas para que no se vea mecánico
ffmpeg -y -i plano.mp4 -i grafico.png -filter_complex "\
[1:v]format=rgba[g];\
[0:v][g]overlay=\
x='420 + 5*sin(2*PI*t*1.7) + 3*sin(2*PI*t*4.3)':\
y='900 + 4*sin(2*PI*t*2.1) + 2*sin(2*PI*t*5.9)'[out]" \
  -map "[out]" -map 0:a? -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p con_temblor.mp4
```

Las amplitudes (5, 3, 4, 2 píxeles) tienen que ser **parecidas al temblor real del plano**, no más. Si
te pasas, el gráfico parece que tiene vida propia.

> ⚠️ **Verifica esto en tu equipo antes de usarlo en producción.** El temblor sintético no coincide con
> el real: solo hace que el gráfico deje de estar sospechosamente quieto. Míralo en cámara lenta antes
> de aceptarlo; si el gráfico y la escena se mueven en direcciones distintas, se ve peor que quieto.

**En CapCut:** hay presets de "sacudida de cámara" en Efectos, y algunos se pueden aplicar solo a la
capa del gráfico. Es la vía rápida, y suele bastar.

---

## 4. La jerarquía de decisión

Cuando te digas "necesito seguimiento", pasa por esta lista **en orden** y para en la primera que
funcione:

```
1. ¿Puedo CONGELAR el fotograma y poner el gráfico ahí?          → hazlo (205)
2. ¿Puedo anclar el gráfico AL CUADRO en vez de al objeto?       → hazlo (205)
3. ¿Hay un tramo de 1-2 s donde el objeto casi no se mueve?      → úsalo (205)
4. ¿Puedo ESTABILIZAR el plano y componer encima?                → vidstab (3.1)
5. ¿La cámara está en trípode y la superficie es plana?          → perspective (2)
6. ¿El objeto tiene contraste y no sale del cuadro?              → seguimiento de CapCut (205)
7. ¿Nada de lo anterior?                                          → el plano está mal grabado.
                                                                    Vuélvelo a grabar (sección 5).
```

**Los pasos 1, 2 y 3 resuelven el 80% de los casos y cuestan menos de dos minutos.** Los pasos 4 en
adelante ya son inversión. Si llegaste al 7, para.

---

## 5. Grabar para no tener que seguir nada

Lo más rentable del módulo, y cuesta cero.

- **Trípode o el celular apoyado en algo.** Un plano quieto no necesita seguimiento nunca. Un soporte de
  celular cuesta menos que una hora de tu tiempo.
- **Deja el objeto quieto dos segundos.** Si sabes que le vas a poner un precio a la calculadora en
  pantalla, deja la pantalla quieta dos segundos. Fin del problema.
- **Mueve la cámara, no el objeto.** Un paneo lento sobre algo quieto se sigue solo. Un objeto agitado
  a pulso, no.
- **60 fps.** Menos borrón de movimiento por fotograma: el seguimiento automático agarra mejor y el
  recorte también (`261`).
- **Fondo contrastado.** Objeto claro sobre fondo oscuro, u objeto oscuro sobre fondo claro. Nunca del
  mismo color.
- **Margen antes y después.** Graba dos segundos de más a cada lado. Un seguimiento que empieza en el
  primer fotograma casi siempre falla.
- **Luz estable.** Apaga las luces que parpadean. Un cambio de brillo brusco rompe cualquier
  seguimiento.

---

## 6. Verificar

Dos comprobaciones, ambas de `205` pero vale repetirlas porque son las que evitan publicar un desastre:

```bash
# Cámara lenta 4x: la deriva se ve muchísimo mejor
ffmpeg -y -i tramo.mp4 -filter_complex "[0:v]setpts=4*PTS[v]" -map "[v]" -an \
  -c:v libx264 -crf 20 -pix_fmt yuv420p revision_lenta.mp4

# Tira de fotogramas: saltos y temblor
ffmpeg -y -ss 3.0 -i tramo.mp4 -t 2.0 -vf "fps=25,scale=180:-1,tile=10x5" -frames:v 1 tira.png
```

Lo que buscas: **deriva** (se va quedando atrás), **salto** (un fotograma donde brinca), **temblor**
(vibración de dos píxeles que delata keyframes de más).

---

## Errores comunes

1. **Pensar que necesitas matchmove 3D.** Para reels casi nunca. El parallax por capas (`89`) da la
   misma sensación de profundidad en cinco minutos.
2. **Buscar corner pin en CapCut.** No lo tiene. La aproximación con máscara + escala + rotación solo
   sirve para superficies de frente.
3. **Usar `perspective` con la cámara en movimiento.** Las esquinas quedan fijas y la pantalla falsa se
   despega. Trípode o nada.
4. **Confundir `sense=source` con `sense=destination`.** Hacen lo contrario. Si se deforma al revés,
   cambia el modo.
5. **Renderizar el video completo para probar un corner pin.** `-frames:v 1` y miras el PNG.
6. **Componer un gráfico quieto sobre un plano que tiembla.** Es de las señales más fuertes de capa
   pegada. Estabiliza el plano con vidstab y compón encima.
7. **Olvidar que `vidstabtransform` recorta bordes.** Con `zoom=2` pierdes un 2% de cuadro: tenlo en
   cuenta al encuadrar zonas seguras.
8. **Exagerar el temblor sintético.** Si el gráfico se sacude más que la escena, parece que tiene vida
   propia. Amplitudes de 2 a 6 píxeles, no más.
9. **Meter una pantalla falsa en un celular** cuando podías grabar el celular ya mostrando el contenido.
   Cero trabajo, mejor resultado.
10. **Saltarse la jerarquía de decisión.** Congelar, anclar al cuadro y elegir el tramo quieto resuelven
    el 80% en dos minutos.
11. **No verificar en cámara lenta.** A velocidad normal, con ojos cansados, la deriva es invisible; en
    el feed publicado, no.

---

## Checklist

Antes de dar por bueno un elemento anclado a algo que se mueve:

- [ ] Pasé por la **jerarquía de decisión** y descarté congelar / anclar al cuadro / tramo quieto.
- [ ] Sé qué tipo de seguimiento necesito: **punto**, **plano** o **cámara**, y sé cuál puedo hacer.
- [ ] Si es de plano, la cámara está **quieta** y probé `perspective` con `-frames:v 1` primero.
- [ ] Si el plano tiembla, **estabilicé con vidstab** y compuse sobre el estable (o le di temblor al
      gráfico, con amplitud pequeña).
- [ ] Verifiqué en **cámara lenta 4x** y en **tira de fotogramas**.
- [ ] No hay **deriva**, ni **saltos**, ni **temblor** de dos píxeles.
- [ ] El tramo dura **más de 2 segundos**, o si no, no valía la pena.
- [ ] No invertí más de **15 minutos** en este elemento (`269`).
- [ ] Anoté qué hacer distinto **al grabar** para que la próxima vez no haga falta seguimiento.
- [ ] Si nada funcionó, acepté que el plano está mal grabado en vez de seguir peleando.
