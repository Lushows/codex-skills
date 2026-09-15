# 256 — Crear tu propia LUT

El módulo `65` te enseñó qué es una LUT, cómo aplicarla y cómo hornear una. Este módulo es lo que
viene después: **cómo convertir una corrección que funcionó en un archivo reutilizable, cómo
verificar que la LUT hace lo que promete, y cómo saber si te está ayudando o tapándote un problema**.

Es la diferencia entre "tengo una LUT" y "tengo una LUT que sé qué hace".

---

## 1. Qué cabe en una LUT y qué no (esto decide todo)

Una LUT 3D es una tabla de traducción de color: **este color entra, este color sale**. Nada más. Y de
esa definición salen límites que no se pueden negociar:

| Operación | ¿Cabe en la LUT? | Por qué |
|---|---|---|
| `curves` | ✅ sí | es color → color |
| `eq` (contraste, saturación, gamma) | ✅ sí | color → color |
| `colorbalance`, `colorchannelmixer` | ✅ sí | color → color |
| **`selectivecolor`** | ✅ sí | color → color, aunque parezca magia |
| `colortemperature`, `colorlevels` | ✅ sí | color → color |
| `unsharp`, `gblur`, `nlmeans` | ❌ **no** | miran los píxeles **vecinos** |
| `vignette` | ❌ **no** | depende de la **posición** en el cuadro |
| `noise` (grano) | ❌ **no** | es aleatorio y cambia por cuadro |
| Máscaras, ventanas, `maskedmerge` | ❌ **no** | dependen de la posición |
| `deband`, `chromanr` | ❌ **no** | espaciales |
| Estabilización, recorte, escalado | ❌ **no** | geometría |

> **Regla:** si el filtro necesita saber **dónde** está el píxel o **qué hay alrededor**, no cabe en
> una LUT.

Consecuencia práctica: tu look casi nunca es "una LUT". Es una LUT **más** una viñeta **más** grano.
El archivo `.cube` guarda la parte de color; el resto va en la cadena de ffmpeg o en el editor.

Y consecuencia más importante todavía: **la secundaria de piel del caso del bar** —que era
`selectivecolor`— **sí** cabe en la LUT. Pero si la hubieras hecho con máscara (`253`, sección 4), no
cabría. Eso puede decidir cómo haces la corrección desde el principio.

---

## 2. El generador de `.cube` sin dependencias

El módulo `65` da un script que usa Pillow. Aquí va uno que **solo necesita Python y ffmpeg**, nada
más que instalar. Es el que uso.

```python
# cube.py — genera un .cube a partir de una cadena de filtros de ffmpeg
# Uso: python cube.py "<cadena de filtros>" mi_look.cube [tamaño]
import subprocess, sys

CHAIN = sys.argv[1]
OUT   = sys.argv[2]
N     = int(sys.argv[3]) if len(sys.argv) > 3 else 33

W, H = N * N, N

# 1. rejilla identidad, en el orden del formato .cube: R rápido, luego G, luego B
buf = bytearray()
for b in range(N):
    for g in range(N):
        for r in range(N):
            buf += bytes((round(r * 255 / (N - 1)),
                          round(g * 255 / (N - 1)),
                          round(b * 255 / (N - 1))))
open("identidad.raw", "wb").write(buf)

# 2. pasar la rejilla por la cadena de filtros
subprocess.run([
    "ffmpeg", "-y", "-v", "error",
    "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-i", "identidad.raw",
    "-vf", f"format=rgb24,{CHAIN},format=rgb24",
    "-f", "rawvideo", "-pix_fmt", "rgb24", "graduada.raw"
], check=True)

d = open("graduada.raw", "rb").read()
assert len(d) == N ** 3 * 3, "la cadena cambió el tamaño de la imagen: quita filtros de geometría"

# 3. escribir el .cube
with open(OUT, "w") as f:
    f.write(f'TITLE "{OUT}"\nLUT_3D_SIZE {N}\nDOMAIN_MIN 0 0 0\nDOMAIN_MAX 1 1 1\n')
    for i in range(N ** 3):
        f.write(f"{d[i*3]/255:.6f} {d[i*3+1]/255:.6f} {d[i*3+2]/255:.6f}\n")
print("listo:", OUT)
```

Uso real:

```bash
python cube.py "eq=contrast=1.10:saturation=1.06,curves=all='0/0 0.25/0.22 0.75/0.79 1/1'" mi_look.cube
```

Ese `.cube` lo lee ffmpeg, DaVinci Resolve, Premiere, Final Cut y CapCut. Es el formato universal.

**Detalle de por qué funciona:** la rejilla se manda como `rawvideo` en `rgb24` puro, sin pasar por
ningún códec ni por `yuv420p`. Si la mandaras como MP4 o dejaras que ffmpeg convierta a 4:2:0, el
submuestreo de croma te destruiría la mitad de los puntos de la tabla y la LUT saldría con errores
que después no sabrías de dónde vienen (`251`, sección 2).

---

## 3. Verificar que la LUT hace lo que la cadena hacía

Este paso no lo hace casi nadie y es lo que separa una LUT confiable de un archivo con nombre bonito.

```bash
# A) el video con la cadena original
ffmpeg -y -i clip.mp4 -vf "eq=contrast=1.10:saturation=1.06,curves=all='0/0 0.25/0.22 0.75/0.79 1/1'" \
  -c:v libx264 -crf 12 con_cadena.mp4

# B) el video con la LUT
ffmpeg -y -i clip.mp4 -vf "lut3d=mi_look.cube" -c:v libx264 -crf 12 con_lut.mp4

# C) medir la diferencia
ffmpeg -hide_banner -i con_cadena.mp4 -i con_lut.mp4 -lavfi psnr -f null - 2>&1 | grep -o "average:[0-9.]*"
```

Resultados reales medidos, con la misma cadena y distintos tamaños de rejilla:

| Tamaño (`LUT_3D_SIZE`) | Puntos en la tabla | PSNR contra la cadena original |
|---|---|---|
| 17 | 4.913 | **48,0 dB** |
| **33** | **35.937** | **49,1 dB** |
| 64 | 262.144 | **50,4 dB** |

Cómo se lee esto, honestamente:

- Por encima de **40 dB** la diferencia es invisible para el ojo. Los tres tamaños pasan.
- Pasar de 17 a 33 gana 1,1 dB. Pasar de 33 a 64 gana otros 1,2 dB, con **7 veces más archivo** y
  peor compatibilidad (algunos programas se atragantan con LUT de 64).
- **33 es el estándar por una razón: es el punto donde deja de valer la pena crecer.**

Y la conclusión que importa: **una LUT nunca es idéntica a la cadena**. Es una aproximación por
interpolación. Si tu look depende de una transición de color extremadamente delicada, la LUT la va a
suavizar. Para el 99 % del trabajo, da igual.

---

## 4. La prueba de la tira de piel (la verificación que sí importa)

Un PSNR alto te dice que la LUT copió bien la cadena. **No te dice que la cadena estuviera bien.**
Para eso está esta prueba, que es la mejor forma de auditar cualquier look antes de aplicarlo a un
proyecto entero.

**Paso 1 — Fabrica una tira de parches de piel:**

```bash
ffmpeg -y -v error \
  -f lavfi -i "color=c=0xF0D0BC:s=100x100:d=0.1" \
  -f lavfi -i "color=c=0xC08A63:s=100x100:d=0.1" \
  -f lavfi -i "color=c=0x8D5524:s=100x100:d=0.1" \
  -f lavfi -i "color=c=0x3B2412:s=100x100:d=0.1" \
  -filter_complex "[0:v][1:v][2:v][3:v]hstack=inputs=4" -frames:v 1 tira_piel.png
```

Cuatro tonos: muy claro, medio, moreno, muy oscuro.

**Paso 2 — Mide la tira original:**

```bash
for x in 0 100 200 300; do
  ffmpeg -y -v error -i tira_piel.png -vf "crop=100:100:$x:0,format=yuv444p,signalstats,metadata=print:file=p.txt" -frames:v 1 -f null -
  echo -n "parche $x: "; grep -E "HUEAVG|SATAVG" p.txt | head -2 | tr '\n' ' '
  echo
done
```

**Paso 3 — Aplica la LUT y vuelve a medir:**

```bash
ffmpeg -y -v error -i tira_piel.png -vf "lut3d=mi_look.cube" tira_lut.png
# ...y el mismo bucle sobre tira_lut.png
```

