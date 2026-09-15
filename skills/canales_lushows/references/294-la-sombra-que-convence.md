# 294 · La sombra que convence

**Qué resuelve:** en este motor la sombra **no es un filtro del render: está horneada
dentro del PNG**, calculada sobre el tamaño nativo del recorte y recortada con él por
`getbbox()`. Eso tiene una consecuencia que no aparece en ningún sitio: la sombra **se
escala con el elemento**, así que el mismo valor escrito produce sombras distintas según
el ancho que le dé el montaje. Y tiene una avería, que se ha encontrado hoy midiendo.

`editpro/394` tiene la unidad —el *contacto*, cuánto se oscurece el anillo de suelo
alrededor del elemento—, la tabla de valores y el hallazgo de que el desenfoque no
controla el contacto. Eso no se repite. Aquí: qué pasa con esa unidad cuando la sombra
viaja dentro del PNG.

---

## Lo que hornean `revista.py` y `recortar_lustig.py`

```python
def montar(img_rgba, mask, borde, sombra=True, desvio=(6, 10), opacidad_sombra=168):
    papel_mask = dilatar(mask, borde)
    if sombra:
        neg = Image.new("RGBA", (w, h), (0, 0, 0, opacidad_sombra))
        neg.putalpha(papel_mask.filter(ImageFilter.GaussianBlur(11)))
        s.paste(neg, (m + desvio[0], m + desvio[1]), neg)
```

Desvío (7, 11) en modo revista, (6, 10) en tijera, (5, 9) en silueta; desenfoque 11;
opacidad 168 sobre 255. Son los valores de `25`, y sobre un PNG de 1.500–2.200 px están
bien. El problema empieza después.

## El desvío en pantalla: un factor de 4,1

`desvio_en_pantalla = 7 × w_del_montaje / ancho_nativo_del_PNG`. Medido sobre los 33
recortes de archivo que usa `ep01-lustig`:

| Recorte | Nativo | `w` | Desvío en pantalla |
|---|---|---|---|
| `torre_postal` | 1140 | 265 | **1,63 px** |
| `reglamento_celda` | 1632 | 446 | 1,91 px |
| … 33 piezas … | | | mediana **2,60 px** |
| `casilla_hospital` | 1341 | 1180 | 6,16 px |
| `casilla_nombre` | 1341 | 1280 | **6,68 px** |

**Mínimo 1,63 · mediana 2,60 · máximo 6,68: factor 4,1×.** Y según `editpro/394`, el
desplazamiento es una de las dos palancas que sí controlan el contacto (la otra es la
opacidad; el desenfoque no). El episodio tiene cuatro alturas de elemento distintas y nadie
las eligió: las eligió la relación entre la resolución de la foto de Commons y el ancho que
le tocó en el guion visual.

## El anillo fijo no sirve aquí

`editpro/394` mide el contacto en un anillo de **2 a 18 px** por fuera de la silueta.
Sobre este material, con la sombra ya escalada, sale esto:

| Recorte | `w` | Desvío | Contacto, anillo 2–18 px | Contacto, anillo proporcional |
|---|---|---|---|---|
| `celda_catre` | 711 | 3,10 | 0,70 | **2,50** |
| `imprenta_sellos` | 752 | 2,39 | 0,47 | **2,34** |
| `ficha_policial` | 1080 | 3,43 | 0,80 | **2,22** |
| `telegrafista` | 778 | 2,47 | 0,29 | **1,61** |
| `retrato_lustig` | 576 | 3,65 | 0,47 | **1,29** |

Con el anillo fijo, **todo el episodio marca contacto por debajo de 0,8**, que en la tabla
de `editpro/394` es «no existe: calcomanía pegada encima del fondo». Con el anillo escalado
por el mismo factor que la pieza, sube a 1,3–2,5.

La medida no está rota: **la sombra entera vive dentro de los primeros 2–4 px**, y un
anillo que empieza en 2 px la deja fuera o la diluye en 16 px de fondo limpio. Cuando la
sombra escala con el elemento, el anillo tiene que escalar también. Y aun corregido,
**1,3–2,5 sigue por debajo del 6–9 que le toca al plano frente**: esta sombra asienta la
mitad de lo que cree.

## La avería: la sombra que se convierte en una barra negra

En modo `revista` —el de los documentos— la máscara es un rectángulo entero:

```python
def revista(rgb, borde=13, semilla=7, grano=True, sombra=True):
    mask = Image.new("L", img.size, 255)          # TODO el lienzo
    return montar(img, mask, borde, sombra, desvio=(7, 11))
```

`dilatar()` sobre una máscara ya llena de 255 no puede crecer, así que `papel_mask` sale
255 en todas partes. Y **desenfocar una imagen uniforme no produce ningún degradado**: sale
255 otra vez. La capa de sombra deja de ser una sombra y pasa a ser **un rectángulo negro
completamente opaco**, desplazado 7 px a la derecha y 11 abajo, del que el papel solo tapa
la parte que le queda debajo.

