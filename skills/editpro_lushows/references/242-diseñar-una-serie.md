# 242 — Diseñar una serie: el molde que se repite y lo que cambia cada episodio

> Verificado a **4 de agosto de 2026**. El caso de trabajo es tu serie real *Historias de Cerveza*
> (Vol. 01 Cusqueña, entregado el 4 de agosto de 2026). Lo que aquí se propone es cómo convertir ese
> episodio en una serie que no te cueste dos días cada vez.

## Por qué una serie y no videos sueltos

Una serie hace tres cosas que un video suelto no puede:

1. **Baja el costo por pieza.** Las decisiones ya están tomadas: formato, duración, tipografía, música,
   estructura. Ver la ley del costo marginal en `240`.
2. **Crea expectativa.** "¿Ya viste el nuevo?" solo existe si hay un *nuevo*. Un video suelto no genera
   la segunda visita.
3. **Le enseña a la plataforma quién eres.** Piezas coherentes en tema y formato consolidan un público.
   Piezas dispersas no.

Y una cuarta, la más importante para un dueño de negocio: **una serie se puede delegar**. Un video
suelto vive en tu cabeza. Una serie con molde escrito la puede montar otra persona.

---

## La anatomía de un formato: lo fijo y lo variable

Esta es la tabla más importante del módulo. Todo formato de serie se define llenando estas dos columnas.

### *Historias de Cerveza* — el molde

| Elemento | FIJO (nunca cambia) | VARIABLE (cambia por episodio) |
|---|---|---|
| Duración | 45–60 s | — |
| Relación de aspecto | 9:16 (1080×1920) | — |
| Apertura | Gancho hablado en los primeros 2 s | La frase del gancho |
| Identidad visual | Grabado dorado sobre azul #09163A | La cerveza / la tinta |
| Tipografía | La del sistema de marca | El texto |
| Estructura | Gancho → conflicto → dato → cierre de marca | El contenido de cada bloque |
| Voz | Misma voz, mismo tono | El guion |
| Música | Misma pieza o misma familia | — |
| Cierre | Placa fija "Bendita Pola · Tocancipá" | — |
| Numeración | "Vol. NN" en la esquina | El número |

**Regla de oro:** si la columna VARIABLE tiene más de 5 filas, no tienes una serie. Tienes videos
distintos con el mismo nombre.

Concretamente en tu caso, lo variable es: la cerveza, el guion, la tinta/color de acento, los fondos, el
número. Cinco cosas. Eso está bien.

---

## Los tres niveles de "fijo"

No todo lo fijo es igual de fijo. Piénsalo en capas:

| Capa | Qué es | Cada cuánto puede cambiar |
|---|---|---|
| **Marca** | azul, dorado, tipografía, logo | Casi nunca (`directorcreativo_lushows`) |
| **Formato** | duración, estructura, tipo de apertura, placa de cierre | Entre temporadas |
| **Episodio** | guion, imágenes, dato, ritmo | Cada vez |

El desastre ocurre cuando tocas la capa **formato** en cada episodio. Ahí vuelves a pagar el costo de
diseño completo. Congela el formato; juega en la capa episodio.

---

## Cuántos episodios antes de evaluar

Esta pregunta tiene una respuesta incómoda: **más de los que quieres hacer**.

| Episodios | Qué puedes concluir |
|---|---|
| 1 | Nada. Absolutamente nada. La varianza del reparto es brutal. |
| 3 | Si el formato es producible. Nada sobre si funciona. |
| **6** | **Primer punto de decisión honesto.** Tendencia visible. |
| 12 | Conclusión sólida. Puedes comparar ganchos entre episodios. |

**Compromiso mínimo recomendado: 6 episodios, publicados en un plazo definido, antes de decidir nada.**

Y esto no es fe ciega. Es que con menos de 6 no tienes cómo separar la señal del ruido: en contenido
corto, dos piezas idénticas en calidad pueden dar 400 y 9.000 vistas por razones que no controlas.

### El compromiso escrito

Antes de grabar el Vol. 02, escribe esto en `00-sistema.md`:

```
SERIE: Historias de Cerveza
Compromiso: 6 episodios (Vol. 01 a Vol. 06)
Cadencia: 1 cada 2 semanas → termina el 27 de octubre de 2026
Presupuesto de horas: 3 h por episodio después del Vol. 02
Criterio de continuación (al Vol. 06):
  - retención media ≥ 45 %
  - envíos/alcance por encima del promedio de mis otros pilares
  - al menos 3 personas mencionaron la serie en el bar
Si no se cumple: se ajusta el formato, no se abandona la serie de una.
```

Fíjate en la última línea. La mayoría de las series no fracasan: se abandonan antes de tener datos.

---

## Cómo abaratar tu serie de 14 h a 3 h

Ataque quirúrgico al caso real. Dónde se te fueron las horas y qué hacer:

| Dónde se fue | Vol. 01 | Cómo se ataca | Vol. 03+ |
|---|---|---|---|
| Investigar la historia | 3 h | Investigar **6 historias de una sola vez**, en una sesión | 25 min |
| Escribir el guion | 2 h | Plantilla de guion con los 4 bloques y sus duraciones | 30 min |
| Generar los 8 fondos | 3 h | Prompt madre guardado; cambia solo la cerveza y la tinta | 40 min |
| Montar | 4 h | Proyecto plantilla: pistas, textos y placa ya puestas | 1 h |
| Color / audio / export | 1 h | Preset verificado una vez y reutilizado (`91`, `98`) | 10 min |
| Copy y publicación | 1 h | Plantilla de copy con hueco para el dato | 10 min |
| **Total** | **14 h** | | **≈ 3 h** |

Las dos palancas que más rinden:

**1. El proyecto plantilla.** Un archivo de CapCut (o el que uses) que ya tiene: la pista de música, la
placa de cierre, el estilo de texto, la numeración, el preset de color. Lo duplicas y solo reemplazas
medios. Ver `88-plantillas-reutilizables.md` y `218-capcut-escribir-recursos-por-codigo.md` si quieres
generarlo por código.

**2. Investigar en lote.** Investigar 6 historias seguidas cuesta mucho menos de 6 veces investigar una:
ya estás en el tema, ya tienes las fuentes abiertas, ya sabes qué buscas. Es el mismo principio del lote
de rodaje (`244`).

---

## La estructura del episodio (plantilla de guion)

Para una serie narrada de 45–60 s en vertical:

| Bloque | Segundos | Qué tiene que pasar |
|---|---|---|
| **Gancho** | 0–2 s | Una afirmación que produzca extrañeza. Sin logo, sin intro, sin "hola" |
| **Anclaje** | 2–6 s | Se ve la cerveza / el objeto. La persona entiende de qué va |
| **Conflicto** | 6–30 s | La tensión de la historia: quién, contra qué, qué pasó |
| **Resolución/dato** | 30–48 s | El dato que la persona se va a llevar y va a repetir |
| **Cierre de marca** | 48–55 s | Placa. Corto. Sin pedir que sigan, sin "dale like" |

La prueba: **si le quitas el audio, ¿se entiende?** Debe entenderse. Y **si le quitas el video, ¿se
entiende?** También. Un episodio que solo funciona con las dos capas juntas pierde a mucha gente, porque
buena parte lo ve sin sonido. Ver `41` y `216` para subtítulos.

> **Frontera con `ventas_lushows`:** el cierre de un episodio de serie **no es un cierre de venta**. La
> serie construye autoridad y recuerdo; la venta la hace el pilar de conversión (`241`) y el copy. Meterle
> "ven hoy y te damos 2x1" a una historia sobre la guerra del Pacífico rompe las dos cosas.

---

## Tipos de serie que funcionan en un negocio local

| Tipo | Cómo funciona | Costo | Riesgo |
|---|---|---|---|
| **Documental corto** (la tuya) | Historia + dato + marca | Alto | Se agota el tema; se vuelve caro |
| **Serie de proceso** | Cómo se hace X, siempre igual | Bajo | Aburre si no hay variedad |
| **Serie de personas** | Un cliente/empleado por episodio | Bajo | Depende de que la gente quiera salir |
| **Serie de reto/comparación** | "Probamos X vs Y" | Medio | Puede parecer relleno |
| **Serie de calendario** | "Los jueves de..." | Muy bajo | Solo convierte, no atrae |

