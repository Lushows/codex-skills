# 296 — El ambiente como pegamento

El ambiente (o *room tone*, o *sonido de sala*) es el sonido que hace un lugar cuando no pasa nada:
el zumbido bajito de la nevera, el aire acondicionado, el murmullo lejano de la calle, la resonancia de
las paredes.

Es el elemento que menos se nota de una mezcla y el que más falta hace. Nadie va a decirte "qué buen
ambiente". Pero sin él, todo el mundo va a sentir que el video está mal armado, y ninguno va a saber
por qué.

---

## El problema que resuelve: el salto de piso de ruido

Aquí es donde los números del caso real explican todo.

Una voz cruda medida daba: **piso de ruido −25,7 dB**. Después de la cadena de tratamiento (`70`–`73`):
**piso de ruido −46,5 dB**.

Ese salto de 21 dB es la prueba de que el tratamiento funcionó. Y también es el origen del problema.

Piensa en un stem de voz consolidado con tres tomas (`292`). Entre toma y toma hay silencio digital
absoluto — no −46,5 dB, sino nada, −∞. El oído entonces recibe esta secuencia:

```
[voz hablando, piso a -46,5 dB]
[silencio absoluto, -∞]              ← el hueco entre tomas
[voz hablando, piso a -46,5 dB]
```

Ese salto a la nada y de vuelta se oye. Se percibe como un "clic" de textura, un hueco, algo que se apaga
y se prende. La sensación que produce es exactamente la que la gente describe como "se nota que está
editado" o "suena cortado".

**Y el caso peor**: si mezclas un clip tratado (piso −46,5) con un clip que no alcanzaste a tratar (piso
−25,7), el corte entre los dos es un salto de 21 dB de ruido de fondo. Eso no se oye como "un clip está
más limpio". Se oye como si alguien hubiera prendido un ventilador.

**El oído no detecta el ruido. Detecta el cambio de ruido.** Un piso de ruido constante desaparece de tu
conciencia en tres segundos. Un piso de ruido que salta te molesta cada vez.

El ambiente resuelve las dos cosas de un golpe: pones una capa continua de ruido de sala debajo de todo
y, como nunca se interrumpe, el oído deja de notar los saltos que hay arriba.

---

## Por qué grabar ambiente puro es obligatorio

En rodaje profesional hay una regla que no se negocia: **antes de levantar el equipo, se graban 60
segundos de silencio en el lugar.** Todos callados, nadie se mueve, la cámara y el micrófono grabando.

Sale un archivo que suena "a nada". Ese archivo es el más valioso de la jornada.

Lo que te permite:

- **Tapar los huecos entre tomas**, con el ruido correcto de ese lugar exacto.
- **Empatar planos grabados con horas de diferencia.** La toma de la mañana y la de la tarde tienen
  ambientes distintos; un lecho común los unifica.
- **Rellenar el hueco cuando cortas una palabra.** Si quitas un "eeeh", queda un agujero; se rellena con
  ambiente y no se nota.
- **Alimentar la reducción de ruido.** `afftdn` y `arnndn` funcionan mejor si sabes exactamente cómo suena
  el ruido que quieres quitar.
- **Poner un lecho debajo de una voz en off** para que no flote sobre la imagen (`294`).

Cuesta un minuto grabarlo y no se puede fabricar después. Es el mejor negocio del rodaje. Si eres el
editor y no lo tienes, pídelo desde ahora en el brief de rodaje (bloque 17: `170`–`179`).

---

## Cuando no te lo grabaron: sacarlo del propio material

Casi siempre pasa esto. La solución: minar el bruto buscando tramos donde nadie hable.

**Paso 1: encontrar los silencios.**

```bash
# lista los tramos de silencio de más de 0,8 s por debajo de -32 dB
ffmpeg -i bruto_audio.wav -af silencedetect=noise=-32dB:d=0.8 -f null - 2>&1 \
  | grep -E "silence_start|silence_end"
```

