# 172 — Audio en rodaje

**Qué resuelve:** el error número uno del video amateur. No es la luz, no es el encuadre, no es el
color. Es el **audio**. La gente perdona una imagen regular; no perdona una voz que suena mal. Y a
diferencia de la imagen, el audio malo **casi nunca se arregla en post**.

> **Este módulo es el más importante del bloque 17.** Si solo vas a leer uno antes de grabar, lee este.

---

## 1. Los tres desastres de audio del rodaje real

Un rodaje verdadero en un bar-restaurante, agosto de 2026. Estos tres problemas salieron del mismo día.

### Desastre 1 — La música del local sonando

El equipo de sonido del bar estuvo prendido todo el rodaje. Consecuencias:

**a) Mató la detección automática de silencios.** El editor busca los cortes con un comando que detecta
los silencios entre tomas. Con la música sonando, **el audio nunca bajó de -34 dB**. Nunca hubo
silencio. El comando no devolvió nada y las 16 tomas hubo que revisarlas a oído, una por una. Horas de
trabajo que no debían existir.

```bash
# Esto es lo que el editor corre. Con música de fondo, no devuelve NADA.
ffmpeg -hide_banner -i clip.mp4 -af "silencedetect=noise=-40dB:d=0.6" -f null - 2>&1 | grep silence_
```

**b) Cada corte se oye.** La canción va sonando en su tiempo. Cuando cortas de la toma 2 a la toma 5, la
música salta de un punto a otro de la canción. Se oye como un tropiezo. Cada corte.

**c) Derechos de autor.** Esa música es de alguien. Instagram, TikTok y YouTube la detectan (`78`) y te
pueden silenciar, bloquear o desmonetizar el video. Y no la puedes sacar: está mezclada con la voz.

**d) La voz suena peor.** El micrófono del celular tiene control automático de ganancia: si hay música,
sube y baja el nivel de la voz solo, y la voz queda "bombeando".

> **La solución cuesta cero pesos y quince segundos: apagar el equipo de sonido.** No bajarlo. Apagarlo.

### Desastre 2 — El audio saturado

Todo el material llegó con el audio **pegado a 0 dB**. Eso se llama saturación o clipping.

> **Saturación (clipping):** el sonido entró tan fuerte que la grabación no pudo representarlo. Las
> ondas quedan literalmente **cortadas en plano** arriba y abajo. Lo que se perdió no está en el
> archivo: no hay filtro, no hay IA, no hay nada que lo devuelva.

Se oye como una voz raspada, dura, con un "fritanga" en las consonantes fuertes. En un video de ventas
suena a barato, y esa es exactamente la sensación que no quieres transmitir.

**Cómo se comprueba después:**

```bash
ffmpeg -hide_banner -i clip.mp4 -af "volumedetect" -f null - 2>&1 | grep -E "max_volume|mean_volume"
```

Si `max_volume` da `0.0 dB` o `-0.1 dB`, está saturado. Sano es entre **-6 y -3 dB** de pico.

Cuenta de picos saturados:

```bash
ffmpeg -hide_banner -i clip.mp4 -af "astats=metadata=1" -f null - 2>&1 | grep -i "Flat factor\|Peak count"
```

### Desastre 3 — No hubo ambiente puro

Nadie grabó cinco segundos de silencio del sitio. Eso hizo imposible dos cosas que el editor necesita
todo el tiempo, y de las que hablamos en la sección 5.

---

## 2. Cómo se graba audio decente con lo que ya tienes

Esta es la escalera, de peor a mejor. Súbete lo más alto que puedas hoy.

| Nivel | Método | Costo | Calidad |
|---|---|---|---|
| 0 | Micrófono del celular a 2 metros | $0 | ❌ Inservible |
| 1 | Micrófono del celular a **30–40 cm** | $0 | 🟡 Aceptable |
| 2 | **Manos libres con cable** (los del celular) | $0 | 🟡 Mejor de lo que crees |
| 3 | Micrófono de solapa con cable | ~$40.000 | ✅ Bien |
| 4 | **Micrófono de solapa inalámbrico** (tipo Boya, Hollyland, DJI Mic) | $200–500 mil | ✅ Muy bien |
| 5 | Grabador aparte + sincronización | Más | ✅ Excelente, más trabajo |

