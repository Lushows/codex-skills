# 293 — Loudness de verdad: el módulo del error

Este módulo existe porque se cometió el error. Vale la pena contarlo entero antes de la teoría, porque
la lección es más útil que la regla.

---

## Lo que pasó

Tres videos terminados. Cadena de voz completa aplicada (bloque 7, nueve módulos). Mezcla correcta.
Último paso: normalizar a −14 LUFS, el objetivo para redes sociales.

Se corrió esto:

```bash
ffmpeg -i mezcla.wav -af "loudnorm=I=-14:TP=-1:LRA=11" salida.wav
```

Sin errores. Sin advertencias. Archivo generado. Se entregó.

Después, al medir el archivo entregado:

```
Integrated loudness: -16.7 LUFS
```

**Tres decibelios y medio por debajo del objetivo.** En los tres videos. Y nadie se dio cuenta hasta
medir, porque el archivo sonaba perfectamente bien — solo que sonaba bajito al lado de todo lo demás en
el feed.

Tres decibelios en un feed de Instagram no son un detalle técnico: son la diferencia entre que tu video
suene igual de fuerte que el anterior o que la gente tenga que subirle el volumen. Y nadie le sube el
volumen a un anuncio: pasa el dedo.

---

## Por qué falló: `loudnorm` en una pasada es aproximado

`loudnorm` tiene dos modos y la diferencia no está documentada de forma obvia:

**Modo dinámico (una sola pasada, el que se usó).** ffmpeg procesa el archivo mientras lo lee. En el
segundo 3 no sabe qué va a pasar en el segundo 25. Entonces trabaja como un compresor con lookahead:
estima, ajusta sobre la marcha, y mete un limitador para no pasarse del `TP`. El resultado es un archivo
**cercano** al objetivo, con un margen de error que fácilmente llega a 2–4 dB, sobre todo cuando el
material tiene mucha variación (voz + música + efectos = mucha variación).

**Modo lineal (dos pasadas).** La primera pasada solo **mide** el archivo completo. La segunda aplica
**una única ganancia constante** calculada con esa medición. Como es una ganancia fija, el resultado cae
exactamente en el objetivo, y la dinámica original queda intacta.

La regla que hay que grabarse:

> `loudnorm` en una pasada te deja cerca. `loudnorm` en dos pasadas te deja donde dijiste.
> Para entregar, siempre dos pasadas.

---

## Las dos pasadas, paso a paso

### Pasada 1 — medir

```bash
ffmpeg -i mezcla.wav \
  -af "loudnorm=I=-14:TP=-1:LRA=11:print_format=json" \
  -f null - 2>&1 | tail -20
```

Al final imprime un bloque JSON como este:

```json
{
    "input_i" : "-19.42",
    "input_tp" : "-3.15",
    "input_lra" : "8.70",
    "input_thresh" : "-29.83",
    "output_i" : "-14.02",
    "output_tp" : "-1.40",
    "output_lra" : "8.30",
    "output_thresh" : "-24.43",
    "normalization_type" : "dynamic",
    "target_offset" : "0.02"
}
```

**Cómo se lee esto, campo por campo:**

| Campo | Qué significa |
|---|---|
| `input_i` | la sonoridad integrada real de tu archivo, en LUFS. Aquí: −19,42 |
| `input_tp` | el pico verdadero, en dBTP. Aquí: −3,15 (hay margen de sobra) |
| `input_lra` | el rango de sonoridad: cuánto varía entre lo bajito y lo fuerte |
| `input_thresh` | el umbral que usó el algoritmo para ignorar los silencios |
| `output_*` | lo que **cree** que va a salir. Con una sola pasada, esto es una promesa, no un hecho |
| `target_offset` | corrección fina que la segunda pasada debe aplicar |
| `normalization_type` | dice `dynamic` porque todavía no le diste las mediciones |

