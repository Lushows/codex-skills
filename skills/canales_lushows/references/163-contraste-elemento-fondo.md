# 163 · Contraste elemento-fondo

**Qué resuelve:** un recorte puede estar en pantalla, durar sus 2,4 s, sumar superficie a
la cobertura y **no verse**, porque su luminancia es casi la del fondo. Las demás medidas
cuentan presencia; ésta cuenta visibilidad. **Caso real:** un retrato quedaba «lavado» y
parecía una marca de agua — declarado, colocado, sin solapes y sin una sola alarma.

---

## Las dos cifras

Se miden sobre el **fotograma ya compuesto**, no sobre el PNG suelto: lo que decide es la
relación con el fondo real.

| Cifra | Qué es | Qué delata |
|---|---|---|
| **`dL`** | Diferencia entre la **mediana de luminancia del cuerpo** y la del **anillo de fondo** | La masa del elemento no se separa del fondo |
| **`frac`** | Proporción de píxeles del cuerpo que se apartan **≥ 16** del nivel del fondo | Cuánta parte del elemento se lee de verdad |

Hacen falta las dos: un plano sobre papel puede tener `dL` alto y `frac` bajo (sólo se
leen las líneas); una lámina oscura sobre fondo oscuro falla las dos.

- **Cuerpo** = máscara alfa del PNG (`>= 200`) **erosionada 16 px**: así no se mide el
  borde crema ni la sombra, claros por construcción, que aprobarían cualquier cosa.
- **Anillo** = 32 px de fondo por fuera, saltando 10 px de cola de sombra. **Mediana**,
  no media: aguanta que otro elemento invada parte del anillo.
- Luminancia **Rec.709** `0,2126·R + 0,7152·G + 0,0722·B`. Promediar RGB no vale.

## El script

```python
#!/usr/bin/env python3
"""contraste.py <proyecto> <episodio> <video> - se VE cada elemento sobre su fondo?"""
import os, subprocess, sys, numpy as np
from PIL import Image, ImageFilter
FPS, W, H = 25, 1920, 1080
GAP, ANILLO, EROSION, MIN_DL, MIN_FRAC = 10, 32, 16, 16.0, 0.45

def luma(im):
    a = np.asarray(im.convert("RGB"), np.float32)
    return 0.2126*a[:,:,0] + 0.7152*a[:,:,1] + 0.0722*a[:,:,2]

def morf(m, px, filtro):                      # erosion / dilatacion solo con PIL
    im = Image.fromarray((m*255).astype(np.uint8))
    for _ in range(max(1, int(round(px/4.0)))):
        im = im.filter(filtro(9))             # size 9 = radio 4 px por pasada
    return np.asarray(im) > 127

def extraer(video, tiempos, dest):
    """UNA pasada de decodificacion para todos los fotogramas que hacen falta."""
    ns = sorted({int(round(t*FPS)) for t in tiempos})
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", video, "-vsync", "0",
                    "-vf", "select=" + "+".join(rf"eq(n\,{n})" for n in ns),
                    os.path.join(dest, "_qc_%04d.png")], check=True)
    return {n: os.path.join(dest, f"_qc_{i+1:04d}.png") for i, n in enumerate(ns)}

def medir(L, png, x, y, w, alto):
    M = GAP + ANILLO + 2                      # recortar al elemento: 2,5x mas rapido
    bx0, by0 = int(max(0, x-M)), int(max(0, y-M))
    bx1, by1 = int(min(W, x+w+M)), int(min(H, y+alto+M))
    if bx1-bx0 < 40 or by1-by0 < 40: return None
    el = Image.open(png).convert("RGBA").resize((max(1,int(w)), max(1,int(alto))), Image.LANCZOS)
    A = np.zeros((by1-by0, bx1-bx0), np.uint8)
    ox, oy = int(round(x))-bx0, int(round(y))-by0
    sx, sy, dx0, dy0 = max(0,-ox), max(0,-oy), max(0,ox), max(0,oy)
    dx1, dy1 = min(A.shape[1], ox+el.width), min(A.shape[0], oy+el.height)
    if dx1-dx0 < 24 or dy1-dy0 < 24: return None
    A[dy0:dy1, dx0:dx1] = np.asarray(el)[sy:sy+dy1-dy0, sx:sx+dx1-dx0, 3]
    Lb = L[by0:by1, bx0:bx1]
    cuerpo = morf(A >= 200, EROSION, ImageFilter.MinFilter)
    fuera  = morf(A >= 8,   GAP,     ImageFilter.MaxFilter)
    anillo = morf(fuera, ANILLO, ImageFilter.MaxFilter) & ~fuera
    if cuerpo.sum() < 400 or anillo.sum() < 400: return None
    Lf, Le = float(np.median(Lb[anillo])), float(np.median(Lb[cuerpo]))
    return Le, Lf, abs(Le-Lf), float((np.abs(Lb[cuerpo]-Lf) >= 16).mean())

def main():
    proy, epi, video = sys.argv[1], sys.argv[2], sys.argv[3]
    tmp = os.path.join(proy, epi, "salida"); sys.argv = ["x", epi]
    sys.path.insert(0, proy); sys.path.insert(0, os.path.join(proy, epi))
    import motor, diccionario
    from importlib import import_module
    gv = import_module("guion_visual")
    if os.path.getmtime(os.path.join(proy, epi, "guion_visual.py")) > os.path.getmtime(video):
        print("  AVISO: el guion visual es MAS NUEVO que el video. Renderizar antes de medir.")
    tareas = []
    for esc in gv.ESCENAS:
        for e in esc["elementos"]:
            t0, t1 = diccionario.resolver(gv.PALABRAS, e, esc["ini"], esc["fin"])
            pr = diccionario.proporcion(e["r"])
            if t1-t0 < 0.5 or pr is None: continue
            tareas.append((e["r"], esc["id"], t0 + 0.55*(t1-t0), e["x"], e["y"], e["w"], e["w"]*pr))
    mapa, filas, cache = extraer(video, [t[2] for t in tareas], tmp), [], {}
    for r, eid, t, x, y, w, alto in sorted(tareas, key=lambda v: v[2]):
        n = int(round(t*FPS))
        if n not in cache: cache = {n: luma(Image.open(mapa[n]))}   # uno cada vez: 8 MB
        m = medir(cache[n], motor.buscar(r), x, y, w, alto)
        if m: filas.append((r, eid, t) + m)
    for p in set(mapa.values()): os.remove(p)
    for r, eid, t, Le, Lf, dl, fr in sorted(filas, key=lambda f: f[6]):
        av = "  <-- LAVADO" if (dl < MIN_DL and fr < MIN_FRAC) else ""
        print(f"{r:<22}{eid:<9}{t:6.2f}{Le:7.1f}{Lf:7.1f}{dl:7.1f}{fr:7.2f}{av}")
    print(f"n={len(filas)}  dL mediana={np.median([f[5] for f in filas]):.1f}"
          f"  frac mediana={np.median([f[6] for f in filas]):.2f}")
main()
```

