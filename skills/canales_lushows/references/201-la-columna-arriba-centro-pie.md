# 201 · La columna: arriba, centro, pie

**Qué resuelve:** en 16:9 el cuadro tiene cuatro direcciones y el montaje reparte el peso
en un plano. En 9:16 hay **una sola dirección**, y el reparto deja de ser geometría para
volverse **guion**: cada franja de la columna dice una cosa distinta y siempre la misma.
Este módulo fija qué dice cada una, antes de que `203` diga dónde cae exactamente.

`editpro 147` explica que en vertical desaparece el plano general y que el sujeto vive en
el tercio superior. Eso vale para vídeo grabado. Aquí no hay sujeto: hay un collage de
recortes sobre un fondo, y la pregunta es otra —**qué función tiene cada altura**.

---

## Lo que el 16:9 reparte y el vertical no puede

El auditor imprime el reparto del cuadro de `ep01-lustig` en nueve recuadros (porcentaje
del tiempo con algo dentro):

```
              izquierda   centro    derecha
     arriba        36%       29%       54%
     medio         53%       53%       61%
     abajo         37%       50%       35%
```

Nueve casillas, ninguna por debajo del 29 %: el peso circula. En vertical ese reparto se
colapsa, y hay que separar dos anchos que en 16:9 daba igual confundir:

| | Ancho disponible | Para qué |
|---|---|---|
| **Imagen** | 1080 px, el lienzo entero | Un recorte puede sangrar por el canto: se lee como collage |
| **Texto** | **820 px** (`49`: 60 a la izquierda, 200 a la derecha) | Un rótulo cortado por el canto se lee como fallo |

Con el ancho de imagen, un elemento de la clase `objeto` (800 px, `203`) puede desplazarse
**±140 px** a izquierda o derecha antes de salirse; con el de texto, ±10. La columna
izquierda y la derecha dejan de existir como posiciones: existen como **sangrado**.

> Regla que sale de ahí: en vertical **no se compone a lo ancho, se compone a lo alto**.
> Todo elemento que informe está centrado en `x` o casi; lo que se mueve es la `y`.

## Los tres registros

| Franja | `y` (sobre 1920) | Qué vive ahí | Por qué |
|---|---|---|---|
| **Arriba** | 200 – 620 | El **quién** y el **cuándo**: retrato, sello de columna, marca de bloque | Es lo primero que el ojo toca al entrar y lo último que la interfaz tapa |
| **Centro** | 620 – 1180 | La **prueba**: el recorte de archivo, el documento, el objeto | Es el centro óptico real (`49`: `x` 470, `y` 800) y donde la mirada descansa |
| **Pie** | 1180 – 1400 | La **cifra** y el **subtítulo** | Justo encima de lo que la red tapa, y donde el pulgar no está |
| *(vetado)* | 0–200 y 1400–1920 | Fondo y nada más | Interfaz de la plataforma (`202`) |

Los tres registros no son decorativos: son **los tres tiempos de una frase documental**.
Quién lo dice, qué lo prueba, cuánto costó. Si un corte vertical pone la cifra arriba y
el retrato abajo, sigue viéndose; deja de leerse como una afirmación con respaldo.

## Por qué el pie es el sitio de la cifra y no de la firma

En 16:9 la banda `cifra` está en `H*0.62`, centro-baja, «donde descansa la mirada y donde
no pelea con el recorte» (`243`). En vertical ese razonamiento se mantiene pero el punto
se mueve: por debajo de `y = 1400` empieza la zona que la red pinta, así que el pie útil
es una franja de **220 px**, y ahí no caben dos cosas.

Compite con el subtítulo quemado, que también quiere el pie (`206`: bloque de una línea a
56 px de caja, unos 150 px con su aire). La resolución es de prioridad, no de geometría:

| Si el corte lleva | El pie es de | La cifra va a |
|---|---|---|
| Subtítulo quemado (lo normal) | El subtítulo | `y ≈ 960`, centro del cuadro |
| Sin subtítulo (raro, sólo piezas mudas) | La cifra | — |

