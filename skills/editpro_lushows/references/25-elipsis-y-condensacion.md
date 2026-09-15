# 25 — Elipsis y condensación

**Qué resuelve:** grabaste 4 minutos y el video tiene que durar 40 segundos. O grabaste 40 segundos pero
hay 12 de muletillas, respiraciones y "eeeh". Este módulo es cómo se le quita tiempo a un video sin que
se note, y por qué el jump cut de YouTube — que en cine sería un error — es hoy el recurso más honesto
que existe.

---

## 1. Los dos conceptos

> **Elipsis:** saltarse tiempo. La persona sale de la casa y en el plano siguiente ya está en el
> restaurante. Nadie extraña el trayecto. Es tan viejo como el cine y el espectador lo entiende solo.
>
> **Condensación:** dejar lo mismo pero más corto. La persona dice la misma idea, pero le quitaste los
> "este…", las repeticiones y las pausas de pensar.

La elipsis se salta **acontecimientos**. La condensación se salta **aire**. Las dos van juntas y las dos
son, en la práctica, en qué consiste editar.

---

## 2. Qué se quita, en orden de prioridad

Cuando abres un bloque de material hablado, esto es lo que sale, en este orden:

| # | Qué | Cuánto pesa típicamente |
|---|---|---|
| 1 | Silencio antes de la primera palabra y después de la última | 1–4 s por toma |
| 2 | Muletillas: "eeeh", "este", "o sea", "digamos", "listo" | 8–15% del total |
| 3 | Pausas de pensar (más de 0,6 s en medio de una idea) | 10–20% |
| 4 | Frases repetidas (arrancó, se equivocó, volvió a arrancar) | 5–15% |
| 5 | Aclaraciones que no aportan ("como les decía hace un momento…") | 5–10% |
| 6 | Respiraciones muy audibles | 2–5% |
| 7 | La idea entera que no hace falta | lo que sea |

**Una toma cruda de alguien hablando sin guion pierde entre 30% y 45% de su duración solo con los
puntos 1 a 6, sin sacrificar una sola idea.** Ese es el margen que tienes antes de tener que empezar a
recortar contenido.

---

## 3. El método: transcripción con tiempos primero

No edites de oído. Se edita sobre el texto.

### Paso 1 — Transcribe con timecodes

Necesitas una transcripción con tiempo de inicio y fin **por palabra o por frase corta**. Cualquier
herramienta de transcripción moderna lo da. El formato que quieres:

```
[00.00 - 00.42] Bueno
[00.42 - 01.10] eeeh
[01.10 - 02.35] entonces lo que pasa con los costos
[02.35 - 03.20] o sea
[03.20 - 05.80] es que la gente no sabe cuánto le cuesta un plato
```

### Paso 2 — Marca lo que se va

```
[00.00 - 00.42] Bueno                                        ← FUERA
[00.42 - 01.10] eeeh                                         ← FUERA
[01.10 - 02.35] entonces lo que pasa con los costos          ← QUEDA
[02.35 - 03.20] o sea                                        ← FUERA
[03.20 - 05.80] es que la gente no sabe cuánto le cuesta     ← QUEDA
```

### Paso 3 — Construye la lista de tramos que quedan

```
1.10 → 2.35
3.20 → 5.80
```

De 5,8 s pasaste a 3,85 s. Un 34% menos, y no se perdió nada.

### Paso 4 — Valida TODOS los tramos antes de cortar

Este paso no se salta. Antes de generar un solo archivo, comprueba que:

- Ningún tramo empieza o termina **a mitad de palabra**.
- Ningún tramo excede la duración del clip fuente.
- Los tramos están en orden y no se solapan.

Cortar de a uno e ir descubriendo errores es la forma más lenta de editar que existe. Ver módulo `16`.

---

## 4. Los comandos

### Cortar los tramos y unirlos

