# 254 — La piel a fondo

El módulo `67` te dio la regla básica: R > G > B, U entre 100 y 122, V entre 138 y 158, y no dejes la
cara verde. Este módulo es el nivel colorista: **la línea de piel, medida**, cómo se comporta en
pieles claras y oscuras, cómo aislarla y cómo protegerla de un look agresivo.

La razón de que exista un módulo entero es esta frase, salida de un caso real:

> Los cuatro indicadores globales quedaron en verde y la cara seguía morada.

La piel no se juzga con promedios de cuadro. Se juzga midiendo la piel.

---

## 1. La línea de piel: el descubrimiento que ordena todo

Toma un vectorscopio y marca dónde caen distintos tonos de piel. **Todos caen sobre la misma línea.**
No en el mismo punto: en la misma línea. Eso es la *skin tone line* y es la herramienta más poderosa
que existe en corrección de color.

Aquí está medida con ffmpeg, con parches de color reales:

| Tono | RGB | Y | U (Cb) | V (Cr) | SAT | **HUE** |
|---|---|---|---|---|---|---|
| Muy clara | `0xF0D0BC` | 201 | 114 | 143 | 20 | **136** |
| Clara | `0xEFC9A8` | 195 | 108 | 147 | 27 | **133** |
| Clara-media | `0xE0B590` | 179 | 105 | 150 | 31 | **133** |
| Media | `0xBE9178` | 150 | 110 | 150 | 28 | **140** |
| Media-morena | `0xC08A63` | 145 | 103 | 155 | 36 | **137** |
| Morena | `0x8D5524` | 99 | 98 | 156 | 41 | **133** |
| Oscura | `0x5A3620` | 69 | 113 | 145 | 22 | **138** |
| Muy oscura | `0x3B2412` | 51 | 117 | 139 | 15 | **135** |

Míralo bien, porque es la lección entera del módulo:

```
La luminancia (Y) va de 51 a 201  → varía 4 veces
La saturación va de 15 a 41       → varía casi 3 veces
El MATIZ (HUE) va de 133 a 140    → varía 7 grados en total
```

> **Lo que cambia entre un tono de piel y otro es cuánta luz refleja y cuánto color tiene.
> El matiz es prácticamente el mismo en todos los seres humanos: alrededor de 135°.**

Por eso una sola corrección de matiz sirve para todas las pieles del video. Y por eso, cuando la piel
está mal, el error es casi siempre de matiz (se fue a verde, a magenta, a naranja), no de brillo.

### Cómo se calcula ese HUE

`signalstats` de ffmpeg entrega `HUEAVG`, y la fórmula es:

```
HUE = atan2(U - 128, V - 128) en grados + 180
```

Verificado: piel `(U=110, V=150)` → 140,7 y ffmpeg reporta 140. Neón morado `(U=194, V=157)` → ffmpeg
reporta 246.

Y esto es lo que hace medible todo el caso del bar:

| Cosa | HUE |
|---|---|
| **Piel humana (cualquier tono)** | **133 – 140** |
| Neón morado del bar | **225 – 246** |
| Cielo azul | ~297 |

Hay **90 a 110 grados** entre la piel y el neón. Esa distancia es la que permite que una secundaria
arregle la cara sin tocar el neón (`253`). Si estuvieran a 10 grados, no habría nada que hacer con
color y tocaría volver a grabar (`259`).

---

## 2. La línea en el vectorscopio de ffmpeg

Genera el vectorscopio con la retícula de color, que dibuja las referencias:

```bash
ffmpeg -y -ss 6 -i clip.mp4 \
  -vf "vectorscope=mode=color3:graticule=color:flags=name+white:envelope=peak,scale=600:600" \
  -frames:v 1 vs.png
```

Cómo está orientado (verificado empíricamente, porque no es obvio):

- **Eje horizontal = U (Cb).** Izquierda = menos azul. Derecha = más azul.
- **Eje vertical = V (Cr), invertido.** Arriba = más rojo. Abajo = menos rojo.
- Por eso **la piel siempre cae en el cuadrante superior izquierdo**, sobre una diagonal que sale del
  centro hacia arriba-izquierda, entre las marcas de rojo y amarillo.

Comprobación: un parche de piel `0xBE9178` (U=110, V=150) dibuja el punto en el cuadrante superior
izquierdo. Un azul `0x2050C0` (U=184, V=99) lo dibuja en el inferior derecho. Opuestos, como debe ser.

