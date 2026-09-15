# 66 · Grano y textura

**Qué resuelve:** un recorte limpio sobre un fondo con grano no empata: se ve pegado
encima, como un PNG. El grano es lo que mete todos los materiales bajo la misma piel —
y, cuando se elige bien, además fecha la imagen.

---

## Cuál para qué

| Textura | Dice | Se usa en |
|---|---|---|
| **Película** | Esto es material de época, filmado | Fotos anteriores a los 90, reconstrucciones, retratos |
| **VHS** | Esto se grabó en vídeo, entre 1980 y 2002 | Noticieros, cámaras de seguridad de la época, juicios |
| **Fotocopia** | Esto es un papel que pasó por una oficina | Expedientes, memorandos, listados, formularios |
| **Escaneo** | Esto es un papel que alguien digitalizó hoy | Cartas, contratos, cheques, documentos manuscritos |

**No se mezclan en el mismo elemento.** Un documento con grano de película no dice nada:
dice que se aplicaron dos filtros. Cada pieza tiene una procedencia y una sola textura.

## Dónde se aplica: al ELEMENTO, no al vídeo

El fondo ya trae su propia capa de grano (capa 5 de `50`) y es la firma del canal. Si al
final se aplica ruido sobre el vídeo entero pasan dos cosas: el grano del fondo se
duplica y se ve sucio, y el bitrate se dispara porque el ruido temporal es lo más caro
de comprimir que existe. Un episodio de 90 s puede duplicar de peso por eso.

```
✅ grano en el PNG del recorte, al generarlo
✅ grano por elemento en el filtro de la escena, cuando debe temblar
❌ noise sobre el concat final
```

## Grano horneado en el PNG (lo normal)

Para casi todo, el grano se hornea al generar la pieza y no cuesta nada en render. En
HTML es la misma receta de los fondos:

```html
<svg width="0" height="0"><filter id="gr">
  <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="5"/>
  <feColorMatrix type="saturate" values="0"/></filter></svg>

<div style="position:absolute;inset:0;z-index:9;pointer-events:none;
     opacity:.20;mix-blend-mode:overlay">
  <svg viewBox="0 0 600 400" preserveAspectRatio="none" style="width:100%;height:100%">
    <rect width="600" height="400" filter="url(#gr)"/></svg></div>
```

`baseFrequency` manda el tamaño del grano: **0,85** es grano fino de foto; **0,35** es
grano grueso de película forzada; por debajo de 0,15 ya son manchas.

En PIL, sobre una pieza ya dibujada:

```python
import random
from PIL import Image, ImageChops
def grano(im, fuerza=18, semilla=5):
    """Ruido monocromo sumado sólo donde el PNG es opaco."""
    random.seed(semilla)
    r = Image.frombytes("L", im.size,
        bytes(random.randint(128-fuerza, 128+fuerza) for _ in range(im.size[0]*im.size[1])))
    rgb = ImageChops.overlay(im.convert("RGB"), Image.merge("RGB", (r, r, r)))
    rgb.putalpha(im.getchannel("A"))          # el alfa NO se toca
    return rgb
```

## Grano temporal en ffmpeg (cuando debe temblar)

El grano de película **se mueve**. Si un retrato va a estar 4 segundos en pantalla, un
grano fijo lo delata como imagen quieta. Ahí se aplica en el filtro, con el cuidado de
**no ensuciar el alfa**:

```
[1:v]format=rgba,split=2[col][alf];
[alf]alphaextract[a];
[col]noise=alls=9:allf=t+u,format=rgba[c];
[c][a]alphamerge[gra]
```

Sin ese `alphaextract`/`alphamerge`, `noise` también motearía el canal alfa y el borde
del recorte quedaría comido, con puntos transparentes dentro de la figura.

- `alls` = fuerza (0-100). **6-12** para película; **14-22** para VHS; más de 25 es nieve
- `allf=t` = el ruido cambia cada fotograma (temporal). Sin la `t` el grano queda clavado
- `allf=u` = ruido uniforme; sin la `u` es gaussiano y se ve más blando

## Las cuatro recetas

```bash
# PELÍCULA — grano temporal fino, negros levantados, saturación baja
noise=alls=9:allf=t+u,curves=all='0/0.06 0.5/0.5 1/0.96',eq=saturation=0.86

# VHS — detalle perdido, croma desplazado y arrastrado, ruido grueso
scale=iw/2.4:-2,scale=iw*2.4:-2:flags=neighbor,
chromashift=cbh=4:crh=-3,noise=alls=18:allf=t+u,eq=saturation=1.14:contrast=1.06

# FOTOCOPIA — sin color, contraste duro, ruido FIJO (el papel no tiembla)
format=gray,eq=contrast=1.95:brightness=0.05,noise=alls=6:allf=u,
unsharp=5:5:0.7,format=rgba

# ESCANEO — gris cálido, blancos altos, un grado de inclinación
format=gray,curves=all='0/0.10 0.5/0.56 1/1',colorbalance=rm=0.05:gm=0.02,
rotate=0.0122:c=none:ow=rotw(0.0122):oh=roth(0.0122)
```

La bajada y subida de escala del VHS es lo que **realmente** hace el efecto: pierde
detalle de verdad. Un filtro de ruido encima de una imagen nítida sigue viéndose nítida
con puntos, que es el aspecto de plantilla que se quiere evitar.

**La fotocopia lleva ruido FIJO** (`allf=u`, sin `t`). Un papel escaneado cuyo grano
tiembla se lee como vídeo con filtro; el papel está quieto porque es papel.

## El grado de inclinación

Escaneo y fotocopia van girados entre **0,5° y 1,4°**. Nadie pone un papel recto en un
escáner. Ese grado es más de la mitad del efecto, y es gratis: `"rot": 0.9` en la tabla
del guion visual.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| `noise` sobre el vídeo final | Grano duplicado sobre el fondo y el peso se dispara |
| `noise` sobre rgba sin separar el alfa | El borde del recorte se come y salen puntos transparentes |
| Dos texturas en el mismo elemento | No dice de dónde viene la pieza: dice que se filtró |
| VHS sólo con ruido, sin bajar la escala | Imagen nítida con puntos: plantilla |
| Fotocopia con ruido temporal | Papel que tiembla: se lee como vídeo, no como documento |
| `baseFrequency` por debajo de 0,15 | Manchas, no grano |
| Escaneo perfectamente recto | Delata que es un `div`, no un papel |
| Grano fijo en un retrato de 4 s | Confirma que la imagen está quieta |

## Relacionado

`23` empatar recorte y fondo · `52` texturas de fondo · `50` la capa de grano del canal · `35` animar una foto fija · `68`
