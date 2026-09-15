# 70 — La cadena de voz profesional

La mayoría de la gente cree que "arreglar el audio" es quitarle el ruido. Le pasan un quitaruidos, oyen
que el zumbido del ventilador se fue y dicen "listo". Y el video sigue sonando a aficionado.

La razón es simple y hay que decirla sin rodeos:

> **Limpio no es igual a bueno.** Una voz sin ruido puede seguir sonando lejana, opaca, con las eses
> silbando y con el volumen bailando. El ruido era solo uno de nueve problemas.

Una voz suena profesional cuando pasa por **nueve procesos, en un orden específico**. Ese orden no es
capricho: cada paso le entrega al siguiente un material más limpio para trabajar, y si los inviertes,
uno amplifica la basura del otro. Este módulo es el mapa. Los módulos `71`, `72` y `73` son el detalle.

---

## Los 9 módulos, en orden

```
1. gate               → apaga lo que suena entre frases
2. reducción de ruido → quita el fondo constante (IA: RNNoise / DeepFilterNet)
3. de-reverb          → quita el "eco de cuarto vacío"
4. de-esser           → doma las eses que silban
5. de-click           → borra chasquidos de boca y clics digitales
6. EQ de voz          → esculpe el tono: quita retumbe, sube presencia
7. compresor          → empareja lo suave con lo fuerte
8. normalización LUFS → pone el volumen al estándar de la plataforma
9. limitador          → tapa el techo para que nada sature
```

Léelo así: **primero se quita, después se esculpe, al final se nivela.** Todo lo que resta va antes.
Todo lo que suma o iguala va después.

---

## Qué hace cada uno, en cristiano

### 1. Gate (compuerta)
Un portero. Cuando la voz habla, abre. Cuando la voz calla, cierra y silencia. Sirve para que los
silencios entre frases sean silencios de verdad y no "shhhhh".

**Por qué va primero:** si dejas silencios sucios, el reductor de ruido tiene que trabajar más y el
compresor —que viene después— va a subirle el volumen justo a esa basura. El gate le baja la carga a
todos los demás.

**Cuidado:** un gate muy agresivo se come el final de las palabras. Ver `71`.

### 2. Reducción de ruido con IA
Aquí es donde se va el aire acondicionado, el computador, la calle, el hum eléctrico. La diferencia
entre un quitaruidos viejo y uno de IA es que el de IA **aprendió qué es voz humana**, entonces no
destruye la voz al perseguir el ruido.

En ffmpeg esto es `arnndn` (una red neuronal, RNNoise) y `afftdn` (resta espectral clásica). Se usan
juntos: el de IA hace el trabajo grueso, el clásico limpia el residuo. Ver `71`.

### 3. De-reverb
El eco de la sala. Si grabaste en un cuarto con piso de baldosa y paredes desnudas, tu voz llega dos
veces: directa y rebotada. Eso es lo que hace que suene "lejos" aunque el micrófono estuviera cerca.

**Sé honesto con esto:** ffmpeg **no tiene** un de-reverb de verdad. Lo que hay son parches (un gate
más apretado, un `anlmdn`) y herramientas externas de código abierto como **DeepFilterNet**
(`deep-filter archivo.wav`), que sí ataca reverb además de ruido. Si el material viene con mucho eco,
la solución honesta es **volver a grabar en un sitio con cortinas, ropa o alfombra**. Un cuarto malo
es el único problema de audio que no se arregla del todo en el computador.

### 4. De-esser
Doma las **eses**. La "s", la "ch" y la "z" viven entre 5 y 9 kHz, y con un micrófono cerca de la boca
salen como un silbido que raspa. El de-esser es un compresor que solo actúa cuando aparece esa banda.

**Por qué va acá y no al final:** porque el EQ de presencia (paso 6) y el compresor (paso 7) **suben**
esa zona. Si no domas las eses antes, después las amplificas y quedan peor.

### 5. De-click
Los chasquidos de boca (esos "tk" de saliva entre palabras), los clics digitales de un archivo mal
cortado, los pops de un cable. En ffmpeg: `adeclick` y `adeclip`.

