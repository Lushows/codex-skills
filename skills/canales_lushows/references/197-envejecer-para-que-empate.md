# 197 · Envejecer para que empate

**Qué resuelve:** los fondos del canal son tinta, verde institucional y ocre. Una foto
moderna a todo color —una celda con puerta amarilla, una chatarrería azul, un cielo
saturado— pegada sobre eso no se lee como archivo: se lee como una captura de Google
Maps sobre un cartel antiguo. El collage se rompe por el color antes que por cualquier
otra cosa.

---

## La función

```python
from PIL import ImageEnhance, ImageOps, Image

def envejecer(rgb, grado):
    """Lleva el material moderno al duotono de archivo.
    grado 0   = no toca nada
          0,2 = archivo que solo necesita un punto menos de color
          0,6-0,8 = foto moderna a todo color que si no, canta."""
    if grado <= 0:
        return rgb
    desat = ImageEnhance.Color(rgb).enhance(max(0.0, 1 - grado * 0.85))
    duo = ImageOps.colorize(ImageOps.grayscale(rgb),
                            black=(38, 33, 27),      # tinta, no negro puro
                            white=(246, 241, 228),   # papel crema, no blanco
                            mid=(142, 126, 104))     # el ocre que une el episodio
    return Image.blend(desat, duo, min(0.85, grado))
```

Tres decisiones dentro:

- **Desaturar y virar, no solo desaturar.** Una foto en gris puro sobre un fondo ocre
  sigue sin empatar: le falta el tinte común.
- **`black` y `white` no son negro ni blanco.** `(38,33,27)` y `(246,241,228)` son la
  tinta y el papel del canal. Un duotono a negro puro mata las sombras y el recorte se
  recorta contra el fondo oscuro.
- **El `blend` topa en 0,85.** Nunca se llega al duotono puro: ese 15% de la foto
  desaturada es lo que impide que todas las piezas parezcan la misma textura.

## La métrica correcta no es la saturación

La tentación es medir saturación media y comprobar que baja. **No baja de forma
monótona**, porque el duotono sepia *tiene* saturación propia. Medido sobre una celda de
Alcatraz de 2005:

| grado | saturación media HSV | **dispersión de tono** |
|---|---|---|
| 0 | 61,1 | 0,049 |
| 0,20 | 52,7 | 0,025 |
| 0,45 | 48,1 | 0,007 |
| 0,62 | **48,0** | 0,002 |
| 0,78 | 51,1 | **0,000** |
| 0,90 | 52,5 | 0,000 |

La saturación toca fondo en 0,62 y **vuelve a subir**. Si el control de calidad usa
saturación, aprueba el grado 0,45 y rechaza el 0,90, que es justo al revés.

Lo que sí mide lo que importa es la **variedad de tonos**: cuántos colores distintos
quedan. Un duotono, por definición, tiene uno.

```python
import numpy as np

def dispersion_tono(im):
    """Variedad de tonos, pesada por saturación. 0 = un solo tono (duotono).
    Es la medida de si una pieza EMPATA con el archivo."""
    h, s, v = [np.asarray(c, dtype=np.float32) for c in im.convert("HSV").split()]
    ang, w = h / 255.0 * 2 * np.pi, s / 255.0
    if w.sum() < 1:
        return 0.0
    R = np.hypot((np.cos(ang) * w).sum(), (np.sin(ang) * w).sum()) / w.sum()
    return float(1 - R)          # 1 - longitud del vector medio circular
```

**Umbral del canal: ≤ 0,005.** Por encima de eso la pieza tiene más de un color vivo y no
va a empatar con los fondos.

## Los grados por tipo de material

Medida la dispersión de tono del material del episodio 01 **sin tratar**, y el grado que
acabó llevando cada uno:

| Material | Dispersión sin tratar | `virar` | Por qué |
|---|---|---|---|
| Ficha policial, grabados, documentos de época | **0,001** | 0 – 0,20 | Ya es archivo. Un documento va a `0` para no ensuciar lo que hay que leer |
| Foto de archivo virada por el escaneo | 0,001 – 0,010 | 0,18 – 0,30 | Solo un punto menos de color |
| Interior moderno de tono contenido (galería de celdas) | 0,026 | 0,60 – 0,66 | Colores apagados pero actuales |
| Exterior moderno con cielo (edificio de Alcatraz) | 0,075 | 0,70 – 0,78 | El azul del cielo es lo que más canta |
| Foto moderna a todo color (automóvil restaurado) | **0,606** | 0,76 | El caso extremo: un solo objeto rojo destruye el cuadro |

Regla práctica: **archivo 0 – 0,30 · interior moderno 0,60 – 0,70 · exterior moderno
0,70 – 0,80**. Por encima de 0,85 no hay ganancia (el `blend` está topado).

## El documento es la excepción

```python
("certificado_defuncion", "victor_lustig_death_certificate_png", "revista",
 D(virar=0, contraste=1.10, nitidez=0.55, grano=False, borde=15, semilla=101)),
```

`virar=0`, `grano=False`, y **nitidez positiva**. El documento está en pantalla para que
se lea; envejecerlo le quita contraste a la tinta contra el papel, que es lo único que lo
hace legible. Su empate con el fondo no lo da el color, lo da el margen de papel (`25`).

## Lo que el envejecido NO arregla

Un anacronismo. Una caravana presidencial de 2021 virada a sepia sigue siendo una
caravana de 2021, y ahora además parece una falsificación. Cuando el problema es el
contenido y no el color, la pieza se descarta (`198`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Medir saturación para validar | Aprueba el grado 0,45 y rechaza el 0,90 |
| El mismo `virar` para todo el episodio | Los documentos pierden legibilidad o el cielo sigue azul |
| Duotono a negro puro y blanco puro | Sombras muertas; el recorte no se despega del fondo |
| `blend` al 100% | Todas las piezas con la misma textura plana |
| Envejecer un documento | Deja de leerse, que era su única función |
| Envejecer para salvar un anacronismo | Sigue siendo un anacronismo, y ahora parece falso |

## Relacionado

`198` · `23` · `51` · `66` · `195` · `163`
