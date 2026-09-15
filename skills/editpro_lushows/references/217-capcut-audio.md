# 217 — Audio en CapCut: limpiar la voz, separar pistas y editar al beat

La gente perdona una imagen mediocre. No perdona un audio malo. Un video con imagen fea y sonido
limpio se ve amateur; uno con imagen linda y sonido saturado se apaga a los tres segundos.

CapCut es sorprendentemente bueno en la parte de **limpiar y separar**, y bastante pobre en la parte
de **mezclar fino**. Este módulo te dice cómo exprimir lo primero y cómo compensar lo segundo.

Dato de tus proyectos: 50 pistas de audio en 51 proyectos. Prácticamente todos llevan al menos una
pista de audio propia (música o voz separada de la imagen). Ese es el flujo correcto.

---

## Lo primero: separar el audio del video

Clic derecho sobre el clip → **Separar audio** (o `Ctrl + Alt + S`).

El audio baja a su propia pista. **Hacé esto siempre, apenas empezás.** Razones:

- Podés cortar la imagen sin cortar el sonido, y viceversa. Eso habilita los cortes en J y en L (el
  audio entra antes que la imagen, o sigue después), que son la base de un montaje que fluye.
- Podés ajustar el volumen de la voz independiente del video.
- Podés borrar el video y quedarte con el audio (útil para dejar que una voz cargue sobre planos de
  recurso).

Si no separás el audio, estás editando con las manos atadas.

---

## Limpiar la voz: las tres herramientas

Seleccioná el clip de audio → panel derecho.

### 1. Reducir ruido

Un interruptor, a veces con niveles (bajo / medio / alto).

- **Qué quita bien:** zumbido constante, aire acondicionado, ventilador, ruido de fondo parejo,
  hiss del micrófono.
- **Qué no quita:** ruidos puntuales (una puerta, un carro que pasa, un grito de fondo).
- **El costo:** cuanto más agresivo, más se come el cuerpo de la voz. Se vuelve delgada, con un
  fondo "de agua". Si la voz suena procesada, bajale.

**Regla:** empezá en el nivel más bajo que sirva. Si con el nivel bajo ya no se oye el ruido, no
subas más.

### 2. Mejorar voz / Realce de voz

Es un procesado con IA que sube la claridad de las frecuencias del habla, controla el volumen y baja
lo demás.

- **Cuándo brilla:** audio de celular, grabado a distancia, en ambiente con eco.
- **Cuándo lo arruina:** audio ya bueno de micrófono decente. Le mete un carácter procesado
  innecesario. **Si grabaste con buen micro, no lo actives.**
- **Ojo con la música:** si el clip tiene música de fondo, "mejorar voz" la va a deformar. Bajo un
  clip con música ambiente, suena raro.

### 3. Aislamiento de voz

Separa la voz de todo lo demás usando redes neuronales. La versión de 2026 (a veces llamada
*Speech Isolation 2.0*) es una de las mejores cosas que le pasaron a CapCut: **reconstruye
frecuencias de voz** en vez de solo filtrar.

Se usa clic derecho sobre el clip → *Aislamiento de voz* / *Separar voz*, y te da opciones tipo
**Conservar voz** o **Quitar voz**.

Casos reales:

- **Grabaste en un local con música puesta.** Aislás la voz, y ponés tu propia música encima. Salva
  material que antes era inutilizable, y de paso te salva de un reclamo de derechos por la música que
  sonaba de fondo.
- **Querés el instrumental de una canción.** *Quitar voz* te deja la pista.
- **Querés solo el acapella.** *Conservar voz*.

Advertencias honestas:

- **Se procesa en la nube.** Necesitás internet y tu audio sube a servidores de ByteDance.
- **Deja artefactos.** Con música fuerte, la voz aislada queda con un halo metálico. Aceptable para
  redes, no para un comercial de TV.
- **Tarda.** En clips largos, minutos.
- **No hace milagros con varias voces encimadas.**

### El orden correcto

Si vas a usar más de una:

> **Aislar voz → Reducir ruido (suave) → Mejorar voz (solo si hace falta) → Volumen**

Y en cada paso, escuchá. El error clásico es apilar los tres al máximo y terminar con una voz que
suena a robot bajo el agua.

---

## Volumen y mezcla

