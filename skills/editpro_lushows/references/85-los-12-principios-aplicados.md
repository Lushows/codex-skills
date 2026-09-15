# 85 — Los 12 principios aplicados

**Qué resuelve:** te dijeron "hazlo más dinámico" y no sabes qué tocar. Los 12 principios de animación
que Ollie Johnston y Frank Thomas escribieron para Disney en 1981 no son teoría de dibujos animados:
son **el manual de por qué un movimiento se siente vivo o se siente muerto**. Aplican igual a un logo
que entra en un reel de 20 segundos. Este módulo traduce cada uno a un elemento concreto de video
social, con el comando que lo produce.

---

## 1. Por qué esto no es un capricho de dibujantes

Los principios describen cómo el cerebro humano interpreta el movimiento. Ese cerebro es el mismo hoy y
está mirando tu reel en un celular. Si tu logo desafía la física, se lee como falso, aunque el logo sea
hermoso.

**Los cuatro que más rendimiento dan en motion de marca**, si solo vas a aprender cuatro:

1. **Anticipación** — avisar antes de que pase.
2. **Aceleración y desaceleración** (slow in / slow out) — nada arranca ni frena de golpe.
3. **Exageración** — en pantalla pequeña, lo sutil no existe.
4. **Arcos** — nada vivo se mueve en línea recta.

Los otros ocho suman, pero estos cuatro son la diferencia entre "de plantilla" y "hecho por alguien".

La mecánica de las curvas está en `84`. Aquí está el **para qué**.

---

## 2. Estirar y encoger (squash and stretch)

**Qué dice:** los objetos se deforman al moverse. Una pelota se aplasta al golpear y se estira al caer.
Es lo que comunica **peso** y **material**: algo rígido se deforma poco, algo blando se deforma mucho.

**En video de marca:** un logo que aterriza se aplasta un 6% en vertical al llegar y vuelve. Un número
que aparece se estira un poco al entrar. Un personaje que salta se alarga en el aire.

**Cuidado:** en marcas el logo casi nunca se puede deformar (el manual lo prohíbe): el squash se aplica al **contenedor** (la pastilla de color detrás), no al logo.

```bash
# La pastilla detras del logo se aplasta al aterrizar y vuelve
ffmpeg -i base.mp4 -i pastilla.png \
  -filter_complex "[1:v]format=rgba,\
scale=w='iw*(1+0.07*sin(PI*clip((t-1.5)/0.22,0,1)))':h='ih*(1-0.07*sin(PI*clip((t-1.5)/0.22,0,1)))':eval=frame[pz];\
[0:v][pz]overlay=x=(W-w)/2:y=(H-h)/2" \
  -map 0:a -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

Se ancha 7% y se achata 7% al mismo tiempo (**el volumen se conserva**: si solo se ancha, parece que
creció). El `sin(PI*p)` hace que vaya de 0 a máximo y vuelva a 0.

**Regla:** 5–8% para marcas serias. 12–18% para marcas juguetonas. Más de 20% es caricatura.

---

## 3. Anticipación

**Qué dice:** antes de la acción principal hay un movimiento preparatorio, casi siempre en dirección
contraria. El brazo va atrás antes de lanzar.

**En video de marca:** el elemento que va a subir, primero baja 25 px. El texto que va a entrar por la
derecha, primero se asoma 15 px por el otro lado. El contador que va a dispararse hace una pausa mínima.

**Para qué sirve de verdad:** avisa al ojo. En un reel donde pasan cosas cada 1,5 segundos, el
espectador se pierde la entrada de un elemento si nada le dijo "mira acá". La anticipación es ese aviso.

```bash
# Baja 26 px durante 0,12 s y despues sube a su sitio con frenado
-filter_complex "[1:v]scale=-1:180,format=rgba[lg];\
[0:v][lg]overlay=x=(W-w)/2:\
y='if(lt(t,1.12), \
     (H-h-200)+26*(1-cos(PI*clip((t-1.0)/0.12,0,1)))/2, \
     st(0,clip((t-1.12)/0.42,0,1)); (H-h-200)+26-26*(1-pow(1-ld(0),3)) )'"
