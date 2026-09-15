# 77 — Sonido real vs efecto de biblioteca

Hay un momento en el que un editor deja de ser aprendiz: cuando apaga la música y escucha lo que el
material ya traía.

La mayoría de la gente hace lo contrario. Graba, mete la voz en off, le pone una música épica, tapa el
audio original con "silenciar pista" y le agrega tres whooshes de biblioteca. Y el resultado es un video
que se ve bien y que **suena a stock**. A cualquiera. A ninguna parte.

Este módulo es sobre la decisión más importante del audio de una pieza: **cuándo el sonido que ya está
ahí vale más que cualquier cosa que le puedas agregar.**

---

## El ejemplo que resuelve el módulo

Estás editando un video de una cervecería. El plano: una cerveza cayendo en un vaso, la espuma
subiendo, el vaso llenándose. Cuatro segundos.

**Opción A.** Silencias el audio original, pones música energética con un beat fuerte, y un "whoosh"
cuando entra el plano.

**Opción B.** Bajas la música a −24 dB, subes el audio original, y dejas que se oiga **el chorro**. El
líquido cayendo, el sonido cambiando a medida que el vaso se llena, la espuma crepitando arriba.

La opción B gana. Siempre. Y no por poquito.

**Por qué:** el chorro de una cerveza cayendo es un sonido que la gente conoce con el cuerpo. No lo
"reconoce": lo **anticipa**. Sabe cómo va a cambiar el tono cuando el vaso se llene, sabe cómo suena la
espuma. Cuando lo oye, activa memoria sensorial: sed, frío, el bar, el viernes. Ningún efecto de
biblioteca —ni un whoosh, ni un impacto, ni la mejor música— hace eso, porque ninguno tiene el vínculo
directo con la experiencia física.

En publicidad de comida y bebida esto tiene nombre desde hace décadas: **el sonido de la venta**. El
"crunch" de una papa, el "tsss" de una lata que se abre, el sonido del aceite cuando cae la carne al
sartén, el "clack" de la tapa de una botella. Las agencias grandes contratan gente solo para eso, y en
sesiones de foley graban el sonido veinte veces hasta que queda perfecto. No es un adorno: **es el
argumento de venta**, dicho con sonido en vez de con palabras.

---

## Cuándo el sonido real gana

Hay un patrón. El sonido del material gana cuando cumple alguna de estas condiciones:

### 1. Es la prueba de una sensación física
Comida, bebida, textura, temperatura. Todo lo que el cuerpo conoce.

- El chorro de cerveza cayendo
- El crujido de un pan al partirse
- El aceite chisporroteando
- El hielo cayendo en un vaso
- El sonido de una tela buena al moverse
- Una máquina de café presurizando

En estos casos el sonido **es más persuasivo que la imagen**, porque la imagen se puede fingir con
retoque y el sonido no.

### 2. Es la prueba de que algo es real
Un testimonio, una reacción, un momento no guionizado.

- La risa espontánea de alguien
- El ruido de la calle detrás de una entrevista
- El sonido de un taller mientras alguien trabaja
- La respiración de alguien que está nervioso antes de hablar

Aquí el sonido es **el certificado de autenticidad**. Un testimonio grabado con audio de estudio y
música bonita suena a actor. El mismo testimonio con el ruido de fondo de su local suena a persona.

### 3. Es un sonido característico e irrepetible
El sonido específico de ese negocio, esa máquina, ese lugar.

- La campana de un restaurante cuando sale un plato
- El motor de una moto específica
- El "clonk" particular de una puerta vieja
- La caja registradora de un local de barrio

Este es el que más se desperdicia. Es el sonido que hace que el video sea de **ese** negocio y no de
cualquiera.

### 4. Marca un ritmo mejor que la música
A veces el material trae su propio pulso: alguien picando cebolla, una máquina repetitiva, pasos. Cortar
al ritmo de ese sonido —y dejarlo oír— es más interesante que ponerle un beat encima.

---

## Cuándo el efecto de biblioteca gana

Sé honesto en las dos direcciones. El efecto gana cuando:

- **El sonido real no existe.** Una transición gráfica, un texto que entra, un logo que aparece. No hay
  sonido "real" de eso. Ver `76`.
- **El sonido real es malo.** Se grabó con viento encima, con el micro saturado, o con alguien tosiendo
  detrás. A veces el material sí es irrecuperable.
- **El sonido real es aburrido.** No todo sonido real es interesante. El zumbido de una nevera es real y
  no aporta nada.
- **Se necesita algo más grande que la realidad.** Un impacto de tráiler, una explosión estilizada. El
  sonido real de una puerta cerrándose no tiene el peso dramático que a veces quieres.
- **Hay que uniformar.** Si tienes 6 planos grabados en 6 sitios con 6 ambientes distintos y los cortas
  seguidos, el cambio de ambiente en cada corte es más molesto que un ambiente sintético parejo.

**La regla que resume las dos listas:** el sonido real gana cuando el sonido **es información sobre lo
que estás mostrando**. El efecto gana cuando el sonido **es información sobre el montaje** (una
transición, un énfasis, un cambio de sección).

---

## Cómo sacarle provecho al audio del material

### Primero: escúchalo

Suena obvio y casi nadie lo hace. Antes de silenciar una pista, escúchala sola, con audífonos, sin
imagen.

```bash
# extraer el audio de un clip para escucharlo aparte
ffmpeg -i clip_cerveza.mp4 -vn -c:a pcm_s16le -ar 48000 audio_clip.wav

# ver la forma de onda para ubicar los momentos con contenido
ffmpeg -i audio_clip.wav -filter_complex "showwavespic=s=1920x400:colors=lime" -frames:v 1 onda.png
```

En la forma de onda vas a ver dónde está el sonido bueno. Casi siempre hay un pico que no habías notado.

### Segundo: aíslalo y súbelo

El sonido bueno suele estar enterrado bajo ruido y a un nivel bajo. Hay que sacarlo:

```bash
# aislar el tramo del chorro (del segundo 3,2 al 7,4), limpiarlo suave y subirlo
ffmpeg -i audio_clip.wav -ss 3.2 -t 4.2 \
  -af "highpass=f=120,afftdn=nf=-30:tn=1,volume=8dB,alimiter=limit=0.9" \
  -c:a pcm_s16le chorro.wav
```

Ojo con la limpieza: **a un sonido real hay que limpiarlo con muchísimo menos mano que a una voz.** Si
le metes `arnndn` al chorro de una cerveza, el modelo —entrenado en voz— va a interpretar el líquido
como ruido y te lo va a borrar. Usa `afftdn` suave y un `highpass`, nada más.

### Tercero: dale espacio

Un sonido real solo funciona si se oye. Y solo se oye si algo se aparta.

```bash
# el chorro entra en el segundo 8,0 del video; la música se aparta
ffmpeg -i mezcla_base.wav -i chorro.wav \
  -filter_complex "[1]adelay=8000|8000,volume=-2dB[fx];[0][fx]amix=inputs=2:duration=first:dropout_transition=0[out]" \
  -map "[out]" mezcla_con_chorro.wav
```

Mejor todavía: usa el propio sonido real como disparador de ducking sobre la música (mismo principio
de `75`):

```bash
ffmpeg -i musica.wav -i chorro_en_su_lugar.wav \
  -filter_complex "[0][1]sidechaincompress=threshold=0.03:ratio=10:attack=10:release=350[out]" \
  -map "[out]" musica_que_se_aparta.wav
```

Y a veces lo mejor es lo más simple: **quitar la música durante esos 4 segundos.** El chorro solo, en
silencio, con la imagen. Eso es lujo.

```bash
ffmpeg -i musica.wav -af "volume='if(between(t,7.8,12.4),0,1)':eval=frame,afade=t=in:st=12.4:d=0.4" musica_hueco.wav
```

### Cuarto: exagéralo un poco

El micrófono de la cámara está a 1,5 metros. El oído de la persona en el video estaría a 30 cm. Subir
el sonido más de lo "realista" no es hacer trampa: es corregir la distancia.

Y ecualizarlo también ayuda. Un chorro de líquido vive en 2–8 kHz; realzar ahí lo hace más apetitoso:

