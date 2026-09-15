# 57 — Glitch y textura: grano, VHS, halftone, tramado

> El módulo anterior (`56`) mete el glitch en la lista negra. Este explica cómo hacerlo bien, porque
> la textura sí es una herramienta legítima — de hecho es una de las pocas que separa el video que
> parece "salido de una cámara" del video que parece "una pieza".

---

## Por qué la textura suma

El video digital limpio es **demasiado limpio**. Sensor perfecto, gradiente perfecto, cero grano. El
ojo, acostumbrado a un siglo de cine con emulsión, lee esa perfección como plástico.

La textura hace tres cosas concretas:

1. **Une planos.** Dos clips grabados con cámaras distintas se sienten hermanos cuando comparten grano.
   Es el truco de emparejado más barato que existe. Ver `62-emparejar-planos.md`.
2. **Esconde defectos de compresión.** El grano rompe el "bandeado" — esas franjas escalonadas que
   salen en cielos y paredes lisas cuando el bitrate no alcanza.
3. **Fecha la imagen.** Grano fino = cine. Ruido de croma + desplazamiento de color = analógico.
   Trama de puntos = impreso. Pixelado = digital antiguo. Cada textura es una época.

Y una advertencia previa: **la textura se aplica al final, sobre el corte terminado**. Nunca sobre
los clips individuales, porque si cada clip tiene su propio grano, el grano cambia en cada corte y
se nota horrible. El grano debe ser continuo a lo largo de toda la pieza.

---

## 1. Grano de película (el que casi siempre vale la pena)

Es el más útil y el menos arriesgado. El filtro es `noise`.

```bash
ffmpeg -y -i corte.mp4 \
  -vf "noise=alls=12:allf=t+u,curves=preset=lighter,eq=saturation=0.9" \
  -c:v libx264 -crf 20 -preset slow -pix_fmt yuv420p con_grano.mp4
```

Verificado y funciona. Qué hace cada parte:

| Parámetro | Qué significa |
|---|---|
| `alls=12` | Intensidad del grano (0–100). **El número que hay que calibrar.** |
| `allf=t` | El grano es **temporal**: cambia en cada fotograma. Obligatorio. |
| `allf=u` | El ruido es **uniforme** en vez de gaussiano. Se ve más a emulsión. |

### Las dosis reales

| `alls` | Resultado |
|---|---|
| 4 – 8 | Casi imperceptible. Rompe el bandeado sin que nadie lo note. **El que se usa en casi todo.** |
| 10 – 16 | Grano visible pero elegante. Look de cine digital. |
| 20 – 30 | Grano marcado, estética de película fotoquímica o de época. |
| 40+ | Ya es ruido, no grano. Se ve a error, no a intención. |

**Regla:** si el cliente nota el grano sin que se lo digas, es demasiado.

### El error que arruina el grano

`allf=t` **no es opcional**. Sin la `t`, el grano es el mismo patrón fijo en todos los fotogramas, y
un patrón fijo se lee como suciedad en el lente, no como grano. Es la diferencia entre "textura" y
"video sucio".

### Grano solo en la luminancia (más fino)

El grano de película real está sobre todo en el brillo, no en el color. Para acercarse:

```bash
ffmpeg -y -i corte.mp4 \
  -vf "noise=c0s=14:c0f=t+u:c1s=3:c1f=t:c2s=3:c2f=t" \
  -c:v libx264 -crf 20 -preset slow -pix_fmt yuv420p grano_fino.mp4
```

`c0` es luminancia, `c1` y `c2` son los canales de color. Grano fuerte en luma, casi nada en croma.
Se ve notablemente más caro que `alls`.

### Ojo con el bitrate

El grano es **ruido**, y el ruido es lo más caro de comprimir. Un video con grano al mismo CRF pesa
un 30–60% más. Si lo vas a subir a una red que recomprime, o bajas el grano o subes el bitrate. Ver
`93-compresion-sin-perder-calidad.md`.

---

