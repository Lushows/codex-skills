# 205 — Gráficos que siguen el movimiento

**Qué resuelve:** quieres que el precio quede pegado a la jarra mientras la mano la levanta, o que una
flecha siga a la persona que camina, o que un difuminado tape la cara de un cliente durante todo el
plano. Eso se llama **seguimiento** (tracking) y tiene fama de ser cosa de programas caros. No lo es.
Este módulo da las tres formas de hacerlo —una automática, una a mano y una tramposa—, y sobre todo
dice **cuándo el resultado no vale el trabajo**, que es más veces de las que uno quisiera.

---

## 1. Qué es seguir un objeto

> **Seguimiento (tracking):** hacer que un elemento superpuesto se mueva junto con algo que está dentro
> del video, de manera que parezca clavado a ese algo.

Hay tres niveles, y confundirlos es lo que hace que la gente se frustre:

| Nivel | Qué sigue | Dificultad | Se ve como |
|---|---|---|---|
| **Posición** | dónde está el objeto | fácil | el gráfico acompaña |
| **Posición + escala** | dónde está y qué tan cerca | media | el gráfico pertenece |
| **Posición + escala + rotación/perspectiva** | además cómo está inclinado | difícil | el gráfico está *pintado* sobre el objeto |

**Para video social, el nivel 1 basta el 90% de las veces.** El nivel 3 es lo que hace falta para
poner un logo en una camiseta o una pantalla falsa en un celular, y ahí sí conviene otro programa o no
hacerlo.

---

## 2. La forma automática: el seguimiento de CapCut

CapCut trae seguimiento en escritorio y en móvil, y funciona sorprendentemente bien cuando las
condiciones son buenas.

**Dónde está:** con el clip de video seleccionado, panel de la derecha, pestaña **Video** → subpestaña
**Seguimiento** (Tracking) → **Seguimiento de movimiento**. Aparece un recuadro que se coloca sobre lo
que quieres seguir. En escritorio puedes elegir dirección **Adelante**, **Atrás** o **Ambas**; usa
**Ambas** para no depender de dónde tengas el cursor.

**Los cinco requisitos para que funcione:**

1. **El objeto no se sale del cuadro.** Si sale y vuelve, el seguimiento se pierde y no vuelve solo.
2. **Contrasta con lo que tiene detrás.** Una jarra ámbar sobre una barra de madera ámbar es un
   infierno. Una jarra ámbar sobre una pared oscura es fácil.
3. **No hay desenfoque de movimiento fuerte.** Si el objeto se mueve tan rápido que se vuelve un
   borrón, no hay qué seguir.
4. **No pasa nada por delante.** Una mano que cruza por encima del objeto rompe el seguimiento.
5. **La luz no cambia bruscamente.** Un flash, una luz de neón que parpadea o alguien que abre la
   puerta y entra sol: todo eso hace perder el rastro.

**El recuadro: dónde ponerlo.** El error de todos es encerrar el objeto entero. Lo que funciona mejor
es un recuadro **pequeño sobre una zona con detalle y contraste**: la etiqueta de la botella, el logo
del delantal, la esquina de un letrero. Un recuadro grande contiene mucho fondo y confunde al
algoritmo.

**Qué hacer cuando falla a mitad de camino:** córtalo. Divide el clip donde el seguimiento se perdió y
haz dos seguimientos separados, uno para cada mitad. Es más rápido que pelear con uno solo.

---

## 3. La forma a mano: seguir con keyframes

Cuando el automático no funciona (que pasa seguido en un bar, entre luz baja y manos cruzando), se
hace a mano. No es tan lento como suena si usas el método correcto.

**El método de la bisección — el único que no te hace perder la tarde:**

No pongas keyframes uno tras otro en orden. Haz esto:

1. Keyframe en el **primer** fotograma del tramo, con el gráfico en su sitio.
2. Keyframe en el **último** fotograma del tramo, con el gráfico en su sitio.
3. Vete **a la mitad**. Mira si el gráfico está donde debería. Si sí, terminaste. Si no, corrígelo:
   se crea un keyframe.
4. Ahora vete a la mitad de cada una de las dos mitades. Corrige solo donde haga falta.
5. Repite hasta que en ninguna revisión haga falta corregir.

Con esto, un tramo de 4 segundos suele quedar resuelto con **5 a 9 keyframes**, no con 120. Y encima
el movimiento queda **suave**, porque el editor interpola entre puntos separados. Si pones un keyframe
por fotograma, el resultado tiembla: cada corrección tuya de dos píxeles se convierte en una vibración.

> **La paradoja del seguimiento a mano:** menos keyframes = más suave. El temblor no viene del objeto,
> viene de tu mano corrigiendo de más.

**El otro método, para movimiento simple:** si el objeto se mueve en línea recta y a velocidad
constante (alguien caminando de un lado al otro del cuadro), **dos keyframes bastan**: inicio y fin,
con curva lineal. Nada más. Probablemente quede mejor que un seguimiento automático.

