# 12 · Capas simultáneas

**Qué resuelve:** el montaje va rápido pero se siente pobre, porque sólo vive un
elemento a la vez: el ojo lo lee en medio segundo y se queda esperando.

---

## La medida

**Simultaneidad = número medio de elementos vivos en pantalla**, muestreada fotograma a
fotograma. No es lo mismo que eventos por minuto: el piloto mide 67 eventos/min con
simultaneidad 1,12 — treinta relevos secos, no un collage. Por eso se ve pobre.

| Simultaneidad media | Cómo se ve |
|---|---|
| menos de 1,0 | hay huecos: el cuadro se vacía |
| 1,0 - 1,5 | pase de diapositivas: uno entra, uno sale |
| **2,0 - 3,0** | **el objetivo**: el ojo recorre y encuentra |
| 3,0 - 4,0 | denso; sólo en el gancho y en los picos |
| más de 4,0 | ruido: todo compite y nada se lee |

Reparto de tiempo objetivo: 0 elementos **0%** · 1 elemento ≤25% · 2-3 ≥60% · 4 ≤15%.

## Los cuatro papeles

En todo momento hay como mucho **un principal**. Lo demás acompaña.

| Papel | Área | Duración | Qué es | A la vez |
|---|---|---|---|---|
| **Principal** | 22-40% | 1,8-3,0 s | Lo que sostiene la frase: retrato, documento, cifra | **1** |
| **Apoyo** | 8-18% | 1,2-2,2 s | Contexto: el objeto, el plano, la segunda foto | 1-2 |
| **Acento** | bajo 6% | 0,6-1,0 s | Sello, tachado, flecha, alerta, subrayado | 0-1 |
| **Suelo** | 5-15%, a un borde | toda la escena | Ficha de caso, chapa, clasificación | 0-1 |

Sobre lienzo 1920, un `w` de 620 px es un principal; 400 px, un apoyo; 200 px, un
acento. **El ancho declarado decide el papel**, no la intención de quien monta.

## Cómo se solapan sin taparse

- **Nunca dos principales.** Si dos elementos pasan de 500 px de ancho y viven a la vez,
  uno baja a 380-420 px o se retrasa 0,4 s.
- **Tolerancia de pisado: 18% del área del más pequeño.** Por debajo se lee como
  collage (papeles apilados, que es lo que se busca); por encima, como que algo tapa.
- **El principal es intocable:** nadie invade su rectángulo más del 18%, ni un acento.
- **El orden de la lista es el orden de apilado.** El último declarado va arriba, así
  que un acento se declara siempre después de aquello que subraya.
- **Tercios distintos:** dos elementos vivos a la vez no comparten tercio vertical
  salvo que uno sea acento del otro.

## El comprobador

Compara sólo pares vivos **a la vez**: comparar todos los pares de la escena da falsos
positivos con las sustituciones, que comparten posición a propósito.

```python
# solape.py - avisa de elementos vivos a la vez que se tapan entre si.
import json, os, sys
from PIL import Image
from auditar import cargar, vidas          # modulo 17
W, H, LIM = 1920, 1080, 0.18
BASE = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")

def buscar(r):
    for d in ("recortes", "recursos", "render", "archivo"):
        for e in (".png", ".jpg", ".webp"):
            p = os.path.join(BASE, d, r + e)
            if os.path.exists(p): return p

def caja(ele):                              # rectangulo real sobre lienzo 1920x1080
    ruta = buscar(ele["r"])
    if not ruta: return None
    iw, ih = Image.open(ruta).size
    an = ele.get("w", 400); al = an * ih / iw
    x = eval(ele["x"], {"W": W, "H": H}); y = eval(ele["y"], {"W": W, "H": H})
    return (x, y, x + an, y + al)

def corte(a, b):                            # fraccion pisada del MAS PEQUENO
    dx = min(a[2], b[2]) - max(a[0], b[0]); dy = min(a[3], b[3]) - max(a[1], b[1])
    if dx <= 0 or dy <= 0: return 0.0
    menor = min((a[2]-a[0])*(a[3]-a[1]), (b[2]-b[0])*(b[3]-b[1]))
    return dx * dy / menor

gv = cargar(os.path.join(BASE, "guion_visual.py"))
with open(os.path.join(BASE, "audio", "tiempos.json"), encoding="utf-8") as f:
    iv, _ = vidas(gv.ESCENAS, json.load(f)["palabras"])
vida = {}
for a, b, esc, r in iv: vida.setdefault((esc, r), []).append((a, b))

for esc in gv.ESCENAS:
    els = esc.get("elementos", [])
    for i, A in enumerate(els):
        for B in els[i+1:]:
            va = vida.get((esc["id"], A["r"]), []); vb = vida.get((esc["id"], B["r"]), [])
            junto = max((min(a1, b1) - max(a0, b0)
                         for a0, a1 in va for b0, b1 in vb), default=0)
            ca, cb = (caja(A), caja(B)) if junto > 0.15 else (None, None)
            if ca and cb and corte(ca, cb) > LIM:
                print(f"{esc['id']:<10}{A['r']:<16}/ {B['r']:<16}"
                      f"{junto:.1f}s juntos, se pisan {corte(ca, cb)*100:3.0f}%")
```

Salida real sobre el piloto:
```
gancho    desaparecido / planeta_cara   0.9s juntos, se pisan 100%
penal     planta       / alerta         1.3s juntos, se pisan  96%
cifra     dinero_real  / con_cifuentes  1.6s juntos, se pisan  24%
```

Los dos primeros son fallos: un recorte enterrado bajo otro casi un segundo es material
tirado. El tercero, al 24%, está en el límite y se deja.

## Cómo se sube la simultaneidad de 1,1 a 2,2

Sin material nuevo y en este orden: **un suelo por escena** (+1,00 de golpe), **un
rótulo por cada principal** con su misma vida menos 0,3 s (+0,35) y **alargar los
apoyos 0,4 s** hasta empalmar con la entrada del siguiente (+0,20). Lo que **no**
funciona es meter más elementos cortos: sube eventos/min y deja la simultaneidad
igual, que es el estado en que está el piloto hoy.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dos elementos de más de 500 px vivos a la vez | Compiten; el espectador no sabe qué mirar y no mira nada |
| Acento declarado antes del elemento que subraya | Queda debajo: el sello no se ve |
| Bajar la opacidad para "que no estorbe" | Doble exposición, no collage: la opacidad es siempre 1 |

## Relacionado

`10` densidad de eventos · `11` el hueco prohibido · `13` ciclo de vida del elemento ·
`20` retícula del collage · `21` peso visual y jerarquía · `26` superposición y oclusión
