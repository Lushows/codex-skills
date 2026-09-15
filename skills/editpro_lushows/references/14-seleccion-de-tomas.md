# 14 — Selección de tomas

## Qué resuelve

Elegir cuál de las veinte veces que alguien dijo lo mismo entra al video. Es la decisión que más define
la calidad final y la que menos gente toma con criterio: lo normal es agarrar la última porque "esa fue
la que quedó" y seguir.

El número que hay que interiorizar viene de un proyecto real: **16 clips, 10 minutos de bruto, 28 tomas
falsas y 6 tomas buenas, para 60 segundos de video.** Eso significa que el 83% de los intentos grabados
no sirven como toma principal, y que las seis que sirven hay que elegirlas bien porque no hay más.

**Toma** = un intento continuo de decir o hacer algo, desde que arranca hasta que se corta.
**Toma falsa** = el intento que se rompió: se equivocó, se rió, se le olvidó, lo interrumpieron.

---

## La primera regla: la última suele ser la mejor, pero no siempre

En un rodaje la gente mejora con la repetición. Para la toma 5 ya no está leyendo mentalmente el guion,
ya sabe dónde va la pausa, ya no mira al techo. Por eso la heurística por defecto es **empezar mirando
la última toma completa**.

Pero hay tres casos frecuentes donde la última es peor, y por eso la heurística no puede ser una regla:

1. **Se sobre-ensayó.** A partir de la toma 8 o 9 la energía cae y la frase suena recitada. La toma 3
   tenía la chispa. Esto es lo más común en gente que no es actor.
2. **Se cansó la voz o cambió la luz.** En rodajes largos la toma 12 puede tener la mejor actuación y el
   peor audio, o una luz distinta a la del resto del video (problema de continuidad, ver módulo 26).
3. **La versión pulida perdió lo específico.** Es el caso del módulo 12: la toma 1 decía "esto nos costó
   catorce meses, fue horrible" y la toma 5 decía "el desarrollo tomó poco más de un año". La segunda
   está mejor dicha y no sirve para nada.

Conclusión operativa: **empieza por la última, pero compara siempre con al menos dos anteriores.**

---

## Los siete criterios, en orden de importancia

Se evalúan en este orden. Si falla uno de los tres primeros, la toma está fuera aunque brille en los
demás.

| # | Criterio | Pregunta | Elimina si |
|---|---|---|---|
| 1 | **Contenido** | ¿dice lo que tiene que decir, completo y correcto? | falta información, dato equivocado |
| 2 | **Audio** | ¿se entiende cada palabra sin esfuerzo? | saturado, tapado, ruido encima de la frase clave |
| 3 | **Frase entera** | ¿empieza y termina sin que la corten? | arranca a mitad, o se pisa con la siguiente |
| 4 | **Energía** | ¿suena a alguien que cree lo que dice? | plano, recitado, sin aire |
| 5 | **Mirada y postura** | ¿está presente, o buscando el guion? | ojos arriba, cuerpo rígido |
| 6 | **Imagen** | ¿encuadre, foco y luz sirven? | movido, desenfocado, contraluz |
| 7 | **Continuidad** | ¿pega con las tomas vecinas? | ropa distinta, luz distinta, fondo cambiado |

**Por qué el audio va tan arriba:** un plano feo se disimula (punch-in, b-roll encima, texto). Un audio
malo no se disimula: la gente se va. En video corto, el audio es el criterio que más elimina.

---

## El método: descartar, no elegir

Elegir entre veinte es difícil. Descartar entre veinte es fácil. Trabaja siempre por eliminación en
pasadas, cada una más cara que la anterior.

### Pasada A — Automática (segundos)

De la transcripción del módulo 13 ya tienes las marcas. Todo lo que sea `>>TOMA FALSA` queda fuera de la
selección principal (pero **no se borra**: va al catálogo de bloopers, módulo 18).

De 34 intentos quedan 6. Ya hiciste el 80% del trabajo sin abrir un reproductor.

### Pasada B — Por texto (minutos)

Lee las 6 tomas buenas en la transcripción, sin video. Aplica criterios 1 y 3: ¿dice lo que toca?
¿está completa? Aquí suelen caer una o dos más.

Este es el momento de comparar versiones. Ponlas lado a lado literalmente:

```markdown
## Bloque: "de que esta hecha la botella"

TOMA A — clip-03, seg 12.4-19.8 (7.4 s)
"Esta hecha de vidrio reciclado, que conseguimos con un proveedor de Bogota."

TOMA B — clip-03, seg 44.1-49.9 (5.8 s)
"Vidrio reciclado. Todo. Cada botella fue otra botella antes."

DECISION: B. Mas corta, mas concreta, la ultima frase funciona sola como titular.
Riesgo: no menciona el proveedor. Si el cliente lo exige, va A.
```

Escribir la decisión con su motivo es lo que hace que no la reabras tres veces.

### Pasada C — Por audio (minutos)

Escucha solo las finalistas. Extrae cada una a un mp3 corto:

```bash
ffmpeg -y -ss 44.1 -i entrada/clip-03.mp4 -to 49.9 -vn -ac 1 -ar 16000 -c:a libmp3lame trabajo/cand-03-44.mp3
```

Ojo: con `-ss` **antes** de `-i`, el `-to` se interpreta como tiempo absoluto del archivo original en
ffmpeg moderno; si te da un fragmento de la longitud equivocada, usa `-t` (duración) en vez de `-to`:

```bash
ffmpeg -y -ss 44.1 -i entrada/clip-03.mp4 -t 5.8 -vn -ac 1 -ar 16000 -c:a libmp3lame trabajo/cand-03-44.mp3
```

Aquí aplicas criterio 2 (audio) y 4 (energía). La energía se juzga mejor con los ojos cerrados: si la
frase te convence solo con el sonido, va a funcionar.

### Pasada D — Por video (la más cara, la más corta)

Ahora sí miras. Solo las finalistas, solo su tramo. Criterios 5, 6 y 7.

```bash
ffmpeg -y -ss 44.1 -i entrada/clip-03.mp4 -t 5.8 -c:v libx264 -crf 20 -c:a aac trabajo/cand-03-44.mp4
```

De 34 intentos llegaste a mirar 4 fragmentos de 6 segundos. Eso es 24 segundos de video visto para tomar
la decisión más importante del montaje.

---

## Extraer todas las candidatas de un golpe

Con una tabla de candidatas en CSV (`clip,inicio,duracion,etiqueta`), este script te deja todos los
fragmentos listos para comparar:

```powershell
$proyecto = "C:\Users\user\Desktop\VIDEO-BOTELLA"
$csv = Import-Csv (Join-Path $proyecto "analisis\candidatas.csv")
$dest = Join-Path $proyecto "trabajo\candidatas"
New-Item -ItemType Directory -Force -Path $dest | Out-Null

foreach ($f in $csv) {
  $src = Join-Path $proyecto ("entrada\" + $f.clip)
  $dur = [double](& ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 $src)
  $fin = [double]$f.inicio + [double]$f.duracion

  if ($fin -gt $dur) {
    Write-Output ("SALTADA {0}: pide hasta {1} s pero el clip dura {2} s" -f $f.etiqueta, [math]::Round($fin,2), [math]::Round($dur,2))
    continue
  }

  $out = Join-Path $dest ("{0}.mp4" -f $f.etiqueta)
  & ffmpeg -y -hide_banner -loglevel error -ss $f.inicio -i $src -t $f.duracion -c:v libx264 -crf 20 -preset veryfast -c:a aac -b:a 128k $out
  Write-Output ("OK {0} -> {1}" -f $f.etiqueta, $out)
}
```

Fíjate en la comprobación de duración antes de cortar. Es la misma lección del módulo 11: **nunca pidas
un tramo sin haber comprobado que existe.** Aquí el script simplemente salta y te avisa, en vez de
producir un archivo silenciosamente roto.

---

## El caso de la toma Frankenstein

A veces ninguna toma es buena entera, pero la primera mitad de la toma 2 y la segunda mitad de la toma 5
juntas son perfectas. Eso se llama armar una toma Frankenstein y **es legítimo**, con dos condiciones:

1. **El corte va en una pausa respiratoria**, nunca a mitad de palabra ni a mitad de aliento.
2. **La imagen tapa el salto**: b-roll encima, punch-in, o un cambio de plano justo ahí. Si dejas el
   mismo encuadre, se ve un salto que la gente registra aunque no sepa nombrarlo (ver `21-tipos-de-corte`
   y `23-voz-continua-imagen-picada`).

Si el tono de voz o el volumen cambian mucho entre las dos mitades, no se puede: se oye como dos personas.

---

## Cuántas tomas necesitas de verdad

