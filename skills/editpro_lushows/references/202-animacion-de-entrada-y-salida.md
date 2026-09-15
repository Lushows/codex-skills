# 202 — Animación de entrada y salida

**Qué resuelve:** el editor te ofrece 60 animaciones de entrada y 40 de salida, con nombres bonitos, y
tú las vas probando hasta que "una queda bien". El resultado es un video donde cada elemento entra de
una forma distinta y el conjunto se siente barato aunque cada pieza por separado estuviera bien. Este
módulo enseña el vocabulario real (son seis familias, no cien), por qué **repetir una sola animación se
ve más profesional que usar diez**, y los tiempos exactos.

En tus 51 proyectos, la animación de entrada más usada es **"Aparición progresiva" con 49 usos** y la
de salida es **"Flash desactivado" con 18**. Eso ya es casi un sistema. Este módulo lo termina de
cerrar.

---

## 1. Qué es una animación de entrada, en cristiano

Cuando pones una palabra, un sticker o un logo encima del video, ese elemento tiene que **llegar**.
Puede llegar de dos maneras:

- **Aparecer de golpe.** En el fotograma 100 no está, en el 101 está. Se llama *corte duro* y es una
  decisión válida (a veces la mejor).
- **Entrar animado.** Durante unos fotogramas, el elemento cambia de estado hasta quedar en su sitio:
  se hace visible, crece, se desliza, se desenfoca menos.

Lo mismo, al revés, cuando se va: **salida**.

> **Entrada:** los 0,3–0,6 segundos donde un elemento pasa de "no está" a "está".
> **Salida:** los 0,2–0,4 segundos donde pasa de "está" a "no está".
> **Loop:** una animación que no entra ni sale, se repite sola mientras el elemento vive en pantalla.

Tú usas **loop 69 veces**, más que cualquier otra animación. Tiene sentido y es correcto: un elemento
que respira levemente durante toda su vida en pantalla resuelve el problema de la imagen fija (`83`)
sin gastar tiempo entrando y saliendo.

---

## 2. Las seis familias (y ya)

Todas las animaciones que trae cualquier editor caen en seis familias. Aprende las familias, no los
nombres comerciales.

| Familia | Qué hace | Se siente | Para qué sirve |
|---|---|---|---|
| **Opacidad** (fade / aparición progresiva) | de invisible a visible | suave, neutro, elegante | casi todo; el valor seguro |
| **Escala** (pop, zoom, crecer) | de pequeño a su tamaño | energía, golpe | énfasis, palabras clave, precios |
| **Posición** (deslizar, subir, entrar por el lado) | viene de fuera de cuadro | dirección, movimiento | listas, elementos que "llegan" de algún lado |
| **Máscara** (revelado, barrido, escribir) | se descubre por partes | premium, editorial | títulos, nombres, cierres (ver `206`) |
| **Desenfoque** (blur in) | de borroso a nítido | cine, suavidad | poco usada, buena para fotos |
| **Rotación** | gira al entrar | juguetona, informal | casi siempre sobra |

**La familia de rotación es una trampa.** Se ve divertida en el editor y en pantalla se lee como
plantilla de app. Si vas a usarla, que sea muy poquita rotación (menos de 8 grados) y solo en un
elemento de humor, nunca en información.

**El nombre comercial no importa.** "Aparición progresiva" es opacidad. "Badbunny" es un efecto de
color, no una animación (ojo con confundirlos, son paneles distintos en CapCut). "Flash desactivado" es
una salida por opacidad con un golpe de brillo. Cuando sepas la familia, puedes traducir cualquier
nombre de cualquier editor.

---

## 3. La idea central: una entrada y una salida, repetidas

Esta es la parte que más cambia la percepción de calidad de tus videos, y es gratis.

Imagina dos reels. En el primero, la primera palabra entra con fade, la segunda con pop, el precio se
desliza desde abajo, el sticker gira y el logo se revela con máscara. Cinco animaciones distintas, cada
una bien hecha.

