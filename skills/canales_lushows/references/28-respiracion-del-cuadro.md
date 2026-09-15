# 28 · Respiración del cuadro

**Qué resuelve:** el cuadro está lleno de arriba abajo, todo grita y nada se lee. El
vacío no es lo que sobra después de colocar los elementos: es un material que se coloca
igual que ellos, y tiene sus medidas.

---

## Los tres márgenes

| Zona | Margen | En 1920 × 1080 | Qué puede haber ahí |
|---|---|---|---|
| **Borde físico** | 0% | — | Solo el fondo full-bleed |
| **Zona de acción** (95%) | 5% | 96 px lados · 54 px arriba/abajo | Recortes, texturas, elementos que pueden cortarse |
| **Zona de título** (90%) | 10% | 192 px lados · 108 px arriba/abajo | **Todo el texto, cifras y rótulos** |

La retícula de `20` ya nace con el margen de 96 px. El texto vive un escalón más
adentro: un rótulo que empieza en `W*0.05` está en zona de acción, no de título.

## Lo que se come YouTube

| Elemento | Zona que ocupa | Cuándo |
|---|---|---|
| Barra de controles | ~90 px inferiores | Al pasar el ratón o tocar la pantalla |
| Título y canal en móvil | ~110 px superiores | Al tocar la pantalla |
| Tarjetas finales | cuadrantes derecho e inferior | **Últimos 20 s del vídeo** |
| Marca de tiempo / calidad | esquina inferior derecha | Al pasar el ratón |

**Consecuencia práctica:** en los últimos 20 segundos, el cuadrante inferior derecho no
lleva nada que haya que leer. Y ninguna cifra vive nunca por debajo de `H*0.90`.

## El recorte a 9:16

Si el episodio se reencuadra para vertical, un recorte 9:16 de un fotograma de 1080 px
de alto mide **607,5 px de ancho** — una columna central del 31,6% del cuadro:

```
columna segura vertical:  x entre W*0.342 y W*0.658
```

Lo que tenga que sobrevivir al recorte (la cara, la cifra) va dentro de esa columna.
Todo lo demás es material de acompañamiento que se pierde, y está bien que se pierda.
No se compone el episodio horizontal para el vertical: se decide **qué** se salva.

## Ocupación de tinta

| Cobertura del cuadro | Cómo se lee |
|---|---|
| menos del 25% | Vacío. Si no es un remate a propósito, es un hueco (`11`) |
| **45 - 65%** | **La banda del canal.** Denso pero legible |
| 66 - 75% | Cargado. Válido para el tablero de investigación |
| más del 75% | Ruido: el ojo no encuentra dónde entrar |

Se mide sobre la tabla, sin renderizar, sumando las cajas de los elementos vivos:

```python
from PIL import Image
from motor import buscar

def ocupacion(elementos, W=1920, H=1080):
    """Fraccion del cuadro cubierta por las cajas de los elementos vivos a la vez."""
    lienzo = Image.new("L", (W, H), 0)
    for e in elementos:
        im = Image.open(buscar(e["r"]))
        w = e.get("w", 400); h = int(im.height * w / im.width)
        ctx = {"W": W, "H": H, "w": w, "h": h}
        x = int(eval(e["x"], {"__builtins__": {}}, ctx))
        y = int(eval(e["y"], {"__builtins__": {}}, ctx))
        lienzo.paste(im.convert("RGBA").resize((w, h)).split()[3]
                       .point(lambda v: 255 if v > 40 else 0), (x, y))
    return sum(lienzo.histogram()[1:]) / (W * H)
```

Usa el alfa, no la caja: un recorte de tijera con esquinas transparentes ocupa menos de
lo que mide. Por eso este número es más honesto que sumar rectángulos.

## El vacío se coloca, no se deja

La regla que ordena el cuadro: **el hueco va enfrente de la masa, entero, no repartido.**

| Mal | Bien |
|---|---|
| Cuatro elementos con 60 px de aire entre todos | Tres elementos apretados a la izquierda y la mitad derecha limpia |
| Un elemento en cada esquina | Un bloque en dos columnas y una columna vacía |
| Aire igual arriba y abajo | Peso arriba, respiración abajo (o al revés) |

Un cuadro con aire repartido a partes iguales se ve indeciso. Un cuadro con todo el
peso a un lado y el vacío al otro se ve compuesto — y además deja sitio a lo que entra
después, que es lo que permite la densidad de `10` sin saturar.

## Cuándo el vacío es el contenido

- **El remate.** La revelación necesita el cuadro casi limpio: un elemento, mucho aire.
  Ocupación por debajo del 30% y `mov` lento.
- **Después de un golpe de cifra.** Un segundo de aire hace que la cifra pese el doble
  en el recuerdo.
- **El silencio de la voz.** Si el guion calla, el cuadro no debe gritar. Es el único
  caso en que un tramo con poca ocupación no cuenta como hueco.

Fuera de esos tres casos, un tramo vacío es el defecto medido del canal: 22 s de fondo
solo en el primer episodio, el 28% de su duración.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Texto en zona de acción y no de título | Se corta en televisores con overscan |
| Cifra por debajo de `H*0.90` | La tapa la barra de controles |
| Información en el cuadrante inferior derecho al final | La tapan las tarjetas finales |
| Aire repartido en partes iguales | El cuadro se ve indeciso |
| Ocupación por encima del 75% | Ruido: no hay por dónde entrar |
| Confundir vacío con hueco | Se rellena un remate que estaba bien y se mata la revelación |
| Medir ocupación con rectángulos | Sobreestima: los recortes de tijera no llenan su caja |

## Relacionado

`20` retícula del collage · `11` el hueco prohibido · `16` el plano de descanso ·
`49` zona segura y tamaños · `29` plantillas de escena
