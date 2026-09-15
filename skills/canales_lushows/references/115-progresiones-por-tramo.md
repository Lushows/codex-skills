# 115 · Progresiones por tramo

**Qué resuelve:** el catálogo cerrado. Qué acordes suenan en cada tramo del episodio
(`93`), con las notas exactas y el código que las toca. Deja de ser "componer" y pasa a
ser elegir de una lista.

---

## La tabla maestra

Todo en **re eólico**, raíz Re2 = 73,42 Hz (`110`). Grados en cifrado romano.

| Tramo (`93`) | Grados | Bajo (Hz) | Acorde | Por qué ahí |
|---|---|---|---|---|
| **Gancho** 0:00-0:20 | i sin 3ª → i add2 | D2 73,42 | `D3 A3` → `D3 A3 E4` | Sin tercera no hay color: no adelanta si la historia acaba bien o mal |
| **Promesa / origen** | i – ♭VI – ♭III – ♭VII | D2 · Bb1 · F2 · C2 | ver abajo | Rueda modal que no cierra (`111`) |
| **La máquina** | i ↔ iv (bucle plagal) | D2 ↔ G2 98,00 | `D3 F3 A3` ↔ `D3 G3 Bb3` | Mecánico y repetido, como el negocio |
| **Cifra ancla** 5:00 | i en octavas, **sin 3ª** | D2 73,42 | `D3 A3 D4` | El cuadro se vacía y el sonido también. La cifra es el evento |
| **La raya / grieta** | i con ♭5 | D2 73,42 | `Ab3 D3 F3` | El tritono (`113`). Es la pieza `mus_sospecha` |
| **La caída** 8:20 | i – ♭VII – ♭VI – v | D2·C2·Bb1·A1 | ver abajo | El bajo baja por tonos hasta el suelo. Literal |
| **Remate** 9:30 | i – ♭VI – iv – i | D2·Bb1·G2·D2 | cadencia plagal | Cierra **una vez** y sin sensible |

## El código

```python
def bloque(t0, raiz, acorde, mel=None, T=3.4):
    ns = [(t0, raiz, 3.0, 0.95)]
    for k, a in enumerate(acorde):
        ns.append((t0 + 1.10 + k * 0.014, a, 2.2, 0.38))
    for off, n in (mel or []):
        ns.append((t0 + off, n, 1.6, 0.50))
    return ns

TRAMOS = {
 "gancho":     [("D2", ["D3","A3"]),        ("D2", ["D3","A3","E4"])],
 "desarrollo": [("D2", ["D3","F3","A3"]),   ("Bb1",["D3","F3","Bb3"]),
                ("F2", ["F3","A3","C4"]),   ("C2", ["E3","G3","C4"])],
 "maquina":    [("D2", ["D3","F3","A3"]),   ("G2", ["D3","G3","Bb3"])],
 "cifra":      [("D2", ["D3","A3","D4"]),   ("D2", ["D3","A3","D4"])],
 "grieta":     [("D2", ["Ab3","D3","F3"]),  ("D2", ["Ab3","D3","F3"])],
 "caida":      [("D2", ["D3","F3","A3"]),   ("C2", ["C3","Eb3","G3"]),
                ("Bb1",["Bb2","D3","F3"]),  ("A1", ["A2","C3","E3"])],
 "remate":     [("D2", ["D3","F3","A3"]),   ("Bb1",["D3","F3","Bb3"]),
                ("G2", ["Bb2","D3","G3"]),  ("D2", ["D3","A3"])],
}

def pieza(nombre, T=3.4):
    ns = []
    for c, (raiz, ac) in enumerate(TRAMOS[nombre]):
        ns += bloque(c * T, raiz, ac)
    return ns

for n in TRAMOS:
    tocar(pieza(n), f"115_{n}.wav")
```

Medido: `gancho` 7 notas · **7,67 s** · `desarrollo` 16 notas · **14,47 s** · `cifra`
8 notas · **7,67 s** · `grieta` 8 notas · **7,67 s** · `caida` 16 notas · **14,47 s** ·
`remate` 15 notas · **14,45 s**. Margen sobre la banda de la voz (`117`): `cifra`
**16,30 dB** y `remate` **18,67 dB** — las dos muy holgadas, que es lo que se busca en
los tramos donde la voz dice lo importante.

