# 431 — La campana del fogonazo

> Un destello es un interruptor o es una campana. El interruptor se lee como un error de decodificación;
> la campana se lee como luz. La diferencia son dos fotogramas de subida.

`53` construye el flash **de transición** con `fade` a blanco, y ahí el escalón está bien porque tapa un
corte. Este módulo es el fogonazo **dentro de un plano continuo** (`430`), y ahí el escalón no vale.

---

## 1. Las tres formas, y por qué sólo una funciona

| Forma | Expresión | Cómo se lee |
|---|---|---|
| **Interruptor** | `brightness='if(between(t,3.20,3.32),0.26,0)'` | Salto seco. Parece un fotograma corrupto |
| **Rampa lineal** | `brightness='max(0,0.2-abs(t-3.2)/0.4)'` | Triángulo. La punta se nota como pico duro |
| **Campana de Gauss** | `brightness='0.18*exp(-pow((t-3.20)/0.075,2))'` | Luz. Sube y baja sin bordes |

La campana gana porque **no tiene derivada discontinua en ningún punto**: no hay un fotograma en el que
la luz "arranque". El ojo detecta bordes; un pulso sin bordes no se lee como un fallo.

La expresión canónica, tal y como la escribe el motor documental (`motor.py`):

```
eq=brightness='F*exp(-pow((t-TD)/A\,2))':contrast='1+F*1.4*exp(-pow((t-TD)/A\,2))':eval=frame
```

`F` = fuerza, `TD` = instante del pico, `A` = ancho (la mitad de la campana, en segundos). La coma
dentro de `pow` va **escapada** (`\,`) o ffmpeg la lee como separador de opciones.

> 🔴 **`eq` sólo evalúa expresiones si se le pide `eval=frame`.** Sin eso lee el valor una vez al
> arrancar, `exp(-pow((0-TD)/A,2))` da prácticamente cero, y el filtro queda en identidad: el vídeo sale
> bien, ffmpeg devuelve 0 y **el destello no ocurre**. Medido: con `eval=frame` el recorrido de
> luminancia es de **26,40 niveles**; sin él, **0,04** — o sea, ruido. Es un fallo mudo de manual (`432`).

Contraste: el compañero `volume` del lado del audio **sí** avisa — sin `eval=frame` responde
`Invalid value NaN for volume` y aborta. `eq` calla. Recordarlo evita horas.

---

## 2. La geometría de la campana, medida

Con `exp(-((t−TD)/A)²)`, dos números salen de la propia función y se comprueban en el render:

- **Anchura a media altura (FWHM) = 2·A·√(ln 2) = 1,665·A**
- **Se sale del 10 % del pico en ±1,517·A** → duración visible = 3,03·A

Barrido real sobre una lámina del piloto (480×270, 25 fps, medido con `signalstats` en la misma cadena,
sin recodificar):

| fuerza | ancho | base Y | pico Y | Δ Y | FWHM medida | FWHM teórica | fotogramas visibles |
|---|---|---|---|---|---|---|---|
| 0,10 | 0,075 | 67,06 | 85,09 | +18,03 | 0,115 s | 0,125 s | 5 |
| 0,14 | 0,075 | 67,06 | 90,89 | +23,83 | 0,118 s | 0,125 s | 6 |
| 0,18 | 0,075 | 67,06 | 97,70 | +30,64 | 0,116 s | 0,125 s | 5 |
| 0,22 | 0,075 | 67,06 | 102,56 | +35,50 | 0,131 s | 0,125 s | 5 |
| 0,30 | 0,075 | 67,06 | 119,13 | +52,07 | 0,119 s | 0,125 s | 5 |
| 0,18 | **0,045** | 67,06 | 97,70 | +30,64 | 0,071 s | 0,075 s | **3** |
| 0,18 | **0,090** | 67,06 | 97,73 | +30,67 | 0,144 s | 0,150 s | 7 |
| 0,18 | **0,120** | 67,06 | 97,66 | +30,59 | 0,190 s | 0,200 s | 9 |
| 0,18 | **0,180** | 67,06 | 97,63 | +30,57 | 0,289 s | 0,300 s | 13 |

Tres lecturas que valen para cualquier pieza:

1. **`ancho` y `fuerza` son independientes.** Cambiar el ancho no mueve el pico ni un nivel (97,70 →
   97,63). Se afinan por separado: primero cuánto dura, luego cuánto sube.
2. **La FWHM medida cae siempre dentro de un fotograma (0,04 s) de la teórica.** La discrepancia es
   cuantización de muestreo: a 25 fps una campana de 0,125 s sólo se muestrea tres veces.
3. **Por debajo de `ancho`=0,045 el pulso sólo toca 3 fotogramas.** Si el reproductor salta uno, se
   pierde un tercio del destello.

**Valores de trabajo:** 0,075 s por defecto (visible ≈ 0,23 s, 6 fotogramas a 25 fps) y 0,090–0,095 s
sólo en el destello de remate, para que el más importante dure más sin ser más brillante.

---

