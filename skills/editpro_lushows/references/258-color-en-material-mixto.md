# 258 — Color en material mixto

El video real casi nunca sale de una sola cámara. Un reel de un negocio típico tiene: dos clips
grabados con el celular del dueño, uno con una cámara prestada, un plano de stock, una imagen
generada con IA animada, una captura de pantalla y un logo en PNG.

Seis fuentes, seis mundos de color distintos. Este módulo es cómo se hace para que convivan.

La idea que ordena todo:

> **No emparejes las fuentes entre sí. Lleva cada una a un mismo punto neutro y empareja desde ahí.**

Emparejar directamente A con B con C con D es un problema de todos contra todos. Normalizar cada una
contra un estándar es un problema lineal. Es la misma lógica que el plano de referencia de `62`, pero
llevada al nivel de **fuente**, no de plano.

---

## 1. Las firmas de cada fuente (qué esperar antes de medir)

| Fuente | Firma típica | Problema principal |
|---|---|---|
| **Celular moderno** | contraste alto, nitidez agresiva, saturación alta, a veces HDR/HLG | balance de blancos que **cambia solo** dentro del clip |
| **Cámara (sin log)** | contraste medio, colores más suaves, menos nitidez | se ve "apagado" al lado del celular |
| **Cámara en log** | gris, lavado, saturación baja | necesita su LUT técnica antes de nada (`65`) |
| **Stock (Pexels, Storyblocks)** | ya viene graduado, a veces muy | trae el look de otro; suele estar sobresaturado |
| **IA generativa** | limpísimo, sin grano, contraste plano o exagerado | **demasiado perfecto**: se ve pegado encima |
| **Captura de pantalla** | rango completo (0–255), colores puros | contraste que explota al mezclarse (`251`) |
| **Archivo / viejo** | ruido, dominante de color, otra relación de aspecto | dominante fuerte, poco rango |

Ninguna de esas firmas es una opinión: todas se miden.

---

## 2. Paso 1 — La auditoría de fuentes

Antes de tocar nada, mide **todo** en una sola tabla. Este bucle saca la ficha técnica y la medición
de cada archivo de la carpeta:

```bash
for f in bruto/*.mp4; do
  echo "=== $f"
  ffprobe -v error -select_streams v:0 \
    -show_entries stream=width,height,r_frame_rate,pix_fmt,color_range,color_space,color_transfer \
    -of default=nw=1 "$f"
  ffmpeg -y -v error -i "$f" -vf "signalstats,metadata=print:file=tmp.txt" -frames:v 1 -f null -
  grep -E "YAVG|UAVG|VAVG|SATAVG" tmp.txt | head -4 | tr '\n' ' ' | sed 's/lavfi.signalstats.//g'
  echo
done
```

Lo que buscas en esa salida, en orden de gravedad:

1. **`color_transfer=arib-std-b67` o `smpte2084`** → material HDR. Hay que convertirlo (sección 3) o
   se va a ver lavado o quemado en todas partes.
2. **`color_range=pc`** → rango completo. Si el resto es `tv`, esa fuente va a explotar al mezclarse.
3. **`pix_fmt` distinto** (`yuv420p10le` vs `yuv420p`) → hay que unificar al final.
4. **Diferencias grandes de Y y SAT** entre fuentes → tu trabajo de emparejamiento, medido.

La tabla del caso del bar, con esta misma auditoría, daba una dispersión de saturación de **43,7**
(SAT de 13 a 57) y de luminancia de **34,4** (Y de 70 a 104). Ese número es el tamaño real del
problema, antes de tener una opinión sobre él.

---

## 3. Paso 2 — HDR del celular: el problema silencioso

Los celulares de gama alta graban en HDR (HLG o Dolby Vision) **por defecto**, sin avisar. Ese
material, metido en una línea SDR, se ve gris y lavado, o con las caras oscurísimas.

Conversión correcta, verificada:

```bash
ffmpeg -y -i celular_hdr.mp4 -vf \
  "zscale=t=linear:npl=100,tonemap=tonemap=hable:desat=0,\
zscale=t=bt709:m=bt709:p=bt709:r=limited,format=yuv420p" \
  -c:v libx264 -crf 16 -preset slow -c:a copy celular_sdr.mp4
```

Los tres pasos: llevar a luz lineal, comprimir el rango con un operador de tono, y volver a Rec.709.

| Operador | Carácter |
|---|---|
| `hable` | equilibrado, el que uso por defecto |
| `mobius` | protege más los colores, altas más suaves |
| `reinhard` | más plano, sirve cuando `hable` deja las altas duras |
| `clip` | recorta y ya. Solo si el material casi no tiene altas |

`desat=0` evita que el filtro le baje saturación a las altas luces por su cuenta; prefiero controlar
eso yo después.

**Trampa verificada:** si le pones a `zscale` etiquetas de entrada que el archivo no tiene (por
ejemplo `tin=smpte2084` a un archivo SDR), falla con:

```
code 3074: no path between colorspaces
```

