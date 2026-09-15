# 235 · Palabras repetidas y anclaje

**Qué resuelve:** el vocabulario visual no crece al mismo ritmo que el guion. Un minuto son
155 palabras y 48 entradas de diccionario; doce minutos son unas 1.760 palabras y **el
mismo diccionario**, porque el episodio sigue tratando del mismo hombre, la misma torre y
el mismo certificado. Las palabras que disparan imagen vuelven una y otra vez, y el motor
tiene dos formas distintas de fallar con ellas: **no colocar** y **colocar en el sitio
equivocado**.

---

## El ritmo real, medido

`ep01-lustig`, 63,45 s de locución ya grabada:

| | Medido | A doce minutos |
|---|---|---|
| Palabras de locución | 155 → **146,6 /min** | ~1.760 |
| Entradas del vocabulario | 48 | 48, salvo que se amplíe |
| Palabras del guion que están en el vocabulario | 46 distintas | — |
| Disparos (apariciones de esas palabras) | 54 → **51,1 /min** | **~612** |
| Entradas con **una sola** opción | **35 de 48** (73 %) | — |
| Entradas con 2 opciones | 11 | — |
| Entradas con 3 opciones | 2 | — |

El número que manda es el último: tres de cada cuatro palabras del diccionario tienen
**una sola imagen**. Una imagen no se puede repetir antes de 25 s (`253`). Así que cada
palabra de un solo recurso sólo puede disparar **una vez cada 25 segundos**, diga el guion
lo que diga.

## Fallo 1 · la palabra vuelve y no hay con qué

Cuántos de los 54 disparos caen a menos de 25 s de una aparición anterior **de la misma
palabra**:

```
apariciones repetidas a <25 s : 7 de 54 (13 %)
```

| Palabra | Apariciones | Máx. en 25 s | Opciones | Faltan |
|---|---|---|---|---|
| miller | 3 | 3 | 1 | **2** |
| aprendiz | 2 | 2 | 1 | 1 |
| años | 2 | 2 | 1 | 1 |
| vendió | 2 | 2 | 1 | 1 |
| chatarrero | 2 | 2 | 1 | 1 |
| llamaba | 2 | 2 | **2** | 0 |
| hombre | 2 | 1 | 2 | 0 |

**Seis alternativas de menos en sesenta y tres segundos.** Y la aritmética es directa: una
palabra necesita tantas opciones como veces aparezca dentro de una ventana de 25 s.

```python
opciones_necesarias(w) = max(#apariciones de w en cualquier ventana de 25 s)
```

Las que no las tienen no producen un error: producen un **hueco**, porque `generar()` hace
`continue` y sigue con la palabra siguiente. El episodio queda con menos elementos y nadie
sabe por qué.

Doce minutos no multiplican el problema por once: lo multiplican **más**. El número de
palabras crece linealmente con la duración, pero el número de palabras *distintas* no —
un documental de doce minutos sobre Lustig dice «torre» cuarenta veces, no cuarenta
palabras nuevas. Con «torre» cada 18 segundos y dos opciones declaradas, la mitad de las
veces que se nombra la torre no entra nada.

> La salida **no** es bajar la ventana de 25 s: eso convierte huecos en repeticiones
> visibles, que es la moneda que el espectador sí nota (`253`). La salida es **material**,
> y concretamente material *por palabra*: no basta con que el cajón tenga 560 piezas si
> «torre» sigue teniendo dos.

## Fallo 2 · la palabra vuelve y el elemento aterriza en la otra

Este es peor porque no deja hueco: deja el elemento **en el sitio equivocado** y con buena
cara. `motor.py` y `diccionario.resolver()` resuelven un ancla así:

```python
cand = [p for p in palabras if p["limpia"] == anc and t0 - 0.6 <= p["t"] <= t1]
i = ele.get("ancla_n", 0)
base = cand[min(i, len(cand) - 1)]["t"] if cand else t0
```

Sin `ancla_n`, **la primera**. Y `generar()`, que recorre el guion palabra por palabra y
puede perfectamente decidirse por la segunda aparición —porque la primera cayó dentro de
`paso_min`, o porque el hueco del cuadro sólo estaba libre después—, emite esto:

```python
# diccionario.py:579
{"r": recurso, "ancla": w, "offset": -0.16, "dura": round(t1 - t0, 2), ...}
```

**Sin `ancla_n`.** El generador eligió un instante y el motor renderiza otro, y nadie los
compara. Medido sobre la escena `torre`, donde «chatarrero» se dice dos veces:

```
ocurrencias de "chatarrero" en la escena torre: [40.286, 44.009]
lo que emite generar() hoy       -> (40.13, 42.53)
si emitiera ancla_n=1            -> (43.85, 46.25)
salto silencioso                 -> 3.72 s
```

