# 165 · La prueba del mudo

**Qué resuelve:** comprobar que el episodio **se entiende sin sonido**. Es gratis —el
pipeline ya deja `salida/_mudo.mp4` antes de que `acabar.py` le ponga la voz— y es la
prueba que más defectos de guion visual encuentra por minuto invertido.

---

## Por qué no es un capricho

Tres razones, y ninguna es estética:

1. **El feed arranca mudo.** En TikTok, Instagram, Facebook y el feed de YouTube el
   vídeo empieza sin sonido. Los primeros 3 segundos —el gancho— se juegan siempre en
   silencio.
2. **Cinco de las seis pistas no son la que se montó.** El canal publica el vídeo con
   locución en inglés, alemán, japonés, francés, español y portugués. **La imagen es la
   misma para las seis.** Lo que sólo existe en la voz española no existe en las otras
   cinco, y el doblaje no traduce los PNG de texto.
3. **El montaje se escribe mirando la tabla de eventos**, donde cada elemento está
   colgado de su palabra y por tanto *parece* explicado. En mudo se ve que el elemento
   está, y que no dice nada.

## Cómo se hace

```bash
# el mudo ya existe: es la salida de motor.py, antes de acabar.py
ls -la salida/_mudo.mp4

# si hace falta reconstruirlo desde el episodio terminado, sin recodificar video
ffmpeg -y -v error -i salida/episodio01.mp4 -an -c:v copy salida/_mudo.mp4
```

Se ve **entero, de una sentada, sin pausar y sin la grilla delante**. La grilla (`160`)
sirve para cazar defectos de fotograma; el mudo sirve para juzgar si la historia llega.
Son dos pasadas distintas y mezclarlas estropea las dos.

## Las tres preguntas

Se responden **al terminar**, de memoria, sin volver atrás. Si hay que rebobinar para
contestar, la respuesta es no.

| # | Pregunta | Qué falla si la respuesta es no |
|---|---|---|
| **1** | **¿De quién es la historia?** ¿Apareció una cara y un nombre escrito, y volvió lo suficiente para pegarse? | El héroe no tiene ficha, o sale una vez y no vuelve. Un retrato sin rótulo es un desconocido |
| **2** | **¿Qué construyó y cómo cayó?** ¿Se ve el arco —lo que levantó, la raya que cruzó, el final— o sólo una sucesión de imágenes de época? | El guion visual ilustra palabras sueltas en vez de contar el arco. Es lo que produce el efecto "banco de imágenes" |
| **3** | **¿Las cifras están escritas?** Las tres o cuatro que sostienen el episodio, ¿aparecieron en pantalla con su unidad y su año? | Las cifras viven sólo en la locución. En japonés no existen |

Un cuarto criterio, más blando pero útil: **¿en qué segundo me habría ido?** Ese punto
marca dónde el montaje se queda sin gesto nuevo, y casi siempre coincide con un tramo
de cobertura baja (`17`) o con tres planos seguidos empujando en la misma dirección.

## Lo que NO puede vivir sólo en el audio

| Información | Cómo entra en imagen |
|---|---|
| Nombre del protagonista | Ficha o rótulo, y vuelve al menos una vez |
| Cualquier cifra de dinero | Cifra en pantalla con moneda y año (`44`) |
| Fechas y orden de los hechos | La línea de tiempo que se va construyendo (`linea_00`, `linea_02`…) |
| Lugar, si cambia | Rótulo de sitio la primera vez que aparece |
| **Qué está probado y qué es relato** | Las marcas de columna `m_consta` / `m_cuenta`. Si sólo lo dice la voz, en las otras cinco pistas el episodio afirma cosas que no puede probar |
| El giro | Un gesto visual propio: un destello, un corte a negro, un documento que se revela |

⚠️ **Un objeto sin rótulo es ruido.** Una tuneladora, un plano técnico o una máquina de
imprimir sellos no se identifican solos. En mudo, un objeto sin explicar no aporta:
ocupa superficie y no comunica nada.

## Lo que la prueba del mudo NO detecta

Se hace **antes** que la mezcla, y por eso no dice nada de sincronía. Un elemento que
entra 0,3 s tarde respecto a su palabra se ve perfectamente normal en mudo y es un
defecto real (`39`). Para eso hace falta el episodio con sonido, y además medido.

Tampoco vale para juzgar el ritmo tal cual: sin voz, los planos parecen más largos de lo
que son. El ritmo se mide en `17`; aquí sólo se juzga **comprensión**.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Hacer la prueba con el sonido bajito | El cerebro rellena con lo que oye; la prueba no vale |
| Verlo pausando para "comprobar una cosa" | Se pierde el juicio de conjunto, que es lo único que aporta |
| Hacerla sólo sobre el gancho | El 60% de los huecos de sentido están en el tramo medio |
| Darla por buena porque "se entiende, yo sé la historia" | El que montó el episodio no puede responder la pregunta 2; conviene otro par de ojos, o dejar pasar un día |
| Arreglar un fallo de mudo añadiendo más texto | El texto no llena el cuadro y satura: lo que falta suele ser un rótulo corto, no un párrafo (`46`) |
| Suponer que las pistas de idiomas lo arreglan | El doblaje traduce la voz, no los PNG de texto |

## Relacionado

`160` la grilla de fotogramas · `166` la prueba del pulgar · `40` el texto como canal
principal · `43` rótulos y etiquetas · `44` la cifra en pantalla · `93` estructura de
episodio
