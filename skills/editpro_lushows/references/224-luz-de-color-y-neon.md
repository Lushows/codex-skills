# 224 — Luz de color y neón

**Qué resuelve:** el problema más caro de tu material. Tu bar tiene neón morado, y en los planos que se
midieron la piel **no era piel**: era una superficie morada con forma de cara. Este módulo explica por
qué pasa, por qué **no se arregla después**, y cómo grabar en ese mismo bar —esta noche, tú solo, con
el celular— para que la cara se vea de color piel y el neón siga viéndose espectacular de fondo.

Es el módulo central del bloque. Si solo lees uno, que sea este.

---

## 1. Lo que midió tu material, y qué significa exactamente

Los planos del bar dieron estos números:

```
U (canal azul)  = 165     (neutro = 128)
V (canal rojo)  = 168     (neutro = 128)
Saturacion      =  57
Luminancia      = 70 a 104 segun el plano

La terraza de dia dio saturacion = 13
```

Traducción, término por término:

> **U y V (también llamados Cb y Cr):** los dos canales que llevan **el color** de un video. La imagen
> se guarda separada en brillo (Y) y color (U y V). El valor **128 es el gris neutro**: sin color. U
> por encima de 128 = tira a azul; por debajo = tira a amarillo. V por encima de 128 = tira a rojo; por
> debajo = tira a verde-cian.

> **Saturación:** qué tan intenso es el color, medido como la distancia desde el gris neutro. 0 = blanco
> y negro. Un valor de 57 es **muy alto** para una escena real con gente.

**Ahora la lectura experta, que es donde está el diagnóstico:**

**a) El plano entero estaba teñido, no solo una parte.** La saturación es la distancia desde el punto
neutro. Con U=165 y V=168:

```
distancia = raiz( (165-128)^2 + (168-128)^2 )
          = raiz( 37^2 + 40^2 )
          = raiz( 1369 + 1600 )
          = raiz( 2969 )
          = 54,5
```

Y la saturación medida fue **57**: prácticamente el mismo número. Eso solo pasa cuando **todo el cuadro
apunta al mismo color**. Si el neón fuera un letrero al fondo y la cara estuviera neutra, el promedio
de U y V estaría cerca de 128 aunque la saturación fuera alta. No es el caso: el morado bañaba la
escena entera.

**b) U=165 es la prueba forense.** La piel humana, de cualquier tono, en video sano, tiene **U por
debajo de 128** (poco azul) y **V por encima de 128** (mucho rojo). Un U=165 significa que en esa
imagen hay **más azul que gris**: no es una cara mal balanceada, es una cara pintada de morado.

**c) 57 contra 13 es una diferencia de 4,4 veces**, el salto entre tu plano de bar y tu plano de
terraza. Ningún emparejamiento de color (`62`) cruza esa distancia sin destrozar uno de los dos. Por
eso el editor terminó usando una sola locación.

---

## 2. Por qué el balance de blancos automático falla exactamente aquí

> **Balance de blancos:** el ajuste que le dice a la cámara de qué color es la luz del sitio, para que
> lo blanco salga blanco.

El automático de cualquier cámara del mundo funciona con una suposición: **"si promedio toda la escena,
me debería dar gris"**. Se llama la hipótesis del mundo gris, y es cierta en el 95% de las escenas
reales, porque las escenas normales tienen de todo un poco.

Un bar bañado en neón morado es el 5% restante. Cuando el celular promedia y le da morado, hace lo
único que sabe hacer: **empuja toda la imagen hacia el color contrario** (verde amarillento) para
"neutralizarla". Resultado: el morado del bar se apaga y se ensucia (pierdes justo lo que te gustaba
del sitio), la piel —que ya estaba morada— se va hacia el verde y queda **enferma**, y como el
promedio cambia cada vez que alguien se mueve o pasa un mesero, **el color cambia dentro de la misma
toma**. Eso último es lo peor de todo, porque los saltos entre planos se emparejan y los saltos dentro
de un plano no.

**Conclusión operativa:** bajo luz de color, el automático no es "menos preciso". Está **resolviendo
un problema distinto al tuyo**. Hay que apagarlo.

---

## 3. La trampa que casi nadie conoce: el balance de blancos no puede quitar el morado

Aquí está el dato técnico que cambia la estrategia entera.

El balance de blancos tiene **dos ejes**, no uno:

```
Eje 1 - TEMPERATURA (Kelvin):  azul  <------->  ambar/naranja
Eje 2 - TINTE (tint):          verde <------->  magenta
```

Las apps de celular casi siempre te dan **solo el primero**: un deslizador de Kelvin, de 2.000 a 8.000.

