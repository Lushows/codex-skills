# 251 — Ciencia del color (lo que necesitas y nada más)

Este módulo existe para que dejes de romper imágenes sin saber por qué. No es teoría por gusto: cada
concepto de aquí corresponde a un daño concreto que verás en tus videos.

Los cuatro daños que este módulo previene:

1. El video se ve **lavado y grisáceo** al subirlo, aunque en tu computador se veía bien.
2. Los negros se ven **grises** y los blancos **sucios** (o al revés: se comen el detalle).
3. Al aplicar una LUT o un filtro, la imagen **explota** en contraste o se vuelve verde.
4. En el celular se ve **completamente distinto** al monitor.

Todos son el mismo problema de fondo: alguien interpretó los números de tu imagen con la regla
equivocada.

---

## 1. Un video son números, y los números no significan nada solos

Un píxel de video es un trío de números. Digamos `(180, 90, 140)`.

Esos números **no son un color**. Son coordenadas. Para que sean un color hace falta saber:

| Pregunta | Nombre técnico | Ejemplo |
|---|---|---|
| ¿Son R,G,B o son Y,U,V? | modelo de color | `yuv420p` vs `rgb24` |
| ¿0–255 o 16–235? | **rango** | full vs limited |
| ¿Qué rojo es "rojo puro"? | **primarios / gamut** | bt709, bt2020, DCI-P3 |
| ¿Cómo se reparte el brillo? | **función de transferencia / gamma** | bt709, sRGB, PQ, log |
| ¿Cómo se convierte YUV↔RGB? | **matriz** | bt709, bt601 |

Si el reproductor asume una regla distinta a la que usaste tú, ves otra cosa. Eso es todo. El 95 %
de los desastres de color de gente que empieza son un desacuerdo de reglas, no un error de gusto.

---

## 2. Y'CbCr: por qué el video no es RGB

Tu cámara captura RGB, pero el video se guarda casi siempre en **Y'CbCr** (que en ffmpeg verás como
YUV):

- **Y (luma)** — el brillo. Es donde vive casi toda la información que el ojo nota.
- **U = Cb** — cuánto se aleja del gris hacia el **azul**. Neutro = 128.
- **V = Cr** — cuánto se aleja del gris hacia el **rojo**. Neutro = 128.

Se hace así por una razón brutal de eficiencia: el ojo humano ve mucho más detalle en brillo que en
color. Entonces el video guarda el color **a menos resolución**. Eso es el `420` de `yuv420p`:

| Formato | Qué guarda | Uso |
|---|---|---|
| `yuv444p` | color a resolución completa | intermedios, trabajo de color, croma |
| `yuv422p` | color a la mitad horizontal | cámaras profesionales, ProRes |
| `yuv420p` | color a la mitad horizontal **y** vertical | **todo lo que se publica** |

Consecuencia práctica número uno: en `yuv420p` tienes **un cuarto** de la información de color. Por
eso los rótulos de color saturado sobre fondo contrastado se ven con bordes sucios, y por eso el
croma (`215`) sufre tanto en material de celular.

Consecuencia práctica número dos: si vas a hacer trabajo pesado de color, trabaja en un intermedio
`yuv444p` y solo baja a `yuv420p` en la exportación final:

```bash
# intermedio de trabajo, sin pérdida perceptible
ffmpeg -i bruto.mp4 -vf "format=yuv444p" -c:v libx264 -crf 12 -preset fast inter.mkv
```

Los valores medidos del caso del bar (`250`) están todos en esta escala: U = 144–165 y V = 143–168
significa "muy por encima de 128 en las dos", o sea magenta cargado.

---

## 3. Rango limitado vs rango completo (el error más caro)

Este solo concepto explica la mitad de los videos "lavados" de internet.

| Rango | Negro | Blanco | Dónde vive |
|---|---|---|---|
| **Limited (tv)** | 16 | 235 | el estándar de video: MP4, H.264, TV, casi todo |
| **Full (pc)** | 0 | 255 | fotos, capturas de pantalla, PNG, algunas cámaras |

