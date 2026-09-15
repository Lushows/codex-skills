# 24 — Ritmo y música

**Qué resuelve:** por qué un video con la misma cantidad de cortes se siente "profesional" o "amateur"
según dónde caigan respecto a la música. Y, sobre todo, cuándo cortar al beat es exactamente lo que
arruina un video.

---

## 1. El vocabulario mínimo

> **Beat (pulso musical):** el golpe regular de la música, lo que marcas con el pie. En la mayoría de la
> música moderna hay 4 beats por compás.
>
> **BPM (beats por minuto):** cuántos golpes hay en un minuto. 120 BPM = 2 golpes por segundo.
>
> **Compás:** grupo de 4 beats. El beat 1 es el fuerte.
>
> **Frase musical:** grupo de 4 u 8 compases. Es donde la música "respira" y cambia. Es el punto de
> corte más potente que existe.
>
> **Downbeat:** el beat 1 del compás. El golpe más fuerte.
>
> **Drop:** el momento donde entra todo el arreglo de golpe. En música electrónica y en trap es el punto
> de máxima energía.

Traducción a segundos, que es lo que le vas a dar a ffmpeg:

```
segundos por beat = 60 / BPM

120 BPM → 0,500 s por beat → 2,000 s por compás
128 BPM → 0,469 s por beat → 1,875 s por compás
100 BPM → 0,600 s por beat → 2,400 s por compás
 90 BPM → 0,667 s por beat → 2,667 s por compás
140 BPM → 0,429 s por beat → 1,714 s por compás
```

**Fíjate en algo:** un compás a 120–128 BPM dura entre 1,875 y 2,0 segundos. Eso cae **exactamente**
dentro del objetivo de pulso del módulo `20` (1,5–2,0 s por cambio visual). No es casualidad: la música
de contenido y el ritmo de edición moderno convergen en la misma ventana porque los dos responden a la
misma atención humana.

**Consecuencia práctica: si eliges una pista entre 120 y 130 BPM y cortas un cambio visual por compás,
tu pulso queda correcto solo.**

---

## 2. Detectar el tempo de una pista

### Opción A — a mano, y es más confiable de lo que crees

1. Reproduce la pista.
2. Cuenta 4 golpes en voz alta y arranca un cronómetro en el golpe 1.
3. Detenlo en el golpe 1 del compás siguiente. Eso son 4 beats.
4. `BPM = 240 / segundos_medidos`.

Si midiste 1,88 s → `240 / 1,88 = 127,7` → la pista está a **128 BPM**. Los BPM de música producida
casi siempre son redondos o muy cerca: 90, 100, 110, 120, 124, 128, 140, 150, 174.

### Opción B — con ffmpeg, detectando los picos de energía

ffmpeg no tiene un detector de BPM, pero sí puedes ver dónde están los golpes fuertes:

```bash
# Aislar los graves (donde vive el bombo) y listar los picos
ffmpeg -hide_banner -i musica.mp3 \
  -af "lowpass=f=150,astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=picos.txt" \
  -f null -
```

Eso te deja en `picos.txt` el nivel de energía de los graves a lo largo del tiempo. Los máximos son los
bombos. No es un detector de BPM elegante, pero sirve para confirmar tu conteo manual.

### Opción C — ver la onda

A veces mirar es más rápido que medir:

```bash
ffmpeg -hide_banner -i musica.mp3 -filter_complex "showwavespic=s=2400x300:colors=white" -frames:v 1 onda.png
```

En esa imagen los picos regulares son los golpes. Si la imagen mide 2400 px y la pista dura 60 s,
entonces `1 px = 0,025 s`. Con eso ubicas cualquier golpe con una regla.

### Opción D — un espectrograma para encontrar los cambios de sección

Los cambios de sección (donde entra la voz, donde entra el drop) se ven a simple vista:

```bash
ffmpeg -hide_banner -i musica.mp3 -lavfi showspectrumpic=s=2400x600:legend=1 espectro.png
```

