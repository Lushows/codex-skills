# 393 — El escalón de contraste y color

**Qué resuelve:** los dos ejes que nadie toca. Casi todo el mundo manda algo al fondo con tamaño y
desenfoque, deja el contraste y la saturación clavados, y luego no entiende por qué el cuadro sigue
plano. Aquí van las dos unidades, los dos escalones y —lo más rentable del módulo— **la demostración
medida de que la luz y la saturación son dos palancas distintas y no se sustituyen.**

---

## 1. Dos unidades que se parecen y no son lo mismo

| Símbolo | Qué es | De dónde sale |
|---|---|---|
| **C** | desviación típica de Y dentro del alfa | `numpy`, o `signalstats` sobre un `crop` |
| **YMAX** | el techo de luz del cuadro (P99,5 de Y) | `lavfi.signalstats.YMAX` |
| **S (HSV)** | media de `(max−min)/max × 100` sobre RGB | `numpy` |
| **SATAVG** | media de la distancia croma a (128,128) en YUV | `lavfi.signalstats.SATAVG` |

> ⚠️ **S y SATAVG no son la misma escala.** El mismo fondo `f_metodo` da **SATAVG 8,79** con
> `signalstats` a 4320 × 2430 y **S = 28,7** con la fórmula HSV a 960 × 540. Ninguno de los dos está
> mal: miden cosas distintas. Elige uno, anótalo en la cabecera de la tabla, y no mezcles.

---

## 2. La luz y la saturación son dos palancas, no una

Experimento sobre `ep01-lustig/render/f_metodo.png`, un único fondo, una palanca cada vez:

| Variante | YAVG | C | YMAX | S (HSV) |
|---|---|---|---|---|
| original | 59,4 | 27,7 | 132 | 28,7 |
| luz × 1,3 | 76,7 | 36,0 | 171 | **28,9** |
| luz × 1,8 | 106,4 | 49,9 | **237** | **28,8** |
| luz × 2,6 | 149,4 | 63,7 | 255 | 27,3 |
| saturación × 1,5 | 59,6 | 27,8 | **132** | 40,1 |
| saturación × 2,2 | 60,2 | 28,1 | **133** | **54,0** |
| saturación × 3,0 | 61,5 | 28,3 | 135 | 66,8 |
| contraste × 1,4 | 59,6 | 38,8 | 160 | 45,2 |
| saturación × 2,2 + luz × 1,3 | 77,8 | 36,5 | 173 | 54,3 |

Léelo dos veces:

- **Subir la luz ×1,8 mueve YMAX de 132 a 237 y deja la saturación en 28,8.** Cero. El fondo queda
  más claro y exactamente igual de apagado.
- **Subir la saturación ×2,2 mueve S de 28,7 a 54,0 y deja YMAX en 133.** También cero. El fondo tiene
  color y sigue oscuro.
- **El contraste mueve los dos a la vez** (YMAX 160, S 45,2) porque separa los canales del punto medio.
  Es la palanca sucia: útil, pero no sirve para diagnosticar.

Éste es el aprendizaje operativo del piloto, y está escrito en la cabecera de `ep01-lustig/fondos.py`:
*"Tono base SATURADO: es la palanca que quita el marrón, no la luz"*. Un fondo que sale marrón y
apagado **no se arregla con luz**. Se arregla saturando el tono base y añadiendo una contraluz
complementaria a media fuerza.

---

## 3. Los cinco fondos del piloto, medidos hoy

`ep01-lustig/render/*.png`, 4320 × 2430, `ffprobe … signalstats`:

| Fondo | YMIN | YLOW | YAVG | YHIGH | YMAX | SATAVG | SATMAX |
|---|---|---|---|---|---|---|---|
| `f_muerte` | 12 | 27 | 67,4 | 115 | 160 | 17,3 | 28 |
| `f_oficio` | 12 | 34 | 76,5 | 123 | **177** | **20,1** | 31 |
| `f_nombre` | 13 | 30 | 52,8 | 90 | 157 | 18,5 | 29 |
| `f_torre` | 7 | 28 | 68,5 | 116 | 168 | **22,4** | 44 |
| `f_metodo` | 15 | 25 | 58,3 | 100 | 145 | **8,8** | **91** |

- Los cinco están **muy por encima** del estado plano que motivó el arreglo (YMAX 51–87, SATAVG 2,3–7,1).
- `f_metodo` es el caso interesante: SATAVG 8,8 —el más bajo de los cinco— con SATMAX 91, el más alto.
  Es el fondo de tinta con la línea roja: casi todo neutro y **un acento muy saturado en poca
  superficie**. La media dice "apagado" y el cuadro no lo está. Es el error del promedio de `332`,
  aplicado al color.