Nunca los dos. Apilarlos deja el subtítulo a `y ≈ 1250` y la cifra a `y ≈ 1100`, y
entonces el centro —donde iba la prueba— queda desierto.

## El vacío de arriba no es un error

En 16:9 un hueco es un defecto que el auditor persigue: `HUECOS 0` es objetivo. En
vertical **la franja de 0 a 200 px se deja vacía a propósito**, y eso son 200 de 1920 px,
el 10,4 % del cuadro, más el 27 % de abajo. El 37,5 % del lienzo es fondo por contrato.

Quien venga de montar 16:9 lo lee como cuadro flojo y lo rellena. El resultado es lo
único peor que un hueco: un elemento que el espectador ve tapado por un botón y del que
deduce, correctamente, que nadie miró el vídeo en un teléfono.

## Comprobación

La columna se audita con la misma aritmética que el resto del montaje, sin renderizar:

```python
ARRIBA, ABAJO = 200.0, 1400.0
REGISTROS = {"arriba": (200, 620), "centro": (620, 1180), "pie": (1180, 1400)}

for a, b, esc, r, caja in vidas:
    y0, y1 = caja[1], caja[3]
    if y0 < ARRIBA or y1 > ABAJO:
        print("  ! fuera de la columna útil:", r, y0, y1)
    reg = [k for k, (u, v) in REGISTROS.items() if y0 < v and y1 > u]
    if len(reg) > 1 and es_texto(r):
        print("  ! pieza de texto a caballo entre registros:", r, reg)
```

Una foto puede cruzar dos registros —es collage, no una rejilla—. **Una pieza de texto,
no**: un rótulo partido entre centro y pie se lee como dos cosas a medias.

## El gesto de entrada cambia con el registro

En 16:9 cada banda trae su gesto porque «un elemento de lado que entra por abajo se lee
como un error» (`243`). En vertical la lógica se invierte: **lo que entra de lado se lee
como error**, porque no hay lado del que venir. El margen horizontal es de ±140 px y una
entrada `izq` de 0,36 s recorre menos de lo que recorre el propio fundido.

```python
ENTRADAS_V = {"arriba": "fade", "centro": "abajo", "pie": "abajo", "cifra": "abajo"}
```

Todo entra por abajo o funde. Es la dirección de la columna, y también la dirección en la
que el espectador acaba de deslizar para llegar al vídeo: el gesto empata con el gesto.

## El registro de arriba manda en el primer segundo

Los tres registros no valen lo mismo en el tiempo. En vertical el espectador decide en el
primer segundo (`205`), y en ese primer segundo **sólo mira arriba**: la mitad inferior
del cuadro todavía está tapada por el pulgar que acaba de deslizar y por la animación de
entrada de la propia app.

De ahí una regla que no existe en 16:9: **el primer elemento del corte entra en el
registro de arriba, sea de la clase que sea.** En el episodio largo el primer elemento de
`ep01-lustig` es `casilla_hospital` a `y` 324–432 sobre 1080, es decir el tercio alto —
por casualidad, correcto. El segundo, `linea_00`, ocupa de 376 a 1104: en vertical eso es
la columna entera y no puede ser el segundo elemento de nada.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Componer a izquierda y derecha como en 16:9 | El margen real es de ±140 px: el elemento sale o se encoge |
| Centrar por el centro geométrico (`y = 960`) | Cae bajo el centro óptico de la zona útil (`y = 800`) |
| Meter cifra y subtítulo en el pie | El centro queda desierto y ninguno de los dos manda |
| Rellenar la franja de 0 a 200 px | Queda debajo de la barra de estado y del nombre de cuenta |
| Poner el retrato abajo y la cifra arriba | Se ve igual y deja de leerse como afirmación probada |
| Partir una pieza de texto entre dos registros | Dos medias frases; una foto puede, un texto no |

## Relacionado

`202` la zona segura real de cada red · `203` densidad en vertical · `206` subtítulos
siempre · `207` la cifra en vertical · `21` peso visual y jerarquía · `49` zona segura y
tamaños · `246` equilibrio del cuadro · editpro `147` formato vertical a fondo