```
[silencedetect] silence_start: 14.216
[silencedetect] silence_end: 16.902 | silence_duration: 2.686
[silencedetect] silence_start: 41.05
[silencedetect] silence_end: 45.83 | silence_duration: 4.78
```

Ahí tienes: 2,7 segundos limpios en el 14,2 y 4,8 segundos en el 41. El segundo sirve.

**Paso 2: extraerlo, sin recomprimir.**

```bash
ffmpeg -ss 41.3 -t 4.2 -i bruto_audio.wav -c:a pcm_s24le ambiente_semilla.wav
```

Deja margen: empieza 0,25 s después del `silence_start` y termina 0,3 s antes del `silence_end`, para no
llevarte la cola de la última palabra ni el arranque de la siguiente.

**Paso 3: verificar que de verdad está limpio.**

```bash
ffmpeg -i ambiente_semilla.wav -af astats=metadata=1 -f null - 2>&1 \
  | grep -E "RMS level dB|Peak level dB"
```

Si el pico está mucho más alto que el RMS (más de 15 dB de diferencia), hay un evento ahí adentro: un
crujido de silla, alguien tragando, una puerta. Búscate otro tramo.

---

## Convertir 4 segundos en 30: el loop sin costura

Cuatro segundos de ambiente tienen que cubrir un video de 30. Un loop crudo produce un "pum" cada 4
segundos, porque el punto de empalme no coincide.

La técnica es un **loop con cruce**: se pega el archivo consigo mismo con un fundido cruzado largo, y
como el ambiente es ruido sin estructura rítmica, el cruce es literalmente inaudible.

```bash
# 1) hacer un bloque de 8 s cruzando el semilla consigo mismo (cruce de 1,5 s)
ffmpeg -i ambiente_semilla.wav -i ambiente_semilla.wav \
  -filter_complex "[0:a][1:a] acrossfade=d=1.5:c1=tri:c2=tri [a]" \
  -map "[a]" ambiente_8s.wav

# 2) repetirlo hasta cubrir el video, y cortar a la duración exacta
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 video.mp4)
ffmpeg -stream_loop -1 -i ambiente_8s.wav -t "$DUR" -c:a pcm_s24le 04_AMB.wav
```

`-stream_loop -1` repite infinitamente y `-t` corta. El bloque de 8 segundos ya tiene el cruce interno,
así que las repeticiones empalman en un punto que ya fue suavizado.

Alternativa en un solo comando, con `aloop`:

```bash
# aloop trabaja en muestras: 8 s a 48 kHz = 384000 muestras
ffmpeg -i ambiente_8s.wav -af "aloop=loop=-1:size=384000,atrim=0:28" -c:a pcm_s24le 04_AMB.wav
```

**El truco de la reversa**, para cuando el semilla es muy corto y aun así se nota la repetición: pega el
tramo seguido de sí mismo al revés. Como el ruido no tiene dirección, el resultado no se percibe como
repetición y el empalme es perfecto por construcción.

```bash
ffmpeg -i ambiente_semilla.wav -filter_complex "
  [0:a] asplit=2 [a][b];
  [b] areverse [br];
  [a][br] concat=n=2:v=0:a=1 [out]
" -map "[out]" ambiente_espejo.wav
```

---

## A qué nivel va el ambiente

| Situación | Nivel relativo a la voz | Comentario |
|---|---|---|
| Video de negocio, voz protagonista | **−36 a −42 dB** | apenas presente; es pegamento, no escena |
| Documental / testimonio en locación | **−28 a −34 dB** | el lugar es parte de la historia |
| Momento sin voz ni música | **−22 a −28 dB** | puede subir y sostener el plano solo |
| Voz en off sobre b-roll | **−34 a −38 dB** | evita que la voz flote (`294`) |

