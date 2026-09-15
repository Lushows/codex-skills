# 22 — Punch-in y reencuadre

**Qué resuelve:** grabaste con una sola cámara, una sola toma, y el video se siente plano y lento. No vas
a volver a grabar. El punch-in te da una **segunda cámara gratis** a partir del material que ya tienes.
Es el recurso más barato que existe en edición y el que más rápido sube el pulso de un video.

---

## 1. Qué es un punch-in

> **Término nuevo — punch-in:** volver al mismo plano pero **más cerrado**, como si hubiera una segunda
> cámara más cerca. Se logra escalando la imagen y recortándola al tamaño original. No es un zoom en
> movimiento: es un corte a un encuadre distinto.

Visualmente el espectador lee: "cambió la cámara". Técnicamente: es el mismo archivo, escalado y
recortado.

Ejemplo con vertical 1080x1920:

```
Plano original:   1080 x 1920  (encuadre normal)
Punch-in 15%:     escalas a 1242x2208 y recortas 1080x1920 del centro
Resultado:        el sujeto se ve 15% más grande. Se lee como otra cámara.
```

**No confundir con:**
- **Zoom digital en movimiento** (el marco se acerca mientras corre el video). Eso es otra cosa y suele
  verse barato. El punch-in es un **corte**, no un movimiento.
- **Reencuadre** (mover el marco de lado sin acercar). También sirve, y lo vemos en la sección 6.

---

## 2. La matemática del recorte

Esta es la parte que hay que entender bien, porque de aquí sale si el video queda nítido o se ve
pixelado.

### La fórmula

```
factor de acercamiento = F   (ejemplo: 1,15 = 15% más cerca)
ancho escalado  = ancho_final  × F
alto escalado   = alto_final   × F
```

Para vertical 1080x1920 con F = 1,15:

```
1080 × 1,15 = 1242
1920 × 1,15 = 2208
```

Entonces: `scale=1242:2208` y después `crop=1080:1920`.

### Tabla lista para copiar (vertical 1080x1920)

| Acercamiento | scale | Se lee como | Uso |
|---|---|---|---|
| 8% | `1166:2074` | Casi imperceptible | Tapar un jump cut mínimo |
| **15%** | **`1242:2208`** | **Otra cámara** | **El estándar. Usa este.** |
| 25% | `1350:2400` | Un plano más cerrado, notorio | Momento de énfasis |
| 40% | `1512:2688` | Primer plano | Solo si la fuente es 4K |
| 60% | `1728:3072` | Detalle | Solo con fuente 4K, y con cuidado |

### Tabla para horizontal 1920x1080

| Acercamiento | scale |
|---|---|
| 15% | `2208:1242` |
| 25% | `2400:1350` |
| 40% | `2688:1512` |

### La regla de la resolución (esta es la importante)

Cuando escalas hacia arriba, estás **inventando píxeles**. Si tu fuente es exactamente 1080x1920 y
escalas 40%, se nota: los bordes se ablandan y el texto de fondo se vuelve papilla.

```
Resolución mínima de la fuente = resolución final × factor
```

| Fuente grabada | Punch-in máximo sin que se note |
|---|---|
| 1080x1920 (Full HD vertical) | **15%**, forzando 20% |
| 2160x3840 (4K vertical) | **60–80%** sin problema |
| 1440x2560 (2.5K) | ~35% |

**Consecuencia práctica:** graba en 4K aunque publiques en 1080. No es por calidad de imagen — es por
**libertad de punch-in en post**. Esta es la razón número uno para grabar en 4K con el celular.

Cómo saber qué tienes:

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate,codec_name \
  -of default=noprint_wrappers=1 entrada.mp4
```

---

## 3. Los comandos

### Punch-in básico (centrado)

```bash
ffmpeg -hide_banner -i plano.mp4 \
  -vf "scale=1242:2208:flags=lanczos,crop=1080:1920" \
  -c:v libx264 -crf 18 -preset slow -c:a copy plano_punch15.mp4
```

`flags=lanczos` es importante: es el algoritmo de escalado que mejor conserva el detalle al agrandar.
El de por defecto (`bicubic`) ablanda más. Es gratis, úsalo siempre que escales.

### Punch-in con la cara descentrada (lo normal)

El sujeto casi nunca está justo en el centro. `crop` acepta coordenadas `x` e `y` desde la esquina
superior izquierda:

```bash
# Recorte desplazado 60 px a la derecha y 120 px hacia arriba respecto del centro
ffmpeg -hide_banner -i plano.mp4 \
  -vf "scale=1242:2208:flags=lanczos,crop=1080:1920:(in_w-1080)/2+60:(in_h-1920)/2-120" \
  -c:v libx264 -crf 18 -preset slow -c:a copy plano_punch15_ajustado.mp4
```

`(in_w-1080)/2` es el centro; le sumas o le restas para mover el marco. Trabaja en múltiplos de 20 px
hasta que la cabeza quede bien.

### Ver el encuadre antes de renderizar todo el clip

No renderices tres minutos para descubrir que le cortaste la frente:

```bash
ffmpeg -hide_banner -ss 2 -i plano.mp4 \
  -vf "scale=1242:2208:flags=lanczos,crop=1080:1920:(in_w-1080)/2+60:(in_h-1920)/2-120" \
  -frames:v 1 prueba_encuadre.png