**La verdad incómoda del nivel 1:** el micrófono de un celular moderno es sorprendentemente bueno **si
está cerca**. La distancia es el factor que más manda. El sonido de la voz cae con la distancia mucho
más rápido que el ruido del ambiente, así que acercar el micrófono no solo sube la voz: **baja
proporcionalmente todo lo demás**.

> **Regla de la mitad de la distancia:** cada vez que reduces a la mitad la distancia al micrófono, la
> voz sube ~6 dB y el ruido del cuarto se queda igual. De 2 m a 50 cm son 12 dB de mejora gratis.

**El truco del celular partido en dos:** si tienes dos celulares, usa uno para la imagen (a la distancia
del encuadre) y otro **fuera de cuadro a 30 cm de la boca**, grabando solo audio con la grabadora de
voz. Después el editor sincroniza. Es el salto de calidad más grande por $0. Se sincroniza con una
palmada al inicio (`161`).

**El nivel 2 merece defensa:** los audífonos con cable que traen micrófono, colgando a la altura del
pecho, dan un audio limpio y cercano. No se ven bien en cuadro — pero para un plano medio o con la
persona de perfil, o escondiendo el cable bajo la camisa, funcionan. Mejor eso que un audio de sala.

---

## 3. Niveles: la única regla que hay que memorizar

El objetivo del rodaje **no** es que suene fuerte. Es que **quepa**.

```
Picos de voz entre -12 dB y -6 dB
NUNCA tocar 0 dB
```

**Por qué esos números:**

- Por debajo de -20 dB, la voz está tan baja que al subirla en post subes también el ruido.
- Entre -12 y -6 hay margen: si la persona se ríe o alza la voz, todavía cabe.
- En 0 dB se rompe. Y romperse es permanente.

**Es infinitamente mejor grabar bajito que grabar saturado.** Una voz grabada a -25 dB se sube en post y
queda bien. Una voz saturada está muerta. Si dudas, aléjate un paso.

**Cómo se monitorea de verdad:**

| Con qué | Cómo |
|---|---|
| Cámara nativa del celular | ❌ No muestra niveles. Estás a ciegas. |
| **Blackmagic Camera** (gratis, iOS/Android) | ✅ Medidores en pantalla mientras grabas |
| **Open Camera** (gratis, Android) | ✅ Medidor de audio |
| Filmic Pro | ✅ Medidores + control manual de ganancia |
| Micrófono inalámbrico con pantalla | ✅ Medidor en el transmisor |

Si no tienes ninguno de esos, el método de emergencia: **grabar 10 segundos de prueba, ponerse los
audífonos y escucharlos**. Si la voz suena raspada en las palabras fuertes ("¡pruébalo!", "¡el mejor!"),
está saturando. Aléjate 15 cm y repite la prueba.

**Esta prueba de 30 segundos habría salvado el rodaje real completo.**

---

## 4. Apagar el local: la conversación

El dueño del bar no va a querer apagar la música. Es su ambiente, hay clientes, se siente raro. Hay que
saber pedirlo.

**Qué NO decir:** "es que el piso de ruido queda en -34 dB y no puedo hacer silencedetect".

**Qué sí decir:**

> "Necesito 20 minutos con el equipo de sonido apagado. Si la música queda grabada, Instagram me puede
> tumbar el video por derechos de autor, y además cada corte se va a oír como un salto. Son 20 minutos y
> lo volvemos a prender."

Tres argumentos que funcionan, en orden de efectividad:
1. **"Te pueden tumbar el video"** — es cierto y asusta.
2. **"Va a sonar como un video mal hecho"** — nadie quiere eso de su negocio.
3. **"Son 20 minutos"** — acotar el tiempo lo hace aceptable.

**Si de verdad no se puede apagar** (hay clientes, es hora pico):

- Grabar en el sitio más lejano al parlante, con el parlante **detrás del micrófono**, no delante.
- Micrófono lo más cerca posible de la boca (solapa, sin excusa).
- Grabar **más ambiente puro** que nunca: 15 segundos con la música sonando igual que en las tomas, para
  que el editor pueda construir una cama continua que disimule los saltos entre cortes.
- Asumir que la limpieza de ruido va a comerse parte de la voz (`71`).
- Avisarle al editor **antes**, no después.

**Lo mismo aplica a:** nevera, extractor de la cocina, aire acondicionado, licuadora, televisor,
ventilador. Todos se apagan. El extractor de una cocina es el asesino silencioso: no lo oyes en vivo
porque tu cerebro lo filtra, pero el micrófono lo graba entero.

