# 05 — Lenguaje audiovisual

Resuelve el problema de **no tener palabras para lo que ves.** Sin vocabulario no puedes pedirle nada
preciso a quien graba, ni explicar por qué un corte no funciona, ni darle una instrucción exacta a una
herramienta. Este módulo es la gramática mínima: tipos de plano, encuadre, eje, continuidad.

Está escrito para vertical y video corto, no para largometraje — pero las reglas son las mismas y
llevan cien años probadas.

---

## 1. Los tipos de plano

El **plano** es lo que cabe en el cuadro. Se nombra por cuánto de la persona entra. La escala estándar,
de más lejos a más cerca:

| Plano | Qué entra | Para qué sirve |
|---|---|---|
| **Gran plano general** | el lugar, la persona diminuta o ausente | ubicar; decir dónde estamos |
| **Plano general** | la persona entera con su entorno | contexto: quién está dónde |
| **Plano entero** | de la cabeza a los pies, justo | mostrar el cuerpo completo, ropa, postura |
| **Plano americano** | de la mitad del muslo hacia arriba | acción con las manos, varias personas |
| **Plano medio** | de la cintura para arriba | el estándar de la conversación |
| **Plano medio corto** | del pecho para arriba | el estándar del talking head vertical |
| **Primer plano** | la cara, hombros apenas | emoción; es el plano que más retiene |
| **Primerísimo primer plano** | de la barbilla a la frente | intensidad máxima; incómodo si se abusa |
| **Plano detalle** | un objeto o parte del cuerpo | manos, producto, texto, un botón |

### Lo que esto cambia en video vertical

En 9:16 el cuadro es angosto y alto. Consecuencias duras:

- **El plano general casi no funciona.** La persona queda de 200 píxeles de alto en una pantalla de
  teléfono. Si necesitas contexto, usa un plano medio con algo del entorno detrás, no un general.
- **El plano medio corto es el caballo de batalla.** Cara grande, algo de hombros, fondo reconocible.
- **El plano detalle vale oro.** Manos haciendo algo, el producto, un número en pantalla. Es lo que
  llena el cuadro vertical sin esfuerzo y lo que da variedad al montaje. Ver `174`.
- **El primerísimo primer plano funciona mejor que en horizontal**, porque el vertical ya está hecho
  para caras.

### El truco del punch-in

**Punch-in** es agrandar digitalmente un plano para simular un plano más cerrado. Si grabaste en 4K
(3840x2160) y entregas en 1080x1920, tienes margen de sobra para "acercarte" sin perder calidad. Es la
segunda cámara más barata que existe: de un solo plano medio sacas plano medio + primer plano, y ya
tienes dos ángulos para cortar entre ellos.

```bash
# Punch-in del 30% sobre un vertical 1080x1920, centrado y un poco arriba
ffmpeg -i plano.mp4 -vf "crop=iw/1.3:ih/1.3:(iw-iw/1.3)/2:(ih-ih/1.3)/3,scale=1080:1920" \
  -c:v libx264 -crf 18 -c:a copy plano_cerrado.mp4
```

Regla: **el punch-in tiene que ser suficiente para que se lea como otro plano.** Un 10% se ve como un
error de encuadre; un 25–40% se lee como corte a otra cámara. Ver `22`.

---

## 2. Encuadre: dónde poner las cosas dentro del cuadro

### La regla de los tercios

Divide el cuadro en tres columnas y tres filas iguales. Los elementos importantes van sobre las líneas
o en los cruces, no en el centro exacto.

**Por qué funciona:** el centro exacto es estático y se lee como foto de documento. Fuera de centro
genera tensión y deja espacio para que pase algo.

**En vertical, la aplicación concreta:**

- Los **ojos** de la persona van sobre la línea del tercio superior. Ese es el error #1 de encuadre
  amateur: la gente centra la cara y queda mucho espacio muerto arriba.
- El **texto** va en el tercio central de la altura, porque los tercios superior e inferior los tapa
  la interfaz de la aplicación (ver `45`).