**Por qué acá:** un clic es un pico instantáneo. Si lo dejas pasar al compresor, el compresor lo lee
como "sonido fortísimo" y **le baja el volumen a toda la frase** por culpa de un chasquido de 3 ms.
Un solo clic sin tratar puede hacer que media oración suene con el volumen hundido.

### 6. EQ de voz
Ahora sí se esculpe. Quitas el retumbe de abajo (80–100 Hz para abajo no hay voz, hay golpes de mesa
y pisadas), subes la presencia (1–4 kHz, donde vive la inteligibilidad) y bajas suave por encima de
10 kHz (donde viven la sibilancia y el siseo residual). Valores exactos en `72`.

**Por qué después de limpiar:** ecualizar audio sucio es subirle el volumen a la suciedad. Si realzas
2 kHz en una toma con ruido, realzas el ruido de 2 kHz también.

### 7. Compresor
Empareja. La parte suave sube, la parte fuerte baja, y la voz queda pareja de principio a fin. Es lo
que hace que una voz "se sienta cerca" en un anuncio.

**Por qué después del EQ:** el compresor reacciona al volumen. Si primero le metes +4 dB en presencia,
cambias el volumen que el compresor va a leer. Ecualizar y luego comprimir da un resultado predecible;
al revés, el compresor pelea contra el EQ.

### 8. Normalización LUFS
Poner el promedio de todo el video en el número que la plataforma espera: **−14 LUFS con pico
verdadero a −1,5 dB** para redes. Ver `73` para plataforma por plataforma.

**Por qué casi al final:** LUFS mide el promedio de toda la pieza terminada, con música y todo. Medirlo
antes de comprimir no sirve porque el compresor cambia el promedio.

### 9. Limitador
El seguro. Nada, jamás, pasa del techo. Es la última puerta antes de exportar. En ffmpeg `alimiter`, y
`loudnorm` ya trae uno adentro (por eso el `TP=-1.5`).

---

## Por qué el orden importa (tres ejemplos concretos)

**Comprimir antes de limpiar.** El compresor sube lo bajito. Lo bajito de una toma sucia *es el ruido*.
Resultado: entre frase y frase se oye una marea de "shhhh" que sube y baja. Es el sonido más delator
de un video amateur. Es literalmente el ruido respirando.

**Ecualizar la presencia antes del de-esser.** Subes 1–4 kHz, la "s" ya venía filuda, y ahora tienes
una voz que silba en cada palabra. La gente lo describe como "me molesta oírlo" sin saber por qué.

**Normalizar antes de comprimir.** Normalizas a −14, luego el compresor te mueve el promedio y quedas
en −17. Mediste para nada. La normalización es la penúltima palabra, no la primera.

---

## La cadena real, medida, en un solo comando

Esta cadena se corrió sobre material real y se midió antes y después. No es teoría:

```bash
ffmpeg -i voz_cruda.wav -af "highpass=f=85,arnndn=m='cb.rnnn':mix=0.85,afftdn=nf=-24:tn=1,deesser=i=0.4,acompressor=threshold=-20dB:ratio=3:attack=15:release=180:makeup=2,loudnorm=I=-14:TP=-1.5:LRA=11" -c:a pcm_s16le voz_lista.wav
```

**Resultado medido:**

| Medida | Antes | Después |
|---|---|---|
| Piso de ruido | −17,9 dB | **−30,7 dB** (12,8 dB menos) |
| Pico | 0,0 dB (saturando) | **−2,7 dB** |

Casi 13 dB menos de ruido es una diferencia enorme: el oído percibe unos 10 dB como "la mitad de
fuerte". El fondo pasó de estar presente a estar prácticamente ausente. Y el pico dejó de estar pegado
al techo, que es donde el audio se distorsiona.

Traducción de cada eslabón:

| Trozo del comando | Qué es | Qué hace |
|---|---|---|
| `highpass=f=85` | EQ, pasa-altos | Corta todo debajo de 85 Hz: retumbe, mesa, pisadas |
| `arnndn=m='cb.rnnn':mix=0.85` | Ruido con IA | Quita el fondo constante — al 85%, no al 100% |
| `afftdn=nf=-24:tn=1` | Ruido clásico | Barre el residuo que dejó la IA |
| `deesser=i=0.4` | De-esser | Doma las eses |
| `acompressor=...` | Compresor | Empareja volumen, +2 dB de recuperación |
| `loudnorm=I=-14:TP=-1.5` | LUFS + limitador | Estándar de redes, techo asegurado |

Fíjate que el `highpass` va **al principio** aunque el EQ sea el paso 6. Es la única excepción y tiene
razón de ser: quitar los graves inútiles antes de la reducción de ruido le da al algoritmo menos basura
que analizar y lo hace más preciso. El resto del EQ (presencia, aire) sí va después.

---

## La clave artística: `mix=0.85` y no `1.0`

Esto es lo que separa a alguien que sabe de audio de alguien que solo sabe usar filtros.

`mix=0.85` significa **"aplica el 85% de la limpieza, deja el 15% del original"**. Se hace a propósito.

Cuando limpias una voz al 100%, pasa algo raro: queda perfecta y **queda muerta**. Suena a cabina de
radio flotando en el vacío. El cerebro sabe que ninguna voz humana existe sin un espacio alrededor, y
cuando no oye ese espacio, algo le suena falso aunque no sepa nombrarlo.

Ese 15% de ruido que dejas es **la información de que se grabó en un lugar real**. Es lo mismo que el
grano en una foto de cine: no es un defecto que se te escapó, es la textura que le dice al ojo que eso
existió.

**Regla práctica:**

| Situación | `mix` |
|---|---|
| Voz en cámara, documental, entrevista | 0,80 – 0,85 |
| Voz en off de anuncio, narración limpia | 0,90 – 0,95 |
| Toma desastrosa donde solo importa entender | 1,0 (y asumes que va a sonar plástica) |

Si te toca ir a 1,0, considera **volver a meter un ambiente suave** debajo (ver `77`): grabas 20
segundos del sitio callado y lo pones a −45 dB por debajo de la voz. Suena más real que la voz
esterilizada.

---

## Cómo aplicar esto en la práctica

**Uno: no montes la cadena entera de una.** Aplícala por partes y escucha después de cada paso. Si
metes los nueve filtros de un tiro y suena raro, no vas a saber cuál fue.

```bash
# paso a paso, guardando cada etapa
ffmpeg -i voz_cruda.wav -af "highpass=f=85" p1.wav
ffmpeg -i p1.wav -af "arnndn=m='cb.rnnn':mix=0.85" p2.wav
ffmpeg -i p2.wav -af "afftdn=nf=-24:tn=1" p3.wav
# ...y así
```

**Dos: trabaja en WAV, no en MP3 ni AAC.** Cada vez que reencodas a un formato comprimido pierdes
calidad, y nueve filtros encima de un audio ya degradado suenan a nueve filtros encima de un audio ya
degradado. Extrae el audio del video sin tocarlo, procesa en WAV, y solo al final vuelves a montar:

```bash
# extraer sin recomprimir a WAV de 48 kHz
ffmpeg -i clip.mp4 -vn -c:a pcm_s16le -ar 48000 voz_cruda.wav

# volver a montar el audio procesado sobre el video original, sin tocar el video
ffmpeg -i clip.mp4 -i voz_lista.wav -c:v copy -map 0:v:0 -map 1:a:0 -c:a aac -b:a 192k final.mp4
```

**Tres: compara con A/B honesto.** Escuchar "después" siempre suena mejor porque estás oyendo lo que
querías oír. Pon los dos al mismo volumen antes de comparar, si no el más fuerte siempre "gana".

```bash
# igualar los dos a -14 LUFS para comparar de verdad
ffmpeg -i antes.wav -af loudnorm=I=-14:TP=-1.5 antes_norm.wav
ffmpeg -i despues.wav -af loudnorm=I=-14:TP=-1.5 despues_norm.wav
```

**Cuatro: mide, no adivines.** El piso de ruido se mide así:

```bash
# volumen general y pico
ffmpeg -i archivo.wav -af volumedetect -f null -

# LUFS integrado, pico verdadero y rango dinámico
ffmpeg -i archivo.wav -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=summary -f null -
```

