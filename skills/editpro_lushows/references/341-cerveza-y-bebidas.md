# 341 — Cerveza y bebidas en cámara

**Qué resuelve:** el plano que más vende en un bar y el que más veces sale mal. Una cerveza mal filmada
no se ve "menos bonita": se ve **tibia**. Y una cerveza que se ve tibia no la pide nadie.

Este módulo es de física de la cerveza aplicada a cámara: espuma, condensación, vidrio y vertido. La
dirección de manos y tiempos está en `237`; la luz, en `340`; el color, en `345`.

---

## 1. Las cuatro cosas que tu cliente lee en 0,8 segundos

Cuando alguien ve una cerveza en pantalla, su cerebro decide si está fría **antes de leer un solo
texto**. Las señales son estas cuatro, en orden de peso:

| Señal | Qué comunica | Se consigue con |
|---|---|---|
| **Condensación en el vidrio** | "Está helada" | Física: vaso más frío que el punto de rocío |
| **Espuma blanca y densa** | "Está recién servida, está viva" | Vaso limpio de grasa + vertido correcto |
| **Burbujas subiendo** | "Está gasificada, no está muerta" | Contraluz + no agitar antes |
| **Color ámbar atravesado por luz** | "Sabe" | Contraluz obligatorio (`340`) |

Las cuatro son **contraluz** y ninguna sobrevive a la luz frontal. Ese es el resumen del módulo.

---

## 2. La espuma: tu carta blanca gratis

Aquí hay un dato medido que te sirve dos veces.

Se midió el color de una espuma de cerveza típica en YUV:

```
Espuma  (#F5EFE0):   Y = 221    U = 121    V = 132    Saturacion = 8
Cerveza (#C87A18):   Y = 131    U =  73    V = 169    Saturacion = 68
```

> **Y = brillo. U y V = los dos canales de color; 128 es el gris neutro.
> Saturación = qué tan lejos del gris está el color.**

Lee lo que dice ese número: la espuma tiene **saturación 8**. Es prácticamente **blanco puro**. Y tiene
Y=221, o sea es lo más brillante del cuadro.

**Consecuencia 1 — la espuma es tu referencia de blanco.** En cualquier plano donde haya espuma tienes
un objeto que **debe** salir blanco. Si en tu material la espuma salió amarilla, azulosa o rosada, tu
balance de blancos está mal, y ya sabes exactamente cuánto y hacia dónde corregir (`345`, `252`).

**Consecuencia 2 — la espuma es el chivato de que te pasaste de "cálido".** Es el error #1 de la
corrección de color de comida: la gente calienta la imagen para que la cerveza se vea rica y termina
con espuma color crema-orina. Umbral medido y verificable:

```
Espuma con saturacion  <= 12  -> se lee como espuma blanca. BIEN.
Espuma con saturacion  15-20  -> se lee "amarillenta". SOSPECHOSO.
Espuma con saturacion  >  20  -> se lee sucia. La cerveza parece vieja. MAL.
```

Lo mides en un fotograma con una línea (`108`):

```bash
ffmpeg -i cerveza.mp4 -vf "crop=120:120:X:Y,signalstats,metadata=print" -f null -
```
donde `X:Y` es la esquina superior izquierda de un recorte que caiga **solo sobre la espuma**.

### Cómo se consigue espuma densa (y no burbujas grandes de gaseosa)

Esto no es cámara, es operación de barra, y es lo que separa un plano bueno de uno triste:

1. **El vaso tiene que estar limpio de grasa.** Grasa de labial, dedos, jabón mal enjuagado o paño con
   suavizante **mata la espuma en segundos**. Prueba de 5 segundos: moja el vaso por dentro; si el agua
   se corre en película uniforme está limpio, si se queda en gotas separadas hay grasa y ese vaso no
   sirve para cámara.
2. **Vaso mojado, no seco.** Enjuagado con agua fría, la espuma queda más pareja y no se pega de un lado.
3. **Vertido en dos tiempos** (sección 5).
4. **No demasiado helada.** A temperatura de congelador la cerveza suelta menos gas y da menos espuma:
   la de nevera normal da mejor espuma para cámara.

---

## 3. La condensación: cuándo aparece de verdad (con los números de Tocancipá)

La condensación no es magia ni "salir con el vaso rápido". Es un umbral:

> **Se condensa agua sobre el vidrio cuando la superficie del vaso está por debajo del punto de rocío
> del aire del bar.**

Tocancipá está a **2.605 msnm**, la temperatura anda entre **7 y 19 °C** y la humedad relativa es
altísima: entre **82% y 91%** según el mes. Con esos números, el punto de rocío calculado:

```
Aire del bar      Humedad     Punto de rocio
  12 °C             85%           9,6 °C
  14 °C             85%          11,5 °C
  16 °C             85%          13,5 °C
  18 °C             90%          16,3 °C
```

**Lectura práctica para ti:**

