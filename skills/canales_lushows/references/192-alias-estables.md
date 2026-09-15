# 192 · Alias estables y colisiones

**Qué resuelve:** el alias es el nombre corto con el que una pieza de archivo vive en
disco, en `fuentes.json`, en la tabla de recortes y en los créditos. Si dos piezas
distintas reciben el mismo alias, el registro que existe para **evitar** errores de
crédito se convierte en la fuente del error.

---

## El caso real

`curar.py` construía el alias así:

```python
alias = re.sub(r"[^\w]+", "_", r["titulo"][5:])[:44].strip("_").lower()
nombre = alias + ext
```

Dos ficheros distintos del Rijksmuseum, ambos en el sondeo del episodio 01:

```
File:Eiffeltoren bij nacht met het woord 'Citroën' in de verlichte letters
     Exposition des Arts Décoratifs La Tour Eiffel vue de nuit (titel op object),
     RP-F-2012-96-168.jpg          2108x3276
File:Eiffeltoren bij nacht met het woord 'Citroën' in de verlichte letters
     Les Illuminations de la Tour Eiffel (titel op object),
     RP-F-2012-96-166.jpg          2084x3282
```

Lo que los distingue —`RP-F-2012-96-168` contra `-166`— está en el carácter 150. El
alias se corta en el 44:

```
eiffeltoren_bij_nacht_met_het_woord_citroën     ← los dos, idéntico
```

Y entonces pasa lo peor que puede pasar, que es que **no falle**:

```python
out = os.path.join(carp, nombre)
if not os.path.exists(out):      # existe: es el primero. No se descarga.
    ...descargar...
fuentes.append({...})            # la ficha del SEGUNDO se añade igual
```

El segundo fichero no se descarga, pero **su ficha entra en `fuentes.json`**: otro
título, otro autor, otra URL, otra licencia, apuntando a una imagen que no es la suya.
En el episodio 01 quedaron dos entradas idénticas en `alias` y `archivo`, con títulos y
URLs distintos, y un solo `.jpg` en disco. Quien escriba los créditos desde ese registro
acreditará la foto equivocada.

## Cuánto de frecuente es

Medido sobre las **988** piezas del sondeo del episodio 01:

| Regla | Alias únicos | Colisiones | Ficheros que se pierden |
|---|---|---|---|
| `titulo[5:]` truncado a 44 | 924 / 988 | **31** | **64** |
| Recortado + huella del título | **988 / 988** | 0 | 0 |

El detalle que lo explica: **336 de los 988 alias miden exactamente 44** — están clavados
en el tope, es decir, truncados. Commons nombra los ficheros con frases larguísimas y el
identificador discriminante casi siempre va al final. Peor caso encontrado: cinco piezas
distintas colapsando en `thursday_afternoon_14_january_2021_seventeen`.

## La regla que no colisiona

```python
import hashlib, re, unicodedata

def alias_estable(titulo, largo=52):
    """Legible para un humano + huella del título completo. Nunca colisiona,
    no cambia entre ejecuciones, y es ASCII puro (sobrevive a Windows y a git)."""
    base = unicodedata.normalize("NFKD", titulo[5:]).encode("ascii", "ignore").decode()
    base = re.sub(r"[^A-Za-z0-9]+", "_", base).strip("_").lower()
    huella = hashlib.sha1(titulo.encode("utf-8")).hexdigest()[:6]
    return (base[:largo - 7].rstrip("_") + "_" + huella)

# ...RP-F-2012-96-168.jpg -> eiffeltoren_bij_nacht_met_het_woord_citroen_i_346b0f
# ...RP-F-2012-96-166.jpg -> eiffeltoren_bij_nacht_met_het_woord_citroen_i_9d1e18
```

Tres propiedades, y las tres hacen falta. **Determinista:** el mismo título da siempre el
mismo alias, así que volver a curar no vuelve a descargar nada ni rompe la tabla de
recortes. **Único:** la huella viene del título completo, no del trozo visible.
**ASCII:** el patrón de `\w` deja pasar la `ë` — 85 de los 988 alias llevaban caracteres
no ASCII, que en disco se vuelven `citro?n` según la consola, rompen el emparejamiento
con `fuentes.json` y estropean cualquier búsqueda.

## La compuerta, además del nombre

```python
# la comprobación que habría cazado el caso del Rijksmuseum en medio segundo
import collections, os, json
f = json.load(open("fuentes.json", encoding="utf-8"))
for campo in ("alias", "archivo"):
    c = collections.Counter(x[campo] for x in f)
    rep = [k for k, v in c.items() if v > 1]
    assert not rep, f"{campo} repetido: {rep}"
assert len(f) == len({x["url"] for x in f}), "dos fichas con la misma URL"
faltan = [x["archivo"] for x in f
          if not os.path.exists(os.path.join("archivo", x["archivo"]))]
assert not faltan, f"ficha sin imagen en disco: {faltan}"
```

La última línea es la importante: **una ficha sin su imagen en disco significa que
alguien se comió la descarga**, que es exactamente la forma que toma la colisión.

## No renombrar nunca

El alias es la clave primaria del episodio: vive en `fuentes.json`, en `archivo/`, en la
tabla `PIEZAS`, en el PNG de `recortes/`, en `_recortes.json` y en el guion visual.
Cambiar la regla a mitad de episodio obliga a tocar seis sitios. Se cambia entre
episodios, y se regenera todo.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Truncar el título y usarlo de nombre | 31 colisiones por cada 988 piezas; créditos equivocados |
| `if not os.path.exists: descargar` sin comprobar identidad | La segunda ficha apunta a la imagen de la primera |
| Alias con acentos o `ë` | Mojibake en disco; `fuentes.json` deja de emparejar |
| Usar el índice del bucle (`foto_01`) como alias | Cambia al reordenar el sondeo; rompe la tabla de recortes |
| Renombrar alias a mitad de episodio | Seis ficheros desincronizados y recortes huérfanos |

## Relacionado

`188` · `190` · `193` · `199` · `184` · `153`
