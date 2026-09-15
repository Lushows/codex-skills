# 42 — Anatomía del golpe: el pop, el sobre-impulso y los 140 milisegundos

## Qué es "el golpe"

Cada vez que el texto cambia en pantalla, eso es un **golpe**. La palabra importa: no es una "aparición",
no es una "transición". Es un golpe, porque tiene que sentirse como un impacto físico sincronizado con
la voz.

La diferencia entre un video que se siente vivo y uno que se siente muerto casi nunca está en el corte
de imagen. Está en **cómo entra el texto**. Un texto que simplemente aparece se lee como una diapositiva.
Un texto que golpea se lee como ritmo.

---

## La animación exacta que funciona

Esto está medido, no estimado. Tres estados en 140 milisegundos:

| Momento | Escala | Opacidad | Qué pasa |
|---|---|---|---|
| 0 ms | 62% | 0 (invisible) | El texto ya existe pero no se ve, y está chiquito |
| 70 ms | **112%** | 100% | Se pasa de largo: llega más grande de lo que debe |
| 140 ms | 100% | 100% | Se asienta en su tamaño real |

En ASS:

```
{\fscx62\fscy62\alpha&HFF&\t(0,70,\fscx112\fscy112\alpha&H00&)\t(70,140,\fscx100\fscy100)}
```

Desglose de cada pieza:

- `\fscx62\fscy62` — estado inicial: escala horizontal y vertical al 62%.
- `\alpha&HFF&` — estado inicial: totalmente transparente (`FF` = invisible, `00` = opaco; sí, al revés
  de lo que uno esperaría).
- `\t(0,70, ...)` — primera transformación: de 0 a 70 ms, sube a 112% y se vuelve opaco (`\alpha&H00&`).
- `\t(70,140, ...)` — segunda transformación: de 70 a 140 ms, baja de 112% a 100%.

Ese bloque va **al inicio del texto** de cada línea `Dialogue`, antes de la primera letra.

---

## Por qué el sobre-impulso es lo que lo hace funcionar

Este es el punto que casi nadie entiende y por eso casi nadie lo hace bien.

Si animas de 62% a 100% y ya, tienes esto:

```
62% ────────► 100%
```

El texto crece y se detiene. Se ve **suave, blando, y ligeramente lento**, aunque dure lo mismo. El ojo
lo lee como "algo apareció".

Con sobre-impulso tienes esto:

```
62% ────────► 112% ──► 100%
             (se pasa)  (rebota)
```

El texto crece **más de lo que debe**, y luego se devuelve. Ese "se devuelve" es lo que el cerebro lee
como masa, peso, física real. Un objeto con masa que se detiene de golpe rebota. Un objeto sin masa
simplemente se detiene.

Es el mismo principio que en animación clásica se llama **overshoot** (ver `84` y `85`). No estás
animando un texto: estás simulando que algo pesado cayó en su sitio.

**Regla del oficio:** una animación sin sobre-impulso se ve barata. Da igual si es texto, un logo, un
gráfico o una barra de datos. El lineal y el ease-out puro son la firma del trabajo de plantilla.

---

## Por qué 140 milisegundos y no otra cosa

| Duración total | Cómo se siente |
|---|---|
| 60-90 ms | Un parpadeo. No se percibe la animación, solo un flash. Cansa. |
| **120-160 ms** | **El punto óptimo. Se percibe el impacto sin sentir espera.** |
| 200-300 ms | Ya se siente como una animación. Elegante, pero pierde el pulso. |
| 400 ms+ | El texto "entra". Correcto para un rótulo, mortal para un golpe. |

Si tu golpe dura 0,9 segundos y la animación se come 300 ms, un tercio del tiempo que el texto está en
pantalla lo pasa moviéndose. Eso es demasiado. Con 140 ms, el texto pasa el 85% de su vida **quieto y
legible**, que es lo que quieres.

El reparto interno también importa: **la mitad para llegar arriba, la mitad para asentarse**. 70/70. Si
haces 40/100, el impulso se siente débil. Si haces 100/40, el rebote se siente brusco.

---

## Por qué 62% y 112% y no otros números

- **62% de entrada.** Suficientemente pequeño para que el crecimiento se note, suficientemente grande
  para que la palabra ya sea legible desde el primer fotograma. Por debajo de ~50% el texto arranca
  ilegible y el ojo pierde el primer instante. Por encima de ~80% el crecimiento no se percibe.
