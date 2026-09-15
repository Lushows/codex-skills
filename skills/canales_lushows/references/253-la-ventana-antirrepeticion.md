# 253 · La ventana antirrepetición

**Qué resuelve:** que la misma imagen no vuelva antes de que el ojo la haya olvidado. Es
el que más caro sale, porque falla **en silencio**: el sistema imprimía «sin
repeticiones» mientras en pantalla salía cuatro veces la misma balanza, y lo vio el dueño
del canal en un fotograma antes que ninguna métrica.

---

## La regla

Veinticinco segundos. Por debajo el ojo reconoce la figura y lee «no tienen material»;
por encima, ni se entera.

```python
recurso = max(opciones, key=lambda o: _ultima(o, t))
if _ultima(recurso, t) < 25.0:
    continue                      # hasta la mas olvidada salio hace nada
```

La misma cifra la usa el auditor (`SEPARACION_MIN = 25.0`): si el montaje colocase con un
criterio y la medida usara otro, estaría arreglando algo que nadie comprueba.

## Fallo 1 · comparaba nombres exactos

`balanza_01` y `balanza_05` son la misma figura con otro encuadre. Para la memoria eran
dos recursos distintos, cada uno con su ventana, y los dos podían salir seguidos: cuatro
balanzas en poco más de un minuto y cero avisos.

```python
def familia(r):                          # balanza_01 y balanza_05 son la MISMA imagen
    return re.sub(r"_?\d+$", "", r)

def _ultima(r, t):                       # distancia al uso mas cercano de ESTE recurso
    ts = _VISTO.get(r, []) + _VISTO.get(familia(r), [])   # o de su familia
    return min((abs(t - x) for x in ts), default=9999.0)
```

Ejecutado:

```
_anotar('balanza_01', 33.0)   ->  _VISTO: {'balanza_01': [33.0], 'balanza': [33.0]}
_ultima('balanza_05', 57.2)   =  24.2  -> pasa? False
comparando nombres exactos:      _VISTO.get('balanza_05') = None   # no sabía nada
```

24,2 segundos: fallaba por ocho décimas, y esas ocho décimas eran lo que se veía.

## Fallo 2 · la capa escrita a mano no se anotaba
`generar()` y `contrapeso()` no sabían que un recurso ya estaba puesto a mano: caso real,
`titular_prensa` a mano en 33,6 s y otra vez de contrapeso en 28,5 s.

```python
def recordar(elementos, palabras, ini, fin):   # lo que ya coloco la capa escrita a mano
    for e in elementos:
        if e["r"] in MOTIVOS:
            continue
        _anotar(e["r"], resolver(palabras, e, ini, fin)[0])
```

**El orden es la mitad del arreglo:** se anota TODA la mano, de todo el episodio, y
después se genera. Bloque a bloque no basta.

## Fallo 3 · la ventana solo miraba hacia atrás

Al ojo le da igual cuál vino antes: ve la misma imagen dos veces en catorce segundos. Por
eso `_ultima` usa `abs(t - x)`:

```
_anotar('titular_prensa', 33.7)
_ultima('titular_prensa', 23.0) = 10.7   # la mano aún no existía; la pieza ya está reservada
```

## Las cuatro versiones, medidas

`python auditar.py ep01-lustig` con cada fallo reintroducido uno a uno:

| Versión | Elem | Recursos distintos | Usos/recurso | Lo que se ve |
|---|---|---|---|---|
| nombres exactos | 63 | 55 | 1,13 | balanza 3× (33,0 · 57,2 · 61,5); dos a 4,3 s y 24,2 s |
| sin `recordar()` | 63 | 52 | 1,19 | `titular_prensa` a 10,7 s · `torre_citroen_noche` a 7,2 s |
| `recordar()` bloque a bloque | 62 | 54 | 1,15 | `columna_doble` 3× y dos a 13,8 s |
| ventana solo hacia atrás | 62 | 51 | 1,22 | las tres anteriores más `sin_padre` a 3,2 s |
| **actual** | **61** | **55** | **1,11** | sin repeticiones |

Objetivo del canal: ≤ 1,25. Ahí está lo grave: **tres de las cuatro versiones rotas lo
pasaban**. La métrica no cazaba el fallo; lo cazaba el fotograma.

## El tamaño de la ventana no se toca

Cuando faltan piezas, la tentación es bajar de 25 s. Medido:
| Ventana | Elem | Usos/recurso | Repeticiones visibles |
|---|---|---|---|
| 8 s | 63 | 1,17 | `casilla_nombre` 12,9 s · `torre_postal` 13,4 s · `columna_doble` 13,8 s |
| 12 s | 63 | 1,17 | las mismas tres |
| 18 s | 61 | 1,11 | ninguna |
| **25 s** | **61** | **1,11** | ninguna |
| 35 s | 60 | 1,09 | ninguna |

Bajar a 12 s devuelve dos elementos y tres repeticiones visibles: densidad comprada con la
única moneda que el espectador nota. Cuando faltan piezas se mira el banco (`259`).

## El precio de la familia

`familia()` recorta el sufijo numérico, y eso **también agrupa lo que no es variante**:
`balanza_01` y `balanza_05` son «balanza», pero `d_1890` es «d» y `p_3` es «p».
En `episodio01`, los rótulos `p_1`…`p_4` son cuatro carteles **distintos** con sufijo
numérico: con familia solo entra `p_1` (67 elementos), con nombres exactos entran `p_1`,
`p_2` y `p_3` (69). El sufijo numérico es una promesa —variantes de la misma imagen—; lo
que sea distinto se llama distinto.

Grieta pendiente: el auditor tiene su **propia** `familia()` (`rsplit` + `isdigit`), que
no coincide con la del diccionario (`planta_pescado2`). Hoy no cambia ningún número del
episodio 01, pero es la misma clase de desfase que causó el fallo 1.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Comparar nombres exactos | Cuatro variantes de la misma figura pasan como cuatro recursos |
| No anotar la capa escrita a mano | El generador repite lo ya puesto, cinco segundos después |
| Anotar la mano bloque a bloque | Lo que la mano usará más tarde no se ve venir |
| Mirar solo hacia atrás | Contrapesos que chocan con la mano del bloque siguiente |
| Bajar la ventana para llenar huecos | 3 repeticiones visibles a cambio de 2 elementos |
| Cosas distintas con sufijo numérico | Se bloquean entre ellas y desaparecen del montaje |
| Dos `familia()` distintas, una por fichero | El montaje evita lo que el auditor no mide |

## Relacionado

`252` · `254` · `250` · `259` · `17` · `147` · `150`