Ahí ves las bandas: donde el dibujo cambia de golpe, hay una frase musical nueva. Esos son tus puntos
de corte fuertes.

---

## 3. La rejilla de beats

Una vez que sabes el BPM y dónde cae el primer beat, calculas todos los demás:

```bash
BPM=128
OFFSET=0.312      # segundo exacto donde cae el primer golpe fuerte
SPB=$(awk -v b=$BPM 'BEGIN{printf "%.4f", 60/b}')
for i in $(seq 0 63); do
  awk -v o=$OFFSET -v s=$SPB -v i=$i 'BEGIN{printf "beat %2d = %.3f s\n", i+1, o+i*s}'
done
```

Salida:

```
beat  1 = 0.312 s
beat  2 = 0.781 s
beat  3 = 1.250 s
beat  4 = 1.719 s
beat  5 = 2.187 s   ← downbeat del compás 2
...
```

Los beats 1, 5, 9, 13… son los downbeats. Esos son los puntos donde un corte se siente "correcto".

**El offset importa muchísimo.** Casi ninguna pista arranca el primer golpe en el segundo 0,000: suele
haber una entrada de 0,2 a 1,5 s. Si asumes offset 0 tu rejilla queda corrida y todos los cortes caen
mal por la misma cantidad — que es el error más frustrante de esta técnica porque "casi funciona".

---

## 4. Los cuatro niveles de cortar al beat

No todo se corta igual. De más agresivo a más sutil:

| Nivel | Dónde cortas | Se siente | Cuándo |
|---|---|---|---|
| **1. Cada beat** | 0,5 s a 120 BPM | Videoclip, agresivo, agota rápido | Solo en ráfagas de 2–4 s |
| **2. Cada 2 beats** | 1,0 s | Enérgico | Secuencias de producto, montajes de acción |
| **3. Cada compás** | 2,0 s | **El estándar.** Vivo y respirable | **Por defecto** |
| **4. Cada 2 compases** | 4,0 s | Calmado, cinematográfico | Video institucional, testimonio |

**El nivel 3 (un cambio por compás) es tu opción por defecto** y coincide con el objetivo de pulso.

### La técnica del acento

No cortes todos los cambios en el downbeat. Reserva el downbeat para los cambios **importantes** y pon
los secundarios en el beat 3:

```
Compás 1  |  beat1: CORTE FUERTE (nuevo plano)   beat3: punch-in (cambio suave)
Compás 2  |  beat1: CORTE FUERTE (inserto)       beat3: —
Compás 3  |  beat1: CORTE FUERTE (vuelta)        beat3: entrada de texto
```

Eso te da 5 cambios en 6 segundos (pulso 1,2 s) pero con jerarquía: se siente estructurado, no
atropellado. La diferencia entre "cortado al beat" y "montado con la música".

### Cortar sobre el drop

El drop es el momento de más energía de la pista. Ahí va tu plano más fuerte: el producto revelado, la
cara del cliente, el precio. Y ahí va, si acaso, tu único efecto de transición del video.

Para encontrar el drop, mira el espectrograma: es donde de golpe se llena todo el rango de frecuencias.

---

## 5. Cuándo NO cortar al beat

Esta es la sección más importante del módulo, y la que casi nadie escribe.

### a) Cuando hay voz hablada

**Regla dura:** si hay alguien hablando, **la voz manda sobre la música**. Siempre.

Si el beat cae a mitad de la palabra "restaurante", el corte va donde termina la palabra, no donde está
el beat. Un corte 0,2 s fuera del beat con la palabra completa se siente bien. Un corte perfecto al beat
que parte una palabra se siente roto.

Orden de prioridad, no negociable:

```
1. La palabra completa        ← manda siempre
2. La acción en el plano      ← corte por acción (módulo 21)
3. El beat                    ← lo último
```

La solución real a este conflicto es el módulo `23`: voz continua, imagen picada. Ahí sí puedes poner
los cambios de imagen exactamente en los beats, porque el audio ni se entera.

