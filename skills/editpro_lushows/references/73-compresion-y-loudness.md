# 73 — Compresión y loudness

Este módulo cierra la cadena de `70`: compresor, normalización LUFS y limitador. Los tres pasos que no
quitan nada, sino que **igualan**.

Y es el módulo que más plata vale de toda la biblioteca de audio, porque es el que decide si tu video
suena igual de fuerte que el del competidor cuando salen uno detrás del otro en el feed. Una voz limpia
y bien ecualizada que sale a −22 LUFS pierde contra una voz mediocre que sale a −14. Injusto, pero así
funciona.

---

## Parte 1 — El compresor

### Qué hace, sin metáforas raras

El compresor **baja lo que suena fuerte**. Punto. Nada más. Lo que pasa es que después le subes el
volumen a todo (eso es el `makeup`), y el resultado neto es que **lo suave subió**.

Un compresor no "hace la voz más fuerte". Achica la distancia entre lo más suave y lo más fuerte, y
después esa señal más pareja se puede subir sin que los picos saturen.

Por qué lo necesitas: nadie habla parejo. Empiezas la frase fuerte y la terminas apagada, das énfasis en
una palabra y la siguiente se cae. Sin compresión, el oyente tiene que subirle y bajarle. Con compresión,
la voz se queda quieta en un nivel y se siente **cerca**.

### Los cinco parámetros

```bash
ffmpeg -i voz_eq.wav -af "acompressor=threshold=-20dB:ratio=3:attack=15:release=180:makeup=2" voz_comp.wav
```

| Parámetro | Qué es | Valor para voz | Qué pasa si te pasas |
|---|---|---|---|
| `threshold` | El nivel a partir del cual empieza a bajar | **−18 a −24 dB** | Muy bajo: comprime todo, suena aplastado |
| `ratio` | Cuánto baja lo que pasó el umbral. `3` = por cada 3 dB que suba, deja pasar 1 | **2,5 – 4** | Arriba de 6 suena a radio AM |
| `attack` | Cuánto tarda en reaccionar, en ms | **10 – 20** | Muy rápido: mata las consonantes, voz sin filo |
| `release` | Cuánto tarda en soltar, en ms | **150 – 250** | Muy corto: "bombea", se oye respirar |
| `makeup` | Cuánto vuelve a subir después | **1,5 – 3** | Mucho: satura |

Los valores medidos que funcionaron en material real (ver `70`):

```
threshold=-20dB : ratio=3 : attack=15 : release=180 : makeup=2
```

Esa es tu configuración por defecto para voz hablada. Empieza ahí y muévete poco.

### Por qué esos valores y no otros

**`attack=15` ms.** El arranque de una consonante ("p", "t", "k") dura unos pocos milisegundos y es lo
que le da claridad y filo a la palabra. Si el attack es de 1 ms, el compresor lo aplasta y la voz queda
blanda, sin ataque. Con 15 ms el compresor deja pasar el filo de la consonante y agarra el cuerpo de la
vocal, que es lo que quieres controlar.

**`release=180` ms.** Aproximadamente el tiempo entre sílabas al hablar normal. Si suelta más rápido,
el compresor sube y baja *dentro* de la palabra y eso es el "bombeo": se oye como si el audio respirara.
Si suelta más lento, se queda agarrado y la frase siguiente empieza hundida.

**`ratio=3`.** Es el punto donde el control se nota pero no se oye. Ratio 2 casi no hace nada. Ratio 8
ya es un efecto, no una corrección.

**`threshold=-20dB`.** Debe quedar donde el compresor solo trabaje en las partes fuertes. Si tu voz vive
en −18 dB y pones el umbral en −30, estás comprimiendo el 100% del tiempo y eso es aplastar, no
controlar.

### Cómo saber si el umbral está bien

La regla profesional: **el compresor debe estar reduciendo entre 3 y 6 dB en los picos, y 0 dB en las
partes suaves.** Si nunca llega a 3, no está haciendo nada. Si nunca baja de 6, está aplastando.

En ffmpeg puedes verlo con `astats` comparando antes y después:

```bash
ffmpeg -i voz_eq.wav -af astats=metadata=1 -f null - 2>&1 | grep -E "Peak level|RMS level"
ffmpeg -i voz_comp.wav -af astats=metadata=1 -f null - 2>&1 | grep -E "Peak level|RMS level"
```

Lo que quieres ver: el **pico** bajó bastante, el **RMS** (el promedio) casi no. Eso es compresión bien
hecha. Si los dos bajaron igual, solo le bajaste el volumen a todo.

### Compresión en dos etapas (el truco de los profesionales)

