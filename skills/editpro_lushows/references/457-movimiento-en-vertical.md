# 457 — Movimiento en vertical

El mismo plano, el mismo recorrido y el mismo coeficiente se comportan de otra manera en 1080×1920.
No es una cuestión de gusto: cambian las tres cantidades que gobiernan el recurso —el margen
disponible, la velocidad percibida y la franja utilizable— y las tres cambian en direcciones
distintas. Este módulo es el ajuste, con los números.

`147` es el formato vertical a fondo y `45` las zonas seguras por plataforma. Aquí solo lo que afecta
al **movimiento sobre imagen fija**.

---

## 1. El margen: horizontal te sobra, vertical no tienes

Casi todo el material de archivo es horizontal. Al cubrir un lienzo de 1080×1920 con él, la escala la
manda **la altura**, y lo que sobra se va todo al ancho:

| Fuente | Escala para cubrir | Resultado | Sobra horizontal | Sobra vertical |
|---|---:|---|---:|---:|
| 16:9 — 4320×2430 | 0,790 | 3413×1920 | **2333 px** | **0 px** |
| 3:2 — 4500×3000 | 0,640 | 2880×1920 | 1800 px | 0 px |
| 4:3 — 4000×3000 | 0,640 | 2560×1920 | 1480 px | 0 px |
| 1:1 — 3000×3000 | 0,640 | 1920×1920 | 840 px | 0 px |

**Cero de margen vertical, siempre.** La consecuencia es dura y hay que asumirla: en vertical, **un
desplazamiento vertical solo existe si lo compras con zoom**, exactamente como en `456 §1`. Con
`z = 1,12` sobre una fuente de 1920 de alto tienes 206 px de recorrido vertical, y ni uno más.

En cambio el recorrido horizontal es enorme y gratuito: 2333 px sobre un cuadro de 1080 de ancho son
**más de dos pantallas** de travelling lateral sin tocar el zoom. Si el material es horizontal y el
destino es vertical, el gesto natural no es el empuje: **es el barrido lateral**, que además recupera
la parte de la foto que el recorte vertical se comió.

```bash
# barrido lateral por una foto 16:9 dentro de un lienzo vertical
ffmpeg -hide_banner -y -loop 1 -framerate 30 -t 5 -i foto.jpg -filter_complex \
"[0:v]scale=-2:1920:flags=lanczos,crop=1080:1920:'(iw-1080)*0.5+(iw-1080)*0.28*(t/5-0.5)':0,\
setsar=1,format=yuv420p[out]" -map "[out]" -frames:v 150 -c:v libx264 -crf 18 barrido.mp4
```
Aquí el desplazamiento va en `crop`, no en `zoompan`: en `crop` **solo `x` e `y` se pueden animar**
(`455 §2`), y aquí es exactamente lo que hace falta. Recorre el 28% del margen disponible, centrado.

---

## 2. La velocidad: el mismo px/s se lee casi el doble de rápido

El cuadro mide 1080 de ancho en vez de 1920. La misma velocidad absoluta recorre casi el doble de
cuadro por segundo:

| px/s | % del ancho por segundo en 1920 | en 1080 |
|---:|---:|---:|
| 15 | 0,78% | **1,39%** |
| 25 | 1,30% | **2,31%** |
| 40 | 2,08% | **3,70%** |
| 60 | 3,12% | **5,56%** |

> **Traducción operativa: la banda de trabajo de `451` (13–40 px/s) se convierte en vertical en
> 8–24 px/s.** Multiplica por 0,56 (1080/1920) los coeficientes que te funcionaban en horizontal.

El error de no hacerlo es el más común al reciclar un montaje horizontal a vertical: los mismos
números, el mismo recorrido, y el resultado se siente acelerado y mareante sin que nadie sepa decir
por qué.

---

## 3. El recorrido cambia de eje dominante

En un empuje, un elemento del borde se desplaza `ancho/2 · r` en horizontal y `alto/2 · r` en vertical.
Al girar el lienzo, los papeles se invierten:

| Recorrido | 1920×1080: borde h / v | 1080×1920: borde h / v |
|---:|---:|---:|
| 8% | 77 / 43 px | 43 / **77** px |
| 12% | 115 / 65 px | 65 / **115** px |
| 16% | 154 / 86 px | 86 / **154** px |
| 22% | 211 / 119 px | 119 / **211** px |

En horizontal el movimiento dominante de un empuje es lateral; en vertical es **vertical**. Por eso
un empuje que en 16:9 se sentía como «acercarse» en 9:16 se siente como «subir»: lo que más se mueve
es el canto de arriba y el de abajo. Si el sujeto está en el tercio superior, un empuje lo empuja
hacia fuera del encuadre útil.

---

## 4. La franja útil, que es el 64% del lienzo

Descontando las zonas seguras típicas (250 px arriba, 440 px abajo, ver `45`), lo utilizable va de
**y = 250 a y = 1480**: 1230 px de alto, el **64%** del lienzo.

Eso obliga a dos cosas que en horizontal no hacen falta:

1. **El sujeto se encuadra en esa franja, no en el centro del lienzo.** El centro visual está en
   y ≈ 865, no en 960.
2. **La deriva vertical no puede sacarlo de ella.** Con una deriva de 20 px/s sobre un plano de 5 s,
   el sujeto recorre 100 px: hay que reservarlos dentro de los 1230, no dentro de los 1920.

```bash
# comprobar sobre un fotograma real que el sujeto sigue dentro al final del gesto
ffmpeg -y -sseof -0.1 -i plano.mp4 -frames:v 1 -vf \
"drawbox=x=0:y=0:w=iw:h=250:color=red@0.35:t=fill,\
 drawbox=x=0:y=ih-440:w=iw:h=440:color=red@0.35:t=fill" ultimo.png
```
`-sseof -0.1` saca el **último** fotograma, que es el que importa: al principio siempre está bien.

---

## 5. Las tres decisiones que se toman distinto en vertical

| Decisión | Horizontal | Vertical |
|---|---|---|
| Gesto por defecto sobre foto horizontal | empuje centrado | **barrido lateral** |
| Coeficiente de velocidad | 13–40 px/s | 8–24 px/s |
| Recorrido de un empuje | 8–16% | **6–12%** (porque el eje dominante es el largo) |
| Dónde se comprueba el encuadre | primer fotograma | **último** fotograma, con zonas seguras |

---

## Errores frecuentes

1. **Reutilizar los coeficientes del montaje horizontal.** El mismo px/s se lee un 78% más rápido.
2. **Pedir deriva vertical sin zoom.** El margen vertical al cubrir un lienzo 9:16 es exactamente
   cero; la coordenada satura y el plano se queda quieto sin aviso (`456`).
3. **Empujar sobre un sujeto colocado en el tercio superior.** El eje dominante del empuje en vertical
   es el vertical: lo saca del encuadre útil.
4. **Encuadrar en el centro del lienzo** en vez de en el centro de la franja útil (y ≈ 865).
5. **Reservar el margen de deriva sobre los 1920 px** y no sobre los 1230 utilizables.
6. **Comprobar el encuadre en el primer fotograma.** El que falla es el último.
7. **Desperdiciar los 2333 px de margen horizontal** haciendo un zoom centrado sobre una foto 16:9
   que estaba pidiendo un travelling.
8. **Animar el ancho del `crop`** para «ir abriendo» el lienzo. No se puede: `455 §2`.

---

## Relacionado

- `451` — la banda de velocidad en horizontal, que aquí se multiplica por 0,56
- `456` — la fórmula del recorrido disponible, que en vertical da cero en el eje corto
- `455` — por qué el barrido va en `crop` con `x` animada y no en `zoompan`
- `450` — el reparto de gestos, y por qué en vertical cambia el gesto por defecto
- `45` — zonas seguras exactas por plataforma (Reels, TikTok, Shorts)
- `147` — el formato vertical a fondo
- `22` — punch-in y reencuadre: el otro camino para pasar de horizontal a vertical
