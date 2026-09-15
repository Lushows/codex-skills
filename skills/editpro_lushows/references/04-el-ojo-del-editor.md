# 04 — El ojo del editor

Resuelve el salto entre "sé qué botones apretar" y "sé si esto está bien". El ojo de editor no es un
don: es un conjunto de ejercicios que se hacen a propósito y que aíslan un canal a la vez para poder
juzgarlo. Este módulo tiene los seis que más rápido cambian el criterio.

---

## Por qué hay que aislar los canales

Cuando ves un video normal, tu cerebro mezcla imagen, sonido, texto y ritmo en una sola impresión:
"me gustó" o "no me gustó". Esa impresión no es accionable — no te dice qué arreglar.

Los ejercicios de este módulo hacen lo mismo que un mecánico cuando desconecta cables uno por uno:
apagan un canal para poder oír el otro. Cada uno responde una pregunta distinta.

| Ejercicio | Pregunta que responde |
|---|---|
| Mirar sin sonido | ¿se entiende visualmente? ¿el texto carga el mensaje? |
| Escuchar sin mirar | ¿la voz fluye? ¿hay baches? ¿la música tapa? |
| Contar cortes | ¿el ritmo es el que creo que es? |
| El test del pulgar | ¿el gancho aguanta el primer segundo? |
| El test del parpadeo | ¿estoy cortando donde el cerebro quiere cortar? |
| La hoja de contactos | ¿qué hay realmente en el material? |

---

## Ejercicio 1 — Mirar sin sonido

**Cómo se hace:** reproduce el video con el volumen en cero, de principio a fin, sin pausar.

**Qué buscas:**

1. ¿Se entiende de qué se trata? Si a los 5 segundos no sabes de qué es el video, tu público tampoco.
2. ¿El texto en pantalla carga el mensaje completo o solo lo decora?
3. ¿Hay algún plano que se quede quieto demasiado tiempo? Sin sonido, los planos muertos se vuelven
   evidentes — con sonido los tapa la voz.
4. ¿Se ve el producto/la cara/lo importante, o está sepultado?

**Por qué importa tanto:** esto no es un ejercicio académico. **Es como se ve tu video en la vida real.**
La mayoría del consumo de video vertical ocurre con el sonido apagado: en el bus, en una reunión, en la
cama al lado de alguien dormido. El video mudo no es un caso extremo, es el caso normal.

**Regla que sale de aquí:** si el video mudo no comunica el mensaje entero, el problema no es el
sonido — es que el texto en pantalla no está haciendo su trabajo. Ver `40`.

**Versión extrema y muy útil:** mira solo los primeros 3 segundos, mudos, y pregúntate si tú te
quedarías. Si dudas, el gancho está débil.

---

## Ejercicio 2 — Escuchar sin mirar

**Cómo se hace:** dale play y voltea la pantalla, o cierra los ojos. Solo audio, de principio a fin.

**Qué buscas:**

1. **Palabras partidas.** El error #1 del montaje rápido. Sin la imagen distrayendo, se oyen de
   inmediato: "...necesito saber cuánto me cues— *corte* —y por eso".
2. **Baches de silencio.** Tres segundos sin nada suenan larguísimos cuando no hay imagen que los tape.
3. **Saltos de nivel.** Que un clip suene más duro que el siguiente. Sin imagen es obvio; con imagen se
   perdona.
4. **Cambios de ambiente.** El zumbido de fondo que cambia en cada corte y delata que son grabaciones
   distintas. Se arregla con un lecho de ambiente continuo (ver `77`).
5. **La música tapando la voz.** Si tienes que esforzarte para entender una palabra, el ducking está
   mal calibrado (`75`).

**Lo que puede hacer un modelo aquí:** no oye, pero puede hacer lo equivalente y más exacto —
transcribir el audio del render final con timecodes y comparar contra el guion. Una palabra partida
aparece en la transcripción como una palabra incompleta o una palabra inventada por el transcriptor.
Ese es el método real, y está en `98`.

Y para los silencios, esto los detecta sin oír nada:

```bash
ffmpeg -hide_banner -i corte_final.mp4 -af silencedetect=noise=-35dB:d=0.8 -f null -
```

Devuelve `silence_start` y `silence_end` de cada tramo de más de 0,8 s por debajo de -35 dB. Si aparece
un silencio de 4 segundos en el segundo 31, ahí tienes tu bache — sin haber oído nada.

---

## Ejercicio 3 — Contar cortes

**Cómo se hace:** cuenta cuántos cambios visuales hay y divide entre la duración. El resultado es tu
**ritmo**, en cambios por segundo.

**Por qué es revelador:** casi nadie acierta contando de memoria. La gente dice "esto va rapidísimo" y
al medirlo son 0,3 cambios por segundo. La percepción de ritmo depende del contenido, no solo del
número — pero el número es el punto de partida objetivo.

**A mano:** dale play y marca con un golpe en la mesa cada cambio. Cuenta los golpes.

**Medido, que es mejor:**

```bash
# Lista los cambios de escena detectados con su timestamp
ffmpeg -hide_banner -i video.mp4 -filter:v "select='gt(scene,0.25)',showinfo" -f null - 2>&1 \
  | grep -o "pts_time:[0-9.]*"
```

