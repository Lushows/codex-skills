# 200 · El vertical se renderiza, no se recorta

**Qué resuelve:** la tentación de sacar los cortes de 9:16 recortando el episodio ya
montado. Es gratis, tarda diez segundos y **produce un vídeo que parece bien y está
roto**. Este módulo mide exactamente cuánto está roto, sobre el episodio real, para que
la decisión no dependa de la impresión de nadie.

`editpro 147` explica por qué el vertical es otro idioma y `editpro 38` da la estrategia
del máster vertical. Aquí no se repite ninguna de las dos: se demuestra, con el motor de
este canal en la mano, que **este montaje en concreto no sobrevive al recorte**, y se
deja fijada la regla de producción que sale de ahí.

---

## La ventana, y por qué engaña

Recortar 9:16 centrado de un lienzo de 1920×1080 conserva el alto entero y deja una
franja de ancho:

```
ancho = 1080 × 9/16 = 607,5 px   →  x de 656,2 a 1263,8
0,316 del ancho original
```

La aritmética de la ventana ya está hecha en `editpro 417` y no se rehace. Lo que allí
no se puede saber —porque depende del montaje— es **qué le pasa a los objetos que hay
dentro**. Y esa es la pregunta.

## La medida, sobre `ep01-lustig`

59 elementos con vida visible en 63,45 s (`auditar.py ep01-lustig`). Se cruza la caja de
cada uno contra la ventana `x ∈ [656,2 · 1263,8]`:

```python
AN = 1080 * 9/16
X0, X1 = (1920 - AN)/2, (1920 + AN)/2
for ele in elementos:
    x0, y0, x1, y1 = caja(ele)
    frac = max(0.0, min(x1, X1) - max(x0, X0)) / (x1 - x0)
```

| Resultado | Elementos |
|---|---|
| Sobreviven **enteros** | **1** |
| Quedan **cortados** (asoman, parcialmente dentro) | **50** |
| Quedan **fuera del todo** | **8** |
| Total | 59 |

| Fracción de su ancho que conserva un elemento | |
|---|---|
| Media | **0,287** |
| Mediana | **0,224** |
| Conservan menos de la mitad | **49 de 59** |
| Conservan menos del 70 % | **54 de 59** |

Y la causa, en una línea: el ancho medio de un elemento del episodio es **802 px** y la
ventana mide **608**. **47 de los 59 elementos son más anchos que la ventana entera.**

## Por qué "se ve bien"

Ese 1 contra 50 es la trampa. Si el recorte dejara la pantalla vacía, nadie publicaría
el corte. Lo que hace es dejarla **llena de trozos**: cincuenta elementos asomando, cada
uno con el 22 % de su superficie dentro. El cuadro tiene peso, tiene movimiento, tiene
color. No tiene ni un solo objeto completo.

El único superviviente entero es `carcel_estampa`, de 458 px, colocado en `x` de 692,6 a
1150,6. Sobrevive por accidente: es el elemento más estrecho del bloque y cayó cerca del
centro. No hay ningún elemento que sobreviva por diseño, porque el diseño era otro.

Y los ocho que desaparecen del todo dicen el resto de la historia:

```
reglamento_celda   x  122,6 -  568,6     torre_construccion x   82,4 -  570,4
reloj_1947         x 1319,4 - 1829,4     monton_chatarra    x    9,4 -  643,4
aviso_falsos       x 1316,0 - 1756,0     telegrama_marshal  x   62,6 -  628,6
torre_postal       x  193,9 -  458,9     guardia_boveda     x 1270,5 - 1801,5
```

Son las dos posiciones de la banda `lado` (`W*0.19` y `W*0.79`), que es donde vive la
clase `objeto` (`243`). **El recorte centrado borra una banda entera del sistema**, y con
ella una de las cinco clases del motor.

## El elemento que lo decide

`retrato_lustig` —la cara del protagonista, el héroe del bloque `nombre`— conserva
**el 3 % de su ancho**. Sale 576 px de ancho en `x` de 1248 a 1824; la ventana acaba en
1263,8. Del retrato del hombre del que trata el episodio quedan dieciséis píxeles de
oreja.

Contra eso no hay reencuadre por plano que valga. `editpro 38` propone reencuadrar plano
a plano cuando el vídeo importa; aquí no hay planos, hay **59 elementos con vida propia
solapada** —simultaneidad media 2,05 y hasta 4 a la vez— y cada fotograma pediría una
ventana distinta. Reencuadrar esto es rehacer la colocación. Y rehacer la colocación es
exactamente lo que hace el motor, gratis, si se le da el lienzo correcto.

## La regla de producción

> **El vertical es una salida del motor, no una exportación del vídeo.** Se renderiza
> con `W_LIENZO, H_LIENZO = 1080, 1920`, su propia tabla de bandas (`203`) y su propia
> selección de elementos. El 16:9 y el 9:16 comparten guion, voz, banco de material y
> diccionario; **no comparten colocación**.

Lo que se hereda y lo que no:

| Comparten | No comparten |
|---|---|
| Guion y locución | Lienzo |
| `tiempos.json` (las anclas) | Bandas y posiciones |
| Banco de recortes, `fx/`, `archivo/` | Anchos de clase y techos de altura (`203`) |
| Diccionario palabra→imagen | Qué elementos entran (el vertical selecciona) |
| Música por bloque (`128`) | Piezas de texto: se redibujan (`204`) |

Cuesta un render más y una tabla más. Contra eso: 58 de 59 elementos rotos.

## Cuándo sí se puede recortar

Hay un caso, y conviene decirlo para que no se convierta en dogma: **un plano de un solo
elemento, centrado y estrecho**. Si el corte se compone a propósito con elementos por
debajo de 600 px en la banda `centro`, el recorte sobrevive. Eso no es recortar el
episodio: es montar un episodio distinto que además aguanta el recorte, y sale más caro
que renderizar en vertical.

## Errores frecuentes

| Error | Consecuencia medida |
|---|---|
| Recortar 9:16 centrado del episodio montado | 1 elemento entero de 59; 47 más anchos que la ventana |
| Mirar el corte de un vistazo y darlo por bueno | 50 elementos asomando llenan el cuadro sin comunicar nada |
| Reencuadrar "solo los planos importantes" | No hay planos: 59 vidas solapadas, 2,05 a la vez |
| Asumir que el héroe cae en el centro | `retrato_lustig` conserva el 3 % de su ancho |
| Dar por hecho que se pierde "algo de los lados" | Se pierde la banda `lado` entera, y con ella la clase `objeto` |
| Compartir la tabla de bandas entre los dos lienzos | Las fracciones sobreviven, los anchos no (`203`) |

## Relacionado

`203` densidad en vertical · `204` el texto manda · `242` colocación por rectángulo ·
`243` bandas y anclaje central · `49` zona segura y tamaños ·
editpro `147` formato vertical a fondo · editpro `38` adaptar a varios formatos ·
editpro `417` del vertical al cuadrado
