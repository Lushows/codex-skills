# 75 — Ducking

**Ducking** es que la música baje sola cuando alguien habla y suba sola cuando deja de hablar.

Antes de que existiera el software, eso lo hacía un operador de radio con la mano puesta en el fader:
el locutor abría la boca, la mano bajaba; el locutor respiraba, la mano subía. Media hora de programa,
media hora de mano en el fader. Los buenos tenían un pulso que se reconocía al aire.

`sidechaincompress` es esa mano, automática. Y en el momento en que entiendes que **eso** es lo que
estás configurando —una mano, no un filtro— los parámetros dejan de ser números al azar.

---

## Por qué no sirve el volumen fijo

La alternativa al ducking es poner la música en un volumen bajito y dejarla ahí. Es lo que hace casi
todo el mundo, y tiene un problema que no se puede resolver:

**No existe un volumen que sirva para los dos momentos.**

- El volumen al que la música no tapa la voz es un volumen al que la música **no se oye** cuando la voz
  calla. Los silencios quedan muertos.
- El volumen al que la música suena bien en los silencios es un volumen que **le come sílabas a la voz**.

Es una elección entre dos cosas malas. El ducking la disuelve: música fuerte cuando no hay voz, música
discreta cuando la hay. Dos volúmenes distintos, uno para cada momento, sin que tú muevas nada.

Y hay un efecto secundario que casi nadie nombra: **el ducking hace que la voz suene más fuerte sin
subirle el volumen.** Como lo que compite con ella se aparta, la voz gana claridad sola. Es la manera
más limpia de resolver "no se entiende bien lo que dice".

---

## `sidechaincompress` — cómo funciona

Es un compresor normal con una diferencia: **lo que dispara la compresión no es la señal que se está
comprimiendo.** Le entran dos pistas:

- La **primera** es la que se comprime (la música).
- La **segunda** es la que dispara (la voz). Esa nunca se toca ni se oye desde el filtro.

En ffmpeg, el orden de las entradas es esa distinción entera, y es donde se equivoca todo el mundo:

```
[musica][voz]sidechaincompress=...
   ↑        ↑
   |        └── el disparador: cuando esto suena, actúa
   └── lo que baja
```

Si inviertes el orden, lo que baja es la voz cuando suena la música. Que es exactamente lo contrario.

---

## El comando completo

```bash
ffmpeg -i voz.wav -i musica.wav -filter_complex "[1][0]sidechaincompress=threshold=0.025:ratio=8:attack=15:release=400[duck];[0][duck]amix=inputs=2:duration=first:dropout_transition=0[out]" -map "[out]" mezcla.wav
```

Léelo por partes:

| Parte | Qué hace |
|---|---|
| `-i voz.wav -i musica.wav` | Entrada 0 = voz, entrada 1 = música |
| `[1][0]sidechaincompress=...` | Comprime la música (`[1]`) disparada por la voz (`[0]`) |
| `[duck]` | El resultado: la música ya con ducking |
| `[0][duck]amix=inputs=2` | Mezcla la voz original con la música duckeada |
| `duration=first` | La mezcla dura lo que dure la voz |
| `dropout_transition=0` | Evita que `amix` suba el volumen cuando una pista se acaba |

Esos valores —`threshold=0.025:ratio=8:attack=15:release=400`— son los que funcionaron en material real
y son tu punto de partida. Cópialos.

---

## Los parámetros, uno por uno

### `threshold` — qué tan fuerte tiene que hablar para que baje

Escala **lineal** de 0 a 1, no dB. Esto confunde a todo el mundo la primera vez.

| Lineal | dB | Comportamiento |
|---|---|---|
| 0,003 | −50 dB | Baja hasta con una respiración. Demasiado sensible |
| 0,015 | −36 dB | Muy sensible |
| **0,025** | **−32 dB** | **El valor probado. Reacciona a la voz, no al ruido** |
| 0,05 | −26 dB | Solo reacciona a voz clara |
| 0,1 | −20 dB | Solo con voz fuerte. La música se queda arriba mucho tiempo |

Conversión: `lineal = 10^(dB/20)`. Y al revés: `dB = 20 × log10(lineal)`.

