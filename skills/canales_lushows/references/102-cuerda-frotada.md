# 102 · Cuerda frotada

**Qué resuelve:** el violín y el violonchelo son **lo contrario del piano**. El piano es
un golpe que se apaga; la cuerda frotada es un arco que **sigue metiendo energía** todo
el tiempo. Copiar el molde del piano (ataque de 8 ms, caída exponencial) da algo que no
se parece a una cuerda ni de lejos.

---

## Las tres diferencias con el piano

Ataque: 7 ms el piano, **266 ms** el chelo. Cuerpo: el piano cae sin parar, la cuerda
**se sostiene**. Altura: fija en el piano, **oscilante** en la cuerda.

Medido sobre las dos síntesis del banco, envolvente en dB bajo su propio pico:

| t | Violonchelo | Piano |
|---|---|---|
| 0,1 s | −4,6 dB | −0,7 dB |
| 0,8 s | −0,3 dB | −5,6 dB |
| 1,5 s | −2,2 dB | −9,5 dB |
| 2,8 s | −0,6 dB | **−21,7 dB** |

El chelo se mantiene dentro de 5 dB durante los tres segundos; el piano pierde 21,7. Esa
tabla **es** la diferencia entre los dos instrumentos, y se consigue con una sola
decisión: la cuerda frotada no lleva `exp(-t/tau)` en ningún armónico.

## El código

```python
def cuerda(nota, dur, n=9, brillo=1.15, pref="s"):
    """Armónicos SOSTENIDOS: sin caída propia. El arco no deja de empujar."""
    f0 = hz(nota); partes, et = [], []
    for i in range(1, n+1):
        f = f0 * i
        if f > 15000: break
        partes.append(f"sine=f={f:.4f}:d={dur:.3f}:sample_rate=44100,"
                      f"volume={1.0/(i**brillo):.4f}[{pref}{i}]")
        et.append(f"[{pref}{i}]")
    return ";".join(partes)+";"+"".join(et)+f"amix=inputs={len(et)}:normalize=0"

def cello(nota, dur=3.2):
    return (cuerda(nota, dur, n=9, brillo=1.15, pref="vc") +
            ",vibrato=f=5.2:d=0.35,atrim=start=0.005,asetpts=PTS-STARTPTS,"
            "afade=t=in:st=0:d=0.22:curve=qsin,"            # el arco entrando
            f"afade=t=out:st={dur-0.40:.2f}:d=0.40,volume=0.55")

def violin(nota, dur=2.6):
    return (cuerda(nota, dur, n=7, brillo=1.35, pref="vn") +
            ",vibrato=f=6.0:d=0.40,atrim=start=0.005,asetpts=PTS-STARTPTS,"
            "afade=t=in:st=0:d=0.13:curve=qsin,"
            f"afade=t=out:st={dur-0.30:.2f}:d=0.30,"
            "equalizer=f=2600:width_type=q:w=1.2:g=3,volume=0.70")
```

Medido con la sala `sala` puesta (`107`): el chelo sale a **I = −23,0 LUFS, pico real
−14,1 dBFS, LRA 0,4 LU** en 3,41 s. Ese LRA de 0,4 confirma que se sostiene — el piano
en el mismo sitio da 20,3.

## El `brillo`: un solo número que cambia el instrumento

Las ganancias salen de `1/n^brillo`: con **1,00** sale una cuerda áspera, cerca del
puente; **1,15** es el violonchelo, rico y cálido; **1,35** el violín, más limpio y menos
grave; a partir de 1,80 se queda casi sin armónicos y deja de ser cuerda. Nueve
armónicos en el chelo y siete en el violín: el chelo suena más grave, así que le caben
más antes de los 15 kHz donde la serie deja de aportar nada.

## El ataque: `curve=qsin`, no lineal

```
afade=t=in:st=0:d=0.22:curve=qsin
```

El arco no entra a velocidad constante: agarra la cuerda, resbala, la engancha. Un
`afade` lineal se oye como un fader que alguien sube. `qsin` (un cuarto de seno) arranca
suave y termina decidido, que es exactamente el gesto. 130 ms para una entrada decidida
de violín, 220 ms para un chelo que empuja, 400 ms o más para algo que aparece.

## El vibrato es modulación de FRECUENCIA

```
vibrato=f=5.2:d=0.35      # f = veces por segundo · d = profundidad (0–1)
```

Hay que usar `vibrato` y no `tremolo`: los dos oscilan, pero `vibrato` mueve la
**frecuencia** (un dedo oscilando sobre la cuerda) y `tremolo` mueve la **amplitud**
(alguien moviendo el fader). Velocidad: por debajo de 4 Hz suena a desafinado, **5–6 Hz**
es el rango de un intérprete real, y por encima de 7,5 Hz suena a sintetizador nervioso.
Profundidad 0,30–0,45 en grave; por encima de 0,55 la nota pierde altura reconocible. El
vibrato va **antes** de los `afade`: después, modula también la entrada del arco.

## 🔴 `vibrato` emite muestras NaN al arrancar

Es el fallo más caro de este bloque y no da ningún error. El filtro saca **una o dos
muestras `NaN`** al principio del flujo, y cuántas depende de la profundidad: con
`d=0.22` da una (muestra 0), con `d=0.35` ninguna, con `d=0.40` da dos (muestras 3 y 4).

Un `NaN` sobrevive a `volume`, a `afade` (`NaN × 0` sigue siendo `NaN`) y a `amix`, y al
llegar a un filtro con línea de retardo contamina la mezcla entera: la flauta del banco
salía con **pico a fondo de escala** y 25 dB de factor de cresta donde debería haber 8.

```
vibrato=f=4.8:d=0.22,atrim=start=0.005,asetpts=PTS-STARTPTS
```

`asetpts` no es opcional: sin él el flujo empieza en t = 0,005 y todo lo de detrás se
desplaza.

## Cuándo usar cuerda en el canal

El **chelo grave** (Do2–Do3) es el único instrumento del canal que se sostiene debajo de
la voz sin taparla: vive por debajo de 300 Hz y la voz vive por encima. Va a −14 LU bajo
la narración en los datos que pesan, y a −12 LU con sala larga en el remate. El violín
agudo sirve para la tensión que crece, pero nunca debajo de la voz. Y debajo de una
cifra no va cuerda: va silencio (`84`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Armónicos con caída exponencial | Sale un piano con vibrato, no una cuerda |
| `afade` lineal en la entrada | Se oye como un fader, no como un arco |
| `tremolo` en vez de `vibrato` | Amplitud en lugar de frecuencia: suena a truco |
| Vibrato después de los `afade` | Tiembla también la entrada del arco |
| Profundidad por encima de 0,55 | La nota pierde altura reconocible |
| Violín sostenido bajo la voz | Compite en el mismo registro y hay que bajarlo hasta no oírlo |

## Relacionado

`100` anatomía · `101` piano · `103` viento y madera · `107` la sala · `109` banco
