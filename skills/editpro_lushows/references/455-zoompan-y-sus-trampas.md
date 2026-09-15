# 455 — `zoompan` y sus trampas

`zoompan` es el filtro que sostiene todo el movimiento sobre imagen fija, y también el que más tiempo
hace perder, porque **casi todos sus fallos son silenciosos**: el render termina con código 0 y el
resultado está mal. Este módulo es el catálogo completo, con el mensaje de error literal de cada uno.

`102` lo presenta. Aquí están las trampas verificadas una por una.

---

## 1. El esqueleto y lo que significa cada parámetro

```bash
ffmpeg -hide_banner -y -loop 1 -framerate 25 -t 6.730 -i foto_2688.png \
  -filter_complex "[0:v]zoompan=z='1+0.00071429*on':d=1:\
x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,format=yuv420p[out]" \
  -map "[out]" -frames:v 168 -c:v libx264 -crf 18 -preset veryfast plano.mp4
```

| Parámetro | Trampa |
|---|---|
| `d` | está en **fotogramas**, no en segundos. Con `-loop 1` el valor correcto es `d=1` |
| `z` | `zoom` dentro de la expresión es el valor del **fotograma anterior**; `on`, el índice del de salida |
| `x`, `y` | en píxeles de la **entrada**, y se evalúan cada fotograma |
| `s` | tamaño de salida. Si no lo pones, sale 1280×720 y no te avisa nadie |
| `fps` | cadencia de salida del filtro; tiene que coincidir con `-framerate` |

**`d` mayor que 1 con `-loop 1`** hace que `zoompan` repita fotogramas: el movimiento sale a tirones y
la duración final no es la que pediste. Es el fallo número uno y no produce ningún mensaje.

---

## 2. La trampa grande: `crop` no se puede animar en tamaño

Lo natural cuando quieres «revelar progresivamente» algo es animar el ancho de un `crop`. No se puede:

```bash
ffmpeg -loop 1 -framerate 25 -t 2 -i foto.png \
  -vf "crop=w='iw*(0.3+0.4*t/2)':h=ih:x=0:y=0,scale=960:-2" -frames:v 50 -y sale.mp4
```
```
[Parsed_crop_0] Error when evaluating the expression 'iw*(0.3+0.4*t/2)'
[Parsed_crop_0] Failed to configure input pad on Parsed_crop_0
[vf#0:0] Error reinitializing filters!
Task finished with error code: -22 (Invalid argument)
```

**`crop` evalúa `w` y `h` UNA SOLA VEZ, al configurar el filtro**, cuando `t` todavía no existe. Solo
`x` e `y` se evalúan por fotograma. Esto sí funciona:

```bash
ffmpeg -loop 1 -framerate 25 -t 2 -i foto_2688.png \
  -vf "crop=w=1400:h=800:x='(iw-1400)*t/2':y=0,scale=960:-2" -frames:v 50 -y barrido.mp4
```

### Las dos salidas para revelar de verdad

**(a) `geq` sobre el canal alfa** — la máscara es una expresión de `X`, `Y` y `T`, y esas sí se
evalúan por píxel y por fotograma:

```bash
ffmpeg -y -loop 1 -framerate 25 -t 2 -i foto.png -vf \
"scale=960:-2,format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='if(lt(X,W*T/2),255,0)',\
format=yuv420p" -frames:v 50 revelado.mp4
```
Cuesta caro (`geq` evalúa la expresión **por píxel**), así que se usa en planos cortos y en resolución
de trabajo, no en 4K.

**(b) Estados sucesivos del PNG** — generas 3 o 4 versiones de la lámina con más elementos en cada una
y las encadenas con `overlay` + `enable='between(t,...)'`. Es lo que hace un motor de montaje serio:
más archivos, pero el render es composición y vuela.

---

## 3. `eq` sin `eval=frame` se congela sin avisar

Un destello, una subida de brillo, cualquier cosa animada con `eq` necesita `eval=frame`. Sin él, la
expresión se evalúa **una vez al iniciar** y el valor se queda fijo para todo el plano. Medido, con
`signalstats` sobre 50 fotogramas:

| Fotograma | sin `eval=frame` | con `eval=frame` |
|---:|---:|---:|
| 0 | 80,68 | 80,76 |
| 12 | 80,69 | 80,70 |
| 24 | 80,69 | 177,70 |
| 25 | 80,69 | **192,55** |
| 37 | 80,69 | 80,70 |
| 49 | 80,69 | 80,69 |

