# 295 · Grano común: lo que de verdad hace la capa

**Qué resuelve:** todo lo que entra en el montaje pasa por la misma capa de ruido, y el
comentario de `revista.py` dice para qué está: «grano y un punto de desaturación: unifica
material de fuentes distintas». Es correcto y es incompleto. Medida hoy, esa capa **aporta
σ 0,617 de ruido y se lleva el 10,2 % del contraste de cada pieza**. O sea: es un velo que
además hace de dithering, no un grano. Saberlo cambia dónde se usa y qué se le pide.

Lo que aquí **no** se repite: las cuatro texturas por procedencia (`66`), la dispersión de
tono para validar el virado (`197`), la dosis de `alls` en ffmpeg y su óptimo técnico
(`editpro/440`), el polvo y el arañazo con sus dosis por megapíxel (`editpro/442`), ni las
huellas que delatan una superficie sintética (`editpro/447`). Aquí: **qué hace esta capa
concreta, horneada dentro del PNG, y qué paga por ello.**

---

## La capa, tal cual

```python
rnd = random.Random(semilla)
ruido = Image.new("L", (w, h))
ruido.putdata([rnd.randint(118, 138) for _ in range(w * h)])
capa = Image.merge("RGBA", (ruido, ruido, ruido, Image.new("L", (w, h), 26)))
img = Image.alpha_composite(img, capa)
```

Ruido uniforme en [118, 138] compuesto con **alfa 26 sobre 255**. Eso es una mezcla:

```
salida = original × (1 − 26/255) + ruido × (26/255)
```

Medido sobre una superficie sintética de σ 40, para poder aislar el efecto:

| Magnitud | Valor |
|---|---|
| Atenuación del original | **10,2 %** |
| σ del original | 39,93 |
| σ tras la capa | 35,86 (**−10,2 %**) |
| σ que aporta el ruido | **0,617 niveles** |
| Media | 127,98 → 127,98 (no la mueve) |

Tres consecuencias, y las tres importan:

1. **Como grano, es exactamente la dosis técnica correcta.** `editpro/440` demuestra que el
   trabajo de antibandeo está hecho en **σ ≈ 0,5** y que por encima solo se pagan bits y
   fidelidad. Esta capa da 0,617. No es una casualidad afortunada, pero es el sitio bueno.
2. **Como velo, es caro.** Un 10,2 % de contraste. Y `editpro/395` demuestra que un punto
   de contraste es un punto de acutancia: la capa también quita un 10 % de filo.
3. **No oscurece.** A diferencia de `noise=alls:allf=t+u` de ffmpeg, que baja la media
   (`editpro/440` §1b), esta capa la deja clavada porque el ruido está centrado en 128.

## Lo que le hace a la huella de textura

`editpro/447` mide dos cosas en cada pieza: el **suelo** (energía de alta frecuencia en el
5 % de bloques más planos) y la **razón p95/suelo**, y fija que el material de archivo real
vive entre **10 y 16**. Medido sobre cinco fuentes crudas de `ep01-lustig/archivo/`, antes
y después de pasar por `granular()`:

| Fuente | Suelo crudo | Suelo con capa | p95 crudo | p95 con capa | **Razón crudo** | **Razón con capa** |
|---|---|---|---|---|---|---|
| `le_wagon_de_l_armistice` | 1,72 | 3,45 | 29,3 | 26,4 | **17,0** | **7,7** |
| `concours_d_élégance` | 4,72 | 5,28 | 84,7 | 76,2 | 18,0 | 14,4 |
| `chaleur_à_paris` (1) | 6,93 | 6,92 | 64,8 | 58,1 | 9,4 | 8,4 |
| `chaleur_à_paris` (2) | 3,00 | 3,99 | 33,3 | 30,1 | 11,1 | 7,5 |
| `157series_scrapped` | 3,06 | 3,94 | 26,1 | 23,7 | 8,5 | 6,0 |

El mecanismo es el que `editpro/447` describe para el grano global, pero aquí ocurre
**dentro de cada PNG**: sube el suelo y baja el p95, y la razón cae entre un 10 % y un
55 %. Tres de las cinco salen del rango 10–16 del material de archivo.