```bash
#!/usr/bin/env bash
set -euo pipefail
FUENTE="toma.mp4"

# Tramos que quedan: inicio fin
TRAMOS=(
  "1.10 2.35"
  "3.20 5.80"
  "7.45 11.90"
)

rm -f lista.txt
i=0
for T in "${TRAMOS[@]}"; do
  set -- $T
  i=$((i+1))
  ffmpeg -hide_banner -y -ss "$1" -to "$2" -i "$FUENTE" \
    -vf "scale=1080:1920:flags=lanczos,fps=30,setsar=1" \
    -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p \
    -c:a aac -b:a 192k -ar 48000 \
    "t$(printf %02d $i).mp4"
  printf "file 't%02d.mp4'\n" $i >> lista.txt
done

ffmpeg -hide_banner -y -f concat -safe 0 -i lista.txt -c copy condensado.mp4
```

> ⚠️ En Windows, genera `lista.txt` sin BOM. `Add-Content -Encoding utf8` rompe el `concat` de ffmpeg
> con un error que no explica nada.

### Detectar los silencios automáticamente (primera pasada)

Antes de transcribir, `silencedetect` te dice dónde están los huecos:

```bash
ffmpeg -hide_banner -i toma.mp4 -af "silencedetect=noise=-35dB:d=0.5" -f null - 2>&1 | grep silence
```

Salida:

```
[silencedetect] silence_start: 12.416
[silencedetect] silence_end: 13.208 | silence_duration: 0.792
```

Ajusta los dos parámetros según tu grabación:
- `noise=-35dB` — el umbral de "esto es silencio". Si la grabación tiene ruido de fondo, sube a `-30dB`.
  Si es muy limpia, baja a `-45dB`.
- `d=0.5` — duración mínima. Menos de 0,4 s suele ser una respiración normal que **no** hay que quitar.

### Quitar los silencios de golpe (con mucho cuidado)

ffmpeg puede eliminar silencios automáticamente del audio:

```bash
ffmpeg -hide_banner -y -i toma.mp4 \
  -af "silenceremove=stop_periods=-1:stop_duration=0.45:stop_threshold=-38dB" \
  -c:v copy audio_apretado.mp4
```

**Advertencia grande:** esto solo funciona bien para audio suelto (un podcast, una locución). Si el video
tiene imagen sincronizada, `silenceremove` te desincroniza todo porque acorta el audio y no la imagen.
Para video, usa el método de tramos de arriba.

Donde sí es oro: preparar una locución antes de montarle imagen encima (módulo `23`, variante de audio
externo).

---

## 5. El jump cut de YouTube y por qué funciona

> **Jump cut:** cortar dentro del mismo plano quitando un pedazo. La persona "salta" de una posición a
> otra porque el trozo del medio ya no está.

En el cine narrativo esto es un error de continuidad. En video para redes es **el estándar**, y hay una
razón concreta:

**El espectador de 2026 lee el jump cut como respeto por su tiempo.** Ve el salto, entiende que le
quitaron la paja, y lo agradece. La alternativa — dejar el "eeeh" para que el plano quede "limpio" — le
dice "no me importó tu tiempo".

Es un cambio de convención real. Un video de 2010 con jump cuts se veía descuidado. Un video de 2026 sin
jump cuts se ve lento.

### Los cuatro grados de disimulo

De crudo a invisible:

| Grado | Técnica | Se ve | Costo |
|---|---|---|---|
| 0 | Jump cut a pelo | Salto visible | cero |
| 1 | Jump cut **cayendo en una respiración** | Salto suave | cero, solo elegir bien el punto |
| 2 | Jump cut **+ punch-in de 15%** | Se lee como cambio de cámara | cero (módulo `22`) |
| 3 | Jump cut **tapado con cutaway** | Invisible | necesitas b-roll |

**El grado 2 es el que quieres el 80% de las veces.** El punch-in convierte un salto accidental en una
decisión de montaje. Es la misma edición leída de dos formas opuestas.

