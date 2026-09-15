# 394 — La sombra que asienta

**Qué resuelve:** el quinto eje, el que no es una propiedad del elemento sino de la relación entre el
elemento y lo que tiene debajo. Una sombra mal puesta **contradice** los otros cuatro ejes: el
desenfoque dice "lejos" y la sombra dice "pegado aquí delante", y el cuadro se lee raro sin que nadie
sepa señalar por qué. Aquí va la unidad para medirla y la tabla de valores.

`204` ya da el rango estético (4–10 px de desplazamiento, 12–25 de desenfoque, 20–35 % de opacidad) y
`263` la llama *sombra de contacto*. Este módulo aporta el número que falta: **cuánto oscurece de
verdad, y cuál de los tres parámetros lo controla.**

---

## 1. La unidad: contacto = cuánto se oscurece el anillo

No se mide la sombra. Se mide **el suelo alrededor del elemento, antes y después**.

- **Anillo cerca:** de 2 a 18 px por fuera de la silueta.
- **Anillo lejos:** de 40 a 70 px por fuera, que actúa de referencia limpia.
- **Contacto = Y(anillo cerca, sin sombra) − Y(anillo cerca, con sombra)**, en niveles de luminancia.

```python
import numpy as np
from PIL import Image, ImageFilter

def dil(m, r):
    im = Image.fromarray((m*255).astype(np.uint8))
    return np.asarray(im.filter(ImageFilter.MaxFilter(2*r+1))) > 127

def contacto(Y_sin, Y_con, alfa):
    dentro = alfa > 200
    cerca  = dil(dentro, 18) & ~dil(dentro, 2)
    return float(Y_sin[cerca].mean() - Y_con[cerca].mean())

def sombra(el, dx, dy, blur, op):
    """Devuelve la capa de sombra y su desplazamiento. El alfa desenfocado es la sombra."""
    a = el.split()[3].filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(v*op))
    s = Image.new("RGBA", el.size, (0, 0, 0, 0)); s.putalpha(a)
    return s, (dx, dy)
```

El anillo **empieza en 2 px, no en 0**: el primer píxel del contorno es alfa parcial y arrastra color
del propio elemento (`canales 161`).

---

## 2. La tabla medida

`retrato_lustig` a 620 px sobre un fondo liso de Y = 87,0, ocho combinaciones. Cada fila es una sombra
distinta; la última columna es el número que importa.

| Desplazamiento (dx, dy) | Desenfoque | Opacidad | Y anillo cerca | Contacto |
|---|---|---|---|---|
| — (sin sombra) | — | — | 87,0 | 0,0 |
| 0, 0 | 10 | 0,35 | 84,2 | **2,8** |
| 4, 6 | 6 | 0,35 | 82,4 | 4,6 |
| **7, 11** | **10** | **0,35** | 79,4 | **7,5** |
| 14, 20 | 18 | 0,35 | 74,5 | 12,5 |
| 7, 11 | 10 | 0,18 | 82,4 | 4,6 |
| 7, 11 | 10 | 0,55 | 76,0 | 11,0 |
| 7, 11 | 3 | 0,35 | 79,6 | 7,4 |
| 7, 11 | 28 | 0,35 | 79,0 | 7,9 |

---

## 3. La sorpresa: el desenfoque **no** controla el contacto

Mira las tres últimas filas. Con el mismo desplazamiento y la misma opacidad:

| Desenfoque | Contacto |
|---|---|
| 3 | 7,4 |
| 10 | 7,5 |
| 28 | 7,9 |

**Un factor 9 de desenfoque mueve el contacto un 7 %.** La sombra se reparte por más superficie, pero la
cantidad total de oscurecimiento apenas cambia, y el anillo de 18 px la integra casi entera.

Lo que sí controla el contacto:

| Palanca | De … a … | Contacto |
|---|---|---|
| **Desplazamiento** | (0,0) → (4,6) → (7,11) → (14,20) | 2,8 → 4,6 → 7,5 → **12,5** |
| **Opacidad** | 0,18 → 0,35 → 0,55 | 4,6 → 7,5 → **11,0** |

