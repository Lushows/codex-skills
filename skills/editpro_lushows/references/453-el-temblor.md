# 453 — El temblor

El plano se mueve, el recorrido es el correcto, la velocidad está en banda… y aun así se ve barato.
Casi siempre es **temblor**: el movimiento no avanza lo mismo en cada fotograma. No es el temblor de
una cámara en mano (eso es `59`, otro problema y otra cura): es un artefacto aritmético del propio
filtro, y se arregla con una multiplicación.

---

## 1. De dónde sale

`zoompan` recorta una ventana de la imagen de entrada y sus coordenadas `x` e `y` son **enteros de la
imagen de fuente**. Si el desplazamiento teórico por fotograma es de 3,84 píxeles, lo que ocurre de
verdad es una sucesión de pasos de 3 y de 4. El plano avanza a trompicones.

> **El error de truncado nunca pasa de medio píxel de fuente. Lo que decide si se ve o no es cuántos
> píxeles de pantalla vale ese medio píxel.**

Ampliación efectiva = `salida / (iw/z)`. Con la fuente al tamaño del lienzo (1920 → 1920, z = 1,25) un
píxel de fuente son 1,25 de pantalla: el error llega a 0,63 px y se ve. Con la fuente a 7680, un píxel
de fuente son 0,31 de pantalla: el error máximo es 0,16 px y no existe para el ojo.

Aritmética exacta de un travelling de 100 fotogramas con `z = 1,25` y salida 1920:

| Fuente | Recorrido (px fuente) | Paso medio | Pasos reales | px salida/f | Error máx. (px salida) |
|---:|---:|---:|---|---:|---:|
| 1920 | 384 | 3,84 | 3 y 4 | 4,80 | **0,63** |
| 2688 | 538 | 5,37 | 5 y 6 | 4,79 | 0,45 |
| 3840 | 768 | 7,68 | 7 y 8 | 4,80 | 0,31 |
| 7680 | 1536 | 15,36 | 15 y 16 | 4,80 | **0,16** |

---

## 2. Medido sobre render real

La diferencia media entre fotogramas consecutivos es proporcional al desplazamiento; su dispersión
**es** el temblor. Medido sobre el mismo travelling, 56 fotogramas útiles:

```bash
ffmpeg -hide_banner -loop 1 -framerate 25 -t 2.44 -i foto.png -vf \
"scale=3840:-2,zoompan=z=1.25:d=1:x='(iw-iw/zoom)*on/60':y='(ih-ih/zoom)/2':s=1920x1080:fps=25,\
tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
-frames:v 61 -f null - 2>&1 | grep -o "YAVG=[0-9.]*"
```

| Fuente | Diferencia media | Desviación | **Coeficiente de variación** |
|---:|---:|---:|---:|
| 1920 (sin preescalar) | 3,486 | 0,181 | **5,2%** |
| 3840 (×2) | 3,277 | 0,070 | **2,1%** |
| 7680 (×4) | 3,276 | 0,043 | **1,3%** |

Preescalar al doble divide el temblor entre 2,5; al cuádruple, entre 4. **El umbral práctico está en
el 3%**: por encima se percibe como escalonado en pantalla grande, por debajo es indistinguible de un
movimiento continuo.

⚠️ Este comando **no imprime nada con `-loglevel error`**: `metadata=print` y `signalstats` escriben
en nivel `info`.

---

## 3. La regla

> **La fuente tiene que ser al menos el doble del lienzo. Para movimientos lentos (por debajo de
> 20 px/s), el cuádruple.**

Y el matiz que ahorra horas de render: **preescalar de más no mejora nada y cuesta mucho**. Pasado el
×4 el error de truncado ya está por debajo de 0,16 px de pantalla y lo que ganas es cero; lo que
pierdes son minutos por plano (`458`). El punto de equilibrio del motor documental es una fuente de
**2688 px para un lienzo de 1920**, que es ×1,4: temblor de 0,45 px, por debajo del medio píxel, y un
tercio menos de render que la cadena de 4320.