Para voz en off de anuncio, dos compresores suaves suenan mejor que uno fuerte:

```bash
ffmpeg -i voz_eq.wav -af "acompressor=threshold=-18dB:ratio=2.5:attack=20:release=200:makeup=1.5,acompressor=threshold=-12dB:ratio=4:attack=5:release=100:makeup=1.5" voz_comp2.wav
```

El primero controla la dinámica general con calma (attack lento). El segundo agarra solo los picos que
se le escaparon al primero (attack rápido, umbral alto). Cada uno reduce 3 dB en vez de que uno solo
reduzca 6. Se oye más natural.

### `compand` — cuando necesitas más control

`acompressor` es fácil. `compand` es el que usan cuando quieren una curva a medida:

```bash
ffmpeg -i voz.wav -af "compand=attacks=0.02:decays=0.2:points=-80/-80|-45/-25|-27/-15|-5/-5|0/-3:soft-knee=6:gain=2" salida.wav
```

Los `points` son pares `entrada/salida` en dB: lo que entre en −45 dB sale en −25 (sube 20 dB); lo que
entre en −5 sale en −5 (no lo toca). Es una curva que levanta lo muy bajito, justo lo que se necesita
cuando alguien habla muy suave en partes. Para el 90% de los casos no lo necesitas.

---

## Parte 2 — LUFS y las plataformas

### Qué es LUFS, otra vez y para que quede

**LUFS** (Loudness Units relative to Full Scale) mide qué tan fuerte suena algo **en promedio y como lo
percibe el oído humano**, no cuánto miden sus picos. Es un promedio ponderado: le da más peso a las
frecuencias que el oído percibe más fuerte.

Tres números salen de la medición:

| Número | Qué es | Qué te dice |
|---|---|---|
| **I (Integrated)** | Promedio de toda la pieza | Qué tan fuerte se va a oír |
| **TP (True Peak)** | El pico real, incluyendo lo que aparece al convertir a MP3/AAC | Si va a distorsionar |
| **LRA (Loudness Range)** | Diferencia entre partes suaves y fuertes | Qué tan dinámico es |

### El estándar: −14 LUFS con pico verdadero a −1,5 dB

Para redes sociales, ese es el destino. Y hay una razón mecánica detrás de cada número.

**Por qué −14 y no más bajo:** las plataformas normalizan. Si entregas a −20, la plataforma le sube 6 dB
a tu video — **y le sube 6 dB al ruido de fondo con él**. Todo el trabajo del módulo `71` se te devuelve.
Entregar bajito no es "seguro": es regalarle el control a un algoritmo que no oyó tu video.

**Por qué −14 y no más alto:** si entregas a −9, la plataforma te baja 5 dB. No te destruye, pero perdiste
dinámica al comprimir de más para llegar allá, y ahora suena aplastado *y* al mismo volumen que el de
todos. Comprimiste gratis.

**Por qué el pico verdadero a −1,5 dB y no a 0:** porque cuando el archivo se convierte a AAC o MP3
(que es lo que hace la plataforma al subirlo), aparecen **picos entre muestras** que no estaban en el
original. Un archivo con picos en 0,0 dB después de la conversión puede tener picos en +0,8 dB, y eso
distorsiona. Dejar 1,5 dB de aire es el seguro. En el ejemplo medido de `70`, el pico pasó de 0,0 dB
(saturando) a −2,7 dB: eso es lo que se busca.

### Tabla por plataforma (agosto 2026)

| Plataforma | Objetivo | Nota importante |
|---|---|---|
| **YouTube** | −14 LUFS | Baja lo que esté más fuerte; **no sube** lo que esté bajito |
| **Instagram / Reels** | −14 LUFS | Normaliza. Circula el rumor de −10/−12; el consenso medido es −14 |
| **Facebook** | −14 LUFS | Igual que Instagram |
| **TikTok** | **−14 LUFS** como referencia sana | **No normaliza el feed** (a jul-2026): un archivo más fuerte suena más fuerte de verdad |
| **Spotify** | −14 LUFS | Para podcast: −16 LUFS |
| **Apple Music / Podcasts** | −16 LUFS | Un poco más bajo por diseño |
| **Netflix / broadcast** | −24 LKFS (ATSC A/85) | Otro mundo. No apliques esto a redes |

**Honestidad obligatoria:** TikTok, Instagram, Facebook y X **no publican objetivos oficiales de LUFS**.
Todo número que encuentres para esas plataformas es una estimación de gente que midió. −14 es el consenso
razonable y es lo que uso. Quien te diga que Instagram "oficialmente normaliza a −11" te está vendiendo
una certeza que no existe.