Resultado real de una LUT de prueba (contraste 1.10 + saturación 1.06 + curva en S suave):

| Parche | HUE antes | HUE después | SAT antes | SAT después |
|---|---|---|---|---|
| Muy clara | 136 | **132** | 20 | 19 |
| Media | 137 | **135** | 36 | **43** |
| Morena | 133 | **135** | 41 | **47** |
| Muy oscura | 135 | **132** | 15 | 14 |

Cómo se interpreta:

- **HUE se movió entre 2 y 4 grados.** Aceptable: el rango sano es 130–145 (`254`) y ninguna se salió.
  Si una LUT te mueve el HUE 15 grados, va a dejar caras verdes o moradas y hay que arreglarla.
- **La saturación de las pieles medias subió un 18 %** (36 → 43, 41 → 47). Ese es el efecto real de un
  contraste "suave": en la piel media se nota mucho más que en los extremos.
- **Las pieles muy claras y muy oscuras casi no se movieron en saturación** pero sí bajaron el HUE.
  Consecuencia práctica: esta LUT trata distinto a distintas personas, y hay que saberlo antes de
  aplicarla a un video con varios protagonistas.

Esa tabla, para tu LUT, en cinco minutos, vale más que cualquier opinión sobre si "se ve cinematográfico".

---

## 5. Cuándo una LUT ayuda de verdad

| Situación | ¿LUT? |
|---|---|
| Mismo material, misma cámara, mismo tipo de escena, muchas piezas | ✅ **sí**, es su mejor uso |
| Convertir material log al espacio de trabajo | ✅ sí, y usa la del fabricante (`65`) |
| Entregarle tu look a un editor que no sabe ffmpeg | ✅ sí, es la razón de que exista el formato |
| Consistencia de marca entre 20 reels al mes | ✅ sí, con la LUT versionada (`88`) |
| Un solo video, una sola vez | ❌ no, es más trabajo que hacer la cadena |
| Material de fuentes distintas sin corregir | ❌ **no, y este es el error grave** |

---

## 6. Cuándo una LUT esconde el problema

La trampa central, y viene directo del caso del bar:

El material tenía **dispersión de luminancia de 34 puntos** (Y de 70 a 104) y **dispersión de
saturación de 43** (SAT de 13 a 57). Si le aplicas la misma LUT a todos los planos:

- el plano oscuro (Y = 70) se vuelve más oscuro y pierde detalle,
- el plano claro (Y = 104) se vuelve más claro,
- **la dispersión no baja: se mantiene o crece.**

Una LUT es una función. La misma función aplicada a entradas distintas da salidas distintas. **La LUT
no empareja: la LUT estiliza.**

> **El orden es: corregir → emparejar → LUT.**
> Nunca: LUT → intentar arreglar lo que la LUT dejó raro.

Las tres señales de que estás usando una LUT para tapar:

1. Tienes que aplicarla **a distinta intensidad en cada plano** para que se vean parecidos. Eso
   significa que la corrección no está hecha.
2. En unos planos la piel queda bien y en otros verde. Los planos no estaban emparejados.
3. Le bajas la intensidad al 40 % "para que no se pase". Si la LUT solo sirve al 40 %, la LUT está
   mal hecha; hazla más suave y aplícala al 100 %.

Dosificar una LUT sí es legítimo como recurso creativo (`65` explica el `blend` con `haldclut` y el
truco de mezclar con el original), pero no como parche.

---

## 7. Higiene de LUTs: nombrarlas, versionarlas, documentarlas

Una LUT sin documentación es un archivo misterioso que dentro de tres meses nadie sabe usar.

```
luts/
  gastrolatam_v3_rec709.cube        ← para material ya corregido, Rec.709
  gastrolatam_v3_rec709.md          ← qué hace, cadena original, cuándo usarla
  gastrolatam_v3_tira_piel.png      ← la prueba de piel, guardada
  bar_neon_v1_rec709.cube
```

El `.md` de al lado, con cuatro líneas basta:

```markdown
# gastrolatam_v3_rec709
Cadena original:
  eq=contrast=1.10:saturation=1.06,curves=all='0/0 0.25/0.22 0.75/0.79 1/1',
  selectivecolor=correction_method=absolute:reds=0 -0.10 0.06 0
Se aplica: DESPUÉS de corregir y emparejar. Nunca sobre bruto.
Verificado: PSNR 49,1 dB contra la cadena · HUE de piel se mueve máximo 4 grados.
No incluye: viñeta ni grano (van aparte en la cadena de ffmpeg).
```

