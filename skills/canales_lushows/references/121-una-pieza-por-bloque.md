# 121 · Una pieza por bloque

**Qué resuelve:** que el espectador note que la historia cambió de terreno antes de que
la voz se lo diga. La pieza musical se cambia cuando cambia lo que el episodio ESTÁ
HACIENDO, no cuando el montador se aburre de la que suena.

---

## El principio

Un documental corto no tiene capítulos, tiene **bloques**: tramos con una función
narrativa distinta. El canal ya los declara en `guion_visual.py`, y sus límites los pone
la locución aprobada — salen de los silencios medidos en `tiempos.json`, no del montaje.

La música se cuelga de esa misma estructura. Una pieza por bloque, declarada en un
diccionario, igual que el relieve de la voz o los destellos:

```python
# bloque -> (pieza, intensidad 0-1)
MUSICA = {
    "muerte": ("mus_expediente", 0.55),   # el documento: sobrio
    "oficio": ("mus_expediente", 0.85),   # "aprendiz de vendedor": el golpe
    "nombre": ("mus_expediente", 0.45),   # se retira: aquí manda la voz
    "torre":  ("mus_sospecha",   0.72),   # la leyenda, con su cuarta aumentada
    "metodo": ("mus_cierre",     0.88),   # el método del episodio
}
```

Cinco bloques, **tres piezas**. Eso no es pobreza de material: la pieza cambia solo dos
veces en 63 s, y cada cambio significa algo.

## Dónde cambia la pieza en el episodio 01

| Bloque | s | Pieza | Por qué esa |
|---|---|---|---|
| `muerte` | 0,00–16,15 | `expediente` | Se lee un documento. Ostinato, sin opinión |
| `oficio` | 16,15–22,88 | `expediente` | Mismo terreno, **solo sube de intensidad** |
| `nombre` | 22,88–34,41 | `expediente` | Mismo terreno, se retira bajo la voz densa |
| `torre` | 34,41–50,29 | **`sospecha`** | 🔴 Aquí el episodio pasa de lo que CONSTA a lo que se CUENTA |
| `metodo` | 50,29–63,45 | **`cierre`** | Se enuncia el método: es el remate |

El cambio de `expediente` a `sospecha` cae exactamente donde el guion deja de estar
probado. `sospecha` usa el mismo bajo en re, pero el acorde lleva la **cuarta aumentada**
(`Ab3` contra `D2`): el intervalo que el oído lee como "algo no encaja". El espectador no
sabe nombrarlo y aun así deja de creerse la historia al 100%. Esa es toda la técnica.

> **Regla:** una pieza nueva SOLO entra donde ya hay una frontera de bloque **y** un
> cambio de estatus de la información. Si solo cambia el tema pero no el estatus, se
> cambia la intensidad (`120`), no la pieza.

## Cuántas piezas caben

| Duración | Piezas distintas | Cambios |
|---|---|---|
| Vertical 60 s | **1** | ninguno (`128`) |
| Episodio 6-8 min | 3 | 2-3 |
| Episodio 12-15 min | **4, tope 5** | 4-6 |

Por encima de cinco piezas el episodio deja de tener sonido propio y suena a recopilación.
La forma correcta de estirar el material no es componer más, es variar (`127`).

## La implementación

Cada bloque genera su propia entrada en `PISTAS`. No hay una "pista de música" global: hay
tantas como bloques, cada una con su archivo, su ventana y su ganancia.

```python
CRUCE = 1.2          # segundos de solape al cambiar de pieza

def pistas_musica():
    """(archivo, inicio, duración, ganancia, bucle) por cada bloque."""
    fuera = []
    for e in ESCENAS:
        pieza, fuerza = MUSICA.get(e["id"], ("mus_expediente", 0.5))
        ini = max(0.0, e["ini"] - CRUCE / 2)
        dur = (e["fin"] - ini) + CRUCE / 2
        # 0,34 es el nivel base medido para quedar 14 LU bajo la voz
        fuera.append((pieza, ini, dur, round(0.34 * fuerza, 3), True))
    return fuera

PISTAS = pistas_musica() + [ ... ]   # y encima el room tone, ambientes y picos
```

`bucle=True` importa: las piezas del canal duran **22 a 27 s medidos** (`expediente`
26,99 · `sospecha` 26,61 · `cierre` 22,57) y los bloques duran más. Sin
`-stream_loop -1` la música se acaba a mitad de bloque y el silencio se lee como avería.

## Dos bloques seguidos con la misma pieza

Es lo normal, no un defecto. `muerte`, `oficio` y `nombre` comparten `expediente` durante
34 s. Lo que evita que canse no es cambiar de archivo, es que la **intensidad** va 0,55 →
0,85 → 0,45: el mismo material suena a tres cosas distintas (`120`, `127`).

Cuando dos bloques seguidos comparten pieza, el cruce entre ellos es un simple cambio de
nivel y **no hace falta rampa de equipotencia** — basta el trapecio lineal. La `qsin` solo
es obligatoria cuando las dos piezas son materiales distintos (`122`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Cambiar de pieza a media escena | Se oye el corte y el espectador busca qué pasó en pantalla |
| Una pieza por escena visual | 20 cambios en 12 min: la banda sonora se vuelve ruido |
| Cambiar de pieza por cambiar | El recurso se gasta y el cambio que SÍ importa no se nota |
| Pieza sin `-stream_loop -1` | La música muere a mitad de bloque y suena a fallo técnico |
| Poner la frontera musical donde manda el montaje | Se pelea con la voz: los límites los pone `tiempos.json` |
| Cinco piezas distintas en 6 minutos | Episodio sin identidad sonora; nada vuelve, nada se reconoce |

## Relacionado

`120` intensidad · `122` el cruce · `126` el tema · `127` variación · `82` componer
