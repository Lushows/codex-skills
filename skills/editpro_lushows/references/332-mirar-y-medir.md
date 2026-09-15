# 332 — Mirar Y medir: por qué ninguna de las dos sola alcanza

**Qué resuelve:** el caso más caro de todos. El de la toma que **pasa todas las mediciones** y está mal. Y
el de la toma que **se ve bien** y está rota. Los dos errores existen, son distintos, y solo se cierran
haciendo las dos cosas.

---

## 1. El caso real: cuatro indicadores en verde y las caras moradas

Material de Bendita Pola, toma `lv_0_20260804122837` — la de las escaleras. Medida completa del cuadro:

| Indicador | Valor | Lectura automática |
|---|---|---|
| `YAVG` (brillo medio) | 72,3 | oscuro pero dentro de rango — **verde** |
| `UAVG` | **127,99** | por debajo de 128, "hay piel posible" — **verde** |
| `SATAVG` | 13,4 | sin luz de color dominando — **verde** |
| Densidad de bordes | 4,24% | fondo normal — **verde** |

Cuatro verdes. Y la toma es **inutilizable**: la persona es una silueta a contraluz de 60 píxeles de
ancho, contra un vano de puerta quemado, entre barandas.

El `UAVG` de 127,99 es el detalle que hay que entender. Pasó el umbral por dos centésimas — no porque
hubiera piel bien expuesta, sino porque **el 96% del cuadro es escalera, pared y sombra**, y ese promedio
gigante empujó el número justo debajo del límite. El neón rojo de arriba y el morado de la derecha se
cancelaron entre sí en la media. El indicador midió correctamente. Midió lo que no importaba.

---

## 2. Por qué el promedio ahoga a la cara

Los números son estos, y explican todo el módulo.

Un fotograma vertical de 540 × 960 tiene **518.400 píxeles**. Una cara en plano medio ocupa unos
80 × 90 = **7.200 píxeles**. Eso es **1,4% del cuadro**.

> Si la cara está completamente equivocada de color y el resto está perfecto, el promedio global se mueve
> **menos de dos unidades**. Un promedio global no puede detectar un problema que vive en el 1,4% de los
> píxeles. **No es que mida mal: es que no lo está mirando.**

Y funciona en las dos direcciones: también hay tomas donde la cara está perfecta y el promedio global sale
horrible porque hay una pared morada detrás. Descartarlas por el promedio es botar la toma buena.

---

## 3. El mismo error, un nivel más adentro

Ahora la parte incómoda. La solución obvia es "medir solo la cara". Pero el promedio sigue ahogando cosas
**dentro** de la cara. Medidas reales de la toma 12 (`155807`, la barra con neón morado):

| Región medida | YAVG | UAVG | VAVG | Veredicto |
|---|---|---|---|---|
| Cuadro completo | 71,6 | 143,2 | 170,5 | rojo evidente |
| Recuadro de la cara (incluye barba) | 119,6 | **127,9** | 176,9 | **verde por 0,1** |
| Solo la mejilla y la frente | 166,0 | **128,1** | 179,8 | rojo |

La barba oscura, dentro del recuadro de la cara, arrastró el `UAVG` de 128,1 a 127,9 y **volteó el
semáforo**. Dos décimas. Y con la cara visiblemente rosada en pantalla.

Compárala con la toma 7 (`135656`, terraza con luz de día), misma región:

| Región | YAVG | UAVG | VAVG | SATAVG |
|---|---|---|---|---|
| Mejilla y frente | 123,0 | **111,4** | 162,3 | 37,8 |

Ahí sí hay piel. La diferencia entre 111 y 128 no es sutil cuando la miras: una cara es una cara y la otra
es una calcomanía rosada.

**Conclusión operativa:** mide en la **mejilla y la frente**, nunca en un recuadro que incluya barba,
pelo, lentes o sombra del cuello. Y aun así, mira la imagen.

---

## 4. Qué ve el ojo que el número nunca verá

- **Si la expresión sirve.** Ningún filtro mide si alguien se ve incómodo.
- **Si la mirada va a cámara.** Cambia todo el sentido del plano y no aparece en ninguna tabla.
- **Si hay algo que no debería estar en cuadro.** Un cable, una caja, alguien pasando al fondo, un vaso a
  medio tomar de otra toma.
- **Si el encuadre deja sitio para el texto** (`262`, `44`).
- **Si la persona está bien.** El material del 4 de agosto tiene tomas donde se ve cansancio. Eso no lo
  mide `signalstats`.

## 5. Qué mide el número que el ojo nunca verá

- **Diferencias de 3–5 puntos de brillo entre dos tomas** que se van a cortar seguidas. Invisibles de a
  una; obvias en el corte (`62`).
- **Una dominante de color que el ojo ya aceptó.** Después de veinte minutos mirando material morado, el
  cerebro te dice que es blanco. Se llama adaptación cromática y es real.
- **Zonas quemadas.** `YHIGH` cerca de 255 dice que ahí no hay información que recuperar; en la pantalla
  del celular parece "un fondo bien iluminado".
