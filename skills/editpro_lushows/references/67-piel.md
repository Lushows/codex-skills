# 67 — La piel

Este módulo existe por un solo error, y es **el error más común y más feo de toda la post-producción
de color**:

> **Dejar la piel verde o naranja al aplicar un look.**

Nadie sabe explicar por qué un video le incomoda, pero el cerebro humano tiene un detector de tonos
de piel calibrado desde el nacimiento. Reconocemos cuándo alguien está enfermo, borracho, con frío o
muerto por el color de su cara, en milésimas de segundo. Cuando la piel de un video está mal, el
espectador no piensa "el balance de color está corrido": piensa **"algo está raro con esta
persona"**, y desconfía. En un testimonio o en un anuncio, eso te cuesta la venta.

La piel es la única zona de la imagen donde no hay margen creativo. Todo lo demás lo puedes teñir
como quieras.

---

## 1. Cómo se comporta la piel, físicamente

La piel humana —**toda**, en todos los tonos— cumple siempre la misma regla:

```
Rojo > Verde > Azul
```

Siempre. Es hemoglobina y melanina; no depende del color de la persona. Lo que cambia entre tonos de
piel es **cuánta luz refleja** (la luma), no el orden de los canales ni el matiz.

Proporciones aproximadas, sobre el mismo valor de rojo:

| Tono | R | G | B | Relación aproximada |
|---|---|---|---|---|
| Muy claro | 240 | 200 | 178 | G ≈ 0.83·R · B ≈ 0.74·R |
| Medio | 190 | 145 | 120 | G ≈ 0.76·R · B ≈ 0.63·R |
| Moreno | 140 | 100 | 80 | G ≈ 0.71·R · B ≈ 0.57·R |
| Oscuro | 85 | 58 | 45 | G ≈ 0.68·R · B ≈ 0.53·R |

Lo que hay que grabarse: el verde está siempre entre el 68% y el 84% del rojo, y el azul entre el
53% y el 75%. Si en tu imagen el verde se acerca al rojo, la piel se ve **verdosa/enferma**. Si el
azul sube hacia el verde, se ve **grisácea/cadavérica**. Si el rojo se dispara, se ve
**anaranjada/quemada**.

### En YUV (que es como vive el video)

Las medidas que puedes sacar con ffmpeg están en Y (brillo), U = Cb (azul↔) y V = Cr (rojo↔):

| Medida | Rango sano de piel |
|---|---|
| **U (Cb)** | **100 – 122** (por debajo de 128: menos azul que el gris) |
| **V (Cr)** | **138 – 158** (por encima de 128: más rojo que el gris) |
| Y (luma) | 45–75 en piel clara, 30–50 en piel media, 18–35 en piel oscura (escala 0–100) |

Y una relación que sirve como semáforo rápido: **V − U debe estar entre 20 y 48**. Si baja de 15, la
piel se está yendo a gris/verde. Si sube de 55, se está yendo a naranja.

---

## 2. Cómo medir la piel de verdad (no a ojo)

No se juzga la piel mirando: se recorta la cara y se mide.

**Paso 1 — Saca un frame y localiza la mejilla.** Un rectángulo en la mejilla o la frente, sin
sombra fuerte, sin brillo especular, sin barba.

```bash
ffmpeg -y -ss 6 -i clip.mp4 -frames:v 1 frame.png
```

Abre `frame.png`, mira dónde queda la mejilla y anota el rectángulo (ancho:alto:x:y).

**Paso 2 — Mide solo ese rectángulo:**

```bash
ffmpeg -hide_banner -ss 6 -t 2 -i clip.mp4 \
  -vf "crop=90:90:520:430,signalstats,metadata=mode=print:file=-" -f null - 2>&1 \
  | grep -E "lavfi\.signalstats\.(YAVG|UAVG|VAVG)"
```

Salida ejemplo:

```
lavfi.signalstats.YAVG=52.310
lavfi.signalstats.UAVG=114.208
lavfi.signalstats.VAVG=147.902
```

Lectura: U = 114 (dentro de rango), V = 148 (dentro de rango), V−U = 34 (perfecto). Esta piel está
bien.

