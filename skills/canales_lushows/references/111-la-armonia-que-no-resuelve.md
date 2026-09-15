# 111 · La armonía que no resuelve

**Qué resuelve:** el mecanismo central de la música de este canal. El oído espera que
la frase cierre, la frase no cierra, y **la espera es atención sostenida**. Este módulo
dice cómo se construye una progresión que no llega nunca, sin que suene a error.

---

## Qué está documentado y qué es nuestra apuesta

| Afirmación | Estado |
|---|---|
| Un oyente criado en música occidental predice la nota siguiente, y predice mejor hacia la tónica | **Documentado.** Es el resultado clásico de los experimentos de tono-sonda (jerarquía tonal, Krumhansl) |
| Romper esa predicción produce una respuesta medible (sorpresa, tensión) | **Documentado** en laboratorio, sobre estímulos cortos |
| Esa tensión sin resolver **retiene al espectador en un vídeo de YouTube** | **Nuestra hipótesis de trabajo.** No la hemos medido. Lo que sí medimos es retención (`17`), y no sabemos separar la parte que aporta la música |
| El efecto es universal | **Falso.** Depende de haber crecido oyendo este repertorio. Para nuestro público, se cumple |

Se usa porque funciona en la sala, no porque haya un número que lo demuestre. Decirlo
así cuando alguien pregunte.

## Dónde está el tirón: la sensible

En re menor, la nota que más empuja es **Do# (C#4 = 277,18 Hz)**: está a un semitono de
Re y el oído la oye como "falta medio paso". Meterla es abrir una puerta; no meterla es
no abrirla nunca.

| Grado | Nota | Hz (octava 3) | Tirón hacia la tónica |
|---|---|---|---|
| 7ª sensible | Do# | 138,59 | **Máximo.** Es el motor de la cadencia |
| 7ª menor (modal) | Do♮ | 130,81 | Ninguno. Deja la frase abierta |
| 2º grado | Mi | 164,81 | Suspende: ni sube ni baja |
| 4º grado | Sol | 196,00 | Pide bajar a Fa, no a Re |
| 6º menor | Si♭ | 116,54 | Pesa hacia abajo. El color de la caída (`115`) |

**Regla del canal: el Do# solo aparece si queremos cerrar.** En todo el colchón de
`_expediente` no hay un solo Do#, y por eso el bucle puede durar minutos.

## Las dos versiones de la misma frase

```python
T = 3.4
def bloque(t0, raiz, acorde, mel=None):
    ns = [(t0, raiz, 3.0, 0.95)]
    for k, a in enumerate(acorde):                 # el acorde entra en contratiempo
        ns.append((t0 + 1.10 + k * 0.014, a, 2.2, 0.38))
    for off, n in (mel or []):
        ns.append((t0 + off, n, 1.6, 0.50))
    return ns

CIERRA   = [("D2", ["D3","F3","A3"]),   ("G2", ["D3","G3","Bb3"]),
            ("A2", ["C#3","G3","A3"]),  ("D2", ["D3","F3","A3"])]   # V7 -> i
NOCIERRA = [("D2", ["D3","F3","A3"]),   ("G2", ["D3","G3","Bb3"]),
            ("A2", ["C#3","G3","A3"]),  ("Bb1",["D3","F3","Bb3"])]  # V7 -> VI

def pieza(prog):
    ns = []
    for c, (raiz, ac) in enumerate(prog):
        mel = [(0.45,"A4"), (1.70,"F4")] if c % 2 else [(0.45,"D4")]
        ns += bloque(c * T, raiz, ac, mel)
    return ns

tocar(pieza(CIERRA),   "111_cierra.wav")     # 22 notas · 14,47 s (medido)
tocar(pieza(NOCIERRA), "111_nocierra.wav")   # 22 notas · 14,47 s (medido)
```

Las dos piezas duran **exactamente lo mismo** y solo cambia **una nota del bajo**
(Re2 = 73,42 Hz por Si♭1 = 58,27 Hz) en el último compás. La primera se acaba. La
segunda pide otro compás. Ese es todo el truco.

## Los seis recursos, de menos a más evidente

| # | Recurso | Cómo se escribe | Cuándo |
|---|---|---|---|
| 1 | **Sin sensible** | Nunca Do#: el acorde de La es La-Do♮-Mi (`A2, C3, E3`) | Colchón por defecto. Es lo que hace modal a `_expediente` |
| 2 | **Tónica en parte débil** | El bajo en el uno, el acorde en `t0 + 1.10` | Siempre. La resolución nunca cae en tiempo fuerte |
| 3 | **Bucle plagal** | `Dm ↔ Gm` (`D2` ↔ `G2`), sin pasar por La | Tramos largos de exposición |
| 4 | **Suspensión que no baja** | `D3, G3, A3` (sus4) y se queda | Pregunta abierta, antes de la cifra |
| 5 | **Cadencia rota** | `A7 → Bb` en vez de `A7 → Dm` | El giro del episodio. Una vez, no dos |
| 6 | **Melodía que muere en el 2º** | Terminar en `E4` = 329,63 Hz | Cada frase del colchón |

## El recurso 6 en el piloto: lo que dice el código y lo que hace

El comentario de `_expediente` dice *"la melodía toca el 6.º grado y baja"*. No es lo que
hace: las dos frases son `A4 · F4 · E4` y `D4 · E4`, y **las dos terminan en Mi4 (329,63
Hz), que es el 2.º grado**. El 6.º grado (Si♭4 = 466,16 Hz) no aparece en toda la pieza.

El efecto es el correcto —el 2.º grado suspende igual de bien— pero **el comentario
miente sobre su propio código**, que es la forma más cara de equivocarse: el día que
alguien "arregle" la melodía siguiendo el comentario, romperá lo que funciona. Si se
quiere el 6.º de verdad, la frase es `Bb4 · A4 · F4`.

## Cuánto aguanta una progresión sin cerrar

| Duración | Qué pasa |
|---|---|
| < 30 s | No da tiempo a instalar la expectativa. Se oye como acompañamiento |
| **30 s – 3 min** | El punto. La espera trabaja y no cansa |
| 3 – 6 min | Aguanta si la cima cambia (`112`, `127`). Con el bajo solo, no |
| > 6 min sin variación | Deja de ser espera y pasa a ser fondo. El oído lo archiva |

Y un cierre por episodio, en el remate (`115`). **Si nada cierra nunca, no hay espera:
hay costumbre.** La resolución final es lo que da valor a los diez minutos anteriores.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Meter Do# "porque suena más musical" | Se abre la cadencia y el colchón empieza a cerrar cada cuatro compases |
| Resolver en el gancho | Se gasta en el segundo 8 la carta que vale en el minuto 9 |
| Dos cadencias rotas seguidas | La segunda ya no sorprende: se lee como que la música está perdida |
| Tónica en tiempo fuerte en todos los compases | La pieza cierra sola aunque la progresión sea abierta |
| No cerrar nunca, tampoco al final | El episodio termina sin sensación de final; sube el abandono en el remate |
| Fiarse del comentario y no de las notas | Ver arriba: `_expediente` dice 6.º grado y toca el 2.º |
| Presentar el mecanismo como neurociencia | Es expectativa documentada + una hipótesis nuestra sobre retención |

## Relacionado

`110` tonalidad y significado · `112` el ostinato · `113` intervalos que inquietan ·
`115` progresiones por tramo · `118` cuándo no debe haber música · `120` curva de intensidad
