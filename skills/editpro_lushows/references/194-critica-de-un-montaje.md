# 194 — Crítica de un montaje

Resuelve el problema de mirar un video ajeno y solo poder decir "está bacano" o "no me gustó". Eso
no es análisis: es una reacción. El análisis produce **una lista de decisiones identificadas** que
puedes copiar, adaptar o descartar mañana.

Este módulo es un protocolo. Se sigue en orden, toma entre 20 y 40 minutos por video, y sirve para
tres cosas distintas:

1. **Estudiar** un video que te gustó, para robarle bien (`195`).
2. **Diagnosticar** un video que no funciona: tuyo, de un cliente o de la competencia.
3. **Sustentar** una opinión frente a alguien que va a preguntarte "¿por qué?" (`08`).

La regla que gobierna todo el protocolo:

> **Primero se describe. Después se explica. De último se juzga.**

El 90% de las opiniones sobre video se saltan los dos primeros pasos, y por eso son inútiles.

---

## Antes de empezar: qué necesitas

- El video descargado (no verlo en el feed: el feed te condiciona con lo que viene antes y después).
- Un reproductor donde puedas ir cuadro por cuadro. VLC sirve (tecla `E` avanza un cuadro).
- Papel o un archivo de texto. **A mano es mejor**, porque obliga a resumir.
- Los datos públicos si los hay: vistas, likes, comentarios, fecha. No son la verdad, pero
  contextualizan.

Si el video es tuyo, deja pasar mínimo un día antes de analizarlo. En caliente no ves nada.

---

## Paso 0 — El contrato: qué se propuso hacer

Antes de mirar nada con lupa, escribe **una sola frase** con lo que crees que el video se propuso:

> "Que alguien que pasa scrolleando quiera ir a comer a este sitio el viernes."
> "Que un dueño de restaurante entienda en 30 segundos que está perdiendo plata sin saberlo."
> "Que un fan se ría y lo mande a un amigo."

Esto es el **contrato**. Todo lo que sigue se juzga contra él. Un video puede estar impecablemente
montado y fallar el contrato, y entonces está mal montado. Y al revés: un video feo que cumple el
contrato está bien montado, y tu trabajo es entender por qué.

Si no puedes escribir el contrato en una frase después de ver el video una vez, **ese ya es el
hallazgo principal**: el video no comunicó su propia intención.

---

## Paso 1 — Las tres pasadas

Esta es la parte que casi nadie hace y la que produce el 70% de los hallazgos. Está en `04`; aquí va
en su versión de análisis.

### Pasada 1: normal, como espectador

Míralo una vez completo, sin pausar, sin analizar. Al terminar, escribe **inmediatamente** y sin
pensar:

- ¿Qué sentí? (una palabra)
- ¿En qué segundo me dieron ganas de irme? (aunque no me fui)
- ¿Qué recuerdo? (sin volver a verlo)

Estas tres respuestas son datos que no vas a poder volver a producir: después de la segunda pasada
ya estás contaminado.

### Pasada 2: sin sonido

Baja el volumen a cero. Ahora estás mirando **montaje puro**: encuadres, ritmo, cortes, gráficos.

- ¿Se entiende de qué se trata sin oír nada? (Importa: la mayoría del consumo en redes empieza en
  mudo.)
- ¿Dónde caen los cortes? ¿Se sienten o no?
- ¿Hay algún plano que se queda largo, o alguno que no alcanzo a ver?
- ¿Dónde está mi ojo en cada momento? ¿Salta de un lado a otro?

### Pasada 3: solo sonido

Tapa la pantalla o pon el video en otra ventana. Ahora estás oyendo **guion y diseño sonoro**.

- ¿La estructura de lo que dice se sostiene sola?
- ¿La voz suena limpia, o es el punto débil?
- ¿La música empuja o tapa?
- ¿Hay silencios? ¿Dónde?
- ¿Se oyen las costuras de los cortes?

**Regla que sale de aquí:** si el video funciona en las tres pasadas, es sólido. Si solo funciona
con las dos juntas, es frágil. Si no funciona en ninguna por separado, la música lo estaba
sosteniendo todo.

---

## Paso 2 — Los números

Ahora sí, con cronómetro. Tres mediciones, ninguna toma más de cinco minutos.

### 2.1 Cortes por minuto

Cuenta los cortes y divide por la duración en minutos. No es para juzgar —no hay un número bueno—
sino para tener la escala. Referencias aproximadas para calibrar el oído:

| Tipo | Cortes por minuto (orden de magnitud) |
|---|---|
| Testimonio sobrio, institucional | 10–25 |
| Video explicativo con b-roll | 30–60 |
| Reel comercial estándar | 60–120 |
| Reel de ritmo alto / trend | 120+ |

Lo interesante no es el número: es **si el número corresponde al contenido**. 120 cortes por minuto
sobre un contenido que exige entender algo es un video que nadie va a entender.

### 2.2 El mapa de bloques

