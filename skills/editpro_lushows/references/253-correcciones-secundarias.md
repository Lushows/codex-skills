# 253 — Correcciones secundarias

Este es el corazón del bloque. Todo lo anterior son **primarias**: filtros que tocan el cuadro
entero. Una secundaria toca **solo una parte**: un rango de color, una zona del encuadre, un nivel de
brillo.

La razón de existir de las secundarias, en una frase que salió de un caso real:

> Bajar el magenta del cuadro completo un 40 % dejó la cara igual de morada y le quitó el neón al
> bar. La secundaria hizo lo contrario: arregló la cara y dejó el neón exactamente como estaba.

Cuando alguien dice "no puedo arreglar esto sin dañar aquello", la respuesta casi siempre es: no
estás usando secundarias.

---

## 1. Las tres maneras de aislar

Solo hay tres formas de decirle a un filtro "aplícate aquí y no allá":

| Tipo | Aísla por | Herramienta ffmpeg | Se mueve con el sujeto |
|---|---|---|---|
| **Calificador de color** | matiz / saturación | `selectivecolor`, `hsvkey`, `colorkey`, `colorhold` | ✅ sí, automáticamente |
| **Calificador de luma** | brillo | `curves` sobre una copia gris, `maskfun` | ✅ sí |
| **Ventana (power window)** | posición en el cuadro | `geq`, `drawbox`, imagen de máscara | ❌ no, salvo que la animes |

El calificador de color es el que más rinde, porque **sigue al sujeto solo**: si la cara se mueve, el
rango de color de la piel se mueve con ella. Una ventana fija se queda quieta y el sujeto se le sale.
Regla de oficio: **empieza siempre por el calificador de color; la ventana es el último recurso.**

---

## 2. `selectivecolor`: la secundaria que más vas a usar

Es el filtro que resolvió el caso del bar. Viene de la imprenta: divide la imagen en nueve familias
y a cada una le suma o le resta tinta CMYK.

```
selectivecolor=correction_method=absolute:reds=C M Y K:magentas=C M Y K:...
```

Las nueve familias: `reds`, `yellows`, `greens`, `cyans`, `blues`, `magentas`, `whites`, `neutrals`,
`blacks`.

Cada una recibe **cuatro números entre −1 y 1**, separados por espacio, en orden **cian, magenta,
amarillo, negro**. Lógica de tinta (importante, porque es contraintuitiva):

| Subes | Efecto en la imagen |
|---|---|
| Cian (+) | más cian, menos rojo |
| Magenta (+) | más magenta, menos verde |
| Amarillo (+) | más amarillo, menos azul |
| Negro (+) | más oscuro esa familia |

Y al revés con los negativos. O sea: **para quitar magenta de la piel, pones magenta en negativo**.

### La corrección real del caso

```bash
ffmpeg -i corregido.mp4 -vf \
  "selectivecolor=correction_method=absolute:reds=0 -0.10 0.06 0:magentas=0 -0.14 0.04 0" \
  -c:v libx264 -crf 16 -preset slow piel_ok.mp4
```

Traducido a español:

- `reds=0 -0.10 0.06 0` → en los rojos (donde vive la piel): **−10 % de magenta** (quita el morado) y
  **+6 % de amarillo** (devuelve el tono cálido natural de la piel).
- `magentas=0 -0.14 0.04 0` → en los magentas (el borde del neón que contaminó la cara): **−14 % de
  magenta**, **+4 % de amarillo**.

Por qué funciona: la piel vive en `reds` y en el borde de `magentas`. El neón morado puro vive en
`magentas` y `blues`. Al no tocar `blues` ni `cyans`, **el neón sobrevive intacto**. Eso es
exactamente lo que una corrección global no puede hacer.

### `absolute` vs `relative`

| Modo | Qué hace |
|---|---|
| `absolute` | el ajuste es el mismo en toda la familia. Predecible. **Úsalo.** |
| `relative` | el ajuste es proporcional a cuánta tinta ya había. Más sutil, menos controlable |

Para trabajo medible, `absolute`. `relative` sirve cuando quieres un toque muy suave sobre material
ya delicado.

### Los usos que valen la pena

```bash
# Cielo más profundo sin tocar nada más
ffmpeg -i clip.mp4 -vf "selectivecolor=correction_method=absolute:blues=0.10 0.04 -0.06 0.05" -c:v libx264 -crf 16 out.mp4

# Verdes de vegetación menos "césped artificial"
ffmpeg -i clip.mp4 -vf "selectivecolor=correction_method=absolute:greens=0.05 0 -0.12 0" -c:v libx264 -crf 16 out.mp4

# Negros con un pelo de azul (look cine, módulo 257) sin teñir la piel
ffmpeg -i clip.mp4 -vf "selectivecolor=correction_method=absolute:blacks=0.04 0 -0.08 0" -c:v libx264 -crf 16 out.mp4
```