---

## 5. Los 5 segundos de ambiente puro (la joya escondida)

**Qué es:** después de grabar en un sitio, con todo el mundo callado y quieto, se graba **5 segundos de
nada**. Solo el sonido del lugar. Sin voz, sin movimiento.

Se hace por locación. Si grabaste en el pasillo, la barra y la terraza: tres ambientes, 15 segundos en
total en todo el día.

**Para qué sirve — y por qué el editor lo pide de rodillas:**

### a) Es la referencia de ruido para limpiar la voz

Los limpiadores de ruido funcionan mucho mejor cuando les enseñas **cómo suena el ruido solo**. Con una
muestra pura, la limpieza es quirúrgica y no se come las consonantes.

```bash
# Recortar la muestra de ruido de los 5 segundos grabados
ffmpeg -hide_banner -y -i ambiente_terraza.mp4 -ss 0.5 -t 3 -vn -c:a pcm_s16le ruido.wav

# Perfil de ruido y limpieza con sox (si está disponible)
sox ruido.wav -n noiseprof perfil.prof
sox voz.wav voz_limpia.wav noisered perfil.prof 0.21
```

Sin la muestra, hay que adivinar el perfil y el resultado se oye metálico (`71`).

### b) Es la cama que tapa los saltos entre cortes

Cuando cortas de la toma 2 a la toma 5, el ruido de fondo salta. Poniendo el ambiente puro **debajo de
todo el video** a un nivel bajito (-35 a -30 dB), la continuidad de audio se restaura y los cortes
desaparecen al oído (`26`, `76`).

```bash
# Hacer un lecho de ambiente de 60 s en bucle a partir de 5 s
ffmpeg -hide_banner -y -stream_loop -1 -i ruido.wav -t 60 -af "volume=-32dB" cama_ambiente.wav
```

### c) Rellena los huecos de silencio

Un silencio digital absoluto suena **muerto**, como si el video se hubiera dañado. Un silencio con
ambiente suena natural.

**Cómo se pide en el rodaje, para que no se sienta absurdo:** "Necesito que todos se queden quietos y
callados cinco segundos. Estoy grabando el silencio del sitio." Se hace una vez y ya nadie pregunta.

---

## 6. Colocación del micrófono de solapa

Si vas a usar solapa (y deberías), tres cosas:

**Dónde:** en el pecho, a **un palmo de la barbilla**, ligeramente hacia el lado. No en el centro exacto
del pecho: ahí retumba más.

**Cuidado con la ropa:** el micrófono rozando la tela produce un "frú-frú" constante que **no se quita**.
Si la camisa es de material sintético o hay una chaqueta encima, asegura el cable con cinta por dentro
para que no se mueva. Este es el error más común con solapas.

**Cuidado con el pelo largo y las cadenas:** rozan, golpean, y suenan.

**Prueba obligatoria:** que la persona diga la frase completa moviéndose como se va a mover en la toma.
Si al girar la cabeza el nivel cae mucho, el micrófono está mal puesto.

---

## 7. El otro audio: el sonido real del producto

En un bar-restaurante, el sonido del producto vale oro (`77`). El destape de una botella, el líquido
cayendo en la copa, el hielo, la parrilla, el cuchillo cortando. Eso es lo que dispara el antojo, y
suena mejor grabado de verdad que sacado de una librería.

**Cómo se graba:** aparte, en un plano dedicado, **con el celular a 15–20 cm del objeto** y todo lo
demás callado. Diez segundos por sonido.

Lista mínima para un bar:
- Destape de botella
- Líquido cayendo en el vaso
- Hielo en el vaso
- El vaso posándose en la barra
- Cocina: sartén, corte, plancha
- Ambiente de gente (útil de fondo, se graba aparte)

En el rodaje real, el clip largo de la secuencia de producto (61 segundos: botella, destape, servido,
copa llena) traía **su propio audio real** y de ahí salieron todos los efectos del video. Ese clip
resolvió imagen **y** sonido. Ver `174`.

---

## 8. Lo que el editor comprueba al recibir el material

Este es el diagnóstico que se corre sobre todos los clips antes de montar (`11`).

