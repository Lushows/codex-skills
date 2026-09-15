# 172 · Categorías contra búsqueda libre

**Qué resuelve:** cuál de las dos vías de Commons se usa para cada cosa, y por qué
mezclarlas mal llena el sondeo de ruido.

---

## La diferencia de fondo

| | **Categoría** | **Búsqueda libre** |
|---|---|---|
| Quién decide qué entra | una persona que conoce el tema | un buscador de texto |
| Contra qué casa | la clasificación del archivo | título, descripción y texto de la página |
| Precisión | altísima | baja para nombres propios |
| Cobertura | solo lo que alguien categorizó | todo lo subido |
| Falla cuando | la categoría no existe | el término tiene homónimos |

Una categoría de Commons es trabajo humano acumulado: alguien miró la foto, supo que
era el edificio de Enron y la metió donde va. La búsqueda libre no mira nada; casa
cadenas de texto.

## La regla

> **Nombres propios → categoría. Lugares, objetos, épocas y documentos → búsqueda libre.**

`sondeo.py` mantiene por eso dos listas separadas por episodio, `CATEGORIAS` y
`TERMINOS`, y las recorre en ese orden: primero lo curado, después lo masivo, y con
deduplicación por título para que lo que ya trajo la categoría no vuelva a entrar.

```python
vistos, todo = set(), []
for c in CATEGORIAS.get(epi, []):
    nuevos = [r for r in categoria(c) if r["titulo"] not in vistos]
    for r in nuevos:
        vistos.add(r["titulo"]); r["via"] = "categoria"
    todo += nuevos
for t in TERMINOS[epi]:
    nuevos = [r for r in buscar(t) if r["titulo"] not in vistos]
    for r in nuevos:
        vistos.add(r["titulo"]); r["via"] = "busqueda"
    todo += nuevos
```

El campo `via` no es decorativo: permite auditar después de dónde vino cada pieza.
Medido sobre los dos sondeos reales del piloto:

```
lustig : 988 piezas · 664 por categoría (67 %) · 324 por búsqueda
enron  : 379 piezas · 175 por categoría (46 %) · 204 por búsqueda
```

Enron depende más de la búsqueda libre precisamente porque sus nombres propios **no
tienen categoría** (`176`).

## Antes de usar una categoría: comprobar que existe

Pedir miembros de una categoría inexistente devuelve vacío, igual que una categoría que
existe pero está vacía. Son dos cosas distintas y hay que distinguirlas. `prop=categoryinfo`
lo dice en una sola llamada, para hasta 50 categorías:

```python
p = {"action": "query", "format": "json", "prop": "categoryinfo",
     "titles": "|".join("Category:" + c for c in cats)}
# ...
ci = pg.get("categoryinfo")
estado = "NO EXISTE" if ("missing" in pg and not ci) else f"files={ci['files']}"
```

**Salida real (11-sep-2026):**

```
Category:Enron                                    files=14      subcats=5
Category:Kenneth Lay                              files=2       subcats=0
Category:Jeffrey Skilling                         NO EXISTE
Category:Wanted posters of the FBI (…)            files=92      subcats=2
Category:Images from the National Archives (…)    files=468078  subcats=25
Category:Rijksmuseum                              files=0       subcats=0
```

Tres estados y tres decisiones distintas: **NO EXISTE** → no hay imagen libre catalogada,
dato firme (`173`). **files=0 con subcats=0** → la categoría es un contenedor vacío o un
redirect; buscar el nombre real. **files=468078** → hay que paginar, no pedir 500 de
golpe, o llega `HTTP 504`.

## `subcats` importa

`categorymembers` con `gcmtype=file` devuelve **solo los archivos del nivel actual**, no
los de las subcategorías. `Category:Enron` tiene 14 archivos y **5 subcategorías**: si no
se bajan, se pierde material del caso. Se recorre un nivel más con
`gcmtype=subcat` y se repite la consulta por cada hija. Dos niveles bastan; a partir de
ahí las subcategorías se alejan del tema.

## Cuándo la búsqueda libre sí es la buena

- **Lugares y edificios:** `"Houston Texas skyline downtown"` trajo 22 piezas útiles.
- **Objetos de época:** `"printing press banknotes"`, `"ocean liner first class 1920s"`.
- **Documentos:** `"United States congressional hearing"` trajo 24; son escaneos del
  Congreso, dominio público, y son la prueba en pantalla.
- **Conceptos visuales:** `"electricity transmission tower"`, `"ledger accounting book"`.

En todos estos casos el término describe **lo que se ve**, no a quién se llama, y ahí el
buscador de texto acierta.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Buscar un nombre propio en libre | Ruido casi puro; ver `173` |
| Buscar un objeto por categoría | La categoría es demasiado estrecha y devuelve 3 piezas |
| No distinguir "no existe" de "vacía" | Se declara sin archivo un caso que sí lo tiene con otro nombre |
| Ignorar `subcats` | Se pierde el material del caso que vive un nivel más abajo |
| No deduplicar por título | La misma foto entra dos veces y falsea el recuento del umbral |
| No guardar `via` | Imposible auditar de dónde salió el ruido |

## Relacionado

`170` · `171` · `173` · `175` · `176`