El umbral `0.25` detecta cambios claros. Súbelo a `0.4` si tienes mucho movimiento de cámara (te va a
dar falsos positivos), bájalo a `0.15` si los cortes son entre planos muy parecidos.

**Referencias de ritmo (agosto 2026):**

| Formato | Cambios por segundo | Duración media de plano |
|---|---|---|
| Reel / TikTok de ritmo alto | 0,7 – 1,0 | 1,0 – 1,4 s |
| Reel / TikTok estándar | 0,5 – 0,7 | 1,5 – 2,0 s |
| Anuncio de Meta | 0,5 – 0,8 | 1,2 – 2,0 s |
| Talking head con b-roll | 0,3 – 0,5 | 2,0 – 3,5 s |
| Documental / entrevista | 0,15 – 0,3 | 3,5 – 7 s |
| Cine contemporáneo de acción | 0,3 – 0,5 | 2 – 3 s |

**Cuidado con el uso mecánico de esto.** El número te dice si estás fuera del rango, no si el video es
bueno. Sally Menke sostiene planos de minutos y funciona. El número sirve para diagnosticar el "se
siente lento" — si estás en 0,2 en un reel, ya sabes por dónde empezar. Ver `20`, `27`.

---

## Ejercicio 4 — El test del pulgar

**Cómo se hace:** mira el video en el teléfono, en la aplicación real donde va a vivir (o al menos a
tamaño real, vertical, en la mano). Deja el pulgar apoyado sobre la pantalla, como cuando estás
scrolleando de verdad. **Y sé honesto contigo mismo sobre en qué segundo lo habrías pasado.**

**Qué mide:** la única métrica que importa antes de publicar. No "¿está bien montado?" sino "¿me
quedaría yo?".

**Cómo se hace bien:**

1. Déjalo reposar. Un video que acabas de montar no lo puedes juzgar: llevas dos horas viéndolo y ya
   sabes lo que viene. Espera unas horas o hasta el día siguiente.
2. Míralo en medio de otros videos, no aislado. Si puedes, súbelo como borrador y velo en el feed
   entre contenido ajeno. Ahí es donde compite de verdad.
3. Anota **el segundo exacto** donde el dedo se te movió. Ese es tu punto de fuga.

**Qué hacer con el resultado:**

| Se cayó en... | Casi siempre es |
|---|---|
| Segundo 0–1 | el gancho no entrega nada; anuncia en vez de mostrar (`30`) |
| Segundo 2–4 | hay introducción/presentación que sobra; empieza más adelante |
| Segundo 5–10 | el bucle no se abrió: no hay razón para seguir (`31`) |
| Mitad del video | plano muerto o repetición; falta un giro (`39`) |
| Justo antes del final | el remate se ve venir y no promete nada nuevo (`33`) |

**Regla práctica que sale de aquí:** cuando el test del pulgar falla en el segundo 2–4, la solución
casi nunca es agregar algo. Es **borrar el principio**. Empieza el video donde se te fue el dedo menos.

**Honestidad obligatoria:** un modelo no puede hacer este test. Puede analizar los primeros fotogramas,
medir cuándo aparece el primer texto, comprobar si el producto se ve antes del segundo 3 — pero el
"¿me quedaría?" es del humano. Dilo así de claro.

---

## Ejercicio 5 — El test del parpadeo (Murch)

**Cómo se hace:** mira el material en bruto sin sonido, con la persona hablando, y **anota dónde
parpadea**.

**Qué descubres:** los parpadeos no son aleatorios. La gente parpadea al terminar de procesar una idea
— es un corte que hace el cerebro. Walter Murch construyó buena parte de su método observando esto
(ver `03`).

**Cómo se usa:** los parpadeos son candidatos naturales de punto de corte. Cortar ahí se siente
invisible; cortar a mitad de un pensamiento se siente brusco aunque el audio esté limpio.

**Prueba directa que puedes hacer hoy:** toma un talking head, marca tres parpadeos, corta en esos tres
puntos, y compara contra tres cortes puestos donde cae bien el ritmo del audio. El primero se siente
más natural casi siempre.

**Limitación honesta:** en material de una sola toma corta esto funciona muy bien. En material muy
picado o con la persona leyendo un teleprompter (que reduce el parpadeo natural), funciona menos.

---

## Ejercicio 6 — La hoja de contactos

**Cómo se hace:** convierte todo el video en una sola imagen con muchos fotogramas en cuadrícula. Se
llama hoja de contactos por analogía con la fotografía analógica, donde se imprimía el rollo entero en
una hoja para elegir cuáles ampliar.

```bash
# 1 fotograma cada 2 segundos, en cuadrícula de 6 columnas, cada uno de 320 px de ancho
ffmpeg -hide_banner -i bruto.mp4 -vf "fps=1/2,scale=320:-1,tile=6x8" -frames:v 1 contactos.png
```

Si el clip es más largo, saca varias hojas:

```bash
ffmpeg -hide_banner -i bruto.mp4 -vf "fps=1/2,scale=320:-1,tile=6x8" contactos_%03d.png
```

