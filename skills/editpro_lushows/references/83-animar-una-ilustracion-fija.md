# 83 — Animar una ilustración fija

**Qué resuelve:** metiste una ilustración, una foto o un gráfico en medio del video y **se siente como
que se congeló la señal**. No es tu imaginación ni es culpa de la imagen: es un problema real y tiene
nombre. Este módulo lo explica, da el parche rápido (que es un parche y hay que decirlo), y da las tres
formas de arreglarlo de verdad.

---

## 1. Por qué una imagen fija mata un video

Un video se mira porque **cambia**. El ojo está enganchado a la novedad: cada fotograma trae información
un poquito distinta y eso sostiene la atención sin esfuerzo.

Cuando metes una imagen fija de 3 segundos en medio de video en movimiento, pasan 75 fotogramas
**idénticos**. El cerebro procesa la imagen completa en unos 400 milisegundos y después se queda sin
nada que hacer durante 2,6 segundos. Y como está viendo video, interpreta la ausencia de cambio como un
fallo técnico:

> **"Se congeló."** Esa es literalmente la sensación. No "qué bonita ilustración", sino "se me trabó".

Peor todavía en redes: el usuario ya tiene el dedo listo. Una pantalla que no cambia es la señal
universal de "aquí no pasa nada, sigue".

**El detector honesto:** exporta el video, saca una grilla de fotogramas (`17`) y cuenta cuántos
cuadritos seguidos son idénticos. Más de tres = hueco.

```bash
ffmpeg -i video.mp4 -vf "fps=2,scale=240:-1,tile=8x6" -frames:v 1 grilla.png
```

---

## 2. El parche: empuje lento de escala (`zoompan`)

La solución de un minuto: que la imagen se acerque muy despacio. Es el efecto Ken Burns de toda la vida.

**Y hay que decirlo claro: esto es un parche.** Le quita al plano la sensación de congelado, sí. Pero no
lo vuelve vivo, solo lo vuelve tolerable. Lo bueno es animarla de verdad (secciones 4 a 6). El empuje es
lo que haces cuando no hay tiempo o cuando la imagen es secundaria.

```bash
ffmpeg -loop 1 -framerate 25 -t 4 -i lamina.png \
  -vf "scale=4320:-2,\
zoompan=z='1+0.0011*on':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=25,\
format=yuv420p" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p lamina_viva.mp4
```

Pieza por pieza:

- `-loop 1 -framerate 25 -t 4` — repite la imagen fija como si fuera video, a 25 fps, durante 4 s.
- `scale=4320:-2` — **el paso que casi todos se saltan.** Agranda la imagen 4x ANTES de hacer zoom. Si
  no lo haces, `zoompan` trabaja con pocos píxeles y el movimiento sale a saltitos (se ve escalonado,
  como si la imagen brincara de píxel en píxel). Este es el error clásico de `zoompan`.
- `z='1+0.0011*on'` — el zoom crece con el número de fotograma de salida (`on`). En 100 fotogramas
  (4 s a 25 fps) llega a 1,11: un acercamiento del 11%.
- `d=1` — cada fotograma de entrada produce **uno** de salida. Con `d` mayor, `zoompan` repite
  fotogramas y el movimiento se ve a tirones. Si usas `-loop 1`, `d=1` es lo correcto.
- `s=1080x1920` — el tamaño de salida.

**Los números que funcionan:**

| Recorrido total | Cómo se siente | Cuándo |
|---|---|---|
| menos de 5% | no se percibe, no sirve de nada | — |
| **8% – 15%** | **respiración, se siente vivo sin llamar la atención** | el estándar |
| 20% – 35% | dramático, empuja la emoción | remates, revelaciones |
| más de 40% | mareo, y se nota la falta de resolución | nunca en imagen fija |

**Alejarse en vez de acercarse:** empieza en zoom alto y baja. Se siente como "abrir" y funciona muy
bien para revelar contexto.

