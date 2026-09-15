# 59 — Estabilización: arreglar un plano movido sin deformarlo

> Un plano movido se puede arreglar. Pero la estabilización **no es gratis**: cuesta encuadre, cuesta
> nitidez y a veces produce una deformación peor que el temblor original. Este módulo tiene el
> procedimiento correcto y, sobre todo, los casos en los que **no debes estabilizar**.

---

## Cómo funciona (la parte que hay que entender antes de tocar nada)

La estabilización hace dos cosas:

1. **Analiza** el video y calcula, para cada fotograma, cuánto se movió respecto al anterior:
   desplazamiento horizontal, vertical, rotación y zoom.
2. **Contra-mueve** cada fotograma para cancelar ese movimiento.

Y aquí está el costo que nadie menciona: si el fotograma se corre 30 píxeles hacia la izquierda para
compensar el temblor, **quedan 30 píxeles vacíos en el borde derecho**. Hay que taparlos. La única
forma es **hacer zoom**: agrandar la imagen para que los bordes vacíos queden fuera del cuadro.

> **Estabilizar = perder encuadre + perder resolución.** Siempre. La pregunta no es si cuesta, sino
> si el temblor cuesta más.

En ffmpeg esto se hace con `libvidstab`, que viene en dos filtros y **obligatoriamente en dos pasadas**.

Comprueba primero que tu ffmpeg lo trae:

```bash
ffmpeg -hide_banner -buildconf | grep -i vidstab
```

Debe aparecer `--enable-libvidstab`. Si no aparece, no hay estabilización y no hay nada que hacer.

---

## Las dos pasadas (verificadas)

### Pasada 1 — analizar

No produce video. Produce un archivo de texto con los datos del movimiento.

```bash
ffmpeg -y -i movido.mp4 -an \
  -vf "vidstabdetect=shakiness=6:accuracy=15:result=transforms.trf" \
  -f null -
```

El `-f null -` significa "no escribas video, solo analiza". Es lo que hace esta pasada rápida.

Al terminar debes tener `transforms.trf`. Si el archivo no existe o pesa cero, el análisis falló y la
segunda pasada no va a servir.

```bash
ls -la transforms.trf
```

Parámetros de `vidstabdetect`:

| Parámetro | Rango | Qué hace |
|---|---|---|
| `shakiness` | 1–10 | Cuánto temblor esperas. **6 es el valor de partida.** Sube si el plano va muy movido. |
| `accuracy` | 1–15 | Precisión del análisis. **15** (el máximo) casi siempre; el costo es tiempo de análisis. |
| `stepsize` | — | Cada cuántos píxeles busca. Bajarlo mejora precisión y cuesta tiempo. |
| `mincontrast` | 0–1 | Contraste mínimo para considerar un punto. Baja a `0.2` en planos oscuros o planos. |
| `result` | ruta | Dónde escribe el archivo de datos |

### Pasada 2 — transformar

Ahora sí produce el video corregido.

```bash
ffmpeg -y -i movido.mp4 \
  -vf "vidstabtransform=input=transforms.trf:smoothing=30:zoom=0:optzoom=1:interpol=bicubic,unsharp=5:5:0.8:3:3:0.4" \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p estabilizado.mp4
```

Verificado y funciona.

Parámetros de `vidstabtransform`:

| Parámetro | Qué hace | Valor recomendado |
|---|---|---|
| `input` | El `.trf` de la pasada 1 | obligatorio |
| `smoothing` | Sobre cuántos fotogramas suaviza. **El parámetro clave.** | 10–30 |
| `optzoom` | Zoom automático para tapar los bordes: `0` ninguno, `1` estático, `2` adaptativo | `1` |
| `zoom` | Zoom fijo adicional en porcentaje | `0` si usas `optzoom=1` |
| `interpol` | Cómo interpola al mover: `no`, `linear`, `bilinear`, `bicubic` | `bicubic` |
| `crop` | Qué hace con los bordes: `keep` (los deja) o `black` (negro) | `keep` |
| `maxshift` | Desplazamiento máximo en píxeles | `-1` (sin límite) |
| `maxangle` | Rotación máxima en radianes | `-1` |

### El `unsharp` del final no es opcional

Al mover y reescalar los fotogramas, la interpolación **suaviza la imagen**. Un video estabilizado sin
re-enfocar se ve notablemente más blando que el original. El `unsharp=5:5:0.8:3:3:0.4` compensa eso.

No lo subas mucho: `0.8` en luma es suficiente. Por encima de `1.2` empiezan a aparecer halos en los
bordes de contraste, y eso sí se nota.

---

## El parámetro que decide todo: `smoothing`

`smoothing` define sobre cuántos fotogramas se promedia el movimiento para decidir cuál es el
movimiento "intencional" de la cámara.