**Cómo se lee en la práctica:** la nube de la cara debe estar **sobre** esa diagonal. Si está a un
lado:

| Desviación | Se ve como | Corrección |
|---|---|---|
| Corrida hacia el amarillo (más abajo) | piel amarillenta, enfermiza | subir magenta o bajar amarillo en `reds` |
| Corrida hacia el magenta (más arriba/derecha) | piel morada, cadavérica | **bajar magenta en `reds` y `magentas`** ← el caso del bar |
| Muy cerca del centro | piel gris, sin vida | subir saturación local, no global |
| Muy lejos del centro | piel de plástico, naranja | bajar saturación local |

---

## 3. El protocolo de medición (el que sí funciona)

Tres pasos. No se salta ninguno.

**Paso 1 — Saca un frame y localiza la cara.**

```bash
ffmpeg -y -ss 6 -i clip.mp4 -frames:v 1 frame.png
```

Ábrelo, busca la **mejilla** o la **frente**. Evita: la zona de brillo especular (el reflejo de la
luz, que no tiene color de piel), la sombra dura, la barba, el maquillaje muy cargado. Anota el
rectángulo en formato `ancho:alto:x:y`.

**Paso 2 — Mide solo ese rectángulo.**

```bash
ffprobe -v error -f lavfi -i "movie=clip.mp4,crop=120:120:840:420,signalstats" \
  -show_entries frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.UAVG,lavfi.signalstats.VAVG,lavfi.signalstats.SATAVG,lavfi.signalstats.HUEAVG \
  -of csv=p=0 -read_intervals "%+#5"
```

**Paso 3 — Compara contra la tabla.**

| Métrica | Sano | Qué significa fuera de rango |
|---|---|---|
| **HUE** | **130 – 145** | < 125: se va a amarillo/verde · > 155: se va a magenta |
| U (Cb) | 96 – 122 | > 128 significa que la piel tiene **más azul que el gris**: imposible en piel sana |
| V (Cr) | 136 – 160 | < 130: piel sin sangre |
| V − U | 20 – 60 | el semáforo rápido del módulo `67` |
| SAT | 15 – 45 | > 55 es piel de plástico; < 12 es piel gris |
| Y | según tono | no lo juzgues por tabla: júzgalo por si se ve la cara |

**El HUE es el rey.** Es el único que no depende del tono de piel de la persona ni de la exposición.
Si el HUE de la mejilla está entre 130 y 145, la piel está bien de color aunque el resto de la imagen
esté teñida.

---

## 4. El caso: cuatro métricas en verde, la cara morada

Reconstrucción de lo que pasó, porque es la enseñanza central del bloque:

1. Se midieron 11 tramos. Los planos de neón daban Y 70–78, U 144–165, V 143–168, SAT 32–57.
2. Se aplicó corrección global (eq por canal + curva en S).
3. Resultado medido: dispersión de saturación **−43 %**, magenta **−40 %**, dispersión de luminancia
   **−55 %**. Todo en verde.
4. Se abrió el video: **la cara seguía morada.**

La aritmética de por qué:

```
Un plano medio en un bar:
  pared + barra + neón + sombra  ≈ 95 % de los píxeles
  la cara                        ≈  5 % de los píxeles

Bajar el magenta global un 40 % =
  bajar el magenta de la pared un 40 %  (visible en la métrica)
  y de la cara, lo que le tocó del promedio  (invisible en la métrica)
```

La métrica global se movió porque se movió la pared. La cara podía haberse quedado exactamente igual
y el número habría dado lo mismo.

**Regla que sale de aquí, y que aplica a todo, no solo a color:**

> Una métrica que promedia todo el cuadro no ve lo que ocupa poco espacio. Y lo que ocupa poco
> espacio (la cara, el logo, el producto) suele ser lo único que importa.

La solución fue una secundaria dirigida al rango de la piel:

```bash
ffmpeg -i corregido.mp4 -vf \
  "selectivecolor=correction_method=absolute:reds=0 -0.10 0.06 0:magentas=0 -0.14 0.04 0" \
  -c:v libx264 -crf 16 -preset slow piel_ok.mp4
```

Y la verificación honesta fueron **dos** mediciones, no una:

```bash
# A) la cara CAMBIÓ (el HUE tiene que bajar hacia 135)
ffprobe -v error -f lavfi -i "movie=piel_ok.mp4,crop=120:120:840:420,signalstats" \
  -show_entries frame_tags=lavfi.signalstats.HUEAVG,lavfi.signalstats.UAVG,lavfi.signalstats.VAVG \
  -of csv=p=0 -read_intervals "%+#3"

# B) el neón NO cambió (el HUE del neón tiene que seguir en 225-245)
ffprobe -v error -f lavfi -i "movie=piel_ok.mp4,crop=200:200:80:100,signalstats" \
  -show_entries frame_tags=lavfi.signalstats.HUEAVG,lavfi.signalstats.SATAVG \
  -of csv=p=0 -read_intervals "%+#3"
```

Si A cambió y B no, la secundaria hizo su trabajo. Si cambiaron las dos, era una global disfrazada.

---

## 5. Piel clara y piel oscura: qué cambia de verdad

Mucho de lo que circula sobre "graduar piel oscura" es ruido. Lo medible es esto:

**Lo que NO cambia:** el matiz. 133–140 en todos los tonos de la tabla de la sección 1. La misma
corrección de matiz sirve para todo el reparto.

**Lo que SÍ cambia:**

1. **La luminancia.** Piel muy clara: Y ≈ 195–205. Piel muy oscura: Y ≈ 50–70. Un contraste que le
   queda bien a la piel clara puede hundir la piel oscura en negro. La curva en S que le da cuerpo a
   una cara clara puede borrarle los rasgos a una oscura. **Este es el error real que se cometió en el
   bar**, solo que con planos en vez de con personas: se aplicó una curva pensada para material bien
   expuesto sobre material que vivía en Y = 75.

2. **La saturación.** Piel oscura mide menos saturación (15–22 en los tonos más oscuros) aunque no sea
   menos "colorida": es que hay menos luz reflejada. Si le subes saturación para "igualarla" a la
   clara, la vuelves anaranjada.

3. **El margen de error.** En piel clara, un tinte de 5 puntos de U se nota poco. En piel oscura, se
   nota mucho más, porque hay menos señal donde esconderlo.

Recomendación práctica cuando hay varios tonos de piel en un mismo video:

```bash
# corrige el MATIZ para todos, con selectivecolor sobre reds
selectivecolor=correction_method=absolute:reds=0 -0.08 0.05 0

# y ajusta el BRILLO por persona, con una ventana o por plano (253)
# nunca al revés
```

---

## 6. Proteger la piel de un look agresivo

Este es el uso avanzado. Quieres un look frío, verdoso, de bar nocturno o de thriller… pero **la cara
no puede irse con él**. Se hace con una máscara de piel invertida.

```bash
ffmpeg -y -i corregido.mp4 -filter_complex "\
[0:v]split=3[base][look][key];\
[key]format=yuva420p,hsvkey=hue=25:sat=0.25:val=0.45:similarity=0.22:blend=0.12,alphaextract,format=gray,gblur=sigma=14,negate[m];\
[look]curves=all='0/0.02 0.3/0.26 0.7/0.74 1/0.98',colorbalance=bs=0.06:gh=-0.03[lk];\
[lk][m]alphamerge[lka];\
[base][lka]overlay,format=yuv420p" \
  -c:v libx264 -crf 16 -c:a copy look_con_piel_sana.mp4
```

Cómo funciona:

1. `hsvkey=hue=25` agarra el rango de la piel (en HSV, la piel está alrededor de 20–30° de matiz;
   ojo, no confundir con el HUE de `signalstats`, que es otra escala).
2. `alphaextract` convierte eso en máscara: piel = blanco.
3. `gblur=sigma=14` suaviza el borde para que no se vea el recorte.
4. **`negate`** la invierte: ahora piel = negro.
5. La capa del look, enmascarada con eso, cae en todas partes **menos en la cara**.

Verifica la máscara antes:

```bash
ffmpeg -y -ss 6 -i corregido.mp4 -vf \
  "format=yuva420p,hsvkey=hue=25:sat=0.25:val=0.45:similarity=0.22:blend=0.12,alphaextract,format=gray,gblur=sigma=14" \
  -frames:v 1 mascara_piel.png
```

Lo blanco debe ser la cara y las manos. Si también agarra una mesa de madera o una pared beige (pasa
mucho), baja `similarity` a 0.15–0.18. Si la máscara pierde la sombra de la cara, súbela a 0.28.

