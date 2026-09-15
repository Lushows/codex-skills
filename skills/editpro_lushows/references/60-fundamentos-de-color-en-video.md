# 60 — Fundamentos de color en video

Antes de tocar un solo filtro tienes que entender **qué es el color dentro de un archivo de video**.
No es lo mismo que en Photoshop. Un video no guarda "rojo, verde y azul" como te imaginas: guarda
brillo por un lado y color por otro, comprimido, con etiquetas que dicen cómo hay que interpretarlo.
Cuando esas etiquetas se pierden o se equivocan, el video se ve lavado, apagado o con los negros
grises. Y ahí es cuando la gente dice "es que ffmpeg me dañó el color". No fue ffmpeg. Fue que
nadie le dijo en qué idioma estaba escrito el archivo.

Este módulo es el piso. Todo el bloque 6 se para encima de él.

---

## 1. Luma y croma: el video separa brillo de color

Una foto en tu computador guarda por cada píxel tres números: cuánto rojo, cuánto verde, cuánto
azul (RGB). El video **casi nunca** hace eso. El video guarda:

- **Luma (Y)** — el brillo. Es la imagen en blanco y negro. Toda la información de forma, textura,
  detalle y nitidez vive aquí.
- **Croma (Cb, Cr)** — el color, expresado como "qué tan azul" y "qué tan rojo" se desvía ese píxel
  respecto al gris.

¿Por qué esa separación tan rara? Porque el ojo humano ve muchísimo mejor el brillo que el color.
Puedes botar tres cuartas partes de la información de color y nadie lo nota. Botar información de
brillo se ve inmediatamente. Entonces el video se aprovecha de eso:

| Notación | Qué significa | Dónde lo ves |
|---|---|---|
| `4:4:4` | color completo, un valor de croma por píxel | ProRes 4444, masters, gráficos |
| `4:2:2` | la mitad de resolución de color en horizontal | ProRes 422, cámaras profesionales |
| `4:2:0` | la cuarta parte de resolución de color | **todo lo que publicas**: H.264, H.265, celular |

Esto tiene una consecuencia práctica enorme y poca gente la conecta: **en 4:2:0 los bordes de color
saturado se ven sucios**. Un texto rojo puro sobre fondo negro en un reel se ve con bordes
"babosos". No es tu tipografía; es el submuestreo de croma. Se arregla no usando rojo puro
saturado en bordes finos, o subiendo un poco el brillo del color para que el luma haga el trabajo.

Para saber qué tiene tu archivo:

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=codec_name,width,height,pix_fmt,color_range,color_space,color_transfer,color_primaries \
  -of default=noprint_wrappers=1 entrada.mp4
```

Salida típica de un celular:

```
codec_name=h264
width=1080
height=1920
pix_fmt=yuv420p
color_range=tv
color_space=bt709
color_transfer=bt709
color_primaries=bt709
```

Si en vez de valores ves `unknown` o el campo no aparece, **el archivo no está etiquetado**. Guarda
ese dato: es la causa número uno de que un video se vea distinto en cada pantalla.

---

## 2. Rango limitado vs rango completo (16–235 vs 0–255)

Este es el concepto que más plata cuesta en tiempo perdido.

Un byte va de 0 a 255. La pregunta es: ¿el negro absoluto es 0 o es 16?

- **Rango completo (full / PC / `jpeg` / `0-255`)**: negro = 0, blanco = 255. Es lo que usa tu
  monitor, una foto JPG, una captura de pantalla, un PNG.
- **Rango limitado (limited / TV / `mpeg` / `16-235`)**: negro = 16, blanco = 235. Los valores por
  debajo de 16 y por encima de 235 existen pero se llaman "footroom" y "headroom": sirven para que
  la señal no se recorte en la cadena de televisión. Es lo que usa **la inmensa mayoría del video**:
  H.264, H.265, lo que sale de tu cámara y de tu celular.

¿Qué pasa si te equivocas?

| Error | Cómo se ve | Explicación en simple |
|---|---|---|
| Tratas limitado como completo | **lavado**: negros grises, blancos apagados, poco contraste | leíste el 16 como si fuera negro puro y lo dejaste ahí gris |
| Tratas completo como limitado | **quemado**: negros tapados, blancos reventados, contraste falso | estiraste una señal que ya estaba estirada |

Esa es exactamente la sensación de "se me lavó el video al exportar". Nadie te dañó el color: se
perdió la etiqueta de rango en algún paso.

### Leerlo y arreglarlo

Para saber qué dice el archivo, el campo es `color_range` (`tv` = limitado, `pc` = completo).

Convertir **limitado → completo** (por ejemplo, para trabajar con una captura de pantalla mezclada
con video de cámara):

```bash
ffmpeg -i entrada.mp4 -vf "scale=in_range=limited:out_range=full,format=yuv420p" \
  -color_range pc -c:v libx264 -crf 18 salida_full.mp4