- **Que una toma esté a 29,58 fps y otra a 30.** Se ve como un tirón raro y nadie sabe por qué.
- **El foco.** Ver enfocado en una pantalla de 6 pulgadas no significa nada.
- **El porcentaje de píxeles quemados en una zona.** El ojo dice "está bien iluminado"; la medición dice
  que ahí no hay información que recuperar (`336`).
- **Que un archivo venga con fps variable.** No se ve en ningún fotograma: se oye tres semanas después,
  cuando el audio se desliza (`339`).

---

## 6. El protocolo: mirar → medir → mirar

Tres pasadas, en este orden. No se puede saltar ninguna.

**Pasada 1 — Mirar (2 minutos).** Hoja de contactos de todo el material (`333`). Descarta lo obvio y marca
3 a 5 finalistas. El ojo humano es el mejor descartador rápido que existe.

**Pasada 2 — Medir (3 minutos).** Solo las finalistas. Cuadro completo, cara, fondo pegado al contorno
(`331`). Ordena por diferencia cara–fondo.

**Pasada 3 — Mirar otra vez (1 minuto).** Abre la ganadora **a tamaño real**, no en miniatura, y
reprodúcela. La miniatura esconde el foco, el micro-movimiento y la expresión.

Si la pasada 3 contradice a la pasada 2, **gana la pasada 3** — pero anota por qué. Esa nota es lo que
mejora tus umbrales para el próximo rodaje.

---

## 7. Los cuatro indicadores que más engañan

1. **`UAVG` global cerca de 128.** Es el peor de todos porque parece preciso. Un cuadro puede promediar
   128 con la mitad naranja y la mitad azul.
2. **`SATAVG` bajo.** Significa "poca saturación **en promedio**". Con un fondo negro grande, una cara
   fosforescente te da saturación media baja.
3. **`blurdetect` global.** Un primer plano con fondo desenfocado a propósito da valores de "toma
   borrosa". Mide siempre en la zona del sujeto.
4. **Densidad de bordes global.** En la toma 7 el cuadro completo da 6,30%, pero la banda alrededor del
   sujeto da **5,74%** y la franja superior (plantas y techo) da **10,47%**. El enredo estaba lejos de la
   persona, donde no molesta. Descartar esa toma por el número global habría sido botar la mejor.

---

## 8. La regla, dicha corta

> **Los números descartan, el ojo decide, y ninguno de los dos trabaja solo.**
>
> - Medir sin mirar produce **la toma correcta según la tabla y equivocada según el mundo**.
> - Mirar sin medir produce **la primera toma que apareció** (`330`).
>
> Y cuando midas, **mide donde está el problema**. Un promedio global es un resumen; los defectos no
> viven en los resúmenes.

Es la misma idea que en `98`: un render que corrió sin errores no prueba que el video tenga sentido. Un
indicador en verde no prueba que la toma sirva.

---

## Errores comunes

1. **Medir el cuadro completo y sacar conclusiones sobre la cara.** La cara es el 1,4% del cuadro.
2. **Creerle a un umbral por dos décimas.** 127,9 y 128,1 son el mismo número; lo que decide es la
   imagen.
3. **Meter la barba, el pelo o los lentes en el recuadro de la piel.** Arrastran la media y voltean el
   semáforo.
4. **Mirar solo la miniatura.** El foco y el micro-movimiento no existen a 200 px.
5. **Confiar en el ojo después de veinte minutos con el mismo material.** El cerebro se adapta al color y
   te miente. Sal, mira otra cosa treinta segundos, vuelve.
6. **Juzgar el color en la pantalla del celular con brillo automático.** Fija el brillo antes de decidir
   (`69`).
7. **Descartar una toma por densidad de bordes global.** Mide la banda alrededor del sujeto.
8. **Usar `blurdetect` global para juzgar el foco de una cara.** Recorta la cara y mide ahí.
9. **Medir después de aplicar un filtro.** Se mide el material como salió de la cámara.
10. **No anotar cuándo el ojo le ganó al número.** Esa nota es la que afina tus umbrales.
11. **Pedirle a un modelo que "vea" el video.** No lo ve: ve los fotogramas que le pases. Pásale la hoja
    de contactos y dile en qué casilla mirar (`333`).
12. **Creer que un solo indicador basta.** Ninguno basta. Ni cuatro bastan si todos son globales.

---

## Checklist

- [ ] Hice la pasada de **mirar** antes de medir nada.
- [ ] Medí solo las **finalistas**, no las 16.
- [ ] Medí el **cuadro completo** y además la **cara** por separado.
- [ ] El recuadro de la piel es **mejilla y frente**, sin barba ni pelo ni sombra.
- [ ] Medí el **fondo pegado al sujeto**, no el fondo en general.
- [ ] Calculé la **diferencia** cara–fondo, no solo los valores sueltos.
- [ ] Miré la ganadora **a tamaño real** y reproducida, no en miniatura.
- [ ] Ningún indicador que use es un **promedio global** como única prueba.
- [ ] Si el ojo contradijo a la tabla, **anoté por qué**.
- [ ] Verifiqué el color de la piel en la **zona de piel**, no en el promedio del cuadro.
- [ ] Descansé la vista antes de la decisión final de color.
- [ ] Dejé escrita, en una línea, la razón de la toma elegida.
