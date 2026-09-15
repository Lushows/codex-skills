# 40 · El texto como canal principal

**Qué resuelve:** el episodio se escribió para el oído y se montó para el ojo, pero la
mayoría de la gente lo ve **sin sonido**. Si la información sólo vive en la locución,
para ese espectador el vídeo no dice nada: ve papel bonito moviéndose. Hoy el canal
tiene texto en una fracción mínima del metraje y eso es el agujero.

---

## La premisa

**El vídeo tiene que entenderse mudo.** No "subtitulado": *entendido*. Son cosas
distintas — un subtítulo obliga a leer un párrafo; el texto en pantalla entrega el
dato de un vistazo, mientras la imagen sigue contando.

El audio y el texto no repiten lo mismo: se reparten el trabajo.

| Canal | De qué se encarga |
|---|---|
| **Voz** | El hilo, la causalidad, el tono, la ironía, el "y entonces…" |
| **Texto en pantalla** | El dato duro: cifras, nombres, fechas, lugares, qué es ese objeto |
| **Imagen** | La prueba y la atmósfera |

Si quitas cualquiera de los tres y el episodio sigue teniendo sentido, los otros dos
están haciendo trabajo de más.

---

## Lo que NO puede vivir sólo en el audio

Cinco clases de información. Si aparecen en el guion y no aparecen en pantalla, es un
defecto, no una decisión de estilo:

| Clase | Por qué no sobrevive al oído | Módulo |
|---|---|---|
| **Cifras** | "Ciento veintiséis toneladas" se oye como un ruido largo. `126 t` se lee de golpe | `44` |
| **Nombres propios** | Un apellido que no se ha visto escrito no se retiene ni se busca después | `43` |
| **Fechas y lugares** | Anclan la historia en el mundo real; oídos se confunden entre sí | `43` |
| **Identificación de objetos** | Una tuneladora, un plano de planta, un acta: sin rótulo es ruido decorativo | `43` |
| **Citas textuales** | El valor de una cita es que es *textual*. Sin verla, es la palabra del narrador | `48` |

**Lo que sí puede vivir sólo en el audio:** el enlace narrativo, el juicio, la
pregunta retórica, la transición. Todo lo que no es dato.

---

## La prueba del mudo

Es el control de calidad del bloque 4. Se hace **antes** de la mezcla de audio, sobre
`_mudo.mp4`, que ya está sin voz por construcción.

```bash
# 1 · grilla de fotogramas cada 2 s: se ve el episodio entero de un vistazo
ffmpeg -i salida/_mudo.mp4 -vf "fps=1/2,scale=440:-1,tile=6x4" -frames:v 1 grilla.png

# 2 · cuánto metraje tiene texto vivo: se cuentan los fotogramas donde hay
#     píxeles del color de texto en la mitad inferior del cuadro
ffmpeg -i salida/_mudo.mp4 -vf "crop=iw:ih/2:0:ih/2,
  colorkey=0xEDE6D6:0.22:0.0,alphaextract,blackframe=amount=99:threshold=32" \
  -f null - 2>&1 | grep -c blackframe
```

Y luego, a mano, las tres preguntas. Se ve la grilla **sin haber leído el guion**:

1. ¿Puedo decir de quién trata y cuánto dinero hay en juego?
2. ¿Hay algún objeto en pantalla que no sepa identificar?
3. ¿Sé cómo termina?

Si la respuesta a 1 o 3 es no, o la 2 es sí, faltan rótulos.

---

## Los objetivos del canal

| Métrica | Objetivo | Cómo se mide |
|---|---|---|
| Metraje con algún texto legible | **≥ 60%** | grilla: contar cuadros con texto |
| Cifras del guion con gemelo en pantalla | **100%** | comparar `guion.txt` con `guion_visual.py` |
| Nombres propios escritos al menos una vez | **100%** | ídem |
| Primeros 5 s con texto | **siempre** | el gancho mudo decide si se quedan |
| Bloques seguidos sin texto | **ninguno > 6 s** | detector de huecos (`11`) |

**El gancho es el caso extremo.** Los primeros 3-5 segundos se reproducen mudos por
defecto en casi todas las plataformas. Si el gancho es una frase hablada sobre una
foto, ese gancho no existe. El gancho lleva **una línea de titular** en pantalla,
siempre.

---

## Dónde se declara

El texto no se improvisa en el montaje: se marca en el guion y se declara en la tabla
de eventos, igual que cualquier recorte.

```
guion.txt        → se subrayan las palabras que exigen gemelo en pantalla
                   (cifras, nombres, fechas, objetos, citas)
fx.py / laminas  → cada una se convierte en un PNG con transparencia
guion_visual.py  → entra anclada a su palabra, con su offset negativo
```

El texto entra **0,15-0,25 s ANTES** de la palabra, no después — más adelanto que un
recorte, porque leer tarda más que reconocer una foto (`39`, `44`).

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Poner el guion entero como subtítulo y darlo por resuelto | Compite con la imagen y no destaca ningún dato; se lee todo o nada |
| Texto que repite literalmente lo que dice la voz en ese instante | Duplica en vez de repartir: se pierde una capa de información |
| Rotular sólo lo que es bonito de rotular | Los objetos raros son justo los que necesitan rótulo |
| Meter el texto después de montar la imagen | No queda sitio: hay que reservarle hueco al componer (`28`) |
| Confiar en que "se entiende por contexto" | El espectador mudo no tiene contexto |

## Relacionado

`41` máquina de escribir · `42` tipografía del canal · `43` rótulos y etiquetas ·
`44` la cifra en pantalla · `45` subtítulos y destacados · `49` zona segura