Tres segundos y siete décimas. En un episodio de doce minutos eso es un recorte de la
chatarrería apareciendo sobre una frase que habla de otra cosa. Hoy el piloto se salva por
poco: **2 de sus 47 anclas son ambiguas** —«vendió» y «chatarrero», las dos en `torre`— y
sólo una declara `ancla_n`. La otra coincide por casualidad con la primera aparición.

El arreglo es una clave más en el elemento generado:

```python
# el generador ya sabe en que aparicion esta: que lo diga
n = sum(1 for q in palabras if q["limpia"] == w and ini - 0.6 <= q["t"] < t)
fuera.append({"r": recurso, "ancla": w, "ancla_n": n, "offset": -0.16, ...})
```

## Por qué esto empeora con escenas más largas

Las anclas se buscan **dentro de la escena** (`t0-0,6 ≤ t ≤ t1`). Esa ventana es la que
protege de la ambigüedad: una palabra dicha en el minuto 2 y en el minuto 9 no compite,
porque están en escenas distintas. Medido por escena en el piloto:

| Escena | Duración | Palabras | Repetidas dentro | Anclas | Ambiguas |
|---|---|---|---|---|---|
| muerte | 16,15 s | 38 | 7 | 9 | 0 |
| oficio | 6,73 s | 16 | 0 | 5 | 0 |
| nombre | 11,53 s | 28 | 4 | 7 | 0 |
| **torre** | **15,88 s** | **41** | **6** | **15** | **2** |
| metodo | 13,16 s | 33 | 4 | 11 | 0 |
| | | **31 de media** | | **47** | **2 (4 %)** |

La escena más larga es la única con anclas ambiguas. No es coincidencia: la ambigüedad
crece con las palabras que caben dentro. **Escenas de doce segundos son también una defensa
del anclaje**, no sólo un ritmo. Una escena de cuarenta segundos en un episodio largo
—porque el bloque «se dejó correr»— multiplica las palabras repetidas dentro y con ellas
las anclas que aterrizan en la aparición que no era.

## La lista que hay que tener antes de montar doce minutos

```python
# palabras del guion que el vocabulario NO cubre y salen mas de una vez:
# son candidatas a entrada nueva, no huecos
import collections, io, json
pal = json.load(io.open("epi/tiempos.json", encoding="utf-8"))["palabras"]
c = collections.Counter(p["limpia"] for p in pal)
falta = [(w, n) for w, n in c.items() if n >= 2 and w not in V and len(w) > 4]
print(sorted(falta, key=lambda z: -z[1])[:30])
```

Y la de al lado, que es la que de verdad decide:

```python
# palabras YA cubiertas que se quedan cortas de alternativas
for w in V:
    ts = [p["t"] for p in pal if p["limpia"] == w]
    pico = max((sum(1 for x in ts if a <= x < a + 25.0) for a in ts), default=0)
    opc = len(V[w][0]) if isinstance(V[w][0], list) else 1
    if pico > opc:
        print("%-14s pico %d en 25 s, tiene %d -> faltan %d" % (w, pico, opc, pico - opc))
```

Esa segunda lista se corre **antes de buscar material**, no después: dice exactamente
cuántas piezas hacen falta y de qué, que es lo contrario de bajar al archivo a ver qué
hay (`170`, `174`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Contar el cajón por total de piezas y no por palabra | 560 piezas y «torre» sigue teniendo dos |
| Bajar la ventana de 25 s cuando faltan alternativas | Huecos convertidos en repeticiones visibles (`253`) |
| Generar elementos sin `ancla_n` | El elemento aterriza en la primera aparición: 3,72 s de salto |
| Escenas largas en episodios largos | Más palabras repetidas dentro, más anclas ambiguas |
| Suponer que el vocabulario crece con el guion | Doce minutos dicen las mismas palabras más veces, no más palabras |
| Añadir alternativas que no son la misma cosa | El antirrepetición las agrupa por familia y se bloquean (`253`) |
| Dar por bueno un ancla porque el motor no avisó | Sólo avisa si no hay **ninguna** coincidencia, no si hay dos |
| Buscar material antes de contar los picos por palabra | Media jornada de archivo para las palabras que no lo necesitaban |

## Relacionado

`250` palabra → imagen: el método · `251` qué palabra merece imagen · `252` alternativas y
rotación · `253` la ventana antirrepetición · `241` resolución de anclas · `257`
vocabulario por episodio · `259` cuando el diccionario no basta · `231` el banco
acumulativo · `174` el umbral de piezas útiles
