# 442 — Papel, polvo y arañazo: la textura barata que sí sobrevive

El grano es la textura cara. El polvo, la raya y el borde de papel son la textura **gratis**, y
además son las únicas que aguantan un recomprimido de red. Este módulo mide las dos cosas y da las
dosis en la única unidad que no depende del tamaño de la pieza.

Frontera: la *elección* de textura por procedencia (película / VHS / fotocopia / escaneo) vive en
`canales/66` y no se repite aquí. El borde de papel del collage vive en `canales/25`. Aquí: **cuánto
polvo, cuánta raya, y qué le hace la compresión a cada uno.**

---

## 1. El hallazgo: cuestan cero

Un fotograma fijo de collage 1080p, 1 s, libx264 `preset medium`:

| | CRF 18 | vs limpio | CRF 24 | vs limpio |
|---|---|---|---|---|
| limpio | 437 317 B | — | 218 904 B | — |
| + polvo 40 motas/Mpx | 435 528 B | **−0,4 %** | 219 160 B | **+0,1 %** |
| + arañazo, 3 rayas | 435 019 B | **−0,5 %** | 219 010 B | **+0,05 %** |
| + `noise=alls=5:allf=t+u` | 1 154 683 B | **+164 %** | 188 362 B | **−14 %** |

Dos lecturas, las dos importantes:

- **El polvo y la raya son gratis.** La diferencia está dentro del ruido de medición. Son rasgos
  escasos, localizados y de alto contraste: el codificador los mete en un puñado de bloques y ya.
- **El grano a CRF 24 hace el archivo más pequeño Y la imagen peor.** −14 % de bytes con el grano ya
  destruido: el ruido subió la complejidad aparente de cada bloque, la cuantización adaptativa
  repartió peor, y se pagó con detalle del material. Es el peor negocio posible: pagas en calidad y
  ni siquiera te llevas la textura.

Y lo que sobrevive, medido como contraste conservado sobre los píxeles tocados:

| | CRF 18 | CRF 24 |
|---|---|---|
| polvo | **86,8 %** | **81,9 %** |
| arañazo | 89,1 % | 88,7 % |
| grano sobre degradado (de `editpro/446`) | 36 % | **0,2 %** |

---

## 2. Polvo: la dosis en motas por megapíxel

La única dosis honesta. «40 motas» no significa nada si no se dice sobre qué superficie.

```python
import numpy as np
from PIL import Image, ImageDraw

def polvo(im, por_megapixel=40, semilla=3, oscuro=0.75):
    """Motas del escáner. Van SOBRE la pieza, no dentro: no se reescalan con ella."""
    rng = np.random.default_rng(semilla)
    w, h = im.size
    cp = im.convert("RGB").copy(); d = ImageDraw.Draw(cp)
    for _ in range(int(por_megapixel * w * h / 1e6)):
        x, y = rng.integers(0, w), rng.integers(0, h)
        r = rng.choice([0.5, 0.5, 1.0, 1.0, 1.5, 2.5], p=[.30, .25, .20, .15, .07, .03])
        claro = rng.random() < 0.22                    # el 22% son CLARAS: pelusa, no mugre
        v = 235 if claro else int(255 * (1 - oscuro))
        d.ellipse([x-r, y-r, x+r, y+r], fill=(v, v, v))
    return cp
```

| motas/Mpx | píxeles tocados | Sensación |
|---|---|---|
| 10 | 0,004 % | negativo bien guardado |
| 25 | 0,012 % | archivo normal |
| **40** | **0,018 %** | **el valor de trabajo** |
| 80 | 0,039 % | negativo maltratado |
| 160 | 0,082 % | ya es un efecto, no una procedencia |

Los tres detalles que separan el polvo creíble del polvo de plantilla:

1. **Tamaños desiguales y sesgados a lo pequeño.** El 55 % de las motas miden medio píxel. Un polvo
   con todas las motas iguales se lee como una trama.
2. **Un 22 % de motas claras.** El polvo del escáner tapa luz (oscuro) pero la pelusa la refleja
   (claro). Solo oscuras = suciedad digital.
3. **Va sobre la pieza, después de escalarla.** Si el polvo entra en el PNG antes del `zoompan`, se
   agranda con la imagen y pasa de mota a mancha.

---

## 3. Arañazo: nunca recto de arriba abajo

