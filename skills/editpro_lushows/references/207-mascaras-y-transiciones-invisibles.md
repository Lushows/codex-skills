# 207 — Máscaras y transiciones invisibles

**Qué resuelve:** en 51 proyectos usaste **una sola transición**. Todo lo demás a corte duro. Ese
instinto es correcto: las transiciones que trae el editor —el disolver, el giro de cubo, el barrido de
estrella— se leen como plantilla y le roban tiempo de pantalla al contenido.

Pero hay una familia distinta: las transiciones que **no se ven**. No hay ningún efecto aplicado; lo
que hay es un corte escondido detrás de algo que pasa por delante, o detrás de un borrón, o detrás de
una forma que coincide. Cuestan casi nada, no dependen de ninguna herramienta, y son lo que hace que
un video se sienta filmado en vez de montado.

Este módulo son las cuatro que valen la pena.

---

## 1. Por qué una transición invisible se ve cara

Una transición de plantilla dice "aquí un editor puso un efecto". Una transición invisible dice "aquí
no pasó nada, esto es continuo". El espectador no la nota, y esa es toda la gracia:

> El cerebro perdona un corte duro porque está acostumbrado. Lo que no perdona es un corte **feo**: un
> salto de encuadre, de luz o de posición que le rompe la continuidad. La transición invisible existe
> para esconder exactamente ese salto.

Regla que ordena todo el módulo:

**Las transiciones invisibles no se usan para adornar. Se usan para tapar un problema.** Si el corte
funciona limpio, déjalo limpio. Si el corte salta, entonces escóndelo.

Los tres problemas que tapan:

| Problema | Cuál usar |
|---|---|
| Los dos planos son parecidos y el corte "salta" | barrido con objeto, o whip pan |
| Cambio brusco de lugar (adentro → afuera) | whip pan o barrido |
| Necesito comprimir tiempo sin que se note | corte por coincidencia de forma |
| El plano B empieza feo (mano entrando, encuadre buscándose) | barrido con objeto |

---

## 2. El barrido con objeto: la mejor del módulo

> Algo pasa muy cerca de la cámara, tapa el cuadro por completo durante 2 o 3 fotogramas, y cuando
> despeja ya estás en otro plano.

Es la más fácil, la más versátil y la que mejor se ve. En un bar tienes objetos perfectos por todos
lados: una jarra, un brazo, una bandeja, una puerta, un trapo, la espalda de alguien que pasa.

### Cómo se graba

**Plano A:** al final de la toma, pasa algo por delante del lente hasta que la pantalla quede
completamente tapada. Tiene que quedar **oscuro o de un color plano** durante mínimo 2 fotogramas.

**Plano B:** empieza con la pantalla igualmente tapada por algo parecido, que despeja.

Dos formas de conseguir el plano B:

- **Grabar el gemelo:** en el sitio nuevo, empieza con el objeto tapando y sepáralo.
- **La trampa que casi nadie ve:** graba el plano A al revés y ya. Si la jarra tapó el lente en A,
  usa ese mismo movimiento invertido para B en otra toma cualquiera. Lo que importa es que **haya
  oscuridad en ambos lados del corte**.

### Cómo se monta

1. Encuentra el fotograma **más tapado** del plano A. Corta ahí.
2. Encuentra el fotograma **más tapado** del plano B. Corta ahí.
3. Pégalos. Sin transición, sin efecto, sin nada.
4. Míralo. Si salta, corre el corte un fotograma para un lado o para el otro.

**Los tres detalles que hacen que funcione:**

- **La dirección debe coincidir.** Si en A el objeto barre de izquierda a derecha, en B tiene que
  despejar en la misma dirección. Si van al revés, el ojo lo detecta como error aunque no sepa por qué.
- **La velocidad debe coincidir.** Si A barre rápido y B despeja lento, se nota. Se arregla acelerando
  o frenando uno de los dos (`201`).
