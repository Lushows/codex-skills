# 392 — El escalón de desenfoque

**Qué resuelve:** "ponle un poco de blur al fondo" no es una instrucción: es un deseo. Sigma 1 y sigma
4 son dos cosas distintas y ninguna de las dos es "un poco". Este módulo fija la unidad del eje de
desenfoque —**la acutancia**—, mide qué sigma hace falta para cruzar el escalón, y desmonta dos
creencias que salen falsas al medirlas.

Ojo con la frontera: el desenfoque **óptico**, el que da el diafragma en rodaje, es `221`. Aquí no hay
lente: hay un PNG plano al que se le fabrica la distancia.

---

## 1. La unidad: acutancia, no sigma

Sigma es lo que tú pones; la acutancia es lo que se ve. Son cosas distintas porque el mismo sigma sobre
un grabado lleno de líneas y sobre una foto blanda dan resultados que no se parecen.

**ACUT = gradiente medio de la luminancia, dentro del alfa opaco.**

```python
import numpy as np
from PIL import Image, ImageFilter

def acut(im):                                   # im: PIL RGBA ya escalada
    m   = np.asarray(im)[:, :, 3] > 200
    rgb = np.asarray(im.convert("RGB")).astype(np.float32)
    Y   = 0.2126*rgb[:,:,0] + 0.7152*rgb[:,:,1] + 0.0722*rgb[:,:,2]
    gy, gx = np.gradient(Y)
    return float(np.hypot(gx, gy)[m].mean())

def al_fondo(im, sigma):
    """Desenfoca RGB y alfa. El alfa a la MITAD de sigma: si la silueta queda dura
       y el interior blando, se lee como fallo de render, no como distancia."""
    rgb = im.convert("RGB").filter(ImageFilter.GaussianBlur(sigma))
    a   = im.split()[3].filter(ImageFilter.GaussianBlur(sigma*0.5))
    return Image.merge("RGBA", (*rgb.split(), a))
```

El número que se apunta en la tabla del plano no es el sigma: es **la caída de ACUT en porcentaje
respecto al plano frente**. Ése es el escalón.

---

## 2. La tabla medida

`retrato_lustig` (nativo 1106 × 1491), a cinco anchos, con seis sigmas. Cada celda es la caída de ACUT.

| Ancho | ACUT σ=0 | σ 0,8 | σ 1,2 | σ 1,8 | σ 2,4 | σ 3,2 | σ 4,5 |
|---|---|---|---|---|---|---|---|
| 280 | 7,16 | −27 % | −42 % | −54 % | −61 % | −66 % | −71 % |
| 420 | 6,20 | −28 % | −41 % | −54 % | −62 % | −67 % | −72 % |
| 620 | 5,43 | −27 % | −41 % | −55 % | −63 % | −69 % | −74 % |
| 900 | 4,54 | −21 % | −37 % | −52 % | −61 % | −67 % | −73 % |
| 1300 | 3,60 | −13 % | −28 % | −47 % | −58 % | −64 % | −71 % |

**El escalón de desenfoque útil está entre −30 % y −65 % de ACUT**, es decir, entre σ 1,0 y σ 2,8 en
este material. Por debajo de −30 % el ojo no lo separa; por encima de −75 % deja de leerse como
distancia y empieza a leerse como un render roto.

| Caída de ACUT | Cómo se lee |
|---|---|
| menos de −20 % | no hay escalón; el elemento sigue en el plano frente |
| **−30 % a −45 %** | **plano medio corto: detrás, pero todavía reconocible** |
| −50 % a −65 % | plano medio largo o fondo: forma y masa, no detalle |
| más de −75 % | mancha. Parece un error de render, no lejanía |

---

## 3. Primera creencia falsa: "el sigma tiene que escalar con el tamaño"

Suena razonable y es lo que todo el mundo asume. Medido: **no**.

| Ancho del elemento | σ para bajar ACUT un 50 % | σ / (ancho ÷ 1000) |
|---|---|---|
| 280 | 1,6 | 5,71 |
| 420 | 1,6 | 3,81 |
| 620 | 1,6 | 2,58 |
| 900 | 1,7 | 1,89 |
| 1300 | 1,9 | 1,46 |

El sigma necesario es **prácticamente constante (1,6 → 1,9) en un rango de tamaño de 4,6×**. Lo que
escala es el sigma *normalizado*, y no hace falta para nada.

**La razón, y su límite:** cada elemento se remuestrea desde el mismo original de alta resolución, así
que su escala de detalle se encoge en proporción al ancho. Si el elemento estuviera ya a su resolución
nativa —un fotograma de vídeo—, esto dejaría de cumplirse. La fila de 1300 px es **un aumento por
encima del nativo** (1106 px): de ahí que su ACUT de partida ya venga caída a 3,60.