### b) Cuando la música es de fondo, no protagonista

En un testimonio, un video corporativo o un tutorial, la música está a -25 dB debajo de la voz. Nadie
la está siguiendo. Cortar al beat de una música que casi no se oye no aporta nada y te obliga a cortes
malos.

### c) Cuando el material tiene su propio ritmo

Comida en la plancha, agua cayendo, una máquina trabajando. Ese material tiene ritmo propio. Forzarle
una rejilla de beats encima pelea con lo que ya funciona.

### d) Cuando genera cortes por debajo de 1,2 s sostenidos

Una pista a 174 BPM (drum and bass) da beats de 0,34 s. Cortar cada beat ahí es ruido puro (módulo `20`).
Ahí cortas cada 4 beats: `0,34 × 4 = 1,38 s`.

### e) En el momento emocional

Si hay un momento de peso — alguien se emociona, se revela algo, cae el remate — **déjalo respirar**.
Cortar al beat ahí es meterle prisa a algo que necesita quedarse. La música sigue; la imagen no tiene
que obedecerle.

### f) Cuando el video es más largo que 90 segundos

Cortar al beat durante tres minutos hipnotiza y luego cansa. En formatos largos la música marca las
**secciones**, no los cortes: cambias de bloque cuando cambia la frase musical, y dentro del bloque
cortas por contenido.

---

## 6. Recortar y adaptar la música

### Cortar la pista respetando el compás

Nunca cortes una pista en un segundo arbitrario: córtala en un downbeat.

```bash
# 128 BPM, offset 0.312, quiero desde el compás 5 (beat 17) durante 8 compases
# beat 17 = 0.312 + 16*0.469 = 7.816
# 8 compases = 8 * 1.875 = 15.0 s
ffmpeg -hide_banner -y -ss 7.816 -t 15.0 -i musica.mp3 -c:a pcm_s16le musica_corte.wav
```

### Terminar sin el fundido barato

El fundido de 3 segundos al final es la marca de agua del video amateur. Tres opciones mejores:

**Opción 1 — terminar en un downbeat con un corte seco.** Si el último plano cae en el beat 1 y la
música se corta ahí, se siente terminado.

```bash
ffmpeg -hide_banner -y -ss 7.816 -t 15.0 -i musica.mp3 -af "afade=t=out:st=14.92:d=0.08" -c:a pcm_s16le fin_seco.wav
```

Un fundido de 0,08 s (menos de 3 fotogramas) evita el "clic" del corte digital sin que se perciba como
fundido.

**Opción 2 — dejar caer la cola de reverberación.** Cortas el arreglo pero dejas 0,5 s de la resonancia.

**Opción 3 — que la música termine antes que el video** y los últimos 2 segundos sean solo la voz o un
sonido real. Funciona muy bien en el llamado a la acción: el silencio de la música lo hace destacar.

### Hacer un loop que no se note

Si la pista es más corta que el video:

```bash
# Recortar exactamente 8 compases (15.0 s a 128 BPM) y repetir 3 veces
ffmpeg -hide_banner -y -ss 7.816 -t 15.0 -i musica.mp3 -c:a pcm_s16le bucle.wav
ffmpeg -hide_banner -y -stream_loop 2 -i bucle.wav -c:a pcm_s16le musica_larga.wav
```

La clave es que el trozo dure un número **exacto** de compases. Si dura 15,3 s en vez de 15,0, cada
vuelta suma 0,3 s de descuadre y a la tercera se oye el tropiezo.

---

## 7. La mezcla: música bajo voz

Esto pertenece al módulo `75` (ducking), pero el nivel base hay que saberlo aquí porque afecta la
decisión de ritmo:

| Situación | Nivel de la música |
|---|---|
| Solo música, sin voz | 0 dB (referencia) |
| Música bajo voz hablada | **-18 a -22 dB** respecto de la voz |
| Música en un momento de énfasis sin voz | -6 dB |
| Música en el remate final | sube a -3 dB |