## 3. Por qué el contraste va atado al brillo (×1,4)

Subir sólo `brightness` **lava** la imagen: todos los píxeles se desplazan hacia arriba y el plano se
vuelve lechoso, que es exactamente el aspecto de un vídeo mal expuesto. Un fogonazo real no desplaza:
**abre**. Las luces se van arriba mucho y las sombras casi no se mueven.

Eso es lo que hace el término de contraste. Con `contrast = 1 + 1,4·fuerza`, las zonas por encima del
medio suben más que las de abajo, y el destello se lee como luz entrando y no como velo.

Medido en el pico, con `fuerza`=0,18 y `contrast`=1,252, sobre la misma lámina:

| | YMIN | YLOW | YAVG | YHIGH | YMAX |
|---|---|---|---|---|---|
| base | 26 | 42 | 68,1 | 108 | 144 |
| pico | 45 | 65 | 97,7 | 147 | 194 |
| subida | **+19** | +23 | +29,6 | +39 | **+50** |

Las altas suben **2,6 veces** lo que suben las sombras. Eso es un fogonazo. Con sólo brillo, las cinco
filas subirían lo mismo: eso es un velo.

La proporción 1,4 no es sagrada: entre **1,2 y 1,6** funciona. Por debajo de 1,0 el destello lava; por
encima de 2,0 quema las altas antes de que el pulso se vea (`436`).

---

## 4. La trampa de los pasos pequeños

`eq` hace su aritmética con enteros, así que **la respuesta a `fuerza` no es monótona en pasos de 0,01**.
Medido sobre la misma base (Y = 67,05), con la campana en su pico:

| fuerza | 0,08 | 0,09 | 0,10 | **0,11** | 0,12 | 0,13 | 0,14 |
|---|---|---|---|---|---|---|---|
| Δ Y medido | +11,13 | +15,08 | +18,02 | **+16,94** | +17,94 | +19,93 | +23,84 |

Subir de 0,10 a 0,11 **baja** el salto casi un nivel y medio. El modelo afín (`255·[(1+1,4F)(Y/255−0,5)
+0,5+F] − Y`) acierta la pendiente global — unos **170 niveles por unidad de fuerza** — pero se va hasta
2,5 niveles en los valores intermedios.

**Consecuencia práctica: los escalones útiles de `fuerza` son de 0,02, no de 0,01, y el único valor que
cuenta es el medido**, no el calculado. Retocar un destello de 0,14 a 0,15 es perder el tiempo.

---

## 5. Campana asimétrica: cuando quieres que "se apague"

Un flash de xenón sube en microsegundos y decae en decenas de milisegundos. Se imita partiendo el ancho
en dos con un condicional — sube en 3 fotogramas, se apaga en 7:

```
eq=brightness='0.20*exp(-pow((t-3.20)/if(lt(t\,3.20)\,0.045\,0.11)\,2))':\
contrast='1+0.28*exp(-pow((t-3.20)/if(lt(t\,3.20)\,0.045\,0.11)\,2))':eval=frame
```

Sirve para el destello de remate y para el flash de cámara de prensa. **No en los destellos de apoyo:**
la cola larga los convierte en un pulso de exposición, que es otro recurso con otras reglas (`436`).

---

## Errores frecuentes

- **Olvidar `eval=frame`.** El filtro queda en identidad, ffmpeg no dice nada y el destello no existe.
  Recorrido medido sin él: 0,04 niveles.
- **No escapar la coma de `pow`.** ffmpeg parte la opción por ahí y da un error de sintaxis confuso.
- **Usar un `if(between(...))` en vez de la campana.** Es el interruptor: se lee como fotograma corrupto.
- **Subir sólo el brillo.** Lava la imagen. El contraste tiene que ir atado (×1,2 a ×1,6).
- **Afinar la fuerza de 0,01 en 0,01.** El filtro no responde a eso; los pasos útiles son de 0,02.
- **Anchos por debajo de 0,045 s.** 3 fotogramas a 25 fps: si el reproductor salta uno, se pierde un
  tercio del pulso.
- **Anchos por encima de 0,12 s en un destello de puntuación.** Ya no puntúa: respira. Eso es `436`.
- **Dar por bueno el pico calculado.** El modelo se va hasta 2,5 niveles; se mide en 30 s (`432`).

---

## Relacionado

- `430` — cuándo un destello puntúa y cuándo decora. `432` — el arnés de las tablas de aquí.
- `433` — el sonido del fogonazo y su tolerancia de sincronía.
- `436` — la campana ancha y suave: pulso de exposición, otro recurso con otras reglas.
- `438` — qué pasa con estas curvas cuando la base es clara: el salto se dobla.
- `53` — el flash de transición con `fade` (escalón legítimo, porque tapa un corte).
- `102`, `109` — filtros de vídeo de ffmpeg y su catálogo de trampas.
- `canales_lushows` `125-musica-y-destello.md` — la misma campana implementada en `motor.py`, con la
  tabla `DESTELLOS` y el acorde de piano que la acompaña.
