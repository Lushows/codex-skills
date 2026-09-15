# 421 — Medir lo que un efecto cambia

`420` dio el arnés genérico: `utime`, PSNR, SSIM y megabytes. Sirve para saber **si** un efecto hace
algo. No sirve para saber **si hace lo que dijiste**.

Un ejemplo de la tabla medida en `420`: `vignette=PI/5.6` da PSNR 23,71 dB. Cambio enorme. Pero
`gblur=sigma=20` da PSNR 23,27 dB —prácticamente el mismo número— y son dos efectos que no tienen
nada que ver. PSNR dice «cambió mucho»; no dice «oscureció las esquinas» ni «borró el detalle».

Este módulo es el segundo piso del arnés: **la magnitud específica de cada familia**.

---

## 1. El instrumento de fondo: `signalstats`

```bash
ffmpeg -hide_banner -i entrada.mp4 -vf "signalstats,metadata=print" -f null - 2>&1 | head -20
```

Escupe una línea por fotograma con dos docenas de claves. Las que se usan aquí:

| Clave | Qué es | Escala |
|---|---|---|
| `YAVG` | luminancia media | 16 (negro) – 235 (blanco) |
| `YMIN` / `YMAX` | extremos de luminancia | los negros lavados y las altas quemadas |
| `YLOW` / `YHIGH` | percentiles 10 y 90 | el **contraste real**, sin que un píxel suelto mande |
| `SATAVG` / `SATMAX` | saturación | 0 – 180 aprox |
| `HUEAVG` | tono dominante | 0 – 360 |
| `UAVG` / `VAVG` | dominante de color | 128 = neutro |
| `YDIF` | diferencia media con el fotograma anterior | 0 = congelado |

Para una sola cifra por clip, se promedia la columna:

```bash
mide () {   # mide <archivo> <clave>
  ffmpeg -hide_banner -i "$1" -vf "signalstats,metadata=print:key=lavfi.signalstats.$2" \
    -f null - 2>&1 | grep -o "$2=[0-9.]*" | cut -d= -f2 \
    | awk '{s+=$1; n++} END {printf "%.2f\n", s/n}'
}
mide base.mp4 YAVG
mide o_vign_5_6.mp4 YAVG
```

> Recordatorio de `420`: **sin `-loglevel error` y con `2>&1`**. `metadata=print` escribe en nivel
> `info` y por stderr. Con el nivel bajado no sale una sola línea y parece que el filtro no midió.

---

## 2. El arnés por familias

Cada familia de efecto tiene su magnitud. Ésta es la tabla de correspondencias, y con ella el arnés
deja de ser genérico.

| Familia | Filtro típico | Magnitud que lo delata | Cómo se mide |
|---|---|---|---|
| **Exposición** | `eq=brightness/gamma` | `YAVG`, `YLOW`, `YHIGH` | `signalstats` |
| **Color** | `eq=saturation`, `hue`, `colorbalance` | `SATAVG`, `UAVG`, `VAVG`, `HUEAVG` | `signalstats` |
| **Contraste** | `eq=contrast`, `curves` | `YHIGH − YLOW` | `signalstats` |
| **Textura** | `noise` | `YDIF` y **peso codificado** | `signalstats` + `stat` |
| **Nitidez** | `unsharp` | energía de alta frecuencia | peso codificado + `edgedetect` |
| **Desenfoque** | `gblur`, `boxblur` | peso codificado (cae en picado) | `stat` |
| **Espacial** | `vignette` | **caída borde→centro**, no `YAVG` | `crop` + `signalstats` |
| **Temporal** | destello, `eval=frame` | perfil de `YAVG` **por fotograma** | `metadata=print` + gráfica |
| **Geométrico** | `crop`, `scale`, `rotate` | dimensiones y SAR | `ffprobe` |

Las dos filas que la gente mide mal son las dos últimas de la mitad: la viñeta y el destello.

---

## 3. La viñeta no se mide con YAVG

Una viñeta baja la luminancia media. Es cierto pero es inútil: también la baja un `eq=brightness=-0.05`
y no tienen nada que ver. **Lo que define una viñeta es el gradiente del borde al centro.** Se mide
recortando dos regiones y comparándolas:

```bash
#!/usr/bin/env bash
# caida.sh <archivo>  -> luminancia del centro, de la esquina, y el escalon
centro () { ffmpeg -hide_banner -i "$1" -vf "crop=iw/3:ih/3:iw/3:ih/3,signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -f null - 2>&1 | grep -o 'YAVG=[0-9.]*' | cut -d= -f2 | awk '{s+=$1;n++}END{printf "%.1f",s/n}'; }
esquina () { ffmpeg -hide_banner -i "$1" -vf "crop=iw/6:ih/6:0:0,signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -f null - 2>&1 | grep -o 'YAVG=[0-9.]*' | cut -d= -f2 | awk '{s+=$1;n++}END{printf "%.1f",s/n}'; }
C=$(centro "$1"); E=$(esquina "$1")
awk -v c="$C" -v e="$E" 'BEGIN{printf "centro %.1f  esquina %.1f  caida %.1f  (%.0f%%)\n", c, e, c-e, 100*(c-e)/c}'
```