Ahora el caso enfermo, después de aplicar un teal & orange mal hecho:

```
lavfi.signalstats.UAVG=126.4
lavfi.signalstats.VAVG=137.1     →  V−U = 10.7  →  PIEL VERDE
```

**Paso 3 — Mide en RGB si prefieres pensar en RGB:**

```bash
ffmpeg -hide_banner -ss 6 -i clip.mp4 -frames:v 1 \
  -vf "crop=90:90:520:430,scale=1:1,format=rgb24" -f rawvideo - 2>/dev/null | xxd -p
```

Te devuelve tres bytes: el promedio R, G, B de la mejilla en hexadecimal. Conviértelos y comprueba
las proporciones de la tabla de arriba.

**Este chequeo se hace DOS veces:** antes del look y después del look. Si los números se movieron
fuera de rango, el look está mal, no la persona.

---

## 3. Prevención: dónde se daña la piel

La piel casi nunca se daña "por accidente". Se daña en cuatro sitios concretos, y en todos se puede
evitar de entrada:

### a) Split toning en los **medios**

El error madre. La piel vive en los tonos medios. Si haces:

```bash
# ❌ MAL — esto pone la cara verde
colorbalance=gm=0.10:bm=0.08
```

…estás empujando los medios al teal y la cara se va con ellos. La regla del módulo `63` era clara:
**en el split toning solo se tocan sombras (`s`) y luces (`h`). Los medios (`m`) no se tocan.**

```bash
# ✅ BIEN — sombras al teal, luces al cálido, medios intactos
colorbalance=rs=-0.05:bs=0.07:rh=0.04:bh=-0.03
```

### b) Saturación global alta

`eq=saturation=1.25` sube todo, y lo que más se nota subido es la cara. Resultado: gente color
zanahoria. Por eso la saturación global se queda por debajo de 1.10 y el resto se hace con
`selectivecolor`.

Y el error silencioso: aplicar saturación en la corrección **y otra vez** en la gradación. 1.10 ×
1.10 = 1.21. Ya estás en zona naranja sin haberlo decidido.

### c) Curvas de contraste muy fuertes en piel oscura

Una curva en S fuerte (`0/0 0.25/0.17 …`) hunde los tonos medios-bajos. Ahí es donde vive la piel
oscura. Resultado: se pierde el detalle de la cara, la persona queda como una silueta y se lee como
descuido (porque lo es).

Con piel oscura en cuadro: **curva suave** (`0.25/0.22`), y si necesitas contraste, sácalo del
fondo, no de la cara.

### d) Balance de blancos mal corregido de origen

Si el plano venía verdoso por un tubo fluorescente y solo lo corregiste "a ojo", el look encima
amplifica lo que quedó. Se corrige antes, midiendo (`61`, `62`).

---

## 4. Corrección: arreglar la piel sin arruinar el look

Si ya mediste y la piel está fuera de rango, hay tres niveles de intervención. Empieza por el
primero.

### Nivel 1 — `selectivecolor` (lo más simple, casi siempre suficiente)

La piel vive en las familias **rojos** y **amarillos**. Los cuatro valores son cian, magenta,
amarillo y negro, de −1 a 1. Valores negativos de cian = **más rojo**.

```bash
# Piel verdosa → quitarle verde/cian y devolverle rojo
ffmpeg -i in.mp4 -vf \
  "selectivecolor=reds=-0.10 0.02 0.05 0:yellows=-0.08 0 0.04 0,format=yuv420p" \
  -c:v libx264 -crf 18 out.mp4

# Piel anaranjada → quitarle amarillo y bajarle un punto de magenta
ffmpeg -i in.mp4 -vf \
  "selectivecolor=reds=0.03 -0.04 -0.10 0:yellows=0.02 0 -0.12 0,format=yuv420p" \
  -c:v libx264 -crf 18 out.mp4
```

Dosis: `0.04 – 0.12`. Si necesitas más de `0.20`, el problema es de corrección y estás parchando.

### Nivel 2 — Gammas por canal en los medios

