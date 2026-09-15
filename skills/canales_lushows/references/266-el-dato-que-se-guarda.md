# 266 · El dato que se guarda

**Qué resuelve:** cómo se retiene un dato que ya se tiene, doce minutos, para gastarlo
en el remate. No es un truco de guion: es una decisión de producción que afecta al
recorte, al diccionario visual, al banco de imágenes y al título de los capítulos. Y
si no se escribe en algún sitio, **se fuga sola**.

Este módulo es el corazón del episodio 01, y termina con la auditoría del minuto 1 tal
como está hoy montado. El resultado de esa auditoría es que **el dato se está fugando
por tres sitios a la vez**.

---

## El caso

La casilla 10 del certificado de defunción dice, escrito a máquina:

> **10. Usual occupation:** *Apprentice Salesman & Counterfeiter*

En el minuto 1 la voz dice **sólo** «aprendiz de vendedor». La segunda palabra
—*Counterfeiter*, falsificador— se guarda para el minuto 12. `guion.md` lo deja
escrito: *«no es un truco: la casilla dice las dos cosas y las dos aparecen en
pantalla cuando toca. Lo que se administra es el orden».*

Y funciona porque el que lo escribió no fue el canal. El remate del episodio lo
mecanografió un funcionario federal en 1947: el Estado que lo tuvo encerrado hasta su
muerte le reconoció **falsificador**, la torre no aparece por ninguna parte, y le
llamó **aprendiz**.

## Las cuatro condiciones

Un dato sólo se puede guardar si cumple las cuatro. Con tres, no se guarda: se cuenta
cuando toque.

| Condición | Por qué | En este caso |
|---|---|---|
| **1. Está en la fuente que ya se ha enseñado** | Si sale de otro sitio, el remate parece sacado de la manga | Es la misma casilla del mismo papel que abre el episodio |
| **2. El episodio se sostiene sin él** | Un episodio que depende del último dato es un chiste con remate, no un documental | Los once minutos funcionan aunque el 12 no existiera |
| **3. Al revelarse, reordena lo anterior** | Si sólo añade, no es remate: es un dato más | Obliga a releer el gancho entero: no era una casilla, era un veredicto |
| **4. Se puede tapar sin mentir** | Callar una parte es legítimo; decir otra cosa no | La voz dice lo que pone, no dice todo lo que pone |

La prueba de la línea roja es la **4**, y se formula así: *al revelarlo, ¿el
espectador siente que se lo escondieron, o que no había mirado bien?* Si es lo
primero, se ha engañado y el dato no se guarda. Aquí es lo segundo: el papel estuvo en
pantalla desde el segundo 16.

## Lo que casi nadie hace: guardar es un acto de MONTAJE

Callarlo en la voz es la parte fácil y es la única que suele hacerse. El dato se fuga
por tres canales que no están en el guion:

| Canal de fuga | Qué lo provoca |
|---|---|
| **El recorte del documento** | El encuadre del papel incluye la parte que se quería guardar |
| **El diccionario visual** | Una palabra del guion tiene asignado un recurso que contiene el dato, y la capa automática lo coloca sola |
| **El banco de imágenes** | El tema se anticipa: media docena de piezas del asunto que aún no se ha nombrado |

## La auditoría del minuto 1 (hecha, con resultado)

### Fuga 1 · el recorte lo enseña entero

`recortar_lustig.py` define:

```python
("casilla_oficio", "victor_lustig_death_certificate_png", "revista",
 D(encuadre=(.038, .600, .535, .655), escala=1.75, ...)),
```

Sobre el PNG de 1532×1358 eso es la caja **(58, 814) → (819, 889)**, y dentro de esa
caja está **«Apprentice Salesman & Counter-»** y, en la línea de abajo —la del
renglón de la casilla 11, porque el funcionario partió la palabra— **«feiter»**. En
`guion_visual.py` el recurso entra anclado a `casilla` a **1180 px de ancho durante
4,2 s**. Es legible. **El dato guardado está en pantalla en el minuto 1.**

Arreglo comprobado sobre la imagen: un segundo recorte corto

```python
("casilla_oficio_corta", "victor_lustig_death_certificate_png", "revista",
 D(encuadre=(.038, .600, .415, .628), escala=1.75, ...)),   # 577x38 px de origen
```

que da exactamente `10. Usual occupation — Apprentice Salesman` y corta **también por
abajo**, que es lo que se olvida: sin el recorte vertical, «feiter» se cuela por el
renglón siguiente aunque se estreche a la derecha. El recorte largo se reserva para el
minuto 12.

