# 104 · Percusión y golpes

**Qué resuelve:** el golpe no tiene nota. No se construye con armónicos: se construye
con **ruido, una envolvente muy corta y un filtro resonante**. Quien intente hacer un
timbal sumando senos acaba con un pitido grave; quien lance ruido blanco sin filtrar
acaba con un «pff» de aerosol.

---

## La receta, en tres piezas

| Pieza | Qué aporta | Filtro |
|---|---|---|
| **Ruido** | La materia | `anoisesrc=c=white:a=0.9:seed=1729` |
| **Envolvente corta** | El gesto de golpear | `volume='pow(max(0,1-t/T),E)':eval=frame` |
| **Filtro resonante** | El objeto golpeado | `bandpass` + `equalizer` con Q alto |

El tercero es el que más se olvida. Un ruido con envolvente es un golpe genérico; el
mismo ruido a través de una resonancia marcada **es un objeto**.

## El golpe de mesa: el más útil del canal

```bash
ffmpeg -filter_complex "\
anoisesrc=c=white:a=0.9:d=0.35:r=44100:seed=1729,\
bandpass=f=240:width_type=h:w=90,\
equalizer=f=240:width_type=q:w=8:g=14,\
equalizer=f=1250:width_type=q:w=6:g=8,\
volume='pow(max(0,1-t/0.075),3.0)':eval=frame,volume=1.6[out]" \
  -map "[out]" -ar 44100 -ac 1 -y mesa.wav
```

Las **dos resonancias** (240 Hz con Q=8, 1250 Hz con Q=6) son la madera. Con `w` (la Q)
por debajo de 4 la resonancia se ensancha tanto que vuelve a ser ruido.

Mismo ruido, misma envolvente, con y sin los filtros — normalizados los dos al mismo
pico de −12 dBFS:

Con los filtros: un nudillo sobre una mesa de madera. El mismo ruido y la misma
envolvente sin ellos, normalizados los dos al mismo pico: un chasquido de estática.

## El timbal: el golpe que **cae de altura**

Un parche tenso baja de frecuencia mientras se relaja; sin esa caída un timbal es un
bombo aburrido. Se escribe como un `aevalsrc` cuya fase es la **integral** de la
frecuencia `f(t) = f1 + (f0 − f1)·e^(−t/τ)`:

```python
def timbal(dur=1.6, f0=92, f1=58, tau=0.090, p="tm"):
    k = (f0 - f1) * tau     # fase = 2π·[ f1·t + k·(1 − e^(−t/τ)) ]
    return (f"aevalsrc='sin(2*PI*({f1}*t+{k:.4f}*(1-exp(-t/{tau}))))':d={dur:.2f}:s=44100,"
            f"volume='pow(max(0,1-t/{dur-0.1:.2f}),2.0)':eval=frame[{p}1];"
            # el golpe de la maza sobre el parche: 35 ms de ruido de banda
            f"anoisesrc=c=white:a=0.9:d={dur:.2f}:r=44100:seed=1729,"
            f"bandpass=f=220:width_type=h:w=180,"
            f"volume='0.5*pow(max(0,1-t/0.035),3)':eval=frame[{p}2];"
            f"[{p}1][{p}2]amix=inputs=2:normalize=0,volume=0.38")
```

92 → 58 Hz en 90 ms. Ojo: `aevalsrc` sale a **escala completa** y `sine` a 0,125;
mezclarlos sin compensar los 18 dB es el error clásico (`100`).

## La caja: tres capas que no se pueden separar

```python
def caja(dur=0.6, p="cj"):
    return (# 1) el cuerpo: ruido de banda estrecha en 190 Hz, 160 ms
            f"anoisesrc=c=white:a=0.9:d={dur}:r=44100:seed=1729,"
            f"bandpass=f=190:width_type=h:w=120,"
            f"volume='1.0*pow(max(0,1-t/0.16),2.4)':eval=frame[{p}1];"
            # 2) la bordonera: ruido agudo, más corto, 110 ms
            f"anoisesrc=c=white:a=0.9:d={dur}:r=44100:seed=1729,"
            f"highpass=f=1800,lowpass=f=9000,"
            f"volume='0.55*pow(max(0,1-t/0.11),3.2)':eval=frame[{p}2];"
            # 3) el tono del parche: altura sin nota, 90 ms
            f"sine=f=190:d={dur}:sample_rate=44100,"
            f"volume='2.6*pow(max(0,1-t/0.09),2.2)':eval=frame[{p}3];"
            f"[{p}1][{p}2][{p}3]amix=inputs=3:normalize=0,volume=0.30")
```

Las tres capas mueren en tiempos **distintos** (160, 110 y 90 ms). Con la misma
envolvente para las tres suena a caja de juguete: el desfase entre ellas es la caja.

## El exponente de la envolvente

`pow(max(0,1-t/T), E)` — `T` es cuánto dura, `E` es la dureza: **1,5–2,0** blanda
(timbal), **2,4–3,0** seca (caja, golpe de mesa), **3,2–4,0** muy seca (click,
bordonera), y de 6 en adelante ya no es un golpe sino un clic digital.

## 🔴 El `max(0, ...)` no es adorno: sin él el golpe explota

Pasado `T` la base `1-t/T` se vuelve **negativa**. Comprobado sobre 0,5 s de ruido con
`T = 0,075`:

| Envolvente | Qué pasa tras los 75 ms | Pico |
|---|---|---|
| `pow(1-t/0.075, 3.0)` | Base negativa al cubo: número grande y negativo, la salida queda **clavada a fondo de escala** | 1,000 |
| `pow(1-t/0.075, 2.4)` | Exponente fraccionario sobre base negativa: `NaN`, que ffmpeg resuelve como silencio | 0,900 |
| `pow(max(0,1-t/0.075), 3.0)` | Silencio limpio | −12 dBFS |

El primer caso es el peligroso: un golpe de nudillo de 75 ms se convierte en medio
segundo de ruido blanco a tope, **y no da ningún error**.

## 🔴 Un golpe no se puede medir con `ebur128`

```
b_mesa   0,39 s   I = -70,0 LUFS   pico real = -12,0 dBFS
b_caja   0,64 s   I = -30,6 LUFS   pico real = -12,0 dBFS
```

El integrado de la norma usa una **puerta** con ventanas de 400 ms: un golpe de 390 ms
no llega a abrirla y el medidor devuelve el suelo, −70 LUFS. No está callado: esa medida
no aplica. **Para percusión se mide el pico**; el integrado sólo vale a partir de ~1 s
de sonido continuo.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Ruido sin filtro resonante | «Pff» de aerosol: no hay objeto |
| Q (`w` del `equalizer`) por debajo de 4 | La resonancia se ensancha y vuelve a ser ruido |
| Las tres capas de la caja con la misma envolvente | Caja de juguete |
| Timbal sin caída de altura | Bombo aburrido |
| `pow` sin `max(0, ...)` | `NaN` pasado `T`: el grafo entero se cae |
| Mezclar `aevalsrc` con `sine` sin compensar | 18 dB de diferencia: uno tapa al otro |
| Juzgar un golpe por su LUFS integrado | −70 LUFS y pánico injustificado |

## Relacionado

`100` anatomía · `105` el bajo · `107` la sala · `109` banco · `84` picos dramáticos