Ese último renglón —"no incluye"— es el que más agradece tu yo del futuro.

Y el número de versión en el nombre no es burocracia: cuando cambies el look, los videos viejos
siguen amarrados a su versión y puedes reproducirlos exactamente (`132`, `96`).

---

## 8. Aplicar la LUT en producción

```bash
# La LUT sola
ffmpeg -i corregido.mp4 -vf "lut3d=luts/gastrolatam_v3_rec709.cube,format=yuv420p" \
  -c:v libx264 -crf 18 -preset slow -c:a copy final.mp4

# La LUT + lo que NO cabe en ella (viñeta y grano), en el orden correcto
ffmpeg -i corregido.mp4 -vf \
  "lut3d=luts/gastrolatam_v3_rec709.cube,vignette=PI/5,noise=alls=4:allf=t+u,\
limiter=min=16:max=235,format=yuv420p" \
  -c:v libx264 -crf 18 -preset slow -c:a copy final.mp4
```

**Trampa de Windows con las rutas** (ya está en `65`, pero cuesta tan caro que se repite): en una
cadena de filtros, los dos puntos de `C:\` y las barras invertidas hay que escaparlos. Lo más fácil es
correr ffmpeg desde la carpeta del proyecto y usar rutas relativas, como arriba.

**Interpolación:** `lut3d=...:interp=tetrahedral` es más preciso que el `trilinear` por defecto para
LUTs pequeñas. Con N=33 la diferencia es marginal; con N=17 sí se nota.

---

## Errores comunes

- **Meter `unsharp`, `vignette` o `noise` en la cadena que genera la LUT.** No caben; la rejilla no
  tiene vecinos ni posición. El resultado será una LUT con valores extraños y nunca sabrás por qué.
- **Generar la rejilla pasando por MP4 o por `yuv420p`.** El submuestreo de croma corrompe la tabla.
  Siempre `rawvideo` en `rgb24`.
- **Aplicar la misma LUT a planos con 34 puntos de dispersión de luma.** La LUT estiliza, no empareja.
- **Bajar la LUT al 40 % para que "no se pase".** Rehaz la LUT más suave.
- **No verificar la LUT contra la cadena.** Un `psnr` de dos minutos te dice si la horneaste bien.
- **No probar la LUT contra tonos de piel.** Es donde una LUT bonita se vuelve un problema.
- **Usar `LUT_3D_SIZE 64` porque "más es mejor".** Gana 1,2 dB, pesa 7 veces más y algunos programas
  no la abren.
- **Aplicar una LUT hecha para material log sobre material Rec.709.** Explota el contraste. Y al
  revés: aplicar una LUT de Rec.709 a log deja todo lavado (`65`).
- **LUT sin documentación al lado.** En tres meses nadie sabe si va antes o después de corregir.
- **Cambiar la LUT y no versionarla.** Los videos viejos ya no se pueden reproducir igual.

---

## Checklist

- [ ] Mi cadena de color **no** tiene filtros espaciales, temporales ni de máscara antes de hornear.
- [ ] Generé la rejilla en `rawvideo`/`rgb24`, sin pasar por códec ni por 4:2:0.
- [ ] Usé `LUT_3D_SIZE 33` salvo que tenga una razón concreta para otra cosa.
- [ ] Verifiqué la LUT contra la cadena original con `psnr` (por encima de 40 dB está bien).
- [ ] Pasé la tira de cuatro tonos de piel por la LUT y medí HUE y SAT antes y después.
- [ ] El HUE de la piel se mueve menos de 5 grados y sigue dentro de 130–145.
- [ ] La LUT se aplica **después** de corregir y emparejar, nunca sobre bruto disparejo.
- [ ] La aplico al 100 %; si tenía que bajarla, rehíce la LUT más suave.
- [ ] La viñeta y el grano van en la cadena, no en la LUT, y están documentados como aparte.
- [ ] El archivo tiene versión en el nombre y un `.md` al lado que dice qué hace y cuándo se usa.
- [ ] Guardé la prueba de piel junto a la LUT como evidencia.