Y la regla de oro: **si lo puedes identificar como una capa aparte, está muy alto.** Baja 4 dB. La
prueba real es al revés: quítalo y escucha. Si al quitarlo el video suena peor y no sabes por qué, está
en el nivel correcto.

El tratamiento estándar del ambiente antes de meterlo:

```bash
ffmpeg -i 04_AMB.wav -af "
  highpass=f=150,
  lowpass=f=6500,
  stereotools=mlev=0.6:slev=1.4,
  volume=-38dB
" ambiente_tratado.wav
```

- `highpass=150`: el ambiente no necesita graves y ahí solo hay barro (`295`).
- `lowpass=6500`: sin agudos suena lejos, que es donde debe estar (`294`).
- `stereotools` ancho: envuelve en vez de venir de un punto.

---

## El caso de los planos grabados en momentos distintos

Este es el uso que le da nombre al módulo. Un video de un restaurante: entrevista al dueño grabada a las
10 a. m. con el local vacío, planos de comida a las 2 p. m. con el local lleno, plano de cierre a las
7 p. m. con música sonando de fondo.

Cortas entre los tres y el audio salta de "silencio", a "murmullo", a "música ajena". El video se
desarma.

La solución tiene dos partes:

**1. Silenciar el audio original de los planos que no aportan.** Si el plano de comida no tiene un sonido
que valga la pena (ver `77`), su audio se va. No se baja: se quita.

**2. Un solo lecho de ambiente para toda la pieza**, elegido a propósito. Casi siempre el más neutro y
más rico de los tres: en el ejemplo, el murmullo del mediodía a nivel bajo.

```bash
# armar la pieza con un ÚNICO ambiente continuo debajo de todos los planos
ffmpeg \
  -i 01_VOZ.wav \
  -i 04_AMB.wav \
  -i sonido_util_del_plato.wav \
  -filter_complex "
    [0:a] volume=0dB [voz];
    [1:a] highpass=f=150, lowpass=f=6500, volume=-36dB [amb];
    [2:a] adelay=12400|12400, highpass=f=120, volume=-14dB [chorro];
    [voz][amb][chorro] amix=inputs=3:duration=longest:normalize=0 [mix]
  " -map "[mix]" -ar 48000 -c:a pcm_s24le mezcla.wav
```

El ambiente corre de principio a fin, sin cortarse nunca, por debajo de todos los cortes de imagen.
**Eso es el pegamento.** Los planos siguen viniendo de tres momentos distintos, pero el oído recibe una
sola continuidad y decide que todo pasó en el mismo lugar y al mismo tiempo.

---

## Tapar un hueco puntual

Cuando cortas una palabra o una muletilla queda un agujero de silencio absoluto de 200–400 ms. Si tienes
lecho de ambiente continuo, el hueco ya está tapado. Si no, se parcha así:

```bash
# insertar 0,35 s de ambiente en el hueco que quedó en el segundo 7,8
ffmpeg -i 01_VOZ.wav -i ambiente_semilla.wav \
  -filter_complex "
    [1:a] atrim=0:0.35, adelay=7800|7800, volume=-30dB,
          afade=t=in:st=7.8:d=0.06, afade=t=out:st=8.09:d=0.06 [parche];
    [0:a][parche] amix=inputs=2:duration=first:normalize=0 [out]
  " -map "[out]" voz_parchada.wav

# comprobar que ya no hay silencio absoluto
ffmpeg -i voz_parchada.wav -af silencedetect=noise=-60dB:d=0.15 -f null - 2>&1 | grep silence
```

Los fundidos de 60 ms en los bordes del parche evitan que el propio parche haga clic.

---

## Fabricar ambiente cuando no hay nada aprovechable

Último recurso, y funciona mejor de lo que parece: ruido rosa filtrado a la forma del espacio.

