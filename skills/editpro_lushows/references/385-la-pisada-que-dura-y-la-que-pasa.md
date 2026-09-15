# 385 — La pisada que dura y la que pasa

**Qué resuelve:** el porcentaje solo no decide. Una pisada del 77% durante catorce centésimas no la ve
nadie; una del 20% durante tres segundos es de lo peor que puede tener un episodio. Este módulo pone el
tiempo dentro de la medida y explica por qué la vida de un elemento **no** es lo que dice su campo `dura`.

---

## 1. El pisada-segundo, y lo que pone del derecho

Dos pisadas reales de `episodio01`, las dos medidas hoy:

| El de abajo | El de encima | Tapado | Duración | Pisada-segundos |
|---|---|---|---|---|
| `fajo` | `camiones` | **77,3%** | 0,14 s | **0,108** |
| `planta_pescado` | `planta_pescado` | 19,6% | **3,16 s** | **0,619** |

La segunda pesa **5,7 veces más** que la primera. Ordenadas por porcentaje, la primera es la peor del
episodio y la segunda es la número doce. Ordenadas por pisada-segundos, se cambian el puesto. La segunda es
la que se ve.

Y cuando se mira la zona protegida (`382`), la distancia crece todavía más: esa pisada del 19,6% es un
**37,1% de cabeza tapada** durante 3,16 s.

---

## 2. La distribución medida

Las dos versiones del episodio 01, todas las parejas con contacto, agrupadas por cuánto dura el contacto:

| Duración del contacto | `ep01-lustig` (n) | Tapado medio | `episodio01` (n) | Tapado medio |
|---|---|---|---|---|
| menos de 0,25 s | 4 | 4,9% | 7 | 21,6% |
| 0,25 – 0,6 s | 7 | 10,2% | 7 | 29,1% |
| 0,6 – 1,2 s | 6 | 10,4% | 6 | 28,9% |
| 1,2 – 2,5 s | **13** | 10,8% | 10 | 20,7% |
| más de 2,5 s | 1 | 1,9% | 5 | 12,9% |

Lo que dice la tabla:

- **El grueso de los contactos vive en la franja de 1,2 a 2,5 s**, que es exactamente la vida típica de un
  elemento (`objeto` dura 2,60 s, `rotulo` 2,10 s). No son roces: son elementos que conviven casi toda su
  vida.
- La versión buena no tiene menos contactos —31 frente a 35— sino **contactos mucho más suaves**: 10,8% de
  media contra 20,7% en la franja larga.
- En `ep01-lustig` no hay ni un contacto largo fuerte. El único de más de 2,5 s tapa el 1,9%.

---

## 3. La vida no es `dura`: los fundidos se comen los extremos

`motor.py` mete cada elemento con `fade=t=in:d=0.30` y lo saca con `fade=t=out:d=fade_out`. Un elemento a
medio fundido **no está en pantalla**. `auditar.py` ya lo corrige y la cuenta es esta:

```python
SUBIDA = 0.30            # lo que tarda en aparecer; fijado en motor.py
OPACIDAD_MIN = 0.35      # por debajo, el ojo no lo registra como presente

def ventana_visible(ele, a, b):
    """(inicio, fin) del tramo en el que el elemento pasa del 35% de opacidad."""
    fo = ele.get("fade_out", 0.4) or 0.001
    return min(b, a + SUBIDA * OPACIDAD_MIN), max(a, b - OPACIDAD_MIN * fo)
```

Traducido a segundos por clase, con los valores reales de `CLASES`:

| Clase | `dura` | `fade_out` | Entra a los | Se va a los | Vida visible | Se pierde |
|---|---|---|---|---|---|---|
| `heroe` | 3,40 s | 0,45 | 0,105 s | 0,158 s antes | 3,14 s | 7,7% |
| `objeto` | 2,60 s | 0,40 | 0,105 s | 0,140 s antes | 2,36 s | 9,4% |
| `dato` | 3,10 s | 0,45 | 0,105 s | 0,158 s antes | 2,84 s | 8,5% |
| `rotulo` | 2,10 s | 0,30 | 0,105 s | 0,105 s antes | 1,89 s | 10,0% |
| `micro` | 1,40 s | 0,25 | 0,105 s | 0,088 s antes | 1,21 s | 13,8% |

