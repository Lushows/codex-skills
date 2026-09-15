# 08 — Presentar y defender un corte

Resuelve el momento donde se pierde más trabajo del oficio: **la entrega.** Un montaje bueno mal
presentado recibe notas destructivas; un montaje regular bien presentado recibe notas útiles. Y una
nota vaga sin traducir produce tres rondas de cambios al azar.

---

## Principio 1 — Nunca mandes un video solo

Un archivo suelto en el chat obliga a la otra persona a inventarse el criterio con el que va a
juzgarlo. Y el criterio que se inventa siempre es "¿me gusta?", que es la pregunta menos útil posible.

**El mensaje que acompaña al video hace tres cosas:**

1. Recuerda cuál era el objetivo (el del brief, `02`).
2. Nombra las decisiones importantes y por qué.
3. Dice exactamente qué tipo de nota necesitas.

Ejemplo real de mensaje de entrega:

> **Reel calculadora — corte 1** (22 s, 9:16)
>
> Objetivo del brief: que escriban al WhatsApp.
>
> Tres decisiones que quiero que veas:
> 1. Arranca con la frase del minuto 1:52 de tu grabación, no con la presentación. Esa frase abre una
>    pregunta y la presentación no.
> 2. No digo el precio hasta el segundo 16, después de que ya se entendió el problema.
> 3. El remate es una sola acción y sin logo encima, para que la última imagen sea la instrucción.
>
> Lo que necesito de ti: si el ángulo es el correcto y si la frase del arranque te representa. **No
> me des notas de color ni de tipografía todavía** — eso lo cerramos en la ronda 2, cuando el corte
> esté aprobado.

Fíjate en la última línea. **Acotar el tipo de nota es la mitad del trabajo.** Si no lo haces, en la
ronda 1 te van a hablar de la fuente y del color y nadie va a haber juzgado la estructura, que es lo
único que se puede cambiar barato en esa etapa.

---

## Principio 2 — Muestra un corte, no tres opciones

La tentación es dar a elegir. No lo hagas.

