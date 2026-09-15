# 384 — Medir el solape antes de renderizar

**Qué resuelve:** el censo completo de pisadas de un episodio sale de la tabla de eventos en **menos de un
segundo**, sin tocar ffmpeg. Renderizar para verlo cuesta entre trescientas y mil veces más. Este módulo es
el script, el coste medido de cada camino y las tres trampas que hacen que el censo mienta.

> `canales_lushows/26` ya trae un chequeo de solapes y avisa de su propio agujero: **no filtra por tiempo**.
> Esta es la versión que sí lo hace, y que además ordena la pareja por capa real y no por reloj.

---

## 1. El coste de los dos caminos, medido hoy

Sobre `ep01-lustig` (63,45 s de vídeo, 5 escenas, 61 elementos), en el equipo de Luis:

| Camino | Tiempo medido |
|---|---|
| generar el guion visual en memoria | 1,61 s |
| **medir las 96 parejas simultáneas** | **0,31 s** |
| renderizar una escena de 6,73 s / 7 elementos (caché caliente / frío) | 50,1 s / 98,3 s |
| renderizar la escena de 16,15 s / 17 elementos | 309,2 s |
| renderizar la escena de 11,53 s / 9 elementos | 215,5 s |
| **solo la grilla de fotogramas del episodio ya renderizado** | **40,3 s** |

El episodio entero está en el orden de los diez a quince minutos de render. La grilla que hay que mirar
después cuesta, ella sola, ciento treinta veces lo que el censo completo. Y cuando el fallo aparece en la
grilla hay que volver a empezar.

> **La cuenta que decide:** medir 0,31 s contra renderizar 600 s. Da igual lo bien afinado que esté el
> render: no hay versión de esto en la que renderizar para ver si hay pisadas sea razonable.

---

## 2. La doble condición, y por qué el filtro temporal no es opcional

Sin filtrar por tiempo, un episodio de 61 elementos son 1.830 parejas. Filtrando por escena, 379. Filtrando
además por vidas que se solapan, **96**. Se descarta el 95% del trabajo antes de calcular un solo
rectángulo, y —más importante— se descarta el 75% de las **alarmas**: tres de cada cuatro parejas que
comparten sitio nunca comparten pantalla.

| Episodio | Parejas todas contra todas | Dentro de la misma escena | **Simultáneas** |
|---|---|---|---|
| `ep01-lustig` (61 elem) | 1.830 | 379 | **96** |
| `episodio01` (71 elem) | 2.485 | 423 | **93** |

---

## 3. El script

```python
# pisadas.py — censo de solapes de un episodio, ANTES de renderizar.
import io, json, os, re, sys
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
EPI  = sys.argv[1]
DIR  = os.path.join(BASE, EPI); sys.path.insert(0, DIR)
from guion_visual import ESCENAS
from diccionario import es_texto
from motor import buscar                       # la MISMA busqueda que el render

PAL = json.load(io.open(os.path.join(DIR, "tiempos.json"), encoding="utf-8"))["palabras"]

_P = {}
def prop(r):                         # alto/ancho, cacheado
    if r not in _P:
        p = buscar(r)
        _P[r] = (lambda s: s[1] / float(s[0]))(Image.open(p).size) if p else None
    return _P[r]

def resolver(esc, ele):              # replica motor.py: ancla + offset + dura
    t0, t1 = esc["ini"], esc["fin"]; dur = t1 - t0
    if "ancla" in ele:
        anc = re.sub(r"[^\wáéíóúüñÁÉÍÓÚÜÑ]", "", ele["ancla"]).lower()
        cand = [p for p in PAL if p["limpia"] == anc and t0 - 0.6 <= p["t"] <= t1]
        base = cand[min(ele.get("ancla_n", 0), len(cand) - 1)]["t"] if cand else t0
    else:
        base = t0 + ele.get("desde", 0)
    e0 = max(t0, base + ele.get("offset", 0)) - t0
    return t0 + e0, t0 + min(dur, e0 + ele.get("dura", 2.0))

def coord(x, W=1920.0, H=1080.0):    # se PARSEA, no se evalua (ver seccion 5)
    m = re.match(r"^\s*([WH])\s*\*\s*([\d.]+)\s*$", str(x))
    if m:
        return (W if m.group(1) == "W" else H) * float(m.group(2))
    try:    return float(x)
    except (TypeError, ValueError): return None

def caja(e):
    x, y = coord(e.get("x", 0)), coord(e.get("y", 0)); pr = prop(e["r"])
    if x is None or y is None or pr is None:
        return None
    a = e.get("w", 400)
    return (x, y, x + a, y + a * pr)

# pisa(a, b) = fraccion de 'a' que queda debajo de 'b'. Es la de diccionario.py:365,
# citada entera en `380` §3.
from diccionario import pisa

pisadas = []
for esc in ESCENAS:
    vivos = []
    for k, ele in enumerate(esc["elementos"]):      # k = LA CAPA. El mayor, encima.
        a, b = resolver(esc, ele); c = caja(ele)
        if c and b > a:
            vivos.append((k, a, b, ele, c))
    for i in range(len(vivos)):
        for j in range(i + 1, len(vivos)):
            k1, a1, b1, e1, c1 = vivos[i]; k2, a2, b2, e2, c2 = vivos[j]
            co = min(b1, b2) - max(a1, a2)
            if co <= 0:
                continue                            # comparten sitio, no pantalla
            baj, cb, arr = (e1, c1, e2) if k2 > k1 else (e2, c2, e1)
            v = pisa(cb, c1 if k2 <= k1 else c2)
            if v > 0:
                pisadas.append((v, v * co, baj["r"], arr["r"], co, esc["id"],
                                es_texto(baj["r"])))
pisadas.sort(reverse=True)
print("parejas simultaneas con contacto: %d · pisada-segundos %.2f"
      % (len(pisadas), sum(p[1] for p in pisadas)))
for v, ps, bajo, arriba, co, e, txt in pisadas[:15]:
    print("  %5.1f%%  %-22s bajo %-22s %5.2f s  %-9s%s"
          % (v * 100, bajo, arriba, co, e, "  [TEXTO]" if txt else ""))
```

