# 119 · Componer con el lenguaje de una época

**Qué resuelve:** que un episodio ambientado en 1925 suene a 1925 sin tocar una nota de
una obra existente. Se copia el **vocabulario** —qué acordes, qué hace el bajo, qué
textura— y se escribe música propia con él: más seguro y mejor que transcribir de memoria.

---

## Por qué componer propio y no transcribir

| | Componer con el vocabulario | Transcribir una obra de memoria |
|---|---|---|
| La composición | **Nuestra.** Nadie puede reclamarla | Ajena. Libre solo si está en dominio público |
| La grabación | Nuestra (sintetizada) | Nuestra también |
| Content ID sobre el audio | **Imposible que case:** no existe una referencia igual | Imposible también |
| Reclamación **por composición** | No cabe | **Sí cabe.** Las editoras registran melodías, no solo grabaciones |
| Si la memoria falla | Da igual: es una pieza nueva | Sale una versión mala de algo reconocible |

El detalle que se escapa: Content ID compara **huellas de audio**, y una síntesis propia
nunca casa. Pero YouTube tiene una segunda vía, la reclamación **por obra**, y ahí una
melodía famosa reconocible sí se puede reclamar aunque la grabación sea tuya. Componer
propio cierra las dos puertas; transcribir solo cierra una. Y el plazo importa: la
**composición** de Satie (murió el 1 de julio de 1925) está en dominio público en
Colombia desde 2006 (vida + 80 años, Ley 23 de 1982 reformada por la Ley 1915 de 2018);
**cualquier grabación de ella, no** (`130`, `131`). Una obra de 1970 no está en dominio
público en ningún sitio.

## Las tres épocas del canal

| | **1890** París | **1925** salón | **1970** oficina |
|---|---|---|---|
| Armonía | Tríadas modales usadas por color, no por función | 7ªs y 6ªs en todos los acordes | 7ªs menores con 9ª añadida |
| Sensible | No la hay | La hay, y empuja | No la hay |
| Bajo | Pedal repetido, la misma nota | **Camina:** fundamental ↔ quinta | Dos notas y para |
| Movimiento | Quieto, casi sin dirección | Círculo de quintas: siempre va a algún sitio | Vaivén de dos acordes |
| Tempo | 60-70 ppm | 76-92 ppm | 56-66 ppm |
| Textura | Escasísima | Densa por abajo, con melodía clara | Acordes anchos, muy quietos |
| Afinación | La4 = **435 Hz** (`110`) | La4 = 440 (norma ya extendida) | La4 = 440 |

## 1890 · modal y quieto

```python
def _1890(c=4, T=3.4):
    """Ni sensible, ni dirección. Alterna raíz y ♭VI y se queda ahí."""
    ns = []
    for i in range(c):
        ns += bloque(i * T,
                     "D2" if i % 2 == 0 else "Bb1",              # 73,42 / 58,27 Hz
                     ["D3","F3","A3"] if i % 2 == 0 else ["D3","F3","Bb3"],
                     [(0.45,"A4"), (1.70,"F4")] if i % 2 else [(0.45,"D4")])
    return ns
tocar(_1890(), "119_1890.wav")      # 22 notas · 14,47 s (medido)
```

Es el lenguaje de `_expediente`. Para rematarlo, bajar la afinación al *diapason normal*
francés de 1859 — **20 centésimas por debajo del La 440 de hoy**:
```python
import os, piano
_hz440 = piano.hz
piano.hz = lambda n: _hz440(n) * (435.0 / 440.0)
piano.MUESTRAS = os.path.join(piano.DEST, "_piano435")   # 🔴 si no, el caché gana
```

## 1925 · el bajo que camina

```python
def _1925(c=4, T=3.0):
    """Séptimas por círculo de quintas y bajo de vaivén: Re7 - Sol7 - Do7 - Fa."""
    prog = [("D2", ["F3","A3","C4"]),    ("G2", ["F3","B3","D4"]),
            ("C2", ["E3","G3","Bb3"]),   ("F2", ["A3","C4","E4"])]
    ns = []
    for i in range(c):
        raiz, ac = prog[i % 4]; t0 = i * T
        ns.append((t0, raiz, 2.4, 0.92))                          # fundamental
        ns.append((t0 + T/2, nombre(semitono(raiz) + 7), 1.5, 0.70))  # su quinta
        for k, a in enumerate(ac):
            ns.append((t0 + 1.00 + k * 0.014, a, 2.0, 0.38))
        ns.append((t0 + 0.40, ac[-1], 1.5, 0.46))
    return ns
```

Las dos marcas de época están en dos líneas: el **vaivén fundamental-quinta** del bajo
(`semitono(raiz) + 7`) y el **Si♮3 = 246,94 Hz** del segundo acorde, que es una sensible
de verdad. Ese Si es lo que hace que suene a 1925 y no a 1890.

## 1970 · dos acordes y nada más

```python
def _1970(c=4, T=3.6):
    """Vaivén de dos acordes con 9ª. Se queda, no va."""
    prog = [("A1", ["E3","G3","B3","D4"]),      # La m 11 (55,00 Hz de raíz)
            ("D2", ["F3","A3","C4","E4"])]      # Re m 9
    ns = []
    for i in range(c):
        raiz, ac = prog[i % 2]; t0 = i * T
        ns.append((t0, raiz, 3.4, 0.95))
        for k, a in enumerate(ac):
            ns.append((t0 + 1.20 + k * 0.020, a, 2.4, 0.34))
        if i >= 1:
            ns.append((t0 + 0.50, "B4" if i % 2 else "E4", 2.0, 0.44))
    return ns
```

Cuatro notas por acorde en vez de tres, y ninguna de ellas es la sensible. La 9ª (`E4` =
329,63 Hz sobre Re) es lo que suena a esa década. ⚠️ Con cuatro voces la pieza gana
energía en la banda de la voz: hay que comprobarlo antes de mezclarla (`117`).

## Lo que NO hace época

**Ensuciar el audio** (grano de vinilo, ruido de aguja, filtro de fonógrafo) no suena a
1925: suena a un archivo de 2026 con un filtro encima. **Bajar el `lowpass`** tampoco —
`piano.py` ya corta a 5.200 Hz y bajarlo solo quita definición. Y **un motivo
reconocible de la época**: si se reconoce, es de alguien. La época va en las notas.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Transcribir de memoria una melodía famosa | Content ID no la casa, pero la editora sí la reclama por obra |
| Suponer que "clásico" = libre | Libre es la **composición**; la grabación tiene derechos propios (`130`) |
| Usar vocabulario de 1970 en un episodio de 1925 | El oído lo detecta aunque no sepa nombrarlo: suena a documental barato |
| Cambiar la afinación sin cambiar `MUESTRAS` | El caché sirve las notas a 440 y no pasa nada, sin aviso |
| Ruido de vinilo como recurso de época | Suena a filtro, no a antiguo |
| Sensible en el episodio de 1890 | Rompe el modalismo y la pieza empieza a cerrar sola (`111`) |
| 4 voces de 1970 sin medir la banda de la voz | La pieza pelea con la locución y hay que bajarla hasta que no se oye (`117`) |

## Relacionado

`110` tonalidad y significado · `114` modos y color · `117` dejarle sitio a la voz ·
`130` la obra es libre, la grabación no · `131` dominio público por país · `132` Content ID