Comprobado sobre los últimos píxeles de la fila central, en RGB/alfa:

| Recorte | Modo | Últimos píxeles | % del PNG semitransparente |
|---|---|---|---|
| `aviso_falsos` | revista | `0,0,0 / 255` | **0,00 %** |
| `cartel_fbi` | revista | `0,0,0 / 255` | **0,00 %** |
| `certificado_defuncion` | revista | `0,0,0 / 255` | **0,00 %** |
| `retrato_lustig` | silueta | `204,200,189/207 → 0,0,0/133 → 0,0,0/119` | 1,70 % |
| `torre_postal` | silueta | degradado limpio hasta alfa 0 | 4,11 % |

**22 de los 69 recortes tienen exactamente 0,00 % de píxeles semitransparentes**, y son
justo los de modo revista: los documentos, los telegramas, las casillas del certificado,
los bonos, los planos, el cartel del FBI. Todos llevan en el borde derecho e inferior una
**barra negra dura de 1,9 a 6,7 px en pantalla**, sin degradado. En pantalla eso no se lee
como sombra: se lee como un error de recorte. Y le pasa justo a las piezas que sostienen
la credibilidad del episodio.

## El arreglo

La máscara del papel tiene que ser **más pequeña que el lienzo** para que el desenfoque
tenga borde donde trabajar. Dos líneas:

```python
def revista(rgb, borde=13, semilla=7, grano=True, sombra=True):
    img = granular(rgb, semilla) if grano else rgb.convert("RGBA")
    w, h = img.size
    mask = Image.new("L", (w, h), 0)
    # el rectangulo del documento, con aire suficiente para que el papel y la
    # sombra tengan sitio: sin este margen, el desenfoque de una mascara llena
    # devuelve 255 y la sombra sale como una barra negra opaca.
    aire = borde + 14
    ImageDraw.Draw(mask).rectangle([aire, aire, w - aire, h - aire], fill=255)
    return montar(img, mask, borde, sombra, desvio=(7, 11))
```

Comprobación de una línea, que debería estar en la auditoría de recortes:

```python
semi = ((a > 4) & (a < 250)).mean()
if semi < 0.005:
    avisar(f"{alias}: sin banda de sombra ({semi*100:.2f}%) — barra dura o sin sombra")
```

Sobre los 47 recortes que sí la tienen, la banda ocupa entre el **0,71 % y el 4,11 %** del
PNG, mediana **1,56 %**. Ese es el rango sano.

## Elegir el desvío contra el ancho del montaje

Como el `w` se conoce antes —está en el guion visual—, el desvío se despeja igual que el
margen de papel (`291`):

```python
def desvio_para(objetivo_px, ancho_nativo, w_montaje):
    """objetivo 4 px en pantalla = plano frente. 2 px = plano medio."""
    k = ancho_nativo / float(w_montaje)
    return (int(round(objetivo_px * k)), int(round(objetivo_px * 1.57 * k)))

# casilla_nombre (nativo 1341, sale a 1280) -> (4, 7): casi lo que ya tiene
# torre_postal   (nativo 1140, sale a  265) -> (17, 27): mas del doble de lo escrito
```

El 1,57 es la proporción del canal entre desvío horizontal y vertical (7 y 11): la luz
viene de arriba a la izquierda en todo el episodio y esa relación no se toca, porque es lo
que hace que treinta recortes distintos parezcan iluminados por la misma lámpara.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Tratar el desvío como píxeles de pantalla | Se hornea sobre el nativo: en pantalla sale entre 1,6 y 6,7 |
| Medir el contacto con anillo fijo sobre sombra escalada | Todo marca «calcomanía» aunque la sombra esté bien puesta |
| Desenfocar una máscara llena de 255 | No hay degradado: sale barra negra opaca |
| Dar por buena una sombra sin mirar el % semitransparente | 22 de 69 piezas tenían 0,00 % y nadie lo vio |
| Subir el desenfoque para «asentar más» | El desenfoque no controla el contacto (`editpro/394`) |
| Heredar la sombra del plano frente en el medio | El tamaño dice lejos y la sombra dice aquí delante (`22`) |
| Cambiar la proporción 7/11 pieza a pieza | Doce recortes con doce lámparas distintas |
| Corregir la sombra sin regenerar el PNG | Está horneada: no hay filtro que la quite en el render |

## Relacionado

`25` el borde de papel · `291` el borde de papel medido en pantalla ·
`22` profundidad por capas (regenerar la sombra, no heredarla) · `293` profundidad sin 3D ·
`196` limpiar el alfa · `161` auditar sobre gris · `297` documentos como imagen ·
`editpro/394` la sombra que asienta (la unidad de contacto y su tabla) ·
`editpro/396` el plano que no separa (§3.3, el plano que la sombra desmiente)