### Los niveles que funcionan

CapCut no tiene medidor de LUFS, así que vas a trabajar de oído y con la forma de onda. Referencias
prácticas:

| Elemento | Nivel relativo |
|---|---|
| **Voz principal** | La referencia. Que la forma de onda llene bien sin tocar el techo. |
| **Música bajo la voz** | Entre 15 y 25 % del volumen de la voz |
| **Música sola (sin voz)** | 60–80 % |
| **Efectos de sonido** | Que se noten sin tapar la voz |
| **Ambiente** | Muy bajo, 10–15 % |

**La regla de la voz:** si tenés que esforzarte para entender una palabra, la música está muy alta.
Escuchalo en el parlante del celular, no en audífonos. Ahí es donde se va a consumir.

### El fundido de entrada y salida

Cada clip de audio tiene tiradores de fundido en las esquinas superiores. Arrastralos.

**Ponele fundido a todo.** Un corte de música seco suena a error. 0,3 a 1 segundo de fundido en cada
extremo y suena intencional.

### Ducking

CapCut tiene un ducking automático (bajar la música cuando hay voz). Está en el clip de música,
suele llamarse *Reducción automática* o *Ducking*.

Funciona, pero:
- **A veces bombea** (la música sube y baja de forma audible, "respirando").
- **No controlás bien el ataque ni la recuperación.**

Si suena raro, hacelo a mano con keyframes de volumen (módulo 213):

- 0,3 s antes de la voz: 100 %
- Al empezar la voz: 25 %
- Al terminar: 25 %
- 0,5 s después: 100 %

Cuatro keyframes por bloque de voz, curva lineal. Se oye mejor y controlás todo.

---

## La biblioteca de sonidos

Pestaña **Audio** → **Efectos de sonido** y **Música**.

### Efectos de sonido: el recurso más subestimado

Categorías útiles: transiciones (whoosh), impactos, interfaz (clic, pop), ambientes, cómicos.

**Por qué importan tanto:** un corte con un *whoosh* de 4 fotogramas se siente mil veces mejor que el
mismo corte en silencio. El sonido hace la transición, no el efecto visual.

Los cinco que resuelven casi todo:
1. **Whoosh** — para cortes y movimientos de cámara.
2. **Impacto / boom** — para golpes, revelaciones, datos duros.
3. **Pop / clic** — para textos que aparecen.
4. **Riser** — un sonido que sube, para generar expectativa antes de un momento.
5. **Silencio** — no es un efecto, es una decisión. Cortar todo el sonido medio segundo antes de algo
   importante es el recurso más poderoso que existe y no cuesta nada.

Volumen de los efectos: suelen venir muy altos. Bajalos al 30–50 % casi siempre.

### Música: la advertencia legal

CapCut te ofrece una biblioteca grande de música. **No toda es libre para uso comercial.**

Lo importante:
- **Tener Pro no es una licencia universal.** Los recursos están licenciados **uno por uno**.
- Muchas pistas están licenciadas solo para publicar **en TikTok**, no en YouTube, no en un anuncio
  pago, no en un video de cliente.
- Un reclamo de derechos en un anuncio pago te tumba la campaña y te puede costar la cuenta
  publicitaria.

**Regla para trabajo de cliente:** música de una biblioteca con licencia clara (Epidemic Sound,
Artlist, Musicbed) o generada (módulo 123). La biblioteca de CapCut, solo para contenido orgánico
propio y revisando la letra chica de cada pista.

---

## Sincronizar al beat

Acá es donde CapCut te da una ventaja real.

### Marcadores automáticos de beat

Seleccioná el clip de música → panel derecho → **Ritmo** / **Beat**. Activás *Marcar ritmo
automáticamente* y CapCut te pone puntos amarillos sobre la forma de onda, en los golpes.

Después:
- Los clips **se imantan a esos marcadores** cuando los arrastrás.
- Podés cortar exactamente en el beat.
- Podés poner los efectos y los textos justo ahí.

Es una función excelente. Con música de beat marcado (electrónica, reggaetón, hip hop) acierta casi
siempre. Con música orgánica o con tempo variable, falla y te toca a mano.

### Marcadores a mano

Poné la cabeza lectora donde oís el golpe y presioná **M**. Se pone un marcador.

