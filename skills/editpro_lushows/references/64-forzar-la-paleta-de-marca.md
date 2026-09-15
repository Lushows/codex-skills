# 64 — Forzar la paleta de marca (duotono)

Este es el módulo más útil de todo el bloque de color, y sale de un problema real y cotidiano:

> **Ninguna IA generativa respeta una paleta de marca. Siempre deriva.**

Le pasas el HEX exacto, le pones el manual de marca, le mandas imágenes de referencia. La primera
imagen sale bien. La tercera ya tiene un azul distinto. La octava tiene un morado que nunca pediste.
Y con video generado es peor, porque el color se mueve **dentro del mismo clip**.

La solución no es pedírselo mejor. **No existe el prompt que lo arregle.** La solución es imponer el
color en post, sobre el resultado, con matemática. Y eso se hace en dos líneas de ffmpeg.

La misma técnica sirve para material filmado: unificar planos de cámaras distintas, hacer que un
video de archivo pertenezca a la marca, o darle a una campaña entera una firma visual que nadie más
puede copiar por accidente.

---

## 1. Qué es un duotono

Un duotono es una imagen construida con **solo dos colores**: uno para las sombras y otro para las
luces, y todos los tonos intermedios son la mezcla de esos dos. No hay ningún otro color en la
imagen. Ninguno.

Por eso funciona tan bien como candado de marca: si el color de sombra es tu azul y el de luz es el
blanco, es **físicamente imposible** que aparezca un morado indeseado. No hay de dónde salga.

El procedimiento tiene dos movimientos:

1. **Quitar todo el color** → la imagen queda en blanco y negro puro (solo luma).
2. **Reasignar el punto negro de cada canal** al color de marca, dejando el blanco intacto.

Eso es todo. Lo que antes era negro ahora es tu azul; lo que era blanco sigue blanco; y todo lo del
medio es un degradado limpio entre los dos.

---

## 2. La receta verificada

Este es el comando que funcionó en producción, para el azul de marca **#09163A**:

```bash
ffmpeg -i entrada.mp4 -vf \
"hue=s=0,curves=r='0/0.035 0.5/0.52 1/1':g='0/0.086 0.5/0.55 1/1':b='0/0.227 0.5/0.62 1/1',eq=contrast=1.12,format=yuv420p" \
  -c:v libx264 -crf 17 -preset slow \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -c:a copy salida_duotono.mp4
```

Pieza por pieza:

| Parte | Qué hace |
|---|---|
| `hue=s=0` | quita **todo** el color. Sin esto, el color original pelea con el mapeo y sale barro. |
| `curves=r='0/0.035 …'` | el negro del canal rojo ya no es 0, ahora es 0.035 |
| `curves=g='0/0.086 …'` | el negro del canal verde ahora es 0.086 |
| `curves=b='0/0.227 …'` | el negro del canal azul ahora es 0.227 |
| `… 1/1` en los tres | el **blanco no se toca**: sigue siendo blanco puro |
| `… 0.5/0.52`, `0.5/0.55`, `0.5/0.62` | los medios, para que el degradado sea suave y no lineal |
| `eq=contrast=1.12` | recupera el punch que se pierde al comprimir el rango de color |

---

## 3. La matemática: de HEX a punto negro por canal

Es una división. Nada más.

### Paso 1 — HEX a decimal

`#09163A` se parte en tres pares:

| Par | Hex | Decimal |
|---|---|---|
| `09` | rojo | **9** |
| `16` | verde | **22** |
| `3A` | azul | **58** |

(Si te da pereza convertir hex a decimal a mano: `09` = 0×16 + 9 = 9. `16` = 1×16 + 6 = 22.
`3A` = 3×16 + 10 = 58, porque A = 10.)

### Paso 2 — Decimal a escala 0–1 (dividir entre 255)

```
rojo   →  9 / 255 = 0.0353  →  0.035
verde  → 22 / 255 = 0.0863  →  0.086
azul   → 58 / 255 = 0.2275  →  0.227
```

Estos tres números son tus **puntos negros**. Van en el `0/…` de cada canal.