---

## 4. La forma tramposa: no seguir nada

Tres alternativas que dan el 80% del efecto con el 5% del trabajo. Son las que más vas a usar.

### 4.1. Congela el fotograma

Si lo que quieres es señalar algo, **congela el video** medio segundo, pon la flecha o el texto sobre
la imagen quieta, y sigue. No hay nada que seguir porque nada se mueve.

Suena bruto y funciona muy bien: el congelado además crea énfasis y le da al espectador tiempo de leer.
En CapCut es el botón **Congelar** (crea un fotograma fijo de 3 segundos que puedes acortar).

**Cuándo es mejor que seguir:** casi siempre que la intención sea "mira esto". Un congelado de 0,7
segundos con la flecha encima comunica más que un seguimiento perfecto de 4 segundos.

### 4.2. Ancla el gráfico al cuadro, no al objeto

En vez de que el precio siga a la jarra, pon el precio **fijo en una esquina** y que la jarra pase.
Nadie espera que un precio esté clavado a un objeto: el precio es información, vive en el cuadro.

**Regla útil:** solo se ancla al objeto lo que **conceptualmente pertenece al objeto**. Un nombre sobre
una persona, un difuminado sobre una cara, una etiqueta sobre un producto. Todo lo demás vive en el
cuadro.

### 4.3. Elige el tramo donde el objeto casi no se mueve

Un plano de 6 segundos donde la jarra se mueve mucho probablemente tenga 1,5 segundos donde está casi
quieta. Pon el gráfico **solo ahí**. Entra, se lee, sale. No hiciste seguimiento y nadie lo notó.

Esta es la jugada más subestimada del módulo. La mayoría de las veces que alguien "necesita
seguimiento", lo que necesita es elegir mejor el tramo.

---

## 5. El caso que sí lo justifica: tapar una cara

Es la única situación donde el seguimiento no es opcional: hay un cliente en el fondo que no quiere
salir, o un menor, o simplemente alguien a quien no le pediste permiso.

**Cómo se hace:**

1. Seguimiento automático sobre la cara (el rostro tiene mucho detalle y contraste, suele seguirse
   bien).
2. Aplica un difuminado o un mosaico como elemento seguido.
3. **Haz el área un 25% más grande de lo que crees que necesitas.** El seguimiento siempre se atrasa
   unos píxeles y un difuminado que deja ver media cara no sirve de nada.
4. **Revisa fotograma a fotograma en los momentos de movimiento rápido.** Ahí es donde se destapa.

```bash
ffmpeg -ss 4.0 -i salida.mp4 -t 2.0 -vf "fps=25,scale=180:-1,tile=10x5" -frames:v 1 revision.png
```

Esa tira te muestra 50 fotogramas de dos segundos en una sola imagen. Si en alguno se ve la cara, lo
vas a notar de inmediato.

Con ffmpeg, para una zona que no se mueve mucho, se puede hacer directo:

```bash
ffmpeg -i entrada.mp4 -filter_complex \
  "[0:v]crop=220:220:640:430,avgblur=28[b];[0:v][b]overlay=640:430:enable='between(t,4.0,9.5)'" \
  -map 0:a -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

Recorta un cuadro de 220×220 en la posición 640,430, lo desenfoca y lo vuelve a pegar en su sitio
entre los segundos 4 y 9,5. Si la cara se desplaza, hay que convertir esos números fijos en
expresiones con `t`, y ahí ya conviene hacerlo en el editor.

---

## 6. Cuándo el resultado no vale el trabajo

La sección más importante. Estas son las señales de que deberías parar:

**1. Llevas más de 15 minutos en un gráfico de un reel.** Un reel completo debería tomarte entre 40
minutos y dos horas. Si un solo elemento se lleva 15 minutos, ese elemento está consumiendo un 10–20%
del presupuesto total del video. Casi nunca lo vale.

**2. El gráfico no cambia lo que la persona entiende.** Pregunta honesta: si quito esto, ¿el
espectador entiende menos o compra menos? Si la respuesta es no, era decoración con esfuerzo.

**3. El plano dura menos de 2 segundos.** No hay tiempo de apreciar el seguimiento. Lo que hiciste no
se va a ver.

**4. Vas a subirlo a Instagram.** La compresión de la plataforma se come los detalles finos. Un
seguimiento con dos píxeles de deriva se ve idéntico a uno perfecto después de que Instagram lo
recomprima.

**5. Es un video que no vas a repetir.** El seguimiento no se reutiliza: es específico de ese plano.
Todo el tiempo que inviertes ahí es tiempo que no se capitaliza, al revés de una plantilla (`88`) o un
sistema de motion (`208`).

> **La cuenta que conviene hacer:** cinco reels decentes le ganan a un reel perfecto. Si el
> seguimiento te va a costar el tiempo de otro video, no lo hagas.

---

## 7. Grabar pensando en el seguimiento

Lo más rentable de todo el módulo: **arreglar el problema en la grabación**, que cuesta cero.

- **Deja el objeto quieto un momento.** Si sabes que vas a poner un precio sobre la jarra, deja la
  jarra quieta dos segundos. Se acabó el seguimiento.
- **Mueve la cámara, no el objeto.** Un paneo suave sobre algo quieto es infinitamente más fácil de
  seguir que un objeto que se agita.
- **Fondo contrastado.** No pongas el objeto delante de algo del mismo color.
- **Luz estable.** Apaga las luces que parpadean mientras grabas ese plano.
- **Graba a 60 fps.** Menos desenfoque de movimiento por fotograma, más fácil de seguir, y además te
  deja acelerar limpio (`201`).
- **Graba dos segundos de más al principio y al final.** Un seguimiento que empieza justo en el primer
  fotograma casi siempre falla; necesita margen.

---

## 8. Verificar un seguimiento

Un seguimiento malo no se nota reproduciendo a velocidad normal cuando ya llevas tres horas editando.
Se nota al día siguiente, publicado, y ahí duele.

**Las dos verificaciones:**

**Tira de fotogramas.** Igual que en `203`: exporta el tramo, saca la tira, y mira si el gráfico
mantiene la misma distancia relativa al objeto en todos los cuadritos. Si en algunos se despega, ahí
está el problema.

**Reproducción a velocidad reducida.** Exporta el tramo a 0,25x y míralo. El ojo detecta la deriva con
muchísima más facilidad en cámara lenta.

```bash
ffmpeg -i tramo.mp4 -filter_complex "[0:v]setpts=4*PTS[v]" -map "[v]" -an \
  -c:v libx264 -crf 20 -pix_fmt yuv420p revision_lenta.mp4
