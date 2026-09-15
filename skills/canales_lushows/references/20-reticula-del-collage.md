# 20 · Retícula del collage

**Qué resuelve:** los elementos se colocan a ojo, cada escena inventa su propio
reparto y el episodio se ve descosido. La retícula da un sitio calculado a cada
recorte — y un desvío también calculado, que es lo que produce el aire hecho a mano.

---

## La retícula: 3 × 3 sobre 1920 × 1080

| Medida | Valor | En expresión |
|---|---|---|
| Margen exterior | 96 px (5%) | `W*0.05` · `H*0.089` |
| Columna | 552 px | — |
| Canaleta vertical | 36 px | — |
| Fila | 280 px | — |
| Canaleta horizontal | 24 px | — |

`96 + 552·3 + 36·2 + 96 = 1920` · `96 + 280·3 + 24·2 + 96 = 1080`. Cuadra exacto.

## Las 9 posiciones canónicas

Se anclan por el **centro**, no por la esquina. En `overlay` de ffmpeg `W`/`H` son el
lienzo y `w`/`h` el elemento, así que el centro se escribe restando la mitad:

| # | Nombre | x | y |
|---|---|---|---|
| P1 | alto-izquierda | `W*0.194-w/2` | `H*0.219-h/2` |
| P2 | alto-centro | `W*0.5-w/2` | `H*0.219-h/2` |
| P3 | alto-derecha | `W*0.806-w/2` | `H*0.219-h/2` |
| P4 | medio-izquierda | `W*0.194-w/2` | `H*0.5-h/2` |
| P5 | centro | `W*0.5-w/2` | `H*0.5-h/2` |
| P6 | medio-derecha | `W*0.806-w/2` | `H*0.5-h/2` |
| P7 | bajo-izquierda | `W*0.194-w/2` | `H*0.781-h/2` |
| P8 | bajo-centro | `W*0.5-w/2` | `H*0.781-h/2` |
| P9 | bajo-derecha | `W*0.806-w/2` | `H*0.781-h/2` |

**Anchos que caben** (el `w` de la tabla de eventos, ya con margen de papel incluido):

| Ocupación | Ancho | Centro x |
|---|---|---|
| 1 columna | hasta **552** | la de su posición |
| 2 columnas (izq) | hasta **1140** | `W*0.347-w/2` |
| 2 columnas (der) | hasta **1140** | `W*0.653-w/2` |
| 3 columnas | hasta **1728** | `W*0.5-w/2` |

## Por qué anclar por el centro y no por la esquina

`motor.py` rota con `rotate=…:ow=rotw(a):oh=roth(a)`, es decir **la caja crece al
girar**. Un elemento de 640 × 420 con `rot: 3` pasa a medir 661 × 453: 21 px más de
ancho. Si lo anclas por la esquina superior izquierda, el recorte se desplaza 10 px
cada vez que tocas el ángulo. Anclado por el centro, girar no lo mueve.

```
ancho_girado = w·cos(a) + h·sin(a)      alto_girado = w·sin(a) + h·cos(a)
```

## Por qué no se colocan a ojo

1. **No escala.** Un episodio de 12 minutos son ~400 eventos. Colocarlos uno a uno es
   inviable; declararlos contra 9 posiciones, no.
2. **La rotación mueve la caja.** Ver arriba: a ojo, cada retoque de ángulo obliga a
   recolocar.
3. **Es lo que hace reconocible el canal.** Dos episodios con el mismo reparto de masa
   se ven de la misma casa; dos episodios improvisados, no.
4. **Se puede auditar.** Con la retícula, un script comprueba márgenes y solapes antes
   de renderizar (`17` medir el montaje, `28` respiración del cuadro).
5. **El collage necesita desorden CONTROLADO.** Un desvío conocido a partir de una
   posición conocida se ve hecho a mano; una posición aleatoria se ve descuidada.

## El desvío: la irregularidad que sí es reproducible

Sobre la posición canónica se suma un desplazamiento de **±12 a ±40 px** derivado del
alias del recurso. Mismo alias, mismo desvío, en todos los renders:

```python
import zlib

def desviar(x_expr, y_expr, alias, amp=28):
    """Desvío determinista sobre una posición canónica. NUNCA hash(): el hash de un
    str cambia entre procesos de Python y el episodio no se reproduce igual."""
    s = zlib.crc32(alias.encode())
    dx = (s % (2 * amp + 1)) - amp
    dy = ((s >> 8) % (2 * amp + 1)) - amp
    return f"{x_expr}{dx:+d}", f"{y_expr}{dy:+d}"

x, y = desviar("W*0.194-w/2", "H*0.5-h/2", "chapo_us")
# -> ('W*0.194-w/2-17', 'H*0.5-h/2+9')
```

El ángulo sigue la misma lógica: `rot` entre **1,2° y 3,4°**, alternando signo entre
elementos vecinos. Dos recortes contiguos inclinados hacia el mismo lado se leen como
un error de render, no como collage.

## Cómo entra en la tabla de eventos

```python
{"r": "chapo_us", "ancla": "hombre", "offset": -0.15, "dura": 2.4,
 "x": "W*0.194-w/2-17", "y": "H*0.5-h/2+9", "w": 620,
 "entrada": "izq", "deriva": (9, -4), "rot": -1.3},
```

`entrada` y `deriva` los envuelve el motor encima de estas expresiones (±520 px en
horizontal, ±380 px en vertical durante 0,36 s). No hay que preverlo en el `x`.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Anclar por esquina y luego tocar `rot` | El elemento se desplaza 8-20 px sin que se sepa por qué |
| Usar `hash(alias)` para el desvío | El collage sale distinto en cada render; no se puede reproducir un episodio |
| Desvío mayor de 40 px | Se pierde la retícula: vuelve a verse improvisado |
| Elemento de 1 columna con `w` mayor de 552 | Invade la canaleta y colisiona con el vecino |
| Dos vecinos con `rot` del mismo signo | Se lee como que el render está torcido |
| Poner algo fuera del margen de 96 px | Se corta en la reproducción a pantalla completa de algunos televisores |

## Relacionado

`21` peso visual y jerarquía · `24` agrupar y separar · `28` respiración del cuadro ·
`29` plantillas de escena · `12` capas simultáneas
