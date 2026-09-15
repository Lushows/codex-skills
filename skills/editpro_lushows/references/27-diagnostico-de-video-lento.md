# 27 — Diagnóstico de video lento

**Qué resuelve:** el cliente dice "se siente lento" o "está aburrido" y no sabe explicar más. Este módulo
convierte esa queja en un diagnóstico concreto: doce causas posibles, cómo medir cuál es, y el arreglo
específico de cada una. Es el módulo que evita re-montar un video entero cuando el problema real eran
tres segundos.

---

## 0. Antes de tocar nada: el triaje

Casi siempre el problema es uno de estos tres, y en este orden:

1. **El arranque.** Los primeros 3 segundos no enganchan. (Causas 1 y 2)
2. **Un bache en el medio.** El video promedio está bien pero hay una zona muerta. (Causa 4)
3. **Falta variedad visual.** Nunca cambia nada. (Causas 3 y 5)

Corre estas tres medidas antes de opinar:

```bash
V=video.mp4

# a) Pulso promedio
ffmpeg -hide_banner -i "$V" -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2> esc.txt
grep -o "pts_time:[0-9.]*" esc.txt | cut -d: -f2 > t.txt
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
N=$(wc -l < t.txt)
awk -v d="$DUR" -v n="$N" 'BEGIN{printf "pulso = %.2f s por cambio (objetivo 1,5-2,0)\n", d/(n+1)}'

# b) Huecos sin cambio visual
awk 'NR>1{d=$1-p; if(d>2.5) printf "HUECO %.1f s entre %.1f y %.1f\n", d, p, $1} {p=$1}' t.txt

# c) Cambios en los primeros 3 segundos
awk '$1<=3' t.txt | wc -l
```

Con esos tres números ya sabes por dónde entrar.

---

## Las 12 causas

### Causa 1 — El gancho llega tarde

**Síntoma:** los primeros 3 segundos son un saludo, una presentación o una intro con logo. La caída de
retención está en el segundo 1–3.

**Cómo medir:**

```bash
ffmpeg -hide_banner -i video.mp4 -vf "fps=4,scale=200:-1,tile=12x1" -frames:v 1 primeros3s.png
```

Doce fotogramas de los primeros 3 segundos. Si en esa tira no pasa nada que dé curiosidad, ese es tu
problema y ninguna otra corrección lo va a compensar.

**Arreglo:** quitar todo lo que va antes del gancho. Literalmente. Si el gancho está en el segundo 6,
el video empieza en el segundo 6.

```bash
ffmpeg -hide_banner -y -ss 6.0 -i video.mp4 -c:v libx264 -crf 18 -c:a aac video_sin_intro.mp4
```

**Prioridad: 🔴 máxima.** Ver módulo `30`.

---

### Causa 2 — El primer plano dura demasiado

**Síntoma:** el gancho está bien pero el primer plano dura 5 segundos sin cambiar nada.

**Cómo medir:** el primer valor de `t.txt` es cuándo ocurre el primer cambio. Si es mayor a 1,5 s, hay
problema.

**Arreglo:** meter un punch-in a los 1,2–1,5 s. No cambia el contenido, solo el encuadre.

**Prioridad: 🔴 alta.**

---

### Causa 3 — Pulso promedio bajo

**Síntoma:** el promedio da más de 2,5 s por cambio. El video entero se arrastra.

**Arreglo, en orden de costo:**

1. Punch-ins cada vez que cambia de idea (módulo `22`) — gratis.
2. Insertos de b-roll o fotos de producto.
3. Entradas de texto con golpe (módulo `42`).

Cuántos cambios te faltan:

```bash
awk -v d="$DUR" -v n="$N" 'BEGIN{printf "tienes %d cambios; para pulso 1.8 necesitas %d; faltan %d\n", n, d/1.8, (d/1.8)-n}'
```

**Prioridad: 🟠 media-alta.**

---

### Causa 4 — Un bache específico

**Síntoma:** el promedio está bien pero hay un tramo de 5+ segundos sin cambios. Suele ser donde la
persona explica algo largo.

**Este es el diagnóstico más rentable de todos**, porque el arreglo es puntual: no tocas el resto del
video.

**Arreglo:** en el tramo detectado, mete 2–3 cambios visuales. Con la técnica del módulo `23` (voz
continua, imagen picada) lo haces sin tocar el audio.

**Prioridad: 🔴 alta, y es la más barata de arreglar.**

---

### Causa 5 — Un solo encuadre en todo el video

**Síntoma:** hay cortes, pero todos vuelven al mismo plano. Hay pulso y no hay variedad.

**Cómo medir:** la grilla te lo dice de un vistazo.

```bash
ffmpeg -hide_banner -i video.mp4 -vf "fps=1,scale=200:-1,tile=10x6" -frames:v 1 grid.png
```

Si los 60 cuadritos son básicamente la misma imagen, ahí está.

**Arreglo:** generar tres encuadres del material (normal, +15%, +25%) y reencuadre lateral, y alternar.
Módulo `22`.

**Prioridad: 🟠 media.**

