# 74 — Música

La música es la palanca emocional más barata que tienes. Cambias el tema y el mismo montaje pasa de
"tutorial de contabilidad" a "trailer de película". Nada más en la edición tiene esa relación
esfuerzo/resultado.

Y por eso mismo es donde se ve más rápido quién sabe y quién no. Un tema mal elegido, mal cortado y con
un fundido de un segundo al final delata el video entero.

Este módulo es sobre el oficio: elegir, cortar, hacer loop, entrar y salir. Los derechos van en `78`. El
ducking (bajar la música bajo la voz) va en `75`.

---

## 1. Elegir el tema

### El error de partida: elegir la que te gusta

La música del video no es la que a ti te gusta. Es la que **hace lo que el video necesita**. Son cosas
distintas y casi nunca coinciden.

Antes de abrir la biblioteca, contesta tres preguntas en una frase cada una:

1. **¿Qué debe sentir la persona?** (curiosidad, urgencia, calma, ganas, nostalgia)
2. **¿Cuánta atención le sobra para la música?** Si hay voz explicando algo denso, la música tiene que
   desaparecer. Si es montaje sin voz, la música es la protagonista.
3. **¿Cuál es el momento más importante del video, en segundos?** Ahí es donde la música tiene que
   hacer algo.

Con eso ya sabes qué buscar. Sin eso, vas a escuchar 40 temas y a elegir el que te pareció "bacano".

### Los criterios técnicos que sí importan

| Criterio | Qué buscar |
|---|---|
| **Tempo (BPM)** | Que coincida con el ritmo de tus cortes. Ver abajo |
| **Densidad** | Si hay voz, busca temas con poco medio (1–4 kHz). Los pianos y los pads dejan espacio; las guitarras distorsionadas y las voces no |
| **¿Tiene voz?** | Si tu video tiene voz hablada, la música **no puede tener voz cantada**. El cerebro no procesa dos voces a la vez. Busca "instrumental" |
| **Estructura** | ¿Tiene un punto donde entra todo (el "drop")? Ese punto vale oro si lo alineas con tu momento clave |
| **Arranque** | ¿Arranca de una o tiene 8 segundos de intro? Para un reel de 20 s, una intro larga te mata |

**Tempo y ritmo de corte.** Si tu video corta cada 1,5 segundos y la música va a 70 BPM (lenta), hay una
pelea. Regla rápida: un corte cada compás o cada dos compases se siente natural.

| BPM | Duración de un compás (4/4) | Sensación |
|---|---|---|
| 70 | 3,4 s | Calmado, documental, emotivo |
| 90 | 2,7 s | Conversacional |
| 120 | 2,0 s | Enérgico, el estándar de redes |
| 140 | 1,7 s | Rápido, urgente |
| 160+ | 1,5 s | Acelerado |

Para saber el BPM de un archivo sin herramienta: cuenta los golpes en 15 segundos y multiplica por 4.
O usa `ffmpeg` para ver la forma de onda y contar los picos:

```bash
ffmpeg -i musica.mp3 -filter_complex "showwavespic=s=1920x300:colors=white" -frames:v 1 onda.png
```

### Dónde NO buscar

En tu playlist de Spotify. Ver `78`. La música comercial en un video comercial es una cuenta que llega
tarde pero llega.

---

## 2. Cortar al largo

Casi nunca vas a usar el tema completo. Necesitas 27 segundos de un tema de 3 minutos, y necesitas que
esos 27 segundos **suenen como si el tema durara 27 segundos**.

### El corte básico

```bash
# desde el segundo 12 hasta el 39 (27 segundos)
ffmpeg -i musica.mp3 -ss 00:00:12 -t 27 -c:a copy recorte.mp3
```

`-c:a copy` copia sin recomprimir: rápido y sin pérdida. Pero solo corta en el keyframe más cercano, así
que si necesitas precisión al milisegundo, recodifica:

```bash
ffmpeg -i musica.mp3 -ss 00:00:12.350 -t 27 -c:a pcm_s16le recorte.wav
```

### Elegir DÓNDE cortar

Este es el oficio. Dos reglas:

**Regla 1: corta en el golpe, no entre golpes.** Un corte que cae medio segundo antes del tiempo fuerte
suena a error. Uno que cae exacto en el golpe suena a decisión.

Para encontrar los golpes, mira la forma de onda con marcas de tiempo:

```bash
ffmpeg -i musica.mp3 -filter_complex "showwavespic=s=1920x400:colors=cyan:split_channels=0" -frames:v 1 onda.png
```

Los picos altos y regulares son los golpes de tambor. Con la imagen de 1920 px sabiendo la duración
total, calculas el tiempo de cada pico: `tiempo = (pixel / 1920) × duración_total`.

**Regla 2: el tema debe TERMINAR, no interrumpirse.** Si tu video cierra y la música se corta a la
mitad de una frase musical, se oye a amateur aunque le pongas fundido. Busca en el tema un punto donde
la música naturalmente resuelve —el final de una sección, un platillo, un silencio— y haz que ese punto
caiga en tu final.

Truco: **arma el video hacia atrás desde el final de la música.** Si el tema resuelve limpio en el
segundo 1:47 y tu video dura 30 s, tu música arranca en 1:17.

```bash
ffmpeg -i musica.mp3 -ss 00:01:17 -t 30 -c:a pcm_s16le musica_video.wav
```

---

## 3. Loop sin costura

Cuando necesitas más música de la que tienes, o cuando el tema no tiene un final útil, se hace loop. Un
loop bien hecho es invisible; uno mal hecho se oye como un tartamudeo cada 20 segundos.

### Encontrar el punto de loop

Un loop funciona cuando el punto de salida y el de entrada están **en la misma posición del compás**. Si
sales en el tiempo 1 de un compás y entras en el tiempo 1 de otro compás, el loop no se oye.

Cómo calcularlo:

```
duración de un compás = (60 / BPM) × 4
```

A 120 BPM: (60/120) × 4 = **2 segundos por compás**. Entonces cualquier loop de 8, 16, 32 segundos cae
en compás. Un loop de 25 segundos no.

```bash
# tema a 120 BPM: loop de 16 segundos (8 compases), desde el segundo 32
ffmpeg -i musica.wav -ss 32 -t 16 -c:a pcm_s16le loop.wav

# repetirlo 4 veces = 64 segundos
ffmpeg -stream_loop 3 -i loop.wav -c:a pcm_s16le musica_64s.wav
```

`-stream_loop 3` significa "repite 3 veces más", o sea 4 en total. `-stream_loop -1` es infinito (úsalo
con `-t` para cortarlo).

### El crossfade: el remedio cuando el loop no es perfecto

Si el punto de loop deja un clic o un salto, se soluciona cruzando el final con el principio:

```bash
# cruce de 0,5 s entre el final de una copia y el principio de la siguiente
ffmpeg -i loop.wav -i loop.wav -filter_complex "[0][1]acrossfade=d=0.5:c1=tri:c2=tri" loop_doble.wav
```

| Parámetro | Qué es |
|---|---|
| `d` | Duración del cruce en segundos |
| `c1` / `c2` | Curva de salida / entrada: `tri` (lineal), `exp`, `qsin`, `log` |

Para música, `qsin` suena mejor que `tri` porque mantiene la potencia constante durante el cruce (con
`tri` hay un bache de volumen en el medio):

```bash
ffmpeg -i loop.wav -i loop.wav -filter_complex "[0][1]acrossfade=d=0.5:c1=qsin:c2=qsin" loop_doble.wav
```

### Cuándo el loop es una mala idea

Si el tema tiene una melodía muy reconocible, el loop se nota a la segunda vuelta y a la tercera irrita.
Los que loopean bien son los que tienen base rítmica constante sin melodía fuerte —los que suenan
"planos" solos. Por eso las bibliotecas venden versiones "loop" y "underscore".

**En un video de menos de 60 segundos casi nunca deberías necesitar loop.** Si lo necesitas, o el tema
está mal elegido o el video está largo.

---

## 4. Entrar y salir

Aquí está lo que separa un video que suena caro de uno que no. Y es donde vive el error más común de
todos.

### Por qué el fundido de 1 segundo se oye barato

Cuando le pones un fade out de 1 segundo al final de la música, no estás terminando el tema: **estás
bajando el volumen de un tema que sigue sonando.** El oyente lo percibe exactamente así, porque lo es.
Es la versión sonora de apagar la televisión a mitad de la escena.

Un fundido corto grita "no encontré cómo terminar esto".

Tres razones concretas de por qué se oye mal:

1. **El oído lo detecta.** Un segundo alcanza y sobra para que el cerebro registre que la música estaba
   en la mitad de una frase.
2. **Rompe la promesa rítmica.** El pulso desaparece por atenuación en vez de resolver: es como una
   frase que se apaga en vez de terminar en punto.
3. **Delata que no elegiste el tramo.** Quien corta bien no necesita fundido: el tema termina solo.

### Qué hacer en su lugar, en orden de preferencia

**Opción A — Que el tema termine de verdad (siempre la mejor).** Elige un tramo cuyo final coincida con
una resolución musical. Arma el video hacia atrás desde ahí. Cero fundido, o un fundido cosmético de
0,3 s solo para matar la cola.

```bash
# el tema resuelve en 2:14.5; el video dura 28 s → arranca en 1:46.5
ffmpeg -i musica.wav -ss 00:01:46.5 -t 28 -af "afade=t=out:st=27.7:d=0.3" musica_final.wav
```

**Opción B — Corte seco en el golpe.** La música se detiene de un tajo justo en un tiempo fuerte, al
mismo tiempo que aparece la última imagen o el logo. Suena intencional y potente. Es lo que hacen los
anuncios buenos.

```bash
# corte seco en el segundo 27,0 exacto (que es un tiempo fuerte)
ffmpeg -i musica.wav -ss 00:01:47 -t 27.0 -c:a pcm_s16le musica_final.wav
```

**Opción C — Fundido largo y con intención (4–8 segundos).** Un fade out de 6 segundos no se lee como
"corté", se lee como "esto se está yendo". Para piezas emotivas funciona.

```bash
ffmpeg -i musica.wav -af "afade=t=out:st=22:d=6" musica_final.wav
```

**Opción D — Fundido de 1 segundo.** Solo si nada de lo anterior es posible y hay prisa. Sabiendo que
se oye barato.

### La entrada

Mismo criterio, invertido.

**Entrada dura, en el golpe.** La música arranca de una, en el primer frame o justo en el primer corte.
Es lo más común y lo más efectivo en redes: el video empieza y la música ya está.

**Entrada con fundido corto (0,3–0,8 s).** Para matar el clic del arranque del archivo sin que se note.
Esto sí es legítimo y casi obligatorio:

```bash
ffmpeg -i musica.wav -af "afade=t=in:st=0:d=0.5" musica_in.wav
```

**Entrada tardía.** La música arranca en el segundo 2 o 3, cuando termina la primera frase de la voz.
Suena a que llegó a acompañar, no a que estaba puesta de fondo. Recurso sutil y muy bueno.

```bash
# retrasar la música 2,4 segundos (adelay va en ms, uno por canal)
ffmpeg -i musica.wav -af "adelay=2400|2400" musica_tarde.wav
```

### Entrada y salida completas, en un comando

```bash
ffmpeg -i musica_cruda.wav -ss 00:01:46.5 -t 28 -af "afade=t=in:st=0:d=0.4,afade=t=out:st=27.6:d=0.4,volume=-16dB" musica_lista.wav
```

Ese `volume=-16dB` es el nivel de la música respecto a la voz. Ver `75` para hacerlo bien con ducking en
vez de un volumen fijo.

---

## 5. Niveles: dónde va la música

Números de partida, respecto a la voz:

| Situación | Nivel de la música |
|---|---|
| Debajo de voz hablada continua | **−18 a −22 dB** bajo la voz |
| Debajo de voz con pausas (ducking) | −12 dB en pausa, −22 dB bajo voz |
| Sin voz, montaje puro | La música es el volumen principal |
| Bajo texto en pantalla sin voz | Volumen pleno |

Si tu música está a −6 dB bajo la voz, se oye mucho. Si está a −30 dB, ¿para qué la pusiste? El rango
útil es estrecho: entre −16 y −24 dB bajo la voz. Se ajusta con `volume=-18dB`.

Mezclar voz y música:

```bash
ffmpeg -i voz.wav -i musica.wav -filter_complex "[1]volume=-18dB[m];[0][m]amix=inputs=2:duration=first:dropout_transition=0" mezcla.wav
```

`duration=first` hace que la mezcla dure lo que dura la voz. `dropout_transition=0` evita que `amix`
suba el volumen automáticamente cuando una pista se acaba (un comportamiento por defecto que sorprende
a todo el mundo).