## 2. VHS / analógico

Esta es la que más se hace mal. Un VHS de verdad no es "un filtro morado": es una suma de defectos
concretos que se pueden reproducir uno por uno.

### Los defectos reales del VHS

| Defecto real | Filtro que lo reproduce |
|---|---|
| El color se desplaza respecto al brillo | `chromashift` |
| Resolución de color bajísima | `scale` a resolución baja y de vuelta |
| Ruido de croma | `noise` |
| Contraste aplastado, negros levantados | `curves` |
| Nitidez pobre | `scale` con `flags=neighbor` o `unsharp` negativo |

### El comando (verificado)

```bash
ffmpeg -y -i corte.mp4 \
  -vf "chromashift=cbh=4:crh=-4,\
noise=alls=8:allf=t,\
curves=preset=vintage,\
scale=iw/3:ih/3:flags=neighbor,scale=iw*3:ih*3:flags=neighbor" \
  -c:v libx264 -crf 20 -preset veryfast -pix_fmt yuv420p vhs.mp4
```

Nota: el doble `scale` (bajar y subir con `flags=neighbor`) es lo que mata la resolución sin
suavizarla. Si usas el escalado normal, queda borroso en vez de degradado, y borroso no es VHS.

`chromashift=cbh=4:crh=-4` desplaza los dos canales de color en direcciones opuestas: 2–3 es sutil,
6–8 ya es muy marcado.

### El VHS necesita audio degradado

Un VHS visualmente perfecto con audio en estéreo cristalino es una contradicción. Baja el audio a mono
y córtale los agudos:

```bash
ffmpeg -y -i vhs.mp4 -af "pan=mono|c0=0.5*c0+0.5*c1,lowpass=f=7000,highpass=f=120" \
  -c:v copy -c:a aac vhs_completo.mp4
```

**Esto vale para todas las texturas de este módulo:** la textura visual sin coherencia sonora se
lee a filtro. Con audio coherente se lee a formato.

---

## 3. Halftone (trama de puntos, estética impresa)

Es la trama de puntos de los periódicos e impresos antiguos. Muy potente para marcas con lenguaje
editorial o retro-gráfico.

```bash
ffmpeg -y -i corte.mp4 \
  -vf "format=gray,geq=lum='if(lt(hypot(mod(X,6)-3,mod(Y,6)-3), 3*(1-lum(6*floor(X/6)+3,6*floor(Y/6)+3)/255)), 0, 255)'" \
  -c:v libx264 -crf 20 -preset veryfast -pix_fmt yuv420p halftone.mp4
```

Verificado. Cómo funciona, en simple: divide la imagen en casillas de 6×6 píxeles. En cada casilla
dibuja un círculo cuyo tamaño depende de qué tan oscura es la imagen en el centro de esa casilla.
Zonas oscuras = puntos grandes. Zonas claras = puntos chiquitos.

- Cambia los `6` por `4` para trama fina, o por `10` para trama gruesa. Los cuatro `6` tienen que
  cambiar juntos, y el `3` es la mitad del tamaño de casilla.

### La advertencia de velocidad

`geq` evalúa una expresión **por cada píxel y cada fotograma**. En 1080×1920 a 30 fps eso son 62
millones de evaluaciones por segundo de video. Es lento.

Estrategias:
1. Aplícalo solo al tramo que lo necesita, no al video completo.
2. Baja la resolución antes de aplicarlo y súbela después (además queda mejor: la trama debe verse
   gruesa).

```bash
ffmpeg -y -i corte.mp4 -vf \
"scale=540:-2,format=gray,\
geq=lum='if(lt(hypot(mod(X,6)-3,mod(Y,6)-3), 3*(1-lum(6*floor(X/6)+3,6*floor(Y/6)+3)/255)), 0, 255)',\
scale=1080:-2:flags=neighbor" \
  -c:v libx264 -crf 20 -preset veryfast -pix_fmt yuv420p halftone_rapido.mp4
```

