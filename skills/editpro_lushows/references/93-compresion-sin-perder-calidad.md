# 93 — Compresión sin perder calidad: dónde está el punto óptimo

> "Sin perder calidad" es mentira si lo tomas literal: toda compresión pierde algo. Lo que sí existe es
> **compresión sin pérdida visible**, y tiene un punto matemático concreto que se puede medir. Este módulo
> te enseña a encontrarlo con números, no con "a mí me parece que se ve bien".

---

## El problema real

Casi todo el mundo comprime así: mueve el deslizador, mira el video, dice "se ve bien" y exporta. Eso
falla por tres razones:

1. **Tu monitor miente.** Lo que se ve bien en una pantalla de 27" a 60 cm se ve horrible en un celular
   con brillo alto, y al revés.
2. **Te acostumbras.** Después de mirar el mismo video 40 veces, tu cerebro rellena el detalle que ya no
   está. Se llama adaptación perceptual y arruina cualquier juicio.
3. **No sabes cuánto margen te queda.** Si "se ve bien" a CRF 20, ¿se vería igual a CRF 23 con la mitad del
   peso? No tienes forma de saberlo mirando.

La solución es **medir**. Y sí, se puede medir gratis con ffmpeg.

---

## Las tres formas de medir calidad

### PSNR — la más vieja y la menos útil

Compara píxel por píxel y saca un promedio de error, en decibelios. Más alto es mejor.

- 40+ dB: prácticamente idéntico
- 30–40 dB: buena calidad
- <30 dB: se nota

**Su problema:** no sabe nada de cómo ve el ojo humano. Un video con ruido leve repartido puede tener PSNR
bajo y verse perfecto; un video con un bloque feo en la cara puede tener PSNR alto y verse horrible.
**Úsalo solo como señal rápida de "algo se rompió mucho".**

### SSIM — mide estructura

*Structural Similarity Index*. En vez de comparar píxeles sueltos, compara **estructura**: bordes,
texturas, contraste local. Va de 0 a 1.

| SSIM | Qué significa |
|---|---|
| **> 0,98** | Indistinguible |
| 0,95 – 0,98 | Muy bueno, diferencias solo si comparas lado a lado |
| 0,90 – 0,95 | Notable si buscas |
| < 0,90 | Se ve |

Es mucho mejor que PSNR y **viene en cualquier ffmpeg sin instalar nada**. Es tu herramienta del día a día.

### VMAF — el que de verdad predice lo que ve la gente

*Video Multi-Method Assessment Fusion*. Lo creó Netflix combinando varias métricas con un modelo entrenado
con **juicios humanos reales**. Da un puntaje de 0 a 100 que corresponde bastante bien a "cuánta calidad
percibe una persona".

| VMAF | Qué significa en la práctica |
|---|---|
| **95–100** | El espectador no puede distinguirlo del original |
| **93–95** | **El punto óptimo. Nadie se queja y pesa mucho menos** |
| 88–93 | Bueno. Aceptable para redes sociales |
| 80–88 | Se empieza a notar en pantalla grande |
| < 80 | Visiblemente comprimido |

**La regla de oro de la industria: apunta a VMAF 93–95.** Por encima de 95 estás gastando megabytes que
nadie percibe. Por debajo de 90 empiezas a regalar calidad.

Nota de estado (2026): las versiones publicadas de libvmaf todavía usan los modelos v0.6.1, que es el
estándar de facto. No necesitas nada más nuevo.

---

## Cómo medir, comandos reales

**Primero verifica que tu ffmpeg trae libvmaf:**

```bash
ffmpeg -filters | grep -i vmaf
```

Si no aparece, tienes ffmpeg "essentials". Baja la compilación "full" (en Windows, gyan.dev) o usa solo
SSIM, que siempre está.

### SSIM y PSNR (funciona siempre)

```bash
ffmpeg -i comprimido.mp4 -i original.mov -lavfi "ssim;[0:v][1:v]psnr" -f null -
```

Al final imprime algo así:

```
SSIM Y:0.982431 U:0.991204 V:0.990877 All:0.985612 (18.421dB)
PSNR y:42.31 u:47.02 v:46.88 average:43.55
```

El número que importa es **`All`** del SSIM: 0,9856 → excelente.

### VMAF

