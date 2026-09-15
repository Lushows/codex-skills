# 171 · La API de Commons

**Qué resuelve:** cómo se le pregunta a Wikimedia Commons por archivos y de dónde sale,
exactamente, el dato de licencia.

---

## El único punto de entrada

`https://commons.wikimedia.org/w/api.php` — todo es GET con parámetros, sin clave ni
registro. Sí hace falta un **User-Agent propio con contacto**: es la norma de Wikimedia
y sin él las peticiones acaban bloqueadas.

## La forma canónica: generador + imageinfo

No se pide una lista y luego se consulta archivo por archivo. Se usa un **generador**:
una consulta produce la lista *y* trae los metadatos de cada pieza en la misma llamada.
Los dos generadores son `search` (texto, con `gsrnamespace=6`) y `categorymembers`
(categoría, con `gcmtype=file`); el tope de ambos es 500. A los dos se les cuelga
`prop=imageinfo` con `iiprop=url|size|extmetadata`, que son las tres piezas que importan.

```python
import json, re, urllib.request, urllib.parse
API = "https://commons.wikimedia.org/w/api.php"
UA  = "PaperEmpires-archivo/1.0 (documental; contacto: ...)"

def pedir(p):
    req = urllib.request.Request(API + "?" + urllib.parse.urlencode(p),
                                 headers={"User-Agent": UA})
    return json.load(urllib.request.urlopen(req, timeout=45))

def por_categoria(cat, limite=100):
    return pedir({"action": "query", "format": "json",
                  "generator": "categorymembers", "gcmtitle": "Category:" + cat,
                  "gcmtype": "file", "gcmlimit": str(limite),
                  "prop": "imageinfo", "iiprop": "url|size|extmetadata"})

# la búsqueda libre es igual, con generator=search + gsrsearch + gsrnamespace=6
```

## Qué devuelve: `imageinfo` y `extmetadata`

`query.pages` es un **diccionario** (clave = id de página), no una lista. De cada
página, `imageinfo[0]` trae lo técnico y `imageinfo[0].extmetadata` lo legal. Cada campo
de `extmetadata` es `{"value": ..., "source": ...}` y el `value` **puede traer HTML**.

```python
def limpiar_html(t): return re.sub(r"<[^>]+>", "", t or "").strip()

d = pedir({"action": "query", "format": "json", "titles": "File:Ken Lay.jpg",
           "prop": "imageinfo", "iiprop": "url|size|extmetadata"})
for pg in d["query"]["pages"].values():
    ii = (pg.get("imageinfo") or [{}])[0]
    md = ii.get("extmetadata") or {}
    print("px :", ii.get("width"), "x", ii.get("height"))
    for k in ("LicenseShortName", "UsageTerms", "Artist", "Credit", "Permission"):
        if k in md:
            print(f"{k:<18}: {limpiar_html(md[k]['value'])[:78]}")
```

**Salida real (ejecutado 11-sep-2026):**

```
px : 324 x 400
LicenseShortName  : Public domain
UsageTerms        : Public domain
Artist            : United States Marshals Service
Permission        : Public domain, United States Marshals Service published it.
```

## Los campos que deciden

| Campo | Uso |
|---|---|
| `LicenseShortName` | "Public domain", "CC BY-SA 4.0", "No restrictions" — el que se filtra |
| `UsageTerms` | la frase larga; segundo filtro, y trampa (abajo) |
| `Artist` | autor, con HTML dentro; va al `fuentes.json` y a los créditos |
| `width` / `height` | píxeles reales; descarta lo que no aguanta 1920 |
| `url` | descarga directa — **lleva query string detrás** |
| `descriptionurl` | la página de Commons; es la URL que se cita |

## Las dos trampas de la URL y del tamaño

`ii["url"]` llega como `...Ken_Lay.jpg?utm_source=commons.wikimedia.org&utm_campaign=...`.
Comprobar la extensión con `endswith(".jpg")` **descarta absolutamente todo** y el caso
parece no tener archivo libre. Se corta primero la cadena de consulta:

```python
ruta = (ii.get("url", "") or "").split("?")[0]
if not re.search(r"\.(jpg|jpeg|png|webp)$", ruta, re.I):
    continue
```

El ancho mínimo del sondeo es **700 px**; `curar.py` lo sube a **1100 px** (`194`).

## La trampa viva del filtro de licencias

El filtro de veto busca la palabra `copyright`. La frase **"No known copyright
restrictions"** —la de las subidas de la Biblioteca del Congreso y de Flickr Commons—
contiene esa palabra y **es material libre**. Medido sobre `Category:Bain News Service`:

```
total = 85 · pasan el filtro de libres = 85
vetados por la palabra "copyright"     = 54
aceptados finalmente                   = 26   (se tira el 64 % de lo libre)
```

El arreglo es anclar el veto a la frase completa, no a la palabra suelta (`180`–`185`).
La prueba mínima de cualquier filtro nuevo son cinco cadenas: `Public domain`,
`No known copyright restrictions`, `CC BY-SA 4.0`, `CC BY-NC 2.0`, `PD-USGov`.

## Cortesía con un servicio gratuito

`time.sleep(0.4)` entre consultas, `0.25` entre descargas. Y `gcmlimit=500` sobre una
categoría enorme revienta: `Category:Images from the National Archives and Records
Administration` tiene **468.078 archivos** y devuelve `HTTP 504 Gateway Timeout`. Para
categorías grandes, 100 por página y continuación (`193`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Tratar `query.pages` como lista | `AttributeError`; es un diccionario por id |
| No limpiar el HTML de `extmetadata` | El autor sale con `<a href=...>` en los créditos |
| Comprobar la extensión sin cortar el `?` | Se descarta el 100 %: el caso parece sin archivo |
| Vetar por la palabra `copyright` | Se tira el 64 % de una categoría libre |
| Ir sin User-Agent con contacto | Bloqueo por parte de Wikimedia |
| `gcmlimit=500` en categorías masivas | 504 y sondeo a medias sin avisar |

## Relacionado

`170` · `172` · `180` · `188` · `193` · `194`