> Regla operativa: **σ entre 1,2 y 2,8 para cualquier elemento de un collage de archivo**, sin
> proporcionalidad con el ancho. Si el material no es archivo remuestreado, vuelve a medir la tabla.

---

## 4. Segunda creencia falsa: "reducir de tamaño ya desenfoca"

Medido sobre el mismo elemento: reducir del 100 % al 65 % de ancho, **sin tocar nada más**, subió ACUT
un **+15,7 %**. Reducir **afila**.

| Operación | ΔACUT |
|---|---|
| 92 % de ancho, nada más | +2,9 % |
| 65 % de ancho, nada más | **+15,7 %** |
| 65 % de ancho + σ 1,2 | −33,8 % |
| 65 % de ancho + σ 2,4 | −58,2 % |

El remuestreo LANCZOS concentra el mismo detalle en menos píxeles y el gradiente por píxel crece. Es
decir: **el escalón de tamaño empuja el de desenfoque en dirección contraria, y hay que pagarlo aparte.**

De aquí sale la consecuencia de pipeline: **el orden importa**. Escalar y luego desenfocar es lo
correcto. Desenfocar y luego escalar deja el resultado sin control: el remuestreo devuelve parte del
filo que acabas de quitar.

```
CORRECTO   original -> scale(ancho del plano) -> gblur(sigma) -> sombra -> compositar
INCORRECTO original -> gblur(sigma) -> scale(ancho del plano)          <- el sigma se falsea
```

---

## 5. El alfa también se desenfoca, y a la mitad

Si desenfocas el RGB y dejas el alfa duro, obtienes una silueta con filo de tijera rellena de papilla.
`canales 22` ya avisa; el número es el aporte: **el alfa va a σ×0,5**. A σ×1,0 el contorno se come 2–3
px de figura por cada punto de sigma y el elemento adelgaza; a σ×0,0 aparece el filo duro.

Comprobación: la caída de ACUT medida **en una banda de 6 px alrededor del contorno** debe quedar entre
el 70 % y el 130 % de la caída medida en el interior. Fuera de ahí, borde y relleno están en planos
distintos.

---

## 6. En ffmpeg, cuando el elemento se reutiliza

Hornear el desenfoque en el PNG es más barato si el elemento sale una vez. Si el mismo recurso aparece
en dos planos distintos, se hace en el filtro y se paga por fotograma:

```bash
ffmpeg -i fondo.mp4 -loop 1 -i elem.png -filter_complex "\
[1:v]scale=403:-1,format=rgba,gblur=sigma=2.4:steps=3,\
     eq=saturation=0.83:brightness=-0.05[e];\
[0:v][e]overlay=x=160:y=H*0.34:shortest=1" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

`gblur` desenfoca **también el alfa** cuando el formato es `rgba`, y con un sigma único para los cuatro
canales. Es decir: en ffmpeg no tienes el σ×0,5 del alfa que sí tienes en PIL. Para un σ pequeño (≤1,5)
da igual; a partir de σ 2,4 el elemento adelgaza de forma visible. Si el escalón es largo, hornéalo con
PIL y mete el PNG ya cocinado.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Apuntar el sigma en vez de la caída de ACUT | El mismo sigma da escalones distintos según el material |
| Escalar el sigma con el ancho | Innecesario: 1,6 → 1,9 en un rango de tamaño de 4,6× |
| Desenfocar y después escalar | El remuestreo devuelve filo; el sigma anotado es mentira |
| Dejar el alfa nítido | Silueta dura con interior blando: se lee como fallo de render |
| Desenfocar el alfa al mismo sigma que el RGB | El elemento adelgaza y pierde silueta |
| Pasar de −75 % de ACUT | Mancha. Deja de leerse como distancia |
| Quedarse por debajo de −20 % | No hay escalón: el elemento sigue en el plano frente |
| Usar `gblur` con σ alto sobre RGBA en ffmpeg | Come alfa; para escalones largos, hornea con PIL |
| Aumentar un elemento por encima de su nativo | ACUT ya cae sin que lo pidas (1106 px a 1300 px) |

## Relacionado

`390` la profundidad es separación medida · `391` el escalón de tamaño ·
`393` el escalón de contraste y color · `395` profundidad sin desenfoque ·
`396` el plano que no separa · `221` profundidad de campo (óptica, en rodaje) ·
`66` viñeta, nitidez y textura · `263` integrar un elemento · `331` medir la separabilidad ·
`canales 22` profundidad por capas (cocinar el plano medio con PIL)
