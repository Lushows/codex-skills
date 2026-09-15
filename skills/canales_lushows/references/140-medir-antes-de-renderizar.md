# 140 · Medir antes de renderizar

**Qué resuelve:** iterar mirando el vídeo. Un render son 15–25 minutos en el i7 de 2009;
la tabla de eventos ya contiene la respuesta y se lee en 1,4 segundos.

---

## El dato ya está escrito

Un episodio de este canal no es material rodado: es una **tabla**. `guion_visual.py`
declara escenas y elementos (`r`, `x`, `y`, `w`, `ancla`, `dura`) y `tiempos.json` dice
en qué segundo cae cada palabra de la locución. Con esas dos cosas se conoce, sin pintar
un solo píxel:

| Se sabe | De dónde sale |
|---|---|
| Cuándo entra y sale cada elemento | `resolver()` sobre `ancla` / `desde` / `offset` / `dura` |
| Dónde cae en el lienzo | `x`, `y`, `w` + proporción del PNG (`PIL.Image.open().size`) |
| Cuánta superficie ocupa | ancho × (ancho·h/w) ÷ (1920·1080) |
| Qué tapa a qué | intersección de los dos rectángulos |
| Qué dice cada pieza de texto | el HTML fuente, antes de convertirse en PNG |

Es decir: **todo menos el color y la textura**. Lo que se mide es la arquitectura del
montaje, y ahí es donde falla un episodio flojo.

## La cuenta de por qué importa

Ciclo "renderizar y mirar" frente a ciclo "auditar y corregir":

| | Render | Auditoría |
|---|---|---|
| Coste por vuelta | 15–25 min | ~1,4 s |
| Vueltas en una tarde de 4 h | 10–16 | miles |
| Qué se ve | el resultado | la causa, con segundo y nombre de recurso |

Seis correcciones de montaje mirando el vídeo son **entre 1,5 y 2,5 horas de máquina**
en la que no se puede hacer nada más. Las mismas seis correcciones con el auditor caben
en un café. Y el auditor no sólo dice "va flojo": dice `46.05 - 46.70 (0.65 s) torre
"volvió"`, que es el sitio exacto donde falta un elemento.

## Cómo se encadena

El auditor se ejecuta **siempre** antes del motor, nunca después:

```bash
cd piloto
python auditar.py ep01-lustig && python motor.py ep01-lustig
```

Salida real del episodio 01 (Lustig, 63,45 s, 5 escenas, 51 elementos):

```
  EVENTOS/min             49.2   (objetivo >= 44)
  simultaneidad media     2.15   (objetivo >= 2,00)
  duracion media          2.68 s (objetivo 1,6 - 2,4)
  COBERTURA media        39.5 %  (objetivo 22 - 38 %)
  cuadro casi vacio       3.15 s = 5%  (menos del 14% cubierto)
  HUECOS                     1   (objetivo 0)
```

Dos medidas fuera de rango (duración 2,68 s y cobertura 39,5%) y un hueco de 0,65 s.
Eso son tres ediciones de la tabla, no tres renders.

## La condición que lo hace válido

El auditor **replica el cálculo del motor**, no lo aproxima. `auditar.resolver()` y
`motor.py` resuelven el ancla igual, incluido `ancla_n`:

```python
def resolver(esc, ele):
    t0, t1 = esc["ini"], esc["fin"]
    dur = t1 - t0
    if "ancla" in ele:
        anc = re.sub(r"[^\wáéíóúüñÁÉÍÓÚÜÑ]", "", ele["ancla"]).lower()
        cand = [p for p in PAL if p["limpia"] == anc and t0 - 0.6 <= p["t"] <= t1]
        if not cand:
            print(f"  ! ancla sin coincidencia en {esc['id']}: '{ele['ancla']}'")
        i = ele.get("ancla_n", 0)
        base = cand[min(i, len(cand) - 1)]["t"] if cand else t0
    else:
        base = t0 + ele.get("desde", 0)
    e0 = max(t0, base + ele.get("offset", 0)) - t0
    e1 = min(dur, e0 + ele.get("dura", 2.0))
    return t0 + e0, t0 + e1
```

Si esas dos funciones se separan, el auditor mide **un montaje que no se va a
renderizar** y todas sus cifras son decorado. Cada vez que se toque la resolución de
anclas en `motor.py` hay que tocar `auditar.py` en la misma sesión, o el error no lo
verá nadie.

Lo mismo con `tiempos.json`: si se regeneró la voz y no el fichero de tiempos, **cada
ancla apunta a otro segundo** y el informe es ficción con formato de tabla.

## Lo que la auditoría no sustituye

Antes de renderizar el episodio entero se renderiza **una rejilla de fotogramas**
(`_grid.png`, un muestreo del episodio en una sola imagen). Cuesta un minuto y enseña
color, empaste y textura, que es exactamente lo que la tabla no sabe (`149`).

Orden de trabajo: **auditar → rejilla → render**. Nunca render primero.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Renderizar para ver si mejoró | 15–25 min por vuelta, y la causa sigue sin nombre |
| Auditar con `tiempos.json` viejo | Cada ancla cae en otro segundo; el informe no describe nada |
| Tocar `motor.py` y no `auditar.py` | Se audita un montaje distinto del que se renderiza |
| Leer sólo la línea que falla | Las medidas se leen juntas (`148`); una sola miente fácil |
| Auditar y renderizar igual porque "ya casi" | El fallo llega al vídeo y cuesta un render más arreglarlo |

## Relacionado

`17` medir el montaje · `141` elegir un umbral · `144` presencia no es superficie ·
`148` el cuadro de mando · `149` lo que no se puede medir
