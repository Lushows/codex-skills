# 14 · Encadenar elementos

**Qué resuelve:** el cuadro se vacía entre un elemento y el siguiente. Cada uno hace su
vida por su cuenta y el montaje se lee como una lista, no como una cadena.

---

## Los tres modos de enganche

| Modo | Solape | Posición | Para qué |
|---|---|---|---|
| **Relevo** | 0,20-0,40 s | distinta | El caso general. B ya está dentro cuando A se va |
| **Solape** | 0,80-1,50 s | distinta | Cuando A y B tienen que leerse juntos (cifra + su fuente) |
| **Sustitución** | 0,00-0,08 s | **la misma** | Estados de una serie: contador, cifra que cambia, ficha que se completa |

**La regla que los une:** entre el final de A y el principio de B nunca puede haber
tiempo muerto. O se pisan, o empatan al fotograma. Nunca se separan.

## Relevo: el caso general

B entra 0,2-0,4 s antes de que A muera. Durante ese solape hay dos elementos vivos, que
es lo que sube la simultaneidad sin añadir material (`12`).

```python
# A muere en 21,90 (entra en 19,90 + dura 2,0). B tiene que entrar antes de 21,70.
{"r": "tuneladora",   "desde": 0.15, "dura": 2.0, ...},                    # A
{"r": "herramientas", "ancla": "ventilación.", "offset": -0.2, "dura": 1.2, ...},  # B
```

**Cómo se calcula el `offset` de B:** se mira el segundo de su palabra en
`tiempos.json`, se resta el final de A y, si la diferencia pasa de 0,4 s, se baja el
`offset` hasta que el solape caiga en la ventana. Si hace falta bajarlo de −0,6 s, el
problema no es el enganche: es que falta un elemento entre los dos.

### La dirección importa

| A sale por... | B entra por... | Cómo se lee |
|---|---|---|
| izquierda | derecha | **Contragolpe**: cambio de tema, corte de idea |
| izquierda | izquierda | **Arrastre**: B empuja a A fuera. Continuidad, misma idea |
| fundido | fundido | Neutro: usar sólo cuando A y B no se relacionan |
| abajo | arriba | **Cierre**: sirve para rematar un bloque |

Alternar. Tres contragolpes seguidos hacen que el cuadro parezca un péndulo.

## Solape: cuando los dos tienen que estar

La cifra y su fuente, el retrato y su ficha, el mapa y su ruta. Conviven 0,8-1,5 s y se
van escalonados: **primero el que aporta menos**. Si el principal muere antes que su
rótulo, el rótulo se queda huérfano explicando algo que ya no está.

```python
{"r": "cara_ovalo", "ancla": "hombre", "offset": -0.15, "dura": 2.6, ...},  # principal
{"r": "rot_alias",  "ancla": "hombre", "offset":  0.05, "dura": 2.0, ...},  # muere antes
```

## Sustitución: el mismo sitio, otro contenido

Misma `x`, misma `y`, mismo `w` (o creciente). El elemento saliente lleva `fade_out`
corto — 0,08-0,12 s — y su `dura` termina exactamente donde arranca el siguiente.

**El error concreto que hay en el piloto:** `cont_02` arranca en "mil" con `dura` 0,55,
y `cont_05` entra en "quinientos", 0,25 s después. Los dos estados se ven encima 0,30 s
al 100% y la cifra queda emborronada durante siete fotogramas y medio.

La corrección es calcular la duración contra el tiempo real de la palabra siguiente:

```python
import json
palabras = json.load(open("audio/tiempos.json", encoding="utf-8"))["palabras"]

def t(palabra, desde=0.0):
    """Segundo de la primera aparición de una palabra a partir de 'desde'."""
    return next(p["t"] for p in palabras if p["limpia"] == palabra and p["t"] >= desde)

def serie(anclas, cola=1.9):
    """Duraciones que empalman al fotograma. La última se queda 'cola' segundos."""
    ts = [t(a) for a in anclas]
    return [round(ts[i+1] - ts[i], 2) for i in range(len(ts) - 1)] + [cola]

print(serie(["mil", "quinientos", "metros", "túnel"]))
```

Sobre el piloto devuelve `[0.14, 0.41, 0.41, 1.9]` para las palabras 19,874 · 20,011 ·
20,424 · 20,837. Dos cosas: las duraciones declaradas (0,55 / 0,50 / 0,50) están mal, y
el primer paso sale en **0,14 s**, por debajo del piso de 0,20 s. Cuando eso ocurre no
se fuerza: la serie tiene un paso de más para lo que dura la frase. Aquí se juntan los
dos primeros estados y quedan tres pasos de 0,55 / 0,41 / 1,90.

## Encadenar una escena entera

Orden de trabajo, en este orden y no otro:

1. Se declaran los elementos con sus anclas y sus duraciones por tipo (`13`).
2. Se ejecuta el auditor (`17`) y se leen los huecos.
3. Cada hueco se cierra con el modo que corresponda: relevo si son elementos distintos,
   sustitución si es una serie.
4. Se vuelve a ejecutar. Si aparece un hueco nuevo al final de la escena, es que se
   adelantó demasiado el último elemento: se alarga su `dura`, no se mueve su `offset`.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Encadenar por `desde` en vez de por ancla | Al retocar la voz se descuadra toda la cadena |
| Solape de más de 1,5 s entre dos principales | Se pisan y compiten: ya no es enganche, es amontonar |
| Sustitución con `fade_out` por defecto (0,40) | Dos estados visibles a la vez: la cifra se emborrona |
| El rótulo sobrevive a su elemento | Explica algo que ya no está en pantalla |
| Bajar el `offset` por debajo de −0,6 s para tapar un hueco | El elemento entra antes de que la voz lo justifique |
| Tres relevos seguidos con la misma dirección | El cuadro se lee como una cinta transportadora |

## Relacionado

`11` el hueco prohibido · `12` capas simultáneas · `13` ciclo de vida del elemento ·
`15` rampa de ritmo · `32` entradas y salidas · `39` sincronizar gesto y palabra
