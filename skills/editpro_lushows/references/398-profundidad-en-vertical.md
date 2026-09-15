# 398 — Profundidad en vertical

**Qué resuelve:** el cuadro que funcionaba en 16:9 se pasa a 9:16 y la profundidad desaparece. No es
impresión: **el eje de tamaño cambia de unidad al girar el lienzo**, y los otros tres se quedan como
estaban. Este módulo mide cuánto cambia y qué hay que recolocar.

---

## 1. El mismo elemento, los dos lienzos

`retrato_lustig`, cinco anchos, sobre 1920 × 1080 y sobre 1080 × 1920. Los dos lienzos tienen
exactamente el mismo número de píxeles, así que cualquier diferencia es de forma, no de resolución.

| Ancho del elemento | 16:9 % ancho | 16:9 % alto | 9:16 % ancho | 9:16 % alto | % área (los dos) |
|---|---|---|---|---|---|
| 280 | 14,6 | 34,9 | **25,9** | **19,6** | 4,99 |
| 420 | 21,9 | 52,4 | **38,9** | **29,5** | 11,23 |
| 620 | 32,3 | 77,4 | **57,4** | **43,5** | 24,48 |
| 900 | 46,9 | 112,3 | **83,3** | **63,2** | 51,57 |
| 1300 | 67,7 | 162,3 | 120,4 | 91,3 | 107,65 |

Tres lecturas:

- **El % de área es idéntico.** Es el único número que sobrevive al giro, y por eso es la unidad
  honesta del eje de tamaño cuando trabajas los dos formatos (`391` §3).
- **El % de alto se hunde a la mitad.** Un elemento que ocupaba el 77 % de la altura pasa al 43,5 %.
  Si anotaste el plano en % de altura, todos tus planos se van al fondo de golpe.
- **El % de ancho casi se dobla.** 32,3 % → 57,4 %. El plano frente pasa a tocar los dos bordes.

> En horizontal el ojo mide contra la **altura** (el cuadro es ancho, la altura es el límite). En
> vertical mide contra el **ancho**. El área es lo único común. Anota el plano en **% de área** y
> traduce al ancho de destino en el render.

```python
def ancho_para_area(png, pct_area, W, H):
    """Ancho en px que hace que el alfa opaco ocupe pct_area % del lienzo."""
    import numpy as np
    from PIL import Image
    im = Image.open(png).convert("RGBA")
    ocup = (np.asarray(im)[:, :, 3] > 200).sum() / (im.width*im.height)  # densidad del alfa
    objetivo = pct_area/100 * W * H / ocup            # área del bbox que hace falta
    return round((objetivo * im.width / im.height) ** 0.5)
```

---

## 2. El escalón de tamaño se estrecha

El vertical tiene 1080 px de ancho útil. Entre el plano frente (que suele ir al 55–65 % del ancho) y el
suelo de peso visual (`canales 21`) queda mucho menos margen que en horizontal.

| Plano | 16:9, ancho px | 9:16, ancho px | Margen restante |
|---|---|---|---|
| Primerísimo | 775 (40 % del lienzo) | 810 (75 %) | ya toca los bordes |
| Frente | 620 (32 %) | 620 (57 %) | cómodo |
| Medio | 403 (21 %) | 403 (37 %) | cómodo |
| Fondo lejano | 279 (15 %) | 279 (26 %) | **al límite del suelo** |

El resultado práctico: **en vertical caben tres cotas, no cuatro.** Meter una cuarta obliga a bajar de
un ancho que ya no pesa. La profundidad que pierdes en el eje de tamaño hay que cobrarla en los otros:

| Eje | Escalón en 16:9 | Escalón en 9:16 |
|---|---|---|
| Tamaño | 25 % mínimo | 30 % mínimo, y solo tres cotas |
| Desenfoque | −30 a −65 % de ACUT | **−40 a −70 %**: más agresivo |
| Contraste | −8 a −18 % | **−12 a −22 %** |
| Saturación | −10 a −20 % | −12 a −24 % |