### Halftone en color de marca

El halftone sale en blanco y negro. Para teñirlo con los colores del cliente, se pasa por duotono
(ver `64-forzar-la-paleta-de-marca.md`):

```bash
ffmpeg -y -i halftone.mp4 -vf "lutrgb=r='val*0.88':g='val*0.03':b='val*0.00'" \
  -c:v libx264 -crf 20 -preset veryfast -pix_fmt yuv420p halftone_marca.mp4
```

---

## 4. Tramado / pixelado (estética digital antigua)

### Pixelado limpio

```bash
ffmpeg -y -i corte.mp4 -vf "pixelize=w=8:h=8" \
  -c:v libx264 -crf 20 -preset veryfast -pix_fmt yuv420p pixelado.mp4
```

Verificado. Es más rápido y más limpio que hacerlo con doble `scale`. Sirve para censurar, para
estética de videojuego, o para el momento antes de un revelado.

### Tramado tipo Bayer (blanco y negro con patrón)

```bash
ffmpeg -y -i corte.mp4 -vf \
"format=gray,geq=lum='255*gt(lum(X,Y)+(mod(X,4)*16+mod(Y,4)*16)/2, 200)'" \
  -c:v libx264 -crf 20 -preset veryfast -pix_fmt yuv420p tramado.mp4
```

Verificado. Convierte a blanco y negro puro con una trama que simula grises. Es la estética de las
pantallas de un bit, del fax, del riso. Muy fuerte; úsala como acento de 1–2 segundos, no como look
del video.

---

## 5. El glitch bien hecho

Aquí está la diferencia con la lista negra de `56`. Un glitch correcto tiene tres propiedades:
**dura 2–3 fotogramas, es irregular, y suena.**

### Separación de canales de color (RGB split)

```bash
ffmpeg -y -i corte.mp4 \
  -vf "rgbashift=rh=6:bh=-6:enable='between(t,0.5,0.6)'" \
  -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p glitch1.mp4
```

Verificado. `between(t,0.5,0.6)` = tres fotogramas a 30 fps. Ese es el rango correcto.

### Glitch irregular (varios instantes, distintos)

La irregularidad es lo que lo hace creíble. Se encadena con distintos `enable` y distintas
intensidades:

```bash
ffmpeg -y -i corte.mp4 -vf \
"rgbashift=rh=8:bh=-8:enable='between(t,1.20,1.27)',\
 rgbashift=rh=-4:bh=5:enable='between(t,1.33,1.37)',\
 pixelize=w=12:h=4:enable='between(t,1.30,1.33)',\
 noise=alls=45:allf=t:enable='between(t,1.20,1.37)'" \
  -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p glitch_bueno.mp4
```

Fíjate en la estructura: tres eventos distintos, con intensidades distintas, en 0,17 segundos, con
ruido de fondo cubriendo todo el episodio. Eso se lee a fallo de señal. Un solo efecto de medio
segundo, no.

### El audio del glitch

Sin distorsión de audio en el mismo instante, no hay glitch. Lo mínimo:

```bash
ffmpeg -y -i glitch_bueno.mp4 \
  -af "volume=0:enable='between(t,1.22,1.26)'" \
  -c:v copy -c:a aac glitch_completo.mp4
```

Un corte seco de audio de 4 fotogramas. Es lo más simple y funciona. Mejor todavía: sustituirlo por
un chasquido o ruido blanco corto. Ver `76-diseño-sonoro.md`.

### Dónde va el glitch

En un cambio de bloque, o justo antes de un revelado. Una vez, dos como máximo, en toda la pieza.
Ver `50`.

---

## Cómo elegir la textura correcta

| Si la marca / el proyecto es... | Textura |
|---|---|
| Cinematográfica, premium, sobria | Grano fino (`alls=6-10`, solo en luma) |
| Documental, testimonial | Grano medio (`alls=12-16`) |
| Nostálgica de los 80–90 | VHS completo, con audio degradado |
| Editorial, gráfica, tipográfica | Halftone teñido en color de marca |
| Digital, tecnológica, gamer | Pixelize + glitch puntual |
| Punk, DIY, riso, fanzine | Tramado Bayer |
| Corporativa seria | **Ninguna.** Solo grano casi invisible (`alls=5`) |

