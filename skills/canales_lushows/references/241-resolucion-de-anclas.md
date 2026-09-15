# 241 · Resolución de anclas: una sola fuente

**Qué resuelve:** convertir `"ancla": "aprendiz"` en dos segundos concretos. Tres
ficheros hacen hoy esa misma cuenta y **tienen que dar el mismo número**: si el auditor
resuelve distinto que el motor, mide un episodio que nadie va a ver.

---

## La cuenta

```python
def resolver(palabras, ele, t0, t1):
    if "ancla" in ele:
        anc = limpiar(ele["ancla"])
        cand = [p for p in palabras if p["limpia"] == anc and t0 - 0.6 <= p["t"] <= t1]
        i = ele.get("ancla_n", 0)
        base = cand[min(i, len(cand) - 1)]["t"] if cand else t0
    else:
        base = t0 + ele.get("desde", 0)
    e0 = max(t0, base + ele.get("offset", 0))
    e1 = min(t1, e0 + ele.get("dura", 2.0))
    return e0, e1
```

Cuatro decisiones dentro de diez líneas, y las cuatro se pagan si se tocan:

- **`limpiar()`** quita puntuación y baja a minúscula con el mismo regex que
  `tiempos.py`: `[^\wáéíóúüñÁÉÍÓÚÜÑ]`. Si el regex del motor no es carácter por
  carácter el del transcriptor, «vendió,» no empata con «vendió» y el elemento cae al
  defecto sin avisar (`154`).
- **La ventana `t0 - 0.6`** deja que un elemento se cuelgue de una palabra dicha justo
  antes del corte de escena. Sin ese margen, toda ancla que caiga en la frontera se
  pierde.
- **`ancla_n`** elige la aparición. «vendió» sale dos veces en el bloque de la torre;
  sin decir cuál, el plano del segundo timo aterriza en el primero. Hoy la usa
  **1 elemento de 61**, y ese uno es el remate del bloque.
- **El repliegue `else t0`** es deliberado: un ancla que no existe no tumba el render,
  coloca el elemento al principio de la escena y **grita por consola**. Un ancla
  huérfana silenciosa es de los fallos que llegan al publicado (`154`).

## Tres copias de la misma cuenta

Hoy conviven `motor.render_escena()` (en línea), `diccionario.resolver()` y
`auditar.resolver()`. Comprobadas las tres sobre el episodio entero, elemento a
elemento:

```
  61 elementos · 0 discrepancias entre las tres copias de resolver()
```

Cero **hoy**. Ese es exactamente el problema: la prueba no dice que el diseño sea
bueno, dice que las tres copias todavía no han divergido. El día que alguien añada
`ancla_fin` o cambie la ventana de 0,6 s en dos de los tres sitios, el auditor aprobará
un montaje que el motor renderiza distinto y **las métricas mejorarán al medir otra
cosa**. La comprobación de arriba vale como prueba de regresión; el arreglo de verdad
es que la función viva en un sitio y los otros dos la importen.

## La trampa del nombre de módulo

`sys.modules` cachea **por nombre, no por ruta**. Dos episodios con un
`guion_visual.py` cada uno son, para Python, el mismo módulo: el primero que se importe
gana para todo el proceso.

Reproducido tal cual ocurrió:

```python
import sys
sys.argv = ['auditar.py']          # sin episodio: auditar cae en 'episodio01'
import auditar
print('auditar cargo:', auditar.EPI, '| escenas', len(auditar.ESCENAS))
sys.path.insert(0, 'ep01-lustig')
from guion_visual import ESCENAS   # 'ep01-lustig/guion_visual.py'... o no
print('mi import trae:', len(ESCENAS), 'escenas ->', [e['id'] for e in ESCENAS])
print('fichero real:', sys.modules['guion_visual'].__file__)
```

```
auditar cargo: episodio01 | escenas 6
mi import trae: 6 escenas -> ['gancho', 'pregunta', 'peso', 'maquina', 'piezas', 'remate']
fichero real: ...\piloto\episodio01\guion_visual.py
```

`sys.path.insert(0, ...)` no sirve de nada: la ruta solo se consulta cuando el módulo
**no está ya cargado**. El síntoma es cruel porque no hay error: salen escenas, salen
elementos, salen métricas. Se diagnostica una ronda entera del episodio equivocado.

Es el mismo error de forma que la caché de `escalado()` por basename (`248`): **una
clave que no contiene todo lo que determina el contenido**.

## Cargar por ruta, con nombre propio

```python
import importlib.util, os, sys

def cargar_guion(epi):
    ruta = os.path.join(epi, "guion_visual.py")
    nombre = "gv_" + os.path.basename(epi).replace("-", "_")
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[nombre] = mod
    sys.path.insert(0, os.path.abspath(epi))
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.path.pop(0)
    return mod
```

```
episodio01   6 escenas · ['gancho', 'pregunta', 'peso', 'maquina', 'piezas', 'remate']
ep01-lustig  5 escenas · ['muerte', 'oficio', 'nombre', 'torre', 'metodo']
```

Dos episodios en el mismo proceso, cada uno con su tabla. El `sys.path` se empuja solo
mientras dura la ejecución del módulo, porque `guion_visual.py` importa a su vez
`vocabulario` desde su propia carpeta y **ese** sí se resuelve por ruta.

Mientras no esté puesto, la regla de andar por casa: **un episodio por proceso, y el
episodio siempre en `sys.argv`**. Nunca `import auditar` desde una sesión interactiva
sin fijar antes el argumento.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Regex de normalización distinto del de `tiempos.py` | Anclas que no empatan y caen al defecto en silencio |
| Quitar la ventana `t0 - 0.6` | Se pierde todo elemento anclado en la frontera de escena |
| Omitir `ancla_n` con una palabra repetida | El plano aterriza en la aparición equivocada |
| Que un ancla huérfana no imprima nada | El elemento se amontona en `ini` y nadie se entera |
| `import guion_visual` con dos episodios vivos | Se audita el episodio que no es, sin un solo error |
| Cambiar la resolución en dos de los tres ficheros | El auditor aprueba un montaje que no es el renderizado |

## Relacionado

`154` anclas que caen al defecto · `155` cachés que sirven el archivo equivocado ·
`240` la tabla de eventos · `235` palabras repetidas y anclaje · `39` sincronizar gesto
y palabra · `248` pre-escalado y caché