```bash
# lecho de "cuarto interior" sintético, 30 segundos
ffmpeg -f lavfi -i "anoisesrc=d=30:c=pink:a=0.06" -af "
  highpass=f=140,
  lowpass=f=2800,
  equalizer=f=220:t=q:w=1.4:g=3,
  tremolo=f=0.13:d=0.15,
  stereotools=mlev=0.5:slev=1.5,
  volume=-40dB
" -c:a pcm_s24le ambiente_sintetico.wav
```

El `tremolo` muy lento (0,13 Hz) es lo que evita que suene a ruido de máquina: le da una respiración
irregular, como la tiene un cuarto real.

Aviso honesto, y esto conecta con `297`: **el ambiente sintético es el único sonido sintético que
funciona de verdad**, porque el ambiente es, por definición, ruido sin estructura. Un whoosh sintético
suena a juguete porque un whoosh real tiene textura y capas. Un ruido de cuarto sintético pasa
desapercibido porque un ruido de cuarto real también es ruido filtrado. Es la excepción que confirma la
regla.

Aun así: prefiere siempre el ambiente real del lugar. Trae información que no puedes inventar.

---

## Errores comunes

1. **No poner ambiente porque "no se oye".** Que no se note es exactamente el punto. Quítalo y compara.
2. **No pedir room tone en el rodaje.** Un minuto de grabación que no se puede fabricar después.
3. **Ambiente demasiado alto.** Por encima de −30 dB relativos deja de ser pegamento y se convierte en
   ruido que compite.
4. **Loop crudo sin cruce.** Un "pum" cada N segundos. `acrossfade` o el truco del espejo.
5. **Usar un tramo con un evento adentro.** Una silla que cruje, repetida 8 veces, se vuelve un ritmo
   involuntario. Verifica con `astats` (pico vs RMS).
6. **Ambiente distinto por plano.** Si cada plano trae su propio ambiente, no pegaste nada: sumaste el
   problema. Un solo lecho para toda la pieza.
7. **Ambiente con graves.** Debajo de 150 Hz solo hay barro que te come margen de mezcla.
8. **Ambiente con todos los agudos.** Suena adelante, compite con la voz. `lowpass` a 6.500 Hz.
9. **Ambiente que se corta cuando entra la música.** Debe correr de principio a fin, sin interrupciones.
10. **Dejar el audio original de todos los planos "por si acaso".** Los que no aportan se silencian; su
    ambiente propio es lo que causa los saltos.
11. **Mezclar clips tratados y sin tratar.** El salto de piso de −25,7 a −46,5 se oye como un ventilador
    prendiéndose. Trata todo o ninguno.
12. **Olvidar que el stem de ambiente debe cubrir la duración exacta.** Si termina un segundo antes, el
    final del video se cae al vacío (`292`).

---

## Checklist

- [ ] Existe un **stem de ambiente** (`04_AMB.wav`) y cubre el **video completo, de 0 a la duración
      exacta**.
- [ ] El ambiente **nunca se interrumpe**, ni siquiera cuando entra la música.
- [ ] La semilla se sacó de un tramo **verificado como limpio** (pico y RMS cercanos).
- [ ] El loop se hizo con **cruce** (`acrossfade`) o con el **truco del espejo**; no se oye la repetición.
- [ ] Hay **un solo ambiente** para toda la pieza, no uno por plano.
- [ ] El ambiente lleva **`highpass=150`** y **`lowpass≈6500`**.
- [ ] El nivel está entre **−34 y −42 dB** relativos a la voz (más alto solo si el lugar es parte de la
      historia).
- [ ] Se hizo la prueba de **quitarlo**: sin él, el video suena peor.
- [ ] No hay **silencios absolutos** en la mezcla (`silencedetect` con `noise=-60dB` no reporta nada).
- [ ] Los planos cuyo audio no aporta están **silenciados**, no bajados.
- [ ] Si se fabricó ambiente sintético, lleva **modulación lenta** para no sonar a máquina.
- [ ] En el próximo rodaje quedó pedido **1 minuto de room tone** en el brief.
