# 213 — Keyframes: animar a mano en CapCut

Las animaciones prehechas (módulo 212) resuelven el 90 % de los casos. Los keyframes son para el
10 % restante: cuando necesitás **exactamente** este movimiento, a esta velocidad, entre estos dos
momentos, y ninguna animación del catálogo lo hace.

Es la única herramienta de CapCut que se parece a un editor profesional de verdad. También es la más
tediosa. Este módulo es sobre cuándo vale la pena pagar ese precio.

---

## Qué es un keyframe, sin vueltas

Un keyframe es **una foto de un valor en un momento**.

Ponés dos: "en el segundo 0 el clip está al 100 % de tamaño" y "en el segundo 2 está al 130 %".
CapCut rellena todo lo del medio. Eso es todo. No hay más misterio.

El rombo (◇) que ves al lado de cada propiedad es el botón. Si está hueco, no hay keyframe en ese
punto. Si está lleno (◆), sí lo hay.

---

## Cómo se ponen (el flujo real)

1. Seleccioná el clip.
2. Poné la cabeza lectora **donde querés que empiece** el movimiento.
3. En el panel derecho, encontrá la propiedad (Escala, Posición, Rotación, Opacidad…).
4. Hacé clic en el **rombo** al lado. Se pone lleno: acabás de fijar el valor actual en ese momento.
5. Mové la cabeza lectora **al final** del movimiento.
6. **Cambiá el valor.** No toques el rombo — CapCut crea el segundo keyframe solo al detectar el
   cambio.
7. Listo. Reproducí.

El paso 6 es donde se confunde todo el mundo. **No hay que hacer clic en el rombo la segunda vez.**
Si lo hacés, ponés un keyframe con el mismo valor y no pasa nada. Solo cambiá el número y CapCut se
encarga.

### Para borrar

Poné la cabeza lectora exactamente encima del keyframe (se pone lleno) y hacé clic en el rombo. Se
vacía. O clic derecho sobre el rombo en la línea de tiempo → *Eliminar*.

### Para mover

Los keyframes aparecen como rombos pequeños sobre el clip en la línea de tiempo. Se arrastran. Ese es
el ajuste fino: primero ponés los valores, después movés los tiempos hasta que el ritmo quede bien.

---

## Qué se puede animar

Estas son las propiedades que valen la pena en la práctica:

| Propiedad | Dónde está | Para qué |
|---|---|---|
| **Escala** | Video → Básico | Zoom lento (Ken Burns), énfasis, golpe |
| **Posición** (X e Y) | Video → Básico | Paneo, entrada desde fuera, seguir a alguien |
| **Rotación** | Video → Básico | Inclinaciones, caídas, giros |
| **Opacidad** | Video → Básico | Fundidos personalizados, apariciones |
| **Volumen** | Audio | Bajar la música bajo la voz (ducking a mano) |
| **Máscara** (posición, tamaño, difuminado) | Video → Máscara | Revelados, barridos. Ver módulo 215 |
| **Parámetros de filtro / ajuste** | Ajustar | Cambio de color progresivo |
| **Croma** | Video → Croma | Rara vez, pero se puede |

Lo que **no** se puede animar: la mayoría de los parámetros internos de los efectos prehechos, la
velocidad (eso es otra herramienta, módulo 214), y el texto letra por letra (eso es animación de
texto, módulo 216).

---

## Cómo se ve por dentro

En el archivo de proyecto, cada keyframe se guarda dentro del segmento, en `common_keyframes` →
`keyframe_list`:

```json
{
  "curveType": "Line",
  "time_offset": 725160000,
  "values": [-0.24043715846994540],
  "left_control": { "x": 0, "y": 0 },
  "right_control": { "x": 0, "y": 0 },
  "id": "<GUID>"
}
```

Lo que hay que entender:

- **`time_offset`: 725160000** — microsegundos **desde el inicio del clip** (no desde el inicio del
  video). Eso son 725,16 segundos. Dividí por 1.000.000 para leerlo.
- **`values`** es un **arreglo**. Para escala u opacidad trae un solo número. Para posición trae dos
  (X e Y). El valor de arriba, `-0.24`, es una posición desplazada a la izquierda — CapCut usa
  coordenadas normalizadas, no píxeles.
- **`curveType`: "Line"** — la interpolación. `Line` es lineal: velocidad constante.
- **`left_control` / `right_control`** — los tiradores de Bézier. En `{x:0, y:0}` están apagados. Ahí
  vive el suavizado.
