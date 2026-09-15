# 144 · Presencia no es superficie

**Qué resuelve:** un episodio con cero huecos, simultaneidad en meta y eventos de sobra
que se ve vacío igual. *"Hay un elemento"* no es *"el cuadro está lleno"*.

---

## El caso

Episodio 01, medido antes de renderizar:

```
  EVENTOS/min             47.9   (objetivo >= 44)     OK
  simultaneidad media     2.04   (objetivo >= 2,00)   OK
  HUECOS                     0   (objetivo 0)         OK
```

Tres de tres. Se renderizó, se miró la rejilla de fotogramas y **los recortes flotaban
perdidos sobre el fondo**. El número que lo explicaba no estaba en el informe:

> **El 30 % del episodio tenía menos del 14 % del lienzo cubierto.**

Las cinco métricas originales miden **presencia**: cuántas cosas hay vivas y cuándo. Un
retrato de 260 px de ancho y un titular de 1500 px cuentan igual: uno. Pero el primero
ocupa el 2 % del lienzo y el segundo el 21 %.

## Qué faltaba medir

La **cobertura**: superficie del lienzo ocupada en cada instante, en tanto por uno. Se
calcula sin renderizar, porque el ancho está en la tabla y la proporción sale del PNG.

```python
def area(recurso, ancho):
    """Superficie del elemento en el lienzo de 1920x1080, en tanto por uno."""
    from PIL import Image
    w, h = Image.open(ruta(recurso)).size
    alto = ancho * h / w
    return (ancho * alto) / (1920.0 * 1080.0)
```

Y se muestrea a 20 Hz, igual que la simultaneidad:

```python
paso = 0.05
n = int(T / paso)
cob = []
for i in range(n):
    t = i * paso
    cob.append(sum(ar for a, b, _, _, ar, _ in vidas if a <= t < b))
media_cob = sum(cob) / len(cob)
pobres = sum(1 for c in cob if c < 0.14) * paso     # segundos de cuadro casi vacío
```

| Métrica | Objetivo |
|---|---|
| cobertura media | 22–38 % |
| cuadro casi vacío (< 14 % cubierto) | ningún tramo de más de 0,8 s |

Salida real de `ep01-lustig` con la medida ya dentro:

```
  COBERTURA media        39.5 %  (objetivo 22 - 38 %)
  cuadro casi vacio       3.15 s = 5%  (menos del 14% cubierto)
```

Cinco por ciento del episodio, no treinta. Y la media se pasa de rango por arriba, que
es un problema distinto (saturación) y también se ve.

## Por qué presencia y superficie no correlacionan

| Situación | Presencia | Superficie | Cómo se ve |
|---|---|---|---|
| Dos rótulos pequeños en esquinas opuestas | 2 elementos, sin hueco | 4 % | Vacío |
| Un documento a media página | 1 elemento | 26 % | Lleno |
| Tres recortes apilados en el mismo sitio | 3 elementos | 18 % | Desordenado y vacío |
| Un titular ancho solo | 1 elemento | 21 % | Plano de texto (`148`) |

Las dos primeras filas explican por qué un montaje puede ganar todas las métricas de
ritmo y perder el cuadro.

## El texto no llena

Los PNG de texto del canal son **anchos y bajos**: proporción alto/ancho entre 0,20 y
0,29. Un titular a 1500 px de ancho ocupa como mucho el **23 % del lienzo**, y eso
siendo grande. Consecuencia práctica:

- Un tramo sostenido **sólo** por texto va a salir flojo de cobertura siempre.
- La respuesta no es agrandar el titular (rompe la zona segura, `49`), sino **poner
  imagen debajo**: un recorte, una lámina de fondo, un documento.

## Cómo se sube la cobertura sin saturar

Por orden de lo que menos rompe:

1. **Ampliar el elemento principal** de la escena. Un retrato a 420 px en vez de 260
   pasa del 2,6 % al 6,8 % sin añadir nada.
2. **Añadir una lámina de fondo** (documento, mapa, textura de página) por debajo de
   todo, con `w` grande y opacidad baja. Es el ascensor más eficaz del suelo.
3. **Encadenar** en vez de sustituir: que el que se va solape 0,4 s con el que entra
   (`14`).
4. **Repartir**, no apilar: si todo cae en el mismo tercio, la cobertura sube pero el
   reparto 3×3 empeora (`148`).

Cuidado con pasarse: por encima del 38 % de media el fondo desaparece y el collage se
lee como ruido. El auditor avisa aparte cuando hay más de 4 elementos vivos a la vez.

## La secuencia correcta de lectura

Presencia primero, superficie después. No sirve subir cobertura sobre un montaje con
huecos o con anclas huérfanas: se estaría rellenando un episodio que no es el que se va
a renderizar (`140`).

```
anclas huérfanas → huecos → simultaneidad → COBERTURA → suelo de cobertura (145) → reparto
```

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dar por bueno "0 huecos" | 30 % del episodio con el cuadro casi vacío y aprobado |
| Contar elementos en vez de superficie | Un rótulo de esquina vale lo mismo que un documento |
| Llenar con texto | Tope del 23 %: el tramo sigue flojo y encima se lee como plano de texto |
| Subir cobertura apilando en el mismo sitio | Sube el número, empeora la composición (`20`, `21`) |
| Medir cobertura antes de arreglar los huecos | Se rellena un montaje que va a cambiar entero |

## Relacionado

`12` capas simultáneas · `17` medir el montaje · `21` peso visual y jerarquía ·
`145` la media esconde el suelo · `146` medir lo que se ve · `148` el cuadro de mando
