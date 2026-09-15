# 80 — Capas y composición

**Qué resuelve:** el salto mental que separa a alguien que "junta clips" de alguien que **compone un
plano**. Si solo sabes cortar, tu video es una fila de pedazos pegados. Cuando aprendes a pensar en
capas, la pantalla se convierte en un escenario donde pueden pasar tres cosas a la vez sin que nada se
interrumpa. Este módulo es la base de todo el bloque 8: sin esto, los módulos `81` a `89` no tienen
dónde pararse.

---

## 1. El cambio de mentalidad: cortar vs. superponer

Esta es la idea más importante del bloque, y sale de un error real que costó una tarde entera.

Se necesitaba meter un personaje ilustrado en un video donde alguien hablaba a cámara. La primera
versión hizo lo obvio: **cortar** al personaje. Es decir, en el segundo 4 desaparecía el presentador y
entraba una lámina a pantalla completa con el personaje dibujado, y dos segundos después volvía el
presentador.

El resultado se sentía **muerto**. Y no era problema de la ilustración: la ilustración era buena.

La segunda versión no cortó nada. **Recortó al personaje del fondo** y lo puso **encima** del plano,
en la esquina inferior derecha, mientras el presentador seguía hablando. Mismo dibujo, mismo segundo.
Esta vez se sentía **vivo y acoplado**: el personaje parecía estar ahí, en la escena, reaccionando a lo
que la persona decía.

> **La regla:** un inserto **reemplaza** la realidad; una capa **convive** con ella. Reemplazar mata el
> plano. Convivir lo enriquece.

| | Inserto (corte a pantalla completa) | Capa (encima del plano) |
|---|---|---|
| Qué pasa con el presentador | desaparece | sigue ahí, sigue hablando |
| Cómo se lee | "pausa, mira este dibujo" | "esto está pasando" |
| Sensación | señal congelada, pausa de PowerPoint | vivo, acoplado |
| Riesgo de perder retención | alto | bajo |
| Cuándo sí sirve | cuando el dibujo ES el contenido (un mapa, un diagrama) | casi siempre lo demás |

Esto no significa que el corte a lámina completa esté prohibido. Significa que es una **decisión cara**:
si sacas al ser humano de la pantalla, lo que pongas en su lugar tiene que valer más que él. Casi nunca
vale más.

---

## 2. Vocabulario mínimo (define esto antes de seguir)

> **Capa:** una imagen o video que se pone encima de otro. Como calcomanías en un vidrio: la de abajo
> se ve donde las de arriba no tapan.

> **Canal alfa:** la información de transparencia de una imagen. Cada píxel, además de tener color
> (rojo, verde, azul), tiene un cuarto dato: qué tan opaco es, de 0 (invisible) a 255 (sólido). Un PNG
> con alfa es un PNG con "agujeros". Un JPG **nunca** tiene alfa: por eso te llega con fondo blanco.

> **Composición (compositing):** el arte de juntar varias capas para que se lean como una sola imagen.

> **Pila de capas (stack):** el orden en que se apilan. La última que superpones queda **arriba**.

> **Modo de fusión (blend mode):** en vez de simplemente tapar, la capa se mezcla con la de abajo según
> una fórmula (aclara, oscurece, suma luz). Sección 8.

---

## 3. El orden de capas: la pila estándar

Casi todo video de marca cabe en esta pila. De abajo hacia arriba:

| Nivel | Qué va ahí | Ejemplo |
|---|---|---|
| 1 — Fondo | el plano principal, el que se filmó | el presentador hablando |
| 2 — Tratamiento | color, viñeta, grano, textura | el look de marca (`63`, `66`) |
| 3 — Elementos de escena | recortes que "están dentro" del plano | el personaje de marca, un producto flotando |
| 4 — Gráficos | formas, barras, contadores, rótulos | el precio, un dato (`86`, `48`) |
| 5 — Texto | subtítulos y palabras clave | lo que dice la voz (`40`) |
| 6 — Firma | logo, marca de agua | tu logo en la esquina (`87`) |