El morado del neón vive en **el segundo eje** (magenta). Y aquí está el problema:

> **No puedes corregir un tinte magenta moviendo el deslizador de Kelvin.**
> Puedes hacerlo más azul o más naranja, pero el magenta se queda ahí.

Es geometría de colores, no una limitación del celular. Por eso mucha gente pasa media hora moviendo el
Kelvin y la cara sigue morada: **están moviendo la perilla equivocada**.

**Qué apps te dan el eje de tinte:** Blackmagic Camera (gratis, iOS y Android) tiene Kelvin **y** tint;
Filmic Pro también. La cámara nativa, casi nunca.

**La conclusión estratégica, que es el corazón de este módulo:**

> Como la herramienta de color de la cámara **no puede** quitar el morado de la piel, la piel hay que
> protegerla **físicamente**, con la posición de la luz y de la persona. No es una preferencia
> estilística: es que la otra vía no existe.

---

## 4. La razón profunda: la información roja no se grabó

Aún hay una capa más abajo, y explica por qué ni siquiera un colorista profesional con equipo de
$50 millones te salva el plano.

> **Espectro de una fuente de luz:** de qué colores está compuesta esa luz. El sol y una bombilla
> incandescente tienen **todos** los colores mezclados. Un neón o un LED de color barato tienen solo
> unas franjas estrechas.

La piel se ve del color que se ve porque **refleja el rojo y el naranja** que le llegan. Si en el
rincón donde grabas la única luz es morada, **no hay luz roja ni naranja en el aire**. La piel no tiene
qué reflejar. La cámara no recibe información roja porque no existe.

Corregir eso después no es "ajustar": es **inventar**. Y se ve inventado: parches, bordes sucios, un
tono de piel plástico que no coincide con las manos.

**La frase que hay que interiorizar:**

> Lo que no iluminó a la persona, no se grabó. Y lo que no se grabó, no se recupera.

**Consecuencia práctica y barata:** basta con que **llegue algo de luz neutra** a la cara —no hace
falta que domine, solo que exista. Una lámpara de escritorio, la linterna de otro celular con una
servilleta encima, una vela grande. Con eso la piel ya tiene rojo que reflejar.

---

## 5. Los siete movimientos que salvan la piel EN RODAJE

Todos gratis o casi. Todos los puedes hacer esta noche.

### Movimiento 1 — La jerarquía: el color va DETRÁS, la luz neutra va DELANTE

Es la regla madre. El neón deja de ser la luz principal y pasa a ser **decorado y contra** (`223`).

```
   [ NEON MORADO ]   <- pared del fondo, a 4-6 m
          .
          .
      [ PERSONA ]
          ^
   [ luz neutra ]     <- lampara del bar, LED, linterna con servilleta.
                         A 45 grados, cerca de la cara (1 m).
      [ CELULAR ]
```

Consigues las tres cosas a la vez: piel de color piel, neón bien morado de fondo, y separación de
figura y fondo. **Es exactamente así como se hacen los videos de bar que te gustan.**

### Movimiento 2 — La distancia mata el tinte (ley del inverso del cuadrado)

Si la persona está a 50 cm del neón, se está bañando en él (`223`, sección 3):

```
Persona a 0,5 m del neon -> tenida por completo
Persona a 1 m            -> 1/4 del tinte
Persona a 2 m            -> 1/16 del tinte
Persona a 3 m            -> practicamente nada
```

**Caminar tres metros es la corrección de color más eficiente que existe.**

### Movimiento 3 — Usar el neón como contra, no como frontal

Neón **detrás** de la persona: le pinta un filo morado en el pelo y el hombro. Ese filo es precioso y
**no toca la piel de la cara**. Es lo mejor de los dos mundos y es literalmente girar a la persona 180°.

### Movimiento 4 — Bloquear el color con algo negro

Un cartón negro, una carpeta o una bandeja, apoyada fuera de cuadro entre el neón y la cara. En cine se
llama **bandera**; en tu bar es un menú de tapa dura. Corta el morado de la cara y deja el del fondo
intacto.

### Movimiento 5 — Elegir colores que la piel sí sobrevive

| Color de la luz sobre la cara | Qué le hace a la piel | Veredicto |
|---|---|---|
| **Ámbar / naranja cálido** | La piel se ve más cálida y sana | ✅ La piel lo agradece |
| **Rosa muy suave** | Favorece, se ve bien | ✅ Aceptable |
| **Amarillo pálido / cian claro** | Apaga la piel, la deja gris | 🟡 Solo como contra |
| **Magenta / morado** | Piel violeta. Destruye. | ❌ Nunca en la cara |
| **Verde / azul profundo** | Piel enferma o muerta, sin rojo | ❌ Nunca |