Los cuatro que importan para la segunda pasada son los `input_*`. En el código de ffmpeg se llaman
`input_i`, `input_tp`, `input_lra`, `input_thresh`; en la sintaxis del filtro se pasan como
`measured_I`, `measured_TP`, `measured_LRA`, `measured_thresh`. Es el mismo dato con dos nombres, y esa
confusión de nombres es la causa de la mitad de los errores.

### Pasada 2 — aplicar

```bash
ffmpeg -i mezcla.wav \
  -af "loudnorm=I=-14:TP=-1:LRA=11:\
measured_I=-19.42:\
measured_TP=-3.15:\
measured_LRA=8.70:\
measured_thresh=-29.83:\
offset=0.02:\
linear=true:print_format=summary" \
  -ar 48000 -c:a pcm_s24le salida_-14LUFS.wav
```

Tres detalles que no se pueden saltar:

- **`linear=true`.** Sin esto, aunque le pases las mediciones, sigue en modo dinámico. Es la palabra que
  activa la ganancia constante.
- **`-ar 48000`.** `loudnorm` internamente trabaja a 192 kHz y, si no le dices nada, **te entrega el
  archivo a 192 kHz**. Se te va el espacio en disco y algunos reproductores se atragantan. Siempre fija
  la frecuencia de salida.
- **`offset`.** Es el `target_offset` de la pasada 1. Es la corrección final que clava el número.

### Pasada 3 — verificar (sí, hay una tercera)

La lección del error no es "usa dos pasadas". Es **"mide el archivo que entregaste"**. Si en el caso real
alguien hubiera corrido este comando sobre el entregable, el problema se habría detectado en 10 segundos.

```bash
ffmpeg -i salida_-14LUFS.wav -af ebur128=peak=true -f null - 2>&1 | tail -12
```

```
Summary:

  Integrated loudness:
    I:         -14.0 LUFS
    Threshold: -24.4 LUFS

  Loudness range:
    LRA:         8.3 LU

  True peak:
    Peak:       -1.4 dBFS
```

`-14.0` y `-1.4`. Eso es lo que se pidió. **Si el número que sale aquí no es el que pediste, el archivo
no está listo, sin importar cuántos comandos corriste bien.**

---

## El script que hace las tres pasadas solo

Escríbelo una vez y no vuelves a cometer el error.

```bash
#!/usr/bin/env bash
# normalizar.sh — loudnorm en dos pasadas + verificación
# uso: ./normalizar.sh entrada.wav salida.wav [LUFS] [dBTP]
set -euo pipefail

IN="$1"; OUT="$2"; I="${3:--14}"; TP="${4:--1}"; LRA=11

echo ">> Pasada 1: midiendo $IN"
JSON=$(ffmpeg -hide_banner -i "$IN" \
  -af "loudnorm=I=$I:TP=$TP:LRA=$LRA:print_format=json" \
  -f null - 2>&1 | sed -n '/^{/,/^}/p')

get() { echo "$JSON" | grep "\"$1\"" | sed 's/.*: *"\([^"]*\)".*/\1/'; }
MI=$(get input_i);  MTP=$(get input_tp)
MLRA=$(get input_lra); MTH=$(get input_thresh)
OFF=$(get target_offset)

echo "   medido: I=$MI  TP=$MTP  LRA=$MLRA  thresh=$MTH  offset=$OFF"

echo ">> Pasada 2: aplicando"
ffmpeg -hide_banner -y -i "$IN" \
  -af "loudnorm=I=$I:TP=$TP:LRA=$LRA:measured_I=$MI:measured_TP=$MTP:\
measured_LRA=$MLRA:measured_thresh=$MTH:offset=$OFF:linear=true" \
  -ar 48000 -c:a pcm_s24le "$OUT" 2>&1 | tail -3

echo ">> Pasada 3: verificando el archivo entregable"
ffmpeg -hide_banner -i "$OUT" -af ebur128=peak=true -f null - 2>&1 \
  | grep -A2 -E "Integrated loudness|True peak"
```

Uso:

```bash
./normalizar.sh 03_MEZCLA/mezcla.wav 03_MEZCLA/entregable.wav -14 -1
```

---

## Cuándo `linear=true` no puede cumplir

