# 348 — El bar como escenario

**Qué resuelve:** cómo usar el local que ya tienes como set de rodaje. Un bar-restaurante es, sin gastar
un peso, mejor escenario que el 90% de los que se alquilan: madera, luz cálida, botellas, profundidad,
gente y neón. También tiene una trampa que arruina más planos que ninguna otra: **el neón de color sobre
la piel**.

Este módulo es el inventario del set y la logística de dónde poner a la gente. La ciencia del color del
neón está en `224`: **si vas a grabar personas bajo neón, lee `224` primero.**

---

## 1. Inventario: lo que ya tienes y cuánto vale

| Elemento del bar | Qué te da en cámara | Cómo se usa |
|---|---|---|
| **Barra de madera** | Textura + color cálido que combina con la piel y con la cerveza | Superficie para planos de producto (`342`) |
| **Fila de botellas** | Profundidad y "esto es un bar" en cero palabras | Fondo desenfocado |
| **Grifos / torre de cerveza** | Verticalidad y marca de categoría | Fondo o protagonista (`341`) |
| **Neón / letrero** | Color, identidad, borde de luz | **Fondo, siempre. Nunca sobre la cara** |
| **Bombillos cálidos colgantes** | Puntos de luz bonitos desenfocados | Fondo, arriba del cuadro |
| **Ventana** | La mejor luz que vas a tener | Luz principal de día (`340`) |
| **Terraza** | Luz natural y aire | Planos de día, comida fresca |
| **Cocina** | Movimiento, vapor, fuego, verdad | El formato más honesto (`351`) |
| **Gente** | Prueba social. Lo más valioso y lo más delicado | Ver `356` |

**Lo que NO tienes y no necesitas:** un fondo neutro. Nadie quiere ver una hamburguesa contra una pared
blanca; la quiere ver en un bar. Tu fondo desordenado es una ventaja si está **desenfocado y
compuesto**, no si está **enfocado y desordenado**.

---

## 2. El activo más grande de un bar: la profundidad

Un bar tiene tres planos de distancia natural, y eso es lo que hace que un video se vea "de verdad" y no
de estudio:

```
PRIMER PLANO  ~30 cm   algo desenfocado que enmarca: vaso, botella, borde de barra
PLANO MEDIO   1-2 m    el producto o la persona: EN FOCO
FONDO         3-6 m    botellas, neon, bombillos, gente: desenfocado
```

**El truco del primer plano** es el más barato y el que más eleva un video de bar: una botella o un vaso
a 30 cm del lente, a un lado del cuadro, ligeramente fuera de foco. La imagen deja de ser una foto de
plato y se convierte en un plano de cine. Cuesta 5 segundos.

**Cómo desenfocas el fondo con celular:** no hay slider mágico, solo dos palancas reales (`221`):
**(1) acércate al sujeto** —cuanto más cerca enfocas, más se desenfoca lo demás— y **(2) aleja el
fondo** —si el sujeto está a 20 cm de la pared, nada lo va a desenfocar; muévelo a la mitad del salón y
tienes 4 metros de fondo desenfocado gratis—. La segunda es la que nadie usa y la más poderosa: **mueve
la mesa, no el teléfono**.

**Modo retrato / cine para video:** funciona bien con caras y **mal con comida**, porque el recorte
falla en bordes complicados (vapor, hilos de queso, espuma, humo). Para comida: acércate de verdad.

---

## 3. El neón: activo por detrás, veneno por delante

### Lo que el neón hace bien

- **Es un fondo que trabaja solo.** Desenfocado a 3–5 metros, llena el fondo de color e identidad sin
  que tengas que componer nada.
- **Es un borde de luz de marca.** Detrás de una persona deja un filo de color en el hombro y el pelo.
  Se ve caro y es gratis.
- **Es la firma visual del local**: aparece en todos los videos y construye memoria de marca (`87`).

### Lo que el neón destruye

**La piel.** Y no se arregla después. Los números medidos:

```
Piel (clara, media y oscura):  U = 98 a 106     HUE = 126 a 140
Neon morado:                   U = 170          HUE = 244
Neon magenta:                  U = 186          HUE = 225
```

> **U = eje azul↔amarillo, 128 es neutro. HUE = el ángulo del color en el círculo.**

**Regla dura y verificada:** *la piel sana siempre mide U por debajo de 128.* Las tres pieles medidas
dieron 98, 102 y 106. Si en tu plano la piel mide U por encima de 128, **ya no hay piel en el archivo**:
hay una superficie morada con forma de cara. El detalle completo está en `224`.

**La buena noticia:** el neón morado/magenta está a **90–120 grados** del tono de piel en el círculo de
color (225–246 contra 126–140). Es muchísima separación, y es lo que permite —**cuando la cara NO está
bañada de morado**— corregir la piel sin tocar el neón del fondo, usando un selector por tono (un
"qualifier" de matiz en DaVinci o la corrección selectiva de CapCut, `253`, `211`).