**La regla del orden:** el texto **siempre** va encima de los gráficos, y la firma **siempre** encima de
todo. Si un recorte te tapa el subtítulo, el error no es del subtítulo: pusiste la capa en el nivel
equivocado.

**El error clásico:** aplicar el color (nivel 2) al final, encima de todo. Entonces el duotono de marca
te tiñe también el logo y el texto blanco te queda morado. El color va **antes** de superponer los
gráficos, nunca después.

---

## 4. `overlay` en ffmpeg: la sintaxis mínima

`overlay` toma dos entradas de video y pone la segunda encima de la primera.

```bash
ffmpeg -i base.mp4 -i personaje.png \
  -filter_complex "[1:v]scale=-1:620[capa];[0:v][capa]overlay=x=W-w-60:y=H-h-200" \
  -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

Cómo se lee, pieza por pieza:

- `[1:v]` — el video de la entrada 1 (el PNG). Las entradas se numeran desde 0 en el orden de los `-i`.
- `scale=-1:620` — escala el PNG a 620 píxeles de alto y el ancho que corresponda (`-1` = calcula tú).
- `[capa]` — le pone nombre al resultado para usarlo después.
- `[0:v][capa]overlay=...` — pone `[capa]` encima de `[0:v]`.
- `x=W-w-60` — **mayúsculas = la base, minúsculas = la capa**. `W` es el ancho del video de abajo, `w`
  el ancho del PNG. Así que esto significa "pegado al borde derecho, con 60 px de aire".
- `y=H-h-200` — apoyado abajo, 200 px por encima del borde inferior.

**Las cuatro posiciones que vas a usar el 90% del tiempo:**

```
Arriba-izquierda:   overlay=x=60:y=60
Arriba-derecha:     overlay=x=W-w-60:y=60
Abajo-derecha:      overlay=x=W-w-60:y=H-h-200
Centrado:           overlay=x=(W-w)/2:y=(H-h)/2
```

El `-200` de abajo no es capricho: en vertical, los últimos ~380 px los tapa la interfaz de la red
(ver `45-zona-segura-por-plataforma.md`).

---

## 5. Encadenar varias capas

Cada `overlay` produce una imagen nueva, que se vuelve la base del siguiente. Se encadena así:

```bash
ffmpeg -i base.mp4 -i personaje.png -i logo.png \
  -filter_complex "\
[1:v]scale=-1:620[pj];\
[2:v]scale=-1:56,format=rgba,colorchannelmixer=aa=0.6[lg];\
[0:v][pj]overlay=x=W-w-60:y=H-h-260[c1];\
[c1][lg]overlay=x=60:y=60[vout]" \
  -map "[vout]" -map 0:a -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

Lo importante:

- `[c1]` es la imagen intermedia (base + personaje). El logo se pone encima de **eso**.
- `-map "[vout]" -map 0:a` — cuando usas `filter_complex` con nombres, tienes que decirle a ffmpeg
  explícitamente qué video y qué audio meter en el archivo final. Si se te olvida, sale sin audio.
- `colorchannelmixer=aa=0.6` — baja la opacidad del logo al 60%. `aa` es "alpha into alpha".

**Truco de orden de operaciones:** escala **antes** de superponer, nunca después. Superponer un PNG de
4000 px y escalar el resultado hace trabajar a ffmpeg diez veces más y se ve peor.

---

## 6. Encender y apagar capas en el tiempo

Una capa que está toda la duración del video es un adorno. Una capa que **entra en un momento exacto**
es montaje. Hay dos formas y sirven para cosas distintas.

### Forma dura: `enable`

Aparece y desaparece de golpe. Sirve para golpes rítmicos (entra en el beat, ver `24`).

```bash
-filter_complex "[0:v][1:v]overlay=x=(W-w)/2:y=1200:enable='between(t,3.2,6.4)'"
```

`between(t,3.2,6.4)` = visible del segundo 3,2 al 6,4. Los tiempos van en segundos con decimales,
**siempre en una sola unidad** (nunca "1:29", ver `15`).

### Forma suave: fundido del alfa

Aparece y desaparece con transparencia. Es lo que quieres el 80% de las veces.

