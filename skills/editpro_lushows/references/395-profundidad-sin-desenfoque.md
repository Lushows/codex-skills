# 395 — Profundidad sin desenfoque

**Qué resuelve:** el caso en el que el eje más potente está prohibido. Un documento que hay que poder
leer, un rótulo, una cifra, un plano de ciudad con nombres de calle: si lo desenfocas, cumple el
escalón y deja de servir para lo que está ahí. Este módulo reparte la distancia entre los ejes que
quedan, con la medida que lo hace posible.

`canales 22` ya dice que sin desenfoque el escalón de tamaño tiene que ser grande (35–55 %). Aquí va
por qué eso solo no basta y **cuál es el eje que lo sustituye de verdad**.

---

## 1. La medida que lo cambia todo

Bajar el contraste **baja la acutancia exactamente en el mismo porcentaje**. Medido sobre
`certificado_defuncion` (620 px, un grabado en blanco y negro):

| Tratamiento | Y | C | ΔC | ACUT | ΔACUT |
|---|---|---|---|---|---|
| base | 210,2 | 78,6 | — | 33,23 | — |
| contraste × 0,90 | 209,7 | 70,7 | **−10,1 %** | 29,89 | **−10,1 %** |
| contraste × 0,80 | 210,0 | 63,0 | **−19,9 %** | 26,65 | **−19,8 %** |
| contraste × 0,70 | 209,7 | 55,0 | **−30,1 %** | 23,24 | **−30,1 %** |
| contraste × 0,60 | 209,9 | 47,4 | **−39,7 %** | 20,03 | **−39,7 %** |

Y lo mismo sobre `bono_20000`: contraste ×0,70 da ΔC −29,9 % y ΔACUT −30,0 %.

No es casualidad: la acutancia es el módulo del gradiente de Y, y bajar el contraste es multiplicar Y
por un factor respecto a su media. El gradiente se multiplica por el mismo factor. **Un punto de
contraste es un punto de acutancia.**

> Y aquí está la diferencia que salva el documento: el desenfoque destruye **la posición** del borde;
> el contraste solo baja **su amplitud**. Las letras siguen donde estaban, con el mismo filo, más
> apagadas. Se leen. El número del eje de desenfoque baja igual.

---

## 2. El reparto cuando σ = 0

| Eje | Con desenfoque | **Sin desenfoque** |
|---|---|---|
| Tamaño | 25 % mínimo | **35 – 55 %** (`canales 22`) |
| Desenfoque | −30 a −65 % de ACUT | 0 % directo… |
| Contraste | −8 a −18 % | **−20 a −32 %** — y arrastra la acutancia con él |
| Saturación | −10 a −20 % | −15 a −25 %, si el material tiene saturación |
| Sombra | contacto 3–5 | contacto **2–4**: más corta, porque la lejanía se apoya en menos ejes |

El truco del reparto es que la casilla del desenfoque **no se queda vacía**: se llena desde el
contraste. Con contraste ×0,72 tienes −28 % de ACUT sin haber tocado un solo píxel de nitidez.

---

## 3. El velo atmosférico: el otro eje disponible

Un grabado en blanco y negro tiene **S = 0,0**. El eje de saturación no se puede bajar: ya está en el
suelo. Lo único que se puede hacer con él es **subirlo hacia el color del fondo**, que es justo como
funciona la perspectiva atmosférica de verdad.

| Tratamiento sobre `certificado_defuncion` | Y | C | ΔC | S | ΔACUT |
|---|---|---|---|---|---|
| velo gris 128 al 12 % | 199,8 | 69,1 | −12,1 % | **0,0** | −12,2 % |
| velo gris 128 al 22 % | 191,9 | 61,4 | −21,9 % | **0,0** | −21,8 % |
| **velo del fondo (ocre 120,104,74) al 22 %** | 186,6 | 61,3 | −22,0 % | **7,4** | −22,0 % |

Sobre `bono_20000`, que ya venía con S = 7,1, el mismo velo ocre la sube a **18,7**.

