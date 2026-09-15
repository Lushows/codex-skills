# 29 — El corte final

**Qué resuelve:** saber **cuándo parar**. La mayoría de los videos no se arruinan por falta de trabajo,
sino por exceso: la vuelta número doce que agregó un efecto, aceleró un corte y le quitó el aire a lo
único que funcionaba. Este módulo te da las señales de sobre-edición, la prueba de dejarlo reposar, y
el criterio para decir "está listo" sin mentirte.

---

## 1. La curva de calidad de un montaje

Todo montaje sigue la misma forma:

```
calidad
   │              ╭──────╮
   │           ╭──╯      ╰──╮
   │        ╭──╯            ╰────╮
   │     ╭──╯                    ╰────
   │  ╭──╯
   └──┴────┴────┴────┴────┴────┴────┴──→ vueltas
      1    2    3    4    5    6    7

   Vuelta 1-2:  montaje bruto. Feo pero funcional.
   Vuelta 3-4:  ZONA ÓPTIMA. Todo lo importante ya está.
   Vuelta 5:    últimos ajustes reales.
   Vuelta 6+:   empiezas a quitarle vida.
```

La parte incómoda: **desde adentro no notas dónde está el pico.** A la vuelta siete sientes que estás
mejorando porque estás haciendo cosas. Por eso necesitas señales externas, no tu sensación.

---

## 2. Las señales de sobre-edición

Si dos o más de estas se cumplen, ya pasaste el pico.

### a) Estás cambiando cosas que ya cambiaste

Moviste un corte de 3,40 a 3,25 y ahora lo estás moviendo a 3,35. Eso no es refinar: es girar en el
sitio. La primera decisión probablemente estaba bien.

**Prueba objetiva:** lleva un registro de cambios. Si un mismo elemento aparece tres veces, para.

### b) Los cambios ya no tienen razón, tienen adjetivo

Cuando dejas de decir "este corte parte una palabra" y empiezas a decir "quiero que se sienta más
dinámico", entraste en territorio de gusto. Los cambios con razón concreta mejoran; los cambios con
adjetivo son ruleta.

### c) Cada corte tiene un efecto

Cuenta cuántos cortes llevan transición. Si pasa del 10%, estás decorando.

```bash
# Cuantos cambios de escena hay en total
ffmpeg -hide_banner -i final.mp4 -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2> e.txt
grep -c "pts_time" e.txt
```

Compara ese número con cuántas transiciones metiste conscientemente.

### d) El pulso bajó de 1,2 s

Empezaste a apretar cortes "para que sea más dinámico" y te pasaste. Por debajo de 1,2 s es ruido y baja
la retención (módulo `20`).

```bash
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 final.mp4)
N=$(grep -c "pts_time" e.txt)
awk -v d="$DUR" -v n="$N" 'BEGIN{p=d/(n+1); printf "pulso = %.2f s ", p; if(p<1.2) print "  <-- SOBRE-EDITADO"; else print ""}'
```

### e) Ya no queda ni un silencio

Un video hablado sano tiene pausas de 0,15–0,35 s entre ideas. Si `silencedetect` no encuentra
absolutamente nada, apretaste de más y el video agota.

```bash
ffmpeg -hide_banner -i final.mp4 -af "silencedetect=noise=-40dB:d=0.12" -f null - 2>&1 | grep -c silence_start
```

Cero resultados en un video hablado de 30 segundos = problema.

### f) La voz suena procesada

Le pasaste denoise, EQ, compresor, saturador, exciter y limitador buscando "que suene pro" y ahora suena
a robot de banco. Menos es más: si la voz suena artificial, quita módulos hasta que vuelva a sonar
humana (módulo `70`).

### g) El color ya no se parece a la realidad

Tres capas de LUT y curvas encima. La piel salió naranja o verde. La corrección de color se juzga con la
piel: si la piel se ve mal, todo está mal (módulo `67`).

### h) No sabes explicar por qué está algo

Te preguntan "¿por qué ese flash ahí?" y no tienes respuesta. Todo elemento tiene que tener una razón de
una frase. Si no la tiene, sale.

### i) El archivo se llama `final_final_v3_bueno`

Suena a chiste y es un indicador real: la nomenclatura descontrolada es síntoma de que el proyecto no
tiene criterio de cierre (módulo `96`).

---

## 3. El test de dejarlo reposar

La única técnica que de verdad funciona para recuperar objetividad.

### Cómo se hace

1. **Exporta el corte.** No lo dejes en la línea de tiempo: exporta el MP4 real.
2. **Ciérralo todo.** No lo vuelvas a abrir.
3. **Espera.** Los tiempos que sirven:

| Tiempo de reposo | Qué recuperas |
|---|---|
| **20 minutos** | Los errores obvios que dejaste de ver por costumbre |
| **2 horas** | La percepción de ritmo |
| **Una noche** | El juicio completo. Este es el bueno. |
| Una semana | Demasiado: ya no recuerdas por qué tomaste ciertas decisiones |

