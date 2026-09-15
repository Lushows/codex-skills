# 114 · Modos y color

**Qué resuelve:** elegir el color emocional de un tramo cambiando **una sola nota**. Un
modo no es una escala exótica: es la escala de siempre con un grado movido, y ese grado
movido es todo el carácter. Aquí están los tres que usa el canal, con sus frecuencias.

---

## Los tres modos del canal, medidos

Todos con tónica **Re4 = 293,66 Hz**. Salida real de `escala()` (abajo):

| Modo | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| **Dórico** | Re4 293,66 | Mi4 **329,63** | Fa4 349,23 | Sol4 392,00 | La4 440,00 | **Si4 493,88** | Do5 523,25 |
| **Eólico** | Re4 293,66 | Mi4 **329,63** | Fa4 349,23 | Sol4 392,00 | La4 440,00 | **Si♭4 466,16** | Do5 523,25 |
| **Frigio** | Re4 293,66 | **Mi♭4 311,13** | Fa4 349,23 | Sol4 392,00 | La4 440,00 | Si♭4 466,16 | Do5 523,25 |

Entre dórico y eólico hay **una nota y 27,72 Hz**. Entre eólico y frigio, **una nota y
18,50 Hz**. Eso es todo lo que separa "melancólico pero digno" de "amenaza".

## Qué evoca cada uno

| Modo | Grado que lo define | Color | Tramo |
|---|---|---|---|
| **Eólico** (menor natural) | ♭6 (Si♭) y ♭7 (Do) | Melancolía sin drama. Neutro y serio | **El colchón por defecto.** Exposición, documento |
| **Dórico** | 6ª mayor (Si♮) sobre modo menor | Menor con una rendija de luz. Digno, no triste | La víctima que todavía cree · el ascenso |
| **Frigio** | ♭2 (Mi♭), a un semitono de la tónica | Amenaza. El ♭2 roza contra la tónica (`113`) | La trampa · la persecución · lo irreversible |
| Lidio | #4 (Sol#) | Irreal, flotante. Lleva el tritono dentro | Rara vez. La fantasía del estafador |
| Mixolidio | ♭7 sobre modo mayor | Abierto, sin sensible. Nada cierra | El auge, antes de la grieta |
| Locrio | ♭2 y ♭5 | Sin suelo: la quinta no sostiene | Nunca como colchón. 1-2 compases como mucho |

> Honestidad: los nombres son griegos, pero los modos tal como los usamos son
> **construcción medieval y renacentista europea** y su carga emocional es convención de
> ese repertorio. La única parte con base física es la del frigio: su ♭2 está dentro de
> la banda crítica de la tónica y produce batido real (`113`).

## El generador

```python
MODOS = {"jonico":    [0,2,4,5,7,9,11],   "dorico": [0,2,3,5,7,9,10],
         "frigio":    [0,1,3,5,7,8,10],   "lidio":  [0,2,4,6,7,9,11],
         "mixolidio": [0,2,4,5,7,9,10],   "eolico": [0,2,3,5,7,8,10],
         "locrio":    [0,1,3,5,6,8,10]}

def escala(tonica, modo, n=8):
    """'D4','frigio' -> ['D4','Eb4','F4','G4','A4','Bb4','C5','D5']"""
    base, p = semitono(tonica), MODOS[modo]       # semitono() y nombre(): ver 110
    return [nombre(base + p[i % 7] + 12 * (i // 7)) for i in range(n)]

def recorrido(modo, T=3.4):
    """La escala sobre el pie del canal. 10 notas · 8,39 s (medido)."""
    notas = [(i * 0.85, n, 1.5, 0.50) for i, n in enumerate(escala("D4", modo))]
    return notas + [(0.0, "D2", 3.0, 0.90), (T, "D2", 3.0, 0.90)]

for m in ("dorico", "frigio", "eolico"):
    tocar(recorrido(m), f"114_{m}.wav")
```

Las tres salen con **exactamente las mismas 10 notas y los mismos 8,39 s**. Solo cambia
la altura de una o dos. Escuchadas seguidas, la diferencia es obvia; leídas en la lista
de notas, casi no se ve. Ese es el punto del módulo.

## Qué modo es el piloto (y por qué funciona)

Contando las notas que suenan de verdad en `piano.py`:

| Pieza | Grados que aparecen | Grados que **faltan** | Modo |
|---|---|---|---|
| `_expediente` | 1 · 2 · ♭3 · 5 · ♭6 | **4 y ♭7** | Eólico incompleto |
| `_sospecha` | 1 · ♭3 · **♭5** · ♭6 | 2, 4, ♭7 | Eólico con el 5.º rebajado |
| `_cierre` | 1 · 2 · ♭3 · 5 · ♭6 · ♭7 | 4 | Eólico completo |

Dos hallazgos que conviene no perder:

1. **`_expediente` no tiene 7.º grado.** Ni Do♮ ni Do#. El oído no puede ni empezar a
   preguntarse si va a haber cadencia, porque la nota que decide eso nunca suena. Es la
   raíz técnica de por qué el colchón puede durar minutos sin cerrar (`111`).
2. **En ninguna de las tres piezas hay un Do# (277,18 Hz).** Ni siquiera en `_cierre`,
   que es la que remata: cierra por camino modal (Re m → Fa → Si♭ → La m), no por
   dominante. El canal no usa la sensible en ningún sitio, y eso es una decisión.

## Cómo se cambia de modo sin que se note el corte

No se transpone: **se mueve un solo grado y se deja el bajo quieto.**

```python
# El mismo ostinato, tres colores. Solo cambia una nota del acorde.
COLOR = {
    "eolico": ["D3","F3","A3"],      # neutro
    "dorico": ["D3","F3","B3"],      # 6ª mayor: se abre  (B3 = 246,94 Hz)
    "frigio": ["D3","F3","Eb4"],     # ♭2 arriba: amenaza (Eb4 = 311,13 Hz)
}
tocar(ostinato(compases=4, acorde=COLOR["frigio"]), "frigio.wav")
```

⚠️ El `Eb4` del frigio va **al nivel de la 2ª menor, no del acorde**: `0,16`, no `0,36`
(`113`). Con el ♭2 al nivel normal, la pieza deja de inquietar y pasa a sonar mal.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Cambiar de modo cambiando también la raíz | Se oye como cambio de tono, no como cambio de color (`110`) |
| Frigio en un bloque entero | El roce del ♭2 cansa el oído en menos de un minuto |
| ♭2 del frigio al nivel del acorde | Deja de ser color y pasa a ser error de afinación |
| Meter el 7.º grado en el colchón "para completar la escala" | Se abre la puerta a la cadencia y el colchón empieza a cerrar solo |
| Locrio como colchón | La quinta disminuida no sostiene: el oído no encuentra suelo |
| Llamar "griego" al color emocional del modo | Los nombres son griegos, el uso es medieval europeo y la carga es convención |
| Cambiar dos grados a la vez | Ya no es cambio de color: es otra pieza |

## Relacionado

`110` tonalidad y significado · `111` la armonía que no resuelve · `112` el ostinato ·
`113` intervalos que inquietan · `115` progresiones por tramo · `119` el lenguaje de una época