**Cómo elegirlo:** debe estar por encima del piso de ruido de tu voz y por debajo del nivel al que
habla. Si limpiaste la voz como manda `71` y tu piso quedó en −30 dB, un umbral en 0,025 (−32 dB) está
justo al filo — súbelo un poco a 0,04. Si el piso está en −45 dB, 0,025 es perfecto.

Si la música baja sola cuando nadie habla, tu umbral está por debajo del ruido de la pista de voz. O
subes el umbral, o limpias mejor la voz.

### `ratio` — cuánto baja

| Ratio | Cuánto baja | Para qué |
|---|---|---|
| 2 – 4 | Poco, 2–4 dB | Música que debe seguir sintiéndose presente |
| **8** | **Notable, 8–12 dB** | **Voz explicando. El valor probado** |
| 12 – 20 | Mucho | Voz que debe dominar totalmente |

Ratio 8 con umbral 0,025 baja la música unos 10 dB cuando hay voz. Eso es la diferencia entre "la
música está ahí" y "la música se apartó".

### `attack` — qué tan rápido baja

En milisegundos. Este parámetro es la mano del operador de radio bajando.

| Attack | Efecto |
|---|---|
| 1 – 5 ms | Baja tan rápido que se oye el brinco. Suena a máquina |
| **15 ms** | **La primera sílaba entra limpia y la música ya bajó. El valor probado** |
| 50 – 100 ms | La primera palabra queda tapada. Se pierde el arranque de la frase |

**Muy importante:** el attack debe ser lo bastante rápido para que la primera sílaba se entienda, pero
no tanto como para que se oiga el escalón. 15 ms es exactamente ese punto. Si tu voz arranca muy de
golpe (interjecciones, gritos), baja a 10 ms.

### `release` — qué tan rápido sube

En milisegundos. Este es **el parámetro que más se equivoca**, y el que decide si el ducking suena
profesional o suena a filtro.

| Release | Efecto |
|---|---|
| 50 – 150 ms | La música sube y baja **entre palabras**. El sonido "respira". Horrible |
| 250 ms | Sube entre frases, pero todavía se nota |
| **400 ms** | **Sube cuando la persona de verdad terminó. El valor probado** |
| 800 – 1500 ms | Muy lento. La música tarda en volver y los silencios quedan vacíos |

La lógica: **una persona hablando hace pausas de 100–300 ms entre palabras y de 400–800 ms entre
frases.** Un release de 400 ms ignora las pausas cortas (no le da tiempo de subir antes de que la
siguiente palabra vuelva a bajarla) y sí responde a las pausas largas.

Si el release es de 100 ms, la música sube en cada coma. Eso es el "bombeo" y es el delator número uno
de un ducking mal hecho: se oye como si la música estuviera nerviosa.

### `makeup`, `level_sc` y los demás

```bash
sidechaincompress=threshold=0.025:ratio=8:attack=15:release=400:makeup=1:level_sc=1:knee=2.8:link=average:detection=rms
```

| Parámetro | Qué es | Valor |
|---|---|---|
| `makeup` | Ganancia después de comprimir | **1** (no queremos recuperar volumen) |
| `level_sc` | Ganancia de la señal disparadora (no se oye, solo dispara) | 1; súbelo si la voz es muy suave |
| `knee` | Suavidad de la transición | 2,8 |
| `link` | `average` o `maximum` en estéreo | `average` |
| `detection` | `peak` o `rms` | **`rms`** para voz |

`detection=rms` importa: mide el promedio en vez del pico instantáneo, lo cual hace que el ducking
responda a "está hablando" y no a "hubo un chasquido".

`level_sc` es útil cuando la voz está muy baja para disparar el compresor pero no quieres cambiar su
volumen real. Súbelo a 2 o 4 y el disparador se hace más sensible sin tocar la voz que se oye.

---

## Cuándo la música DEBE subir

El ducking no es solo "bajar la música". Bien usado, es un instrumento de ritmo. Estos son los momentos
en los que la música tiene que subir, y donde un ducking puramente automático se queda corto:

**1. En el arranque, antes de la primera palabra.** Los primeros 1–3 segundos con música a volumen
pleno le dan energía al video antes de que empiece a hablar. Es lo que hace que un reel "arranque".