---

### Causa 6 — No hay texto en pantalla

**Síntoma:** un talking head puro sin nada escrito.

**Por qué pesa tanto:** un video con texto dinámico y cortes frecuentes retiene alrededor de **35% más**
que un talking head estático. Y la mayoría de la gente ve sin sonido: sin texto, no hay contenido.

**Arreglo:** subtítulos o palabras clave en pantalla (módulos `40`, `41`).

```bash
ffmpeg -hide_banner -y -i video.mp4 -vf "subtitles=subs.ass" -c:v libx264 -crf 18 -c:a copy con_texto.mp4
```

**Prioridad: 🔴 alta si no hay nada de texto.**

---

### Causa 7 — Silencios largos

**Síntoma:** hay tramos donde no se dice nada y no pasa nada.

**Cómo medir:**

```bash
ffmpeg -hide_banner -i video.mp4 -af "silencedetect=noise=-35dB:d=0.8" -f null - 2>&1 | grep silence_duration
```

**Arreglo:** dos caminos según el caso.
- Si el silencio no aporta: **quítalo** (módulo `25`).
- Si es una pausa deliberada: **rellénala con música o con sonido real** (módulos `74`, `77`). Un
  silencio con música se lee como pausa dramática; un silencio total se lee como error.

**Prioridad: 🟠 media.**

---

### Causa 8 — Demasiadas muletillas y aire

**Síntoma:** el contenido está bien pero la persona tarda el doble de lo necesario en decirlo.

**Cómo medir:** cuenta palabras de la transcripción y divide por la duración.

```
palabras por minuto = palabras / (duración_en_segundos / 60)
```

| PPM | Lectura |
|---|---|
| < 110 | Muy lento. Sobra aire. |
| **130–160** | **Rango bueno para video de redes** |
| 160–190 | Rápido pero funciona con subtítulos |
| > 200 | Atropellado |

**Arreglo:** condensar (módulo `25`). Una toma sin guion pierde 30–45% sin sacrificar ideas.

**Prioridad: 🟠 media-alta.**

---

### Causa 9 — La música no ayuda o no está

**Síntoma:** no hay música, o hay una pista lenta y plana.

**Cómo medir:** el BPM. Si está por debajo de 90, la música misma está frenando la percepción de ritmo.

**Arreglo:** pista de 110–130 BPM con energía creciente (módulo `24`). La música es lo más barato que
puede subir la sensación de ritmo sin tocar un solo corte.

**Prioridad: 🟡 media-baja, pero es la de mejor relación esfuerzo/resultado.**

---

### Causa 10 — Falta jerarquía: todo tiene la misma importancia

**Síntoma:** el video corta cada 1,8 s todo el rato, no hay ni un momento que destaque, y aun así se
siente monótono. Este es el caso contrario al esperado: **hay pulso pero no hay dinámica**.

**Por qué pasa:** cuando todo es igual de intenso, nada es intenso. Es como un texto donde todo está en
negrita.

**Arreglo:** construir la curva del módulo `20`:
- Arranque más rápido (0,8–1,2 s).
- Un respiro deliberado (plano de 3–4 s) en el punto de mayor interés.
- Plano más cerrado reservado para la frase más importante.
- Remate final acelerado.

**Prioridad: 🟠 media. Es el diagnóstico que más se pasa por alto.**

---

### Causa 11 — El video es más largo que su contenido

**Síntoma:** ninguna medida técnica sale mal y aun así aburre.

**Cómo medir:** la prueba honesta. Escribe en una frase qué dice el video. Si cabe en una frase y el
video dura 90 segundos, sobra video.

```
Ideas distintas en el video ÷ duración en segundos
```

Un video de redes necesita **una idea nueva cada 4–6 segundos**. No un corte: una **idea**. Si tienes
3 ideas en 60 segundos, el problema no es el ritmo, es el guion.

**Arreglo:** cortar duración, no meter más efectos. Ver módulo `28`.

**Prioridad: 🔴 alta, y es la que nadie quiere oír.**

---

### Causa 12 — Problemas técnicos que se leen como lentitud

**Síntoma:** algo se siente mal pero no es el montaje.

Revisa:

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate,width,height,bit_rate \
  -of default=noprint_wrappers=1 video.mp4