En el segundo, **absolutamente todo entra con fade + una pizca de escala**, siempre en 0,4 segundos, y
todo sale con fade en 0,25 segundos.

El segundo se ve profesional. El primero se ve armado. ¿Por qué?

> Porque el espectador no juzga cada animación por separado: juzga la **coherencia** del conjunto.
> Cuando todo se mueve igual, el cerebro deja de mirar el movimiento y mira el contenido. Cuando cada
> cosa se mueve distinto, el cerebro dedica atención a interpretar cada movimiento nuevo, y esa
> atención se la está quitando a tu mensaje.

Hay una razón más práctica: **con una sola animación, siempre queda bien.** No tienes que decidir nada
en cada elemento, no dudas, y el episodio 10 se ve igual que el episodio 1 (`208`).

**La estructura mínima de un sistema:**

- **1 entrada canónica** — la que usa el 90% de tus elementos.
- **1 entrada de énfasis** — la que usas 1 o 2 veces por video, en lo que de verdad importa.
- **1 salida canónica** — una sola, para todo.

Tres animaciones. No más. Con tus datos, ese sistema ya está casi escrito:

| Papel | Tu animación | Usos medidos |
|---|---|---|
| Entrada canónica | Aparición progresiva (opacidad) | 49 |
| Presencia en pantalla | Loop | 69 |
| Salida canónica | Flash desactivado | 18 |
| Énfasis | *(pendiente de definir: escala/pop)* | — |

Lo único que te falta es elegir conscientemente la de énfasis y usarla poco.

---

## 4. Los tiempos exactos

Los tiempos importan más que la elección de animación. Una entrada bien elegida con mal tiempo se ve
mal; una entrada aburrida con buen tiempo se ve bien.

| Elemento | Entrada | Salida | Por qué |
|---|---|---|---|
| Palabra suelta de subtítulo | 0,10 – 0,20 s | 0,08 – 0,15 s | tiene que sentirse instantánea; ver `206` |
| Texto de énfasis (una frase) | 0,30 – 0,45 s | 0,20 – 0,30 s | es un elemento con peso |
| Gráfico, sticker, ilustración | 0,40 – 0,60 s | 0,25 – 0,40 s | tiene cuerpo, tarda en llegar |
| Logo o cierre de marca | 0,45 – 0,60 s | 0,30 – 0,40 s | es lo último, puede respirar |
| Dato duro (precio, dirección) | 0,35 – 0,50 s | **no sale animado** | se queda quieto y corta duro |

**La banda de 300 a 600 milisegundos es el territorio del motion en video social.** Todo lo que sea un
gráfico vive ahí. Por debajo de 300 ms parece un parpadeo; por encima de 600 ms el espectador ya se
aburrió esperando que el elemento termine de llegar.

**Las dos reglas de tiempo que nunca fallan:**

1. **Lo que sale, sale más rápido de lo que entró.** Entre el 60% y el 70% de la entrada. Si entró en
   0,5 s, sale en 0,3 s. Cuando la salida dura lo mismo que la entrada, se siente como si al elemento
   se le hubiera escapado a alguien.
2. **Nada entra en más de 0,6 segundos.** En vertical, una entrada de 1 segundo se siente eterna. Si
   necesitas más tiempo, lo que necesitas es que el elemento **se quede** más tiempo, no que llegue
   más lento.

### Cuánto tiene que estar quieto

Un error frecuentísimo: el elemento entra en 0,5 s, se queda 0,3 s y se va en 0,3 s. Total 1,1
segundos, de los cuales solo 0,3 estuvo legible. Nadie lo leyó.

> **La regla del doble:** un elemento tiene que estar **quieto** al menos el doble de lo que tardó en
> entrar. Si entra en 0,5 s, se queda mínimo 1,0 s antes de empezar a salir.

Para texto, además, súmale tiempo de lectura: un segundo por cada tres palabras, mínimo 1,2 segundos
aunque sea una sola palabra.

---

## 5. La curva: por qué tu animación se ve barata aunque el tiempo esté bien

