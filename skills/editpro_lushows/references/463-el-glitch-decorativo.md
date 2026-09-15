# 463 — El glitch decorativo: el fallo que tiene metrónomo

**Qué resuelve:** el `56` (punto 4) ya dice por qué la mayoría de los glitches se ven mal —duran
demasiado, son periódicos, van mudos y se aplican al video entero— y el `57-glitch-y-textura.md` da los
comandos para hacerlo bien. **→ ver `56` y `57` primero.** Aquí se mide la característica que el ojo
detecta sin saber nombrarla: **la regularidad**. Un fallo de señal real es irregular; un preset tiene
compás.

---

## 1. La magnitud: YDIF y su autocorrelación

`signalstats` de ffmpeg calcula, entre otras cosas, **YDIF**: cuánto cambia la luminancia media respecto
al fotograma anterior. Sobre un plano estático vale 0; cuando entra un glitch, se dispara. La serie de
YDIF es el electrocardiograma del clip.

🔴 **Con `-loglevel error` no imprime nada** y parece que el filtro falló. Hay que pedir `info` y
redirigir: es la trampa del `460`, §4.

```bash
ffmpeg -hide_banner -loglevel info -i clip.mp4 \
  -vf "signalstats,metadata=print:key=lavfi.signalstats.YDIF" \
  -f null - 2>&1 | grep YDIF | sed 's/.*=//' > clip.ydif
```

```python
# ritmo.py — rachas y periodicidad de la serie YDIF
import numpy as np, sys
for p in sys.argv[1:]:
    y = np.loadtxt(p); u = y > y.max()*0.25
    rachas = []
    for i in np.where(u)[0]:
        if rachas and i == rachas[-1][-1]+1: rachas[-1].append(i)
        else: rachas.append([i])
    c = y - y.mean(); ac = np.correlate(c,c,'full')[len(c)-1:]; ac /= ac[0]
    pico = int(np.argmax(ac[3:20]))+3
    print(f"{p}: {u.sum()}/{len(y)} fotogramas con evento ({u.sum()/len(y)*100:.0f}%)  "
          f"rachas={[len(r) for r in rachas]}  autocorrelación={ac[pico]:+.2f} "
          f"en desfase {pico}")
```

---

## 2. Los dos glitches, medidos

Mismo plano estático de 1,5 s a 30 fps. El de plantilla repite cada 0,30 s durante 0,13 s; el bueno
ocurre **una vez** y dura 3 fotogramas (`57`).

```bash
# el de plantilla: periódico
ffmpeg -y -loglevel error -i plano.mp4 -vf \
"chromashift=cbh=14:crh=-14:enable='lt(mod(t,0.30),0.13)',\
noise=alls=30:allf=t:enable='lt(mod(t,0.30),0.13)'" \
  -r 30 -c:v libx264 -crf 14 -pix_fmt yuv420p preset.mp4

# el bueno: una vez, 3 fotogramas
ffmpeg -y -loglevel error -i plano.mp4 -vf \
"chromashift=cbh=16:crh=-16:enable='between(t,0.60,0.667)',\
noise=alls=34:allf=t:enable='between(t,0.60,0.667)'" \
  -r 30 -c:v libx264 -crf 14 -pix_fmt yuv420p bueno.mp4
```

| | Fotogramas con evento | Rachas y duración | Autocorrelación | Caudal |
|---|---|---|---|---|
| Plano limpio | 0 / 45 | — | — | 0,9 Mb/s |
| Glitch bueno | **4 / 45 (9%)** | 1 racha de 4 | **+0,08** | 6,2 Mb/s |
| Glitch de plantilla | **24 / 45 (53%)** | **5 rachas de 5** | **+0,77** en desfase 9 | **35,3 Mb/s** |

La serie del preset se lee sola —`0 · 19,1 · 19,1 · 19,0 · 13,4 · 0 · 0 · 0 · 0 · 13,4 · 19,1 …`—: el
patrón se repite exacto cinco veces. Eso no es un fallo, es un motor.