- **El brillo del fotograma tapado debe parecerse.** Si A queda negro y B queda blanco, el corte
  destella. Se ajusta bajando el brillo de los primeros fotogramas de B.

### Si no lo grabaste así

Se puede falsificar con una máscara: un rectángulo del color del objeto que barre el cuadro sobre el
corte. Es más trabajo y se ve peor, pero salva un corte imposible.

```bash
ffmpeg -i a.mp4 -i b.mp4 -filter_complex "\
[0:v]trim=0:4.20,setpts=PTS-STARTPTS[va];\
[1:v]trim=1.10:5.00,setpts=PTS-STARTPTS[vb];\
[va][vb]concat=n=2:v=1:a=0[cat];\
color=c=0x1a1208:s=1080x1920:d=8[bar];\
[cat][bar]overlay=x='-W + 2.6*W*clip((t-4.06)/0.28,0,1)':y=0:enable='between(t,4.06,4.34)'[v]" \
  -map "[v]" -an -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

Una barra de color madera cruza el cuadro entero en 0,28 segundos justo encima del corte (que está en
4,20). Con un objeto real se ve mucho mejor; esto es el paracaídas.

---

## 3. El whip pan casero

> **Whip pan:** giras la cámara tan rápido que la imagen se convierte en rayas. Cortas en el punto de
> máximo borrón y sales del otro lado con otro giro igual de rápido.

Es la transición que todo el mundo reconoce de los videos de viaje, y **se puede hacer sin grabarla**,
que es lo que la hace interesante para ti.

### La versión grabada (la buena)

- Final del plano A: gira la cámara rápido, siempre en la **misma dirección**, hasta que todo sea
  borrón.
- Inicio del plano B: la cámara viene girando en **esa misma dirección** y frena en el encuadre nuevo.
- Corta en el fotograma más borroso de cada uno.

Requisito no negociable: **misma dirección**. Si A gira a la derecha y B viene de la izquierda, el
espectador siente un tirón raro.

### La versión falsificada (la que probablemente uses)

Se le agrega desenfoque direccional a los últimos fotogramas de A y a los primeros de B, junto con un
desplazamiento lateral rápido. El truco de ffmpeg es que `avgblur` acepta radios distintos en X y en Y:

```bash
ffmpeg -i a.mp4 -i b.mp4 -filter_complex "\
[0:v]trim=0:4.00,setpts=PTS-STARTPTS,\
avgblur=sizeX='min(70, 70*clip((t-3.86)/0.14,0,1))':sizeY=1,\
crop=1080:1920:'0 + 260*clip((t-3.86)/0.14,0,1)':0[va];\
[1:v]trim=1.00:5.00,setpts=PTS-STARTPTS,\
avgblur=sizeX='max(0, 70*(1-clip(t/0.14,0,1)))':sizeY=1,\
crop=1080:1920:'260*(1-clip(t/0.14,0,1))':0[vb];\
[va][vb]concat=n=2:v=1:a=0[v]" \
  -map "[v]" -an -c:v libx264 -crf 18 -pix_fmt yuv420p whip.mp4