*Variante defendible:* dejar el `&` asomando en el borde de papel (encuadre a `.425`).
Es honesto y planta la pregunta. Pero tiene que ser una **decisión**, no un descuido.

### Fuga 2 · el diccionario lo coloca solo

`vocabulario.py:32`:

```python
"aprendiz":     ("c_oficio",                         "heroe"),
```

y `c_oficio` es, en `texto_lustig.py:365`, la cita completa:

```python
cita("c_oficio", "Usual occupation: Apprentice Salesman &amp; Counterfeiter",
     "certificado de defunci&oacute;n &middot; casilla 10")
```

La palabra `aprendiz` suena a **20,60 s** y otra vez a **27,78 s**. Ejecutando
`guion_visual.py` el elemento aparece colocado en el bloque `oficio`. Es decir: la
capa automática pone en pantalla la cita entera —con la palabra guardada— en el
primer minuto, sin que nadie lo decidiera.

Arreglo: `c_oficio_corto` con el texto truncado para el acto I, y `c_oficio` (entera)
añadido a `NUNCA_AUTO`, reservado para colocarlo **a mano** en el minuto 12. Es
exactamente la razón por la que `NUNCA_AUTO` existe (`259`): recursos que llevan texto
propio y colgados de una palabra cualquiera contradicen a la voz. Aquí no la
contradicen: la adelantan, que es peor.

### Fuga 3 · el banco huele a falsificación desde el minuto 1

Colocados hoy en el primer minuto: `imprenta_sellos` (sobre «escribió», bloque
oficio), `aviso_falsos` (bloque nombre), `jefes_servicio_secreto` y
`grupo_servicio_secreto` (bloque nombre, a 5,50 s y 9,35 s del bloque). Cuatro piezas
del mundo de los billetes falsos antes de que el episodio haya nombrado el asunto.

Ninguna dice la palabra, y por eso esta fuga es de grado menor, pero el efecto se
acumula: cuando en el minuto 8 aparezca el Servicio Secreto, ya no será una revelación
—será un sitio donde el espectador ya ha estado. Arreglo: sacar esas cuatro del
vocabulario del acto I y reservarlas al tramo 08 (`257`, vocabulario por episodio).

## El archivo de lo guardado

Todo lo anterior pasa por una razón simple: **la decisión vivía en un párrafo de
`guion.md` y el que escribe el guion visual no la tiene delante.** Se arregla con tres
líneas en un archivo del episodio:

```
GUARDADO
  dato ........ la casilla 10 dice tambien "& Counterfeiter"
  se gasta en . minuto 12, sobre casilla_oficio (recorte largo)
  prohibido ... c_oficio entero, casilla_oficio largo, la palabra "falsificador"
                en voz, en rotulo y en titulo de capitulo, antes del minuto 8
```

Y se comprueba **antes de cada render** igual que se comprueba todo lo demás: que
ningún recurso de la lista prohibida aparezca en escenas anteriores a su minuto. Es
una comprobación de cuatro líneas y se hace sobre `ESCENAS`, no sobre el guion.

La verificación final es visual: **grilla de fotogramas** del minuto 1 (`160`) mirando
sólo si la palabra se lee. Un dato guardado no se verifica leyendo el guion —ahí está
guardado siempre—, se verifica **mirando el vídeo**.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Guardar el dato sólo en la voz | Se fuga por el recorte, el diccionario o el banco, y nadie se entera hasta que está montado |
| Recortar el documento sólo a lo ancho | La palabra partida aparece en el renglón de abajo |
| Dejar el recurso completo disponible para la capa automática | El motor lo coloca solo en la primera palabra que coincide |
| No escribir en ningún sitio qué está guardado | El que monta el minuto 8 no puede saberlo |
| Titular un capítulo con la palabra guardada | Se regala el remate a quien abre la lista antes de ver (`263`) |
| Guardar un dato que viene de otra fuente | El remate parece inventado justo donde el canal juega su credibilidad |
| Guardar algo que hace falso lo dicho antes | Eso ya no es administrar el orden: es engañar |
| Verificarlo leyendo el guion | El guion siempre pasa la prueba; el vídeo es el que falla |

## Relacionado

`267` el remate diferido · `260` el arco de doce minutos · `262` el bucle dentro del
bucle · `263` capítulos y bisagras · `257` vocabulario por episodio · `259` cuando el
diccionario no basta · `160` la grilla de fotogramas · `96` verificación de datos
