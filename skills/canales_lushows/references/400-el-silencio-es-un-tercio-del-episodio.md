# 400 · El silencio es un tercio del episodio

**Qué resuelve:** por qué un episodio se siente largo aunque la voz vaya a la velocidad
correcta, y cómo arreglarlo sin tocar ni una sílaba. Es el hallazgo que salió de ver el
episodio 1 terminado, y contradice lo que el canal creía sobre el ritmo.

---

## El síntoma y el diagnóstico equivocado

Luis vio el episodio 1 completo y volvió con una frase: *«me tocó verlo en 1,25 más
rápido y me enganchó más tanto en audio como en video»*.

La reacción natural es subir el `rate` de la voz. **Es la reacción equivocada**, y hay
que medir antes de tocarlo. La medida:

```
581 s de episodio  ·  419 s hablando  ·  162 s en SILENCIO  =  27,9%
```

La voz iba a 130-156 palabras por minuto según el minuto — el centro exacto del rango de
un documental (§ `281`). **No hablaba lento.** Casi tres minutos de los diez eran silencio.

## De dónde sale ese silencio

El reparto de las 228 pausas medidas es **bimodal**, y ahí está todo:

| Duración | Pausas | Suman | Qué son |
|---|---|---|---|
| 0,2 – 0,4 s | 93 | 28,5 s | comas. Están bien |
| 0,4 – 0,8 s | 1 | 0,4 s | casi nada: no hay término medio |
| más de 1,0 s | 126 | **134,9 s** | **puntos finales** |

edge-tts pone una pausa **fija de ~1,05 s detrás de cada punto**. El guion del episodio
tiene 135 puntos en 1.378 palabras — frases de diez palabras, que es buena escritura para
el oído (§ `95`). Pero diez palabras + un segundo de silencio, 135 veces seguidas, son
**dos minutos y cuarto de episodio sin nadie hablando**.

> La escritura corta y la pausa fija se multiplican. Cuanto mejor escribes para el oído,
> más te castiga el sintetizador. Es una trampa del medio, no del guion.

## El hallazgo que nadie había visto: la elipsis no existe

El guion marca sus golpes dramáticos con `···`. Medido sobre los diez minutos:

```
pausas de "···"  :  29, media 1,033 s
pausas de punto  :  95, media 1,035 s
```

**Idénticas.** El sintetizador ignora la elipsis por completo. Los 29 golpes dramáticos
escritos a mano en el guion **no existían en el audio**. Por eso el episodio se sentía
plano y largo a la vez: todo respiraba igual, y donde el relato pedía un silencio que
pesara, había el mismo silencio de siempre.

No se arregla escribiendo la elipsis de otra forma. Se arregla midiendo el audio ya
grabado y **recomponiendo las pausas**.

## La recomposición: se recorta el silencio, no la voz

`piloto/pausas.py`. La regla:

| Clase | Duración nueva | Por qué |
|---|---|---|
| punto final | **0,50 s** | respira y sigue |
| `···` (golpe) | **0,90 s** | casi el doble del punto: ahora SÍ se nota |
| coma | intacta | ya estaba bien |

Resultado medido en el episodio 1: **9:41 → 8:46**, silencio del 27,9% al 20,4%, picos
sin tocar (−9,5 dB), y las **únicas pausas largas que quedan en el episodio son los 29
golpes**. El ritmo que el guion declaraba por fin existe en el audio.

## Tres reglas de ejecución que no son opcionales

**1. Sobre el crudo, nunca sobre el máster.** La cadena de proceso (§ `286`) lleva `aecho`
y compresor. Si se corta después, se corta también la cola del eco de la frase anterior y
se oye un clic. Operando antes, el eco se genera sobre el audio ya recompuesto.

**2. No se rellena con ceros: se conserva el principio del silencio original.** El suelo
de ruido del sintetizador sigue siendo el mismo y la junta no se oye ni como clic ni como
bache.

**3. No se vuelve a sintetizar.** Llamar otra vez a edge-tts da **otra toma** — misma voz,
misma frase, otra interpretación — y la toma ya está aprobada. La cirugía se hace sobre el
`_crudo-minN.mp3` que ya existe: cada fonema sigue siendo exactamente el mismo.

## Qué NO hacer

- **No subir el `rate` como primera medida.** Acelerar la voz se oye; quitar silencio no.
  Si después de recomponer las pausas todavía arrastra, entonces sí se discute el `rate`.
- **No tocar las pausas de coma.** Están entre 0,2 y 0,4 s y son la respiración interna de
  la frase. Recortarlas es acelerar el habla por la puerta de atrás.
- **No aplicar un `atempo` global.** Cambia el timbre y comprime por igual lo que debe
  correr y lo que debe pesar.

## Relacionado

§ `281` (palabras por minuto) · § `282` (la puntuación como partitura) · § `286` (la
cadena de proceso) · § `124` (el silencio como instrumento) · § `401` (mover el audio
mueve el montaje) · § `289` (errores de locución)
