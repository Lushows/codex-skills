# 391 — El escalón de tamaño

**Qué resuelve:** dos elementos del mismo cuadro tienen tamaños parecidos y el ojo no sabe cuál está
delante. La pregunta no es "¿lo hago más pequeño?" sino **cuánto más pequeño, medido contra qué**. Este
módulo fija la unidad, el escalón mínimo y el suelo por debajo del cual el elemento deja de existir.

La receta prescriptiva del canal documental —cuántos planos, qué anchos, qué derivas— está en
`canales 22` y no se repite. Aquí va la medida.

---

## 1. La unidad: % de la altura del lienzo, no % del otro elemento

El espectador no compara el retrato con la torre. Compara cada cosa **con el marco**, que es lo único
fijo en pantalla. Por eso el tamaño de un plano se anota siempre como **porcentaje de la altura del
lienzo**, y el escalón entre dos planos como la **razón entre esos dos porcentajes**.

```python
# alto aparente de un elemento, en % de la altura del lienzo
import numpy as np
from PIL import Image

def alto_pct(png, w_destino, H_lienzo):
    im = Image.open(png).convert("RGBA")
    im = im.resize((w_destino, round(im.height*w_destino/im.width)), Image.LANCZOS)
    ys = np.where(np.asarray(im)[:, :, 3] > 200)[0]      # el alfa, no el lienzo del PNG
    return 100.0 * (ys.max() - ys.min() + 1) / H_lienzo
```

**El bbox del alfa, nunca el tamaño del PNG.** Un recorte con 300 px de transparente arriba mide en
disco lo mismo que otro sin margen y ocupa en pantalla mucho menos. Medir el archivo en vez de la
silueta es el error que hace que dos elementos "del mismo tamaño" se vean de tamaños distintos.

---

## 2. El escalón mínimo, medido

`retrato_lustig` (nativo 1106 × 1491) sobre un lienzo de 1920 × 1080. El plano frente va a 620 px de
ancho. Cada fila es un candidato a plano medio:

| Ancho | % del frente | % ancho lienzo | % alto lienzo | Área alfa (% lienzo) | Cómo se lee |
|---|---|---|---|---|---|
| 620 | 100 | 32,3 | 77,4 | 24,5 | el plano frente, referencia |
| 570 | 92 | 29,7 | 71,1 | 20,7 | **dos elementos del mismo plano, uno mal escalado** |
| 496 | 80 | 25,8 | 61,9 | 15,7 | sigue sin separar: parece un descuido |
| 465 | 75 | 24,2 | 58,0 | 13,8 | **el mínimo que se lee como plano distinto** |
| 403 | 65 | 21,0 | 50,3 | 10,3 | escalón cómodo, el más usado |
| 341 | 55 | 17,8 | 42,6 | 7,4 | escalón largo, ya pide compañía en los otros ejes |
| 279 | 45 | 14,5 | 34,8 | 5,0 | **suelo**: por debajo pesa menos de 8 (`canales 21`) |

> **El escalón mínimo es 25 % de diferencia de altura** — es decir, el plano de atrás al **75 % o menos**
> del de delante. Por encima del 80 % no hay profundidad: hay un error de escala.

---

## 3. Por qué el 92 % no se ve como fondo: el eje se lee en área

La razón está en la aritmética y es la parte que casi nadie hace. El ojo estima distancia por **superficie
ocupada**, y la superficie va con el **cuadrado** del ancho.

| Razón de ancho | Razón de área | Pérdida de superficie |
|---|---|---|
| 0,92 | 0,846 | −15 % |
| 0,80 | 0,640 | −36 % |
| **0,75** | **0,563** | **−44 %** |
| 0,65 | 0,423 | −58 % |
| 0,55 | 0,303 | −70 % |
| 0,45 | 0,203 | −80 % |
| 0,30 | 0,090 | −91 % |

