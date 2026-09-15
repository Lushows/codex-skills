# 112 · El ostinato: la inevitabilidad

**Qué resuelve:** una figura grave que se repite **sin cambiar nunca** produce la
sensación de que lo que va a pasar ya está decidido. Es exactamente la forma de nuestras
historias: el espectador sabe desde el primer plano que el imperio se cae. El ostinato
es esa premisa convertida en sonido.

---

## Qué es y qué no es

| | Ostinato | Bucle |
|---|---|---|
| Qué se repite | Una figura **del bajo**, idéntica | El compás entero, todo |
| Qué cambia encima | La cima: melodía, color, densidad | Nada |
| Efecto | Inevitabilidad: el suelo no cede | Monotonía: el oído lo archiva |
| Duración útil | Minutos | 30-40 s y ya sobra |

Una sola decisión los separa: **si algo cambia por arriba mientras el bajo no cambia por
abajo**. Sin cima, un ostinato es un bucle con mejor nombre.

## Por qué encaja con una historia de final conocido

Nuestro gancho (`94`) dice el final en el segundo 6: *"perdió doscientos millones"*.
A partir de ahí el espectador no ve **qué** pasa, ve **cómo** se llega. El ostinato hace
lo mismo en el oído: el bajo ya dijo lo que va a pasar y lo repite mientras la melodía
de arriba se agita sin poder cambiarlo.

> Honestidad: que la repetición produzca "inevitabilidad" es lectura de oficio, no un
> resultado medido. Lo documentado es que la repetición aumenta la fluidez de
> procesamiento. Que eso se lea como destino y no como aburrimiento lo decide la cima.

## El motor

```python
def ostinato(compases=6, T=3.4, raiz="D2",
             acorde=("D3","F3","A3"), cima=None):
    """El bajo NO cambia. Lo único que se mueve es la cima."""
    ns = []
    for c in range(compases):
        t0 = c * T
        ns.append((t0, raiz, 3.0, 0.95))                  # el pie, siempre igual
        for k, a in enumerate(acorde):
            ns.append((t0 + 1.10 + k * 0.014, a, 2.2, 0.36))
        if cima and c >= 1:                               # el primer compás va desnudo
            ns.append((t0 + 0.45, cima[(c - 1) % len(cima)], 1.6, 0.50))
    return ns

tocar(ostinato(),                                "112_desnudo.wav")   # 24 notas · 21,27 s
tocar(ostinato(cima=["A4","F4","E4","D4","E4"]), "112_con_cima.wav")  # 29 notas · 21,27 s
```

Las dos duran **21,27 s** exactos: la cima no alarga nada, solo cambia lo que se oye
encima. Cinco notas de diferencia entre "fondo de ascensor" y "pieza".

## Los tres números del ostinato

| Parámetro | Valor del canal | Por qué |
|---|---|---|
| **Ciclo `T`** | 3,4 s (≈ 70 ppm en 4/4, ver `116`) | Un ciclo por respiración |
| **Duración del bajo** | 3,0 s | Deja 0,4 s de aire antes del golpe siguiente |
| **Intensidad del bajo** | 0,95 | La voz más fuerte de la pieza: manda el pie, no la melodía |

## Qué pasa de verdad si el bajo dura más que el ciclo

Con `dur > T` las notas graves se solapan y `amix=inputs=N:normalize=0` las **suma
aritméticamente** (`piano.py:106`). Lo que se dice siempre —"se satura y se vuelve
turbio"— **no aparece en la medida**. Medido con seis compases idénticos a T = 3,4 s,
cambiando solo la duración del bajo:

| `dur` bajo | Hueco `T−dur` | Total | Pico | < 110 Hz | Banda voz | **Grave − voz** |
|---|---|---|---|---|---|---|
| 2,4 s | 1,0 s | −28,98 | −16,11 | −32,01 | −40,48 | **8,47 dB** |
| **3,0 s** | **0,4 s** | −28,65 | −16,14 | −31,39 | −40,93 | **9,55 dB** |
| 4,2 s | −0,8 (solapa) | −28,34 | −16,01 | −30,83 | −41,49 | 10,66 dB |
| 6,0 s | −2,6 (solapa) | −28,77 | −16,80 | −31,23 | −42,14 | **10,91 dB** |

El nivel total no se mueve (el `loudnorm=I=-30` lo iguala) y el pico tampoco se dispara.
Lo que se mueve es el **reparto**: del bajo más corto al más solapado hay 2,4 dB de
corrimiento hacia el grave y la cima pierde 1,66 dB. Real, pequeño, y no la catástrofe
que se suele contar.

> Entonces, ¿por qué no solapar? **Por una razón musical, no de nivel.** Un bajo que no
> termina antes del siguiente deja de articular: el ostinato pasa a ser un pedal continuo
> y el pulso desaparece. Eso se oye; no se mide en el RMS.

El hueco entre 0,2 y 0,5 s es el punto; por encima de 0,8 s cada golpe queda aislado y
pasados 2,0 s ya no es ostinato, son golpes sueltos. En `_expediente` el hueco es de
**0,2 s** (T = 3,2 · dur = 3,0) y en `_cierre` también (T = 3,6 · dur = 3,4).

## Cómo se sostiene sin cansar

El bajo no se toca. Se varía **una cosa cada vez**: la cima cambia de nota · la cima
desaparece un ciclo entero (el hueco se nota más que cualquier nota) · el acorde cambia
de color sin mover la raíz (`D3·F3·A3` → `D3·F3·Bb3` → `Ab3·D3·F3`, ver `113`) · la
intensidad del acorde baja de 0,36 a 0,22 dos ciclos y vuelve · la raíz alterna entre
`D2` (73,42 Hz) y `Bb1` (58,27 Hz), como en `_expediente`.

Lo último ya es un ostinato de **dos** compases, no de uno: sigue siendo inevitable pero
se instala más despacio. Cualquier cambio que toque el bajo en **cada** compás ya no es
ostinato.

## El ostinato como reloj del montaje

Con `T` fijo, la música da una rejilla temporal gratis; colgar ahí los cortes y las
entradas de elemento (`14`, `39`) sale sin esfuerzo y se nota:
```python
T = 3.4
REJILLA = [round(i * T, 2) for i in range(12)]
# [0.0, 3.4, 6.8, 10.2, 13.6, 17.0, 20.4, 23.8, 27.2, 30.6, 34.0, 37.4]
```

La cifra ancla del episodio cae en un múltiplo de `T`, no donde caiga.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Bajo que dura más que el ciclo | Deja de articular: pedal continuo sin pulso (y −1,7 dB de cima) |
| Ostinato sin cima | Es un bucle: a los 40 s el oído lo archiva como ruido de fondo |
| Cambiar la figura del bajo "para que no aburra" | Se pierde lo único que el ostinato aporta |
| Cima en todos los compases, incluido el primero | El primer ciclo es el que instala el pie. Debe ir desnudo |
| Cima más fuerte que el bajo | Se convierte en canción con acompañamiento y pelea con la voz (`117`) |
| Variar dos cosas a la vez | Se percibe como pieza nueva, no como desarrollo |
| Montar el vídeo ignorando la rejilla de `T` | Imagen y sonido van cada uno por su lado, y se nota sin saber por qué |

## Relacionado

`111` la armonía que no resuelve · `114` modos y color · `116` tempo y pulso ·
`117` dejarle sitio a la voz · `127` variación sin repetición · `39` sincronizar gesto y palabra