**2. Entre secciones.** Cuando termina un bloque y empieza otro, 1,5–2 segundos de música arriba
funcionan como un punto y aparte. El oyente respira y sabe que cambió el tema.

**3. En el momento visual clave.** Cuando aparece el producto, cuando se revela el resultado, cuando
llega el "antes y después". Ahí la voz calla y la música sube. Es la parte emocional del video.

**4. En el cierre.** Después del último dato o del CTA, la música vuelve a subir y cierra la pieza.

**5. Cuando la imagen tiene que hablar sola.** Un plano bonito con voz encima es un plano desperdiciado.
Cállate y sube la música 3 segundos.

`sidechaincompress` hace 1, 2, 4 y 5 solo, siempre que **haya silencio de verdad en la pista de voz**.
Por eso importa que los silencios estén limpios (ver el gate en `71`): si entre bloque y bloque queda
un "shhh" a −28 dB, el ducking cree que sigues hablando y la música no sube.

Para el punto 3 —una subida deliberada, más fuerte que el nivel base— hay que hacerlo a mano con
`volume` y una expresión de tiempo:

```bash
# la música sube 5 dB entre el segundo 14 y el 18, con rampa de medio segundo
ffmpeg -i musica.wav -af "volume='if(between(t,14,18),1.78,1)':eval=frame" musica_realce.wav
```

1,78 en lineal ≈ +5 dB. `eval=frame` hace que la expresión se evalúe todo el tiempo, no una sola vez.

Una versión con rampa suave, usando dos `afade` con `volume` combinados, es más limpia de armar
recortando el tramo, subiéndolo y volviéndolo a pegar:

```bash
# recortar el tramo, subirlo con entrada/salida suave, y volver a concatenar
ffmpeg -i musica.wav -ss 0 -t 14 a.wav
ffmpeg -i musica.wav -ss 14 -t 4 -af "volume=5dB,afade=t=in:st=0:d=0.5,afade=t=out:st=3.5:d=0.5" b.wav
ffmpeg -i musica.wav -ss 18 c.wav
ffmpeg -i a.wav -i b.wav -i c.wav -filter_complex "[0][1][2]concat=n=3:v=0:a=1" musica_realce.wav
```

---

## Ducking de más de dos pistas

Caso real: voz + música + efectos de sonido. La voz duckea a la música, pero los efectos no deberían
duckear (son cortos y puntuales).

```bash
ffmpeg -i voz.wav -i musica.wav -i efectos.wav -filter_complex "\
[1]volume=-14dB[m]; \
[m][0]sidechaincompress=threshold=0.025:ratio=8:attack=15:release=400[duck]; \
[2]volume=-8dB[fx]; \
[0][duck][fx]amix=inputs=3:duration=first:dropout_transition=0[out]" \
-map "[out]" mezcla.wav
```

Si además quieres que los efectos duckeen la música (para que un whoosh tenga espacio), duplicas la
cadena: pero cuidado, dos sidechain encadenados sobre la misma música pueden bajarla demasiado. Suma:
ratio 8 + ratio 8 puede dejar la música 20 dB abajo. Baja el segundo a ratio 3.

---

## Verificar que el ducking está bien

**Prueba 1: escucha solo la pista de música duckeada.** Debe sonar como una marea suave, no como un
interruptor.

```bash
ffmpeg -i voz.wav -i musica.wav -filter_complex "[1][0]sidechaincompress=threshold=0.025:ratio=8:attack=15:release=400[duck]" -map "[duck]" solo_musica_duck.wav
```

**Prueba 2: mira la forma de onda.** Debe verse el patrón de bajadas y subidas alineado con la voz:

```bash
ffmpeg -i solo_musica_duck.wav -filter_complex "showwavespic=s=1920x300:colors=orange" -frames:v 1 onda_duck.png
```

Si la onda parece un peine (sube y baja cada 200 ms), tu release está muy corto.

**Prueba 3: la prueba del celular.** Pon la mezcla en el parlante del celular a volumen medio, a un
metro de distancia, y trata de entender lo que dice sin leer los subtítulos. Si te cuesta, el ducking
está flojo (sube el ratio) o la música está muy arriba.