**Por qué falla:** tres opciones convierten al cliente en editor. Va a mezclar ("me gusta el arranque
de la 1 con el final de la 3"), y esa mezcla casi nunca funciona porque las piezas estaban construidas
con lógicas distintas. Además le quitas la señal más valiosa que puedes darle: tu criterio.

**Lo que sí se hace:** un corte, defendido, y una mención de lo que descartaste y por qué.

> Probé también arrancar con el plano del restaurante lleno. No lo dejé porque tarda 2 segundos en
> decir algo y el ángulo se pierde. Si quieres lo montamos, pero creo que baja retención.

Eso da la sensación de opciones sin los costos de las opciones.

**La excepción legítima:** cuando el destino es pauta y el plan explícito es testear variantes. Ahí no
son "opciones para que elijas": son variantes para que el mercado decida. Se presentan como tal, con la
hipótesis de cada una. Ver `159`.

---

## Principio 3 — Muéstralo donde va a vivir

Mandar un MP4 por correo para que lo vean en un monitor de 27 pulgadas cuando el video va a Reels
produce notas equivocadas. En pantalla grande se ven cosas que en el teléfono no existen (un poro de
la piel, una imperfección del fondo) y no se ven las que sí importan (que el texto queda debajo de la
interfaz).

**Lo correcto:**

- Manda el archivo por WhatsApp o el medio donde lo vayan a abrir en el teléfono.
- Si puedes, súbelo como borrador en la cuenta real y manda el enlace.
- Si tiene que ser por computador, manda además una captura con las zonas seguras dibujadas.

```bash
# Genera una vista previa con la zona segura de Reels marcada, para revisar en escritorio
ffmpeg -i corte_v1.mp4 -vf "drawbox=x=0:y=0:w=iw:h=220:color=red@0.25:t=fill,\
drawbox=x=0:y=ih-420:w=iw:h=420:color=red@0.25:t=fill" \
-c:v libx264 -crf 20 -c:a copy corte_v1_zonasegura.mp4
```

Las bandas rojas marcan lo que la interfaz de la aplicación va a tapar. Nadie discute con una banda
roja encima del texto. Los valores exactos por plataforma están en `45`.

---

## Principio 4 — Defiende con una frase, no con herramientas

Ya está en `00`, pero aquí es donde se aplica de verdad.

| No digas | Di |
|---|---|
| "Le puse un jump cut" | "Corté ahí para que no se note que dudó" |
| "Hice un punch-in del 35%" | "Me acerco cuando dice el precio, para que no se pierda" |
| "Metí un J-cut de 0,4 s" | "El sonido del siguiente plano entra antes para que el cambio no golpee" |
| "Apliqué un duotono con la paleta" | "Forcé tus colores en los planos que venían de otra fuente" |
| "Bajé a -14 LUFS" | "Lo dejé al volumen que Instagram espera, para que no suene más bajo que los demás" |

**La prueba:** si en tu defensa aparece el nombre de una herramienta, el cliente va a discutir la
herramienta. Si aparece el efecto sobre el espectador, va a discutir el efecto — que es la conversación
correcta.

La parte técnica no desaparece: va en la sección de verificación del mensaje, aparte, con números.

---

## Principio 5 — Traduce las notas vagas antes de tocar nada

Aquí está el 80% del valor de este módulo.

Cuando llega "no me gusta", **no toques nada.** Una nota vaga ejecutada al azar consume una ronda y no
resuelve el problema real, porque el problema real sigue sin nombrarse.

### La tabla de traducción

| Lo que dicen | Lo que suele significar | Qué preguntar / qué revisar |
|---|---|---|
| "No me gusta" | no sabe qué le molesta, algo lo incomoda | "¿En qué segundo te bajó el interés?" |
| "Está muy lento" | 0,2 cambios/s, o el gancho no abrió nada | mide el ritmo (`20`) **y** revisa el gancho (`30`) |
| "Falta algo" | falta un plano de contexto, o falta remate | "¿Al final te quedaste esperando algo?" |
| "No se ve profesional" | audio malo, color disparejo o texto de plantilla | revisa en ese orden: `70` → `62` → `44` |
| "Muy largo" | se cayó el interés en algún punto, no la duración | "¿Dónde te empezó a parecer largo?" — recorta ahí, no al final |
| "No me representa" | el tono de voz o el ángulo del brief | vuelve al brief (`02`); esto es un problema de brief, no de montaje |
| "Ponle más energía" | ritmo bajo, música plana, o falta variación | `20`, `74`, y romper el patrón (`06`) |
| "Está muy comercial" | CTA muy temprano o demasiada marca | mueve el CTA al final, quita el logo del cuerpo |
| "La música no va" | tono equivocado, o tapa la voz | primero revisa ducking (`75`); si está bien, es gusto → que elija él |
| "El texto no se lee" | tamaño, contraste, tiempo en pantalla o zona segura | `44`, `45`, `46` — los cuatro se miden |
| "Se ve raro ahí" | casi siempre un raccord roto o un cruce de eje | `05` |
| "A mi esposa no le gustó" | apareció un opinador nuevo | vuelve a `02`: ¿quién aprueba? |

### Las tres preguntas que desatascan casi todo

Cuando la nota es vaga, estas tres traducen mejor que cualquier interrogatorio:

1. **"¿En qué segundo exactamente?"** — Convierte una impresión global en un punto concreto. La mitad
   de las veces la persona descubre al buscarlo que el problema era solo un momento.
2. **"¿Qué sentiste ahí: aburrimiento, confusión o incomodidad?"** — Las tres tienen curas distintas.
   Aburrimiento = ritmo. Confusión = estructura o texto. Incomodidad = tono o algo que chirría.
3. **"Muéstrame un video que sí te guste."** — La comparación desbloquea lo que las palabras no. Y te
   deja algo medible: puedes contar sus cortes y comparar.

### La regla de no ejecutar a ciegas

Si después de las tres preguntas la nota sigue sin traducirse, **dilo**:

> No logro convertir "no me gusta" en un cambio concreto. Si toco cosas al azar gastamos una ronda y
> probablemente no resuelva. ¿Te muestro tres versiones de 5 segundos del arranque para que me digas
> cuál se acerca?

Eso es honesto, y es más rápido que adivinar.

---

## Principio 6 — Separa lo que es criterio de lo que es gusto

Hay dos tipos de nota y se responden distinto:

**Notas de criterio** — tienen respuesta correcta, medible:

- "El texto no se lee" → se mide y se arregla. No se discute.
- "Se oye bajito" → LUFS. No se discute.
- "El texto queda tapado por el botón" → zona segura. No se discute.

**Notas de gusto** — no tienen respuesta correcta:

- "No me gusta esa canción."
- "Prefiero que se vea más cálido."
- "Ese chiste no me convence."

**En las de gusto, el cliente gana.** Es su marca y su plata. Tu trabajo es advertir si el gusto choca
con el objetivo ("esa canción funciona, solo ten en cuenta que baja la energía en el arranque"), y
después ejecutar sin resentimiento.

**En las de criterio, tú tienes la razón y la sostienes con el número.** Pero se sostiene una vez, con
educación y con dato. Si el cliente insiste después del dato, se hace lo que pide y se deja constancia:

> Lo bajo a como lo quieres. Solo te dejo por escrito que a ese nivel Instagram va a normalizar y se
> va a oír más bajo que los videos de al lado.

Eso no es pelear: es dejar el registro. Cuando el resultado confirme el dato, la ronda siguiente será
más fácil.

---

## Principio 7 — Las rondas se acuerdan antes, no durante

El estándar razonable es **dos rondas de notas incluidas**:

| Ronda | De qué se habla | Qué está congelado |
|---|---|---|
| **Ronda 1** | estructura, ángulo, qué entra y qué sale, duración | nada |
| **Ronda 2** | acabado: texto, color, música, ritmo fino | la estructura |
| **Ronda 3+** | se cobra aparte | todo |

**Por qué el orden importa:** cambiar la estructura después de haber puesto texto y color significa
rehacer las fases 5, 6 y 7 completas (ver `07`). Por eso la ronda 1 tiene que ser explícitamente de
estructura, y hay que **prohibir activamente** las notas de acabado en esa ronda.

**Cómo se dice sin sonar rígido:**

> En esta ronda solo necesito que valides la estructura y el ángulo. La tipografía, el color y la
> música los cerramos en la siguiente — si los cambiamos ahora y después movemos un corte, hay que
> rehacerlos.

**Cuando se pasa de la ronda 2:** no se pelea, se cotiza. "Con gusto, esto ya es ronda 3; son X. ¿Lo
hacemos?" Ver `182` y `180`.

---

## Principio 8 — Recoge las notas por escrito y en un solo lote

Notas por audio de WhatsApp, a lo largo de tres días, de dos personas distintas, es como se pierden
proyectos.

**Lo que se pide:** todas las notas juntas, escritas, con el segundo al que se refieren.

Formato que puedes mandarles:

```
segundo 3   - el arranque me gusta
segundo 8   - aqui me perdi, no entendi que es la calculadora
segundo 14  - muy rapido el texto, no alcance a leer
segundo 20  - el precio deberia salir mas grande
general     - la musica muy fuerte
```

Si te mandan un audio de tres minutos, transcríbelo tú y devuélveselo en ese formato para que confirme:
"Entendí esto, ¿es correcto?". Confirmar antes de ejecutar evita rehacer.

---

## El mensaje de entrega completo

La plantilla, con las tres partes obligatorias del cierre de esta skill:

```
PIEZA: reel calculadora - angulo plato que da perdida - corte 2
DURACION: 22 s | 1080x1920 | 30 fps

QUE CAMBIE DESDE LA VERSION ANTERIOR
- arranque nuevo con la frase del min 1:52 (antes empezaba con la presentacion)
- corte el tramo del segundo 9 al 12: repetia la idea anterior
- el precio ahora sale en pantalla, no solo dicho

QUE VERIFIQUE
- 22,4 s reales, 1080x1920, 30 fps, H.264 alto perfil
- -14,1 LUFS integrados, pico real -1,3 dBTP (norma de Instagram)
- transcribi el render final: ninguna palabra queda partida
- todo el texto dentro de la zona segura de Reels (margen de 96 px al borde mas cercano)
- primer fotograma con imagen completa, no negro

QUE NO PUEDO JUZGAR YO
- si la cancion va con el tono de la marca
- si la frase del arranque te representa
- si el chiste del segundo 15 funciona con tu publico

QUE NECESITO DE TI EN ESTA RONDA
- solo estructura y angulo. Color y tipografia van en la ronda 2.
```

---

## Errores comunes

- **Mandar el video sin mensaje.** Obliga al cliente a juzgar con la pregunta "¿me gusta?".
- **No acotar el tipo de nota.** En la ronda 1 te hablan de la fuente y nadie valida la estructura.
- **Mandar tres opciones.** Convierte al cliente en editor y produce mezclas que no funcionan.
- **Mostrar el video en pantalla grande cuando vive en un teléfono.** Genera notas irrelevantes y
  esconde las relevantes.
- **Defender un corte nombrando herramientas.** Traslada la discusión al terreno equivocado.
- **Ejecutar "no me gusta" sin traducirlo.** Gasta una ronda entera y no resuelve.
- **Recortar el final cuando dicen "muy largo".** Casi nunca sobra el final: sobra donde se cayó el
  interés, que suele ser el medio.
- **Discutir una nota de gusto.** Es su marca. Adviertes una vez y ejecutas.
- **Ceder en una nota de criterio sin dejar el dato por escrito.** Después nadie recuerda que avisaste.
- **Aceptar notas de tres personas distintas por canales distintos.** Un lote, escrito, un aprobador.
- **No haber acordado cuántas rondas entran.** Es como llegas a la ronda 6 gratis.
- **Cambiar la estructura en la ronda 2.** Obliga a rehacer sonido, color y gráficos.

---

## Checklist

Antes de mandar un corte:

- [ ] El mensaje recuerda el objetivo del brief.
- [ ] Nombro entre 2 y 4 decisiones importantes y por qué las tomé.
- [ ] Digo explícitamente **qué tipo de nota** necesito en esta ronda.
- [ ] Mando **un** corte, no tres opciones (salvo que sean variantes de pauta declaradas).
- [ ] Menciono qué descarté y por qué.
- [ ] Lo mando por el medio donde lo van a ver en el teléfono, o con zona segura marcada.
- [ ] Las defensas están en efecto sobre el espectador, no en nombres de herramientas.
- [ ] Incluí la sección de verificación con números.
- [ ] Incluí qué **no** pude juzgar yo.

Al recibir notas:

- [ ] No toqué nada antes de traducir la nota a algo concreto.
- [ ] Pregunté el segundo exacto de cada molestia.
- [ ] Pregunté si fue aburrimiento, confusión o incomodidad.
- [ ] Pedí una referencia de algo que sí les guste, si la nota seguía vaga.
- [ ] Separé notas de criterio (se miden) de notas de gusto (manda el cliente).
- [ ] Donde cedí en una nota de criterio, dejé el dato por escrito.
- [ ] Recogí todas las notas en un solo lote escrito y confirmé mi interpretación antes de ejecutar.
- [ ] Verifiqué en qué ronda vamos y si ya se pasó de lo acordado.