**Límite honesto:** este calificador agarra todo lo que sea del rango de piel, incluida madera, arena
y ropa beige. En una escena con mucha madera clara —un bar, precisamente— hay que apretar el rango o
combinarlo con una ventana (`253`, sección 6).

---

## 7. Las zonas de la cara: no toda es piel

Una cara tiene por lo menos cuatro zonas y solo una es "piel de referencia":

| Zona | Comportamiento | ¿Medir aquí? |
|---|---|---|
| **Mejilla / frente en luz difusa** | piel real | ✅ **sí, siempre aquí** |
| Brillo especular (nariz, frente sudada) | es el color de la **luz**, no de la piel | ❌ nunca |
| Sombra del mentón / cuello | piel + rebote del entorno | ❌ engaña |
| Labios, mejillas rojizas | más V que el resto | ❌ sesga hacia arriba |

Si mides sobre el brillo de la frente en un bar con neón morado, vas a medir **el neón**, no la piel.
Y vas a corregir mal. Ese detalle solo cuesta una vez.

---

## 8. Cuándo la piel no tiene arreglo

Tres casos, honestos (más en `259`):

1. **La cara está quemada** (recorte en la forma de onda pegado a 100). No hay dato: los tres canales
   están en el máximo y no se puede reconstruir el matiz. Se disimula bajando el entorno, nada más.
2. **La cara está en el ruido** (Y por debajo de ~18 en un archivo 8 bits de celular). Al levantarla
   sale el ruido de croma antes que el detalle. `chromanr` ayuda un poco; el resto es aceptarlo.
3. **La luz de la escena tiene el mismo matiz que la piel llevado al extremo** (un cuarto entero con
   luz naranja de sodio a tope). No hay separación de matiz entre piel y ambiente, entonces no hay
   nada que la secundaria pueda distinguir. En el bar hubo suerte: 90° de separación.

---

## Errores comunes

- **Juzgar la piel por el promedio del cuadro.** Es literalmente el error que costó el día del caso
  real. La cara son pocos píxeles.
- **Medir sobre el brillo especular.** Mides la luz, no la piel.
- **Creer que la piel oscura necesita otro matiz.** No: necesita otro tratamiento de **brillo** y
  cuidado con la saturación. El matiz es el mismo (133–140).
- **Aplicar la misma curva de contraste a todas las pieles del video.** La que le da cuerpo a la clara
  le borra los rasgos a la oscura.
- **Subir saturación global para que la piel "tenga vida".** Sube todo, incluido el fondo, y la piel
  se vuelve naranja antes de verse viva.
- **Dejar U por encima de 128 en la cara.** Significa que la piel tiene más azul que el gris. No
  existe piel humana así. Si lo mides, tienes tinte.
- **Aplicar un look frío sin proteger la piel.** Cara gris, cliente incómodo sin saber por qué.
- **Máscara de piel sin `gblur`.** Se ve el recorte de la cara como una calcomanía.
- **Confundir el `hue` de `hsvkey` (0–360 HSV) con el `HUEAVG` de `signalstats`** (otra escala, la de
  este módulo). No son el mismo número.
- **Corregir la piel y no verificar que lo protegido siguió igual.** Dos mediciones, no una.
- **Corregir la piel al final, después del look.** Va antes: es corrección, no estilo.

---

## Checklist

- [ ] Localicé la mejilla/frente en un frame y anoté el rectángulo `ancho:alto:x:y`.
- [ ] Medí **esa zona** con `signalstats`, no el cuadro completo.
- [ ] El `HUEAVG` de la piel está entre **130 y 145**.
- [ ] U está por debajo de 128 (por debajo de 122 idealmente) y V por encima de 136.
- [ ] `V − U` cae entre 20 y 60.
- [ ] La saturación de la piel está entre 15 y 45.
- [ ] Si hay varios tonos de piel, corregí el **matiz** para todos y el **brillo** por persona/plano.
- [ ] Miré el vectorscopio de la **cara recortada** y la nube está sobre la diagonal superior izquierda.
- [ ] Si hay look agresivo, tengo la máscara de piel invertida y la revisé como PNG antes de aplicarla.
- [ ] La máscara está suavizada (`gblur`) y no agarra madera ni paredes beige.
- [ ] Verifiqué con dos mediciones: la cara cambió, la zona protegida no.
- [ ] Miré la cara en movimiento, no solo en un frame.
