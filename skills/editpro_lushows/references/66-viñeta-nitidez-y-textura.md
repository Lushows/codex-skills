# 66 — Viñeta, nitidez y textura

Estos son los últimos toques del color: van **después** de corregir, emparejar y graduar. No cambian
el color; cambian **cómo se siente la superficie de la imagen**. Y son los que más fácil se pasan de
dosis, porque cada uno solo se ve un poquito y uno tiende a subirle "para que se note".

Regla general del módulo: **si se nota, ya te pasaste.** Estos efectos trabajan por debajo del
umbral consciente. El espectador no debe pensar "qué buena viñeta"; debe pensar "qué bien se ve".

Orden dentro de la cadena:

```
… look/LUT → NITIDEZ → VIÑETA → GRANO → format=yuv420p → export
```

El grano va **de último** siempre. Si le aplicas nitidez al grano, lo multiplicas; si lo
desenfocas, lo matas.

---

## 1. Nitidez (`unsharp`, `cas`)

La nitidez no añade detalle. Lo que hace es **aumentar el contraste en los bordes** para que el ojo
lea la imagen como más definida. Por eso el exceso produce halos: una línea clara al lado de una
oscura, que es exactamente lo que se ve "de video barato".

### `unsharp` — el clásico

```
unsharp=luma_x:luma_y:luma_amount:chroma_x:chroma_y:chroma_amount
```

```bash
ffmpeg -i in.mp4 -vf "unsharp=5:5:0.5:5:5:0.0,format=yuv420p" -c:v libx264 -crf 18 out.mp4
```

| Parámetro | Qué es | Valores |
|---|---|---|
| `luma_x`, `luma_y` | tamaño de la matriz en luma | **impares**, 3–23. `5:5` es lo normal |
| `luma_amount` | fuerza en luma | −2 a 5. **Zona útil: 0.3 a 0.8** |
| `chroma_x`, `chroma_y` | tamaño en croma | `5:5` |
| `chroma_amount` | fuerza en croma | **déjalo en 0.0. Siempre.** |

**Por qué el croma va en 0.0:** el color en video está submuestreado (4:2:0, ver `60`). Afilar croma
solo hace visibles los bloques de color y ensucia los bordes. La nitidez percibida vive toda en el
luma. Este es probablemente el ajuste más importante del módulo.

Dosis según fuente:

| Material | `luma_amount` |
|---|---|
| Cámara buena, bien enfocado | `0.25 – 0.4` |
| Celular (ya viene con nitidez de fábrica) | `0.0 – 0.2` — casi siempre **nada** |
| Interior oscuro, imagen blanda | `0.4 – 0.6` |
| Después de escalar hacia arriba (1080 → 4K) | `0.5 – 0.7` |
| Imagen generada por IA | `0.0` — ya viene sobre-afilada |

Un tamaño mayor (`unsharp=9:9:0.4`) afila estructuras grandes y se ve más "orgánico"; un tamaño
pequeño (`unsharp=3:3:0.6`) afila detalle fino y se ve más "digital". Para caras, prefiere tamaño
grande y fuerza baja.

### `cas` — la opción moderna

`cas` (Contrast Adaptive Sharpening) afila más donde hace falta y menos donde ya hay detalle. Menos
halos, resultado más natural:

```bash
ffmpeg -i in.mp4 -vf "cas=strength=0.35,format=yuv420p" -c:v libx264 -crf 18 out.mp4
```

`strength` va de 0 a 1. Zona útil: **0.2 – 0.45**. Si tu compilación lo trae, es mejor que
`unsharp` para material de cámara. Compruébalo:

```bash
ffmpeg -hide_banner -filters | grep -E "^ .. (cas|unsharp|smartblur|noise|vignette|deband) "
```

### Suavizar en vez de afilar

A veces el problema es el contrario: la imagen está demasiado dura (celular + luz fuerte) y la piel
se ve texturada de más. `smartblur` suaviza **las zonas planas** y respeta los bordes:

```bash
# lt positivo = filtra zonas planas (piel, paredes) y deja los bordes definidos
ffmpeg -i in.mp4 -vf "smartblur=lr=2:ls=0.5:lt=20,format=yuv420p" -c:v libx264 -crf 18 out.mp4
```

`ls` (fuerza) entre 0.3 y 0.7. Por encima de 0.8 la cara queda de plástico y se nota muchísimo. Es
mucho mejor una piel con textura real que una piel de muñeco.

---

## 2. Viñeta (`vignette`)

La viñeta oscurece las esquinas. Hace dos cosas: **dirige la mirada al centro** y **disimula
desniveles de iluminación** en los bordes del cuadro (que en interiores son constantes).

```bash
ffmpeg -i in.mp4 -vf "vignette=PI/5,format=yuv420p" -c:v libx264 -crf 18 out.mp4
```

El parámetro es el ángulo, de 0 a PI/2. **A mayor ángulo, más viñeta:**

