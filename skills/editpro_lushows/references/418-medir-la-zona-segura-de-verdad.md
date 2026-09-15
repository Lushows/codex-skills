# 418 · Medir la zona segura de verdad

**Qué resuelve:** `45` tiene la tabla, `415` tiene la herramienta. Falta el **protocolo de campo**: qué
se hace con el teléfono en la mano para que salga un número defendible, y los cuatro pasos donde la
medida se estropea en silencio. La regla de la casa: *un número de interfaz sin fecha, dispositivo y
método no es un dato, es un recuerdo.*

---

## La escalera de certeza

Cuatro niveles. Cada uno cuesta más y vale más; se sube sólo hasta donde haga falta.

| Nivel | Qué hace | Cuesta | Qué demuestra |
|---|---|---|---|
| 1 · Aritmética | Cruzar la tabla de eventos contra las bandas (`410`) | segundos | Que la composición es coherente con la tabla |
| 2 · Fotograma de control | `drawbox` rojo sobre la banda vetada (`416`) | 1 min | Que nada crítico cae bajo el rojo |
| 3 · Borrador en la app | Subir sin publicar y mirar la vista previa | 5 min | Dónde caen los botones **de verdad** |
| 4 · Carta + captura + resta | Este módulo | 20 min | El número, en píxeles, con fecha |

El nivel 3 basta para no publicar una barbaridad. El nivel 4 es el que produce la tabla que luego usan
`45` y todos los proyectos, y hay que rehacerlo cuando la app se rediseña.

---

## El protocolo, paso a paso

1. **Generar la carta** del lienzo exacto (`415`). Colores saturados, nunca negro ni blanco.
2. **Convertirla en vídeo** de 6 s: `ffmpeg -loop 1 -i carta.png -t 6 -r 30 -pix_fmt yuv420p carta.mp4`.
3. **Publicarla como borrador o no listada** en la superficie real, con **el caption más largo** que
   vayas a usar y, si es pauta, con el botón de llamada a la acción puesto.
4. **Capturar la pantalla del teléfono** con la interfaz visible. En vídeo largo, tocar antes para que
   salgan los controles: si no se tocan, no se miden.
5. **Devolver la captura al lienzo** y **restar**.

Los pasos 1, 2 y 5 son código; el 3 y el 4 son los que no se pueden saltar y los que todo el mundo se
salta.

---

## El paso que hunde la medida: encuadrar la captura

Una captura de móvil **no es tu lienzo**. Es 1080×2400 con barra de estado, barra de navegación y el
vídeo en algún sitio. Restar sin alinear da ruido con decimales.

Y el primer instinto —«detecto el rectángulo del vídeo buscando los colores de la carta»— **no
funciona**, comprobado: la interfaz tapa justo los bordes que quieres encontrar, así que el rectángulo
detectado sale siendo la zona útil, no el vídeo. Con una captura de 1080×2400 devolvió `y 391-1799`,
proporción 0,7665 donde debía ser 0,5625.

La solución es meter en la carta **fiduciales en el centro**, donde ninguna interfaz pinta: dos líneas
horizontales en `y = 0,40·H` y `y = 0,60·H`, y dos verticales en `x = 0,20·W` y `x = 0,80·W`.

```python
esc_y = (yb - ya) / (0.20 * H);   esc_x = (xb - xa) / (0.60 * W)
y0    = ya - 0.40 * H * esc_y;    x0    = xa - 0.20 * W * esc_x
cap.crop((round(x0), round(y0), round(x0 + W*esc_x), round(y0 + H*esc_y))) \
   .resize((W, H), Image.LANCZOS).save("_encuadrada.png")
```

Ejecutado el **11-sep-2026** contra una captura de 1080×2400 con el vídeo colocado a propósito en
`y = 240`:

```
captura (1080, 2400) · escala x 0.9994 y 0.9990 · origen del vídeo x 0.1 y 240.8 · tamaño 1079x1918
```

Y la resta sobre la captura ya encuadrada devuelve exactamente la interfaz que se había inyectado:

```
arriba    150 px   0.078 de la altura
abajo     360 px   0.188
der       150 px   0.139
útil    x 0-929  y 150-1559   (929x1409 px)
```

150, 360 y 150. **Calibrado contra una verdad conocida, que es el único aval que tiene una medida.**

---

## Las cuatro fugas del método

| Fuga | Síntoma | Arreglo |
|---|---|---|
| Carta con negro o blanco | La franja superior sale a 0 px | Magenta y verde |
| Captura sin encuadrar | Todo desplazado; bordes falsos | Fiduciales centrales |
| Controles no invocados | La barra del reproductor no aparece y se declara «limpio» | Tocar la pantalla antes de capturar |
| Caption vacío | El bloque inferior mide 200 px menos que en producción | Escribir el caption real |

Y una quinta que no es del método sino del teléfono: **las esquinas redondeadas y la muesca recortan
píxeles** que ninguna app declara. Por eso el registro de `415` lleva el modelo de dispositivo: la
misma app en dos teléfonos no tapa lo mismo.

---

## Cada cuánto se rehace

| Disparador | Acción |
|---|---|
| Rediseño visible de la app | Rehacer la medida de esa superficie |
| Empezar pauta en una superficie nueva | Medirla con el CTA puesto, nunca heredar el orgánico |
| Aparece un formato nuevo (un lienzo, una ubicación) | Carta nueva de ese lienzo |
| Han pasado seis meses | Rehacer las tres principales; es media hora |
| Una pieza «se ve rara» y nadie sabe por qué | Antes de discutir, medir |

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Medir en el reproductor del ordenador | No hay interfaz: es la ilusión que causa casi todos estos fallos |
| Restar sin encuadrar la captura | Números con decimales que no significan nada |
| Detectar el vídeo por los colores de la carta | La interfaz tapa justo los bordes que buscas |
| No calibrar contra una interfaz conocida | No se distingue un fallo del script de un dato |
| Capturar sin invocar los controles | Se declara segura una banda que no lo es |
| Medir con el campo de caption vacío | La zona inferior real es mucho mayor |
| Guardar el número sin dispositivo ni fecha | Irreproducible: vuelta a empezar dentro de seis meses |
| Subir al nivel 4 para cada pieza | Es para producir la tabla, no para revisar un reel: ahí basta el nivel 2 o 3 |

## Relacionado

`415` la carta, la resta y el registro por red · `45` la tabla vigente y su fecha ·
`416` el caso del reproductor de YouTube · `410` el mapa de intocables ·
`376` la prueba del brazo estirado, que es la verificación complementaria · `92` exportación