Ese último es oro: teñir sombras sin tocar la cara, que es la promesa del look cinematográfico bien
hecho. Y `whites=0 0 -0.10 0` limpia el amarilleo de la luz cálida **solo** en lo que es blanco.

### Magnitudes honestas

| Rango | Efecto |
|---|---|
| 0.02 – 0.06 | sutil, casi imperceptible. El 80 % de tu trabajo vive aquí |
| 0.08 – 0.15 | visible y todavía natural. La corrección del bar está aquí |
| 0.20 – 0.40 | look declarado, se nota |
| > 0.50 | efecto, no corrección. Va a verse artificial |

---

## 3. Aislar por rango HSV: `hsvkey` y `hsvhold`

Cuando `selectivecolor` no es lo bastante quirúrgico (por ejemplo, quieres solo ese morado y no todo
el rango de magentas), pasas a los calificadores HSV.

| Filtro | Qué hace |
|---|---|
| `hsvkey` | vuelve **transparente** lo que cae en el rango → sirve para fabricar máscaras |
| `hsvhold` | vuelve **gris** lo que cae **fuera** del rango → el efecto "solo un color a color" |
| `colorkey` / `colorhold` | lo mismo pero especificando un color RGB concreto |

Ver qué está agarrando el calificador (paso obligatorio antes de corregir):

```bash
# Deja a color solo el morado del neón; todo lo demás en gris
ffmpeg -y -i clip.mp4 -vf "hsvhold=hue=290:sat=0.35:val=0.25:similarity=0.30:blend=0.10" \
  -frames:v 1 vista_rango.png
```

| Parámetro | Qué es | Rango |
|---|---|---|
| `hue` | el matiz central, en grados | 0–360 (0 rojo, 120 verde, 240 azul, 300 magenta) |
| `sat` | saturación central | 0–1 |
| `val` | valor/brillo central | 0–1 |
| `similarity` | qué tan ancho es el rango | 0.01 muy angosto – 1.0 todo |
| `blend` | qué tan suave es el borde | 0 duro – 0.5 muy suave |

**El error que todo el mundo comete:** dejar `blend=0`. El borde queda como recortado con tijera y se
ve el "halo" del efecto. En material real, `blend` entre 0.05 y 0.15 casi siempre.

Y el efecto "todo gris menos el producto rojo", que sirve de verdad en publicidad (`152`), aunque se
gastó en los 2000 y hoy se lee como barato si no está justificado (`56`):

```bash
ffmpeg -i clip.mp4 -vf "colorhold=color=0xC0392B:similarity=0.30:blend=0.12" \
  -c:v libx264 -crf 16 producto_rojo.mp4
```

---

## 4. Máscaras de verdad: corregir solo lo que la máscara dice

El patrón profesional completo: fabricas una máscara en blanco y negro, corriges una copia del video,
y fundes las dos usando la máscara. Dos formas, ambas verificadas.

### Forma A — `maskedmerge` (la limpia)

```bash
ffmpeg -y -i clip.mp4 -filter_complex "\
[0:v]split=3[base][corr][key];\
[key]format=yuva420p,hsvkey=hue=300:sat=0.30:val=0.20:similarity=0.28:blend=0.06,alphaextract,format=gbrp[m];\
[corr]eq=saturation=0.55,format=gbrp[c];\
[base]format=gbrp[b];\
[b][c][m]maskedmerge,format=yuv420p" \
  -c:v libx264 -crf 16 -c:a copy out.mp4
```

Cómo se lee: donde la máscara es **negra** queda `[b]` (el original), donde es **blanca** queda `[c]`
(la versión corregida). Los grises intermedios funden proporcionalmente.

**Dos trampas verificadas, las dos cuestan una hora si no las sabes:**

1. `alphaextract` necesita un formato con alfa a la entrada. Sin `format=yuva420p` antes de `hsvkey`,
   ffmpeg falla con `The following filters could not choose their formats: Parsed_alphaextract_...`.
2. `maskedmerge` mezcla **plano por plano**. Si le pasas una máscara gris convertida a `yuv420p`, los
   planos U y V de la máscara valen 128 y te funde el color a medias en toda la imagen. Convierte las
   tres ramas a `gbrp` (donde el gris se replica en los tres canales) y sale correcto.

