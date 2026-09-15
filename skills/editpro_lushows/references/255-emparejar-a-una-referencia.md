# 255 — Emparejar a una referencia

El módulo `62` te enseñó a emparejar tus planos **entre sí**. Este módulo es otra cosa: llevar tu
material al color de **una referencia externa** que te gusta —un fotograma de una película, el
anuncio de un competidor, una foto de una marca— y hacerlo con números, no con "a ver si le achunto".

Es el encargo más común del mundo real: *"quiero que se vea como esto"*.

---

## 1. Lo primero: qué se puede copiar y qué no

Antes de medir nada, hay que separar lo que es color de lo que no lo es. La mayoría de las
referencias que a la gente le gustan **no son color**:

| Lo que ves en la referencia | ¿Es color? | ¿Se puede copiar en post? |
|---|---|---|
| Los tonos, el tinte, el contraste, la saturación | ✅ sí | ✅ sí, y este módulo es cómo |
| La dirección y calidad de la luz | ❌ no | ❌ eso se ilumina, no se gradúa |
| La profundidad de campo (fondo desenfocado) | ❌ no | ❌ eso es el lente y el sensor |
| El vestuario y la escenografía | ❌ no | ❌ eso es arte, se compra o se elige |
| El rango dinámico (detalle en luces y sombras a la vez) | ❌ no | ❌ eso es la cámara |
| El grano / la textura | parcial | ✅ se puede aproximar (`257`) |

> Si la referencia se ve así por la luz, tú puedes graduar todo el día y no vas a llegar. Dilo antes
> de empezar, no después de tres horas.

Este es el filtro honesto que ahorra la mitad de los proyectos frustrados. Detalle completo en `259`.

---

## 2. Medir la referencia

La referencia puede ser una imagen o un video. Se mide igual.

**Si es una imagen (un fotograma, una foto):**

```bash
ffprobe -v error -f lavfi -i "movie=referencia.jpg,format=yuv444p,signalstats" \
  -show_entries frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.UAVG,lavfi.signalstats.VAVG,lavfi.signalstats.SATAVG,lavfi.signalstats.HUEAVG \
  -of csv=p=0
```

**Si es un video, mide varios cuadros y saca el promedio:**

```bash
ffprobe -v error -f lavfi -i "movie=referencia.mp4,signalstats" \
  -show_entries frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.UAVG,lavfi.signalstats.VAVG,lavfi.signalstats.SATAVG \
  -of csv=p=0 -read_intervals "%+#30"
```

**Y mide también, aparte, la zona que de verdad te importa** (la cara, el producto). Ya sabes por qué
(`254`): el promedio del cuadro está dominado por el fondo.

```bash
ffprobe -v error -f lavfi -i "movie=referencia.jpg,format=yuv444p,crop=150:150:600:300,signalstats" \
  -show_entries frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.UAVG,lavfi.signalstats.VAVG,lavfi.signalstats.HUEAVG \
  -of csv=p=0
```

**Cuidado con una trampa clásica:** si sacas el fotograma de referencia de un screenshot o de una
imagen JPG bajada de internet, casi seguro está en **rango completo (0–255)** mientras tu video está
en **rango limitado (16–235)** (`251`). Vas a medir una diferencia de contraste que no es real, es de
etiquetado. Normaliza los dos al mismo rango antes de comparar.

---

## 3. Medir lo tuyo y armar la tabla de diferencias

Mismo comando sobre tu material. Y ahora la tabla, que es todo el método:

| Métrica | Referencia | Lo mío | Diferencia | Qué la mueve |
|---|---|---|---|---|
| YAVG | 140 | 108 | **+32** | `eq=gamma` |
| SATAVG | 62 | 79 | **−17** | `eq=saturation` |
| UAVG | 120 | 127 | **−7** | `eq=gamma_b` |
| VAVG | 142 | 125 | **+17** | `eq=gamma_r` |

Regla de orden (es la misma de `250`): **primero Y, después U/V, al final saturación.** Si cambias el
brillo al final, mueves la saturación percibida y hay que volver a empezar.

---

