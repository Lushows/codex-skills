# 71 — Limpieza de ruido

Este es el paso 2 de la cadena de `70`, y es el que todo el mundo cree que es "el" paso. No lo es, pero
sí es el que más se nota cuando está mal hecho: o queda el ventilador puesto, o queda una voz de robot
metálica que suena peor que el ruido.

Aquí están las cuatro herramientas reales de ffmpeg, cuál usar en cada caso, y la razón artística por
la que **nunca** debes limpiar al 100%.

---

## Primero: identifica qué tipo de ruido tienes

No hay un botón universal porque no hay un ruido universal. Escucha 5 segundos de silencio de tu toma y
clasifica:

| Lo que oyes | Qué es | Con qué se ataca |
|---|---|---|
| "Shhhhh" parejo, sin cambios | Ruido de banda ancha: aire acondicionado, ventilador, preamp barato | `arnndn` + `afftdn` |
| Zumbido grave "mmmm" | Hum eléctrico (60 Hz en Colombia, y sus múltiplos) | `highpass` + `equalizer` en 60/120/180 Hz |
| Retumbe sordo, golpes | Vibración: mesa, pisadas, viento en el micro | `highpass=f=85` |
| Calle, gente, música de fondo | Ruido **variable** con contenido | Aquí ffmpeg pierde. Ver "lo que no se arregla" |
| "Tk", "clop" entre palabras | Chasquidos de boca | `adeclick` |
| Crujido, distorsión | El audio ya venía saturado | `adeclip` (y probablemente hay que regrabar) |

Medir el piso de ruido antes de tocar nada:

```bash
# corta 2 segundos donde nadie habla y mide
ffmpeg -i voz_cruda.wav -ss 00:00:04 -t 2 -af volumedetect -f null -
```

El `mean_volume` que sale es tu punto de partida. Anótalo. Sin ese número no puedes saber si mejoraste.

Referencia rápida de qué significa el número:

| Piso de ruido | Veredicto |
|---|---|
| −20 dB o más alto | Grave. Se oye el ruido incluso con la voz encima |
| −30 dB | Aceptable para redes |
| −45 dB | Bien |
| −60 dB o menos | Estudio |

---

## `arnndn` — reducción de ruido con red neuronal

Es la mejor herramienta que tiene ffmpeg para voz, y es la que hace el 80% del trabajo. Usa **RNNoise**,
una red neuronal pequeña entrenada específicamente para distinguir voz humana de ruido. Por eso no
destruye la voz al perseguir el fondo: aprendió cómo suena una voz.

**Necesita un archivo de modelo (`.rnnn`) que no viene con ffmpeg.** Se bajan del repositorio público
**GregorR/rnnoise-models**:

```bash
git clone https://github.com/GregorR/rnnoise-models.git
# adentro hay varios modelos; los más usados:
#   cb.rnnn / conjoined-burgers  → equilibrado, el que uso por defecto
#   bd.rnnn / beguiling-drafter  → agresivo, para ruido fuerte
#   lq.rnnn / leavened-quisling  → suave, conserva más textura
#   mp.rnnn / marathon-prescription → habla en ambientes difíciles
#   sh.rnnn / somnolent-hogwash  → general
```

Uso:

```bash
ffmpeg -i voz_cruda.wav -af "arnndn=m='cb.rnnn':mix=0.85" voz_sin_ruido.wav
```

Parámetros que importan:

| Parámetro | Qué es | Valor |
|---|---|---|
| `m` | Ruta al archivo de modelo. **Obligatorio** | `'cb.rnnn'` |
| `mix` | Cuánto de la limpieza se mezcla con el original. 1,0 = todo limpio, 0 = sin efecto | **0,80 – 0,90** |

Ojo con la ruta en Windows: si el modelo está en otra carpeta, usa barras normales y comillas simples
adentro del filtro, o ffmpeg se confunde con los dos puntos de `C:`:

```bash
ffmpeg -i voz.wav -af "arnndn=m='C\:/modelos/cb.rnnn':mix=0.85" salida.wav
```

**Limitaciones honestas de `arnndn`:**
- Trabaja a 48 kHz. Si tu audio está a 44,1 kHz, conviértelo antes (`-ar 48000`) o el modelo rinde peor.
- Es mono por canal. En estéreo procesa cada canal por separado, lo cual está bien para voz.
- **No sirve para música.** Le arranca los instrumentos porque no son voz.
- Contra ruido con contenido (una conversación de fondo, un carro que pasa) hace poco: eso no es "ruido"
  para la red, es audio.

