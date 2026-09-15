# 408 — Lo que cuesta cada capa

**Qué resuelve:** «el render va lento» se arregla casi siempre quitando elementos, que es lo único que se
ve en el guion visual. Casi siempre es la decisión equivocada. Este módulo pone precio a cada pieza del
apilado con medidas hechas hoy, y el reparto no es el que se supone: **el fondo se lleva más que las
cincuenta y nueve capas juntas, y los adornos de cada capa son gratis.**

> **Frontera.** `canales_lushows/248` explica la función `escalado()` del motor y el fallo de caché por
> basename. **Aquí está el precio**, medido: cuánto se ahorra, cuánta calidad cuesta y cómo se reparte el
> presupuesto de un episodio. `422` mide el coste de un efecto en render y en atención.

Todas las cifras son **tiempo de CPU** (`ffmpeg -benchmark`, campo `utime`), que es lo único estable en
una máquina cargada; el reloj de pared va entre 1,3× y 1,9× por debajo según el paralelismo.

---

## 1. Una capa cuesta lo mismo esté donde esté

Escena de 3 s (75 fotogramas) a 1920×1080, fondo prerreducido, capas de 400–600 px:

| capas | CPU con PNG crudo | CPU con PNG prerreducido | coste marginal crudo | marginal prerreducido |
|---|---|---|---|---|
| 0 | 21,30 s | 21,41 s | — | — |
| 1 | 35,27 s | 24,66 s | 13,97 s | 3,25 s |
| 2 | 44,53 s | 25,58 s | 11,62 s | 2,09 s |
| 4 | 73,28 s | 31,44 s | 13,00 s | 2,51 s |
| 8 | 131,44 s | 43,33 s | 13,77 s | 2,74 s |
| 14 | 216,73 s | 60,36 s | 13,96 s | 2,78 s |

Dos hechos: **el coste es lineal** —la capa número 14 cuesta lo mismo que la primera, así que apilar no se
degrada— y **prerreducir el PNG divide ese coste por cinco** (13,9 s → 2,8 s por capa).

---

## 2. Lo que cuesta no es la capa: es su área

Ocho capas, mismo montaje, variando solo el ancho en pantalla:

| ancho | alto aprox. | CPU 8 capas | CPU por capa |
|---|---|---|---|
| 200 px | 144 | 24,69 s | 0,39 s |
| 400 px | 288 | 36,20 s | 1,83 s |
| 800 px | 576 | 73,30 s | 6,47 s |
| 1600 px | 1152 | 192,83 s | 21,41 s |

Doblar el ancho cuadruplica el área y multiplica el coste por **3,3–4,7**. Es decir: **el precio se paga en
píxeles compuestos, no en número de elementos.** Bajar un principal de 800 a 620 px ahorra más que borrar
tres acentos de 200 px.

---

## 3. Los adornos de una capa son gratis

Ocho capas prerreducidas, 75 fotogramas, añadiendo un filtro cada vez:

| cadena de la capa | CPU |
|---|---|
| `scale` + `overlay` (mínimo) | 41,23 s |
| + `colorchannelmixer` (opacidad) | 43,19 s |
| + dos `fade` con `alpha=1` | 40,20 s |
| + `rotate` 2,4° con `c=none` | 46,50 s |
| + `gblur sigma=0,5` | 44,47 s |

Todo dentro del ruido de medida —el caso con dos `fade` sale *por debajo* del mínimo, que es imposible—.
**Opacidad, fundidos, giro y el medio píxel de desenfoque de `204` §3.2 no cuestan nada** una vez el PNG
entra al tamaño correcto. Quitar el giro para acelerar el render es tiempo perdido.

Lo mismo vale para el destello, medido sobre el fondo: `eq` con `eval=frame` sobre todo el cuadro añade
**0,53 s sobre 20,61** (`405` §2).

---

## 4. Una capa apagada cuesta igual que una encendida

Ocho capas de 600 px, 75 fotogramas:

| montaje | CPU |
|---|---|
| 8 capas visibles todo el rato | 49,89 s |
| 8 capas, cada una visible 1/8 del tiempo | 49,53 s |

`enable` solo decide si se mezcla el resultado; la cadena entera se ejecuta igual en cada fotograma. **Un
contador de diez posiciones cuesta diez capas** aunque cada cifra viva dos décimas (`404` §4). La salida,
si aprieta, es pre-renderizar la secuencia como un único elemento animado.

---

## 5. El fondo: el ahorro grande

El fondo entraba con `scale=4320:-2` —que además no hacía nada, porque los fondos ya vienen a 4320— y se
reescalaba **en cada fotograma**. Prerreducido una vez a 2688 (`W × 1,4`) y cacheado, sobre la escena real
`oficio` de 6,73 s / 168 fotogramas:

| cadena | CPU (mediana de 4) | reloj |
|---|---|---|
| `scale=4320:-2` por fotograma | 71,77 s | 38,4 s |
| PNG prerreducido a 2688, sin `scale` | **44,83 s** | **23,2 s** |
| **ahorro** | **37,5 %** | **≈ 39 %** |

Y la calidad no sufre: comparando las dos salidas, **PSNR 43,69 dB y SSIM 0,969** (anotado en el repo:
43,3 dB y 0,972; reproducido). Bajar en dos pasos —LANCZOS a 2688 y luego el `zoompan`— incluso suaviza
mejor que hacerlo de golpe.

---

## 6. El presupuesto de un episodio, repartido

`ep01-lustig`: 1.586 fotogramas, 59 elementos vivos, 3.596 fotogramas-capa, ancho medio declarado 802 px.
Aplicando los costes de arriba:

| partida | CPU | reparto |
|---|---|---|
| fondo (`zoompan` + codificar) | 435,8 s | **55 %** |
| las 59 capas | 352,8 s | 45 % |
| **total** | **13,1 min CPU** | |

El render completo anotado en el repo son **9 min 42 s de reloj** para 63,45 s de vídeo — unos **9,2 s de
render por segundo de vídeo**. Con el paralelismo medido (~1,9×), 13,1 min de CPU caen exactamente en ese
orden. *(No he vuelto a lanzar el render entero: otra sesión estaba escribiendo en `salida/` mientras
medía.)*

**La regla de decisión:** si el render aprieta, en este orden — ① prerreducir fondo y elementos, ② bajar
el ancho de los principales, ③ recortar el número de capas. Al revés se trabaja mucho y se ahorra poco.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Quitar elementos para acelerar el render | El 55 % del coste es el fondo |
| Dejar un `scale` en la cadena que ya no hace nada | Reescalado completo en cada fotograma, gratis para nadie |
| Medir con el reloj de pared en una máquina cargada | 13 % o 34 % de ahorro según la tirada; mide CPU |
| Quitar giros, fundidos u opacidad para ganar tiempo | Están dentro del ruido de medida |
| Acortar la vida de las capas para ahorrar | Una capa apagada cuesta lo mismo |
| Prerreducir al tamaño exacto de pantalla | El giro y la deriva piden 1,4× de margen o el borde sale blando |
| Suponer que apilar se degrada | Es lineal: la capa 14 cuesta como la primera |

## Relacionado

`400` el orden de render es narrativo · `402` el z dinámico · `404` acumular o sustituir ·
`405` el fondo no es una capa más · `409` depurar un apilado · `108` análisis y medición con ffmpeg ·
`132` render reproducible · `134` procesar por lotes · `422` coste en render y en atención ·
`canales_lushows/248` pre-escalado y caché · `canales_lushows/140` medir antes de renderizar
