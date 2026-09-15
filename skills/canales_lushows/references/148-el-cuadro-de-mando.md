# 148 · El cuadro de mando del episodio

**Qué resuelve:** las doce medidas juntas, cada una con su objetivo y el fallo concreto
que caza. Ninguna se lee sola; siete se añadieron después de que el fallo llegara al vídeo.

---

## La tabla

| # | Medida | Objetivo | Fallo que caza |
|---|---|---|---|
| 1 | **eventos/min** | ≥ 44 (por bloque: gancho 50, remate 30) | Pase de diapositivas; falta material |
| 2 | **simultaneidad media** | ≥ 2,00 elementos vivos | Relevo seco: entra uno, sale uno, nunca hay capas |
| 3 | **cobertura media** | 22–38 % del lienzo | Recortes flotando; o, por arriba, saturación |
| 4 | **cuadro casi vacío** | 0 tramos > 0,8 s con < 14 % cubierto | El suelo: medio episodio pelado con la media en rango |
| 5 | **huecos** | 0 tramos ≥ 0,40 s sin ningún elemento | Fondo solo; colas de escena sin guion visual |
| 6 | **reparto 3×3** | ningún recuadro < 12 % del tiempo | Agujero fijo en la composición |
| 7 | **equilibrio izq/der** | cada mitad ≥ 4 % cubierta | Todo el peso en un lado, que el 3×3 no ve |
| 8 | **oclusión** | 0 elementos > 55 % tapados | Se paga un evento que no comunica nada |
| 9 | **fuera de cuadro** | 0 elementos > 12 % fuera | Al protagonista se le come la cara el borde |
| 10 | **planos de sólo texto** | 0 tramos ≥ 0,7 s | Un titular sobre el fondo no es un plano de collage |
| 11 | **repetición** | ≤ 1,25 usos por recurso; ≥ 25 s entre usos | "Esto ya lo he visto": falta material |
| 12 | **ortografía** | 0 piezas sin tilde | `ANOS` o `DEFUNCION` en pantalla |

Aparte, dos avisos sin umbral propio: **duración media** (1,6–2,4 s) y **saturación**
(segundos con más de 4 elementos vivos).

## Informe real completo

`python auditar.py ep01-lustig`, 63,45 s, 5 escenas, 51 elementos:

```
  EVENTOS/min             49.2   (objetivo >= 44)
  simultaneidad media     2.15   (objetivo >= 2,00)
  duracion media          2.68 s (objetivo 1,6 - 2,4)
  COBERTURA media        39.5 %  (objetivo 22 - 38 %)
  cuadro casi vacio       3.15 s = 5%  (menos del 14% cubierto)
  HUECOS                     1   (objetivo 0)
  vacio total             0.65 s = 1% del episodio

  --- tramos sin ningun elemento en pantalla ---
    46.05 -  46.70  (0.65 s)  torre     "volvió"

  Reparto del cuadro (% del tiempo con algo en cada recuadro):
        izquierda   centro    derecha
   arriba        36%       47%       55%
   medio         50%       40%       70%
   abajo         43%       69%       43%

  Repeticion: 48 gestos · 39 recursos distintos · 1.23 usos por recurso  (objetivo <= 1,25)
```

Lectura: **tres cosas que tocar.** Un hueco de 0,65 s en `torre` sobre la palabra
"volvió"; duración media 2,68 s (planos largos); cobertura 39,5 %, pasada por arriba.
Lo demás pasa. Ninguna de las tres se habría sabido mirando el vídeo sin cronómetro.

## Cómo se leen en pareja

Las medidas se contradicen entre sí a propósito. Ahí está el diagnóstico:

| Combinación | Diagnóstico |
|---|---|
| eventos/min alto + simultaneidad baja | Relevos secos: 67,4 y 1,12 en el piloto, y se veía pobre |
| 0 huecos + cobertura baja | Presencia sin superficie (`144`) |
| cobertura media en rango + suelo malo | Dos láminas grandes tapan medio episodio (`145`) |
| cobertura alta + reparto con recuadro muerto | Todo apilado en un tercio |
| 3×3 correcto + equilibrio malo | Un elemento ancho ocupa 4 recuadros, los 4 a la derecha |
| repetición 1,09 "sin repeticiones" | Se está contando el fichero, no el dibujo (`142`) |
| planos de sólo texto + cobertura ~21 % | Tope del texto: un titular no pasa del 23 % |

## Orden de corrección

Cada paso cambia los siguientes; saltárselo obliga a medir sobre datos falsos.

1. **Anclas huérfanas** (`! ancla sin coincidencia`): hasta que no quede ninguna, todo
   lo demás describe un montaje que no se va a renderizar.
2. **Huecos**, los largos primero. Un hueco de 4,58 s en una escena de 5,44 s no es un
   hueco: es una escena sin guion visual y se rehace entera.
3. **Suelo de cobertura y planos de sólo texto**: ahí falta imagen.
4. **Reparto, equilibrio, oclusión y fuera de cuadro**: colocación, no cantidad.
5. **Repetición**: si sube al arreglar lo anterior, hace falta material nuevo.
6. **Ortografía**: la última, porque se arregla en el HTML y no mueve ninguna otra cifra.
7. **Eventos/min y duración media**: casi nunca hay que tocarlos; se corrigen solos.

## Las siete que nacieron de un fallo publicado

Cobertura y suelo (`144`, `145`), fuera de cuadro y cobertura visible (`146`), oclusión
—la ficha del juicio enterrada bajo la foto del tribunal, que sólo se vio en la rejilla,
ya renderizada—, planos de sólo texto —4,9 s de titular sobre el fondo que el chequeo no
encontraba porque miraba sólo el banco común y no la carpeta del episodio—, repetición
por familia (`142`) y ortografía (`143`).

Ninguna se le ocurrió a nadie por adelantado. **Por eso la tabla no está cerrada:** cada
vez que algo se cuela al vídeo, la pregunta no es "cómo lo arreglo" sino "qué medida me
habría avisado".

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Leer una medida sola | Se aprueba un episodio pobre con 67 eventos/min |
| Corregir en desorden | Se rellena un montaje que va a cambiar entero |
| Perseguir la cifra en vez del cuadro | Sube el número y empeora la composición |
| Tratar la tabla como definitiva | El próximo fallo no tiene medida que lo cace |
| Renderizar con una medida fuera | 15–25 min para ver lo que el informe ya decía |

## Relacionado

`17` medir el montaje · `140` medir antes de renderizar · `141` elegir un umbral ·
`144` presencia no es superficie · `145` la media esconde el suelo · `147` cuándo una
métrica deja de servir
