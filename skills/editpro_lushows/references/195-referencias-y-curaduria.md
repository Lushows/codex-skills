# 195 — Referencias y curaduría

Resuelve el problema de tener una carpeta de "guardados" con 800 videos que nunca has vuelto a
abrir. Eso no es una biblioteca de referencias: es un basurero con buena intención.

Una biblioteca de referencias sirve cuando cumple tres condiciones que casi nadie cumple:

1. **Se puede buscar** por problema, no por video.
2. **Guarda la decisión**, no el video.
3. **Se poda.** Una biblioteca que solo crece deja de servir.

Este módulo es el sistema. Y antes, la parte incómoda: cómo se roba bien, que es una habilidad
técnica y también una posición ética.

---

## Parte 1 — Robar bien

### La cita que hay que corregir

Vas a oír mil veces "los buenos artistas copian, los grandes roban", atribuido a Picasso. **No hay
fuente verificable de que Picasso lo dijera.** Lo más cercano y documentado es T.S. Eliot, en su
ensayo sobre Philip Massinger (*The Sacred Wood*, 1920):

> "Los poetas inmaduros imitan; los poetas maduros roban."

Y Eliot sigue, que es la parte que nadie cita y la única que importa: el poeta malo desfigura lo que
toma, el bueno lo convierte en algo mejor, o al menos en algo distinto.

La formulación más útil para el oficio es la de **Jim Jarmusch**, en sus "reglas de oro" publicadas
en la revista *MovieMaker* en 2004: roba de donde sea que te encienda algo, roba solo lo que te habla
directamente, no te molestes en esconder el robo — y termina citando a **Godard**: *"No importa de
dónde tomas las cosas; importa a dónde las llevas."*

Ese es el criterio completo en una frase. **A dónde la llevas.**

### La diferencia entre robar y copiar, en concreto

| | Copiar | Robar |
|---|---|---|
| Qué te llevas | La apariencia | La decisión |
| Qué produces | Una versión peor del original | Algo que solo se parece por dentro |
| Qué pasa si el original desaparece | Tu video no se entiende | Da igual |
| Ejemplo | Bajas la plantilla y le cambias las fotos | Notas que el original **empieza por el detalle y ubica después**, y aplicas eso a tu material |

La prueba práctica es esta pregunta:

> **Si pusiera mi video al lado del original, ¿alguien podría decir cuál copió a cuál?**

Si sí, copiaste. Si no se parecen en nada por fuera pero comparten una lógica por dentro, robaste
bien.

### Las tres cosas que sí se pueden robar

1. **La estructura.** El orden de los bloques. Es lo más valioso y lo más invisible. Nadie te va a
   acusar de nada y es lo que más cambia el resultado.
2. **El mecanismo.** "Aquí el corte no se ve porque cae sobre un movimiento hacia cámara." "Aquí el
   silencio de medio segundo hace que la frase pese." Herramientas, no adornos.
3. **La energía.** Cómo se siente la curva del video. Se roba imitando la forma, no el contenido.

### Las tres que no

1. **La ejecución exacta.** Los mismos textos, la misma música, el mismo encuadre, el mismo chiste.
   Eso no es referencia, es plagio con pasos intermedios.
2. **La identidad de otra marca.** Copiar el sistema visual de un competidor te vuelve la versión
   barata de él en la cabeza del cliente, aunque tu video sea mejor. Ver `125` y la skill de
   dirección creativa.
3. **Material ajeno sin derecho.** Clips, música y voces tienen dueño. En redes esto no es una
   discusión moral: es un aviso de derechos de autor que te tumba el video, la cuenta o la pauta. La
   música es el caso más frecuente y el más fácil de evitar.

---

## Parte 2 — El sistema de biblioteca

### Principio de diseño: se archiva por problema, no por video

El error universal es organizar por fuente ("TikToks guardados", "Reels que me gustan") o por marca.
Eso no sirve porque **el día que necesitas la referencia no estás buscando un video: estás buscando
una solución.**

La estructura correcta es por **problema del editor**:

```
referencias/
  01-ganchos/
  02-estructuras/
  03-transiciones-y-cortes/
  04-texto-y-graficos/
  05-color-y-look/
  06-sonido-y-musica/
  07-testimonios-y-prueba/
  08-cierres-y-llamados/
  09-antipatrones/          ← lo que NO hay que hacer, y por qué
  _fichas.md                ← el índice buscable
```

Nueve carpetas. No más. Si necesitas una décima, probablemente lo que tienes es una subcarpeta.

