# 215 — Máscaras, croma, superposición y modos de fusión

Este módulo es sobre **componer**: poner una imagen encima de otra y hacer que se vean como una sola.

CapCut tiene cuatro herramientas para eso, y son bastante más limitadas de lo que la gente cree.
Vamos a ver qué hace cada una, cuál usar según el caso, y —esto es lo importante— dónde está la
pared.

---

## Las cuatro herramientas y qué resuelve cada una

| Herramienta | Qué hace | Cuándo se usa |
|---|---|---|
| **Opacidad** | Hace transparente **toda** la capa | Fundidos, marcas de agua, texturas suaves |
| **Máscara** | Muestra solo **una zona con forma** | Recortes, divisiones de pantalla, revelados |
| **Croma** | Quita **un color** | Fondos verdes, elementos con fondo plano |
| **Modo de fusión** | Combina las capas **por brillo/color** | Luces, humo, texturas, destellos |

El error de principiante es intentar todo con opacidad. La pregunta correcta es:

> **¿Qué quiero quitar de la capa de arriba?**
> - Todo, un poco → **opacidad**
> - Una zona con forma → **máscara**
> - Un color → **croma**
> - Lo oscuro (o lo claro) → **modo de fusión**

---

## Superposición: la base

Todo esto vive sobre el mismo principio: **la pista de arriba tapa a la de abajo**.

En CapCut arrastrás un clip por encima de la pista principal y automáticamente se crea una pista
superior. Lo que hagas ahí afecta cómo se ve lo de abajo.

Cosas prácticas que ahorran dolor:

- **El orden importa y no siempre es obvio.** Pista 3 tapa a pista 2 tapa a pista 1. Si "no se ve" un
  elemento, casi siempre está debajo de otra cosa.
- **Podés apilar bastantes pistas**, pero cada una cuesta rendimiento. Pasando de 5 o 6 capas de video
  la previsualización empieza a arrastrarse.
- **Las pistas de efecto y filtro afectan a todo lo que está debajo**, en el tramo que duran. Esto
  incluye tus superposiciones. Si querés que el filtro no toque el logo, poné el logo **arriba** de
  la pista de filtro.
- **Alt + arrastrar** duplica un clip rápidamente. Muy útil para las técnicas de doble máscara que
  vienen abajo.

---

## Máscaras

Seleccioná el clip → panel derecho → **Máscara**.

### Las formas disponibles

| Forma | Para qué |
|---|---|
| **Lineal** | Divide la pantalla por una línea. La más útil de todas. |
| **Espejo** | Una banda: muestra el centro, oculta arriba y abajo |
| **Círculo** | Foco, viñeta con forma, resaltar una cara |
| **Rectángulo** | Recortes, pantalla partida, encuadrar un elemento |
| **Corazón / Estrella** | Decorativo. Se ve a plantilla. Usalo con criterio. |

### Los controles

- **Posición** — dónde está la máscara (arrastrá en la vista previa).
- **Tamaño** — qué tan grande.
- **Rotación** — el ángulo.
- **Difuminado / Pluma** — qué tan suave es el borde. **El control que más importa.**
- **Invertir** — muestra lo de afuera en vez de lo de adentro.

**El difuminado es la diferencia entre que se vea a recorte y que se vea a composición.** Una máscara
con borde duro grita "esto está pegado encima". Con 10–30 % de difuminado, se integra. Salvo que
quieras el borde duro a propósito (pantalla partida), siempre poné algo de difuminado.

### La limitación grande

**Una máscara por clip. Punto.**

No podés poner dos círculos en la misma capa. No podés hacer una forma libre. No hay máscaras de
Bézier, no hay rotoscopia, no hay máscaras animadas por forma.

**El apaño:** duplicá el clip (`Alt + arrastrar` a la pista de arriba) y ponele la segunda máscara a
la copia. Dos círculos = dos copias del mismo clip, cada una con su máscara. Funciona, pero cada
copia cuesta rendimiento y multiplica el trabajo si después cambiás algo.

Si necesitás tres o más máscaras, o una forma que no está en la lista, **ese trabajo no es de
CapCut**. Ver módulo 219.

### Los tres usos que valen la pena

**1. Pantalla partida (antes / después)**
- Clip A en la pista de abajo (el "después").
- Clip B en la pista de arriba (el "antes").
- Máscara **lineal** vertical al clip B, centrada.
- Difuminado en 0 para el borde limpio.
- Bonus: animá la posición de la máscara con keyframes (módulo 213) para que el borde barra de un
  lado al otro. Es el efecto de "antes y después" que se ve en todas las cuentas de reformas.