- Un vaso de nevera normal (**~4 °C**) está muy por debajo del punto de rocío en cualquier noche de
  Tocancipá → **se va a condensar sí o sí**. Tienes el clima a favor.
- Un vaso a temperatura ambiente **jamás** se va a condensar, por más rápido que lo saques.
- **El vaso congelado (−10 a −18 °C) se escarcha**, que también se ve espectacular, pero la escarcha es
  opaca y tapa el color. Sirve para "está helada", no para "mira ese ámbar".

**El tiempo que tienes:** la condensación se forma visiblemente en **20 a 60 segundos** y aguanta bien
**3–4 minutos** antes de chorrear y dejar regueros. Ese es tu bloque de grabación. Por eso el orden es:
**cámara montada, luz montada, foco bloqueado, y ENTONCES sale el vaso** (`237`).

**Lo que NO debes hacer:** rociar el vaso con atomizador para "simular" condensación. Se nota — las
gotas de atomizador son todas del mismo tamaño y se reparten parejo, mientras la condensación real
tiene gotas distintas, más densas abajo, y algunas corren. Además es mentir sobre el producto (`347`).

**Cómo se filma para que se vea:** contraluz, siempre. Cada gota es una lente diminuta que concentra la
luz de atrás y se vuelve un punto brillante. Con luz frontal esas mismas gotas son manchas grises que se
leen como **vaso sucio**: la diferencia entre "helada" y "llevaba rato ahí".

---

## 4. El vidrio: lo que se ve bien y lo que se ve triste

| Se ve bien | Se ve triste | Por qué |
|---|---|---|
| Vaso liso, de pared delgada, transparente | Vaso grueso con relieve o logos gastados | El relieve rompe el paso de luz y la cerveza pierde el ámbar |
| Vaso alto (tulipa, pilsner, weizen) | Vaso pequeño y ancho | Más columna = más burbujas visibles subiendo |
| Vaso limpio con condensación | Vaso con huellas o regueros de espuma seca | En primer plano se ve TODO |
| Botella con etiqueta al frente y recta | Botella con etiqueta torcida o mojada | Lee "descuidado" |
| Fondo oscuro detrás del vaso | Fondo claro detrás del vaso | Contra fondo claro no se ve ni la burbuja ni el filo |

**El detalle que casi nadie cuida:** en primer plano de vaso vas a ver **el reflejo del cuarto** en el
vidrio. Si detrás de ti hay una ventana, una pantalla o una lámpara, vas a ver eso reflejado en la
cerveza. Muévete hasta que el reflejo desaparezca o pon un cartón negro donde estaba la lámpara. Es
15 segundos de trabajo y limpia el plano por completo.

---

## 5. El vertido que antoja: cómo se filma

El vertido es el plano rey. Es el único plano que combina movimiento, sonido, espuma y translucidez de
una sola vez. Y se hace mal casi siempre por dos razones: **muy rápido** y **demasiado lejos**.

### Montaje

```
                LUZ (lampara con difusor / ventana)
                   ▓▓▓▓▓▓▓▓
                       \  <- a las 10 u 11 en punto
                        \
   [FONDO OSCURO]      [VASO]         <- vaso a 25-35 cm del lente
   madera / tabla /       |
   carton negro       [CELULAR en tripode o apoyado]
                          ^
                     REBOTE BLANCO al lado opuesto
```

- **Cámara fija.** El vertido ya tiene movimiento; si además mueves la cámara, se vuelve ruido.
- **Altura del lente: a la altura del líquido**, no arriba. A ras se ve la columna subiendo; desde
  arriba solo se ve un círculo de espuma.
- **Distancia: 25–35 cm.** Suficientemente cerca para que el vaso llene 2/3 del alto del cuadro 9:16.
  Si necesitas estar más cerca de 15 cm, usa el modo macro / la lente 0,5× (en iPhone el ultra gran
  angular enfoca hasta ~2 cm).
- **Foco y exposición bloqueados antes de servir.** Si no, el celular reenfoca cuando entra el chorro y
  pierdes la toma.

### El vertido en sí (esto es de barra, no de cámara)

```
1. Vaso inclinado a 45°, el chorro cae sobre la pared interna.
   -> la cerveza baja sin romper el gas. Poca espuma todavia.
2. A la mitad, enderezas el vaso poco a poco.
3. El ultimo tercio cae al centro, directo.
   -> ahi se forma la espuma densa, de dos dedos.
4. Sueltas. Dejas correr 3 segundos con la camara grabando.
   -> la espuma "se asienta": las burbujas grandes revientan y queda cremosa.
      ESE es el plano bonito, y esta DESPUES del vertido.
```

**El error de tiempo más común:** cortar la cámara apenas se deja de servir. Lo mejor está en los 3–5
segundos siguientes: la espuma bajando, apretándose y quedando lisa. Graba mínimo **10 segundos
después** de terminar de servir.

### Velocidad

