# 70 · Cuándo usar una transición

**Qué resuelve:** decidir, en cada unión entre dos escenas, si hay que hacer algo o si
simplemente se corta. La respuesta por defecto es cortar.

---

## La regla

> **El 90% de las uniones van a corte duro. Una transición es un signo de puntuación:
> si todas las frases llevan coma, ya no hay frases.**

Un episodio de 6 escenas tiene **5 uniones**. Como máximo **2** llevan algo distinto de
un corte seco. Cuando llevan más, el episodio deja de leerse como un documental y pasa a
leerse como una plantilla: el espectador aprende el patrón y empieza a ver el montaje en
lugar de la historia.

Hay además una razón material: el pipeline concatena las escenas con
`concat -c copy` (`motor.py`, `main()`), que es instantáneo y sin pérdida. **Toda unión
que no sea corte duro obliga a recodificar** ese tramo y a recalcular la duración total
(`79`). Cada transición cuesta minutos de render y un riesgo de descuadre con la voz.

## Las cuatro razones válidas

| # | Razón | Qué le pasa al espectador | Recurso | Duración |
|---|---|---|---|---|
| 1 | **Salto de tiempo** — "catorce años después" | Necesita soltar el presente | `xfade=fade` o pase de página | 0,40-0,50 s |
| 2 | **Cambio de lugar** — de Medellín a un juzgado de Miami | Tiene que reorientarse | Barrido de papel o por elemento (`71`, `73`) | 0,32-0,40 s |
| 3 | **Cambio de capítulo** — se cierra "cómo lo construyó" y abre "cómo cayó" | Tiene que entender que empieza otra cosa | Tachado rojo de marca (`77`) | 0,44 s |
| 4 | **El remate** — última escena del episodio | Tiene que saber que terminó | `fadeblack` + `tr_cierre` | 0,80 s |

Fuera de estas cuatro, **corte duro**.

## Lo que NO es una razón

| Excusa habitual | Qué está pasando de verdad | Arreglo real |
|---|---|---|
| "El corte queda raro" | Las dos escenas tienen la misma composición: el peso visual está en el mismo sitio y el ojo no registra el cambio | Cambiar la composición de una de las dos (`21`, `29`), no tapar el corte |
| "El fondo cambia mucho de color" | La paleta del episodio no está planificada | `51` recorrido de color; una transición no arregla un salto de temperatura |
| "Hay que rellenar ese medio segundo" | Falta un evento, no una transición | `11` el hueco prohibido |
| "Para que se vea profesional" | Lo profesional es lo contrario: los documentales caros cortan seco | — |
| "Quedó bonita" | Es la razón por la que los canales se vuelven todos iguales | — |

## El test de las tres preguntas

Antes de poner cualquier cosa en una unión:

1. **¿Cambió el CUÁNDO, el DÓNDE o el DE QUÉ?** Si no cambió ninguno → corte duro.
2. **¿Lo puedo resolver solo con sonido?** Un corte duro con un `tr_whoosh` que entra
   4 fotogramas antes ya se lee como transición (`75`). Si sirve → corte duro + efecto.
3. **¿Usé esta misma transición en la unión anterior?** Si sí → otra, o corte duro (`78`).

Sólo si las tres respuestas lo piden, se construye la transición.

## Presupuesto de un episodio de 6 escenas

| Unión | Qué separa | Decisión típica |
|---|---|---|
| 1→2 | Gancho → contexto | **corte duro** (+ `tr_whoosh` adelantado) |
| 2→3 | Contexto → construcción | **corte duro** |
| 3→4 | Construcción → el momento en que cruza la raya | **tachado rojo** (`77`) |
| 4→5 | La raya → la caída | **corte duro** (idealmente match cut, `72`) |
| 5→6 | La caída → el remate | **barrido de papel** (`71`) o corte duro |
| fin | Remate → negro | **fadeblack 0,80 s** (`76`) |

Dos transitorias más el cierre. Ese es el techo.

## El corte duro no es "no hacer nada"

Un corte duro se prepara igual que una transición:

- El último elemento de A **sale 0,2-0,4 s antes** del final de la escena, para que el
  corte caiga sobre un cuadro ya limpio (`76`).
- El primer elemento de B entra **a los 0,3-0,6 s**, nunca en el fotograma 0: una escena
  que arranca con todo ya colocado se lee como imagen fija.
- El **fondo de B ya viene en movimiento** desde su primer fotograma (`zoompan` arranca
  en el 0), así el corte revela movimiento, no una lámina.
- La **dirección del movimiento cambia** respecto a la escena anterior (`38`). Si A se
  acercaba, B se aleja o deriva. Esto solo ya hace que el corte se sienta.

Con esos cuatro cuidados, el 90% de las uniones no necesitan nada más.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Poner un fundido en cada unión "por si acaso" | El episodio pierde nervio; todo pasa en una nube blanda y el ritmo medido (`17`) se desploma |
| Tapar con una transición un corte que falla por composición | El defecto sigue ahí, ahora con medio segundo de más |
| Usar transición dentro de una misma escena | Una escena es una unidad continua; si necesita cortarse, son dos escenas |
| Meter `xfade` sin recalcular el total | El vídeo se acorta `duración` segundos por transición y la voz se descuadra a partir de ahí (`79`) |
| Decidir la transición en el render | Se decide en el guion visual, con el guion delante; en el render ya no se sabe qué cambió de tiempo o lugar |

## Relacionado

`71` · `72` · `73` · `75` · `76` · `78` · `79`
