# 336 — Descartar: reconocer en treinta segundos la toma que no se salva

**Qué resuelve:** el tiempo que se pierde peleando con material muerto. Hay defectos que la edición
arregla y defectos que **no tienen arreglo**. Saber cuáles son cuáles es lo que separa una tarde
productiva de una tarde de terquedad.

---

## 1. Por qué cuesta tanto descartar

Tres razones, todas humanas:

- **El rodaje costó.** Costó montar la luz, costó pedirle a alguien que se pusiera delante de la cámara,
  costó cerrar el bar media hora. Botar esa toma se siente como botar el esfuerzo.
- **La toma tiene un momento bueno.** Casi todas lo tienen. Un segundo brillante dentro de una toma
  inservible sigue siendo inservible si el segundo brillante está desenfocado.
- **Ya se invirtió tiempo en ella.** Es la trampa clásica: llevo cuarenta minutos arreglando esto, no lo
  puedo botar ahora. Esos cuarenta minutos **ya se perdieron pase lo que pase**. La única pregunta viva
  es qué hago con los próximos cuarenta.

> **Descartar no destruye trabajo. Descartar tarde sí.**

---

## 2. Los cuatro defectos que no se arreglan

### a) Foco perdido sobre la cara

La información no está en el archivo. Ni la nitidez de CapCut, ni ningún modelo de "mejorar video" la
inventa: lo que hacen es **fabricar** detalle plausible, y en una cara eso se ve como plástico.

Comprobación en diez segundos:

```bash
# blurdetect SOLO en la zona de la cara (nunca en el cuadro completo)
ffprobe -v error -f lavfi "movie=frame.png,crop=80:90:230:380,blurdetect" \
  -show_entries "frame_tags=lavfi.blur" -of default=nw=1:nk=1
```

Compara ese número con el de la misma región en otra toma del mismo rodaje. Si es claramente más alto,
está más blanda. Y confírmalo mirando el recorte a tamaño real: los ojos y las pestañas son el juez.

### b) Altas luces quemadas

Un píxel en 255 no tiene información. Bajarle la exposición solo lo vuelve gris plano.

Comprobación exacta, verificada: binariza en 250 y mide la media.

```bash
# Porcentaje de píxeles totalmente quemados = YAVG / 2,55
ffprobe -v error -f lavfi "movie=frame.png,lutyuv=y='if(gte(val,250),255,0)',signalstats" \
  -show_entries "frame_tags=lavfi.signalstats.YAVG" -of default=nw=1:nk=1
```

Datos reales de las 16 tomas de Bendita Pola:

| Toma | Quemado en todo el cuadro | Quemado en la zona clave |
|---|---|---|
| 0 (escaleras, contraluz) | 4,19% | **54,8%** en el vano de la puerta |
| 6 (terraza, día) | 3,28% | — |
| 11 (barra, neón) | 0,27% | — |
| 3 (mano y botella) | 0,68% | — |

El 4,19% global de la toma 0 parece inofensivo. La medición por zona dice la verdad: **más de la mitad
del vano de la puerta está en blanco absoluto**, y esa puerta es justo lo que está detrás de la persona.
Otra vez el promedio global tapando el problema (`332`).

Umbrales de trabajo: por debajo del 1% es normal; entre 1% y 5% hay que mirar **dónde**; por encima del
10% en la zona del sujeto, la toma no se salva.

### c) Encuadre equivocado

Si la cabeza está cortada, si el sujeto quedó en el borde, si sobra medio cuadro de techo — se puede
reencuadrar **una vez** y poco. En vertical 9:16 grabado en vertical no hay margen: cualquier punch-in
mayor al 20% empieza a verse blando.

Y hay un caso sin arreglo: **el sujeto mirando fuera de cuadro hacia el lado equivocado**. Eso no es
encuadre, es dirección, y solo se corrige volviendo a grabar (`234`).

### d) Micro-movimiento y obturador rodante

El "gelatina" de un celular a pulso, o el temblor de alta frecuencia, se estabiliza a medias y siempre
cuesta nitidez y encuadre. Y si además el material tiene distorsión de obturador rodante (las verticales
se inclinan al mover la cámara rápido), no hay estabilizador que lo enderece.

```bash
# vidstabdetect deja un archivo con cuánto se mueve la cámara cuadro a cuadro
ffmpeg -i toma.mp4 -vf vidstabdetect=shakiness=8:result=temblor.trf -f null -
```

Si al abrir `temblor.trf` los desplazamientos son grandes y cambian de signo cada cuadro, es temblor de
alta frecuencia: se puede suavizar. Si son grandes y sostenidos, es una cámara que se movió: eso no es
defecto, es un movimiento, y se respeta o se descarta.

---

## 3. Lo que SÍ se arregla (para no descartar de más)

