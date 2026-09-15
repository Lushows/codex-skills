# 445 — Halación y sangrado: los dos halos, y su factura

Dos módulos ya cubren la halación y no se repiten aquí. `editpro/257` tiene la receta y sus dosis.
`editpro/434` la mide **como luz** —`YAVG`, `YHIGH`, `VAVG`—, demuestra que `blend` en YUV desplaza las
dos crominancias +25 niveles y da la versión correcta en RGB. Lee esos dos primero.

Este módulo mide la halación **como materia**: cuánta superficie ocupa, en qué parte del cuadro cae
realmente su aporte, y el impuesto que cobra la conversión de espacio de color aunque no toques nada.
Y añade el segundo halo, que ninguno de los dos cubre: el **sangrado de croma**, que es otro fenómeno,
de otra época y con otro filtro.

---

## 1. Halación no es glow

| | Halación (película) | Sangrado (vídeo analógico) | Glow (plantilla) |
|---|---|---|---|
| De dónde sale | la luz atraviesa la emulsión, rebota en la base y vuelve | el ancho de banda de croma es menor que el de luma | de un plugin |
| Qué se desborda | **luz**, y sobre todo la roja | **color**, y solo en horizontal | todo |
| Se ve en | luces fuertes: neón, vela, ventana | bordes saturados: un rótulo rojo | todas partes |
| Filtro | `curves` + `gblur` + `blend=screen` | `boxblur` solo en croma / `chromashift` | `gblur` sobre todo |

La diferencia práctica: la halación **respeta las sombras** (solo desborda desde lo brillante) y el
sangrado **respeta la luminancia** (solo mueve color). Un glow hace las dos cosas mal y por eso se ve
barato (`canales/68`).

---

## 2. Lo que hace de verdad la halación, medido

Cadena de `editpro/257` con `sigma=22`, umbral 0,72 y `all_opacity=0.35`, medida contra su propia
línea base (ver §3, es importante):

| medida | valor |
|---|---|
| píxeles del original por encima del 72 % de brillo | **5,82 %** |
| píxeles que cambian más de 2 niveles | **17,46 %** |
| subida media en todo el cuadro | +0,564 |
| subida media **en las propias altas luces** | **+0,104** |
| subida media **en las sombras (<25 %)** | **+0,846** |
| pico | +72 |
| tinte del halo | R **+0,92** · G −0,15 · B −0,46 |

Tres cosas que la receta no dice:

1. **El halo ocupa tres veces la zona que lo genera.** 5,8 % de fuente, 17,5 % de cuadro afectado.
   Ese factor ×3 es lo que hay que tener en la cabeza al elegir `sigma`: no estás encendiendo las
   luces, estás pintando un tercio más de cuadro alrededor de ellas.
2. **Casi nada de la subida cae en las altas luces** (+0,10). Es matemática de `screen`: sobre un
   píxel que ya está a 240 no queda sitio. Toda la halación que ves ocurre **fuera** de la luz.
3. **Donde más sube es en las sombras** (+0,85, ocho veces más que en las luces). Ese es el precio
   real: la halación **levanta los negros**. Si tu look ya lleva el pie levantado de la curva de cine
   (`editpro/257` §2), se suman y el vídeo pierde el negro. Mide el nivel de tu negro más oscuro antes
   y después.

El tinte sale correcto: R +0,92 frente a B −0,46. El halo es cálido, que es lo que lo hace parecer
película y no plantilla.

---

## 3. El fallo de la cadena publicada: el viaje a `gbrp` cuesta un nivel

La receta convierte a `format=gbrp` para hacer las curvas y el `blend`, y vuelve a `yuv420p`. Ese
viaje **no es neutro**. Prueba nula, sin tocar absolutamente nada por el camino:

```bash
# la imagen sale y vuelve sin que ningún filtro la modifique
ffmpeg -v error -y -i in.mp4 -vf "format=gbrp,format=yuv420p" -c:v libx264 -crf 12 nulo.mp4
```

| cadena | luma media |
|---|---|
| `format=yuv420p` (referencia) | **88,476** |
| `format=gbrp,format=yuv420p` | 87,492 |
| `scale=in_range=tv:out_range=pc,format=gbrp,scale=in_range=pc:out_range=tv,format=yuv420p` | 87,492 |
| `format=yuv444p,format=yuv420p` | **88,477** |

**−0,98 niveles, y declarar los rangos no lo arregla.** El croma sale intacto (U y V idénticos hasta
la tercera cifra), así que es pérdida de luma en la conversión de ida y vuelta.

Consecuencia sobre la halación: el resplandor aporta **+0,564** y el viaje se lleva **−0,984**. El
resultado neto, medido sobre el clip entero, es **87,976 frente a 88,476**: una imagen **medio nivel
más oscura que el original**, cuando la halación solo debería aclarar. La receta funciona —el halo
está ahí, con su pico de +72 y su tinte cálido— pero viene con un impuesto plano encima.

Qué hacer:

```bash
# medir TU pérdida (cada compilación y cada material dan un número distinto)
#   → y compensarla al final de la cadena
... blend=all_mode=screen:all_opacity=0.35, eq=brightness=0.0039, format=yuv420p
```

