# 204 · El texto manda

**Qué resuelve:** en 16:9 el ancho de una pieza lo decide la clase y el equilibrio del
cuadro; la legibilidad se comprueba después y casi siempre pasa. En vertical se invierte:
**el ancho lo decide el texto que lleva dentro**, y si el texto no cabe, la pieza no se
encoge — se redibuja. Este módulo mide cuántas piezas del episodio real dejan de leerse
al pasar a vertical, y qué se hace con cada una.

`editpro 412` da la fórmula de las dos reducciones encadenadas y el fallo de comprobar
contra un ancho constante. Ese fallo ya está corregido aquí: `diccionario.ancho_legible()`
lee el `font-size` del HTML de origen y lo compara con el ancho **que decide el montaje**.
Lo que falta —y es lo de este módulo— es qué pasa con ese cálculo cuando el lienzo cambia.

---

## El suelo sube y el ancho baja, a la vez

`SUELO_TEXTO = 28.0` px sobre lienzo de 1920. Dos cosas se mueven al pasar a vertical y
se mueven en direcciones contrarias:

1. **El píxel del lienzo crece.** Un vídeo de 1080 de ancho llena la misma pantalla que
   uno de 1920, así que cada píxel vale 1,778 veces más. El suelo, traducido, sería
   `28 × 1080/1920 = 15,8 px` sobre 1080.
2. **El listón sube.** `49` fija el suelo del vertical en 34 px de caja de mayúscula
   frente a 24 en 16:9: **× 1,417**, porque el vertical se ve con notificaciones encima y
   el pulgar sobre el cristal.

Las dos juntas dan la única cifra que hace falta recordar:

> **Una pieza de texto necesita ser 1,42 veces más ancha, en tanto por uno del lienzo, en
> vertical que en 16:9.**

Y la trampa es que ese 1,42 no se nota mirando: el PNG es el mismo, el montaje lo coloca
«igual de grande» y el texto se ha hecho pequeño en el único sitio donde importa.

## La medida, pieza a pieza

16 de los 59 elementos de `ep01-lustig` son texto (`es_texto()`). Todos pasan en 16:9.
Con el mismo ancho relativo en vertical:

| Pieza | Ancho mostrado (16:9) | Ancho legible | 16:9 | 9:16 |
|---|---|---|---|---|
| `linea_00` | 1190 | 1190 | OK | **NO** (pide 948 px sobre 1080) |
| `linea_02` | 1080 | 850 | OK | **NO** (677) |
| `linea_03` | 900 | 850 | OK | **NO** (677) |
| `linea_06` | 1120 | 850 | OK | **NO** (677) |
| `r_sinfuente` | 720 | 700 | OK | **NO** (558) |
| `c_oficio` | 1011 | 712 | OK | OK (567) |
| `r_casilla` | 968 | 661 | OK | OK (527) |
| `m_consta` | 700 | 450 | OK | OK (359) |
| `sello_consta` | 600 | 355 | OK | OK (283) |
| `d_1890` | 1340 | 283 | OK | OK (226) |
| `d_preso` | 1380 | 253 | OK | OK (202) |
| `d_anos` | 1090 | 220 | OK | OK (175) |

```
16:9   legibles 16 / ilegibles  0
9:16   legibles 11 / ilegibles  5
factor de ensanche necesario:  media 0,88   máximo 1,42
```

**Cinco de dieciséis se caen**, y no al azar: las cuatro son la **línea de tiempo** y la
quinta es un rótulo largo. Las cifras (`d_*`) sobreviven todas con margen de sobra —eso
lo trata `207`—. Lo que muere en vertical es **el gráfico que explica**, no el que grita.

## El caso `linea_00`, entero

Es el peor y conviene verlo con todos los números porque es el patrón de los cuatro:

```
PNG nativo          1700 × 1040 px
font-size mayor       40 px  (el rótulo de cada hito)
mostrada en 16:9    1190 px  →  factor 0,700  →  28,0 px en pantalla
```