```bash
ffmpeg -i comprimido.mp4 -i original.mov \
  -lavfi "[0:v]setpts=PTS-STARTPTS[dist];[1:v]setpts=PTS-STARTPTS[ref];\
[dist][ref]libvmaf=log_path=vmaf.json:log_fmt=json" -f null -
```

Importante: **el primer `-i` es el archivo comprimido (el distorsionado) y el segundo es el original (la
referencia).** Si los inviertes el número sale mal y ni te enteras.

Y si las resoluciones no coinciden, hay que escalar la referencia a la del distorsionado:

```bash
ffmpeg -i comprimido_720.mp4 -i original_1080.mov \
  -lavfi "[0:v]scale=1920:1080:flags=bicubic,setpts=PTS-STARTPTS[dist];\
[1:v]scale=1920:1080:flags=bicubic,format=yuv420p,setpts=PTS-STARTPTS[ref];\
[dist][ref]libvmaf=n_threads=4:log_path=vmaf.json:log_fmt=json" -f null -
```

Leer el resultado:

```bash
grep -A3 '"vmaf"' vmaf.json | tail -20
# o, si tienes jq:
jq '.pooled_metrics.vmaf' vmaf.json
```

Lo que te interesa del JSON:

- **`mean`**: el promedio. Es el número que reportas.
- **`min`**: el peor fotograma. **Si el mínimo baja de 70, hay una escena que se rompió** aunque el
  promedio esté bonito. Siempre mira el mínimo.
- **`harmonic_mean`**: castiga más los momentos malos. Es más honesto que el promedio simple.

---

## El barrido de CRF: cómo encontrar TU punto óptimo

Esta es la técnica que separa a quien adivina de quien sabe. Coges un fragmento representativo de tu video
(30 segundos con la parte de más movimiento), lo exportas a varios CRF, mides cada uno, y **eliges el CRF
más alto que todavía te da VMAF ≥ 93**.

```bash
#!/bin/bash
# barrido-crf.sh — encuentra el CRF óptimo de un video
ORIG="$1"

# 1. Saca un fragmento representativo de 30 s (ajusta el -ss al momento con más movimiento)
ffmpeg -y -ss 00:00:20 -i "$ORIG" -t 30 -c:v prores_ks -profile:v 3 -c:a copy ref.mov

# 2. Codifica y mide cada CRF
for crf in 16 18 20 22 24 26 28; do
  ffmpeg -y -i ref.mov -c:v libx264 -crf $crf -preset slow \
    -pix_fmt yuv420p -an "test_crf$crf.mp4" -loglevel error

  size=$(du -m "test_crf$crf.mp4" | cut -f1)

  ffmpeg -i "test_crf$crf.mp4" -i ref.mov \
    -lavfi "[0:v]setpts=PTS-STARTPTS[d];[1:v]setpts=PTS-STARTPTS,format=yuv420p[r];\
[d][r]libvmaf=log_path=v$crf.json:log_fmt=json" -f null - -loglevel error

  vmaf=$(jq '.pooled_metrics.vmaf.mean' "v$crf.json")
  vmin=$(jq '.pooled_metrics.vmaf.min' "v$crf.json")

  echo "CRF $crf → VMAF medio $vmaf | mínimo $vmin | ${size} MB"
done
```

Un resultado típico se ve así:

| CRF | VMAF medio | VMAF mínimo | Peso |
|---|---|---|---|
| 16 | 98,2 | 94,1 | 88 MB |
| 18 | 97,1 | 92,4 | 62 MB |
| 20 | 95,4 | 89,8 | 44 MB |
| **22** | **93,6** | **86,2** | **31 MB** |
| 24 | 91,0 | 81,7 | 22 MB |
| 26 | 87,4 | 75,3 | 16 MB |
| 28 | 82,9 | 68,1 | 12 MB |

**Lectura:** CRF 22 es el punto óptimo. Comparado con CRF 16, **pesa un tercio y el espectador no ve la
diferencia**. Bajar a CRF 24 ya sacrifica calidad visible en las escenas difíciles (mínimo 81).

Ese ejercicio, hecho una vez por tipo de contenido, te sirve para siempre. **El CRF óptimo depende del
material, no del capricho:**