El vertido es el caso clásico de cámara lenta, pero **no toda la toma**. Ver `344`: el patrón que
funciona es *velocidad normal en la aproximación → lenta en el chorro y la espuma → normal al levantar
el vaso*. Cámara lenta de principio a fin se siente muerta.

---

## 6. Bebidas que no son cerveza

- **Cóctel con hielo:** el hielo es el protagonista. Hielo **transparente y grande** se ve caro; hielo
  de cubetera, blanco y pequeño, se ve barato. A contraluz el hielo transparente prende. Graba el
  momento en que el hielo cae y el líquido salta.
- **Jugo / limonada:** son opacos, así que la translucidez trabaja menos. Compénsalo con **movimiento**
  (revolver, verter) y con **condensación**.
- **Gaseosa:** el efecto que vende es el burbujeo al servir. Ese plano dura 4 segundos, se graba a
  contraluz y a ras.
- **Café / bebida caliente:** cambia todo — el que vende es el **vapor**, y el vapor **solo se ve a
  contraluz contra fondo oscuro** (`343`).
- **Michelada / bebida con escarchado de sal o chile:** luz rasante lateral, para que cada grano del
  borde proyecte su sombra. Contraluz puro deja el borde plano.

---

## 7. La parte legal, en corto

Todo contenido que promueva bebidas alcohólicas en Colombia está sujeto a la **Ley 124 de 1994**, cuyo
artículo 3 exige que la publicidad haga referencia expresa a la prohibición de venta a menores. El
tratamiento completo —qué dice exactamente, si aplica a lo orgánico o solo a la pauta, cómo se pone en
un reel 9:16 sin dañar el video— está en `349`, sección 8. **Léelo antes de publicar el primer video de
cerveza.** También hay contexto de riesgos en `319`.

---

## Errores comunes

1. **Filmar la cerveza con luz frontal.** Mata las cuatro señales de la sección 1 de un solo golpe. El
   ámbar se vuelve café.
2. **Vaso con grasa.** No hay espuma, y sin espuma la cerveza se ve muerta. Prueba del agua antes de
   grabar.
3. **Rociar el vaso con atomizador** para fingir condensación. Se nota y es mentir sobre el producto.
4. **Cortar la cámara apenas termina de servir.** Los 3–5 segundos de espuma asentándose son el plano.
5. **Vertido demasiado rápido.** Sale todo espuma, se ve descuidado y el chorro sale borroso.
6. **Fondo más claro que el vaso.** No se ven ni las burbujas ni el filo de luz. Pon madera, una tabla o
   un cartón oscuro detrás.
7. **Calentar el color hasta que la espuma se pone amarilla.** Umbral: saturación de la espuma > 20 y ya
   se lee sucia (`345`).
8. **Vaso de congelador para el plano que quiere lucir el color.** La escarcha es opaca y tapa el ámbar.
   Congelado = plano de "helada"; nevera = plano de "mírala".
9. **Dejar la exposición en automático.** El chorro claro entra en cuadro, el celular baja la exposición
   y el vaso se oscurece a mitad de toma.
10. **No revisar el reflejo del cuarto en el vidrio.** En primer plano se ve la ventana, la pantalla y
    a veces a ti mismo grabando.
11. **Grabar el vaso a más de 4 minutos de sacado.** Ya está chorreando, ya no hay gotas finas, ya hay
    reguero en la base.
12. **Cámara lenta de principio a fin.** El vertido pide lentitud en el chorro, no en la mano que
    entra (`344`).
13. **Publicar el video de cerveza sin la leyenda de la Ley 124.** Ver `349`.

---

## Checklist

- [ ] El vaso pasó la **prueba de grasa** (el agua se corre en película, no en gotas).
- [ ] El vaso salió de **nevera** (para lucir color) o de **congelador** (para lucir escarcha) —
      decisión tomada a propósito.
- [ ] La **luz está detrás o atrás-lateral**, a las 10 u 11 en punto (`340`).
- [ ] El **fondo es más oscuro** que la cerveza.
- [ ] Hay **rebote blanco** en el lado opuesto.
- [ ] **Foco y exposición bloqueados** antes de que entre el vaso.
- [ ] Se revisó que **no haya reflejos** de ventana, pantalla o lámpara en el vidrio.
- [ ] El lente está a la **altura del líquido**, a 25–35 cm.
- [ ] El vaso ocupa **2/3 del alto** del cuadro 9:16.
- [ ] El vertido va **en dos tiempos** (45° → enderezar → centro).
- [ ] La cámara siguió grabando **10 segundos después** de terminar de servir.
- [ ] La **espuma se ve blanca** en pantalla (saturación medida ≤ 12).
- [ ] La condensación se grabó **entre 20 s y 4 min** de sacado el vaso.
- [ ] No se usó atomizador ni ningún truco que mienta sobre el producto (`347`).
- [ ] La pieza final lleva la **leyenda de la Ley 124** cuando corresponde (`349`).