> **Honestidad con el dato:** el rango que se me dio como verificado para los fondos ya arreglados era
> YMAX 138–249 y SATAVG 12–15,9. Lo que hay hoy en disco es **YMAX 145–177 y SATAVG 8,8–22,4**. El
> sentido coincide (lejos del estado plano) pero los extremos no. O se midió sobre otra tanda de
> fondos, o los cinco actuales se retocaron después. Antes de citar esos números en cualquier sitio,
> vuelve a correr `signalstats` sobre `render/*.png`.

---

## 4. El escalón, en números

Ahora la parte de profundidad. Cuánto tienen que bajar C y S para que un plano se lea detrás.

| Caída de C | Caída de S | Cómo se lee |
|---|---|---|
| 0 a −5 % | 0 a −6 % | **no hay escalón**: mismo plano |
| **−8 % a −18 %** | **−10 % a −20 %** | **plano medio. El escalón de trabajo** |
| −20 % a −35 % | −22 % a −45 % | fondo lejano; ya solo se lee la masa |
| más de −35 % | más de −45 % | gris sucio: no parece lejos, parece estropeado |

Medido con la receta del canal (`canales 22`: σ 2,4 · sat 0,83 · brillo 0,95) sobre `retrato_lustig`:
**ΔC = −13,7 % y ΔS = −14,8 %**. Cae justo en el centro de la franja de trabajo, que es exactamente por
qué esa receta funciona.

Y el contraejemplo que da nombre a todo el bloque: el mismo elemento **al 92 % de tamaño y sin tocar
color** da **ΔC = +0,2 % y ΔS = 0,0 %**. Dos ejes de cuatro, muertos.

---

## 5. Cómo se aplica sin romper la marca

`ImageEnhance.Color` y `eq=saturation=` multiplican la saturación de forma uniforme: **respetan la
paleta**, solo la alejan. Es lo que quieres para profundidad.

Lo que **no** debes usar para mandar algo al fondo:

- **Desaturar a gris (sat 0,0)**. Deja de pertenecer a la escena: se lee como material de otro sitio.
- **Bajar la opacidad.** No es distancia, es transparencia. En un collage rompe el lenguaje: se ve la
  textura del fondo a través del cuerpo (`canales 22` lo tiene prohibido, y con razón).
- **Meter azul "porque lo lejano es azul".** Eso es perspectiva atmosférica de exteriores reales. En un
  collage de archivo sepia introduce una dominante ajena que hay que corregir luego (`263`).

```python
from PIL import ImageEnhance
def color_de_plano(im, sat, brillo):        # im: RGB ya desenfocado
    im = ImageEnhance.Color(im).enhance(sat)        # 0,83 plano medio · 0,76 fondo lejano
    return ImageEnhance.Brightness(im).enhance(brillo)   # 0,95 · 0,92
```

El equivalente en ffmpeg, con la nota de signo: en `eq`, `saturation` es un **factor** (1,0 = neutro) y
`brightness` es un **desplazamiento** de −1 a 1 (0 = neutro). `eq=saturation=0.83:brightness=-0.05` no
es "0,83 y 0,95": son dos escalas distintas y confundirlas es un clásico.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Mezclar S (HSV) y SATAVG (YUV) en la misma tabla | Los números no son comparables: 8,8 y 28,7 son el mismo fondo |
| Subir la luz para quitar el marrón | Medido: luz ×1,8 sube YMAX 105 puntos y deja S en +0,1 |
| Subir la saturación esperando que ilumine | Medido: sat ×2,2 sube S 25 puntos y deja YMAX en +1 |
| Diagnosticar con el mando de contraste | Mueve los dos ejes a la vez; no dice cuál fallaba |
| Fiarse de SATAVG como resumen del cuadro | `f_metodo`: media 8,8 con un acento de 91 en poca superficie |
| Desaturar a gris para "alejar" | El elemento deja de pertenecer a la escena |
| Bajar la opacidad para alejar | Transparencia, no distancia. Se ve el fondo a través del cuerpo |
| Añadir azul por perspectiva atmosférica | En collage sepia introduce una dominante que luego hay que corregir |
| Leer `brightness` de `eq` como factor | Es un desplazamiento de −1 a 1; 0,95 ahí es casi blanco |

## Relacionado

`390` la profundidad es separación medida · `391` el escalón de tamaño ·
`392` el escalón de desenfoque · `396` el plano que no separa · `399` comprobarlo sobre gris ·
`263` integrar un elemento · `331` medir la separabilidad · `332` mirar y medir ·
`60` fundamentos de color · `canales 22` profundidad por capas · `canales 163` contraste elemento-fondo
