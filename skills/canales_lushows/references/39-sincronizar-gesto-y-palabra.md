# 39 · Sincronizar gesto y palabra

**Qué resuelve:** el elemento correcto, en el sitio correcto, y aun así el plano se
siente flojo. Casi siempre es sincronía: llegó tarde. Justo a tiempo **es** tarde, y por
una razón física, no de gusto.

---

## Por qué el ojo exige adelanto

El oído resuelve una palabra en su ataque: la sílaba suena y ya está identificada. La
vista no. Aparece algo en el cuadro, hay que **mover el ojo hasta ahí** (una sacada, 30-80
ms), **reconocerlo** (60-100 ms más) y solo entonces significa algo. Son 100-180 ms de
retraso antes de que la imagen se convierta en información.

Si imagen y palabra salen a la vez, la palabra llega primero al cerebro y la imagen la
alcanza cuando ya pasó: el espectador la vive como ilustración de algo que ya entendió.
Con el adelanto, las dos coinciden **dentro de la cabeza**, y ahí es donde se siente
que el montaje está bien hecho.

Además la tolerancia es asimétrica: **la imagen adelantada se perdona mucho más que la
imagen atrasada.** Por eso, en la duda, siempre antes.

---

## La tabla de adelantos

Se piensan en **fotogramas**, no en milésimas: a 25 fps la rejilla es de 0,04 s y pedir
0,13 s no significa nada.

| Elemento | Adelanto | Fotogramas |
|---|---|---|
| Cifra de impacto | 0,20 s | **5 f** |
| Retrato / recorte principal | 0,12 s | **3 f** |
| Documento, recorte de prensa | 0,12 s | **3 f** |
| Rótulo que explica un objeto | 0,08 s | **2 f** |
| Sello / golpe con sonido | 0,00 s | **0 f** |
| Texto que se escribe (`41`) | 0,04 s | **1 f** |
| Cambio de plano (corte) | 0,08 s | **2 f** |

**El sello es la excepción y es deliberada:** cuando el elemento trae un golpe de sonido,
el sonido y la imagen caen **exactos** sobre la sílaba. El sonido hace de ancla y el
cerebro ya no necesita el adelanto — al revés, adelantarlo suena a desincronía.

## El criterio real: legible, no iniciado

La regla de 0,1-0,2 s se aplica al **arranque** de la entrada suponiendo entradas de
0,25-0,32 s, que es el estándar (`32`). Pero lo que el espectador necesita es que el
elemento **esté legible** cuando suena la palabra. Con entradas largas hay que sumar:

```
t_inicio = t_palabra − adelanto − max(0, duración_entrada − 0,30)
```

Un teletipo de 1,4 s anclado con 3 fotogramas de adelanto termina de escribirse **1,1 s
tarde**. Por eso el teletipo se calcula al revés: su velocidad (18-26 car/s) se ajusta
para que la última letra caiga con la última sílaba de la frase.

## Anclar a la sílaba, no al token

`audio/tiempos.json` da palabra → segundo de inicio. En español el ataque coincide con el
inicio de la palabra en la mayoría de los casos, con dos salvedades:

- **Palabras de 4 o más sílabas con tónica después de la primera** ("cooperativa",
  "extradición"): el acento cae 0,10-0,16 s dentro. Se suma ese desplazamiento
- **Palabras que empiezan por oclusiva sorda** (p, t, k): el silencio de la oclusión hace
  que `tiempos.json` marque el inicio ligeramente antes del sonido audible. Restar 0,04

```python
import json

TIEMPOS = json.load(open("audio/tiempos.json", encoding="utf-8"))
F = 1 / 25

def anclar(palabra, n=1, adelanto_f=3, entrada=0.30, tonica=0.0):
    """Segundo en que debe ARRANCAR el elemento."""
    hits = [w for w in TIEMPOS if w["palabra"].lower() == palabra.lower()]
    t = hits[n - 1]["inicio"] + tonica
    t = t - adelanto_f * F - max(0.0, entrada - 0.30)
    return round(t / F) * F          # a la rejilla de fotogramas

anclar("millones", n=2, adelanto_f=5, entrada=0.18)
```

La **n-ésima aparición** importa: en un guion de 900 palabras, "millones" sale seis veces
y anclar a la primera pone el elemento veinte segundos antes.

## La salida no se ancla a la palabra

El elemento **no** sale con la última sílaba de su frase: sale entre **0,3 y 0,6 s
después**. Salir exacto se lee como si lo hubieran cortado. La única excepción es el
relevo: si otro elemento entra empujándolo, la salida cae donde entra el siguiente.

## Verificación

No se juzga a ojo reproduciendo. Se saca el fotograma exacto de la palabra:

```bash
# la palabra suena en el segundo 12,44 del episodio
ffmpeg -ss 12.44 -i piloto.mp4 -frames:v 1 -y chk.png
```

En ese fotograma el elemento tiene que estar **completo y opaco**. Si todavía está
entrando, el ancla está mal. Para revisar en bloque, la grilla:

```bash
ffmpeg -i piloto.mp4 -vf "fps=1/2,scale=440:-1,tile=6x4" -frames:v 1 grilla.png
```

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Anclar a la primera aparición de la palabra | El elemento sale veinte segundos antes |
| Adelanto en milésimas y no en fotogramas | Se redondea solo, y no siempre hacia donde crees |
| Entrada larga con adelanto estándar | El elemento está legible después de su palabra |
| Adelantar el sello que lleva golpe de sonido | Suena desincronizado |
| `tiempos.json` con la palabra sin tildes | El `lower()` no casa y el ancla se va al plano equivocado |
| Sacar el elemento con la última sílaba | Se lee como recortado |
| Sincronizar de oído reproduciendo | Se pierden los desfases de 2-3 fotogramas, que son los que importan |

## Relacionado

`13` ciclo de vida del elemento · `32` entradas y salidas · `34` movimiento que narra ·
`41` máquina de escribir · `89` biblioteca de sonido
