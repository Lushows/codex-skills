# 178 · Archivos europeos

**Qué resuelve:** de dónde sale el archivo cuando la historia no pasa en Estados Unidos, y
qué licencia lleva de verdad cada casa.

---

## La diferencia de partida con EE.UU.

En Estados Unidos lo federal es dominio público por definición (`177`). En Europa **no
existe esa regla**: cada institución decide qué libera y con qué licencia. Por eso aquí no
se pregunta «¿es de un organismo público?» sino **«¿qué licencia puso esta casa?»**, y la
respuesta cambia de un museo a otro.

Hay dos mundos que no hay que confundir:

- **La obra**, que puede estar en dominio público por antigüedad (un cuadro de 1650).
- **La reproducción fotográfica** de esa obra, que en algunos países se considera obra
  nueva. Quien la hizo puede reclamar derechos sobre el escaneo. Es el mismo problema que
  con la música (`130`): la obra es libre, la grabación no.

Las casas serias resuelven eso declarando **CC0 o dominio público** sobre sus escaneos. Es
lo primero que hay que mirar.

## Lo que hay, medido en Commons

Igual que con lo federal, la vía de trabajo es **Commons**, donde la licencia viene ya en
`extmetadata`. Cifras reales del 11-sep-2026:

| Categoría | Archivos | Subcats | Licencia típica |
|---|---|---|---|
| `Files from Gallica` | **5.992.760** | 35 | dominio público |
| `Images from Nationaal Archief` (NL) | **431.545** | 29 | mayoría CC BY-SA / PD |
| `Images from Gallica` (BnF) | 234.857 | 2.870 | dominio público |
| `Images from the Swedish National Heritage Board` | 185.596 | 15 | CC BY / PD |
| `Images from the German Federal Archive` (Bundesarchiv) | **86.049** | 4 | **CC BY-SA 3.0 de** |
| `Images from the Deutsche Fotothek` | 62.635 | 23 | variada |
| `Images from the Rijksmuseum` | 6.866 | 5 | **dominio público / CC0** |
| `Europeana 1914-1918` | 1.939 | 1 | PD y CC BY-SA 3.0 |

Muestreo de licencias, ejecutado sobre las primeras 60 piezas de cada categoría:

```
Images from the Rijksmuseum          -> Public domain 57 · CC0 2
Images from the German Federal Archive -> CC BY-SA 3.0 de 25
Europeana 1914-1918                  -> Public domain 36 · CC BY-SA 3.0 19
```

## Casa por casa

**Rijksmuseum (Países Bajos).** El mejor caso de Europa: liberó su colección en alta
resolución y sus escaneos salen como **dominio público o CC0**, sin atribución obligatoria.
Pintura, grabado, plano, objeto. Para historias de dinero antiguas —comercio, compañías
comerciales, moneda, puerto— es la primera parada.

**Bundesarchiv (Alemania).** Fotografía del siglo XX en volumen. Ojo: su licencia es
**CC BY-SA 3.0 de**, que **obliga a atribuir** y arrastra la cláusula *share-alike*. Se
puede usar, pero hay que rotular los créditos (`184`) y saber qué significa SA (`183`).
No es lo mismo que dominio público y no se puede mezclar sin pensar.

**Gallica (Biblioteca Nacional de Francia).** Millones de piezas: prensa antigua, grabado,
cartografía, fotografía. Es además el único de esta lista cuya **API pública responde sin
clave** (ver abajo).

**Nationaal Archief (Países Bajos).** 431.545 piezas en Commons, sobre todo fotografía de
prensa del siglo XX; muchas con CC BY-SA.

**Europeana.** No es un archivo: es un **agregador** de miles de instituciones europeas. Su
utilidad real es *encontrar* dónde vive una pieza; después se va a la institución que la
tiene, porque la licencia la pone ella, no Europeana.

**Riksantikvarieämbetet (Suecia).** 185.596 piezas, políticas de licencia generosas.

## Qué responde cada API de verdad

Probado el 11-sep-2026, sin clave y con User-Agent propio:

```
Gallica (BnF) SRU ......................... HTTP 200 · devuelve XML con registros
Europeana API ............................. HTTP 401 Unauthorized  (exige clave)
Rijksmuseum API (endpoint antiguo) ........ HTTP 410 Gone          (retirado)
```

Es decir: **no se manda a nadie a integrarse con el API del Rijksmuseum**, porque el
endpoint público que se usaba devuelve 410. Su material se toma de Commons, donde hay 6.866
piezas con la licencia ya declarada. Europeana necesita registro. Y Gallica sí funciona:

```python
import urllib.request, urllib.parse, re
q = urllib.parse.urlencode({"operation": "searchRetrieve", "version": "1.2",
                            "query": 'gallica all "krach boursier"',
                            "maximumRecords": "3"})
req = urllib.request.Request("https://gallica.bnf.fr/SRU?" + q,
                             headers={"User-Agent": UA})
t = urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "replace")
print(re.search(r"numberOfRecords>(\d+)<", t).group(1))
print(re.findall(r"<dc:rights>(.*?)</dc:rights>", t)[:4])
```

**Salida real:**

```
10151
['domaine public', 'public domain', 'domaine public', 'public domain']
```

El campo `dc:rights` de Gallica trae la declaración en dos idiomas. Ese es el dato que se
copia al `fuentes.json`, no una suposición.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Suponer que «archivo nacional» = dominio público | El Bundesarchiv es CC BY-SA: hay que atribuir |
| Confundir obra libre con escaneo libre | El cuadro es de 1650 y la foto del cuadro no lo es |
| Citar Europeana como fuente | Es agregador; la licencia la pone la institución |
| Integrarse con el API del Rijksmuseum | HTTP 410; su material se toma de Commons |
| Mezclar CC BY-SA con material propio sin leer la cláusula | Obligación *share-alike* sobre lo derivado (`183`) |
| Dar por hecho que hay API abierta | De tres probadas, solo Gallica responde sin clave |

## Relacionado

`130` · `177` · `179` · `181` · `183` · `184` · `188`
