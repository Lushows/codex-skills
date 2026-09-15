# 430 — El destello como puntuación

> Un fogonazo no añade información. Dice **dónde termina la frase**. Es un signo de puntuación, y como
> todos los signos de puntuación, se vuelve ruido en cuanto hay demasiados.

Este bloque (430–439) trata la luz como **recurso de montaje medido**: cuándo un destello puntúa, qué
forma tiene su curva, cuánto dura, cómo se comprueba. No trata de iluminar una escena (eso es `223` y
`275`), ni del color de la luz (`224`), ni de la luz que da hambre (`340`), ni del flash **entre dos
planos** como transición — ese es `53`, y la frontera importa:

| Recurso | Dónde cae | Módulo |
|---|---|---|
| Flash de blanco que tapa un corte entre A y B | **en el corte** | `53` |
| Fogonazo sobre el plano, encima de una palabra | **dentro del plano** | **430–433** |
| Resplandor permanente de las luces del cuadro | **todo el plano** | `434`, `267` |
| Decidir que el vídeo "tenga luz de archivo" | — | `directorcreativo_lushows` |

`53` es un corte disfrazado. Este bloque es un acento sobre una imagen que no se corta.

---

## 1. Los tres trabajos legítimos de un destello

Si tu fogonazo no hace uno de estos tres, es adorno y hay que quitarlo.

1. **Rematar una frase.** La voz cierra el gancho y la luz cae sobre la última palabra tónica. El
   espectador no ve un efecto: siente que la frase terminó con punto y no con coma.
2. **Marcar un cambio de terreno.** Se pasa de un asunto a otro sin cortar a negro. El destello hace de
   salto de párrafo.
3. **Revelar un dato.** Aparece la cifra, el documento, la cara. La luz es el gesto de "míralo".

Lo que **no** es un trabajo: rellenar un tramo aburrido. Un bloque aburrido no se arregla con luz, se
arregla cortando (`27`).

---

## 2. Dato medido: cómo se reparten en dos episodios reales

Del motor documental (`C:\Users\user\Desktop\CANALES-LUSHOWS\piloto`), leyendo `DESTELLOS` en
`guion_visual.py` y resolviendo cada ancla contra `tiempos.json`:

| Episodio | Bloque | Palabra ancla | t (s) | Fuerza | Separación |
|---|---|---|---|---|---|
| 01 | gancho | millones | 1,07 | 0,16 | — |
| 01 | gancho | chapo | 8,74 | 0,19 | +7,67 s |
| 01 | peso | toneladas | 22,18 | 0,17 | +13,45 s |
| 01 | maquina | papel | 50,12 | 0,13 | +27,94 s |
| 01 | piezas | fachada | 63,59 | 0,12 | +13,48 s |
| 01 | remate | **pescado** | 71,88 | **0,22** | +8,29 s |
| lustig | muerte | hombre | 6,88 | 0,15 | — |
| lustig | oficio | **aprendiz** | 20,55 | **0,22** | +13,67 s |
| lustig | nombre | broma | 33,02 | 0,14 | +12,47 s |
| lustig | torre | Eiffel | 41,85 | 0,18 | +8,83 s |
| lustig | metodo | consta | 62,93 | 0,20 | +21,08 s |

Lo que sale de ahí, y que sirve como punto de partida para cualquier pieza hablada:

- **Densidad:** 6 destellos en 79,7 s y 5 en 62,98 s → **uno cada 12,6–13,3 s**. En frecuencia, 0,08 Hz.
- **Separación mínima real: 7,67 s.** Dos fogonazos más cerca que eso empiezan a leerse como parpadeo,
  no como puntuación.
- **Rango de fuerza: 0,12 a 0,22.** No 0,14–0,22: los bloques explicativos bajan a 0,12–0,13 a propósito.
- **El más fuerte (0,22) cae siempre en la palabra que remata**, y es el único que además se ensancha
  (`ancho` 0,090–0,095 en vez de 0,075 → `431`).