Así la hipótesis «esta viñeta dirige la mirada» se convierte en un número comparable entre versiones,
y se puede poner un umbral de casa: **una caída por debajo del 8% no la ve nadie; por encima del 30%
se ve el círculo** (`444` desarrolla la escala y sus excepciones).

Nota práctica medida en `420`: `vignette=PI/5.6` baja el peso del archivo de 1,17 a **1,06 MB**, y
`vignette=PI/12` a 1,13 MB. Oscurecer esquinas le quita trabajo al codificador. Es de los pocos
efectos que se pagan solos en bitrate.

---

## 4. El efecto temporal se mide por fotograma, no de media

El canal documental usa destellos: una campana de Gauss sobre `t` que sube brillo y contraste durante
~0,12 s y vuelve. En `motor.py`:

```python
bri = "+".join(f"{f:.3f}*exp(-pow((t-{td:.2f})/{s:.3f}\\,2))" for td, f, s in picos)
filtros.append(f"[{ultimo}]eq=brightness='{bri}':contrast='1+{con}':eval=frame[fx]")
```

Un destello de 3 fotogramas sobre 168 mueve el `YAVG` **medio** del clip en menos de un punto. Si lo
mides de media, tu conclusión será «el destello no hace nada» y estarás midiendo mal. Se mide la
**serie**:

```bash
ffmpeg -hide_banner -i escena.mp4 \
  -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null - 2>&1 \
  | grep -o 'YAVG=[0-9.]*' | cut -d= -f2 | nl \
  | awk '{printf "%4d %6.1f %s\n", $1, $2, substr("########################################",1,int(($2-90)/1.5))}'
```

Sale una gráfica ASCII. El destello es el pico, y se leen tres cosas de un vistazo: **si existe**,
**cuánto dura** y **si es una campana o un escalón**. Un escalón —subida y bajada instantáneas— es la
firma del destello que se ve barato (`431`, `433`).

> 🔴 **La trampa de `eval=frame`.** `eq` solo evalúa expresiones por fotograma si se le pide
> `eval=frame`. Sin eso lee el valor **una vez al iniciar** y el destello no ocurre: la expresión está
> ahí, el comando no falla, y la serie de `YAVG` sale plana. Está documentado en el propio `motor.py`
> porque costó encontrarlo. Lo mismo aplica a `volume` en audio.

---

## 5. Medir sobre una región, no sobre el cuadro

La mayoría de las hipótesis de efecto son **locales**: «se le ve mejor la cara», «el texto resalta
más», «el fondo deja de competir». El promedio del cuadro entero las diluye hasta hacerlas
invisibles. La herramienta es `crop` antes de `signalstats`:

```bash
# Solo la caja donde vive el rotulo (x=120 y=880, 700x160)
ffmpeg -hide_banner -i escena.mp4 \
  -vf "crop=700:160:120:880,signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null - 2>&1 \
  | grep -o 'YAVG=[0-9.]*' | cut -d= -f2 | awk '{s+=$1;n++}END{printf "%.1f\n",s/n}'
```

Y para «separa del fondo», la magnitud es el **escalón** entre dos regiones, medido antes y después:

| | Sin efecto | Con `vignette=PI/5.6` |
|---|---|---|
| centro (YAVG) | tu número | tu número |
| esquina (YAVG) | tu número | tu número |
| **escalón** | **el que importa** | **el que importa** |

Si el escalón no se movió, el efecto no separó nada, por muy bajo que salga el PSNR global.

---

## 6. El coste en bitrate como medida de textura

El peso del archivo codificado es una medida directa de cuánta **información nueva** metió el efecto.
Es lo que hace de `stat -c%s` un instrumento, no una curiosidad. De la tabla medida en `420`, clip de
4 s a 1080p, CRF 20, `preset veryfast`:

| Efecto | MB | vs. nada |
|---|---|---|
| nada | 1,17 | — |
| `eq=saturation=1.02` | 1,17 | **0%** |
| `eq` completo del motor | 1,22 | +4% |
| `noise=alls=2:allf=t+u` | 1,18 | +1% |
| `noise=alls=6:allf=t+u` | **2,02** | **+73%** |
| `unsharp=5:5:0.2` | 1,34 | +15% |
| `unsharp=5:5:0.8` | **2,06** | **+76%** |
| `vignette=PI/5.6` | 1,06 | **−9%** |
| `hqdn3d=4:3:6:4` | 1,00 | −15% |
| `gblur=sigma=20` | 0,32 | **−73%** |