```bash
# Trozo A: normal
ffmpeg -hide_banner -y -ss 1.10 -to 2.35 -i toma.mp4 \
  -vf "scale=1080:1920:flags=lanczos,fps=30,setsar=1" \
  -c:v libx264 -crf 18 -c:a aac tA.mp4

# Trozo B: mismo plano, 15% más cerrado → el salto desaparece
ffmpeg -hide_banner -y -ss 3.20 -to 5.80 -i toma.mp4 \
  -vf "scale=1242:2208:flags=lanczos,crop=1080:1920,fps=30,setsar=1" \
  -c:v libx264 -crf 18 -c:a aac tB.mp4
```

### Dónde cae el jump cut

Tres reglas de ubicación:

1. **En la respiración**, no a mitad de palabra. La respiración es un punto natural de quiebre y el oído
   la espera.
2. **Al final de la frase completa**, no cortando la última sílaba.
3. **Nunca justo antes del remate.** El remate de una idea se dice completo en el mismo trozo.

---

## 6. Elipsis: saltarse acontecimientos

La condensación quita aire. La elipsis quita **hechos**, y ahí las reglas son otras.

### La regla del "no me hace falta"

Si el espectador puede reconstruirlo solo, se salta. Ejemplos:

| Se puede saltar | Porque |
|---|---|
| El trayecto entre dos lugares | Se entiende que se movió |
| Abrir un empaque completo | Basta ver el inicio y el producto ya afuera |
| Una preparación de 20 minutos | 3 planos: ingredientes, proceso, resultado |
| Escribir un formulario | Un plano de las manos y otro del "enviar" |
| Un saludo protocolario | Nadie lo extraña |

### Cómo se marca una elipsis para que se entienda

El espectador tiene que registrar que pasó tiempo. Cuatro formas, de menos a más explícita:

1. **Cambio de plano fuerte** (de un primer plano a un plano general): la señal más simple.
2. **Cambio de luz o de lugar**: el cerebro entiende solo.
3. **Un plano de transición**: el reloj, el sol, la calle. El clásico.
4. **Texto en pantalla**: "3 horas después". La más explícita; úsala solo si sin ella hay confusión real.

El error es no marcarla: si cortas de la persona en la cocina a la persona en la cocina con otra ropa,
el espectador no lee elipsis, lee error.

### La elipsis de proceso (la que más vas a usar)

Para cualquier video de "cómo se hace":

```
Plano 1: el problema / el punto de partida     (2 s)
Plano 2: el proceso, comprimido                (3 s, acelerado o 3 insertos)
Plano 3: el resultado                          (2,5 s)
```

Veinte minutos de trabajo en 7,5 segundos y nadie siente que le faltó algo. El acelerado:

```bash
# Comprimir 60 s de proceso en 3 s (20x) sin audio
ffmpeg -hide_banner -y -ss 40 -t 60 -i proceso.mp4 \
  -an -vf "setpts=PTS/20,scale=1080:1920:flags=lanczos,fps=30,setsar=1" \
  -c:v libx264 -crf 18 -preset slow acelerado.mp4
```

`setpts=PTS/20` acelera 20 veces. Ojo: si el material es de 30 fps y aceleras 20x, se pierden fotogramas
y el movimiento queda saltón — para acelerados fuertes conviene grabar en 60 fps o usar el filtro
`framerate` para interpolar. Para acelerados de 2x a 4x no hay problema.

---

## 7. Cuánto se puede condensar sin que se note

Límites de la práctica:

| Reducción | Resultado |
|---|---|
| 0–20% | Solo se quitó basura. Nadie nota nada. |
| 20–40% | **El rango bueno.** Se siente ágil, sigue sonando natural. |
| 40–60% | Se nota el ritmo apretado. Funciona si hay punch-ins y cutaways que lo justifiquen. |
| 60–75% | Se siente comprimido. Solo funciona con música fuerte y montaje muy trabajado. |
| Más de 75% | Ya no es condensación: es reescribir. Mejor volver a grabar con guion. |

