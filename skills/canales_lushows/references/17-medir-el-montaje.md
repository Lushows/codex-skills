# 17 · Medir el montaje

**Qué resuelve:** discutir si un episodio "va lento" mirándolo. No se opina: se mide
**antes de renderizar**, porque el dato está ya en `guion_visual.py` y `tiempos.json`.

---

## Qué mide y contra qué

| Métrica | Meta | Qué delata si falla |
|---|---|---|
| **eventos/min** | ≥ 44 | Falta material, o está mal repartido |
| **huecos** | 0 tramos ≥ 0,40 s | Elementos agrupados, colas de escena vacías (`11`) |
| **simultaneidad media** | ≥ 2,0 | Pase de diapositivas en vez de collage (`12`) |
| **duración media** | 1,6-2,4 s | Debajo: parpadeo. Encima: planos muertos (`13`) |
| **anclas huérfanas** | 0 | El motor tira el elemento al inicio de escena, sin avisar |

Cuenta como evento la entrada de un elemento, un corte de escena y una salida que deja
el cuadro sin recambio en ±0,25 s (`10`). **Las métricas se leen juntas.** El piloto mide 67,4 eventos/min —muy por encima de la
meta— y aun así se ve pobre: simultaneidad 1,12 y 19,3% del episodio con fondo solo.
Eventos/min alto con simultaneidad baja significa relevos secos, no capas.

## El script