`0.0039` = 1/255, o sea un nivel. **No lo copies: mídelo.**

Y la tentación obvia —hacer toda la cadena en `yuv444p` y ahorrarse la conversión— está descartada y
medida: el `blend=screen` sobre los planos U y V los empuja **+24 niveles** (115,4 → 139,2 en U). Es
exactamente el defecto 2 de `editpro/434`, que también midió +25 por el mismo camino. El viaje a RGB
con su impuesto de un nivel es la opción correcta; lo que no se puede es no compensarlo.

Nota: la fila de control de `editpro/434` («ida y vuelta a RGB sin efecto», YAVG 66,95 frente a 68,06
de base) es **este mismo impuesto**, −1,11 niveles, medido en otra máquina y sobre otro material. Dos
medidas independientes que coinciden: no es una casualidad de esta compilación.

---

## 4. Sangrado de croma, que es el otro halo

El vídeo analógico transmitía el color con mucho menos ancho de banda que el brillo. Resultado: los
bordes de color se arrastran horizontalmente mientras el dibujo se queda nítido. En ffmpeg se hace
desenfocando **solo** los planos de croma:

```bash
ffmpeg -y -i in.mp4 -vf "format=yuv444p,boxblur=0:0:6:1,format=yuv420p" \
  -c:v libx264 -crf 18 -preset slow -c:a copy out.mp4
```

Los cuatro números de `boxblur` son `luma_radius:luma_power:chroma_radius:chroma_power`. Con luma a
0:0 **la luminancia no se toca**, y eso se verifica:

| `cr` | luma media | satU | satV | bytes |
|---|---|---|---|---|
| 0 | 88,477 | 12,57 | 7,94 | 5 954 674 |
| 3 | **88,477** | 12,58 | 7,93 | 5 856 682 (−1,6 %) |
| 6 | **88,477** | 12,59 | 7,91 | 5 788 447 (−2,8 %) |
| 12 | **88,477** | 12,60 | 7,87 | 5 738 996 (−3,6 %) |

Luma idéntica hasta la tercera cifra en los cuatro casos: la prueba de que el filtro hace lo que dice.
Y **el sangrado abarata el archivo** (−2,8 % a `cr=6`), porque suaviza justo el plano que peor
comprime. Es el único efecto de textura de estos diez módulos que **devuelve** bits.

El desplazamiento lateral de croma (`chromashift`) es otra cosa: es el defecto de un cabezal
desalineado, va con la receta de VHS y vive en `canales/66` y `editpro/57`.

---

## 5. Qué cuesta cada uno

Sobre 5 s de collage 1080p, CRF 12:

| | tiempo | ×ref | bytes | ×ref |
|---|---|---|---|---|
| sin filtro | 22,1 s | 1,00 | 5 979 626 | 1,00 |
| **halación** `sigma=22`, op. 0,35 | **25,9 s** | **1,17** | 6 524 593 | **1,09** |
| sangrado `cr=6` | 23,1 s | 1,05 | 5 788 447 | **0,97** |
| grano `alls=5:t+u` | 35,7 s | 1,62 | 50 758 199 | 8,49 |

**La halación es, con diferencia, la textura con mejor relación efecto/coste** de todo el bloque:
+17 % de tiempo y +9 % de archivo por el rasgo que más lee como cine. Si hay que elegir una sola cosa
con presupuesto de bits apretado, es esta — no el grano.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Confundir halación con glow | El glow desborda desde todo; la halación solo desde las altas luces |
| No hacer la prueba nula de la cadena | El viaje a `gbrp` se come un nivel y nadie lo ve venir |
| Arreglarlo declarando `in_range`/`out_range` | Medido: no cambia nada |
| Pasar toda la cadena a `yuv444p` para evitar la conversión | `screen` sobre U y V: 24 niveles de desvío en el croma |
| Halación encima de una curva de cine con el pie levantado | Se suman en las sombras (+0,85) y el negro desaparece |
| Subir `all_opacity` porque «no se nota en las luces» | Nunca se va a notar ahí: `screen` no tiene sitio. Lo que sube es el resto |
| `sigma` alto creyendo que el halo será más intenso | Solo será más grande; ya ocupa ×3 la zona que lo genera |
| Sangrado con `boxblur` sin poner luma a `0:0` | Desenfocas el dibujo, que es justo lo que el sangrado no hace |
| Sangrado en material moderno sin motivo | Es un defecto de vídeo analógico; en una pieza de 2026 no significa nada |

---

## Relacionado

`editpro/434` bloom y halación medidos como luz (los dos defectos de la receta y la versión en RGB) ·
`editpro/257` la receta de halación, sus dosis y la cadena de look completa ·
`editpro/430` el destello como evento, frente al bloom como estado ·
`editpro/57` `chromashift` y el VHS como efecto declarado · `editpro/443` aberración cromática ·
`editpro/444` viñeta medida · `editpro/449` medir si la textura suma ·
`canales/66` la receta de VHS con croma desplazado · `canales/68` efectos que se ven baratos ·
`canales/67` luz y destellos
