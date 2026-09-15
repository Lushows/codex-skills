# 292 · Empatar recorte y fondo: la compuerta barata

**Qué resuelve:** `23` explica los cuatro ejes del empate (luz, temperatura, grano,
ángulo) y cómo arreglar tres de ellos. `163` mide la visibilidad **sobre el vídeo ya
renderizado**, con `dL` y `frac`, y tarda 4 min 3 s. Falta la pieza de en medio: una
compuerta que cueste segundos y se pueda pasar **antes** de montar, para que el render
caro no se gaste en un elemento que no se ve. Eso es lo que hace ahora `auditar.py`.

Nada de `23` ni de `163` se repite. Aquí: la medida barata, el caso que encontró y el
protocolo de arreglo con su número.

---

## La compuerta, tal como está en `auditar.py`

Se compara la luminancia media de los **píxeles opacos del recorte** con la del **trozo de
fondo que le toca debajo**. Sin renderizar, sin ffmpeg, sobre miniaturas.

```python
LUMA_MIN = 12.0      # diferencia en la escala 0-255

def _luma_elem(png):
    """Solo lo que se ve: los pixeles con alfa > 128. El margen crema y la sombra
    entran, y deben entrar: en pantalla tambien se ven."""
    px = list(Image.open(png).convert("RGBA").resize((96, 96)).getdata())
    vis = [(0.299*r + 0.587*g + 0.114*b) for r, g, b, a in px if a > 128]
    return sum(vis) / len(vis) if len(vis) > 200 else None

def _luma_fondo(fondo_png, caja_px):
    """El trozo que le toca debajo, no la lamina entera: los fondos llevan vineta y
    el borde puede estar 25 L por debajo del centro (23)."""
    im = Image.open(fondo_png).convert("L").resize((192, 108))
    x0, y0 = int(caja_px[0]/1920*192), int(caja_px[1]/1080*108)
    x1, y1 = int(caja_px[2]/1920*192), int(caja_px[3]/1080*108)
    d = list(im.crop((x0, y0, max(x0+1, x1), max(y0+1, y1))).getdata())
    return sum(d) / len(d)
```

Tres decisiones que la hacen barata y aun así útil:

- **192×108 para el fondo y 96×96 para el recorte.** Se está midiendo una masa, no un
  detalle: a esa resolución el resultado no cambia y la auditoría entera sigue tardando
  segundos. La medida fina, con erosión y anillo, es `163`.
- **Alfa > 128, no > 200.** Aquí interesa el bulto que va a estar en pantalla, papel y
  sombra incluidos. `163` erosiona 16 px justamente para lo contrario, porque allí se
  pregunta si se lee el contenido.
- **Luminancia BT.601 (`0,299 / 0,587 / 0,114`)** y no Rec.709. Es la que usa la
  compuerta; `163` usa 709. Para un umbral de cribado la diferencia es menor que el ruido
  de la miniatura, pero conviene saber que son dos escalas y no mezclar sus números.

## El caso: 1,1 puntos sobre 255 durante 3,2 s

En la escena `torre`, `torre_citroen_noche` —la torre iluminada con el anuncio de
Citroën, el plano del remate de la leyenda— caía sobre el fondo de esa misma escena.
Medido con el PNG original, que quedó guardado al lado:

| Elemento | Luz del recorte | Luz del fondo debajo | Diferencia |
|---|---|---|---|
| `torre_citroen_noche_original` | 96,69 | 97,78 | **1,09** |
| `bajo_la_torre_original` | 72,51 | 69,96 | **2,54** |

**1,09 puntos sobre 255.** El elemento estaba declarado, colocado, sin solapes, sumaba
cobertura, aparecía en el reparto del cuadro y **duraba 3,2 s en pantalla sin verse**.
Ninguna de las otras medidas de la auditoría lo nota: todas cuentan presencia.

Y se entiende por qué pasó: una foto nocturna se vira y se apaga para empatar la paleta
del canal (`197`), y el fondo de esa escena es oscuro por diseño. Los dos tratamientos son
correctos por separado y se anulan al juntarse.

## El arreglo: la gamma mínima que separa

Lo que **no** se hace: subir la opacidad (siempre es 1), aclarar el fondo (se lleva la
escena entera por delante) o repintar el recorte a mano.

Lo que se hace: **la gamma más suave que cruce el umbral, y ni un paso más.**