Y sin embargo la decisión sigue siendo la correcta, por una razón que el módulo general no
puede saber: **este canal no busca que cada pieza pase por archivo suelta, sino que 33
piezas de 33 procedencias distintas parezcan la misma copia.** La razón baja porque la capa
las iguala, que es literalmente su trabajo. Lo que hay que vigilar es que no baje de **6**,
que es donde la pieza deja de leerse como fotografía y empieza a leerse como impresión.

## Grano por capa, nunca global

`66` ya prohíbe el `noise` sobre el `concat` final y `editpro/448` lo cuantifica. La
medida de `editpro/447` cierra el argumento con el número que más duele: aplicar
`noise=alls=5` (σ 0,99) a todo el cuadro deja un fotograma de collage en razón **8,18**,
cuando el material real vive en 10–16. Sería pagar dos veces por el mismo velo: una dentro
de cada PNG y otra encima de todo.

## La excepción de los documentos, y su factura

Los documentos llevan `grano=False` en la receta, y con razón: la capa se lleva un 10,2 %
de contraste, y el contraste de la tinta contra el papel es lo único que hace legible un
certificado (`197`). Pero tiene un precio medible:

| Pieza | Suelo | Razón |
|---|---|---|
| `carcel_estampa` (grabado, con capa) | 4,531 | 14,00 |
| `celda_catre` (foto, con capa) | 2,833 | 7,90 |
| `retrato_lustig` (foto, con capa) | 3,532 | 4,78 |
| **`certificado_defuncion` (`grano=False`)** | **0,000** | — |

**Suelo 0,000** es exactamente la huella que `editpro/447` manda rechazar: «no es
materia». Un escaneo real de un certificado de 1947 tendría ruido de sensor; este no tiene
nada porque la fuente venía ya limpia y no se le puso nada encima.

La salida no es devolverle el grano —eso le quitaría la legibilidad que se estaba
protegiendo— sino darle superficie con lo que no cuesta contraste: **polvo y arañazo**
(`editpro/442`), que son rasgos escasos y localizados, conservan el 82–89 % de su contraste
tras CRF 24 y no tocan ni un píxel de la tinta. Dosis de trabajo: 40 motas por megapíxel y
3 rayas, congeladas con la pieza porque la suciedad está en el papel y el papel no se mueve.

## Una semilla por pieza, no una por lote

`25` ya advierte de por qué `hash(alias)` no sirve como semilla y cuál es la alternativa
estable. Lo que aquí se añade es el reparto: en `recortar_lustig.py` cada pieza lleva su
semilla escrita a mano. Comprobado hoy: **70 semillas distintas y las 70 primas**, de 101 a
521. Que sean primas no hace el ruido mejor; hace trivial no repetirlas por descuido, que
es lo que se buscaba.

Importa porque la capa es la misma para todos: mismo rango, mismo alfa, misma media. Si
además compartiesen semilla, treinta recortes llevarían **el mismo patrón de ruido en la
misma posición**, y al superponerse dos en el cuadro el ojo lo ve como una trama fija.
Grano común no es grano idéntico.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Llamar «grano» a la capa | Es un velo del 10,2 % que además dithers; se le pide lo que no da |
| Subir el alfa de la capa para «que se note» | Cada punto de alfa es un punto de contraste y de acutancia |
| Aplicar `noise` global además de la capa | Razón 15,15 → 8,18: fuera del rango del archivo real |
| Devolverle el grano a un documento | Se pierde el contraste de tinta, que era su única función |
| Dejar un documento con suelo 0,000 | La huella de superficie sintética (`editpro/447`) |
| Una sola semilla para todo el lote | Treinta recortes con el mismo patrón: se lee como trama (`25`) |
| Validar el envejecido por saturación | No es monótona: aprueba al revés (`197`) |
| Encadenar dos pasadas de capa | El contraste cae un 19,4 % y el ruido solo sube en cuadratura |

## Relacionado

`66` grano y textura (las cuatro texturas por procedencia) · `197` envejecer para que
empate · `25` el borde de papel · `52` texturas de fondo · `294` la sombra que convence ·
`297` documentos como imagen · `editpro/440` grano: por qué y cuánto ·
`editpro/442` papel, polvo y arañazo · `editpro/447` la textura que delata a la IA ·
`editpro/448` textura por capa, no global · `editpro/449` medir si la textura suma