## Los umbrales, y de dónde salen

Medido sobre `ep01-lustig-min1.mp4` (63,45 s · 41 elementos con vida ≥ 0,5 s): `dL`
mediana **44,9** / p10 **4,1** · `frac` mediana **0,86** / p10 **0,45**.

| Veredicto | Regla |
|---|---|
| **LAVADO** | `dL < 16` **y** `frac < 0,45` |
| Revisar | `frac < 0,45` con `dL` alto: se lee el detalle, no la masa |
| Bien | `frac ≥ 0,45` |

`0,45` es el **percentil 10 del episodio ya aprobado a ojo**: marca a los peores sin
declarar defectuoso lo que ya funciona. Se sube a **0,55** si el episodio va sobre todo a
móvil (`166`). **Coste: 4 min 3 s** el episodio entero en la máquina de 2009 — la versión
que no recorta al elemento antes de la morfología tarda **10 min 31 s**.

## Lo que encontró de verdad

Cuatro marcados: **uno era defecto real** y tres, el mismo fallo de método.

- 🔴 **`torre_esquema`** (t = 44,21 · `dL` 4,1 · `frac` 0,11). Panel azul marino sobre el
  fondo marrón oscuro del bloque. Comprobado en el fotograma: **el panel entero no se
  separa del fondo**; sólo lo sacan las líneas amarillas y el texto, el 11% de su
  superficie. En móvil desaparece. Arreglo: borde de papel crema (`25`) o aclararlo.
- ⚪ `reglamento_celda`, `aviso_falsos`, `balanza_01`: el vídeo se renderizó a las **00:12**
  y `guion_visual.py` se guardó a las **00:16**. Se medía el montaje nuevo contra el
  render viejo y las máscaras caían sobre fondo vacío. De ahí el aviso de fechas (`168`).

Cruce útil: las `balanza_*` flojas aquí son las mismas que `164` marca como ilegibles.
**Dos medidas independientes señalando la misma pieza** es la señal más fiable que da la
auditoría.

⚠️ **Un elemento tapado por otro da el mismo número que uno lavado.** Para el espectador
es correcto —no se ve— pero la causa y el arreglo son distintos. La medida dice *qué*; la
grilla (`160`) dice *por qué*. Nunca se arregla un LAVADO sin mirar antes su fotograma.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Medir sobre el PNG suelto | El fondo real lleva movimiento, viñeta y cosas encima |
| Incluir el borde crema en el cuerpo | Es claro por construcción: aprobaría cualquier cosa |
| Usar la media en vez de la mediana | Un elemento que invada el anillo desplaza el fondo |
| Muestrear al inicio de la vida del elemento | La entrada aún lo mueve: se mide fondo vacío |
| Medir un render más viejo que el guion visual | Tres de cada cuatro hallazgos serán falsos |
| Arreglar un LAVADO subiendo la opacidad | La opacidad **siempre es 1**: se toca el borde o el fondo |

## Relacionado

`160` la grilla de fotogramas · `161` auditar sobre gris · `164` legibilidad por altura ·
`166` la prueba del pulgar · `23` empatar recorte y fondo · `25` el borde de papel