### Paso 3 — El punto medio de cada canal

Para que el degradado no se vea plano, el medio va a mitad de camino entre el punto negro y el
blanco:

```
medio = (1 + punto_negro) / 2
```

```
rojo   → (1 + 0.035) / 2 = 0.5175  →  0.52
verde  → (1 + 0.086) / 2 = 0.5430  →  0.55
azul   → (1 + 0.227) / 2 = 0.6135  →  0.62
```

Que es exactamente lo que hay en el comando verificado. Redondea a dos decimales; la diferencia no
se ve y el comando queda legible.

### Paso 4 — Armar la cadena

```
curves=r='0/<Rk> 0.5/<Rm> 1/1':g='0/<Gk> 0.5/<Gm> 1/1':b='0/<Bk> 0.5/<Bm> 1/1'
```

### El calculador, para no equivocarte

```python
# duotono.py — pásale el HEX y te escribe la cadena de ffmpeg
import sys

hexcolor = sys.argv[1].lstrip('#')
r, g, b = (int(hexcolor[i:i+2], 16) for i in (0, 2, 4))
k = [r/255, g/255, b/255]

# Si el color es claro, hay que oscurecerlo para que sirva como punto negro (ver sección 4)
luma = 0.2126*k[0] + 0.7152*k[1] + 0.0722*k[2]
if luma > 0.14:
    f = 0.10 / luma
    k = [c*f for c in k]
    print(f"# aviso: color claro (luma {luma:.3f}); lo escalé por {f:.2f}", file=sys.stderr)

m = [(1 + c)/2 for c in k]
print(
    f"hue=s=0,curves="
    f"r='0/{k[0]:.3f} 0.5/{m[0]:.2f} 1/1':"
    f"g='0/{k[1]:.3f} 0.5/{m[1]:.2f} 1/1':"
    f"b='0/{k[2]:.3f} 0.5/{m[2]:.2f} 1/1',eq=contrast=1.12"
)
```

```bash
python duotono.py "#09163A"
# hue=s=0,curves=r='0/0.035 0.5/0.52 1/1':g='0/0.086 0.5/0.54 1/1':b='0/0.227 0.5/0.61 1/1',eq=contrast=1.12
```

---

## 4. La trampa: el color de marca tiene que ser OSCURO

El punto negro es, literalmente, **lo más oscuro de la imagen**. Si tu color de marca es brillante,
el duotono te queda lavadísimo, sin negros, sin contraste, imposible de leer.

Ejemplo: el cobalto **#2742F5** (39, 66, 245) da puntos negros de 0.153, 0.259 y **0.961**. Un canal
azul cuyo valor mínimo es 0.961 significa que **el azul nunca baja del 96%**: la imagen entera te
queda azul cielo pálido.

Solución: no uses el color de marca tal cual, usa **su sombra**. Multiplica los tres canales por el
mismo factor (así conservas el tono exacto y solo bajas el brillo):

```
luma = 0.2126·R + 0.7152·G + 0.0722·B          (en escala 0–1)
factor = 0.10 / luma
punto_negro = canal × factor
```

Para #2742F5: luma = 0.287 → factor = 0.35 → puntos negros **0.054, 0.091, 0.336**, medios
**0.53, 0.55, 0.67**. Ese sí funciona, y sigue siendo el mismo azul cobalto, solo que en versión
sombra. El script de arriba ya lo hace solo.

**Regla práctica:** si el color de marca es un pastel, un amarillo, un naranja claro o cualquier
cosa con luma > 0.20, no lo pongas de punto negro. Ponlo de **punto blanco** (siguiente sección) o
escálalo.

---

## 5. Variantes que vas a necesitar

### Duotono de dos colores de marca (sombra Y luz)

En vez de dejar el blanco intacto, le asignas un segundo color. Es el duotono "de verdad", el de los
afiches de Spotify. Cambias el `1/1` por `1/<valor del color claro>`:

```bash
# Sombras al azul #09163A, luces al crema #F2E9D8 (242, 233, 216) → 0.949, 0.914, 0.847
ffmpeg -i in.mp4 -vf \
"hue=s=0,curves=r='0/0.035 0.5/0.50 1/0.949':g='0/0.086 0.5/0.52 1/0.914':b='0/0.227 0.5/0.56 1/0.847',eq=contrast=1.10,format=yuv420p" \
  -c:v libx264 -crf 17 -c:a copy out_duo2.mp4
```

Cuidado: al bajar el punto blanco pierdes brillo. Compénsalo con `eq=contrast` o subiendo un poco
los medios.

### Duotono parcial (tinte, no candado)

A veces el duotono total es demasiado. Quieres que se reconozca la marca pero que la comida siga
viéndose comida. Mezcla el duotono con el original:

```bash
ffmpeg -i in.mp4 -filter_complex "\
[0:v]split=2[orig][duo];\
[duo]hue=s=0,curves=r='0/0.035 0.5/0.52 1/1':g='0/0.086 0.5/0.55 1/1':b='0/0.227 0.5/0.62 1/1'[d];\
[orig][d]blend=all_mode=normal:all_opacity=0.55,format=yuv420p[v]" \
  -map "[v]" -map 0:a? -c:v libx264 -crf 17 -c:a copy out_tinte.mp4
```

`all_opacity=0.55` = 55% duotono, 45% original. Entre `0.35` y `0.65` es la zona útil: se lee la
marca y se lee el contenido. **Para comida rara vez pases de 0.45**: el duotono mata el apetito
porque la comida deja de tener su color real (ver `153-food-y-bebida-en-video.md`).

### Tritono: sombra de marca + medios neutros + luces cálidas

Se hace añadiendo un tercer punto a la curva, en los medios altos:

```bash
hue=s=0,curves=r='0/0.035 0.5/0.52 0.8/0.86 1/1':g='0/0.086 0.5/0.55 0.8/0.84 1/0.99':b='0/0.227 0.5/0.62 0.8/0.80 1/0.96'
```

Fíjate en el punto `0.8`: ahí el azul (0.80) queda por debajo del rojo (0.86), o sea que las luces
altas se van al cálido mientras las sombras siguen azules. Es el split toning del módulo `63`, pero
con un candado de marca.

### Aplicarlo por lotes a toda una campaña

```bash
DUO="hue=s=0,curves=r='0/0.035 0.5/0.52 1/1':g='0/0.086 0.5/0.55 1/1':b='0/0.227 0.5/0.62 1/1',eq=contrast=1.12"

for f in generados/*.mp4; do
  ffmpeg -y -i "$f" -vf "$DUO,format=yuv420p" -c:v libx264 -crf 18 -preset slow \
    -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
    -c:a copy marca/$(basename "$f")
done
```

Y para imágenes fijas, es idéntico:

```bash
ffmpeg -i lamina.png -vf "$DUO" lamina_marca.png
```

---

## 6. Cuándo el duotono se aplica y cuándo NO

**El orden importa muchísimo:** el duotono va **después** de corregir y emparejar, y **antes** de
poner logos, texto y gráficos.

```
corrección → emparejado → DUOTONO → grano/textura → logo, texto, gráficos → export
```

Si pones el logo antes del duotono, el logo también se duotoniza y pierde sus colores. Si un
elemento de marca tiene que conservar su color exacto (un logo a color, un botón, un empaque), va
**encima**, como overlay:

```bash
ffmpeg -i video_duotono.mp4 -i logo.png -filter_complex \
  "[0:v][1:v]overlay=W-w-48:48:format=auto,format=yuv420p" \
  -c:v libx264 -crf 18 -c:a copy final.mp4
```

**No uses duotono total cuando:**
- El producto tiene que verse con su color real (comida, ropa, cosmética, pintura).
- Hay piel como protagonista y el color de marca la vuelve enfermiza (verde, morado intenso).
- Es un testimonio y necesitas que se sienta real, no diseñado.
- La plataforma va a recomprimir fuerte y tu color de marca vive en una zona que se bandea (azules
  y morados oscuros son los peores; ver `68`).

