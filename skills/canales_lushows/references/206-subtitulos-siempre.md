# 206 · Subtítulos siempre

**Qué resuelve:** el episodio largo vive del oído —`95` lo dice: se escribe para el
oído— y el corte vertical no. Se ve en silencio, en el metro, con el teléfono boca abajo
sobre la mesa. Sin subtítulo quemado el corte no existe. Este módulo saca los subtítulos
del material que el canal **ya tiene**, `tiempos.json`, y fija el agrupamiento, el tamaño
y el sitio con números medidos.

`editpro 414` resuelve la geometría de las tres capas de texto que se apilan abajo y por
qué el subtítulo quemado tiene que estar por encima del automático y del caption. Eso no
se repite. Aquí: **cómo se generan desde la locución de este canal y cómo se comprueba que
no parpadean**.

---

## El material ya está

La locución del episodio viene alineada palabra a palabra. `ep01-lustig/tiempos.json`:

```json
{"w": "El",    "limpia": "el",    "t": 0.227, "d": 0.158, "fin": 0.385}
{"w": "once",  "limpia": "once",  "t": 0.385, "d": 0.317, "fin": 0.702}
{"w": "de",    "limpia": "de",    "t": 0.702, "d": 0.158, "fin": 0.860}
```

155 palabras en 63,45 s = **146,6 palabras por minuto**. Es el mismo fichero del que el
motor saca las anclas de los elementos (`241`), así que el subtítulo y el collage caen
sobre exactamente la misma rejilla temporal. Eso no es una casualidad aprovechable: es la
razón por la que los subtítulos de este canal no se transcriben ni se alinean a mano.

## El agrupamiento, medido

El único parámetro que importa es cuántas palabras van juntas. Medido sobre las 155:

| Agrupación | Bloques | Duración media | Duración mínima | Caracteres medios | Cambios/min |
|---|---|---|---|---|---|
| 2 palabras / 16 car | 81 | 0,59 s | **0,20 s** | 9,8 | 77 |
| **3 palabras / 24 car** | **57** | **0,86 s** | **0,31 s** | **14,3** | **54** |
| 4 palabras / 30 car | 44 | 1,11 s | 0,20 s | 18,9 | 42 |

De dos en dos hay bloques de 0,20 s: **parpadeo**. Aparece y desaparece antes de que el
ojo lo haya fijado, y lo que produce no es incomprensión sino cansancio. De tres en tres,
**cero bloques por debajo de 0,30 s** — el suelo.

De cuatro en cuatro vuelve a haber un bloque de 0,20 s, y además la línea se va a 30
caracteres, que no caben (abajo). Tres palabras es el ajuste, y no por gusto.

```python
def agrupar(P, max_car=24, max_pal=3, corte=0.34):
    """Bloques de subtítulo desde tiempos.json. Corta por silencio ANTES que por
    cuenta: una pausa de la locución es un final de frase, y partirla por la mitad
    porque tocaban tres palabras es lo que hace que el subtítulo suene a máquina."""
    bl, cur = [], []
    for i, p in enumerate(P):
        cur.append(p)
        car = sum(len(x["w"]) + 1 for x in cur) - 1
        sig = P[i + 1] if i + 1 < len(P) else None
        salto = sig["t"] - p["fin"] if sig else 99
        if len(cur) >= max_pal or car >= max_car or salto >= corte or sig is None:
            bl.append(cur); cur = []
    return bl
```

El `corte=0.34` es lo que separa un bloque de otro cuando la voz respira. Sin él, los 57
bloques siguen saliendo pero cortan a mitad de frase y se nota en la lectura mucho antes
de que se pueda explicar por qué.

## El ancho, que es el que decide de verdad

El suelo de transcripción en vertical es **56 px de caja de mayúscula** (`49`). En Arial
—0,716 em de caja— eso es un `font-size` de **78 px**. Con un ancho medio de carácter de
0,58 em:

| Caracteres en la línea | Ancho | ¿Cabe en 820 px? |
|---|---|---|
| 16 | 724 px | Sí |
| **18** | **814 px** | **Justo — es el tope** |
| 24 | 1086 px | **No** |
| 30 | 1357 px | No, ni de lejos |

> **18 caracteres por línea, dos líneas como máximo.** No es una preferencia tipográfica:
> es la zona segura de texto de `49` dividida por el ancho del carácter al tamaño mínimo
> legible. Los bloques de 24 caracteres —la media es 14,3, pero el máximo llega a 24— se
> reparten en dos líneas, nunca se encogen.

Y de ahí sale la consecuencia que `201` ya anticipa: el subtítulo de dos líneas ocupa unos
150 px con su aire, colocado con la línea base dentro del pie útil. **El subtítulo se
queda con la banda `pie` entera.** El rótulo que en 16:9 vivía ahí sube a `banda2`, y la
cifra se va al centro (`207`).

## Quemado, y además cerrado

Los dos, siempre, y por razones distintas:

| | Para qué |
|---|---|
| **Quemado** (en los píxeles) | Que se lea aunque la red no ponga nada y aunque el espectador no active nada |
| **Cerrado** (fichero `.srt` subido) | Accesibilidad, y que la red indexe el texto — de ahí sale parte del alcance |

El `.srt` sale del mismo agrupamiento, así que son el mismo bloque escrito dos veces y no
hay forma de que discrepen. La lista de idiomas del canal (`88`) multiplica las pistas: el
mismo agrupador con otra `tiempos.json` y ya está.

## Lo que el subtítulo no es

No es el rótulo. Un rótulo nombra un objeto («Banco de Francia, 1925») y dura lo que dura
el objeto; el subtítulo transcribe la voz y cambia 54 veces por minuto. Si se componen
igual —misma tipografía, mismo tamaño, mismo sitio— el espectador deja de distinguir qué
está oyendo y qué está viendo, que es justo lo que este canal vende.

El subtítulo va en la tipografía de transcripción, sin adorno, sin el destello de la
tipografía cinética (`47`), y **sin resaltar la palabra clave**. Resaltar palabras en el
subtítulo es de otro formato; aquí la palabra clave se resalta poniéndole una imagen
encima, que es el motor entero.

## Errores frecuentes

| Error | Consecuencia medida |
|---|---|
| Subtitular de dos en dos palabras | Bloques de 0,20 s: parpadeo y cansancio |
| Subtitular de cuatro en cuatro | 30 caracteres = 1357 px: no cabe en 820 |
| Cortar sólo por cuenta de palabras | Frases partidas por la mitad; se nota antes de saber por qué |
| Encoger el subtítulo para que quepa en una línea | Por debajo de 56 px de caja no se lee en el metro |
| Dejar el rótulo en el pie | Pelea con el subtítulo por la misma franja |
| Transcribir a mano | `tiempos.json` ya tiene las 155 palabras alineadas |
| Sólo quemado, sin `.srt` | Se pierde accesibilidad y la indexación del texto |
| Resaltar la palabra clave en el subtítulo | Es otro formato; aquí la palabra se resalta con imagen |

## Relacionado

`45` subtítulos y destacados · `49` zona segura y tamaños · `95` escribir para el oído ·
`88` sonido por idioma · `201` la columna · `203` densidad en vertical · `207` la cifra en
vertical · `241` resolución de anclas · editpro `414` subtítulos quemados o cerrados