| Valor | Resultado | Cuándo |
|---|---|---|
| 5–10 | Solo quita el micro-temblor. Conserva el movimiento del operador. | Plano a mano con movimiento intencional |
| **15–30** | El equilibrio. Movimiento suave, se siente estabilizado sin ser robótico. | **El de partida** |
| 40–60 | Muy pulido. Parece cámara en trípode o gimbal. | Plano que debía ser fijo |
| 80+ | Efecto "flotante". Se siente falso y aparece deriva de fondo. | Casi nunca |

**Regla:** empieza en 30. Si el resultado se siente muerto o antinatural, baja. Si sigue temblando,
sube.

Y una advertencia: `smoothing` alto sobre un plano con movimiento intencional (una panorámica, un
seguimiento) hace que el movimiento se sienta con retraso, como si la cámara respondiera tarde. Es un
artefacto muy visible.

---

## Cuánto encuadre vas a perder

Con `optzoom=1`, ffmpeg calcula el zoom mínimo que tapa los bordes. En la práctica:

| Nivel de temblor | Zoom que aplica | Pérdida de encuadre |
|---|---|---|
| Micro-temblor (mano firme) | 2–5% | Imperceptible |
| Temblor de caminata | 8–15% | Se nota: revisa que no cortes cabezas ni texto |
| Movimiento fuerte (correr) | 20–35% | Grave. Considera no estabilizar |
| Golpes / saltos bruscos | 40%+ | **No estabilices.** El resultado es basura |

**Comprueba siempre el encuadre después de estabilizar.** Un plano donde alguien habla y la
estabilización le cortó la coronilla es peor que el plano temblando.

Para ver cuánto perdiste, compara un fotograma de cada uno:

```bash
ffmpeg -y -i movido.mp4 -ss 2 -frames:v 1 antes.jpg
ffmpeg -y -i estabilizado.mp4 -ss 2 -frames:v 1 despues.jpg
```

---

## Cuándo NO estabilizar (la parte más importante del módulo)

### 1. Cuando el temblor es el lenguaje

Un video de creador grabado a mano **debe** temblar un poco. Es lo que dice "esto lo grabó una persona,
no una productora". Estabilizarlo perfectamente lo vuelve corporativo y le quita la credibilidad que
lo hacía funcionar. Ver `158-ugc-y-creador.md`.

Si tu pieza es UGC, testimonial o de creador: **no estabilices, o estabiliza a `smoothing=8`.**

### 2. Cuando hay obturador rodante (rolling shutter)

Casi todos los celulares leen el sensor de arriba abajo, no de golpe. Cuando la cámara se mueve
rápido, las líneas verticales se inclinan y la imagen "gelatina". Ese defecto **no es temblor**, es
deformación dentro de cada fotograma.

`libvidstab` no lo arregla. Peor: al corregir el movimiento global, la gelatina queda flotando sobre
un cuadro estable y **se hace mucho más visible**.

Síntoma: postes y marcos de puerta que se inclinan cuando la cámara pasa. Si lo ves, no estabilices.

### 3. Cuando el plano ya está estabilizado en la cámara

Casi todos los celulares modernos estabilizan internamente. Estabilizar otra vez produce el efecto
"flotante": el fondo deriva lentamente como si la imagen estuviera nadando. Es de los artefactos más
delatores que existen.

Si el material viene de celular reciente o de una acción-cam, **prueba primero sin estabilizar**.

### 4. Cuando el plano dura menos de 1 segundo

En un reel con cortes de 1,5 s, nadie nota el temblor de un plano de 0,8 s. Estás gastando render y
encuadre para arreglar algo que el espectador no va a ver.

### 5. Cuando el plano tiene mucho texto en pantalla o gráficos

Si le vas a poner un rótulo, la estabilización se hace **antes** de poner el texto. Si el texto ya
está puesto, estabilizarlo lo va a mover junto con la imagen y va a temblar respecto al borde de la
pantalla. Orden correcto: estabilizar → color → texto.

### 6. Cuando el fondo es liso o muy oscuro

`vidstabdetect` necesita puntos de contraste para rastrear el movimiento. Una pared blanca, un cielo
uniforme, un plano nocturno subexpuesto: no hay dónde agarrarse. El análisis sale malo y la corrección
mete movimiento que no existía.

Mitigación: `mincontrast=0.2` en la pasada 1. Si aun así se ve raro, no estabilices.

### 7. Cuando algo grande cruza el cuadro

Si un carro o una persona pasa ocupando media pantalla, el análisis puede confundir **el movimiento
del objeto** con el movimiento de la cámara y corregir hacia el lado equivocado. El plano hace un
tirón brusco justo cuando pasa el objeto.

---

## El flujo correcto y completo

