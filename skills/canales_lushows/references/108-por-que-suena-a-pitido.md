# 108 · Por qué suena a pitido

**Qué resuelve:** el catálogo de lo que delata a un sintetizador barato. Son seis
defectos, cada uno con su medición y su arreglo. El fondo que el canal tuvo durante
semanas — ruido rosa filtrado más un tono de 55 Hz — los tenía **todos a la vez**.

---

## El banco de pruebas

Todas las versiones parten del mismo Do4 de cinco armónicos, 2,5 s, y sólo cambian en
un defecto cada una:

```bash
VOCES="sine=f=261.63:d=2.5:sample_rate=44100,volume='1.0*exp(-t/1.375)':eval=frame[h0];\
sine=f=523.26:d=2.5:sample_rate=44100,volume='0.380*exp(-t/0.809)':eval=frame[h1];\
sine=f=784.89:d=2.5:sample_rate=44100,volume='0.180*exp(-t/0.573)':eval=frame[h2];\
sine=f=1046.5:d=2.5:sample_rate=44100,volume='0.085*exp(-t/0.430)':eval=frame[h3];\
sine=f=1308.1:d=2.5:sample_rate=44100,volume='0.040*exp(-t/0.335)':eval=frame[h4];\
[h0][h1][h2][h3][h4]amix=inputs=5:normalize=0"

# la versión buena
ffmpeg -filter_complex "$VOCES,afade=t=in:st=0:d=0.008,afade=t=out:st=2.15:d=0.35,\
aecho=0.92:0.35:55|110:0.10|0.05,volume=2.2,alimiter=limit=0.80:level=disabled[out]" \
  -map "[out]" -ar 44100 -ac 1 -y bien.wav
```

| Versión | I | Pico real |
|---|---|---|
| bien | −31,0 LUFS | −19,5 dBFS |
| caídas iguales | −30,6 LUFS | −19,5 dBFS |
| sin sala | −20,5 LUFS | −9,7 dBFS |
| seno puro | −15,1 LUFS | −11,2 dBFS |

**El defecto nunca está en el volumen. Está en la forma.**

## 1 · Un seno pelado

| | |
|---|---|
| **Antes** | `sine=f=261.63,volume=0.5` → pitido de examen de oído |
| **Después** | Cinco armónicos con ganancias `1 · 0,38 · 0,18 · 0,085 · 0,04` |

Un seno no es un instrumento: es una medida. El timbre vive en los armónicos (`100`).
Y un `sine` de ffmpeg sale a 0,125, no a escala completa: 18 dB por debajo de un
`aevalsrc` equivalente.

## 2 · Todos los armónicos con la misma caída

| | |
|---|---|
| **Antes** | `exp(-t/0.8)` para los cinco → órgano de juguete, la nota muere plana |
| **Después** | `tau = dur·0,55 / caída` con caídas `1,0 · 1,7 · 2,4 · 3,2 · 4,1` |

Con caídas propias el 5.º armónico pierde **39 dB** respecto de la fundamental en 2,4 s
y el 2.º sólo 8,8 (tabla en `101`). Ese desnivel creciente **es** el redondeo de una
nota real.

## 3 · Cero desafine

| | |
|---|---|
| **Antes** | Tres voces en la frecuencia exacta → una sola voz más fuerte, sin cuerpo |
| **Después** | Copias a `×0,9965` y `×1,0037`: el batido es lo que se oye como «cuerpo» |

Medido sobre un colchón de 14 s, recorrido del centroide espectral:

| Versión | Centroide | Desviación |
|---|---|---|
| Pad con desafine y movimiento | 184 Hz | **127,6 Hz** |
| Mismo pad sin ninguna de las dos cosas | 119 Hz | 42,5 Hz |
| El ruido rosa + 55 Hz que teníamos | 405 Hz | **17,4 Hz** |

El fondo viejo era **plano en el tiempo**. Por eso el oído lo archivaba como ruido de
fondo y no como música.

## 4 · Ausencia de sala

Sin `aecho` el instrumento queda pegado a la cara. «Sin sala» mide 10,5 LU **más alto**
que la versión buena con la misma ganancia: la sala reparte la energía en el tiempo, y
esa dispersión es lo que el oído lee como espacio (`107`).

## 5 · El ataque equivocado

El ataque no evita un chasquido (un `sine` arranca en fase cero y no chasquea nunca):
**el ataque dice qué instrumento es.** Medido al 90 % del pico: 7 ms es un golpe de
piano, 46 ms una cuerda pulsada, 271 ms un arco que empuja, 440 ms algo que aparece.

El chasquido de verdad aparece al **cortar dentro de una señal en marcha**: un
`atrim=start=0.5001` sobre un tono deja la primera muestra en **−0,4473**, un escalón 24
veces mayor que el paso natural entre muestras. Ahí sí hace falta un `afade` de 8 ms.

## 6 · Los tres fallos de sintaxis que lo tiran todo

```bash
# 🔴 fuentes en -af: no arranca. Así se cayeron los 22 efectos del canal de golpe
ffmpeg -af "sine=f=55:d=3" -y out.wav                       # ❌
ffmpeg -filter_complex "sine=f=55:d=3,volume=0.3[a]" ...    # ✅

# 🔴 expresión con t sin :eval=frame
volume='exp(-t/1.4)'              # ❌ Invalid value NaN for volume  (el grafo no arranca)
volume='exp(-t/1.4)':eval=frame   # ✅

# 🔴 alimiter con el auto-nivel puesto: NO limita, re-normaliza a fondo de escala
volume=24,alimiter=limit=0.90                  # pico medido:  0,00 dBFS  ❌
volume=24,alimiter=limit=0.90:level=disabled   # pico medido: -0,91 dBFS  ✅
```

El tercero es el más traicionero porque no da error: `level` viene **activado por
defecto** y sube la salida hasta el techo que le pusiste. Sin `:level=disabled`,
`alimiter` no es un limitador: es un normalizador.

## 7 · `anoisesrc` sin semilla no es reproducible

El mismo comando cuatro veces seguidas sobre una flauta con soplo da picos de
`0,00290 · 0,01999 · 0,00290 · 0,00284`: un vaivén de **17 dB**, con una de las cuatro
casi a fondo de escala. Con `seed=1729` las pasadas coinciden a la cuarta cifra.
Cualquier ajuste en dos pasadas es **inservible** sin semilla: la pasada que mides no es
la que se publica.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| `alimiter` sin `:level=disabled` | No limita: normaliza a 0 dBFS |
| `anoisesrc` sin `seed` | Cada render es otro archivo; la medición no vale |

## Relacionado

`100` anatomía · `101` piano · `106` texturas · `107` la sala · `81` sintetizar efectos
