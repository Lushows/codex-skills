# 81 — Recortes sin fondo

**Qué resuelve:** el problema práctico número uno del bloque de motion — **cómo consigues una imagen sin
fondo** para poder superponerla. Sin esto, el módulo `80` no sirve de nada: puedes componer todo lo que
quieras, pero si tu personaje viene dentro de un rectángulo, lo que pegas encima del video es un
rectángulo. Aquí está la técnica que sí funciona con imágenes generadas por IA, y por qué la obvia
falla.

---

## 1. Qué es "sin fondo" de verdad

> **Canal alfa:** el cuarto dato de cada píxel, además de rojo, verde y azul. Dice qué tan opaco es ese
> píxel: 0 = invisible, 255 = sólido. Una imagen "sin fondo" es una imagen donde los píxeles del fondo
> tienen alfa 0.

Lo que **no** es sin fondo:

- Un JPG. Nunca. El formato JPG no tiene canal alfa, punto.
- Un PNG con el fondo blanco. Es un PNG con fondo, solo que blanco. Se ve limpio en el explorador de
  archivos y te tapa medio video cuando lo superpones.
- Un PNG con cuadritos grises que ves en el navegador... eso sí es alfa. Los cuadritos son cómo se
  dibuja "nada".

**Cómo lo compruebas en 5 segundos, sin abrir nada:**

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=pix_fmt -of csv=p=0 personaje.png
```

Si responde `rgba`, `rgb64be`, `ya8` o cualquier cosa con `a`, hay canal alfa. Si responde `rgb24` o
`rgb48be`, **no hay alfa** y estás a punto de perder una hora.

Y para saber si el alfa realmente tiene agujeros (a veces existe el canal pero está todo en 255):

```bash
ffmpeg -v error -i personaje.png -vf "alphaextract,signalstats,metadata=print:key=lavfi.signalstats.YMIN" -f null -
```

Si `YMIN` sale 255, el canal existe pero es sólido: la imagen NO está recortada.

---

## 2. Formatos que soportan transparencia

Esta tabla evita el 90% de las frustraciones:

| Formato | ¿Alfa? | Para qué sirve | Peso |
|---|---|---|---|
| **PNG** | sí | imagen fija recortada. El estándar. | medio |
| **WebP** | sí | igual que PNG, pesa menos, soporte irregular | bajo |
| **ProRes 4444** (`.mov`) | sí | **video con alfa para editar.** El estándar profesional | muy alto |
| **QuickTime Animation** `qtrle` (`.mov`) | sí | alternativa sin pérdida, gráficos planos | altísimo |
| **WebM / VP9** | sí | video con alfa para web y para pipelines livianos | bajo |
| **APNG / GIF** | sí (GIF: solo 1 bit) | GIF no sirve: el borde queda dentado | — |
| **MP4 / H.264** | **NO** | video normal. **No existe alfa aquí** | bajo |
| **HEVC / H.265** | solo en Apple | no cuentes con él fuera de Final Cut | bajo |
| **JPG** | **NO** | fotografía. Jamás para recortes | bajo |

> **La trampa que cuesta medio día:** exportas tu personaje animado a `.mp4` y desaparece la
> transparencia. No hay parámetro que lo arregle. **H.264 no tiene canal alfa.** Si necesitas video con
> transparencia, sales en ProRes 4444 o en WebM VP9. No hay tercera opción.

Exportar video con alfa, los dos comandos que necesitas:

```bash
# ProRes 4444 — pesado, sin pérdida, el que le pasas a un editor
ffmpeg -i entrada_con_alfa.mov -c:v prores_ks -profile:v 4444 -pix_fmt yuva444p10le -alpha_bits 16 salida.mov

