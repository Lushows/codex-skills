# 110 · Tonalidad y significado

**Qué resuelve:** la pregunta "¿en qué tono compongo este episodio?" y, antes de eso,
si la pregunta significa algo. Casi todo lo que se lee sobre el carácter de las
tonalidades es **tradición**, no física — y conviene saber exactamente dónde está la
frontera antes de tomar una decisión creativa apoyándose en ella.

---

## Lo que sí es físico

| Hecho | Medible | Consecuencia práctica |
|---|---|---|
| **Altura absoluta** | Sí. `hz()` la da | Re2 = 73,42 Hz pesa; Re4 = 293,66 Hz no. Subir una octava es multiplicar por 2 |
| **Mayor vs menor** | El intervalo cambia: 3ªM = razón 1,2599 · 3ªm = 1,1892 | Son dos sonidos distintos, no dos etiquetas |
| **Registro y voz** | La energía se corre de banda (`117`) | Un tema en Re2 no pelea con la locución; en Re4 sí |
| **Batido entre notas cercanas** | Sí: dos senos a 293,66 y 311,13 Hz baten a 17,5 Hz | Es lo que hace áspera la segunda menor (`113`) |

## Lo que es convención

El catálogo afectivo de las tonalidades —"re menor es grave y solemne", "mi bemol mayor
es heroico"— viene de tratados: Charpentier (c. 1690), Mattheson (1713), Schubart
(escrito 1784-85). **Se contradicen entre ellos**, y eso ya es la prueba.

Pero hubo un motivo real detrás: se escribieron bajo temperamentos **desiguales**,
donde el tamaño de las terceras cambiaba según la tonalidad. Ahí Fa# mayor sonaba de
verdad distinto de Do mayor. Con el temperamento igual —que es exactamente lo que
implementa `hz()`, `440 · 2^(n/12)`— esa diferencia **desaparece por construcción**.

Y en nuestro motor desaparece dos veces: `ARMONICOS` aplica los mismos cinco
multiplicadores y las mismas caídas a cualquier nota. Transponer no cambia el timbre.
**Transponer es multiplicar todas las frecuencias por la misma constante y nada más.**

> Lo honesto: mayor/menor sí tiene un efecto fuerte y consistente en nuestro público,
> aunque también sea aprendido. Que "re menor" sea más serio que "do menor" no lo es.

## El transpositor

```python
SEMIS  = {"C":0,"D":2,"E":4,"F":5,"G":7,"A":9,"B":11}
NOMBRE = ["C","C#","D","Eb","E","F","F#","G","Ab","A","Bb","B"]

def semitono(nota):
    """'Bb1' -> 22. Semitonos absolutos desde Do0."""
    n, i, alt = nota[0].upper(), 1, 0
    while i < len(nota) and nota[i] in "#b":
        alt += 1 if nota[i] == "#" else -1
        i += 1
    return SEMIS[n] + alt + int(nota[i:]) * 12

def nombre(s):
    return NOMBRE[s % 12] + str(s // 12)

def transponer(notas, semis):
    """La misma pieza, otro tono. Lo único que cambia es la frecuencia."""
    return [(t, nombre(semitono(n) + semis), d, v) for t, n, d, v in notas]
```

Ejecutado sobre la frase base de `piano.py`:

```
Dm   ['D2', 'D3', 'F3', 'A3', 'A4', 'F4']
C#m  ['C#2','C#3','E3','Ab3','Ab4','E4']   (-1 semitono)
Fm   ['F2', 'F3', 'Ab3','C4', 'C5', 'Ab4'] (+3 semitonos)
```

⚠️ `nombre()` escribe siempre con bemoles: el Sol# de Do# menor sale como `Ab3`. Suena
idéntico (temperamento igual) pero la **grafía** es incorrecta. Si alguien va a leer la
partitura, corregir a mano; si solo va a sonar, da igual.

## Lo que sí decide el tono: el registro, no el nombre

La decisión real no es "re menor o mi menor", es **en qué octava vive el bajo**.

| Raíz | Hz | Qué pasa |
|---|---|---|
| `D1` | 36,71 | Un móvil no lo reproduce. Solo sirve para impactos (`84`) |
| `A1` | 55,00 | Suelo absoluto. Solo como final de un descenso (`115`) |
| **`Bb1`** | **58,27** | Suelo habitual. Se siente en auriculares, no molesta en móvil |
| **`D2`** | **73,42** | La raíz del piloto. Es el sitio |
| `A2` | 110,00 | Entra en la región donde la voz tiene sus fundamentales |
| `D3` | 146,83 | Ya no es bajo: es acompañamiento medio |

**Re menor con raíz en Re2 (73,42 Hz) es la tonalidad del canal** y no se cambia entre
episodios. No por lo que "significa" re menor, sino porque 73,42 Hz es un buen suelo y
porque un canal con una raíz fija suena a canal.

## Cuándo sí transponer

| Caso | Movimiento | Por qué |
|---|---|---|
| El episodio se cruza con otro (`122`) | ±2 semitonos | Que no suene a copia del anterior |
| Un tramo tiene que pesar más | −1 o −2 semitonos | Baja la raíz sin cambiar nada más |
| El vertical (`128`) | +3 a +5 semitonos | En altavoz de móvil, 73 Hz no existe |
| Dentro del mismo episodio | **nunca** | Se oye como que empezó otro vídeo (`82`) |

## La afinación de referencia

`hz()` está clavado en La4 = 440 Hz, que es la norma **ISO 16, de 1955**. En el París de
1890 de las *Gnossiennes* la referencia legal francesa era el *diapason normal* de 1859:
**La4 = 435 Hz**, unos **20 centésimas más bajo** (`1200·log2(435/440) = −19,8 cents`).

Se puede usar como recurso de época (`119`):

```python
import os, piano
_hz440 = piano.hz
piano.hz = lambda n: _hz440(n) * (435.0 / 440.0)     # diapasón de París, 1859
piano.MUESTRAS = os.path.join(piano.DEST, "_piano435")   # 🔴 OBLIGATORIO
```

La segunda línea no es opcional: `muestra()` cachea por **nombre de nota**, no por
frecuencia. Sin cambiar la carpeta, el motor devuelve el `D2` a 440 que ya estaba en
disco y el cambio de afinación no ocurre — sin error, sin aviso.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Elegir tono por lo que "significa" en un tratado de 1713 | Decisión sin efecto: en temperamento igual todos los tonos son el mismo sonido movido |
| Cambiar de tonalidad a mitad de episodio | Se percibe como otro vídeo, no como desarrollo |
| Bajar la raíz a Re1 (36,71 Hz) para "que pese más" | En móvil no suena nada; se pierde el colchón entero |
| Transponer y no cambiar `MUESTRAS` con otra afinación | El caché sirve las notas viejas y nada cambia, en silencio |
| Fiarse de la grafía de `nombre()` | Escribe bemoles siempre: Sol# sale como Lab |
| Presentar "re menor = solemne" como dato | Es tradición documentada, no medida. Decirlo así |

## Relacionado

`111` la armonía que no resuelve · `113` intervalos que inquietan · `114` modos y color ·
`117` dejarle sitio a la voz · `119` el lenguaje de una época · `82` música por código