**28,0 px contra un suelo de 28,0.** Pasa por un píxel. No es holgura, es puntería.

En vertical, al mismo ancho relativo (1190 × 0,5625 = 669 px), el factor cae a 0,393 y el
rótulo queda en **15,7 px**. Para llegar al suelo vertical pide **948 px** sobre un lienzo
de 1080 — y la zona segura de texto son **820** (`49`, `203`).

> `linea_00` **no cabe en vertical a ningún ancho.** No es que esté pequeña: es que el
> ancho que necesita es mayor que el que la red le deja usar.

## Qué se hace con una pieza que no cabe

Cuatro salidas, en este orden. Las tres primeras son correctas; la cuarta es la que hay
que saber nombrar para poder rechazarla.

| Salida | Cuándo | Coste |
|---|---|---|
| **Ensanchar** | El ancho pedido cabe en 820 px | Cero: se cambia un número en la tabla |
| **Redibujar para vertical** | El HTML puede reflujarse a columna | Una plantilla más en `texto.py` |
| **Partir en dos piezas** | Una línea de tiempo con seis hitos | Dos elementos, dos anclas, más tiempo |
| ~~Encoger y confiar~~ | Nunca | Un gráfico que es textura (`376`) |

Para las cuatro `linea_*` la salida es **partir**: una línea de tiempo de seis hitos en
horizontal es una columna de tres en vertical, con el doble de cuerpo. El gráfico deja de
ser el mismo gráfico, y eso está bien: `200` ya dice que el vertical no es una exportación.

## Comprobarlo antes de renderizar

La comprobación es la misma que ya existe, con el factor puesto:

```python
FACTOR_VERTICAL = 1.417            # 34 px de caja frente a 24 (49)
ANCHO_MAX_TEXTO = 820              # zona segura de texto sobre 1080

for r, ancho_mostrado in piezas_de_texto:
    pide = ancho_legible(r) * FACTOR_VERTICAL          # en escala de 1920
    pide_v = pide * 1080 / 1920                        # sobre el lienzo vertical
    if pide_v > ANCHO_MAX_TEXTO:
        print(f"  🔴 {r}: pide {pide_v:.0f} px y el tope es {ANCHO_MAX_TEXTO} — redibujar")
    elif pide_v > ancho_mostrado * 1080 / 1920:
        print(f"  ⚠ {r}: ensanchar a {pide_v:.0f} px")
```

Se ejecuta con el resto de la auditoría, antes del render. Un gráfico ilegible cuesta lo
mismo de renderizar que uno legible y no se nota hasta el teléfono.

## Errores frecuentes

| Error | Consecuencia medida |
|---|---|
| Reutilizar el PNG del 16:9 al mismo ancho relativo | 5 de 16 piezas por debajo del suelo |
| Olvidar que el suelo vertical sube ×1,417 | `linea_00` queda en 15,7 px y parece bien en el monitor |
| Comprobar contra un ancho constante | El fallo de editpro `412`: 15 de 16 piezas aprobadas midiendo otra cosa |
| Encoger el gráfico para que quepa | Deja de ser información y pasa a ser decoración |
| Dar por buena una pieza que pasa por un píxel | `linea_00` pasa en 16:9 con 28,0 contra 28,0 |
| Ensanchar más allá de 820 px | Sale de la zona segura: se lee media línea de tiempo |
| Tratar cifras y gráficos con la misma regla | Las cifras sobran de margen; los gráficos se caen (`207`) |

## Relacionado

`203` densidad en vertical · `207` la cifra en vertical · `40` el texto como canal
principal · `42` tipografía del canal · `46` texto sobre collage · `49` zona segura y
tamaños · `164` legibilidad por altura de mayúscula · `166` la prueba del pulgar ·
editpro `412` texto y cifras · editpro `376` legibilidad real en celular
