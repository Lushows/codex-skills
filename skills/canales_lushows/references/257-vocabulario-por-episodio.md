# 257 · Vocabulario por episodio

**Qué resuelve:** que cada episodio traiga su propio diccionario. El del Chapo no sirve
para Lustig: «torre» ahí no significa nada y «casilla» no existe. El banco de
`diccionario.py` es solo el valor por defecto, y el fichero que manda es
`<episodio>/vocabulario.py`, donde un humano declara qué significa cada palabra **en esta
historia concreta**.

---

## Cómo se enchufa

```python
# ep01-lustig/guion_visual.py
from vocabulario import V, CONTRAPESO, NUNCA_AUTO, PROHIBIDAS

diccionario.EPI_DIR = BASE                 # el material propio manda sobre el banco
diccionario.NUNCA_AUTO = NUNCA_AUTO
diccionario.PROHIBIDAS = PROHIBIDAS        # sin esto se usaba la del banco (`258`)
...
auto = generar(PALABRAS, ini, fin, reservados, vocab=V)
```

Cuatro líneas y las cuatro importan. `V` viaja por parámetro; las otras tres se **asignan
al módulo**, porque el generador las lee por nombre global. Es una asimetría fea y es la
que provocó que la lista de palabras prohibidas del episodio fuera decorativa durante
semanas.

```python
V_EPI = vocab if vocab is not None else V   # si no se pasa uno, el banco por defecto
```

## El tamaño de un vocabulario que funciona

`ep01-lustig`, 63,45 s de locución:

| | |
|---|---|
| entradas en `V` | 48 |
| recursos nombrados | 56 (13 entradas con alternativa) |
| palabras del guion | 155, 98 distintas |
| palabras con entrada | 54 apariciones · 46 distintas |
| colocadas por la capa AUTO | 27 |

Regla de bulto que sale de ahí: **una entrada por segundo de locución** es el punto donde
el diccionario empieza a mandar de verdad sobre el montaje. Menos, y la mano tiene que
escribirlo todo; más, y el generador descarta por falta de sitio.

| Bloque | Duración | Palabras | Con entrada | clave + auto + peso |
|---|---|---|---|---|
| muerte | 16,15 s | 38 | 11 | 4 + 8 + 5 = 17 |
| oficio | 6,73 s | 16 | 4 | 3 + 2 + 2 = 7 |
| nombre | 11,53 s | 27 | 11 | 3 + 4 + 2 = 9 |
| torre | 15,88 s | 41 | 16 | 5 + 8 + 3 = 16 |
| metodo | 13,16 s | 33 | 12 | 5 + 5 + 2 = 12 |

## El vocabulario lleva la regla del episodio dentro

En el 01, la regla manda sobre todo lo demás: cada afirmación pertenece a una de dos
columnas y la columna **se ve**.

```
LO QUE CONSTA    -> documento, monoespaciada, papel blanco, sello VERIFICADO
LO QUE SE CUENTA -> leyenda, serif de revista, papel amarillo, sello SIN FUENTE
```

Por eso el fichero está ordenado por columnas y no por orden alfabético: «según»,
«contado», «broma», «chatarrero», «vendió» viven juntas bajo el rótulo *la leyenda · SE
CUENTA*, y arrastran siempre su marca de columna (`254`). Un vocabulario ordenado por
orden alfabético es un vocabulario en el que nadie puede ver si una palabra está en la
columna equivocada.

## Las cuatro listas del fichero

| Lista | Qué declara | Tamaño en ep01 |
|---|---|---|
| `V` | palabra → (recurso o alternativas, clase) | 48 entradas |
| `PROHIBIDAS` | palabras que no se ilustran nunca (`258`) | 6 |
| `NUNCA_AUTO` | recursos que solo entran a mano (`251`) | 8 |
| `CONTRAPESO` | el cajón de relleno, por bloque (`255`) | 5 bloques × 5 |

Las cuatro son del episodio. Las cuatro tienen equivalente en el banco. Y las cuatro han
fallado alguna vez por la misma razón: se editó la del episodio y el código seguía
leyendo la del banco.

## Higiene: lo que no suena, sobra

```python
sordas = sorted(set(V) - set(p["limpia"] for p in PALABRAS))
print("entradas de V que NO suenan nunca:", sordas)
# -> ['nombre', 'vendi']
```

Dos entradas del episodio 01 son restos de una versión anterior del guion. No hacen daño
—nunca se activan— pero inflan el recuento y engañan al que lea el fichero buscando por
qué una palabra no salió. Si el guion cambia, el vocabulario se repasa.

## Cuándo conviene heredar del banco

Casi nunca para `V`, siempre para las clases y las bandas. El banco define la gramática
del canal —qué es un héroe, cuánto dura un micro, dónde vive una cifra— y eso debe ser
idéntico en todos los episodios: si cambia por episodio, el canal deja de tener una forma
reconocible. Lo que cambia por episodio es el **léxico**, no la gramática.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Editar el vocabulario del banco pensando que es el del episodio | El bot sigue igual y nadie entiende por qué |
| Olvidar `diccionario.NUNCA_AUTO = NUNCA_AUTO` | Entran por diccionario piezas con cifras propias |
| Vocabulario alfabético | Nadie ve que una palabra está en la columna equivocada |
| Reutilizar tal cual el vocabulario de otro episodio | Palabras que no suenan y palabras clave sin imagen |
| Cambiar `CLASES` por episodio | El canal pierde su forma reconocible |
| Dejar entradas de un guion anterior | El recuento miente y el diagnóstico se desvía |

## Relacionado

`250` · `251` · `252` · `255` · `258` · `254` · `93`
