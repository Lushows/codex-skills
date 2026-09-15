# 194 · Medir el ancho ÚTIL, no el del lienzo

**Qué resuelve:** una pieza puede cumplir el mínimo de resolución en la fuente, cumplirlo
en el lienzo de trabajo, y aun así llegar al montaje blanda. Lo que se ve en pantalla no
es el lienzo: es la parte **opaca** del PNG. Si no se mide con el alfa, el filtro de
calidad no filtra nada.

---

## El caso real: 694 px

El episodio 01 impone 1100 px de ancho mínimo. La postal de la torre Eiffel los pasaba
con holgura en la fuente. Reproducido hoy, con la primera pasada de `silueta()`:

| Pieza | Fuente | Lienzo de trabajo | Lienzo del PNG | **Ancho útil** |
|---|---|---|---|---|
| `torre_construccion` | 3277×4169 | 1729×2200 | 1532×1927 | 1495 ✅ |
| `torre_hoy` | 2900×5367 | 1189×2200 | 790×1785 | **754** ❌ |
| `torre_postal` | 2334×3301 | 1556×2200 | 732×1638 | **694** ❌ |

La postal entraba a 2334 px. El recorte de silueta salió a 694 px de ancho útil: **el
44% del lienzo de trabajo**. No porque la foto fuera mala, sino porque la torre ocupa un
tercio del encuadre y el resto es cielo, que rembg tira.

`torre_construccion` sale bien con la misma regla y la misma fuente porque el grabado de
Durandelle está encuadrado a la torre: ahí la figura cubre el 29% del cuadro contra el
16% de `torre_hoy`. **La diferencia no está en los píxeles de origen, está en cuánto del
cuadro ocupa la figura.**

## La medida correcta

```python
import numpy as np

def ancho_util(img):
    """Ancho de la parte OPACA (foto + margen de papel), sin contar la sombra.
    La sombra es alfa parcial y engorda el lienzo 30-60 px sin aportar imagen."""
    a = np.asarray(img.convert("RGBA").split()[3], dtype=np.uint8) >= 250
    cols = np.where(a.any(axis=0))[0]
    return int(cols[-1] - cols[0] + 1) if len(cols) else 0
```

`>= 250` y no `> 0`: el umbral es lo que separa la foto de su sombra proyectada. Con
`> 0` la sombra cuenta como imagen y `torre_postal` habría «medido» 732 px en vez de 694,
igual de insuficiente pero además mal medido.

En las piezas terminadas del episodio 01 la relación **útil / lienzo** vale 1,00 en las
de tijera y de revista (el rectángulo llena el lienzo) y baja a **0,966–0,976** en las de
silueta, que es exactamente el ancho que se come la sombra.

## Recuperar el ancho: segunda pasada, no estirar

Cuando el ancho útil se queda corto, la respuesta **no** es escalar el PNG: eso sube el
número sin subir el detalle. Se vuelve a abrir la fuente pidiendo un lienzo más grande —
la fuente ya tenía esos píxeles, solo que el tope de 2200 los estaba tirando:

```python
util = ancho_util(out)
if util and util < ANCHO_MIN:
    f = min(1.8, ANCHO_MIN / util)                       # 1100/694 = 1,58
    rgb2 = abrir(fichero, lado_max=min(4000, round(LADO_MAX * f * 1.04)), **cfg)
    out2, ok2 = silueta(rgb2, borde=borde, semilla=semilla, umbral=umbral)
    if ok2 and ancho_util(out2) > util:
        out, util = out2, ancho_util(out2)
    if util < ANCHO_MIN:                                 # la fuente no daba para más
        g = min(1.6, ANCHO_MIN / util)
        out = out.resize((round(out.width * g), round(out.height * g)), Image.LANCZOS)
        real += " +estirada"                             # queda ANOTADO en el manifiesto
```

Tres umbrales, los tres deliberados:

- **`f = min(1.8, …)`** — pedir más de 1,8× el lienzo dispara la memoria y el tiempo de
  `rembg` sin ganancia; por encima de eso la fuente casi nunca tiene detalle real.
- **`lado_max` tope 4000** — algunas fuentes son de 300 Mpx (`Image.MAX_IMAGE_PIXELS`
  hay que subirlo a 400 millones para abrirlas); sin tope, una pieza sola se come la RAM.
- **`+estirada`** — si aun así no llega, se estira **como máximo 1,6×** y se escribe en
  el manifiesto. El episodio 01 tiene exactamente una pieza así: `torre_postal`, que
  acabó en 1140×2596 con **1101 px** de ancho útil. Uno por encima del mínimo.
  Estirar sin anotarlo es mentirle a la auditoría (`140`).

## El resultado, auditado

Las 69 piezas del episodio, medidas con el alfa:

```
util < 1100 px .............. 0 de 69
mediana útil / lienzo ....... 1,00
mínimos (las tres siluetas) . 1101 · 1155 · 1495
```

Y el reparto de tratamientos explica por qué el problema solo aparece en tres piezas: 42
tijera y 22 revista salen del rectángulo entero, donde útil = lienzo. **Solo la silueta
tiene este fallo**, porque solo la silueta tira parte del cuadro.

## Por qué 1100 y no 1920

El canal entrega a 1080p. Un recorte rara vez ocupa el ancho completo del cuadro: ocupa
entre un tercio y dos tercios, y además se le hace zoom lento (`35`). 1100 px de ancho
útil cubre un elemento a media pantalla con un 20% de margen de zoom. Pedir 1920 a cada
pieza dejaría fuera material de archivo que no existe más grande — el certificado de
defunción de Lustig mide 1532×1358 y no hay otro.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Filtrar por el ancho de la fuente y no volver a mirar | Recortes de 694 px en el montaje final |
| Medir `img.width` del PNG | La sombra y el papel inflan el número 5-40% |
| Umbral `alfa > 0` en vez de `>= 250` | La sombra cuenta como imagen |
| Estirar hasta alcanzar el mínimo | El número cuadra, el detalle no; se ve blando en pantalla |
| Estirar sin anotarlo | La auditoría da por buena una pieza interpolada |
| Subir el mínimo a 1920 «por seguridad» | Se cae material de archivo insustituible |

## Relacionado

`195` · `196` · `140` · `144` · `161` · `199`