Hay un caso donde `linear=true` **no** te da el número exacto, y ffmpeg te lo avisa en la salida:

```
[Parsed_loudnorm_0] The normalization type is dynamic instead of linear
```

Pasa cuando aplicar la ganancia constante necesaria haría que el pico verdadero se pase del `TP` que
pediste. Ejemplo: tu mezcla está a −22 LUFS pero tiene un pico a −0,5 dBTP. Para llegar a −14 LUFS hay
que subir 8 dB, y eso pondría el pico en +7,5 dBTP. Imposible. Entonces `loudnorm` se cambia solo a modo
dinámico y comprime.

**La solución no es aceptar el modo dinámico. Es arreglar la mezcla.** Si hay un pico aislado 20 dB por
encima del resto (casi siempre un efecto, una risa o una "p" explosiva), bájalo en la mezcla y vuelve a
normalizar. Un limitador suave antes de normalizar también sirve:

```bash
# domar los picos aislados antes de normalizar
ffmpeg -i mezcla.wav -af "alimiter=limit=-3dB:attack=5:release=50:level=disabled" mezcla_domada.wav
```

`level=disabled` es clave: sin eso `alimiter` te sube todo automáticamente y ya no controlas nada.

---

## LUFS por plataforma, a agosto de 2026

Con una advertencia honesta: **hay dos categorías de plataforma y confundirlas causa la mayoría de los
malentendidos.**

### Las que publican su objetivo (música y broadcast)

| Plataforma | Objetivo | Pico verdadero |
|---|---|---|
| Spotify | −14 LUFS | −1,0 dBTP |
| YouTube | −14 LUFS | −1,0 dBTP |
| Amazon Music / Tidal | −14 LUFS | −1,0 dBTP |
| Apple Music (Sound Check) | −16 LUFS | −1,0 dBTP |
| Deezer | −15 LUFS | −1,0 dBTP |
| Broadcast Europa (EBU R128) | −23 LUFS | −1,0 dBTP |
| Broadcast EE.UU. (ATSC A/85) | −24 LKFS | −2,0 dBTP |

### Las que NO publican nada (donde vive tu video)

**TikTok, Instagram, Facebook, X y Twitch no publican un objetivo oficial de LUFS.** Cualquier tabla que
te dé un número exacto para ellas está adivinando. Lo que sí se sabe:

- Todas normalizan la reproducción, y las pruebas independientes las ubican **alrededor de −14 a −15
  LUFS**.
- Meta confirmó que usa xHE-AAC con gestión de sonoridad integrada que **se adapta al contexto de
  reproducción**: no suena igual en audífonos que en el parlante del celular en un bus.

La conclusión práctica, que es lo que importa:

> **Para video social: entrega a −14 LUFS con pico verdadero en −1,0 dBTP.**

No porque sea un estándar publicado, sino porque es el punto donde ninguna plataforma te sube (lo cual
mete ruido) ni te baja (lo cual aplasta la dinámica), y quedas parejo con lo que hay alrededor en el
feed. Si te sales por debajo, suenas débil. Si te pasas por encima, la plataforma te baja y de paso te
comprime.

Y verifica estos números antes de confiar en ellos dentro de un año. Esto cambia.

---

## Sobre el pico verdadero: por qué −1 y no 0

El **pico de muestra** es el valor máximo de las muestras del archivo. El **pico verdadero (dBTP)** es
el máximo de la onda analógica reconstruida entre las muestras — y puede ser más alto que cualquier
muestra individual.

Cuando la plataforma reconvierte tu audio a AAC (todas lo hacen), los picos intersample se materializan
y el decodificador satura. Por eso −1,0 dBTP y no 0.

Si vas a entregar en un formato con pérdida muy comprimido (128 kbps), −1,5 dBTP es más seguro.

```bash
# ver los dos números, pico de muestra y pico verdadero
ffmpeg -i entregable.wav -af "astats=metadata=1,ebur128=peak=true" -f null - 2>&1 \
  | grep -E "Peak level dB|Peak:"
```