Escribe la línea de tiempo en segundos con lo que pasa. Así de simple:

```
0.0 – 2.4   Gancho: cara + pregunta "¿sabes cuánto pierdes al mes?"
2.4 – 5.0   Contexto: plano del local lleno
5.0 – 12.0  Problema: voz sobre b-roll de la cocina, 6 cortes
12.0 – 20.0 Solución: pantalla del Excel, 3 cortes lentos
20.0 – 26.0 Prueba: testimonio, plano fijo sin cortes
26.0 – 30.0 Cierre + llamado a la acción
```

Esto es lo mismo que `19` pero aplicado a material ajeno, y es la herramienta más productiva del
protocolo: **te muestra la arquitectura, no la decoración.** La mayoría de los videos que "no
funcionan" tienen un problema de arquitectura, no de cortes.

### 2.3 La curva de energía

Dibuja a mano una línea que suba y baje según cuánta energía tiene cada momento (ritmo + volumen +
intensidad de lo que se dice). No hay que medir nada: es intuición dibujada.

Las tres formas que vas a encontrar:

- **Rampa** (sube desde abajo): buena para narrativa, mala para redes (el arranque pierde gente).
- **Plana alta** (todo al máximo desde el principio): agota; el espectador se sale a los 8 segundos
  porque no hay ningún alivio.
- **Dientes de sierra con tendencia al alza**: sube, baja, sube más, baja, sube al máximo. Es la que
  funciona, y funciona porque las bajadas hacen que las subidas se sientan.

Si la curva es plana en cualquier nivel, ese es tu hallazgo.

---

## Paso 3 — Las diez preguntas

Con las tres pasadas hechas y los números en la mano, pásale al video estas diez preguntas, en este
orden. El orden importa: va de lo más determinante a lo menos.

1. **¿Los primeros 2 segundos justifican los siguientes 28?** ¿Qué exactamente hace el gancho:
   pregunta, promesa, imagen rara, movimiento, cara? Ver `30`.
2. **¿Qué está sintiendo el espectador en el segundo 5, 15 y 25?** Si la respuesta es "lo mismo"
   en los tres, el video no tiene arco.
3. **¿Cuál es la única idea?** Si hay tres, no hay ninguna.
4. **¿Dónde está la prueba?** ¿Hay algo que el video pida creer? ¿Se demuestra sin cortar, o se
   afirma? (Bazin, `191`.)
5. **¿Hay algún corte que produzca una idea que ninguno de los dos planos tiene solo?** (Eisenstein.)
   Si no hay ninguno, el montaje está ilustrando.
6. **¿Los cortes se sienten o no?** ¿Es a propósito? (`192` vs `193`.)
7. **¿Qué manda el ritmo: la música o el contenido?** Prueba a bajar la música: ¿el montaje
   sobrevive?
8. **¿Qué se quitó?** Lo más difícil de ver y lo más revelador. Busca las señales: cambios de
   respiración, cortes tapados con b-roll, ambientes que no empatan, ropa o luz que salta.
9. **¿Cuánto de lo que veo es material y cuánto es efecto?** Un video que se sostiene en efectos es
   un video que no tenía material.
10. **¿Por qué termina donde termina?** El final es la decisión más descuidada del video corto.
    ¿Remata, se apaga, o se acabó porque se acabó? Ver `33`.

---

## Paso 4 — El diagnóstico diferencial

Cuando algo no funciona, el instinto manda a arreglar cortes. Casi siempre está mal. Este es el
orden correcto, y viene directo de la jerarquía de Murch (`03`): emoción → historia → ritmo.

Revisa **en este orden** y **detente en la primera que falle**:

| # | Pregunta | Si falla, el problema es |
|---|---|---|
| 1 | ¿Se siente algo? | **El contenido.** No hay video que arregle esto. Hay que volver a grabar o replantear. |
| 2 | ¿Se entiende? | **La estructura.** Se arregla reordenando bloques, no moviendo cortes. |
| 3 | ¿Se cree? | **La prueba.** Falta una demostración sin cortar o sobra un corte sospechoso. |
| 4 | ¿Retiene? | **El gancho y la curva de energía.** Los primeros segundos y los valles. |
| 5 | ¿Fluye? | **Los cortes.** Aquí sí: J-cuts, corte en el movimiento, duración de planos. |
| 6 | ¿Se ve bien? | **Color, audio, tipografía.** De último, siempre. |

La regla de oro del diagnóstico:

> **El 80% de los videos que "no fluyen" tienen un problema de los niveles 1 a 3, y quien los montó
> lleva tres horas en el nivel 5.**

---

## Paso 5 — La ficha

El análisis solo sirve si queda escrito. Esta ficha cabe en media página y es la unidad que
alimenta tu biblioteca de referencias (`195`).