Ya está desarrollado en `84`, pero el resumen que necesitas aquí:

**Una animación lineal se ve barata.** Punto. Si el elemento avanza la misma distancia en cada
fotograma, el ojo lee "computadora", no "objeto".

Lo que tiene que pasar:

- **Lo que entra frena** (ease out). Llega rápido y se acomoda despacio.
- **Lo que sale acelera** (ease in). Arranca despacio y se va rápido.

En CapCut, las animaciones de entrada que trae ya vienen con curva razonable: no tienes que hacer
nada. El problema aparece cuando animas a mano con keyframes (`203`), porque los keyframes por defecto
son **lineales**. Ahí sí hay que entrar a la opción de velocidad del keyframe y cambiarla.

En ffmpeg, la entrada de opacidad ya trae curva incorporada en el filtro `fade`:

```bash
ffmpeg -i base.mp4 -i grafico.png -filter_complex \
  "[1:v]format=rgba,fade=t=in:st=2.0:d=0.45:alpha=1,fade=t=out:st=5.2:d=0.28:alpha=1[g];\
   [0:v][g]overlay=x=(W-w)/2:y=H*0.62:enable='between(t,2.0,5.5)'" \
  -map 0:a -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

Fíjate: entrada 0,45 s, salida 0,28 s (62% de la entrada), y el elemento vive de 2,0 a 5,5 segundos,
de los cuales está completamente quieto desde 2,45 hasta 5,2 — casi tres segundos. Ese es un elemento
que sí se lee.

---

## 6. La combinación que siempre funciona

Si solo te vas a llevar una cosa de este módulo, llévate esta receta. Es la entrada canónica que casi
nadie mejora:

> **Opacidad de 0 a 100, más escala de 92% a 100%, en 0,40 segundos, con frenado.**

Por qué funciona:

- La opacidad sola es limpia pero **plana**: el elemento aparece sin presencia física.
- La escala sola es enérgica pero **agresiva**: el elemento aparece de golpe y salta.
- Las dos juntas, con la escala partiendo del 92% (no del 50%, no del 0%), producen la sensación de que
  el elemento **se acerca** desde un poco atrás. Es sutil, se siente físico y no distrae.

El número clave es **92%**. Todo el mundo empieza en 0% o en 50% y por eso todas las entradas se ven
como pop de app. Entre 88% y 95% es donde vive lo elegante.

Para la salida canónica: opacidad a 0 en 0,25 s **sin tocar la escala**. Las salidas que encogen se
ven como si el elemento se cayera dentro de la pantalla.

En CapCut esto se arma combinando la animación de entrada de opacidad con dos keyframes de escala
(`203`). Vale la pena hacerlo una vez, guardarlo como plantilla de texto y no volver a pensarlo (`88`).

---

## 7. Cuándo NO animar la entrada

Tres casos donde el corte duro le gana a cualquier animación:

**1. Subtítulos palabra por palabra a ritmo rápido.** Si la palabra dura 0,4 segundos en pantalla, una
entrada de 0,2 s se come la mitad de su vida. Corte duro y ya. Es más legible y se siente más
percusivo.

**2. Cuando el elemento entra justo en un corte de plano.** El corte ya es un evento visual. Si además
el gráfico entra animado, hay dos cosas pasando y compiten. Deja que el gráfico simplemente **esté**
en el primer fotograma del plano nuevo.

**3. Efectos de golpe.** Un flash, un destello, un cambio de color a tiempo con la música. Eso no
entra: **golpea**. Animarlo lo arruina.

Corolario general: **cuanto más rápido el ritmo, menos animación**. Un video acelerado a 2,5x con
cortes cada segundo no necesita entradas suaves; necesita que las cosas estén o no estén.

---

## 8. El loop: tu animación más usada

69 usos. Merece su sección.

Un loop es una animación que se repite mientras el elemento está en pantalla: una pulsación de escala,
una flotación leve, un balanceo. Sirve para una cosa concreta y muy valiosa:

> **El loop mantiene vivo un elemento que tiene que quedarse mucho tiempo en pantalla.**

Un sticker que va a estar 6 segundos, quieto, se muere y se vuelve invisible para el ojo (`83`). Con
un loop leve, sigue existiendo.

**Los números del loop que funciona:**

- **Amplitud pequeñísima:** escala entre 98% y 102%. Movimiento entre 4 y 10 píxeles. Si se nota
  conscientemente, está muy fuerte.
- **Ciclo lento:** entre 1,5 y 3 segundos por vuelta. Los loops rápidos parecen nerviosos.
- **Solo un elemento a la vez.** Dos cosas pulsando en pantalla se pelean.

**El error del loop:** ponerlo en un elemento que solo va a estar 1,5 segundos. No alcanza a dar ni un
ciclo y se ve como un tirón raro. Loop solo en elementos de 3 segundos o más.

---

## Errores comunes

1. **Usar una animación distinta en cada elemento.** Es el error madre del módulo. Una entrada, una
   salida, y ya.
2. **Elegir por el nombre bonito.** Los nombres comerciales no dicen nada. Piensa en familias:
   opacidad, escala, posición, máscara, desenfoque, rotación.
3. **Entradas de un segundo.** Se sienten eternas en vertical. El techo es 0,6 s.
4. **Salidas tan largas como las entradas.** La salida va al 60–70%. Siempre.
5. **No dejar el elemento quieto.** Entra 0,5, se queda 0,3, sale 0,3: nadie lo leyó. Mínimo el doble
   de la entrada quieto.
6. **Escala que arranca en 0% o 50%.** Se ve como pop de aplicación. Arranca en 92%.
7. **Salida que encoge.** Parece que el elemento se cayó dentro de la pantalla. Sale por opacidad.
8. **Animación de rotación en información.** Se lee como plantilla. Resérvala para humor, y con menos
   de 8 grados.
9. **Animar la entrada de subtítulos rápidos.** Si la palabra vive 0,4 s, la animación se come su vida.
   Corte duro.
10. **Animar un gráfico que entra justo en un corte de plano.** Dos eventos compitiendo. Que
    simplemente esté.
11. **Loop en un elemento de 1,5 segundos.** No alcanza un ciclo, se ve como tirón.
12. **Loop demasiado fuerte.** Si lo notas conscientemente, está mal. 98%–102% de escala.
13. **Dos loops a la vez.** Se pelean.
14. **Animar la salida del dato duro.** El precio y la dirección se quedan quietos y cortan duro.
15. **Confundir efecto con animación.** "Badbunny" o "Cassette defectuoso" son efectos de imagen, no
    animaciones de entrada. Viven en otro panel y se cuentan aparte en el presupuesto de movimiento
    (`200`).

---

## Checklist

Antes de dar por buenas las animaciones de un video:

- [ ] Todo el video usa **una sola entrada canónica**, salvo 1–2 elementos de énfasis.
- [ ] Todo el video usa **una sola salida canónica**.
- [ ] Ninguna entrada pasa de **0,6 segundos**.
- [ ] Cada salida dura entre el **60% y el 70%** de su entrada.
- [ ] Cada elemento está **quieto al menos el doble** de lo que tardó en entrar.
- [ ] El texto está en pantalla al menos **1,2 segundos** aunque sea una palabra.
- [ ] Si usé escala en la entrada, arranca en torno al **92%**, no en 0% ni 50%.
- [ ] Ninguna salida **encoge** el elemento.
- [ ] Los **subtítulos rápidos** entran a corte duro, sin animación.
- [ ] Ningún gráfico entra animado **justo encima de un corte** de plano.
- [ ] Los **loops** están solo en elementos de 3 s o más, con amplitud 98%–102% y ciclo de 1,5–3 s.
- [ ] Hay **un solo loop** activo a la vez.
- [ ] El **dato duro del cierre** no tiene animación de salida.
- [ ] Si volviera a editar mañana, sabría exactamente **qué entrada y qué salida usar** sin pensarlo.