Para un video de 60 segundos con estructura de 6 a 8 bloques (módulo 19):

| Bloque | Tomas principales necesarias | Respaldo deseable |
|---|---|---|
| Gancho | 1 | 2 alternativas |
| Cuerpo (4–6 bloques) | 1 cada uno | 1 alternativa en los 2 más importantes |
| Remate | 1 | 1 alternativa |
| B-roll | 3–5 planos mudos | — |

Con 6 tomas buenas y 28 falsas, el proyecto real quedaba justo. Eso significa que **no había margen**: si
una de las 6 hubiera tenido audio saturado, tocaba regrabar. Es información que hay que darle al cliente
el mismo día, no la víspera de la entrega.

Esta es también la razón del módulo 170 (`briefing-de-rodaje-desde-la-edicion`): en el próximo rodaje se
pide explícitamente **tres tomas buenas de cada bloque clave**, y se revisan en sitio.

---

## La ficha de selección

El entregable de este módulo es una tabla que se va directo al mapa de bloques (módulo 19):

```csv
bloque,clip,inicio,fin,duracion,motivo,alternativa
gancho,clip-12,24.9,33.1,8.2,"version mas concreta de la piedra",clip-12@9.1
material,clip-03,44.1,49.9,5.8,"corta y titular",clip-03@12.4
proceso,clip-07,8.0,14.6,6.6,"unica completa con audio limpio",ninguna
remate,clip-15,31.2,36.0,4.8,"cierra con sonrisa",clip-15@18.7
```

La columna `alternativa` es la que salva el proyecto cuando el cliente dice "esa frase no la puedo decir
por temas legales" el día antes de publicar.

---

## Errores comunes

- **Quedarse con la última toma por defecto.** Es un buen punto de partida, no una decisión. Compara
  siempre con dos anteriores.
- **Elegir la toma mejor dicha en vez de la mejor contada.** La versión pulida suele haber perdido el
  dato concreto que hacía interesante la frase.
- **Empezar mirando video.** Es la pasada más cara. Se descarta por texto primero, por audio después, y
  solo se mira lo que sobrevivió.
- **Borrar las tomas falsas.** Son el material de bloopers (módulo 18) y a veces contienen la mejor
  explicación del video. Se apartan, no se botan.
- **Elegir sin escribir el motivo.** Sin motivo escrito, la decisión se reabre cada vez que alguien la
  cuestiona, y se pierde media hora.
- **No dejar alternativa anotada.** Cuando el cliente veta una frase a última hora, sin alternativa hay
  que rehacer la búsqueda entera.
- **Ignorar la continuidad al elegir.** Una toma perfecta grabada con otra luz obliga a corregir color
  después o a descartarla igual. Mejor verlo al seleccionar.
- **Cortar candidatas sin comprobar la duración del clip.** El error de los 128 s en un clip de 101 s
  aparece justo aquí, al extraer fragmentos en lote.
- **Armar una toma Frankenstein cortando a mitad de palabra.** El corte va en la pausa, y la imagen tiene
  que tapar el salto.
- **Aceptar una toma con audio malo porque "la actuación es buenísima".** Nadie ve un video que no se
  entiende. El audio manda por encima de la actuación.

---

## Checklist

- [ ] Todas las tomas están clasificadas como buenas o falsas a partir de la transcripción marcada
- [ ] Las tomas falsas están apartadas en el catálogo de bloopers, no borradas
- [ ] Sabes el número exacto: cuántas tomas buenas hay para cuántos bloques hacen falta
- [ ] Si no alcanzan, el cliente ya está avisado y hay decisión de regrabar o reestructurar
- [ ] Cada bloque tiene una toma principal elegida, con `clip`, `inicio`, `fin` y `duracion`
- [ ] Cada elección tiene su motivo escrito en una frase
- [ ] Los bloques importantes tienen una alternativa anotada
- [ ] Se compararon las versiones cruda y pulida cuando la persona dijo lo mismo varias veces
- [ ] Las finalistas se escucharon en audio antes de mirarlas en video
- [ ] Se verificó con ffprobe que todos los tramos elegidos caben dentro de su clip
- [ ] Se revisó continuidad (luz, ropa, fondo) entre las tomas elegidas de bloques vecinos
- [ ] Si hay tomas Frankenstein, el corte cae en pausa y hay plan de imagen para taparlo
- [ ] La ficha de selección está guardada en `analisis/` y lista para el mapa de bloques