## 4. De la diferencia al parámetro: las tres conversiones medidas

Aquí está lo que este módulo aporta y que no vas a encontrar escrito en ningún lado: **cuánto mueve
cada filtro, medido con ffmpeg**.

### 4.1 Luminancia → `gamma`

El gamma no es proporcional, es una potencia. La fórmula para llegar de tu `Y` a la `Y` objetivo:

```
gamma = ln(Y_mío / 255) / ln(Y_objetivo / 255)
```

Prueba real, medida: material con `YAVG = 108,2`, objetivo `140`.

| Iteración | gamma calculado | YAVG resultante | Error |
|---|---|---|---|
| 1 | 1,4293 | 135,1 | −3,5 % |
| 2 | 1,5141 | **139,4** | **−0,4 %** |

O sea: **la fórmula te deja a un 3–4 % en la primera pasada, y una segunda iteración cierra la
brecha**. Eso es exactamente cómo trabaja un colorista: calcula, aplica, vuelve a medir, corrige.

Por qué no es exacto de una: el promedio de una potencia no es la potencia del promedio. Con imágenes
reales, no con matemáticas puras, siempre hay que iterar. **Quien te venda una fórmula exacta de una
sola pasada te está vendiendo humo.**

La iteración en código:

```bash
# medir
ffmpeg -y -v error -i mio.mp4 -vf "signalstats,metadata=print:file=m.txt" -frames:v 1 -f null -
grep YAVG m.txt | head -1

# calcular
python -c "import math; print(round(math.log(108.2/255)/math.log(140/255),4))"

# aplicar y volver a medir
ffmpeg -y -v error -i mio.mp4 -vf "eq=gamma=1.4293,signalstats,metadata=print:file=m2.txt" -frames:v 1 -f null -
grep YAVG m2.txt | head -1
```

### 4.2 Saturación → `eq=saturation` (esta sí es exacta)

Medido: material con `SATAVG = 78,9`. Aplicando `eq=saturation=1.35` → `SATAVG = 106,7`.
78,9 × 1,35 = 106,5. **Es lineal.**

```
saturation = SAT_objetivo / SAT_mío
```

Ejemplo de la tabla: 62 / 79 = **0,78**. Se aplica `eq=saturation=0.78` y listo, sin iterar.

### 4.3 Tinte (U y V) → `eq=gamma_r` y `eq=gamma_b`

Medido sobre material neutro, y esto es lo bonito: **funciona igual en material claro y en material
oscuro**, y no toca la luminancia.

| Filtro | Efecto medido |
|---|---|
| `eq=gamma_b=1.10` | U **+4** puntos (Y sin cambio) |
| `eq=gamma_r=1.10` | V **+4** puntos (Y sin cambio) |
| `eq=gamma_r=0.90` | V **−5** puntos (Y sin cambio) |

Regla práctica que sale de ahí:

```
gamma_b ≈ 1 + (ΔU / 40)
gamma_r ≈ 1 + (ΔV / 40)
```

Ejemplo de la tabla: ΔU = −7 → `gamma_b ≈ 0.825`. ΔV = +17 → `gamma_r ≈ 1.425`.

⚠️ Esos valores son grandes; en material real rara vez necesitas más de ±0.15. Si te sale ±0.4,
significa que la referencia y tu material son mundos distintos, y probablemente hay que revisar si el
encargo tiene sentido (sección 7).

### 4.4 Por qué NO uso `colorbalance` para esto

Porque su efecto **depende de dónde vive tu material**. Medido, con el mismo ajuste `b=0.10`:

| Material | `colorbalance=bs` (sombras) | `bm` (medios) | `bh` (altas) |
|---|---|---|---|
| Claro (Y ≈ 198) | U +0,3 | U +0,1 | **U +7,6** |
| Oscuro (Y ≈ 61) | **U +4,0** | U +1,5 | U +2,5 |

En material claro, los medios y las sombras de `colorbalance` **no hacen prácticamente nada**. En
material oscuro, las altas hacen poco. Es un filtro excelente para trabajo dirigido por zona (`252`,
sección 3), y malo para apuntarle a un número.

