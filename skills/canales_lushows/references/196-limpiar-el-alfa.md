# 196 · Limpiar el alfa

**Qué resuelve:** `rembg` no devuelve una silueta: devuelve una **probabilidad** por
píxel. Ese alfa blando produce halos translúcidos, figuras fantasma y agujeros que no se
ven sobre el fondo con el que trabajaste y saltan sobre el que acabas usando.

---

## El caso real: el arco de la torre

En la torre en construcción de Durandelle, `rembg` dejaba bajo el arco una zona de alfa
intermedio: un velo semitransparente donde debería haber cielo. Sobre el fondo de tinta
del episodio era invisible; sobre gris medio (`161`) era evidente. Medido hoy, alfa crudo
contra alfa limpio:

| Pieza | | alfa blando | halo | islas | huecos interiores |
|---|---|---|---|---|---|
| `torre_construccion` | crudo | **6,31%** | 1,25% | 1 | **0,64%** |
| | limpio | 0,38% | 0,18% | 1 | 0 |
| `torre_hoy` | crudo | 5,03% | 1,75% | **7** | 0,52% |
| | limpio | 0,39% | 0,19% | **1** | 0 |
| `torre_dirigible` | crudo | 3,27% | **2,71%** | 3 | 0 |
| | limpio | 0,03% | 0,01% | 3 | 0 |

Definiciones, que son las que usa la auditoría del canal:

- **alfa blando** = píxeles con `10 < a < 245`. Es todo lo que no es ni foto ni vacío.
- **halo** = píxeles con `12 < a < 110`. Casi transparentes pero no del todo: el velo.
- **huecos** = agujeros cerrados dentro de la figura. El arco, las ventanas, el espacio
  entre el brazo y el cuerpo. Unos hay que tapar y otros no; ver más abajo.

`torre_hoy` con **7 islas** es el otro síntoma: seis manchas sueltas de cielo que rembg
dio por figura y que al montar aparecen flotando junto a la torre.

## Las cuatro operaciones, en este orden

```python
import numpy as np
from scipy import ndimage
from PIL import Image, ImageFilter

def limpiar_mascara(a, umbral=150, isla_min=0.004, tapar_huecos=True):
    """Alfa blando de rembg -> silueta OPACA y sin fantasmas."""
    # 1 · BINARIZAR: la regla de opacidad 1 del canal empieza aquí.
    m = np.asarray(a, dtype=np.uint8) >= umbral
    # 2 · APERTURA: erosión + dilatación. Borra motas de 1-2 px y deshace los
    #     puentes finos con los que una mancha de cielo se pega a la figura.
    m = ndimage.binary_opening(m, np.ones((3, 3), bool))
    # 3 · TAPAR HUECOS interiores.
    if tapar_huecos:
        m = ndimage.binary_fill_holes(m)
    # 4 · ISLAS: se queda con lo grande y tira lo suelto.
    etq, n = ndimage.label(m)
    if n > 1:
        tam = ndimage.sum(m, etq, range(1, n + 1))
        corte = max(tam.max() * 0.06, m.size * isla_min)
        vivas = {i + 1 for i, t in enumerate(tam) if t >= corte}
        m = np.isin(etq, list(vivas)) if vivas else m
    salida = Image.fromarray((m * 255).astype(np.uint8), "L")
    # el pelo de antialias: 0,7 px. Menos deja escalera; más devuelve el halo.
    return salida.filter(ImageFilter.GaussianBlur(0.7))
```

Los umbrales, y por qué:

| Umbral | Valor | Por qué |
|---|---|---|
| `umbral` de binarización | **150** | 128 se queda con demasiado velo; 190 come el borde de la figura |
| Kernel de apertura | **3×3** | 5×5 redondea las esquinas de una ficha policial |
| `isla_min` | **0,4%** del cuadro | Por debajo, se cuelan manchas de cielo; por encima, se pierde un brazo separado |
| Corte relativo | **6%** de la isla mayor | Protege las figuras con dos partes legítimas (cabeza y sombrero, torre y base) |
| Desenfoque final | **0,7 px** | Un pelo de antialias, que además queda bajo el margen de papel |

El orden importa: **apertura antes que tapar huecos**. Al revés, un puente fino entre la
figura y una mancha de fondo cierra un «hueco» enorme y se rellena media foto.

## Cuándo NO tapar los huecos

`binary_fill_holes` tapa todo agujero cerrado. En una torre eso es correcto —el arco
lleno se lee como silueta de torre—, pero en un objeto calado (una reja, un asa, unas
esposas) el agujero **es** la forma. Ahí se pasa `tapar_huecos=False` y se acepta el
hueco, o se tapan solo los pequeños:

```python
huecos = ndimage.binary_fill_holes(m) & ~m
etq, n = ndimage.label(huecos)
if n:
    tam = ndimage.sum(huecos, etq, range(1, n + 1))
    pequenos = {i + 1 for i, t in enumerate(tam) if t < m.size * 0.002}   # < 0,2%
    m = m | np.isin(etq, list(pequenos))      # tapa las motas, respeta el calado
```

## El margen de papel lo remata, pero no lo arregla

El margen crema se dibuja dilatando la máscara con una transformada de distancia
(`dist <= radio`), más rápida que `MaxFilter` y sin la esquina cuadrada que deja un
kernel cuadrado. De paso tapa el píxel de antialias. Pero el papel **no** tapa un halo
del 2,71%: el velo está dentro de la figura, no en su contorno. Confiar en el borde da el
resultado de siempre: bien sobre negro, sucio sobre cualquier otro fondo.

## La comprobación final

La auditoría del canal erosiona la parte opaca 13 px y exige que **ahí dentro el alfa sea
255 clavado**:

```python
dentro = ndimage.binary_erosion(a >= 250, np.ones((13, 13), bool))
interior = int(a[dentro].min()) if dentro.any() else 255
if interior < 255:  avisar("INTERIOR TRASLÚCIDO")
if ((a > 12) & (a < 110)).mean() > 0.06:  avisar("HALO")
if ((a > 10) & (a < 245)).mean() > 0.10:  avisar("ALFA BLANDO")
```

Los 69 PNG del episodio 01 pasan: **interior = 255 en los 69, ningún halo por encima del
6%, alfa blando máximo 3,19%**.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Usar el alfa de rembg tal cual | Velo translúcido invisible sobre negro y evidente sobre gris |
| Tapar huecos antes de la apertura | Un puente de 2 px rellena media foto |
| Binarizar a 128 | Sobrevive el 40% del velo |
| No quitar islas | Seis manchas de cielo flotando junto a la figura |
| `tapar_huecos=True` en objetos calados | Una reja se convierte en una plancha |
| Revisar sobre fondo negro | Todo parece limpio hasta que el fondo cambia |

## Relacionado

`195` · `194` · `161` · `25` · `144` · `150`