Los valores 0–15 y 236–255 existen en limited, pero son "cabeza y pie": espacio para que un filtro
no recorte de una. No son imagen.

Qué pasa cuando se confunden:

- **Marcaste full, se lee como limited** → el negro 0 se muestra más negro que el negro y el blanco
  255 más blanco que el blanco. Imagen **con contraste exagerado**, sombras tapadas, altas quemadas.
- **Marcaste limited, se lee como full** → el negro 16 se muestra gris y el blanco 235 se ve gris
  claro. Imagen **lavada, sin fuerza**. Este es el clásico.

Cómo saber qué tienes:

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=pix_fmt,color_range,color_space,color_primaries,color_transfer \
  -of default=nw=1 clip.mp4
```

Salida real de un archivo típico de celular sin etiquetar:

```
pix_fmt=yuv420p
color_range=unknown
color_space=unknown
color_transfer=unknown
color_primaries=unknown
```

**`unknown` no significa "no importa".** Significa "que cada reproductor adivine". Y adivinan
distinto. Ese archivo se va a ver diferente en Windows, en el navegador y en Instagram.

Convertir de limited a full de forma correcta (no con `eq`, que solo estira a bruto):

```bash
ffmpeg -i clip.mp4 -vf "zscale=rin=limited:min=709:tin=709:pin=709:r=full:m=709:t=709:p=709,format=yuv420p" \
  -c:v libx264 -crf 16 full.mp4
```

**Trampa real y verificada:** si le pides a `zscale` un cambio de rango sin decirle cuál es la
entrada, revienta con:

```
code 3074: no path between colorspaces
```

Eso NO es un bug: es `zscale` diciéndote "el archivo no dice de dónde viene y yo no adivino". La
solución es la de arriba: declarar `rin`, `min`, `tin`, `pin` explícitamente.

Y la regla de oro:

> **Si no vas a convertir, al menos etiqueta.** Un archivo etiquetado se ve igual en todas partes.

```bash
ffmpeg -i clip.mp4 -c:v libx264 -crf 18 -pix_fmt yuv420p \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -movflags +faststart etiquetado.mp4
```

---

## 4. Gamma: por qué el brillo no es lineal

Si duplicas la cantidad de fotones, el ojo no ve "el doble de brillo": ve bastante menos. La
respuesta humana a la luz es aproximadamente una potencia, no una recta.

El video aprovecha eso: **guarda los valores ya "curvados"** para gastar más bits donde el ojo mira
(las sombras y los medios) y menos donde no distingue (las altas luces). Esa curva es la **función
de transferencia**, y en video estándar (Rec.709) equivale más o menos a un gamma de 2,2–2,4.

Lo que tienes que retener, en práctica:

1. **El 50 % del valor no es el 50 % de la luz.** Un píxel en 128 (mitad de la escala) es más o menos
   el 21 % de la luz real. Por eso "subir el brillo un 10 %" no significa nada por sí solo.
2. **`eq=gamma=X` mueve los medios sin mover los extremos.** Es la herramienta correcta para
   exposición. `eq=brightness` **suma** un valor plano, o sea que levanta también los negros y los
   ensucia.
3. **Gamma menor que 1 oscurece. Gamma mayor que 1 aclara.** Esta es exactamente la trampa del caso
   real: se aplicó `gamma=0.95` a planos que estaban en Y = 75 y quedaron en Y = 52. La gente asume
   que "0.95 es casi 1, no pasa nada". Sobre material oscuro sí pasa, porque el material vive
   precisamente en la parte de la curva donde ese gamma muerde más.

```bash
# aclarar medios sin tocar negros ni blancos
ffmpeg -i clip.mp4 -vf "eq=gamma=1.10" -c:v libx264 -crf 16 out.mp4