```

| Problema | Cómo se percibe | Arreglo |
|---|---|---|
| fps mezclados (24 y 30) | Movimiento saltón | Forzar `fps=30` en todos los pedazos |
| Bitrate muy bajo | Imagen sucia = se lee como barato | Subir a CRF 18–20 |
| Imagen oscura / plana | Se siente pesada | Corrección de color (módulo `61`) |
| Audio bajo o sordo | Se siente muerto | Cadena de voz (módulo `70`) |
| Ritmo lento por resolución mal escalada | Blando | `flags=lanczos` |

**El audio flojo es la causa más subestimada de "se siente aburrido".** Una voz con presencia y cuerpo
hace que el mismo montaje se sienta más vivo. Antes de meter diez cortes más, arregla la voz.

**Prioridad: 🟠 media, pero se resuelve rápido.**

---

## Tabla de diagnóstico rápido

| Medida | Valor malo | Causa probable | Módulo |
|---|---|---|---|
| Cambios en los primeros 3 s | 0–1 | 1, 2 | `30`, `22` |
| Pulso promedio | > 2,5 s | 3 | `20`, `22` |
| Hueco más largo | > 4 s | 4 | `23` |
| Cuadritos idénticos en la grilla | > 40% | 5 | `22` |
| Texto en pantalla | ninguno | 6 | `40` |
| Silencios > 0,8 s | varios | 7 | `25`, `74` |
| Palabras por minuto | < 110 | 8 | `25` |
| BPM de la música | < 90 o no hay | 9 | `24` |
| Todo al mismo ritmo | pulso perfectamente parejo | 10 | `20`, `39` |
| Ideas por minuto | < 8 | 11 | `28`, `35` |
| fps / bitrate / LUFS | inconsistentes | 12 | `91`, `70` |

---

## El orden de ataque

Si tienes tiempo limitado, arregla en este orden. Está ordenado por retorno, no por dificultad:

1. **El arranque** (causas 1 y 2). Si la gente se va en el segundo 2, nada más importa.
2. **El bache** (causa 4). Puntual, barato, alto impacto.
3. **El texto** (causa 6). +35% de retención por sí solo.
4. **El audio** (causa 12). Rápido y cambia la percepción entera.
5. **La duración** (causa 11). Doloroso pero es la verdad.
6. **El pulso general** (causas 3 y 5). Es el que más trabajo cuesta.
7. **La música** (causa 9). Barato, mejora la sensación.
8. **La jerarquía** (causa 10). Refinamiento.

---

## Lo que NO es el problema (casi nunca)

Cuando alguien dice "se siente lento", la respuesta equivocada más común es meter efectos. Estas cosas
**no** arreglan un video lento:

- **Transiciones de zoom con blur.** No suben el pulso: lo bajan, porque la transición dura y ocupa
  tiempo donde no pasa nada.
- **Acelerar todo el video 1,2x.** Se nota en la voz y no arregla la falta de variedad.
- **Más efectos de sonido.** Un whoosh en cada corte cansa en 15 segundos.
- **Filtros de color llamativos.** Cambian el look, no el ritmo.
- **Subtítulos animados de karaoke.** Ayudan, pero no reemplazan cambios visuales reales.

Si después de meter todo eso el video sigue sintiéndose lento, es porque el problema era la causa 11 y
nadie lo quiso decir.

---

## Errores comunes

1. **Diagnosticar de oído sin medir.** "Le faltan cortes" cuando el problema era el arranque. Corre las
   tres medidas del triaje antes de opinar.
2. **Re-montar el video entero cuando el problema era un bache de 6 segundos.** Mide primero dónde está.
3. **Meter transiciones para arreglar lentitud.** Las transiciones ocupan tiempo: empeoran el problema.
4. **Ignorar el audio.** Una voz sin presencia hace que todo se sienta muerto y no se nota como problema
   de audio: se nota como aburrimiento.
5. **No querer aceptar la causa 11.** Si el video no tiene contenido para 90 segundos, la solución es
   que dure 30. Ningún montaje arregla la falta de ideas.
6. **Optimizar el promedio ignorando los huecos.** El promedio miente; los huecos son donde se pierde
   la gente.
7. **Meter pulso sin variedad.** Diez punch-ins al mismo encuadre no arreglan nada. Es la causa 5
   disfrazada de solución.
8. **Arreglar el final antes que el arranque.** El 70% de la audiencia nunca llega al final. El orden
   de ataque no es negociable.
9. **Acelerar el video globalmente.** Se oye en la voz y se nota. Condensa quitando aire, no acelerando.
10. **Entregar sin volver a medir.** Después de arreglar, vuelve a correr el triaje. Si el pulso no
    cambió, no arreglaste nada.

---

## Checklist

- [ ] Corrí las **tres medidas del triaje** (pulso, huecos, cambios en los primeros 3 s) antes de opinar.
- [ ] Revisé las **12 causas** una por una y anoté cuáles aplican, con su medida.
- [ ] Ataqué en el **orden de retorno**: arranque → bache → texto → audio → duración → pulso.
- [ ] El **gancho está en el segundo 0**, no en el 6.
- [ ] El **primer cambio visual** ocurre antes de 1,5 s.
- [ ] **Ningún hueco** supera 2,5 s sin cambio visual.
- [ ] Hay **texto en pantalla**.
- [ ] La **voz tiene presencia** (pasó por la cadena de audio) antes de culpar al montaje.
- [ ] Las **palabras por minuto** están entre 130 y 160.
- [ ] Hay **jerarquía**: un respiro deliberado y un plano reservado para la frase clave.
- [ ] Verifiqué que el video **tiene contenido** para la duración que tiene (una idea cada 4–6 s).
- [ ] **No metí transiciones ni efectos** para tapar un problema de ritmo.
- [ ] **Volví a medir después de arreglar** y los números cambiaron.