Para el piso de ruido, corta 2 segundos de silencio del material y mídelos:

```bash
ffmpeg -i archivo.wav -ss 00:00:03 -t 2 -af volumedetect -f null -
```

El `mean_volume` de ese trozo es tu piso de ruido. Ese es el número que en el ejemplo pasó de −17,9 a
−30,7.

---

## Cuándo NO usar toda la cadena

- **La toma ya está bien.** Si grabaste con un micro decente en un cuarto tratado, el piso de ruido ya
  está en −55 dB. Meterle nueve filtros solo le va a quitar vida. Un `loudnorm` y ya.
- **Es música, no voz.** Nada de esto aplica a una pista musical. `arnndn` está entrenado en voz humana
  y le hace estragos a un instrumento.
- **Es sonido ambiente que quieres conservar** (ver `77`). El chorro de una cerveza cayendo no necesita
  gate ni de-esser. Necesita que lo dejes en paz.

---

## Errores comunes

- **Creer que quitar el ruido es "arreglar el audio".** Es uno de nueve pasos, y ni siquiera es el que
  más se nota. Una voz limpia pero sin compresión ni LUFS sigue sonando amateur.
- **Poner el compresor antes de la limpieza.** El compresor sube el ruido de los silencios. Es el error
  que produce el "shhh" que respira entre frases.
- **Limpiar al 100%.** Voz de robot en el vacío. Usa `mix=0.85`.
- **Saltarse el de-click.** Un chasquido de 3 ms le hunde el volumen a una frase entera cuando pasa por
  el compresor, y después no entiendes por qué esa oración "suena rara".
- **Ecualizar la presencia antes del de-esser.** Terminas amplificando el silbido que ibas a domar.
- **Normalizar a LUFS y después seguir editando.** La medida se invalida en el momento en que agregas
  música, otro clip o un efecto. LUFS es el penúltimo paso del video **terminado**, no del clip suelto.
- **Procesar en MP3.** Cada pasada recomprime. Trabaja en WAV y comprime una sola vez, al exportar.
- **Comparar sin igualar volumen.** Lo más fuerte siempre suena "mejor". Iguala a −14 y vuelve a juzgar.
- **Aplicar la misma cadena a todos los clips sin pensar.** El clip grabado en la calle y el grabado en
  la oficina no necesitan lo mismo. La cadena es una plantilla, no un botón.
- **Intentar salvar un cuarto con eco en el computador.** El de-reverb tiene un límite real. Cambia el
  sitio de grabación o pon una cobija detrás de la cámara.

---

## Checklist

Antes de dar por terminado el audio de voz de una pieza:

- [ ] Extraje el audio a **WAV 48 kHz**, no trabajé sobre el MP4 comprimido.
- [ ] Medí el **piso de ruido antes** (corte de 2 s de silencio + `volumedetect`) y lo anoté.
- [ ] Apliqué la cadena en **el orden correcto**: quitar → esculpir → nivelar.
- [ ] El `highpass` está en **85 Hz** (o entre 80 y 100 según la voz).
- [ ] El `mix` de `arnndn` está entre **0,80 y 0,95**, nunca en 1,0 sin razón.
- [ ] El **de-esser va antes** del realce de presencia y del compresor.
- [ ] Corrí `adeclick` si oí chasquidos de boca.
- [ ] El compresor está **después** del EQ, no antes.
- [ ] `loudnorm` está en **I=−14, TP=−1,5, LRA=11** (o el valor de la plataforma, ver `73`).
- [ ] Medí el **piso de ruido después** y tengo el número. Debería bajar 8–15 dB.
- [ ] El **pico final no está en 0,0 dB**. Si está, estás saturando.
- [ ] Escuché los **silencios entre frases**: no hay "shhh" que respira.
- [ ] Escuché las **eses**: no silban.
- [ ] Comparé antes/después **igualando volumen**, no a ojo.
- [ ] Escuché el resultado en **parlante de celular**, no solo en audífonos. Ahí es donde lo va a oír
      la gente.