**Si necesitas quitar más del 60%, el problema no es de edición: es que el material se grabó sin guion.**
Dilo. Reeditar cinco veces sale más caro que volver a grabar 40 segundos bien.

---

## 8. El detector de "se sintió el corte"

Después de condensar, tres verificaciones concretas:

### a) Transcribe el resultado y léelo

Si al leer la transcripción del video ya editado suena raro, entrecortado o le falta una palabra de
enlace, ahí está el problema. Este método caza el 90% de los cortes malos y no requiere oír nada.

### b) Busca cortes de menos de 0,04 s de aire

Un corte donde la frase siguiente empieza a los 0,02 s se oye atropellado. Los humanos necesitan un
mínimo de aire entre ideas.

```bash
ffmpeg -hide_banner -i condensado.mp4 -af "silencedetect=noise=-40dB:d=0.05" -f null - 2>&1 | grep silence_duration
```

Si no aparece **ningún** silencio en todo el video, lo apretaste demasiado. Un video hablado sano tiene
pausas de 0,15–0,35 s entre frases.

### c) Escucha solo el audio

Sin imagen. Si el audio suelto suena a robot o a montaje, la imagen no lo va a salvar.

---

## Errores comunes

1. **Editar de oído en vez de sobre la transcripción.** Es más lento, más impreciso, y siempre se te
   escapa una palabra mocha.
2. **Apretar tanto que no queda una sola pausa.** Un video sin ningún silencio es agotador. Deja
   0,15–0,35 s entre ideas.
3. **Cortar a mitad de palabra.** El error que más grita "amateur" y el más fácil de evitar: se verifica
   contra la transcripción, no de oído.
4. **Jump cuts a pelo sin punch-in.** Un 15% de acercamiento convierte un descuido en una decisión.
5. **Usar `silenceremove` en video con imagen.** Acorta el audio y no la imagen: te desincroniza todo.
6. **Quitar las respiraciones todas.** Un poquito de respiración es lo que hace que suene humano.
   Quítalas cuando son largas o audibles de más, no todas.
7. **Elipsis sin marcar.** Cortas de la cocina a la cocina con otra ropa y el espectador lee error, no
   salto de tiempo. Marca el paso del tiempo.
8. **Quitar la frase de enlace.** "Y por eso…" parece relleno pero es lo que hace que la idea siguiente
   se entienda. Al quitarla el video queda ágil y confuso.
9. **Umbral de `silencedetect` mal calibrado.** Con `-35dB` en una grabación ruidosa no detecta nada;
   con `-45dB` en una limpia detecta hasta las respiraciones. Ajusta y verifica.
10. **Condensar 70% y entregar.** Si tuviste que quitar tres cuartas partes, el material estaba mal
    grabado. Dilo en vez de tapar el hueco con montaje.

---

## Checklist

- [ ] Trabajé sobre una **transcripción con timecodes**, no de oído.
- [ ] **Validé todos los tramos** (no parten palabras, no exceden el clip, no se solapan) **antes** de
      cortar el primero.
- [ ] Quité silencios de entrada/salida, muletillas, repeticiones y pausas de pensar.
- [ ] La reducción total está entre **20% y 60%**; si pasó de ahí, lo dije en vez de taparlo.
- [ ] Cada **jump cut** cae en una respiración o al final de una frase, nunca a mitad de palabra.
- [ ] Los jump cuts visibles están **justificados con punch-in** o tapados con cutaway.
- [ ] Ningún corte le quita el aire a un remate o a un dato.
- [ ] Quedan **pausas de 0,15–0,35 s** entre ideas (verificado con `silencedetect`).
- [ ] Cada **elipsis está marcada** con un cambio de plano, de luz, de lugar o con un plano de transición.
- [ ] **Transcribí el resultado final** y se lee natural, sin palabras mochas ni saltos raros.
- [ ] **Escuché el audio solo**, sin imagen, y se sostiene.