| Defecto | ¿Se arregla? | Cómo |
|---|---|---|
| Dominante de color | sí | corrección primaria (`61`, `250`) |
| Subexposición moderada | sí, hasta 1,5 pasos | subir y limpiar ruido (`71`) |
| Ruido de imagen | casi siempre | `hqdn3d`, `nlmeans` |
| Audio con eco o ruido | bastante | cadena de voz (`70`) |
| Encuadre un poco flojo | sí | punch-in hasta 20% (`26`) |
| Ritmo lento | sí | es literalmente el oficio |
| Muletillas y repeticiones | sí | corte y tapado (`262`) |
| Temblor suave | sí | `vidstab` |
| **Foco perdido** | **no** | — |
| **Altas quemadas** | **no** | — |
| **Cabeza cortada** | **no** | — |
| **Obturador rodante** | **no** | — |
| **Mirada al lado equivocado** | **no** | — |

La regla que resume la tabla: **lo que es una transformación de valores se arregla; lo que es información
que no se registró, no.**

---

## 4. El protocolo de treinta segundos

Por toma, en este orden. Al primer "no", se descarta y se pasa a la siguiente. No hay que completar el
protocolo.

1. **¿Se le ve la cara enfocada?** Mira los ojos a tamaño real. Si dudas, mide (`331`).
2. **¿Hay zonas quemadas donde importa?** Un vistazo, y si hay duda, el comando del `lutyuv`.
3. **¿El encuadre sirve para el puesto que le tocaba?** (`335`).
4. **¿La imagen está estable en el tramo que voy a usar?** No en toda la toma: en el tramo.
5. **¿El audio de ese tramo es usable?** Si no, ¿sirve la imagen sola con audio de otra toma?

La pregunta 5 es la que rescata material: **una toma se puede descartar por imagen y seguir viva por
audio**, y al revés. Descartar es por puesto, no en absoluto.

---

## 5. Descartar no es botar

Mueve los descartes a una subcarpeta `_descartes` dentro del material, con un `razones.txt` de una línea
por archivo:

```
lv_0_20260804123726.mp4  sujeto muy lejos, no aporta
lv_0_20260804142916.mp4  U=163, morado imposible, ni con corrección
lv_0_20260804122837.mp4  contraluz: inútil para recorte, SIRVE de establecimiento
```

Tres razones para no borrar:

1. En dos semanas hay que hacer la versión de 15 segundos y cambia lo que sirve.
2. Un descarte por imagen puede seguir sirviendo por audio o por ambiente (`296`).
3. Un descarte técnico puede ser un gancho o un blooper (`337`, `34`).

La tercera línea del ejemplo es el caso real de este bloque: la toma peor para recortar es una toma buena
para otra cosa. Si se hubiera borrado, se pierde.

---

## 6. Cuándo un defecto irreversible no importa

- **En el gancho.** El primer segundo perdona casi todo menos el aburrimiento (`335`).
- **Cuando el defecto es el contenido.** Un video sobre la barra oscura del bar puede tener la barra
  oscura. Un contraluz puede ser la imagen.
- **En un plano de menos de medio segundo.** Nadie enfoca la vista en 12 cuadros.
- **En un blooper.** Ahí el defecto es la gracia (`337`).
- **Detrás de un texto grande.** Si el 60% del cuadro va a estar tapado, el fondo blando da igual.

---

## Errores comunes

1. **Seguir con una toma porque ya se invirtió tiempo en ella.** Ese tiempo ya se perdió.
2. **Creer que la nitidez arregla el foco.** Sube el ruido y los bordes, no la información.
3. **Creer que un modelo de IA "mejora" una cara desenfocada.** Inventa una cara parecida. Se nota.
4. **Bajar la exposición de una zona quemada.** Queda gris plano, no queda cielo.
5. **Medir el quemado en todo el cuadro.** 4% global puede ser 55% en la zona que importa.
6. **Medir `blurdetect` global para juzgar el foco de la cara.** Recorta y mide ahí.
7. **Descartar en absoluto en vez de por puesto.** Una toma mala para recortar puede ser buena de
   establecimiento.
8. **Descartar por imagen sin revisar si el audio sirve.**
9. **Reencuadrar más del 20%** en material vertical de celular. Se vuelve blando.
10. **Estabilizar material con obturador rodante fuerte.** Empeora el bamboleo.
11. **Borrar los descartes.** Se necesitan para la segunda versión.
12. **No escribir la razón del descarte.** En una semana la discusión se repite completa.
13. **Descartar todo el rodaje porque el primer archivo estaba mal.** Es el error de `330` con el signo
    cambiado.

---

## Checklist

- [ ] Revisé **el foco en la cara**, a tamaño real, no en miniatura.
- [ ] Medí `blurdetect` **en la región del sujeto** si tenía dudas.
- [ ] Medí el **porcentaje quemado** en la zona que importa, no solo global.
- [ ] Verifiqué que el **encuadre** sirva para el puesto asignado (`335`).
- [ ] Revisé la estabilidad **del tramo** que voy a usar, no de toda la toma.
- [ ] Antes de descartar por imagen, revisé si **el audio** sirve.
- [ ] Antes de descartar en absoluto, me pregunté **para qué otro puesto** serviría.
- [ ] Separé los defectos **reversibles** de los **irreversibles** antes de invertir tiempo.
- [ ] Moví los descartes a `_descartes` con **una línea de razón** por archivo.
- [ ] No borré nada.
- [ ] Si un defecto irreversible cae en el gancho o detrás de un texto, lo **dejé pasar** a propósito.
- [ ] Paré de pelear con una toma en cuanto supe que el defecto no tenía arreglo.
