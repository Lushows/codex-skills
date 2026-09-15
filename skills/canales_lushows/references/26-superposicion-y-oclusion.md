# 26 · Superposición y oclusión

**Qué resuelve:** dos recortes se tocan y no se sabe si es una decisión o un descuido.
La oclusión es la señal de profundidad más fuerte que existe y, en un canal de
documentales, además dice quién manda en la frase.

---

## Cuánto solape

Se mide sobre el **ancho del elemento más pequeño** de los dos:

| Solape | Cómo se lee |
|---|---|
| 0% con menos de 18 px de aire | Colisión: parece que faltó ajustar la posición |
| **2 - 6%** | **El peor caso.** Un mordisco: se lee como error de render |
| **8 - 18%** | **Correcto.** Apilado a propósito, papel sobre papel |
| 19 - 38% | Agresivo. Vale para titulares apilados y para tapar a alguien a propósito |
| más del 40% | Se desperdicia material: el de abajo ya no aporta |

La franja del 2 al 6% es la que sale sola cuando se coloca a ojo. Con la retícula de
`20` no aparece: o van en columnas distintas (aire de 36 px) o se apilan a propósito.

## Quién tapa a quién

`motor.py` encadena los overlays en el orden de la lista, así que **el último de
`elementos` queda encima**. No hay campo de capa: el orden ES la capa.

| Encima va | Por qué |
|---|---|
| El que sostiene la frase que se oye | Regla del canal: nada tapa lo importante |
| Lo nuevo sobre lo viejo | Un recorte que entra empujando cuenta un avance |
| El documento sobre la persona | El papel es el que manda en este canal |
| El plano más cercano (`22`) | Coherencia con el desenfoque y la deriva |

## La oclusión cuenta la historia

Esto es lo que separa un collage compuesto de un montón de imágenes apiladas. Cada
combinación dice algo, y hay que elegirla, no heredarla del orden en que se escribió la
tabla:

| Disposición | Qué cuenta |
|---|---|
| Acta judicial tapando media cara | La identidad queda enterrada bajo el expediente |
| Retrato tapando el edificio de la empresa | La persona es más grande que lo que construyó |
| Cifra grande tapando una esquina del retrato | El dinero por delante de quien lo movió |
| Recorte nuevo entrando **por encima** del anterior | Sustitución: el segundo desplaza al primero |
| Recorte nuevo entrando **por debajo** | Acumulación: se suman, no se sustituyen |
| Sello rojo sobre un documento | Sentencia: cierra el asunto |

La pareja entrar-por-encima / entrar-por-debajo es la más útil y la que más se olvida.
Para "por debajo" hay que declarar el nuevo **antes** en la lista y darle el `ancla`
más tardío — el orden de la lista y el orden temporal no tienen por qué coincidir.

```python
"elementos": [
    {"r": "acta",     "ancla": "sentencia", "offset": -0.15, "dura": 2.6,   # entra DESPUES
     "x": "W*0.44-w/2", "y": "H*0.56-h/2", "w": 820, "entrada": "abajo", "rot": 2.2},
    {"r": "chapo_us", "ancla": "hombre",    "offset": -0.15, "dura": 3.8,   # entra ANTES
     "x": "W*0.36-w/2", "y": "H*0.42-h/2", "w": 640, "entrada": "izq",  "rot": -1.6},
]
# el acta aparece despues pero queda DEBAJO del retrato: se acumula, no sustituye
```

## Comprobar solapes antes de renderizar

Se calcula sobre la tabla, sin renderizar nada. Solo importan las parejas que están
vivas **a la vez**:

```python
import os
from PIL import Image
from guion_visual import ESCENAS
from motor import buscar

def caja(ele, W=1920, H=1080):
    im = Image.open(buscar(ele["r"]))
    w = ele.get("w", 400)
    h = int(im.height * w / im.width)
    ctx = {"W": W, "H": H, "w": w, "h": h}
    x = int(eval(ele["x"], {"__builtins__": {}}, ctx))
    y = int(eval(ele["y"], {"__builtins__": {}}, ctx))
    return x, y, w, h

def solape(a, b):
    ax, ay, aw, ah = a; bx, by, bw, bh = b
    ix = max(0, min(ax+aw, bx+bw) - max(ax, bx))
    iy = max(0, min(ay+ah, by+bh) - max(ay, by))
    return (ix * iy) / min(aw*ah, bw*bh)      # fraccion del MAS PEQUENO

for esc in ESCENAS:
    els = esc.get("elementos", [])
    for i, a in enumerate(els):
        for b in els[i+1:]:
            s = solape(caja(a), caja(b))
            if 0.02 <= s <= 0.06:
                print(f"  ! mordisco {s:.0%}  {esc['id']}: {a['r']} / {b['r']}")
```

`eval` funciona porque la tabla guarda las expresiones limpias (`W*0.5-w/2`): la
envoltura de `entrada` y `deriva` la añade el motor después. Si alguien mete un `if(...)`
a mano en el `x`, este chequeo deja de servir — otra razón para no hacerlo.

⚠️ El chequeo **no** filtra por tiempo. Para que sirva de verdad hay que cruzarlo con
las vidas (`ancla` + `offset` + `dura`) resueltas contra `tiempos.json`: dos elementos
que se solapan al 60% pero nunca coinciden en pantalla no son un problema.

## Lo que nunca se tapa

- El elemento que sostiene la frase que se está oyendo.
- Una **cifra** mientras la voz la dice. Ni una esquina.
- Un **rótulo** (`43`): si algo lo tapa, el objeto se queda sin explicar y pasa a ser
  ruido.
- Los ojos de un retrato, salvo que la oclusión sea justo lo que se quiere contar.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Solape del 2-6% | Mordisco: se lee como error de render |
| Orden de lista heredado del orden en que se escribió | La oclusión cuenta algo que nadie decidió |
| Tapar una cifra mientras se dice | La información se pierde justo en su momento |
| Tapar un rótulo | El objeto se queda sin explicar |
| Solape mayor del 40% | Se paga el recorte de abajo y no se ve |
| Suponer que el orden temporal es el orden de capas | Son independientes: hay que declararlos aparte |

## Relacionado

`21` peso visual y jerarquía · `22` profundidad por capas · `24` agrupar y separar ·
`14` encadenar elementos · `43` rótulos y etiquetas
