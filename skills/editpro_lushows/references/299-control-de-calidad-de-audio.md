# 299 — Control de calidad de audio

La lista que se corre sobre el archivo que vas a entregar, antes de entregarlo. No sobre el WAV
intermedio: sobre el `.mp4` final, el que va a subir a la plataforma.

Este módulo existe por la misma razón que `293`: en el caso real se entregaron tres videos a −16,7 LUFS
creyendo que estaban a −14, y el error habría tardado diez segundos en detectarse si alguien hubiera
corrido una sola verificación sobre el entregable.

> **Nada se entrega sin medir. Nada se mide sobre un archivo intermedio.**

---

## Las nueve verificaciones

| # | Qué | Cómo se falla |
|---|---|---|
| 1 | Sonoridad integrada (LUFS) | suena bajito o la plataforma lo aplasta |
| 2 | Pico verdadero (dBTP) | distorsiona al recodificar a AAC |
| 3 | Muestras recortadas | crujidos audibles |
| 4 | Compatibilidad mono | la música desaparece en el celular |
| 5 | Fase / correlación | cancelaciones raras |
| 6 | Silencios accidentales | huecos, arranques mudos |
| 7 | Frecuencia de muestreo y códec | incompatibilidades, archivos gigantes |
| 8 | Prueba de parlante de celular | la voz no se entiende donde se ve |
| 9 | Los primeros 3 segundos | el 60% del público no pasa de ahí |

---

## 1 y 2 — Sonoridad y pico verdadero

```bash
ffmpeg -i final.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -14
```

```
Summary:
  Integrated loudness:
    I:         -14.0 LUFS
    Threshold: -24.6 LUFS
  Loudness range:
    LRA:         7.9 LU
    Threshold: -34.5 LUFS
    LRA low:   -19.3 LUFS
    LRA high:  -11.4 LUFS
  True peak:
    Peak:       -1.3 dBFS
```

**Qué debe salir:**

| Medida | Objetivo (video social) | Tolerancia |
|---|---|---|
| Integrated | −14,0 LUFS | ±0,5 |
| True peak | −1,0 dBTP o menos | nunca por encima |
| LRA | 6–11 LU | fuera de ahí, revisar |

**Cómo se leen los fallos:**

- **I = −16,7** → el error de `293`. Normaliza en dos pasadas.
- **I = −11** → te vas a pasar; la plataforma te baja y te comprime. Renormaliza.
- **Peak = −0,2** → margen insuficiente. La conversión a AAC lo va a empujar por encima de 0.
- **LRA = 3** → aplastado. Comprimiste demasiado; suena cansador y sin vida.
- **LRA = 16** → demasiado variable. Los momentos bajos no se van a oír en un bus. Comprime más (`73`).

---

## 3 — Muestras recortadas

```bash
ffmpeg -i final.mp4 -af astats=metadata=1 -f null - 2>&1 \
  | grep -E "Number of clipped samples|Peak level dB|Flat factor"
```

```
Number of clipped samples: 0
Peak level dB: -1.30
Flat factor: 0.000000
```

**`Number of clipped samples` debe ser 0.** Cualquier número distinto de cero significa que hay muestras
aplastadas contra el techo, y eso son crujidos.

**`Flat factor`** mide cuántas muestras seguidas tienen exactamente el mismo valor: es la firma de la
saturación. Si es mayor que 0, algo se aplanó. En el caso real de la voz cruda con pico en **0,00 dB**,
este número era alto — esa toma estaba saturada desde la grabación.

---

## 4 — Compatibilidad mono

La verificación que más gente se salta y la que más daño evita. **La mayoría de tu público te oye por un
solo parlante de celular**, que suma los dos canales a mono. Si tu mezcla tiene información en los lados
que se cancela al sumar, en el celular esa información desaparece.

Pasa cuando te pasaste con `stereotools` (`294`) o cuando una música tiene efectos de ancho agresivos.