```

Lo que buscas: **deriva** (el gráfico se va quedando atrás), **saltos** (un fotograma donde brinca) y
**temblor** (vibración de dos píxeles que delata keyframes de más).

---

## Errores comunes

1. **Intentar seguir algo que se sale del cuadro y vuelve.** El seguimiento no vuelve solo. Corta el
   clip en dos.
2. **Poner el recuadro de seguimiento alrededor del objeto entero.** Ponlo pequeño, sobre una zona con
   detalle y contraste.
3. **Seguir algo del mismo color que su fondo.** No hay nada que seguir. Esto se arregla al grabar.
4. **Un keyframe por fotograma.** Produce temblor. Usa bisección: 5 a 9 keyframes para 4 segundos.
5. **Pelear media hora con un seguimiento automático que falla.** Corta el clip donde falla y haz dos.
6. **Difuminar una cara con el área justa.** Hazla 25% más grande; el seguimiento siempre se atrasa.
7. **No revisar el difuminado fotograma a fotograma.** Se destapa en los movimientos rápidos, que es
   justo donde importa.
8. **Anclar al objeto algo que pertenece al cuadro.** Un precio no vive pegado a una jarra.
9. **Hacer seguimiento cuando bastaba congelar el fotograma.** El congelado además da énfasis y tiempo
   de lectura.
10. **Hacer seguimiento cuando bastaba elegir el tramo quieto.** La mayoría de los planos tienen uno.
11. **Invertir 15 minutos en un elemento de un reel.** Cinco reels decentes le ganan a uno perfecto.
12. **Seguimiento en un plano de menos de 2 segundos.** No da tiempo de verse.
13. **Perseguir la perfección para Instagram.** La recompresión de la plataforma iguala el trabajo
    perfecto con el trabajo aceptable.
14. **No verificar en cámara lenta.** A velocidad normal y con ojos cansados, la deriva es invisible.

---

## Checklist

Antes de dar por bueno un gráfico que sigue algo:

- [ ] Comprobé primero si bastaba **congelar el fotograma**, **anclar al cuadro** o **elegir el tramo
      quieto**.
- [ ] El elemento que sigo **pertenece conceptualmente** al objeto (nombre, difuminado, etiqueta).
- [ ] El objeto **no se sale del cuadro** en el tramo, o corté el clip donde sí.
- [ ] El recuadro de seguimiento está sobre una zona **pequeña, con detalle y contraste**.
- [ ] Si lo hice a mano, usé **bisección** y tengo menos de 10 keyframes por cada 4 segundos.
- [ ] Si es un difuminado de cara, el área es **25% más grande** de lo necesario.
- [ ] Revisé el tramo con **tira de fotogramas** y en **cámara lenta**.
- [ ] No hay **deriva**, ni **saltos**, ni **temblor** de dos píxeles.
- [ ] El plano dura **más de 2 segundos**.
- [ ] No invertí más de **15 minutos** en este elemento.
- [ ] Si quito este gráfico, el espectador **entiende menos** (si no, lo quito).
- [ ] Anoté qué hacer distinto **al grabar** para que la próxima vez no haga falta seguimiento.
