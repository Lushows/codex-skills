# 69 — Monitoreo y scopes

Los scopes son los instrumentos de medición del color. Son al colorista lo que el medidor de dB es
al ingeniero de sonido: la manera de saber qué está pasando **sin depender de los ojos**.

Y aquí hay una razón práctica muy fuerte para usarlos siempre:

- Tú no tienes un monitor calibrado, ni una habitación con luz controlada.
- Yo, como modelo, no veo el video corriendo — veo fotogramas y números.
- El cliente lo va a ver en un celular con modo vívido, al sol, con el brillo al 40%.

**Ninguno de los tres puede confiar en "yo lo veo bien".** Los scopes son lo único que dice la
verdad, y son idénticos en tu computador, en el mío y en el estudio de Hollywood.

Los cuatro instrumentos son: **histograma**, **forma de onda** (waveform), **vectorscopio** y
**parade RGB**. Cada uno responde una pregunta distinta.

---

## 1. Histograma — ¿está bien expuesto?

Cuenta cuántos píxeles hay de cada nivel de brillo. Izquierda = oscuro, derecha = claro, altura =
cuántos píxeles hay de ese nivel.

```bash
# Histograma sobre un frame
ffmpeg -y -ss 8 -i clip.mp4 -frames:v 1 \
  -vf "histogram=display_mode=stack:levels_mode=linear:components=7" histograma.png

# Histograma en video, junto al plano, para revisar todo el clip
ffmpeg -y -i clip.mp4 -filter_complex \
  "[0:v]split=2[v][h];[h]histogram=display_mode=stack:levels_mode=logarithmic,scale=540:-1[hist];\
   [v]scale=540:-1[vid];[vid][hist]vstack=inputs=2" \
  -frames:v 300 -c:v libx264 -crf 18 hist_video.mp4
```

Cómo se lee:

| Lo que ves | Qué significa | Qué hacer |
|---|---|---|
| Todo apiñado a la izquierda | subexpuesto | subir `gamma` |
| Todo apiñado a la derecha | sobreexpuesto | bajar exposición; si hay pared vertical al final, hay información **perdida** |
| Pared vertical pegada al borde izquierdo | negros **tapados** | información perdida, no se recupera |
| Pared vertical pegada al borde derecho | blancos **quemados** | información perdida, no se recupera |
| Todo en el centro, sin llegar a los bordes | plano/lavado (o es material log) | subir contraste, o aplicar la LUT técnica |
| Distribución amplia con picos en varios sitios | bien | seguir |

**Lo que el histograma NO te dice:** dónde está cada cosa en el cuadro. Un histograma perfecto puede
corresponder a una cara oscura sobre un fondo brillante. Para eso está la forma de onda.

---

## 2. Forma de onda (waveform) — ¿dónde está cada brillo?

Es el instrumento más importante y el que menos gente usa. La forma de onda conserva la **posición
horizontal**: cada columna del scope corresponde a la misma columna del cuadro. La altura es el
brillo.

Es decir: si la cara está a la izquierda del cuadro, en el waveform la ves a la izquierda. Puedes
saber si la cara está bien expuesta aunque el fondo esté quemado.

```bash
# Forma de onda de luma, con escala de 0 a 100 IRE y números
ffmpeg -y -ss 8 -i clip.mp4 -frames:v 1 -vf \
  "waveform=mode=column:intensity=0.10:mirror=1:components=1:display=overlay:graticule=green:flags=numbers+dots:scale=ire" \
  waveform.png
```

Cómo se lee (escala 0–100 IRE, que es como se habla en la industria):

| Zona | IRE | Qué debe haber |
|---|---|---|
| Negro | 0 | sombras profundas; si hay una línea gruesa pegada al 0, hay negros tapados |
| Sombras | 5–25 | detalle de sombra |
| **Piel** | **45–70** (clara) · **30–50** (media) · **18–35** (oscura) | **la cara vive aquí** |
| Medios | 40–70 | el grueso de la escena |
| Luces | 75–95 | reflejos, ropa blanca |
| Blanco | 100 | solo fuentes de luz y reflejos especulares |

**El uso número uno de la forma de onda: emparejar planos.** Pon dos planos uno tras otro con el
waveform encima y ajusta hasta que la "masa" del gráfico esté a la misma altura. Es mil veces más
preciso que mirarlos.