O sea: **no fuerces las etiquetas, léelas primero con `ffprobe`.** Si el archivo ya viene bien
etiquetado como HDR, la cadena de arriba funciona sin declarar nada de entrada.

---

## 4. Paso 3 — Normalizar cada fuente a neutro

Aquí cada fuente recibe **su propio tratamiento**, con un solo objetivo: quedar neutra, plana y
comparable. Nada de looks todavía.

### Celular

```bash
# Bajar el exceso de fábrica: contraste, saturación y nitidez sobrecocidos
ffmpeg -i celular.mp4 -vf "eq=contrast=0.94:saturation=0.90,colorcorrect=analyze=average" \
  -c:v libx264 -crf 14 -preset fast norm/celular.mp4
```

El celular ya te "graduó" el clip en la cámara. Tu primer trabajo es **deshacerlo**, no sumarle. Y la
nitidez de fábrica no se puede quitar (no existe el "des-sharpen"): lo que sí puedes es **no subirla
más** y, si está muy dura, suavizar apenas con `gblur=sigma=0.4`.

### Cámara sin log

```bash
ffmpeg -i camara.mp4 -vf "colorcorrect=analyze=average,eq=contrast=1.04" \
  -c:v libx264 -crf 14 -preset fast norm/camara.mp4
```

### Cámara en log

```bash
# Primero la LUT técnica del fabricante. SIEMPRE primero.
ffmpeg -i camara_log.mp4 -vf "lut3d=luts/slog3_to_rec709.cube" \
  -c:v libx264 -crf 14 -preset fast norm/camara_log.mp4
```

### Stock

```bash
# El stock viene graduado: hay que APLANARLO para poder emparejarlo
ffmpeg -i stock.mp4 -vf "eq=contrast=0.92:saturation=0.85" \
  -c:v libx264 -crf 14 -preset fast norm/stock.mp4
```

### Captura de pantalla (rango completo)

```bash
ffmpeg -i captura.mp4 -vf \
  "zscale=rin=full:min=709:tin=709:pin=709:r=limited:m=709:t=709:p=709,format=yuv420p" \
  -c:v libx264 -crf 14 -preset fast norm/captura.mp4
```

Después de esta pasada, **vuelve a medir todo**. Las cifras deben estar mucho más juntas. Si una
fuente sigue lejísimos, es la que va a dar problemas y hay que decidir si vale la pena usarla.

---

## 5. Paso 4 — El material de IA: el que más se nota

Un plano generado con IA metido entre material real se delata por cuatro cosas, y **ninguna es el
color**:

| Delator | Por qué | Solución |
|---|---|---|
| **No tiene grano** | el material real siempre tiene algo de ruido | `noise=c0s=5:c1s=2:c2s=2:allf=t+u` |
| **Es demasiado nítido en todo el cuadro** | no hay profundidad de campo real | `gblur=sigma=0.6` general, o desenfocar el fondo |
| **No tiene halación ni aberración** | ningún lente es perfecto | halación suave (`257`) |
| **El contraste es "perfecto"** | no tiene la caída de un sensor real | curva con hombro y pie (`257`) |

Receta de "ensuciado" de material de IA, para que se integre:

```bash
ffmpeg -y -i plano_ia.mp4 -filter_complex "\
[0:v]gblur=sigma=0.6,curves=all='0/0.03 0.5/0.5 1/0.97',split=2[base][hi];\
[hi]format=gbrp,curves=all='0/0 0.78/0 0.95/1 1/1',gblur=sigma=16,\
colorchannelmixer=rr=1:gg=0.35:bb=0.20,format=gbrp[glow];\
[base]format=gbrp[b];\
[b][glow]blend=all_mode=screen:all_opacity=0.22,format=yuv420p,\
noise=c0s=6:c1s=3:c2s=3:allf=t+u" \
  -c:v libx264 -crf 16 -c:a copy norm/ia.mp4
```

Y hay un problema de la IA que **el color no arregla**: la **inconsistencia temporal**. Si la textura
de la pared cambia entre cuadros o el logo de la camiseta muta, eso no es un problema de grado. Es un
plano que hay que volver a generar o descartar (`129`, `259`).

Cómo detectarlo antes de perder tiempo graduándolo:

```bash
# ¿cuánto salta el color entre segundos dentro del mismo plano?
ffprobe -v error -f lavfi -i "movie=plano_ia.mp4,fps=2,signalstats" \
  -show_entries frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.UAVG,lavfi.signalstats.VAVG \
  -of csv=p=0
```

Si esos números saltan de fila en fila más de 3–4 puntos sin que la escena cambie, el plano es
inestable.

---

## 6. Paso 5 — La deriva del balance dentro de un mismo clip

Este es el problema más traicionero del material de celular, y casi nadie lo busca: **el balance de
blancos automático cambia mientras grabas**. Alguien pasa frente a la cámara, entra una nube, y el
celular "corrige" en medio del plano. El resultado es un clip que empieza cálido y termina frío.

Detectarlo (mismo comando, leído distinto):

```bash
ffprobe -v error -f lavfi -i "movie=celular.mp4,fps=1,signalstats" \
  -show_entries frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.UAVG,lavfi.signalstats.VAVG \
  -of csv=p=0
```