```python
import numpy as np
from PIL import Image

def aclarar_minimo(png, luz_fondo, objetivo=16.0, paso=0.02):
    """La gamma MENOR que separa. Guardar el original al lado ANTES de tocar."""
    a = np.asarray(Image.open(png).convert("RGBA"))
    al = a[:, :, 3] > 128
    base = np.arange(256, dtype=np.float64) / 255.0
    for g in np.arange(1.00, 0.55, -paso):              # g < 1 aclara
        tabla = (255 * base ** g).astype(np.uint8)
        rgb = tabla[a[:, :, :3]]
        luz = (0.299*rgb[..., 0] + 0.587*rgb[..., 1] + 0.114*rgb[..., 2])[al].mean()
        if abs(luz - luz_fondo) >= objetivo:
            return round(float(g), 2), float(luz)
    return None, None
```

Aplicado a los dos casos, la respuesta salió idéntica: **gamma 0,80**. Verificado hoy
buscando la gamma que mejor explica el PNG actual a partir del original guardado —error
medio **0,25 sobre 255**, o sea que es exactamente esa transformación y ninguna otra:

| Elemento | Luz antes | Luz después | Diferencia con su fondo |
|---|---|---|---|
| `torre_citroen_noche` | 96,44 | 115,73 | 1,09 → **18,18** |
| `bajo_la_torre` | 72,30 | 89,20 | 2,54 → **19,41** |

**Se guarda el original al lado, con sufijo `_original`.** No es sentimentalismo de
archivo: la gamma se decidió contra *este* fondo, y el día que la escena cambie de lámina
—o que la pieza se reutilice en otro episodio— hay que rehacer el cálculo desde el material
sin tocar. Aclarar sobre lo ya aclarado acumula, y en dos pasadas la foto nocturna es una
foto de día.

## Lo que queda hoy, y por qué no se toca

La auditoría de hoy marca **tres** elementos por debajo del umbral de 12:

| Elemento | Escena | Luz | Fondo | Diferencia | Vida |
|---|---|---|---|---|---|
| `imprenta_sellos` | oficio | 91,0 | 82,6 | 8,4 | 2,4 s |
| `jefes_servicio_secreto` | nombre | 72,0 | 63,6 | 8,5 | 2,4 s |
| `torre_postal` | metodo | 93,1 | 81,9 | 11,3 | 2,4 s |

Ninguno es un 1,09. Los tres caen en la franja 8–12, que es donde el margen de papel crema
hace el trabajo: la **silueta** se separa aunque la masa no lo haga. Antes de aplicarles
gamma hay que mirar el fotograma —la regla de `163`: nunca se arregla un lavado sin verlo—
y comprobar si el borde ya los está salvando. Cuatro puntos de gamma gratuitos ensucian
más de lo que arreglan.

## El orden correcto

1. **`auditar.py`**, antes de renderizar. Segundos. Caza los 1,1.
2. **Gamma mínima**, con el original guardado al lado.
3. **`163` sobre el render**, con `dL` y `frac`. Minutos. Caza lo que depende del
   movimiento del fondo, de la viñeta y de lo que le cae encima.
4. **El ojo**, siempre el último. El número ordena; el ojo decide.

Saltarse el paso 1 es pagar un render por iteración; saltarse el 3 es dar por bueno un
elemento contra un fondo estático que en el vídeo se mueve.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Medir el fondo entero en vez del trozo que le toca | La viñeta falsea el contraste 20–25 L (`23`) |
| Confiar solo en la compuerta barata | No ve el movimiento del fondo ni las oclusiones: eso es `163` |
| Aclarar el fondo para salvar un elemento | Se pierde la escena por salvar un recorte |
| Subir la opacidad del recorte | La opacidad siempre es 1: rompe el lenguaje del canal |
| Aplicar gamma sin guardar el original | La segunda pasada convierte la noche en día |
| Elegir una gamma «que se vea bien» | Se mata el virado que hacía empatar la pieza (`197`) |
| Tratar un 8,4 igual que un 1,1 | En la franja 8–12 suele estar salvando el borde de papel |
| Mezclar este número con el `dL` de `163` | Son dos escalas y dos máscaras distintas |

## Relacionado

`23` empatar recorte y fondo (los cuatro ejes y sus arreglos) ·
`163` contraste elemento-fondo (`dL` y `frac` sobre el render) ·
`197` envejecer para que empate · `196` limpiar el alfa · `161` auditar sobre gris ·
`25` el borde de papel · `291` el borde de papel medido · `299` cuándo una foto no aporta ·
`editpro/399` comprobar la profundidad sobre gris
