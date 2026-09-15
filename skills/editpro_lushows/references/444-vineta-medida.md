# 444 — Viñeta medida: cuántos pasos de luz cierra cada ángulo

`editpro/66` ya dice la dosis de trabajo (`PI/5`) y ya avisa de que en vertical hay que bajarla. Este
módulo no repite ninguna de las dos cosas: las **mide**, y con la medida aparece un hecho que la
advertencia cualitativa esconde — la viñeta de ffmpeg **no depende del formato en la esquina, pero sí
en el borde**, y el borde es donde vive el texto.

---

## 1. Cómo se mide: tarjeta gris, nunca material

Sobre imagen real no se puede medir una viñeta: lo que mides es el contenido. La medida se hace sobre
un gris plano de 128, que es el equivalente a `canales/161` («auditar sobre gris») para el color.

```python
# vin.py — la tabla completa en un minuto
import subprocess, numpy as np, math
from PIL import Image
def render(src, ang):
    subprocess.run(["ffmpeg","-v","error","-y","-i",src,"-vf",f"vignette={ang}","-frames:v","1","_v.png"],check=True)
    return np.asarray(Image.open("_v.png").convert("L")).astype(np.float32)
def informe(src, ang):
    a = render(src, ang); h, w = a.shape
    centro  = a[h//2-20:h//2+20, w//2-20:w//2+20].mean()
    esquina = a[0:40, 0:40].mean()
    borde   = a[0:40, w//2-20:w//2+20].mean()      # medio del borde superior
    return centro, esquina, borde, math.log2(esquina/centro)
```

Tarjetas: `color=c=gray:s=1920x1080` y `color=c=gray:s=1080x1920`.

---

## 2. La tabla, medida

**16:9 (1920×1080), gris 128**

| ángulo | rad | centro | esquina | % del centro | pasos de luz | borde superior |
|---|---|---|---|---|---|---|
| `PI/8` | 0,393 | 128,0 | 94,7 | 74,0 % | −0,43 | 93,3 % |
| `PI/6` | 0,524 | 128,0 | 74,1 | 57,9 % | −0,79 | 88,4 % |
| `PI/5.6` | 0,561 | 128,0 | 68,0 | 53,2 % | −0,91 | 86,7 % |
| `PI/5` | 0,628 | 128,0 | 57,3 | 44,7 % | −1,16 | 83,6 % |
| `PI/4.6` | 0,683 | 128,0 | 48,9 | 38,2 % | −1,39 | 80,9 % |
| `PI/4` | 0,785 | 128,0 | 34,5 | 26,9 % | −1,89 | 75,4 % |
| `PI/3` | 1,047 | 127,9 | 9,5 | 7,4 % | −3,75 | 60,0 % |

**9:16 (1080×1920), gris 128**

| ángulo | esquina | % del centro | pasos | **borde superior** |
|---|---|---|---|---|
| `PI/8` | 94,7 | 74,0 % | −0,43 | 79,5 % |
| `PI/6` | 74,1 | 57,9 % | −0,79 | **66,1 %** |
| `PI/5.6` | 68,0 | 53,1 % | −0,91 | 62,0 % |
| `PI/5` | 57,2 | 44,7 % | −1,16 | 54,6 % |
| `PI/4.6` | 48,8 | 38,2 % | −1,39 | **48,6 %** |
| `PI/4` | 34,5 | 26,9 % | −1,89 | 37,7 % |
| `PI/3` | 9,5 | 7,4 % | −3,75 | 15,4 % |

Los dos hechos:

1. **La esquina es idéntica en los dos formatos.** El filtro trabaja en coordenadas normalizadas, así
   que `PI/5` cierra la esquina al 44,7 % tanto en horizontal como en vertical. Nadie tiene por qué
   adivinarlo: está medido.
2. **El borde de en medio no.** En 16:9 `PI/5` deja el borde superior al 83,6 %; en 9:16 lo deja al
   54,6 %. **La misma orden produce media parada de luz de diferencia en el sitio exacto donde va el
   rótulo.** Eso es lo que hay detrás de «en vertical baja la dosis»: no es prudencia, son 29 puntos
   porcentuales.

---

## 3. El caso real del canal

En `piloto/acabar.py` quedó este comentario:

```python
"vignette=PI/5.6,"                 # antes PI/4.6: cerraba demasiado
```