```bash
ffmpeg -i chorro.wav -af "equalizer=f=4000:t=q:w=1.0:g=4,equalizer=f=8000:t=q:w=1.2:g=3,volume=3dB" chorro_rico.wav
```

Para un crujido (pan, papa, fritura), la banda clave es más arriba: 4–10 kHz. Para un golpe o algo
pesado, abajo: 60–150 Hz.

---

## El ambiente: el sonido real que nadie nota y todos extrañan

Aparte de los sonidos protagonistas, está el **ambiente**: el sonido de fondo del lugar. La gente lejana
en un restaurante, el tráfico suave de una calle, el zumbido de un taller.

Casi todo el mundo lo borra. Y borrarlo es un error, porque el ambiente hace tres cosas:

1. **Le dice al oído dónde está.** Un video sin ambiente flota en el vacío.
2. **Pega los cortes.** Si pones un ambiente continuo debajo de todo el video, los cortes entre planos
   dejan de sonar a cortes. Es el pegamento invisible del montaje.
3. **Vuelve creíble la voz limpia.** Ese es el `mix=0.85` de `71` llevado a su conclusión.

**La técnica del lecho de ambiente:**

```bash
# 1) sacar 20-30 s de ambiente limpio del propio material (donde nadie hable)
ffmpeg -i clip_local.mp4 -vn -ss 00:00:41 -t 25 -af "highpass=f=60,volume=-30dB" ambiente.wav

# 2) hacerlo loop para cubrir todo el video y ponerlo debajo de la mezcla
ffmpeg -i mezcla.wav -stream_loop -1 -i ambiente.wav \
  -filter_complex "[0][1]amix=inputs=2:duration=first:dropout_transition=0:weights=1 0.35[out]" \
  -map "[out]" mezcla_con_ambiente.wav
```

`weights=1 0.35` pone el ambiente al 35% del peso de la mezcla — bien abajo, apenas presente.

**El nivel correcto del ambiente es aquel en el que, si lo quitas, se nota que falta algo, pero cuando
está no lo oyes.** Típicamente −35 a −45 dB. Si lo oyes conscientemente, está muy fuerte.

**Grábalo siempre.** Al terminar de rodar en cualquier sitio, pide silencio y graba 60 segundos del
lugar quieto. Se llama "room tone" y es la cosa más útil que puedes traer de un rodaje. Cuesta un minuto
y salva mezclas enteras.

---

## Cómo decidir en la práctica: el orden de preguntas

Frente a cada plano, en este orden:

1. **¿El material trae un sonido que aporta?** Si sí → úsalo, súbelo, dale espacio.
2. **¿Ese sonido es la prueba de algo (textura, autenticidad, identidad)?** Si sí → es protagonista.
   Baja la música o quítala.
3. **¿Necesito marcar algo del montaje (transición, énfasis, sección)?** Si sí → ahí va el efecto de
   biblioteca (`76`).
4. **¿Tengo ambiente debajo de todo el video?** Si no → ponlo.

Ese orden es el módulo entero. Sonido real primero, efecto después, ambiente siempre.

---

## Un caso de negocio, completo

Video de 25 s de una cervecería. Planos: local, barril, cerveza cayendo, gente brindando, logo.

**Lo que hace la mayoría:** silenciar todo, música energética a volumen pleno, whoosh en cada corte,
impacto en el logo. Resultado: se ve bien, suena a plantilla.

**Lo que hay que hacer:**