**Prueba 4: la prueba del silencio.** Escucha un tramo donde nadie habla. La música debe estar
**presente y viva**. Si está tímida, tu nivel base de música es muy bajo — sube la música y deja que el
ducking haga el trabajo de bajarla.

Ese último punto es el ajuste que más mejora una mezcla: **con ducking bien puesto, la música puede
estar mucho más arriba de lo que te atreverías sin él.**

---

## Tabla de valores por tipo de pieza

| Tipo | threshold | ratio | attack | release | Nivel base de música |
|---|---|---|---|---|---|
| **Reel / TikTok con voz** | 0,025 | 8 | 15 | 400 | −12 dB |
| **Anuncio de radio / spot** | 0,03 | 12 | 10 | 350 | −10 dB |
| **Tutorial / explicativo largo** | 0,03 | 6 | 20 | 500 | −16 dB |
| **Documental / entrevista** | 0,02 | 5 | 25 | 600 | −18 dB |
| **Podcast con música de fondo** | 0,02 | 10 | 20 | 500 | −20 dB |
| **Montaje emotivo con poca voz** | 0,04 | 4 | 30 | 800 | −6 dB |

Fíjate en el patrón: mientras más importa la voz y más corta la pieza, más agresivo el ducking (ratio
alto, attack rápido). Mientras más importa la atmósfera, más suave (ratio bajo, release largo).

---

## Errores comunes

- **Invertir el orden de las entradas.** `[musica][voz]`, no `[voz][musica]`. Si lo inviertes, la voz
  baja cuando suena la música.
- **Release muy corto (< 250 ms).** La música respira entre palabras. Es el delator número uno.
- **Attack muy lento (> 50 ms).** Se pierde la primera palabra de cada frase.
- **Attack muy rápido (< 5 ms).** Se oye el escalón, suena a máquina.
- **Usar volumen fijo en vez de ducking.** No existe un volumen bueno para los dos momentos.
- **Umbral en dB.** `sidechaincompress` usa escala lineal 0–1. 0,025 ≈ −32 dB.
- **Umbral por debajo del ruido de la pista de voz.** La música baja sola sin que nadie hable. Limpia la
  voz (`71`) o sube el umbral.
- **Poner el nivel base de música muy bajo "por si acaso".** Con ducking puedes subirla. Si no la subes,
  desperdicias el ducking.
- **No usar `dropout_transition=0` en `amix`.** Cuando la voz termina, `amix` le sube el volumen a la
  música de golpe, solo.
- **Esperar que el ducking haga las subidas dramáticas.** Los realces en el momento clave se hacen a
  mano. El ducking solo reacciona a la ausencia de voz.
- **Silencios sucios en la pista de voz.** Si entre frases hay ruido, el ducking cree que hablas y la
  música nunca sube.
- **Encadenar dos sidechain con ratio alto sobre la misma música.** Se suman y la música desaparece.

---

## Checklist

- [ ] El orden es **`[musica][voz]sidechaincompress`**, no al revés.
- [ ] `threshold` está en escala lineal y **por encima del piso de ruido** de la voz (0,025 típico).
- [ ] `ratio` elegido según el tipo de pieza (8 para redes con voz).
- [ ] `attack` entre **10 y 25 ms**: la primera sílaba entra limpia y no se oye el escalón.
- [ ] `release` **de 350 ms o más**: la música no sube entre palabras.
- [ ] `detection=rms`, no `peak`.
- [ ] `amix` lleva **`dropout_transition=0`**.
- [ ] La pista de voz tiene **silencios limpios** (gate aplicado, ver `71`).
- [ ] Escuché **la música duckeada sola**: parece marea, no interruptor.
- [ ] Miré la **forma de onda** de la música duckeada: no parece un peine.
- [ ] El **nivel base de la música está lo bastante arriba** para que se sienta en los silencios.
- [ ] Hay música a volumen pleno en el **arranque**, en los **cambios de sección** y en el **cierre**.
- [ ] Si hay un momento visual clave, la **música sube a mano** ahí y la voz calla.
- [ ] Pasé la **prueba del parlante del celular**: se entiende cada palabra sin leer subtítulos.
- [ ] Normalicé la mezcla completa a **−14 LUFS** después de todo esto (ver `73`).