### Forma B — `alphamerge` + `overlay` (la que siempre funciona)

```bash
ffmpeg -y -i clip.mp4 -filter_complex "\
[0:v]split=3[base][corr][key];\
[key]format=yuva420p,hsvkey=hue=300:sat=0.30:val=0.20:similarity=0.28:blend=0.06,alphaextract,format=gray[m];\
[corr]eq=saturation=0.55[c];\
[c][m]alphamerge[ca];\
[base][ca]overlay,format=yuv420p" \
  -c:v libx264 -crf 16 -c:a copy out.mp4
```

Aquí la corrección se convierte en una capa con transparencia y se superpone. Es más fácil de razonar
y no tiene el problema de los planos. Es la que uso por defecto.

### Ver la máscara antes de usarla (no opcional)

```bash
ffmpeg -y -i clip.mp4 -vf \
  "format=yuva420p,hsvkey=hue=300:sat=0.30:val=0.20:similarity=0.28:blend=0.06,alphaextract,format=gray" \
  -frames:v 1 mascara.png
```

Ábrela. Lo blanco es lo que vas a corregir. Si hay manchas blancas en sitios que no querías (típico:
una camisa del mismo tono que la piel), ajusta `similarity` **hacia abajo** hasta que solo quede lo
tuyo.

### Suavizar la máscara (el paso que separa lo pro de lo casero)

```bash
# ...alphaextract,format=gray,gblur=sigma=12[m]
```

Una máscara desenfocada funde suave y no deja bordes. `sigma` entre 6 y 20 según la resolución. Casi
nunca quieres una máscara de bordes duros.

---

## 5. Aislar por brillo: máscaras de luma

Para cosas como "quiero levantar solo las sombras" o "quiero enfriar solo las altas luces sin tocar
la piel":

```bash
ffmpeg -y -i clip.mp4 -filter_complex "\
[0:v]split=3[base][corr][key];\
[key]format=gray,curves=all='0/0 0.45/0 0.65/1 1/1',gblur=sigma=8,format=gbrp[m];\
[corr]eq=saturation=1.30,format=gbrp[c];\
[base]format=gbrp[b];\
[b][c][m]maskedmerge,format=yuv420p" \
  -c:v libx264 -crf 16 -c:a copy out.mp4
```

La clave es la curva `0/0 0.45/0 0.65/1 1/1`: lo que esté por debajo del 45 % de brillo queda en negro
(no se corrige), lo que esté por encima del 65 % queda en blanco (se corrige entero), y entre medio
hay una rampa suave. Es un **calificador de luma** hecho a mano, igual al de los paneles de software
caro. Para corregir solo las sombras, invierte la curva: `0/1 0.35/1 0.55/0 1/0`.

---

## 6. Ventanas (power windows) con `geq`

Cuando lo que quieres aislar no tiene un color propio ni un brillo propio —"quiero oscurecer esa
esquina", "quiero levantar la cara que está en el tercio izquierdo"— toca ventana.

```bash
# Ventana ovalada centrada, suave
ffmpeg -y -f lavfi -i "nullsrc=size=1080x1920:d=1" \
  -vf "format=gray,geq=lum='255*clip(1.3-1.6*hypot((X-W/2)/(W/2),(Y-H/2)/(H/2)),0,1)',gblur=sigma=40" \
  -frames:v 1 ventana.png
```

`hypot((X-W/2)/(W/2),(Y-H/2)/(H/2))` es la distancia normalizada al centro: 0 en el centro, 1 en el
borde. La fórmula `1.3-1.6*d` da blanco en el centro y negro en los bordes; ajusta los dos números
para mover el tamaño y la dureza. `clip(...,0,1)` evita que se desborde.

Para moverla a otro punto, cambia el centro:

```bash
# Ventana sobre la cara, que está en x=420, y=560
-vf "format=gray,geq=lum='255*clip(1.3-2.2*hypot((X-420)/380,(Y-560)/380),0,1)',gblur=sigma=30"
```

Después la usas como máscara con cualquiera de los dos patrones de la sección 4, pasando el PNG como
segunda entrada:

```bash
ffmpeg -y -i clip.mp4 -loop 1 -i ventana.png -filter_complex "\
[0:v]split=2[base][corr];\
[1:v]scale=1080:1920,format=gray[m];\
[corr]eq=gamma=1.18[c];\
[c][m]alphamerge[ca];\
[base][ca]overlay,format=yuv420p" -shortest -c:v libx264 -crf 16 -c:a copy out.mp4
```