```bash
for f in *.mp4; do
  echo "=== $f"
  ffmpeg -hide_banner -i "$f" -af "volumedetect" -f null - 2>&1 | grep -E "max_volume|mean_volume"
done
```

**Cómo se lee:**

| `max_volume` | Diagnóstico |
|---|---|
| 0.0 dB / -0.1 dB | ❌ **Saturado.** Se pierde calidad de forma permanente. |
| -3 a -6 dB | ✅ Perfecto |
| -12 a -6 dB | ✅ Bien, hay margen |
| -25 dB o menos | 🟡 Bajo. Se sube en post pero también sube el ruido. |

Y el piso de ruido, que es el que dice si hubo música sonando:

```bash
ffmpeg -hide_banner -i clip.mp4 -af "silencedetect=noise=-40dB:d=0.5" -f null - 2>&1 | grep -c silence_start
```

Si devuelve `0` en un clip donde hubo pausas, **había música o ruido constante**. Eso le dice al editor
que se olvide de la detección automática y que hay trabajo manual por delante (`13`).

---

## Errores comunes

1. **Dejar la música del local sonando "bajita".** Bajita sigue siendo un piso de -34 dB: mata la
   detección de silencios, mete derechos de terceros, hace que cada corte se oiga y hace que el
   micrófono del celular bombee la voz. Se **apaga**.
2. **Grabar fuerte "para que se oiga bien".** Fuerte es saturado, y saturado es irrecuperable. Es mejor
   quedarse bajo.
3. **No monitorear los niveles.** La cámara nativa no muestra medidores. Instala Blackmagic Camera u
   Open Camera, o al menos haz la prueba de 10 segundos con audífonos.
4. **Poner el micrófono a dos metros.** La distancia es el factor que más manda. 30–40 cm cambia todo.
5. **No grabar los 5 segundos de ambiente puro.** Es lo más barato y lo más útil del día. Sin eso, la
   limpieza de ruido queda metálica y los cortes se oyen.
6. **Olvidar el extractor de la cocina, la nevera y el aire.** No los oyes en vivo porque el cerebro los
   filtra; el micrófono los graba enteros.
7. **Micrófono de solapa rozando la ropa.** Produce un frú-frú permanente que no se quita. Asegura el
   cable.
8. **Creer que la limpieza de ruido arregla cualquier cosa.** Quita ruido constante y suave; no quita
   música, ni conversaciones, ni saturación (`71`).
9. **No grabar el sonido real del producto.** El destape y el líquido cayendo valen más que cualquier
   efecto de librería, y solo se graban en el sitio.
10. **Dejar que el micrófono apunte al parlante.** Si la música es inevitable, que el parlante quede
    detrás del micrófono, nunca al frente.
11. **No avisarle al editor que hubo música.** Si lo sabe antes, planea el montaje distinto (menos
    cortes, cama continua). Si lo descubre después, ya montó mal.
12. **Grabar todo el día sin volver a comprobar el audio.** Un cable que se aflojó o un micrófono que se
    quedó sin batería puede arruinar la segunda mitad del rodaje sin que nadie lo note.

---

## Checklist

- [ ] **Música del local apagada.** Apagada, no bajada.
- [ ] **Nevera, extractor, aire acondicionado y televisor apagados** durante las tomas.
- [ ] Se hizo la **prueba de 10 segundos** y se escuchó con audífonos antes de la primera toma real.
- [ ] Los **picos de voz están entre -12 y -6 dB**; ninguno toca 0 dB.
- [ ] Hay **medidor de audio visible** mientras se graba (app con medidores o micrófono con pantalla).
- [ ] El micrófono está a **30–40 cm de la boca** o hay solapa puesta.
- [ ] Si hay solapa: **no roza la ropa**, el cable está asegurado, y se probó con la persona en
      movimiento.
- [ ] Se grabaron **5 segundos de ambiente puro por cada locación**.
- [ ] Se grabaron los **sonidos reales del producto** por separado (destape, líquido, hielo, cocina).
- [ ] Se **volvió a comprobar el audio a mitad del rodaje** (batería, cable, nivel).
- [ ] El editor corrió `volumedetect` sobre **todos** los clips y ninguno está saturado.
- [ ] El editor corrió `silencedetect` y **sí hay silencios detectables** entre tomas.
- [ ] Si la música no se pudo apagar, **se avisó al editor antes de montar** y se grabó ambiente extra
      para construir la cama continua.