```

**Duración:** 0,08–0,14 s. Más de eso deja de leerse como impulso y se lee como error.

---

## 4. Puesta en escena (staging)

**Qué dice:** en cada momento tiene que estar clarísimo **dónde hay que mirar**. Una sola idea a la vez,
presentada de forma que no se pueda malinterpretar.

**En video de marca:** es el principio más violado del contenido social. Subtítulo grande + personaje
entrando + contador subiendo + logo parpadeando, todo al mismo tiempo. El ojo no elige: se rinde.

**La regla operativa:** **un protagonista por momento.** Si entra el personaje, el texto ya estaba ahí o
todavía no llegó. Si sube el contador, no hay nada más moviéndose.

**Cómo lo verificas:** en cualquier fotograma, ¿cuántas cosas se están moviendo? Si son más de dos, hay
problema de puesta en escena.

Herramienta práctica: oscurece todo lo que no es el protagonista.

```bash
# Oscurece el fondo mientras el gráfico es el protagonista
-filter_complex "[0:v]eq=brightness='-0.18*clip((t-2.0)/0.3,0,1)*clip((5.0-t)/0.3,0,1)'[bg];[bg][1:v]overlay=..."
```

---

## 5. Directo vs. pose a pose

**Qué dice:** dos formas de animar. **Directo** = dibujar fotograma tras fotograma sin saber a dónde vas
(orgánico, impredecible). **Pose a pose** = definir las poses clave y rellenar el medio (controlado,
planificado).

**En video de marca:** trabajas **pose a pose**, siempre. Defines el estado inicial y el final, y ffmpeg
rellena. El "directo" es lo que hace un modelo de IA de video, y por eso deriva e impredecible (`83`).

**El aprovechamiento real:** antes de escribir una expresión, **escribe las poses en una tabla**:

| t | y | escala | opacidad |
|---|---|---|---|
| 1,00 | fuera abajo | 0,85 | 0 |
| 1,12 | +26 px | 0,85 | 1 |
| 1,54 | final | 1,00 | 1 |
| 4,45 | fuera abajo | 1,00 | 0 |

Con esa tabla, las expresiones se escriben solas. Sin ella, escribes y borras durante media hora. Es
además la base de las plantillas de `88`.

---

## 6. Continuación y superposición (follow through / overlapping action)

**Qué dice:** las partes de un cuerpo no llegan todas al mismo tiempo. El abrigo sigue moviéndose
después de que la persona se detuvo. La cola llega después del perro.

**En video de marca: este es el principio más rentable y el más ignorado.** Si tienes tres elementos que
entran (logo, nombre, eslogan) y los haces entrar juntos, se ve como una diapositiva. Si entran
**escalonados 0,08 segundos**, se ve como motion profesional.

```bash
# Tres elementos con desfase de 0,08 s cada uno
-filter_complex "\
[1:v]format=rgba,fade=t=in:st=1.00:d=0.30:alpha=1[e1];\
[2:v]format=rgba,fade=t=in:st=1.08:d=0.30:alpha=1[e2];\
[3:v]format=rgba,fade=t=in:st=1.16:d=0.30:alpha=1[e3];\
[0:v][e1]overlay=x=(W-w)/2:y=760[c1];\
[c1][e2]overlay=x=(W-w)/2:y=960[c2];\
[c2][e3]overlay=x=(W-w)/2:y=1090[vout]"
```

**El desfase (stagger) que funciona:** 0,06–0,10 s entre elementos. Menos no se percibe; más se siente
lento y desconectado.

La otra mitad del principio: el elemento que llega a su sitio **no se detiene en seco**. Sigue un pelín
y vuelve. Eso es el sobre-impulso (`84`, ease out back).

---

## 7. Aceleración y desaceleración (slow in / slow out)

**Qué dice:** el movimiento arranca lento, acelera, y frena antes de parar. Es la base física de todo.

**En video de marca:** es literalmente el módulo `84`. Si solo aplicas un principio de los doce, que sea
este: cambiar lineal por ease out sube la calidad percibida más que cualquier otra cosa que hagas.

```bash
# Ease out cubico: llega y frena
y='st(0,clip((t-1.0)/0.5,0,1)); H-(H-(H-h-200))*(1-pow(1-ld(0),3))'
```

**Cómo lo verificas sin verlo correr:** la tira de fotogramas (`84`, sección 9). Los últimos 3–4 cuadros
de la entrada tienen que verse **casi idénticos**. Si el espaciado es uniforme, es lineal.

---

## 8. Arcos

**Qué dice:** casi todo movimiento natural describe un arco. Solo la maquinaria se mueve en línea recta.

**En video de marca:** un elemento que sube perfectamente vertical se ve mecánico. Con una desviación
lateral de 30–50 px durante el recorrido, se ve natural. Es invisible conscientemente.

```bash
overlay=\
x='(W-w)/2 + 44*sin(PI*clip((t-1.0)/0.5,0,1))':\
y='st(0,clip((t-1.0)/0.5,0,1)); H-(H-(H-h-200))*(1-pow(1-ld(0),3))'
```

También aplica al **movimiento de cámara**: un empuje diagonal (`83`) se siente más orgánico que un zoom
centrado perfecto, por la misma razón.

---

## 9. Acción secundaria

**Qué dice:** un movimiento pequeño que acompaña al principal y lo enriquece sin robarle protagonismo.
La persona camina (principal) y va silbando (secundaria).

**En video de marca:** el personaje llega a su sitio (principal) y queda flotando levemente (secundaria,
ver `82`). El texto entra (principal) y una línea de subrayado se dibuja después (secundaria).

```bash
# Flotacion como accion secundaria, empieza cuando termina la entrada
overlay=x=W-w-56:y='if(lt(t,3.45), <expresion de entrada>, (H-h-470)+9*sin(2*PI*(t-3.45)/2.4))'
```

**La regla:** la acción secundaria es **más pequeña y más lenta** que la principal. Si compite, deja de
ser secundaria y rompes la puesta en escena (principio 4).

---

## 10. Ritmo (timing)

**Qué dice:** cuántos fotogramas dura un movimiento define el peso del objeto y la emoción de la escena.
Lo mismo moviéndose en 6 fotogramas o en 30 son dos cosas distintas.

**En video de marca:** el timing es lo que hace que tu motion se sienta caro o barato, más que la forma.

| Duración | Lectura |
|---|---|
| 0,08 – 0,15 s | golpe, impacto, energía, algo liviano |
| 0,30 – 0,50 s | peso, presencia, algo importante llegó |
| 1,0 s o más | lento, premium... o aburrido. Rara vez lo que quieres |

**La regla de la coherencia:** todos los elementos del mismo tipo, en el mismo video, con el **mismo
timing**. Si un texto entra en 0,15 s y el siguiente en 0,40 s, se siente descuidado aunque cada uno por
separado esté bien. Esto es lo que fuerza la plantilla de `88`.

---

## 11. Exageración

**Qué dice:** la realidad literal se lee como sosa en pantalla. Hay que empujar un poco más allá para
que **se lea** como real.

**En video de marca, y esto es crítico en vertical:** tu video se ve en una pantalla de 6 pulgadas, con
el brillo bajo, en el bus, con el pulgar encima. **Lo sutil, en ese contexto, es invisible.**

Qué hay que exagerar:

- **Tamaño del texto:** lo que en tu monitor se ve grande, en el celular apenas se lee (`44`).
- **Contraste:** un gris sobre gris que en tu pantalla se distingue, en la calle no existe.
- **Amplitud del movimiento:** un desplazamiento de 15 px no se percibe. 60 px sí.
- **La reacción:** si el personaje se sorprende, que se sorprenda de verdad.

Qué **no** hay que exagerar: la duración. Exagerar el timing es hacerlo lento, y lento es aburrido.
Exageras la **amplitud**, no el **tiempo**.

**Cómo lo verificas:** mira el fotograma exportado a tamaño de miniatura, como 300 px de alto. Si no se
lee ahí, no se lee en el celular.

```bash
ffmpeg -ss 3.4 -i salida.mp4 -frames:v 1 -vf "scale=-1:300" prueba_pequena.png
```

---

## 12. Dibujo sólido

**Qué dice:** aunque sea 2D, los elementos deben sentirse con volumen, peso y ocupar espacio real.

**En video de marca:** un recorte pegado plano encima de un video se ve **pegado**. Lo que le da cuerpo:

- **Una sombra suave debajo.** No una sombra dura de PowerPoint: un óvalo difuminado al 25% de opacidad.
- **Coherencia de luz.** Si el video está iluminado desde la izquierda y tu personaje tiene la luz a la
  derecha, el ojo lo detecta como falso.
- **Un mínimo de perspectiva.** Un elemento que entra ligeramente girado y se endereza al llegar tiene
  más cuerpo que uno perfectamente frontal.

```bash
# Sombra suave bajo el recorte: se duplica la capa, se ennegrece, se difumina y se corre
-filter_complex "\
[1:v]scale=-1:620,format=rgba,split=2[pj][sh];\
[sh]colorchannelmixer=rr=0:gg=0:bb=0:aa=0.28,boxblur=18:2[shb];\
[0:v][shb]overlay=x=W-w-44:y=H-h-458[c1];\
[c1][pj]overlay=x=W-w-56:y=H-h-470[vout]"
```

La sombra va 12 px a la derecha y 12 px abajo respecto al personaje. Difuminada, al 28%. Esa sola cosa
hace que el recorte deje de verse como calcomanía.

---

## 13. Atractivo (appeal)

**Qué dice:** el elemento tiene que ser agradable de mirar. No "bonito": **legible, con carácter, con
una silueta que se reconoce.**

**En video de marca:** el test de la silueta. Rellena tu elemento de negro puro. ¿Se sigue reconociendo?
Si no, el diseño no es lo bastante distintivo y ningún movimiento lo va a salvar: el problema no es de
motion, es de diseño, y le toca a `directorcreativo_lushows`.

```bash
ffmpeg -i pj_alfa.png -vf "format=rgba,colorchannelmixer=rr=0:gg=0:bb=0" -y silueta.png
```

---

## 14. La tabla resumen

| # | Principio | Aplicación concreta | Módulo |
|---|---|---|---|
| 1 | Estirar y encoger | pastilla que se achata 7% al aterrizar | `84` |
| 2 | **Anticipación** | baja 26 px antes de subir | `84` |
| 3 | Puesta en escena | un protagonista por momento | `80` |
| 4 | Directo vs. pose a pose | tabla de poses antes de escribir expresiones | `88` |
| 5 | Continuación / superposición | desfase de 0,08 s entre elementos | `84` |
| 6 | **Slow in / slow out** | ease out en todo lo que entra | `84` |
| 7 | **Arcos** | 44 px de desviación lateral en el recorrido | `84` |
| 8 | Acción secundaria | flotación después de llegar | `82` |
| 9 | Ritmo | mismo timing para elementos del mismo tipo | `88` |
| 10 | **Exageración** | tamaño y contraste para pantalla de 6 pulgadas | `44` |
| 11 | Dibujo sólido | sombra difusa bajo el recorte | `81` |
| 12 | Atractivo | test de la silueta | `directorcreativo` |

---

## Errores comunes

1. **Tomarse esto como teoría bonita y no aplicar ninguno.** Son cuatro cambios de una línea que suben
   la calidad percibida más que cualquier efecto.
2. **Aplicar los doce a la vez en un elemento.** Squash + anticipación + arco + secundaria + sobre-impulso
   en un logo de 0,4 s es un ataque epiléptico. Dos o tres por elemento.
3. **Estirar sin encoger.** Si solo anchas, el objeto "crece". El volumen se conserva: lo que se ancha,
   se achata.
4. **Deformar un logo de marca.** El manual lo prohíbe. Deforma el contenedor, no el logo.
5. **Meter tres cosas moviéndose a la vez.** Fallo de puesta en escena. El ojo se rinde.
6. **Elementos que entran todos juntos.** Sin desfase se ve diapositiva. 0,06–0,10 s entre cada uno.
7. **Confundir exagerar la amplitud con exagerar el tiempo.** Amplitud sí, tiempo no. Lento no es
   premium: lento es lento.
8. **Timing inconsistente entre elementos iguales.** Un texto en 0,15 s y otro en 0,40 s se siente
   descuidado aunque cada uno esté bien.
9. **Recorte sin sombra.** Se ve como calcomanía. Un óvalo difuminado al 25% lo arregla.
10. **Luz del recorte contraria a la del plano.** El ojo lo detecta como falso aunque nadie lo diga.
11. **Acción secundaria que compite con la principal.** Deja de ser secundaria y rompe la escena.
12. **Escribir expresiones sin haber hecho antes la tabla de poses.** Media hora escribiendo y borrando.

---

## Checklist

Antes de dar por bueno el motion de una pieza:

- [ ] Escribí la **tabla de poses** antes de tocar una sola expresión.
- [ ] **Nada se mueve lineal**: todo tiene ease out al entrar, ease in al salir.
- [ ] Los elementos importantes tienen **anticipación** de 0,08–0,14 s.
- [ ] Los recorridos van en **arco**, con 30–50 px de desviación.
- [ ] Los grupos de elementos entran con **desfase de 0,06–0,10 s**, no juntos.
- [ ] En cualquier fotograma hay **máximo dos cosas moviéndose**.
- [ ] Cada elemento tiene entre **dos y tres** principios aplicados, no doce.
- [ ] Si hay squash, **conserva el volumen** y no deforma el logo.
- [ ] Todos los elementos del mismo tipo usan **el mismo timing**.
- [ ] Los recortes tienen **sombra difusa** y su luz coincide con la del plano.
- [ ] Verifiqué el fotograma a **300 px de alto**: se lee todo.
- [ ] Pasé el **test de la silueta** en los elementos de marca.