---

## 6. Un caso completo

Reel de 28 segundos: voz en off, música de fondo, cierre con logo.

```bash
# 1) preparar la voz (ver 70)
ffmpeg -i voz_cruda.wav -af "highpass=f=85,arnndn=m='cb.rnnn':mix=0.85,afftdn=nf=-24:tn=1,deesser=i=0.4,acompressor=threshold=-20dB:ratio=3:attack=15:release=180:makeup=2" voz.wav

# 2) elegir el tramo de música que RESUELVE al final, con fade in corto
ffmpeg -i tema.mp3 -ss 00:01:46.5 -t 28 -af "afade=t=in:st=0:d=0.4" musica.wav

# 3) mezclar con ducking (ver 76)
ffmpeg -i voz.wav -i musica.wav -filter_complex "[1][0]sidechaincompress=threshold=0.025:ratio=8:attack=15:release=400[duck];[0][duck]amix=inputs=2:duration=first:dropout_transition=0[out]" -map "[out]" mezcla.wav

# 4) normalizar la mezcla al estándar (ver 73)
ffmpeg -i mezcla.wav -af "loudnorm=I=-14:TP=-1.5:LRA=11" audio_final.wav

# 5) montar sobre el video
ffmpeg -i video.mp4 -i audio_final.wav -c:v copy -map 0:v:0 -map 1:a:0 -c:a aac -b:a 192k ENTREGA.mp4
```

---

## Errores comunes

- **Elegir la música que te gusta y no la que el video necesita.** Contesta las tres preguntas primero.
- **Música con voz cantada debajo de voz hablada.** El cerebro no procesa dos voces. Instrumental
  siempre.
- **El fundido de 1 segundo al final.** Se oye barato porque es bajar el volumen a un tema que sigue.
  Elige un tramo que resuelva, o corta seco en el golpe, o funde 5 segundos.
- **Cortar entre golpes.** Un corte medio segundo antes del tiempo fuerte suena a error.
- **Loop en tramo que no cae en compás.** Se oye el tartamudeo. Calcula: (60/BPM) × 4.
- **Loop de un tema con melodía fuerte.** A la tercera vuelta irrita. Usa temas tipo "underscore".
- **Música muy fuerte "porque suena bien".** La estás oyendo con audífonos y ya sabes lo que dice la
  voz. Quien la oye por primera vez en un parlante de celular no entiende nada.
- **Volumen fijo de música en vez de ducking.** Ver `75`. Un volumen fijo o tapa la voz o no se oye.
- **Intro larga en un reel corto.** Ocho segundos de intro en un video de 20 s es el 40% de la pieza sin
  energía.
- **Usar `amix` sin `dropout_transition=0`.** Cuando una pista termina, la otra sube de golpe sola.
- **No normalizar después de mezclar.** La mezcla cambia el LUFS. Se normaliza al final (ver `73`).
- **Música de Spotify/YouTube en un video comercial.** Ver `78`. Llega la cuenta.

---

## Checklist

- [ ] Contesté las **tres preguntas** (qué debe sentir, cuánta atención sobra, cuál es el momento clave)
      antes de elegir.
- [ ] La música es **instrumental** si hay voz hablada.
- [ ] El **tempo** de la música va con el ritmo de mis cortes.
- [ ] El **momento más importante del video** cae en un momento importante de la música.
- [ ] El tramo elegido **arranca en el golpe**, no a mitad de compás.
- [ ] El tramo elegido **termina resolviendo**, o corta seco en un tiempo fuerte.
- [ ] **No hay un fundido de 1 segundo** al final. O resuelve, o corta seco, o funde 4–8 s.
- [ ] Hay un **fade in de 0,3–0,5 s** para matar el clic del arranque.
- [ ] Si hice loop, el tramo **cae en compás** y usé `acrossfade` con `qsin` si hacía falta.
- [ ] La música está entre **−16 y −24 dB** bajo la voz, con **ducking** (ver `75`), no volumen fijo.
- [ ] Usé `amix` con **`dropout_transition=0`**.
- [ ] **Normalicé la mezcla completa** a −14 LUFS después de montar todo (ver `73`).
- [ ] Escuché la mezcla en **parlante de celular**: se entiende cada palabra de la voz.
- [ ] Tengo claro **de dónde salió la música y bajo qué licencia** (ver `78`).