| Uso | Fuente recomendada | Por qué |
|---|---|---|
| Deriva rápida (> 60 px/s) | 1,4× el lienzo | el ojo no sigue el detalle; el truncado se pierde |
| Empuje normal (13–40 px/s) | 2× | la banda de trabajo |
| Movimiento muy lento (< 12 px/s) | 4× | cada paso es fracción de píxel, el truncado manda |
| Texto o líneas finas en movimiento | 4× **y** `flags=lanczos` | el aliasing del texto se ve antes que nada |

---

## 4. Los otros tres temblores, que se parecen y no lo son

1. **Fotogramas repetidos.** `d>1` en `zoompan`, o `fps` del filtro distinto de `-framerate`. El plano
   avanza y se para, avanza y se para. Se caza con `mpdecimate`, **pero con los umbrales apretados**:
   los de fábrica están pensados para telecine y dejan pasar cualquier movimiento lento.
   ```bash
   ffmpeg -hide_banner -i plano.mp4 -vf "mpdecimate=hi=64:lo=32:frac=0.005" -f null -
   ```
   Medido sobre un plano de 168 fotogramas con un empuje del 12% perfectamente sano, y sobre otro
   completamente quieto de 100:

   | Umbrales | Plano quieto | Empuje 12% |
   |---|---:|---:|
   | `mpdecimate` (por defecto) | 1 de 100 | **3 de 168** |
   | `hi=200:lo=100:frac=0.05` | 1 de 100 | 67 de 168 |
   | `hi=64:lo=32:frac=0.005` | 1 de 100 | **166 de 168** |

   Con los umbrales de fábrica, **un empuje correcto parece 165 fotogramas duplicados**: el filtro no
   sirve para esto sin apretarlo. Con `hi=64:lo=32:frac=0.005` el plano sano conserva 166 de 168 y el
   quieto se hunde hasta 1.
2. **Aliasing de escalado.** La fuente es grande pero el reescalado usa `bilinear` o `area`: los
   bordes finos hierven. Medido sobre un patrón de zonas, `area` mete 22 veces más energía espuria en
   las zonas planas que `lanczos`. Pon `flags=lanczos` y se acabó.
3. **Temblor real del material.** Si la fuente es un vídeo, no una foto, esto no aplica: el sitio es
   `59`, con `vidstabdetect` y `vidstabtransform`.

**Cómo distinguirlos en 10 segundos:** si el temblor desaparece al subir la resolución de la fuente,
era truncado. Si desaparece al fijar `d=1` y `fps`, eran duplicados. Si no desaparece con ninguna de
las dos, es aliasing o es la fuente.

---

## Errores frecuentes

1. **Alimentar `zoompan` con la imagen ya al tamaño del lienzo.** Es la causa del 90% del escalonado.
2. **Preescalar ×4 todo por si acaso.** Multiplica el render sin ganar nada por encima de ese umbral.
3. **Confundirlo con temblor de cámara** y sacar `vidstabtransform`, que sobre imagen fija no tiene
   nada que estabilizar y solo recorta encuadre.
4. **Escalar con `bilinear` o `area`** porque «es más rápido». El hervor de los bordes se ve más que
   el temblor que estabas arreglando.
5. **Dejar `d>1`** y culpar al truncado de un problema de fotogramas repetidos.
6. **Juzgar el temblor en el reproductor a media resolución.** A 50% de escala no se ve; en el móvil
   de quien mira, con la pantalla a 20 cm de la cara, sí.
7. **Medir con `-loglevel error`** y concluir que no hay datos.

---

## Relacionado

- `451` — la media de esa misma serie de diferencias: la velocidad
- `455` — `d`, `fps` y el resto de parámetros de `zoompan` que producen falsos temblores
- `458` — el coste real de preescalar, y por dónde pasa el punto de equilibrio
- `102` — algoritmos de escalado: por qué `lanczos` y no `area`
- `59` — estabilización de vídeo movido de verdad, que es otro oficio
- `canales_lushows/248` — pre-escalado y caché en un motor de montaje, y el fallo de la caché por nombre
- `422` — `utime` frente al reloj: la unidad con la que se compara lo que cuesta preescalar