# WebM VP9 — liviano, para pipeline propio y para web
ffmpeg -i entrada_con_alfa.mov -c:v libvpx-vp9 -pix_fmt yuva420p -auto-alt-ref 0 -b:v 0 -crf 24 salida.webm
```

`-auto-alt-ref 0` es obligatorio en VP9 con alfa. Si se te olvida, ffmpeg falla o te devuelve el video
sin transparencia y sin avisarte.

---

## 3. El problema real: la IA no te da alfa confiable

Le pides a un modelo de imagen "personaje sobre fondo transparente" y pasa una de tres:

1. Te devuelve un fondo blanco.
2. Te devuelve el patrón de cuadritos **dibujado** (sí, dibuja los cuadritos como si fueran textura).
3. Te devuelve algo que dice ser transparente pero trae un halo de píxeles semi-opacos.

**La conclusión honesta a agosto de 2026: los modelos de imagen no dan alfa confiable.** Algunos
servicios ofrecen recorte automático como paso aparte y funcionan decente, pero si estás generando la
imagen tú mismo, no cuentes con eso.

### La técnica que sí funciona

Le pides al modelo el personaje **aislado sobre un fondo plano de color** (croma) y **quitas ese color
después**. Es el mismo principio de la pantalla verde de cine, pero con una imagen fija.

> **Croma (chroma key):** filmar o dibujar sobre un color uniforme que no exista en el sujeto, para
> poder borrarlo por color y dejar solo al sujeto.

En el prompt de generación:

```
personaje de cuerpo entero, aislado, recortado limpio, sobre un fondo completamente plano
de color verde puro #00FF00, sin sombras proyectadas sobre el fondo, sin degradado,
iluminación uniforme, sin elementos tocando los bordes del encuadre
```

Las tres partes que la gente olvida y son las que importan:

- **"sin sombras proyectadas sobre el fondo"** — una sombra en el verde te deja una mancha oscura
  imposible de quitar limpiamente.
- **"sin degradado"** — si el fondo va de verde claro a verde oscuro, un solo color clave no basta.
- **"sin elementos tocando los bordes"** — necesitas que las esquinas sean fondo puro. Ahora verás por
  qué esto es crítico.

---

## 4. El descubrimiento: el modelo NO te devuelve el color que pediste

Aquí está el hallazgo que cambia todo el flujo, y salió de un caso real.

Se pidió explícitamente **verde puro `#00FF00`**. El modelo devolvió un fondo **`#94BF6F`** — un verde
salvia, apagado, completamente distinto. Ni cerca.

Y no es un capricho del modelo: los modelos de imagen no "pintan" un valor hexadecimal, **sintetizan una
imagen** donde ese color pasa por la iluminación, el estilo y el ruido del generador. Vas a recibir un
primo lejano del color que pediste, casi siempre.

**La reacción equivocada:** volver a pedírselo. "Ahora sí, verde puro exacto #00FF00, por favor." Te va
a devolver otro verde distinto. Vas a quemar créditos y tiempo peleando con algo que no está bajo tu
control.

**La reacción correcta:** dejar de suponer y **leer el píxel** de la esquina de la imagen que te
devolvió. Sea cual sea ese color, ese es el que hay que quitar. El pipeline se vuelve inmune al capricho
del modelo.

---

## 5. Detectar el color del fondo automáticamente

La técnica: recortas un cuadrito de 8x8 píxeles de una esquina, lo escalas a 1x1 (eso promedia y mata el
ruido de compresión), lo sacas como video crudo en formato `rgb24` y **lees los 3 bytes**. Esos tres
bytes son R, G y B del fondo.

Se usa 8x8 y no 1x1 directo porque un solo píxel puede caer justo en un artefacto de compresión. El
promedio de 64 píxeles es estable.

### En Bash

```bash
ffmpeg -v error -y -i personaje.png -vf "crop=8:8:0:0,scale=1:1" -frames:v 1 -f rawvideo -pix_fmt rgb24 esquina.raw
HEX=$(xxd -p esquina.raw)
echo "El fondo es 0x$HEX"
```

### En PowerShell (Windows)

```powershell
& ffmpeg -v error -y -i personaje.png -vf "crop=8:8:0:0,scale=1:1" -frames:v 1 -f rawvideo -pix_fmt rgb24 esquina.raw
$b = [System.IO.File]::ReadAllBytes("esquina.raw")
$hex = "0x{0:X2}{1:X2}{2:X2}" -f $b[0], $b[1], $b[2]
Write-Output "El fondo es $hex"
```

En el caso real esto imprimió `0x94BF6F`. No `0x00FF00`. Y con `0x94BF6F` el recorte salió perfecto a
la primera.

**Verifica las cuatro esquinas.** Si las cuatro dan (casi) el mismo color, el fondo es plano y vas bien.
Si una da distinto, el personaje toca ese borde o hay degradado, y toca regenerar:

```bash
for POS in "0:0" "iw-8:0" "0:ih-8" "iw-8:ih-8"; do
  ffmpeg -v error -y -i personaje.png -vf "crop=8:8:$POS,scale=1:1" -frames:v 1 -f rawvideo -pix_fmt rgb24 e.raw
  echo "$POS -> $(xxd -p e.raw)"
done
```

---

## 6. Quitar el color: `colorkey`

Con el color ya detectado:

```bash
ffmpeg -y -i personaje.png -vf "colorkey=0x94BF6F:similarity=0.30:blend=0.10,format=rgba" personaje_alfa.png
```

Los dos parámetros que decides tú:

- **`similarity`** (0 a 1) — qué tan parecido tiene que ser un píxel al color clave para borrarse.
  `0.30` es el punto de partida bueno para fondos generados por IA (que nunca son perfectamente
  uniformes). Muy bajo: quedan manchas de fondo. Muy alto: te empieza a comer partes del personaje.
- **`blend`** (0 a 1) — cuánto se suaviza el borde entre lo que se borra y lo que se queda. `0.10` da un
  borde limpio sin quedar dentado. En `0` el contorno queda de sierra.

**Cómo lo afinas:** cambia solo `similarity`, de a 0,05, y mira el resultado sobre un fondo de color
chillón (sección 8). Si al llegar a 0,45 todavía quedan manchas, el fondo tiene degradado y el problema
está en la generación, no en el filtro. Regenera.

### `colorkey` vs `chromakey`: cuál usar

| | `colorkey` | `chromakey` |
|---|---|---|
| Trabaja en | RGB | YUV (ignora el brillo, mira solo el tono) |
| Bueno para | **imágenes generadas por IA**, gráficos planos, capturas | **video real filmado en pantalla verde** |
| Por qué | el fondo generado es plano de verdad, no hay sombras ni pliegues | perdona sombras y arrugas de la tela |

Regla simple: **si la imagen la generó una IA, `colorkey`. Si la grabó una cámara, `chromakey`.**

Para video real:

```bash
ffmpeg -i tomacroma.mp4 -vf "chromakey=0x1FB93C:similarity=0.16:blend=0.06,format=yuva420p" \
  -c:v prores_ks -profile:v 4444 -pix_fmt yuva444p10le recorte.mov
```

---

## 7. Despill y bordes: el paso que separa lo pro de lo casero

Después de quitar el fondo te queda un **halo verde** alrededor del personaje. Se llama **derrame**
(spill): el verde del fondo rebotó sobre los bordes del sujeto. Si no lo quitas, cuando pongas el
recorte sobre un fondo oscuro se va a ver un contorno fosforescente y el ojo lo detecta al instante.

> **Despill:** quitarle a los píxeles del borde el exceso del color del croma, sin cambiar el color real
> del sujeto.

ffmpeg trae un filtro dedicado:

```bash
ffmpeg -y -i personaje.png \
  -vf "colorkey=0x94BF6F:similarity=0.30:blend=0.10,despill=type=green:mix=0.5:expand=0,format=rgba" \
  personaje_alfa.png
```

- `type=green` o `type=blue` según el croma que usaste.
- `mix` (0 a 1) — cuánto quita. `0.5` es el punto de partida. Si el personaje queda magenta o rosado,
  te pasaste: baja a `0.3`.
- `expand` — qué tanto se mete hacia adentro. Déjalo en `0` salvo que el halo sea grueso.

### Encoger la máscara medio píxel (el remate fino)

Si aún queda una línea de un píxel del color viejo, se **erosiona** solo el canal alfa: se come medio
píxel del contorno y el halo desaparece.

```bash
ffmpeg -y -i personaje_alfa.png \
  -vf "format=rgba,erosion=threshold0=0:threshold1=0:threshold2=0:threshold3=255" \
  personaje_limpio.png
```

Los `threshold0..2` en `0` significan "no toques rojo, verde ni azul". El `threshold3=255` dice "erosiona
el canal alfa". Aplícalo **una sola vez**: dos pasadas te adelgazan el personaje y se nota en el pelo y
en los dedos.

---

## 8. Verificar el recorte antes de usarlo (obligatorio)

Nunca metas un recorte al montaje sin verlo sobre un fondo agresivo. Los halos son invisibles sobre
blanco y evidentes sobre magenta.

```bash
ffmpeg -y -f lavfi -i "color=c=0xFF00AA:s=1080x1920" -i personaje_limpio.png \
  -filter_complex "[1:v]scale=-1:1400[pj];[0:v][pj]overlay=x=(W-w)/2:y=(H-h)/2" \
  -frames:v 1 prueba_magenta.png
```

Miras `prueba_magenta.png` y buscas tres cosas:

1. **Halo de color** alrededor del contorno → falta despill.
2. **Borde dentado** tipo escalera → `blend` muy bajo.
3. **Agujeros dentro del personaje** (se ve el magenta a través de la ropa o el pelo) → `similarity`
   muy alto, o el personaje tiene un color parecido al croma. Si el personaje es verde, usa croma
   **magenta** (`#FF00FF`) desde la generación.

