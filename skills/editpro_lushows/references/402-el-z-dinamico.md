# 402 — El z dinámico: cambiar de plano a mitad de escena

**Qué resuelve:** la cadena de `overlay` es lineal y fija: un elemento va encima de **todo** lo anterior,
desde el primer fotograma hasta el último. Pero la narración pide lo contrario más veces de lo que parece
—el documento pasa por delante del retrato y luego se va detrás, la mano tapa la cifra a mitad de gesto—.
Este módulo es cómo se hace eso sin After Effects, qué cuesta y cuándo no vale la pena.

---

## 1. Por qué no existe un parámetro de z

En `overlay` no hay campo de profundidad. El z **es** la posición en la cadena (`400` §1), y la cadena se
arma una vez, antes del primer fotograma. Un elemento declarado en el eslabón 7 estará en el plano 7
durante toda la escena.

La única manera de que dos elementos intercambien plano es **declarar cada pareja dos veces, con `enable`
complementario**: un tramo con A encima y otro tramo con B encima. Es el mismo truco que el sándwich de
`377` —el mismo clip dos veces— llevado al orden de apilado.

---

## 2. El patrón, ejecutado

A y B se solapan. Hasta 0,6 s manda B; a partir de 0,6 s manda A.

```
[0:v]format=rgba[g];
[1:v]format=rgba,split=2[a1][a2];
[2:v]format=rgba,split=2[b1][b2];
[g][a1]overlay=200:75:enable='lt(t,0.6)'[p1];      # tramo 1: A abajo
[p1][b1]overlay=330:150:enable='lt(t,0.6)'[p2];    #          B encima
[p2][b2]overlay=330:150:enable='gte(t,0.6)'[p3];   # tramo 2: B abajo
[p3][a2]overlay=200:75:enable='gte(t,0.6)'[p4];    #          A encima
[p4]format=yuv420p[out]
```

Leído en el fotograma de cada tramo, en el punto donde los dos rectángulos se cruzan:

| instante | píxel medido | quién está encima |
|---|---|---|
| t = 0,20 s | `(60, 189, 118)` | **B** (verde) |
| t = 1,00 s | `(229, 68, 59)` | **A** (rojo) |

Tres detalles que no son opcionales:

- **`split` es obligatorio.** Una etiqueta de filtergraph se consume una sola vez; reutilizar `[a]` en dos
  `overlay` distintos aborta el render (`404` §2).
- **Los cuatro `overlay` tienen que cubrir todo el tiempo sin hueco ni solape.** `lt(t,0.6)` y
  `gte(t,0.6)` son complementarios exactos; `lte`/`gte` dejarían un fotograma con las dos ramas activas.
- **El cambio es instantáneo.** No hay interpolación de z: en un fotograma manda uno y en el siguiente el
  otro. Por eso el intercambio tiene que caer donde ya hay movimiento o un corte, nunca en medio de una
  imagen quieta, donde se lee como un parpadeo.

---

## 3. Lo que cuesta

Duplicar la pareja duplica los `overlay` de esos elementos. Y aquí está el dato que desarma la excusa
habitual —«pero si con `enable` solo está encendido la mitad del tiempo»—, medido sobre 8 capas de 600 px,
75 fotogramas, 1920×1080:

| montaje | CPU |
|---|---|
| 8 capas visibles todo el rato | **49,89 s** |
| 8 capas, cada una visible 1/8 del tiempo | **49,53 s** |

Idénticas. **Una capa apagada cuesta lo mismo que una encendida**, porque su cadena de `scale`, `format` y
`fade` se ejecuta en cada fotograma y `enable` solo decide si se mezcla el resultado. Así que un
intercambio de z cuesta exactamente el doble que la pareja normal (`408`).

Traducido a presupuesto: sobre el episodio real, elementos de ~800 px de ancho, cada `overlay` extra son
unos **0,09 s de CPU por fotograma de vida**. Un intercambio de 2 s sobre dos elementos son ~9 s de CPU.
Barato para una vez por episodio; caro como norma.

---

## 4. Cuándo vale la pena y cuándo no

| Caso | Vale | Por qué |
|---|---|---|
| Un objeto de la escena pasa por delante del gráfico | **sí** | Es la oclusión que hace creer que el gráfico está *dentro* del plano (`204` §3.5) |
| Un documento se repasa y luego cede el sitio | **sí** | La jerarquía cambia de verdad en ese segundo |
| Texto que se esconde detrás del sujeto | usa `377` | El sándwich lo resuelve mejor y con una sola máscara |
| «Para que se vea más dinámico» | **no** | Nadie lee un cambio de plano si nada más cambia |
| Dos elementos que se pisan y no sabes cuál va delante | **no** | Es un problema de colocación, no de z (`384`) |

**La regla:** una vez por episodio, en el momento que importa. El segundo intercambio ya no se lee como
profundidad, se lee como que las capas parpadean.

---

## 5. En CapCut, lo mismo es mover una pista

Fuera del filtergraph el z dinámico es más barato: se corta el clip en el instante del cambio y se sube o
baja uno de los dos trozos de pista. En `draft_content.json` el orden lo lleva el **`render_index`** de
cada segmento —mayor índice, más arriba (`377` §7, `113`)—, así que un intercambio son dos segmentos con
`render_index` cruzados y `target_timerange` que empalman al microsegundo. Un microsegundo de hueco no se
ve; mil sí.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Reutilizar la etiqueta de un elemento en dos `overlay` sin `split` | `Error binding filtergraph inputs/outputs` y render abortado |
| Condiciones de `enable` que se solapan un fotograma | Ese fotograma tiene las dos ramas: destello sucio |
| Condiciones que dejan un hueco | Un fotograma sin el elemento: parpadeo |
| Cambiar el z en medio de una imagen quieta | Se lee como fallo de render, no como profundidad |
| Contar con que la capa apagada no cuesta | Cuesta lo mismo: medido 49,53 s frente a 49,89 s |
| Usar z dinámico donde basta el sándwich de `377` | El doble de capas para el mismo efecto |
| Más de un intercambio por pieza | Deja de leerse como profundidad y pasa a parpadeo |

## Relacionado

`400` el orden de render es narrativo · `401` quién gana cuando dos coinciden · `404` acumular o
sustituir · `408` lo que cuesta cada capa · `409` depurar un apilado · `105` superponer capas ·
`204` §3.5 oclusión · `377` texto detrás del sujeto · `113` pistas y segmentos en CapCut ·
`canales_lushows/13` ciclo de vida del elemento