```bash
zoompan=z='1.18-0.0012*on':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=25
```

**Empuje en diagonal** (mucho mejor que el zoom centrado, porque el movimiento no es simétrico y el ojo
lo lee como cámara real):

```bash
zoompan=z='1+0.0011*on':d=1:x='iw*0.30-(iw/zoom/2)+on*1.1':y='ih*0.45-(ih/zoom/2)':s=1080x1920:fps=25
```

---

## 3. Por qué el empuje solo no basta

Un empuje uniforme sigue siendo **una sola imagen plana moviéndose**. No hay profundidad, no hay
elementos que se comporten distinto, no pasa nada dentro del cuadro. La sensación que da es "esta es una
foto y le pusieron zoom", que es exactamente lo que es.

Las tres formas de arreglarlo de verdad, de menor a mayor esfuerzo:

1. **Parallax por capas** — partes la ilustración en 2 o 3 planos y los mueves a velocidades distintas.
   Media hora de trabajo, resultado enorme.
2. **Animar elementos sueltos** — recortas una pieza (un brazo, el vapor, una hoja) y la mueves aparte.
3. **Animar con IA de video** usando la ilustración como referencia — la imagen se convierte en un plano
   de video de verdad.

---

## 4. Parallax por capas: el mejor retorno por el esfuerzo

> **Parallax:** cuando te mueves, lo que está cerca se desplaza más que lo que está lejos. Es como el
> cerebro calcula la profundidad. Si en tu ilustración el frente se mueve más que el fondo, el cerebro
> lee **volumen** aunque la imagen sea plana.

### Paso 1: partir la ilustración en capas

Necesitas la ilustración en 2–3 archivos PNG con alfa:

- `fondo.png` — el fondo completo, sin el sujeto (relleno donde estaba).
- `medio.png` — elementos intermedios, con alfa.
- `frente.png` — el sujeto principal, recortado (ver `81`).

Cómo conseguirlas, en orden de preferencia:

- **Pedirle al ilustrador las capas.** Si la hizo un humano, ya existen.
- **Generarlas por separado con IA**: mismo prompt de estilo, uno para "el escenario vacío, sin
  personaje" y otro para "solo el personaje sobre croma plano". Coherencia de estilo garantizada si usas
  la misma imagen de referencia (`126`).
- **Recortar a mano** el sujeto de la ilustración plana y rellenar el hueco del fondo. Es lo más lento.

### Paso 2: moverlas a velocidades distintas

```bash
ffmpeg \
  -loop 1 -framerate 25 -t 4 -i fondo.png \
  -loop 1 -framerate 25 -t 4 -i medio.png \
  -loop 1 -framerate 25 -t 4 -i frente.png \
  -filter_complex "\
[0:v]scale=1300:-2,crop=1080:1920:'(iw-1080)/2 - 22*(t/4)':'(ih-1920)/2'[bg];\
[1:v]scale=1220:-2,format=rgba[md];\
[2:v]scale=1150:-2,format=rgba[fr];\
[bg][md]overlay=x='(W-w)/2 - 55*(t/4)':y='(H-h)/2 + 8*(t/4)'[c1];\
[c1][fr]overlay=x='(W-w)/2 - 120*(t/4)':y='(H-h)/2 + 22*(t/4)',format=yuv420p[vout]" \
  -map "[vout]" -c:v libx264 -crf 18 -pix_fmt yuv420p plano_vivo.mp4
```

Lo que hace: en 4 segundos el fondo se corre 22 px, el plano medio 55 px y el frente 120 px. Todos a la
izquierda. El ojo lee una cámara desplazándose por una escena con profundidad.

**Las proporciones que funcionan:** frente ≈ 5x el fondo, medio ≈ 2,5x el fondo. Si el frente se mueve
solo el doble que el fondo, no se percibe. Si se mueve diez veces más, se despega y parece un error.