- Si la persona mira hacia un lado, el **aire de mirada** (el espacio vacío hacia donde mira) va del
  lado hacia el que mira. Mirar hacia la pared del cuadro se ve mal y nadie sabe por qué.

Guía visual para verificar rápido un encuadre:

```bash
# Superpone una rejilla de tercios sobre un fotograma para revisar el encuadre
ffmpeg -i plano.mp4 -vf "select=eq(n\,0),drawgrid=w=iw/3:h=ih/3:t=2:c=red@0.6" \
  -frames:v 1 encuadre_check.png
```

### Aire de cabeza (*headroom*)

El espacio entre la coronilla y el borde superior del cuadro. Poco aire ahoga; mucho aire deja la cara
pequeña y vacío arriba. En vertical, poco aire funciona mejor que mucho: la cara grande retiene.

### Espacio negativo

Las zonas vacías del cuadro. No son desperdicio: son donde va el texto sin tapar nada. Cuando dirijas
un rodaje pensando en la edición, pide que dejen una zona limpia — una pared lisa, un cielo — donde
después puedas poner los golpes de texto. Ver `170`.

---

## 3. El eje de acción y la regla de los 180 grados

Esta es la regla que más se rompe por accidente y la que produce ese "no sé qué pasó, se siente raro".

### Qué es

Imagina una línea recta invisible que une a dos personas que conversan, o que sigue la dirección en la
que alguien camina. Esa línea es el **eje de acción**.

La regla: **la cámara se queda siempre del mismo lado de esa línea.** Los 180 grados son el semicírculo
de un lado del eje, y ahí puedes poner la cámara donde quieras.

### Por qué importa

Si cruzas el eje, las posiciones se invierten en pantalla. La persona que estaba a la izquierda aparece
a la derecha. El espectador no sabe nombrar el problema, pero pierde la orientación: por medio segundo
cree que hay otra gente o que cambiaron de sitio.

**Ejemplo con dos personas conversando:**

- Desde el lado correcto: A mira hacia la derecha, B mira hacia la izquierda. Se miran entre sí.
- Cruzando el eje: A mira a la derecha y B **también** mira a la derecha. Parece que le hablan a una
  tercera persona fuera de cuadro.

**Ejemplo con movimiento:** un carro que cruza la pantalla de izquierda a derecha, y en el plano
siguiente cruza de derecha a izquierda. El espectador entiende que se devolvió. Si querías decir que
siguió su camino, comunicaste lo contrario.

### Cómo se cruza el eje a propósito (sí se puede)

1. **Con un plano frontal sobre el eje mismo.** Un plano de frente, neutral, y del siguiente ya puedes
   estar del otro lado.
2. **Con un plano detalle.** Cortas a las manos, al producto, a un objeto; se rompe la referencia
   espacial y al volver ya no hay conflicto.
3. **Con la cámara moviéndose y cruzando en el mismo plano.** Si el espectador ve el cruce, lo acepta.
4. **A propósito, para desorientar.** Es un recurso dramático válido cuando quieres incomodar.

### En vertical, ¿importa?

Menos, pero importa. En un talking head de una sola persona hablando a cámara no aplica. En cuanto hay
dos personas, una entrevista o un producto que se pasa de una mano a otra, aplica completo. Y en
demostraciones de producto es donde más se nota: si el producto va de izquierda a derecha en un plano
y al revés en el siguiente, se lee como error aunque nadie sepa por qué.

Recuerda el peso de Murch: esto es "espacio tridimensional", el 4% (`03`). Importa, pero se sacrifica
antes que la emoción.

---

## 4. Raccord: que los planos peguen

**Raccord** (del francés *raccorder*, "empalmar") es que dos planos consecutivos peguen entre sí en
todos los detalles: posición, gesto, luz, vestuario, objetos. Los editores hispanohablantes usan la
palabra francesa; en inglés se dice *continuity* o *matching*.

### Los cuatro raccords que se rompen todo el tiempo

