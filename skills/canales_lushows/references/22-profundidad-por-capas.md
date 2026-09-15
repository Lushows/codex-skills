# 22 · Profundidad por capas

**Qué resuelve:** todo está pegado en el mismo plano y el cuadro se ve plano y apretado.
Como la opacidad no se puede tocar, la profundidad se construye con **escala,
desenfoque, saturación, sombra y velocidad de deriva** — que es como funciona una
cámara de verdad.

---

## Los cuatro planos

| Plano | Ancho vs canónico | `gblur` σ | Saturación | Brillo | Deriva px/s | Sombra (offset · blur) |
|---|---|---|---|---|---|---|
| **Fondo** | full-bleed 4320 px | — (ya construido) | — | — | zoom 8-16% | — |
| **Medio** | 55-75% | 2,0 - 3,2 | 0,80 - 0,86 | −0,05 | 3 - 8 | (4, 6) · 6 |
| **Frente** | 100% | 0 | 1,00 | 0 | 8 - 26 | (7, 11) · 10 |
| **Primerísimo** | 115-140% | 0,8 - 1,4 | 1,02 | +0,02 | 26 - 45 | (14, 20) · 18 |

El primerísimo plano lleva **algo** de desenfoque a propósito: está más cerca que el
plano de foco, y una cámara real lo desenfocaría. Sin ese detalle se lee como un
recorte grande, no como algo delante.

**El parallax es la clave.** Las velocidades guardan proporción **1 : 2,2 : 3,6**
(medio : frente : primerísimo). Si todo deriva igual, no hay profundidad aunque haya
desenfoque.

## Regla de reparto por escena

```
1 fondo   +   0-1 primerísimo   +   1-2 frente   +   1-2 medio
```

- El elemento que **sostiene la frase va SIEMPRE en frente**. Nunca en medio.
- El primerísimo plano no lleva rótulo ni texto: está desenfocado, sería ilegible.
- Como mucho **un** primerísimo vivo a la vez; dos tapan el cuadro.

## Cocinar el plano medio con PIL (recomendado)

Se hornea en el PNG una sola vez, en vez de pagarlo en cada fotograma del render:

```python
from PIL import Image, ImageEnhance, ImageFilter

def a_plano_medio(png, salida, sigma=2.4, sat=0.83, brillo=0.95):
    """Manda un recorte al plano medio. Desenfoca TAMBIEN el alfa: si la silueta
    queda nitida y el interior borroso, se lee como un error de render."""
    im = Image.open(png).convert("RGBA")
    a = im.split()[3]
    rgb = im.convert("RGB").filter(ImageFilter.GaussianBlur(sigma))
    rgb = ImageEnhance.Color(rgb).enhance(sat)
    rgb = ImageEnhance.Brightness(rgb).enhance(brillo)
    a = a.filter(ImageFilter.GaussianBlur(sigma * 0.5))
    Image.merge("RGBA", (*rgb.split(), a)).save(salida)
```

⚠️ **La sombra hay que regenerarla**, no heredarla. Un recorte tratado con
`revista.py` trae la sombra del plano frente (offset 7/11, blur 10). Si lo mandas al
plano medio con esa sombra, el desenfoque dice "lejos" y la sombra dice "cerca": el
cuadro se lee mal sin que se sepa por qué. Pasa `sombra=False` en `modo_revista()` y
compón la sombra corta aparte, o vuelve a generar el recorte con esos valores.

## Hacerlo en el render (cuando el recurso se reutiliza en dos planos)

En el filtro del elemento de `motor.py`, entre el `scale` y el `fade`:

```
[3:v]scale=420:-1,format=rgba,gblur=sigma=2.4,
     eq=saturation=0.83:brightness=-0.05,
     rotate=…,fade=t=in:…[e3]
```

Cuesta más CPU por fotograma pero evita duplicar PNG en `recortes/`. Para un elemento
que aparece una vez, hornéalo; para uno que sale seis veces en dos planos distintos,
hazlo en el filtro.

## Profundidad sin desenfoque: el escalón de tamaño

Cuando el material no admite desenfoque (un documento que hay que poder leer), la
profundidad se hace solo con escala y sombra. El escalón tiene que ser **grande**:

| Salto de tamaño | Cómo se lee |
|---|---|
| menos del 20% | Dos elementos del mismo plano, uno mal escalado |
| **35 - 55%** | **Dos planos distintos. El escalón correcto** |
| más del 70% | El pequeño desaparece: pesa menos de 8 (`21`) |

## Ordenar la profundidad en la tabla de eventos

`motor.py` encadena los overlays en el orden de la lista: **el último de `elementos`
queda encima**. Así que el orden de la lista ES el orden de profundidad. Escríbela
siempre de atrás hacia delante:

```python
"elementos": [
    {"r": "tunel_sinaloa", "…": "…", "w": 380, "deriva": (4, 0)},   # medio
    {"r": "chapo_us",      "…": "…", "w": 620, "deriva": (9, -4)},  # frente
    {"r": "billete_borde", "…": "…", "w": 900, "deriva": (34, 0)},  # primerisimo
]
```

Da igual que sus vidas no se solapen: mantener el orden hace la tabla legible y evita
sorpresas cuando alguien alarga un `dura`.

## Comprobación rápida

Sobre un fotograma del render, tapando la mitad del cuadro con la mano: si no se puede
decir cuál de los elementos está delante, no hay profundidad — hay collage plano.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Desenfocar el RGB y dejar el alfa nítido | Silueta recortada con interior borroso: parece un fallo |
| Heredar la sombra del plano frente en el medio | Señales contradictorias de distancia |
| Misma deriva en los tres planos | No hay parallax: el desenfoque no basta |
| Rótulo sobre un primerísimo plano | Ilegible; el texto va siempre en frente nítido |
| Dos primerísimos a la vez | Tapan el cuadro y no queda dónde mirar |
| Escalón de tamaño menor del 20% | Se lee como error de escala, no como profundidad |
| Bajar opacidad para "alejar" | Doble exposición: rompe el lenguaje del canal |

## Relacionado

`21` peso visual y jerarquía · `23` empatar recorte y fondo · `33` parallax real ·
`25` el borde de papel · `53` luz y viñeta
