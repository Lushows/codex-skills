# 174 · El umbral de piezas útiles

**Qué resuelve:** cuántas piezas de archivo hace falta tener ANTES de escribir, y por qué
el número total del sondeo engaña.

---

## El cálculo

Un episodio de 10 minutos con la densidad del canal (`10`) mueve entre 44 y 48 eventos
por minuto. No todos son piezas de archivo nuevas: hay texto, cifras, fondos y reentradas
del mismo elemento. En la práctica, contando reutilizaciones, sale así:

| Duración | Piezas distintas en pantalla | Mínimo para arrancar | Cómodo |
|---|---|---|---|
| Corto vertical (60 s) | 12–18 | 15 | 25 |
| Episodio de 10 min | 60–80 | **40** | 60–80 |
| Episodio de 20 min | 110–140 | 80 | 120 |

`sondeo.py` imprime el veredicto al terminar:

```
umbral para 10 min: 40 piezas mínimo · SUFICIENTE
```

Y `curar.py` confirma que de 988 piezas sondeadas para el episodio de Lustig acabaron
entrando al montaje **80** — que es exactamente el rango cómodo.

## Por qué 40 y no 25

Con 25 piezas para 10 minutos cada foto sale tres o cuatro veces. El espectador lo nota
antes que el montador: se llama «este vídeo tiene cuatro fotos». Con 40 se puede repetir
sin que cante, y por encima de 60 se puede **elegir**, que es lo que de verdad sube la
calidad: la diferencia entre poner la foto que hay y poner la que encaja.

## El número total engaña: los cuatro descuentos

El total que imprime el sondeo **no es el material del episodio**. Hay que aplicarle
cuatro descuentos antes de creérselo. Medido sobre los dos sondeos reales:

```python
import json, io, re, collections
d = json.load(io.open("ep01-enron/sondeo.json", encoding="utf-8"))
anchos = [int(x["px"].split("x")[0]) for x in d]
pd = sum(1 for x in d if re.search(r"public domain|cc0", x["licencia"], re.I))
print("total          :", len(d))
print(">=1100 px      :", sum(1 for a in anchos if a >= 1100))
print(">=1920 px      :", sum(1 for a in anchos if a >= 1920))
print("dominio público:", pd, "· piden atribución:", len(d) - pd)
print("por vía        :", dict(collections.Counter(x.get("via") for x in d)))
```

**Salida real (11-sep-2026):**

```
                        enron        lustig
total                     379           988
>=1100 px                 331           843
>=1920 px                 262           680
dominio público           161           432
piden atribución          218           556
por vía         cat 175 / bus 204   cat 664 / bus 324
```

| Descuento | Enron | Lustig | Qué se pierde |
|---|---|---|---|
| 1. Resolución (<1100 px) | −48 | −145 | No aguanta 1920 en pantalla (`194`) |
| 2. Ruido de homónimos | brutal | moderado | Ver `173` y `175` |
| 3. Reparto por escenario | — | — | Sobran 90 de Alcatraz y falta el Hotel Crillon (`190`) |
| 4. Lo que no pega visualmente | — | — | Color, ángulo, grano, anacronismo (`197`, `198`) |

## El umbral que de verdad manda

El recuento que decide no es el total, sino **las piezas útiles del caso**. Enron pasa el
umbral por goleada (379 ≫ 40) y aun así **no se puede ilustrar**, porque de esas 379 solo
once son de la historia. El resto son rascacielos de Houston, torres de alta tensión y
libros de contabilidad genéricos: material de stock con el que se hace un vídeo
intercambiable con cualquier otro vídeo sobre fraude contable.

> **Se pasa a guion con 40 piezas útiles Y 15 piezas del caso. Las dos condiciones, no
> una.** La clasificación está en `175`; la decisión de abandonar, en `176`.

## Un umbral por escenario, no solo global

Un sondeo puede dar 200 piezas y dejar un escenario a cero. El reparto por cupos de
`curar.py` lo saca a la luz antes del montaje:

**Salida real de `python curar.py lustig` (11-sep-2026):**

```
escenario        cupo  hay    elegidas
el_hombre        6     2      2 elegidas (2 en dominio publico)
torre            14    99     14 elegidas (11 en dominio publico)
paris            12    93     12 elegidas (12 en dominio publico)
chatarra         10    104    10 elegidas (2 en dominio publico)
falsificacion    12    158    12 elegidas (12 en dominio publico)
ley              10    117    10 elegidas (10 en dominio publico)
alcatraz         12    196    12 elegidas (11 en dominio publico)
viaje            8     74     8 elegidas (6 en dominio publico)
TOTAL 80 piezas · 66 en dominio publico · 14 piden atribucion
```

Ahí está el aviso: **`el_hombre` pedía 6 y solo hay 2.** De 988 piezas libres, el
protagonista aparece en dos. Todo lo demás sobra —196 candidatas para 12 huecos de
Alcatraz— y lo único que importa va corto. Cuando la columna `hay` queda por debajo del
`cupo`, ese escenario se reescribe o se cuenta con otro recurso (documento, mapa, cifra en
pantalla). No se rellena con una foto que no es de ahí.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dar el total por bueno | Enron: 379 piezas y un episodio imposible |
| Contar piezas sin filtrar resolución | El 13 % no aguanta pantalla completa |
| Umbral global sin cupo por escenario | 90 fotos de Alcatraz y ninguna del hotel |
| Bajar el mínimo «por esta vez» | Repetición visible; el espectador lo dice en comentarios |
| Descargar las 988 | Tiempo y disco tirados: se usan 80 (`190`) |

## Relacionado

`10` · `170` · `175` · `176` · `190` · `191` · `194`