```bash
# 1) hacer la versión mono
ffmpeg -i final.mp4 -af "pan=mono|c0=0.5*c0+0.5*c1" -ar 48000 prueba_mono.wav

# 2) medir estéreo vs mono y comparar
echo "--- ESTÉREO ---"
ffmpeg -i final.mp4 -af ebur128 -f null - 2>&1 | grep "I:" | tail -1
echo "--- MONO ---"
ffmpeg -i prueba_mono.wav -af ebur128 -f null - 2>&1 | grep "I:" | tail -1
```

**Interpretación:** de 0 a 1 dB de diferencia es perfecto; de 1 a 2 dB es aceptable (normal con música
ancha); más de 3 dB es cancelación seria — baja el `slev` de `stereotools` a 1.2 o menos y vuelve a
mezclar. Y escúchala: la prueba real es abrir `prueba_mono.wav` y confirmar que la música sigue ahí y la
voz sigue clara.

---

## 5 — Fase y correlación

La correlación de fase mide cuánto se parecen los dos canales. Va de **+1** (idénticos, perfectamente
compatible con mono) a **−1** (opuestos, se cancelan totalmente en mono).

```bash
ffmpeg -i final.mp4 -af "aphasemeter=video=0:phasing=1:duration=1:tolerance=0.005" \
  -f null - 2>&1 | grep -iE "mono|phase"
```

El filtro reporta los tramos donde detecta contenido mono o contenido fuera de fase. Lo que buscas:
**ningún reporte de "out of phase"**. Que reporte tramos mono no es un problema (una voz centrada es
mono por definición); que reporte fuera de fase sí lo es.

Valor de referencia: correlación por encima de **+0,5** en toda la pieza. La causa más común de una
correlación negativa en video es haber invertido un canal por accidente al convertir formatos, o haber
duplicado una pista con un retardo de pocos milisegundos.

Si sospechas de un retardo entre canales:

```bash
# ver los dos canales por separado; un desfase se ve como ondas corridas
ffmpeg -i final.mp4 -lavfi "showwavespic=s=1600x400:split_channels=1" canales.png
```

---

## 6 — Silencios accidentales

```bash
# cualquier tramo por debajo de -55 dB durante más de 0,4 s
ffmpeg -i final.mp4 -af silencedetect=noise=-55dB:d=0.4 -f null - 2>&1 | grep silence
```

**Lo ideal es que no reporte nada**, porque el lecho de ambiente (`296`) debería cubrir toda la pieza.

Si reporta algo, hay tres causas posibles:

- **Al principio**: el stem de ambiente no arranca en 0. El video abre mudo y se siente roto.
- **En el medio**: hueco entre tomas sin tapar. Parche de ambiente (`296`).
- **Al final**: el ambiente terminó antes que el video. Verifica duraciones (`292`).

Y la verificación complementaria, que a veces salva el día:

```bash
# ¿el audio arranca de verdad en 0,0? (los primeros 300 ms)
ffmpeg -i final.mp4 -t 0.3 -af astats=metadata=1 -f null - 2>&1 | grep "RMS level dB"
```

Si eso da `-inf` o algo por debajo de −70 dB, tu video abre en silencio absoluto. En un feed con
autoplay, ese arranque mudo se lee como "video sin sonido" y la gente pasa.

---

## 7 — Formato del contenedor

```bash
ffprobe -v error -select_streams a:0 \
  -show_entries stream=codec_name,sample_rate,channels,bit_rate,channel_layout \
  -of default=noprint_wrappers=1 final.mp4
```

```
codec_name=aac
sample_rate=48000
channels=2
channel_layout=stereo
bit_rate=192000
```

**Lo que debe salir para video social:**

| Campo | Valor | Por qué |
|---|---|---|
| `codec_name` | `aac` | universal; el `opus` en mp4 da problemas en iOS |
| `sample_rate` | `48000` | estándar de video; 44100 obliga a remuestrear |
| `channels` | `2` | estéreo, aunque la voz sea mono |
| `bit_rate` | `128000`–`256000` | 192k es el punto justo |

**El fallo silencioso más común: `sample_rate=192000`.** Es lo que pasa cuando corres `loudnorm` sin
`-ar 48000` (ver `293`). El archivo funciona, pesa cuatro veces más y algunos reproductores lo rechazan.

---

## 8 — La prueba del parlante de celular