```bash
# Piel con verde: bajar verde, subir rojo — solo en los medios
ffmpeg -i in.mp4 -vf "eq=gamma_g=0.97:gamma_r=1.02,format=yuv420p" -c:v libx264 -crf 18 out.mp4
```

Ojo: esto toca **toda** la imagen, no solo la piel. Úsalo cuando el problema sea general.

### Nivel 3 — Máscara de piel (protección quirúrgica)

Cuando el look es muy fuerte (un duotono de marca, por ejemplo) y quieres el look en todo **menos**
en la cara. Se hace con tres piezas: una copia sin graduar, una copia graduada, y una máscara que
diga dónde está la piel.

```bash
ffmpeg -i in.mp4 -filter_complex "\
[0:v]split=3[orig][para_grado][para_mascara];\
[para_grado]curves=all='0/0.03 0.25/0.20 0.5/0.5 0.75/0.81 1/0.99',\
            colorbalance=rs=-0.06:bs=0.09:rh=0.05:bh=-0.04[graded];\
[para_mascara]hsvkey=hue=22:sat=0.32:val=0.55:similarity=0.20:blend=0.14,\
              alphaextract,negate,gblur=sigma=6,lutyuv=y='val*0.75'[mask];\
[graded][orig][mask]maskedmerge,format=yuv420p[v]" \
  -map "[v]" -map 0:a? -c:v libx264 -crf 17 -c:a copy out_piel_protegida.mp4
```

Qué hace cada pieza:

| Pieza | Función |
|---|---|
| `split=3` | tres copias: original, para graduar, para la máscara |
| `hsvkey=hue=22:sat=0.32:val=0.55` | selecciona el rango de tono de la piel (matiz ~22°, naranja) |
| `similarity=0.20:blend=0.14` | qué tan ancha es la selección y qué tan suave el borde |
| `alphaextract` | convierte esa selección en una imagen en blanco y negro |
| `negate` | invierte, para que la piel quede **blanca** |
| `gblur=sigma=6` | suaviza el borde de la máscara — **sin esto se ve el recorte** |
| `lutyuv=y='val*0.75'` | baja la máscara al 75%: protección parcial, no total |
| `maskedmerge` | donde la máscara es blanca toma el original; donde es negra, el graduado |

**Ajusta `hue` según el tono de piel:** 18–20 para piel muy clara, 20–24 para media, 22–28 para
morena y oscura. Y comprueba la máscara antes de usarla:

```bash
# Ver la máscara sola, para saber si está agarrando la cara y no la mesa de madera
ffmpeg -y -ss 6 -i in.mp4 -frames:v 1 -vf \
  "hsvkey=hue=22:sat=0.32:val=0.55:similarity=0.20:blend=0.14,alphaextract,negate" mascara.png
```

Si la máscara agarra la madera, el cartón, el pan o la arena —que están en el mismo rango de matiz
que la piel—, baja `similarity` o sube `sat`. **Ninguna máscara automática es perfecta**; por eso la
protección es parcial (75%) y no total.

**Cuándo usar máscara:** duotono de marca sobre testimonios, looks muy saturados, planos donde la
cara ocupa poco cuadro. **Cuándo no:** si la persona se mueve mucho o hay varias personas con tonos
distintos, la máscara va a fallar. Ahí es mejor bajar la fuerza del look.

---

## 5. Piel oscura: lo que casi nadie hace bien

En Colombia y en toda Latinoamérica vas a grabar todos los tonos de piel, y la mayoría de los tutos
de color están hechos pensando en piel muy clara. Tres cosas concretas:

1. **Expón para la piel, no para el fondo.** Si la persona es de piel oscura y detrás hay una
   ventana, la cámara automática expone para la ventana y la cara se va a negro. Se resuelve en
   rodaje (ver `173-iluminacion-basica.md`), pero en post lo que puedes hacer es **subir gamma sin
   tocar el punto negro**:
   ```bash
   ffmpeg -i in.mp4 -vf "curves=all='0/0 0.2/0.29 0.5/0.56 1/1',format=yuv420p" -c:v libx264 -crf 17 out.mp4
   ```
   Fíjate: el `0/0` se queda; lo que sube es el 0.2 y el 0.5. Eso abre la cara sin lavar la imagen.

