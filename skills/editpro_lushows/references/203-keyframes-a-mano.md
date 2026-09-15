# 203 — Keyframes a mano

**Qué resuelve:** las animaciones que trae el editor cubren el 90% de lo que necesitas (`202`). Este
módulo es sobre el otro 10%: **cuándo vale la pena animar algo a mano**, cómo se hace sin perder la
tarde, y por qué la mayoría de la gente que aprende keyframes empieza a animarlo todo y sus videos
empeoran.

El módulo `84` explica la matemática de las curvas y cómo escribirlas en ffmpeg. Este es el de
**criterio y oficio en el editor**: dónde poner el punto, cuántos poner, qué propiedad tocar y cuándo
no tocar nada.

---

## 1. Tu proporción ya es la correcta

En 51 proyectos tienes **126 keyframes repartidos en solo 12 segmentos**. Vale la pena leer bien ese
número:

- **12 segmentos de cientos.** Animas a mano en menos del 5% de los clips.
- **10,5 keyframes por segmento animado.** Cuando entras a animar, no pones dos puntos: construyes un
  movimiento de verdad.

Esa es exactamente la proporción sana, y es rarísima. La mayoría de la gente hace lo contrario: dos
keyframes en cuarenta clips distintos. Resultado: cuarenta movimientos mediocres en vez de tres
movimientos buenos.

> **La regla que ya sigues sin saberlo:** el keyframe a mano es una herramienta de **momento**, no de
> mantenimiento. Se usa poco y se usa a fondo.

Lo único que cambia este módulo es que ahora vas a saber *cuáles* son esos momentos, en vez de
encontrarlos por intuición.

---

## 2. Qué es un keyframe, en el editor

> **Keyframe (fotograma clave):** un punto en el tiempo donde tú fijas el valor de una propiedad. "En
> el segundo 2 el texto está aquí y mide 100%; en el segundo 2,4 está allá y mide 130%." El editor
> rellena todo lo del medio.

En CapCut, es el **rombo** que aparece arriba a la derecha del panel de la propiedad. Cuando lo
presionas, se crea un punto en la línea de tiempo. A partir de ahí, cada vez que muevas el cursor a
otro momento y cambies el valor, se crea otro punto automáticamente.

**La mecánica correcta, en orden, para que no te pelees con la herramienta:**

1. Pon el cursor **donde termina** el movimiento (la posición final, la buena).
2. Ajusta el elemento como quieres que quede al final.
3. Presiona el rombo. Ese es tu keyframe final.
4. Mueve el cursor **hacia atrás**, a donde empieza el movimiento.
5. Cambia el valor (muévelo fuera de cuadro, hazlo más pequeño, bájale la opacidad). Se crea el
   keyframe inicial solo.

**Por qué al revés:** porque la posición que de verdad importa es la final — es la que el espectador
va a mirar durante segundos. Si empiezas por el principio, terminas ajustando la posición buena con el
elemento ya animado encima y es un dolor de cabeza.

---

## 3. Cuándo vale la pena (y cuándo no)

### Vale la pena

**1. El elemento tiene que ir a un sitio específico del cuadro.** Una flecha que señala la promoción
que está pegada en la pared, un círculo que rodea la cara de alguien. Ninguna animación de plantilla
sabe dónde está tu pared.

**2. El movimiento tiene que sincronizar con algo del video.** El gráfico entra en el instante en que
la persona levanta el vaso. Las animaciones de plantilla entran cuando entra el clip.

**3. Empuje de cámara sobre una foto o una ilustración fija.** Es el uso número uno del keyframe a
mano y por sí solo justifica aprenderlo (`83`).

**4. Un movimiento con carácter que se va a repetir en todos tus videos.** Vale la pena construirlo
una vez bien y guardarlo como plantilla (`88`, `208`).

**5. Corregir un encuadre a lo largo del plano.** El sujeto se movió y se salió del centro: dos
keyframes de posición lo reencuadran sin que se note.

### No vale la pena

**1. Cuando una animación de plantilla hace lo mismo.** Si "Aparición progresiva" resuelve, resuelve.
Animar a mano lo mismo es una hora perdida y probablemente peor.

**2. Cuando el elemento vive menos de un segundo.** No hay tiempo para que un movimiento hecho a mano
se aprecie.

**3. Cuando ya hay tres cosas moviéndose.** Ver presupuesto de movimiento en `200`.

**4. Cuando lo estás haciendo porque aprendiste a hacerlo.** Es la causa real de la mitad de los
keyframes del mundo.

---

## 4. Las cuatro propiedades, y cuál toca cuál

Solo hay cuatro propiedades que valen la pena animar. Cada una tiene una lectura emocional distinta y
mezclarlas mal es lo que produce movimiento confuso.

| Propiedad | Qué comunica | Rango sano | Cuidado |
|---|---|---|---|
| **Posición** | dirección, intención, "viene de" | lo que haga falta | movimiento perfectamente recto se ve mecánico |
| **Escala** | importancia, cercanía, énfasis | 92% – 115% para entradas; 100% – 112% para empujes | pasar de 130% en un elemento pequeño lo pixela |
| **Opacidad** | presencia, aparición | 0 – 100 | animarla junto con posición larga se ve sucio |
| **Rotación** | informalidad, humor, caída | **máximo 8 grados** | es la que más rápido arruina un video |