Sin `eval=frame` la luminancia media no se mueve del 80,69: **el destello sencillamente no ocurre**, y
ffmpeg devuelve código 0 sin una sola línea de aviso.

```bash
# El destello correcto: campana de Gauss sobre t, no un interruptor
eq=brightness='0.45*exp(-pow((t-1.0)/0.10\,2))':contrast='1+0.63*exp(-pow((t-1.0)/0.10\,2))':eval=frame
```
La coma dentro de `pow(...)` va **escapada** (`\,`), o el parser de ffmpeg la lee como separador de
argumentos del filtro. Mismo caso en `hue`, `colorchannelmixer` y `drawtext`.

---

## 4. Las trampas menores, todas silenciosas

- **Sin `s=`** la salida es 1280×720. Si el resto del montaje es 1920×1080, ese plano entra escalado y
  blando y solo se nota comparando.
- **`z` en función de `zoom`** (`z='min(zoom+0.0012,1.35)'`) acumula el valor anterior: el gesto acaba
  donde le toque, no donde dijiste. Con `on` el final es exacto.
- **`x` e `y` sin recalcular con el zoom nuevo.** `iw/2-(iw/zoom/2)` mantiene el centro; poner `x=0`
  con zoom creciente ancla la esquina superior izquierda y el plano se va de lado.
- **No preescalar la entrada.** El movimiento sale a saltitos: es `453`.
- **`format=rgba` olvidado** antes de superponer capas: las transparencias se pierden y salen
  rectángulos negros.
- **`-frames:v` que no coincide con `duración × fps`.** El plano se corta antes y el gesto queda a
  medias. Con 6,730 s a 25 fps son 168 fotogramas, no 168,25.

---

## 5. Los filtros de medida imprimen en nivel `info`

⚠️ `signalstats`, `metadata=print`, `psnr`, `ssim`, `freezedetect`, `blackdetect`, `cropdetect` y
`silencedetect` escriben en nivel `info`. Con `-loglevel error` **no sale absolutamente nada** y
parece que el comando ha fallado:

```bash
ffmpeg -hide_banner -loglevel error -i a.mp4 -i b.mp4 -lavfi psnr -f null -   # no imprime nada
ffmpeg -hide_banner               -i a.mp4 -i b.mp4 -lavfi psnr -f null -   # PSNR y:42.02 ...
```
En un motor de render que corre con `-loglevel error` por limpieza, hay que **quitar el flag solo en
los comandos de medida**. Es la causa habitual de «la verificación no funciona».

---

## Errores frecuentes

1. **`d` en segundos.** `d=5` es un parpadeo de cinco fotogramas, no cinco segundos.
2. **`d>1` con `-loop 1`.** Fotogramas repetidos, movimiento a tirones, duración equivocada.
3. **Animar `w` o `h` de `crop`.** *Error when evaluating the expression*, y la tarea muere con −22.
4. **`eq`, `hue` o `colorchannelmixer` animados sin `eval=frame`.** Se congelan en silencio.
5. **Comas sin escapar dentro de `pow`, `min`, `if`.** El filtro se parte por donde no es.
6. **Olvidar `s=`** y descubrir el 1280×720 al concatenar.
7. **Usar `zoom` en vez de `on`** y que el gesto no acabe donde tenía que acabar.
8. **Medir con `-loglevel error`** y concluir que el comando de verificación está roto.
9. **Confiar en el código de salida.** `zoompan` sale con 0 en casi todos estos casos.

---

## Relacionado

- `450` — el modelo de ventana y margen sobre el que opera `zoompan`
- `451` — de qué velocidad estamos hablando cuando fijamos un coeficiente
- `453` — por qué hay que preescalar la entrada antes de `zoompan`
- `456` — cómo saber si `x` e `y` se han salido del lienzo
- `458` — lo que cuesta cada una de estas cadenas en minutos de render
- `102` — presentación de `zoompan` y de los filtros de encuadre
- `109` — el catálogo general de trampas de ffmpeg
- `108` — `signalstats`, `metadata=print` y el resto del instrumental de medida
- `432` — la trampa de `-loglevel error` documentada sobre el caso de la luz, con el recorrido medido
- `403` — el índice de entrada que se corre cuando un elemento se descarta: el otro fallo mudo del grafo
