# 00 — El método del editor

Resuelve la pregunta que está antes de todas las demás: **cómo se decide.** Todo lo técnico de esta
skill (ffmpeg, LUFS, keyframes) es ejecución. Esto es el criterio que gobierna esa ejecución. Si un
módulo técnico contradice algo de aquí, manda este.

---

## 1. La historia manda sobre el efecto

Un corte no se justifica porque quede bonito. Se justifica porque **hace avanzar algo**: la emoción,
la comprensión o el ritmo.

La prueba es de una sola pregunta, y se hace en voz alta antes de tocar el filtro:

> Si quito esto, ¿el video se entiende peor o se siente peor?

Si la respuesta es "no", el efecto sobra. No importa cuánto tiempo te costó hacerlo. Esa es la parte
difícil: lo que más cuesta botar es lo que más trabajo dio.

**Ejemplo real.** En *Lawrence de Arabia* (1962), Anne V. Coates cortó de Lawrence soplando un fósforo
directo al amanecer en el desierto. Un corte duro, sin transición. La razón que ella misma dio años
después es que **no tenían cómo hacer un fundido encadenado** donde estaban rodando — y al verlo con
el corte duro, ni ella ni David Lean quisieron el fundido nunca más. La limitación técnica produjo el
mejor corte de la historia del cine porque el corte duro servía a la historia: el paso del hombre en
una habitación al hombre frente a un desierto inmenso, instantáneo.

Traducido a lo que tú haces: la transición de zoom con blur que trae CapCut por defecto no es "el
recurso profesional". Casi siempre es el relleno que tapa que no sabías por qué estabas cortando ahí.

**Consecuencia práctica:** el 90% de los cortes de un video bueno son cortes duros. Si en tu línea de
tiempo hay una transición cada tres cortes, no estás editando: estás decorando.

---

## 2. Mides, no adivinas

"Creo que ahí corta bien" no es una frase de esta skill. Todo lo que se puede medir, se mide.

| Lo que la gente dice | Lo que se mide en realidad |
|---|---|
| "Se siente lento" | cambios visuales por segundo (ver `20`) |
| "El audio suena bajito" | LUFS integrados del archivo (ver `73`) |
| "Se ve saturado" | histograma y vectorscopio (ver `69`) |
| "Se corta la palabra" | transcripción con timecodes del render final (ver `98`) |
| "El texto no se alcanza a leer" | palabras por golpe y milisegundos en pantalla (ver `46`) |
| "Quedó pesado el archivo" | bitrate real y CRF usado (ver `93`) |

**LUFS** (Loudness Units relative to Full Scale) es la unidad con que las plataformas miden qué tan
fuerte suena un video en promedio, no en su pico. Es la primera vez que aparece en esta biblioteca, así
que queda definida aquí: si tu video sale a -20 LUFS e Instagram normaliza a -14, tu video se va a oír
más bajo que el del vecino aunque tu voz esté "bien grabada".

Comando para medir, no para adivinar:

```bash
ffmpeg -hide_banner -i corte_v3.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=summary -f null -
```

Eso te devuelve `Input Integrated`, `Input True Peak` y `Input LRA`. Tres números. Con tres números
dejas de discutir de gustos y empiezas a discutir de hechos.