**La regla de "uno por bloque" tiene una excepción medida:** el bloque `gancho` del episodio 01 lleva
dos. Es defendible porque son los 10 primeros segundos y están a 7,67 s, pero es el límite: en el resto
del episodio nunca se repite dentro de un bloque.

---

## 3. La jerarquía: no todos valen lo mismo

Un episodio con cinco destellos iguales no tiene puntuación: tiene un tic. La escalera que funciona:

| Papel | Fuerza | Ancho | Cuántos |
|---|---|---|---|
| El remate del episodio | 0,22 | 0,090–0,095 s | **uno solo** |
| Los golpes de apoyo | 0,16–0,20 | 0,075 s | dos o tres |
| Los marcadores de bloque explicativo | 0,12–0,14 | 0,075 s | los que hagan falta, sin pasar de la densidad |

Si dudas cuál es el remate: es la palabra que, si la quitas, el vídeo ya no se entiende. Esa lleva el
0,22. Todo lo demás baja.

---

## 4. La prueba de que puntúa (y no decora)

Tres comprobaciones, en este orden, antes de dar un destello por bueno:

**La prueba de la transcripción.** Escribe la frase del bloque y pon un punto donde cae el fogonazo. Si
la frase escrita no pediría un punto ahí, el destello está mal colocado. Esta prueba de 20 segundos
resuelve el 80 % de los casos.

**La prueba del mudo.** Quita el audio y mira el vídeo. Si sin voz el destello parece caprichoso, es
porque estaba puntuando algo que sólo existía en la locución, y eso está bien — pero entonces tiene que
llevar su sonido, sin excepción (`433`).

**La prueba del recuento.** Cuenta los destellos y divide por la duración. Si sale más de uno cada 7 s,
sobran (`439`).

---

## 5. Dónde NO va un destello

- **Sobre una cara hablando.** Se lee como un fallo de exposición de la cámara, no como un acento.
- **En los últimos 1,5 s de la pieza.** El cierre necesita que la imagen se apague, no que grite.
- **Sobre comida.** Aplana el plato y le quita el brillo especular, que es justo lo que da hambre
  (`340`).
- **En pieza de menos de 15 s.** El ritmo ya lo llevan los cortes (`20`) y el destello compite con ellos.

En las dos piezas medidas **ningún destello cae en el mismo fotograma que un corte**: todos caen dentro
de un plano que sigue. Por eso se leen como puntuación. Si quieres que luz y corte coincidan, eso ya es
transición y se construye como en `53`, no con la campana de `431`.

---

## Errores frecuentes

- **Poner un destello porque el bloque se hacía largo.** No da ritmo, lo marca. El ritmo se arregla en
  la tijera (`27`).
- **Todos con la misma fuerza.** Sin jerarquía no hay puntuación: hay un tic. Uno a 0,22, el resto abajo.
- **El más fuerte en el sitio equivocado.** El 0,22 va en la palabra que remata, no en la primera imagen
  bonita del episodio.
- **Dos destellos a menos de 7 s.** Se lee como parpadeo; el mínimo medido en material que funciona es
  7,67 s.
- **Confundirlo con la transición de `53`.** Una tapa un corte, la otra puntúa un plano continuo.
  Mezclarlas produce cortes que parpadean sin motivo.
- **Dejarlo mudo.** El error más caro del bloque, y tiene módulo propio: `433`.
- **No medirlo.** "Se ve bien" no es un dato: la curva se mide en 30 segundos con `432`.

---

## Relacionado

- `431` la forma de la curva · `432` cómo se mide · `433` su sonido y la sincronía · `436` el pulso lento
  de exposición · `437` anclar la luz a la palabra · `438` cuándo marea · `439` cuántos caben.
- `53` — whip, flash y golpe **como transición entre dos planos**. `20`, `27` — pulso y diagnóstico.
- `canales_lushows` `125-musica-y-destello.md` — el motor concreto del canal documental (tabla
  `DESTELLOS`, `motor.py`, el acorde que acompaña al golpe). Allí vive la implementación; aquí, el
  criterio.
