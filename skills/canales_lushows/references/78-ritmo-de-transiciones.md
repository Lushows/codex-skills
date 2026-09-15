# 78 · El ritmo de las transiciones

**Qué resuelve:** planificar la secuencia completa de uniones de un episodio para que
ninguna se repita seguida, para que la más fuerte caiga donde importa y para que el
espectador nunca aprenda el patrón.

---

## Las tres reglas

1. **Nunca la misma dos veces seguidas.** Ni la misma familia. Dos barridos de papel
   consecutivos convierten el recurso en plantilla.
2. **Nunca dos uniones no-duras pegadas.** Entre una transición y la siguiente hay al
   menos **una unión a corte duro** y, en tiempo, **25 segundos**.
3. **La más fuerte, una sola vez, en el giro.** El tachado rojo (`77`) marca el momento
   en que el protagonista cruza la raya. Si se gasta antes, el giro llega sin marca.

## La partitura de uniones

Cada unión tiene un **peso de 0 a 3**. El episodio no se planifica transición a
transición sino como una curva que sube hacia el giro y baja hacia el remate:

| Peso | Qué es | Ejemplos |
|---|---|---|
| **0** | Corte duro pelado | Cambio de plano dentro del mismo tema |
| **1** | Corte duro + sonido adelantado (`75`) | Cambio de lugar suave |
| **2** | Objeto que cruza (`73`), barrido de papel (`71`), flash o golpe (`74`) | Cambio de lugar o de tiempo |
| **3** | Tachado rojo (`77`), pase de página, match cut (`72`) | El giro del relato |

Un episodio de 6 escenas (5 uniones) sano se ve así:

```
peso  3 |                    ███
      2 |        ███                      ███
      1 |  ███              (cierre 0,80 s con fadeblack)
      0 |              ███
        +----------------------------------------
unión     1→2    2→3   3→4   4→5   5→6      fin
```

| Unión | Separa | Peso | Recurso | Duración |
|---|---|---|---|---|
| 1→2 | gancho → contexto | 1 | corte duro + `tr_whoosh` −0,14 s | 0 |
| 2→3 | contexto → construcción | 2 | maletín que cruza (`73`) | 0,36 s |
| 3→4 | construcción → **el giro** | 3 | tachado rojo (`77`) | 0,44 s |
| 4→5 | giro → caída | 0 | corte duro pelado | 0 |
| 5→6 | caída → remate | 2 | golpe de negro (`74`) | 0,20 s |
| fin | remate → negro | — | `fadeblack` + `tr_cierre` | 0,80 s |

Suma: **1,00 s** de transición en un episodio de 90 s. Ese es el orden de magnitud
correcto: **por debajo del 1,5% del metraje**.

## El vacío después del pico

Fíjate en la unión 4→5: es la más pelada de todas y va **justo después** de la más
fuerte. No es descuido, es contraste. Después de un peso 3 el episodio necesita un corte
seco, igual que después de un grito hace falta una frase en voz baja. Si detrás del
tachado rojo se pone otro efecto, el tachado se devalúa.

## El sonido también se repite

Aunque las cinco uniones fueran a corte duro, si las cinco suenan con el **mismo**
`tr_whoosh` el oído lo memoriza a la tercera. Se varía sin ampliar la biblioteca,
cambiando el tono del mismo WAV:

```
# el mismo whoosh, cuatro semitonos más grave y un pelo más lento
[2:a]asetrate=48000*0.86,aresample=48000,atempo=1.06,volume=0.62,adelay=51860:all=1[wh]
```

Con `asetrate` entre **0,84 y 1,18** el mismo archivo da cinco efectos distintos. Fuera
de ese rango empieza a sonar a truco.

## Auditar el episodio antes de renderizar

Las uniones se declaran en el guion visual, no se improvisan:

```python
UNIONES = [
    {"de": "gancho",  "a": "contexto",     "peso": 1, "tipo": "duro+sfx", "d": 0.00},
    {"de": "contexto","a": "construccion", "peso": 2, "tipo": "elemento", "d": 0.36},
    {"de": "construccion","a": "giro",     "peso": 3, "tipo": "tachado",  "d": 0.44},
    {"de": "giro",    "a": "caida",        "peso": 0, "tipo": "duro",     "d": 0.00},
    {"de": "caida",   "a": "remate",       "peso": 2, "tipo": "golpe",    "d": 0.20},
]

def auditar(uniones, escenas):
    tot = sum(u["d"] for u in uniones)
    dur = sum(e["fin"] - e["ini"] for e in escenas)
    print(f"transición: {tot:.2f} s de {dur:.2f} s = {100*tot/dur:.1f} %  (objetivo < 1,5 %)")
    for a, b in zip(uniones, uniones[1:]):
        if a["tipo"] == b["tipo"] != "duro":
            print(f"  ! repetida seguida: {a['tipo']} en {a['de']}→{a['a']} y {b['de']}→{b['a']}")
        if a["d"] > 0 and b["d"] > 0:
            print(f"  ! dos uniones no-duras pegadas: {a['a']}")
    if sum(1 for u in uniones if u["peso"] == 3) > 1:
        print("  ! más de un peso 3: el giro pierde su marca")
```

## Episodios largos (8-12 minutos)

El presupuesto no crece igual que la duración: **una transición no-dura cada 90-120
segundos**, y un único peso 3 aunque el episodio dure 12 minutos. Lo que sí crece es la
variedad de la capa sonora, porque son más uniones a corte duro.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Elegir la transición al llegar a cada unión | Salen tres iguales sin que nadie se dé cuenta hasta ver el montaje |
| Dos pesos 3 en un episodio | Ninguno de los dos marca nada |
| Poner algo fuerte justo después del giro | Devalúa el giro y satura al espectador |
| Repetir el mismo efecto sonoro en todas las uniones | El oído aprende el patrón antes que el ojo |
| Subir el porcentaje de transición "porque el episodio es largo" | Un episodio largo necesita más historia, no más efectos |

## Relacionado

`70` · `71` · `73` · `74` · `75` · `77` · `93` · `17`