```

Un solo fotograma, medio segundo de render. Míralo, ajusta, repite.

### Generar los tres encuadres de una vez

Cuando vas a montar un bloque entero, precocina las tres versiones y montas con ellas:

```bash
for F in "1080:1920" "1242:2208" "1350:2400"; do
  W=${F%:*}; H=${F#*:}
  ffmpeg -hide_banner -y -i plano.mp4 \
    -vf "scale=${W}:${H}:flags=lanczos,crop=1080:1920" \
    -c:v libx264 -crf 18 -preset slow -an "enc_${W}.mp4"
done
```

Te quedan `enc_1080.mp4` (normal), `enc_1242.mp4` (+15%) y `enc_1350.mp4` (+25%). Ahora tienes tres
cámaras de una sola toma.

---

## 4. Cómo se usa en el montaje

### El patrón de tres cámaras

La estructura que funciona para un talking head de 30–60 segundos:

```
0,0 – 2,0 s    NORMAL   (establece: dónde está, quién es)
2,0 – 4,0 s    +15%     (entramos: la frase importante)
4,0 – 5,5 s    INSERTO  (el producto, las manos, lo que sea)
5,5 – 7,5 s    NORMAL   (salimos: respiro)
7,5 – 9,0 s    +25%     (énfasis fuerte: el dato o el precio)
9,0 – 11,0 s   NORMAL
```

Seis cambios visuales en 11 segundos = pulso de 1,8 s. Objetivo cumplido, y solo se grabó **una toma**.

### Dónde va cada acercamiento

| Momento del guion | Encuadre |
|---|---|
| Presentación, contexto, "dónde estamos" | **Normal** |
| Argumento, explicación | **+15%** |
| El dato, el precio, la frase que vende | **+25%** |
| Chiste, aparte, cambio de tono | **Normal** (salir de golpe también es un recurso) |
| Llamado a la acción final | **+15%** o normal, nunca el más cerrado |

**Regla de oro del punch-in:** **más cerca = más importante.** Si acercas donde no pasa nada, gastaste
el recurso. Cuando de verdad llegue la frase clave, ya no te queda nada más cerrado que ofrecer.

### La regla del 20%

Si dos planos difieren en menos del **8%** de tamaño, el ojo no lo lee como cambio de cámara: lo lee como
un error, un salto raro. Si difieren más del 50% de golpe, se siente violento.

**La ventana buena está entre 12% y 30% de diferencia entre planos consecutivos.**

---

## 5. Cuándo se nota mal (la lista honesta)

El punch-in falla en estos casos, y hay que saberlo antes de entregar:

### a) Fuente insuficiente

Escalar 40% desde 1080p produce bordes blandos. Se nota especialmente en:
- El **texto de fondo** (un letrero, una pantalla).
- El **pelo** y las **pestañas** — se convierten en una mancha.
- Los **bordes de alto contraste** — aparece un halo.

**Cómo verificarlo:** compara un fotograma del normal contra uno del punch-in, ampliados al 200%.

```bash
ffmpeg -hide_banner -ss 3 -i enc_1080.mp4 -frames:v 1 -vf "crop=400:400" a.png
ffmpeg -hide_banner -ss 3 -i enc_1350.mp4 -frames:v 1 -vf "crop=400:400" b.png
```

Si `b.png` se ve claramente más blando, bajaste demasiado la calidad. Reduce el factor.

### b) Cámara movida

Si el plano original tiene temblor de mano, el punch-in **amplifica el temblor** proporcionalmente. Un
temblor apenas perceptible al 100% se vuelve mareante al 140%.

Solución: estabilizar **antes** de hacer el punch-in (módulo `59`), o no acercar tanto.

```bash
# Paso 1: analizar el movimiento
ffmpeg -hide_banner -i plano.mp4 -vf vidstabdetect=shakiness=5:accuracy=15 -f null -
# Paso 2: estabilizar y hacer punch-in en la misma pasada
ffmpeg -hide_banner -i plano.mp4 \
  -vf "vidstabtransform=smoothing=20,scale=1242:2208:flags=lanczos,crop=1080:1920" \
  -c:v libx264 -crf 18 -c:a copy plano_estable_punch.mp4
```

Ojo: `vidstabtransform` ya recorta un poco por su cuenta para compensar el movimiento. Eso se suma a tu
punch-in. Verifica el encuadre final.

### c) Cortarle la cabeza a alguien

El error clásico. Al acercar, la coronilla sale del cuadro y queda un encuadre incómodo. **Siempre**
revisa el fotograma antes de renderizar (comando de la sección 3).

Regla de encuadre: en vertical, deja **entre 5% y 10% del alto** de aire sobre la cabeza. Ni pegado al
borde, ni con medio cuadro vacío arriba.

### d) Punch-in sobre punch-in

Si ya cortaste el video una vez y le haces punch-in al resultado, estás escalando material ya escalado.
La pérdida se acumula. **Siempre parte del material original**, no del render intermedio.

### e) Usarlo demasiado

Cinco punch-ins seguidos al mismo encuadre dejan de leerse como cámara y empiezan a leerse como tic.
Alterna: normal → cerrado → inserto → normal. La variedad importa más que la cantidad (módulo `20`).

### f) Aspecto distinto

Si escalas sin respetar la proporción, la gente sale estirada o achatada. **Escala siempre con el mismo
factor en ancho y alto.** Si necesitas cambiar de proporción (16:9 a 9:16), eso es reencuadre de formato
y va en el módulo `38`.

---

## 6. Reencuadre lateral: la cuarta cámara

Además de acercar, puedes **mover el marco** sin cambiar el tamaño. Si grabaste en 4K vertical y publicas
en 1080, tienes espacio de sobra para moverte:

```bash
# De 4K vertical, recortar 1080x1920 desplazado a la derecha
ffmpeg -hide_banner -i plano4k.mp4 \
  -vf "scale=2160:3840:flags=lanczos,crop=1080:1920:1400:1200" \
  -c:v libx264 -crf 18 -c:a copy plano_lateral.mp4
```

Esto te da un plano donde el sujeto está descentrado — perfecto para dejar espacio a un texto o a un
gráfico al otro lado. Es la técnica que hace que un talking head se sienta diseñado y no grabado.

**Combinación que funciona muy bien en vertical:**

```
Plano A: sujeto centrado, sin texto
Plano B: sujeto desplazado a la derecha + texto grande a la izquierda
Plano C: punch-in centrado
```

Tres encuadres, una toma, y el video parece producido.

---

## 7. Cuánto punch-in necesita un video

Regla práctica por duración:

| Duración | Encuadres distintos que deberías tener |
|---|---|
| 15 s | 2 (normal + 15%) |
| 30 s | 3 (normal + 15% + inserto) |
| 60 s | 4 (normal + 15% + 25% + reencuadre lateral) |
| 3 min | 4 encuadres + b-roll real. Solo punch-ins no aguanta 3 minutos. |

Por encima de los 90 segundos el punch-in deja de ser suficiente. Ahí necesitas material de verdad
(módulo `174`). El punch-in salva un reel; no salva un documental.

---

## Errores comunes

1. **Escalar sin `flags=lanczos`.** El escalado por defecto ablanda de más. Es una palabra que no cuesta
   nada y se nota en el resultado.
2. **Hacer punch-in de 40% desde material 1080p.** Se ve pixelado y el cliente sí lo nota, aunque no
   sepa nombrarlo. Con 1080 de fuente, el techo real es 15–20%.
3. **No revisar el encuadre antes de renderizar.** Renderizas tres minutos y descubres que le cortaste
   la frente. Un fotograma de prueba cuesta medio segundo.
4. **Acercar donde no pasa nada.** El punch-in es énfasis. Si lo gastas en el saludo, cuando llegue el
   precio no te queda a dónde ir.
5. **Punch-in sobre un plano movido sin estabilizar.** Amplificas el temblor proporcionalmente. Se ve
   peor que el plano original.
6. **Acercar solo 5%.** No se lee como cambio de cámara, se lee como un salto de reproducción. Por
   debajo del 8% no vale la pena.
7. **Partir del render intermedio en vez del original.** Escalar lo ya escalado acumula pérdida. Siempre
   desde el máster.
8. **Estirar la imagen** al escalar distinto en ancho y alto. La persona sale deformada y es un error
   que se ve a un metro de distancia.
9. **Usar zoom en movimiento en vez de punch-in por corte.** El zoom digital lento es el efecto que más
   grita "editado en la app del celular". El punch-in por corte se lee como producción.
10. **Grabar en 1080 pudiendo grabar en 4K.** No es por el detalle final: es por la libertad de recortar
    en post. Es la decisión de rodaje que más impacta la edición.

---

## Checklist

- [ ] Verifiqué la **resolución real de la fuente** con `ffprobe` antes de decidir el factor.
- [ ] El factor de punch-in **respeta el techo** de la fuente (15–20% si es 1080p, hasta 60% si es 4K).
- [ ] Escalé con **`flags=lanczos`**.
- [ ] Escalé con **el mismo factor en ancho y alto** — nadie sale estirado.
- [ ] Revisé un **fotograma de prueba** del encuadre antes de renderizar el clip completo.
- [ ] Hay **entre 5% y 10% de aire** sobre la cabeza en todos los encuadres.
- [ ] La diferencia entre encuadres consecutivos está **entre 12% y 30%**.
- [ ] El encuadre **más cerrado** cae sobre la frase **más importante** del guion, no sobre el saludo.
- [ ] Si el plano tenía temblor, **estabilicé antes** de acercar.
- [ ] Todos los encuadres salen del **material original**, no de un render intermedio.
- [ ] No hay más de dos punch-ins seguidos sin un plano normal o un inserto en medio.
- [ ] Comparé un recorte al 200% del normal contra el punch-in y **no hay pérdida visible**.
