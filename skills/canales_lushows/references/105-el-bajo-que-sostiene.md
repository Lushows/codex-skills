# 105 · El bajo que sostiene

**Qué resuelve:** la nota grave que da fundamento a la pieza sin embarrarla. Es el
instrumento que más fácil se hace mal en las dos direcciones: o no se oye en un móvil, o
se come todo el margen de la mezcla con energía que nadie escucha nunca.

---

## 🔴 El dato que decide todo: por debajo de 50 Hz no hay nada

Un bajo en Re1 (36,7 Hz) y otro en Re2 (73,4 Hz), misma síntesis, mismos armónicos.
Reparto de energía medido por FFT:

| Banda | Re1 (36,7 Hz) | Re2 (73,4 Hz) |
|---|---|---|
| **Menos de 50 Hz** | **76,54 %** | 0,00 % |
| 50–120 Hz | 22,84 % | 73,64 % |
| 120–400 Hz | 0,62 % | 26,36 % |

**Tres cuartas partes de la energía del Re1 son inaudibles en el móvil donde se ve el
canal.** No es que suene flojo: es que ese 76 % ocupa margen, obliga a bajar todo lo
demás y no llega a ningún oído.

Confirmado por el medidor: con la misma ganancia de síntesis, el Re1 mide **5,3 LU menos
que el Re2**. La medida de sonoridad de la norma aplica el mismo descuento a los graves
que un altavoz pequeño — por eso el número coincide con lo que se oye.

## Dónde cortar

```
highpass=f=48:poles=2
```

48 Hz con dos polos: deja intacto el Re2 (73,4 Hz) y su segundo armónico, y corta el
subgrave que no va a salir por ningún lado. Con `poles=1` la pendiente es tan suave que
deja pasar media banda; con `poles=4` empieza a colorear justo donde vive el bajo.

| Nota más grave | Hz | Veredicto |
|---|---|---|
| Do1 | 32,70 | Inservible en móvil |
| Re1 | 36,71 | Inservible en móvil |
| **La1** | **55,00** | El suelo real del canal |
| **Re2** | **73,42** | La nota de trabajo |
| Do2 | 65,41 | Cómoda |
| La2 | 110,00 | Ya no es bajo: es registro medio |

Por debajo de La1 (55 Hz) sólo van los **impactos** (`84`), que se sienten en un buen
equipo y no estorban en el malo porque duran 200 ms, no cuatro segundos.

## El código

```python
def bajo(nota, dur=3.4, p="bj"):
    """Cuatro armónicos, sin caída propia, y un highpass que tira lo inaudible."""
    f0 = hz(nota); ps, et = [], []
    for k, (i, g) in enumerate([(1,1.00),(2,0.50),(3,0.22),(4,0.09)]):
        ps.append(f"sine=f={f0*i:.4f}:d={dur:.3f}:sample_rate=44100,volume={g}[{p}{k}]")
        et.append(f"[{p}{k}]")
    return (";".join(ps) + ";" + "".join(et) + f"amix=inputs=4:normalize=0,"
            # decaimiento lento: sostiene, no golpea
            f"volume='pow(max(0,1-t/{dur:.2f}),1.5)':eval=frame,"
            f"afade=t=in:st=0:d=0.030,"
            f"highpass=f=48:poles=2,volume=1.9")
```

Medido: **I = −26,3 LUFS, pico real −12,0 dBFS, LRA 2,0 LU** en 3,40 s. El ataque de
30 ms da 46 ms medidos al 90 % del pico: una cuerda pulsada, ni golpe ni aparición.

## El 2.º armónico es lo que salva el móvil

`(2, 0.50)` — el segundo armónico a la mitad de la fundamental. Es el número más
importante de la función y por una razón concreta: **un altavoz de móvil no reproduce
73 Hz, pero sí 147 Hz**, y el oído reconstruye la fundamental que falta a partir de los
armónicos. Con el segundo armónico fuerte, la nota se percibe grave incluso en un
altavoz que no puede emitirla.

| Perfil | En equipo bueno | En móvil |
|---|---|---|
| Sólo fundamental | Grave y limpio | **No se oye nada** |
| Fundamental + 2.º a 0,50 | Grave y limpio | Se percibe la nota |
| Fundamental + 2.º a 1,00 | Zumbón | Se oye, pero deja de ser bajo |

## Cuánto sostener

| Tramo | Duración de la nota | Por qué |
|---|---|---|
| Colchón de exposición | 3,0–3,4 s, una por compás | Fundamento sin llamar la atención |
| Antes de una cifra | Se apaga y **no entra** | El grave lleno quita impacto al golpe |
| Remate | 4–5 s con cola larga | Cierra por peso, no por volumen |

La regla del canal: **el bajo se calla antes de la cifra**. No se baja: se calla. Un
grave sostenido debajo de un impacto se lo come entero (`84`).

## El error de mezcla que embarra

Bajo y voz no compiten: viven en sitios distintos. Lo que sí compite es **bajo y piano
grave**. El ostinato del piano (`101`) toca Re2 y Si♭1 en la mano izquierda — las mismas
notas que el bajo. Si suenan los dos, se suman en fase y el resultado es barro.

Con piano en la pieza, **o bajo o mano izquierda**, nunca los dos. En el canal el bajo
se reserva para las piezas sin piano.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Nota por debajo de 50 Hz | El 76 % de la energía es inaudible y gasta margen |
| Sin `highpass` | El subgrave obliga a bajar todo lo demás sin dar nada a cambio |
| `poles=1` en el highpass | La pendiente es tan suave que no corta nada |
| Sólo fundamental, sin 2.º armónico | Desaparece entero en un móvil |
| 2.º armónico igual de fuerte | Zumbón: deja de leerse como bajo |
| Bajo sonando debajo de un impacto | Se come el golpe |
| Bajo y mano izquierda del piano a la vez | Barro: las dos ocupan Re2 |
| Ataque instantáneo | Suena a golpe, no a cuerda pulsada |

## Relacionado

`100` anatomía · `101` piano · `106` texturas · `84` picos dramáticos · `86` medir el audio