Un 92 % de ancho es un 85 % de área: una diferencia del orden del ruido de composición. Un 75 % de ancho
ya es **menos de la mitad** de superficie, y ahí el ojo sí lo lee como otra distancia.

La consecuencia práctica: **si alguien te pide "un poquito más pequeño", el número que tiene en la
cabeza es un 8 % y el que hace falta es un 25 %.**

---

## 4. El escalón de tamaño solo no basta

Medido sobre el mismo elemento (ver `390` §4): reducir del 100 % al 65 % dejó el contraste en **−0,2 %**
y la saturación en **−0,1 %**. Cero movimiento en dos de los cuatro ejes.

Y algo peor, que se explica en `392`: la acutancia **subió un 15,7 %**. Un elemento reducido está más
afilado por píxel que el mismo elemento a tamaño completo, porque el remuestreo comprime el detalle. Es
decir: **el escalón de tamaño empuja el de desenfoque en dirección contraria** y hay que compensarlo a
mano.

Por eso la tabla de trabajo de un plano medio nunca es solo un ancho:

```python
PLANOS = {                       # ancho relativo al frente · sigma · saturación · brillo
    "primerisimo": (1.25, 1.1, 1.02, 1.02),
    "frente":      (1.00, 0.0, 1.00, 1.00),
    "medio":       (0.65, 2.4, 0.83, 0.95),
    "fondo lejano":(0.45, 3.6, 0.76, 0.92),
}
```

---

## 5. El suelo: cuándo el elemento deja de existir

Por debajo de **34 % de la altura del lienzo** (el caso de 279 px de la tabla) el elemento pierde peso
visual: no aporta profundidad, aporta suciedad. Dos salidas, y solo dos:

1. **Subirlo de plano**, dándole el ancho del plano medio y pagando el escalón en los otros ejes.
2. **Quitarlo.** Un cuadro con un elemento de adorno diminuto se lee peor que el mismo cuadro sin él.

La comprobación es de dos segundos: si al **quitarlo** el cuadro no cambia, no estaba aportando
profundidad.

---

## 6. Un escalón por plano, no un escalón por elemento

Error de reparto muy común: cinco elementos con cinco anchos distintos —620, 540, 470, 410, 350—
creyendo que eso es profundidad. No lo es. Son cinco planos separados un 13 % cada uno, o sea, **ninguno
separado**. La profundidad se construye con **tres o cuatro cotas discretas**, y varios elementos pueden
compartir cota.

| Reparto | Lectura |
|---|---|
| 620 · 540 · 470 · 410 · 350 | una nube de tamaños; cuadro plano |
| 620 · 620 · 403 · 403 · 279 | tres planos claros, con población en cada uno |

Es la misma lógica que la de las pistas en `204`: pocas cotas, bien separadas, y cada elemento asignado
a una.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Medir el tamaño del PNG en vez del bbox del alfa | Dos elementos "iguales" se ven de tamaños distintos |
| Escalón por debajo del 20 % | Se lee como error de escala, no como profundidad |
| Pensar el escalón en ancho y no en área | Un 92 % de ancho es un 85 % de área: nada |
| Creer que reducir también desenfoca | Medido: reducir al 65 % **subió** ACUT un 15,7 % |
| Un ancho distinto por elemento | Nube de tamaños; ninguna cota separa |
| Bajar de un 34 % de la altura del lienzo | El elemento pesa menos de 8 y ensucia (`canales 21`) |
| Escalar hacia arriba por encima del nativo | 1106 px nativos a 1300 px: ACUT cae sin que lo pidas |
| Usar el escalón de tamaño como único eje | Pequeño y nítido = mal escalado, no lejos (`396`) |

## Relacionado

`390` la profundidad es separación medida · `392` el escalón de desenfoque ·
`395` profundidad sin desenfoque · `396` el plano que no separa · `398` profundidad en vertical ·
`204` composición en capas · `canales 21` peso visual y jerarquía ·
`canales 22` profundidad por capas (la receta del canal)
