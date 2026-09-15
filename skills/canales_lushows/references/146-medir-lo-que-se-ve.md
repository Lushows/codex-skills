# 146 · Medir lo que se ve, no lo que existe

**Qué resuelve:** métricas que cuentan píxeles fuera del lienzo. El elemento existe en
la tabla, pero el espectador no lo ve, y la nota sube igual.

---

## El caso

La cobertura se calculaba con la superficie **del elemento**: ancho × alto. Un recorte
de 700 px colocado en `x = W*0.78` sobresale 224 px por la derecha; la mitad de un
retrato colocado en `y = H*0.85` cae bajo el borde inferior. Todos esos píxeles se
sumaban como cuadro lleno.

> Una versión del episodio daba **46,9 % de cobertura media** con varios recortes medio
> fuera de cuadro. El lienzo real estaba bastante más vacío que eso.

El error es sistemático y siempre va en la misma dirección: **infla**. Nunca corrige a
la baja. Por eso no se compensa solo y por eso es peligroso: da confianza.

## La corrección: recortar contra el lienzo

Se intersecta el rectángulo del elemento con el rectángulo del lienzo antes de contar.

```python
def caja(ele):
    """Rectangulo del elemento en el lienzo: (x0, y0, x1, y1) en pixeles."""
    W, H = 1920.0, 1080.0
    x, y = coord(ele.get("x", 0), W, H), coord(ele.get("y", 0), W, H)
    prop = _prop(ele["r"])                       # alto/ancho del PNG
    if x is None or y is None or prop is None:
        return None
    anc = ele.get("w", 400)
    return (x, y, x + anc, y + anc * prop)


def visible(c):
    """Superficie del elemento que cae DENTRO del lienzo, en tanto por uno."""
    if c is None:
        return 0.0
    dx = max(0.0, min(c[2], 1920.0) - max(c[0], 0.0))
    dy = max(0.0, min(c[3], 1080.0) - max(c[1], 0.0))
    return dx * dy / (1920.0 * 1080.0)
```

Dos `max(0.0, ...)`: sin ellos, un elemento **completamente** fuera del lienzo daría
`dx` y `dy` negativos y su producto **positivo**, sumando superficie desde la nada. Es
el fallo clásico de intersección de rectángulos y aquí habría sido invisible.

## La otra mitad: avisar de la fuga

Recortar arregla la cifra, pero no dice nada del problema. Un recorte que sangra por un
borde es legítimo en collage (se lee como página que se sale, `25`); uno que se come la
cara del protagonista es un fallo. Por eso hay un aviso separado, a partir del **12 %
del elemento fuera**:

```python
for a, b, e, r, _, c in vidas:
    if c is None:
        continue
    dentro_x = max(0.0, min(c[2], 1920.0) - max(c[0], 0.0))
    dentro_y = max(0.0, min(c[3], 1080.0) - max(c[1], 0.0))
    propia = (c[2] - c[0]) * (c[3] - c[1])
    fuera_pc = 1 - (dentro_x * dentro_y / propia) if propia else 0
    if fuera_pc > 0.12:
        fugados.append((a, e, r, fuera_pc * 100))
```

```
  --- elementos que se salen del cuadro ---
    31.20  torre      'recorte_grua' con el  34% fuera del lienzo
```

**Dos medidas, un fenómeno:** una descuenta lo invisible, la otra lo denuncia. Si sólo
se recorta, el episodio adelgaza de cobertura sin que nadie sepa por qué.

## Dónde más se mide lo que existe en vez de lo que se ve

| Medida | Lo que existe | Lo que se ve |
|---|---|---|
| Cobertura | Superficie del PNG | Intersección con 1920×1080 |
| Elemento tapado | Está vivo en la tabla | Un elemento posterior lo cubre > 55 % (`148`) |
| Zona útil vertical | Hasta `H*1.0` | Hasta `H*0.72`: debajo pinta YouTube la barra (`49`) |
| Recurso repetido | Nombre del fichero | La familia del dibujo (`142`) |
| Elemento con opacidad 0,08 | Cuenta como presencia | No se distingue del fondo |

Las tres primeras están implementadas. La cuarta y la quinta son el recordatorio de que
la lista no está cerrada: cada vez que aparece una forma nueva de que algo esté en la
tabla sin estar en pantalla, hay una métrica que corregir.

## El caso especial de la banda inferior

Un rótulo en `y = H*0.80` está **dentro** del lienzo: `visible()` lo cuenta entero y
con razón, porque el píxel existe en el archivo MP4. Pero en el reproductor de YouTube
esa franja queda bajo la barra de progreso durante buena parte de la reproducción. La
métrica no puede saberlo: el límite de `H*0.72` es una **regla de colocación** (`49`),
no algo que se deduzca del lienzo. Medir lo que se ve tiene un borde donde acaba el
fichero y empieza el reproductor (`149`).

## Comprobación rápida

Un caso de prueba de tres líneas que habría cazado el fallo el primer día:

```python
# elemento de 800x400 colocado con la mitad fuera por la derecha
c = (1520.0, 100.0, 2320.0, 500.0)
assert abs(visible(c) - (400.0 * 400.0) / (1920.0 * 1080.0)) < 1e-9
# elemento entero fuera del lienzo: aporta cero, no un numero positivo
assert visible((2000.0, 1200.0, 2400.0, 1400.0)) == 0.0
```

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Contar el elemento entero | La cobertura infla; 46,9 % con el cuadro medio vacío |
| Intersecar sin `max(0.0, …)` | Un elemento fuera del lienzo suma superficie positiva |
| Recortar y no avisar de la fuga | Baja la nota y nadie sabe qué elemento la baja |
| Tratar todo sangrado como error | En collage el borde que se sale es lenguaje (`25`) |
| Suponer que dentro del lienzo = visible | La banda bajo `H*0.72` la tapa el reproductor |

## Relacionado

`25` el borde de papel · `49` zona segura y tamaños · `144` presencia no es superficie ·
`145` la media esconde el suelo · `148` el cuadro de mando · `149` lo que no se puede medir
