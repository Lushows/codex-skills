# 231 · El banco acumulativo

**Qué resuelve:** la idea de que el material se acumula y que por eso el episodio cinco
costará menos que el primero. Es la premisa sobre la que descansa hacer doce minutos.
Conviene comprobarla antes de apoyarse en ella, porque **hoy es falsa, y se puede medir en
un minuto.**

---

## Lo que hay en disco

`motor.py:81` busca cada alias primero en las carpetas del episodio y después en el banco
común. Contando ficheros de imagen:

| | Alias | texto | fx | recortes | recursos | render | archivo |
|---|---|---|---|---|---|---|---|
| **Banco común** | **186** (216 ficheros) | 26 | 24 | 62 | 25 | 27 | 52 |
| **`ep01-lustig`, suyos** | **198** | 17 | 25 | 72 | — | 5 | 79 |
| **Visibles al montar** | **384** | | | | | | |

Trescientos ochenta y cuatro alias disponibles. Y ahora el número que importa:

```
recursos DISTINTOS usados por el episodio: 56 de 59 gestos
   del material propio: 56 · del banco comun: 0
```

**Cero.** Ni uno. El banco común aporta el 0 % de un episodio que tiene 186 alias
esperando dentro. No es que el episodio prefiera los suyos por la regla de precedencia:
es que `vocabulario.py` sólo nombra 56 alias y **los 56 son suyos**. Nada lee el banco, así
que el banco no es un banco: es un archivo muerto de 216 ficheros y 46 MB.

## Por qué importa a doce minutos y no a uno

A 700 gestos y el umbral de 1,25 usos por recurso del canal hacen falta **560 recursos
distintos**. Si el banco sigue aportando cero, los 560 hay que producirlos **por episodio**.
Al ritmo real del piloto —198 ficheros propios para 63,45 s— eso son **2.250 ficheros por
episodio de doce minutos**. Ahí es donde el proyecto se para, no en el render.

| | 1 minuto (medido) | 12 minutos |
|---|---|---|
| Gestos | 59 | ~700 |
| Recursos distintos necesarios | 56 | ~560 |
| Ficheros propios producidos | 198 | ~2.250 |
| Aportados por el banco | **0** | **0**, si nada cambia |

## Los tres pisos del cajón, y sólo uno acumula

Los 56 recursos del piloto, por carpeta de origen:

| Piso | Carpeta | Recursos | % | ¿Se reutiliza en otra historia? |
|---|---|---|---|---|
| **De esta historia** | `recortes/` | 33 | 59 % | **No.** Son Lustig, la torre, ese expediente |
| **Dibujado** | `fx/` | 15 | 27 % | **Sí**, y es el único que sí |
| **Dato del episodio** | `texto/` | 8 | 14 % | No. «11 de marzo de 1947» no vale para otro |

El error de fondo es tratar los tres pisos igual: se guardan todos juntos, se cuentan
todos juntos y se concluye que «hay 416 piezas». De esas 416, las que pueden volver a
salir en otro episodio son las del piso de en medio, y son poco más de una cuarta parte.

## Lo que de verdad se acumula no son PNG: son los generadores

Este es el hallazgo que cambia la estrategia. Mirando la carpeta `fx/` del episodio:

```
_balanza_00.html  balanza_00.png     _linea_00.html  linea_00.png
_balanza_01.html  balanza_01.png     _linea_01.html  linea_01.png
...
_torre_esquema.html  torre_esquema.png
```

**Cada PNG dibujado tiene su HTML al lado.** Lo mismo en `texto/` (17 PNG, 17 HTML) y en
los cinco fondos (`_f_muerte.html` → `render/f_muerte.png`). Los produce código del
episodio: `fx_lustig.py`, `fx_extra.py`, `texto_lustig.py`, `fondos.py`.

Y ahí está la diferencia: **un PNG de la línea de tiempo de Lustig no sirve para Enron;
el HTML que la dibuja, sí**, cambiándole las fechas. Un `sello_consta` sirve tal cual. Un
`d_1890` no sirve nunca, pero el generador de tarjetas de cifra sirve siempre.

> El banco que acumula no es la carpeta de imágenes: es **la carpeta de plantillas y los
> cuatro scripts que las rellenan**. Pesa 4 MB contra los 672 MB de `archivo/`, y es lo
> único que hace que el episodio cinco cueste menos que el primero.

## Por qué el banco común no se usa (y cómo se arregla)

Tres razones, las tres arreglables y ninguna cara:

1. **Nadie sabe qué hay dentro.** Un alias como `flujo`, `cotas` o `usd_07` no dice qué se
   ve. El vocabulario se escribe mirando el guion, no la carpeta, así que nombra lo que
   el montador tiene en la cabeza. **Hace falta un índice** `alias → qué se ve → de qué
   episodio salió`, en un JSON al lado del banco (`199`).
2. **Los alias chocan.** El banco común tiene **30 basenames repetidos entre carpetas** de
   382 alias, casi todos entre `recortes/` y `archivo/` (`248`). Mientras eso siga así,
   escribir un vocabulario contra el banco es jugar a la lotería con qué fichero sale.
3. **Reutilizar en silencio es peor que no reutilizar.** La ventana antirrepetición de
   25 s vive dentro del episodio (`253`, `236`). Entre episodios **no hay ninguna regla**,
   y el espectador que ve tres vídeos seguidos sí que se acuerda de la balanza. Un banco
   que se usa sin contar convierte el canal en una plantilla.

La tercera se arregla con un contador, no con una prohibición:

```python
# banco/usos.json  ->  {"fajo": ["ep01-lustig", "ep02-enron"], ...}
def puede_volver(alias, episodio, tope=2):
    """Un recurso del banco puede salir en 'tope' episodios. Despues, se jubila
    o se rehace con otro encuadre."""
    hist = USOS.get(alias, [])
    return episodio in hist or len(hist) < tope
```

Dos episodios es un criterio, no una ley; lo que no es negociable es que la decisión sea
**declarada** y no un efecto secundario de que el fichero estuviera ahí.

## El coste en disco, que también escala

`ep01-lustig` completo ocupa **1.726 MB para 63,45 segundos**:

| Carpeta | MB | ¿Escala con la duración? |
|---|---|---|
| `archivo/` (descargas en bruto) | 672 | Sí, con el material |
| `salida/` (renders, caché, grillas) | 667 | Sí, con la duración (`237`) |
| `recortes/` | 351 | Sí, con el material |
| `render/` (fondos) | 38 | Poco: 5 fondos por episodio |
| `fx/` + `texto/` | 6 | **Casi nada, y es el que se queda** |

A doce minutos son del orden de **15-20 GB por episodio**, de los que 6 MB son lo único
que valdrá para el siguiente. Conviene saberlo antes de decidir qué se conserva y qué se
tira cuando el episodio está publicado: se tira `archivo/`, se conserva `recortes/` con su
índice, y **nunca** se tocan los HTML ni los scripts.

## La comprobación, antes de fiarse del banco

```python
import os, sys, collections
sys.path.insert(0, "epi")
from guion_visual import ESCENAS
PROP = ["epi/" + d for d in ("texto", "fx", "recortes", "render", "archivo")]
COMUN = ["texto", "fx", "recortes", "recursos", "render", "archivo"]

def donde(r):
    for c in PROP + COMUN:
        for e in (".png", ".jpg", ".webp"):
            if os.path.exists(os.path.join(c, r + e)):
                return c
    return "??"

u = {e["r"] for s in ESCENAS for e in s.get("elementos", [])}
c = collections.Counter(donde(r) for r in u)
print(c)
print("aporte del banco comun: %.0f %%"
      % (100 * sum(v for k, v in c.items() if not k.startswith("epi/")) / len(u)))
```

Si esa última línea dice 0 %, el banco no existe todavía por mucho que la carpeta pese.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Contar el banco por ficheros en disco | 384 alias visibles y 0 usados: el número no mide nada |
| Guardar PNG y tirar el HTML que lo dibujó | Se acumula lo que no sirve y se pierde lo que sí |
| Meter los tres pisos en la misma carpeta | «Tenemos 416 piezas» cuando reutilizables hay 15 |
| Escribir el vocabulario sin mirar el banco | El banco nunca se usa, por muy lleno que esté |
| Reutilizar entre episodios sin contarlo | El canal empieza a parecer una plantilla y nadie sabe cuándo pasó |
| Alias repetidos entre carpetas | 30 de 382: se sirve el fichero de la otra carpeta sin un solo error (`248`) |
| Conservar `archivo/` de un episodio publicado | 672 MB por minuto de vídeo que ya no se va a volver a cortar |
| Asumir que el episodio 5 costará menos | Sólo si alguien construyó el piso de en medio a propósito |

## Relacionado

`199` el manifiesto del material · `192` alias estables · `248` pre-escalado y caché ·
`174` el umbral de piezas útiles · `170` el sondeo de media hora · `190` curar por
escenario · `259` cuando el diccionario no basta · `235` palabras repetidas y anclaje ·
`239` el episodio como proyecto · `97` banco de historias