> Para **llegar a un número**: `gamma_r` / `gamma_b`.
> Para **corregir un tinte que vive en una zona concreta**: `colorbalance`.

---

## 5. El flujo completo, de principio a fin

```bash
# ── 1. medir la referencia
ffprobe -v error -f lavfi -i "movie=ref.jpg,format=yuv444p,signalstats" \
  -show_entries frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.UAVG,lavfi.signalstats.VAVG,lavfi.signalstats.SATAVG \
  -of csv=p=0
# → 140, 120, 142, 62

# ── 2. medir lo mío
ffmpeg -y -v error -i mio.mp4 -vf "signalstats,metadata=print:file=m.txt" -frames:v 1 -f null -
grep -E "YAVG|UAVG|VAVG|SATAVG" m.txt | head -4
# → 108, 127, 125, 79

# ── 3. calcular
python -c "
import math
Y,Yt = 108.0,140.0
U,Ut = 127.0,120.0
V,Vt = 125.0,142.0
S,St =  79.0, 62.0
print('gamma  ', round(math.log(Y/255)/math.log(Yt/255),3))
print('gamma_b', round(1+(Ut-U)/40,3))
print('gamma_r', round(1+(Vt-V)/40,3))
print('sat    ', round(St/S,3))"

# ── 4. aplicar (orden: luma → tinte → saturación)
ffmpeg -y -i mio.mp4 -vf "eq=gamma=1.429:gamma_b=0.825:gamma_r=1.425:saturation=0.785" \
  -c:v libx264 -crf 16 -preset medium paso1.mp4

# ── 5. volver a medir y ajustar
ffmpeg -y -v error -i paso1.mp4 -vf "signalstats,metadata=print:file=m2.txt" -frames:v 1 -f null -
grep -E "YAVG|UAVG|VAVG|SATAVG" m2.txt | head -4

# ── 6. segunda iteración con los valores corregidos, sobre el ORIGINAL (no sobre paso1)
```

**Detalle importante del paso 6:** la segunda iteración se aplica siempre **sobre el original**, con
los parámetros corregidos. No encadenes correcciones sobre correcciones: acumulas pérdida y pierdes
el control de lo que estás haciendo.

---

## 6. Comparar lado a lado (el juicio final es visual)

Los números te acercan. La aprobación es mirando, siempre.

```bash
# Tu plano corregido junto a la referencia, en la misma imagen
ffmpeg -y -ss 4 -i corregido.mp4 -i ref.jpg -filter_complex "\
[0:v]scale=640:360,setsar=1,format=yuv444p,drawtext=text='MIO':x=20:y=20:fontsize=32:fontcolor=white:box=1:boxcolor=black@0.5[a];\
[1:v]scale=640:360,setsar=1,format=yuv444p,drawtext=text='REF':x=20:y=20:fontsize=32:fontcolor=white:box=1:boxcolor=black@0.5[b];\
[a][b]hstack,format=yuv444p" -frames:v 1 comparacion.png
```

Y con los vectorscopios de los dos, que es donde de verdad se ve si emparejaste:

```bash
ffmpeg -y -ss 4 -i corregido.mp4 -i ref.jpg -filter_complex "\
[0:v]scale=480:270,setsar=1,format=yuv444p,split=2[a1][a2];\
[a2]vectorscope=mode=color3:graticule=color:flags=name+white,scale=270:270,format=yuv444p[av];\
[a1][av]hstack[top];\
[1:v]scale=480:270,setsar=1,format=yuv444p,split=2[b1][b2];\
[b2]vectorscope=mode=color3:graticule=color:flags=name+white,scale=270:270,format=yuv444p[bv];\
[b1][bv]hstack[bot];\
[top][bot]vstack,format=yuv444p" -frames:v 1 vs_comparado.png
```

(Recuerda los `format=yuv444p`: sin ellos ffmpeg falla al apilar el vectorscopio con el video, `252`.)

Lo que buscas: que las dos nubes tengan **el mismo centro de masa y la misma extensión**. No que sean
idénticas —el contenido es distinto—, sino que vivan en el mismo sitio.