| Tipo | Qué se rompe | Ejemplo |
|---|---|---|
| **De posición** | la persona o el objeto cambia de sitio | el vaso estaba en la mano derecha, ahora en la izquierda |
| **De movimiento** | la acción no continúa fluida | se levanta a medias en A y ya está de pie en B, sin transición |
| **De luz** | cambia la iluminación entre planos | se grabó a las 4 p.m. y a las 6 p.m. |
| **De vestuario / detalle** | ropa, peinado, maquillaje, objetos | el mechón de pelo estaba adelante y ahora atrás |

### Raccord de movimiento: la técnica que sí se usa a diario

Cuando cortas en medio de una acción, el corte se vuelve invisible si la acción continúa. La técnica
es **cortar en el movimiento**: si la persona levanta la taza, cortas cuando la taza va a mitad de
camino, y el plano siguiente arranca con la taza un poquito más adelante.

El truco fino: hay que **solapar ligeramente**. El plano B empieza un par de fotogramas antes de donde
terminó A, porque el cerebro tarda en procesar el cambio de plano y si no solapas, la acción parece
saltar hacia adelante.

### Cómo tapar un raccord roto

Cuando ya está grabado y no pega, tienes cuatro salidas:

1. **Un cutaway** (plano de recurso): cortas a otra cosa — las manos, el ambiente, el producto — y
   vuelves. El cerebro perdona porque perdió la referencia.
2. **Un plano detalle** puesto en medio. Igual mecanismo, más útil en vertical.
3. **Convertirlo en jump cut deliberado.** Si el video ya tiene lenguaje de saltos, un salto más no
   molesta. Es lo que hace todo el YouTube moderno.
4. **Tapar con texto o gráfico** en el momento del salto. La atención se va al texto.

Lo que **no** funciona: poner una transición bonita encima. La transición no arregla el raccord, solo
lo anuncia.

---

## 5. Continuidad de mirada

Es un caso particular de raccord, y el que más se siente aunque menos se nombre.

### La regla

Si en el plano A la persona mira hacia arriba a la derecha, en el plano B —lo que ella está mirando—
tiene que estar arriba a la derecha, o al menos coherente con esa dirección.

Y en un plano contraplano de dos personas: si A mira a la derecha, B tiene que mirar a la izquierda.
Es la misma regla de los 180 grados, vista desde los ojos.

### Miradas a cámara

Aparte y muy importante para contenido de marca:

- **Mirar a cámara** = hablarle al espectador. Directo, íntimo, vendedor. Es el estándar del reel.
- **Mirar fuera de cámara** (a un entrevistador) = documental, testimonio, "esto no es publicidad".

**No las mezcles sin razón.** Un testimonio que mira al entrevistador y de pronto mira a cámara rompe
el pacto: pasó de "estoy contando mi experiencia" a "me están pagando por decir esto". Si tienes las
dos, decide cuál es el lenguaje de la pieza y quédate ahí. Ver `154`.

### El detalle que casi nadie cuida en vertical

En 9:16, si la persona está descentrada y mira hacia el lado corto del cuadro, el aire de mirada
desaparece y se siente claustrofóbico. Al hacer punch-in o reencuadre, **respeta hacia dónde mira**:
deja el espacio del lado de la mirada, no del otro. Ver `22`.

---

## 6. El movimiento de cámara, nombrado

Para poder pedirlo y para poder identificarlo en el bruto:

| Nombre | Qué es |
|---|---|
| **Paneo** (*pan*) | la cámara gira horizontalmente sobre su eje |
| **Tilt** | la cámara gira verticalmente sobre su eje |
| **Travelling** | la cámara se desplaza físicamente en el espacio |
| **Zoom** | cambia la distancia focal; la cámara no se mueve |
| **Dolly** | travelling hacia adelante o atrás |
| **Cámara en mano** | movimiento libre, sensación de inmediatez y realidad |
| **Plano fijo** | la cámara no se mueve |