Recomendación honesta para ti: **una serie cara y una barata en paralelo**. La cara (Historias de
Cerveza) construye marca cada 2 semanas. La barata (proceso o personas) llena la cadencia semanal. Si
solo tienes la cara, cualquier semana ocupada rompe la constancia.

---

## Nombre, numeración y portada

Tres detalles que parecen menores y no lo son:

- **Nombre corto y decible.** "Historias de Cerveza" pasa: se puede decir en voz alta en una mesa.
- **Numeración visible.** El "Vol. 01" hace dos cosas: le dice a quien llega tarde que hay más, y a ti
  te obliga a que exista un Vol. 02. Es un compromiso público barato.
- **Portada con sistema.** Misma composición, cambia la cerveza. Que en tu grid se lean como colección.
  Recuerda que el grid recorta a 1:1 (`141`): la numeración va en la franja central, no abajo.

---

## Cuándo matar una serie

Sin drama y sin culpa. Señales claras:

1. **Llegaste a 6 episodios y no cumplió el criterio escrito.** Ajusta formato una vez; si a los 12
   sigue igual, se cierra.
2. **El costo por episodio no baja.** Si el Vol. 05 te cuesta como el Vol. 01, el formato está mal
   diseñado: hay demasiado variable.
3. **Se te acabó el material.** Mejor cerrar una temporada de 8 con dignidad que arrastrar episodios
   flojos.
4. **Te da pereza.** Se nota en pantalla. Siempre.

Cerrar bien: un episodio final que diga "cerramos temporada". Deja la puerta abierta y no parece
abandono. Una serie abandonada en silencio le dice a tu público que no cumples lo que anuncias.

---

## Errores comunes

- **Hacer el episodio 1 como si fuera una película.** El Vol. 01 debe ser el prototipo del molde, no la
  obra de tu vida. Si es irrepetible, el formato está muerto al nacer.
- **No escribir el molde.** Si lo fijo y lo variable no están en un archivo, cada episodio se rediseña
  solo, sin que te des cuenta.
- **Mejorar el formato cada episodio.** Anota las mejoras y aplícalas todas en la temporada 2.
- **Publicar sin numerar.** Pierdes el efecto de colección y la promesa implícita de continuidad.
- **Evaluar al episodio 2.** No hay datos. Es un impulso emocional, no una decisión.
- **Series de una sola persona insustituible.** Si solo tú puedes hacerla, no es sistema (`240`).
- **Cadencia irreal.** Prometer semanal una serie que cuesta 6 h cuando tienes 5 h a la semana en total.
- **Cambiar de plataforma a mitad de temporada.** La serie necesita acumular; mudarla resetea el
  aprendizaje del reparto.
- **No dejar hueco al reciclaje.** Cada episodio debería producir además 2–3 piezas cortas (`245`). Si
  grabas justo lo necesario, tiras a la basura la mitad del valor del rodaje.
- **Que el molde sea tan rígido que aburra.** Lo fijo es el marco, no el contenido. Si los 6 episodios
  se sienten idénticos, mueve algo de la columna fija a la variable — pero solo una cosa.

---

## Checklist

**Antes del episodio 2 (diseño del molde):**

- [ ] Tengo la tabla FIJO / VARIABLE escrita, con máximo 5 filas en variable
- [ ] La estructura del guion está en plantilla, con segundos por bloque
- [ ] Existe un proyecto plantilla de montaje, no un proyecto nuevo
- [ ] El preset de export está verificado una vez y guardado (`91`, `98`)
- [ ] Escribí el compromiso: número de episodios, fechas y criterio de continuación
- [ ] Tengo las historias de los 6 episodios ya elegidas
- [ ] El nombre es corto y la numeración es visible en zona segura

**Por episodio:**

- [ ] Solo toqué la columna VARIABLE
- [ ] El gancho está en los primeros 2 s y no hay intro
- [ ] Se entiende sin sonido y se entiende sin imagen
- [ ] La placa de cierre es idéntica a la de los anteriores
- [ ] Anoté las horas reales que me tomó
- [ ] Saqué al menos 2 piezas cortas adicionales del mismo material (`245`)

**Al episodio 6:**

- [ ] Comparo contra el criterio escrito, no contra mi sensación
- [ ] El costo por episodio bajó respecto al primero
- [ ] Decido: continuar igual · ajustar una cosa · cerrar temporada