- **112% de sobre-impulso.** Un 12% de exceso. Suena poco y es exactamente el punto: se siente, no se ve.
  Con 130%+ el texto se sale de la zona segura en las palabras largas y el efecto se vuelve caricaturesco
  (el "boing" de plantilla). Con 105% no se percibe y volviste al ease-out simple.

Nota importante: `\fscx` y `\fscy` escalan **desde el punto de anclaje del texto**, que depende de la
alineación del estilo. Con alineación 2 (centro-abajo), el texto crece hacia arriba y hacia los lados
por igual. Con alineación 1 (izquierda-abajo), crece hacia la derecha. Si tu texto se sale de cuadro al
112%, revisa la alineación antes que el porcentaje.

---

## El golpe completo en un archivo real

```
[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Golpe,Anton,150,&H00FFFFFF,&H00FFFFFF,&H001C4FE8,&H00000000,0,0,0,0,100,100,0,0,1,14,9,2,60,60,520,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.30,0:00:01.18,Golpe,,0,0,0,,{\fscx62\fscy62\alpha&HFF&\t(0,70,\fscx112\fscy112\alpha&H00&)\t(70,140,\fscx100\fscy100)}TU COCINA
Dialogue: 0,0:00:01.18,0:00:02.05,Golpe,,0,0,0,,{\fscx62\fscy62\alpha&HFF&\t(0,70,\fscx112\fscy112\alpha&H00&)\t(70,140,\fscx100\fscy100)}TE ESTA
Dialogue: 0,0:00:02.05,0:00:02.94,Golpe,,0,0,0,,{\fscx62\fscy62\alpha&HFF&\t(0,70,\fscx112\fscy112\alpha&H00&)\t(70,140,\fscx100\fscy100)}ROBANDO
```

Quemarlo:

```bash
ffmpeg -i entrada.mp4 -vf "subtitles=golpes.ass:fontsdir=fonts" \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a copy salida.mp4
```

---

## Dónde va el golpe respecto a la voz

El golpe **no** cae cuando termina la palabra anterior. Cae en la **sílaba tónica** de la primera palabra
del nuevo golpe, o entre 30 y 60 ms antes.

Que llegue apenas antes es deliberado: el ojo procesa más rápido que el oído en este contexto, y un texto
que llega 50 ms antes se percibe como **exactamente sincronizado**. Un texto que llega 50 ms después se
percibe como **tarde**. La tolerancia es asimétrica.

Regla práctica: si tienes el timecode de inicio de la palabra de la transcripción, réstale 0,04 s.

```
Palabra "ROBANDO" empieza en 2.09  ->  Dialogue Start: 0:00:02.05
```

---

## Variantes del golpe (cuándo usar otra cosa)

El pop de 140 ms es el caballo de batalla. Pero no es lo único.

### Golpe con desplazamiento (para énfasis muy fuerte)

Añade un empujón vertical al pop. Úsalo **una o dos veces por video**, en la palabra más importante.

```
{\fscx62\fscy62\alpha&HFF&\move(540,1450,540,1400,0,140)\t(0,70,\fscx112\fscy112\alpha&H00&)\t(70,140,\fscx100\fscy100)}
```

`\move(x1,y1,x2,y2,t1,t2)` mueve el texto de un punto a otro entre t1 y t2 (en ms). Requiere que uses
`\pos` o `\move`, lo que anula los márgenes del estilo: las coordenadas mandan.

### Golpe con giro leve (para tono lúdico)

```
{\frz-4\fscx62\fscy62\alpha&HFF&\t(0,70,\frz2\fscx112\fscy112\alpha&H00&)\t(70,140,\frz0\fscx100\fscy100)}
```

`\frz` es rotación en Z (grados). De -4 a 2 a 0. Muy poco. Más de 6 grados se ve amateur.

### Entrada sin pop (para rótulos y datos)

Un rótulo informativo no golpea, **entra**. Fundido limpio de 250 ms:

```
{\alpha&HFF&\t(0,250,\alpha&H00&)}
```

Ver `48` para rótulos y lower thirds.

### Salida

En subtitulado completo **no pongas salida**: el golpe siguiente reemplaza al anterior y el corte seco
entre uno y otro es lo que da el pulso. Un fundido de salida crea un instante de pantalla borrosa que
rompe el ritmo.

