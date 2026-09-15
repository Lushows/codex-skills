# 409 — Depurar un apilado

**Qué resuelve:** un apilado falla de tres maneras y solo una avisa: ffmpeg aborta con un mensaje, o el
render sale bien y falta algo, o el render sale bien y en pantalla hay **otra cosa**. Este módulo es el
procedimiento, de más barato a más caro, para no gastar diez minutos de render en averiguar lo que se sabe
leyendo el grafo.

---

## 1. Leer el grafo antes de renderizar

Las tres clases de error que ffmpeg detecta se ven **antes**, en microsegundos, parseando el filtergraph:

```python
import re
SALIDAS = {"out"}                                  # las etiquetas que van en -map

def revisar(entradas, filtros):
    fc, fallos = ";".join(filtros), []
    usados = [int(m) for m in re.findall(r"\[(\d+):[va]\]", fc)]
    if usados and max(usados) >= entradas:
        fallos.append(f"indice corrido: el filtro pide [{max(usados)}:v] y solo "
                      f"hay {entradas} entradas -i (indices 0..{entradas-1})")
    produce, consume = [], []
    for f in filtros:                              # cada cadena: [ent]…[sal][sal]
        ent = re.findall(r"^((?:\[\w+\])+)", f); sal = re.findall(r"((?:\[\w+\])+)$", f)
        consume += re.findall(r"\[(\w+)\]", ent[0]) if ent else []
        produce += re.findall(r"\[(\w+)\]", sal[0]) if sal else []
    produce = [p for p in produce if not re.match(r"^\d+:", p)]
    consume = [c for c in consume if not re.match(r"^\d+$", c)]
    for e in sorted(set(produce)):
        if produce.count(e) > 1: fallos.append(f"[{e}] la producen {produce.count(e)} filtros")
        if e not in consume and e not in SALIDAS: fallos.append(f"[{e}] rama muerta")
    for e in sorted(set(consume)):
        if e not in produce: fallos.append(f"[{e}] se consume sin que nadie la produzca")
        elif consume.count(e) > 1: fallos.append(f"[{e}] consumida 2+ veces: falta split")
    return fallos
```

Ejecutado contra cuatro grafos de prueba y contra las cinco escenas reales de `ep01-lustig`:

```
indice corrido              · el filtro pide [3:v] y solo hay 3 entradas -i
etiqueta consumida 2 veces  · [v1] rama muerta · [bg] consumida 2+ veces: falta split
rama muerta tras split      · [v1] rama muerta
correcto                    OK
muerte 16 entradas 33 filtros -> OK   ·  oficio  8/17 -> OK  ·  nombre  9/19 -> OK
torre  19 entradas 39 filtros -> OK   ·  metodo 13/27 -> OK
```

---

## 2. Los tres mensajes y lo que significan de verdad

| Mensaje de ffmpeg | Causa real | Módulo |
|---|---|---|
| `Invalid file index N in filtergraph description` | Índice corrido: `enumerate()` con `continue` | `403` |
| `Error binding filtergraph inputs/outputs: Invalid argument` | Etiqueta consumida dos veces, o rama sin consumir | `404` §2 |
| `Filter … has an unconnected output` | Rama muerta tras un `split` | `404` §2 |

Los tres llegan por **`stderr` de un subproceso** y devuelven `4294967274` en Windows (`-22` sin signo).
Un bucle que no comprueba `returncode != 0` sigue como si nada.

---

## 3. Espiar el comando sin renderizar

Sustituir `subprocess.run` y quedarse con el comando que el motor *iba* a ejecutar:

```python
cap = []
class F: returncode = 0; stderr = ""; stdout = ""
subprocess.run = lambda cmd, **k: (cap.append(cmd), F())[1]
import motor                                       # el motor cree que ha renderizado
```

Sobre el episodio real, en dos segundos: `muerte` 16 entradas / 4.896 caracteres de filtergraph / comando
de 7.180; `torre` 19 entradas / 5.813 / 8.658. Unos **320 caracteres por elemento**. El límite de la línea
de comandos de Windows son **32.767**: un episodio de 400 eventos en un solo grafo serían ~128.000, cuatro
veces el tope. Si un grafo se acerca, la salida es `-filter_complex_script grafo.txt`, que además se puede
leer y versionar.

---

## 4. La aritmética, antes que el ojo

```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 salida/_mudo.mp4
# 56.72   frente a  sum(e["fin"]-e["ini"] for e in ESCENAS) = 63.45  -> falta una escena
```

Y su pareja en el código: `if len(partes) != len(ESCENAS): raise SystemExit(...)`. Un episodio corto pero
sincronizado se recupera; uno completo y desfasado hay que verlo entero para descubrirlo (`403` §4).

---

## 5. Cuando el render sale bien y la pantalla no

Aquí ya no hay mensajes. Cuatro maniobras, de más barata a más cara:

1. **El fotograma en el segundo exacto.** `ffmpeg -ss 18.4 -i escena.mp4 -frames:v 1 -y f.png`. Un elemento
   que falta ahí está enterrado (`386`), tiene el `enable` mal o el ancla cayó fuera.
2. **Dejar uno fuera.** Renderizar la escena tantas veces como capas, quitando una cada vez, a 200 px y 25
   fotogramas: segundos por pasada (`408` §2). La versión donde reaparece lo que faltaba señala al culpable.
3. **Cortar por la mitad.** Cerrar la cadena en `[v{k}]` y renderizar solo los primeros *k* eslabones. En
   `log₂(n)` pasadas se localiza el que rompe la imagen.
4. **Pintar cada capa.** Un `drawtext` con el índice y un tinte distinto por capa. Un fotograma dice, sin
   dudas, quién está encima de quién y quién no está.

---

## 6. El fallo que no avisa nunca

El peor caso produce **la imagen equivocada sin un solo error**. Anotado en `motor.py:64`: la caché de
pre-escalado se nombraba por `basename`, y como `ficha_policial.png` existe en `fx/` y en `recortes/`, el
segundo reutilizaba el PNG del primero. Render correcto, tiempos correctos, imagen ajena; el arreglo fue
nombrar por hash de la ruta absoluta. La familia es siempre la misma: **cualquier número o nombre derivado
de la posición o del basename** —el color «por turno» (`i % 3`), la posición por índice, el alias de
recurso—. No falla: acierta con lo que no es. Se caza con el barrido del §5.4 contra el guion, nunca
mirando el vídeo.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Depurar renderizando la escena entera a resolución final | Diez minutos por hipótesis |
| No comprobar `returncode` del subproceso | El fallo se lo traga el bucle |
| Comprobar `returncode < 0` | En Windows llega 4294967274: hay que comprobar `!= 0` |
| Creer que si el MP4 existe, el render fue bien | Existe, dura menos y va desfasado |
| Meter un grafo enorme en la línea de comandos | Tope de 32.767 caracteres en Windows: usa `-filter_complex_script` |
| Cachear por `basename` en vez de por ruta | Imagen equivocada sin un solo error |
| Dar por bueno un apilado sin mirar un fotograma | Un elemento 100 % enterrado no cambia ninguna métrica |

## Relacionado

`400` el orden de render es narrativo · `403` índices que se corren · `404` acumular o sustituir ·
`408` lo que cuesta cada capa · `104` filter_complex · `108` análisis y medición · `109` trampas de ffmpeg ·
`133` verificación automática · `386` el elemento enterrado · `canales_lushows/153` índices corridos ·
`canales_lushows/159` cazar un fallo que no avisa · `canales_lushows/155` cachés que mienten ·
`canales_lushows/160` la grilla de fotogramas