```python
from PIL import Image
def velo(im_rgb, color_fondo, fuerza):
    """Mezcla el elemento hacia el color del fondo. fuerza 0,12-0,26."""
    return Image.blend(im_rgb, Image.new("RGB", im_rgb.size, color_fondo), fuerza)
```

El velo hace tres cosas de una vez: baja el contraste, baja la acutancia en el mismo porcentaje y
**mete el elemento dentro de la paleta de la escena**. Es el movimiento de mayor rendimiento cuando el
desenfoque está prohibido.

**Regla de color:** el velo se toma del fondo que ese elemento tiene detrás, no de un gris genérico ni
de un azul de perspectiva. Un gris al 22 % apaga; el ocre del fondo al 22 % apaga **y** empata (`263`,
`canales 23`).

**Regla de fuerza:** por encima del 30 % el documento empieza a no leerse. El límite es el mismo de
siempre y se comprueba igual: ¿se lee la fecha?

---

## 4. Cuándo el desenfoque está prohibido de verdad

No todo lo que parece ilegible lo es. La lista corta:

| Material | ¿Desenfoque? |
|---|---|
| Documento cuya **cifra o fecha** hay que poder leer | **No.** Contraste + velo + tamaño |
| Documento que solo aporta **textura de papel** | Sí, y generoso. Nadie va a leerlo |
| Rótulo o cifra en pantalla | **No, nunca** (`379`, `373`) |
| Subtítulo | **No.** El texto no va al fondo, va detrás del sujeto (`377`, `262`) |
| Mapa con nombres que se citan en la voz | No mientras se citan; sí después |
| Retrato de alguien que se nombra | Sí, si no es el sujeto de la frase |

**La trampa** es el documento del que se lee un trozo en pantalla durante dos segundos y después se
queda seis más. Ahí el reparto cambia en el tiempo: entra nítido con su contraste, y cuando la voz pasa
a otra cosa, se le aplica el velo y baja de plano. Es una animación de dos fotogramas clave y resuelve
el conflicto entero.

---

## 5. El límite honesto

Sin el eje de desenfoque, el número máximo de ejes cruzados es tres, y uno de ellos (contraste) arrastra
al otro (acutancia), así que en el fondo son **dos decisiones independientes: tamaño y velo**. Eso
alcanza para dos planos claramente separados; **no alcanza para cuatro**.

Si una escena necesita cuatro profundidades y todo el material tiene que ser legible, el problema no es
de composición: es de guion visual. Hay demasiadas cosas en el cuadro que se tienen que leer a la vez, y
la solución es repartirlas en el tiempo, no en el eje z.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Desenfocar un documento del que se lee la cifra | Cumple el escalón y deja de servir para lo que está ahí |
| Dejar la casilla del desenfoque vacía | Se pierde el eje: el contraste podía llenarla gratis |
| Bajar el contraste y además desenfocar "por si acaso" | Los dos restan acutancia: se va al doble del escalón |
| Usar un velo gris genérico | Apaga pero no empata; el elemento sigue siendo de otro sitio |
| Velo por encima del 30 % | El documento deja de leerse; era lo único que había que proteger |
| Intentar bajar la saturación de un grabado B/N | S = 0,0. Ese eje solo puede subir, hacia el color del fondo |
| Mantener el mismo tratamiento los ocho segundos | Entra nítido, se vela cuando la voz pasa a otra cosa |
| Pedir cuatro planos con todo legible | No es un problema de composición: es de guion visual |
| Mandar un subtítulo al fondo | El texto no baja de plano: se mete detrás del sujeto (`377`) |

## Relacionado

`390` la profundidad es separación medida · `391` el escalón de tamaño ·
`392` el escalón de desenfoque · `393` el escalón de contraste y color ·
`394` la sombra que asienta · `396` el plano que no separa ·
`262` la técnica del sándwich · `263` integrar un elemento · `377` texto detrás del sujeto ·
`379` números y cifras en pantalla · `canales 22` profundidad por capas (el escalón sin desenfoque)