Diferencia útil de saber: **el zoom no es un travelling.** El zoom aplana la perspectiva y se lee como
lenguaje de video casero o de noticiero. El travelling cambia la relación entre el frente y el fondo,
y se lee como cine. Si alguien te pide "que se vea más cinematográfico", una de las causas puede ser
que todo el material tiene zooms.

**Regla de montaje:** no cortes de un plano en movimiento a otro plano en movimiento en dirección
distinta. Marea. Corta de movimiento a fijo, o de movimiento a movimiento en la misma dirección.

---

## 7. Cómo se usa este vocabulario en la práctica

Tres usos concretos, hoy:

**1. Para pedir material.** En vez de "grábame unas tomas del restaurante", pides:

```
- 1 plano detalle de las manos emplatando (fijo, 8 s)
- 1 plano medio corto del chef hablando a camara, aire de mirada a la derecha
- 1 plano detalle del plato terminado, con giro lento (travelling, no zoom)
- 3 planos detalle de ingredientes, fondo neutro, para b-roll
- todo en 4K vertical para tener margen de punch-in
```

Eso se puede ejecutar. Lo otro no. Ver `170`.

**2. Para diagnosticar.** "Se siente raro el corte del segundo 12" se convierte en "cruzaste el eje: en
el plano A el producto entra por la izquierda y en el B por la derecha".

**3. Para dar instrucciones precisas.** Un punch-in del 30% respetando el aire de mirada es una
instrucción ejecutable. "Acércate un poco" no lo es.

---

## Errores comunes

- **Centrar la cara en el cuadro.** Los ojos van sobre el tercio superior; centrada deja un vacío
  enorme arriba.
- **Dejar a la persona mirando hacia la pared del cuadro.** El aire de mirada va del lado hacia el que
  mira.
- **Cruzar el eje sin darse cuenta**, sobre todo en demostraciones de producto y entrevistas de dos.
- **Creer que una transición arregla un raccord roto.** No lo arregla: lo señala.
- **Cortar sin solapar en un raccord de movimiento.** La acción salta hacia adelante y se nota.
- **Usar plano general en vertical.** La persona queda diminuta; se resuelve con plano medio + entorno.
- **Punch-in del 10%.** Se lee como error de encuadre, no como otro plano. Mínimo 25%.
- **Punch-in que se come el aire de mirada.** Reencuadra respetando hacia dónde mira.
- **Mezclar mirada a cámara con mirada al entrevistador** dentro de un testimonio.
- **Cortar de un movimiento a otro en dirección contraria.** Marea.
- **Confundir zoom con travelling** cuando alguien pide look cinematográfico.
- **No pedir 4K cuando se va a entregar en 1080.** Sin margen no hay punch-in y pierdes tu segunda cámara.

---

## Checklist

Al revisar el encuadre y la continuidad de un montaje:

- [ ] Los ojos de la persona caen sobre el tercio superior en los planos de cara.
- [ ] Hay aire de mirada del lado hacia el que mira, no del contrario.
- [ ] El aire de cabeza es razonable: ni ahogado ni con medio cuadro vacío arriba.
- [ ] Hay espacio negativo disponible para poner texto sin tapar lo importante.
- [ ] Cuando hay dos personas u objetos en relación, la cámara no cruzó el eje sin justificación.
- [ ] Si el eje se cruzó, hay un plano neutro, un detalle o un movimiento visible que lo autoriza.
- [ ] Los raccords de posición, movimiento, luz y vestuario están revisados en cada corte.
- [ ] Los cortes en movimiento tienen un pequeño solape para que la acción no salte.
- [ ] Los raccords rotos que no se pudieron arreglar se taparon con cutaway o detalle, no con transición.
- [ ] La pieza mantiene un solo lenguaje de mirada (a cámara o fuera de cámara).
- [ ] Hay variedad de escala de plano: no todo es plano medio.
- [ ] Los punch-in son del 25% o más y respetan el aire de mirada.
- [ ] No hay cortes de movimiento a movimiento en direcciones opuestas.