---

## 7. Los cuatro límites honestos

**Límite 1 — El promedio del cuadro te puede engañar completo.**

Si la referencia es un plano cerrado de una cara y el tuyo es un plano general de un bar, sus
promedios no son comparables: uno es 60 % piel y el otro es 5 % piel. Vas a "emparejar" dos cosas que
no miden lo mismo. **Compara contenidos comparables**, o compara zonas equivalentes (la cara de la
referencia contra tu cara).

**Límite 2 — No puedes copiar rango dinámico que no grabaste.**

Si la referencia tiene detalle en la ventana y en la cara al mismo tiempo, y tu ventana está quemada,
no hay número que te lleve ahí. Eso se grabó con otra cámara o con otra iluminación.

**Límite 3 — No puedes copiar lo que no es color.** Ver sección 1.

**Límite 4 — La referencia puede estar mintiendo.**

Un fotograma de una película que sacaste de internet ya pasó por: compresión, reencodeo, quizá un
filtro de Instagram, y casi seguro un cambio de rango. Estás midiendo la copia de la copia. Si puedes,
consigue la referencia del original.

---

## 8. Cuando la referencia es un competidor

Caso real y frecuente: *"quiero que mi anuncio se vea como el de esta marca"*. Dos advertencias:

1. **El look de una marca es de la marca.** Copiar la paleta exacta de un competidor directo es mal
   negocio antes que problema legal: te vuelves su versión barata. Toma la referencia como dirección
   (más cálido, más contrastado, menos saturado), no como calco (`64`, `196`).
2. **Casi siempre lo que envidias es la producción.** El anuncio del competidor se ve mejor porque
   tiene luz, arte, cámara y talento, no porque tenga otra curva. Mídelo, cópiale lo copiable, y sé
   claro con el cliente sobre el resto.

---

## Errores comunes

- **Empezar a graduar sin separar qué de la referencia es color y qué es luz.** Se pierden horas
  persiguiendo algo inalcanzable.
- **Comparar un plano cerrado contra un plano general.** Sus promedios miden cosas distintas.
- **Medir una referencia en rango completo contra material en rango limitado.** La diferencia de
  contraste que ves es de etiquetado, no de color (`251`).
- **Creer que la fórmula del gamma acierta a la primera.** Deja un 3–4 % de error. Se itera.
- **Iterar encadenando renders.** La segunda pasada va sobre el original con parámetros corregidos.
- **Usar `colorbalance` para apuntarle a un valor de U o V.** Su efecto depende de dónde vive el
  material: medido, `bm=0.10` mueve U +0,1 en material claro y +1,5 en oscuro.
- **Ajustar el brillo al final.** Cambia la saturación percibida y hay que rehacer.
- **Emparejar solo por promedio de cuadro y no revisar la cara.** El error del caso del bar, otra vez.
- **Copiar el look de un competidor tal cual.** Te vuelve su versión barata.
- **No mirar el resultado al lado de la referencia.** Los números acercan; la aprobación es visual.

---

## Checklist

- [ ] Separé qué de la referencia es color y qué es luz, lente, arte o cámara. Se lo dije al cliente.
- [ ] La referencia y mi material están en el **mismo rango** (limited/full) antes de comparar.
- [ ] Comparo contenidos comparables (plano contra plano equivalente, o zona contra zona).
- [ ] Medí referencia y material: Y, U, V, SAT (y HUE si hay piel).
- [ ] Armé la tabla de diferencias antes de tocar un solo filtro.
- [ ] Calculé `gamma` con la fórmula logarítmica, no a ojo.
- [ ] Calculé `saturation` como cociente directo (esa sí es exacta).
- [ ] Usé `gamma_r` / `gamma_b` para el tinte, no `colorbalance`.
- [ ] Apliqué en orden: luma → tinte → saturación.
- [ ] Volví a medir e hice la segunda iteración **sobre el original**.
- [ ] Verifiqué la cara aparte del promedio del cuadro.
- [ ] Miré la comparación lado a lado y los dos vectorscopios antes de dar por bueno.