---

## `afftdn` — reducción por resta espectral

El método clásico: analiza el espectro, estima cuál es el ruido, y lo resta. Es menos inteligente que
`arnndn` pero es excelente **como segunda pasada**, para barrer el residuo.

```bash
ffmpeg -i entrada.wav -af "afftdn=nf=-24:tn=1" salida.wav
```

| Parámetro | Qué es | Valor típico |
|---|---|---|
| `nf` | Piso de ruido estimado en dB. Más negativo = más suave | **−20 a −30** |
| `nr` | Cuánto reduce, en dB (0,01 a 97) | 12 (defecto) a 20 |
| `tn` | Seguimiento adaptativo del ruido: `1` lo activa | **1** |
| `nt` | Tipo de ruido: `w` blanco, `v` vinilo, `s` shellac, `c` personalizado | `w` |

`tn=1` es importante: hace que el filtro **rastree** cómo cambia el ruido a lo largo de la toma, en vez
de asumir que es el mismo del segundo 1 hasta el final. En material de campo eso cambia todo.

**Modo de aprendizaje.** `afftdn` puede aprender el ruido de un trozo específico. Le señalas un tramo
donde solo hay ruido y él lo caracteriza:

```bash
# el filtro entra en modo "aprender" durante el primer segundo, luego limpia
ffmpeg -i voz.wav -af "afftdn=nr=20:nf=-25:tn=1,asendcmd=0.0 afftdn sn start,asendcmd=1.0 afftdn sn stop" salida.wav
```

Esto funciona bien si tu grabación arranca con un segundo de silencio limpio antes de que empiece a
hablar. Grabar ese segundo a propósito es un hábito que vale oro.

**Por qué `arnndn` + `afftdn` juntos y en ese orden:** la red neuronal quita el grueso sin dañar la voz;
la resta espectral, con menos ruido que perseguir, puede ser suave y aún así dejarlo impecable. Al
revés, `afftdn` primero deja artefactos "burbujeantes" que confunden a la red.

---

## `anlmdn` — reducción por medias no locales

Un tercer método. Busca patrones parecidos en el tiempo y promedia. Es lento, pero es el que mejor
conserva la naturalidad en material **suave** — voz susurrada, ambiente delicado, tomas donde `arnndn`
suena artificial.

```bash
ffmpeg -i entrada.wav -af "anlmdn=s=0.0001:p=0.002:r=0.006" salida.wav
```

| Parámetro | Qué es | Valor |
|---|---|---|
| `s` | Fuerza del filtrado | 0,00001 – 0,001 (**0,0001** para voz) |
| `p` | Duración del "parche" que compara, en segundos | 0,002 |
| `r` | Radio de búsqueda, en segundos | 0,006 |
| `m` | Modo de suavizado | `w` (por defecto) |

Cuándo lo prefiero: cuando la toma ya está casi limpia y solo quiero bajar 3–4 dB sin que se note nada.
`arnndn` en esos casos es un mazo para matar una mosca.

**Advertencia:** es pesado. En un archivo de 10 minutos puede tardar varios minutos. No lo pongas en una
cadena que vas a correr 40 veces mientras pruebas.

---

## `agate` — la compuerta

No quita ruido: **lo apaga cuando no hay voz**. Es el paso 1 de la cadena de `70`.

```bash
ffmpeg -i entrada.wav -af "agate=threshold=0.02:ratio=4:attack=10:release=250:knee=2.8" salida.wav
```

| Parámetro | Qué es | Valor para voz |
|---|---|---|
| `threshold` | Nivel bajo el cual cierra (escala lineal 0–1; 0,02 ≈ −34 dB) | **0,01 – 0,03** |
| `ratio` | Qué tanto baja lo que está por debajo | 2 – 6 (no 100) |
| `attack` | Cuánto tarda en abrir, en ms | **5 – 15** |
| `release` | Cuánto tarda en cerrar, en ms | **200 – 400** |
| `knee` | Qué tan suave es la transición | 2 – 4 |
| `detection` | `peak` o `rms` | `rms` para voz |

**La regla del gate:** `attack` corto, `release` largo. Si el attack es lento, se come el arranque de la
palabra ("...ola" en vez de "hola"). Si el release es corto, corta la cola de las palabras y se oye como
si alguien apagara el micro después de cada frase — el famoso efecto "walkie-talkie".

**Ratio moderado, no infinito.** Un gate con ratio=100 no baja el ruido: lo *apaga*. Y ese contraste
entre "hay fondo" y "no hay nada" es más raro al oído que el fondo mismo. Con ratio 3–4 el fondo baja
10 dB en los silencios y suena natural.

