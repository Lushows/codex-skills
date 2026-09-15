# 30 · Catálogo de movimientos

**Qué resuelve:** todo el material es estático; el movimiento es lo único que separa un
plano vivo de una lámina escaneada. Repertorio cerrado: siete gestos con su expresión.

---

## Los siete gestos

| Gesto | Qué hace | Cuándo |
|---|---|---|
| **Empuje** | El plano crece hacia el centro (o hacia un punto) | Entrar en la historia, la cara, el detalle culpable |
| **Alejamiento** | El plano se abre y aparece el entorno | Revelar contexto, consecuencia, soledad |
| **Deriva diagonal** | El cuadro se desplaza lento sin cambiar de tamaño | Inquietud, transición, planos de apoyo |
| **Parallax** | Figura y fondo a velocidades distintas | Retrato principal, plano de peso (ver `33`) |
| **Golpe de escala** | Un elemento aterriza de 1,14× a 1,00× en 0,18 s | Cifras, sellos, titulares. Con sonido |
| **Péndulo** | Balanceo de ±0,5° a 0,9° con periodo largo | Recortes de papel colgados, fotos sueltas |
| **Latido** | Escala que respira ±1,5% | Elementos que viven mucho y no deben congelarse |

**Presupuesto:** recorrido del fondo entre **8% y 16%**; solo los travellings
intencionados (`37`) pasan de ahí. La tasa se calcula, no se tantea:

```
k = recorrido / (fps · duración_del_plano)

recorrido 0,12 · 25 fps · 4,0 s  →  k = 0,12 / 100 = 0,0012
```

---

## 1 · Empuje

```bash
ffmpeg -loop 1 -t 4 -i fondo.png -filter_complex "
[0:v]scale=4320:-2,
     zoompan=z='1+0.0012*on':d=1:
             x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':
             s=1920x1080:fps=25
" -r 25 -pix_fmt yuv420p -y plano.mp4
```

`scale=4320:-2` **antes** del `zoompan` no es opcional: `zoompan` trunca `x` e `y` a
enteros y sobre una imagen a tamaño final el movimiento sale a saltos.

Para empujar hacia un punto que no es el centro (62% del ancho, 38% del alto):

```
x='(iw-iw/zoom)*0.62':y='(ih-ih/zoom)*0.38'
```

## 2 · Alejamiento

`zoompan` **acota el zoom a un mínimo de 1,0**. Un alejamiento se construye empezando
arriba y bajando hacia 1,0x, nunca por debajo:

```
zoompan=z='max(1.0,1.14-0.0012*on)':d=1:
        x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25
```

## 3 · Deriva diagonal

Con el zoom fijo, el margen disponible es `iw-iw/zoom`. Se recorre en fracciones de ese
margen, así la expresión nunca se sale del cuadro:

```
zoompan=z='1.14':d=1:
        x='(iw-iw/zoom)*(0.30+0.40*on/100)':
        y='(ih-ih/zoom)*(0.60-0.25*on/100)':s=1920x1080:fps=25
```

Para un **elemento** con alfa la deriva va en el `overlay`, en px por segundo:

```
[bg][el]overlay=x='980+18*(t-1.20)':y='320-11*(t-1.20)':
                enable='gte(t,1.20)*lt(t,4.60)'
```

18 px/s a la derecha y 11 px/s hacia arriba. Banda útil: **6 a 30 px/s**. Por debajo de
6 no se percibe; por encima de 30 el elemento "se va" y distrae.

## 4 · Parallax

Dos PNG: fondo a 1,0× y figura a 1,6-2,4× de esa velocidad. Módulo propio: `33`.

## 5 · Golpe de escala

```bash
[1:v]format=rgba,
     scale=w='iw*(1.00+0.14*(1-min(1,max(0,(t-2.00)/0.18))))':h=-1:eval=frame[el];
[bg][el]overlay=x='(W-w)/2':y='(H-h)/2-60':enable='gte(t,2.00)'
```

`overlay` reevalúa `w` y `h` cada fotograma, así que `(W-w)/2` mantiene el centro
mientras el elemento encoge. El golpe dura **0,14-0,20 s**; más largo se vuelve zoom.

## 6 · Péndulo

```bash
[1:v]format=rgba,
     rotate=a='0.012*sin(2*PI*t/3.2)':c=none:ow=rotw(0.012):oh=roth(0.012)[el]
```

`ow`/`oh` se evalúan una sola vez: se les pasa la **amplitud máxima** como constante, no
la expresión. 0,012 rad = 0,69°. Amplitud útil: 0,006 a 0,016 rad. Periodo 2,8-4,5 s.

## 7 · Latido

```bash
[1:v]format=rgba,scale=w='iw*(1+0.015*sin(2*PI*t/2.0))':h=-1:eval=frame[el]
```

±1,5%, periodo 2 s. Suelo mínimo de un elemento que vive más de 3 s sin otro gesto:
impide los fotogramas idénticos (`35`).

**Combinar:** máximo dos gestos por plano y de familias distintas. Fondo con empuje +
elemento con deriva, sí; fondo con empuje + fondo con deriva, cámara borracha.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| `zoompan` sin `scale` previo | El movimiento avanza a saltos de píxel entero |
| `z` por debajo de 1,0 | Se acota a 1,0 y el alejamiento se congela a medio camino |
| Expresión de `ow`/`oh` en `rotate` | Se evalúa una vez y recorta el elemento al girar |
| `zoompan` sobre PNG con alfa | Camino frágil. Con alfa se usa `scale=eval=frame` + `overlay` |
| Recorrido por encima del 16% sin motivo | El fondo se lee antes que el contenido |
| Mismo gesto en tres planos seguidos | El ojo lo detecta y deja de mirar (`38`) |

## Relacionado

`31` curvas de aceleración · `33` parallax real · `34` movimiento que narra ·
`35` animar una foto fija · `37` cámara simulada · `38` ritmo del movimiento