Un bloque de 4 acordes a T = 3,4 s dura 14,47 s, no 13,6: la cola del `aecho` de la
sala añade ~0,97 s al final y la última nota del acorde entra en `t0 + 1,10 + 2,20`.
**Al encadenar piezas hay que contar con ese casi segundo de más** (`122`).

## Las notas, con sus frecuencias

| Acorde | Notas | Hz |
|---|---|---|
| i (Re m) | D3 · F3 · A3 | 146,83 · 174,61 · 220,00 |
| i sin 3ª | D3 · A3 | 146,83 · 220,00 |
| i en octavas | D3 · A3 · D4 | 146,83 · 220,00 · 293,66 |
| i con ♭5 | Ab3 · D3 · F3 | **207,65** · 146,83 · 174,61 |
| ♭VI (Si♭) | D3 · F3 · Bb3 | 146,83 · 174,61 · 233,08 |
| ♭III (Fa) | F3 · A3 · C4 | 174,61 · 220,00 · 261,63 |
| ♭VII (Do) | E3 · G3 · C4 | 164,81 · 196,00 · 261,63 |
| iv (Sol m) | D3 · G3 · Bb3 | 146,83 · 196,00 · 233,08 |
| v (La m) | A2 · C3 · E3 | 110,00 · 130,81 · 164,81 |

**Ningún acorde de la tabla lleva Do# (277,18 Hz).** Ni siquiera el remate: cierra por
plagal (iv → i), nunca por dominante. Es la misma decisión que ya está en `_cierre` de
`piano.py` (`114`).

## Las dos trampas del bajo

```python
"caida": [("D2", …), ("C2", …), ("Bb1", …), ("A1", …)]
#          73,42     65,41      58,27       55,00 Hz
```

1. **La caída llega a La1 = 55,00 Hz, que es el suelo absoluto del canal.** Por debajo
   (Sol1 = 48,99 · Re1 = 36,71) un altavoz de móvil no reproduce nada y el tramo más
   dramático del episodio se queda mudo justo donde importa. Si hace falta bajar más,
   se baja la **intensidad**, no la frecuencia.
2. Por eso el remate usa **Sol2 = 98,00 Hz** y no Sol1: el iv de la cadencia plagal
   tiene que oírse, no adivinarse.

## Cómo se reparte en un episodio de 10 minutos

| Minuto | Pieza | Intensidad (`acabar.py`) |
|---|---|---|
| 0:00-0:20 | `gancho` | 0,85 · el golpe |
| 0:20-2:30 | `desarrollo` | 0,55 |
| 2:30-5:00 | `maquina` | 0,45 · aquí manda la voz |
| 5:00-5:40 | `cifra` | **0,00-0,25** · el silencio es parte del efecto (`118`) |
| 5:40-8:20 | `grieta` | 0,72 |
| 8:20-9:30 | `caida` | 0,80 |
| 9:30-10:00 | `remate` | 0,60, apagándose |

La intensidad multiplica el nivel base **0,34** medido para quedar 14 LU bajo la voz
(`acabar.py:100`, `117`). No se cambia el `loudnorm` de la pieza: se cambia este número.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Tercera en el acorde del gancho | Adelanta el color y gasta la sorpresa del episodio |
| Progresión completa bajo la cifra ancla | El acorde compite con el evento visual: la cifra deja de ser el pico |
| Bajar el bajo de la caída por debajo de 55 Hz | En móvil el tramo más dramático se queda sin fondo |
| Cerrar en el desarrollo | Se gasta en el minuto 2 el remate del minuto 9 |
| Cambiar `loudnorm` de la pieza para "subirla" | Se descuadra toda la mezcla. El mando es la intensidad, no el normalizador |
| Encadenar contando 13,6 s por bloque | Son 14,47: se pisa el cruce con la pieza siguiente (`122`) |
| Usar la misma progresión en gancho y remate | El episodio no cierra: vuelve al principio |

## Relacionado

`93` estructura de episodio · `111` la armonía que no resuelve · `113` intervalos que
inquietan · `114` modos y color · `118` cuándo no debe haber música · `120` curva de intensidad