- **`id`** es un identificador único, tipo GUID. Cada keyframe tiene el suyo.

---

## Las curvas: dónde está la diferencia entre bonito y feo

Un movimiento lineal (`Line`) se ve **mecánico**. Nada en el mundo real arranca a velocidad máxima y
frena en seco. Todo acelera y desacelera.

CapCut te deja elegir la interpolación haciendo **clic derecho sobre el keyframe** en la línea de
tiempo:

| Curva | Qué hace | Cuándo |
|---|---|---|
| **Lineal** | Velocidad constante | Barridos técnicos, ducking de volumen. Casi nunca para movimiento visible. |
| **Suave / Ease in-out** | Acelera y frena | **El que querés el 80 % de las veces.** |
| **Entrada suave (ease in)** | Arranca lento, termina rápido | Algo que sale disparado |
| **Salida suave (ease out)** | Arranca rápido, frena | Algo que llega y se asienta. Muy útil para zooms de énfasis. |
| **Bézier personalizado** | Vos dibujás la curva | Cuando lo demás no da |

**La regla que más impacto tiene en todo este módulo:** poné *ease out* en el keyframe final de casi
todo. Un zoom que llega y frena suave se ve caro. El mismo zoom lineal se ve a plantilla de
PowerPoint.

Advertencia honesta: el editor de curvas Bézier de CapCut es **incómodo**. Los tiradores son
pequeños, no hay números, no hay presets guardables. Si necesitás curvas finas y repetibles, ese es
un síntoma de que el trabajo pertenece a After Effects (módulo 219).

---

## Los cinco movimientos que valen la pena

En la práctica real, 126 keyframes repartidos en apenas 12 segmentos dice algo importante: **los
keyframes se usan poco, pero cuando se usan, se usan en serio.** Un solo segmento puede tener 10 o 15
keyframes. Esa es la forma correcta de usarlos: concentrados en pocos momentos que importan.

Estos son los cinco que se ganan el tiempo que cuestan:

### 1. Ken Burns (foto que respira)

Una foto fija se ve muerta en video. Dos keyframes de escala arreglan eso.

- Segundo 0: Escala 100 %
- Final del clip: Escala 112 %
- Curva: suave en ambos

**Nunca más del 15 % de recorrido.** Si el zoom se nota, distrae. Alterná la dirección entre fotos
consecutivas (una acerca, la siguiente aleja) para que no se sienta repetitivo.

Si además querés paneo, movés la posición un poco en la misma dirección. Cuidado: si te pasás, sale
del cuadro y ves borde negro. Subí la escala base a 105 % para tener margen.

### 2. Zoom de énfasis

Alguien dice algo importante. Querés subrayarlo sin cortar.

- Justo antes de la palabra clave: Escala 100 %
- 4 fotogramas después: Escala 115 %
- Curva del segundo: **ease out** (llega y frena)
- Opcional: volver a 100 % un segundo después

Es rápido y funciona siempre. Es la alternativa elegante al corte de continuidad.

### 3. Ducking de volumen a mano

La música está alta, empieza la voz, hay que bajarla. El ducking automático de CapCut a veces bombea
raro. A mano:

- 0,3 s antes de la voz: Volumen 100 %
- Al empezar la voz: Volumen 25 %
- Al terminar la voz: Volumen 25 %
- 0,5 s después: Volumen 100 %

Cuatro keyframes, curva lineal (acá sí sirve lineal). Se oye profesional.

### 4. Revelado con máscara

Un texto o un elemento que aparece barriendo. Máscara lineal + keyframes de posición de la máscara.
Ver módulo 215 — pero el motor es keyframes.

### 5. Seguir a un sujeto en un plano abierto

Recortás con escala 150 % y animás la posición para que el sujeto quede siempre centrado. Es el
"tracking del pobre", y es más confiable que el tracking automático de CapCut. Para planos cortos, es
la mejor opción.

---

## Trucos que ahorran tiempo

**Copiar keyframes entre clips.** Clic derecho sobre el clip → *Copiar* → seleccioná el destino →
*Pegar atributos* (o `Ctrl + Alt + V`). Lleva las propiedades animadas. Es la forma de aplicar el
mismo Ken Burns a 20 fotos sin morirte.

**Trabajá al revés.** Poné primero el estado **final** (el encuadre que querés que quede), fijalo con
keyframe, y después andá al inicio y armá el estado de partida. Es más fácil porque el destino es lo
que importa.