---

## 4. Qué se mira en la salida, por orden de urgencia

```
parejas simultaneas con contacto: 31 · pisada-segundos 3.33
   28.0%  casilla_nombre         bajo sin_padre              1.07 s  muerte
   27.9%  chatarreria            bajo calle_paris            1.79 s  torre
```

1. **Cualquier fila con `[TEXTO]` por encima del 5%.** Es defecto, no criterio (`383`).
2. **Cualquier fila por encima del 55% que dure más de 0,6 s.** Es un enterrado (`386`).
3. **El total de pisada-segundos**, contra la versión anterior. Es el único número que dice si la cosa va a
   mejor.
4. **La franja 2–6%**, el mordisco: ni limpio ni apilado, se lee como error de render
   (`canales_lushows/26`).

---

## 5. Tres trampas del censo

**a) Evaluar las expresiones de posición.** `canales_lushows/26` usa `eval` sobre `"W*0.5-w/2"` y funciona
mientras nadie meta un condicional a mano. `auditar.py` hace lo contrario y es lo correcto: las expresiones
son nuestras y tienen forma fija, así que **se parsean con una expresión regular**. Si el parseo falla,
devuelve `None` y el elemento se reporta como no medible en vez de colarse con coordenada cero.

**b) Buscar el fichero de otra manera que el motor.** En `auditar.py` llegó a haber **cuatro** copias de
«buscar el recurso», y la más estrecha devolvía superficie cero para los `.jpg` de archivo: elementos que
sí salían en pantalla contaban como área nula. Una sola función `hallar()`, con el mismo orden de carpetas
que `motor.buscar()`, o el censo mide un episodio que no existe.

**c) Medir una generación distinta de la que se va a renderizar.** El guion visual **se genera cada vez que
se importa**. Si entre medir y renderizar cambia el diccionario, el vocabulario o el banco de recursos, el
censo es de otro episodio. Me pasó hoy: tocaron `diccionario.py` a media sesión y el censo de `episodio01`
pasó de 87 a 93 parejas simultáneas sin que yo tocara nada. **Se mide y se renderiza en la misma pasada, o
se guarda la huella del código junto al censo.**

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Renderizar para ver si hay pisadas | 600 s contra 0,31 s, y hay que volver a renderizar tras arreglar |
| No cruzar el solape con las vidas | 1.830 parejas en vez de 96, y tres de cada cuatro alarmas falsas |
| Ordenar la pareja por tiempo en vez de por índice de lista | Se mide al revés en un 30% de los casos (`386`) |
| `eval` sobre las expresiones de posición | Un `if(...)` escrito a mano y el chequeo deja de servir en silencio |
| Una función de búsqueda distinta de la del motor | Elementos reales con superficie cero |
| No fijar el lienzo al mismo que usa el motor | Todas las coordenadas `W*…`/`H*…` salen corridas |
| Medir hoy y renderizar mañana | El guion se regenera: es otro episodio |
| Mirar solo el máximo y no los pisada-segundos | Una pisada del 20% durante 3,16 s no aparece (`385`) |

## Relacionado

`380` qué es pisar en números · `381` el área que importa · `385` la pisada que dura y la que pasa ·
`386` el elemento enterrado · `388` informar una pisada · `389` errores de medición ·
`133` verificación automática · `108` ffmpeg análisis y medición ·
`canales_lushows/26` el chequeo sin filtro temporal · `canales_lushows/140` medir antes de renderizar