**El caso TikTok merece párrafo aparte.** Si TikTok no normaliza, la tentación es entregar a −9 para
sonar más fuerte que los demás. Se puede, pero: (1) suena aplastado y cansa; (2) el mismo archivo lo vas
a subir a Instagram y allá te lo bajan; (3) si TikTok activa normalización mañana, todo tu catálogo
queda comprimido de más para nada. Mi recomendación: −14 en todo, y si de verdad quieres pelear volumen
en TikTok, haz un render aparte a −11 y ya.

---

## Parte 3 — Cómo medir y normalizar con `loudnorm`

### Medir (siempre primero)

```bash
ffmpeg -hide_banner -i video.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=summary -f null -
```

Te devuelve algo así:

```
Input Integrated:   -21.4 LUFS
Input True Peak:     -0.3 dBTP
Input LRA:           14.2 LU
Input Threshold:    -31.8 LUFS
```

Ese `-21.4` es tu problema: vas 7,4 dB por debajo del estándar.

### Normalizar en una pasada (rápido, aceptable)

```bash
ffmpeg -i video.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:v copy -c:a aac -b:a 192k salida.mp4
```

Esto funciona y para la mayoría de los reels es suficiente. Pero `loudnorm` en una pasada trabaja
**adivinando sobre la marcha**: no conoce el final del archivo cuando procesa el principio, así que
aplica una compresión dinámica que puede alterar el material. El resultado casi nunca cae exacto en
−14; suele quedar en −13,2 o −14,8.

### Normalizar en dos pasadas (lo correcto)

Este es el método profesional y no es más difícil, solo son dos comandos.

**Pasada 1 — medir en formato JSON:**

```bash
ffmpeg -hide_banner -i video.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null -
```

Sale un bloque así al final:

```json
{
    "input_i" : "-21.43",
    "input_tp" : "-0.29",
    "input_lra" : "14.20",
    "input_thresh" : "-31.83",
    "target_offset" : "0.42"
}
```

**Pasada 2 — normalizar usando esos números medidos:**

```bash
ffmpeg -i video.mp4 -af "loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-21.43:measured_TP=-0.29:measured_LRA=14.20:measured_thresh=-31.83:offset=0.42:linear=true" -c:v copy -c:a aac -b:a 192k salida.mp4
```

La clave es **`linear=true`**: con las medidas ya conocidas, `loudnorm` puede aplicar una ganancia
lineal — un solo ajuste de volumen parejo — en vez de comprimir dinámicamente. **No altera la dinámica
de tu mezcla.** Todo el trabajo del compresor se respeta.

Si el material no permite ganancia lineal (porque llegaría a saturar el pico), `loudnorm` cae
automáticamente en modo dinámico y te avisa en la consola. Eso es señal de que hay que comprimir un
poco más antes.

### Automatizarlo

En Windows con Git Bash, dos pasadas en un script:

```bash
#!/bin/bash
IN="$1"; OUT="$2"
J=$(ffmpeg -hide_banner -i "$IN" -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | tail -n 14)
I=$(echo "$J"   | grep input_i       | cut -d'"' -f4)
TP=$(echo "$J"  | grep input_tp      | cut -d'"' -f4)
LRA=$(echo "$J" | grep input_lra     | cut -d'"' -f4)
TH=$(echo "$J"  | grep input_thresh  | cut -d'"' -f4)
OFF=$(echo "$J" | grep target_offset | cut -d'"' -f4)
ffmpeg -i "$IN" -af "loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=$I:measured_TP=$TP:measured_LRA=$LRA:measured_thresh=$TH:offset=$OFF:linear=true" -c:v copy -c:a aac -b:a 192k "$OUT"
ffmpeg -hide_banner -i "$OUT" -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=summary -f null -
```

Úsalo así: `bash normalizar.sh entrada.mp4 salida.mp4`.

### El parámetro LRA

`LRA=11` es el rango dinámico objetivo: 11 unidades de diferencia entre lo suave y lo fuerte.

| LRA | Para qué |
|---|---|
| 5 – 8 | Anuncio, contenido de redes muy comprimido |
| **9 – 11** | **Redes, voz + música. El estándar** |
| 12 – 15 | Documental, narrativa con dinámica |
| 18+ | Cine, música clásica |

Si tu LRA de entrada es 20 y pides 11, `loudnorm` va a comprimir bastante para llegar. Mejor comprime tú
antes con el `acompressor` (donde tienes control) y llega a `loudnorm` con un LRA cercano al objetivo.

---

## Parte 4 — El limitador

El seguro final. `loudnorm` ya incluye uno (por eso el `TP=-1.5` se cumple), pero si estás armando la
cadena a mano o quieres control explícito:

```bash
ffmpeg -i entrada.wav -af "alimiter=level_in=1:level_out=1:limit=0.85:attack=5:release=50:asc=1" salida.wav
```

| Parámetro | Qué es | Valor |
|---|---|---|
| `limit` | Techo en escala lineal. **0,85 ≈ −1,4 dB** | 0,85 |
| `attack` | ms | 5 |
| `release` | ms | 50 |
| `asc` | Compensación automática de nivel: suaviza el trabajo del limitador | `1` |

De lineal a dB: 1,0 = 0 dB · 0,9 = −0,9 dB · **0,85 = −1,4 dB** · 0,8 = −1,9 dB · 0,7 = −3,1 dB.

**Un limitador no es un compresor con ratio alto.** Un compresor moldea el sonido, el limitador solo
impide que algo pase el techo. Si tu limitador está trabajando todo el tiempo, el problema está tres
pasos antes.

---

## La cadena completa de compresión y loudness

```bash
# 1) comprimir (sobre el audio ya limpio y ecualizado)
ffmpeg -i voz_eq.wav -af "acompressor=threshold=-20dB:ratio=3:attack=15:release=180:makeup=2" voz_comp.wav

# 2) montar el video completo con música, efectos, todo

# 3) medir el video terminado
ffmpeg -hide_banner -i final_sin_normalizar.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null -

# 4) normalizar con los números medidos + linear=true
ffmpeg -i final_sin_normalizar.mp4 -af "loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=...:measured_TP=...:measured_LRA=...:measured_thresh=...:linear=true" -c:v copy -c:a aac -b:a 192k ENTREGA.mp4

# 5) verificar
ffmpeg -hide_banner -i ENTREGA.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=summary -f null -
```

El orden de los pasos 2 y 3 es lo que más gente equivoca: **se normaliza el video terminado, con música
y todo**, no los clips sueltos. LUFS es un promedio de la pieza completa. Normalizar cada clip a −14 y
después montarlos da una pieza que no está en −14.

---

## Errores comunes

- **Normalizar clips sueltos en vez de la pieza terminada.** LUFS es promedio del todo. Normaliza al final.
- **Entregar a −20 LUFS "para no saturar".** La plataforma te sube el volumen **y el ruido con él**.
- **Entregar con picos en 0,0 dB.** La conversión a AAC crea picos entre muestras y te distorsiona.
  Deja −1,5 dB.
- **Usar `loudnorm` de una pasada y creer que quedó exacto.** Queda cerca, no exacto, y comprime.
  Dos pasadas con `linear=true` cuando importa.
- **Attack de compresor muy rápido (1–3 ms).** Mata las consonantes, la voz queda blanda.
- **Release muy corto (< 100 ms).** El compresor "bombea", se oye respirar.
- **Ratio de 8 o más para voz hablada.** Es un efecto, no una corrección. 2,5–4.
- **Umbral tan bajo que comprime el 100% del tiempo.** Eso no es controlar, es aplastar.
- **Poner un limitador a trabajar 5 dB.** El limitador es un seguro, no una herramienta de mezcla.
- **Aplicar el estándar de broadcast (−24 LKFS) a un reel.** Va a sonar mudo.
- **Creer que los números de Instagram y TikTok son oficiales.** No lo son. −14 es consenso, no ley.
- **Comprimir más para "ganar" en TikTok.** El mismo archivo va a Instagram y allá te lo bajan igual.

---

## Checklist

- [ ] El compresor va **después** del EQ, sobre audio ya limpio.
- [ ] `threshold` está donde el compresor **reduce 3–6 dB en los picos y 0 en lo suave**.
- [ ] `ratio` entre **2,5 y 4**.
- [ ] `attack` entre **10 y 20 ms** (no aplasta las consonantes).
- [ ] `release` entre **150 y 250 ms** (no bombea).
- [ ] Verifiqué con `astats` que **bajó el pico mucho más que el RMS**.
- [ ] La normalización LUFS se hizo sobre el **video terminado**, con música y efectos.
- [ ] Medí primero con **`print_format=json`** y normalicé con **`measured_*` + `linear=true`**.
- [ ] El objetivo es **I=−14, TP=−1,5, LRA=11** (o el de la plataforma correspondiente).
- [ ] **Verifiqué el archivo final** con `print_format=summary` y está dentro de ±0,5 LUFS.
- [ ] El **pico verdadero final no pasa de −1,0 dBTP**.
- [ ] Si el material va a varias plataformas, sé cuál normaliza y cuál no.
- [ ] Escuché el resultado en **parlante de celular** al lado de un video de referencia del mismo nicho:
      suena igual de fuerte, no más bajito.