**La mala noticia:** las bandas de `selectivecolor` en ffmpeg son **demasiado anchas** para aprovechar
esa separación. Comprobado: bajar el morado de una piel levemente teñida con
`selectivecolor=magentas=0 -0.25 0.20 0` la corrige a medias (U de 133 a 128) **pero también desatura el
neón del fondo** (SAT de 46 a 35), justo lo que no querías. Para esto ffmpeg es la herramienta
equivocada: usa un selector por tono en el editor, o mejor:

> **Resuélvelo al grabar. Es gratis al grabar y es imposible después.**

---

## 4. Cómo se graba a una persona en un bar con neón (el montaje que funciona)

```
       [NEON]  <- a 3-5 m DETRAS de la persona, fuera de foco
          |
          |   3-5 metros de distancia  <- clave: la luz cae con la distancia
          |
     [PERSONA]
          |
      60-90 cm
          |
   [LUZ NEUTRA]  <- lampara calida normal, o luz de ventana, o una pantalla blanca
    a las 10 en punto, con papel difusor
          |
     [CELULAR]
```

**Los tres principios:**

1. **Distancia.** La intensidad de una luz cae con el cuadrado de la distancia: a 1 metro del neón la
   cara está bañada, a 4 metros apenas la toca y el neón sigue viéndose igual de bonito **de fondo**.
   Mover a la persona 3 metros resuelve el problema sin apagar nada.
2. **Una luz neutra cerca de la cara.** Una lámpara de mesa con papel mantequilla, un bombillo cálido
   normal, la ventana si aún hay día. Lo único que importa es que **domine sobre el neón en la cara**:
   cerca + neutra vence a lejos + de color.
3. **Balance de blancos manual (bloqueado).** El automático ve el morado, cree que es la luz del sitio y
   empuja toda la imagen a verde: cara enferma y color que cambia dentro de la misma toma. Fíjalo en
   3200–3800 K y no lo toques (`224`, `228`).

**Chequeo en el sitio, sin scopes:** mira la palma de tu mano en la pantalla del celular. Si se ve
morada, estás mal parado. Muévete hasta que la palma se vea color palma. Es el chequeo más rápido que
existe y funciona con cualquier tono de piel.

---

## 5. Qué grabar cuando el bar entero está bañado en color

A veces no hay dónde pararse: el sitio completo es morado. Entonces se separan los rodajes:

```
DE DIA / LUZ DE VENTANA  ->  personas, caras, comida en detalle, producto
DE NOCHE / CON NEON      ->  ambiente, barra, botellas, gente de espaldas o en silueta,
                             manos, vasos, el letrero, planos generales del local
```

Esa división produce además mejor material: lo que el neón hace mejor no son las caras, son las
**siluetas, los brillos en el vidrio y el ambiente**. Un plano de una mano levantando una cerveza con el
neón detrás es espectacular y no tiene ni un pixel de piel en riesgo.

**Regla de montaje:** si mezclas planos de día y de neón en el mismo reel, **agrúpalos por bloques**. Un
corte entre dos planos con 4 veces de diferencia de saturación se lee como error (`62`, `224`).

---

## 6. La luz cálida del bar: tu mejor amiga

Los bombillos cálidos (2700–3000 K) de un bar son **buena luz para comida y para piel**. Ámbar de
cerveza (HUE 126), madera y piel (HUE 126–140) viven en la misma familia de tonos: se llevan bien
naturalmente. Es lo contrario del neón.

**Cómo aprovecharla:** apaga las que están **directamente encima de la mesa** y deja las de atrás
(`340`); un bombillo colgante a **1,5–2 m detrás y arriba** del plato es un contraluz de verdad; y los
bombillos del fondo desenfocados se convierten en **círculos de luz**, el mejor fondo de bar que existe.

**El problema: mezclar cálido con luz de día.** Junto a la ventana con las lámparas prendidas tienes dos
temperaturas en el mismo cuadro: un lado azul y otro naranja, y no se corrige con un ajuste global.
**Elige una y apaga la otra** (o cierra la cortina).

---

## 7. Composición vertical: el bar es alto

El 9:16 castiga lo horizontal (`342`), y ahí el bar te ayuda: está lleno de **verticales** —la torre de
grifos, una fila de botellas de pie, los bombillos colgantes, las columnas o la estantería, un vaso alto
en primer plano.

**Composición de bar en 9:16 que casi siempre funciona:**

```
TERCIO SUPERIOR   bombillos colgantes / neon desenfocado
TERCIO MEDIO      el producto o la persona, EN FOCO
TERCIO INFERIOR   la madera de la barra, un vaso en primer plano
```