En esos casos: duotono **parcial** al 30–45%, o duotono solo en los planos de transición, los títulos
y los fondos, y material real sin tocar.

---

## 7. Cómo verificar que quedó exacto

No lo mires: mídelo. Saca un frame y comprueba que el píxel más oscuro es tu color:

```bash
# Frame de prueba
ffmpeg -y -ss 2 -i salida_duotono.mp4 -frames:v 1 chequeo.png

# Valores mínimos y máximos por canal
ffmpeg -hide_banner -i chequeo.png -vf "signalstats,metadata=mode=print:file=-" -f null - 2>&1 \
  | grep -E "RMIN|GMIN|BMIN|RMAX|GMAX|BMAX"
```

Lo que debe salir (en escala 0–255): `RMIN ≈ 9`, `GMIN ≈ 22`, `BMIN ≈ 58`. Si sale otra cosa,
revisa: casi siempre es porque el material venía en rango limitado y el negro real era 16, no 0
(ver `60`), o porque olvidaste el `hue=s=0`.

La otra verificación, la definitiva, es el **vectorscopio**: en un duotono real todos los puntos
caen sobre **una sola línea recta** que sale del centro. Si ves una nube, quedó color residual.

```bash
ffmpeg -y -ss 2 -i salida_duotono.mp4 -frames:v 1 \
  -vf "vectorscope=mode=color3:graticule=green:flags=name" vectorscopio.png
```

Detalle completo en `69-monitoreo-y-scopes.md`.

---

## Errores comunes

- **Olvidar `hue=s=0`.** Es el error número uno. Sin desaturar, el color original se mezcla con el
  mapeo y sale un barro impredecible — justo lo que querías evitar.
- **Usar un color de marca claro como punto negro.** Imagen lavada, sin contraste. Escálalo primero.
- **Dividir entre 100 en vez de entre 255.** Los canales van de 0 a 255, no son porcentajes.
- **Poner los tres canales con el mismo punto negro.** Eso no es duotono, es solo bajar contraste.
- **Aplicar el duotono antes de corregir.** El error del módulo `61`, aquí también.
- **Poner el logo antes del duotono.** El logo pierde sus colores y toca rehacer.
- **Duotonizar comida al 100%.** Deja de dar hambre. Es un error de negocio, no de color.
- **Duotonizar piel con un color frío intenso.** La gente se ve enferma (ver `67`).
- **Confiar en que la IA sí respetó la paleta esta vez.** Nunca la respeta. Aplica el duotono
  siempre, aunque "se vea bien".
- **No verificar con `signalstats` y asumir que quedó.** Toma 5 segundos y te evita entregar mal.
- **Cambiar el punto negro entre piezas de la misma campaña.** El candado de marca solo sirve si es
  el mismo número siempre. Guárdalo en un archivo del proyecto.

---

## Checklist

- [ ] Tengo el HEX **oficial** de la marca (no uno que saqué de una captura de pantalla).
- [ ] Convertí HEX → decimal → dividí entre 255. Tengo los tres puntos negros.
- [ ] Verifiqué que la luma del color sea < 0.14; si no, lo escalé conservando el tono.
- [ ] Calculé los medios con `(1 + punto_negro) / 2`.
- [ ] La cadena empieza con `hue=s=0`. Siempre.
- [ ] Los tres canales terminan en `1/1` (o en el punto blanco del segundo color de marca).
- [ ] Añadí `eq=contrast=1.10–1.15` para recuperar el punch.
- [ ] Apliqué el duotono **después** de corregir y emparejar.
- [ ] Los logos, texto y gráficos van **encima** del duotono, no debajo.
- [ ] Si es comida o producto con color propio, usé duotono parcial (≤ 0.45) o lo dejé fuera.
- [ ] Verifiqué con `signalstats` que RMIN/GMIN/BMIN dan los valores esperados.
- [ ] Miré el vectorscopio: una sola línea, no una nube.
- [ ] Guardé la cadena exacta en el proyecto para que la próxima pieza use el mismo número.
- [ ] Apliqué el mismo duotono a **todas** las piezas de la campaña, no solo a algunas.