**La regla del par:** anima **una propiedad, o dos como máximo**. Tres o más y el movimiento se
vuelve ilegible: el ojo no puede seguir un elemento que a la vez se mueve, crece, gira y aparece.

Los pares que funcionan:

- **Opacidad + escala** → la entrada canónica (`202`). El par más útil que existe.
- **Posición + opacidad** → algo que llega desde fuera y se materializa. Bien para elementos pequeños.
- **Escala + posición** → empuje de cámara sobre una foto. El único caso donde mover mucho está bien.
- **Rotación + escala** → un sello que cae. Uno por video, si acaso.

Los pares que no:

- **Posición larga + rotación** → parece que se le cayó al editor.
- **Opacidad + rotación** → mareo puro.

---

## 5. El error de animar todo linealmente

Este es el punto que más diferencia produce y el que más se ignora.

**Por defecto, los keyframes son lineales.** El editor reparte el cambio en partes iguales entre un
punto y otro: si el elemento tiene que recorrer 300 píxeles en 12 fotogramas, avanza 25 píxeles en
cada uno, exactamente igual.

Nada en el mundo físico se mueve así. Todo arranca acelerando y termina frenando. Cuando el ojo ve un
movimiento perfectamente uniforme, no piensa "qué animación tan limpia": piensa **"esto lo hizo una
máquina"**, y esa sensación es la que hace que un video se vea barato.

### Cómo se arregla en CapCut

Haz clic derecho sobre el keyframe (o mantén presionado, en móvil). Aparecen opciones de velocidad del
keyframe con nombres tipo **Ease in**, **Ease out**, **Ease in-out**, o una curva editable.

La traducción que necesitas:

| Lo que hace el elemento | Qué le pones |
|---|---|
| **Entra** (llega a su sitio) | **Ease out** — llega rápido y frena |
| **Sale** (se va) | **Ease in** — arranca despacio y acelera |
| **Va de A a B y se queda** | **Ease in-out** — arranca suave y frena suave |
| **Empuje de cámara lento sobre foto** | **lineal está bien**, es la única excepción |

Esa última excepción vale la pena explicarla: un empuje de cámara de 3 segundos que va de 100% a 108%
es tan lento que el ojo no percibe la velocidad, solo el desplazamiento. Ahí el lineal no molesta y
además se siente más "cámara". En todo lo demás, curva.

### Cómo se comprueba sin reproducir

Exporta el tramo y saca una tira de fotogramas:

```bash
ffmpeg -ss 1.9 -i salida.mp4 -t 0.9 -vf "fps=25,scale=200:-1,tile=12x2" -frames:v 1 tira.png
```

Abre `tira.png` y mira el espaciado del elemento entre cuadrito y cuadrito:

- **Espaciado uniforme** → es lineal. Está mal (salvo empuje lento).
- **Saltos grandes al principio, casi imperceptibles al final** → ease out. Correcto para una entrada.
- **Casi quieto al principio, saltos grandes al final** → ease in. Correcto para una salida.

Diez segundos de trabajo y te dice la verdad, que es lo que la vista cansada a las 11 de la noche ya
no te dice.

---

## 6. Cuántos keyframes poner

**Dos.** Casi siempre dos: inicio y fin. Con la curva bien puesta, dos keyframes producen un
movimiento profesional.

Cuándo se justifican más:

- **Tres**, cuando el elemento entra, se queda y se va: keyframe de llegada, keyframe de "aquí empieza
  a irse", keyframe final. Los dos del medio tienen el mismo valor, y ese tramo plano es lo que hace
  que el elemento **se quede quieto** (la regla del doble, `202`).
- **Cuatro o más**, cuando hay un rebote, una anticipación, o un recorrido con curva (`85`).
- **Diez o más**, cuando estás construyendo algo de verdad, que es lo que tú haces en esos 12
  segmentos. Ahí el número no importa; importa que cada punto tenga una razón.

**El error de los keyframes de más:** poner puntos intermedios "para que se vea más suave". No hace
eso. Cada keyframe intermedio **rompe** la curva: convierte un movimiento fluido en una serie de
tramos con frenaditos. Si tu animación se ve entrecortada y tiene siete puntos, el arreglo es borrar
cinco.

---

## 7. Las tres recetas que resuelven casi todo

### Receta A — Empuje de cámara sobre una foto o ilustración

El uso número uno. Convierte una lámina muerta en un plano vivo.

- Keyframe 1, al principio del clip: escala **100%**, posición centrada.
- Keyframe 2, al final del clip: escala **108%**, posición desplazada 20–40 píxeles en diagonal.
- Curva: lineal está bien.
- Duración: mínimo 2,5 segundos. Por debajo de eso se nota y parece un zoom.

**El detalle que lo hace bueno:** que el desplazamiento sea *diagonal* y no solo escala. Un zoom puro
al centro se lee como zoom; un zoom con deriva se lee como cámara.

