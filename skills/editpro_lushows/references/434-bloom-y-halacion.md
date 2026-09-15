# 434 — Bloom y halación

> El destello es un evento; el bloom es un **estado**. Uno dura cinco fotogramas y puntúa una frase
> (`430`); el otro está todo el plano y dice de qué está hecha la imagen. Se confunden porque los dos
> son "luz que sangra", y tienen dosis y controles distintos.

La receta de resplandor vive en `267-particulas-y-elementos-de-luz.md`, §5.1, con su aviso de
"verifícalo en tu equipo". Este módulo **es esa verificación**: la receta medida, los dos defectos que
tiene tal y como está escrita, y la halación, que `267` no cubre.

| | Bloom (resplandor) | Halación |
|---|---|---|
| Qué imita | dispersión de la luz en el objetivo | el halo rojizo del negativo de cine |
| Color | el de la luz que lo produce | **rojo-naranja, siempre** |
| Radio | corto o medio (σ 12–30) | largo (σ 35–60) |
| Se nota en | `YMAX`, `YHIGH` | `VAVG` |

---

## 1. Los dos defectos de la receta clásica

Medido sobre una lámina real del piloto documental (480×270, `YMAX`=145), todo en la misma cadena y con
el mismo método, sin exportar a PNG en medio. Umbral 120 y `sigma`=26 en todas las variantes — 120
porque en esta imagen no hay un solo píxel por encima de 145, y con el 185 de la receta original **el
efecto no tiene a quién iluminar**:

| Variante | YAVG | YHIGH | YMAX | UAVG | VAVG |
|---|---|---|---|---|---|
| **base** | 68,06 | 108 | 145 | 124,06 | 114,16 |
| glow en YUV, suelo `16` (la receta clásica) | **73,70** | 115 | 163 | **149,37** | **139,15** |
| glow en YUV, suelo `0` | 69,36 | 112 | 162 | **149,37** | **139,15** |
| glow en RGB, suelo `0` | 68,36 | 113 | 156 | 123,19 | 113,33 |
| *control: ida y vuelta a RGB sin efecto* | *66,95* | *107* | *144* | *124,03* | *114,17* |

**Defecto 1 — el suelo de 16 lava la imagen entera.** `lutyuv=y='if(gt(val,185),val,16)'` deja la capa
de resplandor a 16 en vez de a 0, y `screen` con un suelo de 16 levanta **todo** el cuadro: +5,64
niveles de luminancia media, un velo lechoso sobre las sombras. Con suelo `0` el velo baja a +1,29.

**Defecto 2, el grave — `blend` en YUV destroza el croma.** Las dos crominancias se desplazan **+25
niveles** (124,06 → 149,37 y 114,16 → 139,15). Es un viraje de color enorme, y es inevitable: `screen`
es una fórmula pensada para valores de luz de 0 a 255, y en YUV los planos U y V tienen el gris en 128.
Aplicarles `screen` los empuja hacia arriba sin sentido físico.

**Lo que no arregla el defecto 2:** `c1_opacity=0:c2_opacity=0` para "proteger" el croma. Medido: el
resultado no cambia **ni un nivel** respecto a no ponerlo. No lo uses como parche.

---

## 2. El bloom que sí: en RGB

Se convierte a RGB, se hace el efecto y se vuelve. Ahí `screen` significa lo que tiene que significar:
sumar luz.

```bash
ffmpeg -y -i plano.mp4 -filter_complex "\
[0:v]format=gbrp,split=2[base][br];\
[br]lutrgb=r='if(gt(val\,190)\,val\,0)':g='if(gt(val\,190)\,val\,0)':b='if(gt(val\,190)\,val\,0)',\
gblur=sigma=26[glow];\
[base][glow]blend=all_mode=screen:all_opacity=0.40,format=yuv420p[o]" \
  -map "[o]" -map 0:a? -c:a copy -c:v libx264 -crf 18 con_glow.mp4
```

El 190 del umbral es sólo un punto de partida: **hay que bajarlo hasta por debajo del `YMAX` real de tu
plano** o no brillará nada. En la lámina medida, con `YMAX`=145, el valor que funciona es 120.

Medido con ese umbral y contra su control: **+1,41 de luminancia media** (nada de velo), `YMAX` de 144 a
156, y las dos crominancias quietas (−0,8). Eso es un resplandor: las luces sangran, el color no se mueve.

> ⚠️ **Mide contra el control, no contra el original.** La ida y vuelta a RGB, por sí sola y sin ningún
> efecto, cuesta **1,11 niveles** de luminancia (68,06 → 66,95). Si comparas el bloom en RGB con el
> vídeo original vas a creer que el efecto no hace nada. El control es
> `-vf "format=gbrp,format=yuv420p"` sin más.

**Los tres mandos y qué hace cada uno:**