| Tipo de material | CRF x264 típico para VMAF ~94 |
|---|---|
| Cara hablando, fondo quieto | 22–24 |
| Producto sobre fondo liso | 21–23 |
| Exteriores con movimiento de cámara | 19–21 |
| Deporte, mucho movimiento rápido | 17–19 |
| Animación / gráficos planos | 20–22 |
| Material con grano o poca luz | 16–18 (el ruido cuesta carísimo) |

---

## La curva de rendimientos decrecientes

Este es el concepto que hay que entender de verdad:

```
Calidad percibida
   ^
100|                    ······················
   |              ·······
 90|          ····
   |        ··
 80|      ··
   |    ··
 70|  ··
   | ·
   +--------------------------------------> Bits gastados
     ↑           ↑                ↑
   barato    PUNTO ÓPTIMO      desperdicio
```

La curva sube rápido al principio y luego se aplana. **En la zona plana estás pagando megabytes por
calidad que nadie percibe.** El punto óptimo es donde la curva empieza a aplanarse: normalmente VMAF 93–95.

Dato concreto para que lo sientas: pasar de VMAF 93 a VMAF 98 típicamente **duplica el peso del archivo**
para una mejora que solo se ve poniendo los dos videos lado a lado, congelados, a pantalla completa.

---

## Trucos reales para bajar peso sin bajar calidad

### 1. Limpia el ruido antes de comprimir (el más grande)

El ruido es aleatorio, y lo aleatorio no se puede predecir, así que el codificador gasta muchísimos bits
en él. **Quitar el ruido antes de comprimir puede bajar el peso entre 20% y 40% con el mismo CRF.**

```bash
# hqdn3d: rápido, suficiente para la mayoría
ffmpeg -i entrada.mov -vf "hqdn3d=2:1.5:3:2.25" -c:v libx264 -crf 20 \
  -preset slow -pix_fmt yuv420p -c:a copy salida.mp4

# nlmeans: mucho mejor, mucho más lento
ffmpeg -i entrada.mov -vf "nlmeans=s=3:p=7:r=15" -c:v libx264 -crf 20 \
  -preset slow -pix_fmt yuv420p -c:a copy salida.mp4
```

Cuidado: pasarse de reducción de ruido convierte las caras en plástico. Mide con SSIM después.

### 2. Baja el preset, no el CRF

Si necesitas 15% menos peso, **no subas el CRF: baja el preset**. De `medium` a `slow` te da ~10% menos
peso con **cero** pérdida de calidad, solo más tiempo de máquina.

### 3. Ajusta el `-tune` al contenido

```bash
-tune film       # material de video normal, con grano
-tune animation  # dibujos, gráficos planos
-tune grain      # preserva el grano a propósito (sube el peso)
-tune stillimage # presentaciones, mucha imagen fija
```

### 4. Recorta la resolución si el destino es pequeño

Un video de 4K en un feed de celular se ve igual que uno de 1080p bien hecho. Bajar de 4K a 1080p corta el
peso **al 25%** con cero pérdida percibida en móvil.

```bash
ffmpeg -i 4k.mov -vf "scale=1920:-2:flags=lanczos" -c:v libx264 -crf 20 \
  -preset slow -pix_fmt yuv420p -c:a copy salida_1080.mp4
```

Usa `flags=lanczos` para reducir: es más nítido que el bicúbico por defecto.

### 5. El audio también pesa

En un video de 60 s, el audio a 320 kbps son 2,4 MB. A 128 kbps son 0,96 MB. **Para voz sola, 96–128 kbps
en AAC es transparente.** No gastes 320 en una persona hablando.

### 6. Recorta lo que sobra

El truco más subestimado: **10 segundos que no aportan pesan 10 segundos de bits**. Cortar es la
compresión más eficiente que existe y además mejora el video.

---

## Rutina completa de "comprimir bien"