# esto NO es lo mismo: sube TODO, incluido el negro, y lo vuelve gris
ffmpeg -i clip.mp4 -vf "eq=brightness=0.06" -c:v libx264 -crf 16 malo.mp4
```

4. **Log no es una imagen, es un contenedor.** Si grabas en un perfil log (S-Log, C-Log, LOG de un
   celular), el archivo se ve gris y lavado a propósito: está guardando un rango dinámico grande en
   pocos bits. Eso **no** se corrige con contraste a ojo; se convierte con la LUT del fabricante
   (`65`, `256`) y después se gradúa.

---

## 5. Gamut: qué colores existen

El **gamut** es el conjunto de colores que un espacio puede representar. Los tres que te van a tocar:

| Espacio | Dónde vive | Qué tan amplio |
|---|---|---|
| **Rec.709 / sRGB** | TV HD, web, casi todo lo que publicas | base |
| **DCI-P3** | cine digital, pantallas de iPhone y Mac modernas | ~25 % más |
| **Rec.2020** | HDR / 4K de nueva generación | mucho más |

Rec.709 y sRGB tienen **los mismos primarios** (los mismos rojo, verde y azul de referencia) pero
**distinta curva de gamma**. Por eso una imagen sRGB metida en una línea de tiempo Rec.709 se ve con
el contraste corrido: mismos colores, otra repartición del brillo.

Qué significa esto para ti, que publicas en redes:

> **Trabaja y entrega en Rec.709 salvo que tengas una razón enorme para no hacerlo.**

Instagram, TikTok, YouTube y WhatsApp reprocesan todo. Si les mandas P3 o HDR, la conversión la hace
su servidor, con su criterio, y casi siempre sale peor que si lo hubieras hecho tú. Detalle por
plataforma en `68`.

El daño típico de gamut: un rojo saturadísimo que en tu monitor P3 se ve vibrante, al pasar a
Rec.709 se **aplana** y pierde todo el detalle interno (el pliegue de una camisa roja se vuelve una
mancha). Eso se llama **recorte de gamut**, y no se arregla después: se evita no saturando de más.

---

## 6. Profundidad de bits y el bandeado

8 bits = 256 niveles por canal. Suena a mucho hasta que estiras.

Si tomas una zona que ocupaba del nivel 40 al 60 (21 niveles) y la estiras al rango 20–120, esos 21
niveles no se multiplican: se **separan**. Quedan escalones visibles. Eso es el **bandeado
(banding)**, y donde más se ve es en cielos, paredes lisas y degradados de neón — justo el material
del caso del bar.

Cómo evitarlo:

1. **No estires de más.** Si tienes que estirar mucho, el problema fue de rodaje (`259`).
2. **Trabaja en 10 bits en los intermedios**, aunque entregues en 8:

```bash
ffmpeg -i bruto.mp4 -vf "format=yuv444p10le" -c:v libx264 -crf 12 -preset fast inter10.mkv
```

3. **Si ya apareció, disimúlalo con `deband` y un poco de grano:**

```bash
ffmpeg -i con_bandas.mp4 -vf "deband=1thr=0.02:2thr=0.02:3thr=0.02:range=16:blur=1,noise=alls=4:allf=t+u" \
  -c:v libx264 -crf 16 sin_bandas.mp4
```

El grano funciona porque rompe el borde limpio entre escalones. Es el mismo truco del cine con
película (`257`). Muy poco (`alls=3` a `alls=6`) es suficiente; más se ve sucio.

---

## 7. La cadena completa, sin romper nada

Cómo se ve todo esto junto en un flujo que no destruye la imagen:

```bash
# 1. inspeccionar
ffprobe -v error -select_streams v:0 \
  -show_entries stream=pix_fmt,color_range,color_space,width,height,r_frame_rate \
  -of default=nw=1 bruto.mp4

# 2. intermedio de trabajo (444, 10 bits, poca compresión)
ffmpeg -i bruto.mp4 -vf "format=yuv444p10le" -c:v libx264 -crf 12 -preset fast trabajo.mkv

# 3. todo el color, en UNA pasada sobre el intermedio
ffmpeg -i trabajo.mkv -vf "colorbalance=rm=-0.06:bm=0.04,exposure=exposure=0.20,\
curves=all='0/0 0.25/0.22 0.75/0.79 1/1',eq=saturation=1.05,\
selectivecolor=correction_method=absolute:reds=0 -0.10 0.06 0" \
  -c:v libx264 -crf 12 -preset fast graduado.mkv