**Combínalo con un empuje suave** y ya no parece una imagen fija en absoluto: parece un plano.

---

## 5. Animar elementos sueltos

A veces la ilustración solo necesita que **una cosa** se mueva. El vapor de un café. Un letrero que
parpadea. Una moneda que cae. Un brazo que saluda.

Recortas ese elemento como PNG con alfa (`81`), lo quitas de la base, y lo animas aparte:

```bash
# El vapor sube y se desvanece, en bucle, encima de la lamina
ffmpeg -loop 1 -framerate 25 -t 4 -i taza_sin_vapor.png -loop 1 -framerate 25 -t 4 -i vapor.png \
  -filter_complex "\
[0:v]scale=1080:1920[bg];\
[1:v]scale=-1:300,format=rgba[vp];\
[bg][vp]overlay=x=612:y='980-70*mod(t,1.6)/1.6':\
enable='1',format=yuv420p" \
  -c:v libx264 -crf 18 taza_animada.mp4
```

Con `mod(t,1.6)` el movimiento se repite cada 1,6 segundos. Para que además se desvanezca arriba,
combínalo con `geq` sobre el alfa o prerrenderiza el vapor como video con alfa (ver `81`).

**La regla del elemento suelto:** con **uno solo** basta. Si mueves cinco cosas a la vez, vuelves la
ilustración un carrusel y el ojo no sabe dónde parar.

---

## 6. Animar con IA de video usando la ilustración como referencia

La opción más potente a agosto de 2026: le pasas tu ilustración a un modelo de video como **imagen de
partida** y le pides un movimiento concreto. Te devuelve 4–8 segundos de video donde tu ilustración se
mueve de verdad.

Detalles de modelos, costos y parámetros en `120`, `121` y `127`. Lo específico de este caso:

**Cómo se pide bien:**

- **Un solo movimiento, descrito en términos de cámara o de acción física.** "La cámara se acerca
  lentamente mientras el vapor sube de la taza." No: "hazlo dinámico e interesante".
- **Prohíbe explícitamente lo que no quieres:** "sin cambiar el estilo de la ilustración, sin cambiar
  los colores, sin añadir elementos nuevos, sin mover la cámara bruscamente".
- **Duración corta.** 3–4 segundos. Entre más largo, más deriva el modelo del estilo original.
- **La imagen de referencia manda más que el texto.** Es la ley de `126`: se enseña el estilo con
  archivos, no con adjetivos.

**Lo que todavía sale mal (honesto, agosto 2026):**

- **Deriva de estilo:** a los 3 segundos la ilustración empieza a parecer otra cosa. Corta antes.
- **Texto dentro de la imagen:** si tu ilustración tiene letras, el modelo las va a convertir en
  garabatos. Si el rótulo importa, quítalo de la ilustración y ponlo encima con `drawtext` después.
- **Caras y manos:** en ilustraciones estilizadas suelen aguantar; en estilo realista se deforman.
- **Deriva de color:** casi garantizada. Vuelve a imponer la paleta de marca en post (`64`, `125`).

**El flujo seguro:** genera el video, córtalo en el punto donde todavía es fiel, y fuerza el color:

```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 ia_bruto.mp4
ffmpeg -i ia_bruto.mp4 -t 3.2 -vf "scale=1080:1920:flags=lanczos,format=yuv420p" -c:v libx264 -crf 18 plano_ia.mp4
```

Y si el color se fue, el duotono de marca del módulo `64` lo devuelve al redil.

---

## 7. Cuánto durar y cómo salir

Una ilustración animada aguanta **más** en pantalla que una fija, pero no infinito:

| Tipo | Duración máxima antes de aburrir |
|---|---|
| Fija, sin nada | 0,8 s (y aun así se siente) |
| Fija con empuje | 2,5 s |
| Parallax por capas | 4 s |
| Animada con IA / elementos | 5 s |

