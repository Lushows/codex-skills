# 168 · Reproducir antes de afirmar

**Qué resuelve:** la regla que ahorra más horas de todo el bloque. **No se reporta un
fallo sin haberlo reproducido, y no se da por bueno un arreglo sin volver a medir.**
Diagnosticar de oído o de vista ha mandado este proyecto a cambiar de herramienta tres
veces cuando el problema era el método.

---

## Las dos mitades de la regla

| Mitad | Qué exige | Qué evita |
|---|---|---|
| **Reproducir** | Antes de decir *«falla X»*: el comando exacto, la salida pegada y el segundo o el fotograma donde ocurre | Perseguir un fallo que no existe, o arreglar el sitio equivocado |
| **Volver a medir** | Después de tocar nada: la MISMA medición de antes, con el mismo umbral, y las dos cifras una al lado de la otra | Dar por resuelto lo que sólo se movió de sitio |

Un arreglo sin medición posterior no es un arreglo: es una hipótesis con el código ya
cambiado, que es la peor combinación posible.

## El coste de diagnosticar de oído

**Caso 1 — «la voz suena cortada».** El diagnóstico fue *el modelo de voz es malo* y se
probaron otros. El problema era el método: la locución se troceaba en frases y se pegaba
con silencios, así que cada trozo arrancaba su entonación desde cero. Se vio al medir:
el mismo párrafo dura **13,99 s troceado y 9,81 s en una sola pasada**. Ningún modelo
de voz habría arreglado eso.
> **Lección:** *«suena mal»* no es un diagnóstico, es un síntoma. El diagnóstico es un
> número y un sitio.

**Caso 2 — los clics del audio.** Se culpó a los efectos de sonido y se bajaron sus
ganancias. Los saltos seguían. Al listar **dónde** caían, todos coincidían con las pausas
del guion: era el colchón, que se apagaba en los silencios. Mirar el segundo exacto
resolvió en cinco minutos lo que dos sesiones de cambiar ganancias no tocó.
> **Lección:** antes de tocar una palanca, **listar los sitios** donde ocurre el fallo.
> Si se reparten uniformemente es una palanca global; si se agrupan, es un patrón.

**Caso 3 — 42 saltos que no existían.** La primera auditoría de audio contó 42 saltos de
nivel en un episodio ya terminado. Eran sílabas: se estaba midiendo sobre el momentáneo
(400 ms), que sube y baja con cada golpe de voz. Medido sobre el corto plazo (3 s), que
es donde vive la estructura: **0 saltos**. La herramienta daba un número correcto de una
pregunta equivocada (`142`).
> **Lección:** una medición que grita también hay que reproducirla. Antes de creerse un
> hallazgo, mirar **tres casos concretos a mano**.

**Caso 4 — el fondo apagado.** *«Se ve marrón»* → se subió la luz. Medido: `YMAX` pasó
de 78 a 242 y `SATAVG` se quedó en 5,4; seguía marrón. Lo que quitaba el marrón era la
**saturación del tono base**, que lo llevó a 12,0. Dos palancas distintas para dos
síntomas que se parecen.
> **Lección:** si el arreglo no mueve la medida, el arreglo no es el arreglo, aunque el
> síntoma parezca haber mejorado.

## El procedimiento

```
1. REPRODUCIR   comando exacto + salida + sitio (segundo, fotograma, archivo:línea)
2. AISLAR       ¿ocurre con una sola escena? ¿con un solo elemento? ¿sin audio?
3. MEDIR ANTES  la cifra de partida, anotada. Sin esto no hay "después"
4. UNA CAUSA    formularla en una frase que se pueda desmentir
5. UN CAMBIO    uno solo. Dos cambios a la vez y no se sabe cuál sirvió
6. MEDIR DESPUÉS  misma medición, mismo umbral, las dos cifras juntas
7. GRILLA       si el cambio toca imagen, grilla nueva y guardada con versión (`160`)
```

**El paso 5 es el que más se salta** y el que más cuesta. Cuando se cambian tres cosas y
el episodio mejora, no se ha aprendido nada: la próxima vez se vuelven a cambiar las
tres, incluidas las dos que no servían.

## Aislar: el material ya está

Aislar es barato en este proyecto porque cada escena es un comando de ffmpeg
independiente y queda en su archivo:

```bash
ls salida/            # e00_muerte.mp4  e01_oficio.mp4  e02_nombre.mp4 ...
```

Un defecto que aparece en `e03_torre.mp4` y no en el resto es un problema del guion
visual de esa escena. Uno que aparece en las cinco es del motor o del fondo. Esa
pregunta se responde en diez segundos y orienta todo lo demás.

Para audio, la mitad equivalente:

```bash
# el mismo tramo, solo voz, sin colchon ni efectos
ffmpeg -y -v error -ss 34 -t 16 -i audio/locucion.mp3 -af ebur128 -f null - 2>&1 | tail -20
```

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Reportar «se ve raro» sin fotograma ni segundo | Nadie puede reproducirlo; se arregla a ciegas |
| Cambiar de herramienta ante un síntoma | Se cambió de modelo de voz por un fallo de método |
| Tocar tres palancas a la vez | Funciona y no se sabe por qué; se repite el ritual entero |
| Fiarse de que un script «corrió» | Dos iteraciones fallaron en silencio por un f-string roto. **Leer la salida** |
| Medir el después con otro umbral | Es la forma elegante de aprobarse a uno mismo |
| Dar por cerrado sin grilla nueva | El arreglo de imagen se verifica en el fotograma, no en la tabla |
| Creerse un hallazgo con 200 ocurrencias sin mirar tres | Casi siempre es la medida la que está mal (`143`) |

## Relacionado

`160` la grilla de fotogramas · `167` verificación cruzada · `169` el informe de
auditoría · `86` medir el audio · `140` medir antes de renderizar · `159` cómo se caza
un fallo que no avisa
