# 21 · Peso visual y jerarquía

**Qué resuelve:** hay cuatro cosas en pantalla y el ojo no sabe cuál mirar. O peor:
mira la que no sostiene la frase. El peso visual se puede calcular antes de renderizar
y ordenar a propósito, en vez de descubrirlo viendo el video.

---

## Qué hace que un elemento se vea primero

En orden de fuerza real, medido sobre este canal:

| Factor | Peso | Por qué |
|---|---|---|
| **Cara humana** | ×1,6 | El ojo la busca antes que nada. Un retrato pequeño gana a un objeto grande |
| **Cifra grande** | ×1,3 | Un número aislado se lee como pregunta pendiente |
| **Tamaño** | √área | La percepción sigue la dimensión lineal, no el área. Duplicar el ancho no duplica el peso: lo multiplica por ~1,4 |
| **Contraste con el fondo** | ×0,35 a ×1,0 | Un recorte claro sobre fondo tinta pesa casi el triple que uno del mismo tono |
| **Posición** | ×0,74 a ×1,0 | El centro manda; la esquina inferior derecha es la última que se mira |
| **Movimiento** | +25% mientras dura la entrada | Por eso una entrada de 0,36 s roba el foco aunque el elemento sea pequeño |

El color **no** entra en la fórmula salvo el rojo `#E3120B`: sobre la paleta del canal
funciona como una cara — gana siempre. Reservado para lo que debe ganar.

## La fórmula

```
peso = 100 · √(A) · (0,35 + 0,65·C) · P · R

A = (w·h) / (1920·1080)                área relativa que ocupa
C = min(1 ; |L_elemento − L_fondo| / 55)   contraste de luminancia (L: 0-100)
P = factor de posición (tabla)
R = 1,6 si hay cara · 1,3 si es cifra grande · 1,0 el resto
```

**Factor de posición** (la retícula de `20`):

| P5 | P2 | P4 | P6 | P1 | P8 | P3 | P7 | P9 |
|---|---|---|---|---|---|---|---|---|
| 1,00 | 0,94 | 0,92 | 0,90 | 0,88 | 0,86 | 0,82 | 0,78 | 0,74 |

Se lee de izquierda a derecha y de arriba abajo, pero el centro pesa más que la
esquina que se lee primero. La P9 va última **y además** es donde YouTube pone sus
tarjetas finales (`28`).

## Calcularlo

```python
import math, os
from PIL import Image, ImageStat

POS = {"P5":1.00,"P2":0.94,"P4":0.92,"P6":0.90,"P1":0.88,
       "P8":0.86,"P3":0.82,"P7":0.78,"P9":0.74}

def lum(png):
    """L media (0-100) de los pixeles OPACOS del PNG."""
    im = Image.open(png).convert("RGBA")
    m = im.split()[3].point(lambda v: 255 if v > 128 else 0)
    if m.getextrema()[1] == 0:
        raise ValueError(f"{png}: alfa vacio, el recorte no tiene pixeles")
    r, g, b = ImageStat.Stat(im.convert("RGB"), m).mean
    return (0.2126*r + 0.7152*g + 0.0722*b) / 255 * 100

def peso(png, ancho, pos, l_fondo, cara=False, cifra=False):
    im = Image.open(png)
    alto = ancho * im.height / im.width
    A = (ancho * alto) / (1920 * 1080)
    C = min(1.0, abs(lum(png) - l_fondo) / 55)
    R = 1.6 if cara else (1.3 if cifra else 1.0)
    return 100 * math.sqrt(A) * (0.35 + 0.65*C) * POS[pos] * R

# fondo tinta tipico del canal: L ~ 20
print(round(peso("recortes/chapo_us.png", 620, "P4", 20, cara=True), 1))
```

## Los umbrales del canal

| Medida | Valor | Si no |
|---|---|---|
| Peso del dominante | **≥ 1,8 ×** el segundo | Empatan y el ojo salta entre los dos |
| Peso de un elemento | 8 a 35 | Por debajo de 8 no se llega a ver; por encima de 35 no deja sitio a nada |
| Suma de los vivos a la vez | **35 a 75** | Más de 90 es saturación: se lee como ruido |
| Elementos vivos | 2 a 4 (`12`) | — |

**La regla que lo amarra todo:** el elemento con más peso tiene que ser el que
sostiene la frase que se está oyendo. Si la voz dice la cifra y el que pesa más es el
retrato, el montaje está contando otra cosa que el guion.

## Cómo se sube o se baja el peso sin romper nada

| Quiero | Qué toco | Qué NO toco |
|---|---|---|
| Que pese más | `w` (+30%), moverlo a P5/P2, más contraste con el fondo | La opacidad: siempre 1 |
| Que pese menos | `w` (−25%), llevarlo a plano medio (`22`), moverlo a P7/P9 | La opacidad: siempre 1 |
| Que gane el foco un instante | Darle una entrada con gesto (`izq`/`der`) | Dejarlo más tiempo: eso no lo hace ganar, lo hace pesado |
| Devolver el foco al principal | Sacar el que compite, no agrandar el principal | — |

Bajar la opacidad para "quitarle importancia" es el error clásico: un recorte de papel
al 70% se lee como doble exposición, no como algo que importa menos.

## El caso de las dos caras

Dos retratos vivos a la vez se pelean siempre (ambos llevan ×1,6). Solución: uno va en
plano medio, con `w` al 60% y el tratamiento de `22`, o uno de los dos entra 0,5 s
después y el primero ya está saliendo (`14` encadenar elementos).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dos elementos con peso parecido a la vez | El ojo salta y no lee ninguno |
| Bajar opacidad para restar peso | Doble exposición; se rompe el lenguaje de collage |
| Cifra grande y retrato al mismo tiempo | ×1,3 contra ×1,6: gana la cara y la cifra se pierde |
| Rojo `#E3120B` en un elemento secundario | Se lleva el foco de lo que sostiene la frase |
| Medir el contraste contra el fondo global | El fondo tiene viñeta: hay que medir la zona donde cae el elemento |
| El que más dura no es el que más pesa | Contradicción entre jerarquía de tiempo y de imagen |

## Relacionado

`20` retícula del collage · `22` profundidad por capas · `12` capas simultáneas ·
`26` superposición y oclusión · `44` la cifra en pantalla