**Qué te da en 10 segundos de mirada:**

- dónde cambia la escena y dónde no pasa nada;
- si hay planos quemados, oscuros o desenfocados;
- si la persona está encuadrada igual en todo o si el encuadre baila;
- si hay material repetido que creías distinto;
- si hay un plano bueno que no recordabas.

**Por qué es el ejercicio más rentable para un modelo:** es la forma de "ver" 10 minutos de video en
una sola imagen, sin reproducir nada. Es el paso 1 real de la lectura del material. Ver `17`.

---

## El orden en que se hacen

No son seis ejercicios sueltos: tienen un momento en el proceso.

| Fase del montaje | Ejercicio que aplica |
|---|---|
| Lectura del material bruto | hoja de contactos (6), test del parpadeo (5) |
| Corte bruto armado | contar cortes (3) |
| Corte fino cerrado | mirar sin sonido (1), escuchar sin mirar (2) |
| Antes de entregar | test del pulgar (4), y otra vez el (1) |

El (1) y el (2) se hacen **siempre** antes de entregar. Los otros según la fase.

---

## Cómo se entrena esto en 20 minutos al día

El ojo se entrena viendo trabajo ajeno con método, no viendo tutoriales.

1. **Toma un anuncio que te haya frenado el dedo.** Uno real, de esta semana, en tu feed.
2. **Hoja de contactos mental:** ¿cuántos planos distintos tiene? ¿de qué tipo?
3. **Míralo mudo.** ¿Se entiende? ¿el texto carga el mensaje?
4. **Cuenta los cortes** y saca cambios por segundo.
5. **Encuentra el gancho:** ¿qué pasa exactamente en el primer segundo?
6. **Encuentra el bucle:** ¿qué pregunta te dejaron abierta y dónde la cerraron?
7. **Escribe una frase** sobre qué hace bien y una sobre qué le sobra.

Siete pasos, cinco minutos por video. Cuatro videos al día. En dos semanas tu criterio no se parece al
de hace dos semanas.

---

## Lo que un modelo sí puede juzgar y lo que no

Vale la pena tenerlo separado, porque es la diferencia entre ser útil y ser un charlatán:

| Puede | No puede |
|---|---|
| Extraer y mirar fotogramas uno por uno | Ver el video reproduciéndose |
| Leer un espectrograma y detectar zumbido, golpes, saturación | Oír si una voz "suena bien" |
| Transcribir con timecodes y detectar palabras partidas | Juzgar si el chiste da risa |
| Medir LUFS, picos, duración, resolución, fps | Sentir si el ritmo "fluye" |
| Contar cortes y calcular ritmo | Hacer el test del pulgar |
| Detectar silencios, negros, congelados, saturación | Decidir si la música va con la marca |
| Verificar zona segura midiendo píxeles | Evaluar el gusto |

La columna izquierda caza la mayoría de los errores reales de un montaje. La derecha es del humano, y
se dice explícitamente en cada entrega.

---

## Errores comunes

- **Juzgar un video recién montado.** Llevas horas viéndolo, ya sabes lo que viene y no puedes
  sorprenderte. Déjalo reposar.
- **Mirarlo siempre con sonido.** Es la condición menos frecuente de consumo real.
- **Mirarlo siempre en el computador a pantalla grande.** Vive en un teléfono, en la mano, entre otros
  videos.
- **Contar cortes de memoria.** La percepción miente; el comando no.
- **Usar el ritmo como regla mecánica.** El número diagnostica, no decide.
- **Hacer el test del pulgar solo y aislado.** Sin competencia alrededor, todo aguanta.
- **Ignorar el segundo exacto donde se te fue el dedo.** Ese dato vale más que toda la opinión posterior.
- **Saltarse la hoja de contactos porque "ya vi el material".** Verlo corriendo y verlo en cuadrícula
  muestran cosas distintas.
- **Fingir haber hecho un ejercicio que requiere oír o ver corriendo.** Se declara y se le pasa al humano.
- **Buscar el problema en el ritmo cuando el video mudo no se entiende.** Ese es problema de texto y
  de estructura, no de velocidad.

---

## Checklist

Antes de dar por bueno cualquier corte:

- [ ] Lo vi **completo y mudo**, y el mensaje se entiende sin sonido.
- [ ] En los primeros 3 segundos mudos hay algo que justifica quedarse.
- [ ] Revisé el audio aislado (o transcribí el render) y ninguna palabra queda partida.
- [ ] Corrí `silencedetect` y no hay baches involuntarios de más de 1 s.
- [ ] Conté los cortes de verdad (comando, no memoria) y el ritmo está en el rango del formato.
- [ ] Hice la hoja de contactos del bruto antes de decidir la estructura.
- [ ] Probé cortar en los parpadeos del talking head y comparé.
- [ ] Hice el test del pulgar en el teléfono, con el video reposado, entre otro contenido.
- [ ] Anoté el segundo exacto donde se me fue el dedo y actué sobre eso.
- [ ] Declaré explícitamente qué de esto no pude juzgar yo y se lo dejé al humano.
