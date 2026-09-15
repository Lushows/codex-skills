# 291 · El borde de papel, medido en pantalla

**Qué resuelve:** `25` da la anatomía del recorte —margen crema, sombra, cinta, grapa,
rasgado— y sus valores en el generador. Esto es la otra mitad: **cuántos píxeles de
margen quedan de verdad en el vídeo**, que no es lo que dice la receta. El margen se
hornea sobre el PNG nativo y el montaje lo escala; entre el valor escrito y el valor visto
hay un factor que nadie mira.

No se repite nada de `25`: ni los colores, ni la cinta, ni el rasgado. Aquí: la
conversión, la medida y el rango que hay que defender.

---

## La conversión, que es toda la trampa

```
margen_en_pantalla = borde_nativo × (w_del_montaje / ancho_nativo_del_PNG)
```

`borde` se escribe en la receta de `recortar_lustig.py` (12–18 px sobre un PNG de
1.100–2.200 px de lado) y `w` lo decide el guion visual muchas horas después. Nadie de los
dos sabe lo que hace el otro. `25` ya avisa de que el margen «se mide en proporción»; el
número de cuánto se desvía es este.

## Medido hoy sobre `ep01-lustig`

Margen crema real, mediana fila a fila sobre el PNG y llevado al ancho del montaje:

| Recorte | Margen nativo | `w` del montaje | **En pantalla** |
|---|---|---|---|
| `boveda_servicio` | 1 px | 486 | **0,3 px** |
| `grupo_servicio_secreto` | 7 px | 820 | 2,6 px |
| `torre_postal` | 13 px | 265 | 3,0 px |
| `trenes_chatarra` | 10 px | 860 | 3,9 px |
| `bajo_la_torre` | 14 px | 820 | 5,2 px |
| `celda_catre` | 13 px | 711 | 5,8 px |
| `galeria_celdas` | 14 px | 802 | 7,0 px |
| `ficha_policial` | 16 px | 1080 | **7,8 px** |

**18 recortes con margen medible: mínimo 0,3 px · mediana 4,6 px · máximo 7,8 px.**
Factor 28,7× entre los extremos, y solo 2 de 18 caen por debajo de 3 px.

Dos lecturas:

- **El sistema aguanta.** 16 de 18 quedan entre 2,6 y 7,8 px, que es un margen que se ve
  como papel sin parecer un marco. No es suerte: los `borde` de la receta suben con el
  tamaño nativo de la fuente, y los `w` del montaje bajan con la altura del recorte, y
  las dos cosas se compensan a medias.
- **Los dos que fallan fallan por lo mismo.** `boveda_servicio` con 1 px nativo no tiene
  margen: la silueta salió tan pegada al borde del lienzo que el dilatado no tuvo sitio.
  Un margen de 0,3 px en pantalla **no es un margen fino, es ninguno**: ese recorte se lee
  como imagen pegada, no como papel, que es justo el defecto que `25` existe para evitar.

## El rango que se defiende

| Margen en pantalla | Cómo se lee |
|---|---|
| menos de 2 px | No hay papel: imagen pegada sobre otra |
| **3 – 8 px** | **Papel. El rango de trabajo** |
| más de 12 px | Marco: se ve el proceso, no el collage |

Con el lienzo de 1920 esos 3–8 px son el **0,16 % – 0,42 % del ancho del cuadro**. Esa es
la unidad portátil: si mañana el canal renderiza a 2160, el rango en píxeles se dobla y el
porcentaje no cambia.

## Elegir el `borde` al revés

Como el `w` final se conoce antes que el recorte —está en el guion visual—, el `borde` se
despeja en vez de adivinarse:

```python
def borde_para(objetivo_px, ancho_nativo, w_montaje):
    """El 'borde' que hay que escribir en la receta para que en pantalla salga
    'objetivo_px'. objetivo 5 px = el centro del rango de trabajo."""
    return max(6, int(round(objetivo_px * ancho_nativo / float(w_montaje))))

# ficha_policial: nativo 2206, sale a 1080 -> borde 10 da 4,9 px en pantalla
# torre_postal:   nativo 1140, sale a  265 -> borde 22 da 5,1 px en pantalla
```

El suelo de 6 no es capricho: por debajo, el dilatado se come el antialias de la silueta y
el margen queda mordido a trozos.

## Comprobarlo sin renderizar

```python
import numpy as np
from PIL import Image

PAPEL = np.array([240, 235, 222])

def margen_pantalla(png, w_montaje):
    """Mediana del margen crema, en px de PANTALLA. Se mide fila a fila desde el
    primer pixel OPACO: empezar desde el primer pixel no vacio mide la sombra."""
    a = np.asarray(Image.open(png).convert("RGBA"))
    al, rgb = a[:, :, 3], a[:, :, :3].astype(int)
    papel = (np.abs(rgb - PAPEL).max(axis=2) <= 8) & (al >= 250)
    op, anchos = al >= 250, []
    for y in range(0, al.shape[0], 7):                 # una de cada 7 filas basta
        idx = np.where(op[y])[0]
        if len(idx) < 5:
            continue
        x, n = idx[0], 0
        while x + n < al.shape[1] and papel[y, x + n]:
            n += 1
        anchos.append(n)
    if not anchos:
        return 0.0
    return float(np.median(anchos)) * w_montaje / a.shape[1]
```

**Se mide desde el primer píxel con alfa ≥ 250, no desde el primero con alfa > 0.** La
sombra horneada vive fuera del papel y con el umbral flojo se cuenta como margen: da
valores de 20–30 px que no existen.

## Dónde NO vale la conversión

Las marcas gráficas que `25` declara sin papel —`cotas`, `alerta`, `sello`, los
contadores— no entran en esta cuenta, y las piezas que pasaron por `tijera.py` traen su
borde propio: aplicarles otro da el marco de 30 px del que ya avisa `25`.

Y hay un caso que parece un margen fino y es otra cosa: un recorte cuyo `w` sube porque
`ancho_legible()` lo empujó hasta su suelo de texto (`297`). Ahí el margen crece con él y
puede pasarse de 12 px sin que nadie lo haya decidido. Cuando el ancho lo manda la
legibilidad, el `borde` se recalcula contra ese ancho, no contra el que estaba escrito.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Escribir `borde` mirando el PNG nativo | En pantalla sale entre 0,3 y 7,8 px sin control |
| Medir el margen desde el primer píxel no vacío | Se cuenta la sombra: 20–30 px que no existen |
| Dar por bueno un margen de 1–2 px | No es papel fino: es imagen pegada sobre otra |
| Dejar el `borde` cuando el suelo de legibilidad sube el `w` | El margen se pasa de 12 px y se ve el marco |
| Pensar el rango en píxeles y no en % del lienzo | Al cambiar de resolución hay que rehacerlo todo |
| Aplicar margen a una pieza que ya pasó por tijera | Marco doble de 30 px (`25`) |
| Auditar el margen sobre fondo negro | El crema sobre negro siempre se ve; sobre ocre, no |

## Relacionado

`25` el borde de papel (anatomía, cinta, grapa, rasgado) · `194` el ancho útil ·
`195` silueta contra tijera · `196` limpiar el alfa · `294` la sombra que convence ·
`297` documentos como imagen · `161` auditar sobre gris