# 4. entrega: legalizar, bajar a 420 8 bits, etiquetar
ffmpeg -i graduado.mkv -vf "limiter=min=16:max=235,format=yuv420p" \
  -c:v libx264 -crf 18 -preset slow -profile:v high -level 4.0 \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -c:a aac -b:a 192k -movflags +faststart final.mp4
```

`limiter=min=16:max=235` es el "legalizador": recorta lo que se salió del rango broadcast. Sin él, un
blanco en 255 puede reventar en algunos reproductores y un negro en 0 puede aparecer como mancha.

---

## 8. Cómo se ve un error de espacio de color en la vida real

Síntomas y diagnóstico rápido:

| Lo que ves | Causa más probable | Arreglo |
|---|---|---|
| Video lavado, negros grises | limited leído como full | etiquetar `-color_range tv` o convertir con `zscale` |
| Contraste exagerado, sombras tapadas | full leído como limited | igual, al revés |
| Todo verdoso o magenta al aplicar una LUT | LUT hecha para log, aplicada a Rec.709 | usar la LUT correcta (`256`) |
| Colores bien en el PC, apagados en el celular | trabajaste en P3, entregaste sin convertir | entregar Rec.709 |
| Escalones en el cielo o en la pared | bandeado por estirar 8 bits | `deband` + grano, o no estirar tanto |
| Bordes de color sucios en rótulos | subsampling 4:2:0 | rótulos menos saturados, o `yuv444p` si el destino lo permite |
| Se ve distinto en cada reproductor | archivo sin etiquetas de color | etiquetar siempre |

---

## Errores comunes

- **Creer que `unknown` en `color_range` es inofensivo.** Es el origen del 90 % de los "se ve
  distinto en cada lado".
- **Convertir de rango con `eq` o `curves`** en vez de `zscale`. Estira a bruto y deja bandeado.
- **Usar `zscale` sin declarar la entrada** y luego pensar que ffmpeg está roto cuando dice
  `no path between colorspaces`. Faltan `rin`, `min`, `tin`, `pin`.
- **`eq=brightness` para exponer.** Suma un valor plano; los negros se vuelven grises. Es `gamma` o
  `exposure`.
- **Asumir que gamma 0.95 "casi no hace nada".** Sobre material oscuro (Y = 75) lo mandó a Y = 52.
- **Trabajar todo el color en `yuv420p`.** Cada filtro de croma trabaja con un cuarto de la
  información. Intermedio en 444.
- **Entregar en P3 o HDR a redes sociales.** Su transcodificador decide por ti, y decide mal.
- **Estirar sombras de 8 bits sin `deband`.** Aparecen escalones que ya no se quitan.
- **Aplicar una LUT de log a material que no es log.** Explota. La LUT asume una curva que tu archivo
  no tiene.
- **Poner `format=yuv420p` al principio de la cadena** en vez de al final. Bajas la información de
  color antes de trabajarla.

---

## Checklist

- [ ] Corrí `ffprobe` y sé el `pix_fmt`, el `color_range` y el `color_space` de mi material.
- [ ] Si venía `unknown`, decidí a qué lo iba a etiquetar y lo etiqueté.
- [ ] Trabajo el color sobre un intermedio `yuv444p` (10 bits si voy a estirar mucho), no sobre el MP4 final.
- [ ] Uso `gamma` / `exposure` para brillo, nunca `brightness`.
- [ ] Antes de aplicar un gamma menor que 1, revisé la Y de los planos más oscuros.
- [ ] Si convierto rango, uso `zscale` con la entrada declarada, no `eq`.
- [ ] Reviso el cielo y las paredes lisas buscando bandeado antes de entregar.
- [ ] La exportación final lleva `limiter=min=16:max=235` y `format=yuv420p` **al final** de la cadena.
- [ ] El archivo entregado lleva `-colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv`.
- [ ] Entrego en Rec.709 salvo que el cliente tenga un flujo HDR real y sepa qué hacer con él.
- [ ] Revisé el resultado en al menos dos reproductores distintos (navegador y celular).
