# 207 · La cifra en vertical

**Qué resuelve:** de todo lo que el canal pone en pantalla, la cifra es lo único que
**gana** al pasar a vertical, y lo único cuyo pie de fuente **muere**. Las dos cosas
salen del mismo cálculo y hay que verlas juntas, porque una cifra sin fuente en este
canal no es una cifra: es una afirmación sin respaldo (`381`).

`44` fija la especificación completa de la cifra en 16:9 —tamaño, unidad, fuente,
duración— y no se repite. Aquí sólo lo que cambia en 1080×1920, con los números de las
piezas reales del episodio.

---

## Por qué la cifra gana

Las tres piezas de dato de `ep01-lustig` comparten plantilla: PNG de 262 px de alto, la
cifra a `font-size: 150px`, una línea de apoyo a 58 y el pie de fuente a 34.

| Pieza | PNG nativo | Ancho legible |
|---|---|---|
| `d_1890` | 1516 × 262 | **283 px** |
| `d_preso` | 1354 × 262 | 253 px |
| `d_anos` | 1180 × 262 | 220 px |

«Ancho legible» es el ancho mínimo para que el **cuerpo mayor** llegue al suelo
(`ancho_legible()`, `SUELO_TEXTO = 28`). 283 px sobre un lienzo de 1920 es nada: la cifra
aguanta cualquier reducción que un montaje razonable le pueda hacer. Y en vertical, donde
`203` le da 980 px de ancho de clase sobre un lienzo de 1080, la cifra ocupa **el ancho
entero de la columna**. En 16:9 comparte cuadro con un recorte a su lado; en vertical no
hay lado, así que la cifra manda sola. Es el único elemento del sistema al que el formato
le sienta bien.

## Por qué el pie muere

El mismo cálculo, aplicado al cuerpo **menor**:

```
d_1890, PNG nativo 1516 px

16:9    mostrada a 1340 px  →  factor 0,884
        cifra   150 × 0,884 = 132,6 px      suelo 28,0  →  OK, ×4,7 de margen
        pie      34 × 0,884 =  30,1 px      suelo 28,0  →  OK, por 2,1 px

9:16    mismo ancho relativo: 754 px sobre 1080  →  factor 0,497
        cifra   150 × 0,497 =  74,6 px            →  OK
        pie      34 × 0,497 =  16,9 px            →  suelo vertical 22,3  →  NO
```

El suelo vertical (`204`) es `28 × 1080/1920 × 1,417 = 22,3 px` sobre el lienzo de 1080.
El pie se queda en 16,9. **Falla por un 24 %.**

Y la asimetría es lo que lo hace peligroso: la cifra sale con un margen de 3,3 veces el
suelo y el pie falla. Quien mire el corte en el monitor verá un número enorme y perfecto
con una línea gris debajo, y dará por hecho que la línea gris se lee porque el número se
lee. En el teléfono la línea gris no existe.

## Las tres salidas

| Salida | Cómo | Cuándo |
|---|---|---|
| **Subir el pie en la plantilla** | `font-size` del pie de 34 a 58 px, misma pieza redibujada | Es la salida por defecto: la plantilla ya tiene ese cuerpo |
| **Sacar el pie a un rótulo propio** | La fuente va como `rotulo` con su propia ancla | Cuando la fuente es larga o hay dos |
| **Poner la fuente en la descripción** | Y sólo ahí | Nunca: la descripción no se ve mientras se ve el vídeo |

La tercera está en la tabla porque es la que todo el mundo propone y hay que poder
rechazarla con un argumento y no con una opinión: **quien ve el corte no ve la
descripción**. El contrato del canal es que la prueba viaja con la afirmación, en el
mismo plano (`381`, `389`). Si el pie no cabe, se redibuja la pieza; no se traslada la
responsabilidad al pie de página.

Redibujar es barato, además, porque la plantilla ya tiene los tres cuerpos:

```
150 px → la cifra          se queda
 58 px → la línea de apoyo pasa a ser el pie de fuente en vertical
 34 px → el pie            desaparece de la versión vertical
```

58 × 0,497 = 28,8 px, por encima del suelo vertical de 22,3. La plantilla vertical de dato
tiene **dos cuerpos, no tres**. Un dato con tres niveles de información en una columna de
1080 px es un dato que no se ha decidido.

## Dónde va

`203` le da a `dato` la banda `cifra`, en `y = 960` y `y = 845`. Es decir, **el centro del
cuadro**, no el pie — que es donde estaba en 16:9 (`H*0.62`, `243`) y donde en vertical
vive el subtítulo (`206`).

Eso cambia el reparto del plano de la cifra: en 16:9 la cifra descansa debajo del recorte;
en vertical **la cifra desplaza al recorte**. Cuando entra un `dato` a 980 px de ancho, lo
que estuviera en `centro` se va a `arriba` o se apaga. Es el mismo cálculo de pila de
`203`: 326 px de cifra más 653 de héroe más 40 de hueco son 1019, que sí cabe en 1200 — así
que un dato y un héroe pueden convivir, pero un dato y un objeto grande, no.

## La duración no cambia, y hay que defenderla

`CLASES` da a `dato` 3,10 s, más que a ninguna otra clase. La tentación en vertical es
recortarla «porque el formato es rápido». Con 54 cambios de subtítulo por minuto (`206`),
una cifra de 3,10 s convive con **unos tres bloques de subtítulo**: el espectador la lee,
la oye nombrar y la ve seguir ahí mientras la voz explica qué significa. Bajarla a 2 s la
deja en dos bloques y se pierde la tercera parte que es la que la convierte en argumento.

En vertical la cifra dura igual o más. Lo que se acorta son los `micro`, que en una
columna sin esquinas casi no tienen sitio.

## Errores frecuentes

| Error | Consecuencia medida |
|---|---|
| Reutilizar la pieza de dato del 16:9 | El pie de fuente queda en 16,9 px contra un suelo de 22,3 |
| Deducir que el pie se lee porque la cifra se lee | La cifra tiene ×3,3 de margen y el pie falla por un 24 % |
| Mandar la fuente a la descripción | Quien ve el corte no ve la descripción |
| Mantener los tres cuerpos de la plantilla | En una columna de 1080 px sobran; dos y se decide |
| Dejar la cifra en el pie como en 16:9 | Ahí vive el subtítulo quemado (`206`) |
| Meter un dato y un objeto grande a la vez | La pila se pasa de los 1200 px de columna |
| Acortar la cifra «porque el formato es rápido» | Pierde el tercio en que la voz explica qué significa |

## Relacionado

`44` la cifra en pantalla · `36` contadores y cifras animadas · `204` el texto manda ·
`203` densidad en vertical · `206` subtítulos siempre · `381` la carga de la prueba ·
`243` bandas y anclaje central · editpro `412` texto y cifras