Tres planos de profundidad, apilados verticalmente. Es el encuadre que hace que un celular parezca una
cámara buena.

---

## 8. Lo que hay que sacar del cuadro (revisión de 20 segundos)

Antes de cada toma, barre el cuadro con la vista:

- **Televisor prendido.** Además de feo, mete contenido con derechos y parpadeo en tu video (`78`).
- **Cables, extensiones, regletas. Bayetillas, escobas, canecas, cajas de mercado.**
- **La nevera de bebidas con etiquetas de otras marcas** (a menos que quieras mostrarlas).
- **Avisos de papel pegados con cinta. Botellas de desinfectante y aerosoles.**
- **Sillas volteadas sobre las mesas** (dice "cerrado").
- **Personas del equipo mirando a la cámara** desde el fondo.
- **Cualquier cliente reconocible que no haya dado permiso** (`356`, `319`).

Un bar tiene 15 objetos que la gente que trabaja ahí ya no ve. La cámara los ve todos.

---

## 9. El bar vacío y el bar lleno

Son dos productos distintos y sirven para cosas distintas:

- **Bar vacío (antes de abrir):** producto, detalle, preparación, todo lo que necesita silencio y
  control. Es el 80% de tu material y se graba en lote (`316`).
- **Bar lleno (viernes/sábado noche):** prueba social — murmullo, movimiento, mesas ocupadas. Planos
  cortos, de mano, imperfectos, y **está bien que lo sean**: la imperfección es la prueba de que es real.

**Combinación que funciona:** producto con control (bar vacío) + ambiente con caos (bar lleno). Ese
contraste es lo que hace que un reel de restaurante se sienta vivo y a la vez cuidado.

---

## Errores comunes

1. **Poner a alguien delante del neón.** El error más caro del bloque. La piel queda morada y no se
   arregla en post (`224`).
2. **Creer que se arregla después "bajando el morado".** Comprobado con ffmpeg: bajas la piel a medias
   y de paso desaturas el neón que sí querías.
3. **Dejar el balance de blancos en automático bajo luz de color.** El color cambia dentro de la misma
   toma, y eso sí que no se empareja.
4. **No revisar la palma de la mano en pantalla** antes de grabar a una persona.
5. **Fondo pegado al sujeto.** Sin distancia no hay desenfoque, por más modo retrato que actives.
6. **Usar modo retrato/cine para comida.** El recorte falla en vapor, espuma y hilos de queso.
7. **Mezclar luz de ventana con bombillos cálidos** en el mismo plano. Un lado azul, otro naranja.
8. **Dejar prendidas las lámparas que están justo encima de la mesa.** Luz cenital dura: ojeras y plato
   plano.
9. **Cortar de un plano de día a uno de neón** sin agrupar por bloques.
10. **No usar primer plano.** Un vaso a 30 cm del lente cambia la calidad percibida y cuesta 5 segundos.
11. **Componer horizontal en un formato vertical** teniendo el bar lleno de verticales que puedes usar.
12. **No barrer el cuadro** antes de la toma: TV prendido, cables, bayetillas, canecas, sillas
    volteadas.
13. **Grabar clientes reconocibles sin permiso** (`356`, `319`), o **grabar todo con el bar lleno**
    cuando lo que necesita control se graba con el bar vacío.

---

## Checklist

- [ ] Hay **tres planos de profundidad**: algo en primer plano, el sujeto, un fondo lejano.
- [ ] El fondo está a **más de 3 metros** del sujeto para que se desenfoque de verdad.
- [ ] Hay un **elemento en primer plano** (vaso, botella, borde de barra) enmarcando.
- [ ] Si hay neón, está **detrás y a 3–5 metros**, nunca iluminando la cara.
- [ ] Hay una **luz neutra a 60–90 cm** de la cara, dominando sobre el neón.
- [ ] **Balance de blancos fijado a mano** (3200–3800 K), no automático.
- [ ] Se hizo el **chequeo de la palma de la mano** en pantalla.
- [ ] No hay **dos temperaturas de color** mezcladas (ventana + bombillos).
- [ ] Las lámparas **justo encima de la mesa están apagadas**.
- [ ] El encuadre 9:16 usa **verticales del bar** y tiene los tres tercios ocupados.
- [ ] Se **barrió el cuadro**: sin cables, bayetillas, canecas, avisos ni TV prendido.
- [ ] No hay **clientes reconocibles sin permiso** (`356`).
- [ ] Los planos de **día** y los de **neón** están agrupados en bloques dentro del reel.
- [ ] El material de **control** (producto, detalle) se grabó con el bar vacío.
- [ ] Hay material de **ambiente** grabado con el bar lleno, guardado para usar de recurso.