Si el bar tiene neones de varios colores, **usa el más cálido para la cara y los otros para el fondo**.

### Movimiento 6 — Contraste de color: la lógica que usa todo el cine

Si el ambiente es frío o magenta, ilumina la cara con algo **ligeramente cálido** (3.800–4.500 K). La
cara se separa del ambiente por color, no solo por brillo, y la imagen se ve rica en vez de monótona:
piel cálida sobre fondo frío es la fórmula que usa prácticamente toda la publicidad nocturna. Con una
lámpara de bombillo cálido apuntando a la cara y el neón atrás, ya lo tienes.

### Movimiento 7 — Vigilar que un canal no se queme solo

Un fallo silencioso: bajo luz morada intensa, los canales **rojo y azul** reciben muchísimo y el
**verde** casi nada, así que el rojo y el azul pueden estar clavados en el máximo sobre la cara aunque
la imagen no se vea "quemada" en general. Esa zona **pierde toda la textura de piel** y queda como una
mancha lisa de color.

**Cómo se evita:** bajar la exposición general un poco más de lo normal en escenas de neón fuerte
(`222`), o —mejor— reducir el neón que llega a la cara con los movimientos 1 a 4.

---

## 6. El protocolo de 4 minutos en el bar

Antes de la primera toma buena. Se hace una vez por sitio.

**1. Instala Blackmagic Camera** (gratis) si no la tienes. Es lo único que te da balance manual con
tinte, cebras e histograma.

**2. Coloca a la persona** según el movimiento 1: neón detrás y lejos, luz neutra al frente y cerca.

**3. Fija el balance de blancos a mano** sobre la luz que le da a la **cara**, no sobre el ambiente:
~3.200 K si es la lámpara cálida del bar, ~5.000–5.600 K si es un LED blanco o la linterna de un
celular, ~5.500–6.500 K si es la ventana. Y si tienes control de tinte, muévelo **hacia el verde lo
justo** para compensar el magenta que igual llegue: dos toques, no diez.

**4. Pon una hoja de papel blanca** donde va la cara, grábala 3 segundos y quítala: es tu referencia de
blanco para después (`228`).

**5. Graba 10 segundos de prueba** y míralos en la pantalla al 100% de brillo, tapando el reflejo:
¿la cara es color piel o es morada, verde o gris? ¿el neón del fondo sigue siendo morado y bonito?
¿se le ven los ojos?

**6. Mide.** Esta es la parte que te diferencia. Pasa el clip de prueba al PC y corre:

```bash
# Escena completa. Para medir SOLO LA CARA, antepon el recorte al filtro:
#   -vf "crop=400:400:340:560,signalstats,..."
# (ajusta las coordenadas a donde cae la cara en tu encuadre 1080x1920)
ffmpeg -hide_banner -i prueba.mp4 \
  -vf "signalstats,metadata=print:key=lavfi.signalstats.UAVG:key=lavfi.signalstats.VAVG:key=lavfi.signalstats.SATAVG" \
  -frames:v 30 -f null - 2>&1 | grep -E 'UAVG|VAVG|SATAVG' | tail -6
```

**Los números objetivo, en la zona de la CARA:**

```
UAVG    entre 105 y 125   (piel = poco azul, o sea POR DEBAJO de 128)
VAVG    entre 135 y 160   (piel = mucho rojo, o sea POR ENCIMA de 128)
SATAVG  entre 15 y 40     (por encima de 45 ya esta tenida)

Senial de alarma inmediata: UAVG por encima de 128.
Eso significa que la cara tiene mas azul que gris = esta morada o azulada.
Tu material media UAVG = 165.
```

**7. Si los números no dan, mueve algo y repite.** Casi siempre la respuesta es aleja a la persona del
neón o acerca la luz neutra a la cara. No es un ajuste de cámara.

---

## 7. Toda la escena teñida: cuándo sí vale la pena

Para que el criterio quede completo: **hay veces en que teñir toda la escena es la decisión correcta.**

**Funciona cuando** el plano es de **ambiente** y no de gente hablando (botellas, la barra, un vaso,
luces, una mano); cuando la persona sale **de espaldas o en silueta**, sin cara reconocible; cuando el
plano es **muy corto** (menos de 1,5 s) dentro de un montaje rápido; o cuando es una **transición** o
el fondo de un texto (`40`).

**No funciona nunca** cuando alguien habla a cámara, cuando sale un plato de comida (la comida morada
da asco literal) o cuando quieres que se lea la etiqueta de un producto.