| Valor | Intensidad | Cuándo |
|---|---|---|
| `PI/6` (≈0.52) | apenas perceptible | testimonios, corporativo |
| **`PI/5` (≈0.63)** | **discreta — el valor de trabajo** | **casi todo** |
| `PI/4` (≈0.79) | claramente visible | dramático, noche, música |
| `PI/3` (≈1.05) | pesada | casi siempre demasiado |

`PI/5` es el que se usó en el emparejado del bar del módulo `62`, y es el que deberías usar por
defecto.

Opciones útiles:

```bash
# Viñeta desplazada (cuando el sujeto no está al centro)
ffmpeg -i in.mp4 -vf "vignette=a=PI/5:x0=w*0.38:y0=h*0.45:eval=init" out.mp4

# Viñeta invertida: oscurece el centro, aclara los bordes (raro, pero existe)
ffmpeg -i in.mp4 -vf "vignette=a=PI/5:mode=backward" out.mp4
```

**Advertencia importante para vertical:** en 9:16 la viñeta se concentra arriba y abajo, que es
justo donde va el texto y donde está la cara en un plano medio. En vertical baja la dosis a `PI/6` o
desplaza el centro hacia arriba con `y0=h*0.42`.

Y una advertencia de compresión: la viñeta crea un degradado suave y oscuro en las esquinas, que es
**exactamente** el tipo de zona que se bandea al recomprimir (ver `68`). Si vas a publicar en
Instagram o WhatsApp, la viñeta discreta + grano es la combinación que sobrevive; la viñeta fuerte
sola se convierte en anillos.

---

## 3. Grano (`noise`)

El grano es el toque más subestimado. Hace **tres** cosas a la vez:

1. **Textura de película.** La imagen digital limpia se lee como "video"; el grano la lee como
   "cine".
2. **Esconde el banding.** Es la razón técnica más fuerte. El ruido rompe los escalones de los
   degradados y el ojo los reconstruye como un degradado continuo.
3. **Une material de fuentes distintas.** Cámara + celular + IA bajo el mismo grano se sienten del
   mismo video. Sin grano, el plano de IA siempre se ve "demasiado limpio".

```bash
ffmpeg -i in.mp4 -vf "noise=alls=7:allf=t+u,format=yuv420p" -c:v libx264 -crf 17 out.mp4
```

| Parámetro | Significado |
|---|---|
| `alls=N` | intensidad, 0–100. **Zona útil: 4 – 12** |
| `allf=t` | **temporal**: el grano cambia en cada fotograma |
| `allf=u` | uniforme (más parecido al grano fotoquímico que el gaussiano por defecto) |
| `allf=p` | patrón fijo — **no lo uses**, se ve como suciedad en el lente |

**La `t` no es opcional.** Sin ella el grano queda quieto pegado a la imagen y el efecto es
horrible: parece que la lente está sucia o que hay un sticker encima. Es el error más común con este
filtro.

Dosis:

| Intensidad | `alls` | Efecto |
|---|---|---|
| Higiénica (solo anti-banding) | `4 – 5` | invisible, pero salva los degradados |
| Cinematográfica | `6 – 9` | se siente, no se ve |
| De carácter | `10 – 14` | visible, decisión estética |
| Efecto | `18+` | look de archivo / VHS (ver `57`) |

### El costo en bitrate (esto sí importa)

El grano es ruido, y el ruido es lo que peor comprime un códec. Si exportas con el mismo CRF de
siempre, el compresor gasta todo su presupuesto en el grano y te devuelve **bloques** en las zonas
importantes.

Regla: **con grano, baja el CRF entre 1 y 2 puntos.**

| Sin grano | Con grano |
|---|---|
| CRF 23 | CRF 21 |
| CRF 20 | CRF 18 |
| CRF 18 | CRF 17 |

También ayuda `-tune film` o `-tune grain` en libx264. `grain` preserva más el ruido a costa de
archivo más pesado:

```bash
ffmpeg -i in.mp4 -vf "noise=alls=8:allf=t+u,format=yuv420p" \
  -c:v libx264 -crf 17 -preset slow -tune grain -movflags +faststart out.mp4
```

### Grano solo en luma (más elegante)

El grano en croma se ve como confeti de colores. Para grano solo en el brillo:

```bash
ffmpeg -i in.mp4 -vf "noise=c0s=8:c0f=t+u,format=yuv420p" -c:v libx264 -crf 17 out.mp4
```

`c0` es el primer plano (luma en YUV). `c1` y `c2` son los de croma. Este es el grano "bueno".

---

## 4. Banding: el enemigo silencioso

El banding son los escalones visibles en un degradado (un cielo, una pared iluminada, un fondo con
gradiente, el propio efecto de viñeta). Aparece porque el video de 8 bits solo tiene 256 niveles por
canal, y la compresión se come varios.

Herramientas, de menos a más agresivas:

```bash
# 1) Grano: la solución más elegante y la primera que hay que probar
ffmpeg -i in.mp4 -vf "noise=c0s=5:c0f=t+u,format=yuv420p" -c:v libx264 -crf 18 out.mp4

# 2) deband: detecta bandas y las suaviza
ffmpeg -i in.mp4 -vf "deband=1thr=0.02:2thr=0.02:3thr=0.02:4thr=0.02:range=16:blur=1,format=yuv420p" \
  -c:v libx264 -crf 18 out.mp4

# 3) gradfun: el clásico, más suave
ffmpeg -i in.mp4 -vf "gradfun=strength=1.2:radius=16,format=yuv420p" -c:v libx264 -crf 18 out.mp4

# 4) La combinación que mejor funciona en la práctica
ffmpeg -i in.mp4 -vf "gradfun=1.2:16,noise=c0s=5:c0f=t+u,format=yuv420p" \
  -c:v libx264 -crf 17 out.mp4
```

Ojo: `deband` y `gradfun` **desenfocan** un poquito. Van antes del grano y después de la nitidez.

Cómo detectar banding sin ojo entrenado: exporta un frame de la zona sospechosa y estíralo:

```bash
ffmpeg -y -ss 5 -i out.mp4 -frames:v 1 -vf "crop=400:400:300:200,scale=1200:1200:flags=neighbor,eq=contrast=2.5" \
  banding_test.png
```

Si en esa imagen ves franjas planas claramente separadas, tienes banding.

---

## 5. El estabilizado, brevemente (vive en `59`)

Se menciona aquí porque va en la misma zona de la cadena y porque **recorta la imagen**, lo cual
cambia el encuadre y por tanto la viñeta. Si vas a estabilizar, hazlo **antes** de la viñeta,
siempre. Detalle completo en `59-estabilizacion.md`.

---

## 6. La cadena de acabado completa

Sobre material ya corregido, emparejado y graduado:

```bash
ffmpeg -i graduado/plano.mp4 -vf "\
cas=strength=0.30,\
gradfun=1.0:16,\
vignette=PI/5,\
noise=c0s=6:c0f=t+u,\
format=yuv420p" \
  -c:v libx264 -crf 17 -preset slow -tune grain \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -movflags +faststart -c:a copy final/plano.mp4
```

Y si no tienes `cas`:

```bash
… -vf "unsharp=5:5:0.4:5:5:0.0,gradfun=1.0:16,vignette=PI/5,noise=c0s=6:c0f=t+u,format=yuv420p" …
```

---

## Errores comunes

- **Grano sin `t` (temporal).** Queda estático y parece mugre en el lente. El peor error del módulo.
- **`chroma_amount` distinto de 0.0 en `unsharp`.** Ensucia los bordes de color por el 4:2:0.
- **Afilar material de celular.** Ya viene afilado de fábrica; le pones halos encima.
- **Afilar material generado por IA.** Idem, ya viene sobre-afilado. Lo que necesita es **grano**,
  no nitidez.
- **Viñeta `PI/3` o más.** Grita amateur. `PI/5` y ya.
- **Viñeta fuerte en vertical.** Se come la cara y el texto. Baja la dosis o desplaza el centro.
- **Grano con el mismo CRF de siempre.** Bloques garantizados. Baja el CRF 1–2 puntos.
- **Poner el grano antes de la nitidez.** Afilas el ruido y queda un mosaico.
- **Suavizar la piel con `ls` alto.** Cara de plástico. Máximo 0.7 y con `lt` positivo.
- **Meter `deband`/`gradfun` en todo el video sin necesidad.** Desenfocan; úsalos solo si hay
  banding real, medido.
- **Poner viñeta antes de estabilizar o recortar.** El recorte se lleva parte de la viñeta y queda
  descentrada.
- **Aplicar el acabado plano por plano con dosis distintas.** El acabado es del video entero, igual
  para todos.

---

## Checklist

- [ ] El material ya está corregido, emparejado y graduado antes de tocar este módulo.
- [ ] Comprobé qué filtros trae mi ffmpeg (`cas`, `smartblur`, `deband`, `noise`).
- [ ] `unsharp` tiene `chroma_amount=0.0`. Sin excepción.
- [ ] La fuerza de nitidez está en 0.3–0.6 (o `cas` en 0.2–0.45), y es 0 si el material es de
      celular o de IA.
- [ ] La viñeta es `PI/5` o menos, y bajé la dosis si el formato es vertical.
- [ ] El grano tiene `f=t` (temporal) y está entre 4 y 12.
- [ ] Preferí grano solo en luma (`c0s`) sobre grano en todos los canales.
- [ ] Bajé el CRF 1–2 puntos por el grano, y consideré `-tune grain`.
- [ ] Revisé banding en la zona más sospechosa con el test de recorte + escalado + contraste.
- [ ] El orden de la cadena es: nitidez → deband → viñeta → grano → `format=yuv420p`.
- [ ] El acabado es idéntico en todos los planos del video.
- [ ] Comparé el antes y el después lado a lado y la diferencia es sutil, no obvia.