**Nota de lectura:** una racha de N fotogramas alterados produce N+1 valores de YDIF distintos de cero,
porque también cuenta el fotograma en que la imagen vuelve a la normalidad. El glitch "bueno" de 3
fotogramas da una racha de 4.

---

## 3. Los umbrales

> **Autocorrelación de YDIF superior a +0,40 en cualquier desfase de 2 a 20 fotogramas: el glitch tiene
> metrónomo y delata.** Por debajo de +0,15, se lee como accidente.
>
> **Más del 15% de los fotogramas con evento: ya no es un fallo, es una textura.** Y una textura
> continua se aplica de otra manera (`57`, grano).

El tercer número es el que nadie mira: **el caudal**. El mismo clip, mismo CRF, pesa **39 veces más**
con el glitch periódico (35,3 Mb/s frente a 0,9). El ruido es lo más caro de comprimir que existe. En
una red que recomprime, ese caudal se lo lleva el glitch y **el resto del video se degrada para
pagarlo**: la cara del presentador pierde detalle por culpa de un adorno. Ver
`93-compresion-sin-perder-calidad.md`.

---

## 4. Qué se hace en su lugar

La receta está en `57` y no la repito. Lo que este módulo añade es **cómo generar la irregularidad**,
que es lo que el preset no sabe hacer: en vez de `mod(t,0.30)`, una lista de instantes elegidos a mano,
cada uno con duración distinta.

```bash
# tres micro-fallos irregulares: 2, 1 y 3 fotogramas, en instantes que no forman serie
-vf "chromashift=cbh=13:crh=-13:enable='between(t,1.233,1.300)+between(t,3.867,3.900)+between(t,7.400,7.500)'"
```

Medido con `ritmo.py` sobre un plano de 9 s: **3 rachas de 4, 2 y 4 fotogramas, el 4% del clip,
autocorrelación +0,11**. No hay compás porque los huecos entre eventos (2,57 s y 3,50 s) no son
múltiplos entre sí. Y **cada uno de los tres necesita su corte de
audio en el mismo fotograma** (`76-diseño-sonoro.md`): un fallo visual en un mundo que suena perfecto es
la incoherencia que el `56` describe.

---

## Errores frecuentes

1. **Medir con `-loglevel error`.** No sale nada. Es la trampa del `460`.
2. **Usar `mod(t, …)` para repartir los glitches.** Es exactamente el generador de compás: la
   autocorrelación lo caza siempre.
3. **Elegir instantes "al azar" que son múltiplos entre sí** (1,0 · 2,0 · 3,0). Siguen dando pico de
   autocorrelación. Que los huecos sean primos entre sí a ojo.
4. **Dar por bueno un glitch sin mirar el caudal.** ×39 en el banco medido. Comprueba el bitrate antes
   de exportar.
5. **Poner el glitch sobre el video entero en vez de sobre el fotograma.** Un fallo de señal es
   instantáneo; si dura, es textura y se trata como textura (`57`).
6. **Glitch visual sin evento de audio.** El fallo más repetido de todos.
7. **Confundir esta medición con la de cambio de escena.** YDIF también se dispara en los cortes; mide
   sobre un tramo sin cortes o descuenta los fotogramas de corte (`108`, cambios de escena).

---

## Relacionado

- `56-efectos-que-se-ven-baratos.md` (punto 4) — el porqué.
- `57-glitch-y-textura.md` — **cómo se hace bien: grano, VHS, halftone, y el glitch con criterio.**
- `108-ffmpeg-analisis-y-medicion.md` — `signalstats` y el resto del instrumental.
- `76-diseño-sonoro.md` — el evento de audio que el glitch necesita para existir.
- `428-el-efecto-que-se-rompe-en-la-compresion.md` — **YDIF como termómetro de textura temporal, y la
  medida de que el glitch de 2 fotogramas sí sobrevive al reencode de la red.**
- `93-compresion-sin-perder-calidad.md` — por qué el caudal del ruido arruina el resto del video.
- `460-el-catalogo-medido.md` — la trampa del `-loglevel` y el banco.