**Cómo se sale:** nunca por corte seco de vuelta al presentador si la ilustración estaba quieta —
el contraste de "quieto → movido" subraya lo congelado. Si tuvo movimiento, cualquier corte funciona,
porque hay continuidad de movimiento entre los dos planos (ver `54`).

**El truco de la salida en movimiento:** corta **mientras** el empuje está en su punto más rápido. El
ojo lleva inercia y el corte se vuelve invisible.

---

## 8. Cuándo NO animar

- **Cuando la imagen es un dato que hay que leer.** Un gráfico, una captura de pantalla, un precio. El
  movimiento estorba la lectura. Ahí déjala quieta y **acórtala**: 1,5 s con texto grande encima es
  mejor que 4 s moviéndose.
- **Cuando ya hay demasiado movimiento en el video.** Si el resto va a 1,5 s por corte, una lámina
  quieta de 0,8 s es un respiro válido y deliberado (`20`).
- **Cuando el zoom te va a mostrar que la imagen tiene poca resolución.** Si la fuente es de 800 px y
  vas a 1080, el empuje solo revela lo pixelada que está. Mejor quieta y encuadrada.

---

## Errores comunes

1. **Dejar la imagen fija tal cual y esperar que se sienta bien.** No se siente bien. Se siente
   congelada, siempre, sin excepción.
2. **Creer que el empuje lento ya resolvió el problema.** Es un parche. Le quita lo peor. No la vuelve
   viva. Si esa lámina importa, anímala de verdad.
3. **No preescalar antes de `zoompan`.** El movimiento sale a saltitos, como escalones. El `scale=4320:-2`
   antes del zoompan no es opcional.
4. **Usar `d` mayor que 1 con `-loop 1`.** `zoompan` repite fotogramas y el movimiento se ve a tirones.
5. **Zoom de más del 40%.** Marea y delata la resolución de la imagen.
6. **Parallax con capas que se mueven casi igual.** Si el frente no se mueve al menos 4x lo que el
   fondo, no hay profundidad: hay temblor.
7. **Mover cinco elementos a la vez.** Uno. Máximo dos.
8. **Pedirle a la IA de video un plano de 8 segundos.** A partir del tercero deriva el estilo. Genera y
   corta corto.
9. **Dejar texto dentro de la ilustración que le mandas a la IA de video.** Vuelve garabatos las letras.
   El texto va encima, después.
10. **Confiar en que la IA respete los colores de marca.** No los respeta nunca. Se fuerzan en post
    (`64`, `125`).
11. **Animar un gráfico de datos que hay que leer.** El movimiento pelea contra la lectura.
12. **Cortar de una lámina quieta a un plano en movimiento.** El contraste subraya lo muerta que estaba.

---

## Checklist

Antes de dar por buena una ilustración dentro de un video:

- [ ] Saqué la **grilla de fotogramas** y no hay más de 3 cuadritos idénticos seguidos.
- [ ] Si es un parche, es un **empuje del 8% al 15%**, no un zoom bruto.
- [ ] **Preescalé la imagen 4x** antes de `zoompan` y el movimiento se ve fluido, no escalonado.
- [ ] Usé `d=1` con `-loop 1`.
- [ ] Si la lámina es importante, la animé de verdad: **parallax, elemento suelto o IA de video**.
- [ ] En el parallax, el frente se mueve **al menos 4x** lo que el fondo.
- [ ] Se mueve **un solo elemento** protagonista, no cinco.
- [ ] Si usé IA de video, corté **antes** de que derivara el estilo y **volví a imponer la paleta**.
- [ ] Si la ilustración tenía texto, lo saqué antes de mandarla a la IA y lo puse encima después.
- [ ] La duración respeta el tope según el tipo (fija 0,8 s / empuje 2,5 s / parallax 4 s / animada 5 s).
- [ ] La salida corta **en movimiento**, no desde una imagen congelada.
- [ ] Si era un dato para leer, la dejé quieta **y corta**, con el texto grande encima.