```bash
ffmpeg -i base.mp4 -i personaje.png \
  -filter_complex "\
[1:v]scale=-1:620,format=rgba,\
fade=t=in:st=3.2:d=0.35:alpha=1,\
fade=t=out:st=6.0:d=0.35:alpha=1[pj];\
[0:v][pj]overlay=x=W-w-60:y=H-h-260:enable='between(t,3.15,6.45)'" \
  -map 0:a -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

La clave es `alpha=1` dentro de `fade`: sin eso, el fundido se hace a negro (te aparece un rectángulo
negro que se aclara) en vez de a transparente. Es el error número uno de este módulo.

Fíjate que el `enable` abre un pelín antes (3,15) y cierra un pelín después (6,45) que el fundido: así
el fundido alcanza a completarse. Si el `enable` corta antes, la capa desaparece de golpe a mitad del
fundido.

---

## 7. Posicionar como diseñador, no como robot

Poner algo "en la esquina" no es una decisión de diseño, es una rendición. Tres criterios:

1. **Que no tape la cara.** Nunca. En vertical la cara suele vivir entre el 20% y el 55% de la altura.
   La capa vive por debajo de eso o al borde.
2. **Que respete la dirección de la mirada.** Si el presentador mira a su izquierda (tu derecha), la
   capa va **a la derecha**: parece que le habla a ella. Si la pones al otro lado, parece que le da la
   espalda. Este detalle solito hace que la composición se sienta "pensada".
3. **Que entre por donde tiene sentido.** Un personaje que sube desde el borde inferior parece que se
   asoma. Uno que aparece de la nada parece un error de render. Ver `84` para las curvas de entrada.

Posición animada de entrada (sube desde abajo del cuadro):

```bash
-filter_complex "[0:v][1:v]overlay=\
x=W-w-60:\
y='if(lt(t,3.2), H, H-(H-(H-h-260))*clip((t-3.2)/0.5,0,1))'"
```

Se lee: antes del segundo 3,2 está fuera de cuadro (`y=H`); después sube durante medio segundo hasta su
posición final. Es movimiento **lineal** y por eso se ve barato — la versión con curva está en `84`.

---

## 8. Modos de fusión: cuando tapar no es lo que quieres

`overlay` tapa. A veces quieres que la capa **se mezcle** con la imagen: una fuga de luz, un destello,
una textura de papel, humo. Eso es `blend`.

```bash
ffmpeg -i base.mp4 -i fuga_de_luz.mp4 \
  -filter_complex "[1:v]scale=1080:1920,format=gbrp[fx];[0:v]format=gbrp[bg];\
[bg][fx]blend=all_mode=screen:all_opacity=0.45,format=yuv420p" \
  -c:a copy salida.mp4