Un parlante de celular no reproduce nada útil por debajo de ~400 Hz ni por encima de ~8 kHz, y suena a
un volumen bajo en un ambiente ruidoso. Simúlalo:

```bash
ffmpeg -i final.mp4 -af "
  highpass=f=400,
  lowpass=f=8000,
  volume=-8dB
" -c:v copy prueba_celular.mp4
```

Escucha eso completo, una vez, sin pausar. Tres cosas se juzgan:

1. **¿Se entiende cada palabra?** Si no, el problema está en 2–4 kHz (`295`), no en el nivel.
2. **¿Sigue habiendo música?** Si la música desapareció, dependía de los graves. Súbele el rango medio.
3. **¿Los efectos siguen ahí?** Un impacto que es puro sub-grave desaparece completo en un celular. Si
   ese impacto era importante, necesita una capa media (`297`).

Y una segunda prueba, más dura: celular **más ruido de calle**, que es como de verdad se ve tu video.

```bash
ffmpeg -i final.mp4 -f lavfi -i "anoisesrc=c=pink:a=0.05" \
  -filter_complex "[0:a]highpass=f=400,lowpass=f=8000,volume=-8dB[v];
                   [1:a]volume=-24dB[n];[v][n]amix=inputs=2:duration=first:normalize=0[o]" \
  -map 0:v -map "[o]" -c:v copy prueba_calle.mp4
```

Si la voz sobrevive ahí, sobrevive en cualquier parte.

---

## 9 — Los primeros 3 segundos

El 60% de tu público no pasa de ahí, así que esos 3 segundos merecen su propia verificación.

```bash
# extraer y medir solo el arranque
ffmpeg -i final.mp4 -t 3 -c copy arranque.mp4
ffmpeg -i arranque.mp4 -af ebur128=peak=true -f null - 2>&1 | grep -E "I:|Peak:"
```

Lo que debe cumplirse:

- **El arranque no está más de 3 LUFS por debajo del promedio de la pieza.** Si el video entero está a
  −14 y los primeros 3 segundos están a −20, tu hook suena débil justo donde se decide todo.
- **No hay silencio absoluto** en los primeros 300 ms.
- **La primera palabra se entiende completa.** Escúchalo. Si la música tapa la primera sílaba, mueve la
  entrada de la música (`298`).

---

## El script de control de calidad completo

Córrelo sobre cada entregable. Diez segundos, y no vuelves a entregar un video a −16,7 LUFS.

```bash
#!/usr/bin/env bash
# qc-audio.sh — control de calidad de audio sobre el entregable
# uso: ./qc-audio.sh final.mp4
set -uo pipefail
F="$1"
echo "═══ CONTROL DE CALIDAD DE AUDIO: $F ═══"

echo; echo "── 1-2. Sonoridad y pico verdadero ──"
ffmpeg -hide_banner -i "$F" -af ebur128=peak=true -f null - 2>&1 \
  | grep -E "^ *(I|LRA|Peak):" | head -4

echo; echo "── 3. Recorte ──"
ffmpeg -hide_banner -i "$F" -af astats=metadata=1 -f null - 2>&1 \
  | grep -E "Number of clipped samples|Flat factor" | head -4

echo; echo "── 4. Compatibilidad mono ──"
EST=$(ffmpeg -hide_banner -i "$F" -af ebur128 -f null - 2>&1 | grep " I:" | tail -1)
ffmpeg -hide_banner -y -i "$F" -af "pan=mono|c0=0.5*c0+0.5*c1" -ar 48000 /tmp/_qc_mono.wav 2>/dev/null
MON=$(ffmpeg -hide_banner -i /tmp/_qc_mono.wav -af ebur128 -f null - 2>&1 | grep " I:" | tail -1)
echo "   estéreo: $EST"
echo "   mono   : $MON   (diferencia máx aceptable: 2 dB)"

echo; echo "── 5. Fase ──"
ffmpeg -hide_banner -i "$F" -af "aphasemeter=video=0:phasing=1:duration=1:tolerance=0.005" \
  -f null - 2>&1 | grep -i "phase" | head -5 || echo "   sin reportes de fase — OK"

echo; echo "── 6. Silencios ──"
ffmpeg -hide_banner -i "$F" -af silencedetect=noise=-55dB:d=0.4 -f null - 2>&1 \
  | grep silence | head -6 || echo "   sin silencios — OK"

echo; echo "── 7. Formato ──"
ffprobe -v error -select_streams a:0 \
  -show_entries stream=codec_name,sample_rate,channels,bit_rate \
  -of default=noprint_wrappers=1 "$F"

echo; echo "── 9. Primeros 3 segundos ──"
ffmpeg -hide_banner -i "$F" -t 3 -af ebur128 -f null - 2>&1 | grep " I:" | tail -1

echo; echo "── 8. Prueba de celular generada ──"
ffmpeg -hide_banner -y -i "$F" -af "highpass=f=400,lowpass=f=8000,volume=-8dB" \
  -c:v copy prueba_celular.mp4 2>/dev/null
echo "   escucha prueba_celular.mp4 completo antes de entregar."
rm -f /tmp/_qc_mono.wav
```