2. **No apliques curvas en S fuertes.** Hunden justo la zona donde vive esa piel.

3. **Cuidado con el magenta.** Los sensores tienden a meter magenta en piel oscura, y con look
   encima se ve morado. Comprueba: si V−U pasa de 50 y la piel se ve rosada, baja magenta en
   `selectivecolor=reds` (segundo valor, negativo).

Y una regla que vale para todos los tonos: **el color de la piel no se "corrige hacia un ideal"**.
Se corrige hacia el color real de esa persona. Aclarar u oscurecer sistemáticamente la piel de
alguien no es color: es otra cosa, y no la hacemos.

---

## 6. La prueba final de un minuto

Antes de entregar cualquier video con gente:

```bash
# 1) Frame de la cara, antes y después
ffmpeg -y -ss 6 -i bruto/clip.mp4  -frames:v 1 -vf "crop=90:90:520:430,scale=200:200" piel_antes.png
ffmpeg -y -ss 6 -i final/clip.mp4  -frames:v 1 -vf "crop=90:90:520:430,scale=200:200" piel_despues.png

# 2) Los dos parches lado a lado
ffmpeg -y -i piel_antes.png -i piel_despues.png -filter_complex "hstack=inputs=2" piel_comparacion.png

# 3) Los números del resultado final
ffmpeg -hide_banner -ss 6 -t 2 -i final/clip.mp4 \
  -vf "crop=90:90:520:430,signalstats,metadata=mode=print:file=-" -f null - 2>&1 \
  | grep -E "UAVG|VAVG"
```

Verifica: **U entre 100 y 122**, **V entre 138 y 158**, **V − U entre 20 y 48**. Si pasa, entrega.
Si no pasa, vuelve al nivel 1 de corrección.

---

## Errores comunes

- **Mover los medios en el split toning.** Es la causa del 90% de las caras verdes. Solo sombras y
  luces.
- **Saturación global por encima de 1.10.** Caras naranja.
- **Saturación aplicada dos veces** (corrección + gradación) sin darte cuenta. Se multiplican.
- **Curva en S fuerte con piel oscura en cuadro.** La cara pierde detalle y queda de silueta.
- **Juzgar la piel a ojo en un monitor sin calibrar.** Mide con `signalstats` en un recorte de la
  mejilla.
- **Medir la piel en un frame con brillo especular o con sombra fuerte.** El parche tiene que ser
  piel plana e iluminada.
- **Aplicar un duotono de marca al 100% sobre un testimonio.** La persona se ve enferma y la pieza
  pierde credibilidad. Usa máscara o baja la intensidad.
- **Máscara de piel sin `gblur`.** Se ve el borde del recorte y queda peor que sin máscara.
- **Máscara de piel que agarra la madera, el pan o la arena.** Míra la máscara antes de confiar en
  ella.
- **Protección de piel al 100%.** La cara se queda fuera del look y se ve pegada. 60–80% es la zona.
- **Asumir que un rango de `hue` sirve para todos los tonos de piel.** Ajústalo por persona.
- **Corregir la piel hacia un "ideal" en vez de hacia el color real de esa persona.**

---

## Checklist

- [ ] Identifiqué todos los planos donde hay piel visible.
- [ ] Medí U, V e Y en un recorte de mejilla **antes** de graduar.
- [ ] El split toning no toca `rm/gm/bm` (los medios).
- [ ] La saturación global final está por debajo de 1.10, contando **todas** las etapas.
- [ ] Si hay piel oscura, la curva en S es suave y el punto negro sigue en `0/0`.
- [ ] Medí U, V y V−U **después** del look, en el mismo recorte.
- [ ] U está entre 100 y 122; V entre 138 y 158; V−U entre 20 y 48.
- [ ] Si usé máscara de piel: la revisé como imagen, tiene `gblur`, y la protección es parcial
      (60–80%).
- [ ] Comparé el parche de piel antes/después lado a lado.
- [ ] Si el look fuerte y la piel son incompatibles, bajé el look — no la credibilidad de la persona.
- [ ] Todos los planos con la misma persona tienen la misma piel entre sí (no salta de un corte a
      otro).