El truco real para hacerlo rápido: **reproducí la música y presioná M al ritmo, como si tocaras una
batería.** En una pasada tenés todos los golpes. Después ajustás los que quedaron corridos.

### La regla de edición al beat

No cortes en **todos** los beats. Eso es agotador.

- Cortá en el **primer tiempo de cada compás** (cada 4 beats) para el ritmo base.
- Cortá en **cada beat** solo en tramos cortos de alta energía.
- Dejá **un tramo largo sin cortar** justo antes de un momento importante. El contraste es lo que da
  impacto.

---

## Lo que CapCut NO hace en audio

- **No hay medidor de LUFS.** Estás exportando sin saber tu loudness real. Las plataformas normalizan
  a ~-14 LUFS y si estás muy por debajo, tu video suena más bajo que el del vecino.
- **No hay EQ paramétrico.** Hay presets de ecualización, no bandas ajustables.
- **No hay compresor con controles.** No podés ajustar umbral, ratio, ataque, release.
- **No hay de-esser** (quitar las eses sibilantes).
- **No hay reverb de calidad** ni control de espacio.
- **No hay mezclador multipista** con faders y buses.
- **No hay grabación multipista** decente dentro del editor.

**El apaño para el loudness:** exportá el video de CapCut y pasá el audio por ffmpeg con `loudnorm`
apuntando a -14 LUFS (ver módulo 103). Es un comando, tarda segundos, y hace que tu contenido suene
a la par del resto de la plataforma. Es la mejora de audio con mejor relación esfuerzo/resultado que
existe.

---

## Errores comunes

- **No separar el audio del video al empezar.** Te deja sin cortes en J y L, y sin control
  independiente. Es el primer paso, siempre.
- **Apilar reducir ruido + mejorar voz + aislamiento al máximo.** La voz queda a robot bajo el agua.
  Uno a la vez, en el nivel mínimo que sirva.
- **Usar "mejorar voz" en audio ya bueno.** Le mete carácter procesado sin necesidad.
- **Mezclar con audífonos y no revisar en el parlante del celular.** El 90 % de tu audiencia va a oír
  esto en un parlante malo. Si ahí no se entiende, no se entiende.
- **Música demasiado alta bajo la voz.** El error más común de todos. Si tenés que esforzarte para
  entender una palabra, bajala.
- **Cortes de música secos.** Ponele fundido a todo, 0,3 a 1 segundo.
- **Confiar en el ducking automático sin escucharlo.** A veces bombea de forma muy audible.
- **Usar música de la biblioteca de CapCut en un anuncio pago o trabajo de cliente.** Riesgo real de
  reclamo. Pro no es licencia universal.
- **Efectos de sonido al 100 %.** Vienen muy altos. Bajalos al 30–50 %.
- **Cortar en todos los beats.** Agota. Cortá en el primer tiempo del compás y guardá los cortes
  densos para los momentos altos.
- **Exportar sin normalizar el loudness.** Tu video va a sonar más bajo que el de al lado en el feed.
- **Olvidar que aislar voz y mejorar voz suben tu material a la nube.** Con material de cliente
  confidencial, es una decisión, no un detalle.

---

## Checklist

- [ ] Separé el audio del video en el primer minuto del proyecto.
- [ ] Usé la mínima cantidad de procesamiento de voz posible.
- [ ] Escuché la voz procesada aislada, buscando que no suene metálica.
- [ ] La música está entre 15 y 25 % del volumen de la voz cuando hay voz.
- [ ] Todos los clips de audio tienen fundido de entrada y salida.
- [ ] Si el ducking automático bombea, lo hice a mano con keyframes.
- [ ] Los efectos de sonido están bajados al 30–50 %.
- [ ] Hay al menos un *whoosh* o impacto acompañando los cortes importantes.
- [ ] Usé el silencio a propósito al menos una vez.
- [ ] Marqué el ritmo (automático o con **M**) y los cortes principales caen en el beat.
- [ ] No corté en todos los beats; hay contraste de densidad.
- [ ] Verifiqué la licencia de la música si esto es trabajo de cliente o anuncio pago.
- [ ] **Escuché el corte final en el parlante de un celular.**
- [ ] Normalicé el loudness a ~-14 LUFS con ffmpeg antes de publicar.