Y la pregunta filtro: **¿la textura sale del concepto o la puse porque se veía bien?** Si el proyecto
no tiene un motivo para verse analógico, el VHS es solo un filtro. Ver `56`.

---

## El orden correcto en la cadena

La textura va **al final de todo**, después del color:

```
corte → corrección de color → gradación / look → textura → viñeta → exportación
```

Si aplicas grano antes de corregir color, la corrección va a amplificar el ruido de forma
impredecible. Si aplicas textura antes de montar, el grano se corta en cada corte. Ver `61`.

Ejemplo de cadena completa en un solo comando:

```bash
ffmpeg -y -i corte.mp4 \
  -vf "eq=contrast=1.08:saturation=0.95,curves=preset=medium_contrast,\
noise=c0s=10:c0f=t+u:c1s=2:c1f=t:c2s=2:c2f=t,\
vignette=PI/5" \
  -c:v libx264 -crf 19 -preset slow -pix_fmt yuv420p final.mp4
```

---

## Errores comunes

- **Aplicar la textura clip por clip.** El grano cambia en cada corte y se ve como un error. La
  textura se aplica una sola vez sobre el corte terminado.

- **Olvidar `allf=t` en `noise`.** Sin la `t` el patrón es fijo y se lee como suciedad en el lente,
  no como grano. Es el error número uno de este módulo.

- **Poner demasiado grano.** Si el cliente lo nota sin que se lo digas, sobra. `alls=6-12` cubre casi
  todo.

- **Aplicar textura antes de corregir el color.** La corrección amplifica el ruido de forma
  impredecible. Textura al final.

- **VHS sin degradar el audio.** Imagen de 1988 con sonido de 2026. Se lee a filtro, no a formato.

- **VHS con escalado suave.** Bajar y subir con el escalador normal deja borroso, no degradado. Usa
  `flags=neighbor`.

- **Glitch de medio segundo.** Un fallo real dura 2–3 fotogramas. Medio segundo es un adorno.

- **Glitch regular y repetido.** La regularidad delata el preset. El glitch real es irregular.

- **Glitch mudo.** Sin evento de audio no existe.

- **Aplicar `geq` a resolución completa "porque se ve mejor".** No se ve mejor: se ve igual y tarda 20
  veces más. Baja resolución, aplica, sube con `flags=neighbor`.

- **No revisar el peso final.** El grano encarece muchísimo la compresión. Un video con grano puede
  pesar 60% más al mismo CRF.

- **Usar textura sin motivo conceptual.** Si el proyecto no tiene razón para verse analógico, es
  decoración. Ver `56`.

---

## Checklist

- [ ] La textura se aplica sobre el corte terminado, no clip por clip.
- [ ] Va al final de la cadena, después de la corrección y la gradación de color.
- [ ] `noise` lleva `allf=t` (grano temporal).
- [ ] El nivel de grano está entre 6 y 16 salvo que la estética pida más.
- [ ] Si es VHS: el audio también está degradado (mono, sin agudos).
- [ ] Si es VHS: el escalado usa `flags=neighbor`, no el suave.
- [ ] Si hay `geq`: lo apliqué a resolución reducida y escalé después.
- [ ] Si hay glitch: dura 2–3 fotogramas, es irregular, y hay evento de audio en el mismo instante.
- [ ] El glitch aparece 1 o 2 veces en toda la pieza, no más.
- [ ] La textura elegida responde al concepto del proyecto, no a mi gusto.
- [ ] Comprobé el peso del archivo final y sigue dentro del límite de la plataforma (`92`, `93`).
- [ ] Miré el render completo buscando que el grano no salte entre cortes (`98`).
