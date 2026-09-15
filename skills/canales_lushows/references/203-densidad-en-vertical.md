# 203 · Densidad en vertical

**Qué resuelve:** el motor coloca por bandas declaradas en fracciones del lienzo
(`W*0.44`, `H*0.36`), y eso da la impresión de que cambiar `W_LIENZO, H_LIENZO` de
1920×1080 a 1080×1920 basta. **No basta.** Las fracciones sobreviven al cambio de lienzo;
los anchos, los techos de altura y la simultaneidad, no. Este módulo mide qué se rompe y
deja el mapa de bandas verticales con sus números.

---

## Lo que la trasposición ingenua le hace a la densidad

Mantener el mismo ancho **relativo** al lienzo es lo que parece correcto y es lo que
destruye el montaje. Un elemento declarado a `0,667 W` mide 1280 px sobre 1920 y 720 px
sobre 1080; su alto baja en la misma proporción, así que su **superficie cae al cuadrado**
—y el lienzo tiene la misma área. Medido sobre los 59 elementos de `ep01-lustig`:

| | 16:9 | 9:16 traspuesto a ciegas |
|---|---|---|
| Superficie media por elemento | **18,4 %** del cuadro | **5,8 %** |
| Factor | — | **× 0,32** |
| Cobertura media del episodio | **36,1 %** | **11,4 %** |

11,4 % es un cuadro vacío: el auditor marca «casi vacío» por debajo del 14 %. El mismo
montaje, el mismo material, la misma tabla — y un vídeo que parece que se ha caído el
render.

Para conservar la superficie habría que multiplicar el ancho relativo por **1,778**. Con
la clase `heroe` eso es pasar de `0,667 W` a `1,185 W`: más ancho que el lienzo. **No se
puede conservar la densidad por elemento.** Lo que se puede es cambiar la mezcla.

## Qué manda en cada lienzo

En 16:9 el recurso escaso es el **alto**, y por eso existe `alto_max` en `CLASES`: un
recorte apaisado a 1280 px de ancho mide 909 de alto y no cabe. En vertical el recurso
escaso es el **ancho**, y `alto_max` deja de ser el freno. Medido:

| | 16:9 | 9:16 |
|---|---|---|
| Elementos recortados por el techo de altura (`0,72 H` = 778 px) | **3 de 59** | — |
| Elementos más anchos que el 94 % del lienzo (1015 px) | — | **11 de 59** |
| Elementos más anchos que la zona segura de texto (820 px) | — | **21 de 59** |

Y la proporción del material lo explica: **47 de 59 elementos son apaisados** (alto/ancho
mediano **0,672**). El banco de archivo de este canal es horizontal porque la fotografía
de prensa del siglo XX lo era.

Trasponer `alto_max` tal cual es absurdo y se ve en cuanto se escribe:

```
heroe   alto_max 0,72 →  16:9   778 px = 0,41 del ancho del lienzo
                         9:16  1382 px = 1,28 del ancho del lienzo
```

Un techo de altura mayor que el ancho no es un techo: es un permiso.

## El límite duro: la pila

La zona útil de trabajo son 1200 px de alto (`y` de 200 a 1400, `49`). El episodio tiene
**simultaneidad media 2,05, máximo 4, y tres o más elementos el 30 % del tiempo**:

```
elementos vivos:  0 → 33 muestras   1 → 286   2 → 575   3 → 334   4 → 41
```

Apilando los vivos en la columna con 40 px de hueco y un ancho de `0,86 W`, la pila
**no cabe en los 1200 px el 50 % del tiempo**, y en el peor instante (t = 56,05 s) pide
2476 px. Con cuatro elementos a la vez cada uno tendría 270 px de alto: a proporción
0,672, elementos de 402 px de ancho. Ilegibles y ridículos.

> **La conclusión operativa: el corte vertical baja a dos elementos simultáneos.** No es
> una concesión estética, es aritmética de columna. El vertical no monta menos porque sea
> más pobre; monta menos porque cada elemento tiene que ser mucho más grande.

## El mapa de bandas verticales

Centros sobre 1080×1920, con la misma mecánica de `243` —son centros, `rect()` traduce a
esquina— y todos dentro de la columna útil, comprobado:

```python
W_LIENZO, H_LIENZO = 1080.0, 1920.0

BANDAS_V = {
    "gancho":  [("W*0.50", "H*0.26")],                              # y = 499
    "centro":  [("W*0.50", "H*0.40"), ("W*0.48", "H*0.46"),         # y = 768, 883
                ("W*0.52", "H*0.34")],                              # y = 653
    "banda2":  [("W*0.50", "H*0.60"), ("W*0.46", "H*0.66"),         # y = 1152, 1267
                ("W*0.54", "H*0.55")],                              # y = 1056
    "cifra":   [("W*0.50", "H*0.50"), ("W*0.50", "H*0.44")],        # y = 960, 845
    "pie":     [("W*0.50", "H*0.71"), ("W*0.50", "H*0.675")],       # y = 1363, 1296
    "esquina": [("W*0.30", "H*0.155"), ("W*0.70", "H*0.155")],      # y = 298
}
ENTRADAS_V = {"gancho": "fade", "centro": "abajo", "banda2": "abajo",
              "cifra": "abajo", "pie": "abajo", "esquina": "fade"}
```

Trece posiciones frente a las dieciséis del 16:9, y **la `x` es casi siempre 0,50**: la
banda `lado` desaparece porque no hay lado (`201`). `esquina` sobrevive a `y = 298` sólo
para la marca de columna, que es estrecha.

## La tabla de clases verticales

Anchos en píxeles sobre 1080; `alto_max` en tanto por uno de 1920. Calibrada contra los
59 elementos del episodio:

| Clase | 16:9 (px reales) | superficie | 9:16 (px reales) | superficie |
|---|---|---|---|---|
| `heroe` | 1157×778 | 43,4 % | **971×653** | 30,6 % |
| `objeto` | 900×605 | 26,3 % | **800×538** | 20,7 % |
| `dato` | 482×324 | 7,5 % | **486×326** | 7,6 % |
| `rotulo` | 321×216 | 3,3 % | **286×192** | 2,6 % |
| `micro` | 418×281 | 5,7 % | **371×250** | 4,5 % |

```python
CLASES_V = {
    #            dura   ancho  alto_max  fade_out  banda
    "heroe":   (3.40,  1015,   0.34,     0.45,  "centro"),
    "objeto":  (2.60,   940,   0.28,     0.40,  "banda2"),
    "dato":    (3.10,   980,   0.17,     0.45,  "cifra"),
    "rotulo":  (2.10,   880,   0.10,     0.30,  "pie"),
    "micro":   (1.40,   600,   0.13,     0.25,  "esquina"),
}
ANCHO_MAX_TEXTO, ANCHO_MAX_IMAGEN = 820, 1015
```

Dos topes, no uno, y esa es la diferencia que más se olvida: **una fotografía puede
sangrar hasta el borde del lienzo; una pieza de texto no puede salir de la zona segura**.
Un recorte cortado por el canto se lee como collage; un rótulo cortado por el canto se
lee como un fallo.

## El objetivo de cobertura cambia

Con esa tabla, el mismo episodio da **22,9 % de cobertura media en vertical** contra
36,1 % en 16:9. No es un fallo de calibración: es el techo. `heroe` y `objeto` no pueden
coexistir a tamaño pleno —653 + 538 + 40 = **1231 px** contra 1200 de columna— y dos
`heroe` a la vez son 1346 px, imposibles.

> **Objetivo de cobertura del vertical: 20–30 %.** El 22–38 % del auditor está calibrado
> para 16:9 y en vertical marcaría en rojo un cuadro correcto. Se cambia el umbral, no el
> montaje (`141`).

## Errores frecuentes

| Error | Consecuencia medida |
|---|---|
| Cambiar sólo `W_LIENZO, H_LIENZO` | Superficie por elemento × 0,32; cobertura 36,1 % → 11,4 % |
| Trasponer `alto_max` en tanto por uno | `heroe` con techo de 1382 px: mayor que el ancho del lienzo |
| Mantener las cuatro posiciones de `lado` | No hay lado: el margen horizontal real es de ±140 px |
| Conservar la simultaneidad de 16:9 | La pila no cabe en 1200 px el 50 % del tiempo |
| Un solo tope de ancho para foto y texto | O el texto sale de la zona segura, o la foto se queda enana |
| Juzgar el vertical con el umbral 22–38 % | Marca en rojo un cuadro correcto; el techo real es 30 % |
| Meter cuatro elementos «porque en 16:9 caben» | 270 px de alto cada uno: 402 px de ancho, ilegibles |

## Relacionado

`200` el vertical se renderiza · `201` la columna · `204` el texto manda · `10` densidad
de eventos · `141` elegir un umbral · `242` colocación por rectángulo · `243` bandas y
anclaje central · `244` el techo de altura · editpro `147` formato vertical a fondo