Para casos difíciles hay `sidechaingate`, que abre la compuerta de una pista usando **otra** como
disparador. Útil si tienes una pista limpia de referencia (por ejemplo, el audio de un micro de solapa)
para abrir el de la cámara.

---

## `adeclick` y `adeclip` — chasquidos y saturación

```bash
# chasquidos de boca, clics digitales
ffmpeg -i entrada.wav -af "adeclick=w=55:o=2:a=2:m=a" salida.wav

# audio que venía saturado (recorta los picos aplanados y los reconstruye)
ffmpeg -i entrada.wav -af "adeclip=w=55:o=2:a=2:t=10:n=1000" salida.wav
```

`adeclick` va **antes del compresor** siempre. Un chasquido es un pico instantáneo; el compresor lo lee
como si fuera un grito y le baja el volumen a la frase entera. Es la causa oculta de "esa oración suena
hundida y no sé por qué".

`adeclip` **no** hace milagros. Si grabaste saturado, la información no existe; el filtro la inventa. Se
nota. Sirve para salvar una toma irrepetible, no para grabar mal a propósito.

---

## Hum eléctrico: el caso especial

El zumbido de 60 Hz (Colombia, EE.UU.) o 50 Hz (Europa) no se quita con `arnndn` porque es una frecuencia
pura, no ruido de banda ancha. Se ataca con filtros de banda estrecha en la fundamental y sus armónicos:

```bash
ffmpeg -i entrada.wav -af "highpass=f=85,equalizer=f=120:t=q:w=8:g=-18,equalizer=f=180:t=q:w=8:g=-15,equalizer=f=240:t=q:w=8:g=-12" salida.wav
```

El `highpass=f=85` ya se lleva la fundamental de 60 Hz. Los `equalizer` con `w=8` (Q alto = muy estrecho)
atacan los armónicos en 120, 180 y 240 Hz. Baja solo lo necesario; si te pasas, la voz pierde cuerpo.

Para saber si tienes hum, mira el espectro:

```bash
ffmpeg -i entrada.wav -lavfi showspectrumpic=s=1024x512:legend=1 espectro.png
```

Si ves líneas horizontales rectas en la parte baja, eso es hum.

---

## Por qué NO limpiar al 100%

Esta es la parte que casi nadie te dice.

Cuando pones `mix=1.0` y le sacas hasta el último decibel de fondo, la voz queda **perfecta y muerta**.
Suena a cabina de radio flotando en el vacío. Y aunque la gente no sepa explicar por qué, lo percibe:
"suena raro", "suena a inteligencia artificial", "suena falso".

La razón es física. En el mundo real no existe una voz sin espacio alrededor. Tu cerebro lleva toda la
vida oyendo voces acompañadas de aire, reflejo y ambiente. Cuando le quitas eso, le quitas la prueba de
que la grabación ocurrió en un lugar. Es lo mismo que una foto con la piel retocada al 100%: técnicamente
perfecta, y sin embargo el ojo sabe que algo pasó ahí.

**Ese 15% de ruido que dejas no es un descuido. Es la información de que esto es real.**

Guía de valores:

| Material | `mix` | Por qué |
|---|---|---|
| Entrevista, documental, testimonio | **0,80** | Se necesita la sensación de sitio real |
| Talking head para redes | **0,85** | El punto dulce. Limpio pero vivo |
| Voz en off de anuncio | **0,90 – 0,95** | Aquí sí se busca voz "de estudio" |
| Rescate de toma desastrosa | 1,0 | Y le vuelves a poner ambiente encima |

**La técnica del ambiente reinyectado.** Si tuviste que limpiar a fondo, graba (o toma del propio
material) 20–30 segundos del sitio en silencio, hazlo loop, y ponlo debajo de la voz a −45 dB:

```bash
# 1) sacar un trozo de ambiente limpio del propio material
ffmpeg -i original.wav -ss 00:00:02 -t 20 -af "volume=-45dB" ambiente.wav

# 2) mezclarlo debajo de la voz procesada, en loop
ffmpeg -i voz_limpia.wav -stream_loop -1 -i ambiente.wav -filter_complex "[0][1]amix=inputs=2:duration=first:weights=1 0.06[out]" -map "[out]" voz_final.wav
```

Suena más real que la voz esterilizada. Contradictorio pero cierto: le agregas ruido para que suene
mejor. Ver `77` para la idea completa.

---