### Receta B — Flecha o círculo que señala algo

- Pon el elemento **donde va a señalar**, ajustado bien.
- Keyframe ahí (será el final).
- Retrocede 0,4 s: mueve el elemento 60–100 px hacia atrás en la dirección de donde viene y bájale la
  opacidad a 0.
- Curva: **ease out**.
- Déjalo quieto mínimo 1,2 s antes de sacarlo.

### Receta C — Reencuadre a lo largo del plano

El sujeto se salió del centro a mitad del clip.

- Keyframe al principio con el encuadre actual.
- Keyframe donde el sujeto ya se movió, con la posición corregida.
- Curva: **ease in-out** en los dos.
- **Máximo 6–8% de desplazamiento del ancho.** Más que eso se nota como paneo falso y además te obliga
  a escalar tanto que pierdes nitidez.

---

## 8. Keyframes a mano por código

Si estás generando el video por ffmpeg o construyendo un draft de CapCut por código (`112`), los
keyframes son expresiones. La forma completa está en `84`; aquí el patrón mínimo que cubre el 90%:

```bash
ffmpeg -i base.mp4 -i flecha.png -filter_complex "\
[1:v]format=rgba,fade=t=in:st=3.0:d=0.35:alpha=1,fade=t=out:st=5.4:d=0.22:alpha=1[f];\
[0:v][f]overlay=\
x='920 + 90*pow(1-clip((t-3.0)/0.4,0,1),3)':\
y=1180:enable='between(t,3.0,5.7)'" \
  -map 0:a -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

Léelo así: la flecha vive de 3,0 a 5,7 segundos. Su X final es 920. Durante los primeros 0,4 segundos
está desplazada hasta 90 píxeles a la derecha, y ese desplazamiento se va a cero con curva cúbica
(`pow(...,3)`), que es un **ease out**: llega rápido y frena. La opacidad la maneja `fade`, que ya trae
curva.

**El patrón general para memorizar:**

```
valor = VALOR_FINAL + DESPLAZAMIENTO * pow(1 - clip((t - INICIO)/DURACION, 0, 1), 3)
```

Cambia `pow(..., 3)` por `pow(..., 5)` si quieres un frenado más marcado. Nunca lo dejes sin `pow`:
eso sería lineal.

---

## Errores comunes

1. **Animar a mano lo que una plantilla ya resuelve.** Una hora perdida y un resultado peor.
2. **Dejar los keyframes lineales.** El error madre. Toda entrada lleva ease out, toda salida ease in.
3. **Empezar por el keyframe inicial.** Empieza por la posición final, que es la que importa.
4. **Animar tres o más propiedades a la vez.** El ojo no puede seguirlo. Máximo dos.
5. **Rotación de más de 8 grados.** Se lee como error, no como estilo.
6. **Poner keyframes intermedios "para suavizar".** Hacen lo contrario: rompen la curva en tramitos.
7. **Escalar por encima de 130% en un gráfico pequeño.** Se pixela y no hay vuelta atrás.
8. **Reencuadrar más del 8% del ancho.** Se nota como paneo falso y pierdes nitidez.
9. **Empuje de cámara de menos de 2,5 segundos.** Se lee como zoom, no como cámara.
10. **Empuje puro al centro sin deriva.** Zoom de PowerPoint. Métele diagonal.
11. **No dejar tramo plano entre entrada y salida.** El elemento nunca se queda quieto y nadie lo lee.
12. **Animar a mano un elemento que vive menos de un segundo.** No da tiempo de apreciarlo.
13. **Animar porque acabas de aprender a animar.** La causa real de la mitad de los keyframes del
    mundo. Si el video funcionaba sin eso, no lo pongas.
14. **No verificar con la tira de fotogramas.** A las 11 de la noche tu ojo miente; la tira no.

---

## Checklist

Antes de dar por buena una animación hecha a mano:

- [ ] Comprobé que **ninguna animación de plantilla** hacía lo mismo.
- [ ] El elemento vive en pantalla **más de un segundo**.
- [ ] Estoy animando **una o dos propiedades**, no tres.
- [ ] Si hay rotación, es de **8 grados o menos**.
- [ ] Empecé por el **keyframe final** y trabajé hacia atrás.
- [ ] Las entradas tienen **ease out**; las salidas, **ease in**.
- [ ] No hay **keyframes intermedios** que rompan la curva sin razón.
- [ ] Hay **tramo plano** en el medio: el elemento se queda quieto el doble de lo que tardó en entrar.
- [ ] Si es empuje de cámara: dura **2,5 s o más**, va del 100% al ~108% y tiene **deriva diagonal**.
- [ ] Si es reencuadre: el desplazamiento no pasa del **8%** del ancho.
- [ ] Ninguna escala pasa de **130%**.
- [ ] Saqué la **tira de fotogramas** y el espaciado confirma la curva.
- [ ] Sumando este elemento, no hay más de **tres cosas moviéndose** en ese segundo (`200`).
- [ ] Si este movimiento me gustó, lo **guardé como plantilla** para no reinventarlo (`88`).
