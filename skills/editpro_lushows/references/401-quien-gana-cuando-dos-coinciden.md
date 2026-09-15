# 401 — Quién gana cuando dos coinciden

**Qué resuelve:** «el de arriba tapa al de abajo» es verdad solo cuando el de arriba es opaco. En cuanto
hay alfa, fundidos u opacidad, **no gana nadie: se mezclan**, y el resultado es un color que no es el de
ninguno de los dos. Este módulo mide exactamente qué sale, para poder predecirlo sin renderizar.

`105` explica la sintaxis de `overlay`. Aquí está lo que devuelve, píxel a píxel.

---

## 1. El banco de pruebas

Tres imágenes planas, un fotograma, y se lee el píxel del centro. Todo lo que sigue sale de este arnés:

```python
def render(fc, sal, ent):
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error"]
    for e in ent: cmd += ["-loop","1","-framerate","25","-t","1.2","-i", e]
    cmd += ["-filter_complex", fc, "-map","[out]", "-frames:v","1", "-y", sal]
    return subprocess.run(cmd, capture_output=True, text=True).returncode

def pix(f, x, y):
    return Image.open(f).convert("RGB").getpixel((x, y))
```

Fondo `(18,22,40)`, capa **A** roja `(230,70,60)`, capa **B** verde `(60,190,120)`, las dos opacas y en el
mismo rectángulo.

---

## 2. Dos capas opacas: gana la última declarada

```
[0:v]format=rgba[bg];[1:v]format=rgba[a];[2:v]format=rgba[b];
[bg][a]overlay=250:75[v1];[v1][b]overlay=250:75[v2];[v2]format=rgb24[out]
```

| Orden de declaración | píxel medido | quién se ve |
|---|---|---|
| fondo · A · **B** | `(60, 189, 118)` | **B** |
| fondo · B · **A** | `(229, 68, 59)` | **A** |

Sin ambigüedad y sin aviso: el que pierde desaparece entero y el render sale con código 0. Un elemento
100% enterrado es el defecto que mejor se esconde (`386`).

**El orden de las dos entradas de cada `overlay` también manda:** la primera es el fondo (*main*), la
segunda es la capa. Invertirlas no «pone el logo debajo», pone el vídeo encima del logo y además recorta
el lienzo al tamaño del logo (`405`).

---

## 3. Con opacidad no gana nadie: se mezclan

Misma pila, bajando la opacidad de B con `colorchannelmixer=aa`:

| `aa` | medido | esperado `aa·B + (1−aa)·A` |
|---|---|---|
| 1,00 | `(60, 189, 118)` | `(60, 190, 120)` |
| 0,75 | `(100, 159, 103)` | `(102, 160, 105)` |
| 0,50 | `(144, 129, 89)` | `(145, 130, 90)` |
| 0,25 | `(186, 99, 74)` | `(188, 100, 75)` |

La fórmula es exacta: **composición alfa normal, sin sorpresas.** Y de ahí sale la regla de oficio que
`canales_lushows/12` da en una línea y que aquí queda demostrada: bajar la opacidad para «que no estorbe»
no produce collage, produce **doble exposición**, un color intermedio que no pertenece a ninguna de las
dos piezas. Si dos elementos compiten, la solución es moverlos o retrasarlos, no volverlos translúcidos.

---

## 4. La desviación de 1–2 niveles: dónde compone `overlay`

Fíjate en que lo medido nunca es exactamente `(60,190,120)`. Esa deriva tiene causa y se puede apagar:

| `overlay=…:format=` | píxel medido | original |
|---|---|---|
| *(sin poner nada: `auto`)* | `(60, 189, 118)` | `(60, 190, 120)` |
| `format=yuv420` | `(60, 189, 118)` | `(60, 190, 120)` |
| **`format=rgb`** | **`(60, 190, 120)`** | `(60, 190, 120)` |

Con `auto`, ffmpeg elige el espacio según lo que venga después; si la salida es `yuv420p`, compone en
YUV con croma a la mitad de resolución. Un desvío de 1–2 niveles **es invisible en una foto y no lo es**
en dos sitios: en un color de marca que tiene que empatar entre piezas, y en los bordes duros de un
rótulo, donde el croma submuestreado produce un filo sucio (`407`).

**Cuándo forzar `format=rgb`:** logotipo, texto quemado, cifra, cualquier plano de marca. Cuesta memoria y
un poco de CPU; en el resto del apilado no compensa.

---

## 5. El empate que no resuelve el orden

Hay un caso que el z no arregla, porque el problema no es quién tapa a quién:

> **Dos elementos grandes vivos a la vez y el ojo no sabe dónde ir.** Aunque no se toquen.

`canales_lushows/12` lo pone en número: nunca dos elementos de más de 500 px de ancho vivos a la vez; uno
baja a 380–420 px o entra 0,4 s más tarde. El orden de apilado no tiene nada que decir ahí. Si estás
reordenando capas para arreglar un plano confuso, estás usando la herramienta equivocada.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Invertir las dos entradas del `overlay` | El vídeo tapa la capa y el lienzo se recorta al tamaño de la capa |
| Bajar la opacidad para que dos elementos «convivan» | Doble exposición: un color que no es de ninguno |
| Dar por hecho que el elemento perdedor «se nota un poco» | Si el de encima es opaco y lo cubre, no se ve nada y no hay error |
| Comparar un color de marca sin fijar `overlay=format=rgb` | Deriva de 1–2 niveles entre piezas que deberían empatar |
| Reordenar capas para arreglar un plano confuso | El problema es de tamaño y de tiempo, no de z |
| Suponer que `enable` decide quién gana | `enable` solo apaga la mezcla; el orden sigue siendo el de la cadena |

## Relacionado

`400` el orden de render es narrativo · `402` el z dinámico · `404` acumular o sustituir ·
`406` el texto siempre arriba · `407` sombras y halos entre capas · `105` superponer capas ·
`104` filter_complex · `386` el elemento enterrado · `383` umbrales por tipo de contenido ·
`canales_lushows/12` capas simultáneas · `canales_lushows/26` superposición y oclusión
