# 103 · Viento y madera

**Qué resuelve:** flauta y clarinete son los dos instrumentos que rompen la regla de
«suma armónicos y ya». La flauta casi no tiene armónicos y **sí tiene soplo**; el
clarinete tiene sólo los **impares**. Copiar el molde del piano para ellos da un
resultado que no se parece a nada.

---

## La flauta: el soplo es la mitad del instrumento

Una flauta es una fundamental casi limpia más **el aire que no llegó a convertirse en
nota**. Sin ese ruido no suena a flauta: suena a seno con vibrato. Pesos: fundamental
1,00 · 2.º armónico 0,16 · 3.º 0,05 · **soplo 0,085**.

```python
def flauta(nota, dur=2.4, p="fl"):
    f0 = hz(nota)
    return (
        f"sine=f={f0:.4f}:d={dur:.3f}:sample_rate=44100,volume=1.00[{p}1];"
        f"sine=f={f0*2:.4f}:d={dur:.3f}:sample_rate=44100,volume=0.16[{p}2];"
        f"sine=f={f0*3:.4f}:d={dur:.3f}:sample_rate=44100,volume=0.05[{p}3];"
        f"[{p}1][{p}2][{p}3]amix=inputs=3:normalize=0[{p}t];"
        # el soplo: ruido blanco ceñido a la región de la nota
        f"anoisesrc=c=white:a=0.9:d={dur:.3f}:r=44100:seed=1729,"
        f"highpass=f={f0*1.4:.0f},lowpass=f={min(f0*7,11000):.0f},volume=0.085[{p}a];"
        f"[{p}t][{p}a]amix=inputs=2:normalize=0,"
        f"vibrato=f=4.8:d=0.22,atrim=start=0.005,asetpts=PTS-STARTPTS,"
        f"afade=t=in:st=0:d=0.075:curve=qsin,"
        f"afade=t=out:st={dur-0.30:.2f}:d=0.30,volume=0.95")
```

El soplo va **ceñido a la nota**: `highpass=f0·1,4` lo despega de la fundamental (si no,
embarra el grave) y `lowpass=f0·7` evita que suene a escape de aire, con tope en 11 kHz
porque por encima ya no es aire, es siseo. El ataque de 75 ms con `curve=qsin` es lo que
distingue una flauta de un órgano: al aire le cuesta poner la columna en vibración,
aunque mucho menos que a un arco (`102`).

## El clarinete: sólo los impares

Un tubo cilíndrico cerrado por un extremo sólo resuena en armónicos impares. No es un
detalle de manual: es **lo que hace que un clarinete suene hueco** y no dulce.

```python
ARM_CLARINETE = [(1, 1.00), (3, 0.42), (5, 0.22), (7, 0.11), (9, 0.05)]
```

Medido por FFT sobre la síntesis real, un Re4 (293,7 Hz):

| Armónico | Frecuencia | Nivel bajo la fundamental |
|---|---|---|
| 1 | 293,7 Hz | 0,0 dB |
| 2 | 587,3 Hz | **−48,9 dB** |
| 3 | 881,0 Hz | −6,9 dB |
| 4 | 1174,7 Hz | **−47,1 dB** |
| 5 | 1468,3 Hz | −10,7 dB |
| 6 | 1762,0 Hz | **−41,7 dB** |
| 7 | 2055,7 Hz | −17,8 dB |
| 9 | 2643,0 Hz | −25,7 dB |

Los pares están 30–40 dB por debajo: lo que se ve ahí no son armónicos, es el suelo del
soplo. **Ese hueco de 40 dB entre par e impar es el clarinete.**

```python
def clarinete(nota, dur=2.8, p="cl"):
    f0 = hz(nota); ps, et = [], []
    for k, (i, g) in enumerate([(1,1.0),(3,0.42),(5,0.22),(7,0.11),(9,0.05)]):
        if f0*i > 15000: break
        ps.append(f"sine=f={f0*i:.4f}:d={dur:.3f}:sample_rate=44100,volume={g}[{p}{k}]")
        et.append(f"[{p}{k}]")
    ps.append(f"anoisesrc=c=white:a=0.9:d={dur:.3f}:r=44100:seed=1729,"
              f"highpass=f={f0*2:.0f},lowpass=f=7000,volume=0.045[{p}a]")
    et.append(f"[{p}a]")
    return (";".join(ps) + ";" + "".join(et) + f"amix=inputs={len(et)}:normalize=0,"
            "afade=t=in:st=0:d=0.055:curve=qsin,"
            f"afade=t=out:st={dur-0.28:.2f}:d=0.28,"
            # el formante que le da madera en vez de plástico
            "equalizer=f=1500:width_type=q:w=1.5:g=2.5,volume=0.80")
```

El clarinete **no lleva vibrato**: en la escritura orquestal es un instrumento de
sonido fijo, y ponérselo lo convierte inmediatamente en un sintetizador de los años 80.

## 🔴 El vibrato de la flauta necesita un `atrim` detrás

`vibrato` emite una o dos muestras `NaN` al arrancar, y un `NaN` sobrevive a `volume`,
a `afade` y a `amix`. En la flauta del banco eso dejaba el pico a fondo de escala sin
dar ningún error. El arreglo va inmediatamente después del filtro:

```
vibrato=f=4.8:d=0.22,atrim=start=0.005,asetpts=PTS-STARTPTS
```

Detalle completo y la tabla de cuántos `NaN` da cada profundidad, en `102`.

## Cuándo usar cada uno en el canal

| Tramo | Instrumento | Por qué |
|---|---|---|
| Una frase suelta sobre el colchón | Flauta aguda (La5) | Se recorta del piano sin taparlo |
| Algo que se cuenta y no consta | Clarinete grave (Re3–Re4) | Hueco, sin dulzura: suena a sospecha |
| Bajo la voz | **Ninguno de los dos** | Ambos viven en el registro de la voz y compiten |

Es la regla dura: la madera entra en los huecos de la narración, nunca debajo de ella.
Debajo va el piano y el bajo, que ocupan otro sitio del espectro (`105`).

## El formante: lo que separa madera de plástico

`equalizer=f=1500:width_type=q:w=1.5:g=2.5` resalta una resonancia **fija**, que no se
mueve con la nota. Un instrumento real tiene resonancias de cuerpo que están donde están
toque lo que toque; un sintetizador sube todo junto con la nota, y por eso se delata en
cuanto cambias de registro. En el canal: clarinete 1500 Hz +2,5 dB, violín 2600 Hz
+3,0 dB, flauta ninguno (el soplo ya cumple).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Flauta sin soplo | Un seno con vibrato; no se reconoce como instrumento |
| Soplo sin `highpass` | El ruido embarra el grave y tapa el piano |
| Clarinete con armónicos pares | Se pierde lo hueco: queda un oboe indeciso |
| Clarinete con vibrato | Sintetizador de los 80, sin remedio |
| Madera debajo de la voz | Compite en el mismo registro; toca bajarla hasta no oírse |
| Ataque instantáneo en viento | Suena a órgano: al aire le cuesta arrancar |
| `anoisesrc` sin `seed` | Cada render sale distinto (`108`) |

## Relacionado

`100` anatomía · `102` cuerda frotada · `105` el bajo · `109` banco · `85` ducking
