# 199 · El manifiesto del material

**Qué resuelve:** un PNG recortado no dice de dónde vino. Sin un registro que lo diga, al
publicar hay que reconstruir a mano de qué foto salió cada elemento, con qué licencia y
de quién — y eso, con 69 piezas, no se hace: se inventa o se omite. El manifiesto es lo
que hace el episodio **defendible**.

---

## Los dos ficheros

| Fichero | Lo escribe | Una línea por | Responde a |
|---|---|---|---|
| `fuentes.json` | `curar.py`, al descargar | **fuente** (80) | ¿de dónde salió esta imagen y con qué licencia? |
| `recortes/_recortes.json` | el script de recortes | **pieza montada** (69) | ¿qué hay en el montaje y de qué fuente sale? |

No son el mismo fichero porque no son la misma cosa: en el episodio 01, dos fuentes
dieron ocho piezas (`191`). La relación es de uno a muchos y el manifiesto la guarda.

## Una ficha

```json
{
  "alias": "certificado_defuncion",
  "escenario": "el_hombre",
  "trato": "revista",
  "origen": "victor_lustig_death_certificate_png",
  "px": "1539x1369",
  "kb": 540,
  "licencia": "Public domain",
  "autor": "The State Board of Health of Missouri",
  "url": "https://commons.wikimedia.org/wiki/File:Victor_Lustig_Death_Certificate.png"
}
```

Nueve campos, cada uno porque alguien lo necesita después:

| Campo | Para qué sirve, en concreto |
|---|---|
| `alias` | La clave con la que el guion visual pide la pieza. Es el nombre del PNG (`192`) |
| `escenario` | Comprobar que el montaje usa los ocho escenarios y no cuatro (`190`) |
| `trato` | `tijera`, `revista`, `silueta`, `silueta +estirada`, `tijera (silueta sucia)` — deja por escrito **lo que pasó de verdad**, incluidas las degradaciones (`194`, `195`) |
| `origen` | El puente a `fuentes.json`. Sin él no hay créditos |
| `px` / `kb` | La auditoría (`140`): peso por megapíxel, anchos, PNG vacíos |
| `licencia` | Decide si esta pieza obliga a poner un crédito **y cuál** (`184`) |
| `autor` / `url` | El crédito literal y la prueba de que existe |

## Se escribe al generar, no después

```python
manifiesto.append(dict(alias=alias, escenario=it["escenario"], trato=real,
                       origen=origen, px=f"{out.width}x{out.height}", kb=kb,
                       licencia=it["licencia"], autor=it.get("autor", ""),
                       url=it["url"]))
```

`trato=real` y no `trato=trato`: se anota el tratamiento **que salió**, no el que se pidió.
En el episodio 01 eso deja constancia de tres piezas que no salieron como se pedían —dos
siluetas caídas a tijera y una estirada—. Anotar la intención es como no anotar nada.

## Para qué sirve después

**1 · Los créditos de la descripción, en una línea.**

```python
import json, itertools
SIN_CREDITO = ("public domain", "cc0", "no known copyright")
m = json.load(open("recortes/_recortes.json", encoding="utf-8"))
piden = [x for x in m if not any(s in x["licencia"].lower() for s in SIN_CREDITO)]
for url, filas in itertools.groupby(sorted(piden, key=lambda x: x["url"]),
                                    key=lambda x: x["url"]):
    f = next(filas)
    print(f"· {f['autor']} — {f['licencia']} — {url}")
```

Se agrupa por `url` y no por `alias`: cuatro casillas del certificado son cuatro piezas y
**un** crédito.

Sobre el episodio 01 imprime **cero líneas**, y es correcto: las 69 piezas salen de 60
fuentes en dominio público y 9 en CC0, y ninguna obliga a acreditar. Conviene saberlo
porque `curar.py` dice otra cosa —imprime «14 piden atribución» contando como tales las
CC0, que no la piden—: **el mensaje del curador está mal, y el manifiesto tiene razón.**

**2 · Responder a una reclamación.** Alguien dice que el segundo 47 usa una foto suya: se
busca el alias de ese segundo, se lee su `url` y su `licencia`, y se contesta con el
enlace. Sin manifiesto la respuesta tarda una tarde, y puede no existir (`189`).

**3 · Regenerar solo lo que cambia.** El manifiesto dice qué piezas salieron de cada
fuente: reencuadrar el certificado regenera sus cinco piezas, no las 69.

**4 · Auditar sin abrir un PNG.** Un recuento por `trato` y por `escenario` —42 tijera,
22 revista, 3 silueta (una estirada), 2 degradadas— dice antes de montar si algún
escenario va a dejar un agujero.

## Lo que NO va en el manifiesto

Describe **material**, no montaje. En qué segundo entra una pieza, con qué movimiento y
sobre qué fondo es del guion visual y vive en otro fichero: mezclarlo obligaría a
regenerar los recortes en cada retoque del montaje.

## La comprobación de cierre

```python
import os, json
m = json.load(open("recortes/_recortes.json", encoding="utf-8"))
f = {x["alias"] for x in json.load(open("fuentes.json", encoding="utf-8"))}
png = {p[:-4] for p in os.listdir("recortes") if p.endswith(".png") and not p.startswith("_")}

assert {x["alias"] for x in m} == png,            "PNG y manifiesto no cuadran"
assert all(x["origen"] in f for x in m),          "pieza sin fuente en fuentes.json"
assert all(x["licencia"] for x in m),             "pieza sin licencia"
assert all(x["url"].startswith("http") for x in m), "pieza sin URL de prueba"
```

Cuatro líneas. **Si alguna falla, el episodio no se publica**: no porque falte un dato,
sino porque hay una imagen en pantalla que nadie puede justificar.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Escribir el manifiesto a mano al final | Se inventan campos; el 20% no cuadra |
| Anotar el tratamiento pedido y no el que salió | Una pieza estirada pasa por buena |
| No guardar `origen` | Los créditos hay que reconstruirlos foto a foto |
| Agrupar los créditos por `alias` | Cuatro casillas del mismo documento, cuatro créditos |
| Meter datos de montaje en el manifiesto | Retocar el guion obliga a regenerar los recortes |
| PNG en `recortes/` que no está en el manifiesto | Material en pantalla sin licencia conocida |

## Relacionado

`188` · `184` · `189` · `190` · `194` · `140`