```bash
# Waveform en vivo, debajo del video — el monitor de trabajo
ffmpeg -y -i clip.mp4 -filter_complex \
  "[0:v]split=2[v][w];\
   [w]waveform=mode=column:intensity=0.08:mirror=1:components=1:graticule=green:flags=numbers:scale=ire,scale=720:240[wf];\
   [v]scale=720:-1[vid];[vid][wf]vstack=inputs=2" \
  -frames:v 400 -c:v libx264 -crf 18 monitor_waveform.mp4
```

### Parade RGB — el detector de balance de blancos

Es la misma forma de onda pero con los tres canales lado a lado. Es **la herramienta definitiva para
el balance de blancos**:

```bash
ffmpeg -y -ss 8 -i clip.mp4 -frames:v 1 -vf \
  "waveform=mode=column:intensity=0.10:components=7:display=parade:graticule=green:flags=numbers:scale=ire" \
  parade.png
```

Cómo se lee:

- **Mira la parte de abajo de los tres canales.** Si el rojo empieza más arriba que los otros, tus
  sombras tienen un tinte rojo. Igual con verde y azul.
- **Mira la parte de arriba.** Si el azul llega más alto que el rojo, tus luces son frías.
- **En una escena neutra, los tres deben empezar y terminar más o menos al mismo nivel.**

Ese "más o menos al mismo nivel" arriba y abajo es, literalmente, la definición de balance de
blancos correcto. Es la única forma de corregir tinte sin adivinar.

---

## 3. Vectorscopio — ¿qué colores hay y cuánto?

Ignora el brillo completamente. Solo muestra color:

- **Centro** = sin color (gris, blanco, negro).
- **Distancia al centro** = saturación. Más lejos, más saturado.
- **Ángulo** = matiz. Cada dirección es un color.

```bash
ffmpeg -y -ss 8 -i clip.mp4 -frames:v 1 -vf \
  "vectorscope=mode=color3:intensity=0.12:graticule=green:flags=name:opacity=0.4" vectorscopio.png
```

Con `graticule=green:flags=name` te dibuja las cajas de los colores primarios y secundarios con su
nombre (R, G, B, Cy, Mg, Yl). Esas cajas son la referencia.

Cómo se lee:

| Lo que ves | Qué significa |
|---|---|
| Nube compacta en el centro | imagen desaturada o en blanco y negro |
| Nube desplazada hacia un lado | **hay un tinte** — todo el plano tira a ese color |
| Nube que sale de las cajas de referencia | saturación ilegal; se va a embarrar al comprimir |
| **Una sola línea recta desde el centro** | **duotono perfecto** (ver `64`) |
| Puntos concentrados entre las cajas de rojo y amarillo, algo más cerca del rojo | **piel** |

### La línea de piel

Es el uso clásico del vectorscopio. Todos los tonos de piel humana caen sobre la **misma dirección**
en el vectorscopio, entre rojo y amarillo. Lo que cambia entre una persona y otra es qué tan lejos
del centro está (saturación), no el ángulo.

Práctica: recorta la mejilla y mira solo eso en el vectorscopio. Debe caer en esa dirección. Si se
desvía hacia el verde o hacia el magenta, la piel está mal (ver `67`).

```bash
ffmpeg -y -ss 8 -i clip.mp4 -frames:v 1 -vf \
  "crop=120:120:520:400,vectorscope=mode=color3:intensity=0.3:graticule=green:flags=name" \
  piel_vectorscopio.png
```

---

## 4. Los números: `signalstats` y `showinfo`

Los scopes son imágenes. Para un flujo automatizado —y para que yo pueda leerlos— lo que sirve son
**números**. `signalstats` los produce.

```bash
ffmpeg -hide_banner -ss 8 -t 4 -i clip.mp4 \
  -vf "signalstats,metadata=mode=print:file=-" -f null - 2>&1 \
  | grep "lavfi.signalstats"
```

Las claves que importan:

| Clave | Qué mide | Rango sano (8 bits, limitado) |
|---|---|---|
| `YMIN` | brillo más oscuro | ≥ 16; si es 16 en área grande, negros tapados |
| `YLOW` | percentil bajo de brillo | 20–40 |
| `YAVG` | brillo promedio | 90–150 en una escena normal |
| `YHIGH` | percentil alto | 180–225 |
| `YMAX` | brillo más claro | ≤ 235; si es 235 en área grande, quemado |
| `UAVG` | promedio de Cb (azul↔) | ~128 en escena neutra |
| `VAVG` | promedio de Cr (rojo↔) | ~128 en escena neutra |
| `SATAVG` | saturación promedio | 20–70 según el material |
| `SATMAX` | saturación máxima | > 110 = saturación problemática |
| `HUEAVG` | matiz promedio | útil para comparar planos |
| `YDIF` | diferencia entre fotogramas | picos = corte o flash |
| `TOUT` | píxeles atípicos | > 0.005 = ruido o píxeles muertos |
| `BRNG` | proporción de píxeles fuera del rango legal | debería ser ~0 en entrega |

Resumen de un clip en una línea (promedios de todo el clip):

```bash
ffmpeg -hide_banner -i clip.mp4 -vf "signalstats,metadata=mode=print:file=-" -f null - 2>&1 \
| awk -F= '/YMIN|YAVG|YMAX|UAVG|VAVG|SATAVG/ {s[$1]+=$2; n[$1]++} 
           END {for (k in s) printf "%-38s %8.2f\n", k, s[k]/n[k]}' | sort
```

Y para **ver** dónde están los píxeles fuera de rango legal (se pintan del color que le digas):

```bash
ffmpeg -y -ss 8 -i clip.mp4 -frames:v 1 \
  -vf "signalstats=out=brng:color=yellow" fuera_de_rango.png
```

Todo lo que salga amarillo en esa imagen se va a comportar mal al comprimir y al emitir. En una
entrega para redes no es fatal, pero si hay mucho, es señal de que te pasaste con el contraste.

### `showinfo` — el inspector fotograma a fotograma

```bash
ffmpeg -hide_banner -i clip.mp4 -vf showinfo -f null - 2>&1 | head -20
```

Te da por fotograma: número, `pts_time` (el tiempo exacto), tipo de fotograma (I/P/B), si es clave,
tamaño, y `mean`/`stdev` por plano. Sirve para:
- **Encontrar el tiempo exacto** de un fotograma para un corte (ver `15`).
- **Detectar flashes o cambios bruscos**: un salto grande en `mean` es un corte o un flash.
- **Verificar que la conversión no cambió el número de fotogramas.**

---

## 5. La sala de control: todos los scopes en una sola imagen

Este es el comando que más vas a usar. Video arriba, forma de onda y vectorscopio abajo, todo en un
solo archivo que puedes mirar (o que me puedes pasar a mí para que lo lea):

```bash
ffmpeg -y -ss 8 -i clip.mp4 -frames:v 1 -filter_complex "\
[0:v]split=4[v][w][vec][hist];\
[v]scale=640:-1,pad=640:400:(ow-iw)/2:(oh-ih)/2:black[vid];\
[w]waveform=mode=column:intensity=0.10:mirror=1:components=1:graticule=green:flags=numbers:scale=ire,scale=640:400[wf];\
[vec]vectorscope=mode=color3:intensity=0.15:graticule=green:flags=name,scale=400:400[vs];\
[hist]histogram=display_mode=stack:levels_mode=logarithmic,scale=400:400[hg];\
[vid][wf]hstack=inputs=2[top];\
[vs][hg]hstack=inputs=2,scale=1280:400[bot];\
[top][bot]vstack=inputs=2" \
  sala_de_control.png
```

Y la versión en video, para revisar un clip entero:

```bash
ffmpeg -y -i clip.mp4 -filter_complex "\
[0:v]split=3[v][w][vec];\
[v]scale=720:-1[vid];\
[w]waveform=mode=column:intensity=0.08:mirror=1:components=1:graticule=green:scale=ire,scale=720:220[wf];\
[vec]vectorscope=mode=color3:intensity=0.12:graticule=green:flags=name,scale=220:220,pad=720:220:(ow-iw)/2:0:black[vs];\
[vid][wf]vstack=inputs=2[a];[a][vs]vstack=inputs=2" \
  -c:v libx264 -crf 20 -preset fast sala_de_control.mp4
```

---