**2. Revelado con barrido**
- Clip o texto en la pista de arriba.
- Máscara lineal fuera del cuadro.
- Keyframe de posición de la máscara al inicio (fuera) y al final (dentro).
- Difuminado al 5–15 %.
- Resultado: el elemento aparece barriendo. Mucho más elegante que un fundido.

**3. Foco en una persona**
- Duplicá el clip.
- A la copia de arriba, máscara circular sobre la cara, difuminado alto (40 %+).
- A la copia de abajo, un filtro oscuro o un desenfoque.
- Resultado: la cara queda iluminada y el resto apagado. Barato y efectivo.

---

## Croma (fondo verde)

Seleccioná el clip → panel derecho → **Croma**.

### Los controles

- **Selector de color** — un gotero. Hacé clic en el color que querés quitar, **en la vista previa**.
- **Intensidad / Similitud** — cuánto rango de ese color se quita. Subilo hasta que el fondo
  desaparezca.
- **Sombra / Reducción de sombra** — limpia los restos oscuros en el borde.

### Cómo hacerlo bien

1. **Elegí el color con el gotero en la zona más representativa del fondo**, no en una esquina rara.
2. **Subí la intensidad lentamente** hasta que el fondo se vaya.
3. **Pará justo antes de que empiece a comerse al sujeto.** Si el pelo o los bordes empiezan a
   desaparecer, te pasaste.
4. **Usá sombra para limpiar el halo verde** del borde.
5. **Mirá el resultado sobre el fondo real, no sobre negro.** Un croma que se ve perfecto sobre negro
   puede tener bordes horribles sobre un fondo claro.

### La verdad sobre el croma de CapCut

Es **aceptable**, no bueno. Comparado con Resolve o After Effects:

- **No hay control de spill (derrame de color)** más allá del ajuste de sombra. El verde que rebota
  sobre la piel y el pelo se queda ahí.
- **No hay refinamiento de borde** (edge choke, blur del matte).
- **No hay vista de matte** (ver el recorte en blanco y negro para juzgarlo). Estás trabajando a ojo.
- **El pelo suelto se pierde.** Siempre.
- **Con fondo mal iluminado, se rinde.** Si el verde tiene manchas de sombra, no hay forma.

**Regla:** el croma se gana en el rodaje. Fondo parejo, bien iluminado, sujeto separado al menos un
metro del fondo, ropa que no sea verde. Con buen material, el croma de CapCut alcanza. Con material
malo, ninguna herramienta te salva y CapCut menos.

### La alternativa: *Quitar fondo*

CapCut tiene también *Quitar fondo* (a veces *Recorte inteligente*), que usa IA y **no necesita fondo
verde**. Para personas sobre fondos normales funciona sorprendentemente bien.

Pero:
- Se procesa en la nube en varias versiones. Necesitás internet.
- El borde parpadea con movimiento rápido.
- Falla con varias personas, con oclusiones y con poca luz.
- Es lento en clips largos.

Para un plano corto de una persona hablando, suele ser mejor que armar un croma. Probalo primero.

---

## Modos de fusión

Seleccioná el clip → panel derecho → **Modo de fusión** (a veces dentro de *Básico*, según versión).

Un modo de fusión combina la capa de arriba con la de abajo usando una fórmula matemática de brillo y
color. Suena abstracto; en la práctica son tres los que importan:

| Modo | Qué hace | Para qué |
|---|---|---|
| **Normal** | Tapa | El defecto |
| **Trama / Screen** | **Elimina el negro** | Destellos, humo, luces, chispas, fuego |
| **Multiplicar** | **Elimina el blanco** | Texturas de papel, tinta, rayado, polvo |
| **Superponer / Overlay** | Sube contraste combinando | Texturas de color, grano, look |
| **Añadir / Add** | Como Trama pero más fuerte | Destellos muy brillantes |
| **Luz fuerte** | Contraste agresivo | Efectos duros |
| **Aclarar / Oscurecer** | Se queda con lo más claro / oscuro | Casos puntuales |

### El truco que resuelve el 80 %

**Descargás un video de "destellos de luz" o "humo" o "partículas" sobre fondo negro. Lo ponés
encima. Modo de fusión: Trama. El negro desaparece.**

Eso es todo. No necesitás croma, no necesitás máscara. Es la forma más rápida de meter elementos
visuales de verdad en una pieza.

Y el inverso: **elementos sobre fondo blanco → modo Multiplicar.** Ideal para texturas de papel,
sellos, tinta, rayaduras de película.

Cuando busques material para esto, buscá literalmente "overlay black background" o "sobre fondo
negro". Hay bibliotecas enteras gratuitas.

### Consejos

- **Bajá la opacidad después de poner el modo.** Un overlay de luz al 100 % en Trama casi siempre es
  demasiado. 40–70 % suele ser lo correcto.