```python
#!/usr/bin/env python3
"""auditar.py - mide el montaje ANTES de renderizar.   python auditar.py [carpeta]"""
import importlib.util, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
FPS, HUECO_MIN = 25, 0.40
META = {"ev_min": 44.0, "simul": 2.0, "dur_min": 1.6, "dur_max": 2.4}
def cargar(ruta, nombre="guion_visual"):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
def vidas(escenas, palabras):
    """[(t0,t1,escena,recurso)] absoluto. Resuelve las anclas igual que motor.py:
    si la palabra no aparece, el elemento cae al inicio de la escena."""
    out, huerfanas = [], []
    for esc in escenas:
        t0, t1 = esc["ini"], esc["fin"]
        for ele in esc.get("elementos", []):
            if "ancla" in ele:
                anc = re.sub(r"[^\wáéíóúüñÁÉÍÓÚÜÑ]", "", ele["ancla"]).lower()
                cand = [p for p in palabras if p["limpia"] == anc and t0-0.6 <= p["t"] <= t1]
                if not cand: huerfanas.append((esc["id"], ele["ancla"], ele["r"]))
                base = cand[0]["t"] if cand else t0
            else: base = t0 + ele.get("desde", 0.0)
            e0 = max(t0, base + ele.get("offset", 0.0))
            e1 = min(t1, e0 + ele.get("dura", 2.0))
            if e1 > e0: out.append((e0, e1, esc["id"], ele["r"]))
    return sorted(out), huerfanas
def huecos(iv, total, descansos=()):
    fus, libres, cursor = [], [], 0.0
    for a, b in sorted((v[0], v[1]) for v in iv):
        if fus and a <= fus[-1][1]: fus[-1][1] = max(fus[-1][1], b)
        else: fus.append([a, b])
    for a, b in fus:
        if a - cursor >= HUECO_MIN: libres.append((cursor, a))
        cursor = max(cursor, b)
    if total - cursor >= HUECO_MIN: libres.append((cursor, total))
    return [(a, b) for a, b in libres
            if not any(a >= d0-0.05 and b <= d1+0.05 for d0, d1 in descansos)]
def simul(iv, ini, fin):
    """Media de elementos vivos y reparto del tiempo, muestreado a FPS."""
    n = max(1, int((fin - ini) * FPS)); rep = {}; suma = 0
    for k in range(n):
        c = sum(1 for a, b, *_ in iv if a <= ini + (k + .5) / FPS < b)
        rep[c] = rep.get(c, 0) + 1; suma += c
    return suma / n, {k: v / n * 100 for k, v in sorted(rep.items())}
def salidas(iv, universo=None):
    """Una salida es evento solo si el cuadro no recibe nada en +-0,25 s."""
    ini = [a for a, *_ in (iv if universo is None else universo)]
    return sum(1 for _, b, *_ in iv if not any(abs(a - b) <= 0.25 for a in ini))
def main():
    proy = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    gv = cargar(os.path.join(proy, "guion_visual.py"))
    with open(os.path.join(proy, "audio", "tiempos.json"), encoding="utf-8") as f:
        palabras = json.load(f)["palabras"]
    esc_l, desc = gv.ESCENAS, getattr(gv, "DESCANSOS", [])
    total = max(e["fin"] for e in esc_l)
    iv, huerf = vidas(esc_l, palabras)
    hu = huecos(iv, total, desc); sm, rep = simul(iv, 0.0, total)
    dm = sum(b - a for a, b, *_ in iv) / len(iv)
    cortes, sal = len(esc_l) - 1, salidas(iv)
    ev = cortes + len(iv) + sal; evm = ev / total * 60
    seg = sum(b - a for a, b in hu); ok = lambda c: "OK" if c else "FLOJO"
    print(f"\nEPISODIO {total:.2f}s · {len(esc_l)} escenas · {len(iv)} elementos\n" + "="*62)
    print(f"eventos        {ev:>7}   {len(iv)} entradas + {cortes} cortes + {sal} salidas")
    print(f"eventos/min    {evm:>7.1f}   meta >={META['ev_min']}   {ok(evm >= META['ev_min'])}")
    print(f"simultaneidad  {sm:>7.2f}   meta >={META['simul']}    {ok(sm >= META['simul'])}")
    print(f"duracion media {dm:>7.2f}s  meta {META['dur_min']}-{META['dur_max']} "
          f"{ok(META['dur_min'] <= dm <= META['dur_max'])}")
    print(f"huecos         {len(hu):>7}   {seg:.1f}s = {seg/total*100:.0f}% del episodio"
          f"   {ok(not hu)}\n\nreparto de simultaneidad")
    for k, v in rep.items():
        print(f"  {k} elem {v:5.1f}% {'#'*int(v/2)}{'   <-- fondo solo' if k == 0 else ''}")
    for a, b in hu:
        e = next((x["id"] for x in esc_l if x["ini"] <= a < x["fin"]), "?")
        print(f"HUECO  {a:6.2f}-{b:6.2f}  {b-a:4.2f}s  escena '{e}'")
    for e, a, r in huerf:
        print(f"ANCLA HUERFANA  escena '{e}'  '{a}'  ({r}) -> cae al inicio de escena")
    print(f"\n  {'escena':<12}{'dur':>6}{'elem':>6}{'ev/min':>8}{'simul':>7}{'huecos':>7}")
    for e in esc_l:
        t0, t1 = e["ini"], e["fin"]; sub = [v for v in iv if t0 <= v[0] < t1]
        s, _ = simul(sub, t0, t1); n = len(sub) + 1 + salidas(sub, iv)
        print(f"  {e['id']:<12}{t1-t0:6.2f}{len(sub):6}{n/(t1-t0)*60:8.1f}{s:7.2f}"
              f"{sum(1 for a, b in hu if t0 <= a < t1):7}")
    fallos = (evm < META["ev_min"]) + bool(hu) + (sm < META["simul"]) + bool(huerf)
    print("\n" + ("APTO PARA RENDER" if not fallos else f"{fallos} criterios sin cumplir"))
    return 1 if fallos else 0
if __name__ == "__main__":
    sys.exit(main())
```

Se guarda como `auditar.py` en la raíz del episodio; devuelve **código de salida 1** si
algo falla (`python auditar.py && python motor.py`). Los módulos `11` y `12` importan
de aquí `cargar`, `vidas` y `huecos`.