```python
from PIL import Image, ImageFilter, ImageDraw
def aranazo(im, n=3, semilla=5, fuerza=22):
    rng = np.random.default_rng(semilla); w, h = im.size
    capa = Image.new("L", (w, h), 0); d = ImageDraw.Draw(capa)
    for _ in range(n):
        x, y = rng.integers(int(w*0.06), int(w*0.94)), 0
        while y < h:                                   # la raya se INTERRUMPE
            largo = rng.integers(int(h*0.10), int(h*0.45))
            if rng.random() < 0.7:
                d.line([x+rng.integers(-1,2), y, x+rng.integers(-1,2), min(y+largo,h)],
                       fill=int(fuerza*rng.uniform(0.5,1.0)), width=int(rng.choice([1,1,2])))
            y += largo + rng.integers(int(h*0.02), int(h*0.20))
    capa = capa.filter(ImageFilter.GaussianBlur(0.6))
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    return Image.fromarray(np.clip(a + np.asarray(capa, np.float32)[...,None], 0, 255).astype("uint8"))
```

| rayas | píxeles tocados | Cuándo |
|---|---|---|
| 1 | 0,045 % | material cuidado |
| **3** | **0,134 %** | **el valor de trabajo** |
| 6 | 0,378 % | copia de proyección |
| 12 | 0,811 % | efecto declarado |

`fuerza=22` sobre 255 da un delta medio de **8,5 niveles**: por debajo del umbral consciente, y aun
así conserva el 89 % del contraste tras CRF 24. El desenfoque de 0,6 px es obligatorio: una línea de
1 px perfectamente dura es lo que delata un `drawLine`.

---

## 4. Quieto o en movimiento: depende de la procedencia

| Material | Polvo / raya | Por qué |
|---|---|---|
| Papel escaneado, fotocopia, documento | **congelado** con la pieza | La suciedad está en el papel, y el papel no se mueve |
| Negativo, película, noticiero | **cambia cada fotograma** | La suciedad está en la ventanilla del proyector |

Congelado se hornea en el PNG. Por fotograma se genera una tira de N variantes y se alterna, o se
resuelve con `noise` de pico alto y densidad baja. La regla general y la medida que la comprueba están
en `editpro/441`; aquí solo la asignación.

---

## 5. Lo que el polvo NO arregla

No arregla el color. Una foto moderna a todo color con polvo encima sigue siendo una foto moderna con
polvo encima. Eso se resuelve virando, y la métrica correcta para saber si ya empata **no es la
saturación**: la saturación no baja de forma monótona al envejecer (61,1 → 48,0 → 52,5 medido en
`canales/197`, porque el sepia tiene saturación propia). La medida que sí sirve es la **dispersión de
tono**, con umbral ≤ 0,005. Está resuelta y medida ahí: úsala, no la reescribas.

Tampoco arregla un anacronismo (`canales/198`) ni un alfa sucio (`canales/196`): el polvo sobre un
halo translúcido solo añade motas al halo.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dosificar en «número de motas» sin referencia a la superficie | La misma receta da polvo fino en 4K y viruela en 720p |
| Todas las motas del mismo tamaño | Se lee como trama, no como suciedad |
| Solo motas oscuras | Falta la pelusa clara: suciedad digital |
| Meter el polvo en el PNG antes de escalar o de animar | Las motas crecen y viajan con la pieza |
| Raya recta de borde a borde | Delata el `drawLine`; la raya real se interrumpe |
| Raya de 1 px sin desenfoque | Idem, y además desaparece al reescalar |
| Polvo temporal en un documento | Papel que hormiguea |
| Usar polvo para tapar un problema de color | Ver `canales/197`: el problema es la dispersión de tono |
| Subir el grano cuando lo que faltaba era materia | +164 % de archivo frente a 0 % del polvo |

---

## Relacionado

`editpro/441` grano temporal o congelado · `editpro/440` grano: por qué y cuánto · `editpro/446`
ruido que sobrevive a la compresión · `editpro/447` la textura que delata a la IA ·
`editpro/57` VHS, halftone y tramado como efecto declarado ·
`canales/66` las cuatro texturas por procedencia · `canales/25` el borde de papel ·
`canales/197` envejecer para que empate (dispersión de tono) · `canales/196` limpiar el alfa ·
`canales/198` el anacronismo