```

Los tres modos que de verdad usas:

| Modo | Qué hace | Para qué |
|---|---|---|
| `screen` | suma luz, el negro desaparece | destellos, fugas de luz, humo, polvo, fuego |
| `multiply` | oscurece, el blanco desaparece | sombras, viñetas, texturas de papel o suciedad |
| `overlay` (como blend) | sube contraste | textura de grano o tela sin aplanar la imagen |

**Por qué esto importa:** un destello grabado en negro que pegas con `overlay` te mete un rectángulo
negro en pantalla. Con `blend=all_mode=screen` el negro se vuelve invisible y solo queda la luz. Es la
diferencia entre parecer un efecto y parecer que pasó de verdad.

Ojo con `blend`: exige que las dos entradas tengan **el mismo tamaño y el mismo formato de píxel**. Si
te tira un error raro, casi siempre es eso: escala las dos a lo mismo y mételes `format=gbrp` antes.

---

## 9. Lo que cuesta y cómo no sufrir

Componer es caro en tiempo de render. Reglas prácticas:

- **Escala primero, compón después.** Siempre.
- **Prerrenderiza lo que se repite.** Si el mismo personaje animado va en 8 videos, sácalo una vez como
  video con alfa (ProRes 4444 o WebM VP9, ver `81`) y superpónlo. No lo recalcules 8 veces.
- **Un `filter_complex` de 30 líneas es un olor a problema.** Pártelo en dos pasadas y guarda el
  intermedio. Depurar un filtro gigante es infierno; depurar dos de quince líneas es martes.
- **Nunca dejes el intermedio en H.264.** Si vas a hacer dos pasadas, el archivo de en medio va en
  calidad alta (`-crf 12` o ProRes). Encadenar compresiones te ensucia los bordes de los recortes.

```bash
ffmpeg -i base.mp4 -i personaje.png -filter_complex "..." -c:v libx264 -crf 12 -preset fast paso1.mp4
ffmpeg -i paso1.mp4 -i texto.mov -filter_complex "..." -c:v libx264 -crf 18 final.mp4
```

---

## 10. Cuándo la capa sobra

Sé honesto: no todo video necesita composición. La capa sobra cuando:

- El plano ya está lleno (mucho movimiento, mucho texto). Otra capa es ruido.
- Es un testimonio real. Un personaje animado encima de alguien contando su experiencia mata la
  credibilidad, que es lo único que ese video vende (`154`).
- La capa solo dice lo mismo que ya dice la voz y ya dice el texto. Tres canales repitiendo un dato no
  es énfasis, es tartamudeo.
- No tienes tiempo de animarla. Una capa quieta encima de un plano vivo se ve pegada, como una
  calcomanía. Mejor sin ella que mal.

---

## Errores comunes

1. **Cortar a lámina completa cuando bastaba superponer.** El error que abre este módulo. Sacaste al
   humano de la pantalla para mostrar un dibujo. La retención se va con el humano.
2. **Usar `fade` sin `alpha=1`.** Te aparece un rectángulo negro que se aclara en vez de una capa que
   se desvanece. Pasa siempre la primera vez.
3. **Olvidar `-map 0:a`.** Usaste `filter_complex` con etiquetas y el video final salió mudo. No es un
   bug: ffmpeg dejó de adivinar cuando le pusiste nombres a las salidas.
4. **Superponer un JPG esperando transparencia.** El JPG no tiene canal alfa. Nunca lo tuvo. Te va a
   quedar el rectángulo blanco, y no hay parámetro que lo arregle (ver `81`).
5. **Escalar después de componer.** El render se demora el triple y los bordes del recorte quedan
   sucios.
6. **Cerrar el `enable` justo donde termina el fundido.** La capa se corta de golpe a mitad del
   desvanecido. Deja 0,05 s de aire a cada lado.
7. **Aplicar el color de marca al final, encima de las capas.** Te tiñe el logo y el texto. El color va
   en el nivel 2 de la pila, antes de los gráficos.
8. **Poner la capa del lado contrario a donde mira la persona.** Técnicamente correcto, visualmente
   incómodo. El ojo lo nota aunque nadie sepa explicarlo.
9. **Pegar un destello grabado en negro con `overlay`.** Queda un cuadro negro. Ese material va con
   `blend=all_mode=screen`.
10. **Meter tres capas a la vez "porque quedan bien".** Si el ojo no sabe dónde mirar, no mira a ningún
    lado. Una capa protagonista por momento.

---

## Checklist

Antes de dar por buena una composición:

- [ ] Me pregunté si esto era **capa o corte**, y elegí capa salvo que el corte estuviera justificado.
- [ ] Cada elemento está en su **nivel correcto** de la pila (color abajo, texto arriba, firma al final).
- [ ] Las capas con transparencia son **PNG con alfa** verificado, no JPG ni PNG con fondo blanco.
- [ ] Escalé cada capa **antes** de superponerla.
- [ ] Las entradas y salidas usan `fade=...:alpha=1`, no fundido a negro.
- [ ] El `enable` abre y cierra con **0,05 s de aire** respecto a los fundidos.
- [ ] Ninguna capa **tapa la cara** ni entra en la zona muerta de la plataforma (`45`).
- [ ] La capa está del lado **hacia donde mira** la persona.
- [ ] Puse `-map "[vout]" -map 0:a` y comprobé que el archivo final **tiene audio**.
- [ ] Si hay dos pasadas, el archivo intermedio va en calidad alta (`-crf 12` o ProRes).
- [ ] Vi un fotograma del momento de cada capa (`98`) y no hay bordes duros, rectángulos ni recortes
      pegados encima del subtítulo.