```bash
# 1) ambiente del local, loop, debajo de todo (−38 dB)
ffmpeg -i local.mp4 -vn -ss 20 -t 25 -af "highpass=f=60,volume=-38dB" ambiente.wav

# 2) el chorro de cerveza, aislado, limpio y realzado (protagonista, segundos 9-13)
ffmpeg -i cerveza.mp4 -vn -ss 2.1 -t 4.0 \
  -af "highpass=f=120,afftdn=nf=-30:tn=1,equalizer=f=4000:t=q:w=1.0:g=4,equalizer=f=8000:t=q:w=1.2:g=3,volume=6dB,alimiter=limit=0.9" \
  chorro.wav

# 3) el brindis real (segundos 17-19)
ffmpeg -i brindis.mp4 -vn -ss 1.4 -t 2.0 -af "highpass=f=100,volume=4dB" brindis.wav

# 4) la música se abre entre 8,8 y 13,2 (el chorro manda) y vuelve
ffmpeg -i musica.wav -af "volume='if(between(t,8.8,13.2),0.15,1)':eval=frame" musica_abierta.wav

# 5) mezclar todo + impacto solo en el logo (segundo 22)
ffmpeg -i musica_abierta.wav -i chorro.wav -i brindis.wav -i impacto.wav -stream_loop -1 -i ambiente.wav \
  -filter_complex "\
[1]adelay=9000|9000[c]; \
[2]adelay=17000|17000,volume=-4dB[b]; \
[3]adelay=22000|22000,volume=-6dB[i]; \
[0][c][b][i][4]amix=inputs=5:duration=first:dropout_transition=0:weights=1 1 1 1 0.3,alimiter=limit=0.9[out]" \
-map "[out]" mezcla.wav

# 6) normalizar
ffmpeg -i mezcla.wav -af "loudnorm=I=-14:TP=-1.5:LRA=11" audio_final.wav
```

Un solo efecto de biblioteca en todo el video (el impacto del logo). El resto es sonido que ya existía.
Y suena a **esa** cervecería.

---

## Errores comunes

- **Silenciar el audio original por costumbre.** Es el error madre. Escúchalo antes de botarlo.
- **Tapar el sonido protagonista con música.** Si el chorro es el argumento de venta, la música se
  aparta o se va.
- **Limpiar un sonido real como si fuera voz.** `arnndn` te borra el líquido, el crujido y el fuego
  porque no son voz. Para sonido real: `highpass` + `afftdn` suave y ya.
- **No grabar room tone.** Un minuto en el rodaje te ahorra horas en la mezcla.
- **Video sin lecho de ambiente.** Los cortes suenan a cortes y todo flota en el vacío.
- **Ambiente demasiado fuerte.** Si lo oyes conscientemente, está 6 dB arriba.
- **Creer que "realista" significa "al volumen que lo grabó el micro".** El micro estaba a 1,5 m; el
  oído del espectador debería estar a 30 cm. Súbelo.
- **No ecualizar el sonido real.** Un chorro con +4 dB en 4 kHz es apetitoso; sin eso es un ruido de
  agua.
- **Efecto de biblioteca donde había sonido real.** Un whoosh sobre un plano de alguien caminando cuando
  los pasos ya estaban grabados.
- **Sonido real donde no aporta.** El zumbido de la nevera es real y no significa nada. No todo lo real
  sirve.
- **No cortar los ambientes distintos entre planos.** Seis planos con seis ambientes distintos suenan a
  seis videos pegados. Ahí sí toca uniformar.

---

## Checklist

- [ ] **Escuché el audio original de cada clip** antes de decidir silenciarlo.
- [ ] Identifiqué si hay un **sonido protagonista** (textura, autenticidad, identidad del negocio).
- [ ] Ese sonido está **aislado, limpio con mano suave, ecualizado y subido**.
- [ ] La música **se aparta o se va** durante el sonido protagonista.
- [ ] La limpieza del sonido real fue con **`highpass` + `afftdn` suave**, no con `arnndn`.
- [ ] Realcé la banda que le da carácter (4–8 kHz para líquido, 4–10 kHz para crujido, 60–150 Hz para
      peso).
- [ ] Hay un **lecho de ambiente** debajo de todo el video, a −35/−45 dB.
- [ ] El ambiente **no se oye conscientemente**, pero si lo quito se nota que falta.
- [ ] Si los planos vienen de sitios muy distintos, **uniformé el ambiente** para que los cortes no
      salten.
- [ ] Los efectos de biblioteca están solo donde **no hay sonido real posible** (transiciones, gráficos,
      logo).
- [ ] En el rodaje **grabé 60 s de room tone** del sitio.
- [ ] Escuché la mezcla final **sin mirar la pantalla**: ¿suena a este negocio o suena a cualquier video?