En palabras clave (resaltes largos) **sí** conviene una salida, porque después viene pantalla vacía:

```
{\fscx62\fscy62\alpha&HFF&\t(0,70,\fscx112\fscy112\alpha&H00&)\t(70,140,\fscx100\fscy100)\t(2100,2300,\alpha&HFF&)}
```

Los tiempos de `\t` son **relativos al inicio de esa línea**, no absolutos del video. Ese último `\t`
desvanece entre los 2100 y 2300 ms de vida de la línea.

---

## Cómo verificar que el golpe quedó bien

No lo juzgues reproduciendo el video: 140 ms son ~4 fotogramas a 30 fps y el ojo no los descompone.
**Extrae los fotogramas.**

```bash
ffmpeg -i salida.mp4 -vf "select='between(t,1.15,1.40)'" -vsync 0 -y golpe_%03d.png
```

Eso te da los fotogramas del golpe uno por uno. Deberías ver: uno con el texto chico y tenue, uno con el
texto claramente más grande de lo normal, y luego el texto en tamaño estable. Si no ves el fotograma
sobredimensionado, el sobre-impulso no está ocurriendo (o tu `\t` está mal escrito y libass lo ignoró en
silencio).

**Trampa:** libass **no da error** ante una etiqueta mal escrita. Se la come y renderiza el texto sin
animación. Si tu texto aparece plano, revisa las llaves, las barras invertidas y el `&` de cierre en
`\alpha&HFF&` (los dos `&` son obligatorios).

---

## Errores comunes

- **Animar sin sobre-impulso.** De 62% a 100% directo. Es la diferencia entre "profesional" y "plantilla".
  Este es el error central de todo el módulo.
- **Sobre-impulso exagerado (125%+).** El texto rebota como caricatura, se sale de la zona segura en
  palabras largas, y se ve más barato que sin animación.
- **Animación demasiado larga.** 300-400 ms dentro de un golpe de 0,9 s: el texto pasa un tercio de su
  vida moviéndose y no se alcanza a leer quieto.
- **Reparto asimétrico del tiempo.** 70/70 está medido. 30/110 o 110/30 se sienten mal, cada uno a su modo.
- **Confundir tiempos relativos con absolutos.** Dentro de `\t(...)` los milisegundos cuentan desde el
  inicio de esa línea `Dialogue`, no desde el inicio del video. Es la causa #1 de "puse la salida y no
  pasa nada".
- **Poner fundido de salida en subtitulado completo.** Crea un microhueco entre golpes y mata el pulso.
- **Escribir `\alpha&HFF` sin el `&` final.** libass lo ignora en silencio y el texto arranca visible.
- **Olvidar `ScaledBorderAndShadow: yes`.** Sin eso, al escalar el texto al 112% el contorno no escala con
  él y se ve un borde que "respira" raro.
- **Usar `\move` sin darte cuenta de que anula los márgenes.** Al usar coordenadas, `MarginV` deja de
  aplicar y el texto se te va a donde diga el `\move`, aunque sea encima del caption de Instagram.
- **Juzgar el golpe reproduciendo.** Son 4 fotogramas. Extráelos y míralos.

---

## Checklist

- [ ] Todos los golpes llevan el bloque de override completo, no solo algunos.
- [ ] La animación es 62% → **112%** → 100%. El sobre-impulso está presente.
- [ ] Los tiempos son 0-70-140 ms, reparto simétrico.
- [ ] `\alpha&HFF&` y `\alpha&H00&` escritos con los dos `&`.
- [ ] `ScaledBorderAndShadow: yes` está en `[Script Info]`.
- [ ] Los tiempos dentro de `\t()` los calculé **relativos al inicio de la línea**.
- [ ] El golpe cae 30-60 ms **antes** de la sílaba tónica, no después.
- [ ] En subtitulado completo: sin fundido de salida.
- [ ] En resaltes largos: salida de ~200 ms al final.
- [ ] El golpe con desplazamiento o giro lo usé máximo 2 veces en todo el video.
- [ ] Extraje los fotogramas del golpe y **vi el fotograma sobredimensionado** al 112%.
- [ ] Ningún texto se sale de la zona segura al escalar al 112% (revisé las palabras más largas).
- [ ] Verifiqué que la fuente correcta se renderizó (no sustitución silenciosa a Arial).