| Mando | Rango útil | Qué controla |
|---|---|---|
| umbral del `lutrgb` | 160–215 | **quién** brilla. Por debajo de `YMAX−25` no brilla nadie |
| `sigma` del `gblur` | 12–30 | cuánto se derrama |
| `all_opacity` | 0,25–0,50 | la dosis |

**El umbral es el mando que más se equivoca.** Si la imagen tiene `YMAX`=145 y pones el umbral en 185,
no hay un solo píxel por encima y el efecto no existe — pero como `screen` con el suelo a 16 levanta el
cuadro igual, **parece** que funciona. Mide `YMAX` antes de elegir el umbral (`432`).

---

## 3. Halación

En el negativo de cine, la luz fuerte atraviesa la emulsión, rebota en el soporte y vuelve. Como el
rojo es el que más penetra, el halo que queda alrededor de las altas es **rojo-anaranjado**. Eso es la
halación, y es la mitad de lo que la gente llama "que se vea a película" (`257`).

Se hace igual que el bloom pero **coloreando el halo**: todo el rojo, un tercio del verde, nada de azul.

```bash
ffmpeg -y -i plano.mp4 -filter_complex "\
[0:v]format=gbrp,split=2[base][h];\
[h]lutrgb=r='if(gt(val\,190)\,val\,0)':g='if(gt(val\,200)\,val*0.35\,0)':b=0,gblur=sigma=40[hal];\
[base][hal]blend=all_mode=screen:all_opacity=0.45,format=yuv420p[o]" \
  -map "[o]" -map 0:a? -c:a copy -c:v libx264 -crf 18 con_halacion.mp4
```

Medido contra el control:

| Opacidad | Δ YAVG | YMAX | Δ VAVG (rojo) |
|---|---|---|---|
| 0,45 | +0,08 | 144 → 146 | **+0,11** |
| 0,70 | +0,17 | 144 → 148 | **+0,17** |

La halación casi no mueve la luminancia media — **su firma está en `VAVG`**, el canal de diferencia de
rojo. Si retocas una halación y `VAVG` no se mueve, no estás haciendo halación: estás haciendo bloom
con otro nombre.

**La dosis honesta:** si en una comparación lado a lado ves el halo rojo conscientemente, está al doble.
La halación buena se nota al quitarla, no al ponerla.

---

## 4. Cuándo vale la pena

**Bloom: sí** en cualquier plano con una fuente de luz visible (ventana, lámpara, letrero, reflejo en
metal) y en material de archivo, suave. **No** en producto sobre fondo blanco — se come el borde — ni en
comida (`340`). En vertical para redes, sí, contando con que la recompresión se lleva medio efecto.

**Halación: sólo si el look de película es la marca.** Nunca en archivo en blanco y negro: en ese papel
no había halación, y ponerla es un anacronismo visual.

Y la regla que vale para los dos: **son de plano, no de pieza.** Un bloom global aplicado al render
final aplana los planos que no tenían luces. Se aplica plano a plano, o al menos bloque a bloque.

---

## Errores frecuentes

- **Hacer el `blend` en YUV.** Desplaza las dos crominancias +25 niveles. Es el error grande: se ve como
  un viraje de color que luego se intenta arreglar en el grado.
- **Dejar el suelo del umbral en 16.** Velo lechoso de +5,6 niveles sobre todo el cuadro.
- **Poner `c1_opacity=0:c2_opacity=0` como parche.** Medido: no cambia nada.
- **Elegir el umbral sin mirar `YMAX`.** Si el umbral está por encima del máximo de la imagen, el efecto
  no existe.
- **Comparar el bloom en RGB contra el vídeo original.** La ida y vuelta ya cuesta 1,11 niveles; parece
  que el efecto no hace nada. Compara contra el control.
- **Confundir bloom con destello.** El destello es un evento de 5 fotogramas con sonido (`430`, `433`);
  el bloom está todo el plano y es mudo.
- **Halación sin `VAVG`.** Si el canal rojo no se mueve, es bloom disfrazado.
- **Bloom global sobre el render final.** Aplana los planos sin luces. Va plano a plano.
- **Bloom en producto sobre fondo blanco.** Se come el borde y el producto pierde definición.

---

## Relacionado

- `267` — de dónde viene la receta y el resto del catálogo de partículas y elementos de luz.
- `430`, `431` — el destello: el evento, no el estado. `432` — el arnés de todas las tablas de aquí.
- `435` — fugas de luz: el otro efecto de "luz que sangra", pero local y desde el borde.
- `222` — por qué hay que mirar `YMAX` antes de tocar las altas.
- `63`, `65`, `257` — look de cine, LUTs y emulación de película, donde la halación es media receta.
- `224` — luz de color y neón, si el resplandor tiene que tener color propio.