**La regla:** cuando alguien te dé una nota subjetiva, tu primer movimiento es convertirla en un número.
Si no se puede convertir en número, se convierte en una comparación ("¿más parecido a este otro video
o menos?"). Lo que nunca se hace es asentir y mover cosas al azar.

---

## 3. Verificas el resultado, no el proceso

Este es el punto donde más trabajo se pierde, y por eso `98-verificacion-del-corte.md` es el módulo
más importante de toda la skill.

**Renderizar no es terminar.** El archivo que salió del render puede tener:

- una palabra partida a la mitad porque el corte cayó 0,2 s antes de tiempo;
- audio saturado porque dos pistas se sumaron;
- el subtítulo del último bloque debajo del botón de "Seguir" de Instagram;
- el logo pegado al borde, que en TikTok queda tapado por la descripción;
- silencio de 8 segundos al final porque el clip de música era más largo;
- rotación invertida porque el celular grabó con metadato `rotate=90` y ffmpeg lo ignoró.

Ninguno de esos se ve mirando la línea de tiempo. Todos se ven **abriendo el archivo final y midiéndolo**.

El flujo correcto es siempre el mismo:

```
montar → renderizar → MEDIR EL RENDER → comparar contra lo esperado → entregar
```

Y "medir el render" significa cosas concretas: extraer fotogramas, transcribir el audio del archivo
final, correr `loudnorm`, revisar duración real. No significa "lo vi y quedó bien".

**Ejemplo de verificación mínima que se hace siempre:**

```bash
# Duración, resolución, fps, códec, rotación real del entregable
ffprobe -v error -show_entries format=duration,size,bit_rate \
  -show_entries stream=codec_name,width,height,r_frame_rate,sample_rate,channels \
  -of default=noprint_wrappers=1 entrega_final.mp4
```

Si ese comando dice `width=1080 height=1920`, `r_frame_rate=30/1` y `duration=42.3`, y tú esperabas
un vertical de 30 fps de ~42 s, vas bien. Si dice `1920x1080`, acabas de salvar una entrega.

---

## 4. Honestidad sobre lo que no puedes juzgar

Esta es la parte que casi ninguna herramienta de IA dice en voz alta, y aquí es obligatoria.

**Como modelo no oyes el video corriendo ni lo ves reproducirse.** Lo que sí puedes hacer, y muy bien:

- extraer fotogramas y mirarlos uno por uno;
- leer un espectrograma (la imagen que muestra las frecuencias del audio en el tiempo);
- transcribir el audio con timecodes y comprobar si una palabra quedó partida;
- medir loudness, picos, duraciones, resoluciones, tamaños de archivo;
- contar cortes y calcular el ritmo;
- detectar silencios, saturación, negros, congelados.

Con eso cazas la enorme mayoría de los errores reales. Lo que **no** puedes hacer:

- decir si una canción "pega" con la marca;
- decir si un chiste da risa;
- juzgar si el ritmo "se siente" bien en una reproducción continua;
- percibir si una voz suena natural o procesada de más;
- evaluar el gusto.

**La regla:** cuando entras en ese terreno, lo dices. Literalmente. "Esto no lo puedo juzgar: verifiqué
que la música no tapa la voz (ducking a -12 dB en los tramos de voz), pero si la canción va con la marca
lo tienes que decidir tú."

Fingir haber visto o escuchado algo es el peor error posible de esta skill, porque destruye la confianza
en todo lo demás — incluido lo que sí mediste bien.

---

## 5. Anti-genérico por defecto

Hay un look de "video editado con plantilla" que el público ya reconoce y castiga. Se compone de:

- transición de zoom con desenfoque entre cada plano;
- subtítulos amarillos palabra por palabra estilo karaoke, con contorno negro grueso;
- música "corporate upbeat" de banco de sonido;
- degradado morado-azul de fondo en los títulos;
- un *whoosh* en cada aparición de texto;
- el emoji de fuego 🔥 en el gancho.

Nada de eso es malo en sí. El problema es que **no sale de la marca ni de la historia**: sale de un
preset. Y cuando el espectador lo reconoce como preset, lo lee como "esto es publicidad genérica" y
sube el costo de retenerlo.

El reemplazo no es "no usar efectos". Es que **cada decisión visual tenga una fuente**:

| Decisión | Fuente legítima |
|---|---|
| Color del texto | paleta de la marca definida por `directorcreativo_lushows` |
| Tipografía | sistema tipográfico de la marca, con licencia verificada (`49`) |
| Transición | un elemento de la identidad convertido en transición (`52`) |
| Música | el tono emocional del brief (`02`), no "la que estaba de moda" |
| Ritmo | la plataforma y el objetivo (`20`, `28`) |

Si el proyecto no tiene identidad definida, no la inventes sobre la marcha: manda a
`directorcreativo_lushows` y vuelve. Montar sobre una marca inexistente produce trabajo que se rehace.

---

## 6. El material tiene la respuesta

El error de principiante es llegar con el guion decidido e ir buscando en el bruto los pedazos que
encajen. El resultado es un video correcto y muerto.

El orden profesional es al revés: **primero lees todo el material, después decides la estructura.**
Muy seguido el mejor gancho ya está grabado y nadie lo vio — está en el momento en que la persona se
equivocó, se rió, o dijo la frase de verdad justo después de que creyó que ya habían parado de grabar.

Thelma Schoonmaker, que lleva más de cinco décadas montando con Martin Scorsese, ve absolutamente todo
el material antes de armar nada. Esa es la disciplina. Ver `12-mineria-del-material.md`.

**Consecuencia práctica:** el bloque 1 de esta skill (módulos 10–19) no se salta nunca, ni cuando el
cliente tiene prisa. Un montaje hecho sin conocer el material se rehace entero, y rehacerlo cuesta más
que haberlo leído.

---

## 7. Un corte se defiende con una frase

Si no puedes explicar por qué cortaste ahí en una sola frase que no mencione herramientas, el corte
está débil.

| Mala defensa | Buena defensa |
|---|---|
| "Le puse un jump cut ahí" | "Corté ahí para que no se note que dudó" |
| "Le metí un punch-in" | "Me acerco cuando dice el precio, para que no se pierda" |
| "Ahí va la música" | "La música entra cuando deja de hablar, para que el silencio no se sienta un bache" |
| "Usé xfade fade 0.3" | "Ese fundido marca que pasó tiempo entre las dos escenas" |

Nota que en la columna buena no aparece ni una herramienta. Las herramientas van en la documentación
técnica, no en la defensa del corte. Ver `08-presentar-y-defender-un-corte.md`.

---

## 8. Terminar es una decisión, no un estado

Un video nunca "queda listo" solo. Siempre hay un corte más que se puede afinar. El editor profesional
se distingue del amateur en que **decide cuándo parar**, y esa decisión tiene criterios:

1. El objetivo del brief está cumplido (ver `02`).
2. La verificación técnica pasa completa (ver `98`).
3. Los últimos tres cambios que hiciste ya no mejoraron nada medible.
4. Llevas más tiempo del presupuestado en cosas que solo tú vas a notar.

Cuando se cumplen los cuatro, se entrega. Seguir puliendo después de eso no es profesionalismo: es
miedo a mostrar. Ver `29-el-corte-final.md`.

---

## 9. El orden de las prioridades cuando hay conflicto

Cuando dos criterios chocan — y chocan todo el tiempo — este es el orden. Está tomado del "orden de
prioridad" de Walter Murch (ver `03-estudiar-a-los-maestros.md`), adaptado a video corto:

1. **Que se sienta algo.** Si el corte técnicamente perfecto mata la emoción, se bota.
2. **Que se entienda.** Un video hermoso que no se entiende no vende nada.
3. **Que fluya.** El ritmo se sacrifica antes que la claridad, nunca al revés.
4. **Que el ojo no se pierda.** A dónde mira el espectador entre un plano y el siguiente.
5. **Que la composición aguante.** El encuadre, la línea del horizonte, la zona segura.
6. **Que la continuidad cierre.** El vaso que estaba lleno y ahora está vacío. Importa, pero es lo
   último. Murch lo puso último a propósito y tenía razón.

En video vertical de 30 segundos, el punto 6 casi nunca importa. En un documental de 40 minutos, sí.
El contexto define cuánto pesan del 4 al 6; del 1 al 3 no se negocian nunca.

---

## Errores comunes

- **Editar antes de haber visto todo el material.** Produce el video que te imaginaste, no el que
  estaba grabado. Siempre es peor.
- **Defender un efecto porque costó trabajo.** El tiempo invertido no es un argumento. Si no sirve a
  la historia, se bota igual.
- **Decir "quedó bien" en vez de dar un número.** "Quedó bien" no es verificable y no se puede repetir
  la próxima vez.
- **Fingir haber escuchado o visto el video corriendo.** Rompe la confianza en todo el trabajo.
- **Usar la transición de zoom con blur por defecto.** Casi siempre está tapando un corte que no tenía
  razón de ser.
- **Confundir renderizar con terminar.** El render es el principio de la verificación, no el final.
- **Aceptar una nota vaga sin traducirla.** "No me gusta" no es una instrucción; hay que convertirla
  en algo medible antes de tocar nada (ver `08`).
- **Montar sobre una marca inexistente.** Si no hay paleta ni tipografía definidas, el video se rehace
  cuando aparezcan.
- **Corregir errores de a uno según van apareciendo.** Se validan todos los cortes de una vez, antes
  de montar (ver `16`).
- **Seguir puliendo después de que los cambios ya no mejoran nada medible.** Eso no es rigor, es no
  querer entregar.

---

## Checklist

Antes de considerar terminada cualquier pieza de video:

- [ ] Vi/leí **todo** el material en bruto antes de decidir la estructura.
- [ ] Cada corte que puse lo puedo defender en una frase sin nombrar una herramienta.
- [ ] Cada efecto pasó la prueba: si lo quito, el video empeora.
- [ ] Convertí toda nota subjetiva del cliente en algo medible o comparable.
- [ ] Medí lo medible: duración, resolución, fps, LUFS, pico real, ritmo de cortes.
- [ ] Verifiqué **el archivo renderizado**, no la línea de tiempo (`98`).
- [ ] Transcribí el audio del render final y confirmé que ninguna palabra quedó partida.
- [ ] Comprobé zona segura de la plataforma destino (`45`, `92`).
- [ ] Las decisiones visuales salen de la marca o de la historia, no de un preset.
- [ ] Dije explícitamente qué **no** pude juzgar y se lo dejé al humano.
- [ ] Los últimos cambios ya no mejoraban nada medible → paré y entregué.