```bash
# 0. Confirma que hay libvidstab
ffmpeg -hide_banner -buildconf | grep -i vidstab

# 1. Mira el plano y decide si de verdad hay que estabilizar (lee la seccion de arriba)

# 2. Analiza
ffmpeg -y -i movido.mp4 -an \
  -vf "vidstabdetect=shakiness=6:accuracy=15:mincontrast=0.3:result=transforms.trf" \
  -f null -

# 3. Comprueba que el archivo de analisis existe y pesa algo
ls -la transforms.trf

# 4. Transforma
ffmpeg -y -i movido.mp4 \
  -vf "vidstabtransform=input=transforms.trf:smoothing=30:zoom=0:optzoom=1:interpol=bicubic:crop=keep,unsharp=5:5:0.8:3:3:0.4" \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p estabilizado.mp4

# 5. Compara el encuadre antes y despues
ffmpeg -y -i movido.mp4      -ss 2 -frames:v 1 antes.jpg
ffmpeg -y -i estabilizado.mp4 -ss 2 -frames:v 1 despues.jpg

# 6. Mira el resultado COMPLETO buscando: deriva de fondo, gelatina, tirones, encuadre cortado
```

El paso 6 no se salta. La estabilización produce artefactos que solo aparecen en algunos segundos del
plano; mirar solo el principio no sirve.

---

## Cuando el resultado no queda bien: qué mover

| Síntoma | Causa probable | Ajuste |
|---|---|---|
| Sigue temblando | `shakiness` muy bajo | Sube a 8–10 y repite la pasada 1 |
| Se ve "flotante", el fondo deriva | `smoothing` muy alto, o ya venía estabilizado | Baja a 10–15, o no estabilices |
| Perdí demasiado encuadre | Temblor muy fuerte | Baja `smoothing`, o acepta `crop=black` y rellena |
| Se ve blando / borroso | Interpolación sin re-enfoque | Añade o sube el `unsharp` |
| Tirones bruscos en algunos puntos | Objeto grande cruzando el cuadro | No estabilices ese plano |
| Movimiento con retraso | `smoothing` alto sobre movimiento intencional | Baja a 8–12 |
| Líneas verticales que ondulan | Obturador rodante | No estabilices; el defecto es otro |

---

## La alternativa que casi nadie considera

Antes de estabilizar, pregúntate: **¿necesito este plano completo?**

Muchas veces el plano está movido en el segundo 3 al 6, y los segundos 0 al 3 están bien. Cortar el
tramo malo es gratis, no cuesta encuadre, no cuesta nitidez y no produce artefactos.

Otra alternativa: **usar el plano temblado como plano corto**. Un plano de 0,7 s temblando dentro de
un montaje rápido se lee como energía, no como error.

> El mejor arreglo de un plano movido suele ser usar menos plano.

---

## Errores comunes

- **Hacerlo en una sola pasada.** `vidstabtransform` sin `vidstabdetect` no tiene datos. Son dos
  pasadas y no hay atajo.

- **No comprobar que `transforms.trf` se creó.** Si el análisis falló, la segunda pasada corre igual
  y produce un video sin corregir. Revisa el archivo.

- **Estabilizar material de celular moderno.** Ya viene estabilizado. La doble corrección produce el
  efecto flotante. Prueba sin estabilizar primero.

- **Estabilizar un plano con obturador rodante.** La gelatina se hace más visible, no menos.

- **`smoothing` muy alto.** El plano se siente muerto y con retraso. 30 es el punto de partida, no 100.

- **No revisar el encuadre después.** Cabezas cortadas, texto fuera de cuadro, producto que ya no se
  ve completo.

- **Olvidar el `unsharp`.** El resultado sale notablemente más blando que el original y no se sabe por
  qué.

- **Estabilizar después de poner el texto.** El texto se mueve con la imagen y tiembla respecto al
  borde. Orden: estabilizar → color → texto.

- **Estabilizar un plano de UGC / creador.** Le quitas exactamente lo que lo hacía creíble.

- **Estabilizar planos de menos de 1 segundo.** Nadie nota el temblor y estás gastando encuadre.

- **Mirar solo el principio del render.** Los artefactos aparecen en tramos concretos. Míralo entero.

- **Estabilizar cuando bastaba con cortar el tramo malo.** El arreglo más barato es usar menos plano.

---

## Checklist

- [ ] Confirmé que este ffmpeg trae `libvidstab`.
- [ ] Decidí conscientemente que hay que estabilizar; no es reflejo automático.
- [ ] El plano no viene ya estabilizado por la cámara.
- [ ] El plano no tiene obturador rodante (líneas verticales que ondulan).
- [ ] El plano dura más de 1 segundo en el montaje.
- [ ] No hay objetos grandes cruzando el cuadro.
- [ ] El fondo tiene contraste suficiente para rastrear; si no, bajé `mincontrast`.
- [ ] Corrí la pasada 1 y verifiqué que `transforms.trf` existe y no está vacío.
- [ ] Usé `optzoom=1` para que tape los bordes automáticamente.
- [ ] `smoothing` está entre 10 y 30, ajustado a si el movimiento era intencional.
- [ ] Añadí `unsharp` para compensar el suavizado de la interpolación.
- [ ] Comparé un fotograma antes/después y el encuadre sigue funcionando.
- [ ] Miré el render **completo** buscando deriva, tirones y gelatina.
- [ ] El texto y los gráficos se pusieron **después** de estabilizar.
- [ ] Si el resultado no convence, consideré cortar el tramo movido en vez de arreglarlo.