```

Lo que hace: en los últimos 0,14 segundos de A, el desenfoque horizontal sube de 0 a 70 y la imagen se
desplaza 260 píxeles. En B pasa lo mismo al revés. Total: unos 8 fotogramas de borrón.

**Ojo:** para que el `crop` con desplazamiento funcione, el material tiene que ser más ancho que el
cuadro final, o vas a llegar al borde y ver negro. Graba en 1080 y trabaja en un lienzo un poco menor,
o escala el plano un 115% antes.

En CapCut es más simple aunque menos fino: pon desenfoque al máximo en los últimos fotogramas con
keyframes, agrega desplazamiento de posición, y haz lo inverso en el plano siguiente. Con 6–8
fotogramas de cada lado basta.

**Duración total del whip pan: 0,20 a 0,30 segundos.** Más largo se ve como un efecto; más corto no se
alcanza a leer como giro.

---

## 4. El corte por coincidencia de forma

> **Corte por forma (match cut):** cortas en el momento en que algo del plano A tiene la misma forma,
> tamaño y posición que algo del plano B. El ojo enlaza las dos formas y no registra el corte.

Es la más elegante de todas y la única que no requiere ningún efecto: solo requiere **ver**.

Ejemplos para tu material:

- Círculo de la boca de una jarra → círculo de una moneda, de un plato, del sol.
- Movimiento de la mano bajando → movimiento de la puerta bajando.
- Alguien girando la cabeza a la derecha → un carro pasando a la derecha.
- Espuma subiendo en el vaso → gente subiendo la escalera del local.

**Los tres criterios para que enlace:**

1. **Forma parecida** (círculo con círculo, línea con línea).
2. **Posición parecida en el cuadro** (si el círculo de A está a la izquierda, el de B también).
3. **Movimiento en la misma dirección** — este es el que más pesa. Dos formas idénticas moviéndose en
   direcciones opuestas no enlazan; dos formas distintas moviéndose igual, sí.

**Cómo se encuentran:** revisando el material con la mentalidad de "qué se parece a qué". Es trabajo
de minería (`12`), no de edición. Vale la pena porque un solo corte por forma bien hallado le levanta
el nivel a todo un video.

**La versión barata y funcional:** el **corte por movimiento**. No hace falta que las formas se
parezcan; basta con que el movimiento continúe. Si en A la mano va hacia abajo y en B algo sigue yendo
hacia abajo, el corte fluye. Esto lo puedes hacer en casi cualquier par de planos y nadie lo enseña.

---

## 5. La máscara de forma como transición

La última: en vez de que el plano B reemplace al A, **crece dentro de él** a través de una forma.

- Un círculo que se abre desde el centro de una lámpara y revela el plano B.
- Una franja vertical que se ensancha desde el borde de una puerta.
- El plano B apareciendo dentro de la silueta de la jarra, que luego crece hasta llenar la pantalla.

Funciona cuando la forma **coincide con algo del plano A**. Si el círculo se abre desde donde está la
lámpara, se lee como que la luz se expandió. Si se abre desde el centro por defecto, se lee como
plantilla de PowerPoint.

```bash
ffmpeg -i a.mp4 -i b.mp4 -filter_complex "\
[0:v]trim=0:5.0,setpts=PTS-STARTPTS[va];\
[1:v]trim=0:5.0,setpts=PTS-STARTPTS[vb];\
[va][vb]xfade=transition=circleopen:duration=0.5:offset=3.6[v]" \
  -map "[v]" -an -c:v libx264 -crf 18 -pix_fmt yuv420p forma.mp4
```

`xfade` (ver `107`) trae `circleopen`, `circleclose`, `wipeleft`, `radial` y más. **La condición para
usarlo sin que se vea barato:** el centro de la forma tiene que coincidir con algo real del plano A, y
la duración no puede pasar de **0,5 segundos**. Los `xfade` de un segundo son la firma del video
amateur.

Y la advertencia general: de las cuatro técnicas del módulo, esta es la que más se acerca a "efecto".
Úsala como mucho una vez por video, y solo cuando la forma coincida con algo.

---

## 6. Cuántas usar y dónde

Con tu estilo —corte duro casi siempre— la dosis correcta es baja:

```
REEL DE 25 SEGUNDOS