```

Convertir **completo → limitado** (lo normal antes de publicar):

```bash
ffmpeg -i entrada.mov -vf "scale=in_range=full:out_range=limited,format=yuv420p" \
  -color_range tv -c:v libx264 -crf 18 salida_tv.mp4
```

Y la manera manual, útil cuando quieres entender qué está pasando (16/255 = 0.0627,
235/255 = 0.9216):

```bash
# Estirar 16-235 hasta 0-255 con colorlevels (mismo efecto que limited->full)
ffmpeg -i entrada.mp4 -vf \
  "colorlevels=rimin=0.0627:gimin=0.0627:bimin=0.0627:rimax=0.9216:gimax=0.9216:bimax=0.9216" \
  -c:v libx264 -crf 18 salida.mp4
```

> **Regla de oro:** no conviertas rango "por si acaso". Primero **mira** el `color_range` con
> ffprobe. Si el material y la salida son ambos `tv`, no toques nada. La conversión de más es tan
> destructiva como la de menos.

---

## 3. Espacios de color: BT.601, BT.709, BT.2020, sRGB

Un espacio de color define **qué rojo es "rojo"**. El número 255 en el canal rojo no significa nada
por sí solo; significa "el rojo más saturado que este sistema puede mostrar", y ese rojo es distinto
en cada sistema.

| Espacio | Dónde vive | Notas |
|---|---|---|
| **BT.601** | video estándar antiguo (SD, DVD, cámaras viejas, algunos celulares en 480p) | matriz distinta de luma; mezclarlo con 709 mueve los tonos |
| **BT.709** | **HD: es tu caso el 95% del tiempo** | 1080p, 4K SDR, Instagram, TikTok, YouTube SDR |
| **sRGB** | imágenes, gráficos, PNG, capturas de pantalla | primarios prácticamente iguales a 709, gamma distinta |
| **BT.2020 / PQ / HLG** | HDR | otro mundo; si no sabes que estás en HDR, no estás en HDR |

El caso real que más te va a pasar: mezclas un clip de cámara (BT.709) con una animación exportada
de un navegador o con un PNG generado por IA (sRGB, rango completo). Sin conversión, la animación
sale más contrastada y más saturada que el video. Se ve "pegada encima", no integrada.

Conversión correcta de espacio (no solo de rango):

```bash
ffmpeg -i clip_sd_601.mp4 -vf \
  "colorspace=all=bt709:iall=bt601-6-625:format=yuv420p" \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -c:v libx264 -crf 18 clip_709.mp4
```

Si tu compilación trae `libzimg` (compruébalo con `ffmpeg -hide_banner -buildconf | grep zimg`),
`zscale` hace lo mismo con mejor precisión:

```bash
ffmpeg -i entrada.mp4 -vf \
  "zscale=matrix=709:transfer=709:primaries=709:range=limited,format=yuv420p" \
  -c:v libx264 -crf 18 salida.mp4
```

---

## 4. Gamma: por qué el 50% de brillo no es el 50% de luz

La curva de transferencia (transfer / gamma / EOTF) es la traducción entre "el número guardado" y
"la luz que sale de la pantalla". No es lineal, y por una buena razón: el ojo tampoco lo es. El ojo
distingue muchísimos matices en las sombras y muy pocos en las luces altas, así que el sistema
guarda más precisión abajo.

Consecuencia práctica: **cuando subes el brillo con `eq=brightness=`, estás sumando en un espacio no
lineal**, y por eso los grises se ensucian rápido. Para levantar sombras sin dañarlas, casi siempre
es mejor `gamma` que `brightness`:

```bash
# MAL para levantar sombras: aplasta el negro hacia gris plano
ffmpeg -i in.mp4 -vf "eq=brightness=0.08" out.mp4

# BIEN: levanta la zona media sin mover el punto negro
ffmpeg -i in.mp4 -vf "eq=gamma=1.10" out.mp4
```

Ojo con la trampa histórica del "gamma shift de QuickTime": un mismo archivo se veía más claro en
un reproductor de Mac que en otro. Hoy está en gran parte resuelto, pero sigue apareciendo con
archivos ProRes sin etiquetar. Si un video se te ve distinto entre VLC y el reproductor del sistema,
el sospechoso número uno es el etiquetado, no el filtro que aplicaste.

---

## 5. Por qué un mismo video se ve distinto en cada pantalla

Junta todo lo anterior y tienes la respuesta completa. Cuando el cliente te escribe "en mi celular
se ve más oscuro", la causa está en una de estas seis, en este orden de frecuencia:

1. **El archivo no está etiquetado.** Sin `color_space`/`color_range`, cada reproductor adivina. Los
   reproductores de escritorio suelen asumir BT.709 limitado; algunos navegadores asumen otra cosa.
   Resultado: el mismo archivo, dos colores.
2. **Rango mal convertido.** Ya lo viste: lavado o quemado.
3. **La pantalla del cliente.** Un celular con "modo vívido" satura todo un 20%. Un modo de ahorro
   de batería baja el brillo y aplasta las sombras. No lo puedes controlar, pero **sí puedes evitar
   depender de matices finos en las sombras**, que son los primeros que desaparecen.
4. **Brillo automático + luz ambiente.** El mismo teléfono se ve distinto al sol.
5. **Recompresión de la plataforma.** Instagram, TikTok y WhatsApp vuelven a comprimir tu archivo.
   Los degradados se bandean y la saturación alta se ensucia. Ver `68-color-por-plataforma.md`.
6. **HDR mal manejado.** Un clip grabado en HDR (Dolby Vision del iPhone) metido en una línea SDR sin
   tonemapping sale lavadísimo y con la piel gris. Es un caso aparte y se ve así de feo, siempre.

### La regla de higiene mínima al exportar

Etiqueta **siempre**. Cuesta cuatro parámetros y te ahorra la mitad de los problemas de color:

```bash
ffmpeg -i corte.mov -vf "format=yuv420p" \
  -c:v libx264 -crf 18 -preset slow \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -x264-params "colorprim=bt709:transfer=bt709:colormatrix=bt709" \
  -movflags +faststart master.mp4