- **Superponer y Luz fuerte son muy agresivos.** Empezá al 20–30 % de opacidad.
- **Los modos de fusión no funcionan bien apilados en muchas capas.** Dos overlays con Trama ya es
  bastante. Tres es exceso.
- **El resultado cambia según lo que haya debajo.** Un overlay que se ve bien sobre un plano oscuro
  puede desaparecer sobre uno claro. Revisá en cada tramo.

---

## Combinarlo todo

La composición real casi nunca usa una sola herramienta. Un ejemplo completo:

**Objetivo:** una persona hablando, con un video de la ciudad de fondo y luces de bokeh encima.

1. **Pista 1** — video de la ciudad (el fondo).
2. **Pista 2** — la persona, con *Quitar fondo* o croma.
3. Ajustá el color de la pista 2 para que **coincida** con la temperatura del fondo. Si no, se ve
   pegoteado. Este paso es el que casi nadie hace y el que más importa.
4. **Pista 3** — overlay de bokeh sobre negro, modo **Trama**, opacidad 45 %.
5. Opcional: máscara circular difuminada en la pista 3 para que las luces solo aparezcen en un lado.
6. **Pista de filtro** debajo de todo, estirada, para unificar el color de la escena completa.

El paso 3 y el 6 son los que hacen que se vea compuesto en vez de collage. Si dos capas tienen
temperaturas de color distintas, el ojo detecta el truco al instante.

---

## Dónde está la pared

Sé honesto con el alcance:

- **Una máscara por clip.** Sin formas libres, sin Bézier, sin rotoscopia.
- **Sin tracking planar.** No podés pegar un elemento a una superficie en movimiento.
- **Croma sin spill suppression real ni vista de matte.**
- **Sin precomposiciones.** No podés agrupar capas y tratarlas como una.
- **Sin canal alfa en la exportación.** No podés exportar un elemento con fondo transparente desde
  CapCut para usarlo en otro lado. Esto es una limitación grande y sorprende a mucha gente.
- **Sin capas de ajuste de verdad** con máscara propia.

Si tu trabajo necesita dos o más de esas cosas, el trabajo es de After Effects. No pelees.

---

## Errores comunes

- **Usar opacidad cuando querías máscara.** Opacidad hace transparente **todo**. Si querés que solo
  una parte se vea, es máscara.
- **Máscara con borde duro.** Se ve a recorte. Poné 10–30 % de difuminado casi siempre.
- **Subir la intensidad del croma hasta que el fondo se va del todo.** Te comés el pelo y los bordes
  del sujeto. Parás antes y limpiás con sombra.
- **Juzgar el croma sobre fondo negro.** Poné el fondo real antes de decidir que quedó bien.
- **No igualar el color entre las capas compuestas.** Es lo que más delata una composición falsa.
  Antes de los detalles, hacé que las dos capas tengan la misma temperatura.
- **Overlays al 100 % de opacidad.** Un destello en modo Trama al 100 % tapa la escena. 40–70 %.
- **Buscar un elemento "con fondo transparente" cuando lo que necesitás es "sobre fondo negro" +
  modo Trama.** Es mucho más fácil de encontrar y funciona igual.
- **Apilar 8 capas de video.** La previsualización se muere y no vas a poder juzgar el ritmo.
- **Duplicar el clip para poner una segunda máscara y después olvidarse de que hay dos.** Cambiás algo
  en uno y el otro queda distinto. Nombrá o agrupá mentalmente esas parejas.
- **Esperar exportar con fondo transparente.** CapCut no exporta alfa. Si necesitás eso, no es acá.
- **Poner el logo debajo de la pista de filtro** y después no entender por qué se le cambió el color.

---

## Checklist

- [ ] Me pregunté qué quiero quitar de la capa de arriba antes de elegir herramienta.
- [ ] Toda máscara tiene difuminado, salvo que el borde duro sea intencional.
- [ ] El croma lo juzgué **sobre el fondo real**, no sobre negro.
- [ ] Paré la intensidad del croma antes de que se comiera bordes y pelo.
- [ ] Probé *Quitar fondo* antes de armar un croma, si el material lo permitía.
- [ ] Las capas compuestas tienen temperaturas de color parecidas.
- [ ] Los overlays van con modo Trama (fondo negro) o Multiplicar (fondo blanco), y con opacidad
      bajada.
- [ ] No tengo más de 5 o 6 pistas de video simultáneas.
- [ ] Lo que no debe recibir el filtro está **encima** de la pista de filtro.
- [ ] Si necesité dos máscaras, duplique el clip y tengo claro que ahora son dos objetos.
- [ ] Verifiqué que ninguna parte del trabajo requiere alfa, rotoscopia, tracking planar o
      precomposiciones — porque nada de eso existe en CapCut.