Cortes duros                 el 90 al 95 por ciento de los cortes
Barrido con objeto           1, en el cambio de escenario
Whip pan                     1, opcional, en el momento de mas energia
Corte por forma o movimiento cuantos encuentres, no cuestan nada
Mascara de forma             0 o 1, y solo si coincide con algo
```

**El corte por movimiento es el único ilimitado**, porque no es un efecto: es elegir mejor dónde
cortar. Todo lo demás va con cuentagotas.

Y una comprobación de honestidad: si un video tuyo tiene tres transiciones invisibles y ninguna estaba
tapando un problema, no estabas escondiendo cortes, estabas decorando. Vuelve a los cortes duros.

---

## 7. Verificar una transición invisible

Se verifica de una sola manera: **fotograma a fotograma**.

```bash
ffmpeg -ss 3.9 -i salida.mp4 -t 0.6 -vf "fps=30,scale=200:-1,tile=9x2" -frames:v 1 corte.png
```

Eso te da los 18 fotogramas alrededor del corte en una sola imagen. Lo que buscas:

- **Al menos 2 fotogramas completamente tapados** en un barrido con objeto. Si hay solo uno, se ve el
  salto.
- **Continuidad de dirección**: el objeto o el borrón va para el mismo lado antes y después.
- **Continuidad de brillo**: ningún fotograma destella más claro o más oscuro que sus vecinos.
- **Ningún fotograma "limpio" en medio del borrón**. Si en la mitad del whip pan hay un cuadro nítido,
  el corte se ve.

Ese último es el error que más aparece y el que menos se detecta reproduciendo: un solo fotograma
nítido en medio del borrón delata todo, y a velocidad normal solo se percibe como "algo raro pasó ahí".

---

## Errores comunes

1. **Usar transiciones para adornar.** Existen para tapar un problema. Si el corte funciona limpio,
   déjalo.
2. **Barrido con solo un fotograma tapado.** Hacen falta dos como mínimo, tres es mejor.
3. **Dirección invertida entre los dos planos.** El ojo lo detecta como error aunque no sepa nombrarlo.
4. **Velocidades distintas a cada lado del barrido.** Se arregla acelerando uno de los dos.
5. **Brillo distinto en los fotogramas tapados.** Produce un destello en medio del corte.
6. **Whip pan de más de 0,3 segundos.** Deja de leerse como giro y se lee como efecto.
7. **Un fotograma nítido en medio del borrón.** Delata todo el truco. Solo se ve en la tira.
8. **`crop` con desplazamiento sobre material del tamaño justo.** Llegas al borde y aparece negro.
   Escala 115% antes.
9. **`xfade` de un segundo.** Es la firma del video amateur. Máximo 0,5 s.
10. **Máscara de forma centrada por defecto.** Tiene que coincidir con algo real del plano A.
11. **Buscar coincidencia de forma e ignorar la dirección del movimiento.** La dirección pesa más que
    la forma.
12. **Meter tres o cuatro transiciones invisibles en un reel.** Deja de ser invisible y pasa a ser un
    estilo, y no uno bueno.
13. **Olvidar el audio en el corte.** Una transición visual perfecta con un empalme de audio brusco no
    engaña a nadie. El sonido tiene que cruzar el corte (`103`).
14. **Verificar reproduciendo.** A velocidad normal se percibe "algo raro" pero no se localiza. La tira
    de fotogramas te dice el fotograma exacto.

---

## Checklist

Antes de dar por buena una transición invisible:

- [ ] Esta transición está **tapando un problema real**, no decorando.
- [ ] Si es barrido: hay **2 o más fotogramas completamente tapados**.
- [ ] La **dirección** del movimiento coincide antes y después del corte.
- [ ] La **velocidad** del barrido o el giro coincide a ambos lados.
- [ ] El **brillo** de los fotogramas del corte es parecido; no hay destello.
- [ ] Si es whip pan: dura entre **0,20 y 0,30 segundos**.
- [ ] Si es whip pan: **no hay ningún fotograma nítido** en medio del borrón.
- [ ] Si es máscara de forma: el centro **coincide con algo real** del plano A y dura menos de 0,5 s.
- [ ] Si es corte por forma: coinciden **forma, posición y dirección**.
- [ ] El **audio cruza el corte** de forma continua.
- [ ] En todo el reel hay como mucho **una o dos** transiciones invisibles (los cortes por movimiento
      no cuentan).
- [ ] Saqué la **tira de fotogramas** alrededor del corte y la revisé cuadro por cuadro.
- [ ] El resto del video sigue siendo **corte duro**, como corresponde al formato.
