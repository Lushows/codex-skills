# 415 · La interfaz de cada red: medirla, no recordarla

**Qué resuelve:** las cifras de interfaz caducan. `45` tiene la tabla por plataforma con fecha de
agosto de 2026 y `376` la actualización de Meta de marzo de ese año; ninguna de las dos sobrevivirá
intacta a un rediseño. Este módulo no añade números: añade **el procedimiento que los vuelve a
producir** en veinte minutos, y el formato en que se guardan para que el siguiente sepa de cuándo son.

> Un módulo que dice «Instagram tapa 320 px» sin fecha ni método es una trampa a seis meses vista.
> Todo número de interfaz que uses debe poder responder a dos preguntas: **¿quién lo midió y cuándo?**

---

## Qué se mide, exactamente

No es un rectángulo: son cinco cosas distintas, y tres de ellas **crecen**.

| Elemento | Fijo o variable | Qué lo hace crecer |
|---|---|---|
| Franja superior (pestañas, buscador, estado) | Fijo por dispositivo | La muesca/isla del teléfono |
| Columna de iconos (derecha) | Casi fijo | Un icono nuevo cuando la app añade función |
| **Caption / descripción** | **Variable** | Longitud del texto y hashtags: de 1 a 4 líneas |
| **Botón de llamada a la acción** | **Variable** | Sólo en anuncios; no existe en orgánico |
| **Barra de progreso y controles** | **Variable** | Aparece al tocar; en vídeo largo, siempre |

De ahí que la medida honesta no sea un número sino **dos**: el caso vacío y el caso lleno. Se mide con
el caption más largo que vayas a usar de verdad, no con el campo en blanco.

---

## El método: carta de medida + captura + resta

La idea es simple y no admite discusión: publicas una imagen donde **cada píxel dice dónde está**, la
capturas con la interfaz encima, y restas. Lo que cambió, es lo que la plataforma pinta.

### 1 · La carta

```python
A, B = (214, 26, 160), (26, 188, 132)          # magenta y verde: imposibles de imitar
im = Image.new("RGB", (W, H), A); d = ImageDraw.Draw(im)
for i in range(50):                             # una franja por cada 2% de la altura
    y0, y1 = int(H*i/50), int(H*(i+1)/50)
    d.rectangle([0, y0, W, y1], fill=A if i % 2 else B)
    d.text((14, y0+4), f"{i*2:02d}%  y={y0}", fill=(255,255,255), font=f)
for j in range(1, 10):                          # regla de ancho cada 10%
    x = int(W*j/10); d.line([x, 0, x, H], fill=(255,236,0), width=3)
```

**La carta no puede llevar negro ni blanco.** Lo aprendí rompiéndolo: la primera versión alternaba
negro y rojo, la interfaz también es negra, y la resta no vio la franja superior —dio 0 px arriba donde
había 150—. Dos colores saturados que ninguna app usa y el problema desaparece.

La carta se convierte en vídeo de 6 s (`ffmpeg -loop 1 -i carta.png -t 6 ...`), porque las plataformas
verticales no aceptan imágenes fijas como Reel.

### 2 · La resta

```python
dif = ImageChops.difference(carta, cap).convert("L").point(lambda p: 255 if p > 28 else 0)

def franja(rango, largo, eje):                  # líneas tapadas en más del 35%
    return [i for i in rango
            if sum(1 for j in range(0, largo, 4)
                   if (px[j, i] if eje == "y" else px[i, j])) / (largo/4.0) > 0.35]
```

El umbral de 28 sobre 255 aguanta la recompresión de la plataforma sin dar falsos positivos. El 35%
de la línea evita que un icono suelto declare tapada una fila entera; para la columna de iconos hay
una medida aparte, por columna.

### 3 · La calibración (el paso que casi nadie hace)

Antes de creerse un resultado, **se inyecta una interfaz conocida y se comprueba que la sale**. Hecho
el 11-sep-2026: sobre la carta de 1080×1920 se pintaron a propósito 150 px arriba, 360 abajo y una
columna de 150 px a la derecha. La resta devolvió:

```
arriba    151 px   0.079 de la altura
abajo     360 px   0.188
der       150 px   0.139
útil    x 0-929  y 151-1559   (929x1408 px)
columna más tapada: x=930 (1092 px de alto, 0.569)
```

Un píxel de diferencia arriba, por el borde del antialiasing. **Una herramienta de medida que no se ha
calibrado contra una verdad conocida no es una herramienta: es una opinión con decimales.**

---

## Dónde se guarda el resultado

Un archivo por red y por fecha, nunca un número suelto en la cabeza:

```json
{"red": "reels", "fecha": "2026-09-11", "dispositivo": "Redmi Note 12, 1080x2400",
 "lienzo": [1080, 1920], "caption": "3 líneas con 4 hashtags",
 "arriba": 269, "abajo": 672, "izq": 65, "der": 65,
 "columna_iconos": {"x": 930, "alto": 1092},
 "metodo": "carta+diff, umbral 28, calibrado contra UI inyectada"}
```

Con el dispositivo dentro, porque **la misma app tapa distinto en un teléfono con muesca que en uno
sin ella**, y sin esa línea el archivo no se puede reproducir ni discutir.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Copiar cifras de un blog sin fecha | Se diseña contra una interfaz que ya no existe |
| Carta con negro o blanco | La resta no ve la franja superior: da 0 px donde hay 150 |
| No calibrar la herramienta contra una interfaz conocida | Se confunde un fallo del script con un dato |
| Medir con el caption vacío | En producción el caption real sube el bloque inferior 200 px |
| Medir sólo el caso orgánico | En pauta aparece el botón de CTA y se come otra franja |
| Guardar el número sin el dispositivo | Irreproducible: la muesca cambia la franja superior |
| Declarar tapada una fila por un icono suelto | Zona segura mucho más pequeña de lo real |
| Comparar capturas de tamaños distintos sin reescalar | Todo sale desplazado y el diagnóstico es ruido |
| Medir una vez y no volver | Es el error original, otra vez, seis meses después |

## Relacionado

`45` las cifras por plataforma con su fecha · `418` el protocolo completo de medida en el teléfono ·
`416` el caso del reproductor de YouTube · `410` el mapa de intocables · `92` especificaciones de
exportación · `376` la advertencia sobre las cifras de TikTok, que no son oficiales