```bash
# Bajar la música 18 dB y mezclarla con la voz
ffmpeg -hide_banner -y -i voz.wav -i musica.wav \
  -filter_complex "[1:a]volume=-18dB[m];[0:a][m]amix=inputs=2:duration=first:normalize=0[a]" \
  -map "[a]" -c:a pcm_s16le mezcla.wav
```

Si la música está tan alta que compite con la voz, no importa lo bien cortado que esté el video: la
gente se va porque no entiende.

---

## 8. Elegir la pista (lo que de verdad decide)

En orden de importancia:

1. **BPM entre 100 y 130.** Te da compases de 1,8–2,4 s, que es tu ventana de pulso. Por fuera de ese
   rango te vas a pelear con la música todo el montaje.
2. **Que la energía suba.** Una pista plana no ayuda; una que crece te regala la curva emocional
   (módulo `39`).
3. **Que tenga secciones claras.** Entrada, cuerpo, drop, salida. Eso te da la estructura del video.
4. **Sin voz.** Una pista cantada compite con tu locución. Si hay voz hablada, la música va instrumental.
   Sin excepción.
5. **Que se pueda licenciar.** Ver módulo `78`. Una pista perfecta que te tumba el video por Content ID
   no es perfecta.

---

## Errores comunes

1. **Asumir que el primer beat cae en el segundo 0,000.** Casi nunca. Si no mides el offset, todos tus
   cortes quedan corridos por la misma cantidad y el video "casi" funciona, que es peor que no intentarlo.
2. **Cortar al beat partiendo palabras.** La voz manda sobre la música, siempre. Si hay conflicto, la
   palabra gana.
3. **Cortar en cada beat de una pista rápida.** A 174 BPM cada beat son 0,34 s. Eso es ruido. Corta cada
   4 beats.
4. **Elegir una pista cantada bajo una locución.** Dos voces compitiendo: no se entiende ninguna.
5. **Fundido de salida de 3 segundos.** Es la firma del video amateur. Termina en downbeat con corte
   seco y 0,08 s de fundido anticlic.
6. **Hacer loop de un trozo que no dura compases exactos.** Cada vuelta acumula el desfase y a la tercera
   se oye el tropiezo.
7. **Poner la música tan alta que tapa la voz.** El error de mezcla más común. Música a -18/-22 dB bajo
   la voz.
8. **Cortar al beat en un momento emocional.** Le metes prisa a lo que necesitaba quedarse quieto.
9. **Elegir la música al final.** La música define el ritmo del montaje: se elige **antes** de cortar,
   no después de armado. Cambiar de pista al final obliga a re-cortar todo.
10. **Cortar al beat un video de 3 minutos.** Hipnotiza los primeros 40 s y luego cansa. En formatos
    largos la música marca secciones, no cortes.

---

## Checklist

- [ ] Medí el **BPM** de la pista (no lo asumí) y anoté el valor.
- [ ] Encontré el **offset del primer downbeat** con precisión de centésimas.
- [ ] Calculé la **rejilla de beats** y la tengo en segundos, lista para pasar a ffmpeg.
- [ ] El BPM elegido da compases dentro de la **ventana 1,5–2,5 s**.
- [ ] Los cortes fuertes caen en **downbeats**; los suaves, en beats intermedios.
- [ ] **Ninguna palabra se parte** por perseguir un beat (la voz mandó).
- [ ] Si hay locución, la música es **instrumental**.
- [ ] El plano más fuerte del video cae en el **drop** o en el punto de mayor energía.
- [ ] La música está mezclada **18–22 dB por debajo de la voz**.
- [ ] Si hay loop, el trozo dura un **número exacto de compases**.
- [ ] El final **no** es un fundido de 3 segundos: es un corte en downbeat con fundido anticlic de 0,08 s.
- [ ] Verifiqué que la pista se puede **licenciar** para el uso previsto.
- [ ] Elegí la música **antes** de montar, no después.
