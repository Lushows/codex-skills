# 106 · Texturas y pads

**Qué resuelve:** el colchón armónico — lo que suena por debajo de todo y sostiene la
escena sin que nadie lo note. Es exactamente donde el canal falló: durante semanas el
colchón fue `anoisesrc=c=pink` filtrado más un `sine` de 55 Hz, y el espectador lo dijo
antes que nosotros: «se siente como un ruido».

---

## Por qué aquello era un zumbido y no un pad

Un pad tiene tres cosas que un tono sostenido no tiene:

| # | Ingrediente | Qué hace |
|---|---|---|
| 1 | **Osciladores desafinados** | El batido entre voces cercanas: eso es «cuerpo» |
| 2 | **Movimiento interno lento** | El timbre cambia aunque la nota no |
| 3 | **Entrada y salida muy largas** | Nunca se le oye empezar |

Medido: recorrido del **centroide espectral** (dónde está el «centro de gravedad» del
sonido) en tres colchones de 14 segundos.

| Colchón | Centroide medio | Recorrido | Desviación |
|---|---|---|---|
| Pad con desafine y filtro en movimiento | 184 Hz | 116–963 Hz | **127,6 Hz** |
| Mismo pad sin desafine ni movimiento | 119 Hz | 105–418 Hz | 42,5 Hz |
| **El ruido rosa + 55 Hz que teníamos** | 405 Hz | 359–448 Hz | **17,4 Hz** |

El fondo viejo era **plano en el tiempo**. No cambiaba nunca, y un sonido que no cambia
nunca lo archiva el cerebro como ruido ambiente y deja de oírlo. Esa es la definición
técnica de «se siente como un ruido».

## El pad, completo

```python
def pad(nota, dur=14.0, p="pd"):
    r = hz(nota)
    des = (1.000, 0.9965, 1.0037)          # ±0,35 %: el batido
    ps, et, k = [], [], 0
    for f, g in [(r,1.00), (r*1.4983,0.62), (r*1.1892,0.40), (r*2,0.30)]:
        for d in des:                       # tres osciladores POR VOZ
            ps.append(f"sine=f={f*d:.4f}:d={dur:.2f}:sample_rate=44100,"
                      f"volume={g/len(des):.4f}[{p}{k}]")
            et.append(f"[{p}{k}]"); k += 1
    return (";".join(ps) + ";" + "".join(et) + f"amix=inputs={k}:normalize=0,"
            # el filtro que se MUEVE: dos copias cruzándose cada 11 s
            f"asplit=2[{p}a][{p}b];"
            f"[{p}a]lowpass=f=520:poles=2,"
            f"volume='0.5+0.5*cos(2*PI*t/11)':eval=frame[{p}c];"
            f"[{p}b]lowpass=f=2600:poles=2,"
            f"volume='0.5-0.5*cos(2*PI*t/11)':eval=frame[{p}d];"
            f"[{p}c][{p}d]amix=inputs=2:normalize=0,"
            f"afade=t=in:st=0:d=3.0,afade=t=out:st={dur-3.0:.2f}:d=3.0,volume=1.6")
```

Las voces son fundamental, quinta (×1,4983), tercera menor (×1,1892) y octava (×2). La
tercera es siempre la más floja: es la que decide mayor o menor y no conviene que grite.

## El desafine: ±0,35 %, ni más ni menos

```
des = (1.000, 0.9965, 1.0037)
```

Dos senos separados un 0,35 % en 73 Hz baten a unos **0,26 veces por segundo**: una
respiración lenta. La fórmula es `batido = |f1 − f2|`.

| Desafine | Batido en 73 Hz | Se oye como |
|---|---|---|
| 0 % | — | Una sola voz, plana y delgada |
| **0,3–0,4 %** | 0,22–0,29 Hz | **Cuerpo, respiración** |
| 1 % | 0,73 Hz | Un trémolo evidente |
| 3 % | 2,2 Hz | Desafinado; suena a error |

**El desafine cuesta nivel, y mueve el timbre.** Dos colchones idénticos de 10 s,
mismas ganancias nominales, única diferencia el desafine:

| | Integrado | Desviación del centroide |
|---|---|---|
| Con desafine ±0,35 % | −26,2 LUFS | **18,6 Hz** |
| Con las tres voces afinadas igual | −21,2 LUFS | **0,5 Hz** |

Cinco LU más flojo y **37 veces más movimiento**. Lo primero no es un fallo: las voces
idénticas se suman en fase y las desafinadas se cancelan a ratos. Se compensa al
normalizar (`109`). Lo segundo es todo el punto.

## El movimiento: cruzar dos filtros, no mover uno

ffmpeg no tiene un `lowpass` con frecuencia variable en el tiempo. El truco que sí
funciona es **hacer dos copias con filtros distintos y cruzarlas** con volúmenes que
dependen de `t`:

```
asplit=2 → una copia a lowpass=520, otra a lowpass=2600
volume='0.5+0.5*cos(2*PI*t/11)':eval=frame   ← sube mientras la otra baja
volume='0.5-0.5*cos(2*PI*t/11)':eval=frame
```

El período de 11 s no es redondo a propósito: si coincide con la duración de una escena
el oído lo pilla. Regla: **el período del movimiento nunca debe ser divisor de la
duración del bloque**.

Por debajo de 5 s el movimiento se oye como efecto; entre **9 y 14 s** no se oye y se
percibe como que el colchón está vivo; por encima de 25 s vuelve a ser plano.

## Cuándo un pad ayuda y cuándo estorba

En una exposición larga sin música, **sí**: a −30 LUFS evita el hueco prohibido (`11`).
Debajo del piano, **no**: dos colchones se suman y embarran. Antes de una cifra se abre
el filtro y **se corta**, porque el silencio es lo que da el golpe (`84`). En el remate,
sí, con cola de 4–5 s.

La prueba dura: **si al quitar el pad la escena no pierde nada, sobraba.** Un colchón
que no se echa de menos es el zumbido que teníamos.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Ruido filtrado como colchón | Plano en el tiempo: el cerebro lo archiva y deja de oírlo |
| Osciladores sin desafinar | Delgado, plano, sin cuerpo |
| Desafine por encima del 1 % | Trémolo evidente; al 3 % suena a error |
| Filtro en movimiento con período corto | Se oye como efecto |
| Período del movimiento divisor de la escena | El oído lo pilla y deja de ser textura |
| Pad debajo del piano | Dos colchones sumados: barro |
| Pad sostenido bajo una cifra | Se come el impacto |

## Relacionado

`100` anatomía · `105` el bajo · `107` la sala · `108` por qué suena a pitido · `11` el hueco prohibido