## Orden de corrección

Cada paso arregla parte del siguiente; saltárselo obliga a medir sobre datos falsos.

1. **Anclas huérfanas** (`14`): hasta que no quede ninguna, las otras cuatro métricas
   describen un montaje que no es el que se va a renderizar.
2. **Huecos** (`11`), los de más de 1 s primero: un hueco de 4,58 s en una escena de
   5,44 s no es un hueco, es una escena sin guion visual, y se rehace entera.
3. **Simultaneidad** (`12`): un suelo por escena y un rótulo por principal.
4. **Duración media** (`13`), sólo si sigue fuera de rango tras los tres anteriores.
5. **Eventos/min**: casi nunca hay que tocarlo, sube solo al arreglar 2 y 3.

## Las dos métricas que faltaban: superficie y reparto

Las cinco de arriba miden **presencia**. Se puede pasarlas todas y tener una pantalla
vacía, porque *«hay un elemento»* no es *«el cuadro está lleno»*.

**Medido en el episodio 01:** con 0 huecos, simultaneidad 2,04 y 47,9 eventos/min, la
grilla de fotogramas mostraba los recortes flotando perdidos sobre el fondo. El número
que lo explicaba: **el 30% del episodio tenía menos del 14% del lienzo cubierto.**

### Cobertura

Superficie ocupada en cada instante, en tanto por uno del lienzo. Se calcula sin
renderizar: el ancho está en la tabla y la proporción sale del PNG.

```python
def area(recurso, ancho):
    from PIL import Image
    w, h = Image.open(ruta(recurso)).size
    return (ancho * (ancho * h / w)) / (1920.0 * 1080.0)
```

| Métrica | Objetivo |
|---|---|
| cobertura media | 30-45% |
| tramos con menos del 14% cubierto | ninguno de más de 0,8 s |

⚠️ **La media engaña**: sube con dos láminas grandes y deja medio episodio pelado. Lo
que hay que subir es el SUELO. Por eso el auditor lista los tramos flojos con su pico,
igual que lista los huecos.

⚠️ **El texto no llena.** Los PNG de texto son anchos y bajos (proporción 0,20-0,29):
un titular a 1500 px de ancho no pasa del **23% del lienzo**. Un tramo sostenido sólo
por texto va a salir flojo siempre.

### Reparto por recuadros

Cobertura del 44% y aun así desordenado, porque todo se apila arriba. Una rejilla 3×3
sobre el lienzo, contando el tiempo que cada recuadro tiene algo encima (≥30% del
recuadro cubierto):

```
        izquierda   centro    derecha
arriba      28%       53%       48%
medio       46%       71%       60%
abajo       39%       40%       24%
```

- **Menos del 12% = recuadro muerto:** un agujero fijo en la composición. El ojo lo
  detecta aunque el episodio tenga elementos de sobra
- La banda baja útil **acaba en `H*0.72`**: por debajo pinta YouTube la barra de
  progreso. Colocar rótulos en `H*0.78-0.86` es regalarlos
- Si una columna entera va por debajo del 35%, el episodio se ve escorado

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Medir después de renderizar | Se pagan 6-10 min de render por cada iteración |
| Perseguir eventos/min a solas | Se llega a 67 con simultaneidad 1,1 y sigue pobre |
| Dar por bueno un montaje con 0 huecos | Presencia no es superficie: mirar cobertura y reparto |
| Mirar la cobertura media y no el suelo | Dos láminas grandes tapan medio episodio pelado |
| Cambiar `META` para que el episodio pase | El umbral es el oficio; lo que se mueve es el montaje |
| Auditar con un `tiempos.json` viejo | Si la voz cambió, cada ancla apunta a otro segundo |

## Relacionado

`10` densidad de eventos · `11` el hueco prohibido · `12` capas simultáneas ·
`16` el plano de descanso · `18` densidad por tipo de bloque · `19` errores de ritmo