**El límite honesto de las ventanas en ffmpeg: no siguen al sujeto.** Si la persona camina, la ventana
se queda. Se puede animar con expresiones de tiempo (`t`) dentro de `geq`, pero es tedioso y frágil.
Si necesitas seguimiento de verdad, ahí sí vale la pena DaVinci Resolve (`117`, `219`).

---

## 7. Cuántas secundarias son demasiadas

Guía honesta para video social: **1–2 es lo normal** (la piel y una cosa más), 3–4 en un proyecto
exigente de producto o comercial, y **5 o más casi siempre significa que estás tapando un problema de
rodaje** (`259`). Cero también es señal de algo: casi todo material tiene un problema local.

Y el orden entre ellas importa: **primero la piel, después lo demás**. Si arreglas el cielo primero y
luego la piel, la corrección de la piel puede volver a mover el cielo si los rangos se tocan.

---

## 8. Verificar que la secundaria hizo lo que dijo

No basta con mirar. Mide la zona antes y después:

```bash
# antes
ffprobe -v error -f lavfi -i "movie=antes.mp4,crop=120:120:840:420,signalstats" \
  -show_entries frame_tags=lavfi.signalstats.UAVG,lavfi.signalstats.VAVG -of csv=p=0 -read_intervals "%+#3"

# después
ffprobe -v error -f lavfi -i "movie=despues.mp4,crop=120:120:840:420,signalstats" \
  -show_entries frame_tags=lavfi.signalstats.UAVG,lavfi.signalstats.VAVG -of csv=p=0 -read_intervals "%+#3"
```

Y —esto es lo que casi nadie hace— **mide también una zona que NO querías tocar**, por ejemplo el
neón. Si el neón cambió, tu secundaria no era tan secundaria.

Esa doble medición (la zona objetivo cambió + la zona protegida no cambió) es la definición
verificable de una secundaria bien hecha.

---

## Errores comunes

- **Resolver con globales lo que pide una secundaria.** Bajar saturación global para quitar el morado
  de una cara te apaga toda la escena y no arregla la cara.
- **Usar `selectivecolor` sin saber en qué familia vive tu problema.** La piel está en `reds` y en el
  borde de `magentas`. Mira el vectorscopio primero (`252`).
- **Confundir el orden CMYK.** Son cian, magenta, amarillo, negro. Para quitar verde subes magenta;
  para quitar magenta bajas magenta.
- **`blend=0` en un calificador.** Bordes recortados, halos visibles. Siempre 0.05–0.15.
- **No mirar la máscara antes de aplicarla.** El 90 % de los "el efecto se ve raro" es una máscara que
  agarra cosas que no debía.
- **Máscara con bordes duros.** Sin `gblur` sobre la máscara, se nota el parche.
- **`alphaextract` sin `format=yuva420p` antes.** Error de negociación de formatos, garantizado.
- **`maskedmerge` con máscara gris convertida a `yuv420p`.** Los planos de croma quedan en 128 y te
  funde el color a medias en todo el cuadro. Usa `gbrp`.
- **Ventana fija sobre un sujeto que se mueve.** A los dos segundos está corrigiendo la pared.
- **No verificar que la zona protegida siguió igual.** Sin esa medición no sabes si aislaste o solo
  corregiste distinto.
- **Cinco secundarias para arreglar un plano.** Ese plano probablemente hay que volverlo a grabar
  (`259`).

---

## Checklist

- [ ] Intenté resolverlo con primarias primero y confirmé que no se puede sin dañar otra cosa.
- [ ] Sé en qué familia de color vive mi problema (lo vi en el vectorscopio, no lo adiviné).
- [ ] Empecé por el calificador de color; la ventana fija es mi último recurso.
- [ ] Vi la máscara exportada como PNG antes de aplicar nada.
- [ ] La máscara tiene `blend` (0.05–0.15) y/o `gblur` para que el borde funda.
- [ ] Usé `format=yuva420p` antes de `hsvkey` y `gbrp` en las tres ramas de `maskedmerge`.
- [ ] La magnitud del ajuste está en el rango honesto (0.02–0.15 para corregir).
- [ ] Corregí la piel **antes** que las demás zonas.
- [ ] Medí la zona objetivo antes y después: cambió lo que tenía que cambiar.
- [ ] Medí una zona protegida antes y después: **no** cambió.
- [ ] Miré el resultado en movimiento, no solo en un frame (los calificadores parpadean si el rango
      está muy justo).