**Ampliá la línea de tiempo antes de tocar keyframes.** Con el zoom bajo, los rombos quedan encimados
y vas a mover el que no era. `Ctrl + rueda del mouse`.

**Dos keyframes primero, ritmo después.** No trates de acertar el timing y el valor al mismo tiempo.
Poné los valores, después arrastrá los rombos hasta que el ritmo quede.

**Si el movimiento tiembla, tenés keyframes de más.** Cinco keyframes intentando hacer un movimiento
suave siempre se ven peor que dos con buena curva. Menos es más, literalmente.

**Si tenés que animar 5 elementos como un bloque, parate.** CapCut no tiene precomposiciones. Ese
trabajo es de After Effects. Ver módulo 219.

---

## Lo que los keyframes de CapCut NO pueden hacer

Sé honesto con vos mismo antes de invertir dos horas:

- **No hay editor de gráficos de valor.** No podés ver la curva de escala en el tiempo como una línea.
  Estás animando a ciegas, guiándote por la vista previa.
- **No hay números exactos en las curvas.** No podés escribir "ease out al 70 %".
- **No hay presets de curva guardables.** Cada vez lo hacés a mano.
- **No se pueden animar la mayoría de parámetros de efectos prehechos.**
- **No hay motion blur.** Un movimiento rápido con keyframes se ve entrecortado, porque le falta el
  arrastre que tendría en cámara real. Esto es lo que más delata a un movimiento hecho en CapCut.
- **No hay expresiones ni vínculos entre propiedades.**
- **No hay anclaje (anchor point) editable.** El punto sobre el que rota o escala un elemento es el
  centro, siempre. Si necesitás que rote sobre una esquina, no se puede directamente.

Esa última limitación es la que más frustra a quien viene de After Effects. No hay truco. Es así.

---

## Errores comunes

- **Hacer clic en el rombo dos veces.** El segundo keyframe se crea solo al cambiar el valor. Si le
  das al rombo, fijás el mismo valor y no pasa nada — y después no entendés por qué no se mueve.
- **Poner el primer keyframe con la cabeza lectora en el lugar equivocado.** Verificá siempre dónde
  está la cabeza antes de tocar el rombo. Es el error número uno.
- **Dejar todo lineal.** El movimiento mecánico es lo que hace que se vea a plantilla. Ease out en el
  keyframe final, casi siempre.
- **Zoom Ken Burns demasiado grande.** Más del 15 % se nota y marea. Menos es más.
- **Animar posición sin margen de escala.** Movés el clip y aparece borde negro. Subí la escala a
  105–110 % antes de empezar a mover.
- **Demasiados keyframes.** Cinco puntos intentando suavizar siempre salen peor que dos con curva
  buena.
- **Animar el clip y después estirarlo.** Los keyframes se quedan donde estaban en tiempo absoluto y
  el movimiento se desincroniza del clip. Terminá el largo del clip **antes** de animar.
- **Confundir `time_offset` con tiempo del video.** Está medido desde el inicio del clip, no del
  proyecto. Si movés el clip, el keyframe se mueve con él (eso está bien) — pero al leer el archivo
  no confundas los dos relojes.
- **Intentar hacer motion graphics complejos con keyframes de CapCut.** Si llevás más de 20 minutos
  en un movimiento, la herramienta es la equivocada.
- **No copiar atributos.** Hacer el mismo Ken Burns 20 veces a mano cuando `Ctrl + Alt + V` lo
  resuelve.

---

## Checklist

- [ ] Verifiqué dónde está la cabeza lectora antes de poner cada keyframe.
- [ ] Puse el primer keyframe con el rombo y el segundo **cambiando el valor**, no con el rombo.
- [ ] El clip ya tiene su duración final; no lo voy a estirar después de animarlo.
- [ ] Le puse curva a los keyframes; no dejé todo en lineal.
- [ ] El keyframe final tiene *ease out* si el movimiento tiene que llegar y asentarse.
- [ ] El Ken Burns no pasa del 15 % de recorrido y alterna dirección entre fotos.
- [ ] Si animé posición, subí la escala base para no ver borde negro.
- [ ] Usé la mínima cantidad de keyframes posible (casi siempre dos).
- [ ] Amplié la línea de tiempo antes de arrastrar rombos.
- [ ] Si tenía que repetir el movimiento, usé *Pegar atributos* (`Ctrl + Alt + V`).
- [ ] Si llevo más de 20 minutos peleando con un movimiento, ya me pregunté si esto es trabajo de
      After Effects.