Con la tabla delante se ve exactamente qué se corrigió: el borde superior pasó de **80,9 % a 86,7 %**
en 16:9. En el episodio anterior el remate era `PI/6.0` (`ep01-lustig/acabar.py`), o sea 88,4 %. La
progresión PI/6 → PI/4.6 → PI/5.6 es un ajuste de **1,7 puntos de borde**, y aun así se notó. La
viñeta se juzga por el borde, no por la esquina.

Y la viñeta del fondo HTML, que es otra capa y se suma a esta:

```python
# piloto/episodio01/fondos.py — "La vineta NO pasa de .54: al .70 se comia el
# tercio exterior, que es donde faltaba peso en el reparto 3x3."
radial-gradient(84% 78% at 50% 46%, transparent 42%, rgba(0,0,0,.50) 100%)
```

**Dos viñetas se multiplican.** El degradado del fondo llega a `rgba(0,0,0,.50)` en su parada del
100 %, que cae dentro del cuadro, así que la esquina se queda con el factor 0,50 entero. Con el
`PI/5.6` del remate encima: 0,50 × 0,532 = **26,6 %** del centro — es decir, **la esquina acaba
exactamente donde la dejaría un `PI/4` solo** (26,9 %), que es un ángulo que nadie habría aprobado si
se lo pides de una vez. Antes de subir el ángulo hay que comprobar si el fondo ya trae la suya
(`canales/53`).

---

## 4. El precio en bits, que nadie cuenta

Sobre 5 s de collage 1080p, CRF 12:

| | tiempo | ×ref | bytes | ×ref |
|---|---|---|---|---|
| sin filtro | 22,1 s | 1,00 | 5 979 626 | 1,00 |
| `vignette=PI/5.6` | 26,9 s | 1,22 | 7 842 005 | **1,31** |

Un +31 % de archivo por oscurecer las esquinas. La razón es que la viñeta **crea un degradado nuevo**
—suave, extenso y oscuro— justo en las zonas que antes eran planas y baratas. Y ese degradado es
material de primera para bandear (`editpro/66` §4): en los negros hay menos niveles disponibles, así
que la misma rampa se cuantiza más grueso.

Consecuencia operativa: **si pones viñeta, el grano deja de ser opcional**, y tiene que ir *después*
de la viñeta para dispersar sus escalones. El orden del remate del canal —`eq` → `noise` →
`vignette`— pone el grano **antes**, y eso deja la rampa de la viñeta sin dither. Es un orden
discutible; ver `editpro/440` §2 y la cadena de `editpro/66`.

---

## 5. Desplazar el centro en vertical

Si el sujeto está arriba (encuadre de retrato en 9:16) la viñeta le come la cara. En vez de bajar el
ángulo, se mueve el centro:

```bash
ffmpeg -i in.mp4 -vf "vignette=a=PI/5:x0=w*0.5:y0=h*0.40:eval=init,format=yuv420p" out.mp4
```

`eval=init` calcula la máscara una vez: es lo que hace que no cueste por fotograma. Sin él, ffmpeg la
recalcula en cada cuadro sin ninguna ganancia.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Medir la viñeta sobre material en vez de sobre gris plano | Mides el contenido; el número no sirve para comparar |
| Juzgarla por la esquina | La esquina es igual en 16:9 y 9:16; el problema está en el borde |
| Usar el mismo ángulo en horizontal y en vertical | 29 puntos de diferencia en el borde superior a `PI/5` |
| Sumar viñeta de fondo y viñeta de remate sin multiplicar | `.50` × `PI/5.6` ≈ 24,9 %: más cerrada que `PI/4` |
| Viñeta sin grano detrás | Anillos en las esquinas al recomprimir |
| Poner el grano antes de la viñeta | La rampa nueva de la viñeta se queda sin dither |
| Omitir `eval=init` con `x0`/`y0` | La máscara se recalcula en cada fotograma sin ganancia |
| Dar por gratis la viñeta | +31 % de archivo medido |

---

## Relacionado

`editpro/66` viñeta, nitidez y textura (la dosis de trabajo y el orden de la cadena) ·
`editpro/440` grano: por qué y cuánto (el antibandeo que la viñeta necesita) ·
`editpro/445` halación y sangrado · `editpro/449` medir si la textura suma ·
`canales/53` luz y viñeta · `canales/161` auditar sobre gris · `canales/50` el esqueleto de capas
del fondo
