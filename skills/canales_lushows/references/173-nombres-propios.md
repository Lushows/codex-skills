# 173 · Nombres propios: por qué la búsqueda libre falla

**Qué resuelve:** el caso medido en el que buscar a los protagonistas por su nombre
devolvió cientos de piezas —277 en la primera pasada, 379 en el sondeo guardado del
piloto— y casi ninguna era de la historia.

---

## El fallo, medido

Buscando los nombres de Enron en Commons con `generator=search`, esto es lo que devuelve
de verdad (ejecutado 11-sep-2026, 25 resultados por término):

| Se buscaba | Commons devolvió |
|---|---|
| **Kenneth Lay** | apartaderos de carretera (*lay-by*), marineros depositando coronas (*lay a wreath*), un poema titulado *Kenneth*, y `Lam Lay Yong` |
| **Jeffrey Skilling** | `Genetic correlation results about traits, IQ and language skills`, un jugador de hockey llamado Jeffrey, un almirante llamado Jeffrey, `Francis Jeffrey, Lord Jeffrey` |
| **Arthur Andersen** | `Hans Christian Andersen by Arthur Rackham`, *Andersen's Fairy Tales* ilustrados por Arthur Szyk, `Arthur David-Andersen` (un orfebre danés), una planta neozelandesa `Hebe subalpina (Cockayne) Andersen` |
| **Sarbanes-Oxley Act** | `1916 Chicago White Sox`, `J. B. Shuck White Sox in Houston May 2015` |
| **Andrew Fastow** | ninguna pieza con su nombre; sí las actas del Congreso sobre Enron |

El buscador no busca personas: busca cadenas. `Lay`, `Skilling`, `Sox` y `Andersen` son
palabras corrientes en inglés o apellidos de otras personas, y por eso ganan.

## El coste real

El sondeo del episodio de Enron devolvió **379 piezas con licencia libre verificada**.
De esas, **solo 31 llevan en el título alguna palabra del caso**. Y de esas 31, al
mirarlas una a una, **once son del caso** y veinte son homónimos: los cuentos de Andersen,
la planta *Hebe subalpina*, una luchadora apellidada Andersen, tuberías que se estaban
*laying* en Omagh, un asfaltado en Portrush y marineros de la Armada estadounidense
recogiendo amarras.

Eso es un **3 % de acierto** sobre el material que nombra al caso.

## El parche: exigir la palabra en el título

`sondeo.py` filtra por título antes de mirar la licencia. Es un filtro barato y salva
buena parte del ruido:

```python
VACIAS = {"the", "of", "and", "in", "a", "united", "states", "new", "york"}

def relevante(titulo, termino):
    """El título tiene que contener alguna palabra distintiva de la búsqueda."""
    t = titulo.lower()
    palabras = [w for w in re.findall(r"[a-z]{3,}", termino.lower())
                if w not in VACIAS]
    if not palabras:
        return True
    return any(w in t for w in palabras)
```

**Medido, el mismo día:**

```
'Jeffrey Skilling'    25 títulos -> 19 pasan el filtro
'Arthur Andersen'     25 títulos -> 25 pasan el filtro
'Sarbanes Oxley Act'  25 títulos -> 12 pasan el filtro
'Andrew Fastow'       24 títulos ->  0 pasan el filtro
```

## Lo que el parche NO arregla

El filtro es un **OR sobre palabras sueltas**, así que basta con que aparezca el nombre
de pila para colar ruido: `File:Jeffrey Springs`, `File:Francis Jeffrey, Lord Jeffrey` y
`File:Alex Stalock and Dustin Jeffrey` lo pasan. Y con `Arthur Andersen` **pasan los 25**,
porque todos los cuentos de Hans Christian Andersen llevan "Andersen" en el título.

Un AND (exigir **todas** las palabras distintivas) sería más limpio, pero rompería casos
legítimos: `File:Ken Lay.jpg` no contiene "Kenneth". Por eso el parche se deja en OR y
**el trabajo de verdad no lo hace el filtro: lo hace la categoría.**

## La regla firme

> Para un nombre propio, la vía es **la categoría**. La búsqueda libre es, como mucho,
> una red de arrastre para ver si a alguien se le olvidó categorizar algo.

Y el corolario que más tiempo ahorra:

> **Si la categoría del nombre no existe, eso SÍ es un dato fiable: no hay imagen libre
> de esa persona en Commons.**

No es un "no encontré nada". Commons tiene categorías para personas con una sola foto
—`Category:Kenneth Lay` tiene exactamente **2 archivos**—. Que no exista la categoría de
alguien tan documentado como Jeffrey Skilling significa que nadie ha podido subir una
imagen suya con licencia libre, y no la va a haber mañana. Se decide con ese dato
(`176`).

```
Category:Kenneth Lay       files=2    subcats=0
Category:Jeffrey Skilling  NO EXISTE
Category:Andrew Fastow     NO EXISTE
```

## Cómo se escribe un término de búsqueda que sí funciona

| Mal | Bien | Por qué |
|---|---|---|
| `Kenneth Lay` | `Category:Kenneth Lay` | nombre propio → categoría |
| `Enron` a secas | `Enron Complex Houston` | añadir el lugar ancla el sentido |
| `Arthur Andersen` | `Arthur Andersen tower` / `Immeuble Andersen` | el edificio, no el apellido |
| `Sarbanes-Oxley Act` | `United States congressional hearing` | el escenario, no la ley |
| `fraude` | `ledger accounting book` | lo que se ve, no el concepto |

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Buscar personas en libre y dar el número por bueno | 379 piezas, 11 del caso |
| Leer "0 resultados" como "hay que buscar mejor" | Se pierden días; suele ser el dato definitivo |
| Endurecer el filtro a AND | Se cae `File:Ken Lay.jpg`, que sí es el retrato bueno |
| Confiar en el filtro de título para apellidos comunes | Andersen pasa el 100 % del ruido |
| No mirar los títulos uno a uno antes de escribir | Se descubre en el montaje que no hay caras |

## Relacionado

`170` · `172` · `174` · `175` · `176`