---

## La verificación que ningún script reemplaza

Después de todos los números: **escucha el video completo, una vez, sin pausar, sin tocar nada.** Con el
oído descansado (no en la misma hora en que mezclaste), a volumen normal, mirando la imagen. Esa pasada
detecta lo que ninguna medición detecta: un efecto que llegó tarde, una frase que quedó rara, la música
entrando en un momento incómodo. Y si puedes, hazla en tres sitios: audífonos, parlante de celular y
parlante del computador.

---

## Errores comunes

1. **Medir el WAV intermedio y no el MP4 entregable.** La codificación a AAC cambia el pico verdadero.
2. **Confiar en el `output_i` de la pasada 1 de `loudnorm`.** Es una predicción, no una medición.
   Verifica el archivo real (`293`).
3. **No probar en mono.** La mayoría de tu público escucha por un solo parlante.
4. **Dejar el pico en −0,2 dBTP.** Sin margen para la recodificación de la plataforma.
5. **Ignorar `Number of clipped samples`.** Cualquier valor distinto de 0 son crujidos.
6. **Ignorar el `Flat factor`.** Es la firma de la saturación de origen; delata material que ya venía
   dañado.
7. **No revisar los primeros 300 ms.** Un arranque mudo en autoplay se lee como "video sin sonido".
8. **Sample rate a 192 kHz.** Es lo que pasa al normalizar sin `-ar 48000`. Archivo gigante e
   incompatible.
9. **LRA muy bajo (menos de 5).** Sobre-comprimido; suena cansador y sin vida.
10. **Aprobar solo con audífonos.** Los audífonos perdonan todo lo que el celular castiga.
11. **Hacer el QC en la misma sesión de la mezcla.** El oído está adaptado y ya no oye lo que hay.
12. **Correr el QC y no leer la salida.** Pasó en el caso real: el comando corrió, nadie miró el número.
13. **Entregar sin ver el video completo una vez.** Los números no detectan un efecto llegando tarde.

---

## Checklist

- [ ] Todas las mediciones se hicieron sobre el **MP4 entregable**, no sobre archivos intermedios.
- [ ] **Integrated loudness** dentro de ±0,5 del objetivo (−14 LUFS para video social).
- [ ] **True peak** en **−1,0 dBTP o menos**.
- [ ] **LRA** entre 6 y 11 LU.
- [ ] **`Number of clipped samples` = 0** y `Flat factor` = 0.
- [ ] La versión **mono** no pierde más de 2 dB ni pierde elementos.
- [ ] `aphasemeter` **no reporta contenido fuera de fase**.
- [ ] `silencedetect` **no reporta silencios**; los primeros 300 ms tienen señal.
- [ ] Códec **AAC**, **48.000 Hz**, **estéreo**, **≥128 kbps**.
- [ ] Se escuchó la **prueba de parlante de celular** completa: se entiende cada palabra.
- [ ] Los **primeros 3 segundos** no están más de 3 LUFS por debajo del promedio.
- [ ] Se escuchó el **video completo, una vez, sin pausar**, con el oído descansado.
- [ ] Se escuchó en **al menos dos sistemas** distintos.