```

`format=yuv420p` no es opcional: sin él puedes exportar en `yuv444p` o `yuvj420p` y hay
reproductores (y plataformas) que sencillamente no lo muestran o lo muestran con el color corrido.

---

## 6. Cómo tomar una decisión de color sin tener los ojos calibrados

Tú no tienes un monitor de referencia. Yo, como modelo, no veo el video corriendo. Entonces el
método no es "mirar y decidir": es **medir y decidir**, y dejar el gusto para el humano.

Lo mínimo antes de graduar cualquier cosa:

```bash
# Promedios y mínimos/máximos por canal de un tramo de 5 s
ffmpeg -hide_banner -ss 12 -t 5 -i entrada.mp4 \
  -vf "signalstats,metadata=mode=print:file=-" -f null - 2>&1 | grep -E "YAVG|YMIN|YMAX|SATAVG"
```

Con eso sabes si el plano está oscuro (YAVG bajo), si tiene los negros tapados (YMIN pegado a 16),
si está quemado (YMAX pegado a 235) y qué tan saturado viene. Es información dura, no impresión.
El detalle completo está en `69-monitoreo-y-scopes.md`.

---

## Errores comunes

- **Convertir rango sin mirarlo primero.** Aplicar `in_range=limited:out_range=full` a un archivo que
  ya venía en full te revienta los blancos y tapa los negros. Siempre `ffprobe` antes.
- **Exportar sin `format=yuv420p`.** Funciona en tu VLC y se ve verde o no reproduce en el celular
  del cliente. Es gratis ponerlo; ponlo siempre.
- **Exportar sin etiquetas de color.** El archivo "se ve bien aquí" y distinto en todas partes.
  Cuatro parámetros lo resuelven.
- **Mezclar PNG/capturas sRGB con video BT.709 sin convertir.** El gráfico se ve más contrastado y
  "pegado". Convierte el gráfico, no el video.
- **Meter un clip HDR del iPhone en una línea SDR sin tonemapping.** Sale lavado y con la piel gris,
  y después le echas la culpa a la gradación.
- **Usar `brightness` para levantar sombras.** Ensucia el negro. Usa `gamma`.
- **Usar rojo o azul puros saturados en texto delgado.** El 4:2:0 te va a devolver bordes sucios.
- **Creer que "se ve más oscuro en su celular" es culpa tuya siempre.** A veces es el modo de ahorro
  de batería del cliente. Pídele una captura antes de rehacer nada.
- **Trabajar todo el grado sobre un H.264 de 8 bits y encima re-exportar tres veces.** Cada pasada
  añade banding. Haz el grado en una sola cadena de filtros y exporta una vez.

---

## Checklist

- [ ] Corrí `ffprobe` y anoté `pix_fmt`, `color_range`, `color_space`, `color_transfer` de **cada**
      fuente distinta del proyecto.
- [ ] Identifiqué si hay material mezclado (cámara + captura de pantalla + PNG de IA + clip HDR).
- [ ] Convertí a un espacio común (normalmente BT.709, rango limitado, 4:2:0) **antes** de corregir.
- [ ] Verifiqué que no apliqué conversión de rango doble ni innecesaria.
- [ ] Levanté sombras con `gamma`, no con `brightness`.
- [ ] Medí con `signalstats` en vez de opinar: YMIN, YMAX, YAVG, SATAVG.
- [ ] El export final lleva `format=yuv420p`.
- [ ] El export final lleva las cuatro etiquetas: `-colorspace`, `-color_primaries`, `-color_trc`,
      `-color_range` (y `-x264-params` si uso libx264).
- [ ] El export final lleva `-movflags +faststart` si va a web.
- [ ] Solo hice **una** codificación final; no re-comprimí un archivo ya comprimido.
- [ ] Si el cliente reporta diferencia de color, pedí captura de pantalla antes de tocar el proyecto.