## Lo que la limpieza NO arregla

Sé honesto con el cliente y contigo:

- **Un cuarto con eco.** El reverb no es ruido, es tu propia voz llegando tarde. `arnndn` no lo ve. Lo
  único que ataca reverb de verdad es una herramienta dedicada (DeepFilterNet, iZotope RX) y aun así con
  límite. La solución real: cortinas, alfombra, ropa colgada, o grabar en un clóset.
- **Ruido más fuerte que la voz.** Si el aire acondicionado está a −20 dB y la voz a −18, no hay
  algoritmo. Regraba.
- **Conversación o música de fondo.** Para el modelo eso es voz/música, no ruido.
- **Audio saturado.** La información se perdió al grabar.
- **Un micrófono malo.** Un micro que no captura los 4 kHz no los va a inventar después.

Decirle a alguien "esto hay que regrabarlo" a tiempo es más profesional que entregarle una voz de robot
y esperar que no se dé cuenta.

---

## Cadena de limpieza recomendada, completa

```bash
ffmpeg -i voz_cruda.wav -af "agate=threshold=0.02:ratio=4:attack=10:release=250:knee=2.8,highpass=f=85,arnndn=m='cb.rnnn':mix=0.85,afftdn=nf=-24:tn=1,adeclick=w=55:o=2" voz_limpia.wav
```

Y la verificación inmediata:

```bash
ffmpeg -i voz_limpia.wav -ss 00:00:04 -t 2 -af volumedetect -f null -
```

Compara el `mean_volume` con el que anotaste al principio. Una bajada de **8 a 15 dB** es un buen
resultado. Menos de 5 dB, el filtro no está haciendo nada útil. Más de 20 dB, revisa que no hayas
destruido la voz.

---

## Errores comunes

- **Usar `arnndn` sin bajar el `mix`.** Voz de robot. 0,85 es el valor por defecto que deberías tener en
  la cabeza, no 1,0.
- **Poner `arnndn` sobre música.** Le arranca los instrumentos. La red solo sabe de voz.
- **Gate con ratio muy alto.** Los silencios quedan *absolutamente* vacíos y eso suena peor que el ruido.
  Ratio 3–4.
- **Gate con release corto.** Corta las colas de las palabras. Mínimo 200 ms.
- **Olvidar `adeclick` antes del compresor.** Un chasquido le hunde el volumen a una frase entera.
- **No medir el antes.** Sin el número inicial no sabes si mejoraste o si solo te acostumbraste.
- **Correr el filtro varias veces "para que quede más limpio".** Cada pasada agrega artefactos. Una vez,
  bien configurada.
- **Atacar hum de 60 Hz con reducción de ruido.** Es una frecuencia pura; se quita con EQ estrecho.
- **Trabajar a 44,1 kHz con `arnndn`.** El modelo espera 48 kHz. Convierte antes.
- **Prometer que "en posproducción se arregla".** El cuarto con eco y el audio saturado no se arreglan.
  Dilo antes de grabar, no después.

---

## Checklist

- [ ] Escuché 5 s de silencio de la toma y **clasifiqué el tipo de ruido**.
- [ ] Medí el **piso de ruido antes** con `volumedetect` y anoté el número.
- [ ] El audio está a **48 kHz** antes de pasarle `arnndn`.
- [ ] Bajé el modelo `.rnnn` de **GregorR/rnnoise-models** y la ruta del `m=` es correcta.
- [ ] El `mix` está entre **0,80 y 0,95**, elegido a propósito según el material.
- [ ] `arnndn` va **antes** de `afftdn`, no al revés.
- [ ] `afftdn` tiene **`tn=1`** para seguir el ruido variable.
- [ ] El gate tiene **attack corto (5–15 ms) y release largo (200–400 ms)**.
- [ ] El gate tiene **ratio moderado (3–4)**, no infinito.
- [ ] Corrí **`adeclick`** si oí chasquidos de boca, y va antes del compresor.
- [ ] Si había hum, lo ataqué con **EQ estrecho en 60/120/180 Hz**, no con reducción de ruido.
- [ ] Medí el **piso de ruido después**: bajó entre 8 y 15 dB.
- [ ] Escuché la voz sola: **no suena metálica, no "burbujea", no tiene cola de robot**.
- [ ] Escuché los **silencios**: bajaron pero no quedaron muertos.
- [ ] Si limpié a fondo, **reinyecté ambiente** a −45 dB por debajo.
- [ ] Si el material no tiene arreglo, **lo dije** en vez de entregar una voz plástica.