La carpeta `09-antipatrones` es la que nadie hace y la que más rápido mejora el criterio: guardar
lo que está mal **con la razón escrita** te entrena a nombrar problemas, y nombrar es la mitad del
oficio.

### Qué se guarda de cada cosa

**No guardes el video solo.** Un video sin ficha es un video que no vas a volver a abrir.

De cada referencia guardas tres cosas:

1. **El archivo** (o un fragmento de 10–15 segundos, que casi siempre alcanza).
2. **Una captura del cuadro clave**, si lo que te importa es visual.
3. **La ficha**, que son cinco campos y no más:

```
[G-014] Gancho — comida a pantalla completa antes de ubicar
Fuente: @cuenta / link / 2026-07-30
Problema que resuelve: arrancar sin contexto y ganar 2 segundos
La decisión: los primeros 2 s son un detalle de comida ocupando el cuadro
  entero, sin logo ni establecimiento. El contexto (el local) llega en el
  segundo 4, cuando el espectador ya se quedó.
Dónde probarla: reels de plato del día; NO en video institucional.
```

El código (`G-014`) sirve para nombrar el archivo igual y encontrarlo en dos segundos.

**Regla dura:** si no puedes escribir el campo "la decisión" en dos o tres líneas, **no entendiste la
referencia y no vale la pena guardarla.** Ese filtro solo ya te deja el 20% de lo que ibas a
guardar, que es exactamente el 20% que sirve.

### El índice

Un solo archivo de texto, `_fichas.md`, con todas las fichas una tras otra. Lo buscas con Ctrl+F por
palabra: "silencio", "testimonio", "punch-in", "cierre". Nada de bases de datos, nada de
herramientas: **cualquier sistema que exija mantenimiento se abandona en seis semanas.**

### El flujo diario: la bandeja de entrada

El problema real no es organizar: es capturar sin frenar. El flujo que funciona tiene dos tiempos:

**En el momento (5 segundos):** guardas en la carpeta de guardados de la app, sin pensar. No
interrumpas el consumo para archivar; no vas a hacerlo.

**Una vez por semana (30 minutos):** abres los guardados de la semana y le haces a cada uno una sola
pregunta:

> **¿Puedo escribir en dos líneas qué decisión me llevo?**

- Si **sí** → ficha, archivo, carpeta. Entra a la biblioteca.
- Si **no** → se borra. Sin culpa. Te gustó, no te enseñó nada. Son cosas distintas.

De veinte guardados de la semana, entran tres o cuatro. Eso es normal y es el punto.

### La poda trimestral

Cada tres meses, lee el índice completo de corrido. Media hora. Y borra:

- Lo que ya interiorizaste (si lo haces sin pensar, no necesitas la ficha).
- Lo que envejeció (efectos de moda, formatos que la plataforma dejó de premiar).
- Lo que guardaste por gusto y nunca usaste (dos trimestres sin usar = fuera).

Una biblioteca sana tiene entre 60 y 150 fichas vivas. Con más, no la conoces. Con menos, no
alcanza.

La poda tiene un efecto secundario que es la razón real de hacerla: **leer el índice de corrido te
muestra tu propio gusto.** Los patrones que se repiten en lo que guardaste son tu estilo antes de
que sepas que lo tienes. Ver `196`.

---

## Parte 3 — Qué mirar para que la biblioteca no sea endogámica

Si solo guardas reels, tus reels van a parecerse a todos los reels. Las referencias más valiosas
vienen de donde nadie de tu competencia está mirando.

**Fuera del formato:**
- **Cine y series bien montadas.** Ver `03` y `190`. Una secuencia de dos minutos de una película
  enseña más que cien reels.
- **Documental.** Es donde mejor se resuelve el problema de "tengo material feo y tengo que hacer
  que importe", que es tu problema todos los días.
- **Publicidad de televisión de los 80 y 90.** Treinta segundos, sin posibilidad de saltarse, sin
  algoritmo. Densidad narrativa brutal.
- **Videoclips.** El laboratorio de montaje rítmico. Ver `190`.
- **Deportes en vivo.** Realización en tiempo real: qué plano se toma en cada momento y por qué.
- **Trailers.** Estructura de gancho comprimida al máximo.

**Fuera del video:**
- **Diseño editorial** para tipografía y jerarquía (`42`).
- **Fotografía** para encuadre y luz.
- **Standup** para tiempos, silencio y remate. El *timing* de un chiste es montaje puro.
- **Música** para estructura: intro, verso, coro, puente, coro final. Es la misma arquitectura que
  un video que funciona.

