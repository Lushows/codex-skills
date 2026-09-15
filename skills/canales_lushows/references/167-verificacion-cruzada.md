# 167 · Verificación cruzada entre módulos

**Qué resuelve:** el fallo más caro que ha tenido este proyecto. **El auditor y el motor
resolvían los recursos con listas de carpetas distintas, así que el auditor medía un
montaje diferente del que se renderizaba.** Las once medidas salían bien y el vídeo
tenía elementos que en la tabla no existían.

---

## Por qué pasa

Dos módulos replican la misma lógica porque cada uno la necesita:

- `motor.py` resuelve `recurso → ruta de archivo` para componer el fotograma.
- `diccionario.py` resuelve `recurso → proporción del PNG` para calcular el rectángulo
  que el auditor mide.

Son la misma pregunta —*¿dónde está este recurso?*— contestada en dos sitios. Mientras
contesten igual no hay problema; **el día que una de las dos listas crece, el auditor
empieza a medir un montaje imaginario y nadie se entera**, porque un recurso que el
auditor no encuentra no da error: no cuenta. No suma superficie, no solapa con nadie, no
aparece en el reparto por recuadros. **El fallo mejora las notas.**

## La discrepancia que sigue viva hoy

```python
# motor.py
PROPIAS = [os.path.join(DIR_EPI, d)
           for d in ("texto", "fx", "recortes", "render", "archivo")]
def buscar(recurso):
    carpetas = PROPIAS + [DIRS[d] for d in
                          ("texto", "fx", "recortes", "recursos", "render", "archivo")]
    for carp in carpetas:
        for ext in (".png", ".jpg", ".webp"):     # <-- TRES extensiones
            ...

# diccionario.py
def proporcion(recurso):
    carpetas = ([EPI_DIR + "/" + d for d in ("texto", "fx", "recortes", "render")]
                if EPI_DIR else [])               # <-- falta "archivo"
    for d in carpetas + ["texto", "fx", "recortes", "recursos", "render", "archivo"]:
        p = os.path.join(BASE_REC, d, recurso + ".png")   # <-- SOLO .png
```

Dos diferencias silenciosas: la lista del episodio **no incluye `archivo/`**, y
`proporcion` sólo prueba **`.png`** mientras `buscar` prueba además `.jpg` y `.webp`. Y
el material de archivo es justamente el que no es PNG:

| Carpeta | archivos | de ellos `.jpg`/`.webp` |
|---|---|---|
| `piloto/archivo` | 56 | **36** |
| `piloto/ep01-lustig/archivo` | 81 | **77** |

Reproducido, con cuatro recursos reales del banco:

```
avion              motor.buscar=recortes\avion.png             proporcion=0.616  rect=(192,324,1092,878)
barco_carga        motor.buscar=recortes\barco_carga.png       proporcion=0.478  rect=(192,324,1092,754)
billete            motor.buscar=archivo\billete.jpg            proporcion=None   rect=None
casilla_hospital   motor.buscar=ep01-lustig\recortes\...png    proporcion=0.092  rect=(192,324,1092,406)
```

**`billete` se renderiza y el auditor no lo ve.** Hoy no hay ningún `.jpg` en el guion
visual del piloto —la comprobación da 0 discrepancias sobre sus 46 recursos—, así que el
fallo está **latente**: dispara el día que alguien escriba una foto de archivo directa.

## El arnés

Se ejecuta antes del render, junto al resto de comprobaciones. No prueba que la lógica
sea correcta: prueba que **las dos copias coinciden**, que es lo único que puede
verificarse automáticamente.

```python
#!/usr/bin/env python3
"""cruzar.py <episodio> - motor.py y el auditor, ven el mismo montaje?"""
import os, sys
from importlib import import_module
BASE = os.path.dirname(os.path.abspath(__file__))

def main(epi):
    sys.argv = ["motor.py", epi]
    sys.path.insert(0, BASE); sys.path.insert(0, os.path.join(BASE, epi))
    import motor, diccionario
    diccionario.EPI_DIR = os.path.join(BASE, epi)
    gv = import_module("guion_visual")
    recursos = sorted({e["r"] for s in gv.ESCENAS for e in s.get("elementos", [])})
    malos = []
    for r in recursos:
        try: ruta = motor.buscar(r)
        except FileNotFoundError: ruta = None
        pr = diccionario.proporcion(r)
        if (ruta is None) != (pr is None):          # uno lo ve y el otro no
            malos.append((r, ruta, pr))
        elif ruta and pr and not ruta.lower().endswith(".png"):
            malos.append((r, ruta, pr))             # proporcion leyo OTRO archivo
    print(f"{len(recursos)} recursos en el guion visual de {epi}")
    for r, ruta, pr in malos:
        print(f"  DISCREPANCIA {r:<22} "
              f"motor={os.path.relpath(ruta, BASE) if ruta else 'NO'} proporcion={pr}")
    print(f"{len(malos)} discrepancias")
    return 1 if malos else 0

sys.exit(main(sys.argv[1]))
```

## Cómo se arregla de verdad

El arnés avisa; **la cura es que la lógica viva en un solo sitio**. Ya se aplicó una vez
en este proyecto: `resolver()` —en qué segundo entra y sale cada elemento— vive sólo en
`diccionario.py`, con su motivo escrito en el propio docstring: *«es la misma cuenta que
hace motor.py: si vive en dos sitios se desincroniza, así que vive aquí y los demás la
importan»*. `buscar` todavía no ha recibido ese trato; mientras tanto, el arnés es la
red.

## La regla general

| Señal de que hace falta cruzar | Ejemplo en este proyecto |
|---|---|
| Una **constante duplicada** en dos módulos | `FPS`, `W`, `H`, la lista de carpetas, las extensiones |
| Dos módulos que **derivan el mismo valor** por caminos distintos | el rectángulo de un elemento: uno lo pinta, otro lo mide |
| Un **generador** y un **validador** del mismo formato | `guion_visual.py` genera, `auditar.py` valida |
| Un módulo que **cachea** lo que otro lee del disco | `_PROP`, `_ESCALADOS` (`155`) |

Prueba mínima de cualquier cruce: **alimentar a las dos copias con el mismo caso límite**
—un `.jpg`, un recurso que no existe, un nombre con tilde— y exigir que contesten lo
mismo, aunque contesten mal las dos.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Copiar una lista de carpetas «para que el auditor también la tenga» | Nace la segunda copia que se va a desincronizar |
| Añadir una extensión sólo donde se necesita hoy | Es exactamente cómo apareció la discrepancia de `.jpg` |
| Comprobar el cruce sólo con los recursos del episodio actual | Da 0 y el fallo sigue latente: hay que probar el caso límite a mano |
| Confiar en que «si falta, dará error» | Un recurso que el auditor no encuentra **sube** las notas |
| Arreglar el arnés en vez de la duplicación | El arnés es la red, no la cura |

## Relacionado

`168` reproducir antes de afirmar · `169` el informe de auditoría · `156` recursos que
no existen y mejoran las notas · `155` cachés que sirven el archivo equivocado ·
`17` medir el montaje