---

## Y el video, no solo el WAV

Todo lo anterior mide y normaliza el audio. El entregable es un `.mp4`. Dos maneras:

```bash
# opción A (la buena): montar el audio ya normalizado sobre el video, sin recodificar video
ffmpeg -i video_sin_audio.mp4 -i entregable_-14LUFS.wav \
  -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -ar 48000 final.mp4

# opción B: normalizar directo sobre el mp4 (las mediciones se sacan del mp4)
# ...pero mide SIEMPRE el mp4 resultante, no el wav
```

Y el paso que cierra el círculo:

```bash
# medir el MP4 ENTREGABLE, no el wav intermedio
ffmpeg -i final.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -12
```

La codificación a AAC cambia ligeramente el pico verdadero. Normalmente sube 0,1–0,3 dBTP. Con techo en
−1,0 estás cubierto; con techo en −0,2 no.

---

## Errores comunes

1. **Usar `loudnorm` en una sola pasada para entregar.** Es el error de este módulo. Te deja 2–4 dB
   lejos del objetivo, sin avisarte.
2. **Pasar las mediciones pero olvidar `linear=true`.** Sigue en modo dinámico. Las mediciones no sirven
   de nada.
3. **Confundir los nombres.** La salida dice `input_i`; el filtro espera `measured_I`. No es lo mismo el
   campo `output_i`, que es una predicción.
4. **No verificar el archivo entregado.** El error de los tres videos se habría visto en 10 segundos con
   `ebur128`. Medir el entregable no es opcional.
5. **Olvidar `-ar 48000` en la segunda pasada.** Te sale un WAV a 192 kHz, enorme, que algunos
   reproductores rechazan.
6. **Ignorar la advertencia "normalization type is dynamic instead of linear".** Es ffmpeg diciéndote
   que no pudo cumplir. Arregla los picos de la mezcla y vuelve.
7. **Normalizar cada stem por separado.** Cuatro stems a −14 LUFS suman una mezcla saturada. Se
   normaliza una sola vez, al final.
8. **Normalizar antes de terminar la mezcla.** Cualquier cambio posterior invalida la medición.
9. **Dejar el pico verdadero en 0 dBTP.** La conversión a AAC de la plataforma va a distorsionar.
10. **Creer que TikTok o Instagram publican un objetivo de LUFS.** No lo hacen. −14 es la mejor apuesta,
    no un estándar.
11. **Medir el WAV y entregar el MP4 sin volver a medir.** La codificación cambia el pico verdadero.
12. **Aplicar `loudnorm` dos veces seguidas.** La segunda pasada mide un archivo ya procesado y el
    resultado es peor, no mejor.
13. **Usar `alimiter` sin `level=disabled`.** Te sube el nivel por su cuenta y pierdes el control del
    resultado.

---

## Checklist

- [ ] La normalización se hizo en **dos pasadas**, nunca en una.
- [ ] La pasada 1 se corrió con **`print_format=json`** y se leyeron los cuatro `input_*`.
- [ ] La pasada 2 lleva `measured_I`, `measured_TP`, `measured_LRA`, `measured_thresh`, `offset` **y
      `linear=true`**.
- [ ] La pasada 2 lleva **`-ar 48000`**.
- [ ] No apareció la advertencia **"normalization type is dynamic instead of linear"**; si apareció, se
      arreglaron los picos de la mezcla.
- [ ] Se **midió el archivo entregable** con `ebur128=peak=true` y el número coincide con el objetivo
      (±0,2 LUFS).
- [ ] El **pico verdadero** quedó en **−1,0 dBTP o menos**.
- [ ] Se midió el **MP4 final**, no solo el WAV intermedio.
- [ ] La normalización se aplicó **una sola vez**, sobre la mezcla completa, al final.
- [ ] **Ningún stem** quedó normalizado por separado.
- [ ] El objetivo elegido corresponde a la plataforma real (**−14 LUFS** para video social).
- [ ] Existe un **script** que hace las tres pasadas, para no volver a depender de la memoria.