Salida sana (un clip estable): los tres números casi no se mueven.

```
125.276,127.922,125.120
125.167,127.997,125.950
125.011,128.649,126.185
```

Salida enferma: U o V se mueven 6, 10, 15 puntos a lo largo del clip.

Qué hacer:

1. **Cortar el clip** en la parte estable y descartar el resto. Es lo más honesto y lo más rápido.
2. Si necesitas todo el clip, hay que animar la corrección, y ffmpeg no lo hace cómodo: se parte el
   clip en tramos, se corrige cada tramo y se unen con un `xfade` corto de 6–10 cuadros para tapar el
   salto.
3. Y para el futuro: **bloquear el balance de blancos en la cámara antes de grabar** (`170`+). Es un
   toque en la pantalla y ahorra horas.

---

## 7. Paso 6 — Emparejar y unificar

Con todo normalizado en `norm/`, ya es el trabajo de `62` y `255`: eliges el plano de referencia y
llevas los demás a él, midiendo.

Y al final, **unificar lo técnico**, que es lo que hace que el ensamble no falle:

```bash
for f in norm/*.mp4; do
  ffmpeg -y -v error -i "$f" \
    -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p" \
    -c:v libx264 -crf 16 -preset medium \
    -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
    -c:a aac -b:a 192k -ar 48000 "listo/$(basename $f)"
done
```

Unificar: resolución, relación de aspecto, fps, formato de píxel, etiquetas de color, y frecuencia de
audio. Sin eso, el `concat` te sale con saltos, con audio desincronizado o con clips que cambian de
color en medio del video.

---

## 8. La jerarquía cuando no todo se puede salvar

Con seis fuentes, alguna va a estar irremediablemente peor. La decisión no es técnica, es de montaje:

| Prioridad | Qué hacer |
|---|---|
| 1. El plano donde está la **cara** o el **producto** | se salva sí o sí; es el que manda |
| 2. Los planos largos | se ven más tiempo, se notan más |
| 3. Los planos de apoyo (b-roll) | si están feos, **se acortan**: un plano malo de 0,4 s no se juzga |
| 4. El plano irrecuperable | se saca. Un video de 8 planos buenos gana a uno de 12 con dos malos |

El truco #3 es real y muy usado: **el corte arregla lo que el color no puede**. Un plano con un
problema de color que dura 12 cuadros pasa desapercibido; el mismo plano de 3 segundos es el que el
cliente va a señalar.

---

## Errores comunes

- **Emparejar fuente contra fuente en vez de normalizar todas a neutro.** Se vuelve un problema de
  todos contra todos y nunca cierra.
- **No detectar material HDR del celular.** Se ve lavado en la línea SDR y nadie entiende por qué.
- **Forzar etiquetas de entrada en `zscale`.** Falla con `no path between colorspaces`. Lee primero
  con `ffprobe`.
- **Mezclar rango completo (captura de pantalla) con rango limitado sin convertir.** Contraste que
  explota en un solo clip.
- **Sumarle contraste y saturación al material de celular.** Ya viene sobrecocido de fábrica; el
  trabajo es al revés.
- **Meter stock sin aplanarlo.** Trae el look de otro y pelea con el tuyo.
- **Aplicar la LUT técnica de log después de corregir.** Va primero, siempre.
- **Meter material de IA sin grano.** Se ve pegado encima por más que el color esté perfecto.
- **Graduar un plano de IA temporalmente inestable.** No hay grado que arregle una textura que muta.
- **No revisar la deriva de balance dentro de un mismo clip.** Es invisible en un frame y evidente en
  movimiento.
- **No unificar fps y formato de píxel antes de ensamblar.** Saltos, audio corrido, colores que
  cambian en medio del video.
- **Insistir en salvar un plano que se puede acortar a 12 cuadros.**

---

## Checklist

- [ ] Hice la auditoría de **todas** las fuentes: `ffprobe` + `signalstats` en una sola tabla.
- [ ] Detecté material HDR (`arib-std-b67` / `smpte2084`) y lo convertí con `tonemap`.
- [ ] Detecté material en rango completo y lo pasé a limitado.
- [ ] Al material log le apliqué la LUT técnica del fabricante **antes** que nada.
- [ ] Al celular le **bajé** contraste y saturación en vez de subírselos.
- [ ] Al stock le quité el look que traía antes de emparejarlo.
- [ ] Al material de IA le puse grano, un poco de desenfoque y halación suave.
- [ ] Revisé la estabilidad temporal de los planos de IA con `fps=2,signalstats`.
- [ ] Revisé la deriva de balance dentro de cada clip de celular con `fps=1,signalstats`.
- [ ] Volví a medir todas las fuentes **después** de normalizar y la dispersión bajó.
- [ ] Emparejé contra un plano de referencia solo después de normalizar.
- [ ] Unifiqué resolución, aspecto, fps, `pix_fmt`, etiquetas de color y audio antes de ensamblar.
- [ ] Los planos que no se pudieron salvar los acorté o los saqué.