Las dos son casi lineales. La conclusión práctica:

> **El desplazamiento y la opacidad dicen a qué distancia está el elemento. El desenfoque dice cómo es
> la luz.** Si tocas el desenfoque esperando "asentarlo más", no estás asentando nada: estás cambiando
> de lámpara.

---

## 4. La sombra tiene que estar de acuerdo con los otros ejes

Aquí está el fallo caro. `canales 22` avisa de que un recorte tratado en modo revista trae la sombra del
plano frente (7/11, desenfoque 10) y que al mandarlo al plano medio hay que **regenerarla**. El número
es el que lo hace accionable:

| Plano | Escalón de tamaño | Caída de ACUT | Sombra | Contacto objetivo |
|---|---|---|---|---|
| Primerísimo | 115–140 % | −30 a −45 % | 14,20 · blur 18 · 0,35 | **11 – 14** |
| Frente | 100 % | 0 % | 7,11 · blur 10 · 0,35 | **6 – 9** |
| Medio | 55–75 % | −50 a −65 % | 4,6 · blur 6 · 0,30 | **3 – 5** |
| Fondo lejano | 40–50 % | −65 a −75 % | sin sombra | **0 – 2** |

Un elemento en el plano medio con contacto 7,5 está diciendo dos cosas a la vez. En pantalla eso se
percibe como un recorte que "flota mal", y la reacción instintiva —subirle el desenfoque— no lo
arregla, porque el desenfoque no es lo que estaba mal.

**Regla corta:** el contacto escala con el tamaño del plano, no con las ganas. Si el elemento baja al
65 %, su contacto baja a la mitad.

---

## 5. El suelo y el techo

- **Contacto por debajo de 2:** no existe. El elemento está pegado con cinta encima del fondo. Es el
  aspecto de calcomanía de `204`.
- **Contacto por encima de 16:** se ve la sombra conscientemente. Ahí ya no asienta: decora. La regla
  de `204` sigue siendo la buena —si la ves, está al doble— y ahora tienes el número que la respalda.

El contacto se mide en niveles absolutos de Y, así que sobre un fondo de Y = 200 los mismos 7,5 puntos
son un 3,8 % de caída, contra el 8,6 % que eran sobre Y = 87. **Sobre fondo claro sube la opacidad;
nunca el desplazamiento**, que es el que delata la altura y debe seguir contando la verdad del plano.

Y una distinción que ahorra discusiones: un elemento que flota sin apoyarse en nada no lleva sombra de
contacto sino **proyectada**. La de contacto vive pegada a la silueta y el anillo de 18 px la recoge
entera; la proyectada vive a distancia y el anillo casi no la ve. Si mides contacto 1,2 en algo con una
sombra grande y evidente, el medidor no está roto: esa sombra no hace contacto. Elige una y quita la
otra.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Subir el desenfoque para "asentar más" | Medido: de blur 3 a blur 28 el contacto sube un 7 % |
| Heredar la sombra del plano frente en el plano medio | Desenfoque dice lejos, sombra dice cerca |
| Contacto por debajo de 2 | Calcomanía pegada encima del fondo |
| Contacto por encima de 16 | Se ve la sombra conscientemente: decora en vez de asentar |
| Medir el anillo desde 0 px | El contorno de alfa parcial mete color del elemento |
| Usar los mismos valores sobre fondo claro y oscuro | El contacto es absoluto; sobre Y=200 se ve la mitad |
| Subir el desplazamiento sobre fondo claro | Delata una altura que el plano no tiene; sube la opacidad |
| Poner sombra a los subtítulos | Tu estilo es contorno sin sombra y es el correcto (`204`) |
| Confundir sombra de contacto y sombra proyectada | Dos cosas distintas; juntas se anulan |

## Relacionado

`390` la profundidad es separación medida · `392` el escalón de desenfoque ·
`395` profundidad sin desenfoque · `396` el plano que no separa ·
`204` composición en capas · `263` integrar un elemento (sombra de contacto) ·
`canales 22` profundidad por capas (regenerar la sombra, no heredarla) ·
`canales 161` auditar sobre gris (el borde de alfa parcial)