**Consecuencia directa:** dos elementos cuyos `dura` se tocan por una décima puede que no coincidan nunca
en pantalla. Si el censo usa la vida entera, esa décima entra como pisada real y hay que salir a
arreglarla. El error no es teórico: la misma confusión daba por cubierto un cuadro cuyo único elemento
«vivo» estaba al 6% de opacidad, y las doce métricas del auditor decían que no pasaba nada.

**Y el error simétrico:** para juzgar la **densidad** del episodio hay que usar la ventana visible, pero
para juzgar la **duración media** de los elementos hay que usar la vida entera, rampas incluidas. Son dos
preguntas distintas y el auditor guarda las dos.

---

## 4. Umbral por duración

Con la distribución de arriba, esto es lo que sostengo:

| Contacto | Qué hacer |
|---|---|
| menos de 0,20 s | **Indulto automático**, salvo que sea texto. Es un cruce de entradas, no una pisada |
| 0,20 – 0,45 s | Se mira si el porcentaje pasa del umbral de su clase (`383`) |
| 0,45 – 1,2 s | Se aplica el umbral sin excepciones |
| más de 1,2 s | El umbral **baja un escalón**: lo que se sostiene un segundo largo, se lee |
| más de 2,5 s | Se mira aunque esté por debajo del umbral. El ojo tiene tiempo de sobra |

Y una regla que ahorra discusiones: **el indulto por duración corta nunca se aplica al texto.** 0,16 s de
titular tapado se leen como un parpadeo de error, no como un roce; el elemento no estaba ahí para mirarlo,
estaba para leerlo, y leer cuesta más que mirar.

---

## 5. El caso que no se ve por ningún lado: la pisada intermitente

Dos elementos que se pisan al 40% durante 0,3 s, se separan por `deriva`, y vuelven a pisarse. El censo
reporta **una** pisada de 0,3 s y la indulta. En pantalla son dos golpes, y dos golpes leves seguidos se
leen peor que uno fuerte porque parecen un fallo de render.

Se caza sumando los pisada-segundos **por pareja**, no por contacto:

```python
por_pareja = {}
for v, ps, bajo, arriba, co, esc, txt in pisadas:
    por_pareja.setdefault((bajo, arriba, esc), [0.0, 0.0])
    por_pareja[(bajo, arriba, esc)][0] += ps      # pisada-segundos acumulados
    por_pareja[(bajo, arriba, esc)][1] += co      # segundos de contacto
```

Si una pareja aparece dos veces en el mismo bloque, se trata como una sola y se la juzga por el total.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Ordenar las pisadas por porcentaje | La peor del episodio (19,6% × 3,16 s) queda en el puesto doce |
| Contar la vida entera, con fundidos | Elementos que nunca coinciden en pantalla entran como pisadas |
| Usar la ventana visible también para la duración media | La media de vida sale corta y el episodio parece más picado de lo que es |
| Indultar por duración corta también al texto | 0,16 s de titular tapado se leen como error de render |
| Sumar duraciones sin ponderar por lo tapado | Un roce del 2% pesa igual que un enterramiento |
| Tratar dos contactos de la misma pareja como dos casos | Dos golpes leves seguidos pasan el filtro y se ven peor que uno |
| Suponer que `fade_out` es siempre 0,4 | Un `micro` pierde el 13,8% de su vida, un `heroe` el 7,7% |

## Relacionado

`380` qué es pisar en números · `382` la zona protegida · `383` umbrales por tipo de contenido ·
`384` medir el solape antes de renderizar · `386` el elemento enterrado · `388` informar una pisada ·
`canales_lushows/13` ciclo de vida del elemento · `canales_lushows/144` presencia no es superficie