**Una regla que vale oro:** por cada cinco referencias de tu formato, guarda una de otro lado. Esa
proporción es la que evita que tu trabajo se vea como el de todos.

---

## Parte 4 — La biblioteca del proyecto (distinta de la personal)

La biblioteca de arriba es tuya y dura años. Para cada proyecto o cliente, además, se arma una
**carpeta de referencias del proyecto** con entre 5 y 10 videos, no más, y una línea por cada uno que
diga qué se toma de él:

```
CLIENTE: restaurante — reels semanales
REF 1 — [link] — la energía general y el ritmo (no los textos)
REF 2 — [link] — cómo hace el primer plano de comida en el segundo 0
REF 3 — [link] — el cierre con el precio en pantalla 1,5 s
NO QUEREMOS — [link] — este tono de "influencer gritando"; el cliente lo odia
```

Esa última línea, **la anti-referencia**, ahorra más discusiones que las otras tres juntas. Ver `02`.

Y una advertencia de oficio: la carpeta de referencias del cliente no es un contrato. Si el cliente
manda una referencia con producción de cien millones, hay que decirlo en el momento y no al
entregar. Ver `08`.

---

## Parte 5 — La honestidad sobre la referencia

Tres reglas que evitan problemas reales:

1. **Nunca presentes una referencia como si fuera trabajo tuyo.** Ni en un portafolio, ni en una
   propuesta, ni "para dar una idea". Si se ve, se aclara de quién es.
2. **Si tu video se parece mucho a otro, dilo tú primero.** "Esto está inspirado en X" te da
   autoridad. Que lo descubra el cliente te la quita.
3. **Si vas a usar material que no es tuyo en el video final** —un clip, una canción, una foto—
   tiene que tener licencia. En redes esto no es teoría: es una reclamación de derechos que te
   silencia el audio, te baja el video o te tumba la pauta, y suele aparecer justo cuando el video
   está funcionando.

---

## Errores comunes

- **Guardar sin ficha.** Un guardado sin la decisión escrita es un video que no vas a volver a
  abrir. Es el error que produce las carpetas de 800.
- **Organizar por fuente en vez de por problema.** El día que necesitas la referencia buscas una
  solución, no una cuenta.
- **Robar la ejecución en vez de la decisión.** Produce una versión peor del original y se nota.
- **No podar.** Una biblioteca que solo crece deja de ser buscable y deja de servir.
- **Guardar solo lo que te gusta.** Lo que odias y funciona enseña más. Y los antipatrones enseñan a
  nombrar problemas.
- **Mirar solo tu formato.** Cinco referencias de reels producen un reel promedio. Una de fuera
  produce uno distinto.
- **Interrumpir el consumo para archivar.** No lo vas a hacer. Captura rápido, procesa una vez por
  semana.
- **Montar un sistema con herramientas complicadas.** Se abandona. Carpetas y un archivo de texto.
- **Usar música o clips ajenos "porque es solo un reel".** Es el aviso de derechos de autor más
  común y llega siempre en el peor momento.
- **Presentar la referencia como trabajo propio.** Se descubre y cuesta la relación entera.

---

## Checklist

De reflexión. Léelo mirando tu carpeta de guardados actual.

- [ ] ¿Cuántos videos tengo guardados y cuántos he vuelto a abrir de verdad?
- [ ] ¿Puedo encontrar en menos de un minuto una referencia para un problema concreto —por ejemplo,
      "cómo cerrar un video de servicio"?
- [ ] De mis últimas diez referencias, ¿en cuántas puedo escribir la decisión en dos líneas?
- [ ] ¿Tengo una carpeta de antipatrones, o solo guardo lo que me gusta?
- [ ] ¿Cuántas de mis referencias son de fuera de mi formato? ¿Llego a una de cada cinco?
- [ ] ¿Cuándo fue la última vez que podé? ¿Hay cosas ahí que ya hago sin pensar?
- [ ] Cuando me inspiro en algo, ¿me llevo la estructura o la apariencia?
- [ ] Si pusiera mi último video al lado de su referencia, ¿se notaría cuál copió a cuál?
- [ ] En mis proyectos, ¿tengo anti-referencias escritas, o solo referencias?
- [ ] Leyendo mi índice de corrido, ¿qué se repite? ¿Eso ya es mi estilo? (Sigue en `196`.)