4. **Vuelve a verlo una sola vez, entero, sin pausar.** Sin la línea de tiempo abierta. En el dispositivo
   donde se va a ver (el celular, no el monitor de 27 pulgadas).
5. **Anota SOLO lo que te saltó.** No busques errores: anota lo que te sacó del video sin que lo
   estuvieras buscando.

### Por qué funciona

Después de la vuelta cinco ya no ves el video: ves tu memoria del video. Sabes lo que viene, entiendes
las decisiones, y tu cerebro rellena lo que falta. El reposo borra ese caché y vuelves a verlo como lo
va a ver un desconocido.

### La regla de las tres notas

Si al volver anotas **tres cosas o menos**, el video está listo. Arréglalas y entrega.

Si anotas **diez**, no estaba listo y lo sabías.

Si anotas **cero**, o el video está perfecto o no lo viste de verdad. Vuelve a verlo en el celular con
el sonido a la mitad, como lo va a ver la gente.

---

## 4. Los tests que reemplazan tu opinión

Como no puedes confiar en tu percepción después de la quinta vuelta, usa pruebas que no dependan de ella.

### Test 1 — El primer segundo aislado

```bash
ffmpeg -hide_banner -y -t 1.5 -i final.mp4 -c:v libx264 -crf 18 -c:a aac primer_segundo.mp4
```

Mira solo eso. Si ese segundo y medio no te da curiosidad, el video no funciona por más bueno que sea el
resto.

### Test 2 — Sin sonido

Reprodúcelo en silencio de principio a fin. La mayoría de la gente lo va a ver así.

**Pregunta:** ¿se entiende qué se está ofreciendo? Si no, faltan textos (módulo `40`).

### Test 3 — Solo el audio

```bash
ffmpeg -hide_banner -y -i final.mp4 -vn -c:a mp3 solo_audio.mp3
```

Escúchalo sin imagen. Si suena a robot, entrecortado, o con saltos de volumen, la imagen no lo va a
salvar. Este test caza cortes malos que visualmente pasan desapercibidos.

### Test 4 — La tira de fotogramas

```bash
ffmpeg -hide_banner -y -i final.mp4 -vf "fps=1,scale=200:-1,tile=10x4" -frames:v 1 tira_final.png
```

De un vistazo ves: si hay variedad visual, si hay zonas muertas, si el color es coherente.

### Test 5 — La verificación técnica

Esta no es opinión, es medición. Es el módulo `98` completo. Como mínimo:

```bash
V=final.mp4
echo "--- duracion, resolucion, fps ---"
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate:format=duration \
  -of default=noprint_wrappers=1 "$V"

echo "--- loudness (objetivo ~-14 LUFS para redes) ---"
ffmpeg -hide_banner -i "$V" -af "loudnorm=print_format=summary" -f null - 2>&1 | grep -E "Input (Integrated|True Peak)"

echo "--- silencios colgando al final ---"
ffmpeg -hide_banner -i "$V" -af "silencedetect=noise=-45dB:d=0.5" -f null - 2>&1 | grep silence_start | tail -2

echo "--- ultimo fotograma (no debe ser negro) ---"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
ffmpeg -hide_banner -y -ss $(awk -v d="$DUR" 'BEGIN{printf "%.2f", d-0.08}') -i "$V" -frames:v 1 ultimo.png
```

### Test 6 — La persona que no sabe nada

El más valioso y el más incómodo. Se lo muestras a alguien que no ha visto ninguna de las versiones y
le haces **una sola pregunta**:

> "¿De qué se trata?"

Si no lo puede decir en una frase, el video no comunicó. No preguntes "¿te gustó?" — nadie te va a decir
la verdad y además el gusto no es la métrica.

---

## 5. El criterio de "está listo"

Un montaje está terminado cuando se cumplen las cinco condiciones. No cuatro: las cinco.

1. **Todas las verificaciones técnicas pasan.** Ninguna palabra cortada, loudness en rango, sin negro
   al final, resolución y fps correctos. Módulo `98`.
2. **El video cumple su objetivo declarado.** Si era vender, se entiende qué se vende y qué hacer
   después. Si era enseñar, se aprende.
3. **Al volver después de reposar, anotaste tres cosas o menos.**
4. **Cada elemento tiene una razón que cabe en una frase.** Todos. Si hay uno que no, sale.
5. **Los cambios que quedan son de gusto, no de función.** Cuando lo único que queda por discutir es si
   la música te gusta o no, terminaste.

---

## 6. Qué hacer con las ganas de seguir tocando

Son reales y hay que darles a dónde ir.

### a) Guarda la versión y bifurca

```bash
cp final.mp4 v03_aprobado.mp4
```

Ahora experimenta sobre una copia. Si la versión experimental resulta mejor, la comparas lado a lado:

```bash
ffmpeg -hide_banner -y -i v03_aprobado.mp4 -i v04_experimento.mp4 \
  -filter_complex "[0:v]scale=540:960[a];[1:v]scale=540:960[b];[a][b]hstack" \
  -c:v libx264 -crf 20 -an comparacion.mp4
```

Verlas juntas mata la discusión en 30 segundos. Casi siempre gana la más simple.

### b) Anota para el siguiente

La mayoría de las ideas tardías no son para este video: son aprendizajes. Escríbelas en una lista de
"para el próximo" y sigue. Ahí es donde se acumula el estilo propio (módulo `196`).

### c) Acepta el límite del material

Muchas ganas de seguir editando son en realidad frustración con el material. Si el plano está movido,
la luz es fea o la persona se trabó, **ninguna cantidad de edición lo arregla**. Dilo:

> "Este video está en su techo con este material. Para subir de aquí hay que volver a grabar el bloque
> del minuto 0:12."

Eso es más profesional que entregar la vuelta quince y culpar al montaje.

---

## 7. La entrega

Cuando cierras, cierras con tres cosas (es el cierre estándar de toda esta skill):

1. **Qué se hizo y por qué.** Una frase sobre la decisión de montaje, no una lista de filtros.
   > "Lo monté con la voz continua y la imagen picada para que el pulso quedara en 1,8 s sin partir
   > ninguna palabra."

2. **Qué se verificó y con qué medida.**
   > "Transcribí el resultado final y ninguna palabra queda cortada. Loudness a -14,2 LUFS. Sin negro
   > al final. Pulso medido: 1,84 s por cambio."

3. **Qué no puedes juzgar.** Honestidad explícita.
   > "No puedo juzgar si la música pega con la marca ni si el chiste del segundo 14 da risa. Eso lo
   > decides tú."

Nunca finjas haber visto o escuchado algo que no verificaste.

---

## Errores comunes

1. **Seguir editando porque queda tiempo.** El tiempo disponible no es criterio de calidad. Si está
   listo a la vuelta cuatro, se entrega en la vuelta cuatro.
2. **Juzgar el corte sin haberlo dejado reposar.** Después de la quinta vuelta ves tu memoria del video,
   no el video. Una noche cambia todo.
3. **Revisar en el monitor grande un video que se va a ver en un celular.** El texto que se lee perfecto
   en 27 pulgadas es ilegible en 6.
4. **Preguntar "¿te gustó?".** Nadie dice la verdad y el gusto no es la métrica. Pregunta "¿de qué se
   trata?".
5. **Apretar el pulso por debajo de 1,2 s en la última vuelta** buscando dinamismo. Empeora la retención.
6. **Apilar procesos de audio hasta que la voz suena a robot.** Si suena artificial, quita módulos.
7. **Meter un efecto que no sabes justificar.** Si no cabe la razón en una frase, sale.
8. **No guardar la versión aprobada antes de experimentar.** Pierdes la buena persiguiendo la perfecta.
9. **Confundir "el material es limitado" con "el montaje está incompleto".** Reconoce el techo y dilo,
   en vez de dar veinte vueltas.
10. **Entregar sin correr la verificación técnica** porque "se ve bien". Ver bien no es estar bien.
11. **Cambiar cosas ya cambiadas.** Girar en el sitio se siente como trabajar y no lo es.
12. **Entregar sin decir qué no pudiste juzgar.** El cliente merece saber qué queda a su criterio.

---

## Checklist

Este es el último checklist antes de entregar. Si algo falla, no está listo.

- [ ] Corrí la **verificación técnica completa** (`98`): duración, resolución, fps, loudness, sin negro
      al final, sin palabras cortadas.
- [ ] **Dejé reposar** el corte al menos una noche y lo volví a ver **una sola vez, entero, sin pausar**.
- [ ] Al volver anoté **tres cosas o menos**.
- [ ] Lo vi en el **dispositivo real** donde se va a consumir.
- [ ] Pasé el **test del primer segundo** aislado.
- [ ] Pasé el **test sin sonido**: se entiende qué se ofrece.
- [ ] Pasé el **test de solo audio**: no suena entrecortado ni robótico.
- [ ] Saqué la **tira de fotogramas** y hay variedad visual y color coherente.
- [ ] El **pulso está entre 1,5 y 2,0 s** — no lo apreté por debajo de 1,2 en la última vuelta.
- [ ] Quedan **pausas naturales**; `silencedetect` encuentra silencios de 0,15–0,35 s.
- [ ] **Cada elemento tiene una razón** que cabe en una frase.
- [ ] Menos del **10% de los cortes** llevan transición.
- [ ] La **piel se ve natural** (ni naranja ni verde).
- [ ] Se lo mostré a alguien nuevo y **supo decir de qué se trata** en una frase.
- [ ] Guardé la **versión aprobada** con nombre claro antes de experimentar con nada más.
- [ ] En la entrega dije **qué hice, qué verifiqué y qué no puedo juzgar**.