**La estrategia inteligente para tus reels:** planos de ambiente bien teñidos de morado (rápidos y muy
de bar) **alternados** con planos de cara con luz neutra. El neón te da la identidad visual sin
costarte la piel, y como cada corte cambia de tipo de plano, los saltos de saturación se leen como
estilo y no como error (`62`).

---

## 8. Si ya lo grabaste mal: qué se puede y qué no

Honestidad, porque tienes material así en el disco.

**Se puede, en CapCut o con ffmpeg:** bajar la saturación general (la cara queda menos violeta, pero
el bar entero se apaga); mover el tinte hacia el verde para compensar el magenta (funciona **poco** y
ensucia el resto); convertir el plano a **blanco y negro** —suena a rendición, pero en un montaje de
bar un plano en B&N bien puesto se ve intencional y resuelve el problema del todo—; o aislar la piel
con una máscara y corregirla aparte (costoso, y con material comprimido de celular el borde se ve).

**No se puede:** devolverle a la piel el rojo que nunca la iluminó (sección 4); corregir un canal
saturado, porque donde el rojo llegó al tope no hay textura; ni emparejar un plano de saturación 57
con uno de saturación 13.

**La decisión práctica:** el material morado que ya tienes, úsalo **corto y de ambiente**, no para las
frases importantes; y regraba esas frases con el movimiento 1. Regrabar 40 segundos cuesta menos que
pelear tres horas con un plano que no va a quedar bien.

---

## Errores comunes

1. **Usar el neón como luz de la cara.** Es el error raíz. El neón va **detrás**; la cara lleva luz
   neutra al frente.
2. **Dejar el balance de blancos en automático bajo luz de color.** El celular neutraliza el bar, pone
   la piel verde y encima cambia de tono a mitad de toma.
3. **Intentar quitar el morado con el deslizador de Kelvin.** El magenta vive en el otro eje. Estás
   moviendo la perilla equivocada.
4. **Grabar con la persona pegada a la pared del neón.** A 50 cm se baña en morado. A 3 m no le llega
   casi nada. Es caminar.
5. **Creer que se arregla en CapCut.** La luz roja que nunca existió no se puede inventar. Lo que no
   iluminó a la persona no se grabó.
6. **No meter ninguna luz neutra.** Basta con que exista, aunque sea tenue: una lámpara, una linterna
   con servilleta. Sin ella, la piel no tiene rojo que reflejar.
7. **Mezclar en el mismo video planos de saturación 57 y de saturación 13** sin decisión de montaje. El
   salto es de 4 veces y se lee como error.
8. **Iluminar la comida con luz de color.** Un plato bajo neón morado da asco literal. La comida
   siempre con luz cálida o neutra (`153`).
9. **Exponer normal bajo neón fuerte.** El rojo y el azul se saturan solos y la piel pierde textura sin
   que la imagen parezca quemada. Baja un poco más.
10. **No fijar el balance por sitio.** Cada rincón del bar tiene mezcla distinta. Se fija una vez por
    sitio y no se toca durante ese bloque.
11. **Olvidar los 3 segundos de papel blanco.** Es la referencia que hace que corregir después sea
    cuestión de un minuto en vez de una tarde (`228`).
12. **Renunciar al neón por miedo.** El neón es la identidad visual de tu bar y es un activo. No se
    quita: se relega al fondo, donde brilla sin hacer daño.

---

## Checklist

- [ ] El **neón está detrás** de la persona, no delante, y a **2 m o más**.
- [ ] Hay **luz neutra o cálida sobre la cara**, a 45° y cerca (1 m).
- [ ] El **balance de blancos está fijo a mano**, ajustado a la luz que le da a la **cara**.
- [ ] Si la app lo permite, ajusté también el **tinte** (verde/magenta), no solo los Kelvin.
- [ ] Ninguna luz **verde, magenta o azul profundo** toca la cara.
- [ ] Grabé **3 segundos de papel blanco** en el sitio donde va la cara.
- [ ] Miré la prueba en pantalla: **la piel es color piel** y el neón del fondo sigue morado.
- [ ] Medí con ffmpeg la **zona de la cara**: UAVG por debajo de 128, VAVG por encima de 128,
      SATAVG por debajo de 45.
- [ ] Bajé la exposición un poco extra por ser escena de neón fuerte (`222`).
- [ ] Los planos **teñidos a propósito** son de ambiente, cortos y sin caras hablando.
- [ ] La **comida y las etiquetas** de producto no están bajo luz de color.
- [ ] El balance y la posición **no cambian** dentro del mismo bloque.