Se lee como un eje: **los efectos que añaden detalle cuestan bitrate; los que lo quitan lo ahorran.**
Y el porcentaje es la magnitud objetiva de «cuánta textura metí». Si tu grano subió el archivo un 1%,
tu grano no existe para el codificador —y por tanto tampoco para el espectador después de que la red
lo recomprima (`428`).

---

## 7. Antes y después, mirando

Las métricas dicen cuánto; el ojo dice si vale la pena. La forma barata de mirar:

```bash
# Diferencia amplificada: lo que el efecto toco, en blanco
ffmpeg -hide_banner -y -i base.mp4 -filter_complex \
"[0:v]split=2[a][b];[a]vignette=PI/5.6[a2];[a2][b]blend=all_mode=difference,eq=contrast=8" \
-frames:v 1 diferencia.png

# Lado a lado, misma escala
ffmpeg -hide_banner -y -i base.mp4 -filter_complex \
"[0:v]split=2[a][b];[a]vignette=PI/5.6,drawtext=text='CON':x=40:y=40:fontsize=48:fontcolor=white[a2]; \
 [b]drawtext=text='SIN':x=40:y=40:fontsize=48:fontcolor=white[b2];[b2][a2]hstack" \
-frames:v 1 comparativa.png
```

La imagen de diferencia es la que más enseña: si sale casi negra, el efecto no está tocando nada
(`423`); si sale uniformemente gris, el efecto es un cambio global que no discrimina; si sale con
estructura —bordes, esquinas, la cara— está haciendo algo local y puedes decir exactamente qué.

---

## 8. La plantilla de informe de un efecto

Cuando un efecto entra en la plantilla del canal, entra con esta ficha. Es lo que hace que dentro de
seis meses nadie tenga que volver a discutirlo:

```
EFECTO      vignette=PI/5.6
HIPOTESIS   dirige la mirada al centro en los fondos de archivo
MAGNITUD    caida borde->centro
MEDIDO      sin: centro 118.4 esquina 116.9 (1.3%)  ->  con: centro 117.1 esquina 74.2 (36.6%)
COSTE       +1.72 s CPU por cada 100 fotogramas 1080p;  peso -9%
ENTREGA     sobrevive a CRF 24 y al reencode de red (comprobado, ver 428)
DECISION    queda. PI/4.6 se descarto: cerraba demasiado
FECHA       2026-09-11
```

---

## Errores frecuentes

- **Medir la magnitud equivocada.** La viñeta no se mide con `YAVG` del cuadro, sino con la caída
  borde→centro. El destello no se mide de media, sino por fotograma.
- **Promediar un efecto temporal.** Tres fotogramas sobre 168 desaparecen en la media.
- **`eq` con expresiones y sin `eval=frame`.** La expresión se evalúa una vez y el efecto no ocurre.
  El comando no falla: la serie sale plana.
- **Medir el cuadro entero cuando la hipótesis es local.** El promedio diluye el efecto hasta cero.
- **Confundir `YMIN`/`YMAX` con contraste.** Un píxel suelto los mueve. El contraste real es
  `YHIGH − YLOW`.
- **Olvidar que `SATAVG` sube sola al subir contraste.** Si mides saturación después de tocar
  contraste, no sabes cuál de los dos la movió. Mide uno cada vez (`425`).
- **Comparar YAVG entre clips de escenas distintas.** Solo tiene sentido antes/después del **mismo**
  material.
- **Usar el peso del archivo sin fijar CRF y preset.** Cambiar el preset mueve el peso más que el
  efecto.
- **No guardar la ficha.** Un efecto sin ficha se vuelve a discutir cada trimestre.

---

## Checklist

- [ ] Identifiqué la familia del efecto y, con ella, la magnitud que lo delata.
- [ ] La medición usa `signalstats` con `metadata=print`, sin `-loglevel error` y con `2>&1`.
- [ ] Si el efecto es espacial, medí regiones (`crop`) y no el cuadro entero.
- [ ] Si el efecto es temporal, miré la serie por fotograma, no la media.
- [ ] Si el efecto usa expresiones en `eq`, comprobé que lleva `eval=frame`.
- [ ] Medí el peso codificado a CRF y preset fijos, con y sin efecto.
- [ ] Saqué la imagen de diferencia amplificada y la miré.
- [ ] Solo cambié una cosa entre las dos versiones comparadas.
- [ ] Escribí la ficha del efecto: hipótesis, magnitud, medida, coste, decisión y fecha.

---

## Relacionado

- `420` — el arnés base y las dos trampas de medición
- `422` — cuánto cuesta en render y en atención
- `423` — el efecto que no se ve
- `425` — efectos que compiten: por qué se mide uno cada vez
- `444` — viñeta medida, con la escala completa de la caída
- `431`, `433` — la campana del destello y el destello mudo
- `108` — `signalstats`, `ebur128` y el resto del instrumental
- `69` — scopes y monitoreo: la versión visual de estas mismas magnitudes
