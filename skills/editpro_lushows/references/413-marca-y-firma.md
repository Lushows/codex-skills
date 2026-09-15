# 413 · Marca y firma: la esquina que sobrevive

**Qué resuelve:** `87` decide **si** firmar, **de qué tamaño** (44–64 px de alto), **con qué opacidad**
(50–65%) y en qué esquina del lienzo. Todo eso sigue valiendo y no se repite aquí. Lo que falta —y es
donde la firma se pierde de verdad— es qué le pasa a esa esquina **cuando el vídeo cambia de formato o
cae debajo de la interfaz**. Una firma bien puesta en el máster puede no existir en tres de las cuatro
superficies donde se publica.

---

## La esquina no es un sitio: es un sitio por formato

Comprobado por aritmética el **11-sep-2026** con una firma de 200×56 px y recortes centrados:

**Máster vertical 1080×1920**

| Posición | x, y | 9:16 | 4:5 | 1:1 | 16:9 |
|---|---|---|---|---|---|
| arriba-izquierda (la de `87`) | 64, 290 | sí | sí | **NO** | **NO** |
| centro-arriba | 440, 290 | sí | sí | **NO** | **NO** |
| **centro-medio** | 440, 932 | sí | sí | **sí** | **sí** |
| abajo-derecha | 816, 1574 | sí | sí | **NO** | **NO** |

**Máster horizontal 1920×1080**

| Posición | x, y | 9:16 | 4:5 | 1:1 | 16:9 |
|---|---|---|---|---|---|
| abajo-derecha (la de `87`) | 1648, 952 | **NO** | **NO** | **NO** | sí |
| arriba-izquierda | 72, 72 | **NO** | **NO** | **NO** | sí |
| **centro-abajo** | 860, 722 | sí | sí | sí | sí |

Las ventanas de recorte centrado sobre 1920×1080, en píxeles y en tanto por uno del ancho:

| Destino | Ventana x | Ancho | t/1 |
|---|---|---|---|
| 1:1 | 420 – 1500 | 1080 | 0,562 |
| 4:5 | 528 – 1392 | 864 | 0,450 |
| 9:16 | 656 – 1264 | 608 | **0,316** |

**La conclusión incómoda: en un máster 16:9 no existe ninguna esquina que sobreviva al corte vertical.**
La columna que aguanta los cuatro formatos es la central, y una firma en el centro del cuadro no es una
firma, es una marca de agua de banco de imágenes. La salida no es mover la esquina: es **volver a
colocar la firma en cada formato**, que es barato si el logo va como capa suelta y carísimo si va
quemada en el máster (`38`).

---

## La comprobación, ejecutada

```python
def ventana(W, H, r):                      # r = ancho/alto del destino
    if W/H > r: w, h = H*r, H
    else:       w, h = W, W/r
    return ((W-w)/2, (H-h)/2, (W+w)/2, (H+h)/2)

def dentro(caja, v):
    return caja[0] >= v[0] and caja[1] >= v[1] and caja[2] <= v[2] and caja[3] <= v[3]
```

Cuatro líneas y responde lo que quince minutos de exportar y mirar no responden bien. Se corre con la
caja real del logo —ancho y alto del PNG escalado, no «más o menos»— antes de tocar ffmpeg.

---

## El otro enemigo: la interfaz encima de la firma

El recorte se la lleva; la interfaz la tapa. Las dos esquinas peores en vertical son las de abajo
(iconos, disco de audio, botón de suscribirse: cifras en `45`), y en horizontal la **inferior derecha**,
donde YouTube pinta el tiempo, la calidad y el botón de pantalla completa, dentro de la banda vetada
que mide `416`. Es decir: **la esquina que `87` recomienda para horizontal es la que el reproductor
usa para sus controles.** No es contradicción, es que `87` habla del lienzo y esto habla del
reproductor; en un vídeo que va a YouTube manda el segundo.

Alternativa medida: la firma horizontal sube a `y = 0,72·H − alto` (con 56 px de alto: `y = 722`), que
es el techo de la banda baja útil de `416`, y se pega al borde derecho sólo si no va a haber recorte.

---

## Verificar que la firma existe de verdad

Tres comprobaciones, ninguna opinable:

```bash
# 1 · la firma sobre fondo claro y sobre fondo oscuro (87 explica por qué)
ffmpeg -ss 4 -i salida.mp4 -frames:v 1 -y wm_claro.png

# 2 · la firma después del recorte al que vaya de verdad
ffmpeg -ss 4 -i salida.mp4 -vf "crop=608:1080:656:0,scale=1080:1920" -frames:v 1 -y wm_916.png

# 3 · la firma debajo de la interfaz real: carta de medida + captura + diff (415, 418)
python diff_interfaz.py carta_1080x1920.png captura_reels.png
```

La 2 es la que casi nadie hace y la que más firmas mata.

---

## Cuándo la firma no es un logo

`87` ya lista las alternativas (el `@usuario`, el isotipo, el personaje, el color). Lo que añade la
geometría: **el color y el personaje son las únicas firmas inmunes a las tres capas de `410`** —no
ocupan una esquina, no se recortan y ninguna interfaz las tapa. Para el canal documental de Paper
Empires, donde cada episodio 16:9 se despieza en verticales, esa es la firma que de verdad viaja: el
papel, la tinta y las dos marcas de columna, no un logotipo en una esquina que el corte se lleva.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Heredar la esquina del máster en los formatos derivados | La firma existe en uno de cuatro |
| Firmar abajo a la derecha en 16:9 pensando en televisión | Ahí viven los controles del reproductor (`416`) |
| Quemar el logo en el máster | Cada formato hay que rehacerlo entero |
| Buscar «la esquina que vale para todo» en un 16:9 | No existe: la ventana vertical es el 0,316 del ancho |
| Mover la firma al centro para que sobreviva | Deja de leerse como firma |
| Verificar la firma sólo en el máster | El recorte y la interfaz son las dos capas que se la comen |
| Medir la caja del logo «a ojo» | El alto del PNG escalado decide si entra o no; se lee, no se estima |
| Olvidar que un logo claro desaparece sobre fondo claro | Lo cubre `87`, y sigue siendo la causa número uno |

## Relacionado

`87` tamaño, opacidad, intermitencia y cuándo no firmar · `410` el mapa de intocables ·
`416` la banda de la barra de YouTube · `417` del vertical al cuadrado · `418` medir con captura real ·
`38` dejar el texto y el logo como capa suelta