## 6. Otros instrumentos que existen y sirven

```bash
# oscilloscope: sonda de una línea concreta del cuadro (útil para degradados y banding)
ffmpeg -y -ss 8 -i clip.mp4 -frames:v 1 \
  -vf "oscilloscope=x=0.5:y=0.5:s=0.9:t=0.5" oscilloscope.png

# pixscope: los valores numéricos exactos de un puñado de píxeles (para leer un color a mano)
ffmpeg -y -ss 8 -i clip.mp4 -frames:v 1 \
  -vf "pixscope=x=0.42:y=0.35:w=12:h=12" pixscope.png

# datascope: los valores en hexadecimal, píxel por píxel
ffmpeg -y -ss 8 -i clip.mp4 -frames:v 1 \
  -vf "crop=32:32:520:400,datascope=mode=color2:size=hd480" datascope.png
```

`pixscope` es la forma más directa de contestar "¿qué color exacto tiene ese píxel?" — útil para
verificar un duotono o para sacar el HEX real de un elemento de marca dentro del video.

---

## 7. Cómo usar todo esto en la práctica

El flujo de monitoreo de un proyecto real:

1. **Antes de tocar nada** — `signalstats` de todos los clips, tabla comparativa. Sabes qué tienes.
2. **Durante la corrección** — parade RGB para el balance de blancos, waveform para la exposición.
3. **Durante el emparejado** — waveform de dos planos juntos hasta que las masas coincidan.
4. **Después del look** — vectorscopio para la piel, `signalstats` en la mejilla (ver `67`).
5. **Antes de entregar** — `signalstats=out=brng` para ver si hay algo ilegal, y la sala de control
   de tres o cuatro frames representativos.

Y la regla que ata todo: **si vas a decir "quedó bien", tienes que poder decir con qué lo mediste.**

---

## Errores comunes

- **Juzgar el color mirando, en un monitor sin calibrar, con la lámpara del cuarto encendida.**
- **Usar solo el histograma.** No te dice dónde está cada cosa. La forma de onda sí.
- **No usar el parade RGB para el balance de blancos** y andar adivinando el tinte.
- **Leer el vectorscopio como si midiera brillo.** No mide brillo. Solo color.
- **Poner `intensity` muy alto en el waveform o el vectorscopio.** Se satura el gráfico y no se
  distingue nada. Zona útil: 0.05–0.20.
- **Medir un solo fotograma de un clip que cambia** (entra una nube, la persona se voltea). Mide al
  menos 3 puntos, o corre `signalstats` sobre un tramo.
- **Confundir un `SATMAX` alto legítimo** (hay un letrero de neón rojo en cuadro) con un problema de
  grado. Lee la imagen junto con el número.
- **Interpretar `UAVG`/`VAVG` de una escena dominada por un color grande** (una pared roja) como si
  fuera un tinte. El promedio es de todo el cuadro.
- **Ignorar `BRNG` en la entrega.** Si hay mucho fuera de rango, la compresión te va a castigar.
- **Generar los scopes y no mirarlos.** Pasa más de lo que parece.
- **No guardar las medidas del proyecto.** La próxima pieza del mismo cliente empieza de cero.

---

## Checklist

- [ ] Corrí `signalstats` en todos los clips **antes** de tocar color, y tengo la tabla.
- [ ] Usé el **parade RGB** para verificar el balance de blancos de cada plano.
- [ ] Usé la **forma de onda** (no el histograma) para emparejar exposición entre planos.
- [ ] Verifiqué que la piel esté en la zona IRE correcta según el tono de la persona.
- [ ] Miré el **vectorscopio** de un recorte de mejilla y la piel cae en la dirección correcta.
- [ ] Si hice duotono, el vectorscopio muestra **una línea**, no una nube.
- [ ] `YMIN` no está clavado en 16 ni `YMAX` en 235 en áreas grandes por culpa de mi grado.
- [ ] Corrí `signalstats=out=brng` sobre la entrega y no hay zonas grandes fuera de rango.
- [ ] Generé la "sala de control" de al menos 3 frames representativos del video final.
- [ ] Puedo decir con qué medí cada afirmación que hago sobre el color.
- [ ] Guardé las medidas y los comandos en el proyecto para la próxima pieza del mismo cliente.
