# 190 · Curar por escenario, no por orden

**Qué resuelve:** el sondeo devuelve cientos de piezas y un episodio usa entre 60 y 120.
Si se eligen «las mejores», salen noventa fotos del mismo sitio y ninguna del sitio que
la historia necesita. El reparto se decide **antes** de mirar una sola imagen.

---

## El embudo real del episodio 01 (Lustig)

Medido hoy sobre `piloto/ep01-lustig/`:

| Paso | Piezas | Qué las quita |
|---|---|---|
| Sondeo (`sondeo.json`, 27 búsquedas) | **988** | — |
| Pasan 1100 px de ancho en la fuente | 843 | resolución |
| Cupo repartido por escenario | **84** | el reparto |
| Descargadas de verdad (`fuentes.json`) | 80 | dos escenarios sin material |
| Recortes montados (`recortes/`) | **69** | descartes de tratamiento (`198`) |

De 988 a 69. El paso que más quita no es la resolución: es el **cupo**. Y quitar por
cupo es lo único que garantiza que el episodio tenga imágenes de todos sus sitios.

De las 988, **432 estaban en dominio público o CC0** — casi la mitad. Nunca falta
material libre; falta material libre *del escenario correcto*.

## Por qué ordenar por calidad no sirve

Si se ordena las 843 piezas útiles por resolución y se cortan las 84 primeras, el
episodio de Lustig sale con: los planos del metro de París de 300 Mpx, los grabados del
Rijksmuseum a 3000 px… y **cero** fotos de Victor Lustig, porque su ficha policial mide
2746×1798 y queda en el puesto 400.

El guion no pide píxeles. Pide un hombre, una torre, una chatarrería, una imprenta, un
agente, una celda y un barco. Esa lista es el reparto.

## El criterio, en este orden

```python
# curar.py — el orden importa: primero el escenario, después la licencia, al final el ancho.
ESCENARIOS = {
    "el_hombre":     (6,  ["Victor Lustig", "Victor Lustig mugshot", "Mugshots"]),
    "torre":         (14, ["Eiffel Tower", "Eiffel Tower 1925", "Eiffel Tower construction"]),
    "paris":         (12, ["Paris in the 1920s", "Hotel de Crillon", "Hotel Crillon Paris"]),
    "chatarra":      (10, ["Scrap metal", "scrap metal yard"]),
    "falsificacion": (12, ["Printing presses", "Counterfeit money", "counterfeit banknote"]),
    "ley":           (10, ["United States Secret Service", "wanted poster criminal"]),
    "alcatraz":      (12, ["Alcatraz Federal Penitentiary", "Alcatraz cell", "Prison cells"]),
    "viaje":         (8,  ["Ocean liners", "limousine 1920s", "passport 1920s"]),
}

def puntua(x):
    """Dominio público primero; después, resolución. Nunca al revés."""
    ancho = int(x["px"].split("x")[0])
    libre_del_todo = 1 if re.search(r"public domain|cc0", x["licencia"], re.I) else 0
    return (libre_del_todo, ancho)

elegidas, vistos = [], set()
for esc, (cupo, terminos) in ESCENARIOS.items():
    cand = [x for x in sondeo
            if x["busqueda"] in terminos
            and int(x["px"].split("x")[0]) >= 1100     # umbral duro de la fuente
            and x["titulo"] not in vistos]             # sin repetir entre escenarios
    cand.sort(key=puntua, reverse=True)
    for x in cand[:cupo]:
        x["escenario"] = esc
        vistos.add(x["titulo"])
        elegidas.append(x)
```

Tres detalles que no son decorativos:

- **`vistos`** impide que una foto sirva a dos escenarios. Una torre Eiffel que ya entró
  por `torre` no puede volver a entrar por `paris`, aunque la búsqueda la devuelva otra
  vez. Sin eso, el escenario que se evalúa último se queda vacío.
- **Dominio público antes que resolución.** Una foto DP de 1200 px se prefiere a una
  CC-BY-SA de 4000: la primera no obliga a poner un crédito en pantalla (`184`).
- **El filtro de 1100 px mira la fuente**, que no es el ancho que va a tener el recorte.
  Esa trampa se resuelve en `194`.

## Lo que imprime al terminar

```
escenario        cupo  hay    elegidas
--------------------------------------------------------------------------
el_hombre        6     2      2 elegidas (2 en dominio publico)   <-- aviso
torre            14    61     14 elegidas (11 en dominio publico)
paris            12    38     12 elegidas (9 en dominio publico)
...
--------------------------------------------------------------------------
TOTAL 80 piezas · 66 en dominio publico · 14 piden atribucion
```

La columna **`hay`** es la que se lee de verdad. Si `hay` es mucho mayor que el cupo, el
escenario está sobrado y se puede subir el cupo. Si `hay < cupo`, el episodio tiene un
agujero y hay que decidirlo ahora, no a mitad del montaje (`191`).

## Cuánto cuesta no curar

Las 80 piezas descargadas pesan **702 MB** (media 8,8 MB, la mayor 82,9 MB: un plano del
metro de París de 300 Mpx). Bajar las 988 del sondeo serían **~8,7 GB** y unas dos horas
de descarga cortés (`193`), para tirar el 93%.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Ordenar las candidatas por resolución y cortar | Episodio sin el protagonista; sobran paisajes |
| Cupos inventados sin leer el guion | Escenarios con 14 fotos que salen 3 segundos |
| No marcar `vistos` entre escenarios | El último escenario del diccionario se queda vacío |
| Descargar primero y curar después | 8,7 GB y dos horas para usar el 7% |
| Filtrar por licencia *después* de cortar el cupo | El cupo se llena de CC-BY y el episodio se llena de créditos |

## Relacionado

`170` · `174` · `180` · `191` · `194` · `199`