```
VIDEO: ______________________  Fuente/link: ______________  Fecha: ______
Duración: ____  Formato: ____  Cortes/min: ____  Vistas (si aplica): ____

CONTRATO (qué se propuso, una frase):

¿LO CUMPLE? Sí / No / A medias — por qué:

LO QUE HACE BIEN (máximo 3, concretas y accionables):
 1.
 2.
 3.

LO QUE HACE MAL (máximo 3):
 1.
 2.
 3.

LA DECISIÓN QUE ME LLEVO (una sola, escrita como instrucción para mí):

DÓNDE LA VOY A USAR:
```

El campo que importa es el penúltimo, y tiene que estar escrito **como instrucción**, no como
observación:

- ❌ "Usa muchos primeros planos de comida." (observación inútil)
- ✅ "En los primeros 2 s pone comida ocupando toda la pantalla, sin contexto ni logo; el contexto
  llega en el segundo 4. Probar: empezar por el detalle y ubicar después." (instrucción)

---

## Cómo criticar el video de otra persona sin dañar la relación

Distinto del análisis privado. Si te van a mostrar un video y quieren tu opinión:

1. **Pregunta primero cuál era la intención.** No opines sin conocer el contrato. La mitad de las
   críticas son en realidad desacuerdos sobre el objetivo.
2. **Describe antes de juzgar.** "En el segundo 7 hay un corte a negro" es un hecho que los dos
   pueden ver. "Se siente pesado" es tuyo y no se puede discutir.
3. **Separa el problema de la solución.** Di el problema. Deja que la persona proponga la solución
   primero: es su video y va a defender mejor una idea suya.
4. **Ordena por costo.** Empieza por lo que se arregla en cinco minutos y termina por lo que exige
   volver a grabar. Al revés desmoraliza.
5. **Una crítica de estructura vale diez de detalle.** Si la estructura está mal, comentar la
   tipografía es cruel e inútil.
6. **Di qué NO hay que tocar.** Es la parte que más se agradece y la que nadie dice.

Ver `08` para el lado contrario: cómo defender tu propio corte.

---

## Un ejercicio de treinta días

Analiza **un video al día** con este protocolo, en versión corta (contrato + tres pasadas + una
decisión). Quince minutos.

Mezcla deliberadamente:
- 10 videos que te encantan.
- 10 videos que odias pero que funcionan (millones de vistas).
- 10 videos de tu competencia directa o de tu propio nicho.

Los del segundo grupo son los que más enseñan, porque te obligan a separar **tu gusto** de **lo que
funciona**, que es la distinción más difícil y más valiosa del oficio.

A los treinta días tienes treinta fichas. Cuando las leas de corrido vas a ver dos cosas: patrones
que se repiten en lo que funciona, y **tu propio gusto dibujado**, que es de donde sale el estilo
(`196`).

---

## Errores comunes

- **Juzgar antes de describir.** "No me gustó" no es un hallazgo; es un sentimiento. El hallazgo es
  qué decisión concreta lo produjo.
- **Analizar sin conocer el contrato.** Criticar un video de humor por no ser informativo es criticar
  un martillo por no cortar.
- **Ver una sola vez.** Sin las tres pasadas no ves ni la mitad.
- **Confundir "me gusta" con "funciona".** Los videos que odias y funcionan son tu mejor material de
  estudio.
- **Analizar en el feed.** El contexto (lo que venía antes, tu estado de ánimo, la hora) contamina
  todo. Descárgalo.
- **Arreglar cortes cuando el problema es la estructura.** El error de diagnóstico más caro en horas.
- **Quedarse en la decoración.** Tipografía, LUT y transiciones son la última capa. Si empiezas por
  ahí, nunca llegas a la primera.
- **No escribir.** Un análisis que no queda en una ficha se olvida en tres días y no construye nada.
- **Sacar más de una decisión por video.** Si te llevas cinco, no te llevas ninguna. Una, escrita
  como instrucción.
- **Analizar solo lo que te gusta.** Produce un gusto endogámico y un estilo que se parece a diez
  personas.

---

## Checklist

De reflexión, sobre un análisis que acabes de hacer.

- [ ] ¿Escribí el contrato en una frase antes de mirar nada?
- [ ] ¿Hice las tres pasadas (normal, sin sonido, solo sonido) o me salté alguna?
- [ ] ¿Anoté mi reacción cruda antes de contaminarme con el análisis?
- [ ] ¿Tengo el mapa de bloques escrito, no solo en la cabeza?
- [ ] ¿Dibujé la curva de energía? ¿Qué forma tiene?
- [ ] ¿Puedo nombrar el momento exacto donde daban ganas de irse?
- [ ] ¿Identifiqué qué se quitó, no solo qué quedó?
- [ ] En el diagnóstico, ¿me detuve en la primera capa que falló, o me fui derecho a los cortes?
- [ ] ¿Mi conclusión está escrita como instrucción para mí, o como observación sobre otro?
- [ ] Si tuviera que defender esta crítica frente a quien hizo el video, ¿tengo hechos o tengo
      opiniones?
- [ ] ¿Analicé esta semana algo que no me gusta pero que funciona?