```bash
# 1. Mira lo que tienes
ffprobe -v error -show_entries format=duration,size,bit_rate \
  -show_entries stream=codec_name,width,height,r_frame_rate \
  -of default=noprint_wrappers=1 master.mov

# 2. Limpia ruido si el material lo pide
ffmpeg -i master.mov -vf "hqdn3d=2:1.5:3:2.25" -c:v prores_ks -profile:v 3 \
  -c:a copy limpio.mov

# 3. Codifica en el CRF que el barrido determinó
ffmpeg -i limpio.mov -c:v libx264 -crf 22 -preset slow -profile:v high -level 4.1 \
  -pix_fmt yuv420p -g 60 -keyint_min 60 -c:a aac -b:a 128k -ar 48000 \
  -movflags +faststart final.mp4

# 4. Mide contra el original
ffmpeg -i final.mp4 -i master.mov \
  -lavfi "[0:v]setpts=PTS-STARTPTS[d];[1:v]setpts=PTS-STARTPTS,format=yuv420p[r];\
[d][r]libvmaf=log_path=vmaf.json:log_fmt=json" -f null -
jq '.pooled_metrics.vmaf' vmaf.json

# 5. Confirma peso y specs
ls -lh final.mp4
ffprobe -v error -show_entries format=duration,size,bit_rate -of default=nw=1 final.mp4
```

---

## Cuándo NO vale la pena medir

Seamos honestos: medir cuesta tiempo. **No midas** cuando:

- Es un borrador o revisión interna
- Es un reel de 20 s que va a redes (la plataforma lo va a recomprimir de todas formas y tu CRF importa
  poco por debajo de 20)
- Ya hiciste el barrido para ese tipo de material y estás repitiendo el mismo formato

**Sí mide** cuando:

- Es un máster de entrega a cliente
- Es un video largo donde el peso es dinero (hospedaje, ancho de banda)
- Estás decidiendo un preajuste que vas a usar 100 veces
- Alguien se quejó de la calidad y necesitas saber si es real o percepción

---

## Errores comunes

1. **Juzgar la calidad mirando el video en tu monitor.** Tu ojo se adapta y tu monitor no es el del
   público. Mide.
2. **Invertir el orden en el comando de VMAF.** El distorsionado va primero, la referencia segunda. Al
   revés te da un número que parece válido y no lo es.
3. **Mirar solo el VMAF promedio.** Un promedio de 94 con mínimo de 62 significa que hay una escena rota.
   Mira siempre el mínimo.
4. **Medir contra un archivo que ya estaba comprimido.** Si tu "referencia" es un H.264 de la cámara, estás
   midiendo contra algo imperfecto. La referencia debe ser el máster.
5. **Subir el CRF para ahorrar peso cuando podías bajar el preset.** El preset es peso gratis; el CRF es
   peso que cuesta calidad.
6. **Comprimir sin limpiar el ruido.** Estás pagando bits por granito aleatorio que además se ve peor.
7. **Pasarse con la reducción de ruido.** Caras de plástico, detalle borrado. Mide con SSIM: si baja de
   0,95 contra el original sin filtrar, te pasaste.
8. **Guardar 320 kbps de audio para una persona hablando.** Desperdicio puro.
9. **Reescalar con el filtro por defecto.** Para bajar resolución usa `lanczos`; para subir, `bicubic`. El
   por defecto (`bilinear`) es blando.
10. **Buscar VMAF 99.** Es imposible de percibir y te cuesta el doble de peso. 93–95 es la respuesta.
11. **Hacer el barrido sobre un fragmento fácil.** Si mides sobre 30 s de una persona quieta, el CRF que
    salga va a fallar en la escena de movimiento. Mide sobre lo más difícil.
12. **Comprimir un archivo ya comprimido en vez de volver al máster.** Doble pérdida, siempre.

---

## Checklist

Antes de dar por buena la compresión de un entregable:

- [ ] Estoy comprimiendo **desde el máster**, no desde una exportación anterior
- [ ] Si el material tiene ruido, ya lo limpié antes de codificar
- [ ] El CRF que usé viene de un **barrido medido**, no de una corazonada
- [ ] Medí **VMAF (o al menos SSIM)** contra el máster
- [ ] VMAF medio **≥ 93** y VMAF **mínimo ≥ 80**
- [ ] (o) SSIM `All` **≥ 0,96**
- [ ] Usé `-preset slow` antes de considerar subir el CRF
- [ ] El bitrate de audio es acorde: 96–128 kbps para voz, 192+ solo si la música protagoniza
- [ ] Si reescalé, usé `lanczos` para reducir
- [ ] El peso final entra en el límite de la plataforma de destino
- [ ] Miré el resultado en **un celular real**, no solo en el monitor de edición
- [ ] Guardé el CRF y los parámetros que funcionaron para no repetir el barrido la próxima vez