Repite la prueba sobre negro (`color=c=black`) para cazar halos oscuros.

---

## 9. El flujo completo, de punta a punta

```bash
# 1. Detectar el color real del fondo
ffmpeg -v error -y -i pj_bruto.png -vf "crop=8:8:0:0,scale=1:1" -frames:v 1 -f rawvideo -pix_fmt rgb24 e.raw
HEX=$(xxd -p e.raw)

# 2. Quitar fondo + despill en una sola pasada
ffmpeg -y -i pj_bruto.png \
  -vf "colorkey=0x$HEX:similarity=0.30:blend=0.10,despill=type=green:mix=0.5:expand=0,format=rgba" \
  pj_alfa.png

# 3. Verificar sobre magenta
ffmpeg -y -f lavfi -i "color=c=0xFF00AA:s=1080x1920" -i pj_alfa.png \
  -filter_complex "[1:v]scale=-1:1400[p];[0:v][p]overlay=(W-w)/2:(H-h)/2" -frames:v 1 prueba.png

# 4. Ya está listo para superponer (modulo 80)
ffmpeg -i base.mp4 -i pj_alfa.png \
  -filter_complex "[1:v]scale=-1:620,format=rgba,fade=t=in:st=3.2:d=0.35:alpha=1[p];\
[0:v][p]overlay=x=W-w-60:y=H-h-260:enable='between(t,3.15,8)'" \
  -map 0:a -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

Guárdalo como script y parametrízalo (ver `88`). Este flujo se corre veinte veces por proyecto.

---

## Errores comunes

1. **Confiar en que el modelo devuelve el color que le pediste.** Pediste `#00FF00`, te dio `#94BF6F`.
   Leer el píxel de la esquina no es un lujo: es la única forma robusta.
2. **Insistirle a la IA con el prompt.** Cada regeneración cuesta créditos y devuelve otro verde
   distinto. El problema no se arregla por ahí.
3. **Exportar video con alfa a `.mp4`.** H.264 no tiene canal alfa. Ni con `-pix_fmt yuva420p` ni con
   nada. ProRes 4444 o WebM VP9.
4. **Olvidar `-auto-alt-ref 0` en VP9.** El archivo sale sin transparencia y ffmpeg no te avisa.
5. **Generar un personaje que toca el borde del cuadro.** Te quedas sin esquina limpia para muestrear y
   sin saber el color del fondo.
6. **Usar croma verde con un personaje verde.** Se le come la ropa. Elige un croma que no exista en el
   sujeto: magenta para personajes verdes, verde para casi todo lo demás.
7. **Saltarse el despill.** Sobre fondo claro no se nota; sobre fondo oscuro el halo fosforescente grita
   "esto está mal recortado".
8. **Erosionar dos o tres veces "por si acaso".** Le comes el pelo y los dedos al personaje.
9. **Aceptar el recorte sin verlo sobre magenta.** Es la única prueba que caza halos y agujeros. Toma
   cinco segundos.
10. **Usar `chromakey` en imágenes generadas o `colorkey` en video real.** Al revés funciona peor y vas
    a echarle la culpa al material.
11. **Usar GIF para un recorte animado.** El GIF tiene transparencia de 1 bit: cada píxel es opaco o
    invisible, sin medias tintas. El borde queda de sierra siempre.

---

## Checklist

Antes de dar por bueno un recorte:

- [ ] Confirmé con `ffprobe` que el archivo final tiene `pix_fmt` con alfa (`rgba` / `yuva...`).
- [ ] Comprobé con `alphaextract` + `signalstats` que el alfa **tiene agujeros** (YMIN < 255).
- [ ] **Leí el color real** de la esquina en vez de asumir el que pedí en el prompt.
- [ ] Muestreé **las cuatro esquinas** y dan el mismo color (fondo plano, sin degradado).
- [ ] Usé `colorkey` para imagen generada / `chromakey` para video filmado.
- [ ] Ajusté `similarity` de a 0,05 hasta que no queden manchas ni agujeros.
- [ ] Apliqué **despill** con el `type` correcto y el personaje no quedó rosado.
- [ ] Verifiqué el recorte **sobre magenta y sobre negro**: sin halo, sin sierra, sin agujeros.
- [ ] Si es video con alfa, salió en **ProRes 4444** o **WebM VP9 con `-auto-alt-ref 0`**, nunca en mp4.
- [ ] Guardé el PNG con alfa como archivo maestro; el montaje consume ese, no el bruto con croma.
