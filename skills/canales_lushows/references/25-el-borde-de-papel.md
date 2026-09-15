# 25 · El borde de papel

**Qué resuelve:** una foto pegada sin borde no es un collage, es una imagen encima de
otra. El margen crema, la sombra y el accidente físico (rasgado, cinta, grapa) son lo
que convierte material de archivo en **papel**, y son la firma visual del canal.

---

## Anatomía del recorte

De fuera hacia dentro: **sombra proyectada** → **margen de papel** `#F0EBDE` → **la
foto**, con grano y −12% de saturación.

| Pieza | Valor en `revista.py` | Cuándo se cambia |
|---|---|---|
| Margen | `MaxFilter(borde*2+1)`, borde 14 | Tijera: 15-20 (foto abierta, `tijera.py`) |
| Color del papel | `(240, 235, 222)` | Fijo. Es el papel del canal |
| Sombra | offset (7, 11), `GaussianBlur(10)`, alfa 170 | Plano medio: (4, 6) blur 6 · levantado: (14, 20) blur 18 |
| Grano | valores 118-138, alfa 26 | Subir a 34 si el fondo es muy texturado (`23`) |
| Saturación | −12%, contraste +4% | Fijo, es lo que unifica fuentes distintas |

**El margen se mide en proporción, no en píxeles absolutos.** 14 px sobre una imagen de
1500 px de lado es ~0,93% del lado largo. Si el recorte entra al montaje con `w: 620`,
ese margen queda en 5,8 px en pantalla — correcto. Si entra con `w: 1400`, queda en 13
px y se ve grueso. Para elementos grandes, generar el PNG con `borde=9`.

## Qué NO lleva margen de papel

`revista.py` lo tiene declarado y hay que respetarlo:

- **Marcas gráficas**: `cotas`, `alerta`, `sello`, `desaparecido`, los contadores
  `cont_00`…`cont_10`. Son tinta sobre el cuadro, no papel pegado.
- **Lo que ya pasó por `tijera.py`**: trae su propio borde. Doblarlo da un marco de
  30 px que se ve como un error.

## Borde rasgado

El margen liso se lee como recorte de tijera. El rasgado se lee como página arrancada
—más agresivo, para titulares de prensa y documentos filtrados:

```python
import random
from PIL import Image, ImageChops, ImageFilter

def borde_rasgado(mask, amplitud=11, semilla=7):
    """Dilata el alfa y luego le arranca mordiscos al margen nuevo."""
    w, h = mask.size
    rnd = random.Random(semilla)
    ruido = Image.new("L", (w, h))
    ruido.putdata([rnd.randint(0, 255) for _ in range(w * h)])
    ruido = ruido.filter(ImageFilter.GaussianBlur(2.4))       # manchas, no puntos
    dil = mask.filter(ImageFilter.MaxFilter(amplitud * 2 + 1))
    anillo = ImageChops.subtract(dil, mask)                   # solo el margen nuevo
    mordidas = ruido.point(lambda v: 0 if v < 118 else 255)
    return ImageChops.lighter(mask, ImageChops.multiply(anillo, mordidas))
```

Se usa **en vez de** la línea `papel_mask = sil.filter(MaxFilter(...))` de
`modo_revista()`. La sombra se calcula después, sobre la máscara ya rasgada: si no, la
sombra sale lisa y el borde dentado, y la contradicción se ve.

`GaussianBlur(2.4)` es lo que convierte ruido de píxel en mordiscos de papel. Con blur
0 salen puntos sueltos y parece suciedad del render.

## Cinta adhesiva

Es la **única excepción** a la opacidad 1 del canal, y se sostiene porque la cinta real
es translúcida. Se hornea **dentro** del PNG: nunca se baja la opacidad del elemento
entero en el filtro de ffmpeg.

```python
from PIL import Image, ImageDraw, ImageFilter

def cinta(lienzo, centro, largo=180, ancho=54, angulo=-24, alfa=118):
    """Pega un trozo de cinta translucida sobre el lienzo RGBA, in place."""
    t = Image.new("RGBA", (largo, ancho), (238, 234, 220, alfa))
    d = ImageDraw.Draw(t)
    d.rectangle([0, 0, largo, 3], fill=(255, 252, 244, alfa + 40))          # brillo
    d.rectangle([0, ancho - 4, largo, ancho], fill=(176, 168, 146, alfa))   # borde
    for x in range(0, largo, 7):                                            # dentado
        d.rectangle([x, 0, x + 3, 2], fill=(0, 0, 0, 0))
    t = t.rotate(angulo, expand=True, resample=Image.BICUBIC)
    s = Image.new("RGBA", t.size, (0, 0, 0, 0))
    s.putalpha(t.split()[3].filter(ImageFilter.GaussianBlur(4)).point(lambda v: v // 3))
    lienzo.alpha_composite(s, (centro[0] - t.width//2 + 3, centro[1] - t.height//2 + 5))
    lienzo.alpha_composite(t, (centro[0] - t.width//2, centro[1] - t.height//2))
```

La cinta va **en una esquina o en el borde superior**, cruzando el límite del papel: si
queda toda dentro de la foto, no está pegando nada. Dos trozos por recorte como máximo.

## Grapa y clip

```python
def grapa(lienzo, pos, largo=40, angulo=8):
    g = Image.new("RGBA", (largo, 13), (0, 0, 0, 0))
    d = ImageDraw.Draw(g)
    d.rectangle([0, 4, largo, 8], fill=(126, 122, 112, 255))   # cuerpo
    d.rectangle([0, 3, largo, 5], fill=(196, 192, 182, 255))   # brillo superior
    d.rectangle([0, 8, largo, 9], fill=(58, 55, 48, 255))      # sombra inferior
    g = g.rotate(angulo, expand=True, resample=Image.BICUBIC)
    lienzo.alpha_composite(g, pos)
```

El clip es el mismo principio con un contorno en U (`d.arc` + dos líneas) y **tiene que
asomar por fuera del papel**: uno que no sobresale no sujeta nada.

**Reparto:** la mayoría de los recortes van limpios — 1 de cada 4 lleva accidente
físico, y nunca dos del mismo tipo seguidos. Si todos llevan cinta, la cinta no dice nada.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Doble margen (revista sobre tijera) | Marco de 30 px: se ve como error de proceso |
| Margen fijo en px para elementos de `w` muy distinto | Uno con marco fino y otro con marco gordo en la misma escena |
| Sombra calculada antes del rasgado | Borde dentado con sombra lisa |
| Ruido del rasgado sin desenfocar | Puntos sueltos: parece suciedad del render |
| Bajar la opacidad del elemento para simular cinta | Doble exposición: rompe la regla del canal |
| Cinta que no cruza el borde del papel | No pega nada; se lee como una mancha |
| `hash(alias)` como semilla | El grano cambia entre procesos: el episodio no se reproduce igual. Usar `zlib.crc32` |

## Relacionado

`23` empatar recorte y fondo · `22` profundidad por capas · `24` agrupar y separar ·
`66` grano y textura · `62` efectos de documento