---

## 3. La profundidad choca con las zonas seguras

En horizontal el plano medio se coloca donde estorbe menos. En vertical el cuadro ya está repartido por
la interfaz de la app, y las franjas de `204` mandan sobre la profundidad:

```
0    - 250 px    ZONA MUERTA SUPERIOR    aquí no va ningún plano que importe
250  - 700 px    ZONA DE GRÁFICO         aquí vive el plano medio y el fondo lejano
700  - 1450 px   ZONA DEL SUJETO         aquí SOLO el plano frente
1450 - 1650 px   ZONA DE TEXTO           subtítulos; ningún plano compite
1650 - 1920 px   ZONA MUERTA INFERIOR    aquí no va nada
```

De donde salen dos reglas que en horizontal no existen:

1. **El plano medio se coloca arriba, no a los lados.** En vertical no hay lados: 1080 px de ancho se
   los come el sujeto. El sitio libre está entre 250 y 700 px de altura.
2. **El primerísimo entra por abajo y sale por abajo**, entre 1450 y 1920, pisando la zona de texto solo
   mientras no haya subtítulo. Si hay subtítulo, no hay primerísimo. Es una de las dos y nunca las dos.

---

## 4. El solape es más fácil y más peligroso

En vertical los planos se solapan casi por obligación: no hay sitio para que no lo hagan. Eso resuelve
gratis el problema de `396` §3.5 (sin oclusión no hay prueba de profundidad) y crea el contrario:

| Solape en vertical | Qué pasa |
|---|---|
| menos del 10 % | raro en 9:16; si lo consigues, revisa que no esté todo amontonado arriba |
| **12 – 28 %** | **el rango bueno** |
| más del 35 % | el plano de atrás deja de existir; en vertical se alcanza enseguida |

El margen entre "hay oclusión" y "está tapado" es mucho más estrecho. Mídelo, no lo estimes.

---

## 5. Comprobarlo donde se ve

La profundidad en vertical se revisa **en el móvil y dentro de la app**, no en el editor. Dos cosas que
solo aparecen ahí:

- El plano medio colocado en 1500 px se ve perfecto en el editor y **debajo del subtítulo** en la app.
- El contacto de la sombra (`394`) se lee distinto en una pantalla de 6 pulgadas a media luz: lo que en
  el monitor era un contacto de 7,5 discreto, en el móvil se ve como un cerco.

La comprobación numérica que sí se puede hacer antes: exportar el fotograma, escalarlo a 360 px de
ancho —el tamaño real en el que mucha gente lo ve— y volver a pasar `separa.py` (`396`). Si a 360 px los
ejes ya no cruzan, en el móvil tampoco.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Anotar el plano en % de altura y reusarlo en vertical | Todos los planos se van al fondo: 77 % pasa a 43,5 % |
| Llevar las cuatro cotas de 16:9 al vertical | La cuarta cae por debajo del suelo de peso visual |
| No subir el escalón de desenfoque al girar | Se pierde el tamaño y no se compensa en ningún sitio |
| Colocar el plano medio a los lados | En vertical no hay lados; el sitio está entre 250 y 700 px |
| Primerísimo y subtítulo a la vez | Compiten por la misma franja: es una de las dos |
| Solape por encima del 35 % en vertical | El plano de atrás desaparece; el margen es estrecho |
| Revisar la profundidad en el editor | El subtítulo tapa el plano medio y no lo ves hasta publicar |
| Dar por buena la separación sin mirarla a 360 px | Los ejes que cruzan en el monitor pueden no cruzar en el móvil |

## Relacionado

`390` la profundidad es separación medida · `391` el escalón de tamaño ·
`392` el escalón de desenfoque · `394` la sombra que asienta · `396` el plano que no separa ·
`397` el primer término que se come al sujeto · `204` composición en capas (zonas seguras) ·
`376` legibilidad real en celular · `45` zona segura por plataforma · `canales 21` peso visual
